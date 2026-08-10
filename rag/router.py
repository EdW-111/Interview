"""Route a question to the documentation categories that can answer it."""
import json

from rag.config import CATEGORIES, LLM_MODEL, llm

SYSTEM = """You route floor-supervisor questions at a plastic injection molding plant to the \
right documentation set. Reply with JSON only.

The three sets:
- safety: lockout/tagout, machine guarding and light curtains, burns and molten polymer, \
chemicals and spills, PPE, emergency and evacuation, forklifts and crane/rigging.
- maintenance: preventive maintenance schedules, mold changes, hydraulics, resin dryers, \
chillers and mold temperature, alarm and fault codes, lubrication and torque specs.
- quality: incoming material inspection, first article inspection, SPC and capability, \
visual defect standards, nonconforming material, gage calibration, customer complaints/CAPA.

Return every category that holds part of the answer, not just the closest one. Many real \
questions span two sets: a defect is described in quality but its root cause lives in \
maintenance; a maintenance task that opens the mold area is gated by a safety procedure.

Return this JSON shape:
{"categories": ["quality","maintenance"], "confidence": 0.0-1.0,
 "reasoning": "one short sentence", "out_of_scope": false}

Set out_of_scope true and categories [] only for questions this plant documentation cannot \
answer at all (HR, payroll, vacation, benefits, personal matters)."""

FEWSHOT = [
    ("Parts have silver streaks near the gate.",
     {"categories": ["quality", "maintenance"], "confidence": 0.9,
      "reasoning": "Splay is a visual defect standard, but its root cause is resin drying.",
      "out_of_scope": False}),
    ("How do I clear a mold protect fault?",
     {"categories": ["maintenance", "safety"], "confidence": 0.9,
      "reasoning": "Fault code is a maintenance topic, but clearing it opens the mold area, "
                   "which is gated by lockout/tagout.",
      "out_of_scope": False}),
    ("What Cpk do we need on a safety characteristic?",
     {"categories": ["quality"], "confidence": 0.95,
      "reasoning": "Capability requirement, purely a quality standard.",
      "out_of_scope": False}),
]


def route(question: str) -> dict:
    """Classify a question. Never raises — falls back to searching everything."""
    msgs = [{"role": "system", "content": SYSTEM}]
    for q, a in FEWSHOT:
        msgs.append({"role": "user", "content": q})
        msgs.append({"role": "assistant", "content": json.dumps(a)})
    msgs.append({"role": "user", "content": question})

    try:
        r = llm().chat.completions.create(
            model=LLM_MODEL,
            messages=msgs,
            temperature=0,
            max_tokens=200,
            response_format={"type": "json_object"},
        )
        d = json.loads(r.choices[0].message.content)
        cats = [c for c in d.get("categories", []) if c in CATEGORIES]

        if d.get("out_of_scope") and not cats:
            return {"categories": [], "confidence": float(d.get("confidence", 0.5)),
                    "reasoning": d.get("reasoning", ""), "out_of_scope": True,
                    "mode": "llm"}
        if not cats:
            raise ValueError("no usable categories")
        return {"categories": cats, "confidence": float(d.get("confidence", 0.5)),
                "reasoning": d.get("reasoning", ""), "out_of_scope": False,
                "mode": "llm"}

    except Exception as e:
        # Fail open. A supervisor on the floor must never get a hard error
        # because a classifier hiccuped — degrade to searching everything.
        return {"categories": list(CATEGORIES), "confidence": 0.0,
                "reasoning": f"router unavailable ({type(e).__name__}); searching all sources",
                "out_of_scope": False, "mode": "fallback"}
