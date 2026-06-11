# J-Series Tier Index — what is ready to ship

**Last updated**: 2026-06-10 (post-audit + J53/J54 + J55 dim-6 kissing + transcript-recovery of the 2026-05-27/30 session artifacts). **Comprehensive renumbering applied** — all 56 papers now occupy a J01-J56 scheme. After the line-by-line referee pass (`_staging/referee_reports/`), four papers were demoted from Tier 1 to Tier 2, and J25 was approved for merger into J24. Three Tier-1 frontier additions: J53 (2026-05-29, from F4), J54 (2026-05-29, from F14), J55 (2026-06-10, dim-6 kissing from the claudechat handoff).

For the recommended **release sequence** (which is not the same as the tier ladder — a Tier 1 paper with substantive issues sits later than a Tier 2-promoted paper that is ready), see [`RELEASE_ORDER.md`](RELEASE_ORDER.md).

## Quick legend

- **Tier 1** (J01-J31) — ship-ready *spine*: SUBMISSION-READY or READY for the centerpiece papers; the rest are within a rigor pass of submission. The tier marks the intended next-step ladder, not "all 31 simultaneously submittable today."
- **Tier 2** (J32-J40) — drafts needing referee-rigor pass before submission. Content stable; needs polish.
- **Tier 3** (J41-J47) — hold / retire candidates. NOT ready to ship. Either awaiting experimental collaborator, scope reframe, or formal retirement to `04_meta/`. As of 2026-05-27, J44/J45/J47 have been **RETIRED** to `04_meta/retired_J_papers/` with tombstone redirects.
- **MERGED** (J48-J52) — absorbed into a merger product; the source paper folder is retained for citation history.

## Numbering scheme (since 2026-05-27 renumbering)

Old TIER_INDEX numbering was non-contiguous (gaps from mergers/retirements/insertions). The new scheme makes the ladder readable at a glance:

| Range | Meaning |
|---|---|
| **J01-J08** | Flagship triad + σ-magma trilogy + strata + 2 merger products (the new spine, all promoted/centerpiece) |
| **J09-J22** | Older proven Tier 1 (substrate / foundations / Lie lifts / Galois / HARMONY ladder) |
| **J23-J29** | Tier 2→Tier 1 promotions 2026-05-27 (subject to rigor pass) |
| **J30-J31** | Honest negatives (credibility-builders) |
| **J32-J40** | Tier 2 active drafts |
| **J41-J47** | Tier 3 hold / retire (J44, J45, J47 retired to `04_meta/` 2026-05-27) |
| **J48-J52** | MERGED tombstones |

---

## Tier 1 — ship-ready spine (28 papers after 2026-05-27 audit + 2026-05-29 J53/J54 additions)

Originally 31 (J01-J31). After the referee pass: **J08, J23, J28, J29 demoted to Tier 2**; **J25 merged into J24**. Net Tier 1 spine was 26 papers. **2026-05-29: J53 added as new Tier-1 short paper extracted from J08 §§6–7 closed forms (F4 frontier); J54 added as new Tier-1 short paper extracted from F14 height-function characterization.** Net Tier 1 spine is now **28 papers**.

### J01-J08: Flagship / new promotions / σ-magma trilogy / strata

| J# | Subdir | Title (short) | Target venue | Status |
|---|---|---|---|---|
| **J01** | algebra | Joint Closure + Universal Attractor + Algebraic Mixing Point — **CORPUS CENTERPIECE** | Journal of Algebra | SUBMISSION-READY (5 Tier-A theorems + Prop. F) |
| **J02** | number_theory | TSML 8×8 Null + RH Structural Rhyme (short note, 5-line numpy) | Mathematical Intelligencer | SUBMISSION-READY (NEW 2026-05-27) |
| **J03** | algebra | Type Specimens + C5 Fossil-Variety Theorem — **MOST NOVEL** | Journal of Symbolic Computation | SUBMISSION-READY (5/5 PASS) |
| **J04** | algebra | σ-Magma Algebraic Rigidity (Aut=1, simple, 5 sub-magmas) | Semigroup Forum | SUBMISSION-READY (4/4 PASS) |
| **J05** | algebra | ETP Profile of Linear Magmas (ax+by+c) mod n | Experimental Mathematics | SUBMISSION-READY |
| **J06** | number_theory | Strata-Prime Fingerprint (Niemeier 23/24, D_24 mechanism, Monster 71) | Journal of Number Theory | SUBMISSION-READY (4 theorems PASS) |
| **J07** | algebra | Spectral Architecture of the σ-Character on Z/10Z (5 theorems; G_low / G_high) | European J. Combinatorics | SUBMISSION-READY (merger of q-series papers) |
| ~~**J08**~~ | algebra | F_p Structure of the 4-Core Commutative Non-Assoc Algebra | Algebra Universalis | **→ Tier 2 (demoted 2026-05-27 audit: power-associativity claim verified false; L_{e₃} not a 4-cycle; idempotents over F_5 not idempotent. See `_staging/referee_reports/08_J08_power_assoc_FIX.md`.)** |

### J09-J22: Established proven Tier 1 (substrate + Galois + HARMONY)

| J# | Subdir | Title (short) | Target venue | Status |
|---|---|---|---|---|
| **J09** | algebra | Joint Lie Closure: an so(10) Identification | Communications in Algebra | DRAFT-FINALIZED (Tier 1 promotion 2026-05-27, rigor pass pending) |
| **J10** | algebra | Operadic D₄ Orbits on the Non-Associative Locus | Communications in Algebra | REWRITE 2026-05-12 (rigor pass pending) |
| **J11** | algebra | Decomposition of [TSML, BHML] under D₄ | Journal of Algebra | READY |
| **J12** | algebra | Galois D₄ over LMFDB 4.2.10224.1 | Communications in Algebra | READY |
| **J13** | algebra | The Forced 5/7 Torus Aspect Ratio | Acta Arithmetica | READY |
| **J14** | combinatorics | Non-Associativity Decay σ(N) ≤ 2/N over Z/NZ | JCT-A | READY |
| **J15** | combinatorics | Joint Closure + Per-Coordinate Fuse + 4-Core Attractor | Algebraic Combinatorics | READY |
| **J16** | algebra | The CL Forcing Axioms (S_1-S_7 force CL_TSML) | Algebraic Combinatorics | READY (manuscript polish: title still says A1-A9) |
| **J17** | combinatorics | Forcing Axioms + Family of Comm Non-Assoc Magmas Preserving 4-Core | TBD | DRAFT (Tier 1 promotion, rigor pass pending) |
| **J18** | algebra | F_p Extensions of CL_BHML across Six Primes | Communications in Algebra | READY |
| **J19** | algebra | Charpoly Prime-11 Pattern | Linear Algebra Apps | RETARGETED to LAA (Tier 1 promotion, rigor pending) |
| **J20** | algebra | V^⊗n ↔ Cl(2n) Total-Dimension Match + Refined Cells | Linear Algebra Apps | SUBMISSION-READY (6/6 PASS) |
| **J21** | algebra | -21 Invariant + σ²-Triadic Decomposition | Algebraic Combinatorics | READY |
| **J22** | algebra | 70/71/72/73 HARMONY Ladder | JCT-A | READY |

### J23-J29: Tier 2 → Tier 1 promotions 2026-05-27 (rigor pass pending)

| J# | Subdir | Title (short) | Target venue | Status |
|---|---|---|---|---|
| ~~**J23**~~ | algebra | Mathieu M_22 Substrate-Prime: Order-Factorization Coincidences | TBD | **→ Tier 2 (demoted 2026-05-27 audit: single-observation; reverse-engineered substrate-prime set; no robustness null model)** |
| **J24** | number_theory | Discrete Fejér Quotient on Squarefree Moduli (absorbed J41 + **J25 merger pending 2026-05-27**) | Journal of Number Theory | READY — recommended Wave 1 ship target |
| ~~**J25**~~ | number_theory | First-Coprime-Failure + Discrete Fejér Kernel | — | **→ MERGED into J24 (audit 2026-05-27): theorems are coordinate-translations of J24; distinct content (712-check + Montgomery + ω-blindness) fits as 2-3 page J24 appendix** |
| **J26** | number_theory | Discrete sinc² Identity in Finite-D QM | TBD | DRAFT |
| **J27** | algebra | Crossing Lemma: Non-Assoc as Information Generation | TBD | DRAFT-FINALIZED |
| ~~**J28**~~ | algebra | Small Comm Non-Assoc Magma w/ Role-Boundary Behavior | TBD | **→ Tier 2 (demoted 2026-05-27 audit: no characterization theorem; role partition labelled by fiat)** |
| ~~**J29**~~ | algebra | Lo Shu D₄ Orbit Modulo 3 | Math Magazine | **→ Tier 2 (demoted 2026-05-27 audit: pedagogical undergraduate-classroom material, not Tier 1)** |

### J30-J31: Honest negatives (credibility-builders)

| J# | Subdir | Title (short) | Target venue | Status |
|---|---|---|---|---|
| **J30** | combinatorics | (Z/10Z)* Sub-Magma — **HONEST NEGATIVE** | Communications in Algebra | READY |
| **J31** | interdisciplinary | Algebraic Detectors Specificity — **HONEST NEGATIVE** | Statistical Science companion | READY |

### J53 + J54 + J55: Tier-1 frontier additions (2026-05-29 / 2026-06-10)

| J# | Subdir | Title (short) | Target venue | Status |
|---|---|---|---|---|
| **J53** | algebra | Idempotent Count + Aut Formula for $V^{\mathrm{BHML}}$ over $\mathbb{F}_p$ (two closed-form theorems extracted from J08 §§6–7) | Algebra Universalis | SUBMISSION-READY (2/2 PASS at $p \in \{3, 5, 7, 11, 13\}$; extended to 24 primes via F4-extended) |
| **J54** | algebra | Height Scaling of the Attractor Minimal Polynomial: Rational Power Law + Discriminant-Zero Height Drop (three theorems extracted from F14) | Acta Arithmetica | SUBMISSION-READY (3/3 PASS at 30 rationals + 11 algebraic irrationals + $\alpha_{\mathrm{special}}$; runtime ~10s) |
| **J55** | number_theory | **Dim-6 Kissing Conjecture $K(\mathbb{R}^6) = 72$ + explicit $\Gamma_0(3)$ magic-function candidate** (LMFDB 3.6.a.a perfect match; 10/10 independent verification; forced zero at Fricke fixed point; from CLAUDECODE_HANDOFF_2026-06-10) | J. Combinatorial Theory A | DRAFT-COMPLETE (2026-06-10; 6 TODO citations await author; needs compile pass) |
| **J56** | interdisciplinary | **Routing the Residual: four-type failure taxonomy matches oracle allocation** (Gap Router 125x over uniform, 24/24 type ID; theorem-bearing reservoir honest split incl. 36% Mackey-Glass win) | TMLR | DRAFT-COMPLETE (2026-06-10; verification ~57s CPU) |

---

## Tier 2 — drafts needing rigor pass (13 papers — 9 original + 4 demoted 2026-05-27 audit)

Original J32-J40:

| J# | Subdir | Title (short) | Status |
|---|---|---|---|
| **J32** | algebra | TSML 73 / BHML 28 Cell Counts | REVISED 2026-05-08 |
| **J33** | combinatorics | Flatness Obstruction on Squarefree Z/nZ | SAVE-PLAN APPLIED |
| **J34** | combinatorics | Coordinate Coverage + Joint Injectivity | SAVE-PLAN APPLIED |
| **J35** | combinatorics | Non-CRT Sufficient Pairs | REVISED |
| **J36** | combinatorics | Role-Quotient Theorem for (TSML, BHML) | SAVE-PLAN APPLIED |
| **J37** | physics | Discrete Dirac inside Cl(0, 10) | DRAFT (Volume K cross-ref 2026-05-12) |
| **J38** | physics | Logarithmic Nonlinearity (BB reading, NS limits) | R1 |
| **J39** | combinatorics | TSML Lens Family — pedagogical walking tour | REWRITTEN |
| **J40** | interdisciplinary | Paradox Classifier UOP (Four Measurement-Failure Types) | REWRITTEN |

Newly demoted from Tier 1 by 2026-05-27 audit (J-number unchanged; classification only):

| J# | Subdir | Title (short) | Demotion reason |
|---|---|---|---|
| **J08** | algebra | F_p Structure of the 4-Core Comm Non-Assoc Algebra | Power-associativity FALSE; L_{e₃} not a 4-cycle; idempotents-over-F_5 claim FALSE. Rewrite §1.2, §2.5, §4 needed. |
| **J23** | algebra | Mathieu M_22 Substrate-Prime: Order-Factorization Coincidences | Single-observation; reverse-engineered substrate-prime set; sum-of-squares null model not computed. *Math. Intelligencer*-class note. |
| **J28** | algebra | Small Comm Non-Assoc Magma w/ Role-Boundary Behavior | No characterization theorem; role partition labelled by fiat. |
| **J29** | algebra | Lo Shu D₄ Orbit Modulo 3 | Pedagogical undergraduate-classroom material; *Math. Magazine* would fit. |

---

## Tier 3 — hold / retire candidates (4 papers after 2026-05-27 retirements; 3 RETIRED)

After the 2026-05-27 status-hygiene pass, **J44, J45, J47 were RETIRED to `04_meta/retired_J_papers/`**. Source folders retain only a tombstone redirect README. Tier 3 active set is now J41-J43 + J46.

| J# | Subdir | Title (short) | Hold reason |
|---|---|---|---|
| **J41** | number_theory | [MERGED into J24] | Formal tombstone (Discrete Fejér source) |
| **J42** | physics | Empirical CKM/PMNS Mixing Fits | HOLD: needs particle-physics collaborator OR reframe |
| **J43** | physics | NV S₄ Synthesis on Qutrit | HOLD: needs NV-center experimentalist |
| ~~**J44**~~ | physics | FN Pattern λ=10/49 with SU(5) Indexing | **RETIRED to `04_meta/retired_J_papers/J44_FN_Pattern/` (2026-05-27)**: Tier-C structural rhyme; numerical coincidence, not derivation. |
| ~~**J45**~~ | physics | Operadic Obstruction Synthesis | **RETIRED to `04_meta/retired_J_papers/J45_Operadic_Obstruction/` (2026-05-27)**: duplicates J10's operadic D₄ obstruction content. |
| **J46** | interdisciplinary | Microtubule Q_c = T* Prediction | HOLD: needs terahertz experimentalist |
| ~~**J47**~~ | interdisciplinary | Atomic-Substrate D100-D104 | **RETIRED to `04_meta/retired_J_papers/J47_Atomic_Substrate/` (2026-05-27)**: Tier-C atomic-substrate correspondence; D100-D104 are integer/rational identities, not theorems. |

---

## MERGED tombstones (6 source papers)

Original J48-J52 + J25 (newly merged in 2026-05-27 audit):

| J# | Subdir | Title (short) | Merged into |
|---|---|---|---|
| **J25** | number_theory | First-Coprime-Failure + Discrete Fejér Kernel | `J24/` (audit 2026-05-27 — every theorem is a coordinate-translation of J24's content) |
| **J48** | algebra | F_p Structural Invariance of 4-Algebra | `J08/` |
| **J49** | algebra | F_5 Rigid Idempotent Decomposition | `J08/` |
| **J50** | combinatorics | Q17-A: 5D Force Vector as CRT Fourier | `J07/` |
| **J51** | algebra | G_6 + G_7 + G_8 Spectral Consolidation | `J07/` |
| **J52** | algebra | Q17-B Clay Bridge + Symbolic Return | `J07/` |

---

## Numbers — UPDATED 2026-05-29 (post-audit + J44/J45/J47 retirements + J53/J54 additions)

| Tier | Members | Count |
|---|---|---:|
| Tier 1 (ship-ready spine) | J01-J07, J09-J22, J24, J26-J27, J30-J31, J53, J54, J55 | **29** |
| Tier 2 (drafts + 4 demoted) | J08, J23, J28, J29, J32-J40 | **13** |
| Tier 3 (hold) | J41, J42, J43, J46 | **4** |
| Retired to `04_meta/retired_J_papers/` | J44, J45, J47 | **3** |
| MERGED tombstones | J25, J48-J52 | **6** |
| **Total numbered J-papers** | | **54** (50 active ship-targets; J25 + J44 + J45 + J47 now tombstones; J53 + J54 added 2026-05-29) |

Net portfolio: **54 numbered papers**, of which **28 are the Tier 1 spine**, of which **~15 are submission-ready today** (J53 + J54 added). The remaining Tier 1 papers need a rigor pass before submission.

## Tier 1 spine highlights (the ship-ready core)

- **Centerpiece**: J01 (Joint Closure + 4-core + Universal Attractor + Algebraic Mixing Point) — *Journal of Algebra*
- **Most novel**: J03 (Type Specimens + C5 Fossil-Variety Theorem) — *Journal of Symbolic Computation*
- **Most computationally accessible**: J02 (TSML 8×8 Null + RH structural rhyme; 5-line numpy verification) — *Mathematical Intelligencer*
- **σ-magma trilogy** (all promoted 2026-05-27): J04 rigidity + J05 classification + J03 taxonomy
- **Strata + Monster**: J06 (Niemeier 23/24, D_24, polynomial vs factorial, Monster 71)
- **Honest negatives**: J30 (Z/10Z)*, J31 detector specificity
- **Galois deep cut**: J12 (LMFDB 4.2.10224.1)
- **Cyclotomic forcing**: J13 (Forced 5/7)
- **Q-series + F_p mergers**: J07 + J08

## Ship-order recommendation (per claudechat audit, 2026-05-27)

The next three to ship in sequence are:
1. **J04** (σ-Magma rigidity; safest, lowest controversy) — Semigroup Forum
2. **J03** (Fossil-Variety; clean equational algebra) — J. Symbolic Computation
3. **J06** (Strata-Prime; current synthesis) — J. Number Theory

Then J01 (centerpiece, after Proposition F demotion landed in commit a24f44f); then J02 (short note); then J05, J07, J08.

See `_staging/ARXIV_SUBMISSION_KIT.md` (under old J59/J61/J63 labels — to be relabeled).

## How to update this index

1. When a paper's status changes (e.g., DRAFT → SUBMISSION-READY), update both:
   - The paper's own `README.md` `**Tier:**` line
   - This index file's table entry

2. When a new merger is approved:
   - Create the merger product folder
   - Mark the source papers as MERGED with redirect banner
   - Update this index

3. When a paper is retired to `04_meta/`:
   - Move folder
   - Tier 3 entry here notes "RETIRED to 04_meta/PATH"
   - Source README turns into a tombstone with redirect

4. Use `_staging/portfolio_review_2026-05-27/apply_tier_marks.py` to batch-update Tier markers from the script's `TIER` dictionary.
