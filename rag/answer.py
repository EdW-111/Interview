"""Grounded answer generation over retrieved chunks."""
from rag.config import LLM_MODEL, llm
from rag.router import route
from rag.store import search

SYSTEM = """You answer questions for floor supervisors at a plastic injection molding plant, \
using ONLY the documentation excerpts provided.

Rules:
- Use only the excerpts. Never add procedures, numbers, or steps from general knowledge.
- Cite the source inline after each factual claim, in square brackets, exactly as the excerpt \
is labelled: [MNT-007 §3].
- If the excerpts do not contain the answer, say so plainly and name the document that would \
most likely hold it. Do not guess.
- If the excerpts disagree, say so rather than silently picking one.
- Be direct and concrete. A supervisor is reading this on the floor: lead with the answer, \
then the conditions attached to it.
- Preserve exact figures, tolerances, and units as written.
- When a procedure has a safety precondition in the excerpts, state it before the steps, \
not after."""

SAFETY_NOTE = (
    "This answer draws on safety documentation. Safety requirements are "
    "preconditions, not suggestions — do not begin the task until they are met."
)


def build_context(chunks):
    parts = []
    for c in chunks:
        parts.append(
            f"[{c['citation']}] {c['title']} > §{c['section_num']}. {c['section_title']}\n"
            f"{c['text']}"
        )
    return "\n\n---\n\n".join(parts)


def ask(question: str, k=None, max_chunks=None) -> dict:
    r = route(question)

    if r["out_of_scope"]:
        return {
            "question": question, "route": r, "chunks": [],
            "answer": ("That falls outside the Plant 4 documentation set, which covers "
                       "safety procedures, maintenance manuals, and quality standards. "
                       "For this, contact HR or your supervisor."),
            "safety_flagged": False,
        }

    kw = {}
    if k is not None:
        kw["k"] = k
    if max_chunks is not None:
        kw["max_chunks"] = max_chunks
    chunks = search(question, categories=r["categories"], **kw)

    if not chunks:
        return {"question": question, "route": r, "chunks": [],
                "answer": "No relevant documentation found for that question.",
                "safety_flagged": False}

    safety_flagged = any(c["category"] == "safety" for c in chunks)

    user = (f"Documentation excerpts:\n\n{build_context(chunks)}\n\n"
            f"Question: {question}")

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
    }
