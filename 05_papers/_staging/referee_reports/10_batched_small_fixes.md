# Batched small fixes — referee pass

**Date:** 2026-05-28
**Scope:** Six precise, independently verifiable fixes flagged by the post-renumbering referee pass.
**Status:** All six applied and verified.

---

## FIX 1 — J09 cover letter / README / manuscript venue mismatch

**Problem.** J09 target venue read "Israel Journal of Mathematics" / "Israel J. Math" / "IJM" but per TIER_INDEX the target is "Communications in Algebra."

**Action.** Replaced every occurrence across the J09 folder:
- `05_papers/algebra/J09/cover_letter.md` — addressee line, "Why ..." section heading and bullets, suggested-reviewers note, per-venue cap paragraph, fallback list (Communications in Algebra removed from fallbacks since it is now primary).
- `05_papers/algebra/J09/README.md` — Target venue line, TIG-framing strip note, per-venue cap check, citation footprint.
- `05_papers/algebra/J09/manuscript/manuscript.md` — Status header line 9.
- `05_papers/algebra/J09/SAVE_PLAN_J30.md` — Verdict header, save-mode outcome quote, Family-Structure rescue paragraph, §2(e) heading, §6 Venue paragraph, §7 substrate-bound appropriateness sentence, final summary line.

**Verify.** `Grep -i "israel|IJM"` over `05_papers/algebra/J09/` returns **zero hits**. PASS.

---

## FIX 2 — J31 stray file deletion + J26 stray confirmation

**Problem.** `05_papers/interdisciplinary/J31/manuscript/J15_DiscreteSinc2_QM_JMathPhys.md` is an unrelated paper (Sanders+Mayes discrete-sinc² for J. Math. Phys.) wrongly located in J31's folder. The J31 paper is the algebraic-detector paper.

**Verification before delete:**
- `J31/manuscript/manuscript.md` is the correct J31 detector paper (verified by reading lines 1–15: title "Algebraic Detectors as Specificity Tests for a Finite-Magma Substrate ...", target *Statistical Science*).
- The stray `J15_DiscreteSinc2_QM_JMathPhys.md` in J31 is authored Sanders+Mayes, target Journal of Mathematical Physics — different paper, different author combination.
- No other "J15" files exist in J31's folder.

**Action.** `git rm 05_papers/interdisciplinary/J31/manuscript/J15_DiscreteSinc2_QM_JMathPhys.md`. PASS.

**Companion check — J26.** `05_papers/number_theory/J26/manuscript/J15_DiscreteSinc2_QM_JMathPhys.md` was inspected: its content (Sanders + Gish, discrete-sinc² paper, MSC 81S05/42A16/11A41/11Y05) matches `J26/manuscript/manuscript.tex` (also Sanders + Gish, discrete-sinc² paper, same MSC). J26 IS the discrete-sinc² paper, so this .md file is an earlier draft of the same paper and **belongs in J26**. **KEPT** (not deleted).

---

## FIX 3 — J02 typo "Z/10Z = {0,1,2,3,4,5,6,8,9}" missing 7

**Problem.** §1 of `05_papers/number_theory/J02/manuscript/manuscript.md` listed Z/10Z as a 9-element set.

**Action.** Line 29: replaced
> `Let $\mathbb{Z}/10\mathbb{Z} = \{0, 1, 2, 3, 4, 5, 6, 8, 9\}$ (we use 8, 9 because we want zero-indexed operator labels; the carrier set is just the integers mod 10).`

with

> `Let $\mathbb{Z}/10\mathbb{Z} = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$ (zero-indexed operator labels; the carrier set is just the integers mod 10).`

PASS.

---

## FIX 4 — J02 §7 σ³ wrong cycle structure

**Problem.** §7 read "σ³ on indices 5, 6 is the 2-cycle (5 4)(2 7)(1 6) — i.e., σ³ swaps 5 and 4." This is incorrect: σ = (1 7 6 5 4 2), so σ³ on the orbit {1, 2, 4, 5, 6, 7} is **(1 5)(7 4)(6 2)** — three disjoint transpositions of distance-3 partners around the 6-cycle. σ³(5) = 1 (not 4), σ³(4) = 7 (not 5).

**Action.** Replaced the bracketed parenthetical with the corrected statement:
> `(specifically: $\sigma^3 = (1\,5)(7\,4)(6\,2)$, three disjoint transpositions on the non-fixed orbit)`

PASS. (Note: surrounding sentence about "two '5-6 structures' (TSML row degeneracy and σ³ orbit structure) appear to be different artifacts of the same carrier" is preserved verbatim — that statement is unaffected by the cycle-structure correction.)

---

## FIX 5 — J07 D₁₀ no-op check

**Problem.** `05_papers/algebra/J07/manuscript/verify_qseries_merged.py` line 151 had `base_translation = lambda v_s, v_s1: True  # structural check, not strict` — a stub returning True unconditionally for any input. The line below then printed "D_10 symmetry (structural): PASS" regardless of correctness.

**Action.** Per the instruction's preferred option (b), removed the no-op stub and added an honest TODO comment block documenting (i) what the previous implementation was, (ii) why it was inadequate, (iii) what a real implementation would need to specify, and (iv) a reference to "Open Problem O_X." Changed the printed line to `"D_10 symmetry: SKIP (not implemented; see Open Problem O_X)"` so the script no longer falsely advertises a pass.

PASS.

---

## FIX 6 — Verify script renames

**Two renames** (paper has been renumbered; verification script names lagged):

(a) `05_papers/algebra/J20/manuscript/verify_J17.py` → `verify_J20.py`
- Renamed via `git mv`.
- Updated references in:
  - `J20/cover_letter.md` (2 occurrences, lines 32 and 37)
  - `J20/README.md` (6 occurrences: status, local path, run command, cover letter section, COMPUTED bullet, Hardening status, submission checklist)
  - `J20/manuscript/manuscript.tex` (2 occurrences: line 136 and line 412)
  - Inside the script itself: docstring header (lines 2–3), main() print line (line 176)
- Left referee report files (`05_linalg_spectral_J07_J19_J20.md`, `04_clean_tier1_J12_J13_J14_J20_J22.md`) untouched — those are historical referee documentation.
- Left `R1 (2026-05-07)` log entry mentioning `J17_LinAlgApps_FreshEyes.md` untouched — that's a historical referee report filename.

(b) `05_papers/algebra/J12/manuscript/verify_J15_galois.py` → `verify_J12_galois.py`
- Renamed via `git mv`.
- Updated references in:
  - `J12/README.md` (6 occurrences: status, local path, run command, cover letter section, COMPUTED bullet, submission checklist)
  - `J12/cover_letter.md` (2 occurrences: lines 28 and 39)
  - `J12/manuscript/manuscript.tex` (3 occurrences: line 10 header comment, line 133 PROVEN-section reference, line 436 §Verification-section reference)
  - Inside the script itself: line-3 header (kept as `verify_J12_galois.py  (formerly verify_J15_galois.py)` for self-documentation), line-26 run-command
- Left referee report files untouched.

**Verify.** `Grep "verify_J17|verify_J15_galois"` over the corresponding J-folders returns no matches (other than the one intentional "formerly verify_J15_galois.py" provenance line inside the renamed J12 script header). PASS.

---

## Summary

| # | Fix | Status |
|---|---|---|
| 1 | J09 venue Israel J. Math → Communications in Algebra | PASS |
| 2 | J31 stray J15_DiscreteSinc2 .md (Sanders+Mayes) deleted; J26 .md kept | PASS |
| 3 | J02 §1 Z/10Z element list (add missing 7) | PASS |
| 4 | J02 §7 σ³ corrected to (1 5)(7 4)(6 2) | PASS |
| 5 | J07 verify script D₁₀ no-op replaced with honest TODO | PASS |
| 6 | J20 / J12 verify script renames + reference updates | PASS |

All six fixes applied without modifying the mathematics of any paper.
