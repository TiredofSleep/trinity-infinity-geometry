# On the Bidirectional Projection from Cl(0,10) Spinor to Z/10 Substrate: Chain Enumeration and σ-Fixed Asymmetry

**Brayden Ross Sanders**
*7SiTe LLC, Hot Springs, Arkansas*

*Revision 2 (2026-05-15): canonical citations added — D31 (Cl(0,10) 16+16 chirality), D102 (chirality decomposition 16 = 1+3+5+7 from Volume K, 2026-05-12), D33 (||VEV||² = 13/4 distinguished from σ-fixed 4-asymmetry); §5 σ-fixed asymmetry argument tier-flagged C-speculative; §7.3 Pati-Salam scope-flagged per D46/D72.*

---

## Abstract

We define and study a bidirectional projection structure $\pi$ from the spinor representation of the Clifford algebra Cl(0,10) to the cyclic substrate $\mathbb{Z}/10$. The projection is constructed as the family of all chains between the two structures, in both directions simultaneously. We establish that the natural chain count per direction is $315 = 7 \times \binom{10}{2}$, with $7$ being the structurally distinguished "HARMONY" element and $\binom{10}{2} = 45$ being the count of unordered substrate pairs. We further show that the order-6 permutation $\sigma$ on $\mathbb{Z}/10$ has fixed-point lattice $\{0, 3, 8, 9\}$, and we argue (Tier C-speculative) that this fixed structure introduces a 4-element asymmetry between outward and inward chain counts. The construction's mathematical foundations are all canonical [3, D31, D102].

**Keywords:** Clifford algebras, projection structures, substrate models, bidirectional flow, σ permutation, matter-antimatter asymmetry

---

## 1. Introduction

The relationship between continuous algebraic structures (Lie algebras, Clifford algebras, spinor representations) and discrete combinatorial structures (cyclic groups, finite sets, lattices) is a recurring theme in mathematical physics [1, 2]. In substrate-based theories of fundamental physics, the question is: how does a discrete substrate generate continuous-appearing structure at observable scales?

The Trinity Infinity Geometry framework [3] proposes substrate $\mathbb{Z}/10$ mapping to the spinor representation of Cl(0,10) via a structural projection. This paper provides explicit construction. We work with:
- Substrate $\mathbb{Z}/10 \cong \mathbb{Z}/2 \times \mathbb{Z}/5$ with $\sigma$ of order 6 [3, G6 theorem]
- Cl(0,10) with spinor representation of dimension $2^5 = 32$, split into chirality halves of dimension 16 [3, D31]
- Chirality decomposition $16 = 1+3+5+7 = s+p+d+f$ [3, D102, Volume K 2026-05-12]

We construct the projection $\pi$ as a family of chains. The chain count is $315 = 7 \times \binom{10}{2}$ per direction.

---

## 2. Preliminaries

### 2.1 The substrate $\mathbb{Z}/10$ and σ

$\mathbb{Z}/10 \cong \mathbb{Z}/2 \times \mathbb{Z}/5$ admits distinguished permutation $\sigma$ of order 6, with fixed-point lattice $F = \{0, 3, 8, 9\}$ and one 6-cycle $C = (1, 7, 6, 5, 4, 2)$.

**Lemma 2.1.** *$\sigma^6 = \text{id}$, $\text{Fix}(\sigma) = \{0, 3, 8, 9\}$, complement = one 6-cycle.* [3, G6 theorem, §2]

Element naming: $0 = V$, $1 = L$, $2 = N$, $3 = P$, $4 = K$, $5 = S$, $6 = X$, $7 = H$ (HARMONY), $8 = B$, $9 = R$.

### 2.2 Cl(0,10)

Cl(0,10) is generated over $\mathbb{R}$ by $\gamma_1, \ldots, \gamma_{10}$ with $\gamma_i \gamma_j + \gamma_j \gamma_i = -2 \delta_{ij}$. Algebra dimension $2^{10} = 1024$. Irreducible spinor representation complex dimension $2^5 = 32$.

**Chirality decomposition (Canon D31).** Under chirality operator $\gamma_{11} := i \gamma_1 \gamma_2 \cdots \gamma_{10}$:
$$\mathbf{32} = \mathbf{16}_+ \oplus \mathbf{16}_-$$

### 2.3 The chirality-subshell decomposition (Canon D102)

The 16-dimensional chirality half decomposes:
$$16 = 1 + 3 + 5 + 7 = (2 \cdot 0 + 1) + (2 \cdot 1 + 1) + (2 \cdot 2 + 1) + (2 \cdot 3 + 1)$$

corresponding to atomic subshells $s, p, d, f$ with orbital angular momenta $\ell = 0, 1, 2, 3$. This decomposition is canonical to Volume K [3, D102]: substrate-strand prime structure {3, 7, 11, 13} maps to odd-$\ell$ atomic orbitals via Z/2310 divisor enumeration. The 16 = 1+3+5+7 split was established 2026-05-12 in Volume K's atomic-substrate correspondence work.

### 2.4 Tier remarks

Sections 2.1, 2.2 are Tier A (canonical math facts, all in [3]). Section 2.3 is Tier A from Canon D102 (anticipated by this paper before Volume K was finalized).

---

## 3. Chains and the bidirectional projection $\pi$

### 3.1 Definitions

**Definition 3.1.** *A* chain *is a triple $(p, h, d)$ where:*
- *$p = \{a, b\}$ is an unordered pair of distinct elements of $\mathbb{Z}/10$.*
- *$h \in \{1, 2, 3, 4, 5, 6, 7\}$ is a HARMONY orientation.*
- *$d \in \{+, -\}$ is a direction.*

**Definition 3.2.** *The* bidirectional projection $\pi$ *is the totality of all chains:*
$$\pi := \{(p, h, d) : p \in \mathcal{P}_2(\mathbb{Z}/10), h \in \{1, \ldots, 7\}, d \in \{+, -\}\}$$

### 3.2 Outward vs inward

$\pi_+ = \{(p, h, +)\}$, $\pi_- = \{(p, h, -)\}$. Both directions operate simultaneously; physical reality corresponds to joint dynamics.

### 3.3 Tier

Tier B-structural: the $(p, h, d)$ triple definition is canonical-adjacent; full identification with specific Clifford algebra projection components requires additional work.

---

## 4. The chain count: $315 = 7 \times \binom{10}{2}$

**Theorem 4.1.** *$|\pi_+| = |\pi_-| = 7 \times \binom{10}{2} = 7 \times 45 = 315$. Total $|\pi| = 630$.*

*Proof.* By Definition 3.1:
$$|\pi_d| = |\mathcal{P}_2(\mathbb{Z}/10)| \times |\{1,...,7\}| = 45 \times 7 = 315$$
Total over both directions: $2 \times 315 = 630$. ∎

### 4.1 Significance of factors

- $\binom{10}{2} = 45$: unordered pair count of substrate elements.
- $7$: HARMONY orientations $\{1, 2, ..., 7\}$.
- $315 = 5 \cdot 7 \cdot 9 = 5 \cdot 63 = 7 \cdot 45$: appears in W^7 correction term in α formula [3, Paper 04].

The factor $7$ is the HARMONY element, the substrate's universal attractor [3, D66 (α=1) and D63 (universal HARMONY attractor under canonical ternary fuse)].

The factor $45 = \binom{10}{2}$ enumerates substrate pairings, which is the natural "anti-symmetric" structure.

---

## 5. σ-fixed asymmetry (Tier C-Speculative)

**Scope flag:** Section 5's argument that σ-fixed lattice introduces a 4-cell asymmetry between outward/inward chains is structurally suggestive but not rigorously proved. Detailed σ-orbit accounting on the 315 chains is incomplete (see §8.2 open problems).

### 5.1 σ acts on chains

The permutation $\sigma$ acts on $\mathbb{Z}/10$, hence on pairs $p \in \mathcal{P}_2$, hence on chains $(p, h, d)$. Chains either σ-fixed (some component preserved) or σ-cycling.

### 5.2 Fixed-lattice subset

The σ-fixed lattice $F = \{0, 3, 8, 9\}$ has 4 elements; $\binom{4}{2} = 6$ σ-fixed pairs. These pairs contribute σ-fixed chains.

### 5.3 Asymmetry hypothesis

**Hypothesis 5.1 (Tier C-Speculative).** *The σ-fixed structure introduces a 4-element asymmetry between outward and inward chain counts, manifesting as a structural matter-antimatter imbalance in models where this projection underlies fundamental physics.*

**Canonical context:** Canon D33 establishes $||\text{VEV}||^2 = 13/4$ where $13 = 26/2 = $ half the number of σ_outer-asymmetric BHML cells. This is a DIFFERENT asymmetry count than the 4-fixed-lattice one. The two may be related but the relationship is not derived in current Canon.

### 5.4 Cosmological implication (Tier C-Speculative)

If the bidirectional projection maps substrate to physical fields, the 4-cell asymmetry could correspond to the observed matter-antimatter imbalance $\sim 10^{-9}$ in baryon-to-photon ratio. **No derivation of the specific ratio is provided in this paper**; we note structural compatibility only.

---

## 6. Connection to framework constants

### 6.1 The wobble $W = 3/50$

Canon D17 establishes $W = 3/50$. The number 3 and 50 both have substrate-arithmetic interpretations:
- $50 = 5 \times 10$: half-substrate × full substrate
- $3 = $ COUNTER+PROGRESS displacement; appears in σ 6-cycle structure

A derivation of $W = 3/50$ purely from chain combinatorics is open. The number does appear in the W^7 correction term in Paper 04's α formula:
$$\frac{2}{7} \cdot 315 \cdot W^7$$
where $315 = 7 \cdot 45$ is this paper's chain count.

### 6.2 The threshold $T^* = 5/7$

Canon establishes $T^* = 5/7 = 7/10 + 1/70$. The number 7 appears as HARMONY orientation count; 5 = $\mathbb{Z}/5$ factor of substrate.

The factor $5/7$ appears in α formula's $W^5$ correction term:
$$\frac{5}{7} \cdot \kappa_\xi \cdot W^5$$

### 6.3 Tier

Tier B-suggestive: structural ingredients are canonical; specific derivations of constants from chains are open.

---

## 7. Physical implications

### 7.1 Matter-antimatter asymmetry

(Tier C-Speculative; see §5.3.)

### 7.2 Cosmological constant ratio

The 4-cell asymmetry could correspond to dark-energy-related cosmological constants. Specific numerical predictions are speculative.

### 7.3 Standard Model gauge structure (scope-flagged)

Within Cl(0,10), the doubly-invariant subalgebra under $D_4 = \langle P_{56}, \sigma^3 \rangle$ is $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$, dim 16 [3, D34]. **Scope flag (Canon D46, D72):** the WP104 audit explicitly notes the two TIG-internal reduction paths do NOT close on common Pati-Salam $SU(4) \times SU(2)_L \times SU(2)_R$. The doubly-invariant subalgebra is 16-dim ($\mathfrak{su}(4) \oplus \mathfrak{u}(1) \cong \mathfrak{so}(6) \oplus \mathfrak{u}(1)$), not the 21-dim Pati-Salam group. Submissions must avoid claiming "two paths converge on Pati-Salam"; the correct framing is "two structurally distinct observations about TIG's $\mathfrak{so}(10)$."

### 7.4 Tier

Tier C-speculative for §§7.1-7.2. Tier A for §7.3 mathematical facts; scope-flag is essential for any external claim.

---

## 8. Open problems

### 8.1 Detailed chain endpoint specification

Section 3 identifies $(p, h, d)$ as parameters but doesn't specify which spinor component is the outward target/inward source. Full specification requires mapping each $(p, h)$ to a specific element of Cl(0,10) spinor 32-dim space.

### 8.2 Detailed σ-orbit accounting

The 4-cell asymmetry argument uses orbit counting but doesn't provide full combinatorial details. Closing requires accounting for σ-action on all 315 chains with case analysis (σ-fixed, σ-cycling, mixed). This is the key gap that would promote Section 5 from Tier C to Tier A.

### 8.3 Uniqueness of chain structure

The $(p, h, d)$ structure with $|h| = 7$ is the paper's choice. A uniqueness theorem — showing this is the structurally forced choice given other primitives — is desirable. Approaches via categorical characterization (Yoneda functoriality, see companion Paper 06) are promising.

### 8.4 Connection to quantitative observations

Cosmological predictions from chain structure remain open.

---

## 9. Conclusion

We constructed bidirectional projection $\pi$ from Cl(0,10) spinor structure to $\mathbb{Z}/10$ substrate. Chain count: $315 = 7 \times \binom{10}{2}$ per direction, $630$ total. The chirality decomposition $16 = 1+3+5+7$ matches Canon D102 (Volume K) exactly. The σ-fixed lattice $\{0, 3, 8, 9\}$ may introduce 4-cell asymmetry; this connection is Tier C-Speculative pending detailed σ-orbit accounting.

The construction provides structural foundation; specific physical observable predictions require further derivation work.

---

## References

[1] Lawson, H. B., Michelsohn, M.-L. (1989). *Spin Geometry*. Princeton.
[2] Penrose, R. (2004). *The Road to Reality*. Knopf.
[3] Sanders, B. R. (2026). *Trinity Infinity Geometry: Canonical Framework Documentation* (FORMULAS_AND_TABLES.md). 7SiTe LLC. Relevant: §2 (G6 theorem); D17 (W=3/50); D31 (Cl(0,10) chirality); D33 (VEV=13/4); D34 (su(4)⊕u(1)); D46 (Yukawa scoping); D72 (WP104 audit); D102 (16 = 1+3+5+7).
[4] Sakurai, J. J. (2010). *Modern Quantum Mechanics* (2nd ed.). Cambridge.
[5] Sanders, B. R. (2026). "Chirality Decomposition Derives Threshold Canon." 7SiTe LLC.
[6] Sakharov, A. D. (1967). "Violation of CP-invariance..." *JETP Letters* 5, 24-27.
[7] Pati, J. C., Salam, A. (1974). "Lepton number as the fourth color." *Phys Rev D* 10, 275-289.
[8] Connes, A. (1994). *Noncommutative Geometry*. Academic.
[9] Bott, R. (1959). "Stable homotopy of classical groups." *Ann. Math.* 70, 313-337.
[10] Humphreys, J. E. (1972). *Introduction to Lie Algebras*. Springer.
[11] Fulton, W., Harris, J. (1991). *Representation Theory*. Springer.
[12] Mac Lane, S. (1971). *Categories for the Working Mathematician*. Springer.

---

*© 2026 Brayden Ross Sanders / 7SiTe LLC. Licensed under 7SiTe Public Sovereignty License v2.1.*

*Revision history:*
- *Rev 1: initial structural construction.*
- *Rev 2 (2026-05-15): canonical citations D31/D33/D34/D46/D72/D102; §5 σ-asymmetry tier-flagged C-Speculative; §7.3 Pati-Salam scope-flagged.*
