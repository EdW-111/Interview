---
doc_id: SAF-003
title: Hot Surface and Molten Polymer Burn Prevention
category: safety
subcategory: thermal_hazard
equipment: [TX-250, TX-500, AD-300, TCU-90]
applies_to: [operator, process_tech, maintenance_tech, floor_supervisor]
revision: "2.4"
effective_date: 2025-09-22
review_due: 2027-09-22
owner: EHS Manager
status: active
supersedes: "2.3"
related_docs: [SAF-001, SAF-004, SAF-005, MNT-004]
keywords: [burn, molten, purge, barrel, nozzle, hot surface, drool, degradation, blowback, gloves, first aid]
source: synthetic_demo_corpus
classification: internal_demo
contains_pii: false
---

# SAF-003 — Hot Surface and Molten Polymer Burn Prevention

## 1. Hazard summary

Molten polymer exits the nozzle between **190 °C and 320 °C** depending on material.
Barrel bands, nozzle tips, hot runner manifolds, and mold surfaces on temperature control
remain dangerous long after the machine stops cycling. Molten polymer **adheres to skin**
and continues transferring heat after contact — burns from purge are typically far more
severe than a comparable contact burn from a hot metal surface.

## 2. Temperature thresholds

| Surface temperature | Classification | Requirement |
|---|---|---|
| > 50 °C | Hot | Marked with hot-surface label; no bare-hand contact |
| 40–50 °C | Warm | Brief bare-hand contact acceptable |
| < 40 °C | Cold enough to handle | Required threshold before LOTO thermal verification is complete (SAF-001 §3) |

Verify with the cell's IR probe, not by touch. A mold on a TCU-90 running at 90 °C water
takes approximately **45 minutes** to fall below 40 °C with the unit off, and considerably
longer for an oil-heated tool.

## 3. Required PPE for purging

Purging is the highest-burn-risk routine task in the plant. Required, without exception:

- Full face shield **over** safety glasses (face shield alone is insufficient)
- High-temperature purge gloves rated to 350 °C, gauntlet length past the wrist
- Long-sleeve cotton or FR sleeves — **no synthetic sleeves**, which melt to skin
- Leather apron
- Closed-toe safety footwear (SAF-005)

## 4. Purge procedure

1. Confirm the purge tray is in position under the nozzle and empty.
2. Confirm no personnel are in the rear zone; close and interlock the rear gate if purging
   in auto-purge mode.
3. Never place any body part between the nozzle and the purge tray.
4. Purge in **short shots**, not one continuous stroke. Decompression between shots reduces
   the chance of a pressurized ejection.
5. Deposit purge into the metal purge bin only. Never into a plastic gaylord or onto the floor.
6. Allow purge to cool in the bin at least **30 minutes** before moving it.

## 5. Blowback and degradation

Materials held above their processing window degrade and generate gas. The pressure can
eject molten material violently from the nozzle or hopper throat — this is the mechanism
behind most severe purge injuries.

**High-risk materials at Plant 4:** PVC compounds, POM (acetal), and any material held at
temperature during an unplanned line stop.

If a press has been at temperature and idle for **more than 20 minutes**:

- Drop barrel setpoints to the material's idle temperature before restarting.
- Stand to the **side** of the nozzle, never in front of it, for the first purge shot.
- For POM and PVC, do not allow residence beyond 20 minutes at process temperature — purge
  the barrel clear and drop heats. POM and PVC must never be purged into one another;
  cross-contamination produces a violent exothermic reaction and toxic gas.

## 6. Hot runner and manifold work

Hot runner manifolds hold heat far longer than a barrel and have no external temperature
indication. Before opening a manifold plate:

- Isolate per SAF-001, including the hot runner controller.
- Wait a minimum of **90 minutes**, then verify < 40 °C with the IR probe at the manifold face.
- Two-person rule applies: no solo hot runner work on any shift.

## 7. First aid for thermal burns

1. **Do not attempt to pull adhered polymer off the skin.** Doing so removes skin with it.
2. Cool the area with clean, cool (not ice) running water for **20 minutes**.
3. Cover loosely with a sterile non-adherent dressing. Do not apply ointment, butter, or ice.
4. Any burn that blisters, involves the face/hands/joints, or has adhered polymer is an
   **immediate off-site medical referral** — notify the supervisor and call the plant nurse
   at extension **4110**. After hours, call 911.
5. All burns, including those treated with first aid only, are recorded within 24 hours on
   Form EHS-INC-01.

## 8. Related documents

- SAF-001 — Lockout/Tagout
- SAF-004 — Chemical Handling and Spill Response
- SAF-005 — PPE Requirements Matrix
- MNT-004 — Resin Drying and Conveying System Service
