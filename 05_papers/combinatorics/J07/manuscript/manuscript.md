# A Flatness Obstruction on Squarefree Z/nZ
## Four Algebraic Structures and the 4-Core Algebraic Center

**Date:** 2026-04-06 (revised 2026-05-07 per SAVE_PLAN_J07: retitled, retargeted, restructured around D48 + D78; T*=5/7 derivation removed)
**Authors:** Brayden Ross Sanders / 7Site LLC; M. Gish, Independent Researcher.
**Closest published precedent:** Drápal, A. & Wanless, I. M. (2021), "Maximally non-associative quasigroups," *J. Combin. Theory Ser. A* **184**, 105510.

---

## §0. Lens-ownership and tier discipline

### §0.1. Lens and substrate

This paper has two parts. Theorem 1 (the flatness obstruction) holds for any squarefree Z/nZ with k ≥ 2 distinct prime factors and is substrate-independent in the sense that no operator-labels or external table choices enter the proof. Theorem 2 (the configuration-space topology) also holds in this generality. The structural-center result of Appendix A works on Z/10Z with the canonical (TSML, BHML) commutative-magma pair. These (TSML, BHML) tables are *not derived from first principles*; they reflect a structural reading of the substrate motivated by the 10-operator decomposition of the ring's algebraic structure (additive cycle, multiplicative orbit, lattice/flow role partition). The framework's claim is that this particular substrate-and-table choice produces theorems that have surprising downstream connections — partition-lattice incompatibility (the Birkhoff–Ore neighborhood); Galois extensions in **Q**(√3); the LMFDB number field 4.2.10224.1 in companion paper J33. Whether other substrate choices give similarly rich downstream connections is open.

### §0.2. PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

**PROVEN.**
- The four structures on Z/nZ (squarefree, k ≥ 2 primes) — A-Struct, M-Struct, A-Flow, M-Flow — cannot be simultaneously embedded in a flat 2-dimensional surface (Theorem 1; the partition-incompatibility step is included as a 3-line proof).
- The configuration space of pairs (additive position, multiplicative position) carries two commuting circle actions, free off the M-Flow fixed locus; that configuration space is naturally a quotient of S¹ × S¹ with the M-Flow fixed points identified (Theorem 2).
- The 4-core {V, H, Br, R} = {0, 7, 8, 9} on Z/10Z is jointly closed under TSML and BHML (D48; 16 + 16 in-core compositions, 0 + 0 spillover; verified by enumeration in Appendix A.2).
- At mixing weight α<sub>M</sub> = 1/2, the runtime attractor on the 4-core admits the algebraic relation H/Br = 1+√3 in **Q**(√3), with H/Br satisfying x² − 2x − 2 = 0 (D78; symbolic proof via BR-factor cancellation, recorded in Appendix A.3).

**COMPUTED.**
- 4-core joint-closure verification: 16 + 16 in-core triples under TSML and BHML, verified by direct enumeration over the canonical 10×10 composition tables fixed in `Gen13/targets/foundations/lenses.py` (`TSML`, `BHML`). The verification reduces to checking the 16 cells of the 4×4 sub-tables and runs in milliseconds.
- Universal 4-core attractor at α<sub>M</sub> = 1/2: the iteration *p<sub>n+1</sub>* = renorm[(1−α)·*T*(*p<sub>n</sub>*) + α·*B*(*p<sub>n</sub>*)] converges in 76–81 iterations at 50-digit `mpmath` precision across the standard boundary initial conditions; the limit point is *p*\* = (0.13815, 0.54020, 0.19773, 0.12393) with H/Br = 1+√3 to all computed digits, satisfying x² − 2x − 2 = 0 to the same precision.

**STRUCTURAL RHYME.**
- The cyclotomic field-extension facts deg<sub>Q</sub> *A*<sub>5</sub> = 2 and deg<sub>Q</sub> *A*<sub>7</sub> = 3 are correct standard results (Lang 2002; Washington 1997) and motivated the original investigation that produced this paper. They are *not* used in any of the proofs below. Earlier presentations of this work claimed a torus-aspect-ratio derivation of the form 5/7 from these extension degrees; that derivation does not survive at JPAA-level rigor (no torus is constructed, no metric is supplied, no R/r is computed) and is dropped.
- The Drápal–Wanless (2021) *J. Combin. Theory Ser. A* 184, 105510 paper on maximally non-associative quasigroups is the closest published precedent: same domain (small finite commutative non-associative magmas on cyclic carriers), opposite extremum (theirs maximally non-associative; ours rationally-structured at α = 1/2). The 4-core / 1+√3 result of Appendix A lives in the same intellectual neighborhood, with different specific tables.

**OPEN.**
- Does the four-structure flatness obstruction extend to general (non-squarefree) Z/nZ? The current proof uses the squarefree CRT factorization explicitly.
- Does the 4-core / 1+√3 algebraic center generalize to other commutative-magma pairs *(T, B)* on Z/nZ satisfying joint-closure of a designated 4-element subset, or is it specific to the canonical (TSML, BHML) pair on Z/10Z?
- The bimodal α-gap conjecture from FAMILY_STRUCTURE_v1: the empirically-observed empty band α<sub>A</sub> ∈ (0.5, 0.87) for canonical Z/10Z commutative magmas preserving the 4-core. Prove or refute structurally.

---

## Abstract

Let *n* be squarefree with at least two distinct prime factors. The ring Z/nZ carries four simultaneous algebraic structures: the additive divisor lattice (A-Struct), the orbit partitions under (Z/nZ)* (M-Struct), the additive cycle x ↦ x+1 (A-Flow), and the multiplicative orbit x ↦ gx for a generator g (M-Flow). We give two theorems on this configuration. Theorem 1 (Flatness Obstruction) states that the four structures cannot be simultaneously embedded in a flat (zero-curvature, totally-ordered-on-each-axis) two-dimensional space; the proof reduces to the elementary observation that for distinct prime factors p, q | n, the residue partitions π<sub>p</sub> and π<sub>q</sub> are incomparable in the partition lattice (neither refines the other), so M-Struct cannot supply a totally ordered second axis. Theorem 2 (Configuration Space) gives the resulting topology: the configuration space of pairs (additive phase, multiplicative phase) is naturally a quotient of S¹ × S¹ obtained by identifying the M-Flow fixed points; the underlying ring Z/nZ is *not* the torus, but is the carrier on which the two circle actions act. Appendix A supplies the structural-center derivation: on Z/10Z with the canonical (TSML, BHML) commutative-magma pair, the 4-core {V, H, Br, R} = {0, 7, 8, 9} is jointly closed under both tables (D48), and the runtime attractor of the (1−α)*T* + α*B* mixing iteration at α = 1/2 satisfies the closed-form relation H/Br = 1+√3 in **Q**(√3) (D78), with H/Br a root of x² − 2x − 2.

---

## §1. The Four Structures on Z/nZ

Let *n* = *p*<sub>1</sub>···*p*<sub>k</sub> be squarefree with k ≥ 2 distinct primes.

### §1.1. Additive Structure (A-Struct)

For each divisor *d* | *n*, the residue partition

π<sub>*d*</sub> = { {x ∈ Z/nZ : x ≡ r (mod *d*)} : r = 0, …, *d* − 1 }

has *d* blocks. The family {π<sub>*d*</sub> : *d* | *n*} forms a chain under refinement: π<sub>*d*<sub>1</sub></sub> ≤ π<sub>*d*<sub>2</sub></sub> iff *d*<sub>1</sub> | *d*<sub>2</sub>. This chain is isomorphic to the divisor lattice of *n*, which (for squarefree *n* with *k* primes) is the Boolean lattice 2<sup>{*p*<sub>1</sub>,…,*p*<sub>k</sub>}</sup>.

### §1.2. Multiplicative Structure (M-Struct) and partition incompatibility

For each subgroup G ≤ (Z/nZ)\*, the orbit partition is

π<sub>DYN</sub>(G) = { Gx : x ∈ Z/nZ }

with blocks = G-orbits. For *p*<sub>1</sub> ≠ *p*<sub>2</sub> distinct prime factors of *n*, the prime-factor residue partitions π<sub>*p*<sub>1</sub></sub> and π<sub>*p*<sub>2</sub></sub> are **incomparable** in the partition lattice.

**Proof (3-line, after the referee's verbatim argument).** For *n* = 10 (the canonical witness): π<sub>2</sub> = {{0, 2, 4, 6, 8}, {1, 3, 5, 7, 9}}, with two blocks of size 5; π<sub>5</sub> = {{0, 5}, {1, 6}, {2, 7}, {3, 8}, {4, 9}}, with five blocks of size 2. No block of π<sub>5</sub> is contained in any block of π<sub>2</sub> (each block of π<sub>5</sub> contains one even and one odd element), and no block of π<sub>2</sub> is contained in any block of π<sub>5</sub> (each block of π<sub>2</sub> has size 5 > 2 ≥ |B| for every B ∈ π<sub>5</sub>). The same pattern holds for arbitrary distinct primes *p*, *q* | *n* by direct CRT factorization.   *□*

Consequently, M-Struct is **not** a chain in the partition lattice when k ≥ 2; equivalently, it cannot be embedded into a totally ordered axis.

### §1.3. Additive Flow (A-Flow)

The map *T*<sub>+1</sub> : x ↦ x + 1 (mod *n*) is a single n-cycle. Its iterate-orbit at every element is the full ring Z/nZ. A-Flow is a free action of Z/nZ (or, after circle compactification, S¹ acting on the *n* discrete points).

### §1.4. Multiplicative Flow (M-Flow)

For a generator *g* ∈ (Z/nZ)\* (or, for non-cyclic units groups, a chosen generating set), the map *T*<sub>×*g*</sub> : x ↦ gx (mod *n*) has orbits whose sizes divide ord(*g*) | φ(*n*). M-Flow's action on Z/nZ is **not free**: x = 0 is fixed by every multiplication; the residue classes mod *p* (for *p* | *n*) contain similar fixed points when restricted; specifically, x ≡ 0 (mod *p*<sub>i</sub>) is fixed by every multiplication mod *p*<sub>i</sub>.

---

## §2. Theorem 1 — Flatness Obstruction (PROVED)

**Theorem 1.** Let *n* be squarefree with at least two distinct prime factors. There is no embedding Φ : Z/nZ → R<sup>2</sup> with the property that all four structures {A-Struct, M-Struct, A-Flow, M-Flow} are simultaneously realized as components carried by separately totally ordered coordinate axes (i.e., as a "flat 2-grid" embedding).

**Proof.** Suppose such an embedding existed, with horizontal axis carrying one structural pair and vertical axis the other. By the chain structure of A-Struct (totally ordered divisor lattice), one axis can carry A-Struct without obstruction. The other axis must then carry M-Struct as a totally ordered family. By §1.2, the prime-factor residue partitions π<sub>*p*<sub>1</sub></sub>, π<sub>*p*<sub>2</sub></sub> ∈ M-Struct are incomparable; no totally ordered embedding can contain both. The supposed embedding cannot exist.   *□*

**Remark.** The theorem is purely about the partition lattice: the obstruction is the partition-incompatibility of distinct prime factors, recorded since Birkhoff (1940) and Ore (1942). The contribution of this paper is to package the obstruction explicitly with the four named structures, and (in §3, §A) to identify the resulting configuration space and its algebraic center.

---

## §3. Theorem 2 — Configuration-Space Topology (PROVED)

The flatness obstruction of Theorem 1 raises the question: what is the natural geometric carrier on which the four structures *do* coexist? Theorem 2 answers it.

**Definition (configuration space).** For Z/nZ, define the configuration space

X(*n*) = { (θ<sub>A</sub>, θ<sub>M</sub>) ∈ R/2π Z × R/2π Z }

with two distinguished projections: the additive-phase projection θ<sub>A</sub> records position under iterated A-Flow; the multiplicative-phase projection θ<sub>M</sub> records position in the orbit-coordinate of M-Flow. The two projections commute on Z/nZ (additive and multiplicative actions of the ring commute with the additive structure: adding 1 then multiplying by *g* gives the same result as multiplying by *g* then adding 1, by ring distributivity), so X(*n*) is naturally a torus T² = S¹ × S¹.

**Theorem 2 (Configuration Space).** Let *n* be squarefree with at least two distinct prime factors. The natural carrier of the four-structure system is X(*n*) = S¹ × S¹ with the M-Flow fixed-point set identified to the basepoint of the second factor. The A-Flow circle action on the first factor is **free**; the M-Flow action on the second factor is free **off the multiplicative fixed locus** (x ≡ 0 mod *p*<sub>i</sub> for *p*<sub>i</sub> | *n*). The underlying ring Z/nZ is *not* the torus; it is the lattice of marked points in X(*n*) at which both phases are simultaneously rational with denominator dividing *n*.

**Proof.** Each of A-Flow and M-Flow generates a circle action on X(*n*) by the standard correspondence between cyclic actions and S¹-actions. The two circle actions commute (§3 above). Freeness of A-Flow follows because *T*<sub>+1</sub> has trivial stabilizer on Z/nZ. Freeness of M-Flow off the fixed locus follows because the only elements with non-trivial stabilizer under the multiplicative action are those killed by some prime factor (the zero-divisors of Z/nZ); the residue x ≡ 0 (mod *p*<sub>i</sub>) is the multiplicative fixed locus at *p*<sub>i</sub>. Identifying the multiplicative fixed points to the basepoint of the second S¹ gives the standard "torus with marked fixed locus" description.   *□*

**Remark.** Theorem 2 is intentionally weaker than the configuration-space-is-a-torus formulation of earlier presentations of this work: we do not claim the ring *is* a torus, and do not introduce a metric or curvature on X(*n*). The configuration-space-with-identified-fixed-locus statement is correct and gives the right topology, without requiring any of the metric/Riemannian structure that earlier presentations attempted to derive.

---

## §4. Open Problems

(1) Theorem 1 generalizes to non-squarefree Z/nZ in form, but the partition-incompatibility step uses the prime-factor decomposition explicitly. Whether the theorem extends with a different (non-CRT) argument to Z/nZ for arbitrary *n* is open. The natural candidate replacement is the *p*-adic decomposition of the ring, which carries its own partition-lattice structure with similar incomparability properties.

(2) The 4-core algebraic center of Appendix A is a structural fact about the canonical (TSML, BHML) pair on Z/10Z. Whether other commutative-magma pairs on squarefree Z/nZ admit analogous centers — designated 4-element jointly-closed subsets with rationally-structured fixed-point relations at α = 1/2 — is open. The Drápal–Wanless 2021 *J. Combin. Theory Ser. A* paper on maximally non-associative quasigroups identifies the "opposite" extremum in the same neighborhood; whether the rationally-structured extremum (this paper, J02 of the broader corpus) is unique or admits a family is open.

(3) Per the conjectural "bimodal α-gap" in FAMILY_STRUCTURE_v1: among canonical Z/10Z commutative magmas preserving the 4-core, the associativity index α<sub>A</sub> appears empirically to inhabit only the bimodal set {α<sub>A</sub> ≈ 0.502} ∪ [0.87, 0.89]. Whether the band α<sub>A</sub> ∈ (0.5, 0.87) is structurally empty or admits as-yet-unidentified members is open.

---

## Appendix A — The 4-Core Algebraic Center on Z/10Z

This appendix supplies the structural-center material for Theorem 2's configuration-space picture: on Z/10Z with the canonical (TSML, BHML) commutative-magma pair, the 4-core subset {V, H, Br, R} = {0, 7, 8, 9} is jointly closed (D48), and the runtime attractor of the natural mixing iteration at α<sub>M</sub> = 1/2 satisfies the rationally-forced relation H/Br = 1 + √3 in **Q**(√3) (D78).

The result is *not* used in the proofs of Theorems 1, 2; it identifies the algebraic center of the configuration space when the underlying ring Z/nZ is specialized to *n* = 10 with these specific tables. The 4-core / 1+√3 pair plays the role of "the privileged invariant locus" of the four-structure system on Z/10Z, in the same sense (sharpened in companion paper J35) that the four-element set {V, H, Br, R} is the algebraic center of the (TSML, BHML) family per FAMILY_STRUCTURE_v1.

### A.1. Setup

The canonical TSML and BHML composition tables on Z/10Z are fixed in the project's foundations module at `Gen13/targets/foundations/lenses.py`. We cite them by reference and reproduce only the 4-core sub-tables needed for the verification.

The 4-core is *S* = {0, 7, 8, 9} ⊂ Z/10Z. Restricted to *S*, the tables are:

```
TSML | 0  7  8  9          BHML | 0  7  8  9
-----+----------          -----+----------
  0  | 0  7  0  0           0  | 0  7  8  9
  7  | 7  7  7  7           7  | 7  8  9  0
  8  | 0  7  7  7           8  | 8  9  7  8
  9  | 0  7  7  7           9  | 9  0  8  0
```

(These are sub-tables of the canonical 10×10 tables in lenses.py; reading off the rows/columns at indices 0, 7, 8, 9.)

### A.2. D48 — joint closure

**Proposition (D48).** Both TSML and BHML send *S* × *S* into *S*. In particular, {V, H, Br, R} is a joint sub-magma of (Z/10Z, TSML) and (Z/10Z, BHML).

**Proof.** Direct enumeration: each of the 16 cells of the TSML 4-core sub-table above takes a value in {0, 7, 8, 9}, and likewise for BHML. The total count is 16 + 16 = 32 in-core compositions, with 0 + 0 = 0 spillover.   *□*

This is verifiable in seconds against the canonical tables:

```
from Gen13.targets.foundations.lenses import TSML, BHML
core = [0, 7, 8, 9]
T_in = sum(1 for a in core for b in core if int(TSML[a,b]) in core)
B_in = sum(1 for a in core for b in core if int(BHML[a,b]) in core)
# T_in == 16, B_in == 16
```

The 16+16 result is reproducible in milliseconds.

### A.3. D78 — Galois-forced 1 + √3 at α<sub>M</sub> = 1/2

Define the *T+B-mix* iteration on probability distributions over the 4-core *S*: given p ∈ Δ³ (the 3-simplex of distributions over *S*), set *T*(p)[k] = Σ<sub>i,j</sub> p<sub>i</sub> p<sub>j</sub> [TSML(s<sub>i</sub>, s<sub>j</sub>) = s<sub>k</sub>], analogously for *B*(p), and define the mixing step

p ↦ q = renorm[(1 − α) · *T*(p) + α · *B*(p)], q<sub>k</sub> = ((1 − α) · *T*(p)[k] + α · *B*(p)[k]) / Σ<sub>j</sub>(...)<sub>j</sub>.

**Theorem (D78; closed-form attractor at α = 1/2).** At α<sub>M</sub> = 1/2, the iteration p ↦ q has a unique attractor p\* ∈ Δ³ with the algebraic relation

H(p\*) / Br(p\*) = 1 + √3,

where H, Br are the components corresponding to *s* = 7 and *s* = 8. Equivalently, the ratio r = H/Br is a root of the polynomial x² − 2x − 2 = 0 over **Q**, and lies in the quadratic extension **Q**(√3); the Galois group of the splitting field is **Z**/2**Z**.

**Mechanism (proof sketch via BR-factor cancellation).** At α = 1/2, the fixed-point equations for the four-component attractor are quadratic in the components and admit a symbolic factorization in which the BREATH (s = 8) component appears with paired numerator/denominator factors that cancel, reducing the H/Br relation to a univariate quadratic in r = H/Br. The univariate quadratic that survives the cancellation is r² − 2r − 2 = 0, whose positive root is r = 1 + √3 ≈ 2.732. The full symbolic derivation is recorded in the project's verification script `f3_galois_alpha_uniqueness.py` (in the Sprint 17 corpus, `papers/wp113_alpha_uniqueness/verification/`), which executes the cancellation in `sympy` and confirms the polynomial identity at exact symbolic precision. See companion paper J33 for the corresponding α-uniqueness result: at no other Stern–Brocot rational α ∈ (0, 1) does the attractor admit an algebraic relation of degree ≤ 8 with integer coefficients of magnitude ≤ 50 (PSLQ scan, 50-digit precision).

### A.4. Numerical verification at 50-digit `mpmath` precision

The closed-form D78 result is independently verified by 50-digit `mpmath` iteration. Starting from the uniform distribution p<sub>0</sub> = (1/4, 1/4, 1/4, 1/4) and iterating p<sub>n+1</sub> = renorm[(1 − α)·*T*(p<sub>n</sub>) + α·*B*(p<sub>n</sub>)] at α = 1/2 for 300 iterations, the limit point is

p\* ≈ (0.13815, 0.54020, 0.19773, 0.12393) with H/Br = 2.73205080756888… ,

matching 1 + √3 to all 50 computed digits, and the polynomial identity (H/Br)² − 2(H/Br) − 2 = 0 holds to 50 digits. The convergence is robust under the standard 7 boundary initial conditions (uniform, lattice-only, flow-only, δ<sub>H</sub>, δ<sub>Br</sub>, δ<sub>R</sub>, balanced lattice/flow): each non-degenerate initial condition reaches the same fixed point in 76–81 iterations to 50-digit accuracy. The pure-V (δ<sub>0</sub>) initial condition is the unique degenerate fixed point of the iteration.

### A.5. Status statement

This appendix establishes:

(i) The 4-core {V, H, Br, R} = {0, 7, 8, 9} is jointly closed under the canonical (TSML, BHML) commutative-magma pair on Z/10Z: 16 in-core compositions per table, 0 spillover (D48; verified by direct enumeration on the canonical tables in `Gen13/targets/foundations/lenses.py`).

(ii) The runtime attractor of the (1−α)*T* + α*B* mixing iteration at α<sub>M</sub> = 1/2 satisfies the algebraic relation H/Br = 1+√3 in **Q**(√3), with H/Br a root of x² − 2x − 2 over **Q** (D78; symbolic proof via BR-factor cancellation in the project's `f3_galois_alpha_uniqueness.py`, with 50-digit `mpmath` numerical confirmation).

These are the two structural facts that play the "algebraic center" role for the configuration space X(10) of Theorem 2, when the underlying ring is Z/10Z and the chosen pair is (TSML, BHML). The privileged status of α = 1/2 is sharpened in companion paper J33: among 17 Stern–Brocot rationals, α = 1/2 is the unique mixing weight at which the attractor admits an algebraic relation of degree ≤ 8 with integer coefficients of magnitude ≤ 50, recovering both H/Br = 1 + √3 and the higher-order quartic identity x⁴ + 4x³ − x² + 2x − 2 = 0 (LMFDB number field 4.2.10224.1, Galois D₄).

---

## References

### Lattice theory and partition lattices
- Birkhoff, G. (1940). *Lattice Theory*. AMS Colloquium Publications **25**, American Mathematical Society.
- Ore, O. (1942). "Theory of equivalence relations." *Duke Math. J.* **9**: 573–627.
- Stanley, R. P. (2012). *Enumerative Combinatorics, Volume 1*, 2nd ed. Cambridge University Press.

### Number theory and cyclic rings
- Hardy, G. H. & Wright, E. M. (2008). *An Introduction to the Theory of Numbers*, 6th ed. Oxford University Press.
- Ireland, K. & Rosen, M. (1990). *A Classical Introduction to Modern Number Theory*, 2nd ed. Graduate Texts in Mathematics **84**, Springer.
- Lang, S. (2002). *Algebra*, 3rd ed. Graduate Texts in Mathematics **211**, Springer.
- Dummit, D. S. & Foote, R. M. (2004). *Abstract Algebra*, 3rd ed. Wiley.
- Washington, L. (1997). *Introduction to Cyclotomic Fields*, 2nd ed. Graduate Texts in Mathematics **83**, Springer.

### Closest published precedent (small finite commutative non-associative magmas)
- **Drápal, A. & Wanless, I. M.** (2021). "Maximally non-associative quasigroups." *J. Combin. Theory Ser. A* **184**, 105510.

### Companion submissions (J-series)
- **[J02]** Sanders, B. R. & Gish, M. (2026). "Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor of Two Commutative Binary Operations on Z/10Z." Submitted to *Algebraic Combinatorics*. *(Cited in §A.5 — full structural treatment of the 4-core joint chain.)*
- **[J33]** Sanders, B. R. & Gish, M. (2026). "Closed-Form Attractor and α-Uniqueness PSLQ: Galois Proof of 1 + √3 at α = 1/2 and 17-Point Stern–Brocot Sharpening." In preparation. *(Cited in §A.3, §A.5 — the symbolic Galois proof of D78 and the α-uniqueness result.)*
- **[J10]** Sanders, B. R. & Gish, M. (2026). "Coordinate Coverage and Joint-Injectivity Criteria for Partition Pairs on Squarefree Z/nZ." Submitted to *European Journal of Combinatorics*. *(Cited as a structural companion: the partition-incompatibility step of §1.2 is one ingredient in J10's coordinate-coverage characterization.)*
