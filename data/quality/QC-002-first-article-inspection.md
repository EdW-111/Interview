---
doc_id: QC-002
title: First Article Inspection (FAI) and Production Approval
category: quality
subcategory: first_article
equipment: [TX-250, TX-500, QC_lab, CMM]
applies_to: [quality_tech, process_tech, floor_supervisor]
revision: "4.3"
effective_date: 2026-04-13
review_due: 2028-04-13
owner: Quality Manager
status: active
supersedes: "4.2"
related_docs: [SAF-005, MNT-002, QC-003, QC-004, QC-005, QC-006]
keywords: [fai, first article, first off, approval, setup approval, cmm, dimensional, layout, control plan, last off, ppap]
source: synthetic_demo_corpus
classification: internal_demo
contains_pii: false
---

# QC-002 — First Article Inspection and Production Approval

## 1. When an FAI is required

An FAI is mandatory before production starts in **every** one of these cases:

- After any mold change or new job setup (MNT-002 §6)
- After a tool repair, tool modification, or cavity block change
- After a material grade or supplier lot change on a dimensionally critical part
- After a press change (same tool moved to a different press)
- After any process parameter change outside the approved setup sheet window
- At the **start of every shift** on continuously running jobs
- After any unplanned stoppage longer than **30 minutes**
- After a mold temperature control unit or cooling configuration change (MNT-005)

There is no "we ran this yesterday" exemption. If any item above applies, the FAI is required.

## 2. Sample preparation

1. The process technician runs **10 stabilization shots to scrap** after startup.
   Parts from stabilization shots are never submitted — the process is not yet at steady state.
2. Take **5 consecutive parts** (all cavities on a multi-cavity tool).
3. Label each part with **cavity number**, date, time, press, and shift. Unlabeled samples
   are rejected by the lab, because a dimensional failure that cannot be tied to a cavity
   cannot be corrected.
4. Allow parts to reach ambient before dimensional measurement. Semi-crystalline materials
   (PA66, PBT, POM) continue shrinking after ejection.

### Conditioning before measurement

| Material class | Minimum conditioning before dimensional check |
|---|---|
| Amorphous (PC, ABS) | 1 hour at ambient |
| Semi-crystalline (PA66, PBT, POM, PP) | **24 hours** at ambient, or per the control plan |

Where a 24-hour hold would stop production, the control plan may authorize a **1-hour
provisional check** to release production at risk, with the 24-hour full layout following.
Product made in the interim is traceable and held until the full layout passes.

## 3. What is inspected

Per the part's **control plan and FAI dimensional layout**:

| Characteristic type | Requirement |
|---|---|
| Critical-to-quality (CTQ) / safety characteristics | 100% of listed dimensions, all cavities, on all 5 parts |
| Major dimensions | All listed, all cavities, minimum 1 part per cavity |
| Visual / cosmetic | Against QC-004 limit samples, all 5 parts |
| Functional (gauge, fit, assembly check) | Per control plan |
| Weight (part and shot) | All 5 parts; compare to the approved master value |
| Material and lot traceability | Recorded from the release tag (QC-001 §7) |

Part weight is the cheapest and fastest process check available. A shot weight more than
**±2%** from the approved master is investigated before any dimension is trusted — it usually
means a process, material, or check-ring problem rather than a tool problem.

## 4. Disposition

| Result | Action |
|---|---|
| **Approved** | QC signs the FAI record; the green approved-sample board at the cell is updated; production starts |
| **Approved with deviation** | Requires Quality Manager signature and a documented, time-boxed deviation with customer approval where the print is the customer's |
| **Rejected** | Process technician adjusts; a **new** full FAI is run from Section 2. Parts made are scrap |

**Production may not run on a pending FAI.** If the press runs while the FAI is in the lab,
everything produced is held under QC-005 until disposition. This is the single most common
process discipline failure found in internal audits.

The approved first-article sample is retained at the cell in the sample board for the
duration of the run and is the operator's visual reference.

## 5. Last-off sample

At the end of a run, before the tool is pulled, take a **last-off sample** of 3 consecutive
parts and label them. The last-off sample:

- Confirms the process was still capable at end of run,
- Provides evidence if a customer complaint arrives later (QC-007),
- Is the reference for the tool's condition tag (MNT-002 §8).

Last-off samples are retained for **12 months**, or the customer's specified retention period
if longer.

## 6. Records

The FAI record contains: part number and revision, tool number, press, material and internal
lot ID, date/time/shift, all measured values (actual numbers, never "OK"), gage IDs used
(QC-006), the technician's and approver's names, and the disposition.

Recording "OK" or a checkmark instead of an actual measured value makes the record
worthless for later investigation and is treated as an incomplete record.

FAI records are retained for **7 years**, or per the customer contract if longer.

## 7. Related documents

- MNT-002 — Mold Change Procedure
- QC-003 — In-Process Inspection and Statistical Process Control
- QC-004 — Visual Defect Standards
- QC-005 — Nonconforming Material Control
- QC-006 — Gage Calibration and Measurement System Analysis
