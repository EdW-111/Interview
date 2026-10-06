"""Extract plant identifiers (fault codes, equipment ids, fastener sizes) from text."""
import re

from rag.config import CODE_RE, EQUIPMENT_ALIASES, MATERIAL_CODES

# Case-sensitive on purpose: "PC" is a resin grade, "pc" in prose is not.
MATERIAL_RE = re.compile(r"\b(" + "|".join(sorted(MATERIAL_CODES, key=len, reverse=True)) + r")\b")


def normalize(code: str) -> str:
    return code.upper().replace("-", "").replace(" ", "")


def extract_codes(text: str) -> set[str]:
    found = {normalize(m.group(0)) for m in CODE_RE.finditer(text)}
    found.update(m.group(1) for m in MATERIAL_RE.finditer(text))
    return found


def detect_equipment(question: str) -> set[str]:
    """Equipment ids (normalized) implied by colloquial names or typed directly."""
    q = question.lower()
    ids = {normalize(i) for alias, eq_ids in EQUIPMENT_ALIASES.items()
           if alias in q for i in eq_ids}
    return ids
