---
doc_id: MNT-007
title: Lubrication Chart and Torque Specifications
category: maintenance
subcategory: specifications
equipment: [TX-250, TX-500, PR-12, GR-40, overhead_crane]
applies_to: [maintenance_tech, process_tech]
revision: "4.1"
effective_date: 2026-03-02
review_due: 2028-03-02
owner: Maintenance Manager
status: active
supersedes: "4.0"
related_docs: [SAF-001, SAF-004, MNT-001, MNT-002, QC-006]
keywords: [lubrication, grease, oil, torque, bolt, clamp, tie bar, ncr, interval, nlgi, iso vg, torque wrench, calibration]
source: synthetic_demo_corpus
classification: internal_demo
contains_pii: false
---

# MNT-007 — Lubrication Chart and Torque Specifications

## 1. Lubricant list

| Code | Type | Specification | Used on |
|---|---|---|---|
| **L1** | Hydraulic oil | ISO VG 46, anti-wear | Press hydraulic reservoirs |
| **L2** | Toggle grease | NLGI 2 lithium complex, EP | Toggle pins, bushings, links |
| **L3** | Linear guide grease | NLGI 2 synthetic | Robot linear guides, ejector guides |
| **L4** | Gear oil | ISO VG 220 | Granulator GR-40 gearbox |
| **L5** | Food-grade grease | NLGI 2, H1 registered | Any tool running a food-contact program |
| **L6** | Wire rope lubricant | Penetrating, tacky | Crane hoist rope |

**Never mix lubricant types.** Mixing a lithium and a polyurea grease can cause the mixture
to liquefy and run out of the bearing, leaving it dry. If the incumbent grease is unknown or
the type is changing, purge the point completely.

Colour-coded grease guns are dedicated per lubricant and are **not** interchangeable. A gun
used for the wrong lubricant is taken out of service and cleaned before reuse.

Food-grade **L5** is mandatory on any tool assigned to a food-contact program. Using a
non-H1 lubricant on such a tool is a product contamination event: quarantine per QC-005 and
raise a customer notification per QC-007.

## 2. Lubrication chart

| Point | Lubricant | Interval | Quantity / note |
|---|---|---|---|
| Toggle pins and bushings | L2 | Weekly | 2 shots per zerk, machine at mold-close |
| Tie-bar bushings | L2 | Weekly | 2 shots per zerk |
| Platen guide shoes | L2 | Weekly | Wipe excess; excess attracts resin dust |
| Ejector guide pins | L3 | Weekly | Light film only |
| Mold leader pins and bushings | L2 (L5 if food) | Every mold change | Thin film; wipe excess to avoid part contamination |
| Screw drive gearbox | L1 | Check level monthly | Change at 8,000 h |
| Robot linear guides | L3 | Monthly | Per axis grease port |
| Granulator gearbox GR-40 | L4 | Check level monthly | Change annually |
| Crane hoist rope | L6 | Quarterly | Inspect for broken strands at the same time (SAF-007 §7) |
| Hydraulic reservoir | L1 | Level daily; analysis every 500 h | MNT-001 §6 |

Over-greasing is a real failure mode, not just waste: it blows seals, and on the platen guide
shoes the excess collects resin dust into an abrasive paste. **Wipe every point after greasing.**

Automatic lubrication systems, where fitted, are verified monthly: confirm the reservoir
level, that the pump cycles, and that each metering point actually delivers. A blocked
metering point gives no alarm on this system.

## 3. Torque specifications

All values are for clean, dry threads unless noted. Lubricated threads require roughly
**25% less torque** — applying a dry-thread value to a lubricated fastener overloads and can
snap the bolt.

### Mold clamping — grade 12.9 bolts

| Size | Torque | Note |
|---|---|---|
| M12 | 90 N·m | TX-250 light tooling |
| **M16** | **210 N·m** | Standard mold clamp bolt, both presses |
| M20 | 410 N·m | TX-500 heavy tooling |
| M24 | 710 N·m | Large tool mounting |

Minimum thread engagement is **1.5 × bolt diameter** (MNT-002 §5). Tighten clamps in a
**cross pattern**, in two passes: 60% of final torque, then 100%.

### Other fasteners

| Application | Size | Torque |
|---|---|---|
| Tie-bar nut | — | Per press data plate; OEM procedure and sequence required |
| Barrel heater band clamp | M8 | 12 N·m — **re-torque after first heat cycle** |
| Nozzle body to barrel | — | Per OEM, hot-torqued at process temperature |
| Hydraulic manifold bolts | M10 | 45 N·m |
| Robot EOAT mounting | M6 | 10 N·m |
| Guard panel fasteners | M8 | 20 N·m |

### Bolt condition

Mold clamp bolts are consumable. Replace, do not reuse, any bolt that is stretched, galled,
has damaged threads, or has been heated. Grade 12.9 bolts are **never** substituted with a
lower grade — check the head marking before installation.

## 4. Torque wrench control

Torque wrenches are measuring instruments and are controlled under **QC-006**:

- Calibrated **annually**, and immediately after any drop or suspected overload.
- Each wrench carries a unique ID and a current calibration sticker with the due date.
- The wrench ID used is recorded on the mold changeover record (MNT-002 §7).
- Click wrenches are **wound down to the lowest setting before storage** — leaving a wrench
  loaded takes the spring out of calibration.
- A wrench past its calibration due date may not be used. Any work performed with a wrench
  later found out of calibration triggers a QC-005 review of affected product.

## 5. Related documents

- SAF-001 — Lockout/Tagout
- SAF-004 — Chemical Handling and Spill Response
- MNT-001 — Injection Press Preventive Maintenance Schedule
- MNT-002 — Mold Change Procedure
- QC-006 — Gage Calibration and Measurement System Analysis
