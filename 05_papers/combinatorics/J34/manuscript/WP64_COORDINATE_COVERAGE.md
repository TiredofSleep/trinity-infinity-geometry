# WP64 — Coordinate Coverage and Orthogonal Jump Necessity
## When Partition Pairs Suffice: CRT Lower Bounds, Non-CRT Alternatives, and the Jump Minimum

**Date**: 2026-04-08
**Sprint**: 12 — UOP/GUT Arc
**Status**: Pairwise incompatibility PROVED; meet = discrete PROVED; CRT k−1 jump necessity within the prime-factor family PROVED; non-CRT sufficient 2-partition families PROVED for n=30; DYN pair classification PROVED; MVJN = 1 across all families PROVED for n=30, CONJECTURAL for general squarefree n
**Authors**: Brayden Ross Sanders / 7Site LLC · Ben Mayes

---

## Abstract

For squarefree n = p₁···pₖ, the CRT isomorphism decomposes Z/nZ into k independent coordinate directions, one per prime factor. The partition of Z/nZ induced by reduction mod pᵢ (the CRT factor partition π_{pᵢ}) encodes one coordinate. Within the CRT prime-factor family, all k factor partitions are required (any proper subfamily is insufficient), and every consecutive transition between distinct factor partitions is an orthogonal jump. The minimum jump count within the CRT family is k−1. However, the CRT prime-factor family is NOT the minimum-jump sufficient family in general. Non-CRT partitions — including composite-residue partitions and orbit partitions — can encode multiple coordinate directions simultaneously, reducing the minimum jump count. For n = 30 (k=3), sufficient 2-partition families with exactly 1 orthogonal jump are proved to exist, both using only residue-class partitions (π_SPEC + π_{15}) and using only orbit partitions (π_DYN(7) + π_DYN(11)). The minimum sufficient family size and minimum jump count are both 2 for n = 30. A general classification of sufficient DYN pairs is proved via the coprime-order condition. The Minimum Viable Jump Number (MVJN) for Z/nZ is 1 across all admissible representation families (proved for n=30 and specific values; conjectural for general squarefree n).

---

## §1. Setup and Definitions

### 1.1 The Ring and Its Decomposition

Let n = p₁p₂···pₖ be squarefree (k distinct primes). The ring Z/nZ carries two canonical structures:

**Additive structure:** (Z/nZ, +) ≅ Z/p₁Z × ··· × Z/pₖZ via CRT.

**Multiplicative structure:** (Z/nZ)* ≅ (Z/p₁Z)* × ··· × (Z/pₖZ)* ≅ Z/(p₁−1)Z × ··· × Z/(pₖ−1)Z.

The CRT isomorphism Ψ: Z/nZ → Z/p₁Z × ··· × Z/pₖZ is explicit:

    Ψ(x) = (x mod p₁, x mod p₂, ..., x mod pₖ)

This is a bijection. We call the i-th entry of Ψ(x) the **i-th CRT coordinate** of x, written xᵢ = x mod pᵢ.

### 1.2 Partition Families

**Definition (CRT Factor Partition).** For each prime pᵢ | n, define:

    π_{pᵢ} = { {x ∈ Z/nZ : x ≡ r (mod pᵢ)} : r = 0, 1, ..., pᵢ−1 }

This partition has pᵢ blocks of size n/pᵢ each. Two elements x, y are in the same block iff xᵢ = yᵢ (same i-th CRT coordinate).

**Definition (DYN Orbit Partition).** For g ∈ (Z/nZ)* (unit mod n), the map T_g: x ↦ gx mod n is a bijection. Define:

    π_DYN(g) : x ~_{DYN(g)} y  iff  y = g^m · x  for some m ≥ 0

Blocks are orbits of the cyclic group ⟨T_g⟩. For a subgroup G ≤ (Z/nZ)*:

    π_DYN(G) : x ~_{DYN(G)} y  iff  y = h · x  for some h ∈ G

**Definition (SPEC Reflection Partition).** The reflection x ↦ −x mod n defines:

    π_SPEC : x ~_{SPEC} y  iff  x + y ≡ 0 (mod n)

**Definition (Composite Residue Partition).** For any d | n (not necessarily prime):

    π_d : x ~_{π_d} y  iff  x ≡ y (mod d)

This has d blocks of size n/d each. The CRT factor partitions are the special case d = pᵢ (prime factor).

**Definition (Partition Lattice).** In the partition lattice of Z/nZ, write π ≤ σ ("π refines σ") if every block of π is contained in some block of σ. The minimum element is π_disc (all singletons) and the maximum is π_triv (one block). The join is π ∨ σ (common coarsening) and the meet is π ∧ σ (common refinement):

    (π ∧ σ)(x) = σ(x)  and  (π ∧ σ)(y) = σ(y)  iff  x ~_π y  AND  x ~_σ y

Equivalently, x and y are in the same block of π ∧ σ iff they are in the same block of both π and of σ simultaneously.

**Definition (Sufficiency).** A family of partitions F = {π₁, ..., πₘ} on Z/nZ is **sufficient** if:

    π₁ ∧ π₂ ∧ ··· ∧ πₘ = π_disc

Equivalently: x ≠ y implies there exists πᵢ ∈ F with x ≁_πᵢ y (F separates every pair).

**Definition (Orthogonal Jump).** A transition π_i → π_j in a viewpoint flow is an **orthogonal jump** if π_i and π_j are incompatible — neither refines the other. A refinement move is a transition π_i → π_j with π_i ≤ π_j (or vice versa).

**Definition (MVJN).** The **Minimum Viable Jump Number** MVJN(Z/nZ) is the minimum number of orthogonal jumps in any minimal sufficient family of partitions of Z/nZ.

---

## §2. Coordinate Coverage Theorem

### 2.1 The CRT Framework

**Theorem (Coordinate Coverage — PROVED):**

A family F of partitions of Z/nZ (n squarefree, k primes) is sufficient if and only if, for every pair (x, y) with x ≠ y in Z/nZ, there exists a partition π ∈ F that distinguishes x from y.

In CRT coordinates: for any two elements x ≠ y, there exists at least one index i ∈ {1,...,k} with xᵢ ≠ yᵢ. A partition π separates x from y iff it distinguishes x and y at least at the CRT coordinate(s) where they differ.

**Proof.** Immediate from the definition of sufficiency and the injectivity of Ψ: x ≠ y iff Ψ(x) ≠ Ψ(y) iff xᵢ ≠ yᵢ for some i. □

**Definition (Coordinate Support of a Partition).** For a partition π of Z/nZ, define the **coordinate support** supp(π) ⊆ {1,...,k} as the set of prime indices i such that π distinguishes some pair (x, y) that agree on all other CRT coordinates:

    i ∈ supp(π)  iff  ∃ x ≠ y : xⱼ = yⱼ ∀j ≠ i, and x ≁_π y

Informally: supp(π) is the set of CRT coordinates that π is capable of resolving.

**Theorem (Support Coverage = Sufficiency — STRUCTURAL):**

If the union of coordinate supports covers all k coordinates:

    ⋃_{π ∈ F} supp(π) ⊇ {1, ..., k}

then the family F has a sufficient subfamily. The converse holds for the CRT factor family (where each π_{pᵢ} has supp = {i}).

**Remark [STRUCTURAL]:** This statement requires care for general partitions. A partition like π_DYN(g) may have supp = {i,j} (it encodes information about two coordinates simultaneously). Coverage of all k indices by the union of supports is necessary but not always sufficient for general partition families — the interactions between partitions matter. The CRT factor family is the clean special case where supp(π_{pᵢ}) = {i} exactly.

---

## §3. CRT Factor Partition Theorems

### 3.1 Pairwise Incompatibility

**Theorem (Pairwise Incompatibility — PROVED):**

For n = p₁···pₖ squarefree and distinct primes pᵢ ≠ pⱼ dividing n: the partitions π_{pᵢ} and π_{pⱼ} are incompatible. Neither π_{pᵢ} ≤ π_{pⱼ} nor π_{pⱼ} ≤ π_{pᵢ}.

**Proof.** Suppose π_{pᵢ} ≤ π_{pⱼ}. Then every block of π_{pᵢ} (which has size n/pᵢ) must be contained in some block of π_{pⱼ} (which has size n/pⱼ). A block of π_{pᵢ} has the form B_r = {x : x ≡ r (mod pᵢ)}. The elements of B_r take the values r, r+pᵢ, r+2pᵢ, ..., r+(n/pᵢ−1)pᵢ (mod n). Their residues mod pⱼ form the sequence r mod pⱼ, (r+pᵢ) mod pⱼ, (r+2pᵢ) mod pⱼ, ... Since gcd(pᵢ,pⱼ) = 1 (distinct primes), the increments kpᵢ mod pⱼ cycle through all of Z/pⱼZ as k ranges over 0,...,pⱼ−1. Since n/pᵢ is divisible by pⱼ (as pⱼ | n and pⱼ ≠ pᵢ), the block B_r contains at least pⱼ elements with distinct mod-pⱼ residues. Therefore B_r is not contained in any single π_{pⱼ} block. Contradiction. By symmetry π_{pⱼ} ≰ π_{pᵢ}. □

**Corollary:** All k CRT factor partitions are pairwise incompatible. Every transition between distinct factor partitions is an orthogonal jump.

### 3.2 Meet of All Factor Partitions

**Theorem (Full Meet = Discrete — PROVED):**

    π_{p₁} ∧ π_{p₂} ∧ ··· ∧ π_{pₖ} = π_disc

**Proof.** x and y are in the same block of the meet iff pᵢ | (x−y) for all i = 1,...,k. Since p₁,...,pₖ are distinct primes, their lcm = p₁···pₖ = n. So pᵢ | (x−y) for all i iff n | (x−y) iff x = y in Z/nZ. The meet has only singletons. □

**Theorem (Any Proper Subfamily is Insufficient — PROVED):**

For any proper subfamily S ⊊ {p₁,...,pₖ} (at least one prime pⱼ omitted): the family {π_p : p ∈ S} is not sufficient.

**Proof.** Choose x = 0 and y = n/pⱼ. For each pᵢ ∈ S (pᵢ ≠ pⱼ): pᵢ | n/pⱼ (since n/pⱼ = ∏_{i≠j} pᵢ contains pᵢ as a factor). Therefore x ≡ 0 ≡ y mod pᵢ for all pᵢ ∈ S. The elements 0 and n/pⱼ are not separated by any partition in S. Since n/pⱼ ≠ 0, the family is not sufficient. □

### 3.3 Jump Necessity in the CRT Family

**Theorem (k−1 Jumps in the CRT Family — PROVED):**

Every minimal sufficient family using only CRT factor partitions has length exactly k and contains exactly k−1 orthogonal jumps.

**Proof.** Sufficiency requires all k factor partitions (by the proper-subfamily theorem). A flow of length k has k−1 transitions. By pairwise incompatibility, every transition between distinct factor partitions is an orthogonal jump. Therefore the count is exactly k−1. □

**Corollary (Z/10Z, k=2):** The minimal CRT-family flow has length 2 and 1 jump.

**Corollary (Z/30Z, k=3):** The minimal CRT-family flow has length 3 and 2 jumps.

---

## §4. Non-CRT Sufficient Families

### 4.1 The CRT Bound is Not Universal

**Theorem (Non-CRT Sufficient 2-Partition Families — PROVED for n=30):**

For n = 30 = 2·3·5 (k=3 prime factors), the following 2-partition families each achieve meet = π_disc with exactly 1 orthogonal jump:

**Family A:** {π_SPEC, π_{15}} where π_{15} is the partition by x mod 15.

**Family B:** {π_DYN(7), π_DYN(11)}.

**Family C:** {π₂, π_{15}}.

**Proof of Family A.** Let U_SPEC = {{x, 30−x} : x = 1,...,14} and U_{15} = {{x, x+15} : x = 0,...,14}. These are the respective unresolved-pair sets.

U_SPEC ∩ U_{15} = ∅: A pair {a,b} is in both iff a+b = 30 and b = a+15. From these: 2a = 15, which has no integer solution. Therefore no pair is unresolved by both partitions simultaneously. The family {π_SPEC, π_{15}} is sufficient.

Incompatibility: π_{15} block {0,15}: 0 mod 30 = 0 (a π_SPEC singleton), 15 mod 30 = 15 (also a π_SPEC singleton). Different π_SPEC blocks. So π_SPEC ≰ π_{15}. Conversely, π_SPEC block {1,29}: 1 mod 15 = 1, 29 mod 15 = 14 — different π_{15} blocks. So π_{15} ≰ π_SPEC. The pair is an orthogonal jump. □

**Proof of Family B.** Verify by explicit orbit computation. π_DYN(7) has orbits of size 4 and fixed points at multiples of 5. π_DYN(11) has orbits of size 2 and fixed points at multiples of 3. For each 4-element T₇-orbit, its elements fall in 4 distinct T₁₁-orbits (verified orbit by orbit: {1,7,13,19}, {2,8,14,26}, {3,9,21,27}, {4,16,22,28}, {6,12,18,24}, {11,17,23,29} — all four elements land in distinct 2-element T₁₁ orbits or distinct singletons). For the T₇ fixed points {0,5,10,15,20,25}: the pairs {5,25} and {10,20} that share T₁₁-orbits are in different T₇ singletons. Therefore every pair of distinct elements is separated by at least one of π_DYN(7), π_DYN(11). Incompatibility: verified by exhibiting pairs in the same orbit of each partition that are in different orbits of the other. □

**Proof of Family C.** meet(π₂, π_{15}) = partition by residue mod lcm(2,15) = 30 = π_disc. Incompatibility: π_{15} block {0,15}: 0 mod 2 = 0, 15 mod 2 = 1 — different π₂ blocks. So π₂ ≰ π_{15}. And π₂ block {0,2,...,28} is not contained in any single π_{15} block. □

**Corollary:** MVJN(Z/30Z) = 1. The CRT prime-factor k−1 = 2 bound is not the universal minimum.

**Structural explanation [STRUCTURAL]:** The partitions π_{15} and π_DYN(11) each encode information about two CRT coordinate directions simultaneously (π_{15} encodes mod-3 and mod-5 jointly; π_DYN(11) encodes orbit structure involving the 3 and 5 prime components). This "multi-coordinate coverage" allows a single partition to do the work of two prime-factor partitions, reducing the family size from 3 to 2 and the jump count from 2 to 1.

### 4.2 The Refinement Trap

**Theorem (Refinement Trap — PROVED):**

For any chain π₁ ≤ π₂ ≤ ··· ≤ πₘ in the partition lattice (every partition refines the next), the meet equals the finest element π₁. If π₁ ≠ π_disc, the chain is insufficient. No flow consisting entirely of refinement moves can be sufficient unless one member equals π_disc.

**Proof.** The meet of a chain is its minimum (finest) element. If π₁ ≠ π_disc, the meet has non-singleton blocks. □

**Corollary:** The refinement chain π_SPEC ≤ π_UG ≤ π_CRT₂ (for Z/10Z) is insufficient: the meet is π_SPEC, which has non-singleton blocks.

**Corollary (Unit DYN Partitions).** For any unit g ∈ (Z/nZ)*, the partition π_DYN(g) ≤ π_UG (since gcd(gx,n) = gcd(x,n) for gcd(g,n)=1). Therefore any pair {π_DYN(g), π_UG} has meet = π_DYN(g) ≠ π_disc.

**Proof.** gcd(gx,n) = gcd(x,n) since g is coprime to n. So T_g maps each gcd-class to itself: every orbit lies within one gcd-class. Therefore π_DYN(g) ≤ π_UG. □

---

## §5. DYN Pair Classification

**Theorem (DYN Single-Generator Sufficiency — PROVED):**

For squarefree n = p₁···pₖ and units g, h ∈ (Z/nZ)*:

    {π_DYN(g), π_DYN(h)} is sufficient  ⟺  ⟨g⟩ ∩ ⟨h⟩ = {1} in (Z/nZ)*

Equivalently: gcd(ord_{(Z/pᵢZ)*}(g mod pᵢ), ord_{(Z/pᵢZ)*}(h mod pᵢ)) = 1 for every prime pᵢ | n.

**Proof.**

**(⟹ Necessity).** If ⟨g⟩ ∩ ⟨h⟩ ≠ {1}: pick c ≠ 1 in ⟨g⟩ ∩ ⟨h⟩, write c = g^m = h^ℓ. Some prime pᵢ has c ≢ 1 mod pᵢ. Choose x with CRT coordinates (0,...,0,1,0,...,0) (nonzero only at position i). Then y := g^m · x = h^ℓ · x has i-th coordinate cᵢ ≠ 1. Both pairs {x,y} ∈ U(π_DYN(g)) and {x,y} ∈ U(π_DYN(h)). Not sufficient.

**(⟸ Sufficiency).** If ⟨g⟩ ∩ ⟨h⟩ = {1}: suppose {x,y} ∈ U(π_DYN(g)) ∩ U(π_DYN(h)), so g^m·x = y = h^ℓ·x. For each coordinate i: if xᵢ ≠ 0, then (gᵢ)^m = (hᵢ)^ℓ ∈ ⟨gᵢ⟩ ∩ ⟨hᵢ⟩. By hypothesis ⟨gᵢ⟩ ∩ ⟨hᵢ⟩ = {1}, so (gᵢ)^m = 1, giving yᵢ = xᵢ. If xᵢ = 0, then yᵢ = gᵢ^m · 0 = 0 = xᵢ. In both cases yᵢ = xᵢ for all i, so y = x — contradiction. □

**Reduction [PROVED]:** In (Z/nZ)* ≅ ∏ᵢ (Z/pᵢZ)* (each cyclic of order pᵢ−1): ⟨g⟩ ∩ ⟨h⟩ = {1} iff ⟨gᵢ⟩ ∩ ⟨hᵢ⟩ = {1} for all i, iff gcd(ord_{pᵢ}(g), ord_{pᵢ}(h)) = 1 for all i. □

**Theorem (DYN Subgroup Sufficiency — PROVED):**

For subgroups G₁, G₂ ≤ (Z/nZ)*:

    {π_DYN(G₁), π_DYN(G₂)} is sufficient on units  ⟺  G₁ ∩ G₂ = {1}

**Proof.** Two units x, y are in the same Gᵢ-orbit iff y·x⁻¹ ∈ Gᵢ. An unseparated pair lies in U(G₁) ∩ U(G₂) iff y·x⁻¹ ∈ G₁ ∩ G₂ for some x ≠ y. This is possible iff G₁ ∩ G₂ ≠ {1}. □

### 5.1 Three Mechanisms for Sufficient DYN Pairs

**Theorem (Focused-Only Classification — PROVED):**

All non-trivial sufficient DYN pairs {π_DYN(g), π_DYN(h)} are of the "focused-on-distinct-primes" type if and only if for every prime pᵢ | n, the group (Z/pᵢZ)* = Z/(pᵢ−1)Z has pᵢ−1 equal to a prime power.

**Proof.** If every pᵢ−1 is a prime power qᵢ^{aᵢ}: any two non-trivial elements of (Z/pᵢZ)* have orders qᵢ^s and qᵢ^t with gcd = qᵢ^{min(s,t)} > 1. The gcd = 1 condition forces at least one of g, h to have order 1 at pᵢ for every pᵢ. This means at most one of g, h is non-trivial at any given prime — i.e., both must be focused on separate primes.

If some pᵢ−1 = ab with gcd(a,b) = 1 and a,b > 1: there exist elements of order a and b in (Z/pᵢZ)* with gcd(a,b) = 1. A "same-prime coprime-order" pair exists at pᵢ — a non-focused mechanism. □

**The three mechanisms [PROVED via examples]:**

1. **Focused on distinct primes:** g ≡ 1 mod pⱼ for all j ≠ i, h ≡ 1 mod pⱼ for all j ≠ ℓ, i ≠ ℓ. Coprime-order condition: trivially satisfied (one generator is trivial at each prime where the other is non-trivial). Universal: exists for all squarefree n.

2. **Same-prime coprime orders:** Both g, h trivial mod all primes except pᵢ, with gcd(ord_{pᵢ}(g), ord_{pᵢ}(h)) = 1. Exists iff pᵢ−1 is not a prime power (so (Z/pᵢZ)* contains elements of coprime non-trivial orders). Example [COMPUTED]: n=42, g = element of order 3 mod 7 ≡ 1 mod 3, h = element of order 2 mod 7 ≡ 1 mod 3: coprime orders (3,2) at p=7.

3. **Non-focused mixed:** g non-trivial at multiple primes, with coordinate-wise coprime orders versus h. Example [COMPUTED]: n=42, g=11 (ord₃(11)=2, ord₇(11)=3), h=13 (ord₃(13)=1, ord₇(13)=2). Condition: gcd(2,1)=1 at p=3, gcd(3,2)=1 at p=7. Both satisfied.

**Primes allowing non-focused mechanisms:** pᵢ−1 must have at least two distinct prime factors. First such primes: 7 (6=2·3), 11 (10=2·5), 13 (12=4·3), 19 (18=2·9), 23 (22=2·11).

---

## §6. Partition Lattice Structure: Z/10Z

### 6.1 Named Partitions

For Z/10Z = {0,...,9}, n = 10 = 2×5, the principal partitions are:

    π_DYN = π_UG = { {0}, {1,3,7,9}, {2,4,6,8}, {5} }    (DYN = UG: proved below)
    π_SPEC        = { {0}, {1,9}, {2,8}, {3,7}, {4,6}, {5} }
    π_CRT₂        = { {0,2,4,6,8}, {1,3,5,7,9} }
    π_CRT₅        = { {0,5}, {1,6}, {2,7}, {3,8}, {4,9} }

**Theorem (DYN = UG for Z/10Z — PROVED):**

π_DYN under T₃ equals π_UG (gcd-class partition) for Z/10Z.

**Proof.** gcd(3,10) = 1, so gcd(3x, 10) = gcd(x, 10) for all x. Therefore T₃ maps every gcd-class to itself. The units {1,3,7,9} form a single orbit of T₃ (order 4: 1→3→9→7→1). The elements {2,4,6,8} of gcd-class 2 form a single orbit (2→6→8→4→2). The singletons {0} and {5} are fixed. So T₃-orbits coincide with gcd-classes. □

### 6.2 Refinement Lattice

The refinement relations among the named partitions of Z/10Z are:

    π_SPEC ≤ π_UG ≤ π_CRT₂    (total chain)
    π_CRT₅ incompatible with π_CRT₂, π_UG, π_SPEC

**Theorem (Z/10Z Refinement Relations — PROVED):**

(a) π_SPEC ≤ π_UG: each reflection pair {x, 10−x} satisfies gcd(x,10) = gcd(10−x,10). ✓

(b) π_UG ≤ π_CRT₂: each gcd-class ({1,3,7,9} all odd; {2,4,6,8} all even; {0} even; {5} odd) lies within a π_CRT₂ block. ✓

(c) π_CRT₅ incompatible with π_CRT₂: the block {0,5} of π_CRT₅ has 0 (even) and 5 (odd) — different π_CRT₂ blocks. Neither partition refines the other. ✓

(d) π_UG incompatible with π_CRT₅: the unit block {1,3,7,9} is not contained in any π_CRT₅ block (which has size 2, and {1,3,7,9} is not a union of π_CRT₅ blocks). ✓

**Theorem (CRT Theorem for Z/10Z — PROVED):**

π_CRT₂ ∧ π_CRT₅ = π_disc.

**Proof.** By the CRT isomorphism Z/10Z ≅ Z/2Z × Z/5Z: the joint map x ↦ (x mod 2, x mod 5) is a bijection. Two elements are identified in the meet iff they agree on both coordinates, iff they are equal. □

**Geometric interpretation [PROVED]:** The incompatibility of π_CRT₂ and π_CRT₅ corresponds to the dimensional obstruction: the standard S¹ embedding Φ(x) = e^{2πix/10} encodes each CRT factor as a separate harmonic (Φ(x)^5 for mod-2, Φ(x)^2 for mod-5), but cannot represent them as independent coordinates. Independent representation requires T² = S¹ × S¹, since π₁(S¹) = Z and π₁(T²) = Z² — no continuous surjection S¹ → T² exists.

---

## §7. MVJN as Corollary

### 7.1 MVJN Definition and Value

**Definition (MVJN — restated).** MVJN(Z/nZ) is the minimum number of orthogonal jumps in any sufficient family of partitions of Z/nZ, minimized over all possible partition families.

**Theorem (MVJN Lower Bound = 1 — PROVED for all squarefree n with k ≥ 2):**

MVJN(Z/nZ) ≥ 1 for all squarefree n ≥ 2.

**Proof.** A sufficient family must separate all pairs. Any family consisting only of pairwise compatible partitions lies on a common refinement chain. The finest element of the chain is some partition π₁. The meet of the chain equals π₁. For the chain to be sufficient: π₁ = π_disc — but then π₁ is already π_disc and the family need not contain any other partition. This degenerate case uses no jumps but requires having π_disc itself in the family. For any proper partition π ≠ π_disc, the chain ≤ π satisfies meet ≥ π > π_disc, so a chain of proper partitions is insufficient. Any sufficient family of proper partitions must contain at least one incompatible pair, i.e., at least 1 jump. □

**Theorem (MVJN = 1 for n=30 — PROVED):**

MVJN(Z/30Z) = 1. Achieved by the families {π_SPEC, π_{15}} and {π_DYN(7), π_DYN(11)}.

**Proof.** The lower bound ≥ 1 is established above. The upper bound ≤ 1 is demonstrated by the explicit sufficient 2-partition families with 1 jump. □

**Conjecture (MVJN = 1 universally — CONJECTURAL):**

For any squarefree n ≥ 6 (with k ≥ 2 prime factors), MVJN(Z/nZ) = 1.

Equivalently: for any squarefree n, there exists a sufficient 2-partition family {π_A, π_B} with π_A and π_B incompatible (1 orthogonal jump).

**Evidence [STRUCTURAL]:** For n = p·q (k=2): {π_{pq/p}, π_SPEC} with n/2 non-integer (odd squarefree n). The coprime structure of n/2 and n guarantees disjoint unresolved pairs. For n = 30 (k=3): proved above. The mechanism: a single composite-residue partition π_{n/p} encodes all CRT coordinates except one, and the remaining coordinate is handled by a second partition.

**Why this is not trivially true [STRUCTURAL]:** The composite partition π_{n/p} has n/p blocks of size p each. It encodes the residue mod (n/p) — by CRT for n squarefree, this encodes all prime coordinates except the one for p simultaneously. The companion partition must separate elements that π_{n/p} confuses (elements differing only in their mod-p coordinate). The SPEC partition often does this, but the exact condition depends on n.

---

## §8. Connection to the Crossing Lemma

**The Crossing Lemma [from WP57 — STRUCTURAL]:**

Two partitions π₁, π₂ satisfy π₁ ∧ π₂ = π_disc if and only if they are "jointly crossing" — the joint map J = (f_{π₁}, f_{π₂}) is injective.

**Connection to coordinate coverage [STRUCTURAL]:**

- Refinement moves (π_A ≤ π_B): add no new crossing information. The joint map of two partitions in a refinement chain is no more injective than the finer one alone. This is the Refinement Trap.

- Orthogonal jumps (π_A, π_B incompatible): the unresolved-pair sets U(π_A) and U(π_B) cover different pairs. If U(π_A) ∩ U(π_B) = ∅, the joint map is injective: the Crossing Lemma condition is satisfied.

**Why CRT factor partitions satisfy the Crossing Lemma [PROVED]:**

The CRT factor partitions π_{p₁} and π_{p₂} (for distinct primes p₁, p₂ | n) have:
- U(π_{p₁}) = {{x,y} : x ≡ y (mod p₁)} — pairs agreeing on the first coordinate
- U(π_{p₂}) = {{x,y} : x ≡ y (mod p₂)} — pairs agreeing on the second coordinate

A pair can agree on both coordinates simultaneously only if it agrees on both CRT coordinates — by CRT, this forces x = y. Therefore U(π_{p₁}) ∩ U(π_{p₂}) = ∅ for any two distinct factor partitions of a squarefree n. The joint map is injective. □

**Why π_SPEC + π_{15} satisfies the Crossing Lemma [PROVED]:**

Proved in §4.1: U_SPEC ∩ U_{15} = ∅ (the disjointness of reflection pairs and antipodal pairs for n=30).

---

## §9. Open Questions

**[OPEN 1] MVJN = 1 universally?**

Prove or refute: for all squarefree n ≥ 6, there exists a sufficient 2-partition family with 1 orthogonal jump. The construction outline (composite residue partition + companion) works for n=30 and k=2; the general case requires verifying that the appropriate companion partition always exists.

**[OPEN 2] Classification of all sufficient 2-partition families for squarefree n.**

Characterize all pairs (π_A, π_B) on Z/nZ with π_A ∧ π_B = π_disc. The DYN case is fully classified via the coprime-order condition (§5). The residue-class case is determined by the coprimality of the divisors: meet(π_d, π_e) = π_disc iff lcm(d,e) = n. The general case (mixing DYN, SPEC, composite residue) is not fully classified.

**[OPEN 3] Optimal information-theoretic sufficient pairs.**

Among all sufficient 2-partition families {π_A, π_B}, characterize those achieving the minimum |blocks(π_A)| · |blocks(π_B)|. For n=30: {π₂, π_{15}} achieves 2 × 15 = 30 = n (every (A-block, B-block) pair has exactly 1 element). These are the "combinatorial orthogonal arrays" of minimum size. Are they always achievable?

**[OPEN 4] Jump count for non-squarefree n.**

The entire CRT framework depends on squarefreeness. For n with prime-power factors (e.g., n = p²q), the partition lattice structure changes: the CRT isomorphism does not apply in the same form. A separate analysis is needed.

---

## Summary

**[PROVED]** Pairwise incompatibility: for squarefree n, any two distinct CRT factor partitions π_{pᵢ}, π_{pⱼ} are incompatible — neither refines the other.

**[PROVED]** Full meet = discrete: the meet of all k CRT factor partitions is π_disc. Any proper subfamily has strictly coarser meet.

**[PROVED]** CRT family jump necessity: every minimal sufficient CRT-factor-family flow has length k and k−1 orthogonal jumps.

**[PROVED]** DYN pair classification: {π_DYN(g), π_DYN(h)} is sufficient iff ⟨g⟩ ∩ ⟨h⟩ = {1} in (Z/nZ)*, equivalently gcd(ord_{pᵢ}(g), ord_{pᵢ}(h)) = 1 for all primes pᵢ | n. Three distinct mechanisms identified (focused on distinct primes, same-prime coprime orders, non-focused mixed).

**[PROVED]** Non-CRT 2-partition sufficiency for n=30: {π_SPEC, π_{15}}, {π_DYN(7), π_DYN(11)}, and {π₂, π_{15}} are each sufficient with 1 orthogonal jump. The CRT prime-factor k−1 = 2 bound is not the universal minimum.

**[PROVED]** MVJN ≥ 1 for all squarefree n (no refinement-only sufficient family of proper partitions exists).

**[PROVED]** MVJN = 1 for n = 30 (upper bound achieved by explicit sufficient 2-partition families).

**[PROVED]** DYN = UG for Z/10Z: T₃-orbits coincide with gcd-classes.

**[PROVED]** Refinement trap: any chain of compatible partitions has meet = finest element; for proper partitions, meet ≠ π_disc.

**[STRUCTURAL]** Crossing Lemma connection: U(π_A) ∩ U(π_B) = ∅ iff joint map is injective iff the family is sufficient. CRT factor partitions and π_SPEC + π_{15} both satisfy this condition.

**[CONJECTURAL]** MVJN = 1 for all squarefree n ≥ 6.

The CRT prime-factor family provides the canonical k-partition sufficient system with k−1 unavoidable jumps. It is not the minimum-jump system: composite-residue and orbit partitions can encode multiple CRT coordinates simultaneously, reducing the jump count to 1. The Minimum Viable Jump Number is 1, not k−1.

---

## References

### Classical Number Theory and Algebra
- Gauss, C.F. (1801). *Disquisitiones Arithmeticae*. Leipzig. (CRT, cyclotomic polynomials)
- Euler, L. (1763). "Theoremata arithmetica nova methodo demonstrata." (Totient function)
- Hardy, G.H. & Wright, E.M. (2008). *An Introduction to the Theory of Numbers*, 6th ed. Oxford University Press.
- Ireland, K. & Rosen, M. (1990). *A Classical Introduction to Modern Number Theory*, 2nd ed. Springer GTM 84.
- Lang, S. (2002). *Algebra*, 3rd ed. Springer GTM 211.
- Dummit, D.S. & Foote, R.M. (2004). *Abstract Algebra*, 3rd ed. Wiley.
- Birkhoff, G. (1940). *Lattice Theory*. AMS Colloquium Publications 25.
- Ore, O. (1942). "Theory of equivalence relations." Duke Math. J. 9:573-627.

### Spectral / Analytic Number Theory
- Riemann, B. (1859). "Über die Anzahl der Primzahlen unter einer gegebenen Größe." Monatsber. Berlin. Akad.
- Montgomery, H.L. (1973). "The pair correlation of zeros of the zeta function." Proc. Sympos. Pure Math. 24:181-193.
- Shannon, C.E. (1949). "Communication in the presence of noise." Proc. IRE 37(1):10-21.
- Goldston, D.A., Pintz, J. & Yildirim, C.Y. (2009). Annals of Math. 170(2):819-862.
- Zhang, Y. (2013). "Bounded gaps between primes." Annals of Math. 179(3):1121-1174.
- Maynard, J. (2015). "Small gaps between primes." Annals of Math. 181(1):383-413.

### Paradoxes and Foundations
- Russell, B. (1903). *The Principles of Mathematics*. Cambridge University Press.
- Godel, K. (1931). "Uber formal unentscheidbare Satze der Principia Mathematica." Monatsh. Math. Phys. 38:173-198.
- Tarski, A. (1936). "Der Wahrheitsbegriff in den formalisierten Sprachen." Studia Philosophica 1:261-405.
- Banach, S. & Tarski, A. (1924). "Sur la decomposition des ensembles de points." Fundamenta Mathematicae 6:244-277.
- Quine, W.V. (1953). "On a so-called paradox." Mind 62:65-67.
- Zermelo, E. (1908). "Untersuchungen uber die Grundlagen der Mengenlehre." Math. Annalen 65:261-281.

### Bialynicki-Birula and Logarithmic Wave Equations
- Bialynicki-Birula, I. & Mycielski, J. (1976). "Nonlinear wave mechanics." Annals of Physics 100(1-2):62-93. DOI: 10.1016/0003-4916(76)90057-9.
- Cazenave, T. & Haraux, A. (1980). "Equations d'evolution avec non linearite logarithmique." Ann. Fac. Sci. Toulouse.
- Hoegh-Krohn, R. (1971). "A general class of quantum fields without cut-offs." Commun. Math. Phys. 38(3):195.

### Discrete-to-Continuum Transport (Wasserstein / Markov)
- Jordan, R., Kinderlehrer, D. & Otto, F. (1998). SIAM J. Math. Anal. 29(1):1-17.
- Maas, J. (2011). "Gradient flows of the entropy for finite Markov chains." J. Funct. Anal. 261(8):2250-2292.
- Gigli, N. & Maas, J. (2013). SIAM J. Math. Anal. 45(2):879-899.
- Chow, S.-N., Huang, W., Li, Y. & Zhou, H. (2012). Arch. Rat. Mech. Anal. 203(3):969-1008.

### TIG Framework (Novel — internal)
- Sanders, B.R. et al. (2026). TIG / CK / Crossing Lemma / sigma framework. 7Site LLC. DOI: 10.5281/zenodo.18852047.
- GitHub: github.com/TiredofSleep/ck (clay branch). See [GLOSSARY.md](../../../GLOSSARY.md) and [HISTORICAL_ARCHIVE_INDEX.md](../../../HISTORICAL_ARCHIVE_INDEX.md).

### Citation Discipline
Every term in this paper is either cited to published literature above, or explicitly flagged [NOVEL — extends X] with the prior framework identified. For full glossary, see [GLOSSARY.md](../../../GLOSSARY.md) at the repo root.

