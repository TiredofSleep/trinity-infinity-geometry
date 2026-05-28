# Cover Letter — JCT-A Submission

**To:** Editors, Journal of Combinatorial Theory, Series A

**From:** B. R. Sanders (corresponding author)
7Site LLC, Hot Springs, Arkansas, USA
brayden@7site.co

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** Non-Associativity Decay in Binary Composition
Tables over ℤ/Nℤ

**Co-author:** M. Gish (Independent Researcher, Hot Springs, AR)

---

## Summary

We submit for consideration in JCT-A an explicit O(1/N) bound on the
non-associativity density σ(N) of a specific finite binary operation
CL_N defined on ℤ/Nℤ:

> **Theorem.** For squarefree N ≥ 3,
> 2(N-2)² − 2φ(N) ≤ σ(N) · N³ ≤ 2(N-2)² + 2φ(N),
> hence σ(N) < 2/N for all such N, and Nσ(N) → 2 from below as
> N → ∞ along any sequence of squarefree integers.

The proof is elementary and self-contained: the dominant contribution
2(N-2)² comes from a clean enumeration of two boundary cases (HARM and
VOID rules), and the residual ε(N) is bounded by 2φ(N) via direct
case analysis using the Chinese Remainder Theorem. The matching lower
bound, which makes the asymptotic Nσ(N) → 2 rigorous (rather than
merely numerically observed), is obtained by the same enumeration
read in reverse.

## Why JCT-A

The result fits the JCT-A profile in three ways:

1. **Combinatorial enumeration of a finite binary operation.** The
   counting is exhaustive on ℤ/Nℤ, with explicit formulas verified
   over a broader squarefree test set
   {10, 30, 42, 66, 105, 110, 154, 210, 330, 462, 770, 1155}.
2. **Number-theoretic structure.** The squarefree hypothesis is used
   essentially: it forces (a-1)(b-1) ≡ 0 mod N to have no nontrivial
   solutions in Case 3.B-i of the proof, closing the residual count.
3. **σ → 0 as a counterpoint.** The result gives an explicit O(1/N)
   bound in the σ → 0 regime, which is opposite in direction to the
   maximally-non-associative quasigroup program (Drápal, Kepka, and
   collaborators) where σ → 1.

## Companion submissions

Two companion papers with overlapping authorship are submitted
simultaneously to other venues:

- "Logarithmic Quintessence: A Dimensionless Scalar Dark Energy Model
  with an Analytic Vacuum"
  (submitted to JCAP)
- "The First-G Event and a Discrete Sinc² Identity"
  (submitted to Integers)

The JCT-A paper does not depend on either; the cross-references are
provided for readers tracking the broader program. All three are
archived in the shared Zenodo deposit DOI 10.5281/zenodo.18852047
(a single-deposit bundle of the family's verification scripts and
preprint PDFs, not a per-paper preprint DOI).

## Reproducibility

A self-contained Python script verify_sigma_rate.py is provided as
supplementary material. The script enumerates σ(N) directly for every
squarefree N ≤ 100 (and the full target test set up to N = 210),
confirming the bound σ(N) < 2/N with zero counterexamples and
producing the exact ε(N), φ(N), and Nσ(N) values stated in the
manuscript.

## Suggested reviewers

We will provide suggested reviewers through the JCT-A submission
portal's reviewer-recommendation field rather than in this cover
letter.

## Conflict of interest

The authors declare no competing interests. No funding was received
for this work.

---

Thank you for considering the manuscript.

Sincerely,
B. R. Sanders
