"""Offline retrieval inspector — no LLM, no API calls.

  python scripts/search.py "silver streaks on parts"
  python scripts/search.py "clear a mold protect fault" --cat maintenance safety
  python scripts/search.py "torque for M16 clamp bolts" --k 5 --full
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from rag.store import search  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--cat", nargs="*", default=None,
                    help="restrict to categories (default: all)")
    ap.add_argument("--k", type=int, default=4, help="top-k per category")
    ap.add_argument("--max", type=int, default=8, help="total chunks returned")
    ap.add_argument("--full", action="store_true", help="print full chunk text")
    a = ap.parse_args()

    hits = search(a.query, categories=a.cat, k=a.k, max_chunks=a.max)

    print(f"\nQ: {a.query}")
    print(f"   categories={a.cat or 'ALL'}  k={a.k}\n")
    for i, h in enumerate(hits, 1):
        print(f"{i:2}. {h['score']:.4f}  [{h['category']:11}] "
              f"{h['citation']:12} {h['title']}")
        print(f"              > {h['section_title']}")
        if a.full:
            body = h["text"]
            print("\n" + "\n".join("      " + ln for ln in body.splitlines()) + "\n")
        else:
            snippet = " ".join(h["text"].split())[:150]
            print(f"              {snippet}...")
    print()


if __name__ == "__main__":
    main()
