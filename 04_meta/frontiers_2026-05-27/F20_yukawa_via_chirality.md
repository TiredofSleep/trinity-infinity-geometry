# Frontier F20 — Yukawa structure via J37 Cl(0,10) chirality + 1+3+5+7 substrate decomposition

**Status:** REPRESENTATION-THEORY COMPUTATION COMPLETE. **Verdict: PARTIAL CORRESPONDENCE.** The substrate decomposition `1+3+5+7 = 16` IS a representation-theoretic decomposition of the 16-spinor of SO(10) — specifically, it is the branching under the sl(2)-triple associated to the **(5, 5) nilpotent orbit** of so(10), which is the "diagonal principal sl(2)" of the SO(5) x SO(5) subgroup. However, this sl(2) does NOT match the standard SU(5) x U(1) decomposition (1 + 5bar + 10) that gives SM fermion identification, NOR does it match the Pati-Salam SU(2)_L x SU(2)_R (which gives 8+8). The 1+3+5+7 substrate decomposition is therefore NOT a coincidence (it's a real Lie-algebraic structure), but it is NOT the standard GUT-fermion decomposition (so it gives no Yukawa numerical prediction). The atomic-shell rhyme "1+3+5+7 = (2l+1) for l = s, p, d, f at n = 4" (J37 §2.1, Volume K D101-D102) is upgraded from "structural rhyme" to "the SU(2)-spin labels of the (5,5)-orbit sl(2)" — but the SM identification fails because the (5,5) sl(2) mixes left/right rather than separating them.

**Verification:** [`../../verification/frontier_F20_yukawa_via_chirality.py`](../../verification/frontier_F20_yukawa_via_chirality.py) (stdlib + sympy not required; enumeration of all 16 type-D nilpotent orbits of so(10) + sl(2)-branching of 16-spinor + Yukawa-irrep cross-check; runtime <1s).
**Date:** 2026-05-30.
**Builds on:** J37 §2.1 (Cl(0,10) chirality split + atomic-substrate refinement); J11 (9-vector inside 54 of so(10)); F7/F8/F11/F15 Yukawa-RG arc (closed as SUBSTRATE INDEPENDENT at GUT scale).

---

## §1 — J37 setup recap

### §1.1 Cl(0,10) construction (J37 §2.1)

Ten gamma matrices $\gamma_a$ on $\mathbb{C}^{32}$ built from Pauli tensor products in standard Cl(0,10) convention satisfy all 100 anticommutation relations $\{\gamma_a, \gamma_b\} = 2\delta_{ab} I$. The 45 generators $\Sigma_{ab} = (1/4)[\gamma_a, \gamma_b]$ form a faithful 32-dimensional representation of $\mathfrak{so}(10) = D_5$. The volume element $\omega = \gamma_1 \cdots \gamma_{10}$ satisfies $\omega^2 = -I$, and chirality projectors $P_\pm = (I \pm i\omega)/2$ split $\mathbb{C}^{32}$ as $16 + 16$ (left + right chirality).

### §1.2 P_56 = sigma_outer + the atomic-substrate refinement

The $5 \leftrightarrow 6$ swap on $\mathbb{R}^{10}$ is implemented in the Clifford algebra by conjugation with $P_{56}^{\text{spin}} = (\gamma_5 - \gamma_6)/\sqrt{2}$, which anticommutes with $\omega$ and therefore exchanges the two chiral 16-irreps. This identifies $P_{56}$ with $\sigma_{\text{outer}}$ (the unique nontrivial outer automorphism of so(10)) — the standard SO(10)-GUT matter/antimatter exchange.

### §1.3 The 1+3+5+7 atomic-substrate refinement (Volume K D101-D102)

J37 §2.1 documents:

> Each 16-dim chirality half admits a finer structural decomposition: $16 = 1 + 3 + 5 + 7$, indexed by spatial-state count $(2\ell + 1)$ for $\ell = 0, 1, 2, 3$ — i.e. atomic shell $n = 4$ at fixed spin.

From the substrate side, 1+3+5+7 reads as (kernel base) + (strand 1 = prime 3) + (kernel-Z/5 partner = prime 5) + (strand 2 = prime 7). The triple coincidence is: $\mathbb{Z}/2310$ has 32 divisors = atomic Pauli capacity at $n=4$ = Cl(0,10) spinor dim.

J37 marks this as **STRUCTURAL RHYME**, not derivation.

**F20's question:** is 1+3+5+7 actually a representation-theoretic decomposition of the 16-spinor under some Lie-subgroup of SO(10), or is it just a numerical partition coincidence?

---

## §2 — Standard 16 of SO(10) and SM fermion mapping

The standard SU(5) x U(1) decomposition of the 16 of SO(10) is:

$$
\mathbf{16} \;=\; \mathbf{1}_{-5} \;\oplus\; \overline{\mathbf{5}}_{+3} \;\oplus\; \mathbf{10}_{-1}
$$

with U(1) charges as subscripts (Slansky 1981).

The SM fermion content per generation:

| SU(5) irrep | dim | SM components | Hypercharge under U(1)_Y |
|---|---:|---|---|
| **1** | 1 | $\nu_R^c$ (sterile RH neutrino) | 0 |
| **5̄** | 5 | $d_R^c$ (color triplet) + $L_L = (e_L, \nu_L)$ (lepton doublet) | $(+1/3, -1/2)$ |
| **10** | 10 | $Q_L = (u_L, d_L)$ (quark doublet, 6) + $u_R^c$ (3) + $e_R^c$ (1) | $(1/6, -2/3, +1)$ |

Total: $1 + 5 + 10 = 16$ ✓.

**The standard 16 x 16 Yukawa contractions** are with Higgs irreps:

$$
\mathbf{16} \otimes \mathbf{16} \;=\; \underbrace{\mathbf{10}_s}_{\text{Dirac}} \;\oplus\; \underbrace{\mathbf{120}_a}_{\text{antisym Dirac}} \;\oplus\; \underbrace{\mathbf{126}_s}_{\text{Majorana RH-}\nu}
$$

(symmetric = 10 + 126, antisymmetric = 120; total 10 + 120 + 126 = 256 = 16²).

**The substrate decomposition 1+3+5+7 is DISTINCT from the standard 1 + 5bar + 10**:
- Substrate `1` matches the SU(5) singlet (1-dim).
- Substrate `3` has no direct SU(5) irrep in the 16 (the 5bar has SM "color triplet" content, but 3 is not an SU(5) irrep on its own inside 16).
- Substrate `5` is dim-matched with SU(5) 5bar but is structurally different (substrate 5 is an SU(2)-quintet, SU(5)-5bar is an SU(5)-anti-fundamental).
- Substrate `7` doesn't match SU(5) 10 (dim 7 ≠ 10).

**Pati-Salam decomposition** (SO(10) → SU(4) × SU(2)_L × SU(2)_R): the 16 branches as $(4, 2, 1) + (\bar 4, 1, 2) = 8 + 8$. Also distinct from 1+3+5+7.

So the natural standard-GUT decompositions do not give 1+3+5+7. **The question:** is there ANY subgroup G of SO(10) under which 16 branches as 1+3+5+7?

---

## §3 — Search for subgroup G with 16 → 1+3+5+7

### §3.1 Lie-algebraic enumeration

The natural candidates for subgroups G of SO(10) under which 16 might branch as irreps of dimensions $\{1, 3, 5, 7\}$:

| Candidate G | 16 branching | Match? |
|---|---|---|
| SU(5) x U(1) | $1 + 5 + 10$ | NO |
| Pati-Salam SU(4) x SU(2) x SU(2) | $(4,2,1) + (\bar 4,1,2) = 8 + 8$ | NO |
| SO(7) | (8-dim spinor) | NO |
| SO(8) | $8_s + 8_c$ | NO |
| SO(5) x SO(5) | $4 \otimes 4 = 16$ as $(4,4)$ irreducibly | NO (single irrep) |
| **SU(2) [principal embedding]** | depends on embedding | TEST |
| **SU(2) [non-principal embedding]** | depends on embedding | TEST |

The natural place to find dimensions $\{1, 3, 5, 7\}$ is **SU(2)** (or SO(3)), whose irreps have dimension $2j+1$ for integer/half-integer spin $j$. For integer-spin irreps with $j = 0, 1, 2, 3$ we get dimensions $1, 3, 5, 7$ summing to 16. 

**Question:** does there exist an sl(2)-embedding inside so(10) whose 16-spinor branching is $1+3+5+7$?

### §3.2 Nilpotent orbits and their sl(2)-triples

The nilpotent orbits in so(10) are classified by **type-D partitions of 10**: partitions where even parts appear with even multiplicity (Collingwood-McGovern 1993, Theorem 5.1.4). For each such orbit, the Jacobson-Morozov theorem gives an associated sl(2)-triple $\{H, E, F\}$, unique up to conjugacy, and the 10-vector and 16-spinor representations decompose into sl(2)-irreps.

The 16 type-D partitions of 10 enumerated by the verification script:

```
(9, 1)                      (4, 4, 1, 1)               (3, 1, 1, 1, 1, 1, 1, 1)
(7, 3)                      (3, 3, 3, 1)               (2, 2, 2, 2, 1, 1)
(7, 1, 1, 1)                (3, 3, 2, 2)               (2, 2, 1, 1, 1, 1, 1, 1)
(5, 5)                      (3, 3, 1, 1, 1, 1)         (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
(5, 3, 1, 1)                (3, 2, 2, 1, 1, 1)
(5, 2, 2, 1)
(5, 1, 1, 1, 1, 1)
```

### §3.3 Computing the 16-spinor branching

**Method.** For a partition $\lambda = (\lambda_1, \ldots, \lambda_k)$ of 10, the sl(2)-triple acts on the 10-vector $V$ with eigenvalues $\{\lambda_i - 1, \lambda_i - 3, \ldots, -(\lambda_i - 1)\}$ for each block. To compute the spinor action, take the "positive half" $\{a_1, \ldots, a_5\}$ of these eigenvalues (one per $\pm$-pair in the orthogonal pairing of $V$), then for each chiral 16-spinor weight $(\epsilon_1, \ldots, \epsilon_5)/2$ with $\sum \epsilon_i = $ even, the sl(2)-Cartan eigenvalue is $\frac{1}{2}\sum_i \epsilon_i a_i$.

Decomposing the resulting 16-element multiset into sl(2)-irreps gives the spinor branching.

**Result (per `frontier_F20_yukawa_via_chirality.py`):**

| Nilpotent orbit | 16-spinor sl(2)-branching |
|---|---|
| (9, 1) [principal] | $5 + 11$ |
| (7, 3) | $2 + 6 + 8$ |
| (7, 1, 1, 1) | $1 + 1 + 7 + 7$ |
| **(5, 5)** | **$1 + 3 + 5 + 7$ ← MATCH** |
| (5, 3, 1, 1) | $3 + 3 + 5 + 5$ |
| (5, 2, 2, 1) | $3 + 4 + 4 + 5$ |
| (5, 1, 1, 1, 1, 1) | $4 + 4 + 4 + 4$ |
| (4, 4, 1, 1) | $1 + 1 + 1 + 4 + 4 + 5$ |
| (3, 3, 3, 1) | $2 + 2 + 2 + 2 + 4 + 4$ |
| (3, 3, 2, 2) | $1 + 1 + 2 + 2 + 3 + 3 + 4$ |
| (3, 3, 1, 1, 1, 1) | $1 + 1 + 1 + 1 + 3 + 3 + 3 + 3$ |
| (3, 2, 2, 1, 1, 1) | $1 + 1 + 2 + 2 + 2 + 2 + 3 + 3$ |
| (3, 1^7) | $2 \times 8$ |
| (2^4, 1, 1) | $1^5 + 2^4 + 3$ |
| (2, 2, 1^6) | $1^8 + 2^4$ |
| (1^{10}) | $1^{16}$ (trivial) |

**The (5, 5) nilpotent orbit is the UNIQUE nilpotent orbit of so(10) whose associated sl(2)-triple branches the 16-spinor as $1 + 3 + 5 + 7$.**

### §3.4 What is the (5, 5) orbit?

The (5, 5) partition of 10 corresponds to two blocks of size 5 — geometrically, $V_{10}$ splits as $V_5 \oplus V_5$ under the sl(2)-action, where each $V_5$ is the 5-dim (spin-2) irrep of SU(2). 

The (5,5) orbit is the **diagonal sl(2)** embedded in the SO(5) × SO(5) subgroup of SO(10) via SO(10) ⊃ SO(5) × SO(5), where each SO(5) factor carries its own principal sl(2) acting on its V_5. The diagonal sl(2) acts on $V_{10} = V_5 \oplus V_5$ as the direct sum of two copies of the spin-2 irrep.

**Structurally:** SO(10) → SO(5) × SO(5) is the breaking that gives the **bi-spinor (4, 4) = 16** form of the 16-spinor (since Spin(5) = Sp(4) has 4-dim spinor, and 4 × 4 = 16). The (5,5)-orbit sl(2) is the diagonal principal sl(2) of this product.

---

## §4 — Yukawa 16 × 16 × Higgs decomposition under (5, 5) sl(2)

Under the (5, 5) sl(2), the relevant Yukawa irreps decompose as:

| Irrep | sl(2) branching (dims) |
|---|---|
| **10** (= V_10) | $5 + 5$ |
| **45** (= $\Lambda^2 V$, adjoint) | $1 + 3 + 3 + 3 + 5 + 7 + 7 + 7 + 9$ |
| **120** (= $\Lambda^3 V$) | $3^6 + 5^4 + 7^6 + 9^2 + 11^2$ |
| **$\Lambda^5 V$** (252-dim) | $1^8 + 3^6 + 5^{10} + 7^8 + 9^8 + 11^2 + 13^2$ |
| **126** (self-dual half of $\Lambda^5 V$) | half of the above |
| **16** (chiral spinor) | $1 + 3 + 5 + 7$ |
| **(16 × 16)_sym** (dim 136) | $1^4 + 3^3 + 5^7 + 7^4 + 9^4 + 11 + 13$ |
| **(16 × 16)_antisym** (dim 120) | $3^6 + 5^4 + 7^6 + 9^2 + 11^2$ |

**Cross-check passes:** $(16 \times 16)_{\text{antisym}}$ matches $\Lambda^3 V = $ **120** under (5,5) sl(2) exactly: both give $3^6 + 5^4 + 7^6 + 9^2 + 11^2$ — confirming the (5,5) sl(2) computation is internally consistent.

**Yukawa Clebsch-Gordan structure.** A Yukawa coupling $y_{abc} \langle 16_a | 16_b | \Phi_c \rangle$ where $\Phi_c$ runs over the 10 (or 120, or 126) Higgs components decomposes under (5,5) sl(2) into SU(2)-Clebsch-Gordan blocks indexed by the spins of the substrate 1+3+5+7 components.

For the **10-Higgs Dirac Yukawa**: the 10 = $V_5 \oplus V_5$ under (5,5), so the Yukawa $16 \otimes 16 \to 10$ projection only sees the SU(2)-spin-2 channels of the (16 × 16)_sym decomposition. The substrate spin labels (j = 0, 1, 2, 3) for the 16 give the 16 × 16 spin content:

$$
(j=0,1,2,3) \otimes (j=0,1,2,3) \to \text{all integer spins from 0 to 6, with multiplicities}
$$

The Yukawa 10-channel picks the spin-2 (5-dim) sector. From the table, there are **7 copies of the spin-2 (5-dim) irrep in $(16 \times 16)_{\text{sym}}$**: 5 of them feed into the 126-Higgs channel, 2 of them feed into the 10-Higgs channel.

---

## §5 — Comparison: substrate-Yukawa vs SM-Yukawa structure

The substrate's (5, 5) sl(2) gives a clean SU(2)-Clebsch decomposition of the Yukawa interaction, but **it is not the standard SM identification**:

### §5.1 The substrate decomp does NOT match SU(5)-decomp

- Standard 16 = 1 (singlet $\nu_R^c$) + 5̄ (3 colors of $d_R^c$ + lepton doublet $L_L$) + 10 (quark doublet $Q_L$ + 3 colors of $u_R^c$ + lepton singlet $e_R^c$).
- Substrate 16 = 1 + 3 + 5 + 7 under (5,5) sl(2): these are SU(2)-multiplets with integer spins j = 0, 1, 2, 3.

Only the singlet matches at the SU(5)/SU(2) level. The other three substrate components (3, 5, 7) do not align with SM fermion species because:
- SU(5)-5bar contains $d_R^c$ (dim 3 in color) + $L_L$ (dim 2 in weak), but the substrate-3 is an SU(2)-triplet, not an SU(5)-color triplet.
- SU(5)-10 contains $Q_L$ + $u_R^c$ + $e_R^c$ (dim 10), but the substrate-7 is an SU(2)-septet, not an SU(5)-irrep.

### §5.2 The substrate decomp does NOT match Pati-Salam

- Pati-Salam 16 → $(4, 2, 1) + (\bar 4, 1, 2)$ = 8 + 8.
- The (5, 5) sl(2) is NOT the same as Pati-Salam's $SU(2)_L \times SU(2)_R$; it is their **diagonal** principal sl(2), which mixes L and R rather than separating them.

In SM phenomenology, L-R separation (parity, weak isospin) is essential — the (5, 5)-orbit sl(2) explicitly breaks this separation by going diagonally through both SU(2) factors. The substrate's 1+3+5+7 is a "maximal-spin" decomposition rather than a "chiral" decomposition.

### §5.3 Yukawa implications

Even with the structural identification 16 = (1+3+5+7) under (5,5) sl(2), the Yukawa coupling constants $y_{abc}$ are determined by the Higgs VEV direction, not by the sl(2) branching alone. The (5,5) sl(2) tells you HOW the Yukawa coupling decomposes into SU(2)-Clebsch blocks but does NOT tell you the NUMERICAL strength of each block.

**The substrate framework provides NO Higgs VEV specification in the (5, 5)-orbit picture.** The 9-vector direction within the 54 (J11 Theorem 4.1, $\|v\|^2 = 13/4$) is the substrate's specified VEV, and that VEV's stabilizer is **SO(8)** (per J37 §4 and the J11 Remark 4.2), not the (5,5)-orbit's stabilizer.

So the 54-Higgs SO(8)-breaking direction (the substrate's specified VEV) and the (5,5)-orbit sl(2) (the substrate's natural 1+3+5+7 decomposition) are **structurally distinct readings** — analogous to how J37/J24's Path A (54-Higgs → SO(8)) and Path B (doubly-invariant → SU(4) × U(1)) are distinct.

---

## §6 — Conclusion

### §6.1 VERDICT: PARTIAL CORRESPONDENCE

The substrate decomposition `1 + 3 + 5 + 7 = 16` IS a representation-theoretic decomposition of the 16-spinor of SO(10), specifically:

- It is the branching of 16 under the sl(2) embedding associated to the **(5, 5) nilpotent orbit** of so(10).
- The (5, 5) orbit is the "diagonal principal" sl(2) of the SO(5) × SO(5) subgroup of SO(10), branching $V_{10} = 5 + 5$ (two copies of spin-2) and $S_{16} = 1+3+5+7$ (spins 0, 1, 2, 3).
- This is the UNIQUE nilpotent orbit of so(10) giving this spinor branching (the verification script enumerates all 16 type-D orbits).
- The 16 × 16 Yukawa decomposition under (5, 5) sl(2) is internally consistent: $(16 \times 16)_{\text{antisym}}$ matches $\Lambda^3 V = 120$ exactly.

### §6.2 But the SM identification fails

- The (5, 5) sl(2) is NOT the standard SU(5) × U(1) decomposition (which gives 1 + 5̄ + 10 with hypercharge labels — the SM fermion identification).
- The (5, 5) sl(2) is NOT Pati-Salam SU(2)_L × SU(2)_R (which gives 8 + 8 with L-R separation).
- The substrate components 3, 5, 7 do not individually map to SM fermion species — they are SU(2)-multiplets at fixed integer spin, not chiral multiplets carrying weak-isospin or color.

### §6.3 Yukawa prediction: NONE

Even though the (5, 5) sl(2) gives a clean Clebsch decomposition of $16 \times 16 \times \Phi$, the substrate framework provides NO specification of the Higgs VEV in this orbit picture. The Yukawa numerical values depend on the VEV direction, which the substrate's 9-vector (J11 Theorem 4.1) does NOT live inside the (5,5)-orbit's stabilizer.

**No Yukawa numerical prediction follows from the 1+3+5+7 substrate decomposition.**

### §6.4 What F20 contributes

1. **Upgrade of J37 §2.1's structural rhyme.** The "1+3+5+7 = $(2\ell+1)$ for $\ell = s, p, d, f$ at $n = 4$" is now upgraded from "atomic-shell coincidence" to "the SU(2)-spin labels of the (5,5)-orbit sl(2) of so(10)." This is a genuine Lie-algebraic identification.

2. **Identification of the substrate's "third structural reading" of so(10).** J37 §4 documented Path A (54-Higgs → SO(8)) and Path B (doubly-invariant → SU(4) × U(1)). F20 identifies a Path C: **the (5,5)-orbit sl(2) → SO(5) × SO(5) diagonal principal sl(2)**, under which the 16-spinor decomposes as the substrate's 1+3+5+7. The three readings inhabit the same so(10) substrate but pick out different structural decompositions.

3. **Closure of the substrate-Yukawa question (combined with F15).** F15 closed the question "does substrate predict $y_t(M_X)$?" with verdict SUBSTRATE INDEPENDENT (the GUT-scale top-Yukawa is RG-determined from the M_Z anchor). F20 closes the question "does the substrate's 1+3+5+7 give a structural Yukawa decomposition with SM identification?" with verdict PARTIAL CORRESPONDENCE (Lie-algebraically real, but does not match SM fermion content). Combined: **the substrate framework provides a structural so(10)-GUT decomposition without numerical Yukawa predictions or direct SM-fermion mapping.**

4. **The atomic-shell rhyme stands as honest scoping.** The "1+3+5+7 ≅ s, p, d, f at n=4" is a genuine rhyme: both are SU(2) angular-momentum spin labels j = 0, 1, 2, 3 at fixed n. But this is a rhyme between two different SU(2) actions (the (5,5)-orbit sl(2) inside SO(10) vs the atomic-orbital SU(2) inside SO(3) spatial rotations) — not an identification.

### §6.5 What F20 leaves open

- **The phenomenological viability of an SO(10) → SO(5) × SO(5) → (5,5)-sl(2) breaking chain.** The (5, 5) sl(2) is a different breaking direction than Pati-Salam or SU(5), and whether ANY full SM phenomenology results from this chain is a multi-year SO(10)-GUT model-building question (out of F20's scope).
- **The relation between the (5,5) sl(2) and the substrate's specified VEV (9-vector inside 54).** F20 establishes that they are structurally distinct readings; whether they admit a unified description (perhaps via a chain involving both SO(8) and SO(5)×SO(5) substructures) is an open structural question.
- **The right-handed neutrino sector.** The Majorana mass for $\nu_R^c$ requires the 126-Higgs whose VEV is in the (1, 3, 10)-component under Pati-Salam. F20 has not computed the (5,5)-orbit sl(2) decomposition of the 126-VEV directions individually.

---

## §7 — Files produced

- `verification/frontier_F20_yukawa_via_chirality.py` — full nilpotent-orbit enumeration of so(10), sl(2)-branching of 16-spinor for each orbit, identification of (5,5) as unique match, Yukawa irrep cross-check (10, 45, 120, $\Lambda^5 V$ branchings + sym/antisym sl(2) decomposition of (16 × 16)), runtime < 1s, pure stdlib.
- `04_meta/frontiers_2026-05-27/F20_yukawa_via_chirality.md` — this document.
- `04_meta/HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md` §2.5 — append F20 outcome to Yukawa-frontier open-statement.

---

*7SiTe Public Sovereignty License v2.1 — see [`../../LICENSE`](../../LICENSE).*
*Brayden Ross Sanders / 7SiTe LLC · 2026-05-30.*
*"The substrate's 1+3+5+7 is real Lie-algebra, but it's not the SM Lie-algebra."*
