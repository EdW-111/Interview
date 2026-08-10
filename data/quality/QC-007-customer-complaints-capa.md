---
doc_id: QC-007
title: Customer Complaints and Corrective Action (CAPA)
category: quality
subcategory: capa
equipment: [QC_lab, plant_wide]
applies_to: [quality_tech, floor_supervisor, process_tech, maintenance_tech]
revision: "3.1"
effective_date: 2026-03-30
review_due: 2028-03-30
owner: Quality Manager
status: active
supersedes: "3.0"
related_docs: [QC-001, QC-004, QC-005, QC-006, MNT-003]
keywords: [complaint, capa, corrective action, 8d, root cause, containment, five why, fishbone, effectiveness, recall, supplier, escalation]
source: synthetic_demo_corpus
classification: internal_demo
contains_pii: false
---

# QC-007 — Customer Complaints and Corrective Action

## 1. Response clock

A customer complaint starts a clock that does not pause for shifts or weekends.

| Milestone | Due |
|---|---|
| Acknowledge receipt to the customer | **24 hours** |
| Containment actions in place (plant, WIP, warehouse, in-transit, customer site) | **24 hours** |
| Initial written response with containment and interim protection | **3 business days** |
| Root cause identified and verified | **15 business days** |
| Permanent corrective action implemented | **30 business days** |
| Effectiveness verification closed | **90 days** after implementation |

Extensions require the customer's agreement in writing. **Containment is never extended** —
if root cause is still unknown at 24 hours, containment stays in force and typically escalates
to 100% inspection.

## 2. Containment first, always

Before any investigation begins:

1. Quarantine suspect stock at the plant per **QC-005 §2**.
2. Bound the population per **QC-005 §3** — back to the last known-good verification point.
3. Determine what has shipped, to whom, and when, using the internal lot ID traceability
   established at **QC-001 §7**. This is what makes a targeted containment possible instead
   of a blanket one.
4. Notify the customer of affected shipments — dates, quantities, lot IDs.
5. Institute 100% inspection or a certified-stock process for continuing shipments, with
   clear visual identification (a certified-lot label) so the customer can tell protected
   stock from suspect stock.

Never ship unprotected product into an open complaint to keep a line running. If supply is
at risk, that is a conversation with the customer, not a decision made on the floor.

## 3. Root cause

Two questions must be answered, not one:

- **Occurrence** — why was the defect made?
- **Escape** — why did our inspection not catch it?

A CAPA that only fixes occurrence leaves the detection gap open for the next defect. Both
require a corrective action.

Use 5-Why with a fishbone (Man, Machine, Material, Method, Measurement, Environment) to
structure the search. A root cause is only accepted when the team can **turn the defect on
and off** — reproduce it by reintroducing the suspected cause, and eliminate it by removing
that cause.

**"Operator error" is not a root cause.** It is a symptom. Ask why the process permitted the
error: was the instruction unclear, the limit sample missing (QC-004 §4), the gage
inadequate (QC-006 §5), the training absent, or the correct action harder than the wrong one?

Common verified root causes at Plant 4, for orientation:

| Defect reported | Frequently traced to |
|---|---|
| Splay / brittleness | Under-dried material — dew point or residence time (MNT-004) |
| Warp, dimensional drift | Cooling — delta-T over 3 °C or circuits mis-plumbed (MNT-005, MNT-002 §5) |
| Contamination, black specks | Changeover purge, regrind, or conveying line debris (MNT-004 §5) |
| Flash | Tool parting-line condition; masked by raising tonnage |
| Mixed or wrong parts | Changeover discipline; missing last-off check (QC-002 §5) |

## 4. Corrective action and verification

Actions are rated by how robust they are. Prefer the top of this list:

1. **Error-proofing (poka-yoke)** — the defect becomes physically impossible.
2. **Automated detection** — the process detects and stops itself.
3. **Process or design change** — removes the cause.
4. **Procedure change plus training** — depends on human compliance; weakest, and never
   sufficient on its own for a safety characteristic.

Every action needs an owner, a due date, and objective evidence of implementation.

**Effectiveness verification at 90 days** asks for data, not opinion: scrap rate at the defect
code, SPC behavior, audit results, absence of recurrence. A CAPA closed without data is not
closed. If the defect recurs after closure, the CAPA is reopened at a higher escalation level —
it is not logged as a new complaint.

## 5. Supplier-caused issues

Where the cause is purchased material, raise a supplier corrective action request with the same
clock and the same occurrence/escape requirement. Move the supplier to 100% incoming inspection
until effectiveness is verified — this cancels any skip-lot status under **QC-001 §5**.

Repeat failures of the same mode trigger a supplier escalation review with Purchasing and,
where warranted, a supplier audit.

## 6. Read-across

Every closed CAPA is assessed for **read-across**: does the same failure mode exist on other
tools, presses, materials, or programs? A CAPA applied to only the complaining customer's part
number, when the same tool family or process runs elsewhere, is an incomplete CAPA.

## 7. Internal escalation

The following are handled as CAPAs even with no customer complaint:

- Any safety characteristic nonconformance
- The same defect recurring three times in 90 days (QC-005 §6)
- Product shipped nonconforming, discovered internally
- A records-integrity finding under QC-003 §5
- A repeated equipment failure with quality impact (MNT-003 §7)

## 8. Records

CAPA records are retained **7 years**, consistent with QC-002 §6 and QC-005 §6, and include
the complaint, containment evidence, investigation, root cause with verification, actions with
evidence of implementation, and the effectiveness data.

## 9. Related documents

- QC-001 — Incoming Material Inspection and Release
- QC-004 — Visual Defect Standards
- QC-005 — Nonconforming Material Control
- QC-006 — Gage Calibration and Measurement System Analysis
