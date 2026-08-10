---
doc_id: QC-004
title: Visual Defect Standards and Acceptance Criteria
category: quality
subcategory: visual_inspection
equipment: [QC_lab, all_cells]
applies_to: [operator, quality_tech, floor_supervisor, process_tech]
revision: "6.2"
effective_date: 2026-06-15
review_due: 2028-06-15
owner: Quality Manager
status: active
supersedes: "6.1"
related_docs: [MNT-004, MNT-005, MNT-006, QC-002, QC-003, QC-005]
keywords: [defect, splay, flash, short shot, sink, weld line, burn, warp, jetting, drag, contamination, cosmetic, zone, limit sample]
source: synthetic_demo_corpus
classification: internal_demo
contains_pii: false
---

# QC-004 — Visual Defect Standards and Acceptance Criteria

## 1. Inspection conditions

Visual inspection is only valid under standard conditions. Judgments made at the press under
bay lighting are not equivalent to a lab call.

| Condition | Standard |
|---|---|
| Illumination | 1,000 lux at the part surface, diffuse |
| Light source | D65 daylight-equivalent for any color assessment |
| Viewing distance | **450 mm** (arm's length) |
| Viewing time | **10 seconds** per surface |
| Viewing angle | Normal to the surface, ±45° |
| Part condition | As-molded, clean, at ambient |

If a defect is not visible under these conditions, it is not a rejectable cosmetic defect.
If it is visible, it is assessed against the zone limits below.

## 2. Cosmetic zones

Every part drawing assigns surfaces to a zone. When the drawing is silent, default to Zone B.

| Zone | Definition | Acceptance |
|---|---|---|
| **Zone A** | Visible in the customer's end use, primary appearance surface | Strictest limits; no defect that alters appearance |
| **Zone B** | Visible only on inspection or when the assembly is opened | Moderate limits |
| **Zone C** | Hidden in the assembly, non-appearance | Functional defects only |

**No zone permits a defect that affects function, strength, sealing, or assembly.**
Zone C is not "anything goes" — it means cosmetic-only criteria are relaxed.

## 3. Defect catalog

Each entry: what it looks like, the usual root cause, and where the fix lives.

### Splay (silver streaking)
Silver or white streaks radiating from the gate in the flow direction.
**Root cause:** moisture in the material, nearly always. Less often, degradation from excess
melt temperature or residence time, or air entrainment from a worn check ring.
**Fix:** verify dryer dew point and residence time per **MNT-004 §2/§3**; confirm moisture
by test (QC-006) before touching the process.
**Acceptance:** Zone A — none. Zone B — none if longer than 5 mm. Zone C — accept if function
is unaffected. *Note: splay is evidence of moisture, which can reduce strength even where it
is cosmetically acceptable. Splay on a structural or safety part is rejected in all zones.*

### Short shot
Incomplete fill; a missing or thin region at the end of flow.
**Root cause:** insufficient shot size or injection pressure/speed, blocked vent, low melt or
mold temperature, starved feed (check throat cooling, MNT-005 §1), non-return valve wear.
**Acceptance:** **Reject in all zones, always.** A short shot is a functional defect.

### Flash
Thin excess material at the parting line, around inserts, or at ejector pins.
**Root cause:** insufficient clamp tonnage, excessive injection pressure, parting-line damage
or wear, debris on the parting line, mold not seated (MNT-002 §5).
**Acceptance:** Zone A — none. Zone B — ≤ 0.05 mm thick and ≤ 3 mm long, not sharp.
Zone C — ≤ 0.15 mm, not sharp and not liable to break free.
**Any flash that is sharp, or that could detach and become loose debris in the customer's
assembly, is rejected in all zones.** Recurring flash indicates a tool condition problem —
raise a tool report, do not just increase tonnage.

### Sink marks
Localized depressions, typically opposite a rib, boss, or thick section.
**Root cause:** insufficient packing pressure or time, gate freezing early, mold temperature
too high, part design (thick section).
**Acceptance:** Zone A — not perceptible at 450 mm. Zone B — perceptible but not measurable
by touch. Zone C — accept if dimensions are in tolerance.

### Weld / knit lines
A visible line where two flow fronts meet.
**Root cause:** unavoidable around holes and inserts; severity is driven by melt and mold
temperature and by flow-front velocity.
**Acceptance:** Zone A — faint, no visible notch or color change. Zone B — visible line
acceptable, no notch. Zone C — accept.
**A weld line with a visible notch is a strength defect and is rejected in all zones.**

### Burn marks (dieseling)
Brown or black discoloration, usually at the end of fill or in a blind rib.
**Root cause:** trapped air with no vent path; injection speed too high; blocked or worn vents.
**Acceptance:** **Reject in all zones.** Burning means material degradation and local strength loss.

### Warp / dimensional distortion
Part out of flat or twisted.
**Root cause:** uneven cooling — the leading cause at Plant 4. Check TCU delta-T across the
tool is within **3 °C** (MNT-005 §2) and that water circuits are plumbed per the setup sheet
(MNT-002 §5) before adjusting process. Also: non-uniform wall, ejection while too hot,
residual stress.
**Acceptance:** Against the drawing's flatness/profile tolerance, measured after the
conditioning period in QC-002 §2 — not judged by eye.

### Black specks / contamination
Dark specks or foreign particles in the part.
**Root cause:** degraded material in the barrel, carbon from a poorly purged color change,
contaminated regrind, angel hair or line debris (MNT-004 §5), airborne dust.
**Acceptance:** Zone A — none visible. Zone B — max 2 specks ≤ 0.3 mm per part.
Zone C — max 5 specks ≤ 0.5 mm per part.
**Any metallic contamination is rejected in all zones and triggers a QC-005 containment**,
because its source (a wearing screw, check ring, or tool component) affects everything since
the last known-good check.

### Jetting
A snake-like squiggle from the gate.
**Root cause:** injection speed too high at gate entry; gate size or location.
**Acceptance:** Zone A — none. Zone B — none if in the primary field of view. Zone C — accept.

### Drag marks / scuffing
Scratches in the draw direction from ejection.
**Root cause:** insufficient draft, tool surface damage, galling, inadequate release,
ejection while too hot.
**Acceptance:** Zone A — none. Zone B — not felt with a fingernail. Zone C — accept.
Progressive worsening indicates tool damage — raise a tool report.

### Color variation
**Root cause:** masterbatch dosing error, inadequate mixing, screw wear, lot-to-lot pigment
variation, residence time.
**Acceptance:** Compared against the approved master color standard under **D65** light.
Color is **never** judged from memory or against a previous production part.

## 4. Limit samples

Physical limit samples ("worst acceptable") are maintained for each part and each applicable
defect type at the cell's sample board.

- Limit samples are approved by the Quality Manager and, where the customer owns the print,
  by the customer.
- They are **replaced every 12 months** or sooner if they yellow, warp, or become damaged —
  an aged limit sample silently loosens the standard over time.
- A defect judged more severe than the limit sample is a reject. When there is no limit
  sample for a defect type, the part is escalated to QC, **not** passed by the operator.

## 5. When in doubt

**When in doubt, quarantine and escalate — never pass.** An operator is never disciplined
for escalating a part that turns out to be good. Passing a doubtful part is the failure mode
that reaches the customer.

## 6. Related documents

- MNT-004 — Resin Drying and Conveying System Service
- MNT-005 — Chiller and Mold Temperature Control
- QC-002 — First Article Inspection
- QC-003 — In-Process Inspection and Statistical Process Control
- QC-005 — Nonconforming Material Control
