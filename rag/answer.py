"""Grounded answer generation over retrieved chunks."""
import re

from rag.confidence import combine, retrieval_signal
from rag.config import LLM_MODEL, SCORE_FLOOR, llm
from rag.router import route
from rag.store import search

SYSTEM = """You answer questions for floor supervisors at a plastic injection molding plant, \
using ONLY the documentation excerpts provided.

Each excerpt is labelled with a citation and a relevance score from 0 to 1, which is the \
semantic similarity between the question and that excerpt.

Rules:
- Use only the excerpts. Never add procedures, numbers, or steps from general knowledge.
- Cite the source inline after each factual claim, exactly as the excerpt is labelled: \
[MNT-007 §3]. Never cite a document that does not appear in the excerpts.
- Preserve exact figures, tolerances, and units as written.
- Be direct. A supervisor is reading this on the floor: lead with the answer, then the \
conditions attached to it.
- When a procedure has a safety precondition in the excerpts, state it before the steps.
- If the excerpts disagree, say so rather than silently picking one.

Using the relevance scores:
- Scores are a retrieval signal, not a truth signal. A high score does not make an excerpt \
correct, and the highest-scoring excerpt is not always the one that answers the question. \
Read them all and use whichever actually contains the answer.
- If the top score is below 0.62, treat the match as weak: say plainly that the \
documentation may not cover this, give whatever partial information exists, and name the \
document most likely to hold the full answer.
- Never mention the numeric scores in your answer. They inform how much you hedge, \
not what you say."""

SAFETY_NOTE = (
    "This answer draws on safety documentation. Safety requirements are "
    "preconditions, not suggestions — do not begin the task until they are met."
)

CITE_RE = re.compile(r"\[([A-Z]{2,3}-\d{3})(?:\s*§\s*([\d.]+))?\]")


def build_context(chunks):
    parts = []
    for c in chunks:
        parts.append(
            f"[{c['citation']}] (relevance {c['score']:.3f}) "
            f"{c['title']} > §{c['section_num']}. {c['section_title']}\n{c['text']}"
        )
    return "\n\n---\n\n".join(parts)


def check_citations(answer_text, chunks):
    """Validate that every citation in the answer was actually in context.

    Catches the failure mode where the model cites a plausible-looking document
    it saw referenced inside another excerpt but never actually received.
    """
    in_context = {c["citation"] for c in chunks}
    in_context_docs = {c["doc_id"] for c in chunks}

    cited, unsupported = [], []
    for m in CITE_RE.finditer(answer_text):
        doc, sec = m.group(1), m.group(2)
        full = f"{doc} §{sec}" if sec else doc
        cited.append(full)
        if full not in in_context and doc not in in_context_docs:
            unsupported.append(full)

    return {"cited": sorted(set(cited)),
            "unsupported": sorted(set(unsupported)),
            "all_supported": not unsupported}


def ask(question: str, k=None, max_chunks=None) -> dict:
    r = route(question)

    if r["out_of_scope"]:
        return {
            "question": question, "route": r, "chunks": [], "sources": [],
            "answer": ("That falls outside the Plant 4 documentation set, which covers "
                       "safety procedures, maintenance manuals, and quality standards. "
                       "For this, contact HR or your supervisor."),
            "safety_flagged": False, "safety_note": None,
            "retrieval": retrieval_signal([]),
            "confidence": combine(r["confidence"], retrieval_signal([])),
            "citations": {"cited": [], "unsupported": [], "all_supported": True},
        }

    kw = {}
    if k is not None:
        kw["k"] = k
    if max_chunks is not None:
        kw["max_chunks"] = max_chunks
    chunks = search(question, categories=r["categories"], **kw)

    retrieval = retrieval_signal(chunks)
    confidence = combine(r["confidence"], retrieval)

    if not chunks:
        return {"question": question, "route": r, "chunks": [], "sources": [],
                "answer": "No relevant documentation found for that question.",
                "safety_flagged": False, "safety_note": None,
                "retrieval": retrieval, "confidence": confidence,
                "citations": {"cited": [], "unsupported": [], "all_supported": True}}

    safety_flagged = any(c["category"] == "safety" for c in chunks)

    user = (f"Documentation excerpts:\n\n{build_context(chunks)}\n\n"
            f"Question: {question}\n\n"
            f"Top relevance score: {retrieval['top']:.3f} "
            f"(weak-match threshold is {SCORE_FLOOR}).")

    try:
        resp = llm().chat.completions.create(
            model=LLM_MODEL,
            messages=[{"role": "system", "content": SYSTEM},
                      {"role": "user", "content": user}],
            temperature=0,
            max_tokens=800,
        )
        answer = resp.choices[0].message.content.strip()
    except Exception as e:
        answer = (f"Could not generate an answer ({type(e).__name__}). "
                  f"The relevant documents are: "
                  f"{', '.join(sorted({c['citation'] for c in chunks}))}")

    return {
        "question": question,
        "route": r,
        "chunks": chunks,
        "answer": answer,
        "safety_flagged": safety_flagged,
        "safety_note": SAFETY_NOTE if safety_flagged else None,
        "sources": sorted({c["citation"] for c in chunks}),
        "retrieval": retrieval,
        "confidence": confidence,
        "citations": check_citations(answer, chunks),
    }
