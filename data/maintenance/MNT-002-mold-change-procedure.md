---
doc_id: MNT-002
title: Mold Change Procedure
category: maintenance
subcategory: changeover
equipment: [TX-250, TX-500, overhead_crane, TCU-90]
applies_to: [maintenance_tech, process_tech, floor_supervisor]
revision: "4.0"
effective_date: 2026-04-06
review_due: 2028-04-06
owner: Maintenance Manager
status: active
supersedes: "3.5"
related_docs: [SAF-001, SAF-003, SAF-007, MNT-005, MNT-007, QC-002]
keywords: [mold change, changeover, setup, clamp, tie bar, crane, water lines, hot runner, first article, smed, tool]
source: synthetic_demo_corpus
classification: internal_demo
contains_pii: false
---

# MNT-002 — Mold Change Procedure

## 1. Scope and roles

A mold change is a **two-person minimum** job on every press at Plant 4. Roles:

- **Setter (lead)** — owns the LOTO, directs the sequence, signs the changeover record.
- **Assistant** — rigging, water lines, staging.
- **Process technician** — startup, process parameters, first-article submission.
- **Crane operator / rigger** — required for any mold over 25 kg (all TX-500 tools and most
  TX-250 tools).

Target changeover time is **45 minutes** on TX-250 and **75 minutes** on TX-500, measured
last-good-part to first-good-part. **Time targets never justify skipping a safety step.**

## 2. Pre-change preparation (while the press is still running)

Prepare off-line to keep the press down-time short:

- Pull the new tool from storage; verify tool number, cavity count, and last-run condition
  tag. Confirm the stamped weight is legible (needed for rigging, SAF-007 §7).
- Verify the tool is not on QC hold (QC-005) and that any open tool CAPA is closed.
- Stage clamps, bolts, T-nuts, water jumpers, hot runner cable, and the correct torque wrench.
- Pre-heat the tool at the mold preheat station if the job requires a tool temperature above
  60 °C — this saves 20+ minutes of press time.
- Print the setup sheet and the FAI dimensional layout (QC-002).
- Confirm dried material is available and within its drying window (MNT-004).

## 3. Shutdown and isolation

1. Run the last-good-part; record the count and notify QC.
2. Purge the barrel per SAF-003 §4 if the next job uses a different material or color.
3. Bring the mold to the open position and drive ejectors fully forward (releases spring
   stored energy, SAF-001 §3).
4. Turn off the TCU and **isolate mold water**. Blow the mold circuits clear with air at
   the manifold before disconnecting — an undrained tool drips onto the platen and into the
   tie-bar area.
5. Allow the tool to cool below **40 °C** before hand contact, or wear high-temp gloves.
   A tool from a 90 °C TCU takes roughly 45 minutes to reach this (SAF-003 §2).
6. **Apply full LOTO per SAF-001**, including the hot runner controller if fitted, and both
   accumulators on TX-500. Verify by try-start.

## 4. Mold removal

1. Install the **mold safety strap** across the mold halves before releasing any clamp.
   The strap stays on until the tool is seated in its storage rack.
2. Disconnect water jumpers, hot runner cables, core-pull hydraulics, and any air lines.
   Cap all hydraulic quick-disconnects.
3. Attach rigging to the rated lift eyes. Verify sling condition and capacity tag (SAF-007 §7).
4. Take up slack, lift 50 mm, confirm balance and brake hold.
5. Loosen clamps in a **cross pattern**, keeping the last two clamps opposite each other
   until the crane is taking the load.
6. Withdraw the tool clear of the tie bars, set it on the mold cart or rack, and remove the
   rigging before releasing the strap.

## 5. Mold installation

1. Inspect the platen face and the tool's mounting surfaces. Remove any resin, burrs, or
   old thread-locker. A chip under a mold face is a leading cause of platen damage.
2. Set the tool on the locating ring; confirm the ring is fully seated before releasing
   crane load.
3. Install clamps in a **cross pattern**. Clamp bolts must engage a minimum of **1.5× bolt
   diameter** of thread.
4. Torque to spec — **M16 mold clamp bolts: 210 N·m** (full torque table in MNT-007 §3).
   Use a calibrated torque wrench; do not "feel" it.
5. Connect water in the correct **series/parallel arrangement shown on the setup sheet**.
   Circuits connected in the wrong order are a frequent and hard-to-diagnose cause of
   dimensional drift and warp.
6. Connect the hot runner, core pulls, and air. Cap unused ports.
7. Remove the mold safety strap **only after all clamps are torqued.**

## 6. Startup

1. Remove LOTO per SAF-001. Only the person who applied a lock removes it.
2. Restore guards. Perform the SAF-002 §3 safety device checks — a mold change can knock a
   light curtain out of alignment, and this is the most common post-changeover safety finding.
3. Set mold protect to low-pressure creep and verify it trips on a **3 mm obstruction**
   before running in auto.
4. Bring the TCU to setpoint and confirm delta-T across the tool is within **3 °C** of the
   setup sheet (MNT-005).
5. Dry-cycle **5 shots** with no material to confirm mold open/close, ejection, and robot path.
6. Load the process from the setup sheet and run **10 stabilization shots to scrap.**
7. Take **5 consecutive parts** for First Article Inspection and submit per QC-002.
   **Production does not start until the FAI is approved by QC.**

## 7. Changeover record

The setter completes the changeover record before leaving the cell:

- Tool number, press, date, shift, start and end time
- Names of everyone who applied a lock
- Torque wrench ID used and torque value applied
- Water circuit configuration
- Any damage found on the tool, photographed and reported to the tool room
- FAI submission time and QC disposition

## 8. Post-run tool care

Returning a tool to storage:

- Clean the tool; blow the water circuits clear with air to prevent internal corrosion.
- Apply rust preventative RP-5 to cavity and core surfaces (SAF-004 §2 for PPE).
- Close the tool and secure the safety strap.
- Attach the condition tag noting cycles run, any damage, and any repair required.
- A tool needing repair goes to the tool room, **not back into the rack.**

## 9. Related documents

- SAF-001 — Lockout/Tagout
- SAF-003 — Hot Surface and Molten Polymer Burn Prevention
- SAF-007 — Powered Industrial Trucks and Pedestrian Traffic (crane/rigging)
- MNT-005 — Chiller and Mold Temperature Control
- MNT-007 — Lubrication and Torque Specifications
- QC-002 — First Article Inspection
