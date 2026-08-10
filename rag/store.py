"""Offline retrieval: BGE dense search over the cached chunks.

No LLM involved — this layer is deliberately testable on its own.
"""
import json
import functools

import numpy as np

from rag.config import (CHUNKS_PATH, EMBED_MODEL, EMBED_PATH, K_PER_CATEGORY,
                        MAX_CHUNKS, PER_DOC_CAP_BROAD, PER_DOC_CAP_NARROW,
                        QUERY_PREFIX)


@functools.lru_cache(maxsize=1)
def _load():
    if not CHUNKS_PATH.exists():
        raise RuntimeError("cache missing — run: python -m rag.ingest")
    chunks = json.loads(CHUNKS_PATH.read_text(encoding="utf-8"))
    vecs = np.load(EMBED_PATH)
    cats = np.array([c["category"] for c in chunks])
    return chunks, vecs, cats


@functools.lru_cache(maxsize=1)
def _model():
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer(EMBED_MODEL)


def embed_query(q: str) -> np.ndarray:
    return _model().encode(
        QUERY_PREFIX + q, normalize_embeddings=True
    ).astype("float32")


def search(query, categories=None, k=K_PER_CATEGORY, max_chunks=MAX_CHUNKS,
           per_doc_cap=None):
    """Top-k per category with a per-document diversity cap, merged and capped.

    Two deliberate choices here:

    1. Per-category top-k, not a global top-k. A global top-k on a
       cross-cutting question returns whichever category scores highest, so
       the second source never surfaces. This is what routing buys.

    2. A per-document cap. Without it, "silver streaks on parts" fills every
       quality slot with sibling chunks from the QC-004 defect catalog
       (splay, jetting, flash, sink) because they are near-identical in
       shape, crowding out the actual root cause in MNT-004.
    """
    chunks, vecs, cats = _load()
    qv = embed_query(query)
    scores = vecs @ qv

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
        for i in idx[np.argsort(-scores[idx])]:
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
    for rank in range(k):
        for lane in per_cat:
            if rank < len(lane) and len(picked) < max_chunks:
                picked.append(lane[rank])

    picked.sort(key=lambda i: -scores[i])
    return [{**chunks[i], "score": round(float(scores[i]), 4)}
            for i in picked[:max_chunks]]
