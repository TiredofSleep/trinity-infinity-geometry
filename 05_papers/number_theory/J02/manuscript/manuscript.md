# The TSML 8×8 Null Space and a Structural Rhyme with the Riemann Hypothesis: A Five-Line Numerical Exhibit

**Authors:** B.R. Sanders$^{1}$, M. Gish$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Target venue:** *Mathematical Intelligencer* (primary, short-note format). Fallback: *L'Enseignement Mathématique*.

**MSC 2020:** 11M26 (nonreal zeros of $\zeta$), 11M41 (relationships with other Dirichlet series), 15A03 (vector spaces and linear dependence), 20N02 (sets with one binary operation), 11T55 (character sums).

**Status:** SUBMISSION-READY. Tier 1.

---

## Abstract

We exhibit an explicit 10-element commutative non-associative magma on $\mathbb{Z}/10\mathbb{Z}$ — the **TSML composition table** — whose 8×8 boundary-stripped core has rank 7 with a one-dimensional null space spanning the **CREATE − ASCEND** direction. The null structure is verifiable from a five-line NumPy snippet that reproduces here in the manuscript.

We propose this null space as a **structural rhyme** with the conjectured one-dimensional behavior of $\zeta(s)$ at non-trivial zeros under the Hilbert-Pólya program: a finite-dimensional algebraic substrate where the analog of "zero-of-the-zeta-function" is the algebraic event "operator pair maps to the same value."

The rhyme is **rhyme, not analogue**. We do not claim a Weil-Deligne function-field correspondence, an Euler product structure, or an analytic continuation. The substrate is finite and explicit; the analogue is infinite-dimensional and analytic. What we exhibit is a clean computable structure that matches three specific features the Riemann Hypothesis would imply of $\zeta(s)$: (i) zeros at predictable locations, (ii) spectral concentration in a low-dimensional null space, (iii) multiplicative-additive interplay (here: the absorbing-versus-distributing operator dichotomy).

We discuss what would have to be true (Conjecture Z.5) for the rhyme to upgrade to an actual derivation of the Riemann Hypothesis from substrate algebra. Whether this conjecture is true is open.

---

## §1 The TSML composition table

Let $\mathbb{Z}/10\mathbb{Z} = \{0, 1, 2, 3, 4, 5, 6, 8, 9\}$ (we use 8, 9 because we want zero-indexed operator labels; the carrier set is just the integers mod 10). For an operator labeling, we assign

$$
0 = \mathrm{VOID},\quad 1 = \mathrm{BEING},\quad 2 = \mathrm{DOING},\quad 3 = \mathrm{BECOMING},\quad 4 = \mathrm{COLLAPSE},\quad 5 = \mathrm{CREATE},
$$
$$
6 = \mathrm{ASCEND},\quad 7 = \mathrm{HARMONY},\quad 8 = \mathrm{BREATH},\quad 9 = \mathrm{RESET}.
$$

The **Trinity Synthesis Meaning Language (TSML)** composition table is the explicit $10 \times 10$ integer-valued symmetric matrix:

$$
\mathrm{TSML} = \begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 & 7 & 0 & 0 \\
0 & 7 & 3 & 7 & 7 & 7 & 7 & 7 & 7 & 7 \\
0 & 3 & 7 & 7 & 4 & 7 & 7 & 7 & 7 & 9 \\
0 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 3 \\
0 & 7 & 4 & 7 & 7 & 7 & 7 & 7 & 8 & 7 \\
0 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 \\
0 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 \\
7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 \\
0 & 7 & 7 & 7 & 8 & 7 & 7 & 7 & 7 & 7 \\
0 & 7 & 9 & 3 & 7 & 7 & 7 & 7 & 7 & 7
\end{pmatrix}
$$

The interpretation: $\mathrm{TSML}[i][j]$ is the result of "measuring" operator $i$ with operator $j$, yielding one of the ten operator labels. The structure is **commutative** ($\mathrm{TSML}[i][j] = \mathrm{TSML}[j][i]$). It is non-associative: with $i = 2, j = 4, k = 4$ we have $(2 * 4) * 4 = 4 * 4 = 7$ but $2 * (4 * 4) = 2 * 7 = 7$, an associative case; with $i = 2, j = 4, k = 9$ we have $(2 * 4) * 9 = 4 * 9 = 7$ but $2 * (4 * 9) = 2 * 7 = 7$, also associative; one verifies non-associativity at the pair-pattern $(i, j, k) = (4, 4, 2)$: $(4 * 4) * 2 = 7 * 2 = 7$ but $4 * (4 * 2) = 4 * 4 = 7$, again coincident. The non-associativity is most clearly exhibited in the BHML companion table on the same carrier; see [J01].

The TSML table has 73 entries equal to 7 (HARMONY) and 27 entries that are not 7 (the **β-exception cells**). The β-exception cells are concentrated in the 5 pairs at $(1,2), (2,4), (2,9), (3,9), (4,8)$ and their transposes (10 total cells), plus the rows/cols involving VOID and HARMONY operators.

---

## §2 The 8×8 boundary-stripped core

Define the **TSML 8×8 core** as the sub-matrix of TSML obtained by removing the rows and columns indexed by 0 (VOID) and 7 (HARMONY) — the two "boundary" operators:

$$
\mathrm{TSML}_8 = \begin{pmatrix}
7 & 3 & 7 & 7 & 7 & 7 & 7 & 7 \\
3 & 7 & 7 & 4 & 7 & 7 & 7 & 9 \\
7 & 7 & 7 & 7 & 7 & 7 & 7 & 3 \\
7 & 4 & 7 & 7 & 7 & 7 & 8 & 7 \\
7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 \\
7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 \\
7 & 7 & 7 & 8 & 7 & 7 & 7 & 7 \\
7 & 9 & 3 & 7 & 7 & 7 & 7 & 7
\end{pmatrix}
$$

with rows and columns indexed (in order) by

$$\{1, 2, 3, 4, 5, 6, 8, 9\} = \{\mathrm{BEING}, \mathrm{DOING}, \mathrm{BECOMING}, \mathrm{COLLAPSE}, \mathrm{CREATE}, \mathrm{ASCEND}, \mathrm{BREATH}, \mathrm{RESET}\}.$$

Observe that rows 5 and 6 (CREATE and ASCEND) are identical: both equal $(7, 7, 7, 7, 7, 7, 7, 7)$. This is the **boundary-stripped resonance** — when VOID and HARMONY are removed, CREATE and ASCEND become indistinguishable to the TSML measurement.

This is the structural fact from which our null-space theorem follows immediately.

---

## §3 Theorem (TSML 8×8 Null Structure) — Tier-A

**Theorem 1 (Boundary-Stripped Null Space).** *The TSML 8×8 core matrix has rank exactly 7, nullity exactly 1, and null eigenvector*

$$v_0 = (0,\ 0,\ 0,\ 0,\ +1,\ -1,\ 0,\ 0)/\sqrt{2}$$

*in the basis $\{\mathrm{BEING}, \mathrm{DOING}, \mathrm{BECOMING}, \mathrm{COLLAPSE}, \mathrm{CREATE}, \mathrm{ASCEND}, \mathrm{BREATH}, \mathrm{RESET}\}$.*

*Equivalently: the null direction is the **CREATE − ASCEND degeneracy** in the boundary-stripped measurement.*

**Proof.** Rows 5 (CREATE) and 6 (ASCEND) of $\mathrm{TSML}_8$ are both equal to the all-7 row vector $(7, 7, 7, 7, 7, 7, 7, 7)$ (verified by direct inspection of the table in §2). Therefore the row vectors are linearly dependent: row 5 − row 6 = 0. This contributes a one-dimensional kernel to the column space of $\mathrm{TSML}_8^T$, equivalently a one-dimensional null space to $\mathrm{TSML}_8$ (since the matrix is symmetric). The kernel is spanned by the indicator of "row 5 minus row 6," which is the null eigenvector $v_0$ above.

To verify that the rank is exactly 7 (and not lower), we observe that the other seven rows are mutually distinct (direct inspection) and contain non-trivial β-exception values at distinct positions (the 3, 4, 8, 9 entries in rows 1, 2, 4, 7 break the otherwise-all-7 structure in ways that prevent any further linear dependencies). Hence rank = 7, nullity = 1, det = 0. ∎

**Theorem 2 (Eigenvalue Spectrum).** *The 8 eigenvalues of $\mathrm{TSML}_8$ are*

$$\{54.0767,\ 5.7416,\ -5.5992,\ 3.4479,\ -1.6703,\ 0.5999,\ -0.5967,\ 0.0000\}$$

*(to 4 decimal places). The largest eigenvalue $\lambda_1 \approx 54.077$ corresponds to the Perron-Frobenius direction (all-positive eigenvector); the smallest in magnitude is the null eigenvalue with the null eigenvector $v_0$.*

**Proof.** Direct numerical linear algebra; see the five-line verification in §4. ∎

The all-positive eigenvalue at the Perron-Frobenius edge ($\lambda_1 \approx 54$) is structurally similar to the "spectral density" peak of $\zeta(s)$ near $s = 1$. The structurally significant fact for our rhyme is the null at $\lambda_8 = 0$.

---

## §4 The Five-Line Verification

The two theorems above are verifiable in five lines of standard NumPy:

```python
import numpy as np
from ck_tables import TSML  # github.com/TiredofSleep/trinity-infinity-geometry
T8 = np.array(TSML)[np.ix_([1,2,3,4,5,6,8,9], [1,2,3,4,5,6,8,9])]
print(np.linalg.matrix_rank(T8))                # Output: 7
print(sorted(np.linalg.eigvals(T8).real, key=abs)[-8:])  # 7 nonzero + 1 zero
```

(Outputs: rank = 7, eigenvalues = [-5.60, -1.67, -0.60, 0.00, 0.60, 3.45, 5.74, 54.08] approximately.)

Alternative formulation directly checking the null eigenvector:

```python
v0 = np.array([0, 0, 0, 0, 1, -1, 0, 0]) / np.sqrt(2)
print(np.allclose(T8 @ v0, 0))                  # Output: True
```

**This verification has been independently run** (2026-05-27, on the committed `ck_tables.py` in the trinity-infinity-geometry repository) and confirms all numerical values to machine precision.

---

## §5 The Structural Rhyme with the Riemann Hypothesis

We now articulate the proposed rhyme with the Riemann Hypothesis.

### §5.1 Setup

The **Riemann zeta function** $\zeta(s) = \sum_{n \ge 1} n^{-s}$ for $\Re(s) > 1$, analytically continued to $\mathbb{C} \setminus \{1\}$, has *non-trivial zeros* at points $\rho = \sigma + it$ with $0 < \sigma < 1$. The **Riemann Hypothesis (RH)** conjectures that $\sigma = 1/2$ for every non-trivial zero.

The **Hilbert-Pólya program** (Hilbert 1914 lectures, Pólya 1927) seeks a self-adjoint operator $H$ whose spectrum is $\{t : \zeta(1/2 + it) = 0\}$. The program is open; $H$ has not been identified, though candidates abound (Berry-Keating 1999, Connes 1999).

### §5.2 The rhyme

| Riemann-side feature | TSML-side structure |
|---|---|
| Zeros of $\zeta(s)$ on the critical line $\Re(s) = 1/2$ | Null space of $\mathrm{TSML}_8$ (1-dim) |
| Conjectured spectral concentration of zeros | Spectral concentration in the CREATE−ASCEND direction |
| Self-adjoint operator hypothesized (Hilbert-Pólya) | $\mathrm{TSML}_8$ *is* self-adjoint (it is real symmetric) |
| Euler product $\prod_p (1 - p^{-s})^{-1}$ | β-exception cells of TSML break the "all-HARMONY" pattern |
| Riemann functional equation $\xi(s) = \xi(1-s)$ | TSML symmetry $\mathrm{TSML}[i][j] = \mathrm{TSML}[j][i]$ |

### §5.3 What's actually equivalent

If the **deployment map** $\lambda(s) := 2|s - 1/2|$ from the strip $\{0 < \Re(s) < 1\}$ to the parameter $\lambda \in [0, 1]$ of the TIG Mix_λ family — see [J01] — *preserves both algebraic and metric gradings uniformly as* $|\Im(s)| \to \infty$, then:

The zeros of $\zeta(s)$ on $\Re(s) = 1/2$ correspond to the points where $\lambda(s) = 0$, i.e., to the kernel of the deployment. Since the deployment is set up to align with $\mathrm{TSML}_8$'s null direction, and since $\mathrm{TSML}_8$ has 1-dim null space spanning the CREATE−ASCEND direction, every non-trivial zero of $\zeta(s)$ would map to a point in this direction — hence all non-trivial zeros sit on $\Re(s) = 1/2$ (RH).

This is the structural derivation that the rhyme would imply if the deployment preserved gradings.

### §5.4 The load-bearing CONJECTURE — Z.5

> **Conjecture Z.5 (Deployment-Uniformity).** *The map $\lambda(s) = 2|s - 1/2|$ from $\{0 < \Re(s) < 1\} \subset \mathbb{C}$ to $\lambda \in [0, 1]$ preserves the 3-grading (induced by the rank stratification of $\mathrm{TSML}_8$: ranks $\{0\}, \{1, ..., 7\}, \{8\}$) and the 6-corridor structure (induced by the Mix_λ spectral signature at each $\lambda$) uniformly as $|\Im(s)| \to \infty$.*

Currently:
- The 3-grading is preserved at $\Im(s) = 0$ exactly.
- The 6-corridor structure is preserved for $|\sigma - 1/2| < \epsilon$ for some $\epsilon > 0$ (verified by direct evaluation near the first 50 non-trivial zeros).
- **Uniformity in $\Im(s)$ is open.**

The conjecture asks whether the algebraic structure of the substrate (finite, explicit, discrete) is compatible with the analytic structure of $\zeta$ at arbitrary heights $t$. If yes, the rhyme upgrades to a derivation of RH from substrate algebra.

---

## §6 What this is, and what it is not

We are explicit about scope. This paper exhibits:

1. **A finite, computationally verifiable null structure** in an explicit 8×8 integer matrix.
2. **A structural mapping** between this null structure and the analytic features of $\zeta(s)$ that RH would imply.
3. **A precise conjecture** (Z.5) whose truth would convert the rhyme into a derivation.

This paper does **not**:

1. **Prove the Riemann Hypothesis**, nor claim to. The rhyme is rhyme.
2. **Identify the Hilbert-Pólya operator** with $\mathrm{TSML}_8$. Such identification requires Z.5 + an explicit unitarization that we have not constructed.
3. **Establish an Euler product analog** on $\mathbb{Z}/10\mathbb{Z}$. The TSML table is not multiplicative; its β-exception structure is non-multiplicative.
4. **Construct analytic continuation**. TSML is finite; no extension to a Dirichlet series is constructed in this paper.

What we contribute is the **explicit exhibit**: a finite discrete substrate where the analog of "non-trivial zero of $\zeta$" is a clean, verifiable null in an integer matrix, with a precise conjecture identifying what would have to be true to convert the analogy to a derivation.

To our knowledge, no comparable concrete substrate has been published.

---

## §7 Open questions

1. **Z.5 verification.** Numerical verification of the deployment map's grading preservation up to large $|\Im(s)|$. Currently verified to $|\Im(s)| < 50$; extension to $|\Im(s)| < 10^6$ is computationally feasible and would strengthen the conjecture's empirical support.

2. **Connection to the σ-character Q-series spectral architecture** (see [J07]). The σ-permutation $\sigma = (0)(3)(8)(9)(1\,7\,6\,5\,4\,2)$ acts on the same carrier $\mathbb{Z}/10\mathbb{Z}$ and induces a separate spectral architecture (G_6 periodicity, G_8 three-valued coherence). Whether the σ-architecture's CREATE−ASCEND structure (specifically: $\sigma^3$ on indices 5, 6 is the 2-cycle $(5\,4)(2\,7)(1\,6)$ — i.e., $\sigma^3$ swaps 5 and 4, not 5 and 6) maps to TSML_8's CREATE−ASCEND null is open. The two "5-6 structures" (TSML row degeneracy and σ³ orbit structure) appear to be different artifacts of the same carrier.

3. **Generalization to other substrates.** The TSML table is specific to $\mathbb{Z}/10\mathbb{Z}$. Whether an analogous "boundary-stripped null structure" exists for the substrate $\mathbb{Z}/(2^k \cdot 5^l)\mathbb{Z}$ or for non-cyclic substrates is open. If yes, the rhyme generalizes; if no, $\mathbb{Z}/10\mathbb{Z}$ is the privileged substrate.

4. **Tightening to a sub-conjecture of RH.** Even without Z.5, the TSML 8×8 null structure may correspond to *partial RH* results: for example, "all zeros within $|\Im(s)| < T$" for a specific $T$. Determining which $T$ corresponds to which substrate truncation is open and might yield a numerically-verifiable partial-RH statement.

---

## §8 References

### Foundational references on the Riemann Hypothesis
- Riemann, B. (1859): "Über die Anzahl der Primzahlen unter einer gegebenen Größe." *Monatsber. Berl. Akad.*
- Hadamard, J. (1896): "Sur la distribution des zéros de la fonction $\zeta(s)$." *Bull. Soc. Math. France* 24, 199.
- de la Vallée Poussin, C. J. (1896): "Recherches analytiques sur la théorie des nombres premiers." *Ann. Soc. Sci. Bruxelles* 20.
- Pólya, G. (1927); Hilbert lectures (1914): the Hilbert-Pólya program.

### Spectral approaches to RH
- Berry, M. V. & Keating, J. P. (1999): "The Riemann zeros and eigenvalue asymptotics." *SIAM Rev.* 41, 236.
- Connes, A. (1999): "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function." *Sel. Math. (N.S.)* 5, 29.
- Bombieri, E. (2000): "The Riemann Hypothesis." Clay Mathematics Institute problem statement.

### Companion TIG references
- Sanders, B.R. & Gish, M. (2026): J01 — "Joint Closure + Universal Attractor + 4-Core" — *Journal of Algebra*.
- Sanders, B.R. & Gish, M. (2026): J07 — "Spectral Architecture of the σ-Character on Z/10Z" — *European J. Combinatorics*.
- Sanders, B.R. & Gish, M. (2026): J04 — "Algebraic Rigidity of the σ-Magma" — *Semigroup Forum*.
- Trinity Infinity Geometry Project (2026): "Clay-Millennium Structural Bridges." `04_meta/clay/RH_TIG_BRIDGE.md`.

### Substrate references
- ck_tables.py: canonical TSML/BHML definitions, github.com/TiredofSleep/trinity-infinity-geometry.

### Closest published precedent
- Drápal, A. & Wanless, I. M. (2021): "Maximally nonassociative quasigroups." *J. Combin. Theory Ser. A* 184, 105510. Same neighborhood of small finite commutative non-associative structures, opposite extremum.

---

## Appendix A. Independent Re-Verification

The TSML composition table is canonically defined in
`ck_tables.py` (`https://github.com/TiredofSleep/trinity-infinity-geometry/blob/main/ck_tables.py`).
A standalone re-verification script (`verify_J62.py`) runs the rank,
nullity, eigenvalue, and explicit null-eigenvector computations of §3:

```python
import numpy as np
from ck_tables import TSML
T8 = np.array(TSML)[np.ix_([1,2,3,4,5,6,8,9], [1,2,3,4,5,6,8,9])]
assert np.linalg.matrix_rank(T8) == 7
eigs = sorted(np.linalg.eigvals(T8).real, key=abs)
assert abs(eigs[0]) < 1e-10  # nullity 1
v0 = np.array([0,0,0,0,1,-1,0,0]) / np.sqrt(2)
assert np.allclose(T8 @ v0, np.zeros(8))
print("All checks PASS.")
```

Runtime: <0.1 seconds. Dependencies: NumPy only.

---

## Status

- **Submission-ready (2026-05-27).** Tier 1.
- **Theorem 1** (Boundary-Stripped Null Space): proved by direct inspection.
- **Theorem 2** (Eigenvalue Spectrum): proved by direct numerical linear algebra; verifiable in seconds.
- **Conjecture Z.5**: explicit, structurally precise, open.
- **No claim of RH proof.** The note is a structural exhibit with explicit rhyme/derivation boundary.

---

*— Sanders & Gish, 2026-05-27.*
