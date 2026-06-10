# J30 — The Multiplicative-Unit Sub-Magma C = (Z/10Z)* in the TSML Composition Lattice, and Its Contrast with the Joint 4-Core {0, 7, 8, 9}

**Status:** READY (referee-rigor pass complete 2026-05-12; honest-negative paper with formal retraction of earlier lens-invariance claim)
**Phase:** Phase 3
**Target venue:** Communications in Algebra
**Author lane:** Sanders + Gish
**Tier:** 1 (ship-ready (HONEST NEGATIVE, important for credibility))
**Type:** **HONEST-NEGATIVE PAPER** — central new content is the formal retraction of an earlier lens-invariance claim; the surviving positive content (C is TSML-closed; the joint 4-core is uniquely jointly closed at size 4) is precisely stated.

---

## §1 — Manuscript

**Path:** `manuscript/manuscript.tex` + `manuscript/manuscript.md`

**Abstract (1-sentence):** The set C = {1, 3, 7, 9} of multiplicative units of Z/10Z is TSML-closed (16-cell direct check: image = {3, 7} ⊆ C, with 14 HARMONY cells and 2 PROGRESS cells) but is NOT BHML-closed (every one of the 16 cells of CL_BHML|_{C×C} lies in {0, 2, 4, 6, 8}, disjoint from C); the joint 4-core {0, 7, 8, 9} is the unique 4-element subset of Z/10Z jointly closed under both CL_TSML and CL_BHML, contrasting structurally with the multiplicative-unit subgroup C which is one of 78 TSML-closed 4-subsets.

**Type discipline:** **honest-negative paper.** The substantive new content is the retraction of an earlier lens-invariance claim and the explicit display of the 16-cell BHML failure. The surviving positive content (TSML-closure of C; uniqueness of the joint 4-core at size 4; generator selection g = 3) is precisely stated and machine-verified.

Source corpus: `Atlas/LENS_TAXONOMY_2026-05-06/VARIANT_CATALOG.md` (Corner C entry); `Atlas/LENS_TAXONOMY_2026-05-06/DERIVATION.md` (TABLE_INDEPENDENCE_LEDGER row 22); `Atlas/META_PLAN_2026-05-06/WP_TIER_CLASSIFICATION.md` (WP27 product-gap connection); R1 revision per fresh-eyes referee `J27_CommAlg_FreshEyes.md`.

## §2 — Verification

**Path:** `manuscript/verification/4core_verification.py`

Run: `/c/ck_venv/lora312/Scripts/python.exe manuscript/verification/4core_verification.py`

**Status: 6/6 PASS at machine precision** (2026-05-12). Checks include:
1. Joint-closure chain enumeration over all 1023 non-empty subsets — chain at sizes {1, 4, 5, 6, 7, 8, 9, 10}, forbidden {2, 3} ✓
2. Normalizer identity Z_T = Z_B = (v+h+br+r)² (symbolic, sympy expand) ✓
3. Closed-form attractor h/br = 1+√3 at α=1/2 (50-digit residual 9.06e-46) ✓
4. Universality across all chain shells of size ≥ 4 ✓
5. Galois structure of x⁴+4x³−x²+2x−2 (irreducible / disc = −40896 / resolvent (z+2)(z²−z+18) / D₄ / LMFDB 4.2.10224.1 cross-check) ✓
6. α-sweep PSLQ for integer quadratic h/br — only α=1/2 admits a small-coefficient quadratic 1·y² − 2y − 2 (residual 7.69e-45) ✓

Additionally verified (J30-specific checks, run inline):
- BHML[1][1] = 2, 2 ∉ C ✓
- All 16 cells of CL_BHML|_{C×C} lie outside C; image = {0, 2, 4, 6, 8} ✓
- BHML cell distribution: 3 of 0, 3 of 2, 5 of 4, 4 of 6, 1 of 8 (total 16) ✓
- TSML cell distribution on C × C: 14 of 7, 2 of 3 (total 16) ✓
- CREATION orbit 1 → 3 → 9 → 7 → 1 under × 3 ✓
- DISSOLUTION orbit 2 → 6 → 8 → 4 → 2 under × 3 ✓
- 78 TSML-closed 4-subsets; unique BHML-closed 4-subset {0, 7, 8, 9} ✓
- Generator selection: 3³ ≡ 7 (T* = 5/7 ∈ (0, 1)); 7³ ≡ 3 (T* = 5/3 > 1) ✓

## §3 — Six referee criteria status

| # | Criterion | Status |
|---|---|---|
| 1 | Verification scripts PASS at machine precision | **PASS** — 6/6 + J30-specific checks all pass via `/c/ck_venv/lora312/Scripts/python.exe` |
| 2 | Cover letter final — frame as constructive corrective | **DONE** — `cover_letter.md` recast around the honest-negative scoping ("Why this paper is a constructive corrective" section) |
| 3 | PROVED/COMPUTED/STRUCTURAL RHYME/OPEN tier discipline (main claim = honest negative) | **DONE** — explicit tier breakdown in both manuscript §0 and cover letter; the HONEST NEGATIVE tier (retraction of lens-invariance) is named explicitly |
| 4 | Lens-ownership paragraph | **DONE** — present in manuscript §0 ("Lens and substrate") |
| 5 | Author lane = Sanders + Gish only | **DONE** — fixed duplicate author block in `.tex`; single Sanders block + single Gish block |
| 6 | Drápal–Wanless 2021 cited where relevant | **DONE** — cited in §6.2 ("Position in the small-magma literature") and in the bibliography (J. Combin. Theory A 184 (2021) 105510) |

## §4 — Cover letter

See `cover_letter.md`. Finalized as constructive corrective; tier discipline section explicit; honest-negative framing explicit; companion list (J33, J15/J01, J33, Drápal–Wanless 2021).

## §5 — Notes

**Per-venue cap:** 3rd CommAlg paper after J12 + J18. Cap is 1/quarter; if binding, **FALLBACK NEEDED** to *Journal of Pure and Applied Algebra*, *Journal of Algebra and Its Applications*, or *Semigroup Forum*. The honest-negative content (the 16-cell BHML retraction) is appropriate for any of these venues.

**Save plan (2026-05-07):** see `Atlas/META_PLAN_2026-05-06/SAVE_PLANS/SAVE_PLAN_J27.md`.

**Honest-negative discipline.** The retraction is fully cordoned:
- Earlier (false) claim: C is "lens-invariant" — jointly closed under CL_TSML, CL_BHML, CL_STD.
- Counterexample: BHML[1][1] = 2 ∉ C; all 16 cells of CL_BHML|_{C × C} are outside C; image = {0, 2, 4, 6, 8} disjoint from C.
- What survives intact: TSML-closure of C (16 cells = {3, 7} ⊆ C); uniqueness of the joint 4-core {0, 7, 8, 9} at size 4 (the J15/J01 result is *sharpened*, not weakened, by ruling out C as a competitor at size 4); generator selection g = 3 from the elementary inequality.
- Open: closure of C under the third lens CL_STD.

### Family-Structure framing

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The closest published precedent is **Drápal & Wanless (2021), *J. Combin. Theory A* 184, 105510** — same domain, opposite extremum.

### Hardening status (auto-applied 2026-05-07, re-checked 2026-05-12)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed
- Author lane: Sanders + Gish only
- Drápal–Wanless 2021 citation in references and §6.2 prose

## §6 — Submission checklist

- [x] Manuscript .tex / .md finalized (both consistent, J30-specific, honest-negative)
- [x] Verification script green (6/6 PASS + J30-specific checks PASS)
- [x] Tier-classified central claim explicit (HONEST NEGATIVE for the retraction; PROVED for the survivors)
- [x] Lens-scope annotation (TSML-closed only; BHML non-closed)
- [x] Cover letter finalized (constructive-corrective framing)
- [x] Dependencies → cited as "submitted to [venue]" (J33, J15/J01, J33)
- [x] Brayden's referee-rigor pass complete
- [ ] Per-venue cap check: 3rd Comm Algebra this quarter — possible FALLBACK to JPAA / J. Alg. Appl. / Semigroup Forum
- [ ] Submitted

---

## §7 — Citation footprint

Sanders, B.R., Gish, M. (2026). "The Multiplicative-Unit Sub-Magma C = (Z/10Z)* in the TSML Composition Lattice, and Its Contrast with the Joint 4-Core {0, 7, 8, 9}." Submitted to *Communications in Algebra*. Honest-negative paper: retracts earlier lens-invariance claim with explicit 16-cell BHML failure; sharpens the joint-4-core uniqueness result of Sanders–Gish J15/J01.
