---
doc_id: MNT-005
title: Chiller and Mold Temperature Control — TCU-90 and Central Loop
category: maintenance
subcategory: auxiliary_equipment
equipment: [TCU-90, chiller_loop, cooling_tower]
applies_to: [maintenance_tech, process_tech]
revision: "2.8"
effective_date: 2026-05-11
review_due: 2028-05-11
owner: Maintenance Manager
status: active
supersedes: "2.7"
related_docs: [SAF-001, SAF-004, MNT-002, MNT-003, QC-003]
keywords: [chiller, tcu, mold temperature, cooling, water, delta t, glycol, scale, fouling, flow rate, warp, cycle time]
source: synthetic_demo_corpus
classification: internal_demo
contains_pii: false
---

# MNT-005 — Chiller and Mold Temperature Control

## 1. System overview

Plant 4 runs three water circuits. Confusing them is a common source of misdiagnosis.

| Circuit | Medium | Supply temp | Serves |
|---|---|---|---|
| **Chilled water** | 30% propylene glycol | 10 °C | Mold cooling via TCUs, hydraulic oil coolers, throat cooling |
| **Tower water** | Treated water | 27–32 °C (ambient dependent) | Chiller condensers only |
| **TCU circuit** | Treated water, closed | 20–120 °C per job | Individual mold circuits |

Barrel **throat cooling is always on** whenever the barrel is hot, regardless of the job.
Loss of throat cooling causes material to soften and bridge in the feed throat, which
presents as starved feed and erratic shot size.

## 2. TCU-90 operating parameters

| Parameter | Value |
|---|---|
| Temperature range | 20–120 °C (water) |
| Control accuracy | ±1 °C at setpoint |
| Max working pressure | 4 bar |
| Target flow, per circuit | Turbulent flow — Reynolds number above 4,000 |
| Max delta-T across the tool | **3 °C** (per MNT-002 §6 startup check) |

Delta-T across a tool circuit larger than 3 °C means the flow is too low — nearly always
scale, a partially closed valve, or a kinked jumper. Low flow produces uneven cooling,
which shows up in QC as **dimensional drift and warp within a single cavity**, not as an
obvious cooling alarm. This is why QC-003 requires checking water before adjusting process.

## 3. Troubleshooting

| Symptom | Check in order |
|---|---|
| Mold will not reach setpoint | TCU heater elements; flow blocked; setpoint vs. job sheet; leaking circuit |
| Mold overshoots setpoint | Cooling solenoid stuck open; oversized circuit; failed thermocouple |
| High delta-T across the tool | Scale in circuit; valve partly closed; jumper kinked; circuits plumbed wrong (MNT-002 §5) |
| Cycle time creeping up | Chilled water supply temp rising; condenser fouling; mold scale |
| Chiller short-cycling | Low load; low refrigerant charge; flow switch fault |
| Chilled water temp high | Condenser fouled; tower fan fault; low glycol level; excess plant load |
| Water in hydraulic oil | Heat exchanger tube leak — see MNT-003 §5 |
| Rust-colored water at TCU | Scale/corrosion; check treatment program (§4) |

## 4. Water treatment

Untreated water scales mold cooling channels. A **1 mm scale layer** in a cooling channel can
increase cycle time by 10% or more and is effectively invisible from outside the tool.

| Test | Frequency | Target |
|---|---|---|
| pH, chilled loop | Weekly | 8.0–9.0 |
| Glycol concentration | Monthly | 30% ±3% |
| Conductivity, tower | Weekly | Per treatment vendor program |
| Biological (dip slide), tower | Monthly | Below vendor action level |
| Full loop water analysis | Quarterly | Vendor report retained 3 years |

Tower water is treated for biological growth. Handle tower water as a potential inhalation
hazard: **no compressed-air blow-down of tower components or condenser tubes**, which
aerosolizes the water. Use mechanical cleaning or a wet method.

Mold circuits are descaled on condition — when delta-T exceeds 3 °C and flow restriction is
confirmed — using the tool room's circulating descale unit, never by drilling or rodding a
cooling channel.

## 5. Maintenance schedule

### Daily *(no LOTO)*
- Log chilled water supply and return temperatures.
- Log TCU setpoints against the job setup sheet.
- Visual check for leaks at jumpers and manifolds.

### Weekly
- Chilled loop pH and tower conductivity.
- Clean TCU strainers.
- Check chiller and tower sight glasses and levels.

### Monthly
- Glycol concentration.
- Inspect and clean the tower basin and strainer.
- Verify flow switches and low-level cutouts function.

### Annually
- Condenser tube cleaning.
- Full refrigerant leak check by a certified technician.
- Calibrate TCU temperature sensors against a reference (record per QC-006).
- Replace the tower fill if degraded.

## 6. Safety

- **The chilled loop contains 30% propylene glycol** — a slip hazard when spilled and subject
  to the spill handling in SAF-004 §5. Never discharge glycol to a floor drain.
- LOTO per SAF-001 before opening any TCU panel, pump, or refrigeration circuit. The chiller
  has both an electrical disconnect and a refrigerant circuit; only certified technicians open
  the refrigerant side.
- **TCU water above 100 °C is under pressure.** Never crack a fitting or disconnect a jumper
  on a hot circuit — allow it to cool below 40 °C and depressurize first. Scald injuries from
  hot TCU jumpers are treated as thermal burns per SAF-003 §7.
- Tower work at height requires fall protection and a work permit.

## 7. Related documents

- SAF-001 — Lockout/Tagout
- SAF-004 — Chemical Handling and Spill Response
- MNT-002 — Mold Change Procedure
- MNT-003 — Hydraulic System Troubleshooting
- QC-003 — In-Process Inspection and Statistical Process Control
