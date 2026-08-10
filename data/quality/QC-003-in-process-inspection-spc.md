---
doc_id: QC-003
title: In-Process Inspection and Statistical Process Control
category: quality
subcategory: process_control
equipment: [TX-250, TX-500, QC_lab]
applies_to: [operator, quality_tech, process_tech, floor_supervisor]
revision: "5.1"
effective_date: 2026-05-04
review_due: 2028-05-04
owner: Quality Manager
status: active
supersedes: "5.0"
related_docs: [MNT-005, MNT-006, QC-002, QC-004, QC-005, QC-006]
keywords: [spc, control chart, cpk, ppk, subgroup, out of control, western electric, sampling frequency, in process, capability, trend]
source: synthetic_demo_corpus
classification: internal_demo
contains_pii: false
---

# QC-003 — In-Process Inspection and Statistical Process Control

## 1. Sampling plan

| Characteristic class | Sample | Frequency |
|---|---|---|
| CTQ / safety characteristic | Subgroup of **n = 5** | Every **30 minutes** |
| Major dimension | Subgroup of n = 5 | Every 2 hours |
| Visual (QC-004) | 5 parts | Every 30 minutes |
| Part weight | 5 parts | Every hour |
| Full layout (all dimensions) | 1 part per cavity | Start of shift and end of run |

On multi-cavity tools, subgroups are drawn **from the same cavity**. Mixing cavities inside
one subgroup inflates within-subgroup variation, widens the control limits, and hides real
process shifts — it is the most common SPC error in molding. Rotate which cavity is charted,
or chart each cavity separately, as the control plan specifies.

Sampling frequency doubles for the first 2 hours after any FAI approval, any process
adjustment, or any material lot change.

## 2. Capability requirements

| Characteristic | Requirement | If not met |
|---|---|---|
| Safety / CTQ characteristic | **Cpk ≥ 1.67** | 100% inspection until capability is restored |
| Major characteristic | **Cpk ≥ 1.33** | Increase sampling; open an improvement action |
| New tool at PPAP | **Ppk ≥ 1.67** on all CTQ | Tool not approved for production |

Capability is calculated on a minimum of **25 subgroups (125 measurements)** from a stable
process. **Capability calculated on an out-of-control process is meaningless** — establish
statistical control first, then assess capability.

Cpk uses within-subgroup variation (short-term); Ppk uses total variation (long-term). A
large gap between Cpk and Ppk indicates the process is drifting between subgroups — look at
material lot changes, shift changes, and mold temperature stability (MNT-005 §2).

## 3. Out-of-control rules

A point triggering **any** of these signals is an out-of-control condition requiring action:

1. Any point outside a control limit (±3σ).
2. **7 consecutive points** on one side of the centerline.
3. **7 consecutive points** trending steadily up or down.
4. 2 of 3 consecutive points beyond 2σ on the same side.
5. 4 of 5 consecutive points beyond 1σ on the same side.
6. 14 consecutive points alternating up and down.

**Control limits are not specification limits.** A process can be inside spec and out of
control — that means it is unpredictable and will eventually make bad parts. Both are acted on.

Control limits are recalculated only when the process is deliberately and permanently
changed, with Quality Manager approval. Recalculating limits to make a signal disappear is
falsification of quality records.

## 4. Operator response to an out-of-control signal

1. **Stop and contain.** Quarantine everything produced back to the last known-good subgroup.
   Apply a red hold tag (QC-005).
2. **Notify** the supervisor and the process technician immediately. Do not adjust the
   process yourself.
3. **Check the measurement before the process.** Re-measure with a second, calibrated gage.
   A large share of "process shifts" are gage or method problems (QC-006).
4. **Investigate in this order** — cheapest and most likely first:
   - Material: correct grade? correct lot? dryer dew point and residence time (MNT-004)?
   - Water: TCU at setpoint? delta-T across the tool within 3 °C (MNT-005 §2)?
   - Machine: any active alarms or recent faults (MNT-006)? shot weight within ±2%?
   - Tool: flash, vent condition, wear, sticking?
   - Process: only after the above are cleared.
5. **One change at a time**, then re-sample a full subgroup. Changing several parameters at
   once makes the cause unknowable and destroys the process record.
6. **Document** the signal, the investigation, the change made, and the verification result
   on the process adjustment log.

## 5. Prohibited practices

- Adjusting the process based on a **single** measurement rather than a subgroup — this is
  over-adjustment (tampering) and provably increases variation.
- Re-measuring until a passing value appears and recording only that one.
- Recording expected values rather than measured values.
- Writing up a shift's readings at end of shift from memory.
- Continuing to run while an out-of-control signal is open and unresolved.

Any of these is a records-integrity issue and is escalated to the Quality Manager directly,
outside the normal reporting line.

## 6. Process adjustment authority

| Change | Who may authorize |
|---|---|
| Within the setup sheet's approved window | Process technician |
| Outside the approved window | Process Engineer + new FAI (QC-002 §1) |
| Cooling / TCU setpoint change | Process Engineer + new FAI |
| Material grade or supplier change | Quality Manager + customer notification if the print requires it |
| Cycle time reduction | Process Engineer + capability re-verification |

Every out-of-window change requires a fresh FAI before production resumes. The setup sheet
is then updated — an undocumented "known good" setting that lives only in a technician's
head is a single point of failure for the plant.

## 7. Charting and data retention

Control charts are maintained at the cell, visible to the operator, and updated in real time
as subgroups are taken. Charts are reviewed by the supervisor at least once per shift and
signed.

SPC data and control charts are retained for **7 years**, matching the FAI retention in
QC-002 §6.

## 8. Related documents

- MNT-005 — Chiller and Mold Temperature Control
- MNT-006 — Alarm and Fault Code Reference
- QC-002 — First Article Inspection
- QC-004 — Visual Defect Standards
- QC-005 — Nonconforming Material Control
- QC-006 — Gage Calibration and Measurement System Analysis
