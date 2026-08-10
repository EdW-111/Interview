"""Confidence signals.

The router's self-reported confidence is close to useless on its own — the
model returns ~0.95 for almost everything, because an LLM asked to rate its own
certainty is not calibrated. Retrieval cosine is grounded evidence: it says
whether the corpus actually contains anything close to the question.

So we report both, and combine them with retrieval dominating.
"""
from rag.config import SCORE_FLOOR, SCORE_OOS_ANCHOR, SCORE_STRONG


def retrieval_signal(chunks):
    """Summarise how strong the retrieved evidence is."""
    if not chunks:
        return {"top": 0.0, "mean3": 0.0, "band": "none", "score": 0.0,
                "note": "nothing retrieved"}

    scores = [c["score"] for c in chunks]
    top = scores[0]
    mean3 = sum(scores[:3]) / min(3, len(scores))

    if top >= SCORE_STRONG:
        band, note = "strong", "close match in the documentation"
    elif top >= SCORE_FLOOR:
        band, note = "moderate", "relevant material found, may be partial"
    else:
        band, note = "weak", "no close match — the corpus may not cover this"

    # Map onto 0-1 anchored on the observed populations rather than an
    # arbitrary range: the out-of-scope score sits at ~0.5, the weak-match
    # floor at 0.6, and a strong match at 0.85. Anchoring this way stops a
    # correctly-answered question at the low end of in-scope (top1 ~0.665)
    # from being scored as if it were barely retrieved.
    norm = max(0.0, min(1.0, (top - SCORE_OOS_ANCHOR) /
                        (SCORE_STRONG - SCORE_OOS_ANCHOR) * 0.85))

    return {"top": round(top, 4), "mean3": round(mean3, 4),
            "band": band, "score": round(norm, 3), "note": note}


def combine(router_conf: float, retrieval: dict) -> dict:
    """Overall answerability.

    The label comes from the retrieval band, not from the blended number. The
    band is derived from two empirically separated populations (in-scope vs
    out-of-scope top-1 cosine), whereas the blended number is dragged around by
    the router's uncalibrated self-report. Reporting a number that disagrees
    with the evidence band would just produce false alarms on questions that
    were in fact answered correctly.
    """
    overall = round(0.25 * float(router_conf) + 0.75 * retrieval["score"], 3)
    label = {"strong": "high", "moderate": "medium",
             "weak": "low", "none": "low"}[retrieval["band"]]
    return {"overall": overall, "label": label,
            "router_confidence": round(float(router_conf), 3),
            "retrieval_confidence": retrieval["score"],
            "retrieval_band": retrieval["band"]}
