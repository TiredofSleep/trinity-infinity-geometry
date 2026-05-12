# Cover letter — Algebraic Combinatorics

Dear Editors,

Please find enclosed the manuscript

> **Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor of Two Commutative Binary Operations on $\mathbb{Z}/10\mathbb{Z}$**
>
> B. R. Sanders, M. Gish

submitted for consideration in *Algebraic Combinatorics*.

## Summary of contributions

We study a specific pair of commutative binary operations $T, B$ on $\mathbb{Z}/10\mathbb{Z}$, given explicitly by their Cayley tables and arising as the canonical $N=10$ instance of the operator-substrate composition family of our companion paper [SandersGish2026Sigma]. Three exact structural results, all verified at machine precision or symbolically by deterministic Python scripts, are established.

1. **The joint-closure chain** (Theorem 1). The sub-magmas of $\mathbb{Z}/10\mathbb{Z}$ that are simultaneously closed under both $T$ and $B$ form a strict 8-element chain in inclusion order, with sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$. Sizes 2 and 3 are forbidden. Among all 1023 non-empty subsets exactly these eight satisfy joint closure.

2. **Per-coordinate fuse data on the 4-core** (Proposition 5.1). The minimal non-trivial element of the chain is $\mathcal{C} = \{0, 7, 8, 9\}$. The two operations have markedly different per-coordinate fuse images on $\mathcal{C}$: $T$ has rank-2 image $\{0, 7\}$, while $B$ has rank-4 image $\mathcal{C}$. The explicit symbolic forms of the four output coordinates are recorded for both, and the support-preservation property inherited from joint closure makes any convex combination $F_\alpha = \alpha\widehat{T} + (1-\alpha)\widehat{B}$ a self-map of the 4-core simplex $\Delta^3_\mathcal{C}$ for $\alpha \in [0, 1]$.

3. **A closed-form algebraic attractor** (Theorems 6, 7, 8). The iteration $F_{1/2}$ on $\Delta^3_\mathcal{C}$ has a unique attractor $p^*$ with closed-form algebraic ratios:

   - $p^*_7 / p^*_8 = 1 + \sqrt{3}$ exactly (Theorem 7).
   - $\xi^* := p^*_9 / p^*_8$ is the unique positive real root of the irreducible monic integer quartic $f(x) = x^4 + 4x^3 - x^2 + 2x - 2$ (Theorem 8).
   - The Galois group of $f$ over $\mathbb{Q}$ is $D_4$ (dihedral of order 8). The number field $\mathbb{Q}(\xi^*)$ has signature $(2, 1)$, class number 1, discriminant $-2^4 \cdot 3^2 \cdot 71$, and is the catalogued field LMFDB 4.2.10224.1.
   - The intermediate field $\mathbb{Q}(\sqrt{3}) \subset $ Galois closure arithmetically anchors the $\sqrt{3}$ in $1 + \sqrt{3}$, with explicit factorization
     $$f(x) = (x^2 + (2 - \sqrt{3})x + (\sqrt{3} - 1))(x^2 + (2 + \sqrt{3})x - (\sqrt{3} + 1)).$$

   Conjecture 9.1 states that $\alpha = 1/2$ is the unique rational mixing weight in $(0, 1) \cap \mathbb{Q}$ at which both ratios admit small-coefficient algebraic relations (degree $\le 8$, integer coefficients $\le 50$ in absolute value). The corresponding empirical evidence is a high-precision PSLQ scan over the 17-point Stern–Brocot grid of denominators $\le 7$, with the predicted relations recovered exactly at $\alpha = 1/2$ and no relations detected at the 16 other rationals.

## Why *Algebraic Combinatorics*

The paper sits at the intersection of finite-magma combinatorics (chain enumeration, per-coordinate fuse polynomials), simplex dynamics (convex-combination iteration on $\Delta^3$), and algebraic number theory (the $D_4$-Galois quartic, LMFDB cross-reference, Stern–Brocot PSLQ analysis). To our knowledge, no prior literature connects the catalogued field LMFDB 4.2.10224.1 to a fuse-iteration on a finite-magma simplex; the closed-form attractor is a new route to a known number field. The combinatorial content (chain + fuse-polynomial structure) and the algebraic-number-theoretic content (Galois group, subfield, PSLQ uniqueness) are inseparable in our derivation: each motivates the other, and neither result stands alone as the paper's contribution.

## Reproducibility

Five Python scripts (`numpy + sympy + mpmath`) reproduce all numerical and symbolic claims at machine precision (double for chain enumeration, 50-digit `mpmath` for the PSLQ scan), each in $\le 1$ minute on standard hardware:

- `4core_verification.py` — chain enumeration + per-coordinate fuse polynomials
- `04_bridge_attractor.py` — global attraction of $F_\alpha$ on the simplex
- `06_attractor_closed_form.py` — symbolic derivation of $h/\beta = 1 + \sqrt{3}$
- `07_full_closed_form.py` — quartic + Galois + LMFDB cross-check
- `alpha_pslq_sweep.py` — Stern–Brocot $\alpha$-uniqueness scan

All scripts are archived in the shared Zenodo deposit at DOI 10.5281/zenodo.18852047 (a single deposit bundle of the family's verification scripts and preprint PDFs).

## Companion submissions

This paper is the structural companion to:

- "Non-Associativity Decay in Binary Composition Tables over $\mathbb{Z}/N\mathbb{Z}$" (B. R. Sanders, M. Gish; submitted to *J. Combin. Theory Ser. A*) — establishes the operator-substrate composition family $(\text{CL}_N, B_N)$ and the rate theorem $\sigma(N) < 2/N$ as $N \to \infty$ over squarefree $N$.
- "Forcing Axioms and the Family of Commutative Non-Associative Magmas on $\mathbb{Z}/10\mathbb{Z}$ Preserving a Designated 4-Core" (B. R. Sanders, M. Gish; submitted to *Algebraic Combinatorics*) — establishes the 9-axiom forcing theorem and the three-substrate $(T, B, S)$ chain. The present paper studies the two-operation pair $(T, B)$ in depth (per-coordinate fuse polynomials, Galois $D_4$ quartic, Stern–Brocot PSLQ scan); the companion treats the larger family-of-magmas framing and the three-substrate joint closure, citing the present paper's closed-form attractor and Galois results as proved here.

The present paper does not depend on either companion's results; cross-references are provided for readers interested in the broader algebraic-combinatorial program. All three papers share the Zenodo deposit DOI 10.5281/zenodo.18852047.

## Suggested reviewers

We will provide suggested reviewers through the *Algebraic Combinatorics* submission portal's reviewer-recommendation field rather than in this cover letter.

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

Thank you for considering the manuscript.

Sincerely,
B. R. Sanders
