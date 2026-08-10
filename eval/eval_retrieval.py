"""Retrieval-only eval — no LLM, no API calls, runs in seconds.

Scores at SECTION level ("MNT-003 §2"), not document level. Document-level
scoring is too generous: MNT-003 has seven sections and only one of them
answers "why is the oil milky", so a doc-level hit can pass while the chunk
the generator actually needs is absent.

  python eval/eval_retrieval.py
  python eval/eval_retrieval.py --ablate
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rag.store import search  # noqa: E402

QUESTIONS = Path(__file__).parent / "questions.json"


def ablation(scored, n):
    """Section-level context recall vs. a naive flat top-k baseline."""
    import numpy as np
    from rag.store import _load, embed_query

    chunks, vecs, _ = _load()

    def naive(q):
        s = vecs @ embed_query(q)
        return {chunks[i]["citation"] for i in np.argsort(-s)[:n]}

    def ours(q):
        cats = next(x["expected_categories"] for x in scored if x["question"] == q)
        return {h["citation"] for h in search(q, cats, max_chunks=n)}

    cc = [q for q in scored if q["kind"] in ("cross-cutting", "safety-gated")]

    def rate(fn, qs_):
        return sum(1 for q in qs_ if set(q["expected_citations"]) <= fn(q["question"]))

    print(f"\n  ABLATION — section-level context recall @ {n} chunks")
    print(f"    {'':32} {'all':>9}   {'multi-source':>12}")
    for name, fn in [("naive flat top-k (plain RAG)", naive),
                     ("routed fan-out + diversity  ", ours)]:
        print(f"    {name}  {rate(fn, scored):>3}/{len(scored):<5} "
              f"{rate(fn, cc):>7}/{len(cc)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=8, help="chunks sent to generator")
    ap.add_argument("--ablate", action="store_true")
    ap.add_argument("--no-route", action="store_true",
                    help="search all categories instead of the labelled route")
    a = ap.parse_args()

    qs = json.loads(QUESTIONS.read_text(encoding="utf-8"))
    scored = [q for q in qs if q["expected_citations"]]

    full = partial = 0
    rows, misses = [], []

    for q in scored:
        # Oracle routing: use the labelled categories so this measures
        # retrieval in isolation. Router accuracy is scored separately.
        cats = None if a.no_route else q["expected_categories"]
        hits = search(q["question"], categories=cats, max_chunks=a.max)
        got = [h["citation"] for h in hits]
        want = set(q["expected_citations"])
        found = want & set(got)

        if found == want:
            full += 1
            mark = "PASS"
        elif found:
            partial += 1
            mark = "PART"
        else:
            mark = "MISS"

        # Show the rank each expected citation landed at — a hit at rank 8 is
        # meaningfully weaker than a hit at rank 1.
        detail = []
        for c in q["expected_citations"]:
            r = got.index(c) + 1 if c in got else None
            detail.append(f"{c}@{r}" if r else f"{c}@--")
        rows.append((mark, q["id"], " ".join(detail)))
        if mark != "PASS":
            misses.append((q, got))

    print(f"  section-level recall in top {a.max} chunks "
          f"(expected citation @ rank, -- = absent)\n")
    for mark, qid, detail in rows:
        print(f"    {mark}  {qid}  {detail}")

    n = len(scored)
    print(f"\n  all expected sections retrieved : {full}/{n}  ({full/n:.0%})")
    print(f"  at least one retrieved          : {full+partial}/{n}  ({(full+partial)/n:.0%})")

    if misses:
        print("\n  not fully retrieved:")
        for q, got in misses:
            missing = [c for c in q["expected_citations"] if c not in got]
            print(f"    {q['id']}  missing {missing}")
            print(f"          {q['question'][:66]}")

    if a.ablate:
        ablation(scored, a.max)


if __name__ == "__main__":
    main()
