---
doc_id: QC-001
title: Incoming Material Inspection and Release
category: quality
subcategory: incoming_inspection
equipment: [receiving, QC_lab]
applies_to: [material_handler, quality_tech, floor_supervisor]
revision: "3.2"
effective_date: 2026-01-26
review_due: 2028-01-26
owner: Quality Manager
status: active
supersedes: "3.1"
related_docs: [SAF-005, SAF-007, MNT-004, QC-005, QC-006]
keywords: [incoming, receiving, coa, certificate of analysis, lot, traceability, resin, sampling, quarantine, release, skip lot]
source: synthetic_demo_corpus
classification: internal_demo
contains_pii: false
---

# QC-001 — Incoming Material Inspection and Release

## 1. Purpose

Ensure that no raw material, colorant, or purchased component enters production until it is
verified against specification and traceable to a supplier lot.

## 2. Material status states

Every lot on site is in exactly one state at all times:

| Status | Tag color | Location | May be used? |
|---|---|---|---|
| Quarantine (awaiting inspection) | **Yellow** | Receiving hold area | No |
| Released | **Green** | General storage / floor | Yes |
| On hold / under investigation | **Red** | Quarantine cage, NE corner | No |
| Rejected, awaiting return or disposal | **Red** + Reject tag | Quarantine cage | No |

**Untagged material is treated as quarantine, not as released.** Material found on the floor
without a status tag is moved to quarantine and investigated as a nonconformance (QC-005).

## 3. Receiving checks — performed on 100% of deliveries

Performed by receiving before the material leaves the dock:

1. Compare the packing slip to the purchase order: material grade, quantity, lot number.
2. Verify **each** container's label matches the packing slip — mixed-lot pallets happen.
3. Inspect packaging: tears, water damage, crushed or bulging gaylords, broken pallet.
   Damaged or wet packaging is a **reject on receipt** — moisture-damaged resin is not
   recoverable by drying to the standard of a sealed lot.
4. Confirm the **Certificate of Analysis (CoA)** is present and matches the lot number on
   the containers.
5. Apply a yellow quarantine tag with the receipt date and internal lot ID.

## 4. Certificate of Analysis review — QC

QC reviews the CoA against the material specification. Minimum verified attributes:

| Attribute | Verified against |
|---|---|
| Material grade and supplier part number | Approved material list |
| Melt flow rate (MFR) | Spec range for the grade |
| Moisture as shipped | Supplier spec |
| Color / colorant loading (for pre-colored) | Approved standard |
| Regrind content, if any | Must be declared; undeclared regrind is a rejection |
| Lot number and manufacture date | Traceable, and within shelf life (§6) |

A missing, illegible, or mismatched CoA blocks release. Do not accept a CoA "to follow" —
material stays in quarantine until the document is on file.

## 5. Sampling and testing

| Material class | Test | Sampling |
|---|---|---|
| Hygroscopic resin (PC, PA66, PBT, ABS, POM) | Moisture content (QC-006 method) | 1 container per lot, plus any container with damaged packaging |
| All resin | Visual: contamination, discoloration, foreign pellets, angel hair | 1 container per lot |
| Pre-colored resin | Color match to master standard under D65 light | 1 container per lot |
| Colorant / masterbatch | Visual + label verification | 100% of containers |
| Purchased components (inserts, packaging) | Per component control plan | Per control plan |

Moisture at receipt is checked against the **supplier's as-shipped spec**, not the at-press
limit. The at-press moisture limits in MNT-004 §2 apply after drying, immediately before molding.

### Skip-lot provision
A supplier with **20 consecutive accepted lots** and no open corrective action may be moved to
skip-lot sampling (1 in 4 lots) with Quality Manager approval. Any single rejection returns
the supplier to 100% lot inspection for the next 20 lots. Skip-lot status is reviewed quarterly.

## 6. Shelf life and stock rotation

| Material | Shelf life from manufacture | Storage |
|---|---|---|
| PC, PBT, PA66 (sealed foil-lined) | 24 months | Dry, sealed, 15–30 °C |
| ABS, POM (sealed) | 24 months | Dry, sealed, 15–30 °C |
| PP, PE | 36 months | Dry, 15–30 °C |
| Masterbatch / colorant | 24 months | Sealed, out of direct light |
| Opened container, any hygroscopic resin | **7 days**, then re-test moisture before use | Resealed |

Stock is rotated **first-expiry-first-out**. Material past shelf life is not automatically
scrap: it moves to red hold and may be re-qualified by moisture and MFR testing with Quality
Manager approval, documented on Form QC-001-F3. Undocumented use of expired material is a
nonconformance.

## 7. Release

Release is a **positive act by a QC technician**: the yellow tag is replaced with a green
release tag showing internal lot ID, material, release date, and technician initials.
Production may not pull material that has not been positively released.

Traceability from finished part back to supplier lot is maintained through the internal lot
ID recorded on the production run record. This is the link that makes a targeted recall
possible instead of a blanket one (QC-007).

## 8. Rejection

On rejection: apply a red tag, move to the quarantine cage, raise a nonconformance per QC-005,
and notify Purchasing the same day. Supplier corrective action is requested for any rejection;
repeat rejections of the same failure mode trigger a supplier CAPA under QC-007.

## 9. Related documents

- SAF-005 — PPE Requirements Matrix
- SAF-007 — Powered Industrial Trucks (gaylord stacking, damaged containers)
- MNT-004 — Resin Drying and Conveying System Service
- QC-005 — Nonconforming Material Control
- QC-006 — Gage Calibration and Measurement System Analysis
