"""End-to-end LLM eval — runs the full pipeline and writes a Markdown report
you can read to inspect what the model actually produced.

  python eval/eval_llm.py                    # all questions -> eval/report.md
  python eval/eval_llm.py --limit 5          # quick smoke run
  python eval/eval_llm.py --out out.md --workers 6

Scored automatically (no LLM judge):
  - routing        : did the router pick the labelled categories
  - section recall : did the expected sections reach the context
  - citation trust : did the answer cite only documents it was actually given
  - grounding      : did the answer cite at least one expected section
"""
import argparse
import datetime as dt
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rag.answer import ask  # noqa: E402
from rag.config import EMBED_MODEL, LLM_MODEL  # noqa: E402

QUESTIONS = Path(__file__).parent / "questions.json"


def evaluate(q):
    r = ask(q["question"], role=q.get("role"))
    got_cats = set(r["route"]["categories"])
    want_cats = set(q["expected_categories"])
    got_cites = [c["citation"] for c in r["chunks"]]
    want_cites = set(q["expected_citations"])

    # Distinguish over-broad from actually wrong. A router that returns the
    # right category plus an extra one still surfaces the right document; a
    # router that drops a required category loses the answer outright. Only
    # the second is a real failure for a plant assistant.
    if got_cats == want_cats:
        route_mark = "exact"
    elif want_cats and want_cats <= got_cats:
        route_mark = "over-broad"
    elif got_cats & want_cats:
        route_mark = "partial"
    else:
        route_mark = "miss"

    found = want_cites & set(got_cites)
    if not want_cites:
        recall_mark = "n/a"
    elif found == want_cites:
        recall_mark = "full"
    elif found:
        recall_mark = "partial"
    else:
        recall_mark = "miss"

    answered_cites = set(r["citations"]["cited"])
    grounded = bool(want_cites & answered_cites) if want_cites else None

    return {**q, "result": r, "route_mark": route_mark, "recall_mark": recall_mark,
            "found": sorted(found), "grounded": grounded}


def md_escape(s):
    return s.replace("|", "\\|")


def render(rows, path, elapsed):
    L = []
    A = L.append
    n = len(rows)
    scored = [r for r in rows if r["expected_citations"]]

    route_exact = sum(1 for r in rows if r["route_mark"] == "exact")
    route_nomiss = sum(1 for r in rows if r["route_mark"] in ("exact", "over-broad"))
    route_broad = sum(1 for r in rows if r["route_mark"] == "over-broad")
    route_miss = sum(1 for r in rows if r["route_mark"] in ("miss", "partial"))
    recall_full = sum(1 for r in scored if r["recall_mark"] == "full")
    cite_clean = sum(1 for r in rows if r["result"]["citations"]["all_supported"])
    grounded = sum(1 for r in scored if r["grounded"])

    A("# LLM Eval Report — Plant 4 Documentation Assistant\n")
    A(f"- generated: `{dt.datetime.now():%Y-%m-%d %H:%M:%S}`  ")
    A(f"- generator: `{LLM_MODEL}`  ")
    A(f"- embeddings: `{EMBED_MODEL}`  ")
    A(f"- questions: {n}  ")
    A(f"- wall time: {elapsed:.1f}s\n")

    A("## Aggregate\n")
    A("| metric | result | |")
    A("|---|---|---|")
    A(f"| Routing — exact category set | {route_exact}/{n} | {route_exact/n:.0%} |")
    A(f"| Routing — never dropped a required category | {route_nomiss}/{n} "
      f"| {route_nomiss/n:.0%} |")
    A(f"| Routing — over-broad (correct + extra) | {route_broad}/{n} | |")
    A(f"| Routing — dropped a required category | {route_miss}/{n} | |")
    A(f"| Section recall — all expected in context | {recall_full}/{len(scored)} "
      f"| {recall_full/len(scored):.0%} |")
    A(f"| Citation trust — no unsupported citations | {cite_clean}/{n} | {cite_clean/n:.0%} |")
    A(f"| Grounding — answer cites an expected section | {grounded}/{len(scored)} "
      f"| {grounded/len(scored):.0%} |")
    A("")

    A("## Summary\n")
    A("| id | kind | route | recall | conf | band | exact | top1 | cites | unsupported |")
    A("|---|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        res = r["result"]
        c, ret = res["confidence"], res["retrieval"]
        uns = res["citations"]["unsupported"]
        exact = ", ".join(ret.get("exact_match", [])) or "—"
        A(f"| [{r['id']}](#{r['id']}) | {r['kind']} | {r['route_mark']} "
          f"| {r['recall_mark']} | {c['overall']:.2f} {c['label']} | {ret['band']} "
          f"| {exact} | {ret['top']:.3f} | {len(res['citations']['cited'])} "
          f"| {', '.join(uns) if uns else '—'} |")
    A("")

    A("---\n")
    for r in rows:
        res = r["result"]
        c, ret, rt = res["confidence"], res["retrieval"], res["route"]

        A(f"<a id=\"{r['id']}\"></a>")
        role_tag = f" (role: {r['role']})" if r.get("role") else ""
        A(f"## {r['id']} — {r['kind']}{role_tag}\n")
        A(f"**Q:** {r['question']}\n")

        A("| | expected | actual |")
        A("|---|---|---|")
        A(f"| route | `{r['expected_categories'] or '[] (out of scope)'}` "
          f"| `{rt['categories'] or '[] (out of scope)'}` → **{r['route_mark']}** |")
        A(f"| sections | `{r['expected_citations'] or '—'}` "
          f"| found `{r['found'] or '—'}` → **{r['recall_mark']}** |")
        A("")
        A(f"**Router reasoning:** _{md_escape(rt['reasoning'])}_  ")
        A(f"**Confidence:** overall **{c['overall']:.2f} ({c['label']})** "
          f"— router {c['router_confidence']:.2f} × retrieval {c['retrieval_confidence']:.2f} "
          f"| band `{ret['band']}` (top1 {ret['top']:.3f}, mean3 {ret['mean3']:.3f}) — {ret['note']}\n")

        if res["chunks"]:
            A("<details><summary>Retrieved context "
              f"({len(res['chunks'])} chunks)</summary>\n")
            A("| # | score | exact | citation | category | section | expected |")
            A("|---|---|---|---|---|---|---|")
            for i, ch in enumerate(res["chunks"], 1):
                hit = "**YES**" if ch["citation"] in r["expected_citations"] else ""
                ex = ", ".join(ch.get("code_hits", [])) or ""
                A(f"| {i} | {ch['score']:.3f} | {ex} | `{ch['citation']}` | {ch['category']} "
                  f"| {md_escape(ch['section_title'][:44])} | {hit} |")
            A("\n</details>\n")

        if res["safety_flagged"]:
            A(f"> **SAFETY OVERLAY FIRED** — {res['safety_note']}\n")

        A("**Answer:**\n")
        A("> " + res["answer"].replace("\n", "\n> ") + "\n")

        cit = res["citations"]
        status = "all supported" if cit["all_supported"] else \
            f"**UNSUPPORTED: {cit['unsupported']}**"
        A(f"**Citations in answer:** {', '.join(f'`{x}`' for x in cit['cited']) or '—'} "
          f"— {status}\n")
        A("---\n")

    path.write_text("\n".join(L), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(Path(__file__).parent / "report.md"))
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()

    qs = json.loads(QUESTIONS.read_text(encoding="utf-8"))
    if a.limit:
        qs = qs[:a.limit]

    t0 = dt.datetime.now()
    print(f"running {len(qs)} questions through the full pipeline "
          f"({a.workers} workers)...", file=sys.stderr)

    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        rows = list(ex.map(evaluate, qs))
    rows.sort(key=lambda r: r["id"])

    elapsed = (dt.datetime.now() - t0).total_seconds()
    out = Path(a.out)
    render(rows, out, elapsed)

    n = len(rows)
    scored = [r for r in rows if r["expected_citations"]]
    print(f"\n  routing exact   : {sum(1 for r in rows if r['route_mark']=='exact')}/{n}")
    print(f"  section recall  : {sum(1 for r in scored if r['recall_mark']=='full')}/{len(scored)}")
    print(f"  citation trust  : {sum(1 for r in rows if r['result']['citations']['all_supported'])}/{n}")
    print(f"  grounded answers: {sum(1 for r in scored if r['grounded'])}/{len(scored)}")
    print(f"\n  report -> {out.resolve()}  ({elapsed:.1f}s)")


if __name__ == "__main__":
    main()
