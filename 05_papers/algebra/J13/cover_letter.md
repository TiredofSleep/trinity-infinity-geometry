# Cover letter — J13: The Forced 5/7 Torus Aspect Ratio (Up to a Calibration Choice)

**To:** Editors, *Acta Arithmetica*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *The Forced 5/7 Torus Aspect Ratio (Up to a Calibration Choice): Cyclotomic Forcing on Z/10Z*

---

## Summary

The ring `Z/10Z` carries four simultaneous algebraic structures (additive divisor chain, multiplicative orbit lattice, additive translation flow `x -> x + 1`, multiplicative root flow `x -> g x`) whose joint embedding into the minimal smooth 2-manifold is the torus `T^2 = S^1 x S^1` (Sanders-Gish *Flatness Theorem*, companion, submitted to *J. Pure Appl. Algebra*). The present paper isolates the cyclotomic data that determines the torus aspect ratio and proves the following structural statement:

**Theorem 1.1 (Cyclotomic-calibrated 5/7 aspect ratio).** Fix the cyclotomic-embedding calibration in which a prime-`p` closed circle has circumference `p`. The major radius `R` equals the smallest prime divisor of `n = 10` at which the cyclotomic value `A_p = 2 cos(pi/p)` is irrational of algebraic degree at most 2 over `Q` (giving `p = 5` with `A_5 = phi`, the golden ratio). The minor radius `r` equals the smallest prime (not necessarily dividing `n`) at which `A_p` has algebraic degree at least 3 over `Q` (giving `p = 7` with minimal polynomial `g(x) = x^3 - x^2 - 2 x + 1` over `Q`, irreducible). Under this calibration,

      T* = R / r = 5 / 7.

The proof is short and self-contained: the cyclotomic degree formula `deg_Q(2 cos(pi/p)) = (p-1)/2` for odd primes `p` (Lehmer 1933; Watkins-Zeitlin 1993) gives `deg = 0, 1, 2, 3` at `p = 2, 3, 5, 7`. The minimal polynomial `g(x) = x^3 - x^2 - 2 x + 1` of `A_7` is irreducible over `Q` by the rational-root test (`g(+/-1) = -1, 1`), and its discriminant equals `49 = 7^2`, so its Galois group is `A_3 = Z/3Z` (the totally real cubic subfield of `Q(zeta_7)`).

We are explicit about the conditional nature of the result: the forcing is conditional on the cyclotomic-embedding calibration imported from the *Flatness Theorem*; a calibration-free derivation is identified as an open problem (Open question (b)).

## Errata against earlier versions

This is a corrected resubmission. The original draft contained two material mathematical errors which have been fixed:

- **The minimal polynomial of A_7 = 2 cos(pi/7) over Q is `x^3 - x^2 - 2 x + 1`, not the previously cited `8 x^3 - 4 x^2 - 4 x + 1`.** The latter polynomial is the minimal polynomial of `cos(pi/7)` (without the factor 2); the two are related by `(8 x^3 - 4 x^2 - 4 x + 1)|_{x -> x/2} = x^3 - x^2 - 2 x + 1`. The structural conclusion (degree-3 obstruction at `p = 7`) is unchanged.
- **Lemma 4.2 of the original draft evaluated `f(-1/2) = 3` when the correct value was `1`.** The lemma is rewritten for the correct minimal polynomial; the rational root test now reduces to two evaluations, `g(1) = -1` and `g(-1) = 1`.

In addition, the earlier numerical claim that `73 / 101 = 5 / 7` exactly is retracted: `73 / 101 - 5 / 7 = 6/707 ~ 1.2%`. This is now recorded as an open numerical question (Open question (e)) rather than a claim.

All claims are verified by the included script `manuscript/verify_J13.py` (6 / 6 PASS at machine precision; sympy-based; pure-standard-library otherwise; runtime under five seconds).

## Why *Acta Arithmetica*

- The paper is a self-contained algebraic forcing argument over `Q(zeta_p)`, with the central technical input being the irreducibility of the cubic `x^3 - x^2 - 2 x + 1` over `Q` (Lehmer 1933 in the equivalent `cos(pi/7)` form; Watkins-Zeitlin 1993 for the general degree formula).
- *Acta Arithmetica* regularly publishes short notes establishing rigidity properties of cyclotomic structures — the calibration-conditional 5/7 forcing is exactly such a result.
- The companion (J33, *Flatness Theorem*) is targeted at *J. Pure Appl. Algebra*; this paper is the cyclotomic appendix that does not fit the JPAA scope.

If the editors judge a shorter-note venue more appropriate (the result is calibration-conditional rather than unconditional), we would welcome a redirect to *Integers* as a secondary target.

## Companion submissions and conditionality on J33

**Conditionality flag (please note).** This work is conditional on the companion paper J33 (*Flatness Obstruction on Squarefree* `Z/nZ`, currently Tier 2 in our portfolio) being available as a preprint at the time of consideration. J33 supplies the cyclotomic-embedding calibration (Definition 2.5 / Remark 2.6 of the present paper) and the existence of the torus `T^2` itself (Theorem 2.4). The 5/7 aspect-ratio forcing of Theorem 1.1 is established here \*relative to\* that calibration; the absence of J33 would not invalidate the cyclotomic / algebraic content (Theorems 3.1, 4.1; Lemma 4.2) but would leave the geometric interpretation of `T^*` provisional. **We will provide the arXiv ID for J33 as soon as it lands** and ask the editors to defer formal evaluation of the geometric claims until that preprint is publicly available.

The TIG / CK research program is shipping a coordinated multi-paper sequence over Summer 2026. Papers cited as already-submitted companions are:

- J33 (Sanders-Gish, *Flatness Theorem* / *Flatness Obstruction on Squarefree* `Z/nZ`, currently Tier 2; targeted preprint within 2–4 weeks of this submission) — the parent result. The present paper is the cyclotomic / aspect-ratio sequel.
- J24 (Sanders-Gish, *First-G Law*, submitted to *Integers*) — provides the `sinc^2` framework cited in the catalog of companion appearances (§6).
- J27 (Sanders-Mayes, *Crossing Lemma*, submitted to *J. Combin. Theory Ser. A*) — provides the structural input on pairwise incompatibilities of CRT factor partitions (Lemma 2.2).
- J34 (Sanders-Mayes, *Universal Orthogonality Principle*, submitted to *J. Number Theory*) — provides the cited pairwise-incompatibility lemma.

## Reproducibility

The single included script `manuscript/verify_J13.py` reproduces all the algebraic claims at machine precision: minimal polynomial identification (sympy `minimal_polynomial`), the cos-vs-2cos disambiguation (the M1 erratum fix), irreducibility (rational root test plus sympy `Poly.is_irreducible`), discriminant `= 49`, Galois group `Z/3Z` (by the discriminant-square criterion for irreducible cubics), and the degree threshold (degree 2 at `p = 5`, degree 3 at `p = 7`). All six checks PASS.

## Suggested reviewers

- A specialist in cyclotomic field theory.
- A specialist in algebraic number theory with experience in rational forcing arguments over `Q(zeta_p)`.
- A specialist in the algebraic geometry of finite cyclic groups and their continuum limits.

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

Sincerely,
B.R. Sanders
