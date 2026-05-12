# Cover letter — J21: A 5-Dimensional CRT Fourier Embedding of Z/10Z

**To:** Editors, *American Mathematical Monthly*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *The 5D Force Vector as a CRT Fourier Embedding of Z/10Z into R^5*

---

## Summary

We give a self-contained presentation of the canonical 5-dimensional embedding of Z/10Z that respects both the CRT isomorphism Z/10Z ≅ F_2 × F_5 and the standard real Fourier basis on F_5. The embedding sends the operator with CRT coordinates (ε, y) to v(ε, y) = (ε, cos(2πy/5), sin(2πy/5), cos(4πy/5), sin(4πy/5)) ∈ R^5. The embedding is folklore in finite Fourier analysis (Diaconis 1988 Ch. 1, Terras 1999 Ch. 11). The note's contributions are two: (i) an equivariance-based rigidity statement (Theorem) — any F_5-equivariant embedding of F_5 into R^4 satisfying the regular-pentagon condition equals the standard Fourier basis up to an orthogonal change of variables; (ii) an explicit calculation of a natural spectral functional G(n) on the image — G takes ten distinct values across the operators of Z/10Z, attains its global maximum G(7) ≈ 19.47 at the single operator n = 7, and vanishes on the four σ-fixed indices {0, 3, 8, 9} where σ = (0)(3)(8)(9)(1 7 6 5 4 2). Two short applications close the note: the natural decagonal D_10-action and a Plancherel-style identity in CRT coordinates.

## Why American Mathematical Monthly

- **Audience fit.** The note is genuinely accessible to advanced undergraduates: one page of CRT, one page of finite Fourier analysis, an equivariance-based rigidity theorem, and an explicit spectral table of ten values. *Monthly* readers encounter these tools as separate pieces; the value here is in showing how naturally they fit together for the case n = 10.
- **Pedagogical hook.** The embedding's existence is "obvious" once stated, but the surprises land cleanly: the image consists of 10 distinct points on the disjoint union of two parallel 4-spheres in R^5, with a transparent decagonal orbit structure; the spectral functional has a unique global maximum at one operator, with four σ-fixed indices yielding zero by geometric-series cancellation.
- **Companion structure.** The embedding plays a structural role in a coordinated research program on substrate algebra over Z/10Z; companion papers cite this embedding as the geometric backbone for their algebraic results. *Monthly* is well-suited to host the foundational note.

## Revision history

This is a Reject-Without-Prejudice resubmission following an external referee report (2026-05-07). The revision (i) replaces the previous (tautological) rigidity premise with an F_5-equivariance + regular-pentagon condition, giving a non-trivial rigidity theorem that recovers the Fourier basis from a structural condition that does not name the conclusion; (ii) replaces the previous (numerically incorrect) two-point-maximum lemma with a corrected explicit computation tabulating G(n) at all 10 operators, with the actual maximum at n = 7 alone (G(7) ≈ 19.47, not 25 at both n = 5, 7) and the Cauchy-Schwarz upper bound G(n) < 25 proved strictly; (iii) corrects the σ-permutation prose (σ has order 6, not order 2; fixes {0, 3, 8, 9}, not {0, 5}); (iv) replaces the literal "?" in the §7 companion description with the actual 4-core {0, 7, 8, 9}; (v) adds Diaconis 1988 and Steinberg 2012 to the references (the first is the canonical *Monthly*-level reference for finite-Fourier embeddings).

## Companion submissions

The TIG/CK research program is shipping a coordinated 55-paper sequence (J01-J55) over Summer 2026. The papers most relevant as already-submitted companions to this manuscript are:

- J02 — Sanders & Gish, *Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor*, submitted to *Algebraic Combinatorics*. Defines the substrate (Z/10Z, σ, W) including the σ-permutation used in the spectral functional and the 4-core {0, 7, 8, 9} cited in §7.

## Reproducibility

A short Python script `spectral_functional.py` (≤30 lines, NumPy only) builds the CRT coordinates, computes the embedding's 10 image points, computes the spectral functional G(n) at each operator (reproducing Table 1), and verifies the rigidity assertion at random orthogonal perturbations. Wall-clock under 1 second.

## Suggested reviewers

- A specialist on finite Fourier analysis or representation theory of finite abelian groups (Diaconis / Terras / Steinberg lineage).
- A specialist on accessible expository combinatorics / number theory for the *Monthly*.
- A specialist on finite-cyclic-group embeddings and their rigidity theory.

(Specific names available on request from the corresponding author.)

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

Sincerely,
B.R. Sanders
