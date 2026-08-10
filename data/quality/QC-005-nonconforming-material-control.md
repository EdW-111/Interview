---
doc_id: QC-005
title: Nonconforming Material Control and Containment
category: quality
subcategory: nonconformance
equipment: [all_cells, quarantine_cage, QC_lab]
applies_to: [operator, quality_tech, floor_supervisor, material_handler]
revision: "4.0"
effective_date: 2026-02-09
review_due: 2028-02-09
owner: Quality Manager
status: active
supersedes: "3.4"
related_docs: [QC-001, QC-002, QC-003, QC-004, QC-007, MNT-007]
keywords: [nonconforming, ncr, quarantine, red tag, containment, mrb, disposition, scrap, rework, sort, deviation, suspect]
source: synthetic_demo_corpus
classification: internal_demo
contains_pii: false
---

# QC-005 — Nonconforming Material Control

## 1. What counts as nonconforming

Any material or product that does not meet specification, **or whose conformance cannot be
demonstrated**. The second half matters: product made during an unresolved out-of-control
signal, during a pending FAI, or with an out-of-calibration gage is nonconforming even if it
measures good. Suspect product is handled exactly like known-bad product until proven otherwise.

## 2. Immediate containment

The person who finds the problem performs these steps before anything else:

1. **Stop** — do not keep producing into the defect.
2. **Red-tag** everything affected with the hold tag: part number, quantity, date, defect
   found, finder's name.
3. **Move to the quarantine cage** in the **NE corner** of the plant. Physically separated,
   not just marked. If it is too large to move, rope it off and tag it in place.
4. **Notify** the supervisor and QC within the shift.
5. **Bound the population** — see §3.

Red-tagged material may not be moved, reworked, shipped, or consumed by anyone except QC.

## 3. Bounding the affected population

Containment must extend back to the **last known-good verification point** and forward to the
present. Work outward from the defect:

| Trigger | Contain back to |
|---|---|
| SPC out-of-control signal | Last in-control subgroup (QC-003 §4) |
| Visual defect found at the cell | Last passing visual check |
| Failed FAI | The entire run since setup (QC-002 §4) |
| Metallic contamination | Last known-good check — **and quarantine the tool and press** (QC-004 §3) |
| Out-of-calibration gage discovered | All product accepted with that gage since its last good calibration (QC-006 §4) |
| Wrong-lot or expired material | The full run made on that lot (QC-001 §7) |
| Non-food-grade lubricant on a food-contact tool | The full run since the lubrication event (MNT-007 §1) |

Containment is **not** limited to the plant floor. Check WIP, the warehouse, in-transit stock,
and product already delivered. Anything already shipped escalates immediately to QC-007.

## 4. Material Review Board (MRB)

The MRB is Quality (chair), Manufacturing, and Engineering. It meets on demand and must
disposition every open nonconformance within **3 business days** of the red tag.

| Disposition | Meaning | Authority |
|---|---|---|
| **Scrap** | Destroyed and recorded | Quality tech |
| **Rework** | Restored to full spec by a defined, approved procedure | MRB, with written rework instruction |
| **Sort / 100% inspect** | Good separated from bad, criteria documented | MRB |
| **Use as is** | Accepted despite the deviation | **Quality Manager + customer approval** where the customer owns the print |
| **Return to supplier** | Purchased material rejected | Quality Manager + Purchasing |
| **Regrade** | Diverted to a lower-requirement program | Quality Manager |

"Use as is" is never granted by Manufacturing, never granted verbally, and never granted to
hit a shipping date. Customer-print deviations require the customer's written acceptance.

Rework requires a **written, approved rework instruction** before work starts, and reworked
product is re-inspected against the full original acceptance criteria — not just the reworked
feature. Undocumented rework is itself a nonconformance.

## 5. Scrap handling

Scrap is defaced or segregated so it cannot re-enter the flow. This matters most for parts
that look acceptable — a cosmetically fine part scrapped for a strength defect will be
picked back up if it is left loose in a bin.

Scrap is coded to a defect reason at the time of scrapping. Reason codes drive the weekly
Pareto review; miscoded scrap ("other") makes the plant blind to its own biggest losses.

Regrind of scrap back into production is permitted **only** where the part's control plan
allows it, at the allowed percentage, and never for scrap that was contaminated, burnt,
or of unknown material.

## 6. Records and escalation

Every nonconformance gets an NCR number, and the record retains: what, how many, where found,
containment boundary, disposition, approver, and verification that the disposition was carried
out. NCRs are retained **7 years**, matching QC-002 §6.

Escalate to QC-007 (CAPA) when any of these is true: product has shipped; the same defect
recurs three times in 90 days; scrap value on a single NCR exceeds the plant threshold; or a
safety-related characteristic is involved.

## 7. Related documents

- QC-001 — Incoming Material Inspection and Release
- QC-002 — First Article Inspection
- QC-003 — In-Process Inspection and SPC
- QC-004 — Visual Defect Standards
- QC-006 — Gage Calibration and Measurement System Analysis
- QC-007 — Customer Complaints and Corrective Action
