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

    def cats_for(q):
        return next(x["expected_categories"] for x in scored if x["question"] == q)

    def naive_ranked(q):
        s = vecs @ embed_query(q)
        return [chunks[i]["citation"] for i in np.argsort(-s)[:n]]

    def routed_dense(q):
        return [h["citation"] for h in search(q, cats_for(q), max_chunks=n, lexical=False)]

    def routed_hybrid(q):
        return [h["citation"] for h in search(q, cats_for(q), max_chunks=n)]

    cc = [q for q in scored if q["kind"] in ("cross-cutting", "safety-gated")]
    codes = [q for q in scored if q["kind"] in ("code-lookup", "role-gated")]
    variants = [("naive flat top-k (plain RAG)  ", naive_ranked),
                ("routed fan-out, dense only    ", routed_dense),
                ("routed fan-out + code boost   ", routed_hybrid)]
    got = {name: {q["id"]: fn(q["question"]) for q in scored} for name, fn in variants}

    def recall(name, qs_):
        return sum(1 for q in qs_ if set(q["expected_citations"]) <= set(got[name][q["id"]]))

    # Recall @ 8 saturates on single-hop questions; where an identifier
    # lookup actually differs is whether the right section is at the top or
    # buried under a look-alike sibling (E-104 is in §2, §3 and §4 all look
    # the same to the embedding).
    def at_rank1(name, qs_):
        return sum(1 for q in qs_ if got[name][q["id"]][:1] and
                   got[name][q["id"]][0] in q["expected_citations"])

    print(f"\n  ABLATION — section-level context recall @ {n} chunks")
    print(f"    {'':34} {'all':>9}   {'multi-source':>12}   {'code/role':>9}")
    for name, _ in variants:
        print(f"    {name}  {recall(name, scored):>3}/{len(scored):<5} "
              f"{recall(name, cc):>7}/{len(cc):<5} {recall(name, codes):>7}/{len(codes)}")

    print(f"\n  ABLATION — an expected section at rank 1")
    print(f"    {'':34} {'all':>9}   {'code/role':>9}")
    for name, _ in variants:
        print(f"    {name}  {at_rank1(name, scored):>3}/{len(scored):<5} "
              f"{at_rank1(name, codes):>7}/{len(codes)}")


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
