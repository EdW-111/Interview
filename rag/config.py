"""Shared configuration and the DeepSeek client factory."""
import os
import re
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

# Lexical layer for plant identifiers the embedding model handles poorly:
# fault codes (E-301, D-01), equipment (TX-250, AD-300), fasteners (M16),
# valve tags (BV-1), priorities (P1). Compared uppercase with hyphens removed
# so "e301", "E301" and "E-301" all hit the same chunk.
CODE_RE = re.compile(r"\b([A-Za-z]{1,4})-?(\d{1,4})([A-Za-z]?)\b")
# Material grades carry no digits, so the regex cannot find them.
MATERIAL_CODES = {"PA66", "PA6", "PBT", "POM", "PC", "ABS", "PP", "PET"}
# In-scope top-1 cosine spans ~0.665-0.824. One exact-code hit worth 0.10
# lifts a matching chunk to the top of its lane without pulling an unrelated
# chunk from below the out-of-scope floor into context. Provisional.
CODE_BOOST = 0.10

# Colloquial equipment names -> frontmatter equipment ids. "press" is
# deliberately absent: it is the default context of a molding plant, and
# boosting every doc that lists a press demoted the resin-drying manual on
# "silver streaks on press 4" (its equipment list has no press).
EQUIPMENT_ALIASES = {
    "dryer": ["AD-300"],
    "tcu": ["TCU-90"],
    "chiller": ["TCU-90", "chiller_loop"],
    "robot": ["PR-12"],
    "granulator": ["GR-40"],
    "crane": ["overhead_crane"],
    "forklift": ["forklift_FL_series"],
}
# Document-level signal, so keep it weak.
EQUIP_BOOST = 0.03

ROLES = ["operator", "process_tech", "maintenance_tech", "quality_tech",
         "floor_supervisor", "material_handler"]
DEFAULT_ROLE = "floor_supervisor"


def llm() -> OpenAI:
    key = os.getenv("DEEPSEEK_API_KEY")
    if not key:
        raise RuntimeError("DEEPSEEK_API_KEY missing from .env")
    return OpenAI(api_key=key, base_url=DEEPSEEK_BASE_URL, timeout=30.0)
