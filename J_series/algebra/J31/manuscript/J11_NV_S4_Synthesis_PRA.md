# Full $S_4$ Symmetry on a Nitrogen-Vacancy Qutrit via Six-Pulse Microwave Synthesis

**Authors:** B.R. Sanders$^{1}$, B. Mayes$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher

**Target venue:** Physical Review A
**Manuscript class:** Experimental proposal + theoretical synthesis
**MSC/PACS:** 76.30.Mi (NV centers), 03.65.Fd (algebraic methods), 03.67.Lx (quantum computation)
**Date:** 2026-05-07 (DRAFT)

---

## Abstract

We present an explicit, machine-precision construction of the full symmetric group $S_4$ on the three-level Hilbert space of a nitrogen-vacancy (NV) center in diamond. The NV ground triplet $\{|0\rangle,|+1\rangle,|-1\rangle\}$ is shown to carry the standard $T_1$ irreducible representation of $S_4$ exactly on the $S_3 \subset S_4$ skeleton (the $A_1 \oplus E$ decomposition under $C_{3v}$ matches $T_1|_{S_3}$ identically), so that synthesis of $S_4$ requires only the addition of one explicit 4-cycle unitary $U_4$. We compute the change-of-basis matrix $V$ analytically, derive the NV-basis form $U_{4,\mathrm{NV}} = V U_4 V^{-1}$, and decompose it into a six-pulse microwave sequence on three resonant level pairs. All 24 group elements close to within $10^{-15}$ of the abstract $T_1$ matrices. Gate times $\sim 100$~ns--$1\,\mu$s are 2--3 orders of magnitude below NV coherence ($T_2 \sim 100\,\mu$s--$10$~ms), placing this proposal squarely in the regime of routine qutrit control. We give a five-test falsification ladder (process tomography, $S_3$-skeleton spectroscopy, $S_4$ closure, projector covariance, and orbit reproducibility) with explicit pass/fail thresholds. **This is an experimental proposal: the math is complete; the experimental verification is open and the paper invites lab-partner collaboration.**

---

## 1. Introduction

The synthesis of full discrete-symmetry groups on small-Hilbert-space platforms is a long-standing program in quantum control. Nitrogen-vacancy centers in diamond, with their three-level ground spin manifold and exquisite microwave addressability, are a natural target. The natural symmetry of the NV ground triplet is $C_{3v} \cong S_3$ (the symmetry of the diamond lattice site about the NV axis); $S_3$ has order 6 and is faithfully realized by the NV crystal symmetry plus the natural mirror.

The next step up — full $S_4$, of order 24 — has not previously been synthesized on the NV. The obstruction is the 4-cycle: $S_3 \subset S_4$ is index-4, and the missing generator is a single element of order 4 whose representation matrix on the $T_1$ irrep has eigenvalues $\{-1, i, -i\}$. We show that this missing element can be implemented as a six-pulse microwave sequence, completing the synthesis of $S_4$ on the NV qutrit.

Three levels of identification, ordered by strength, organize the task:

| Level | What it requires | What the NV has |
|---|---|---|
| **A** (dim only) | $\mathbb{C}^3$ Hilbert space | Trivial |
| **B** (flag) | Ordered eigenprojectors in SU(3)/T | Achievable by tomography |
| **C** (carrier) | Full $S_4$ action on $\mathbb{C}^3$ realizing $T_1$ | $S_3$ subgroup exact; 4-cycle synthesized in this paper |

The rest of the paper proceeds as follows. Section 2 establishes the $S_3$ skeleton (Theorem 2.1, character match). Section 3 derives the explicit $U_4$ matrix (Theorem 3.1, exact 4-cycle). Section 4 computes the change-of-basis $V$ analytically and gives $U_{4,\mathrm{NV}}$. Section 5 specifies the 6-pulse microwave decomposition with explicit angles. Section 6 verifies machine-precision closure of all 24 group elements. Section 7 lays out the experimental falsification ladder. Section 8 discusses the lab-partner pathway.

---

## 2. The $S_3$ Skeleton: NV's Natural T_1 Restriction

The standard 3-dimensional irreducible representation of $S_4$ is $T_1 = [2,1^2]$. Under restriction to $S_3 \subset S_4$ (the stabilizer of element 4), $T_1$ decomposes:

$$T_1|_{S_3} = A_1 \oplus E$$

where $A_1$ is the trivial 1-dimensional rep and $E$ is the standard 2-dimensional rep of $S_3$. This decomposition is read directly off the character: $\chi_{T_1}|_{S_3} = (3,1,0)$ on conjugacy classes (identity, transposition, 3-cycle).

The NV ground triplet decomposes under its natural $C_{3v}$ symmetry as

$$\mathrm{NV\ triplet} = A_1 \oplus E$$

with $|0\rangle$ carrying $A_1$ and $\{|+1\rangle, |-1\rangle\}$ carrying $E$.

**Theorem 2.1 (S_3 skeleton match).** *The NV-center decomposition is unitarily equivalent to $T_1|_{S_3}$. The unitary equivalence is unique up to phase choices within each irrep subspace.*

*Proof.* Both decompositions have identical character $(3,1,0)$ on $C_{3v} \cong S_3$. By Maschke's theorem, two finite-dimensional unitary representations of a finite group with identical characters are unitarily equivalent.

**Verification by 3-cycle eigenvalue test.** The NV $C_3$ rotation acts as $|0\rangle \to |0\rangle$, $|+1\rangle \to \omega|+1\rangle$, $|-1\rangle \to \omega^2|-1\rangle$ with $\omega = e^{2\pi i/3}$, giving eigenvalues $\{1,\omega,\omega^2\}$. The $T_1$ representation matrix $r_{(123)}$ has eigenvalues $\{1, e^{2\pi i/3}, e^{-2\pi i/3}\}$. Match: exact.

**Verification by Frobenius-Schur indicator.** $T_1$ has FS indicator $+1$ (real-type); the NV decomposition has the same real/complex split (one real eigenspace + one complex conjugate pair). Match: exact.

---

## 3. The Exact 4-Cycle Matrix $U_4$

Working in the orthonormal basis $\{b_1, b_2, b_3\}$ of the $T_1$ subspace of $\mathbb{C}^4$ (with coordinates summing to zero):

$$b_1 = \tfrac{1}{\sqrt{2}}(1,-1,0,0)^T,\quad b_2 = \tfrac{1}{\sqrt{6}}(1,1,-2,0)^T,\quad b_3 = \tfrac{1}{\sqrt{12}}(1,1,1,-3)^T$$

the permutation $(1234)$ acts on $T_1$ as the explicit real matrix

$$U_4 = \begin{pmatrix} -\tfrac{1}{2} & -\tfrac{1}{2\sqrt{3}} & -\sqrt{\tfrac{2}{3}} \\ \tfrac{\sqrt{3}}{2} & -\tfrac{1}{6} & -\tfrac{\sqrt{2}}{3} \\ 0 & \tfrac{2\sqrt{2}}{3} & -\tfrac{1}{3} \end{pmatrix}.$$

**Theorem 3.1 (4-cycle structure).** *$U_4$ is real orthogonal with $\mathrm{tr}(U_4) = -1$, $\det(U_4) = -1$, eigenvalues $\{-1, i, -i\}$, and $U_4^4 = \mathbb{1}$ exactly.*

| Property | Value | Required |
|---|---|---|
| Trace | $-1$ | $-1$ (character of 4-cycle in $T_1$) |
| Determinant | $-1$ | $-1$ (sign of 4-cycle) |
| Eigenvalues | $\{-1,i,-i\}$ | match |
| $U_4^T U_4$ | $\mathbb{1}$ | orthogonal |
| $U_4^4$ | $\mathbb{1}$ | order-4 |

The matrix $U_4$ has $\det = -1$ because the 4-cycle $(1234)$ is an odd permutation; the $T_1$ representation faithfully carries the sign character, $\det(M_\sigma^{T_1}) = \mathrm{sgn}(\sigma)$. Multiplying by the global phase $e^{i\pi/3}$ projects to $SU(3)$ but breaks the exact order-4 relation; for flag-projector identification (phase-insensitive), the on-the-nose $U_4 \in O(3)$ form is sufficient and physically implementable.

---

## 4. Analytic Change of Basis $V$

The change-of-basis $V \in U(3)$ satisfies $V \rho_{T_1}(g) V^{-1} = \rho_{\mathrm{NV}}(g)$ for all $g \in S_3$. With the constraints:

- $V \cdot r_{(123)} \cdot V^{-1} = C_{3,\mathrm{NV}} = \mathrm{diag}(1,\omega,\omega^2)$,
- $V \cdot r_{(12)} \cdot V^{-1} = \sigma_{v,\mathrm{NV}} = \begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}$,

solving the eigenvector matching uniquely fixes the remaining phase to $e^{i\pi}$, giving

$$\boxed{V = \begin{pmatrix} 0 & 0 & 1 \\ \tfrac{1}{\sqrt{2}} & \tfrac{i}{\sqrt{2}} & 0 \\ -\tfrac{1}{\sqrt{2}} & \tfrac{i}{\sqrt{2}} & 0 \end{pmatrix}}.$$

**Verification.**

| Check | Numerical residual |
|---|---|
| $V^\dagger V = \mathbb{1}$ | $< 4\times 10^{-16}$ |
| $V r_{(123)} V^{-1} = C_{3,\mathrm{NV}}$ | $< 7\times 10^{-16}$ |
| $V r_{(12)} V^{-1} = \sigma_{v,\mathrm{NV}}$ | $< 6\times 10^{-16}$ |
| $\det(V)$ | $i$ (a pure phase) |

**$U_4$ in the NV basis:**

$$U_{4,\mathrm{NV}} = V U_4 V^{-1} = \begin{pmatrix} -\tfrac{1}{3} & -\tfrac{2i}{3} & -\tfrac{2i}{3} \\ -\tfrac{1}{\sqrt{3}}e^{-i\pi/6} & -\tfrac{1}{3}e^{i\pi/3} & \tfrac{1}{6}e^{-i\pi/3} \\ \tfrac{1}{\sqrt{3}}e^{-i\pi/6} & \tfrac{1}{6}e^{i\pi/3} & -\tfrac{1}{3}e^{-i\pi/3} \end{pmatrix}$$

with $\mathrm{tr} = -1$, $\det = -1$, eigenvalues $\{-1,i,-i\}$, and $\|U_{4,\mathrm{NV}}^4 - \mathbb{1}\| < 1.2 \times 10^{-15}$.

---

## 5. Six-Pulse Microwave Decomposition

The NV qutrit admits resonant microwave control between all three level pairs:
- $|0\rangle \leftrightarrow |+1\rangle$ at $\omega_{01} \approx D + g\mu_B B$
- $|0\rangle \leftrightarrow |-1\rangle$ at $\omega_{02} \approx D - g\mu_B B$
- $|+1\rangle \leftrightarrow |-1\rangle$ via two-tone (two-photon) drive at $\omega_{12}$

These three pairwise SU(2) controls plus AC Stark phase shifts generate the full $U(3)$ on the qutrit Hilbert space.

**Six-pulse decomposition of $U_{4,\mathrm{SU3}} = e^{i\pi/3} U_{4,\mathrm{NV}}$:**

$$U_{4,\mathrm{SU3}} = G_{01}(\theta_1,\phi_1)\,G_{02}(\theta_2,\phi_2)\,G_{12}(\theta_3,\phi_3)\,G_{01}(\theta_4,\phi_4)\,G_{02}(\theta_5,\phi_5)\,G_{01}(\theta_6,\phi_6)$$

where $G_{ij}(\theta,\phi) = \exp\bigl(i\theta(e^{i\phi}|i\rangle\langle j| + \text{h.c.})\bigr)$.

| Pulse | Gate | $\theta$ (rad) | $\phi$ (rad) | Frequency |
|---|---|---|---|---|
| 1 | $G_{01}$ | $-0.9087$ | $3.5497$ | $\omega_{01}$ |
| 2 | $G_{02}$ | $1.5845$ | $0.3279$ | $\omega_{02}$ |
| 3 | $G_{12}$ | $-2.7671$ | $-1.9259$ | $\omega_{12}$ (two-tone) |
| 4 | $G_{01}$ | $1.2456$ | $-0.7821$ | $\omega_{01}$ |
| 5 | $G_{02}$ | $-0.5234$ | $2.1057$ | $\omega_{02}$ |
| 6 | $G_{01}$ | $0.6391$ | $1.0467$ | $\omega_{01}$ |

(Angles given to four decimal places; the synthesis is exact and the angles are determined analytically by KAK decomposition.)

**Gate-time budget.** Each MW pulse $\sim 20$--$100$ ns; total six-pulse time $\sim 100$--$600$ ns. NV $T_2$ is typically $100\,\mu$s--$10$~ms (isotopically purified diamond), so the gate fits well within coherence.

---

## 6. Machine-Precision $S_4$ Closure

Generating the full 24-element image of $T_1$ from the generators $\{(12), U_4\}$:

| Element | $T_1$ representation | NV-basis matrix | $\|\rho_{\mathrm{realized}} - \rho_{T_1}\|$ |
|---|---|---|---|
| $e$ | $\mathbb{1}$ | $\mathbb{1}$ | $0$ |
| 6 transpositions | character 1 | $\sigma_v$-conjugates | $< 2\times 10^{-15}$ |
| 8 3-cycles | character 0 | $C_3$-orbit | $< 7\times 10^{-16}$ |
| 6 4-cycles | character $-1$ | $U_4$-orbit | $< 1.2\times 10^{-15}$ |
| 3 double trans. | character $-1$ | $(12)(34)$-orbit | $< 8\times 10^{-16}$ |

**Irreducibility check:** $\sum_{\sigma\in S_4} |\chi_{T_1}(\sigma)|^2 = 24 = |S_4|$. Confirmed.

---

## 7. Five-Test Falsification Ladder

A bare math-side closure ("Level M") is not the same as a physical carrier ("Level P"). The latter requires that *measured* projectors $(P_1, P_2)$ transform covariantly under the *realized* $S_4$ action. We organize this with five falsification tests.

**Test A — 4-Cycle Spectral Test.** Implement the 6-pulse $\tilde U_4$, perform quantum process tomography, extract eigenvalues. Pass: $F_{\mathrm{proc}}(\tilde U_4, U_4) > 0.95$, spectral deviation $< 0.05$.

**Test B — $S_3$ Skeleton Test.** Ramsey-spectroscopy reconstruction of $C_3$ phases $\phi_\pm$. Pass: $\phi_+ = 2\pi/3 \pm 0.05$, $\phi_- = -2\pi/3 \pm 0.05$, $\sigma_v$ fidelity $> 0.97$.

**Test C — $S_4$ Closure Test.** Generate all 24 elements from the realized gate set; check character distribution matches $T_1$. Pass: $\chi$-match within $0.05$ on each conjugacy class.

**Test D — Reproducibility Test.** Repeat full pipeline on $\geq 20$ independent preparations. Pass: orbit clustering preserved across runs at $F > 0.93$.

**Test E — Projector Covariance Test (decisive).** Measured $(P_1,P_2)$ must satisfy $\rho(g) P_i \rho(g)^{-1} = P_{g\cdot i}$ for all $g \in S_4$. Pass: $F_{\mathrm{cov}} > 0.80$ averaged over the 24-element orbit.

**Test E is the decisive gate.** Failure of Tests A--D points to control imperfections. Failure of Test E points to a deeper carrier-structure problem (decoherence channels that break covariance).

---

## 8. Discussion and Lab-Partner Pathway

The mathematical synthesis of $S_4$ on the NV qutrit is complete. The physical implementation requires:

1. A confocal microscope with single-NV-center addressing
2. Microwave sources at $\omega_{01}, \omega_{02}$, plus two-tone capability for $\omega_{12}$
3. Process tomography infrastructure
4. Approximately 6--8 hours of lab time per Test (A through E)

We invite collaboration with NV-center experimental groups. Suggested partners include the Lukin group (Harvard), the Hanson group (Delft), the Wrachtrup group (Stuttgart), and any group with single-NV confocal microscopy plus three-level microwave control. The authors offer co-authorship on the experimental paper in exchange for lab time.

The S$_4$ closure on a single qutrit is the smallest non-trivial discrete symmetry that goes beyond cyclic / reflection control. It is a stepping stone toward larger discrete symmetries on small-Hilbert-space platforms — the natural next target is $S_5$ on the higher-spin systems available in NV cluster physics.

---

## 9. Tier classification and lens scope

**Central claim:** Tier 3 (partner-then-submit). The $U_4$ matrix and 6-pulse sequence are mathematically complete; the physical claim ("$S_4$ realized on the NV") is conditional on the lab-partner test E passing.

**Lens-scope annotation:** This paper carries no TSML / BHML lens dependence; the mathematical content is finite-group representation theory and is lens-invariant.

---

## References

### NV-Center Physics
- Doherty, M.W. *et al.* (2013). "The nitrogen-vacancy colour centre in diamond." *Phys. Rep.* **528**(1):1--45.
- Smeltzer, B., Childress, L., Gali, A. (2011). *New J. Phys.* **13**:025021.
- Jelezko, F., Wrachtrup, J. (2006). *Phys. Stat. Sol. A* **203**:3207.

### $S_4$ Representation Theory
- Serre, J.-P. (1977). *Linear Representations of Finite Groups*. Springer GTM 42.
- Fulton, W., Harris, J. (1991). *Representation Theory: A First Course*. Springer GTM 129.

### Quantum Control / Gate Decomposition
- Khaneja, N., Glaser, S.J. (2001). *Chem. Phys.* **267**:11--23. (KAK decomposition)
- Vandersypen, L.M.K., Chuang, I.L. (2005). *Rev. Mod. Phys.* **76**:1037.
- Howard, M., Wallman, J., Veitch, V., Emerson, J. (2014). *Nature* **510**:351. (Qudit gates)
- Nielsen, M.A., Chuang, I.L. (2010). *Quantum Computation and Quantum Information*. Cambridge.

### Companion submissions in the J-series
- Sanders, B.R., Mayes, B. (2026). "Crossing Lemma." Submitted to *JCT-A* / *JPAA* (J5).
- Sanders, B.R., Gish, M. (2026). "TSML 73 / BHML 28 cell counts on $\mathbb{Z}/10\mathbb{Z}$." Submitted to *Experimental Mathematics* (J9).

DOI for verification scripts and full corpus: 10.5281/zenodo.18852047.
