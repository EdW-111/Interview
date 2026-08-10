# LLM Eval Report — Plant 4 Documentation Assistant

- generated: `2026-08-10 11:28:26`  
- generator: `deepseek-chat`  
- embeddings: `BAAI/bge-small-en-v1.5`  
- questions: 22  
- wall time: 32.3s

## Aggregate

| metric | result | |
|---|---|---|
| Routing — exact category set | 17/22 | 77% |
| Routing — never dropped a required category | 22/22 | 100% |
| Routing — over-broad (correct + extra) | 5/22 | |
| Routing — dropped a required category | 0/22 | |
| Section recall — all expected in context | 20/21 | 95% |
| Citation trust — no unsupported citations | 22/22 | 100% |
| Grounding — answer cites an expected section | 21/21 | 100% |

## Summary

| id | kind | route | recall | conf | band | top1 | cites | unsupported |
|---|---|---|---|---|---|---|---|---|
| [q01](#q01) | single-hop | exact | full | 0.99 high | strong | 0.824 | 2 | — |
| [q02](#q02) | cross-cutting | exact | full | 0.79 medium | moderate | 0.724 | 2 | — |
| [q03](#q03) | safety-gated | exact | full | 0.99 high | strong | 0.785 | 3 | — |
| [q04](#q04) | single-hop | exact | full | 0.60 medium | moderate | 0.667 | 1 | — |
| [q05](#q05) | single-hop | exact | full | 0.67 medium | moderate | 0.694 | 2 | — |
| [q06](#q06) | single-hop | exact | full | 0.99 high | strong | 0.804 | 2 | — |
| [q07](#q07) | single-hop | exact | full | 0.65 medium | moderate | 0.675 | 1 | — |
| [q08](#q08) | single-hop | exact | full | 0.87 medium | moderate | 0.748 | 1 | — |
| [q09](#q09) | cross-cutting | exact | partial | 0.69 medium | moderate | 0.701 | 5 | — |
| [q10](#q10) | single-hop | exact | full | 0.62 medium | moderate | 0.671 | 2 | — |
| [q11](#q11) | single-hop | over-broad | full | 0.70 medium | moderate | 0.699 | 2 | — |
| [q12](#q12) | single-hop | exact | full | 0.65 medium | moderate | 0.680 | 1 | — |
| [q13](#q13) | single-hop | over-broad | full | 0.97 high | strong | 0.819 | 2 | — |
| [q14](#q14) | single-hop | exact | full | 0.85 medium | moderate | 0.738 | 1 | — |
| [q15](#q15) | single-hop | over-broad | full | 0.84 medium | moderate | 0.746 | 2 | — |
| [q16](#q16) | single-hop | exact | full | 0.72 medium | moderate | 0.704 | 2 | — |
| [q17](#q17) | single-hop | exact | full | 0.58 medium | moderate | 0.665 | 1 | — |
| [q18](#q18) | single-hop | over-broad | full | 0.63 medium | moderate | 0.685 | 3 | — |
| [q19](#q19) | single-hop | over-broad | full | 0.67 medium | moderate | 0.685 | 3 | — |
| [q20](#q20) | cross-cutting | exact | full | 0.82 medium | moderate | 0.740 | 2 | — |
| [q21](#q21) | cross-cutting | exact | full | 0.78 medium | moderate | 0.721 | 2 | — |
| [q22](#q22) | out-of-scope | exact | n/a | 0.25 low | none | 0.000 | 0 | — |

---

<a id="q01"></a>
## q01 — single-hop

**Q:** What torque do I use on M16 mold clamp bolts?

| | expected | actual |
|---|---|---|
| route | `['maintenance']` | `['maintenance']` → **exact** |
| sections | `['MNT-007 §3']` | found `['MNT-007 §3']` → **full** |

**Router reasoning:** _Torque specs are in the maintenance documentation._  
**Confidence:** overall **0.99 (high)** — router 0.95 × retrieval 1.00 | band `strong` (top1 0.824, mean3 0.757) — close match in the documentation

<details><summary>Retrieved context (4 chunks)</summary>

| # | score | citation | category | section | expected |
|---|---|---|---|---|---|
| 1 | 0.824 | `MNT-007 §3` | maintenance | Torque specifications — Mold clamping — grad | **YES** |
| 2 | 0.744 | `MNT-007 §3` | maintenance | Torque specifications — Bolt condition | **YES** |
| 3 | 0.702 | `MNT-007 §3` | maintenance | Torque specifications — Other fasteners | **YES** |
| 4 | 0.692 | `MNT-002 §5` | maintenance | Mold installation |  |

</details>

**Answer:**

> **210 N·m** for M16 mold clamp bolts, on both presses [MNT-007 §3].
> 
> **Conditions:**
> - Use a calibrated torque wrench — do not "feel" it [MNT-002 §5].
> - Minimum thread engagement is **1.5 × bolt diameter** (i.e., 24 mm for M16) [MNT-002 §5].
> - Tighten in a **cross pattern**, in two passes: 60% of final torque first, then 100% [MNT-007 §3].
> - Before torquing, inspect the platen face and tool mounting surfaces; remove any resin, burrs, or old thread-locker [MNT-002 §5].
> - Remove the mold safety strap **only after all clamps are torqued** [MNT-002 §5].
> - Check the bolt head marking — grade 12.9 bolts are **never** substituted with a lower grade [MNT-007 §3]. Replace, do not reuse, any bolt that is stretched, galled, has damaged threads, or has been heated [MNT-007 §3].

**Citations in answer:** `MNT-002 §5`, `MNT-007 §3` — all supported

---

<a id="q02"></a>
## q02 — cross-cutting

**Q:** Parts coming off press 4 have silver streaks near the gate. What's causing it?

| | expected | actual |
|---|---|---|
| route | `['quality', 'maintenance']` | `['quality', 'maintenance']` → **exact** |
| sections | `['QC-004 §3', 'MNT-004 §1']` | found `['MNT-004 §1', 'QC-004 §3']` → **full** |

**Router reasoning:** _Silver streaks are a visual defect (quality), but the root cause is often resin drying or moisture (maintenance)._  
**Confidence:** overall **0.79 (medium)** — router 0.95 × retrieval 0.74 | band `moderate` (top1 0.724, mean3 0.671) — relevant material found, may be partial

<details><summary>Retrieved context (8 chunks)</summary>

| # | score | citation | category | section | expected |
|---|---|---|---|---|---|
| 1 | 0.724 | `QC-004 §3` | quality | Defect catalog — Splay (silver streaking) | **YES** |
| 2 | 0.660 | `QC-004 §3` | quality | Defect catalog — Flash | **YES** |
| 3 | 0.630 | `MNT-003 §2` | maintenance | Symptom → cause index |  |
| 4 | 0.601 | `MNT-007 §2` | maintenance | Lubrication chart |  |
| 5 | 0.600 | `MNT-004 §1` | maintenance | Why drying matters | **YES** |
| 6 | 0.598 | `QC-007 §3` | quality | Root cause |  |
| 7 | 0.595 | `MNT-003 §4` | maintenance | Leaks |  |
| 8 | 0.576 | `QC-003 §4` | quality | Operator response to an out-of-control signa |  |

</details>

**Answer:**

> Silver streaks near the gate is **splay**, and the cause is almost certainly moisture in the material [QC-004 §3]. Under-dried material is the most common single root cause of scrap at Plant 4 [MNT-004 §1].
> 
> Before touching the process, confirm the moisture by test per QC-006 [QC-004 §3]. Then verify the dryer dew point and residence time per MNT-004 §2/§3 [QC-004 §3]. Less often, splay comes from material degradation from excess melt temperature or residence time, or air entrainment from a worn check ring [QC-004 §3].
> 
> Note the acceptance rule: splay is rejected in all zones on structural or safety parts, because it indicates moisture that can reduce strength even where cosmetically acceptable [QC-004 §3].

**Citations in answer:** `MNT-004 §1`, `QC-004 §3` — all supported

---

<a id="q03"></a>
## q03 — safety-gated

**Q:** How do I clear a mold protect fault E-301?

| | expected | actual |
|---|---|---|
| route | `['maintenance', 'safety']` | `['maintenance', 'safety']` → **exact** |
| sections | `['MNT-006 §4', 'SAF-001 §4']` | found `['MNT-006 §4', 'SAF-001 §4']` → **full** |

**Router reasoning:** _Fault code E-301 is a maintenance alarm, but clearing it requires opening the mold area, which is gated by lockout/tagout safety procedures._  
**Confidence:** overall **0.99 (high)** — router 0.95 × retrieval 1.00 | band `strong` (top1 0.785, mean3 0.719) — close match in the documentation

<details><summary>Retrieved context (8 chunks)</summary>

| # | score | citation | category | section | expected |
|---|---|---|---|---|---|
| 1 | 0.785 | `MNT-006 §4` | maintenance | Clamp and mold faults — `E-3xx` (level B) | **YES** |
| 2 | 0.690 | `MNT-002 §3` | maintenance | Shutdown and isolation |  |
| 3 | 0.682 | `MNT-006 §2` | maintenance | Safety faults — `E-1xx` (clearance level C) |  |
| 4 | 0.680 | `MNT-002 §6` | maintenance | Startup |  |
| 5 | 0.654 | `SAF-002 §8` | safety | Damaged or nuisance-tripping devices |  |
| 6 | 0.650 | `SAF-001 §4` | safety | Required six-step sequence | **YES** |
| 7 | 0.648 | `SAF-003 §4` | safety | Purge procedure |  |
| 8 | 0.641 | `SAF-003 §2` | safety | Temperature thresholds |  |

</details>

> **SAFETY OVERLAY FIRED** — This answer draws on safety documentation. Safety requirements are preconditions, not suggestions — do not begin the task until they are met.

**Answer:**

> To clear a mold protect fault **E-301**, you must first perform **full LOTO per SAF-001** — there is no exception for "just grabbing the part" [MNT-006 §4]. The fault means a part or sprue is stuck in the mold, the ejector has not returned, or the 3 mm sensitivity setting is triggering [MNT-006 §4].
> 
> **Before any steps, complete the LOTO sequence in SAF-001 §4:**
> 1. Notify the cell operator and shift supervisor; log the cell on the LOTO board.
> 2. Shut down via HMI *Cycle Stop* (not E-stop unless emergency).
> 3. Isolate all devices listed in SAF-001 §3 for the work.
> 4. Apply personal red padlock and completed danger tag to each isolation device.
> 5. Release stored energy: bleed accumulator via `BV-1`, wait **minimum 5 minutes**, confirm `PG-1` reads **0 psi**, bleed air at `AV-1`, install mold safety strap if mold is open.
> 6. Verify with a try-start from the HMI — confirm no motion, return selector to OFF. **LOTO is not complete until Step 6 is done** [SAF-001 §4].
> 
> **After LOTO is verified, clear the obstruction:**
> - Open the mold area and remove the stuck part or sprue.
> - Check that the ejector has fully returned.
> - Verify the mold protect sensitivity setting — it should trip on a **3 mm obstruction** [MNT-006 §4].
> 
> **Before returning to auto, per MNT-002 §6:**
> - Remove LOTO per SAF-001 (only the person who applied a lock removes it).
> - Restore guards and perform SAF-002 §3 safety device checks.
> - Set mold protect to low-pressure creep and verify it trips on a **3 mm obstruction**.
> - Dry-cycle **5 shots** with no material to confirm mold open/close, ejection, and robot path.
> - Load process from setup sheet and run **10 stabilization shots to scrap**.
> - Take **5 consecutive parts** for First Article Inspection; **production does not start until FAI is approved by QC** [MNT-002 §6].
> 
> **Note:** If the fault recurs after clearing the obstruction, re-check the 3 mm sensitivity setting and the ejector return. If it still trips, treat it as a persistent fault and escalate per the alarm reference [MNT-006 §4].

**Citations in answer:** `MNT-002 §6`, `MNT-006 §4`, `SAF-001 §4` — all supported

---

<a id="q04"></a>
## q04 — single-hop

**Q:** Can I start running production while the first article is still in the lab?

| | expected | actual |
|---|---|---|
| route | `['quality']` | `['quality']` → **exact** |
| sections | `['QC-002 §4']` | found `['QC-002 §4']` → **full** |

**Router reasoning:** _First article inspection is a quality gate._  
**Confidence:** overall **0.60 (medium)** — router 0.90 × retrieval 0.50 | band `moderate` (top1 0.667, mean3 0.658) — relevant material found, may be partial

<details><summary>Retrieved context (4 chunks)</summary>

| # | score | citation | category | section | expected |
|---|---|---|---|---|---|
| 1 | 0.667 | `QC-002 §1` | quality | When an FAI is required |  |
| 2 | 0.663 | `QC-002 §2` | quality | Sample preparation |  |
| 3 | 0.645 | `QC-002 §4` | quality | Disposition | **YES** |
| 4 | 0.590 | `QC-001 §1` | quality | Purpose |  |

</details>

**Answer:**

> No. Production may not run on a pending FAI. If the press runs while the FAI is in the lab, everything produced is held under QC-005 until disposition [QC-002 §4].

**Citations in answer:** `QC-002 §4` — all supported

---

<a id="q05"></a>
## q05 — single-hop

**Q:** The mold was running at 90 degrees. How long before I can touch it with bare hands?

| | expected | actual |
|---|---|---|
| route | `['safety']` | `['safety']` → **exact** |
| sections | `['SAF-003 §2']` | found `['SAF-003 §2']` → **full** |

**Router reasoning:** _Burns and molten polymer safety, cooling time is a safety concern._  
**Confidence:** overall **0.67 (medium)** — router 0.85 × retrieval 0.61 | band `moderate` (top1 0.694, mean3 0.645) — relevant material found, may be partial

<details><summary>Retrieved context (4 chunks)</summary>

| # | score | citation | category | section | expected |
|---|---|---|---|---|---|
| 1 | 0.694 | `SAF-003 §2` | safety | Temperature thresholds | **YES** |
| 2 | 0.623 | `SAF-003 §7` | safety | First aid for thermal burns |  |
| 3 | 0.618 | `SAF-003 §6` | safety | Hot runner and manifold work |  |
| 4 | 0.607 | `SAF-005 §3` | safety | Glove selection guidance |  |

</details>

> **SAFETY OVERLAY FIRED** — This answer draws on safety documentation. Safety requirements are preconditions, not suggestions — do not begin the task until they are met.

**Answer:**

> You can touch the mold with bare hands once it falls below 40 °C, but you must verify that with the cell's IR probe, not by touch [SAF-003 §2]. With the TCU-90 unit off, a mold running at 90 °C water takes approximately **45 minutes** to fall below 40 °C [SAF-003 §2]. Oil-heated tools take considerably longer [SAF-003 §2].
> 
> Note: this applies to the mold surface. If you are working on a hot runner manifold, the wait is a minimum of **90 minutes** before verifying < 40 °C with the IR probe at the manifold face [SAF-003 §6].

**Citations in answer:** `SAF-003 §2`, `SAF-003 §6` — all supported

---

<a id="q06"></a>
## q06 — single-hop

**Q:** What dew point should the resin dryer be running at, and when does it alarm?

| | expected | actual |
|---|---|---|
| route | `['maintenance']` | `['maintenance']` → **exact** |
| sections | `['MNT-004 §3']` | found `['MNT-004 §3']` → **full** |

**Router reasoning:** _Resin dryer settings and alarms are maintenance topics._  
**Confidence:** overall **0.99 (high)** — router 0.95 × retrieval 1.00 | band `strong` (top1 0.804, mean3 0.765) — close match in the documentation

<details><summary>Retrieved context (4 chunks)</summary>

| # | score | citation | category | section | expected |
|---|---|---|---|---|---|
| 1 | 0.804 | `MNT-004 §3` | maintenance | Dryer setpoints and alarms — AD-300 | **YES** |
| 2 | 0.763 | `MNT-004 §4` | maintenance | Maintenance schedule |  |
| 3 | 0.729 | `MNT-004 §5` | maintenance | Conveying system |  |
| 4 | 0.698 | `MNT-006 §6` | maintenance | Auxiliary faults — Dryer — `D-xx` (level A/B |  |

</details>

**Answer:**

> The dryer should be running at a dew point of **−40 °C**. It alarms when the dew point reaches **−25 °C** [MNT-004 §3].
> 
> When the alarm triggers, investigate the desiccant/regen cycle before running [MNT-004 §3]. Material dried at an out-of-spec dew point must be verified by moisture test (QC-006) before molding, or re-dried — do not assume a full drying cycle fixes it [MNT-004 §3]. This is also reflected in fault code D-01, which means "Dew point above alarm (−25 °C)" [MNT-006 §6].

**Citations in answer:** `MNT-004 §3`, `MNT-006 §6` — all supported

---

<a id="q07"></a>
## q07 — single-hop

**Q:** A technician left their lock on the press and went home. How do I get it off?

| | expected | actual |
|---|---|---|
| route | `['safety']` | `['safety']` → **exact** |
| sections | `['SAF-001 §8']` | found `['SAF-001 §8']` → **full** |

**Router reasoning:** _Lockout/tagout procedure for removing a lock, safety topic._  
**Confidence:** overall **0.65 (medium)** — router 1.00 × retrieval 0.53 | band `moderate` (top1 0.675, mean3 0.628) — relevant material found, may be partial

<details><summary>Retrieved context (4 chunks)</summary>

| # | score | citation | category | section | expected |
|---|---|---|---|---|---|
| 1 | 0.675 | `SAF-001 §8` | safety | Removing another employee's lock | **YES** |
| 2 | 0.611 | `SAF-001 §4` | safety | Required six-step sequence |  |
| 3 | 0.598 | `SAF-001 §5` | safety | Press-specific isolation notes |  |
| 4 | 0.593 | `SAF-002 §3` | safety | Daily pre-shift verification (operator) |  |

</details>

> **SAFETY OVERLAY FIRED** — This answer draws on safety documentation. Safety requirements are preconditions, not suggestions — do not begin the task until they are met.

**Answer:**

> Use the exceptional lock-removal procedure in [SAF-001 §8]. No supervisor can authorize this alone — you need both the Plant Manager and EHS Manager.
> 
> Before cutting the lock:
> 1. Physically inspect the equipment to confirm it is clear of personnel and safe to energize.
> 2. Make a documented attempt to contact the lock owner.
> 3. Obtain signatures from **both** the Plant Manager and the EHS Manager on **Form SAF-001-F2**.
> 4. Cut the lock, then notify the owner before they return to work.
> 
> Note: this is the only path — locks are personal property and are removed only by their owner, except in this exceptional case where the owner is unavailable (left site, unreachable).

**Citations in answer:** `SAF-001 §8` — all supported

---

<a id="q08"></a>
## q08 — single-hop

**Q:** What Cpk do we need on a safety characteristic?

| | expected | actual |
|---|---|---|
| route | `['quality']` | `['quality']` → **exact** |
| sections | `['QC-003 §2']` | found `['QC-003 §2']` → **full** |

**Router reasoning:** _Capability requirement, purely a quality standard._  
**Confidence:** overall **0.87 (medium)** — router 0.95 × retrieval 0.84 | band `moderate` (top1 0.748, mean3 0.673) — relevant material found, may be partial

<details><summary>Retrieved context (4 chunks)</summary>

| # | score | citation | category | section | expected |
|---|---|---|---|---|---|
| 1 | 0.748 | `QC-003 §2` | quality | Capability requirements | **YES** |
| 2 | 0.640 | `QC-003 §1` | quality | Sampling plan |  |
| 3 | 0.629 | `QC-002 §3` | quality | What is inspected |  |
| 4 | 0.625 | `QC-003 §6` | quality | Process adjustment authority |  |

</details>

**Answer:**

> **Cpk ≥ 1.67** on a safety/CTQ characteristic. If that capability is not met, you must run **100% inspection** until capability is restored [QC-003 §2].
> 
> Conditions attached to that number:
> - Capability must be calculated on a minimum of **25 subgroups (125 measurements)** from a **stable process**. Capability calculated on an out-of-control process is meaningless — establish statistical control first [QC-003 §2].
> - Cpk uses within-subgroup variation (short-term). A large gap between Cpk and Ppk indicates the process is drifting between subgroups — check material lot changes, shift changes, and mold temperature stability [QC-003 §2].
> - For a **new tool at PPAP**, the requirement is **Ppk ≥ 1.67** on all CTQ characteristics; otherwise the tool is not approved for production [QC-003 §2].

**Citations in answer:** `QC-003 §2` — all supported

---

<a id="q09"></a>
## q09 — cross-cutting

**Q:** Parts are warping after ejection. Where do I start?

| | expected | actual |
|---|---|---|
| route | `['quality', 'maintenance']` | `['quality', 'maintenance']` → **exact** |
| sections | `['QC-004 §3', 'MNT-005 §2']` | found `['QC-004 §3']` → **partial** |

**Router reasoning:** _Warp is a defect, but likely caused by mold temperature or cooling issues._  
**Confidence:** overall **0.69 (medium)** — router 0.85 × retrieval 0.64 | band `moderate` (top1 0.701, mean3 0.680) — relevant material found, may be partial

<details><summary>Retrieved context (8 chunks)</summary>

| # | score | citation | category | section | expected |
|---|---|---|---|---|---|
| 1 | 0.701 | `QC-004 §3` | quality | Defect catalog — Warp / dimensional distorti | **YES** |
| 2 | 0.682 | `QC-004 §3` | quality | Defect catalog — Flash | **YES** |
| 3 | 0.656 | `MNT-003 §7` | maintenance | Escalation |  |
| 4 | 0.650 | `QC-002 §2` | quality | Sample preparation |  |
| 5 | 0.648 | `MNT-002 §6` | maintenance | Startup |  |
| 6 | 0.648 | `MNT-002 §3` | maintenance | Shutdown and isolation |  |
| 7 | 0.626 | `MNT-003 §2` | maintenance | Symptom → cause index |  |
| 8 | 0.609 | `QC-005 §3` | quality | Bounding the affected population |  |

</details>

**Answer:**

> Start with the cooling system, not the process. Uneven cooling is the leading cause of warp at Plant 4 [QC-004 §3].
> 
> Before adjusting anything, verify two things:
> 1. **TCU delta-T across the tool is within 3 °C** of the setup sheet [QC-004 §3] [MNT-002 §6].
> 2. **Water circuits are plumbed per the setup sheet** [QC-004 §3] [MNT-002 §5].
> 
> Only after those checks pass should you look at other causes: non-uniform wall, ejection while too hot, or residual stress [QC-004 §3].
> 
> **Important condition:** Do not judge warp by eye. Acceptance is measured against the drawing's flatness/profile tolerance, after the conditioning period in QC-002 §2 [QC-004 §3]. For semi-crystalline materials (PA66, PBT, POM, PP), that means a minimum 24-hour hold at ambient before the dimensional check, unless the control plan authorizes a 1-hour provisional release [QC-002 §2].
> 
> Note: The documentation excerpts do not cover the full troubleshooting sequence for warp beyond the cooling checks and defect catalog. The most likely document to hold the complete procedure is MNT-005 (referenced for TCU delta-T and chilled water flow) [MNT-002 §6] [MNT-003 §2].

**Citations in answer:** `MNT-002 §5`, `MNT-002 §6`, `MNT-003 §2`, `QC-002 §2`, `QC-004 §3` — all supported

---

<a id="q10"></a>
## q10 — single-hop

**Q:** The hydraulic oil looks milky. What does that mean?

| | expected | actual |
|---|---|---|
| route | `['maintenance']` | `['maintenance']` → **exact** |
| sections | `['MNT-003 §5']` | found `['MNT-003 §5']` → **full** |

**Router reasoning:** _Hydraulic oil condition is a maintenance topic._  
**Confidence:** overall **0.62 (medium)** — router 0.95 × retrieval 0.51 | band `moderate` (top1 0.671, mean3 0.646) — relevant material found, may be partial

<details><summary>Retrieved context (4 chunks)</summary>

| # | score | citation | category | section | expected |
|---|---|---|---|---|---|
| 1 | 0.671 | `MNT-003 §5` | maintenance | Water in oil | **YES** |
| 2 | 0.653 | `MNT-003 §3` | maintenance | Pressure and temperature reference |  |
| 3 | 0.614 | `MNT-003 §2` | maintenance | Symptom → cause index |  |
| 4 | 0.591 | `MNT-006 §3` | maintenance | Hydraulic and drive faults — `E-2xx` (level  |  |

</details>

**Answer:**

> Milky hydraulic oil means water is in the oil. Do not simply change the oil — find the water source first, or the new charge will be contaminated within weeks [MNT-003 §5].
> 
> Check these sources in order of likelihood at Plant 4:
> 1. Heat exchanger tube leak — chilled water is at higher pressure than the oil side. Isolate the exchanger and watch whether water ingress stops.
> 2. Mold cooling leak with water running down a tie bar into the reservoir vent.
> 3. Reservoir breather saturated — condensation. Replace the desiccant breather.
> 4. Wash-down or a leaking overhead line above the reservoir.
> 
> Water content above 500 ppm means water is entering the system [MNT-003 §5]. Milky oil is also listed as a symptom of water ingress or air entrainment via a suction leak [MNT-003 §2].
> 
> Note: the documentation covers the cause and source-finding procedure, but the exact ppm threshold (500 ppm) is referenced from MNT-001 §6, which is not included in these excerpts. If you need the full oil-sampling procedure, that document is the one to consult.

**Citations in answer:** `MNT-003 §2`, `MNT-003 §5` — all supported

---

<a id="q11"></a>
## q11 — single-hop

**Q:** What PPE does an operator need to purge the barrel?

| | expected | actual |
|---|---|---|
| route | `['safety']` | `['safety', 'maintenance']` → **over-broad** |
| sections | `['SAF-003 §3']` | found `['SAF-003 §3']` → **full** |

**Router reasoning:** _PPE is safety, but purging is a maintenance task that involves molten polymer._  
**Confidence:** overall **0.70 (medium)** — router 0.90 × retrieval 0.63 | band `moderate` (top1 0.699, mean3 0.681) — relevant material found, may be partial

<details><summary>Retrieved context (8 chunks)</summary>

| # | score | citation | category | section | expected |
|---|---|---|---|---|---|
| 1 | 0.699 | `SAF-003 §3` | safety | Required PPE for purging | **YES** |
| 2 | 0.695 | `SAF-003 §4` | safety | Purge procedure |  |
| 3 | 0.650 | `SAF-005 §4` | safety | Inspection, replacement, and cost |  |
| 4 | 0.638 | `SAF-005 §5` | safety | Visitors and contractors |  |
| 5 | 0.623 | `MNT-001 §4` | maintenance | 500 operating hours |  |
| 6 | 0.618 | `MNT-002 §3` | maintenance | Shutdown and isolation |  |
| 7 | 0.614 | `MNT-001 §6` | maintenance | Oil analysis program |  |
| 8 | 0.606 | `MNT-006 §5` | maintenance | Barrel and heat faults — `E-4xx` (level B) |  |

</details>

> **SAFETY OVERLAY FIRED** — This answer draws on safety documentation. Safety requirements are preconditions, not suggestions — do not begin the task until they are met.

**Answer:**

> The operator needs, without exception: a full face shield worn **over** safety glasses (a face shield alone is not sufficient), high-temperature purge gloves rated to 350 °C with gauntlet length past the wrist, long-sleeve cotton or FR sleeves (no synthetic sleeves, which melt to skin), a leather apron, and closed-toe safety footwear [SAF-003 §3].
> 
> Before starting, inspect the gloves and face shield for damage — discard any glove with a tear, stiffening, or heat glazing, and discard face shields that are crazed, scratched, or impact-marked [SAF-005 §4]. Replacement PPE is stocked in the crib at no cost, with no approval needed and no limit on safety-critical replacements [SAF-005 §4].

**Citations in answer:** `SAF-003 §3`, `SAF-005 §4` — all supported

---

<a id="q12"></a>
## q12 — single-hop

**Q:** Our gage R&R came back at 25 percent. Can we still use that gage?

| | expected | actual |
|---|---|---|
| route | `['quality']` | `['quality']` → **exact** |
| sections | `['QC-006 §5']` | found `['QC-006 §5']` → **full** |

**Router reasoning:** _Gage calibration and capability are quality topics._  
**Confidence:** overall **0.65 (medium)** — router 0.95 × retrieval 0.55 | band `moderate` (top1 0.680, mean3 0.674) — relevant material found, may be partial

<details><summary>Retrieved context (4 chunks)</summary>

| # | score | citation | category | section | expected |
|---|---|---|---|---|---|
| 1 | 0.680 | `QC-006 §3` | quality | Control of gages |  |
| 2 | 0.673 | `QC-006 §4` | quality | When a gage is found out of calibration |  |
| 3 | 0.669 | `QC-006 §5` | quality | Measurement System Analysis | **YES** |
| 4 | 0.592 | `QC-003 §4` | quality | Operator response to an out-of-control signa |  |

</details>

**Answer:**

> Yes — you can still use the gage, but only with Quality Manager approval.
> 
> Per the MSA acceptance table, a % Gage R&R between 10% and 30% is **conditionally acceptable**: usable only with Quality Manager approval, based on the characteristic's criticality and the cost of improvement [QC-006 §5].
> 
> Before using it, confirm the **ndc is ≥ 5** — an ndc below 5 means the gage cannot resolve process variation well enough to chart it, regardless of the R&R percentage [QC-006 §5].
> 
> Also note: if this gage is on a control plan, MSA is required before production acceptance and must be repeated after any change to the gage, method, or fixturing [QC-006 §5].

**Citations in answer:** `QC-006 §5` — all supported

---

<a id="q13"></a>
## q13 — single-hop

**Q:** What is the crane capacity for lifting a mold, and what do I check before rigging?

| | expected | actual |
|---|---|---|
| route | `['safety']` | `['safety', 'maintenance']` → **over-broad** |
| sections | `['SAF-007 §7']` | found `['SAF-007 §7']` → **full** |

**Router reasoning:** _Crane capacity and rigging checks are safety, but mold changes are maintenance._  
**Confidence:** overall **0.97 (high)** — router 0.90 × retrieval 1.00 | band `strong` (top1 0.819, mean3 0.749) — close match in the documentation

<details><summary>Retrieved context (8 chunks)</summary>

| # | score | citation | category | section | expected |
|---|---|---|---|---|---|
| 1 | 0.819 | `SAF-007 §7` | safety | Overhead crane and mold handling | **YES** |
| 2 | 0.715 | `MNT-002 §5` | maintenance | Mold installation |  |
| 3 | 0.712 | `MNT-002 §4` | maintenance | Mold removal |  |
| 4 | 0.707 | `SAF-007 §6` | safety | Load handling |  |
| 5 | 0.626 | `SAF-001 §3` | safety | Energy sources present on a molding cell |  |
| 6 | 0.625 | `SAF-001 §5` | safety | Press-specific isolation notes |  |
| 7 | 0.623 | `MNT-007 §3` | maintenance | Torque specifications — Mold clamping — grad |  |
| 8 | 0.618 | `MNT-005 §2` | maintenance | TCU-90 operating parameters |  |

</details>

> **SAFETY OVERLAY FIRED** — This answer draws on safety documentation. Safety requirements are preconditions, not suggestions — do not begin the task until they are met.

**Answer:**

> The bay crane rated capacity is **3,200 kg**. Before rigging, verify the mold's stamped weight; if the stamp is missing or illegible, do not lift — consult the tool record [SAF-007 §7].
> 
> Before the lift, also:
> - Only trained riggers may rig a lift. One designated signal person per lift; the crane operator takes signals from that person only — except a stop signal, which is accepted from anyone [SAF-007 §7].
> - Inspect slings, shackles, and eyebolts before every lift. Remove from service any sling with cuts, broken strands, heat damage, or a missing/illegible capacity tag [SAF-007 §7].
> - Lift eyebolts must be fully seated and rated for the mold half's weight [SAF-007 §7].
> - Never stand or reach under a suspended load. Establish an exclusion zone and keep hands off the load — use a tag line to control swing [SAF-007 §7].
> - Lift 50 mm, stop, and confirm balance and brake hold before continuing [SAF-007 §7].
> 
> Note: Mold removal also requires verifying sling condition and capacity tag per SAF-007 §7 [MNT-002 §4].

**Citations in answer:** `MNT-002 §4`, `SAF-007 §7` — all supported

---

<a id="q14"></a>
## q14 — single-hop

**Q:** If the evacuation alarm sounds while I'm in Bay 2, where do I go?

| | expected | actual |
|---|---|---|
| route | `['safety']` | `['safety']` → **exact** |
| sections | `['SAF-006 §3']` | found `['SAF-006 §3']` → **full** |

**Router reasoning:** _Evacuation procedures are a safety topic._  
**Confidence:** overall **0.85 (medium)** — router 1.00 × retrieval 0.80 | band `moderate` (top1 0.738, mean3 0.700) — relevant material found, may be partial

<details><summary>Retrieved context (4 chunks)</summary>

| # | score | citation | category | section | expected |
|---|---|---|---|---|---|
| 1 | 0.738 | `SAF-006 §2` | safety | Alarm signals |  |
| 2 | 0.694 | `SAF-006 §7` | safety | Severe weather |  |
| 3 | 0.668 | `SAF-006 §3` | safety | Evacuation | **YES** |
| 4 | 0.581 | `SAF-007 §5` | safety | Blind corners and high-traffic points |  |

</details>

> **SAFETY OVERLAY FIRED** — This answer draws on safety documentation. Safety requirements are preconditions, not suggestions — do not begin the task until they are met.

**Answer:**

> Go to **Point A** — the north parking lot, by the flagpole. Bay 2 is in Bays 1–4 (molding), which reports to Point A [SAF-006 §3].
> 
> Before evacuating, press **Cycle Stop** only if you can do so in under 5 seconds. Do not attempt to complete a cycle, finish a part, or shut down heats — equipment is replaceable [SAF-006 §3].
> 
> Leave belongings, do not use the freight elevator, and exit by the nearest marked route (primary and secondary routes are posted at every cell). Remain at Point A until released by a warden [SAF-006 §3].
> 
> Do not cross the truck court to reach a different point — report to whichever point your exit leads to and tell the warden where you normally work [SAF-006 §3].

**Citations in answer:** `SAF-006 §3` — all supported

---

<a id="q15"></a>
## q15 — single-hop

**Q:** What is the maximum moisture content for polycarbonate before molding?

| | expected | actual |
|---|---|---|
| route | `['maintenance']` | `['quality', 'maintenance']` → **over-broad** |
| sections | `['MNT-004 §2']` | found `['MNT-004 §2']` → **full** |

**Router reasoning:** _Incoming material spec is quality, but drying is a maintenance task._  
**Confidence:** overall **0.84 (medium)** — router 0.85 × retrieval 0.83 | band `moderate` (top1 0.746, mean3 0.716) — relevant material found, may be partial

<details><summary>Retrieved context (8 chunks)</summary>

| # | score | citation | category | section | expected |
|---|---|---|---|---|---|
| 1 | 0.746 | `MNT-004 §2` | maintenance | Drying parameters by material | **YES** |
| 2 | 0.718 | `MNT-004 §1` | maintenance | Why drying matters |  |
| 3 | 0.684 | `QC-001 §5` | quality | Sampling and testing |  |
| 4 | 0.665 | `QC-004 §3` | quality | Defect catalog — Splay (silver streaking) |  |
| 5 | 0.664 | `QC-006 §6` | quality | Moisture analyzer method |  |
| 6 | 0.664 | `QC-001 §6` | quality | Shelf life and stock rotation |  |
| 7 | 0.664 | `MNT-002 §2` | maintenance | Pre-change preparation (while the press is s |  |
| 8 | 0.636 | `MNT-005 §4` | maintenance | Water treatment |  |

</details>

**Answer:**

> The maximum moisture content for polycarbonate (PC) before molding is **0.02%** [MNT-004 §2].
> 
> This is the at-press limit, meaning it applies after drying and immediately before molding [MNT-004 §2]. The drying parameters to achieve this are a drying temperature of **120 °C** with a minimum residence time of **4 hours** and a target dryer dew point of **−40 °C** [MNT-004 §2]. Do not exceed the drying temperature—over-drying degrades PC and can cause yellowing, embrittlement, and volatile generation [MNT-004 §2].
> 
> Note that moisture at receipt is checked against the supplier's as-shipped spec, not this at-press limit [QC-001 §5].

**Citations in answer:** `MNT-004 §2`, `QC-001 §5` — all supported

---

<a id="q16"></a>
## q16 — single-hop

**Q:** A customer just complained about a defect. How fast do we have to contain it?

| | expected | actual |
|---|---|---|
| route | `['quality']` | `['quality']` → **exact** |
| sections | `['QC-007 §1']` | found `['QC-007 §1']` → **full** |

**Router reasoning:** _Customer complaint/CAPA is a quality topic._  
**Confidence:** overall **0.72 (medium)** — router 0.90 × retrieval 0.66 | band `moderate` (top1 0.704, mean3 0.685) — relevant material found, may be partial

<details><summary>Retrieved context (4 chunks)</summary>

| # | score | citation | category | section | expected |
|---|---|---|---|---|---|
| 1 | 0.704 | `QC-007 §1` | quality | Response clock | **YES** |
| 2 | 0.696 | `QC-007 §2` | quality | Containment first, always |  |
| 3 | 0.655 | `QC-005 §2` | quality | Immediate containment |  |
| 4 | 0.654 | `QC-007 §7` | quality | Internal escalation |  |

</details>

**Answer:**

> Containment actions must be in place within **24 hours** of the complaint [QC-007 §1]. This clock does not pause for shifts or weekends [QC-007 §1].
> 
> Before any investigation begins, you must follow the containment-first sequence [QC-007 §2]:
> 
> 1. Quarantine suspect stock at the plant per QC-005 §2 [QC-007 §2].
> 2. Bound the population back to the last known-good verification point [QC-007 §2].
> 3. Determine what has shipped, to whom, and when, using internal lot ID traceability [QC-007 §2].
> 4. Notify the customer of affected shipments — dates, quantities, lot IDs [QC-007 §2].
> 5. Institute 100% inspection or a certified-stock process for continuing shipments, with clear visual identification (a certified-lot label) [QC-007 §2].
> 
> **Safety precondition:** Never ship unprotected product into an open complaint to keep a line running. If supply is at risk, that is a conversation with the customer, not a decision made on the floor [QC-007 §2].
> 
> Note: Containment is never extended — if root cause is still unknown at 24 hours, containment stays in force and typically escalates to 100% inspection [QC-007 §1].

**Citations in answer:** `QC-007 §1`, `QC-007 §2` — all supported

---

<a id="q17"></a>
## q17 — single-hop

**Q:** Oil temperature on the press is reading 62 C. Is that a problem?

| | expected | actual |
|---|---|---|
| route | `['maintenance']` | `['maintenance']` → **exact** |
| sections | `['MNT-003 §3']` | found `['MNT-003 §3']` → **full** |

**Router reasoning:** _Hydraulic oil temperature is a maintenance parameter, but the question lacks context for a definitive answer._  
**Confidence:** overall **0.58 (medium)** — router 0.85 × retrieval 0.49 | band `moderate` (top1 0.665, mean3 0.655) — relevant material found, may be partial

<details><summary>Retrieved context (4 chunks)</summary>

| # | score | citation | category | section | expected |
|---|---|---|---|---|---|
| 1 | 0.665 | `MNT-003 §3` | maintenance | Pressure and temperature reference | **YES** |
| 2 | 0.661 | `MNT-001 §6` | maintenance | Oil analysis program |  |
| 3 | 0.640 | `MNT-001 §2` | maintenance | Daily — operator, start of shift |  |
| 4 | 0.638 | `MNT-001 §4` | maintenance | 500 operating hours |  |

</details>

**Answer:**

> Yes — 62 °C is a problem. Stop and investigate.
> 
> Per the pressure and temperature reference, oil temperature above **60 °C** is in the **Stop** column: "> 60 °C — stop and investigate" [MNT-003 §3]. Oil above 60 °C degrades rapidly and softens seals; every 10 °C above 60 °C roughly halves oil life. Do not run production to the end of a shift with oil over 60 °C [MNT-003 §3].
> 
> Normal operating oil temperature is **40–55 °C**; 55–60 °C is the "investigate" band [MNT-003 §3]. At 62 °C you are past that band, so stop the press and investigate the cause before resuming.
> 
> Note: the documentation excerpts do not specify what to check once you stop. The most likely document to hold the full troubleshooting procedure is MNT-003 (Hydraulic System Troubleshooting), which is the source of the temperature reference table.

**Citations in answer:** `MNT-003 §3` — all supported

---

<a id="q18"></a>
## q18 — single-hop

**Q:** I found a gaylord of resin on the floor with no status tag on it. What now?

| | expected | actual |
|---|---|---|
| route | `['quality']` | `['quality', 'maintenance']` → **over-broad** |
| sections | `['QC-001 §2']` | found `['QC-001 §2']` → **full** |

**Router reasoning:** _Untagged material is a nonconforming material issue, but it may also involve resin handling and dryer maintenance._  
**Confidence:** overall **0.63 (medium)** — router 0.80 × retrieval 0.57 | band `moderate` (top1 0.685, mean3 0.641) — relevant material found, may be partial

<details><summary>Retrieved context (8 chunks)</summary>

| # | score | citation | category | section | expected |
|---|---|---|---|---|---|
| 1 | 0.685 | `QC-001 §2` | quality | Material status states | **YES** |
| 2 | 0.628 | `QC-005 §2` | quality | Immediate containment |  |
| 3 | 0.611 | `MNT-004 §4` | maintenance | Maintenance schedule |  |
| 4 | 0.606 | `QC-005 §4` | quality | Material Review Board (MRB) |  |
| 5 | 0.599 | `QC-001 §7` | quality | Release |  |
| 6 | 0.586 | `MNT-004 §5` | maintenance | Conveying system |  |
| 7 | 0.580 | `MNT-002 §8` | maintenance | Post-run tool care |  |
| 8 | 0.569 | `MNT-002 §7` | maintenance | Changeover record |  |

</details>

**Answer:**

> Untagged material is treated as **quarantine, not released** — do not use it. Move it to the receiving hold area and investigate it as a nonconformance [QC-001 §2].
> 
> Before anything else, follow the immediate containment steps [QC-005 §2]:
> 1. **Stop** — do not produce into this material.
> 2. **Red-tag** the gaylord with part number, quantity, date, defect found (untagged), and your name.
> 3. **Move it to the quarantine cage** in the NE corner of the plant — physically separated, not just marked.
> 4. **Notify** the supervisor and QC within the shift.
> 5. **Bound the population** — determine how much material is affected.
> 
> Red-tagged material may not be moved, reworked, shipped, or consumed by anyone except QC [QC-005 §2]. The MRB must disposition the nonconformance within 3 business days of the red tag [QC-005 §4].
> 
> Note: the documentation excerpts do not specify whether an untagged gaylord of resin is treated as a "lot" for MRB disposition purposes, but the untagged-material rule in [QC-001 §2] is explicit. If you need the full nonconformance investigation procedure, that would be in QC-005 (the containment section is excerpted here, but the full document likely covers the investigation steps).

**Citations in answer:** `QC-001 §2`, `QC-005 §2`, `QC-005 §4` — all supported

---

<a id="q19"></a>
## q19 — single-hop

**Q:** The light curtain on press 6 keeps tripping intermittently. Can we keep running?

| | expected | actual |
|---|---|---|
| route | `['safety']` | `['safety', 'maintenance']` → **over-broad** |
| sections | `['SAF-002 §8']` | found `['SAF-002 §8']` → **full** |

**Router reasoning:** _Light curtain is a safety device, but intermittent tripping is a maintenance issue._  
**Confidence:** overall **0.67 (medium)** — router 0.95 × retrieval 0.57 | band `moderate` (top1 0.685, mean3 0.610) — relevant material found, may be partial

<details><summary>Retrieved context (8 chunks)</summary>

| # | score | citation | category | section | expected |
|---|---|---|---|---|---|
| 1 | 0.685 | `SAF-002 §8` | safety | Damaged or nuisance-tripping devices | **YES** |
| 2 | 0.582 | `SAF-002 §3` | safety | Daily pre-shift verification (operator) |  |
| 3 | 0.563 | `MNT-001 §7` | maintenance | Work order priority definitions |  |
| 4 | 0.559 | `SAF-001 §4` | safety | Required six-step sequence |  |
| 5 | 0.555 | `MNT-001 §6` | maintenance | Oil analysis program |  |
| 6 | 0.548 | `MNT-002 §6` | maintenance | Startup |  |
| 7 | 0.544 | `SAF-004 §5` | safety | Spill response — the SWIM sequence |  |
| 8 | 0.528 | `MNT-003 §4` | maintenance | Leaks |  |

</details>

> **SAFETY OVERLAY FIRED** — This answer draws on safety documentation. Safety requirements are preconditions, not suggestions — do not begin the task until they are met.

**Answer:**

> No. Stop the cell and tag it out. A light curtain that trips intermittently is treated as a **failed** device, not a nuisance [SAF-002 §8]. A cell with a failed safety device may not run production under any circumstance [SAF-002 §3].
> 
> Before raising the work order, clean the lens with the supplied optical wipe only — do not use purge solvent or compressed air with oil carryover. Common causes are misalignment after a mold change, resin dust on the lens, and vibration from an adjacent cell [SAF-002 §8].
> 
> If the device still faults after cleaning, tag out and raise a maintenance work order. Note: a failed light curtain is **always P1**, never P2, regardless of production pressure [MNT-001 §7]. The cell does not run until it is corrected [MNT-001 §7].

**Citations in answer:** `MNT-001 §7`, `SAF-002 §3`, `SAF-002 §8` — all supported

---

<a id="q20"></a>
## q20 — cross-cutting

**Q:** How many stabilization shots do I run before pulling first article samples?

| | expected | actual |
|---|---|---|
| route | `['quality', 'maintenance']` | `['quality', 'maintenance']` → **exact** |
| sections | `['QC-002 §2', 'MNT-002 §6']` | found `['MNT-002 §6', 'QC-002 §2']` → **full** |

**Router reasoning:** _First article inspection is quality, but the shot count is tied to process stabilization, which is a maintenance/process setup topic._  
**Confidence:** overall **0.82 (medium)** — router 0.85 × retrieval 0.81 | band `moderate` (top1 0.740, mean3 0.689) — relevant material found, may be partial

<details><summary>Retrieved context (8 chunks)</summary>

| # | score | citation | category | section | expected |
|---|---|---|---|---|---|
| 1 | 0.740 | `QC-002 §2` | quality | Sample preparation | **YES** |
| 2 | 0.688 | `QC-002 §5` | quality | Last-off sample |  |
| 3 | 0.639 | `QC-001 §5` | quality | Sampling and testing |  |
| 4 | 0.633 | `QC-004 §4` | quality | Limit samples |  |
| 5 | 0.626 | `MNT-001 §6` | maintenance | Oil analysis program |  |
| 6 | 0.607 | `MNT-001 §4` | maintenance | 500 operating hours |  |
| 7 | 0.589 | `MNT-002 §6` | maintenance | Startup | **YES** |
| 8 | 0.587 | `MNT-002 §2` | maintenance | Pre-change preparation (while the press is s |  |

</details>

**Answer:**

> Run **10 stabilization shots to scrap** before pulling first article samples [QC-002 §2]. Parts from those shots are never submitted — the process is not yet at steady state [QC-002 §2].
> 
> After the 10 scrap shots, take **5 consecutive parts** (all cavities on a multi-cavity tool) for the First Article Inspection [QC-002 §2]. Label each part with cavity number, date, time, press, and shift — unlabeled samples are rejected by the lab [QC-002 §2].
> 
> This same sequence is confirmed in the mold change startup procedure: run 10 stabilization shots to scrap, then take 5 consecutive parts for FAI, and production does not start until QC approves the FAI [MNT-002 §6].

**Citations in answer:** `MNT-002 §6`, `QC-002 §2` — all supported

---

<a id="q21"></a>
## q21 — cross-cutting

**Q:** Someone spilled hydraulic oil under press 3. What do I do?

| | expected | actual |
|---|---|---|
| route | `['safety', 'maintenance']` | `['safety', 'maintenance']` → **exact** |
| sections | `['SAF-004 §5', 'MNT-003 §4']` | found `['MNT-003 §4', 'SAF-004 §5']` → **full** |

**Router reasoning:** _Spill cleanup is a safety procedure, but hydraulic oil is a maintenance fluid._  
**Confidence:** overall **0.78 (medium)** — router 0.95 × retrieval 0.72 | band `moderate` (top1 0.721, mean3 0.702) — relevant material found, may be partial

<details><summary>Retrieved context (8 chunks)</summary>

| # | score | citation | category | section | expected |
|---|---|---|---|---|---|
| 1 | 0.721 | `SAF-004 §5` | safety | Spill response — the SWIM sequence | **YES** |
| 2 | 0.703 | `MNT-003 §5` | maintenance | Water in oil |  |
| 3 | 0.682 | `MNT-003 §4` | maintenance | Leaks | **YES** |
| 4 | 0.681 | `SAF-004 §4` | safety | Solvent use and ventilation |  |
| 5 | 0.661 | `MNT-001 §6` | maintenance | Oil analysis program |  |
| 6 | 0.653 | `MNT-001 §4` | maintenance | 500 operating hours |  |
| 7 | 0.631 | `SAF-006 §3` | safety | Evacuation |  |
| 8 | 0.602 | `SAF-006 §5` | safety | Fire |  |

</details>

> **SAFETY OVERLAY FIRED** — This answer draws on safety documentation. Safety requirements are preconditions, not suggestions — do not begin the task until they are met.

**Answer:**

> **Stop the source first, then warn others, isolate the area, and manage the cleanup** — the SWIM sequence from SAF-004 §5 [SAF-004 §5].
> 
> **Before cleanup:** If the spill is **large, unknown material, or reaches a floor drain**, do not attempt cleanup. Evacuate the immediate area and call extension **4111** [SAF-004 §5]. Floor drains in Bays 1–4 discharge to the storm system — any release to a drain is a reportable environmental event and must be reported to EHS within **1 hour** [SAF-004 §5].
> 
> **For a small spill (< 20 L, known material, no injury):** Trained floor personnel may clean up using the nearest spill kit (yellow bins at Bays 2, 5, and 8). Absorb with pads, place used pads in the labeled waste drum, and complete the spill log at the EHS station [SAF-004 §5].
> 
> **Specific to hydraulic oil:** Use **oil-only absorbent socks** — do not use floor-dry granules within the guard envelope, as they migrate into the tie-bar area and contaminate parts [SAF-004 §5].
> 
> **After cleanup:** Hydraulic oil spills under a press are almost always a symptom, not just a mess. Raise a work order and reference MNT-003 §4 — a recurring leak at the same fitting indicates a failing seal or a hose approaching end of life [SAF-004 §5].
> 
> **Also note:** Any leak reaching the floor is a slip hazard and requires cleanup before the cell resumes, regardless of leak severity classification [MNT-003 §4]. If the leak is running or spraying, stop the press, isolate, and clean per SAF-004 §5 [MNT-003 §4].

**Citations in answer:** `MNT-003 §4`, `SAF-004 §5` — all supported

---

<a id="q22"></a>
## q22 — out-of-scope

**Q:** What is the plant's vacation accrual policy?

| | expected | actual |
|---|---|---|
| route | `[] (out of scope)` | `[] (out of scope)` → **exact** |
| sections | `—` | found `—` → **n/a** |

**Router reasoning:** _HR policy is not covered by plant documentation._  
**Confidence:** overall **0.25 (low)** — router 1.00 × retrieval 0.00 | band `none` (top1 0.000, mean3 0.000) — nothing retrieved

**Answer:**

> That falls outside the Plant 4 documentation set, which covers safety procedures, maintenance manuals, and quality standards. For this, contact HR or your supervisor.

**Citations in answer:** — — all supported

---
