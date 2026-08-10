---
doc_id: MNT-006
title: Alarm and Fault Code Reference — TX Series and Auxiliaries
category: maintenance
subcategory: diagnostics
equipment: [TX-250, TX-500, AD-300, TCU-90, PR-12, GR-40]
applies_to: [operator, process_tech, maintenance_tech, floor_supervisor]
revision: "7.0"
effective_date: 2026-06-01
review_due: 2028-06-01
owner: Maintenance Manager
status: active
supersedes: "6.4"
related_docs: [SAF-001, SAF-002, MNT-001, MNT-003, MNT-004, MNT-005]
keywords: [fault code, alarm, error code, e-code, diagnostics, reset, troubleshooting, hmi, robot, dryer alarm]
source: synthetic_demo_corpus
classification: internal_demo
contains_pii: false
---

# MNT-006 — Alarm and Fault Code Reference

## 1. How to use this document

Codes are grouped by prefix. Each entry gives the meaning, the first checks, and who may
clear it.

**Clearance authority:**

| Level | Who | Codes |
|---|---|---|
| **A** | Operator may reset after correcting the obvious cause | Process and material alarms |
| **B** | Process technician or maintenance | Machine faults |
| **C** | Maintenance only, with LOTO | Safety and drive faults |

**No alarm is ever cleared by cycling the main disconnect to make it go away.** If a code
returns after a reset, it is a real fault — raise a work order rather than resetting again.
Repeated resets of the same code within a shift is itself a reportable condition.

## 2. Safety faults — `E-1xx` (clearance level C)

| Code | Meaning | First checks |
|---|---|---|
| E-101 | Operator gate open during cycle | Gate closed and latched; actuator key aligned; switch damage |
| E-102 | Light curtain blocked or misaligned | Obstruction; lens dust; alignment after mold change (MNT-002 §6) |
| E-103 | Safety relay contact mismatch | Relay fault, wiring. **Do not bypass.** SAF-002 §4 |
| E-104 | E-stop active | Identify which device; reset at the device, then at the HMI |
| E-105 | Rear/purge gate open | Gate position; purge tray in place |
| E-106 | Robot fence door open | Door closed; interlock function |
| E-107 | Safety circuit response time out of range | **Cell stays down.** P1 work order, SAF-002 §6 |

Any `E-1xx` that does not clear after correcting the obvious cause is a **P1** work order.
The cell does not run production with an active or intermittent safety fault.

## 3. Hydraulic and drive faults — `E-2xx` (level B, C where noted)

| Code | Meaning | First checks |
|---|---|---|
| E-201 | Pump motor overload | Reset overload; check oil viscosity when cold; MNT-003 §2 |
| E-202 | System pressure below setpoint | Oil level; relief setting; transducer; MNT-003 §3 |
| E-203 | Oil temperature high (> 60 °C) | Cooler fouling; chilled water flow (MNT-005); relief dumping |
| E-204 | Oil level low | **Do not top up and walk away** — find the leak (MNT-003 §4) |
| E-205 | Return filter differential high | Change filter; send oil sample (MNT-001 §6) |
| E-206 | Accumulator pre-charge low | Level C. LOTO + bleed per SAF-001 §5 before service |
| E-207 | Proportional valve feedback fault | Level C. Connector, coil resistance, contamination |

## 4. Clamp and mold faults — `E-3xx` (level B)

| Code | Meaning | First checks |
|---|---|---|
| E-301 | Mold protect trip | Part or sprue stuck in mold; ejector not returned; 3 mm sensitivity setting |
| E-302 | Clamp did not reach position in time | Mechanical obstruction; low pressure; position sensor |
| E-303 | Ejector overload | Part sticking; check release, draft, and mold surface finish |
| E-304 | Tie-bar strain imbalance | Level C. Platen parallelism; MNT-001 §5 |
| E-305 | Mold height/tonnage setup fault | Re-run mold height setup after changeover |

**E-301 is the most frequent fault in Plant 4.** Clearing it requires opening the mold area,
which requires **LOTO per SAF-001**. There is no exception for "just grabbing the part."
Every year this is the fault most often associated with hand-injury near-misses in the industry.

## 5. Barrel and heat faults — `E-4xx` (level B)

| Code | Meaning | First checks |
|---|---|---|
| E-401 | Zone over temperature | Thermocouple; contactor welded closed; controller tuning |
| E-402 | Zone under temperature / heat-up timeout | Failed band; open thermocouple; loose terminal |
| E-403 | Thermocouple open or reversed | Polarity at terminal; broken lead |
| E-404 | Cold start inhibit active | Barrel below minimum; wait for soak. **Do not override** — turning the screw in a cold barrel will break it |
| E-405 | Hot runner zone fault | Hot runner controller; zone wiring; see MNT-002 for cable seating |

## 6. Auxiliary faults

### Dryer — `D-xx` (level A/B)
| Code | Meaning | First checks |
|---|---|---|
| D-01 | Dew point above alarm (−25 °C) | Regen cycle; desiccant condition; MNT-004 §3. **Verify moisture before molding** |
| D-02 | Hopper temperature deviation | Heater; thermocouple; setpoint vs. MNT-004 §2 |
| D-03 | Process filter ΔP high | Clean/replace filter |
| D-04 | Regen temperature out of band | Regen heater and thermocouple |
| D-05 | Low material level | Refill; confirm residence time before restart (MNT-004 §4) |

### TCU / chiller — `T-xx` (level A/B)
| Code | Meaning | First checks |
|---|---|---|
| T-01 | Setpoint not reached | Heater; flow; MNT-005 §3 |
| T-02 | Flow low | Strainer; valve position; scale in mold circuit |
| T-03 | High pressure | Blocked return; closed valve |
| T-04 | Chilled water supply high | Condenser fouling; tower; MNT-005 §3 |

### Robot PR-12 — `R-xx` (level B)
| Code | Meaning | First checks |
|---|---|---|
| R-01 | Part not detected at EOAT | Vacuum level; suction cup wear; sensor |
| R-02 | Axis position error | Obstruction; belt tension; home the robot |
| R-03 | Vacuum low | Cup wear, leak, filter, generator |
| R-04 | Interference / mold not clear | Timing signals; mold-open position |

## 7. When a code is not listed

1. Capture a photo of the HMI alarm screen including the raw code and timestamp.
2. Check the alarm history for what preceded it — the first alarm in a cascade is the real one.
3. Raise a work order with the code, cell, tool, material, and what changed recently.
4. Do not clear the alarm history before maintenance has seen it.

## 8. Related documents

- SAF-001 — Lockout/Tagout
- SAF-002 — Machine Guarding and Interlock Verification
- MNT-003 — Hydraulic System Troubleshooting
- MNT-004 — Resin Drying and Conveying System Service
- MNT-005 — Chiller and Mold Temperature Control
