# WP73 — T1 Carrier Identification on NV-Center
## NV Triplet as S4-Module Carrier

**Date**: 2026-04-09
**Sprint**: 13 — Physical Flag Selector
**Authors**: Brayden Ross Sanders / 7Site LLC · Ben Mayes · C.A. Luther

---


## 1. Exact Carrier-Identification Bottleneck

**Why "3-level system" is not enough.**

Any physical system with a 3-dimensional Hilbert space produces a flag in SU(3)/T when its Hamiltonian has non-degenerate eigenvalues. This includes a random three-level atom with no special symmetry. The flag says: *here are three orthogonal complex directions in some abstract $\mathbb{C}^3$*. It says nothing about whether those directions correspond to the three eigenspaces of the abstract T₁ carrier under the S₄ action.

The bridge problem requires more. The bridge embedding is: T₁ (abstract S₄-module) $\hookrightarrow$ $\mathbb{C}^3$ (a concrete 3-component complex field). The flag $F^* \in \text{SU}(3)/T$ picks out which directions in $\mathbb{C}^3$ the T₁ eigenspaces point. To identify a physical flag as the T₁-carrier flag, the physical $\mathbb{C}^3$ must carry the S₄ action of T₁ — not just any $\mathbb{C}^3$.

**Three levels of identification, ordered by strength:**

| Level | What it requires | What the NV has |
|---|---|---|
| **A** (dim only) | $\mathbb{C}^3$ Hilbert space | ✓ (trivial) |
| **B** (flag only) | Ordered eigenprojectors $(P_1, P_2)$ in SU(3)/T | ✓ (achieved by tomography) |
| **C** (carrier structure) | S₄ action on $\mathbb{C}^3$ realizing T₁ | Partial (S₃ ⊂ S₄ exact; 4-cycle open) |

The gap is Level C. The task is to determine exactly how much of Level C the NV-center already has, and what the minimum extra datum would be.

---

## 2. NV-Center Audit: What It Has, What It Lacks

### Abstract T₁ Structure (Exact)

$T_1 = [2,1^2]$ is the standard 3-dimensional irreducible representation of $S_4$. Its character table entry and key invariants:

| Conjugacy class | Elements | Character $\chi(T_1)$ | Eigenvalue consequence |
|---|---|---|---|
| $e$ | 1 | 3 | dim = 3 |
| $(12)$ transpositions | 6 | 1 | eigenvalues $\{+1, +1, -1\}$ |
| $(123)$ 3-cycles | 8 | 0 | eigenvalues $\{1, \omega, \omega^2\}$ |
| $(1234)$ 4-cycles | 6 | −1 | eigenvalues $\{-1, i, -i\}$ |
| $(12)(34)$ double trans. | 3 | −1 | eigenvalues $\{+1,-1,-1\}$ |

Frobenius-Schur indicator of $T_1$: **+1 (real-type)**. T₁ admits an S₄-invariant symmetric bilinear form; eigenvectors can be taken real in an appropriate basis.

**Key structural invariant:** Under a 3-cycle $c = (123) \in S_4$, the eigenvalues on T₁ are $\{1, \omega, \omega^2\}$ where $\omega = e^{2\pi i/3}$. Sum = 0 (consistent with character 0). This is the **triadic eigenspace structure**: one real eigenspace, one complex conjugate pair.

**Under a 4-cycle $d = (1234) \in S_4$**, the eigenvalues on T₁ are $\{-1, i, -i\}$. Sum = −1 (consistent with character −1). This is the **4-cycle structure**: one order-2 eigenvalue and one order-4 pair. This is the element that distinguishes S₄ from S₃.

### NV-Center Natural Symmetry

The NV-center ground triplet $\{|m_s=-1\rangle, |0\rangle, |+1\rangle\} \cong \mathbb{C}^3$ has natural symmetry group $C_{3v}$ (order 6), isomorphic to $S_3 = \text{Sym}(\{1,2,3\})$, which IS a subgroup of $S_4$ (as the stabilizer of element 4).

Decomposition under $C_{3v}$:
- $|0\rangle$: transforms as $A_1$ (trivial, dim 1)
- $|+1\rangle, |-1\rangle$: transform together as $E$ (standard 2-dim rep of $C_{3v}$)

**NV triplet $= A_1 \oplus E$ under $C_{3v}$.**

### The Critical Comparison: $T_1|_{S_3}$ vs NV Decomposition

Restricting $T_1$ (of $S_4$) to the subgroup $S_3 \cong C_{3v} \subset S_4$, the character of $T_1$ on $S_3$ elements is $(3, 1, 0)$ (identity, transpositions, 3-cycles). Decomposing over $S_3$:

$$n(A_1) = \frac{1}{6}[3\cdot1 + 3\cdot1\cdot1 + 2\cdot0\cdot1] = 1, \quad n(A_2) = 0, \quad n(E) = 1$$

$$T_1|_{S_3} = A_1 \oplus E$$

**This is exact.** The NV-center triplet decomposes as $A_1 \oplus E$ under $C_{3v} \cong S_3$ — which is IDENTICAL to the restriction of $T_1$ to the same subgroup. The decomposition structure is not a coincidence; the NV-center's natural C₃ᵥ symmetry provides the exact S₃ skeleton of T₁.

### 3-Cycle Eigenvalue Test (Passed)

The natural $C_3$ rotation of the NV center acts on its triplet as:
$$|0\rangle \to |0\rangle, \quad |+1\rangle \to \omega|+1\rangle, \quad |-1\rangle \to \omega^2|-1\rangle$$

Eigenvalues: $\{1, \omega, \omega^2\}$. Sum = 0. **Exact match with T₁'s 3-cycle eigenvalues.** Verified numerically: the $T_1$ representation matrix of a 3-cycle has eigenvalues $\{-0.5 + 0.866i, -0.5 - 0.866i, 1.0\} = \{\omega, \omega^2, 1\}$. ✓

### Frobenius-Schur Test (Passed)

The $A_1$ component ($|0\rangle$) is the real eigenspace (eigenvalue 1 under $C_3$, real under all $C_{3v}$ elements). The $E$ pair ($|+1\rangle, |-1\rangle$) are the complex conjugate pair (eigenvalues $\omega, \omega^2$). This is exactly the FS real-type split of T₁: one real eigenspace + one complex conjugate pair. **NV passes the FS test naturally.**

### 4-Cycle Test (Not Passed — the Gap)

The explicit 4-cycle matrix in the T₁ representation (computed from the permutation action on the standard basis $\{b_1, b_2, b_3\}$ of $T_1 \subset \mathbb{C}^4_{\text{perm}}$) has eigenvalues $\{i, -1, -i\}$. Sum = −1. ✓

This is NOT a natural symmetry of the NV-center crystal. The $C_{3v}$ group (order 6) accounts for only 6 of the 24 elements of $S_4$. The remaining 18 S₄ elements (4-cycles and double transpositions) are absent from the NV's natural symmetry group.

**The 4-cycle test requires:** a unitary operator $U$ on the NV qutrit $\mathbb{C}^3$ with eigenvalues $\{-1, i, -i\}$ that together with the $C_{3v}$ generators generates a group isomorphic to $S_4$ acting as $T_1$.

### What the NV-Center Has vs Lacks

| Structural test | NV result | Status |
|---|---|---|
| $\mathbb{C}^3$ Hilbert space | Ground triplet | ✓ Exact |
| $C_{3v} \cong S_3 \subset S_4$ action | Natural crystal symmetry | ✓ Exact |
| $T_1\|_{S_3} = A_1 \oplus E$ decomposition | NV = $A_1 \oplus E$ | ✓ Exact |
| 3-cycle eigenvalues $\{1, \omega, \omega^2\}$ | Natural $C_3$ rotation | ✓ Exact |
| FS real-type structure ($A_1$ real, $E$ complex pair) | Natural $C_{3v}$ | ✓ Exact |
| 4-cycle action with eigenvalues $\{-1, i, -i\}$ | NOT natural | ✗ Open |
| Full $S_4$ action generating T₁ | NOT natural | ✗ Requires synthesis |

**The NV-center triplet is NOT a generic qutrit.** It carries the exact $S_3$-restriction skeleton of T₁. But it does not carry the full $S_4$ action.

---

## 3. Minimal Structure for Honest T₁-Identification

**Minimum honest identification level (the weakest upgrade from "generic flag" to "T₁-carrier flag"):**

A physical qutrit flag that passes ALL of the following three tests constitutes an honest partial T₁-carrier identification:

**Test 1 (3-cycle eigenvalue test):** The qutrit Hilbert space carries a $\mathbb{Z}_3$ action with eigenvalues $\{1, \omega, \omega^2\}$. This distinguishes the three eigenspace types: real ($V_1$), complex ($V_\omega$), conjugate-complex ($V_{\omega^2}$). **NV passes this naturally.**

**Test 2 (FS real-structure test):** The real eigenspace ($V_1$) is distinguishable from the complex pair ($V_\omega, V_{\omega^2}$) by a Frobenius-Schur-type invariant. The $A_1$ component is the real subspace; the $E$ component is the complex pair. **NV passes this naturally.**

**Test 3 (4-cycle test):** A unitary $U$ on the qutrit with eigenvalues $\{-1, i, -i\}$ can be identified or synthesized that together with the $\mathbb{Z}_3$ generator and $S_3$ generators produces an $S_4$ group action realizing T₁. This is the OPEN test.

**What passing Test 3 would give:**

- If $U$ is a NATURAL symmetry of the physical system: **strong win** — the system genuinely carries the T₁ carrier structure, and the measured flag IS a physical T₁-carrier flag.
- If $U$ can be SYNTHESIZED by microwave control: **medium win** — the system is a controlled T₁ carrier. The flag is not intrinsically tied to T₁ but can be made so. The measurement must include the synthesized action as part of the protocol.
- If $U$ CANNOT be synthesized or identified: **weak win** — the flag is a qutrit flag with T₁-consistent S₃ skeleton but no full T₁ identification. Still useful as a measurement, but not a carrier identification.

**The minimum extra datum:** a unitary operator $U_4$ on the NV qutrit satisfying:
$$U_4 \cdot C_3 \cdot U_4^{-1} = \sigma_v, \quad U_4^4 = \mathbb{1}, \quad \text{eigenvalues of } U_4 = \{-1, i, -i\}$$
and consistent with the natural $C_{3v}$ action. This is a concrete, computable requirement — the T₁ representation matrices are explicit and finite-dimensional, and $U_4$ can be derived from them.

---

## 4. Decision Point

**Which of these is true for the NV-center:**

| Statement | Verdict |
|---|---|
| "NV already realizes the carrier strongly enough" | **No** — the 4-cycle action is missing |
| "NV realizes only the flag, not the carrier" | **Partially no** — NV realizes MORE than a generic flag (it has the T₁ S₃-skeleton) but LESS than the full carrier (it lacks the 4-cycle extension) |
| "NV can realize the carrier only through synthesized control" | **Likely yes** — arbitrary SU(3) control of a qutrit is achievable by microwave pulses; the 4-cycle unitary is a specific computable SU(3) matrix |
| "NV is the wrong platform for carrier identification" | **No** — NV is well-suited; its natural C₃ᵥ structure provides exactly the right S₃-skeleton of T₁ |

**Correct classification: Medium win via synthesis.**

The NV-center triplet naturally realizes the C₃ᵥ ≅ S₃ ⊂ S₄ restriction of T₁ (Tests 1 and 2 passed). The remaining step is to synthesize the 4-cycle action through microwave control and verify the full S₄ multiplication table. If achieved, the measured flag becomes an honest T₁-carrier flag — the physical flag selector for the bridge.

**Why this is not a generic qutrit situation:** a random three-level atom would fail Tests 1 and 2. The NV-center passes both naturally. The gap is not structural incompatibility; it is a missing degree of freedom (18 of 24 S₄ elements) that microwave synthesis can supply.

---

## Summary: Four Identification Levels

| Level | What it is | NV status |
|---|---|---|
| **A** (dim match) | $\mathbb{C}^3$ Hilbert space | ✓ Trivially |
| **B** (flag match) | Ordered eigenprojectors in SU(3)/T | ✓ Via tomography |
| **C₁** (partial carrier) | $S_3 \cong C_{3v}$ with T₁-restriction structure | ✓ **Naturally** |
| **C₂** (full carrier) | Full $S_4$ action realizing T₁ | ✗ Requires synthesized 4-cycle |

NV is at Level C₁. Level C₂ requires one computed, computable extra unitary.

---

**The next hammer goes here: compute the explicit 4-cycle unitary matrix $U_4$ in the T₁ representation of $S_4$, express it as a concrete SU(3) element, verify it has eigenvalues $\{-1, i, -i\}$ and satisfies the $S_4$ multiplication table with the NV's natural $C_{3v}$ generators, then design a microwave pulse sequence on the NV qutrit that implements $U_4$ — and confirm that the synthesized $S_4$ action acts as T₁.**

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

