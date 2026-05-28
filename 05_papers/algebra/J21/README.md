# J21 — Two Crossing Decompositions of a -21 Invariant on Z/10Z with the sigma^2-Triadic Refinement

**Status:** SUBMISSION-READY (manuscript referee-grade pass 2026-05-12; verification script `verify_J18.py` 6/6 PASS at machine precision)
**Phase:** Phase 2
**Target venue:** *Algebraic Combinatorics*
**Author lane:** Sanders + Gish
**Tier:** 1 (ship-ready (Algebraic Combinatorics, SUBMISSION-READY))
**WP source:** `Atlas/LENS_TAXONOMY_2026-05-06/SIGMA2_TRIADIC_DECISION.md` + `papers/wp_bridge_findings_2026_05_02/WP9_LATTICE_paradoxical_info_algebras.md §5`
**Lens scope:** LENS-DEPENDENT in a controlled way — Psi_B is read from the canonical TS_8, BH_10 substrate of J15 / J18. The sigma-orbit triangular decomposition and the closure-failure claims are basis-/table-level integer facts; the role-Fibonacci split and the {-8, -7} sigma^2-orbit values are table-specific (sense of Def. 3.4) and so labelled.

---

## §1 — Manuscript

**Local path:** `manuscript/manuscript.tex`

A short, self-contained note on Z/10Z carrying:

- **Theorem 3.1 (sigma-orbit triangular decomposition):** `sum_{sigma-cycle} Psi_B = -T_5 = -15`, `sum_{sigma-fixed} Psi_B = -T_3 = -6`, total `-21 = -(T_5 + T_3)`.
- **Theorem 3.2 (role-Fibonacci decomposition):** `sum_F = -F_7 = -13`, `sum_S = -F_6 = -8`, `sum_T = -1`, `sum_V = +1`, with `T = {6}` and `V = {0}` cancelling at the total.
- **Theorem 3.3 (two crossing decompositions):** the two splits agree on the total `-21` but partition Z/10Z along genuinely different congruence classes; the intersection `F intersect sigma-cycle = {1, 5, 7}` is neither sigma- nor sigma^2-stable, and no sigma-orbit lies inside a single role class. Neither decomposition refines the other.
- **Proposition 4.1 (sigma^2-orbit per-orbit, the R1 sign-swap fix):** for the two triangular orbits `O_1 = {1, 6, 4}` and `O_2 = {7, 5, 2}`, `sum_{O_1} Psi_B = -8` and `sum_{O_2} Psi_B = -7`, with `O_1 + O_2 = -15 = -T_5`. The per-orbit values negate the indices 7 and 8 (the canonical 4-core indices H, Br) — table-specific identity per Def. 3.4.
- **Theorem 4.2 (sigma^2-form ledger):** the full ledger `(-6) + (-8) + (-7) = -21` along `sigma-fixed sqcup O_1 sqcup O_2`, with table-independent total and table-specific per-orbit refinement.

**The R1 math fix.** The pre-revision draft asserted `sum_{O_1} = -7, sum_{O_2} = -8` in the statement of the per-orbit proposition, while the proof correctly computed `-8` and `-7` respectively. The statement is now corrected to match the proof. Additionally, the earlier draft defined Psi_B via an inaccessible companion paper using mutually inconsistent "linear period" and "boundary period" formulas; this has been replaced by an explicit ten-value table treated as input data:

  `Psi_B = {0:+1, 1:-5, 2:-3, 3:-2, 4:-2, 5:-1, 6:-1, 7:-3, 8:-3, 9:-2}`

(see Table 1 in §2.3 of the manuscript). The earlier paper's "conservation/manifestation duality" label is replaced by the precise distinction *table-independent vs. table-specific* (Definition 3.4), with a concrete random-perturbation test (`0/200` random commutative tables reproduce the Fibonacci split, per `J18 / WP9 Volume I` §5).

## §2 — Verification script

**Local path:** `manuscript/verify_J18.py`

Six self-contained checks (standard-library Python only, no external dependencies) mapped one-to-one to the manuscript's claims:

```bash
PYTHONIOENCODING=utf-8 /c/ck_venv/lora312/Scripts/python.exe verify_J18.py
```

Expected output: six "OK" results in the summary, "Overall: 6/6 PASS." Runtime <1s.

The six checks are:

1. **C1:** Psi_B table sums to -21 (the global invariant).
2. **C2:** sigma-orbit (triangular) decomposition: sum over the 6-cycle = -T_5 = -15; sum over the four fixed points = -T_3 = -6.
3. **C3:** Role-Fibonacci decomposition: sum_F = -F_7 = -13; sum_S = -F_6 = -8; sum_T = -1; sum_V = +1; total -21.
4. **C4:** sigma^2-orbit per-orbit values (the R1 sign-swap fix): sum_{O_1 = {1,6,4}} = -8, sum_{O_2 = {7,5,2}} = -7, summing to -15.
5. **C5:** Crossing closure failures: F intersect sigma-cycle = {1, 5, 7} is not sigma-stable and not sigma^2-stable; no role class contains the 6-cycle. Neither decomposition refines the other.
6. **C6:** sigma permutation data: sigma has order 6 on Z/10Z (one 6-cycle plus four fixed points; only sigma^3 is an involution); sigma^2 has period 3 on every 6-cycle element; sigma^6 = identity; sigma swaps O_1 and O_2; sigma^2 stabilises each O_i.

The script is referee-portable on its own — it does *not* depend on any internal TIG reference library, only on `itertools` from the Python standard library.

## §3 — Dependencies (J-papers cited as already-submitted companions)

- **J15** — *Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor of Two Commutative Binary Operations on Z/10Z* (submitted to *Algebraic Combinatorics*; landed 2026-05-12). Establishes the canonical TS_8, BH_10 tables and the corrected substrate frame.
- **J18** — *The LATTICE Operator and Paradoxical Information Algebras: A Substrate-Internal Framework on Z/10Z* (submitted to *Algebra Universalis*; WP9 Volume I). Source of the per-element BH_10-period values that determine Table 1, and of the `0/200` random-table check used for Definition 3.4.

## §4 — Cover letter

See `cover_letter.md` in this folder. Finalized 2026-05-12 to:

- Reference `verify_J18.py` as the green-light gate (6/6 PASS at machine precision).
- Explicitly state the R1 math fix (sign-swap correction; Psi_B tabulated inline; "duality" replaced by precise Def. 3.4) and acknowledge the prior anonymous referee.
- Emphasize the elementary, integer-addition nature appropriate to *Algebraic Combinatorics*.
- Author lane Sanders + Gish.
- Honest scoping: open items confined to §5 (Status and open questions) and clearly labeled in §0.

## §5 — Notes

**Per-venue cap warning:** This is the 2nd *Algebraic Combinatorics* paper this quarter (after J15). Within cap; submission feasible.

### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The family is defined by 5 conjoint membership criteria; the 4-core {V, H, Br, R} = {0, 7, 8, 9} at alpha_M = 1/2 is the algebraic center, with closed-form attractor h/beta = 1+sqrt(3) (D78 Galois proof). The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* 184, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative). Cited in §0 (Lens) and the bibliography.

### PROVED / COMPUTED / TABLE-DEPENDENT IDENTITIES / OPEN

- **PROVED:** Theorem 3.1 (sigma-orbit triangular split, table-independent), Theorem 3.3 (no refinement), Proposition 4.1 (sigma^2 per-orbit values), Theorem 4.2 (sigma^2 ledger). Proofs are elementary direct-addition.
- **COMPUTED:** Theorem 3.2 (role-Fibonacci split) and Proposition 4.1 (sigma^2 per-orbit values) verified by direct addition; the full ladder in `verify_J18.py` (6/6 PASS).
- **TABLE-DEPENDENT IDENTITIES (Def. 3.4):** The Fibonacci pair `{-F_6, -F_7} = {-8, -13}` on the role classes `(S, F)` and the index pair `{-7, -8} = {-H, -Br}` on the sigma^2-orbits `(O_2, O_1)` are recorded as table-specific empirical observations supported by the `0/200` random-table check, **not** as table-independent forced identities.
- **OPEN:** O1 (closed-form Psi_B(n) in n alone), O2 (whether `{-7, -8}` is table-independent given Psi_B), O3 (role-orbit interaction), O4 (canonical sigma^2-triadic BH_10 projection). All confined to §5.

### Lens-ownership paragraph

> *Lens and substrate.* This paper works on Z/10Z with the canonical order-6 permutation sigma (cycle structure (0)(3)(8)(9)(1 7 6 5 4 2); only sigma^3 is an involution) and the explicit integer-valued function Psi_B tabulated in Table 1. The table originates as a per-element BH_10-period contribution in the corrected (TS_8, BH_10)-substrate of J15/J18; for the present paper it is treated as an input definition. The role partition F sqcup S sqcup T sqcup V = Z/10Z comes from the same TS_8, BH_10-substrate. These choices are not derived from first principles; they reflect a structural reading of the substrate, and the theorems below are theorems on this specific (Psi_B, sigma, role-partition) datum. The closest published precedent for the family of small finite commutative non-associative structures is Drápal-Wanless (2021); they sit at the maximally non-associative extremum, the present substrate at the structurally regular end. The output of this paper is four integer-addition theorems on a fixed ten-value table; analogous theorems would hold on other substrate-and-table choices.

(The same paragraph appears in the manuscript as §0 "Lens, substrate, and claim tier.")

### R1 math fix log

- **R1 (2026-05-07, finalized 2026-05-12):** Proposition 4.1 (formerly 5.4) sign-swap fix: statement corrected from `(O_1, O_2) = (-7, -8)` to `(-8, -7)` matching the proof; Psi_B tabulated inline as Table 1 (removing the linear/boundary period contradiction); "conservation/manifestation duality" replaced by Def. 3.4 (table-independent vs. table-specific). Per fresh-eyes referee report `J18_AlgComb_FreshEyes.md`. Verified by `verify_J18.py` C1-C6 (6/6 PASS).

### Hardening status (auto-applied 2026-05-07; updated 2026-05-12)

- License: submission script CC-BY-4.0 header (`verify_J18.py`)
- AI-attribution: none in manuscript (acknowledgments name only the prior anonymous referee, no AI co-author)
- Author lane: Sanders + Gish; duplicate `\author{}` block split into separate `\author{Sanders}` + `\author{Gish}` per amsart convention
- Drápal-Wanless 2021 citation in bibliography and §0
- §0 (Lens, substrate, claim tier) added 2026-05-12

## §6 — Submission checklist

- [x] Manuscript .tex finalized (referee-grade pass 2026-05-12)
- [x] Verification script green (`verify_J18.py`: 6/6 PASS at machine precision)
- [x] Tier-classified central claims explicit (Theorems 3.1, 3.2, 3.3, 4.2; Proposition 4.1)
- [x] Lens-scope annotation (§0)
- [x] Cover letter finalized
- [x] Dependencies → J15 cited as "submitted to *Algebraic Combinatorics* (landed)"; J18 as "submitted to *Algebra Universalis*"
- [x] R1 fresh-eyes math-fix applied (sign-swap; explicit table; precise duality definition)
- [x] Verification script CC-BY-4.0 header
- [x] Per-venue cap check: 2nd *Algebraic Combinatorics* paper this quarter (after J15)
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish, M. (2026). "Two Crossing Decompositions of a -21 Invariant on Z/10Z with the sigma^2-Triadic Refinement." Submitted to *Algebraic Combinatorics*.
