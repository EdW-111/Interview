"""Shared configuration and the DeepSeek client factory."""
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
CACHE_DIR = ROOT / ".cache"
CHUNKS_PATH = CACHE_DIR / "chunks.json"
EMBED_PATH = CACHE_DIR / "embeddings.npy"
# Human-readable copy in the project root, since .cache/ is hidden in Explorer.
REVIEW_PATH = ROOT / "chunks_review.json"

EMBED_MODEL = "BAAI/bge-small-en-v1.5"
# BGE v1.5 is asymmetric: passages embed raw, queries take this prefix.
QUERY_PREFIX = "Represent this sentence for searching relevant passages: "

LLM_MODEL = "deepseek-chat"
DEEPSEEK_BASE_URL = "https://api.deepseek.com"

CATEGORIES = ["safety", "maintenance", "quality"]

K_PER_CATEGORY = 4
MAX_CHUNKS = 8
# Max chunks from any single document, so one document cannot fill the context
# with near-duplicate siblings. Adaptive: a single-category route can go deeper
# into one manual, a multi-category route needs breadth instead.
PER_DOC_CAP_NARROW = 3   # router returned one category
PER_DOC_CAP_BROAD = 2    # router returned two or more

# Retrieval-score bands, calibrated on the 22-question eval set. Observed
# top-1 cosine: in-scope 0.665-0.824 (median 0.704), out-of-scope 0.576.
# The floor sits in the gap between those two populations.
# These are fitted to 22 questions — treat as provisional, re-fit with more data.
SCORE_STRONG = 0.75      # top quartile of in-scope questions
SCORE_FLOOR = 0.62       # below every in-scope question seen; likely uncovered
SCORE_OOS_ANCHOR = 0.55  # where an uncovered question lands; the zero point
# Split a section further on ### only when it is bigger than this.
MAX_SECTION_CHARS = 1200


def llm() -> OpenAI:
    key = os.getenv("DEEPSEEK_API_KEY")
    if not key:
        raise RuntimeError("DEEPSEEK_API_KEY missing from .env")
    return OpenAI(api_key=key, base_url=DEEPSEEK_BASE_URL, timeout=30.0)
