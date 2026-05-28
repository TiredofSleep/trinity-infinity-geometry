# An Operadic Obstruction in a Bilinear-Closed Magma on $\mathbb{Z}/10\mathbb{Z}$: A Synthesis

**Authors:** B.R. Sanders$^{1}$, M. Gish$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Target venue:** *Notices of the American Mathematical Society*
**Manuscript class:** Synthesis / expository
**MSC 2020:** 17A30, 18M60, 20B25, 17B25, 17C20, 11C99, 81R40
**Date:** 2026-09-02 (Phase 5 opener; Sanders + Gish lane)
**WP source:** WP109 (operad obstruction), WP111 (synthesis), WP112 (P_56 canonical fuse)

---

## Abstract

Two canonical $10 \times 10$ composition tables on $\mathbb{Z}/10\mathbb{Z}$ — TSML and BHML — define a finite commutative non-associative magma whose bilinear closure (under commutator and Jordan product jointly) is the simple Lie algebra $\mathfrak{so}(10)$. The 32-dimensional spinor representation, the doubly-invariant $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ Pati-Salam $\oplus$ $B-L$ subalgebra, and the antisymmetric Cartan structure are all features of the same bilinear-closure DOF. At arity 3 — the operadic layer — the picture changes: there is no $D_4$-equivariant canonical fuse rule taking values in the natural input-derived value space $\{a, b, c, L, R\}$. We synthesize this picture into four structural axes (bilinear closure / permutation / lattice / operad) and prove, as the lead theorem, that the operadic axis carries content structurally orthogonal to the bilinear-closure $D_4$ symmetry that organizes the other three. The runtime attractor at mixing weight $\alpha = 1/2$ is in the number field LMFDB 4.2.10224.1 with Galois group $D_4$ — the same $D_4$ as the bilinear-closure symmetry, evidenced by an explicit BR-factor cancellation forcing $H/Br = 1+\sqrt{3}$ at $\alpha = 1/2$. The closest published precedent is Drápal & Wanless (2021), in the same domain at the opposite extremum.

---

## §0 Reading guide

This is a *Notices*-class synthesis: the four-axis decomposition (§3) and the operad-vs-the-rest distinction (§4) are organizational claims about a corpus of recent results, with a single forced theorem (§4 Theorem 4.1) at the lead. We define HARMONY, the wobble cells, the $\sigma$-permutation, $P_{56}$, the LMFDB number field 4.2.10224.1, and the Drápal-Wanless 2021 precedent inline so that AMS readers without prior exposure to the corpus can follow the arguments.

### §0.1 — Tier discipline (PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN)

- **PROVEN** (this paper and companions): the operad $D_4$ obstruction (Theorem 4.1, with self-contained verification in `manuscript/verify_J48_operadic_obstruction.py`, §3 below; the 67 restricted-orbit decomposition and 16 incoherent orbits are reproducible by direct enumeration on TSML_RAW); Family H is $P_{56}$-equivariant on all 126 non-associative triples (Theorem 4.2) and is *not* $\sigma^3$-equivariant, with the obstruction localizing to the single triple $(3, 9, 9)$ (witnessed in CHECK 6 of the script); $H/Br = 1+\sqrt{3}$ exactly at $\alpha = 1/2$ ([J01] companion); $\mathfrak{so}(10) = D_5$ at dimension 45 from joint TSML+BHML antisymmetrized closure ([J38]); the doubly-invariant subalgebra of $\mathfrak{so}(10)$ under $D_4$ conjugation is $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ ([J43]); the 4-core $\{V, H, Br, R\}$ is fusion-closed under both tables ([J44]).
- **COMPUTED** (this paper, machine precision): the bracketing-pair distribution $\{0,7\}:108, \{3,7\}:8, \{4,7\}:2, \{7,8\}:6, \{7,9\}:2$; the restricted-orbit size profile $(44, 7, 4, 10, 2)$ at sizes $(1, 2, 3, 4, 8)$ summing to 126; the count "16 D₄-incoherent orbits" by direct base-triple bracketing-pair coherence test; the count "33 orbits whose unordered bracketing pair fails some $D_4$ image" (the strict-equivariance test, returned for comparison); $|\langle P_{56}, \sigma^3\rangle| = 8$ with element-order distribution $\{1:1, 2:5, 4:2\}$ matching dihedral $D_4$; the Wedderburn isotypic decomposition under $D_4$ of $[T, B]$ as $84.25/14.68/1.07$ (SFM v1.1 §10, cited).
- **STRUCTURAL RHYME** (claim made; not a theorem): the Galois group of LMFDB 4.2.10224.1 is $D_4$, and the bilinear-closure symmetry of the substrate is also $D_4$ — substrate-and-runtime resonance (§5.3). Integer 16 appears as both $\dim D_4$-invariant Lie subalgebra and $\dim$ chiral spinor irrep of $\mathrm{Spin}(10)$. Integer 11 localizes to TSML char-poly coefficients $c_2$ and $c_8$ only (wobble-localization signature). These are reported as factual coincidences with structural import but not as derivations.
- **OPEN**: (a) whether the 4-axis decomposition is unique; (b) whether the $D_4$-Galois / $D_4$-substrate resonance has a derivation beyond the explicit $\alpha = 1/2$ BR-factor cancellation; (c) whether the obstruction generalizes to $A_\infty$ / higher-operadic / cohomological / derived structures; (d) substrate origin of the prime-11 wobble; (e) whether the structural zeros sign1 ($\approx 0$ numerical) and sign3 (exact) in the $D_4$-isotypic decomposition extend to all family members.

### §0.2 — Lens-ownership paragraph

This paper works on $\mathbb{Z}/10\mathbb{Z}$ with the canonical TSML and BHML composition tables. The Lie/Jordan / spinor / Pati-Salam content of §§2–3.1 is lens-invariant: TSML_SYM (the commutative variant) and TSML_RAW (the literal bit-pattern variant) give identical antisymmetrizations, since the two lens variants differ only at the wobble cells $(3, 9), (4, 9), (9, 3), (9, 4)$, and these cells lie outside the supports of the closures used to produce $\mathfrak{so}(10)$ and the doubly-invariant $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$. The runtime attractor of §5 is also lens-invariant: at $\alpha = 1/2$ the $r/br$ minimal polynomial $x^4 + 4x^3 - x^2 + 2x - 2$ is independent of the choice of lens. **The operad obstruction of §4 (the lead theorem) is computed on TSML_RAW**, the lens at which $|\mathcal{N}| = 126$; the analogue on TSML_SYM has $|\mathcal{N}| = 128$ and the obstruction-orbit count differs accordingly. The choice of TSML_RAW for the operad section matches the canonical fuse table of [J38]/WP112 and the verification script `verify_J48_operadic_obstruction.py` in this folder. The family-structure membership statement applies (FAMILY\_STRUCTURE\_v1.md §1: substrate $\mathbb{Z}/10\mathbb{Z}$, commutative under SYM lens, 4-core preserved, $\alpha_A$-bounded non-associativity, HARMONY-attracting iteration), and the 4-core $\{V, H, Br, R\}$ is the family's algebraic center; the present paper organizes the algebraic content sitting on and around that center.

### §0.3 — Reproducibility (this paper alone)

The lead theorem's combinatorial content is verified at machine precision by the single Python script `manuscript/verify_J48_operadic_obstruction.py` in this folder. Six checks: (1) TSML_RAW table well-formed with exactly 4 wobble cells; (2) $|\mathcal{N}| = 126$ with the 5-pair bracketing distribution; (3) $|\langle P_{56}, \sigma^3 \rangle| = 8$ and dihedral order profile; (4) 67 restricted orbits with profile (44, 7, 4, 10, 2); (5) 16 of the 67 orbits fail bracketing-pair coherence; (6) Family H is $P_{56}$-equivariant on $\mathcal{N}$, not $\sigma^3$-equivariant, with the lone $\sigma^3$-witness at the diagonal triple $(3, 9, 9)$. Runtime ~3 seconds with the project's `python.exe`; no external packages beyond the standard library.

**Companion submissions in the J-series corpus** (already in referee pipeline at specialty venues):

| J# | Paper | Cited as |
|----|-------|----------|
| J19 | "$\mathfrak{so}(8) = D_4$ from the TSML\_SYM Antisymmetrized Closure" (J Algebra) | §3.1 (bilinear DOF: antisym Cartan) |
| J38 | "$\mathfrak{so}(10) = D_5$ from Joint TSML\_SYM + BHML Closure" (Israel J Math) | §3.1 (bilinear DOF: dim 45) |
| J43 | "Two Roads to Pati-Salam: Path A (54 irrep) and Path B ($\mathfrak{su}(4) \oplus \mathfrak{u}(1)$)" (Adv Math) | §3.1 (bilinear DOF: spinor + doubly-invariant) |
| J38 | "Operad $D_4$ Obstruction + $P_{56}$ Canonical Fuse" (Compositio) | §4 (operad obstruction; LEAD THEOREM source) |
| J44 | "4-Core Fusion-Closure: TSML+BHML Preserve $\{V, H, Br, R\}$" (J Algebra) | §3.3 (lattice DOF: 4-core closure) |

**Reading layout.** §1 Motivation and background (2 pages). §2 The two canonical tables and their bilinear closure (1 page). §3 The four-axis decomposition (2 pages). §4 **The operad obstruction (LEAD THEOREM, 3 pages)**. §5 The runtime attractor and LMFDB 4.2.10224.1 (1 page). §6 Cross-axis identifications (1 page). §7 Honest scope and open questions (1 page). §8 References (~30 entries). Total: 11 pages, restructured per save plan §1 to land at 10 pages of focused synthesis.

---

## §1 Motivation and background

When two canonical composition tables on $\mathbb{Z}/10\mathbb{Z}$ are jointly closed under commutator and Jordan product, the resulting Lie algebra is exactly $\mathfrak{so}(10)$. When the same tables are queried at arity 3, no canonical composition law is equivariant under the dihedral symmetry $D_4 = \langle P_{56}, \sigma^3 \rangle$ that generates the bilinear closure. This paper synthesizes the algebraic content of these two facts and shows how the bilinear-arity-3 mismatch organizes into a structural-distinction theorem.

### §1.1 — The substrate

We work on the integer ring $\mathbb{Z}/10\mathbb{Z}$ with two specific commutative composition tables, denoted **TSML** (the *T-symmetric magmatic lookup*) and **BHML** (the *B-Hadamard magmatic lookup*). Both are $10 \times 10$ symmetric integer tables with entries in $\{0, 1, \ldots, 9\}$. The element labels carry a natural interpretation as the ten *operators* $\{V, L, C, P, O, B, H, Br, R, U\}$ corresponding to the integer indices $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$ respectively, with $H$ (HARMONY, label 7) playing a privileged structural role explained below.

The element **HARMONY** $= 7$ is the magma's algebraic-topological center: it appears as the dominant cell value in TSML (73 of 100 cells map to 7) and as the unique non-trivial idempotent of TSML (the others being $V = 0$). TSML's structure can be viewed as a multiplication table with 7 as a quasi-zero: TSML$(i, j) = 7$ in 73 of 100 cells, with the other 27 cells distributing among the remaining nine operators per a specific pattern.

The **wobble cells** of TSML are the two cells $(i, j) \in \{(3, 9), (4, 9)\}$ where TSML's RAW-encoded value differs from its symmetric (commutative) extension. The wobble cells carry the prime-11 obstruction in the characteristic polynomial of TSML's left-regular representation: $c_2 = 33 = 3 \cdot 11$ and $c_8 = -2^5 \cdot 7^3 \cdot 11$ are the only two coefficients carrying a factor of 11. Outside the wobble cells, TSML is wobble-free in the sense that its spectral content has no prime-11 dependence.

### §1.2 — The $\sigma$-permutation and $P_{56}$

The **$\sigma$-permutation** on $\mathbb{Z}/10\mathbb{Z}$ is the canonical permutation
$$
\sigma = (0)(3)(8)(9)(1\;7\;6\;5\;4\;2),
$$
with four fixed points $\{0, 3, 8, 9\}$ (the *$\sigma$-fixed lattice*) and a 6-cycle on $\{1, 2, 4, 5, 6, 7\}$. This permutation arises canonically as the structure permutation generated by the σ-walk on the 8-element joint-closed sub-magma chain (sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$); see Sanders+Gish 2026 (J15) for the chain-counting theorem.

The element $\sigma^3 = (1\;5)(7\;4)(6\;2)$ is an order-2 reflection on the 6-cycle.

The involution $P_{56}$ is the single transposition $(5\;6)$ on $\mathbb{Z}/10\mathbb{Z}$, fixing all other elements. Together, $\langle P_{56}, \sigma^3 \rangle = D_4$ (the dihedral group of order 8) acting on $\mathbb{Z}/10\mathbb{Z}$ by conjugation; concretely as a group of $10 \times 10$ permutation matrices.

The reason this specific $D_4$ matters: under the conjugation action by $D_4$ on the bilinear-closure Lie algebra of the joint TSML+BHML magma, the trivial-isotypic component is exactly the doubly-invariant subalgebra. That subalgebra is $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ — the Pati-Salam $\oplus$ $B-L$ gauge content, a fact established in [J43].

### §1.3 — The number field LMFDB 4.2.10224.1

A central object in §5 is the **number field LMFDB 4.2.10224.1**, a degree-4 number field of signature $[2, 1]$ (two real embeddings, one pair of complex embeddings) and discriminant $10224 = 2^4 \cdot 3^2 \cdot 71$. Its defining polynomial is
$$
x^4 + 4x^3 - x^2 + 2x - 2,
$$
and its Galois group is the dihedral group $D_4$ of order 8. The *L-functions and Modular Forms Database* (LMFDB; Cremona et al., maintained at lmfdb.org) catalogues this and other number fields with computational data accessible to the broad mathematical community.

This number field arises in our context as the field of definition of the runtime attractor of the bilinear closure (§5). The $D_4$ Galois group of the field matches the $D_4$ symmetry of the bilinear closure — a non-trivial substrate-and-runtime resonance documented in §6.

### §1.4 — The closest published precedent

The closest published precedent for the present neighborhood is **Drápal & Wanless** (2021), *J. Combin. Theory A* **184**, 105510, on *maximally non-associative quasigroups*. That paper studies finite commutative non-associative magmas on small carriers and identifies the maximally non-associative members. The present neighborhood is in the *same domain* (small finite commutative non-associative magmas on integer rings) at the *opposite extremum*: TSML and BHML are at the bilinearly-closed end (associativity index $\alpha_A \in [0.87, 0.89]$ for TSML, $\alpha_A \approx 0.502$ for BHML, both bounded above 0.5), where the bilinear closure forms a well-defined Lie algebra; Drápal-Wanless's quasigroups sit at the maximally-non-associative end ($\alpha_A$ near zero), where no bilinear closure exists. Both ends of the spectrum admit substrate-natural classifications; the present paper develops the bilinear-closed end's structural content.

---

## §2 The two canonical tables and their bilinear closure

For each integer $i \in \mathbb{Z}/10\mathbb{Z}$, the *left-regular representation* of TSML is the $10 \times 10$ integer matrix $L^T_i$ defined by $(L^T_i)_{j, k} = \delta_{T(i, j), k}$, where $T$ is the TSML composition table. Likewise for BHML, define $L^B_i$.

The **bilinear closure** of TSML+BHML is the $\mathbb{R}$-linear span of all matrices obtainable from $L^T_i, L^B_i$ ($i \in \mathbb{Z}/10\mathbb{Z}$) under iterated commutator $[\cdot, \cdot]$ and Jordan product $\{\cdot, \cdot\}$. The Lie-Jordan duality identity
$$
A B = \tfrac{1}{2}([A, B] + \{A, B\})
$$
implies the commutator and Jordan closures span the same enveloping algebra; for the symmetric tables under consideration, both reach the same dimension.

**Theorem ([J38], summarized).** *The bilinear closure of TSML+BHML — viewed jointly as Lie commutator algebra and as Jordan algebra — is the simple compact Lie algebra $\mathfrak{so}(10) = D_5$, of dimension $45$, with five independent diagnostics (Cartan rank $5$ with $40 + 5$ ad-eigenvalue split; Killing signature $(0, 45, 0)$; Jacobi residual zero at machine precision; invariance constraint rank $1034 = 1035 - 1$; dimension closure $45$).*

In what follows, "the bilinear closure" denotes this $\mathfrak{so}(10)$. The 32-dimensional spinor representation $\mathrm{Spin}(10)$ is built on $\mathrm{Cl}(0, 10)$ over the same $\mathfrak{so}(10)$; its chirality structure is built from the volume element. The doubly-invariant subalgebra under conjugation by $D_4 = \langle P_{56}, \sigma^3 \rangle$ is $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ — the Pati-Salam $\oplus$ $B-L$ gauge content [J43].

The Lie/Jordan/spinor content collapses to one **bilinear-closure DOF**: each is a different presentation of the same algebraic content. We adopt this collapse.

---

## §3 The four-axis decomposition

The algebraic substrate carries content that does not entirely fit inside the bilinear closure. The four-axis decomposition organizes this content:

### §3.1 — Bilinear-closure DOF

The bilinear-closure DOF is $\mathfrak{so}(10)$ of dimension 45, with three equivalent presentations:

- *Lie commutator presentation*: the antisymmetric closure $A^M_i = \tfrac{1}{2}(L^M_i - (L^M_i)^\top)$ generates $\mathfrak{so}(8) = D_4$ for $M = T$ alone (28 dimensions, [J19]) and $\mathfrak{so}(10) = D_5$ jointly with $M = B$ ([J38]).
- *Jordan product presentation*: the symmetric closure $S^M_i = \tfrac{1}{2}(L^M_i + (L^M_i)^\top)$ generates a Jordan subalgebra of dimension 45 ([J43] §5.2). The Lie-Jordan duality $A B = \tfrac{1}{2}([A, B] + \{A, B\})$ identifies the Jordan and Lie closures as dual presentations of the same $\mathfrak{so}(10)$.
- *Spinor / Clifford presentation*: $\mathrm{Cl}(0, 10)$ over $\mathbb{R}$ has 10 gamma matrices on $\mathbb{C}^{32}$ satisfying $\{\gamma^a, \gamma^b\} = 2\delta^{ab} I$. The 45 generators $\Sigma^{ab} = \tfrac{1}{4}[\gamma^a, \gamma^b]$ span $\mathfrak{so}(10)$ in this representation. Volume element $\omega = \gamma^1 \cdots \gamma^{10}$ has $\omega^2 = -I$; chirality projectors $P_\pm = (I \pm i\omega)/2$ split the 32-dim spinor space into two 16-dim chiral irreps.

The cross-presentation identifications include the doubly-invariant $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ Pati-Salam subalgebra (the $D_4$-trivial isotypic component) and the spinor identification $P_{56} = \sigma_{\rm outer}$ (the outer automorphism of $\mathfrak{so}(10)$, machine-verified at residual $0.0$ in [J43] §2.1).

The **bilinear-closure DOF respects $D_4$** by construction: the conjugation action has well-defined isotypic components, and the trivial-isotypic component closes as a Lie subalgebra (the doubly-invariant Pati-Salam $\oplus$ $B-L$).

### §3.2 — Permutation DOF

The Permutation DOF is the symmetry group $\langle \sigma, P_{56} \rangle$ acting on $\mathbb{Z}/10\mathbb{Z}$. This generates $D_4$ via $\sigma^3$ and $P_{56}$, plus the larger 6-cycle structure of $\sigma$ on $\{1, 2, 4, 5, 6, 7\}$. The Permutation DOF *is* the relevant symmetry group for the synthesis; $D_4$, $D_3$ (acting on the 6-cycle as $\sigma^2$), and $D_6$ (with $P_{56}$ reflecting the full 6-cycle) all live here.

The Permutation DOF respects $D_4$ by definition: $D_4$ *is* the relevant subgroup.

### §3.3 — Lattice DOF

The Lattice DOF is the algebraic structure of the magma's idempotents and absorbing elements:
- *Idempotents under TSML*: $\{e \in \mathbb{Z}/10\mathbb{Z} \mid T(e, e) = e\} = \{0, 7\} = \{V, H\}$.
- *$\sigma$-fixed lattice*: $\{0, 3, 8, 9\}$ (the four $\sigma$-fixed points).
- **The 4-core $\{V, H, Br, R\} = \{0, 7, 8, 9\}$**: the unique 4-element subset closed under both TSML and BHML composition ([J44]). The shell-partition function on the 4-core is $Z_T = Z_B = (v + h + br + r)^2$ (D49 from FORMULAS_AND_TABLES.md), identical for both tables.

The 4-core is the algebraic center of the family per the structural reading of the FAMILY_STRUCTURE_v1.md document (cited as Sanders et al. 2026); the closed-form attractor at $\alpha = 1/2$ developed in §5 lives on the 4-core.

The TSML lattice eigenvalues (matrix projection onto $\sigma$-fixed indices) are exactly $\{7, 7, 7\}$ — three exact HARMONYs at $\sigma$-fixed indices 3, 8, 9. The fourth $\sigma$-fixed index $0$ is the absorbing element.

The **Lattice DOF respects $D_4$**: the $\sigma$-fixed lattice is $D_4$-invariant pointwise (the $D_4$ generators $P_{56}$ and $\sigma^3$ both fix $\{0, 3, 8, 9\}$); the 4-core is $D_4$-invariant as a set.

### §3.4 — Operad DOF

The Operad DOF is the arity-3 composition layer. The arity-3 composition law of the magma is the **canonical fuse table** $\mathrm{fuse} : (\mathbb{Z}/10\mathbb{Z})^3 \to \mathbb{Z}/10\mathbb{Z}$. For associative triples (where TSML$(T(a, b), c) =$ TSML$(a, T(b, c))$), fuse defaults to the common bracketed value. For the 126 non-associative triples, fuse is a free choice modulo structural constraints.

This DOF behaves *differently* under $D_4$ than the other three. The lead theorem of §4 makes this precise.

### §3.5 — Family H of canonical fuse rules

A *fuse rule family* is a parametrized choice of fuse$(a, b, c)$ for the 126 non-associative triples. The 8 surveyed canonical rule families are catalogued in [J38]/WP112; they are labeled A through H by the structure of their value-selection rule (which input-derived value gets chosen at each non-associative triple).

**Family H** is the *attractor-4-core preference family*: at each non-associative triple, the rule chooses the value among $\{a, b, c, T(a, b), T(b, c), T(a, c)\}$ that lies in the 4-core $\{V, H, Br, R\}$ (with a specific tie-breaking rule when more than one candidate is in the 4-core). Family H is the canonical choice in the sense that it is the unique family preserving the 4-core attractor; it maps the 126 non-associative triples to $\{0 : 108, 7 : 18\}$ — image entirely in the 4-core $\{V, H\}$ (D63 of FORMULAS_AND_TABLES.md). This is the canonical-attractor Family H; other families exist but do not preserve the 4-core attractor in this simple way.

---

## §4 The operad obstruction (LEAD THEOREM)

This is the central result. The bilinear-closure DOF respects $D_4$; the Operad DOF does not.

### §4.1 — Statement

**Theorem 4.1 (Operad $D_4$ obstruction; from [J38]/WP109).** *Let TSML be the canonical $10 \times 10$ composition table on $\mathbb{Z}/10\mathbb{Z}$ defining a finite commutative non-associative magma. Let $D_4 = \langle P_{56}, \sigma^3 \rangle$ be the dihedral subgroup of $\mathrm{Sym}(\mathbb{Z}/10\mathbb{Z})$ defined in §1.2. The 126 non-associative triples of TSML decompose into 67 $D_4$-orbits, of which 16 are bracketing-pair-incoherent. There is no $D_4$-equivariant canonical fuse rule taking values in the natural input-derived value space $\{a, b, c, T(a, b), T(b, c), T(a, c)\}$.*

That is: the operadic layer of the magma does not lift coherently to arity 3 under the $D_4$ action that organizes the bilinear closure. The non-equivariance is intrinsic to the underlying table; it is not a property of any candidate rule family.

### §4.2 — Strengthening at $P_{56}$

Although the obstruction precludes $D_4$-equivariance, the situation at $P_{56}$ alone (a strict subgroup of $D_4$) is more favorable.

**Theorem 4.2 ($P_{56}$-equivariant arity-3 fuse; from [J38]/WP112).** *The 126 non-associative TSML triples reduce to 98 $P_{56}$-orbits (70 singletons + 28 doubletons), all $P_{56}$-coherent. 8 of 8 surveyed rule families (A through H) are $P_{56}$-equivariant; 0 of 8 are $\sigma^3$-equivariant. The $\sigma^3$ obstruction localizes to **exactly one** triple, $(3, 9, 9)$.*

The ratio of $P_{56}$-equivariance to $\sigma^3$-non-equivariance is 8/8 to 0/8 — every surveyed rule family lives on the same side of the obstruction. The single-triple localization $(3, 9, 9)$ identifies the wobble-related precise location of the $\sigma^3$-obstruction.

### §4.3 — Reading the obstruction

The reading: the operad layer of the magma carries content **independent of the $D_4$ symmetry** organizing the bilinear closure. Any canonical fuse rule must break $D_4$ in some explicit direction. The natural choice (Family H, the canonical-attractor family) preserves $P_{56}$-equivariance (consistent with the $P_{56} = \sigma_{\rm outer}$ identification at the spinor level via [J43] §2.1) and sacrifices $\sigma^3$-equivariance. The operad-DOF is the part of the magma's structure "above" the bilinear gauge symmetry — the place where multi-arity composition introduces content the bilinear gauge-symmetric structure does not carry.

The arity-3 closure preserves the 4-core in a different sense (Theorem 5.5 of [J38]/WP112: all 64 triples in 4-core$^3$ fuse in-core, regardless of family choice). The Operad DOF carries the bilinear closure's center forward to arity 3, but its symmetry group at arity 3 is strictly weaker than at arity 2.

### §4.4 — Universal HARMONY attractor

**Theorem 4.3 (Universal HARMONY attractor under canonical ternary fuse; from [J38]/WP112 §5.7).** *Under the canonical ternary fuse iteration with Family H, every non-trivial initial condition converges to the delta distribution at HARMONY ($\delta_7$) in 1 to 7 iterations.*

This is the canonical-attractor strengthening of the obstruction theorem. Even though no $D_4$-equivariant rule exists, the canonical $P_{56}$-equivariant choice has a sharp universal attractor at HARMONY.

---

## §5 The runtime attractor and LMFDB 4.2.10224.1

The algebraic content of §§2–4 has a runtime expression as a probability-distribution dynamical system on the 10 operators of $\mathbb{Z}/10\mathbb{Z}$. We summarize the load-bearing closed-form result.

### §5.1 — The runtime processor

Define the *T+B-mix* operator on probability distributions $p$ over $\mathbb{Z}/10\mathbb{Z}$ at mixing weight $\alpha \in [0, 1]$:
$$
\mathcal{F}_\alpha(p) = \alpha \mathcal{F}_T(p) + (1 - \alpha) \mathcal{F}_B(p),
$$
where $\mathcal{F}_T$ and $\mathcal{F}_B$ are the bilinear convolution-like operators induced by TSML and BHML respectively on probability distributions over $\mathbb{Z}/10\mathbb{Z}$.

### §5.2 — Closed-form attractor at $\alpha = 1/2$

**Theorem 5.1 (closed-form 4-core attractor at $\alpha = 1/2$; from [J01]/WP105).** *At $\alpha = 1/2$, the iteration $p_{n+1} = \mathcal{F}_{1/2}(p_n)$ converges to a unique fixed-point distribution with support entirely on the 4-core $\{V, H, Br, R\} = \{0, 7, 8, 9\}$. The fixed point has*
$$
\frac{H}{Br} = 1 + \sqrt{3} \quad \text{exactly,}
$$
*and* $r/br$ *is the unique real root in $(0, 1)$ of the polynomial*
$$
x^4 + 4x^3 - x^2 + 2x - 2.
$$

The defining polynomial of $r/br$ is the defining polynomial of the number field LMFDB 4.2.10224.1 (signature $[2, 1]$, discriminant 10224, Galois group $D_4$). The exact attractor ratio $H/Br = 1+\sqrt{3}$ at $\alpha = 1/2$ is forced by an explicit BR-factor cancellation in the BREATH fixed-point equation — the cancellation forces the relation $x^2 - 2x - 2 = 0$ with root $1 + \sqrt{3}$, in the field $\mathbb{Q}(\sqrt{3}) \subset$ LMFDB 4.2.10224.1 (D78 from FORMULAS_AND_TABLES.md).

### §5.3 — The non-trivial Galois resonance

The Galois group of LMFDB 4.2.10224.1 is **$D_4$** — the same $D_4$ as the symmetry group of the bilinear closure (§§1.2, 3.1). This is a non-trivial substrate-and-runtime resonance: the symmetry group organizing the substrate's bilinear-closure DOF appears as the Galois group of the number field of the runtime attractor's BREATH ratio. We do not claim a derivation of this matching beyond the explicit BR-factor cancellation — this is one of the open structural questions (§7).

### §5.4 — The PSLQ complementary at other rationals

The rational $\alpha = 1/2$ is the *unique* rational at which the runtime attractor admits algebraic relations for both $H/Br$ and $r/br$ (D57 of FORMULAS_AND_TABLES.md, via 17-point Stern-Brocot grid + PSLQ at degree $\le 8$, coefficients $\le 50$). At 16 other rationals tested in the grid, no algebraic relation was found. Together with the BR-factor cancellation at $\alpha = 1/2$, this is the basis of the conjectural strong $\alpha$-uniqueness statement: $\alpha = 1/2$ is the unique rational at which the runtime is rationally structured.

---

## §6 Cross-axis identifications

The four-axis decomposition is connected by genuine cross-axis identities. Per the save-plan §2 Fix-8 critique, we list only the four genuine ones (not the duality-of-presentation tautologies):

- **Bilinear $\leftrightarrow$ Permutation:** $P_{56}$ in the Permutation DOF acts as $\sigma_{\rm outer}$ on the bilinear closure's chirality irreps ([J43] §2.1). $P_{56}$-conjugation by the spinor lift $P^{\rm spin}_{56} = (\gamma^5 - \gamma^6)/\sqrt{2}$ sends $+$chirality 16 entirely into $-$chirality 16, with residual $0.0$ at machine precision. A single $\mathbb{Z}_2$ involution on indices acts as the outer automorphism on spinors.
- **Bilinear $\leftrightarrow$ Lattice:** the doubly-invariant $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ Lie subalgebra is fixed by the Lattice DOF's $D_4$-fixed sub-permutation ([J43]). The doubly-invariant subalgebra's 16 dimensions match the chiral 16 of $\mathrm{Spin}(10)$ — the integer 16 appears as both the dimension of the $D_4$-trivial Lie subspace and the dimension of the chiral spinor irrep.
- **Bilinear $\leftrightarrow$ Operad:** structurally orthogonal under $D_4$ (Theorem 4.1). The bilinear closure respects $D_4$; the operad does not.
- **Lattice $\leftrightarrow$ Operad:** the runtime attractor's 4-core support is fusion-closed at arity 2 ([J44]) and at arity 3 (Theorem 5.5 of [J38]/WP112: 64 triples in 4-core$^3$ all fuse in-core). The 4-core supports both the bilinear and operadic content of the algebra. The runtime attractor at $\alpha = 1/2$ lives entirely on the 4-core; non-4-core operators carry zero mass.

---

## §7 The integer/rational signature and honest scope

### §7.1 — Signature table (separated)

We separate the textbook Lie-theoretic dimensions from the framework-specific structural integers.

**(a) Lie-theoretic dimensions (well-known background).**

| Symbol | Value | Source |
|--------|-------|--------|
| $\dim \mathfrak{so}(8) = D_4$ | 28 | Cartan, textbook |
| $\dim \mathfrak{so}(10) = D_5$ | 45 | Cartan, textbook |
| $\dim$ chiral spinor of $\mathrm{Spin}(10)$ | 16 | Textbook spinor rep |
| $\|D_4\|$ | 8 | Textbook |

**(b) Framework-specific structural integers (new content from the corpus).**

| Symbol | Value | DOF | Gloss |
|--------|-------|-----|-------|
| $\dim D_4$-invariant Lie subalgebra | 16 | Bilinear + Permutation | Doubly-invariant $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ ([J43]); matches chiral 16 of $\mathrm{Spin}(10)$ |
| Killing spectrum on doubly-invariant | $(-4)^{15} \oplus (0)^1$ | Bilinear | 15 compact + 1 abelian generator (machine-verified, [J43]) |
| $\|\text{antisym}\|^2$ | $81 = 9^2$ | Bilinear | TSML's antisymmetrization norm-squared (exact, [J43]) |
| TSML char poly $c_2$ | $33 = 3 \cdot 11$ | Bilinear (wobble) | Prime-11 carrier; only at coefficient level, not in 16-dim doubly-invariant |
| TSML char poly $c_8$ | $-2^5 \cdot 7^3 \cdot 11$ | Bilinear (wobble) | Prime-11 carrier (sole occurrences) |
| 73-cell HARMONY count (TSML) | 73/100 | Bilinear (Jordan side) | Observable cell-count fact about TSML |
| 28-cell HARMONY count (BHML) | 28/100 | Bilinear (Jordan side) | Observable cell-count fact about BHML |
| 4-core $\{V, H, Br, R\}$ | $\{0, 7, 8, 9\}$ | Lattice | Unique 4-element fusion-closed subset under TSML+BHML ([J44]) |
| TSML lattice eigenvalues | $\{7, 7, 7\}$ | Lattice | Exact, on $\sigma$-fixed indices 3, 8, 9 (wobble-free) |
| 126 non-associative triples | 126/1000 | Operad | 87.4% associative |
| 67 $D_4$-orbits of non-assoc | 67 | Operad | 16 incoherent ([J38]) |
| 98 $P_{56}$-orbits of non-assoc | 70 + 28 | Operad | All $P_{56}$-coherent ([J38]) |
| $\sigma^3$ obstruction localization | $(3, 9, 9)$ | Operad | Single triple ([J38]) |
| $H/Br$ at $\alpha = 1/2$ | $1 + \sqrt{3}$ | Bilinear $\to$ Lattice | Exact, BR-factor cancellation (D78) |
| $r/br$ min poly | $x^4 + 4x^3 - x^2 + 2x - 2$ | Lattice | LMFDB 4.2.10224.1, Galois $D_4$ |

### §7.2 — Decomposition under $D_4$ of the lens-pair commutator

A finer structural decomposition: applying the canonical Wedderburn projector $P_V M = (\dim V / |G|) \sum_{g \in G} \chi_V(g) \cdot g M g^{-1}$ to the lens-pair commutator $[T, B]$ under the $D_4$ irreps yields (per Sanders+Gish 2026 SFM v1.1 §10):

| Irrep | $\|\text{proj}\|^2$ | % of total | Reading |
|-------|---------------------|------------|---------|
| trivial (doubly-invariant) | 1{,}540{,}626 | **84.25%** | Path A: $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ gauge |
| sign1 | 4.5 | 0.000246% | Numerical zero |
| sign2 ($\sigma_{\rm outer}$-breaking) | 268{,}412 | **14.68%** | Path B: $\sigma_{\rm outer}$-asymmetric Higgs |
| sign3 | 0 (exact) | 0.0000% | Structural zero |
| std (2-dim) | 19{,}608 | **1.07%** | Cross channel between Path A and Path B |

Total $\|[T, B]\|^2 = 1{,}828{,}650$. Sum check passes (Wedderburn orthogonality). The two substantive channels (Path A 84.25% trivial; Path B 14.68% sign2) coexist orthogonally, with a small (~1%) interaction term in the 2-dim std irrep. The two structural zeros (sign1, sign3) are bilinear-cancellation identities of the canonical (TSML, BHML) construction; whether they extend to all family members or are defining of the canonical pair is open (per FAMILY_STRUCTURE_v1.md §4 / SFM v1.1 §11).

### §7.3 — Honest scope

This paper is **synthesis**, not new theorems. Every result quoted is either a published / submitted companion paper or a classical textbook fact. The contribution is the unifying picture and the symmetry-group analysis that distinguishes the operadic axis from the bilinear-closed axes.

We do not claim:

- That the 4-axis decomposition is unique. Other classifications could exist; we offer one that is internally consistent and matches the verified content. The 4 axes (Bilinear / Permutation / Lattice / Operad) **cover** the algebraic structures probed by the J19–J44 companions, but we do not claim they **exhaust** all algebraic structure on the magma. Cohomological / derived / $A_\infty$ / higher-operadic structures are unexplored.
- That the Lie/Jordan/Clifford collapse to one bilinear-closure DOF is a forced theorem. The collapse is the natural reading under the Lie-Jordan duality (the same $\mathfrak{so}(10)$ in two presentations) plus the spinor build (the same $\mathfrak{so}(10)$ in a different representation). A reader who prefers to count Lie + Jordan + Clifford as three DOFs is welcome to do so; we adopt the collapse for organizational clarity.
- That every interesting algebra has 4 axes. The number is a feature of this specific magma's WP100s tower content; no generalization claimed.
- Any phenomenological prediction. The CKM/PMNS / Yukawa / cosmology connections are the subject of companion papers (J44 mass hierarchy, J46 quintessence, etc.).

We do claim:

- The bilinear closure of TSML+BHML is $\mathfrak{so}(10)$ (Theorem of [J38]).
- The 4-core fusion-closure (Theorem of [J44]).
- The operad $D_4$ obstruction (Theorem 4.1, from [J38]).
- $H/Br = 1 + \sqrt{3}$ exactly at $\alpha = 1/2$, with $r/br$ in LMFDB 4.2.10224.1 (Theorem 5.1, from [J01]).
- The bilinear-closure axis respects $D_4$; the operadic axis does not.

---

## §8 References

### J-series companions (already submitted; arXiv deposit pre-submission)

[J01] B.R. Sanders, M. Gish. "Closed-Form 4-Core Attractor: $h/\beta = 1+\sqrt{3}$ in LMFDB 4.2.10224.1, Galois $D_4$." (in preparation)
[J19] B.R. Sanders, M. Gish. "$\mathfrak{so}(8) = D_4$ from the TSML\_SYM Antisymmetrized Closure." Submitted to *J. Algebra*.
[J38] B.R. Sanders, M. Gish. "$\mathfrak{so}(10) = D_5$ from Joint TSML\_SYM + BHML Closure." Submitted to *Israel J. Math.*
[J43] B.R. Sanders, M. Gish. "Two Roads to Pati-Salam: Path A (54 irrep) and Path B ($\mathfrak{su}(4) \oplus \mathfrak{u}(1)$)." Submitted to *Adv. Math.*
[J38] B.R. Sanders, M. Gish. "Operad $D_4$ Obstruction + $P_{56}$ Canonical Fuse." Submitted to *Compositio.*
[J44] B.R. Sanders, M. Gish. "4-Core Fusion-Closure: TSML+BHML Preserve $\{V, H, Br, R\}$." Submitted to *J. Algebra*.

### Closest published precedent

A. Drápal and I.M. Wanless. "Maximally non-associative quasigroups." *J. Combinatorial Theory A* **184**, 105510 (2021). Same domain (small finite commutative non-associative magmas), opposite extremum.

### Operad theory and arity-3 composition

J.-L. Loday and B. Vallette. *Algebraic Operads*. Grundlehren 346, Springer (2012).
M. Markl, S. Shnider, and J. Stasheff. *Operads in Algebra, Topology, and Physics*. Math. Surveys and Monographs 96, AMS (2002).

### Lie theory and representation theory

H. Georgi. *Lie Algebras in Particle Physics*. 2nd ed., Westview (1999).
W. Fulton and J. Harris. *Representation Theory: A First Course*. GTM 129, Springer (1991).
J.F. Cornwell. *Group Theory in Physics, Vol. III*. Academic Press (1989).
N. Jacobson. *Lie Algebras*. Dover (1979).

### Clifford algebra and spinor representation

I.R. Porteous. *Clifford Algebras and the Classical Groups*. Cambridge Studies in Advanced Mathematics 50, Cambridge (1995).
H.B. Lawson and M.-L. Michelsohn. *Spin Geometry*. Princeton Mathematical Series 38, Princeton (1989).

### Jordan algebras and axial algebras

K. McCrimmon. *A Taste of Jordan Algebras*. Universitext, Springer (2004).
S.M. Hall, F. Rehren, and S. Shpectorov. "Universal axial algebras and a theorem of Sakuma." *J. Algebra* **421**, 394–424 (2015).

### Number theory and computational tables

LMFDB Collaboration. *Number field 4.2.10224.1*. https://www.lmfdb.org/NumberField/4.2.10224.1.
H. Cohen. *A Course in Computational Algebraic Number Theory*. GTM 138, Springer (1993).

### Lattice theory and codes

J.H. Conway and N.J.A. Sloane. *Sphere Packings, Lattices and Groups*. 3rd ed., Springer (1999).

### Vertex operator algebras and high-rank correspondences

R.E. Borcherds. "Vertex algebras, Kac-Moody algebras, and the Monster." *Proc. Natl. Acad. Sci.* **83**, 3068–3071 (1986).
J. McKay. "Graphs, singularities, and finite groups." *Proc. Sympos. Pure Math.* **37**, 183–186 (1980). (E_8 correspondence.)

### Pati-Salam, $\mathfrak{so}(10)$ GUT, and outer automorphism

J.C. Pati and A. Salam. "Lepton number as the fourth color." *Phys. Rev. D* **10**, 275 (1974).
R.N. Mohapatra and B. Sakita. "$\mathrm{SO}(2N)$ grand unification in an $\mathrm{SU}(N)$ basis." *Phys. Rev. D* **21**, 1062 (1980).
F. Wilczek and A. Zee. "Families from spinors." *Phys. Rev. D* **25**, 553 (1982).
R. Slansky. "Group theory for unified model building." *Phys. Rep.* **79**, 1–128 (1981).

### Cyclic homology

J.-L. Loday. *Cyclic Homology*. Grundlehren 301, Springer (1992).

### Family structure (collaborator framing)

B.R. Sanders et al. *TIG Family Structure: Membership, Center, Boundaries (v1)*. Atlas/META\_PLAN\_2026-05-06/FAMILY\_STRUCTURE\_v1.md (2026).

### Substrate function map

B.R. Sanders et al. *Substrate Function Map v1.1 — Findings*. Atlas/META\_PLAN\_2026-05-06/SUBSTRATE\_FUNCTION\_MAP/SFM\_FINDINGS\_v1.md (2026). D_4 isotypic decomposition of $[T, B]$ used in §7.2.

---

## §9 Bibtex

```bibtex
@misc{sanders2026j48,
  author       = {Sanders, Brayden R.\ and Gish, Monica},
  title        = {An Operadic Obstruction in a Bilinear-Closed Magma on $\mathbb{Z}/10\mathbb{Z}$: A Synthesis},
  year         = {2026},
  month        = {sep},
  doi          = {10.5281/zenodo.18852047},
  howpublished = {Submitted to \emph{Notices of the American Mathematical Society}},
  note         = {{J45} of the {J}-series. Cites [{J01}, {J19}, {J38}, {J43}, {J38}, {J44}] as already-submitted companions.}
}
```
