---
doc_id: SAF-002
title: Machine Guarding and Interlock Verification
category: safety
subcategory: machine_safeguarding
equipment: [TX-250, TX-500, PR-12, GR-40]
applies_to: [operator, floor_supervisor, maintenance_tech]
revision: "3.1"
effective_date: 2026-01-12
review_due: 2028-01-12
owner: EHS Manager
status: active
supersedes: "3.0"
related_docs: [SAF-001, SAF-007, MNT-001, MNT-006]
keywords: [guarding, light curtain, interlock, gate switch, two-hand control, muting, bypass, e-stop, safety circuit]
source: synthetic_demo_corpus
classification: internal_demo
contains_pii: false
---

# SAF-002 — Machine Guarding and Interlock Verification

## 1. Purpose

Define the guarding required on molding cells and the daily verification that safety
devices are functional.

## 2. Guarding required by cell

| Zone | Required safeguard | Standard |
|---|---|---|
| Operator-side mold area | Interlocked sliding gate + secondary light curtain | Category 3 / PL d |
| Non-operator side | Interlocked fixed gate | Category 3 / PL d |
| Rear (purge zone) | Interlocked gate, purge tray in place | Category 3 / PL d |
| Top of clamp | Fixed guard, tool-removable only | Fixed |
| Robot envelope | Perimeter fence + interlocked access door | Category 3 / PL d |
| Granulator GR-40 infeed | Fixed chute, minimum 900 mm reach distance | Fixed |

## 3. Daily pre-shift verification (operator)

Performed at the start of **every shift**, recorded on the cell's Shift Start checklist.

1. **Gate interlock** — With the machine in auto and the cycle stopped at mold-open, slide
   the operator gate open. The clamp must not close. Close the gate; the machine must
   **not** restart automatically — a deliberate cycle-start input is required.
2. **Light curtain** — Break the curtain with the supplied test rod (Ø30 mm). All beams
   must trip; the status lamp turns red and clamp motion is inhibited.
3. **E-stop** — Press one E-stop per shift on a rotating schedule (front, rear, robot
   pendant). Verify all motion stops and the fault must be manually reset.
4. **Robot fence door** — Open and confirm the robot goes to protective stop.

Any failure: **stop the cell, tag it out, notify the supervisor immediately.**
A cell with a failed safety device may not run production under any circumstance.

## 4. Prohibited practices

The following are terminable offenses at Plant 4:

- Taping, wiring, magnetizing, or otherwise defeating a gate switch.
- Placing an object in the light curtain to hold it clear.
- Running with a guard removed, propped, or with a missing interlock actuator key.
- Overriding a safety relay from the PLC or forcing a safety input online.

## 5. Authorized bypass for setup and troubleshooting

Limited bypass is permitted **only** in Setup mode, **only** by a trained setter or
maintenance technician holding the cell's setup key, and **only** while:

- Speed is limited to the mold-protect creep speed (≤ 25 mm/s clamp),
- The technician uses continuous hold-to-run enable on the pendant,
- No other person is inside the guard envelope,
- The setup key is retained on the technician's person, not left in the switch.

The setup key is signed out from the supervisor's cabinet and signed back in at end of
task. Keys left in machines are collected by EHS and treated as a reportable near-miss.

Setup mode is **not** a substitute for LOTO. Any work that puts a body part in the
clamp path or mold area requires full LOTO per SAF-001.

## 6. Safety circuit function testing (maintenance)

| Test | Interval | Performed by | Record |
|---|---|---|---|
| Gate interlock functional | Every shift | Operator | Shift Start checklist |
| Light curtain functional | Every shift | Operator | Shift Start checklist |
| Light curtain response time measurement | Annually | Maintenance / contractor | Form SAF-002-F1 |
| Safety relay contact integrity | Annually | Maintenance | Form SAF-002-F1 |
| E-stop full circuit (all devices) | Quarterly | Maintenance | Form SAF-002-F1 |
| Two-hand control anti-tie-down | Semi-annually | Maintenance | Form SAF-002-F1 |

## 7. Safety distance for light curtains

Minimum safety distance is recalculated whenever a curtain is moved, replaced, or when
stopping performance changes after a clamp valve or brake repair. The stopping performance
test must be repeated after any repair affecting clamp deceleration. Do not relocate a
curtain without an EHS-approved recalculation on Form SAF-002-F2.

## 8. Damaged or nuisance-tripping devices

A light curtain that trips intermittently is treated as a **failed** device, not a nuisance.
Common causes are misalignment after a mold change, resin dust on the lens, and vibration
from an adjacent cell. Clean the lens with the supplied optical wipe only; do not use
purge solvent or compressed air with oil carryover.

If the device still faults, tag out and raise a maintenance work order at priority **P2**
(see MNT-001, Section 7).

## 9. Related documents

- SAF-001 — Lockout/Tagout
- SAF-007 — Powered Industrial Trucks and Pedestrian Traffic
- MNT-001 — Injection Press Preventive Maintenance Schedule
- MNT-006 — Alarm and Fault Code Reference
