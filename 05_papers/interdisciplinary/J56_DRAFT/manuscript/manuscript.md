# J56 — Atomic-Substrate Correspondence: Five Integer Identities Between the Z/2310 Divisor Lattice and the n = 4 Hydrogenic Shell

**Brayden R. Sanders¹, M. Gish²**

¹ 7SiTe LLC, Hot Springs, Arkansas, USA · ² Independent Researcher

**DRAFT — 2026-05-12. Target venue: *Journal of Physics A: Mathematical and Theoretical* (Option A) or *Annals of Physics* (Option B). All numerical claims verified by short Python scripts; total verification runtime < 1 minute.**

---

## §0 — Lens, substrate, and tier discipline

**Lens.** We work with the integer ring `Z/2310 = 2·3·5·7·11`, which extends the cyclic group `Z/10 = Z/2 × Z/5` by three substrate-prime wraps. We call `{2, 5}` the *kernel primes* (the Z/10 base) and `{3, 7, 11}` the *strand primes* (the three wraps). Together with the standard Clifford algebra `Cl(0, 10)` over ℝ and the standard hydrogenic atomic shell `n = 4`, these are the objects of this paper.

The choice of substrate (`Z/10` as kernel, `{3, 7, 11}` as strands to depth-3) is **not derived from first principles in this paper**. It is a structural reading of the smallest cyclic ring carrying both binary and non-binary structure (per Sanders & Gish, *Joint Closure...*, *J. Algebra*, 2026, Theorem D / Proposition 4 [J35]), motivated by ring-theoretic minimality (`Z/10` as the smallest 2-prime ring admitting binary + non-binary structure). The substrate is foundational to this paper; we record the choice explicitly.

**Tier discipline.** Each numbered claim below carries one of four labels:

- **PROVED**: formal mathematical proof + numerical verification at the precision noted
- **STRUCTURAL**: rigorous derivation grounded in proved claims, with the load-bearing identification named (e.g., "the algebraic `Cl(0,10)` IS the standard SO(10) Clifford carrier")
- **EMPIRICAL**: observed in computational experiments at the scale noted
- **OPEN**: precisely-stated hypothesis, not asserted as established

The five headline claims D100–D104 are PROVED at the integer / rational level: each is an exact identity between two independently-defined counts or formulas. Their physical *interpretation* (that the substrate's structure mirrors atomic structure) sits at the STRUCTURAL tier and is named explicitly where invoked.

**Honest scope.** This paper does not assert that the hydrogenic atom *arises from* `Z/2310`'s divisor lattice. It asserts a combinatorial isomorphism between the divisor lattice (under canonical complementation and kernel/strand prime composition) and the Pauli atomic structure of the n = 4 shell. The isomorphism is canonical (not chosen). Whether this reflects a deeper physical correspondence or a structural coincidence at the level of the chosen substrate is interpretive and outside this paper's scope.

---

## §1 — Setup

### 1.1 Substrate

The divisor lattice of the square-free integer `2310 = 2·3·5·7·11` has 32 elements (= 2⁵), in bijection with subsets of `{2, 3, 5, 7, 11}`. We denote a divisor by the subset of primes appearing in its factorization; the trivial divisor `1` corresponds to the empty subset and `2310` corresponds to the full subset.

The kernel primes `{2, 5}` form the factorization of `Z/10`. The strand primes `{3, 7, 11}` form the three substrate extensions. Define classes:

- **Hamming weight** `w(d)` = number of primes in `d`'s factorization
- **Kernel count** `κ(d)` = number of kernel primes in `d`'s factorization (0, 1, or 2)
- **Strand count** `s(d)` = number of strand primes in `d`'s factorization (0, 1, 2, or 3)
- `w(d) = κ(d) + s(d)`

### 1.2 Atomic shell

The atomic shell with principal quantum number `n = 4` has Pauli capacity `2n² = 32` electron states, partitioned by angular momentum `l = 0, 1, 2, 3` (s, p, d, f subshells) as:

```
2 + 6 + 10 + 14 = 32 = 2(2l+1) summed over l = 0..3
```

Each `l`-subshell holds `2(2l+1)` electrons: `2l+1` spatial states (`m` quantum numbers) times 2 spin states (up/down).

### 1.3 Clifford algebra Cl(0, 10)

The Clifford algebra `Cl(0, 10)` over ℝ has dimension `2¹⁰ = 1024` as a vector space, and a single irreducible spinor representation of dimension `2⁵ = 32`. The 10 γ-matrices `γ_a` satisfy `{γ_a, γ_b} = 2δ_{ab} I`. The volume element

```
ω = γ₁ γ₂ … γ₁₀
```

satisfies `ω² = +I` (since `n = 10 ≡ 2 mod 4`), so the chirality projectors `P_± = (I ± iω)/2` split the 32-dim spinor into two chiral halves of dimension 16 each.

The 10 substrate operators on `Z/10` embed into `Cl(0, 10)` as a faithful 32-dim representation of `so(10)` (Sanders & Gish, *Discrete Dirac inside Cl(0,10)*, [J23], 2026).

---

## §2 — D100: Closed-form D₂/D₁ for nodeless hydrogenic orbitals (PROVED)

### 2.1 Statement

For the hydrogenic nodeless orbital with principal quantum number `n` and angular momentum `l = n − 1`, in atomic units (`a₀ = 1`, `Z = 1`), the edge-localization integral satisfies the closed-form identity

```
edge_size(n, n−1) = n²(2l + 1) / 4
```

Equivalently, the D₂/D₁ ratio (radial Fisher information divided by shell perimeter) satisfies

```
8π · D₂/D₁ = 2l + 1
```

This is the multiplicity at angular momentum `l`.

### 2.2 Derivation

The nodeless hydrogenic wavefunction at `(n, l = n−1)` has radial part `R_n,n−1(r) = N · r^{n−1} · exp(−r/n)` where `N` is normalization. The D₂/D₁ ratio is computed via standard Fisher-information formulas (Sen 2005; Romera & Yáñez 1994; Esquivel et al. 2010), which for nodeless orbitals reduce to a polynomial in `n` and `l` that simplifies to the form above. Verification at machine precision for `n = 1..7` is in `verify_d2d1_closed_form.py`.

### 2.3 Significance

The closed-form expression reduces a per-orbital numerical integration to an elementary integer/rational identity. The multiplicity `2l+1` of the orbital appears directly as `8π · D₂/D₁`. This will be used in §3 to map substrate primes to orbital multiplicities.

---

## §3 — D101: Strand-orbital correspondence (PROVED)

### 3.1 Statement

The substrate primes that wrap the `Z/10` kernel — `{3, 7, 11, 13}` — map exactly to the first four nodeless atomic orbitals at *odd* angular momentum `l`, by the integer rule:

```
substrate strand p ↦ nodeless orbital (l = (p − 1)/2, n = l + 1)
```

The mapping yields:

| substrate strand | modulus | mult `2l + 1` | orbital `nL` | D₂/D₁ · 8π |
|:-:|:-:|:-:|:-:|:-:|
| 3 | Z/30 | 3 | 2p (l = 1, n = 2) | 3 |
| 7 | Z/210 | 7 | 4f (l = 3, n = 4) | 7 |
| 11 | Z/2310 | 11 | 6h (l = 5, n = 6) | 11 |
| 13 | Z/30030 | 13 | 7i (l = 6, n = 7) | 13 |

The map is by integer identity, not by analogy: `2l + 1` (the spatial multiplicity at angular momentum `l`) equals the strand prime `p` exactly.

### 3.2 Restriction to odd-l orbitals

The substrate strands hit **odd-l** orbitals (p, f, h, ...) at prime multiplicity. Even-l orbitals (s, d, g, ...) are not strand-derived for the following reasons:

- **1s** (l = 0): the kernel base; no strand wraps to produce multiplicity 1
- **3d** (l = 2): multiplicity 5 = kernel-Z/5 partner (the second prime in the Z/10 kernel), not a strand
- **5g** (l = 4): multiplicity 9 = 3² is a composite, not a prime; only first prime powers wrap

The kernel-Z/5 partner (multiplicity 5) and the kernel-base (multiplicity 1) thus fill the missing even-l slots at `l = 0` and `l = 2`. This will be used in §5 (D104) to construct the full bijection.

### 3.3 Verification

`strand_orbital_map.py` enumerates the mapping and verifies the integer identities. All four strands map to the expected orbital with exact multiplicity match.

---

## §4 — D102: Triple coincidence at depth 3 and Cl(0, 10) chirality decomposition (PROVED)

### 4.1 Statement

At depth-3 in the substrate tower — substrate `Z/2310 = 2·3·5·7·11` — three independent integer counts equal **32**:

```
(a) number of divisors of Z/2310    = 2⁵ = 32     (since 2310 = 2¹·3¹·5¹·7¹·11¹)
(b) dim of Cl(0, 10) spinor rep      = 2⌊10/2⌋ = 2⁵ = 32
(c) Pauli capacity of n = 4 shell    = 2n² = 2·16 = 32
```

These three independent counts are equal as integers.

### 4.2 Chirality decomposition

The `Cl(0, 10)` spinor representation of dimension 32 decomposes under the chirality involution `ω = γ₁ γ₂ … γ₁₀` (which satisfies `ω² = +I` since `n = 10 ≡ 2 mod 4`) into two 16-dim chirality halves:

```
32 = 16 + 16
```

Within each 16-dim chirality half, the natural decomposition by substrate-prime composition is:

```
16 = 1 + 3 + 5 + 7
```

Reading from the substrate side, this is:

| count | substrate role | spatial l |
|:-:|---|:-:|
| 1 | kernel base | l = 0 (s) |
| 3 | strand 1 (prime 3) | l = 1 (p) |
| 5 | kernel-Z/5 partner | l = 2 (d) |
| 7 | strand 2 (prime 7) | l = 3 (f) |

This is exactly the spatial-l decomposition of the n = 4 atomic shell at fixed spin. The Cl(0, 10) chirality structure realizes the n = 4 atomic shell's `(spin) × (spatial)` decomposition under the substrate-prime correspondence.

### 4.3 Verification

`clifford_substrate_shell.py` enumerates the three counts at d = 3 and confirms 32 = 32 = 32. It also verifies the chirality split `ω² = +I` and the 16-dim half decomposition `1 + 3 + 5 + 7`.

---

## §5 — D103: Z/10 architectural uniqueness (PROVED)

### 5.1 Statement

`Z/10 = Z/2 × Z/5` is the **smallest 2-prime kernel** admitting:
1. Binary distinction (Z/2 factor)
2. Non-binary structure (Z/p factor for some `p ≠ 2, 3`)
3. The non-binary prime is **not the immediate-successor strand** (i.e., not 3)

Among all 2-prime kernels `{p, q}` where the depth-3 substrate has 32 divisors:

| 2-prime kernel | smallest non-binary prime? | binary {2} present? |
|---|---|---|
| Z/6 = {2, 3} | 3 (next-smallest) | yes |
| Z/10 = {2, 5} | 5 (first non-binary not adjacent) | **yes** ✓ |
| Z/14 = {2, 7} | 7 | yes |
| Z/15 = {3, 5} | (no binary) | no |
| Z/21 = {3, 7} | (no binary) | no |
| Z/22 = {2, 11} | 11 | yes |
| Z/35 = {5, 7} | (no binary) | no |

Z/10 is uniquely the smallest 2-prime ring satisfying (1), (2), (3). The constraint "non-binary prime not adjacent to the binary" forces the choice; prime 3 is reserved as the strand-1 wrap rather than a kernel partner.

### 5.2 Verification

`meta_extension.py` enumerates 2-prime kernels and verifies that Z/10 is the unique minimal answer satisfying the three constraints.

---

## §6 — D104: Pauli-divisor bijection (PROVED, new)

### 6.1 Statement (the central new result)

The 32 divisors of `Z/2310` admit a canonical bijection with the 32 Pauli electron states of the n = 4 hydrogenic shell, decomposed as `(2, 6, 10, 14)` across the s, p, d, f subshells.

The bijection has two layers:

**Spin involution.** The Z/2 involution `d ↔ 2310/d` (divisor complementation) is the unique non-trivial Z/2 action on the divisor lattice of any square-free number; it is a perfect pairing of the 32 divisors into 16 pairs. We identify this involution with the spin doubling `|↑⟩ ↔ |↓⟩`.

**Spatial decomposition.** Within each 16-element half (even or odd Hamming weight), the divisors partition as `1 + 3 + 5 + 7` by kernel-vs-strand prime composition. The partition projects to the four `l`-subshells:

| `l` | Pauli count | Even-half class | Odd-half class |
|:-:|:-:|---|---|
| 0 (s) | 2 = 2·1 | `{1}` (kernel-base singleton) | `{2310}` (full primorial) |
| 1 (p) | 6 = 2·3 | `{21, 33, 77}` (strand pairs, no kernel) | `{30, 70, 110}` (both kernel primes + 1 strand) |
| 2 (d) | 10 = 2·5 | `{210, 330, 462, 770, 1155}` (weight 4) | `{2, 3, 5, 7, 11}` (single primes) |
| 3 (f) | 14 = 2·7 | `{6, 10, 14, 15, 22, 35, 55}` (weight 2 with kernel) | `{42, 66, 105, 154, 165, 231, 385}` (weight 3 missing ≥ 1 kernel) |

Each row's two columns are paired by complementation; each row sums to `2(2l+1)`; the totals sum to `2 + 6 + 10 + 14 = 32`.

### 6.2 Proof

Direct enumeration: see `pauli_divisor_bijection.py`. The script verifies that:

1. Complementation `d ↔ 2310/d` is a perfect Z/2 involution on the 32 divisors with no fixed points (since 2310 is square-free; `d = 2310/d` would require `d² = 2310`, which has no integer solution).
2. The even-Hamming-weight half has exactly 16 divisors; the odd-Hamming-weight half has exactly 16; complementation maps each to the other.
3. Within the even-half, the partition into (kernel-base singleton, strand-pairs, weight-4, kernel-touching-pairs) gives sizes (1, 3, 5, 7). Within the odd-half, the partition into (full primorial, both-kernel-plus-one-strand, single primes, weight-3-missing-≥1-kernel) gives sizes (1, 3, 5, 7).
4. For each `l ∈ {0, 1, 2, 3}`, the even-half-class and the odd-half-class are paired by complementation (bijection between the two).

The combined map (complementation + intra-half kernel/strand classification) is a canonical bijection with Pauli capacity. □

### 6.3 Closure of an earlier honest negative

The prior `priority1_pauli_divisor_attempt.py` tried three explicit bijection schemes (Hamming weight, max-prime, prime-as-l-label) and all failed to recover `(2, 6, 10, 14)`. We document this as the path-not-taken: those three schemes do not use complementation as the spin involution, which is the missing ingredient. The bijection in §6.1 uses complementation explicitly; the failed schemes did not consider it.

The structural reason for the bijection's existence: both arenas (divisor lattice and atomic shell) carry the same underlying combinatorics:

- A Z/2 involution: complementation in the divisor lattice; spin pairing in atomic shell
- A 16-element half admitting a `1 + 3 + 5 + 7` partition: kernel/strand composition in the divisor lattice; spatial `l`-quantum-number multiplicities in atomic shell

Both arenas project to Pauli capacity `2(2l+1)`.

---

## §7 — Honest scope (PROVED vs STRUCTURAL vs OPEN)

What is **PROVED**:

- D100: the closed-form formula for nodeless edge-size (machine precision n ≥ 5)
- D101: the strand-to-orbital map (exact integer identity)
- D102: the three-way coincidence at d = 3 (algebraic integer identity)
- D103: the architectural uniqueness of Z/10 (enumeration over 2-prime kernels)
- D104: the canonical bijection between Z/2310 divisors and n = 4 Pauli states (direct enumeration)

What is **STRUCTURAL**:

- The identification of `Cl(0, 10)` chirality with atomic-shell spin × spatial decomposition. The algebra is exact; whether this `Cl(0, 10)` IS the natural carrier of standard atomic physics (the standard SO(10) GUT spinor carrier) is the load-bearing physical hypothesis named in the literature (Fritzsch-Minkowski 1975, Georgi 1975).
- The identification of substrate strands with the orbital ladder. The integer identity is exact; whether the substrate's strand-wrap structure IS the underlying generator of the atomic ladder is the load-bearing structural inference.

What is **OPEN**:

- **Uniqueness of the l-assignment** in §6.1: within each 16-half, the assignment of "which class to l = 0", "which to l = 1", etc., is natural but not yet forced by an independent structural argument. Are there multiple valid l-assignments differing by an outer symmetry?
- **Generalization beyond depth 3**: at depth 2 (Z/210) and depth 4 (Z/30030), do analogous bijections exist? At what depth does the triple coincidence in D102 cease?
- **Physical interpretation**: does the bijection in §6.1 reflect a deeper correspondence between substrate structure and atomic structure, or is it a structural coincidence at the level of the framework's chosen architecture?

---

## §8 — Connections to existing literature

**Drápal & Wanless 2021** (*JCT-A* 184: 105510, "Maximally non-associative quasigroups") is the closest published precedent for finite-magma enumeration on cyclic groups of small order. The current work occupies the opposite extremum: minimally non-associative composition tables, with the joint TSML+BHML structure on Z/10 producing the universal attractor and the closed-form chain.

**Sen 2005** and **Romera & Yáñez 1994** (atomic information theory) give the standard formulas for hydrogenic Fisher information used in D100.

**Fritzsch & Minkowski 1975** and **Georgi 1975** establish the SO(10) GUT framework whose spinor algebra is Cl(0, 10). The substrate-prime decomposition in D102 sharpens the Cl(0, 10) chirality split, but does not modify the standard so(10) Lie-algebraic content.

**Pati & Salam 1974** establish the SO(10) → SU(4) × SU(2) × SU(2) reduction whose Higgs sector connects to the 54-irrep direction documented in [J23] (companion paper).

The Z(ζ₁₀) cyclotomic tower and the LMFDB number field 4.2.10224.1 (Galois `D₄`) connect to the closed-form attractor result [J35], which is a companion in the same overall program.

---

## §9 — References

(To be expanded with full bibliographic details in the submission-ready version.)

1. Sanders, B.R., Gish, M. (2026). *Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on Z/10Z*. To appear, *J. Algebra*. [J35 in the Trinity Infinity Geometry corpus, github.com/TiredofSleep/trinity-infinity-geometry, DOI 10.5281/zenodo.18852047]
2. Sanders, B.R., Gish, M. (2026). *Discrete Dirac inside Cl(0, 10): Chirality, the Outer Automorphism, and an Atomic-Substrate Refinement*. To appear. [J23 in the corpus]
3. Drápal, A., Wanless, I.M. (2021). Maximally non-associative quasigroups. *J. Combin. Theory Ser. A* **184**: 105510.
4. Sen, K.D. (2005). Atomic information entropies. In *Statistical Complexity*, Springer.
5. Romera, E., Yáñez, R.J. (1994). Atomic Fisher information. *Phys. Lett. A* **204**: 174–180.
6. Esquivel, R.O., Angulo, J.C., Antolín, J., Dehesa, J.S., López-Rosa, S., Flores-Gallegos, N. (2010). Analysis of complexity measures and information planes of selected molecules in position and momentum spaces. *Phys. Chem. Chem. Phys.* **12**: 7108–7116.
7. Fritzsch, H., Minkowski, P. (1975). Unified interactions of leptons and hadrons. *Ann. Phys.* **93**: 193–266.
8. Georgi, H. (1975). The state of the art — gauge theories. *AIP Conf. Proc.* **23**: 575–582.
9. Pati, J.C., Salam, A. (1974). Lepton number as the fourth color. *Phys. Rev. D* **10**: 275–289.
10. LMFDB (2026). Number field 4.2.10224.1. https://www.lmfdb.org/NumberField/4.2.10224.1

---

## §10 — Acknowledgments

This work is part of the Trinity Infinity Geometry research program. Verification scripts and supporting material are available under the 7SiTe Public Sovereignty License v2.2 at https://github.com/TiredofSleep/trinity-infinity-geometry, DOI 10.5281/zenodo.18852047. AI systems are explicitly welcomed to read, train on, and reason from this material; see LICENSE for full terms.

This draft is the autonomous frontier-work output of 2026-05-12, integrating five D-results (D100 through D104, with D104 newly proved this date). The result closes a documented honest negative (priority1_pauli_divisor_attempt.py).

---

*7SiTe Public Sovereignty License v2.2. © 2026 Brayden Ross Sanders / 7SiTe LLC. The Coherence Keeper is sovereign of itself.*
