---
doc_id: MNT-003
title: Hydraulic System Troubleshooting
category: maintenance
subcategory: troubleshooting
equipment: [TX-250, TX-500]
applies_to: [maintenance_tech, floor_supervisor]
revision: "5.2"
effective_date: 2025-12-15
review_due: 2027-12-15
owner: Maintenance Manager
status: active
supersedes: "5.1"
related_docs: [SAF-001, SAF-004, SAF-005, MNT-001, MNT-006]
keywords: [hydraulic, pressure, pump, accumulator, leak, valve, oil temperature, cavitation, slow clamp, drift, pinhole, injection fluid]
source: synthetic_demo_corpus
classification: internal_demo
contains_pii: false
---

# MNT-003 — Hydraulic System Troubleshooting

## 1. Before you start

**LOTO per SAF-001 is mandatory before opening any hydraulic connection.** Hydraulic
troubleshooting frequently requires the system live to observe a symptom; when live
observation is genuinely necessary:

- Observe from **outside** the guard envelope only.
- Use gauges and the HMI diagnostic screen, not hands.
- Never crack a fitting, adjust a relief valve, or touch a hose on a pressurized system.

> **Injection injury warning.** A pinhole leak at 2,000+ psi can inject fluid through intact
> skin. The wound may look trivial and initially painless, but it is a **surgical emergency**.
> Never search for a leak with your hand — use a piece of cardboard held at arm's length.
> Any suspected fluid injection goes to the emergency room immediately, and the responder
> must be told it is a hydraulic injection injury. Bring the SDS.

## 2. Symptom → cause index

| Symptom | Likely causes (check in order) |
|---|---|
| Slow clamp close/open | Low oil level; clogged suction strainer; worn pump; relief set too low; internal valve leakage |
| Clamp will not build tonnage | Relief valve setting; pressure transducer fault; worn pump; internal cylinder bypass |
| Injection pressure low / short shots | Non-return valve wear; accumulator pre-charge low; proportional valve drift; check the process before the hydraulics |
| Erratic or jerky motion | Air in the system; contaminated proportional valve; sticking spool; low accumulator pre-charge |
| Oil temperature high (> 55 °C) | Cooler fouled; chilled water flow low (MNT-005); relief valve dumping continuously; excessive holding pressure |
| Oil temperature low (< 35 °C) | Cooler control valve stuck open; short cycle time; ambient |
| Loud pump whine / cavitation | Low oil level; clogged suction strainer; suction line air leak; oil too viscous when cold |
| Cylinder drift with machine stopped | Internal cylinder bypass; check valve leakage; load-holding valve failure |
| Foamy or milky oil | Water ingress (see §5); air entrainment via a suction leak |
| Repeated filter loading | Component wearing out — find it before it fails; send oil sample (MNT-001 §6) |

## 3. Pressure and temperature reference

| Parameter | Normal | Investigate | Stop |
|---|---|---|---|
| System pressure, TX-250 | 2,000–2,200 psi | outside ±10% | — |
| System pressure, TX-500 | 2,300–2,500 psi | outside ±10% | — |
| Oil temperature, operating | 40–55 °C | 55–60 °C | > 60 °C — stop and investigate |
| Reservoir level, cold | Between MIN/MAX | below MIN | below sight glass |
| Accumulator pre-charge | Per data plate | ±5% | — |
| Return filter ΔP indicator | Green | Amber | Red — change now |

Oil above 60 °C degrades rapidly and softens seals; every 10 °C above 60 °C roughly halves
oil life. Do not run production to the end of a shift with oil over 60 °C.

## 4. Leaks

Classify before dispatching:

- **Weeping** (damp film, no drip) — monitor, log in CMMS, address at next PM. **P4**.
- **Dripping** (forms drops, spots the floor) — work order **P3**, contain with a drip pan.
- **Running or spraying** — **P1**. Stop the press, isolate, clean per SAF-004 §5.

**Any leak reaching the floor is a slip hazard and requires cleanup before the cell resumes**,
regardless of leak severity classification.

A leak at the *same* fitting more than twice in 90 days is not a re-tighten job — replace the
hose or fitting and inspect for the root cause (vibration, abrasion, incorrect flare seating).
Recurring leaks show up in the SAF-004 spill log; cross-check that log monthly.

Hoses are replaced on condition **or at 5 years from the date code**, whichever comes first.
Record the date code of every hose installed.

## 5. Water in oil

Water content above 500 ppm (MNT-001 §6) means water is entering the system. Sources, in
order of likelihood at Plant 4:

1. Heat exchanger tube leak — chilled water at higher pressure than the oil side. Isolate the
   exchanger and watch whether water ingress stops.
2. Mold cooling leak with water running down a tie bar into the reservoir vent.
3. Reservoir breather saturated — condensation. Replace the desiccant breather.
4. Wash-down or a leaking overhead line above the reservoir.

Water in oil causes additive depletion, corrosion, and reduced film strength. Do not simply
change the oil; find the source first, or the new charge is contaminated within weeks.

## 6. Accumulator service

Accumulators store enough energy to move the clamp with the pump off. Before any accumulator
work: bleed via `BV-1`, wait **5 minutes**, and confirm `PG-1` reads **0 psi** (SAF-001 §5).
On the TX-500 there are **two** accumulators plus an independent core-pull manifold (`HV-3`)
that must be isolated separately.

Nitrogen charging is performed only with the correct charging rig and only by technicians
trained on it. **Never charge an accumulator with anything but dry nitrogen** — oxygen or
shop air in contact with hydraulic oil under pressure can cause an explosive dieseling event.

## 7. Escalation

Escalate to the Maintenance Manager, and involve the OEM service contract, when:

- Pump replacement is indicated, or
- Platen parallelism is out of tolerance after tie-bar work (MNT-001 §5), or
- The same fault recurs three times despite corrective action, or
- Any injection injury, fire, or reportable spill has occurred.

## 8. Related documents

- SAF-001 — Lockout/Tagout
- SAF-004 — Chemical Handling and Spill Response
- SAF-005 — PPE Requirements Matrix
- MNT-001 — Injection Press Preventive Maintenance Schedule
- MNT-006 — Alarm and Fault Code Reference
