# Cover letter — J19: On the Prime-Divisibility Pattern of the Characteristic Polynomial of a 10×10 Integer Matrix

**To:** Editors, *Linear Algebra and Its Applications* (LAA)

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *On the Prime-Divisibility Pattern of the Characteristic Polynomial of a 10×10 Integer Matrix Arising in a Discrete Magma on $\mathbb{Z}/10\mathbb{Z}$*

---

## Summary

For a specific 10×10 integer matrix $T \in M_{10}(\mathbb{Z})$ — the canonical composition table of a discrete commutative magma on $\mathbb{Z}/10\mathbb{Z}$ — the integer characteristic polynomial $f(\lambda) = \det(\lambda I - T)$ has **exactly two** of its nine nonzero coefficients divisible by $11$:
$$
c_2 = 33 = 3 \cdot 11, \qquad c_8 = -120{,}736 = -2^5 \cdot 7^3 \cdot 11.
$$
The discriminant of the eighth-degree polynomial $g(\lambda) = f(\lambda)/\lambda^2$ factors as
$$
\mathrm{disc}(g) = 2^{16} \cdot 7^7 \cdot 659 \cdot 95{,}184{,}709 \cdot 222{,}007{,}939 \cdot 2{,}545{,}644{,}917 \cdot 295{,}153{,}052{,}072{,}903,
$$
with no factor of $11$. The result therefore records a clean structural separation: the prime $11$ lives at the *coefficient* level (sums and products of eigenvalues — the elementary symmetric functions), while the large exponents $2^{16}$ and $7^7$ live at the *separation* level (eigenvalue gaps — the discriminant). A second theorem (Theorem 4.1) shows that the prime-$11$ divisibility pattern is **lens-dependent**: the upper-triangle authoritative symmetrization $T_{\mathrm{SYM}}$ — a 2-cell perturbation of $T$, with rank dropping from $8$ to $7$ — has $c_2 = -23$ and no factor of $11$ in any nonzero coefficient of its characteristic polynomial. The single 2-cell perturbation entirely destroys the prime-$11$ pattern.

The paper is a 5-6 page short note. All claims are verified by a self-contained sympy computation in under 5 seconds.

## Why *Linear Algebra and Its Applications*

* The result is a clean prime-divisibility / lens-dependence observation about the characteristic polynomial of a specific integer matrix — exactly the kind of short structural observation LAA publishes routinely.
* The verification artifact (`wobble_check.py`, sympy + `factorint`) is reproducible by any referee in under 5 seconds with no external dependencies beyond `sympy`.
* The lens-dependence theorem (4.1) is itself a clean linear-algebra observation — a 2-cell perturbation that destroys a prime-divisibility pattern at the coefficient level — and welcome in the LAA neighborhood.
* The paper does not claim any physical or conceptual interpretation beyond the integer arithmetic; the abstract and §3 are explicit on this point.

## Companion submissions

The matrix $T$ studied here arises in a separate research program on commutative non-associative magmas on $\mathbb{Z}/10\mathbb{Z}$ (the "TIG" program). The relevant companion submissions cited as already-submitted are:

* J15 (Sanders & Gish), *Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor of Two Commutative Binary Operations on $\mathbb{Z}/10\mathbb{Z}$*, submitted to *Algebraic Combinatorics*, 2026.
* J32 (Sanders & Mayes), *Crossing Lemma: Non-Associativity as Information Generation in Finite Magmas*, submitted to *J. Combin. Theory A*, 2026.

The closest published precedent is Drápal & Wanless (2021), *JCTA* **184**, 105510 (small finite commutative non-associative structures with integer invariants).

## Reproducibility

A self-contained verification script is bundled at `manuscript/verification/wobble_check.py`. Dependencies: Python 3.11+, sympy. Wall-clock under 5 seconds; output is a 7/7 pass-table covering the integer characteristic polynomial, the trace identity $\mathrm{tr}(T) = 63 = 9 \cdot 7$, the prime-$11$ divisibility of $c_2$ and $c_8$, the absence of $11$ in any other nonzero coefficient, the discriminant factorization, and the SYM-lens comparison.

## Suggested reviewers

- A specialist in the structure of integer characteristic polynomials of small structured matrices.
- A specialist in finite commutative non-associative magmas / quasigroup combinatorics (e.g., the Drápal-Wanless neighborhood).
- A specialist on the relationship between matrix perturbations and prime-divisibility patterns of elementary symmetric functions.
- (Three to five named candidates appropriate to the LAA editorial board to be identified during the pre-submission referee-rigor pass.)

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

Sincerely,
B.R. Sanders
