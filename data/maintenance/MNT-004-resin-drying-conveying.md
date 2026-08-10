---
doc_id: MNT-004
title: Resin Drying and Conveying System Service — AD-300
category: maintenance
subcategory: auxiliary_equipment
equipment: [AD-300, vacuum_conveying, GR-40]
applies_to: [maintenance_tech, process_tech, material_handler]
revision: "3.4"
effective_date: 2026-02-23
review_due: 2028-02-23
owner: Maintenance Manager
status: active
supersedes: "3.3"
related_docs: [SAF-003, SAF-004, MNT-001, QC-001, QC-006]
keywords: [dryer, desiccant, dew point, drying temperature, residence time, hopper, conveying, filter, moisture, splay, regen]
source: synthetic_demo_corpus
classification: internal_demo
contains_pii: false
---

# MNT-004 — Resin Drying and Conveying System Service

## 1. Why drying matters

Hygroscopic resins absorb atmospheric moisture. Moisture in the barrel flashes to steam and
produces **splay** (silver streaking), bubbles, brittleness, and — in condensation polymers
like PA, PET, and PBT — **irreversible molecular weight loss** that reduces part strength
even when the part looks acceptable.

Under-dried material is the most common single root cause of scrap at Plant 4. A splay
defect is a QC finding (QC-004) whose corrective action almost always lands here.

## 2. Drying parameters by material

These values are the plant standard and match the QC moisture acceptance limits in QC-006.

| Material | Drying temp | Min residence time | Target dryer dew point | Max moisture at press |
|---|---|---|---|---|
| PC (polycarbonate) | 120 °C | 4 h | −40 °C | **0.02%** |
| PA66 (nylon) | 80 °C | 4 h | −40 °C | **0.20%** |
| PBT | 120 °C | 4 h | −40 °C | **0.04%** |
| ABS | 80 °C | 3 h | −40 °C | **0.10%** |
| PP / PE | Not required (non-hygroscopic) | — | — | surface moisture only |
| POM (acetal) | 80 °C | 3 h | −40 °C | **0.10%** |

**Do not exceed the drying temperature.** Over-drying degrades PC and PA and can cause
yellowing, embrittlement, and volatile generation. Over-drying is not a safe error.

## 3. Dryer setpoints and alarms — AD-300

| Parameter | Setpoint | Alarm | Action |
|---|---|---|---|
| Dew point | −40 °C | **−25 °C** | Investigate desiccant/regen before running |
| Hopper temperature | Per §2 | ±5 °C | Stop and correct |
| Return air temperature | ≤ 65 °C | > 80 °C | Check hopper level; possible short-cycling |
| Regeneration temperature | 175–190 °C | outside band | Check regen heater and thermocouple |
| Process filter ΔP | < 0.5 kPa | > 1.5 kPa | Clean or replace filter |

**Material dried at an out-of-spec dew point must be verified by moisture test (QC-006)
before it is molded, or re-dried.** Do not assume a full drying cycle fixes it — a dryer with
failed desiccant will not reach spec no matter how long it runs.

## 4. Maintenance schedule

### Daily *(operator/process tech, no LOTO)*
- Read and log dew point, hopper temperature, and material level.
- Confirm the hopper is full enough to give the required residence time. **A partially full
  hopper cuts residence time proportionally** and is a silent cause of under-dried material.
- Check for hose damage and material leaks at couplings.

### Weekly *(maintenance)*
- Clean the process air filter and the aftercooler.
- Inspect and clean hopper sight glasses.
- Verify the closed-loop conveying receivers seal and dump correctly.
- Check the vacuum pump inlet filter.

### Monthly
- Verify dew point sensor reading against the portable reference instrument. Deviation > 5 °C
  → send sensor for calibration (QC-006 governs the calibration record).
- Inspect and clean the regeneration blower and heater.
- Inspect all hopper insulation for damage.

### Annually
- Desiccant condition assessment; replace if dew point performance has degraded.
- Full electrical inspection of heaters, contactors, and thermocouples.
- Verify hopper high-level and low-level sensors.

## 5. Conveying system

- Vacuum receivers are sequenced by the central controller; a single blocked line will
  starve downstream receivers. Symptom: intermittent low-level alarms at multiple cells.
- Check for **angel hair** (fine strands from material shearing on long horizontal runs) at
  every elbow and at the receiver screen. Angel hair blocks screens and contaminates parts.
- Clean the receiver screen at every material changeover, without exception.
- On a material or color change, purge the line and the receiver before conveying the new
  material. Residual material from the previous job is a contamination nonconformance
  (QC-005) and can trigger a customer complaint (QC-007).

## 6. Safety notes

- Hopper surfaces at 120 °C are **hot** by SAF-003 §2 and are labeled accordingly. Wear
  high-temperature gloves for any contact.
- **Drying hoppers are confined spaces.** No entry under any circumstance without an EHS
  entry permit — this includes reaching in through the top to clear a bridge. Use the
  external bridge-breaking port.
- Isolate the dryer per SAF-001 before opening any panel or the regen section. The regen
  heater holds heat well past shutdown; wait for the panel probe to read < 40 °C.
- Do not store aerosols or solvents near the dryer exhaust (SAF-004 §3).

## 7. Related documents

- SAF-003 — Hot Surface and Molten Polymer Burn Prevention
- SAF-004 — Chemical Handling and Spill Response
- QC-001 — Incoming Material Inspection
- QC-006 — Gage Calibration and Measurement System Analysis
