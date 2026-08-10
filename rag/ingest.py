"""Parse the markdown corpus, chunk it by section, embed, and cache.

Run once:  python -m rag.ingest
"""
import json
import re
from collections import Counter

import numpy as np
import yaml

from rag.config import (CACHE_DIR, CHUNKS_PATH, DATA_DIR, EMBED_MODEL,
                        EMBED_PATH, MAX_SECTION_CHARS, REVIEW_PATH)

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)
H2_RE = re.compile(r"^## ", re.MULTILINE)
H3_RE = re.compile(r"^### ", re.MULTILINE)
# "## 4. Disposition" -> ("4", "Disposition")
HEADING_RE = re.compile(r"^(#{2,3})\s*(\d+)?\.?\s*(.*)$")

# Pure cross-reference lists; they retrieve as noise and answer nothing.
SKIP_SECTIONS = {"related documents"}


def parse_doc(path):
    raw = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(raw)
    if not m:
        raise ValueError(f"no frontmatter in {path}")
    return yaml.safe_load(m.group(1)), m.group(2)


def split_sections(body):
    """Split on ##, then split oversized ## sections on ###."""
    out = []
    # parts[0] is the pre-first-heading preamble (the H1 title line), not a
    # section — keeping it produces a title-only chunk that retrieves as noise.
    parts = H2_RE.split(body)[1:]
    for part in parts:
        if not part.strip():
            continue
        head, _, rest = part.partition("\n")
        h = HEADING_RE.match("## " + head.strip())
        num, title = (h.group(2), h.group(3)) if h else (None, head.strip())
        if title.strip().lower() in SKIP_SECTIONS:
            continue

        if len(rest) > MAX_SECTION_CHARS and H3_RE.search(rest):
            # Keep the section preamble, then one chunk per ### subsection.
            pre, *subs = H3_RE.split(rest)
            if pre.strip():
                out.append((num, title, pre.strip()))
            for sub in subs:
                shead, _, sbody = sub.partition("\n")
                out.append((num, f"{title} — {shead.strip()}", sbody.strip()))
        else:
            out.append((num, title, rest.strip()))
    return [(n, t, b) for n, t, b in out if b]


def build_chunks():
    chunks = []
    for path in sorted(DATA_DIR.glob("*/*.md")):
        fm, body = parse_doc(path)
        keywords = ", ".join(fm.get("keywords", []) or [])
        for num, title, text in split_sections(body):
            label = f"§{num}. {title}" if num else title
            # The embedded text carries document context, or a chunk headed
            # "Disposition" embeds with no idea what it dispositions.
            embed_text = (
                f"[{fm['category']}] {fm['title']} > {label}\n"
                f"keywords: {keywords}\n\n{text}"
            )
            chunks.append({
                "doc_id": fm["doc_id"],
                "title": fm["title"],
                "category": fm["category"],
                "revision": str(fm.get("revision", "")),
                "effective_date": str(fm.get("effective_date", "")),
                "section_num": num,
                "section_title": title,
                "citation": f"{fm['doc_id']} §{num}" if num else fm["doc_id"],
                "path": str(path.relative_to(DATA_DIR.parent)).replace("\\", "/"),
                "text": text,
                "embed_text": embed_text,
            })
    return chunks


def main():
    from sentence_transformers import SentenceTransformer

    chunks = build_chunks()
    print(f"parsed {len(set(c['doc_id'] for c in chunks))} docs -> {len(chunks)} chunks")
    print("  by category:", dict(Counter(c["category"] for c in chunks)))
    lens = [len(c["text"]) for c in chunks]
    print(f"  chars: min={min(lens)} median={int(np.median(lens))} max={max(lens)}")

    model = SentenceTransformer(EMBED_MODEL)
    vecs = model.encode(
        [c["embed_text"] for c in chunks],
        normalize_embeddings=True,      # cosine becomes a plain dot product
        batch_size=32,
        show_progress_bar=True,
    ).astype("float32")

    CACHE_DIR.mkdir(exist_ok=True)
    payload = json.dumps(chunks, ensure_ascii=False, indent=2)
    CHUNKS_PATH.write_text(payload, encoding="utf-8")
    np.save(EMBED_PATH, vecs)
    # Second copy outside the dotted cache dir — Explorer hides .cache/, and
    # the chunk boundaries are the thing most worth eyeballing.
    REVIEW_PATH.write_text(payload, encoding="utf-8")

    print(f"cached {vecs.shape} -> {EMBED_PATH}")
    print(f"REVIEW CHUNKS HERE -> {REVIEW_PATH}")


if __name__ == "__main__":
    main()
