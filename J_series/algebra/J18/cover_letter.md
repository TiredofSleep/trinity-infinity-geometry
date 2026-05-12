# Cover letter — J18: Two Crossing Decompositions of a -21 Invariant on Z/10Z with the sigma^2-Triadic Refinement

**To:** Editors, *Algebraic Combinatorics*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *Two Crossing Decompositions of a -21 Invariant on Z/10Z with the sigma^2-Triadic Refinement*

---

## Summary

On the residue ring Z/10Z, fix the canonical involution sigma with cycle structure `(0)(3)(8)(9)(1 7 6 5 4 2)` — four fixed points plus one 6-cycle. We record an integer-valued function `Psi_B : Z/10Z -> Z` defined explicitly by the ten values

  `Psi_B = {0:+1, 1:-5, 2:-3, 3:-2, 4:-2, 5:-1, 6:-1, 7:-3, 8:-3, 9:-2}`

(Table 1 of the manuscript). The total `sum Psi_B = -21` admits two decompositions of independent combinatorial origin:

1. a **sigma-orbit decomposition** producing the triangular split `T_5 + T_3 = 15 + 6 = 21`, with `-T_5 = -15` summed over the 6-cycle and `-T_3 = -6` over the four fixed points (Theorem 3.1);
2. a **role-partition decomposition** producing the Fibonacci split `F_7 + F_6 = 13 + 8 = 21` on the role classes `F = {1, 3, 5, 7, 9}` (`-F_7 = -13`) and `S = {2, 4, 8}` (`-F_6 = -8`), with singletons `T = {6}` (`-1`) and `V = {0}` (`+1`) cancelling (Theorem 3.2).

The two decompositions cross: they agree on the total `-21` but partition Z/10Z along genuinely different congruence classes (Theorem 3.3). Refining the sigma-orbit side by `sigma^2`, the two triangular orbits `O_1 = {1, 6, 4}` and `O_2 = {7, 5, 2}` carry per-orbit sums `-8` and `-7` (Proposition 4.1); these match the canonical TIG primes BREATH = 8 and HARMONY = 7 in sign-flipped form.

The paper is short and entirely concrete. Every numerical claim reduces to a direct sum of ten integer values from Table 1, which the reader can check by inspection or run the bundled script `verify_J18.py` (6/6 PASS, standard-library Python, runtime <1s).

## R1 fresh-eyes math fix

The pre-revision draft asserted the sigma^2-orbit per-orbit values in the Proposition statement as `sum_{O_1} = -7, sum_{O_2} = -8`, while its proof correctly computed `-8` and `-7` respectively, and the downstream ledger used the proof's values. The statement is now corrected to match the proof and the ledger. Additionally:

- the earlier draft defined Psi_B by reference to an inaccessible companion paper using mutually inconsistent "linear period" and "boundary period" formulas; the present manuscript replaces both formulas with the explicit Table 1 above, treated as the single source of truth, with the original formulas mentioned only in Remark 2.1 for the interested reader;
- the earlier draft used the phrase "conservation/manifestation duality" as a label without a precise definition; this is replaced by Definition 3.4, distinguishing table-independent identities (true for any commutative Psi_B-analogue with the same sigma-orbit structure) from table-specific identities (true for the canonical TS_8, BH_10 of J02 but broken in `0/200` random commutative tables).

These three corrections are acknowledged in the manuscript's Acknowledgments. The R1 corrected per-orbit values are verified at machine precision by `verify_J18.py` check C4.

## Why Algebraic Combinatorics

- **Subject fit.** A short combinatorial note: cycle structure of an involution on Z/10Z, two distinct decompositions of an integer invariant on a small base set, triangular- and Fibonacci-number agreement, role-partition closure failures. The result is entirely at the integer-addition level; no representation theory, Galois theory, or analytic machinery is needed to follow the proofs.
- **Self-contained presentation.** Approximately 11 pages including bibliography. Verification reduces to a single standard-library Python script with six checks corresponding one-to-one to the manuscript's claims; runtime under one second.
- **Honest scoping.** The paper does *not* claim the role-Fibonacci or `{-7, -8}` sigma^2-orbit values are forced by the sigma-orbit structure of Z/10Z alone. They are table-specific (Def. 3.4) and recorded as such; whether the `{-7, -8}` split is in fact a forced identity given Table 1 is recorded as Open Question O2 in §5.

## Reproducibility

A single Python script `verify_J18.py` (CC-BY-4.0, standard library only — `itertools` is the only import beyond built-ins, no `numpy`, no `sympy`, no external dependencies) bundled with the manuscript performs six checks:

1. Psi_B total `-21`.
2. sigma-orbit triangular split: `sigma-cycle = -15`, `sigma-fixed = -6`.
3. Role-Fibonacci split: `F = -13`, `S = -8`, `T = -1`, `V = +1`.
4. sigma^2-orbit per-orbit values (the R1 sign-swap fix): `O_1 = -8`, `O_2 = -7`.
5. Crossing closure failures: `F intersect sigma-cycle = {1, 5, 7}` is not sigma- nor sigma^2-stable.
6. Involution data: sigma^2 of period 3 on the 6-cycle, sigma swaps `O_1` and `O_2`.

All six checks PASS at machine precision in approximately one second. The script and the manuscript are deposited at https://github.com/TiredofSleep/ck/tree/tig-synthesis.

## Companion submissions

The TIG/CK research program is shipping a coordinated paper sequence. The papers most relevant as already-submitted companions to this manuscript are:

- **J02** — *Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor of Two Commutative Binary Operations on Z/10Z*, submitted to *Algebraic Combinatorics* (landed 2026-05-12). Establishes the canonical TS_8, BH_10 tables and the corrected substrate frame from which Psi_B originates.
- **J26** — *The LATTICE Operator and Paradoxical Information Algebras: A Substrate-Internal Framework on Z/10Z*, submitted to *Algebra Universalis*. Source of the per-element BH_10-period values determining Table 1 and of the `0/200` random-table empirical check supporting Definition 3.4.

## Closest published precedent

- **Drápal & Wanless (2021), *J. Combin. Theory A* 184, 105510** — *Maximally nonassociative quasigroups*. Same domain (small finite commutative non-associative structures on a base set of size 10 and related), opposite structural extremum (theirs maximally non-associative; the present substrate sits at the structurally regular end of the same family). Cited in §0 (Lens) and the bibliography as the closest neighbour for the input substrate.

## Per-venue cap

This is the 2nd *Algebraic Combinatorics* submission of the J-series this quarter, after J02 (landed 2026-05-12). Within cap; submission feasible.

## Suggested reviewers

- A specialist on cycle structure of involutions on small base sets and integer-invariant decompositions.
- A specialist on combinatorial identities relating triangular and Fibonacci numbers.
- A specialist on small finite commutative non-associative magmas or quasigroups (Drápal-Wanless neighbourhood).

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

Sincerely,
B.R. Sanders
