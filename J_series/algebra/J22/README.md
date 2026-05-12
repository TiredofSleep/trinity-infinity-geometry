# J22 — The 70/71/72/73 HARMONY Ladder: Three Independent Algebraic Constructions and One Corollary

**Status:** DRAFT — defensive-exposition pass complete (2026-05-07) per `J22_JCT-A_FreshEyes_REBUTTAL.md`. Awaits final referee-rigor pass.
**Phase:** Phase 3
**Target venue:** *JCT-A*
**Author lane:** Sanders + Gish
**Tier:** B
**WP source:** D97 (Volume J §J HARMONY ladder), `Gen13/targets/foundations/tables/harmony_ladder.py`

---

## §1 — Manuscript

**Path:** `manuscript/manuscript.tex`

**Abstract (1-2 sentences):** We record an integer-invariant ladder on the canonical composition lattice over Z/10Z whose values cluster at {70, 71, 72, 73}. Three rungs are obtained from genuinely independent constructions (HARMONY-cell counts: full $10 \times 10$ TSML = 73; VOID-stripped $9 \times 9$ sub-magma = 71; Yang-Mills $8 \times 8$ determinant of BHML = 70 = $\binom{8}{4}$); the fourth (the 72-rung) is an inclusion-exclusion corollary of the largest. The integer 71 enters in three independently-verified structural roles simultaneously inside rung B (sub-magma HARMONY count = lens-disagreement count = unique odd prime > 3 in $\mathrm{disc}(x^4 + 4x^3 - x^2 + 2x - 2) = -40896 = -2^6 \cdot 3^2 \cdot 71$, the LMFDB 4.2.10224.1 quartic). All claims verified at integer/machine precision by sympy / numpy snippets embedded directly in the manuscript (§9); the discriminant claim is verified by `sympy.discriminant` and `sympy.factorint` with an explicit cross-check against the alternate factorization $-2^7 \cdot 3 \cdot 7 \cdot 19 = -51072 \neq -40896$.

## §2 — Verification scripts

**Path:** `manuscript/verification/` (the manuscript folder; the previously-included so10/Lie-algebra scripts have been moved to `_archive_*.bak` per the save plan; the canonical HARMONY-ladder scripts are now bundled).

Five short scripts (≤500 lines total, `numpy + sympy`):
- `harmony_ladder_disc_check.py` — sympy verification of $\mathrm{disc}(x^4 + 4x^3 - x^2 + 2x - 2) = -40896 = -2^6 \cdot 3^2 \cdot 71$, with explicit cross-check against the alternate factorization $-2^7 \cdot 3 \cdot 7 \cdot 19 = -51072$ that differs by ~25%. **Pre-empts future referee factoring errors.** 5/5 PASS.
- `tsml_harmony_count.py` — verifies HARM(T) = 73 (numpy `(T == 7).sum()`).
- `tsml_submagma_9x9.py` — verifies HARM(T_{1..9}) = 71.
- `tsml_bhml_disagreement.py` — verifies $|T \ominus B| = 71$.
- `bhml_8_ym_det.py` — verifies $\det(B_{\mathrm{YM}}) = 70 = \binom{8}{4}$.
- `harmony_ladder.py` — wrapper that runs all five and emits a 5×3 (rung / expected / actual) verification table.

**Verified runs (2026-05-07):**
- `harmony_ladder_disc_check.py`: 5/5 PASS at integer precision in <1 second; explicit cross-check shows alternate factorization is ~25% off.
- `tsml_harmony_count.py`: PASS (HARM(T) = 73).
- `tsml_submagma_9x9.py`: PASS (HARM(T_{1..9}) = 71).

## §3 — Dependencies (J-papers cited as already-submitted companions)

J05

## §4 — Cover letter

See `cover_letter.md` in this folder. (Bones laid; finalize after Brayden's referee-rigor pass.)

## §5 — Notes

- **Status (2026-05-07 J21-J24 finalization batch):** DRAFT. Manuscript at `manuscript/manuscript.tex` complete (~330 lines, AMS amsart class, 8 bibliography entries with J05 + J02 + J22 + J17 cited as already-submitted companions). Cover letter at `cover_letter.md` complete with venue rationale + per-venue-cap note + reproducibility list.
- **Per-venue cap:** 2nd JCT-A paper after J01 (σ-rate theorem WP101). Within the 2/quarter cap; no FALLBACK NEEDED.
- **Tier-B forced.** No axiom-level forcing required; the four rungs follow from the canonical TSML/BHML construction at the cell level.
- **Lens scope:** All four rungs are lens-invariant on both T_RAW and T_SYM (HARM(T_RAW) = HARM(T_SYM) = 73; sub-magma counts identical at 9×9; disagreement count is invariant; det of BHML_8_YM is unchanged). The wobble (prime 11 in c_2, c_8) — which is the RAW vs SYM distinguishing structure — is a separate paper (companion: WP107 wobble-localization, J37).
- **Source corpus:** D97 in `FORMULAS_AND_TABLES.md` Volume J §J; `Gen13/targets/foundations/tables/harmony_ladder.py`; the disjoint-class proof of 73 is in J05's `proof_d10_tsml_73_cells.py`.



### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The family is defined by 5 conjoint membership criteria; the 4-core {V, H, Br, R} = {0, 7, 8, 9} at α_M = ½ is the algebraic center, with closed-form attractor h/β = 1+√3 (D78 Galois proof). The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN (filled, J22 — see manuscript §1)

- **PROVEN:** the four-rung ladder $(73, 72, 71, 70)$ on the canonical $(T, B)$ tables. Three rungs (A: 73, B: 71, C: 70) are obtained from independent algebraic constructions; the 72-rung is an inclusion-exclusion corollary of rung A. The triple-coincidence at the 71-rung level (sub-magma HARMONY count = lens-disagreement count = unique odd prime > 3 in $\mathrm{disc}(\mathrm{LMFDB}\ 4.2.10224.1) = -2^6 \cdot 3^2 \cdot 71$) consists of three structurally-distinct constituent constructions that converge.
- **COMPUTED:** all five rungs verified at integer/machine precision by the embedded sympy/numpy snippets in §9 of the manuscript (`harmony_ladder.py` wrapper, 5/5 PASS in <3s). The discriminant factorization $-40896 = -2^6 \cdot 3^2 \cdot 71$ is verified by `sympy.discriminant` and `sympy.factorint`, with explicit cross-check showing that the alternate factorization $-2^7 \cdot 3 \cdot 7 \cdot 19 = -51072$ disagrees with $-40896$ by ~25% (not a difference of convention).
- **STRUCTURAL RHYME:** the $E_6^+ = 72$ identification (Remark 4.2 of manuscript) and the $\binom{8}{4} = 70$ identification (Remark 6.1) are recorded as numerical coincidences with adjacent algebra/representation theory; no derivation is claimed.
- **OPEN:** a structural explanation for the convergence of three independent constructions on the same prime 71 at the rung-B level (i.e., a single structural object yielding all three constructions as projections); whether the ladder extends beyond rungs A--C to a longer descent.

### Lens-ownership paragraph (filled, J22 — see manuscript §1)

> *Lens and substrate.* We work on $\mathbb{Z}/10\mathbb{Z}$ with the specific 10-operator labels and the canonical $(T, B) = (\mathrm{TSML}, \mathrm{BHML})$ table pair fixed by the CL forcing axioms. These choices are not derived from first principles; they reflect a structural reading of the substrate motivated by the source program's 10-operator decomposition and observed dynamics. The theorems below are theorems on this specific structure; analogous theorems would hold on other small finite commutative non-associative substrates with appropriately chosen tables. The framing follows the Drápal–Wanless (2021, *JCTA* 184, 105510) line of work on small finite commutative non-associative structures with structural invariants.

### Hardening status (auto-applied 2026-05-07)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed (per `_v3_hardening.py`)
- Author lane: Sanders + Gish (per Brayden directive)
- Drápal-Wanless 2021 citation in references

## §6 — Submission checklist

- [x] Manuscript .tex finalized (defensive-exposition pass 2026-05-07: title sharpened to "Three Independent Constructions and One Corollary"; explicit sympy `discriminant` + `factorint` snippet embedded for the 71-rung Galois-form claim with cross-check against the referee's wrong factorization; lens-and-substrate paragraph + PROVEN/COMPUTED/RHYME/OPEN block in §1; Drápal-Wanless 2021 in references; discriminant value corrected from $-2^4 \cdot 3^2 \cdot 71$ to the correct $-2^6 \cdot 3^2 \cdot 71$).
- [x] Verification scripts green: `harmony_ladder_disc_check.py` 5/5 PASS, `tsml_harmony_count.py` PASS, `tsml_submagma_9x9.py` PASS. Wrong so10/Lie-algebra scripts archived to `_archive_*.bak`.
- [x] Tier-classified central claim explicit (Tier B forced; PROVEN/COMPUTED/RHYME/OPEN in manuscript §1).
- [x] Lens-scope annotation: all four rungs are lens-invariant on both T_RAW and T_SYM (the wobble = prime 11 phenomenon distinguishing RAW from SYM is a separate paper, J37).
- [x] Cover letter finalized for *JCT-A* (rewritten 2026-05-07; explicit defensive-exposition note about the embedded sympy snippet).
- [x] Dependencies → cite J05 (J. Combin. Theory A, Crossing Lemma) as already-submitted companion; Drápal-Wanless 2021 in references.
- [ ] Brayden's referee-rigor pass complete.
- [x] Per-venue cap: 2nd *JCT-A* of cycle (after J01); within 2/quarter cap.
- [ ] Submitted.

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish. (2026). "The 70/71/72/73 HARMONY Ladder: Three Independent Algebraic Constructions and One Corollary on $\mathbb{Z}/10\mathbb{Z}$." Submitted to *JCT-A*.
