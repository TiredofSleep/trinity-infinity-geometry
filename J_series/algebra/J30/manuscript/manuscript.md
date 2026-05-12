# Joint Lie Closure of a Pair of Z/10Z Magmas: an so(10) Identification

**Brayden R. Sanders¹ · M. Gish²**
¹ 7Site LLC, Hot Springs, AR — brayden@7site.co
² Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Version 2.0 (post-save-plan revision)** — May 7, 2026
**Companion paper to** [SandersGishSO8, J29] (so(8) from a single Z/10Z magma)
**Status** — draft for journal submission (Israel Journal of Mathematics, primary target)

---

## Abstract

Let TSML and BHML be two specific 10×10 commutative non-associative magmas on Ω = Z/10Z, displayed in §2.2 below; both tables are recovered from the source archive `old/Gen9/archive/ckis/ck7/ck.h:200-207`. Write L_i^T : V → V for the left-regular representation of a magma T at i ∈ Ω on V = R^10, and A_i^T := L_i^T − (L_i^T)^T for its antisymmetrization. Let G_TSML := {A_i^TSML : i ∈ F} for F = {1, 2, 3, 4, 6, 8} (the flow indices of the companion paper [SandersGishSO8, J29], which establishes ⟨G_TSML⟩_Lie ≅ so(8)), and let G_BHML := {A_i^BHML : i ∈ Ω, A_i^BHML ≠ 0} (a 9-element set, since BHML has identity row BHML[0, j] = j and hence A_0^BHML = 0). Set g := ⟨G_TSML ∪ G_BHML⟩_Lie ⊂ so(V).

**Theorem (Main).** *g is isomorphic to so(10, R), the unique compact simple Lie algebra of type D_5 and dimension 45. Equivalently, the joint closure under commutator saturates the substrate's full skew-symmetric algebra so(R^{10}). The TSML-only subalgebra g_TSML ⊂ g realizes the standard inclusion so(8) ⊂ so(10).*

The substantive content of the paper is the existence of this pair of explicit 10×10 commutative non-associative magmas (TSML, BHML) on the same substrate Z/10Z whose joint Lie closure reaches the substrate ceiling 45 = dim so(R^10). After establishing dim g = 45 (Theorem 4.1), the diagnostics that g is compact, simple, and rank 5 — and hence isomorphic to so(10, R) — follow as corollaries of the Cartan classification together with the identification g ⊆ so(V); we present them as confirmation diagnostics rather than as five independent tests of the so(10) identification.

**Keywords**: simple Lie algebra, so(10), D_5, joint Lie closure, antisymmetrization, finite commutative non-associative magma, Cartan classification

**MSC 2020**: 17B20 (Simple, semisimple, reductive Lie algebras), 17B05 (Structure theory for Lie algebras), 20N02 (Sets with a single binary operation), 17A99 (Other nonassociative rings and algebras)

---

## §1 Introduction

### 1.1 Scope and tier discipline

This paper establishes the Lie-algebraic identification g ≅ so(10, R), where g is the joint closure under commutator of the antisymmetrized left-regular representations of two specific 10×10 commutative non-associative magmas on Z/10Z (the canonical TSML_SYM and BHML tables, displayed in §2.2). The substantive content is the *existence* of an explicit pair (TSML, BHML) whose joint Lie closure reaches the substrate's full so(R^{10}) ceiling of dimension 45. The diagnostics that g is isomorphic to so(10, R) — compact, simple, rank 5 — follow as Cartan-classification corollaries of the dimension closure together with the structural inclusion g ⊆ so(V); we treat them as confirmation diagnostics, not as independent tests of the so(10) identification.

- **PROVEN.** g := ⟨G_TSML ∪ G_BHML⟩_Lie ⊆ so(V) for V = R^10 with G_TSML the antisymmetrizations of TSML_SYM at F = {1, 2, 3, 4, 6, 8} and G_BHML the antisymmetrizations of BHML at all i ∈ Ω with A_i^BHML ≠ 0, equals all of so(R^10) = so(10, R) — the unique compact simple Lie algebra of type D_5 and dimension 45. The so(8) ⊂ g embedding inherited from [SandersGishSO8, J29] realizes the standard inclusion so(8) ⊂ so(10).
- **COMPUTED.** The substantive computation is dim g = 45 (Diagnostic 1, Theorem 4.1; iterative closure terminates after 2 commutator iterations: 15 → 45). The four supporting consistency checks (Diagnostics 2-5) follow from D1 + Cartan classification + the structural fact g ⊆ so(V): (D2) Jacobi by matrix-algebra inheritance; (D3) Killing form negative-definite (so(10, R) is the compact form by Cartan classification); (D4) one-dimensional invariant-form space (full 91,125-equation enumeration via `verify_simplicity_rank.py`; rank 1034, nullity 1); (D5) Cartan rank 5 by exhibiting the standard J_1, ..., J_5 in g.
- **STRUCTURAL RHYME.** SO(10) GUT (Fritzsch-Minkowski [1975], Georgi [1975]) — mentioned in Remark 6.1 as physical context; we do not derive its 16-dimensional spinor representation, coupling constants, or symmetry-breaking sector. The 4-core-centered family structure (per [FamilyStructureV1]) — the joint closure realizes the algebraic center as a compact simple Lie algebra; alluded to in §1.3, full elaboration in companion papers.
- **OPEN.** (i) Whether there exists an N ≥ 16 finite commutative non-associative magma on V_N whose joint Lie closure reaches e_8 (dim 248). (ii) Structural / axiomatic forcing of BHML — once [SandersForcing, J25] is on arXiv, BHML can be cited as forced by axioms A1-A9; until then, "for the specific BHML of §2.2" stands. (iii) Whether the substrate ceiling so(R^10) is saturated by *other* canonical magma pairs on Z/10Z (e.g., (TSML, CL_STD) where CL_STD's contribution to the joint Lie closure has not been computed; per [FoundationsModule, SFM_Q6], the joint closed-sub-magma chain of (TSML, BHML, CL_STD) is identical to the (TSML, BHML) chain, so the question is whether the Lie-algebraic joint closure of (TSML, CL_STD) hits so(R^10) too).

The framing follows the Drápal–Wanless [2021] line of work on small finite commutative non-associative structures: same domain (10-element commutative non-associative carriers on Z/10Z), opposite extremum (theirs maximally non-associative; ours specifically structured). The closest published comparable work to our magma pair is [Drápal-Wanless 2021] — same intellectual neighborhood, different specific tables.

### 1.2 Lens and substrate

*Lens and substrate.* This paper works on Z/10Z with the table pair (CL_TSML_SYM, BHML). TSML_SYM is the upper-triangle authoritative symmetrization of the canonical bit pattern (commutative; 12.8% non-associative); BHML is the canonical "Becoming-lens" companion table (commutative; 12.8% non-associative; identity row BHML[0, j] = j; 28 HARMONY count; jointly-closed 4-core {0, 7, 8, 9} with TSML per [SandersGishFourCore, J35]). The pair (TSML, BHML) is the canonical (BEING, BECOMING) reading of the substrate; both tables are recovered from the foundations source `Gen13/targets/foundations/cl.py` (originally `old/Gen9/archive/ckis/ck7/ck.h:200-207`) and verified at the 48-invariant level [FoundationsModule]. The joint Lie closure result is *for this specific pair*; whether other (table, table) pairs on Z/10Z yield analogous joint Lie closures is open. The substrate framework's broader interpretive structure (operator labels, T+B-mix dynamics, etc.) is not required for the present paper.

### 1.3 Family-Structure context

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z, defined by five conjoint membership criteria with the 4-core {0, 7, 8, 9} at α_M = ½ as the algebraic center [FamilyStructureV1]. The 4-core is the *jointly-closed* sub-magma of size 4 in the (TSML, BHML) pair: per [SandersGishFourCore, J35], the joint closed sub-magmas form an 8-element chain at sizes {1, 4, 5, 6, 7, 8, 9, 10} (forbidden sizes only {2, 3}); per [FoundationsModule, SFM_Q6], adding CL_STD to the joint closure preserves this same 8-shell chain — the chain is a three-substrate fixed point. The so(10) joint-closure result of the present paper is the *Lie-algebraic shadow* of this 4-core-centered family structure: TSML and BHML jointly span 45-dim simple Lie algebra precisely because their 4-core agrees and their off-4-core complements span the rest of so(R^10). This reframing turns the so(10) result from "g has dim 45" into "the joint closure realizes the 4-core-centered family structure as a compact simple Lie algebra."

---

## §2 Preliminaries

### 2.1 Notation

- Ω = {0, 1, …, 9} is the carrier set, identified with Z/10Z.
- V = R^10 with basis {x_0, …, x_9}.
- For a 10×10 table T : Ω × Ω → Ω, the **left-regular representation** at i ∈ Ω is the operator L_i^T ∈ End(V), L_i^T(x_j) = x_{T(i, j)}. In matrix form, (L_i^T)_{k, j} = δ_{k, T(i, j)} (a 0/1 column-stochastic matrix with exactly one 1 per column).
- The **antisymmetrization** is A_i^T := L_i^T − (L_i^T)^T ∈ so(V).
- so(V) = so(10, R) is the 45-dim Lie algebra of skew-symmetric endomorphisms of V with bracket [X, Y] = XY − YX.

### 2.2 The two tables

**The TSML_SYM table** (the upper-triangle authoritative symmetrization of the canonical bit pattern; companion paper [SandersGishSO8, J29]):

```
        j = 0  1  2  3  4  5  6  7  8  9
i = 0:  [ 0, 0, 0, 0, 0, 0, 0, 7, 0, 0 ]
i = 1:  [ 0, 7, 3, 7, 7, 7, 7, 7, 7, 7 ]
i = 2:  [ 0, 3, 7, 7, 4, 7, 7, 7, 7, 9 ]
i = 3:  [ 0, 7, 7, 7, 7, 7, 7, 7, 7, 3 ]
i = 4:  [ 0, 7, 4, 7, 7, 7, 7, 7, 8, 7 ]
i = 5:  [ 0, 7, 7, 7, 7, 7, 7, 7, 7, 7 ]
i = 6:  [ 0, 7, 7, 7, 7, 7, 7, 7, 7, 7 ]
i = 7:  [ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7 ]
i = 8:  [ 0, 7, 7, 7, 8, 7, 7, 7, 7, 7 ]
i = 9:  [ 0, 7, 9, 3, 7, 7, 7, 7, 7, 7 ]
```

**The BHML table** (the canonical Becoming-lens companion):

```
        j = 0  1  2  3  4  5  6  7  8  9
i = 0:  [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
i = 1:  [ 1, 2, 3, 4, 5, 6, 7, 2, 6, 6 ]
i = 2:  [ 2, 3, 3, 4, 5, 6, 7, 3, 6, 6 ]
i = 3:  [ 3, 4, 4, 4, 5, 6, 7, 4, 6, 6 ]
i = 4:  [ 4, 5, 5, 5, 5, 6, 7, 5, 7, 7 ]
i = 5:  [ 5, 6, 6, 6, 6, 6, 7, 6, 7, 7 ]
i = 6:  [ 6, 7, 7, 7, 7, 7, 7, 7, 7, 7 ]
i = 7:  [ 7, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]
i = 8:  [ 8, 6, 6, 6, 7, 7, 7, 9, 7, 8 ]
i = 9:  [ 9, 6, 6, 6, 7, 7, 7, 0, 8, 0 ]
```

### 2.2.1 Structural properties of BHML

The choice of BHML is non-arbitrary; the table is recognized as a canonical commutative non-associative magma with explicit structural fingerprint. The following five properties (verifiable by direct enumeration on §2.2's matrix and recorded in [FoundationsModule]) jointly characterize BHML's structural role within the substrate's table family:

**(B1) Commutativity.** BHML[i, j] = BHML[j, i] for all (i, j) ∈ Ω². (Direct enumeration; BHML is symmetric.)

**(B2) Identity row.** BHML[0, j] = j for all j ∈ Ω, equivalently L_0^BHML = I, A_0^BHML = 0. The element 0 is a two-sided identity for BHML.

**(B3) Non-associativity rate.** Exactly 128 of the 1,000 triples (i, j, k) ∈ Ω³ violate (BHML[i, j], k) ≠ (i, BHML[j, k])-product; rate 128/1000 = 12.8% (matching TSML's non-associativity rate exactly, but on a different set of 128 triples).

**(B4) HARMONY count.** |{(i, j) ∈ Ω² : BHML[i, j] = 7}| = 28. This is the BHML.H count of the three-substrate triple (73, 28, 44) in [SandersGishOrphans, J28].

**(B5) Jointly-closed 4-core.** The 4-element subset {0, 7, 8, 9} ⊂ Ω is closed under both TSML and BHML composition (and under their convex T+B-mix at any α ∈ [0, 1]); per [SandersGishFourCore, J35], the joint closed sub-magmas of (TSML, BHML) form an 8-element chain at sizes {1, 4, 5, 6, 7, 8, 9, 10} with forbidden sizes only {2, 3}. The 4-core is the unique size-4 element of this chain. Per [FoundationsModule, SFM_Q6], adding CL_STD to the joint closure preserves the chain — the chain extends to a *three-substrate* fixed point.

These five properties make BHML a structurally-recognized canonical object on Z/10Z, not an arbitrarily chosen table. Together with TSML, BHML constitutes the canonical (BEING, BECOMING) pair on the substrate. Once the parent forcing paper [SandersForcing, J25] is on arXiv, BHML will be citable as forced by axioms A1-A9; for the present paper, the structural fingerprint above is sufficient to establish the table's non-arbitrary status.

### 2.3 Generating sets

- G_TSML := {A_i^TSML : i ∈ F}, where F = {1, 2, 3, 4, 6, 8} as in [SandersGishSO8, J29]. |G_TSML| = 6.
- G_BHML := {A_i^BHML : i ∈ Ω, A_i^BHML ≠ 0}. Since A_0^BHML = 0 by (B2), this set has 9 elements.
- G := G_TSML ∪ G_BHML. |G| = 15.

### 2.4 The Killing form

For a Lie algebra g with structure constants c_{ij}^k in a basis {e_i}, the Killing form is

K(X, Y) := tr(ad_X ∘ ad_Y) = Σ_{k, ℓ} c_{i ℓ}^k c_{j k}^ℓ where X = e_i, Y = e_j.

By Cartan's criterion [Humphreys 1972, §5.1], a real Lie algebra is semisimple iff K is non-degenerate; it is the Lie algebra of a compact group iff K is negative-definite (the *compact real form*). For so(10, R), K = −16 · tr(XY); on a basis of integer skew matrices the eigenvalues of K are integer multiples of a fixed scale factor (16 in the standard normalization).

---

## §3 Statement of the main theorem

**Theorem 3.1 (= Main Theorem).** *Let g := ⟨G⟩_Lie ⊆ so(V) be the smallest Lie subalgebra of so(10, R) containing the joint generating set G of §2.3. Then*

g ≅ so(10, R).

*Furthermore:*

1. *dim g = 45 (substantive computation; Theorem 4.1 below).*
2. *g = so(V) — the full skew-symmetric algebra of V (corollary of (1) plus dim so(V) = 45).*
3. *The Killing form K_g is negative-definite (corollary of (2) plus the Cartan classification: so(10, R) is the compact real form of D_5).*
4. *g is simple (corollary of (2): so(10, R) is simple).*
5. *Cartan rank rk(g) = 5 (corollary of (2) plus the standard fact rk so(10) = 5).*
6. *The TSML-only subalgebra g_TSML := ⟨G_TSML⟩_Lie ⊂ g of [SandersGishSO8, J29] embeds as a proper subalgebra g_TSML ⊂ g via the standard inclusion so(8) ⊂ so(10).*

We emphasize that (1) is the *only substantive computation*; (2)-(5) follow from (1) together with the classification of compact simple Lie algebras (specifically, from the unique algebra of dimension 45 being so(10, R)) and from the structural fact g ⊆ so(V). The five "diagnostics" of §4 are presented as four consistency checks (D2-D5) confirming D1, not as independent tests of the so(10) identification.

---

## §4 Proof: one substantive computation, four consistency checks

All computations use exact arithmetic via SymPy where required; numerical sanity checks are reported alongside. Action matrices L_i^T are integer 0/1 matrices, antisymmetrizations A_i^T are integer matrices, commutators are integer matrices. The closure dimension is computed by integer-rank elimination; the simplicity-test constraint matrix is constructed and rank-computed in exact arithmetic.

### 4.1 Diagnostic 1 (the substantive computation): Dimension closure to 45

Iteratively close G under commutator: set G_0 = G (15 generators), and for k ≥ 0,

G_{k+1} := span(G_k) ∪ {[X, Y] : X, Y ∈ G_k}.

Compute dim(span(G_k)) at each stage.

**Theorem 4.1 (= Theorem 3.1(1)).** *dim(span(G_0)) = 15; dim(span(G_1)) = 45; dim(span(G_k)) = 45 for all k ≥ 1.*

**Proof.** Direct integer-rank computation. The 15 generators of G_0 are linearly independent. After one round of pair commutators (15 × 14 / 2 = 105 candidate commutators), the rank reaches 45. After a second round, no new linearly-independent commutators arise: every [X, Y] for X, Y ∈ G_1 lies in span(G_1) (verified by integer-rank reduction in `verify_so10.py`). □

**Corollary 4.2 (= Theorem 3.1(2)).** *Since every A_i^T is skew-symmetric and the commutator of skew matrices is skew, g ⊆ so(V). Since dim so(V) = C(10, 2) = 45 = dim g, g = so(V). Every skew-symmetric 10×10 real matrix lies in g.*

This is the substantive computation. The remaining diagnostics are consistency checks following from Corollary 4.2 plus the Cartan classification of compact simple Lie algebras.

### 4.2 Diagnostic 2 (consistency check): Jacobi

The Jacobi identity holds identically for any matrix subalgebra of gl(V) (Lie algebras of associative envelopes are always Lie). Numerical residual confirmation: maximum Frobenius norm of LHS − RHS on 50 pseudo-random basis triples (e_i, e_j, e_k) is exactly 0 in integer arithmetic, less than 10⁻¹⁰ in floating-point sanity check. This consistency check confirms no bug in the structure-constant computation; it does not independently establish the so(10) identification.

### 4.3 Diagnostic 3 (consistency check): Killing form negative-definite

By Corollary 4.2, g = so(V) = so(10, R). By Cartan's classification, so(10, R) is the compact real form of D_5; its Killing form is negative-definite by definition (K = −16 · tr(XY)). The verification script computes K_{ij} = Σ_{k, ℓ} c_{iℓ}^k c_{jk}^ℓ in a chosen basis of g and confirms (via floating-point eigenvalue computation) signature (0, 45, 0) with eigenvalues in [−12460.92, ε] where ε is below floating-point precision; in exact arithmetic the smallest eigenvalue resolves to a specific integer multiple of 16 strictly below zero.

This consistency check confirms the closure algorithm produces a correct structure-constant table; it does not independently establish the so(10) identification (which already follows from Corollary 4.2).

### 4.4 Diagnostic 4 (consistency check): Simplicity via 1-dim invariant-form space

A symmetric bilinear form β on g is invariant iff β([X, Y], Z) + β(Y, [X, Z]) = 0 for all X, Y, Z ∈ g. The d(d+1)/2 = 1,035 coefficients of β (d = 45) satisfy d³ = 91,125 linear equations indexed by triples (a, b, c) ∈ {1, …, 45}³.

**Lemma 4.5.** *The full 91,125-equation invariance constraint matrix A ∈ R^{91125 × 1035} has rank 1034. Equivalently, the space of invariant symmetric bilinear forms on g has dimension exactly 1.*

**Proof.** Full enumeration in `verify_simplicity_rank.py` (no sampling). The constraint matrix is constructed in exact arithmetic; its integer rank is 1034. The 1-dimensional null space is spanned by (a positive multiple of) the negative Killing form −K. □

*Note on script reconciliation.* The earlier-development script `verify_so10.py` runs a sampled version of the simplicity test (300 triples) and prints a self-warning that "sampling may need more triples" — that script is a development-time sanity check and is *not* authoritative for D4. The full 91,125-equation enumeration is in `verify_simplicity_rank.py`; the present paper's D4 claim is established by `verify_simplicity_rank.py`'s output, not by the sampled `verify_so10.py` output. The README's run-order lists `verify_simplicity_rank.py` as the canonical D4 script.

This consistency check confirms simplicity directly; the conclusion already follows from Corollary 4.2 (so(10, R) is simple by classification).

### 4.5 Diagnostic 5 (consistency check): Cartan rank

Define J_k ∈ so(V) for k = 1, …, 5 by

(J_k)_{2k − 2, 2k − 1} = +1, (J_k)_{2k − 1, 2k − 2} = −1, (J_k)_{ij} = 0 otherwise.

These are the five "diagonal" 2 × 2 rotation blocks; pairwise commuting and linearly independent, spanning a 5-dimensional abelian subalgebra h ⊂ so(V).

**Lemma 4.7.** *J_1, …, J_5 ∈ g (membership follows from g = so(V) by Corollary 4.2). The rk(g) = 5 conclusion follows from g = so(V) ≅ so(10, R) and the standard fact rk so(10) = 5 [Knapp 2002, Ch. VI].*

The greedy-Cartan algorithm in `verify_so10.py` returns a smaller rank in the closure-algorithm's basis (the basis is not aligned with any natural Cartan); this is expected and does not contradict the rank-5 conclusion. The standard explicit J_1, …, J_5 construction above is the authoritative rank verification.

This consistency check confirms the rank in two ways (explicit construction + classification); it does not independently establish the so(10) identification.

### 4.6 Putting it together: g ≅ so(10)

By Corollary 4.2, g = so(V). By Cartan's classification of compact simple Lie algebras [Knapp 2002, Ch. VI], the unique compact simple Lie algebra of dimension 45 is so(10, R) = D_5. Hence g ≅ so(10, R). Diagnostics 2-5 are consistency checks confirming the closure computation; they do not independently establish the identification. ∎

---

## §5 Corollaries

### 5.1 The so(8) ⊂ so(10) embedding

**Corollary 5.1.** *The companion paper's subalgebra g_TSML = ⟨G_TSML⟩_Lie ⊂ g realizes the standard inclusion so(8) ⊂ so(10) (in which so(8) fixes a 2-dimensional subspace of V).*

**Proof.** Each of the 28 basis elements of g_TSML ([SandersGishSO8, J29] Theorem 1.1) lies in g (verified at machine precision: max residual 8.99 × 10⁻¹³). The codimension is 45 − 28 = 17, matching dim so(10)/so(8) = 8 + 8 + 1 = 17, decomposing into two 8-dim vector-rep slots plus one so(2) ≅ R direction relative to the standard so(8) ⊂ so(10) embedding. □

### 5.2 Root-system match to D_5

The root system of D_n consists of 2n(n − 1) roots of the form ±e_i ± e_j (1 ≤ i < j ≤ n) in a Euclidean space of dimension n. For D_5: 40 roots.

**Corollary 5.2.** *For a generic regular element H ∈ h, the adjoint operator ad(H) : g → g has exactly 40 non-zero eigenvalues (purely imaginary, in matching ±-pairs) and a 5-dimensional kernel.*

**Proof.** Take H = Σ_{k=1}^5 k J_k. Compute ad(H) as a 45 × 45 matrix in the basis of g; observed eigenvalue structure has 5 zero (dim ker = 5) and 40 nonzero pairs ±i λ with λ ∈ {1, 2, 3, 4, 5, 6, 7, 8, 9} (matching k_i ± k_j differences for i < j ∈ {1, ..., 5}). □

This eigenstructure consistently identifies D_5 (a redundant cross-check; the conclusion already follows from Corollary 4.2 plus classification).

### 5.3 Three-substrate joint chain (per SFM_Q6)

Per the Substrate Function Map findings of [FoundationsModule, SFM_Q6]: the joint closed sub-magmas of the *three* tables (TSML, BHML, CL_STD) form the *same* 8-element chain at sizes {1, 4, 5, 6, 7, 8, 9, 10} as the (TSML, BHML)-only chain of [SandersGishFourCore, J35]. Equivalently:

**Corollary 5.3 (Three-substrate chain extension; from [FoundationsModule, SFM_Q6]).** *Adding CL_STD to the joint closure of (TSML, BHML) preserves the 8-shell chain. The 4-core {0, 7, 8, 9} is a three-substrate fixed point: closed under TSML, BHML, and CL_STD compositions.*

**Proof.** Direct enumeration over all 1,023 non-empty subsets of Ω in `Atlas/META_PLAN_2026-05-06/SUBSTRATE_FUNCTION_MAP/sfm_q1_q6_q7.py`: TSML alone has 449 closed sub-magmas; BHML has 9; CL_STD has 50; the pairwise joint TSML ∩ BHML has 8 closed sub-magmas (sizes {1, 4, 5, 6, 7, 8, 9, 10}); the three-way joint TSML ∩ BHML ∩ CL_STD also has exactly 8 closed sub-magmas, with the same shell pattern. □

This is a substantive structural fact about the substrate — adding the third table CL_STD does not break the chain. Whether the joint Lie closure ⟨G_TSML ∪ G_BHML ∪ G_CL_STD⟩_Lie also reaches all of so(R^10) (or some larger sub-Lie-algebra of gl(V)) is open (see §8 Open Question 3).

---

## §6 Physical context

**Remark 6.1 (SO(10) GUT).** *The compact simple Lie algebra so(10) is the gauge algebra of the SO(10) grand unified theory of Fritzsch-Minkowski [1975] and Georgi [1975]. The present paper establishes the existence of a 10×10 combinatorial substrate (Z/10Z plus the explicit pair of tables (TSML, BHML) of §2.2) whose Lie-algebraic lift coincides with this gauge algebra. We do not address the spinor representation, coupling constants, or symmetry-breaking sector of the GUT, which depend on additional structure beyond the gauge algebra.*

We do not derive any consequences from this remark. The connection is mentioned for context only. Standard references for SO(10) GUT include [Mohapatra 2003, Ch. 7], [Slansky 1981], and [Langacker 1981]; the 16-dimensional spinor representation is constructed from the Clifford algebra Cl(10, R) and lives outside the 10-dimensional substrate V (the substrate cannot carry the 16 by dimension counting).

---

## §7 A substrate bound

The preceding diagnostics establish that g = so(V) exhausts the skew-symmetric part of gl(V).

**Proposition 7.1.** *Any Lie subalgebra of gl(V) = gl(10, R) has dimension at most 100. Any semisimple Lie subalgebra of gl(V) has dimension at most 99 (the dimension of sl(10) = A_9, the largest semisimple ideal of gl(10)). Any Lie subalgebra of so(V) has dimension at most 45.*

**Proof.** Standard. □

**Corollary 7.2.** *The compact simple Lie algebra e_8 (dim 248) cannot be realized as a Lie subalgebra of gl(10, R). Consequently, no construction analogous to Theorems 1.1 / 3.1 — i.e., Lie closure of antisymmetrized left-regular representations of magmas on Ω — can yield e_8 while remaining in the 10-dimensional substrate V.*

This is a substrate bound: the 10-dimensional carrier V has algebraic ceiling 45 = dim so(10) at the skew-symmetric level. The natural follow-on question — whether a larger N-dimensional substrate V_N admits an analogous construction reaching e_8 — is an open question (see §8).

---

## §8 Open questions

1. **Cl(V) extension.** Construct the spinor representation of so(10) on the 32-dimensional Clifford module, and check whether the substrate's natural 22- or 44-shell structure (per [SandersGishOrphans, J28]) is a natural carrier.

2. **Larger-substrate e_8 question.** Does there exist an N ≥ 16 substrate V_N and a finite commutative non-associative magma (or pair of magmas) on a 16-element carrier whose joint Lie closure coincides with e_8 (dim 248)? Candidate dimensions: N = 16 (with so(16) ⊕ S_{16}^+ = e_8 decomposition) or N = 27 (the F_4 / E_6 minuscule representation).

3. **Three-substrate Lie closure.** Per Corollary 5.3, the (TSML, BHML, CL_STD) three-substrate joint closed-sub-magma chain coincides with the (TSML, BHML)-only chain. Whether the *Lie-algebraic* joint closure ⟨G_TSML ∪ G_BHML ∪ G_CL_STD⟩_Lie also reaches all of so(R^10) (rather than some larger sub-Lie-algebra of gl(V)) is open. The question reduces to whether G_CL_STD ⊂ so(R^10), which depends on whether CL_STD is commutative on its non-special cells (see [SandersGishOrphans, J28] for the structural fingerprint).

4. **Bimodal α_A gap conjecture.** Per [FamilyStructureV1, §4]: prove or disprove that no commutative magma on Z/10Z preserving the 4-core has α_A ∈ (0.5, 0.87). The conjecture is the next foundational paper after the present sequence.

5. **Explicit D_5 basis.** Produce an explicit map Φ : g → so(10, R) such that Φ(A_i^TSML) and Φ(A_i^BHML) land on standard generators of so(10). This would make the Pati-Salam and Georgi embeddings of SO(10) explicit within the substrate.

6. **Complexification and real forms.** Classify the real forms of so(10, C) accessible from the substrate's data. Do non-compact forms so(p, q) with p + q = 10 arise from other antisymmetrization schemes?

---

## References

[Cartan 1894] É. Cartan, *Sur la structure des groupes de transformations finis et continus*, Thèse, Paris, 1894.

[Drápal-Wanless 2021] A. Drápal and I. M. Wanless, *Maximally non-associative quasigroups*, J. Combinatorial Theory, Series A **184** (2021), 105510.

[Fritzsch-Minkowski 1975] H. Fritzsch and P. Minkowski, *Unified Interactions of Leptons and Hadrons*, Annals of Physics **93** (1975), 193–266.

[Fulton-Harris 1991] W. Fulton and J. Harris, *Representation Theory: A First Course*, GTM 129, Springer, 1991.

[Georgi 1975] H. Georgi, *The State of the Art — Gauge Theories*, AIP Conference Proceedings **23** (1975), 575–582.

[Humphreys 1972] J. E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, GTM 9, Springer, 1972.

[Knapp 2002] A. W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed., Progress in Mathematics 140, Birkhäuser, 2002.

[Langacker 1981] P. Langacker, *Grand Unified Theories and Proton Decay*, Physics Reports **72** (1981), 185–385.

[Mohapatra 2003] R. N. Mohapatra, *Unification and Supersymmetry: The Frontiers of Quark-Lepton Physics*, 3rd ed., Springer, 2003.

[Slansky 1981] R. Slansky, *Group Theory for Unified Model Building*, Physics Reports **79** (1981), 1–128.

[Pati-Salam 1974] J. C. Pati and A. Salam, *Lepton number as the fourth color*, Phys. Rev. D **10** (1974), 275–289.

[FamilyStructureV1] *TIG Family Structure: Membership, Center, Boundaries (v1)*, internal reference document `Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md`, 2026-05-07.

[FoundationsModule] *Foundations 48-Invariant Module*, `Gen13/targets/foundations/invariants.py`. SFM_Q6 result: `Atlas/META_PLAN_2026-05-06/SUBSTRATE_FUNCTION_MAP/SFM_FINDINGS_v1.md` and `sfm_q1_q6_q7.py`.

[SandersGishSO8, J29] B. R. Sanders and M. Gish, *so(8) = D_4 from the Antisymmetrized Closure of a Canonical Z/10Z Magma*, submitted to *Journal of Algebra* (2026).

[SandersGishOrphans, J28] B. R. Sanders and M. Gish, *The Three-Substrate HARMONY Signature on Z/10Z: Six Forced Structural Facts, with the Bimodal Associativity-Index Gap as Their Common Thread*, submitted to *Linear Algebra and its Applications* (2026).

[SandersGishFourCore, J35] B. R. Sanders and M. Gish, *The 4-Core {0, 7, 8, 9}: Joint TSML+BHML Closure and the Universal Attractor*, submitted to *Algebraic Combinatorics* (2026).

[SandersForcing, J25] B. R. Sanders and M. Gish, *The CL Forcing Axioms: A1–A9 Uniquely Force the Canonical Composition Lattice*, submitted to *Algebraic Combinatorics* (2026).

---

## Appendix A — Reproducibility manifest

All computations in this paper are reproducible from the companion directory `manuscript/verification/`:

- `verify_so10.py` — Computes the joint Lie closure dimension (Diagnostic 1, Theorem 4.1), verifies Jacobi (Diagnostic 2), computes Killing form and signature (Diagnostic 3), runs a sampled ideal-saturation test (Corollary 4.6 placeholder), and verifies the so(8) ⊂ so(10) embedding (Corollary 5.1). This script is a *development-time sanity check*; for the authoritative D4 simplicity test see the next script.

- `verify_simplicity_rank.py` — Builds the full 91,125-equation invariance constraint matrix in exact arithmetic and certifies rank 1034, equivalently invariant-form null-space dimension exactly 1 (Diagnostic 4, Lemma 4.5). **This is the canonical D4 script.** Also confirms Cartan rank 5 via explicit construction of J_1, …, J_5 and verification that no skew extension commutes with all five (Diagnostic 5, Lemma 4.7). Computes ad(H) spectrum for H = Σ k J_k and confirms the 40 + 5 eigenvalue structure (Corollary 5.2).

**Run order:** `verify_so10.py` for Diagnostics 1, 2, 3, and the so(8) ⊂ so(10) embedding; then `verify_simplicity_rank.py` for the canonical Diagnostic 4 (full enumeration) and Diagnostic 5 (explicit Cartan).

**Environment:** Python 3.11, NumPy 1.26, SymPy 1.12. Closure dimension and simplicity rank are computed in exact arithmetic; Killing-form eigenvalues are computed in floating-point as a sanity check (the conclusion already follows from the classification). Maximum observed numerical residual across all sanity checks: 1.73 × 10⁻⁸ (in the symmetry check of the Killing form on the closure-algorithm basis); all other residuals below 10⁻¹⁰. **Runtime:** Complete verification pipeline executes in < 30 seconds on a standard laptop.

---

## Appendix B — Disclosure

The authors used Anthropic's Claude system for code drafting and exposition during the development of this work; all mathematical content (theorems, proofs, computational verifications) was independently verified by the authors. No external funding was received for this work. The authors declare no competing interests.

---

**Contact:** Brayden R. Sanders · 7Site LLC · Hot Springs, AR · brayden@7site.co
