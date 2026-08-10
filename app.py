"""Plant 4 Documentation Assistant — FastAPI surface.

  uvicorn app:app --reload
"""
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from rag.answer import ask

STATIC = Path(__file__).parent / "static"

app = FastAPI(title="Plant 4 Documentation Assistant")


@app.on_event("startup")
def warmup():
    """Force the embedding model to load before the first request.

    Without this, SentenceTransformer loads lazily inside the first /ask and
    that request takes ~17s while every later one takes ~3s. In a live demo
    that cost lands on the very first question someone asks.
    """
    import time
    from rag.store import _load, embed_query
    t = time.time()
    _load()
    embed_query("warmup")
    print(f"[startup] embedding model warm in {time.time() - t:.1f}s")


class Query(BaseModel):
    question: str


@app.get("/")
def index():
    return FileResponse(STATIC / "index.html")


@app.get("/health")
def health():
    from rag.store import _load
    chunks, vecs, _ = _load()
    return {"status": "ok", "chunks": len(chunks), "dims": int(vecs.shape[1])}


@app.post("/ask")
def ask_endpoint(q: Query):
    import time
    t0 = time.time()
    r = ask(q.question)
    r["elapsed_ms"] = int((time.time() - t0) * 1000)
    # Trim chunk bodies for transport; the UI shows a preview, not the full doc.
    r["chunks"] = [{
        "citation": c["citation"], "title": c["title"], "category": c["category"],
        "section_title": c["section_title"], "score": c["score"],
        "path": c["path"], "preview": " ".join(c["text"].split())[:280],
    } for c in r["chunks"]]
    return r
