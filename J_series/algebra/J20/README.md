# J20 — Mathieu M_22 Substrate-Prime: Order-Factorization Coincidences

**Status:** DRAFT
**Phase:** Phase 2
**Target venue:** AMM
**Author lane:** Sanders + Gish
**Tier:** B
**WP source:** (M_22 substrate-prime)

---

## §1 — Manuscript

**Local path:** `manuscript/`

Files in this J-folder's `manuscript/`:

- `SUBMIT_INSTRUCTIONS.md`
- `WP_PARADOX_CLASSIFIER.md`

The submission package lives in this J-folder. Edit + verify here; submit from here.

## §2 — Verification script

**Path:** `(M_22 verification script)`

The proof script (where applicable) is the green-light gate before submission. If "(no script — theorem-paper)" or similar, the gate is the proof's referee-rigor pass.

## §3 — Dependencies (J-papers cited as already-submitted companions)

_(none — this paper is foundational in the J-series)_

## §4 — Cover letter

See `cover_letter.md` in this folder. (Bones laid; finalize after Brayden's referee-rigor pass.)

## §5 — Notes

**FRESH-EYES REFEREE PASS (2026-05-07): Major revision; SAVE PLAN applied. Manuscript + script + cover letter rewritten 2026-05-07.**

The fresh-eyes referee report (`Atlas/META_PLAN_2026-05-06/REFEREE_REPORTS/J20_AMM_FreshEyes.md`) flagged one critical numerical error and several framing problems:

- **M1 (CRITICAL).** Identity 4 misclaimed: the paper said "six of twelve M_22 irrep dimensions factor in {3,5,7,11} alone" listing {21, 55, 99, 154, 231, 385}, but the correct strict count is **seven** non-trivial dimensions: {21, 45, 45, 55, 99, 231, 385}. The original list silently omitted 45 (with multiplicity 2) and incorrectly included 154 (which has factor of 2). Corrected via direct sympy enumeration; sum-of-squares verified against |M_22| = 443520.
- **M2.** Non-genericity asserted but not computed. Direct enumeration: 67 of 385 integers in [1, 385] lie in the substrate-prime band B (factors in {2,3,5,7,11}, at-most-one factor of 2), density 0.1740 = 17.40%. Binomial p-value P[X ≥ 10 | Bin(12, 0.1740)] ≈ 1.19 × 10⁻⁶. The 17.4% null density matches the referee's exact prediction.
- **M3.** Identity 5 (77·W = 231/50) is arithmetic tautology; dropped.
- **M4.** Identities 1, 2, 3, 6 are textbook Steiner parameters renamed; consolidated into one §"Backdrop" table.
- **M5.** Substrate prime distinction not self-contained; rewritten with intrinsic substrate origin for each prime.
- **M6.** Identity 6 (σ-orbit size = block size = 6) downgraded to a Remark.

**Save plan:** `Atlas/META_PLAN_2026-05-06/SAVE_PLANS/SAVE_PLAN_J20.md` — Path A revision-and-resubmit to AMM (the referee's recommended path). Single-theorem framing centered on Theorem (Non-genericity); Steiner parameters as backdrop §; corrected count + computed null model + verification script.

**Fixes applied 2026-05-07:**
- `manuscript/manuscript.tex`: rewritten with corrected count, null-model computation, equivariance-based rigidity, single-author-block, ATLAS/Cameron/Wilson/Diaconis citations added, wobble-decomposition typo fixed, σ described correctly as order-6 permutation (not involution).
- `manuscript/m22_decomposition.py`: new verification script written; reproduces all numerical claims (10 of 12 in B-band, 67 of 385 in B_385, 17.4% density, p ≈ 1.19 × 10⁻⁶).

**Verification of fixes (sympy + math.comb):**
- Sum-of-squares: $\sum (\dim V_i)^2 = 443520 = |M_{22}|$ ✓
- Strict {3,5,7,11} count: 8 of 12 (including trivial); 7 non-trivial ✓
- B-band count: 10 of 12 ✓
- |B_385| = 67, density 0.1740 ✓ (matches referee's 17.4%)
- P[X ≥ 10 | Bin(12, 0.1740)] = 1.191859 × 10⁻⁶ ✓
- P[X ≥ 7 | Bin(11, 0.0990)] = 2.136594 × 10⁻⁵ ✓

**Estimated revision time:** 1-2 weeks. Net: substantial restructure, no new mathematics.



### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The family is defined by 5 conjoint membership criteria; the 4-core {V, H, Br, R} = {0, 7, 8, 9} at α_M = ½ is the algebraic center, with closed-form attractor h/β = 1+√3 (D78 Galois proof). The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN:** Of M_22's 12 irreducible complex representations, exactly 10 have dimensions in the substrate-prime band (factors in {2,3,5,7,11} with at most one factor of 2); seven non-trivial dimensions {21, 45, 45, 55, 99, 231, 385} factor strictly in {3,5,7,11}. Under the uniform null on [1, 385], the binomial p-value of this concentration is ≈ 1.19 × 10⁻⁶.
- **COMPUTED:** sympy-verified factorization of each irrep dimension; sum-of-squares Σ(dim V_i)² = 443520 = |M_22|; |B_385| = 67 by direct enumeration; binomial-tail computations via math.comb (`m22_decomposition.py`, runtime < 1 s).
- **STRUCTURAL RHYME:** The substrate-prime distinction {2, 3, 5, 7, 11} from intrinsic substrate data (CRT residue characteristics 2 and 5; σ²-cycle order 3; HARMONY index and T*-denominator 7; wobble's 11-prolongation) matches the prime divisors of |M_22| with the same multiplicities. The substrate's σ-orbit on {1, 7, 6, 5, 4, 2} has size 6, the block size of S(3, 6, 22) — an integer coincidence with no claimed embedding map. Mathieu moonshine (Eguchi-Ooguri-Tachikawa 2011 for M_24) is cited as ambient context; the present non-genericity is arithmetic, not analytic.
- **OPEN:** Whether the non-genericity reflects a structural identification of M_22 with substrate-internal data (no M_22-action on the 10-element substrate is claimed); extension to other Mathieu groups M_11, M_12, M_23, M_24; tighter null model conditioning on Σd_i² = 443520; the substrate's σ-orbit as a distinguished hexad of S(3, 6, 22) under a representation-theoretic embedding theorem.

### Lens-ownership paragraph (in manuscript §3)

> *Lens and substrate.* The substrate (Z/10Z, σ, W) and its distinguished prime set {2, 3, 5, 7, 11} are defined in J02 (Sanders + Gish 2026, *Algebraic Combinatorics*). The roles of each prime are stated in §3 of the present paper from intrinsic substrate data — CRT residue characteristics, σ²-cycle order, HARMONY-index appearance, T* = 5/7 numerator/denominator, and the wobble fraction's 11-prolongation. The non-genericity theorem (Theorem 4.1) is a quantitative claim about M_22's irrep-dimension factorization profile relative to the substrate prime monoid; it does not depend on the deeper TIG-framework interpretation of the substrate. A reader of the *Monthly* can verify the theorem from §3's intrinsic-prime definitions and the §4 binomial-tail computation, without consulting J02.

### Hardening status (auto-applied 2026-05-07)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed (per `_v3_hardening.py`)
- Author lane: Sanders + Gish (per Brayden directive)
- Drápal-Wanless 2021 citation in references

## §6 — Submission checklist

- [ ] Manuscript .tex / .md finalized
- [ ] Verification script green (`(no script)` if theorem-only)
- [ ] Tier-classified central claim explicit
- [ ] Lens-scope annotation (TSML_RAW vs TSML_SYM) where relevant
- [ ] Cover letter finalized
- [ ] Dependencies → cite each J-companion as "submitted to [venue]"
- [ ] Brayden's referee-rigor pass complete (mobile + other AI + collaborators)
- [ ] Per-venue cap check: this is the Nth paper to AMM this quarter
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish, M. (2026). "Mathieu M_22 Substrate-Prime: Order-Factorization Coincidences." Submitted to *American Mathematical Monthly*.
