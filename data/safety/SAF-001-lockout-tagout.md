---
doc_id: SAF-001
title: Lockout/Tagout (LOTO) — Control of Hazardous Energy
category: safety
subcategory: energy_control
equipment: [TX-250, TX-500, AD-300, TCU-90, PR-12]
applies_to: [maintenance_tech, floor_supervisor, process_tech]
revision: "4.2"
effective_date: 2025-11-03
review_due: 2027-11-03
owner: EHS Manager
status: active
supersedes: "4.1"
related_docs: [SAF-002, SAF-003, MNT-002, MNT-003]
keywords: [loto, lockout, tagout, zero energy, isolation, accumulator, bleed down, group lockout, lock removal]
source: synthetic_demo_corpus
classification: internal_demo
contains_pii: false
---

# SAF-001 — Lockout/Tagout (LOTO)

## 1. Purpose

Establish the minimum requirements for isolating hazardous energy before any employee
performs service, maintenance, mold changes, or clearing of jams on production equipment
at Plant 4.

## 2. Scope

Applies to all molding cells, auxiliary equipment, resin conveying, granulators, and the
central chiller loop. Applies to Northgate employees and to contractors working under a
Northgate work permit.

**This procedure does not apply to** normal production operations, cycle-time adjustment
from the HMI, or purging performed from outside the guard envelope (see Section 9).

## 3. Energy sources present on a molding cell

| Energy type | Source | Isolation point | Verification method |
|---|---|---|---|
| Electrical | 480 V 3-phase main | Wall disconnect `DS-xx` at cell entry | HMI dark; test with meter at L1/L2/L3 |
| Hydraulic | Pump + accumulator | Pump breaker + accumulator bleed valve `BV-1` | Gauge `PG-1` reads 0 psi |
| Pneumatic | 90 psi shop air | Lockable ball valve `AV-1` at drop | Gauge `PG-2` reads 0 psi after bleed |
| Thermal | Barrel heaters, mold heat | Heater contactor via main disconnect | Surface probe < 40 °C (see SAF-003) |
| Gravity | Vertical mold half, robot arm | Mold safety strap / robot arm support stand | Physical restraint installed |
| Stored (spring) | Ejector return springs | Ejectors driven fully forward before shutdown | Visual: ejector plate at forward stop |

## 4. Required six-step sequence

1. **Notify** — Inform the cell operator and the shift supervisor. Log the cell in the
   LOTO board at the north aisle.
2. **Shut down** — Bring the press to a controlled stop using the HMI *Cycle Stop*, not
   E-stop, unless an emergency exists.
3. **Isolate** — Operate every isolation device listed in Section 3 for the work being done.
4. **Lock and tag** — Apply a personal red padlock and a completed danger tag to every
   isolation device. One lock per person per device. Tags must show name, date, and
   expected duration.
5. **Release stored energy** — Bleed the accumulator via `BV-1`. **Wait a minimum of
   5 minutes** and confirm `PG-1` reads **0 psi**. Bleed air at `AV-1`. Install mold safety
   strap if the mold is open.
6. **Verify** — Attempt to start the machine from the HMI (try-start), confirm no motion,
   then return the selector to OFF. Verify gauges and temperatures per the table above.

> A LOTO is not complete until Step 6 is performed. Try-start verification is the single
> most commonly skipped step in Plant 4 audits.

## 5. Press-specific isolation notes

### TX-250 (250 ton)
- Main disconnect is on the operator-side column, labeled `DS-04` through `DS-09`.
- Single accumulator, bleed valve behind the rear guard door.
- Screw drive is electric; no separate isolation needed beyond the main disconnect.

### TX-500 (500 ton)
- **Two** accumulators (clamp and injection). Both `BV-1A` and `BV-1B` must be bled.
  Confirm both `PG-1A` and `PG-1B` read 0 psi.
- Core-pull hydraulics have an independent manifold with its own lockable valve `HV-3`.
  This is frequently missed — core pulls can move even after the main accumulator is bled.
- Mold weight exceeds the manual-handling limit; see MNT-002 for crane requirements.

## 6. Group lockout

For jobs involving more than one person (typical mold change, any job crossing a shift):

- The **authorized lead** applies the primary lock and hangs a group lockout box at the cell.
- The key to the primary lock goes **into** the box.
- Every additional person applies a personal lock to the **box**, not to the machine.
- The box cannot be opened until every personal lock is removed, which cannot happen until
  every person has cleared the equipment.

## 7. Shift change continuity

Hazardous energy control must remain unbroken across a shift change. The outgoing lead and
the incoming lead perform a **face-to-face handoff at the cell**, walk the isolation points
together, and the incoming lead applies their lock **before** the outgoing lead removes theirs.
Energy isolation is never allowed to lapse, even momentarily.

## 8. Removing another employee's lock

Locks are personal property and are removed only by their owner. In the exceptional case
where the owner is unavailable (left site, unreachable):

1. Verify by physical inspection that the equipment is clear of personnel and safe to energize.
2. Make a documented attempt to contact the lock owner.
3. Obtain signatures from **both** the Plant Manager and the EHS Manager on
   **Form SAF-001-F2**.
4. Cut the lock. Notify the owner before they return to work.

No supervisor may authorize lock removal alone.

## 9. Minor servicing exception

Routine, repetitive tasks integral to production — sprue picking, purging from outside the
guard, adding colorant at the hopper — may be done without full LOTO **only if**:

- The task is listed in the cell's Alternative Measures sheet, **and**
- The interlocked guard and light curtain are verified functional that shift (SAF-002), **and**
- No body part enters the mold area or the clamp path.

Any task requiring the operator to reach past the tie bars requires full LOTO. There is no
"quick job" exemption.

## 10. Training and audit

- Authorized employee training is required before first use and **annually** thereafter.
- Affected-employee awareness training is required annually.
- EHS performs a **quarterly** periodic inspection of each energy control procedure and a
  documented observation of one LOTO per authorized employee per year.

## 11. Related documents

- SAF-002 — Machine Guarding and Interlock Verification
- SAF-003 — Hot Surface and Molten Polymer Burn Prevention
- MNT-002 — Mold Change Procedure
- MNT-003 — Hydraulic System Troubleshooting
