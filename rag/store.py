"""Offline retrieval: BGE dense search plus a lexical boost for plant identifiers.

No LLM involved — this layer is deliberately testable on its own.
"""
import json
import functools
from collections import defaultdict

import numpy as np

from rag.codes import detect_equipment, extract_codes, normalize
from rag.config import (CHUNKS_PATH, CODE_BOOST, EMBED_MODEL, EMBED_PATH,
                        EQUIP_BOOST, K_PER_CATEGORY, MAX_CHUNKS,
                        PER_DOC_CAP_BROAD, PER_DOC_CAP_NARROW, QUERY_PREFIX)


@functools.lru_cache(maxsize=1)
def _load():
    if not CHUNKS_PATH.exists():
        raise RuntimeError("cache missing — run: python -m rag.ingest")
    chunks = json.loads(CHUNKS_PATH.read_text(encoding="utf-8"))
    vecs = np.load(EMBED_PATH)
    cats = np.array([c["category"] for c in chunks])
    return chunks, vecs, cats


@functools.lru_cache(maxsize=1)
def _indexes():
    """Inverted indexes: normalized code / equipment id / doc id -> chunk indices."""
    chunks, _, _ = _load()
    code_idx, equip_idx, doc_idx = defaultdict(list), defaultdict(list), defaultdict(list)
    for i, c in enumerate(chunks):
        for code in c.get("codes", []):
            code_idx[code].append(i)
        for eq in c.get("equipment", []):
            equip_idx[normalize(eq)].append(i)
        doc_idx[normalize(c["doc_id"])].append(i)
    arr = lambda d: {k: np.array(v) for k, v in d.items()}  # noqa: E731
    return arr(code_idx), arr(equip_idx), arr(doc_idx)


@functools.lru_cache(maxsize=1)
def _model():
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer(EMBED_MODEL)


def embed_query(q: str) -> np.ndarray:
    return _model().encode(
        QUERY_PREFIX + q, normalize_embeddings=True
    ).astype("float32")


def lexical_boost(query, n_chunks):
    """Additive boost per chunk from exact identifier, doc-id and equipment matches.

    Returns the boost vector and, per chunk index, which query codes it hit.
    """
    code_idx, equip_idx, doc_idx = _indexes()
    boost = np.zeros(n_chunks, dtype="float32")
    hits = defaultdict(list)

    qcodes = extract_codes(query)
    for code in sorted(qcodes):
        # A code in the body (E-301) or the document the user named (SAF-001).
        for idx in (code_idx.get(code), doc_idx.get(code)):
            if idx is not None:
                boost[idx] += CODE_BOOST
                for i in idx:
                    hits[int(i)].append(code)

    # Equipment named colloquially ("the dryer") or by id ("AD-300").
    qequip = detect_equipment(query) | (qcodes & set(equip_idx))
    for eq in qequip:
        if eq in equip_idx:
            boost[equip_idx[eq]] += EQUIP_BOOST

    return boost, hits


def search(query, categories=None, k=K_PER_CATEGORY, max_chunks=MAX_CHUNKS,
           per_doc_cap=None, lexical=True):
    """Top-k per category with a per-document diversity cap, merged and capped.

    Three deliberate choices here:

    1. Per-category top-k, not a global top-k. A global top-k on a
       cross-cutting question returns whichever category scores highest, so
       the second source never surfaces. This is what routing buys.

    2. A per-document cap. Without it, "silver streaks on parts" fills every
       quality slot with sibling chunks from the QC-004 defect catalog
       (splay, jetting, flash, sink) because they are near-identical in
       shape, crowding out the actual root cause in MNT-004.

    3. Ranking by cosine + lexical boost, but reporting raw cosine as `score`.
       bge-small does not reliably separate E-203 from E-204; an exact code
       hit does. Keeping `score` as pure cosine leaves the calibrated
       confidence bands and the eval reports comparable across runs.
    """
    chunks, vecs, cats = _load()
    qv = embed_query(query)
    scores = vecs @ qv

    if lexical:
        boost, hits = lexical_boost(query, len(chunks))
    else:
        boost, hits = np.zeros(len(chunks), dtype="float32"), {}
    rank = scores + boost

    categories = list(categories) if categories else sorted(set(cats.tolist()))

    # Let the route shape the strategy, not just the filter. A single-category
    # route means the answer sits in one manual, so allow more sections from
    # the same document. A multi-category route means breadth matters more
    # than depth, so tighten the cap to stop one document eating the window.
    if per_doc_cap is None:
        per_doc_cap = PER_DOC_CAP_NARROW if len(categories) == 1 else PER_DOC_CAP_BROAD

    per_cat = []
    for cat in categories:
        idx = np.flatnonzero(cats == cat)
        if idx.size == 0:
            continue
        lane, seen = [], {}
        for i in idx[np.argsort(-rank[idx])]:
            doc = chunks[i]["doc_id"]
            if seen.get(doc, 0) >= per_doc_cap:
                continue
            seen[doc] = seen.get(doc, 0) + 1
            lane.append(int(i))
            if len(lane) >= k:
                break
        per_cat.append(lane)

    # Round-robin across categories rather than a global score sort. A plain
    # sort lets the highest-scoring category eat the whole context window,
    # which silently undoes the fan-out on exactly the cross-cutting questions
    # routing exists to serve.
    picked = []
    for r in range(k):
        for lane in per_cat:
            if r < len(lane) and len(picked) < max_chunks:
                picked.append(lane[r])

    picked.sort(key=lambda i: -rank[i])
    return [{**chunks[i],
             "score": round(float(scores[i]), 4),
             "rank_score": round(float(rank[i]), 4),
             "code_hits": hits.get(i, [])}
            for i in picked[:max_chunks]]
