# Cover letter — J20: Total-Dimension Match between Tensor Powers of a Finite-Field 4-Algebra and Real Clifford Algebras Cl(2n), with a Refined-Cell Grading

**To:** Editors, *Linear Algebra and its Applications*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *Total-Dimension Match Between Tensor Powers of a Finite-Field 4-Algebra and Real Clifford Algebras Cl(2n), with a Refined-Cell Grading*

---

## Summary

We record two elementary linear-algebraic facts about the tensor powers `V^{⊗n}` of a particular 4-dimensional commutative non-associative algebra `V` over `F_5`. First, the total dimension matches that of the real Clifford algebra `Cl(2n) = Cl(2n, 0)`:

  `dim_{F_5} V^{⊗n} = 4^n = 2^{2n} = dim_R Cl(2n)` for every `n ≥ 0`.

This is forced by `dim V = 4 = 2^2` and holds for any 4-dimensional algebra over any field. The non-trivial content is the second result: each tensor slot of `V^{⊗n}` carries two structural sign bits (one for each of the two `F_5`-line summands of the slot's basis), giving `4^n = 2^{2n}` one-dimensional *refined cells*. The Hamming-weight distribution of these `2n` structural bits is exactly the binomial sequence `C(2n, k)`, `k = 0, ..., 2n`, which matches the grade dimensions of `Cl(2n)` exactly.

We are explicit about what is *not* proved. The mapping from refined cells of `V^{⊗n}` to basis multivectors of `Cl(2n)` is a bookkeeping bijection on basis-element labels; we do not claim it extends to a structure-preserving map of vector spaces or algebras over a common base ring (the domain is over `F_5`, the codomain is over `R`). The agreement between the coarse-cell weights `C(5, k) = 1, 5, 10, 10, 5, 1` at `n = 5` and the dimensions of the `SU(5)` one-generation representation `1 ⊕ 5̄ ⊕ 10` plus its conjugate is recorded as a binomial-coefficient coincidence, not a representation-theoretic theorem. All such open items are confined to §6 (Open questions).

## R1 fresh-eyes math fix

An earlier draft conflated the coarse-cell distribution `C(n, k)` (`2^n` total cells, weighted by the number of `V_+`-slots, each cell `2^n`-dimensional) with the `Cl(2n)` grade distribution `C(2n, k)` (sum `2^{2n}`, one summand per multivector grade). These are distinct sequences over distinct index sets. The revised manuscript distinguishes them cleanly: the coarse-cell distribution sums to `2^n`, the refined-cell distribution sums to `4^n`, and only the latter matches the `Cl(2n)` grade dimensions. The misstatement is acknowledged in the manuscript's Acknowledgments and corrected as the revised Theorem 4.1 (refined-cell binomial grading). The previous false coupling of `C(n, k)` to `Cl(2n)` grades is now noted explicitly in Remark 4.2.

## Why Linear Algebra and its Applications

- **Subject fit.** A short, elementary linear-algebra note: tensor-power dimensions, basis-cell decompositions, binomial-coefficient identities, and the Hamming-weight grading on a 2n-bit label string. The result is recorded for the literature; no representation-theoretic machinery is invoked.
- **Self-contained presentation.** Approximately 12 pages including bibliography. Verification reduces to a single standard-library Python script (`verify_J17.py`) with six independent checks corresponding one-to-one to the manuscript's claims; runtime under one second.
- **Honest scoping.** The paper does *not* claim a structure-preserving map between `V^{⊗n}` and `Cl(2n)`; it claims a basis-label bijection with a matching Hamming grading. The companion open question (whether such a structure-preserving map exists over a common base ring) is recorded in §6, not in the abstract.

## Reproducibility

A single Python script `verify_J17.py` (CC-BY-4.0, standard library only — no `numpy`, no `sympy`, no external dependencies) bundled with the manuscript performs six checks:

1. Total-dimension match `dim_{F_5} V^{⊗n} = 4^n = 2^{2n} = dim_R Cl(2n)` for `n = 0..5`.
2. Coarse-cell count `2^n` for `n = 1..5`.
3. Coarse-cell distribution at `n = 5`: `1, 5, 10, 10, 5, 1`, sum `32`.
4. Refined-cell total `4^n` for `n = 0..5`.
5. Refined-cell distribution `C(2n, k)` matches `Cl(2n)` grade dimensions, closed-form vs. direct enumeration over the `4^n` structural-bit strings, for `n = 0..5`.
6. Refined `n = 5` distribution `1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1`, sum `1024 = 4^5`.

All six checks PASS at machine precision in approximately one second. The script and the manuscript are deposited at https://github.com/TiredofSleep/ck/tree/tig-synthesis.

## Companion submissions

- **J37** — *Discrete Dirac on F_5^4: Substrate Algebra of the 4-Core*, submitted to *Algebras and Representation Theory*. Defines the algebra `V` and its multiplication table. J20 cites the data needed in §2 directly so verification is self-contained at the basis level.
- **J50** — *F_p Universality: The Operator-Substrate Construction over Prime Fields*, submitted to *Algebra Universalis*. Sister companion in the same finite-field family; not load-bearing for J20.

## Closest published precedent

- **Drápal & Wanless (2021), *J. Combin. Theory A* 184, 105510** — *Maximally nonassociative quasigroups*. Same domain (small finite commutative non-associative structures), opposite structural extremum (theirs maximally non-associative; the present `V` is at the structurally regular end of the same family, with idempotents and a Grassmann annihilator). Cited in §0 (Lens) and the bibliography as the closest neighbour for the input substrate.

## Suggested reviewers

- A specialist on tensor algebras over finite fields and their structural decompositions.
- A specialist on Clifford algebras, their grade structure, and Bott periodicity.
- A specialist on small finite commutative non-associative magmas or quasigroups (Drápal–Wanless neighbourhood).

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

Sincerely,
B.R. Sanders
