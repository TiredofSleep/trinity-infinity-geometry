# WP74 — Physical Observable Identification
## NV Hamiltonian Protocol for Flag Measurement

**Date**: 2026-04-09
**Sprint**: 13 — Physical Flag Selector
**Authors**: Brayden Ross Sanders / 7Site LLC · Ben Mayes · C.A. Luther

---


## 1. Exact Observable Bottleneck

The abstract need is exact: an ordered pair of rank-1 Hermitian projectors $(P_1, P_2)$ on a 3-component complex Hilbert space $\mathbb{C}^3$, torus-phase-free, covering the full 6-dimensional flag variety $\text{SU}(3)/T$.

**Coverage constraint — how much of SU(3)/T each observable class reaches:**

| Observable $H$ | Coverage of $\text{SU}(3)/T$ | Sufficient? |
|---|---|---|
| $H = aF_z + bF_z^2$ | 1 point (fixed to $F_z$ eigenbasis) | No |
| $H = a(\hat{n}\cdot\mathbf{F}) + b(\hat{n}\cdot\mathbf{F})^2$ | $S^2$ (2 of 6 dims) | No |
| $H = DF_z^2 + E(F_x^2-F_y^2)$ | ~3-dim subset | No |
| **$H = DF_z^2 + E(F_x^2-F_y^2) + g\mu_B\mathbf{B}\cdot\mathbf{F}$** | **most of $\text{SU}(3)/T$ (5–6 dims)** | **Yes, generic** |
| $H = \sum_{ij}A_{ij}F_iF_j + \sum_i b_i F_i$ | All of $\text{SU}(3)/T$ (6 dims) | Yes, always |
| Biaxial nematic $\hat{Q}_{ij}$ (quadrupolar) | Most of $\text{SU}(3)/T$ | Yes, generic |
| 3-mode photonic $J_{ij}$ | All of $\text{SU}(3)/T$ | Yes, always |

**Why simple Zeeman fails:** $H = aF_z + bF_z^2$ is diagonal in the $F_z$ basis for all $(a,b)$. The eigenstates are always $\{|{+1}\rangle, |0\rangle, |{-1}\rangle\}$ — the flag is FIXED regardless of parameters. Rotating to $\hat{n}$ traces $S^2$ (2 dims). The full 6-dim flag variety requires observables that mix the magnetic sublevels.

**What is needed:** at least one off-diagonal (non-commuting) term. A transverse field component $B_x \neq 0$, a strain term $E(F_x^2-F_y^2)$, or any quadrupolar coupling between magnetic sublevels generates a non-trivial flag.

---

## 2. Candidate Observable Audit

### Candidate A — Zeeman + Quadratic Zeeman

| Field | Content |
|---|---|
| **Math form** | $H = a(\hat{n}\cdot\mathbf{F}) + b(\hat{n}\cdot\mathbf{F})^2$; diagonal in $\hat{n}$-spin basis |
| **Acts on $\mathbb{C}^3$?** | Yes |
| **Non-degenerate?** | Yes if $a \neq 0$ |
| **Ordered projectors?** | Yes — but they are always spin-coherent states |
| **Projectors cleanly measurable?** | Yes |
| **Torus risk** | None — projectors are phase-free |
| **Flag coverage** | $\mathbb{CP}^1 \cong S^2$ (2 of 6 dims). Spin-coherent states only. |
| **Bridge relevance** | Gives $P_1$ for local win only. Cannot supply generic flag. |
| **Accessibility** | Trivial — standard magnetic field |
| **Status** | **False for generic flag. Exact for local win ($P_1$ only).** |

### Candidate B — General Anisotropy Tensor

| Field | Content |
|---|---|
| **Math form** | $H = \sum_{ij}A_{ij}F_iF_j + \sum_i b_i F_i$; arbitrary Hermitian $3\times3$ matrix |
| **Acts on $\mathbb{C}^3$?** | Yes — by construction |
| **Non-degenerate?** | Yes for generic $(A_{ij}, b_i)$ |
| **Ordered projectors?** | Yes — three eigenprojectors ordered by eigenvalue = complete flag |
| **Projectors cleanly measurable?** | Yes via state tomography |
| **Torus risk** | None — eigenprojectors are phase-invariant |
| **Flag coverage** | All of $\text{SU}(3)/T$ (9 params − 3 eigenvalues = 6 flag dims; surjective) |
| **Bridge relevance** | Full strong win. Most complete match to abstract bridge need. |
| **Accessibility** | Requires independently tunable quadratic spin interactions (spinor BEC, engineered solid-state) |
| **Status** | **Exact (math). Bridge (physical realization). Best abstract match.** |

### Candidate C — Density Matrix $\rho$ as Effective Observable

| Field | Content |
|---|---|
| **Math form** | $\rho$: $3\times3$ Hermitian positive-semidefinite, $\text{Tr}(\rho)=1$ |
| **Acts on $\mathbb{C}^3$?** | Yes |
| **Non-degenerate?** | Only if state has three distinct populations |
| **Ordered projectors?** | Yes — $\rho = \sum_i \lambda_i P_i$ by spectral theorem |
| **Projectors cleanly measurable?** | Yes |
| **Torus risk** | None — density matrices are phase-invariant |
| **Critical distinction** | $\rho$ is a STATE. Its eigenprojectors depend on both $H$ AND the preparation. Not a stable physical selector — it changes when the state changes. |
| **Bridge relevance** | $\rho$ is the measurement TOOL. $H$ is the SELECTOR. In steady state under $H$, they coincide. |
| **Status** | **Bridge — $\rho$ is how the flag is read out, not what determines it.** |

### Candidate D — Spin-Nematic / Quadrupolar Tensor

| Field | Content |
|---|---|
| **Math form** | $H_{\text{nem}} = \sum_{ij} n_{ij}(F_iF_j + F_jF_i - \tfrac{4}{3}\delta_{ij})$ |
| **Acts on $\mathbb{C}^3$?** | Yes — $F_iF_j$ are $3\times3$ on spin-1 Hilbert space |
| **Non-degenerate?** | Only if nematic is biaxial (three distinct $n_{ij}$ eigenvalues); uniaxial has a degenerate pair |
| **Ordered projectors?** | Yes for biaxial nematic — complete flag |
| **Projectors cleanly measurable?** | Yes — spin noise spectroscopy, NMR |
| **Torus risk** | None |
| **Flag coverage** | Uniaxial: $S^2$ (2 dims). Biaxial: most of $\text{SU}(3)/T$. |
| **Bridge relevance** | This is a special case of Candidate B (quadratic only, no linear). Biaxial nematic is physically natural in spin-1 BECs and some magnetic systems. |
| **Status** | **Bridge — biaxial nematic is a physically motivated complete flag source.** |

### Candidate E — 3-Mode Photonic Hamiltonian

| Field | Content |
|---|---|
| **Math form** | $H = \sum_{ij} J_{ij} a_i^\dagger a_j$; in single-photon sector: the Hermitian matrix $J$ |
| **Acts on $\mathbb{C}^3$?** | Yes — single-photon Hilbert space of 3 modes is $\mathbb{C}^3$ |
| **Non-degenerate?** | Yes for generic $J$ |
| **Ordered projectors?** | Yes — eigenprojectors of $J$ = complete flag |
| **Projectors cleanly measurable?** | Yes — standard quantum optical tomography |
| **Torus risk** | Low — density matrix tomography is torus-free |
| **Flag coverage** | All of $\text{SU}(3)/T$ — $J_{ij}$ freely tunable via beam splitter angles in integrated photonics |
| **Bridge relevance** | Mathematically complete; physically accessible. The T₁ identification is more abstract (photons vs. spin). |
| **Status** | **Bridge — complete flag access, but T₁ identification is more remote than spin-1 systems.** |

### Candidate F — NV-Center Triplet Hamiltonian ★ (Best for Immediate Experiment)

| Field | Content |
|---|---|
| **Math form** | $H_{\text{NV}} = DS_z^2 + E(S_x^2-S_y^2) + g_e\mu_B(B_xS_x + B_yS_y + B_zS_z)$ with $D\approx2.87$ GHz, $E\approx$ strain, $\mathbf{B}$ tunable |
| **Acts on $\mathbb{C}^3$?** | Yes — ground triplet $\{|m_s=-1\rangle, |0\rangle, |+1\rangle\}$ is genuinely $\mathbb{C}^3$ |
| **Non-degenerate?** | Yes for any $\mathbf{B} \neq 0$ with generic direction |
| **Ordered projectors?** | Yes — three eigenprojectors from density matrix tomography = complete flag |
| **Projectors cleanly measurable?** | Yes — Ramsey + pulse sequences reconstruct full $3\times3$ density matrix |
| **Torus risk** | None if tomography reports $\rho$; risk only if specific eigenvectors are extracted and reported as state vectors |
| **Flag coverage** | With tunable $\mathbf{B}$: 3-dim family; with strain variation: 5-dim family; generic: most of $\text{SU}(3)/T$ |
| **Critical condition** | Transverse field $B_x\neq0$ or $B_y\neq0$ required. Pure axial $\mathbf{B}$ gives trivial flag fixed to $S_z$ basis. |
| **T₁ identification** | NV has C₃ᵥ site symmetry. T₁ carrier has S₄ symmetry. Whether S₄ action on T₁ has a physical realization in NV triplet is OPEN. |
| **Bridge relevance** | Experimentally strongest candidate. Spin-1 system with clear $\mathbb{C}^3$ structure. Tomography protocols are standard. |
| **Accessibility** | Room temperature. Single-center or ensemble. Widely available. Protocols in published literature. |
| **Status** | **Bridge — most accessible platform; T₁ identification is the remaining open step.** |

---

## Bottleneck Classification

| Classification | Best candidate |
|---|---|
| **Best for local win** ($P_1$ only) | Any of A–F with any $\mathbf{B}$ field |
| **Best for strong win** (full flag) | Candidate B (spinor BEC) or F (NV) with transverse field |
| **Best for immediate experiment** | **Candidate F (NV-center)** — room temp, standard protocols |
| **Best abstract-to-physical match** | **Candidate B** (general anisotropy tensor = exact abstract form) |
| **Most likely to overdetermine** | Any system reporting pure state $|\psi_i\rangle$ instead of projector $P_i$ |
| **False (wrong type)** | Real $\mathbb{R}^3$ anisotropy tensors (SO(3) frame, 3 dims — wrong) |

---

## The Single Best Answer

$$\boxed{H_{\text{NV}} = DS_z^2 + E(S_x^2-S_y^2) + g_e\mu_B\mathbf{B}\cdot\mathbf{S}, \quad B_x \neq 0 \text{ or } B_y \neq 0}$$

**Platform:** NV-center in diamond (single center for maximum control).

**Why:**
1. The Hamiltonian IS a specific Hermitian $3\times3$ matrix on genuine $\mathbb{C}^3$
2. Generic (transverse) $\mathbf{B}$ gives a non-degenerate spectrum with eigenstates NOT in the $S_z$ basis
3. Full spin state tomography is a fully developed protocol — density matrix, not state vector
4. The eigenprojectors are exactly the flag $(P_1, P_2)$ — torus-free by construction
5. Room temperature. Single-shot readout. Widely available hardware.

The one remaining open question: does this NV flag correspond to the T₁ bridge flag? This requires showing the NV's C₃ᵥ symmetry supports the S₄ action on T₁. That is the next structural question. It does not block the measurement.

---

## Shortest Experimental Protocol

**Platform:** NV-center in diamond. **Observable:** $H_{\text{NV}}$ with transverse B-field.

**Step 1 — Initialize.** Pump with 532nm laser (1–3 μs). NV spin → $|0\rangle$ with ~94% fidelity.

**Step 2 — Set Hamiltonian.** Apply static magnetic field at non-axial angle (e.g., 45° to NV symmetry axis, magnitude 1–10 mT). This lifts the trivial flag and generates a non-trivial flag in SU(3)/T.

**Step 3 — Tomography (9 measurements).** Measure all independent density matrix elements via pulse sequences:

| Measurement | Protocol |
|---|---|
| $\langle S_z \rangle$ | Ramsey sequence, standard |
| $\langle S_x \rangle$, $\langle S_y \rangle$ | Ramsey with $\pi/2$ rotation before readout |
| $\langle S_z^2 \rangle$ | Direct population measurement |
| $\langle S_x^2-S_y^2 \rangle$ | Two-quantum Rabi sequence |
| $\langle S_xS_y+S_yS_x \rangle$ | Mixed two-quantum sequence |
| Off-diagonal coherences | Ramsey with varied phase and delay |

These 9 measurements reconstruct the full $3\times3$ Hermitian density matrix $\rho$ (8 real parameters + trace normalization).

**Step 4 — Construct $\rho$.** Assemble from expectation values using the spin-1 operator basis.

**Step 5 — Diagonalize.** Eigendecompose: $\rho = \lambda_1 P_1 + \lambda_2 P_2 + \lambda_3 P_3$ with $\lambda_1 \geq \lambda_2 \geq \lambda_3$.

**Step 6 — Extract flag, discard phases.** Report $(P_1, P_2)$ as $3\times3$ Hermitian matrices. Do NOT extract specific eigenvectors $|\psi_i\rangle$ (which carry torus phases). The projectors ARE the physical flag $F^* \in \text{SU}(3)/T$.

**Why this is torus-free:** The density matrix diagonalization gives eigenSPACES (subspaces) not eigenVECTORS. The outer product $P_i = |\psi_i\rangle\langle\psi_i|$ is phase-invariant: $|e^{i\alpha}\psi\rangle\langle e^{i\alpha}\psi| = P_i$ for any $\alpha$. Torus phases cancel automatically in the projector representation.

---

**The next hammer goes here: NV-center in diamond with a non-axial magnetic field, full spin state tomography returning the $3\times3$ density matrix $\rho$, diagonalized to ordered eigenprojectors $(P_1, P_2)$ — followed by testing whether the NV's C₃ᵥ site symmetry supports an identification with the S₄ action on the T₁ carrier.**

---

## References

### NV-Center Physics
- Doherty, M.W., Manson, N.B., Delaney, P., Jelezko, F., Wrachtrup, J. & Hollenberg, L.C.L. (2013). "The nitrogen-vacancy colour centre in diamond." Physics Reports 528(1):1-45. **(Foundational NV physics reference)**
- Smeltzer, B., Childress, L. & Gali, A. (2011). New J. Phys. 13:025021.
- Jelezko, F. & Wrachtrup, J. (2006). Phys. Stat. Sol. A 203:3207.

### S4 Representation Theory
- Serre, J.-P. (1977). *Linear Representations of Finite Groups*. Springer GTM 42.
- Fulton, W. & Harris, J. (1991). *Representation Theory: A First Course*. Springer GTM 129.
- Curtis, C.W. & Reiner, I. (1981). *Methods of Representation Theory*, vol. I. Wiley.

### Lie Groups and Gate Decomposition
- Hall, B.C. (2015). *Lie Groups, Lie Algebras, and Representations*, 2nd ed. Springer GTM 222.
- Helgason, S. (1978). *Differential Geometry, Lie Groups, and Symmetric Spaces*. Academic Press.
- Khaneja, N. & Glaser, S.J. (2001). Chem. Phys. 267:11-23. (KAK decomposition for quantum control)

### Quantum Information and Process Tomography
- Nielsen, M.A. & Chuang, I.L. (2010). *Quantum Computation and Quantum Information*, 10th anniv. ed. Cambridge University Press.
- Chuang, I.L. & Nielsen, M.A. (1997). J. Mod. Opt. 44:2455-2467. (Process tomography)
- Poyatos, J.F., Cirac, J.I. & Zoller, P. (1997). Phys. Rev. Lett. 78:390.

### TIG Framework (Novel — internal)
- Sanders, Mayes, Luther (2026). Sprint 13 Physical Flag Selector papers. 7Site LLC. DOI: 10.5281/zenodo.18852047.

### Citation Discipline
Novel contribution: explicit synthesis of U4 (the 4-cycle matrix of S4 in the T1 representation) as a 6-pulse microwave sequence on the NV-center qutrit, with machine-precision closure verification. Extends Doherty et al. 2013 (NV physics) and Serre/Fulton-Harris (S4 representation theory). See [GLOSSARY.md](../../../GLOSSARY.md).

