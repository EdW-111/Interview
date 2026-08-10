---
doc_id: QC-006
title: Gage Calibration and Measurement System Analysis
category: quality
subcategory: metrology
equipment: [QC_lab, CMM, torque_wrenches, moisture_analyzer]
applies_to: [quality_tech, maintenance_tech, process_tech]
revision: "3.5"
effective_date: 2025-11-17
review_due: 2027-11-17
owner: Quality Manager
status: active
supersedes: "3.4"
related_docs: [QC-002, QC-003, QC-005, MNT-004, MNT-007]
keywords: [calibration, gage, msa, gage r&r, traceable, due date, caliper, cmm, moisture analyzer, torque wrench, bias, resolution]
source: synthetic_demo_corpus
classification: internal_demo
contains_pii: false
---

# QC-006 — Gage Calibration and Measurement System Analysis

## 1. Scope

Covers every device used to accept or reject product or to make a process decision: calipers,
micrometers, height gages, pin and thread gages, the CMM, force and torque devices, the
moisture analyzer, thermocouples and IR probes used for verification, and the dryer dew point
reference instrument.

A device used only for rough indication is stamped **"INDICATION ONLY"** and may never be
used to accept product. If it isn't calibrated, it can't accept.

## 2. Calibration intervals

| Device | Interval | Also recalibrate after |
|---|---|---|
| Calipers, micrometers, height gages | 12 months | Any drop or visible damage |
| Pin, plug, thread gages | 12 months | Visible wear or galling |
| CMM | 12 months, by external accredited lab | Any collision, relocation, or repair |
| **Torque wrenches** (MNT-007 §4) | **12 months** | Any drop or suspected overload |
| Moisture analyzer | 12 months | Any relocation or repair |
| Reference weights and gage blocks | 24 months | Any damage |
| Thermocouples / IR probes used for verification | 12 months | Any suspected drift |
| Dryer dew point reference instrument | 12 months | Deviation > 5 °C vs. field sensor (MNT-004 §4) |

All calibration is traceable to national standards, performed against a reference at least
**4× more accurate** than the device under test, and recorded with as-found and as-left values.

**As-found values are mandatory.** A device recorded only as-left destroys the ability to
judge whether prior measurements were valid.

## 3. Control of gages

- Every gage has a unique ID and a current calibration label showing the due date.
- **A gage past its due date is removed from service immediately** — not "used until the
  calibration comes back."
- Gages are checked out from the crib against the user's name; personal gages brought from
  home are prohibited.
- Damaged or suspect gages go to the quarantine shelf with a red tag, not back in the drawer.
- Gage resolution must be at most **10% of the tolerance** being measured. A 0.01 mm caliper
  cannot police a ±0.02 mm tolerance.

## 4. When a gage is found out of calibration

This is the trigger most often mishandled. On an out-of-tolerance as-found result:

1. Remove the gage from service and red-tag it.
2. Identify **every characteristic accepted with that gage since its last good calibration.**
3. Raise a nonconformance and contain that product per **QC-005 §3**.
4. Re-measure a representative sample with a known-good gage to assess actual risk.
5. If product has shipped, escalate to **QC-007** the same day.
6. Record the impact assessment even when the conclusion is "no product affected" — the
   reasoning is the record.

## 5. Measurement System Analysis

MSA is required for every gage on a control plan before it is used for production acceptance,
and repeated after any change to the gage, method, or fixturing.

### Gage R&R acceptance

| % Gage R&R (of tolerance) | Verdict |
|---|---|
| **≤ 10%** | Acceptable |
| **> 10% and ≤ 30%** | Conditionally acceptable — usable only with Quality Manager approval, based on the characteristic's criticality and the cost of improvement |
| **> 30%** | **Not acceptable** — the measurement system must be improved before use |

Standard study: **3 appraisers × 10 parts × 3 trials**, parts spanning the expected process
range, presented in random order, appraisers blind to prior readings.

Also assess **number of distinct categories (ndc)**: **ndc ≥ 5** is required. An ndc below 5
means the gage cannot resolve the process variation well enough to chart it.

For attribute (go/no-go and visual) inspection, run an **attribute agreement analysis**;
target ≥ 90% agreement both within and between appraisers. Poor agreement on visual defects
usually means the limit samples in QC-004 §4 are missing, aged, or ambiguous — fix the
standard before retraining the people.

## 6. Moisture analyzer method

The method referenced by QC-001 §5 and MNT-004:

1. Sample from the **dryer hopper discharge**, as close to the throat as possible — never
   from the top of the hopper or from the gaylord.
2. Seal the sample immediately in a moisture-tight vial. An open sample equilibrates with room
   air within minutes and reads high.
3. Test within **15 minutes** of sampling.
4. Run per the analyzer's programmed method for the material class.
5. Compare against the at-press limits in **MNT-004 §2**.
6. Record material, lot, dryer, hopper temperature, dew point at time of sampling, and result.

Vials come out of the oven above 120 °C — heat-resistant gloves are required (SAF-005 §2).

## 7. Related documents

- QC-002 — First Article Inspection
- QC-003 — In-Process Inspection and SPC
- QC-005 — Nonconforming Material Control
- MNT-004 — Resin Drying and Conveying System Service
- MNT-007 — Lubrication and Torque Specifications
