---
doc_id: MNT-001
title: Injection Press Preventive Maintenance Schedule — TX-250 / TX-500
category: maintenance
subcategory: preventive_maintenance
equipment: [TX-250, TX-500]
applies_to: [maintenance_tech, floor_supervisor, process_tech]
revision: "6.1"
effective_date: 2026-01-05
review_due: 2028-01-05
owner: Maintenance Manager
status: active
supersedes: "6.0"
related_docs: [SAF-001, SAF-002, MNT-003, MNT-006, MNT-007]
keywords: [pm, preventive maintenance, schedule, interval, tie bar, platen, filter, oil analysis, work order, priority, cmms]
source: synthetic_demo_corpus
classification: internal_demo
contains_pii: false
---

# MNT-001 — Injection Press Preventive Maintenance Schedule

## 1. Scope

Covers the TX-250 (250 ton) and TX-500 (500 ton) hydraulic injection molding presses in
Bays 1–8. Auxiliary equipment schedules are in MNT-004 (dryers/conveying) and MNT-005
(chillers/TCUs).

**All PM work requires LOTO per SAF-001 before any guard is opened or any tool enters the
clamp area.** Inspection tasks that can be performed from outside the guard envelope with
the machine in a safe stopped state are marked *(no LOTO)*.

## 2. Daily — operator, start of shift

| Task | Accept criteria |
|---|---|
| Safety device checks *(no LOTO)* | Per SAF-002 §3 |
| Hydraulic oil level at sight glass *(no LOTO)* | Between MIN and MAX, cold |
| Visible leaks under press and at hose runs *(no LOTO)* | None. Any leak → work order + SAF-004 §5 |
| Oil temperature at operating condition *(no LOTO)* | 40–55 °C |
| Water manifold flow and return temps *(no LOTO)* | Per setup sheet, ±3 °C |
| Purge tray empty and in position *(no LOTO)* | Empty |
| Housekeeping around cell *(no LOTO)* | Aisles and exits clear (SAF-006 §8) |

## 3. Weekly — maintenance technician

| Task | Accept criteria |
|---|---|
| Clean cabinet air filters | No visible loading |
| Check and clean mold-area limit switches and prox sensors | Free of resin dust |
| Grease toggle pins and bushings per MNT-007 chart | Per lubrication chart |
| Verify ejector plate return and mold protect settings | No overtravel; mold protect trips on 3 mm obstruction |
| Inspect hoses at flex points | No abrasion, blistering, or weeping |
| Drain water separator on the air drop | Bowl clear |

## 4. 500 operating hours

| Task | Accept criteria |
|---|---|
| Hydraulic return filter — inspect differential indicator | Green. Replace if amber/red or at 2,000 h regardless |
| Oil sample for analysis | See §6 |
| Check tie-bar nut torque markings | Witness marks aligned |
| Barrel heater band amp draw, each zone | Within ±10% of nameplate; log values |
| Thermocouple response check, each zone | Reaches setpoint ±2 °C within 15 min |
| Clean and inspect purge tray and nozzle area | Free of carbonized resin |
| Verify accumulator pre-charge pressure | Per press data plate, ±5% |

## 5. 2,000 operating hours

| Task | Accept criteria |
|---|---|
| Replace hydraulic return and pressure filters | Regardless of indicator state |
| Replace cabinet air filters | — |
| Platen parallelism check | Within 0.10 mm across the platen face |
| Tie-bar strain balance measurement | Max deviation ≤ 5% between the four tie bars |
| Clamp toggle wear inspection | No measurable play at pins |
| Screw and non-return valve inspection (pull screw) | Flight wear within 0.20 mm of nominal OD |
| Full E-stop and safety circuit test | Per SAF-002 §6 |
| Robot EOAT and axis check | Per MNT-006 |

## 6. Oil analysis program

Samples are drawn every **500 hours** from the dedicated sample port on the return line
while the oil is at operating temperature and the pump is running — never from the reservoir
bottom or from a drain.

| Parameter | Target | Action limit |
|---|---|---|
| ISO cleanliness code | 18/16/13 or better | 20/18/15 → change filters, resample at 100 h |
| Water content | < 200 ppm | > 500 ppm → investigate cooler leak (MNT-005) |
| Viscosity @ 40 °C | 46 cSt nominal | ±10% → investigate contamination or wrong-grade top-up |
| TAN (acid number) | < 0.5 mg KOH/g | > 1.0 → schedule oil change |
| Particle count trend | Stable | Two consecutive rising codes → investigate before failure |

Rising water content on a press is the single most common early indicator of a mold cooling
or heat exchanger leak. Treat it as a lead, not a nuisance.

## 7. Work order priority definitions

| Priority | Definition | Response target |
|---|---|---|
| **P1** | Safety device failed, injury risk, or fire/spill hazard | Immediate; cell stops production |
| **P2** | Machine down, or a condition that will stop it within a shift | Same shift |
| **P3** | Degraded performance, quality risk, or scheduled PM overdue | Within 5 working days |
| **P4** | Cosmetic, convenience, or improvement request | Next planned shutdown |

A failed light curtain or gate interlock is **always P1**, never P2, regardless of production
pressure. The cell does not run until it is corrected.

## 8. PM compliance

- PM compliance target: **≥ 95%** of scheduled PMs completed within their window.
- The window is ±10% of the interval (e.g. a 500 h PM may be done between 450 h and 550 h).
- A PM deferred past its window requires Maintenance Manager approval and is logged as an
  exception in the CMMS with a written justification.
- All PM completion, readings, and part numbers used are recorded in the CMMS at the time of
  work — not batched at end of shift.

## 9. Related documents

- SAF-001 — Lockout/Tagout
- SAF-002 — Machine Guarding and Interlock Verification
- MNT-003 — Hydraulic System Troubleshooting
- MNT-006 — Alarm and Fault Code Reference
- MNT-007 — Lubrication and Torque Specifications
