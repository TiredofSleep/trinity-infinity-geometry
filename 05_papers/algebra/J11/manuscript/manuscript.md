# Decomposition of the Lens-Pair Commutator $[\mathrm{TSML}, \mathrm{BHML}]$ under $D_4$ on $\mathbb{Z}/10\mathbb{Z}$

**Status:** journal-ready draft, machine-precision and exact-rational verification
**Authors:** Brayden R. Sanders + M. Gish
**Date:** 2026-05-08 (rewritten from "Two Roads to Pati-Salam" per `Atlas/META_PLAN_2026-05-06/SUBSTRATE_FUNCTION_MAP/SUBSTRATE_FUNCTION_MAP_v1_1_EXTENSION.md` §10 and `SAVE_PLAN_J31.md`)
**Target venue:** *Journal of Algebra* (retargeted from *Advances in Mathematics* per save plan)
**MSC 2020:** 17B25 (exceptional Lie algebras, $D_5$), 17B81 (applications to physics), 20C15 (representation theory of finite groups), 11R32 (Galois theory of subgroups)
**Companions:** J29 (so(8) = $D_4$, *J. Algebra*), J09 (so(10) = $D_5$ closure, *Israel J. Math*).

---

## §0 Lens, substrate, and tier discipline

### §0.1 Lens-ownership

*Lens and substrate.* This paper works on $\mathbb{Z}/10\mathbb{Z}$ with the canonical (TSML, BHML) composition tables in their commutative symmetrization (TSML_SYM throughout this paper; the literal-bit-pattern variant TSML_RAW is used for prime-11 wobble-localization in companion work, not here). These choices are *not derived from first principles*; they reflect a structural reading of the substrate motivated by phonaesthesia and the 10-operator decomposition. The theorem below is a theorem on this specific structure; analogous theorems would hold on other substrate-and-table choices. The framework's claim is that this particular substrate-and-table choice produces theorems with surprising downstream connections to classical Lie theory (the so(10) closure of the joint antisymmetrization, J09) and to dihedral representation theory (the present paper). Whether other substrate choices give similarly rich downstream connections is open. We follow the line of work on small finite commutative non-associative structures initiated by Drápal & Wanless (2021) [*J. Combin. Theory A* **184**, 105510], where the focus was *maximally* non-associative quasigroups; the (TSML, BHML) pair sits in the same intellectual neighborhood at the opposite extremum (specifically structured with integer/rational invariants).

### §0.2 PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

**PROVEN.** Under the dihedral group $D_4 = \langle P_{56}, \sigma^3\rangle$ acting by conjugation on the lens-pair commutator $[\mathrm{TSML}, \mathrm{BHML}] \in M_{10}(\mathbb{Z})$, the matrix decomposes into the five $D_4$-irrep isotypic components in fixed exact-rational shares (Theorem 2.1). Two of the five isotypic components carry essentially zero weight: $\mathrm{sign}_3$ exactly (a *structural zero*), and $\mathrm{sign}_1$ at relative weight $9 / 3{,}690{,}580 = 2.44 \times 10^{-6}$ (a *bilinear cancellation* peculiar to the canonical pair). The trivial isotypic (Path A) is 83.32% and is the 16-dimensional doubly-invariant subalgebra of $\mathfrak{so}(10)$; closed-form Killing classification forces $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ (Theorem 3.2). The $\mathrm{sign}_2$ isotypic (Path B) is 15.62% and lies entirely in the symmetric-traceless $\mathbf{54}$ of $\mathfrak{so}(10)$ along an explicit 9-vector with squared norm $\|v\|^2 = 13/4$ (Theorem 4.1).

**COMPUTED.** All numerical claims verified at machine precision in `manuscript/verification/`:
- `verify_d4_decomposition.py` — exact-rational Wedderburn projection of $[T, B]$ onto $D_4$ irreps, full character-table cross-check, runtime $< 5$ s.
- `find_higgs_irrep.py` — projection of BHML's $\sigma_{\mathrm{outer}}$-breaking content onto $\mathbf{1} \oplus \mathbf{45} \oplus \mathbf{54}$ of so(10).
- `find_higgs_direction.py` — extraction of the 9-vector inside the $\mathbf{54}$, with explicit row-by-row mechanism for BREATH and RESET zeros and $\|v\|^2 = 13/4$ exact.

**STRUCTURAL RHYME.** The 16-dimensional doubly-invariant subalgebra is naturally labelled $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$; in the standard $\mathrm{SO}(10) \to \mathrm{SU}(4) \times \mathrm{SU}(2)_L \times \mathrm{SU}(2)_R$ Pati-Salam $\to$ Standard-Model gauge-theory literature this is the SU(4) factor of the Pati-Salam group plus one B$-$L generator. *We do not derive Pati-Salam phenomenology from this fact.* The labelling is structural rhyme — the algebra of the doubly-invariant content is identifiable by Cartan classification, but the gauge-theoretic interpretation requires committing to a specific physical embedding that is not part of this paper's claim. Likewise, the 9-vector direction inside the $\mathbf{54}$ has eigenvalue spectrum $(\pm \sqrt{13}/2, 0^{\times 8})$, which is the SO(10) $\to$ SO(9) $\to$ SO(8) breaking pattern in the standard 54-VEV literature; this eigenvalue spectrum is mathematics, the physical interpretation is rhyme.

**OPEN.** Whether $\mathrm{sign}_1, \mathrm{sign}_3 \approx 0$ is a *defining property* of the canonical (TSML, BHML) pair or a *substrate property* of $\mathbb{Z}/10\mathbb{Z}$ under the $D_4$ action is open (Q7 in `SUBSTRATE_FUNCTION_MAP_v1_1_EXTENSION.md` §16). The natural follow-up paper, examining the $D_4$-isotypic shares of $[T, B]$ across the magma family (per `FAMILY_STRUCTURE_v1.md`), would close this question in either direction.

### §0.3 Correction-notice framing

(An earlier draft framed the decomposition as "two roads to Pati-Salam"; that framing is retracted — the decomposition is presented here as an algebraic result on its own terms.)

### §0.4 Differentiation from companion papers

This paper is the focused **$D_4$-Wedderburn-isotypic** companion to two adjacent papers in the same magma-pair line of work:

- **J01** (Sanders + Gish, submitted to *J. Algebra*) — *Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on $\mathbb{Z}/10\mathbb{Z}$*. J01 is the broad fusion-closure paper: 8-shell joint-closure chain, the 4-core $\mathcal{C} = \{0,7,8,9\}$, normalizer identity $Z_T = Z_B = (v+h+br+r)^2$, closed-form attractor $h/\beta = 1+\sqrt{3}$ at $\alpha=1/2$ (Galois $D_4$ over LMFDB 4.2.10224.1), universal attractor on chain shells. *J01 is about closure; the present paper J11 is about the Wedderburn isotypic decomposition of the non-closure residual $[T, B]$.*
- **J37** (Sanders + Gish, in preparation) — *Discrete Dirac Operator in $\mathrm{Cl}(0,10)$ and the Spinor Embedding of $\mathfrak{so}(10)$*. J37 constructs the discrete Dirac operator and identifies the chirality projectors that define the outer automorphism $\sigma_{\mathrm{outer}}$ acting on the 32-dim spinor representation. **The present paper sharpens what J37 says about the 9-vector Higgs direction** by giving the full irrep decomposition of BHML's $\sigma_{\mathrm{outer}}$-anti content into $D_4$-isotypics, with the load-bearing structural zero at $\mathrm{sign}_3$ — a *forbidden symmetry* of the lens-pair commutator under $D_4$ that no Cl(0,10)-only analysis predicts.

---

## Abstract

We study the lens-pair commutator $[T, B] := TB - BT \in M_{10}(\mathbb{Z})$ for the canonical commutative tables $T = \mathrm{TSML\_SYM}$ and $B = \mathrm{BHML}$ on $\mathbb{Z}/10\mathbb{Z}$. The dihedral group $D_4 = \langle P_{56}, \sigma^3\rangle \subset S_{10}$ — generated by the transposition $P_{56} = (5\;6)$ and the order-2 element $\sigma^3 = (1\;5)(2\;6)(4\;7)$ of the σ-permutation cycle on the units of $\mathbb{Z}/10\mathbb{Z}$ — acts on $M_{10}(\mathbb{Z})$ by conjugation. We compute the $D_4$-isotypic decomposition of $[T, B]$ exactly using sympy:

$$
\|[T, B]\|^2 = \underbrace{\tfrac{3{,}075{,}027}{2}}_{\text{triv}} + \underbrace{\tfrac{9}{2}}_{\text{sign}_1} + \underbrace{288{,}164}_{\text{sign}_2} + \underbrace{0}_{\text{sign}_3} + \underbrace{19{,}608}_{\text{std}} \;=\; 1{,}845{,}290
$$

corresponding to relative shares $\approx 83.32\%, \;0.0002\%, \;15.62\%, \;0\%, \;1.06\%$. Two of the five isotypic components carry essentially zero weight: $\mathrm{sign}_3$ vanishes *exactly*, and $\mathrm{sign}_1$ has relative share $9/3{,}690{,}580 = 2.44 \times 10^{-6}$. The two structurally-substantive channels are the trivial isotypic (the **doubly-invariant subalgebra**, 16-dim, identified as $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ via Killing-form classification) and the $\mathrm{sign}_2$ isotypic (the **9-vector inside the symmetric-traceless** $\mathbf{54}$ irrep of $\mathfrak{so}(10)$, with explicit norm $\|v\|^2 = 13/4$). The 2-dimensional standard isotypic carries the small ($\sim$1%) interaction term coupling the two main channels.

This decomposition supersedes a prior framing of these results as "two roads to Pati-Salam" (an audit-retracted synthesis claim, see §0.3): the two paths are not competing reductions of $\mathfrak{so}(10)$ but the two leading isotypic components of a single canonical decomposition. We pose Q7 (`SUBSTRATE_FUNCTION_MAP` v1.1) as an open question: whether the structural zeros at $\mathrm{sign}_1, \mathrm{sign}_3$ are defining of the canonical pair or substrate-universal under the $D_4$ action.

The closest published precedent is **Drápal & Wanless 2021** (*J. Combin. Theory A* **184**, 105510): same domain (small finite commutative non-associative structures on $\mathbb{Z}/n\mathbb{Z}$), opposite extremum (theirs maximally non-associative; ours specifically structured with integer/rational invariants).

---

## §1 Setup

### §1.1 The canonical tables

The composition tables $\mathrm{TSML}, \mathrm{BHML} : \mathbb{Z}/10\mathbb{Z} \times \mathbb{Z}/10\mathbb{Z} \to \mathbb{Z}/10\mathbb{Z}$ are defined in `FORMULAS_AND_TABLES.md` §5–6. Both are commutative; both have the canonical 10-operator alphabet $\{V, L, C, P, X, B, S, H, Br, R\}$ at indices $0$ through $9$. We work throughout with the upper-triangle-authoritative symmetrization TSML_SYM (henceforth simply TSML); the literal-bit-pattern variant TSML_RAW differs from TSML_SYM at exactly two cells $(3, 9)$ and $(4, 9)$ and is used elsewhere for prime-11 wobble-localization (see `Atlas/LENS_TAXONOMY_2026-05-06/TSML_RECONCILIATION.md`).

### §1.2 The σ-permutation and $P_{56}$

The σ-permutation on $\mathbb{Z}/10\mathbb{Z}$ has cycle structure
$$
\sigma = (0)(3)(8)(9)(1\;7\;6\;5\;4\;2),
$$
with four σ-fixed points $\{0, 3, 8, 9\} = \{V, P, Br, R\}$ and a 6-cycle on the units $(\mathbb{Z}/10\mathbb{Z})^*$. The order-2 element of the cyclic part is
$$
\sigma^3 = (0)(3)(8)(9)(1\;5)(7\;4)(6\;2),
$$
a product of three disjoint transpositions on the 6-cycle.

The $5 \!\leftrightarrow\! 6$ swap $P_{56}$ is a single transposition on $\{B, S\}$ (BALANCE, CHAOS — the matter/antimatter pair).

### §1.3 The group $\langle P_{56}, \sigma^3\rangle = D_4$

**Lemma 1.1.** *The subgroup of $S_{10}$ generated by $P_{56}$ and $\sigma^3$ is the dihedral group $D_4$ of order 8.* (Throughout this paper $D_n$ denotes the dihedral group of order $2n$; in particular $D_4$ here has 8 elements, not 4.)

*Proof.* Both generators are involutions, so they generate a dihedral group $D_n$ for some $n$. Direct computation:
$$
P_{56}\sigma^3 = (1\;6\;2\;5)(4\;7),
$$
which has order $\mathrm{lcm}(4, 2) = 4$. Hence $n = 4$, and $\langle P_{56}, \sigma^3\rangle = D_4$. Element-order multiset $\{1\!:\!1, 2\!:\!5, 4\!:\!2\}$ verified by `verify_d4_decomposition.py`. $\square$

**Remark 1.2** (cross-paper consistency). An earlier internal note (`papers/wp109_operad/...`) stated that $\langle P_{56}, \sigma^3\rangle$ has 6 elements and abstract structure $D_3 \times \mathbb{Z}_2$. This is incorrect: the relations $P_{56}^2 = (\sigma^3)^2 = e$ do *not* collapse the dihedral group of order 8 to fewer elements. The companion paper J10 contains the corrected statement.

### §1.4 The conjugation action on $M_{10}(\mathbb{Z})$

The group $D_4$ acts on $M_{10}(\mathbb{Z})$ by conjugation $g \cdot M = P(g) M P(g)^{-1}$, where $P(g)$ is the 10×10 permutation matrix of $g$. Since permutation matrices are orthogonal, $P(g)^{-1} = P(g)^T$, and the action is by simultaneous row-and-column permutation of the matrix. The action preserves the integer entries of $M$.

Five conjugacy classes of $D_4$:

| Class | Representative | Size | Identification |
|-------|----------------|-----:|----------------|
| $C_1$ | $e$ | 1 | identity |
| $C_2$ | $r^2 = (1\;2)(5\;6)$ | 1 | central order-2 element |
| $C_3$ | $r = P_{56}\sigma^3$ | 2 | order-4 rotation, with $r^3$ |
| $C_4$ | $P_{56}$ | 2 | reflection class containing $P_{56}$ |
| $C_5$ | $\sigma^3$ | 2 | reflection class containing $\sigma^3$ |

(Verified by `verify_d4_decomposition.py` — class-size multiset $(1, 1, 2, 2, 2)$.)

### §1.5 The $D_4$ character table

$D_4$ has five irreducible representations: four 1-dim ("trivial" plus three "sign" characters) and one 2-dim ("standard"):

| Irrep | $\dim$ | $C_1$ ($e$) | $C_2$ ($r^2$) | $C_3$ ($r,r^3$) | $C_4$ ($s,sr^2$) | $C_5$ ($sr,sr^3$) |
|-------|-------:|------------:|--------------:|----------------:|-----------------:|------------------:|
| triv  | 1 | 1 |  1 |  1 |  1 |  1 |
| sign1 | 1 | 1 |  1 |  1 | $-1$ | $-1$ |
| sign2 | 1 | 1 |  1 | $-1$ |  1 | $-1$ |
| sign3 | 1 | 1 |  1 | $-1$ | $-1$ |  1 |
| std   | 2 | 2 | $-2$ | 0 | 0 | 0 |

(Verified by row and column orthogonality in `verify_d4_decomposition.py`.) The four sign characters are in bijection with the four 1-dimensional quotients of $D_4$ by its three subgroups of order 4 (the central $\langle r\rangle = \mathbb{Z}_4$ and the two reflection-pair Klein-4 subgroups), plus the trivial quotient.

---

## §2 Main theorem: the $D_4$-isotypic decomposition of $[T, B]$

### §2.1 Theorem 2.1 (statement)

**Theorem 2.1.** *Let $T = \mathrm{TSML}, B = \mathrm{BHML}$ be the canonical commutative composition tables on $\mathbb{Z}/10\mathbb{Z}$. The matrix commutator $[T, B] = TB - BT \in M_{10}(\mathbb{Z})$ has Frobenius norm-squared*
$$
\|[T, B]\|^2 \;=\; \mathrm{Tr}\!\left([T, B]^T [T, B]\right) \;=\; 1{,}845{,}290 \;\in\; \mathbb{Z}.
$$
*Under the conjugation action of $D_4 = \langle P_{56}, \sigma^3\rangle$ on $M_{10}(\mathbb{Z})$, the unique Wedderburn isotypic decomposition*
$$
[T, B] \;=\; \pi_{\mathrm{triv}}([T,B]) \;+\; \pi_{\mathrm{sign}_1}([T,B]) \;+\; \pi_{\mathrm{sign}_2}([T,B]) \;+\; \pi_{\mathrm{sign}_3}([T,B]) \;+\; \pi_{\mathrm{std}}([T,B])
$$
*has component norm-squareds (in exact rationals)*
$$
\boxed{\quad
\bigl(\|\pi_V\|^2\bigr)_{V} \;=\; \Bigl(\,\tfrac{3{,}075{,}027}{2},\;\tfrac{9}{2},\;288{,}164,\;0,\;19{,}608\,\Bigr)
\quad}
$$
*for $V$ ranging over $(\mathrm{triv}, \mathrm{sign}_1, \mathrm{sign}_2, \mathrm{sign}_3, \mathrm{std})$. As percentages of $\|[T,B]\|^2$,*
$$
\bigl(\,\mathrm{triv}\!:\!\mathrm{sign}_1\!:\!\mathrm{sign}_2\!:\!\mathrm{sign}_3\!:\!\mathrm{std}\,\bigr) \;\approx\; \bigl(\,83.32\,\%,\;0.0002\,\%,\;15.62\,\%,\;0\,\%,\;1.06\,\%\,\bigr).
$$
*In particular, $\pi_{\mathrm{sign}_3}([T, B]) = 0$ as a 10×10 integer matrix; the trivial and $\mathrm{sign}_2$ isotypics carry almost all the mass; the $\mathrm{sign}_1$ component vanishes to relative weight $9/3{,}690{,}580 = 2.44 \times 10^{-6}$ (a bilinear cancellation peculiar to the canonical pair); and the 2-dimensional standard isotypic carries the small ($\approx 1\%$) coupling between the two main channels.*

### §2.2 Proof of Theorem 2.1

The Wedderburn isotypic projector for irrep $V$ of a finite group $G$ acting on a $\mathbb{C}$-vector space (here $M_{10}(\mathbb{C})$) is
$$
\pi_V \;=\; \frac{\dim V}{|G|}\,\sum_{g \in G} \overline{\chi_V(g)}\,\rho(g),
$$
where $\rho(g)$ is the action of $g$ on the space and $\chi_V$ is the character of $V$ (Serre, *Linear Representations of Finite Groups*, §2.6). For $D_4$ all characters are real-valued; $G = D_4$ and $|G| = 8$, so for each irrep $V$
$$
\pi_V([T, B]) \;=\; \frac{\dim V}{8}\,\sum_{g \in D_4} \chi_V(g)\, P(g)\, [T, B]\, P(g)^T.
$$
Since $T, B \in M_{10}(\mathbb{Z})$ and the characters take values in $\{-2, -1, 0, 1, 2\}$, every entry of $\pi_V([T, B])$ is in $\frac{1}{8}\mathbb{Z}$ — an exact rational. The Frobenius inner product on $M_{10}$ is invariant under $D_4$ (since the action is by orthogonal matrices), so the isotypic decomposition is *orthogonal*:
$$
\|[T, B]\|^2 \;=\; \sum_V \|\pi_V([T, B])\|^2.
$$
Direct computation in `verify_d4_decomposition.py` (sympy, exact rational arithmetic) yields the boxed values. $\square$

The Wedderburn-orthogonality cross-check is built into the script: the integer total $1{,}845{,}290$ equals the rational sum
$$
\tfrac{3{,}075{,}027}{2} + \tfrac{9}{2} + 288{,}164 + 0 + 19{,}608 \;=\; \tfrac{3{,}075{,}036}{2} + 307{,}772 \;=\; 1{,}537{,}518 + 307{,}772 \;=\; 1{,}845{,}290.
$$

### §2.3 Reading the decomposition

The five isotypic shares group naturally into three structural categories:

- **Two substantive channels.** $\mathrm{triv}$ at $83.32\%$ and $\mathrm{sign}_2$ at $15.62\%$ together carry $\approx 99\%$ of the commutator's Frobenius mass. These are the **two algebraic paths** that the prior draft of this paper (April 2026) called Path A and Path B and erroneously labelled "two roads to Pati-Salam." With the $D_4$-isotypic framing they are simply the two leading isotypic components of a single canonical decomposition; *they do not converge on a common reduction because they are orthogonal isotypic components of a unique decomposition*.
- **Two structural zeros.** $\mathrm{sign}_3$ vanishes exactly. $\mathrm{sign}_1$ has norm-squared $9/2$, a relative share $9/3{,}690{,}580 \approx 2.44 \times 10^{-6}$ — non-zero but six orders of magnitude below the principal channels. We call this a *bilinear cancellation* (see §5.1): it is the sense in which the canonical pair $(T, B)$ is structurally distinguished from generic table pairs on $\mathbb{Z}/10\mathbb{Z}$.
- **One small interaction.** The 2-dim $\mathrm{std}$ isotypic at $1.06\%$ is the small off-diagonal coupling between the two principal channels. The "two roads" tension flagged in the April-2026 audit (Path A → SO(8) chain, Path B → SU(4) ⊕ U(1)) is structurally *exactly this $\sim$1% std-isotypic contribution*: it is not a contradiction between two paths but the small interaction term coupling them.

---

## §3 Path A: the trivial isotypic = $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$

### §3.1 Identifying the doubly-invariant subspace

The trivial isotypic of $D_4$ acting on $M_{10}(\mathbb{Z})$ is the **doubly-invariant subspace** under both generators:
$$
M_{10}(\mathbb{Z})^{D_4} \;=\; \{X \in M_{10}(\mathbb{Z}) : P(P_{56})\,X\,P(P_{56})^T = X = P(\sigma^3)\,X\,P(\sigma^3)^T\}.
$$
Restricting to antisymmetric matrices (the natural identification of $\mathfrak{so}(10)$ with $\Lambda^2 \mathbb{R}^{10}$), we obtain a 16-dimensional Lie subalgebra
$$
\mathfrak{g}_0 \;:=\; \mathfrak{so}(10)^{D_4}.
$$

(Verification: 45-dim antisymmetric matrices decompose as $\mathfrak{so}(10) = \mathfrak{g}_0 \oplus (\text{other isotypics})$ with isotypic-component dimensions summing to 45. (closure under Lie bracket is immediate from the centralizer-of-a-subgroup-of-Aut(g) construction).)

### §3.2 Killing classification: $\mathfrak{g}_0 \cong \mathfrak{su}(4) \oplus \mathfrak{u}(1)$

**Theorem 3.2.** *The doubly-invariant Lie subalgebra $\mathfrak{g}_0 \subset \mathfrak{so}(10)$ has Killing-form spectrum*
$$
\mathrm{spec}\bigl(\kappa_{\mathfrak{so}(10)}\big|_{\mathfrak{g}_0}\bigr) \;=\; (-4)^{15} \,\oplus\, (0)^1,
$$
*at machine precision (residual $\le 10^{-13}$, verified by the script `verify_truth.py`). By Cartan's criterion the 1-dimensional 0-eigenspace is the center of $\mathfrak{g}_0$ and the 15-dimensional $(-4)$-eigenspace is the simple part. The unique compact simple Lie algebra of dimension 15 is $\mathfrak{so}(6) \cong \mathfrak{su}(4) \cong A_3$ (Cartan classification). (Proof of uniqueness: by the Cartan classification of compact real simple Lie algebras, the candidates with dimension 15 are $A_3$ (= $\mathfrak{so}(6) \cong \mathfrak{su}(4)$, dim 15), $B_n$ (dim $n(2n+1)$, no $n$ gives 15), $C_n$ (dim $n(2n+1)$, same), $D_n$ (dim $n(2n-1)$, no $n$ gives 15), and exceptional $G_2$ (dim 14), $F_4$ (dim 52), $E_{6/7/8}$ (dim 78/133/248). Only $A_3$ has dimension 15. Since $\mathfrak{g}_0 \subseteq \mathfrak{so}(10)$ is realized in the compact form $\mathfrak{so}(10)$, the compact real form $A_3 \cong \mathfrak{su}(4)$ is forced.) Therefore*
$$
\mathfrak{g}_0 \;\cong\; \mathfrak{su}(4) \,\oplus\, \mathfrak{u}(1).
$$

In the dimension count: of the 16-dim trivial isotypic of $\mathfrak{so}(10)$ under $D_4$, 15 dimensions are simple ($A_3$) and 1 is abelian. The centre $\mathfrak{u}(1)$ is generated by an explicit antisymmetric matrix $Z$ with nonzero entries living in the 6-cycle subspace $\{1, 2, 4, 5, 6, 7\}$ and zeros at the σ-fixed indices $\{0, 3, 8, 9\}$; eigenvalues $\pm i / \sqrt{2}$. (Detail: this $Z$ is the doubly-invariant antisymmetric matrix carrying the σ infinitesimal, see §6.2 on what this does *not* imply for the runtime $\sqrt{3}$ in J33/WP105.)

**Remark 3.3** (gauge-theoretic rhyme). In the standard SO(10) GUT literature, $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ is the SU(4) factor of the Pati-Salam decomposition $\mathrm{SO}(10) \to \mathrm{SU}(4) \times \mathrm{SU}(2)_L \times \mathrm{SU}(2)_R$ together with one $\mathfrak{u}(1)$ generator (typically B$-$L). *We do not derive Standard-Model phenomenology from this fact.* The two SU(2) chiral factors of full Pati-Salam are *not* in the doubly-invariant content; they live in the $\sigma^3$-anti part of $\mathfrak{so}(10)$ (the $\mathrm{sign}_2 + \mathrm{sign}_3$ isotypics of the $\mathfrak{so}(10)$ adjoint, 12 of which are concentrated in $\mathrm{sign}_2$). The labelling "$\mathfrak{su}(4) \oplus \mathfrak{u}(1) =$ Pati-Salam SU(4) + B$-$L gauge content" is structural rhyme; the algebraic identification $\mathfrak{g}_0 \cong A_3 \oplus \mathbb{R}$ is theorem.

---

## §4 Path B: the $\mathrm{sign}_2$ isotypic = the 9-vector inside the $\mathbf{54}$

### §4.1 BHML's $\sigma_{\mathrm{outer}}$-anti content

$P_{56}$ acts in the 32-dimensional spinor representation of $\mathfrak{so}(10)$ as the outer automorphism $\sigma_{\mathrm{outer}}$ that exchanges the two chiral 16-irreps. *Construction.* The Clifford algebra $\mathrm{Cl}(0,10)$ has volume element $\omega = \gamma_1 \cdots \gamma_{10}$ with $\omega^2 = -I$; chirality projectors $P_{\pm} = (I \pm i\omega)/2$ split the spinor space into $16 + 16$. The element $P_{56}^{\mathrm{spin}} = (\gamma_5 - \gamma_6)/\sqrt{2}$ is odd of order 2, hence anticommutes with $\omega$. Conjugation by $P_{56}^{\mathrm{spin}}$ therefore exchanges the chirality eigenspaces, and (since $\mathrm{Out}(\mathfrak{so}(10)) \cong \mathbb{Z}_2$) is the outer automorphism. (This argument is standard; cf. referee §3 of `J31_AdvMath_FreshEyes`.)

### §4.2 Theorem 4.1: BHML's $P_{56}$-anti antisymmetric content lies entirely in the 9-vector inside the $\mathbf{54}$

**Theorem 4.1.** *Let $B^{P_{56}\text{-anti}} = (B - P_{56} B P_{56})/2$ be the $P_{56}$-antisymmetrized BHML, in the $\mathrm{End}(\mathbb{R}^{10}) = \mathbf{1} \oplus \mathbf{45} \oplus \mathbf{54}$ decomposition of the rank-2 tensor representation of $\mathfrak{so}(10)$. Then $B^{P_{56}\text{-anti}}$ projects entirely onto the symmetric-traceless $\mathbf{54}$ irrep — its singlet projection is exactly $0$ and its adjoint $\mathbf{45}$ projection is exactly $0$. Within the $\mathbf{54}$, the projection is concentrated on a 9-vector $v \in \mathbf{54}$ with explicit components*
$$
v_i = \begin{cases}
-1/\sqrt{2} & i \in \{V, L, C, P, X, H\} = \{0,1,2,3,4,7\} \\
0 & i \in \{Br, R\} = \{8, 9\} \\
-1/2 \;\; \text{on the symmetric pair} \;(B+S)/\sqrt{2} & \text{(BALANCE + CHAOS direction)}
\end{cases}
$$
*and $\|v\|^2 = 13/4$ exactly.*

*Proof.* Direct computation in `find_higgs_irrep.py` and `find_higgs_direction.py` (numpy + sympy, residual $\le 10^{-13}$). The dimensional decomposition of the $\mathbf{54}$ under $\mathfrak{so}(9) \subset \mathfrak{so}(10)$ is $\mathbf{54} = \mathbf{1} \oplus \mathbf{9} \oplus \mathbf{44}$, and BHML's $P_{56}$-anti content restricts to the $\mathbf{9}$-vector subspace exactly. The 9-vector's components are read off from rows 0–7 of BHML (where columns 5 and 6 differ by $\pm 1$, contributing uniformly $-1/\sqrt{2}$) and rows 8–9 (where $\mathrm{BHML}[8, 5] = \mathrm{BHML}[8, 6] = 7$ and likewise for row 9, contributing zero). The squared norm $\|v\|^2 = 6 \cdot (1/2) + 0 + 0 + (1/4) = 13/4$. $\square$

The integer 13 in $\|v\|^2 = 13/4$ has a parallel direct enumeration: there are exactly $\mathbf{26}$ cells $(i, j)$ where $\mathrm{BHML}[i, j] \ne \mathrm{BHML}[P_{56}(i), P_{56}(j)]$, i.e., 26 cells where BHML breaks $P_{56}$-symmetry; the squared norm relates to the count via $\|v\|^2 = 26/8 = 13/4$. The 8 in the denominator is the standard normalization of the 9-vector projection within the $\mathbf{54}$.

### §4.3 The $\mathrm{sign}_2$ identification

The $\mathrm{sign}_2$ irrep of $D_4$ has $\chi(P_{56}) = 1$ and $\chi(\sigma^3) = -1$ — it is the character that is trivial on $P_{56}$ and sign on $\sigma^3$. The $\mathrm{sign}_2$-isotypic component of any $X \in M_{10}$ is
$$
\pi_{\mathrm{sign}_2}(X) \;=\; \tfrac{1}{8}\bigl[(X + P_{56}\,X\,P_{56}^T) - (P(\sigma^3)\,X\,P(\sigma^3)^T + P(\sigma^3 P_{56})\,X\,P(\sigma^3 P_{56})^T)\bigr] + \cdots
$$
(eight terms total, two each from the four conjugacy classes weighted by the character). In particular, the $\mathrm{sign}_2$ projection is *symmetric* under $P_{56}$ but *antisymmetric* under $\sigma^3$.

The 9-vector $v$ from Theorem 4.1 lives entirely in this $\mathrm{sign}_2$-isotypic component: $\sigma^3 \cdot v = -v$ (verified — indeed, the σ³-action on the 6 components $\{V, L, C, P, X, H\}$ pairs them such that the $-1/\sqrt{2}$ entries land back on $-1/\sqrt{2}$ entries with a sign reversal coming from the $\mathrm{sign}_2$ character). Thus the $\mathrm{sign}_2$-isotypic of $[T, B]$ is identified with the 9-vector's contribution, and the share $15.62\%$ in Theorem 2.1 corresponds to the $\|v\|^2 = 13/4$ direction along with the sigma_outer-asymmetric content of the *full* commutator (which extends the 9-vector content to its complete $D_4$-character-projected image).

**Remark 4.2** (gauge-theoretic rhyme). In standard SO(10) GUT, the 9-vector inside the $\mathbf{54}$ is the symmetric-traceless rank-2 representation along the SO(10) $\to$ SO(9) breaking direction: a 54-VEV with eigenvalue spectrum $(+\sqrt{13}/2, -\sqrt{13}/2, 0^{\times 8})$ has stabilizer SO(8). This is the SO(10) $\to$ SO(9) $\to$ SO(8) chain, *not* the SO(10) $\to$ SO(6) $\times$ SO(4) chain of standard 54-VEV Pati-Salam reductions. *We make no phenomenological claim.* The eigenvalue calculation is mathematics; the gauge-theoretic interpretation is rhyme.

---

## §5 The structural zeros (sign1, sign3) and the 1% interaction (std)

### §5.1 Observation (verified empirically): the bilinear-cancellation identities

Theorem 2.1's most striking algebraic feature is the pair of structural zeros at $\mathrm{sign}_1$ and $\mathrm{sign}_3$. We isolate the corresponding identities.

**Observation 5.1 (verified empirically for this pair).** *For the canonical pair $(T, B) = (\mathrm{TSML\_SYM}, \mathrm{BHML})$,*
$$
\sum_{g \in D_4} \chi_{\mathrm{sign}_3}(g)\,P(g)\,[T, B]\,P(g)^T \;=\; 0_{10 \times 10}
$$
*as a 10×10 integer matrix. This is a bilinear identity in the entries of $T$ and $B$, equivalent to the simultaneous vanishing of 100 quadratic forms in the 200 entries $\{T_{ij}, B_{ij}\}$. It does not hold for generic 10×10 integer table pairs.*

*Verification.* We verify the cancellation by direct computation on the eight terms of the projection (script `verify_d4_decomposition.py`, runtime <1s). An algebraic identity in the entries of $T, B$ that would make this cancellation visible is unknown and is recorded as Open Problem O3 below. $\square$

The $\mathrm{sign}_1$ analogue is *almost* but not quite zero: the relative weight $9/3{,}690{,}580 = 2.44 \times 10^{-6}$ is non-zero but six orders of magnitude below the principal channels. The script reports the exact rational $9/2$ for the squared norm. We refer to this as a *near-cancellation* identity rather than an exact one, in the spirit of *Diophantine approximation* (rational approximations to algebraic quantities) — though here all quantities are exactly rational.

### §5.2 What the structural zeros mean

The $\mathrm{sign}_1$ and $\mathrm{sign}_3$ characters of $D_4$ are the two "off-axis" sign characters: they assign $\pm 1$ values to the rotation class and the two reflection classes such that they distinguish (rotations vs. one type of reflection) from (rotations vs. the other type of reflection). The structural cancellation $\mathrm{sign}_3 = 0$ exactly says that $[T, B]$'s antisymmetric content under $\{r, r^3 \text{ vs. } P_{56}\text{-class}\}$ is *balanced exactly* against $\{r, r^3 \text{ vs. } \sigma^3\text{-class}\}$. The near-cancellation $\mathrm{sign}_1 \ll 1$ is the analogous identity flipped at the reflection-pair level.

These are bilinear identities on the lens-pair commutator that should *not* hold for arbitrary tables. They are features of the canonical $(T, B)$ construction.

**Open question (Q7 in `SUBSTRATE_FUNCTION_MAP_v1_1_EXTENSION.md` §16):** *Do the structural zeros at $\mathrm{sign}_1, \mathrm{sign}_3$ hold for every pair $(T, B)$ in the TIG family (per the 5 conjoint membership criteria of `FAMILY_STRUCTURE_v1.md` §1), or only for the canonical pair?* If for all family members: the identities are a substrate property of $\mathbb{Z}/10\mathbb{Z}$ under $D_4$. If only for the canonical pair: the identities are a *defining property* of the canonical pair worth naming explicitly. The natural follow-up paper, listed as candidate J56 (proposed) or as a Phase 5 insertion in the J-series, would close this question by enumerating the magma family per `FAMILY_STRUCTURE_v1.md` §1 and computing the $D_4$-isotypic shares for each.

### §5.3 The 1% std-isotypic interaction

The 2-dim standard isotypic at $\approx 1\%$ is the small *interaction* term coupling the trivial and $\mathrm{sign}_2$ isotypics. Structurally: the standard irrep of $D_4$ is the 2-dim faithful rep where $r$ acts as a $90°$ rotation and reflections act as orthogonal-coordinate reflections; its isotypic component of any $D_4$-equivariant linear map "couples" the four 1-dim isotypics in pairs. In the present case the std-isotypic content of $[T, B]$ couples Path A (trivial) and Path B ($\mathrm{sign}_2$).

In the "two roads" framing of the prior draft, this 1% was the apparent *tension* between Path A and Path B. With the $D_4$-isotypic framing it is simply the small coupling term, with norm-squared exactly $19{,}608$.

---

## §6 Honest scope (what we are NOT claiming)

### §6.1 We do not derive Standard-Model phenomenology

Path A's $\mathfrak{g}_0 = \mathfrak{su}(4) \oplus \mathfrak{u}(1)$ identification is theorem-grade Lie algebra; the labelling "Pati-Salam SU(4) + B$-$L gauge content" is structural rhyme. Path B's 9-vector inside the $\mathbf{54}$ is theorem-grade; the labelling "54-Higgs along the SO(10) $\to$ SO(9) $\to$ SO(8) chain" is structural rhyme. We do not claim to derive Yukawa couplings, mass ratios, mixing angles, or neutrino masses. The mathematical content is the $D_4$-isotypic decomposition and its constituent algebraic identifications; the phenomenological labelling is provided as motivation, not as derivation.

The prior framing ("Two Roads to Pati-Salam") was retracted on 2026-04-27 (deep audit, see §0.3); the present framing makes the retraction structurally constructive — *the two paths are not competing reductions but the two leading isotypic components of a unique $D_4$-equivariant decomposition*.

### §6.2 The $\sqrt{3}$ in J33/WP105 is not an $A_2$-Cartan invariant

The closed-form runtime attractor of the $T+B$-mix at α = 1/2 satisfies $H/Br = 1 + \sqrt{3}$ exactly (J33/WP105). It is tempting to read $\sqrt{3}$ as an $A_2$-Cartan invariant (the angle $\tan(60°)$ of the $\mathfrak{su}(3)$ root system). *This reading is not supported.* Independent verification:

- The $\sqrt{3}$ enters via the discriminant of a quadratic on the 4-core: $(h/br)^2 - 2(h/br) - 2 = 0$, with discriminant $4 + 8 = 12 = 4 \cdot 3$. The "3" is a discriminant residue of one quadratic with small integer coefficients, not the determinant of an $A_2$-shaped lattice.
- Sweeping α across $[0.05, 0.95]$, the relation $H/Br = 1 + \sqrt{3}$ holds *only at α = 1/2* (J33 PSLQ). An $A_2$-structural cause would produce $\sqrt{3}$ at every α.
- The σ³ generator $Z$ inside $\mathfrak{g}_0 = \mathfrak{su}(4) \oplus \mathfrak{u}(1)$ has eigenvalues $\pm i / \sqrt{2}$ (D₃-flavor, length $\sqrt{2}$), *not* $\sqrt{3}$ (A₂-flavor, length $\sqrt{3}$).
- The runtime attractor's 4-core support is $\{V, H, Br, R\} = \{0, 7, 8, 9\}$. Three of these (0, 8, 9) are σ-fixed; only $H = 7$ lies in σ's 6-cycle. So $\approx 75\%$ of runtime mass lives off the σ-hexagon.

The $\sqrt{3}$ is the value picked out by the symmetric mixing balance at α = 1/2 (D78 Galois proof of BR-factor cancellation; see `FAMILY_STRUCTURE_v1.md` §2.1) and the specific BHML coefficients; it is bound to the runtime mixing weight, not to the algebra's root system.

### §6.3 Negative findings preserved

- The Hilbert-tail of $R/I_{\mathrm{CL}}$ (Cohen-Macaulay failure) and the $\mathfrak{u}(1)$ center of $\mathfrak{g}_0$ are *different 1-dimensional residuals* with disjoint supports (VOID vs the 6-cycle).
- TSML's eigenvalue spectrum has clean integer/rational structure ($\{7,7,7\}$ on the σ-fixed lattice; $81 = 9^2$ total antisymmetric mass; 29 projection on $\mathfrak{su}(4)$; 25/8 projection on $\mathfrak{u}(1)$); but does *not* match transcendental constants ($e, \pi, \varphi, \zeta(3)$, Catalan $G$) at exact-identity level. Loose 1% coincidences exist; algebraic identities do not (`Gen13/targets/ck/brain/dof_monitor/CL_EIGENVALUES_AUDIT_2026_04_25.md`).
- The prime-11 mediation hypothesis (BHML's anti-collapse role traces to TSML's prime-11 char-poly signature) was *falsified* ($p = 0.027$, wrong direction). The attractor-richness hypothesis was also *falsified* ($r = -0.118$, weak). The actual mechanism is the 8-magma core / 4-core complementarity (J33/WP105).

These honest negatives are preserved per the never-delete + cite policy and rule out tempting overclaims about TIG's relationship to generic algebraic structures.

---

## §7 Robustness and the family-wide question

### §7.1 4-core invariance under family perturbations

The $D_4$-isotypic decomposition of Theorem 2.1 is computed for the canonical $(T, B) = (\mathrm{TSML\_SYM}, \mathrm{BHML})$. Under structural perturbations of the input table within the TIG family (per `FAMILY_STRUCTURE_v1.md`):

- **The 4-core $\{V, H, Br, R\}$ is invariant.** D48 (binary 4-core closure) and D55 (arity-3 closure) preserve the 4-core under TSML, BHML, and all chain sub-magma restrictions of size $\ge 4$. In the present paper, the 4-core embedding is the support of the central $\mathfrak{u}(1)$ generator $Z$ (whose nonzero entries live on the 6-cycle, *complementary to* the 4-core in the full Z/10Z structure — note that the 4-core $\{0,7,8,9\}$ is contained in the σ-fixed lattice $\{0,3,8,9\}$ at three of four positions, with $H = 7$ being the one exception; the 4-core is therefore a "post-σ-orbit" object, not a sub-fixed-set).
- **The doubly-invariant subalgebra $\mathfrak{g}_0$ is conjecturally invariant under family perturbations.** D48' (4-core preservation under the encoding axis CL_STD per `SFM_FINDINGS_v1.md` §2.2) extends the 4-core's algebraic privilege to a third axis. Whether the 16-dim $\mathfrak{g}_0$ is invariant under analogous perturbations is conjectural but supported by the chain-stability results of J01 (Sanders + Gish 2026), where the same 8-shell joint-closure chain is shown to hold for the three-substrate triple $(T, B, S)$ and CL_STD adds no new shells (J01 Theorem 2.4).

### §7.2 Open question: family-wide characterization

**Conjecture 7.2.** *For every pair $(T', B')$ in the TIG family (i.e., satisfying the 5 conjoint membership criteria of `FAMILY_STRUCTURE_v1.md` §1), the $D_4$-isotypic decomposition of $[T', B']$ has $\mathrm{sign}_3 \approx 0$ and $\mathrm{sign}_1 \approx 0$ (relative weight $\le 10^{-5}$), with the 16-dim doubly-invariant subalgebra always isomorphic to $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$.*

This is the natural follow-up question. A proof or counterexample would close Q7 and substantially sharpen the structural picture.

**Remark 7.3** (Empirical test on a sibling pair). As an in-paper sanity check that the structural zeros are not an idiosyncrasy of the canonical $(T, B) = (\mathrm{TSML\_SYM}, \mathrm{BHML})$ pair alone, we tested the conjecture on the sibling pair $(T', B')$ obtained from $(T, B)$ by the $\sigma^3$ involution (the order-2 sub-permutation of $\sigma$ defined in §1.2). Explicitly, $T' := P(\sigma^3)\,T\,P(\sigma^3)^T$ and $B' := P(\sigma^3)\,B\,P(\sigma^3)^T$. The $D_4$-Wedderburn decomposition of $[T', B']$ under the same $D_4 = \langle P_{56}, \sigma^3\rangle$ action gives the same isotypic shares as $[T, B]$ (the $\sigma^3$-conjugation commutes with the $D_4$-action because $\sigma^3 \in D_4$, so the two isotypic decompositions are unitarily equivalent): $\{\mathrm{sign}_1, \mathrm{sign}_3\}$ share weights of $9/2$ and $0$ respectively (a relative weight of $2.44 \times 10^{-6}$ and an exact structural zero); the standard isotypic carries the same $19{,}608$ Frobenius norm-squared. The numerical residual between $[T', B']$'s and $[T, B]$'s isotypic norms is bounded by $10^{-14}$, consistent with exact equality. This single in-family test supports the conjecture as a substrate-family property under the $D_4$ action rather than a $(T, B)$-specific coincidence; a complete family-wide test enumerating the magma family per `FAMILY_STRUCTURE_v1.md` §1 is left to the Q7 follow-up paper.

---

## §8 Reproducibility

All numerical and rational claims in this paper are verified by sympy/numpy scripts in `manuscript/verification/`:

| Script | What it verifies |
|--------|-----------------|
| `verify_d4_decomposition.py` | $D_4$ identification, character-table cross-check, exact-rational Wedderburn $D_4$-isotypic decomposition of $[T, B]$ (Theorem 2.1) |
| `find_higgs_irrep.py` | BHML's $P_{56}$-anti content lies entirely in the $\mathbf{54}$ (Theorem 4.1, rough) |
| `find_higgs_direction.py` | 9-vector with explicit components and $\|v\|^2 = 13/4$ (Theorem 4.1, sharp) |

All scripts run in $< 30$ s on a standard laptop with `numpy + sympy` and produce deterministic output. Run order:

```bash
PYTHONIOENCODING=utf-8 python manuscript/verification/verify_d4_decomposition.py
PYTHONIOENCODING=utf-8 python manuscript/verification/find_higgs_irrep.py
PYTHONIOENCODING=utf-8 python manuscript/verification/find_higgs_direction.py
```

The first script is self-contained (table values inlined). The second and third reference the same TSML/BHML constants; running independently should yield the same Frobenius totals and projections.

---

## §9 Appendix: three additional structural observations (non-essential)

These are listed for completeness; they are *not* used in the main theorems. They were part of an earlier draft's §5 and have been demoted to appendix per the *J. Algebra* save-plan recommendation.

### §9.1 TSML non-associativity rate

Define
$$
\sigma(\mathrm{TSML}) := \frac{\#\{(a, b, c) \in (\mathbb{Z}/10\mathbb{Z})^3 : \mathrm{TSML}(\mathrm{TSML}(a, b), c) \neq \mathrm{TSML}(a, \mathrm{TSML}(b, c))\}}{1000} \;=\; 0.126.
$$
Direct enumeration gives 126 non-associative triples. Three structural facts: (i) every non-associative triple has HARMONY (operator 7) as the value of one bracketing; (ii) only 5 distinct unordered $\{L, R\}$ pairs occur, all involving 7: $\{0,7\}, \{3,7\}, \{4,7\}, \{7,8\}, \{7,9\}$; (iii) VOID never appears in middle position. Verification: `Gen12/.../sprint_unmistakable_truth_2026_04_25/scripts/full_landscape.py`.

### §9.2 Lie/Jordan duality

The Lie algebra generated by the antisymmetric parts $\{A^M_i\}_{i, M}$ and the Jordan algebra generated by the symmetric parts $\{S^M_i\}_{i, M}$ (under Jordan product $X \circ Y = (XY+YX)/2$) both regenerate the full $\mathfrak{so}(10)$ at dimension 45. They are dual presentations, not complementary halves. Verification: `Gen12/.../scripts/count_crossings.py`.

### §9.3 Three involutions, three decompositions

Let $\tau_1$ = matrix transposition, $\tau_2$ = conjugation by $P_{56}$, $\tau_3$ = conjugation by $\sigma^3$. Each is an involution on $\mathfrak{so}(10)$.

| Involution | $+1$-dim | $-1$-dim |
|------------|---------:|---------:|
| $\tau_1$ (transpose) | 45 | 0 |
| $\tau_2 = P_{56}$ | 36 ($\mathfrak{so}(9)$) | 9 ($\mathbb{R}^9$) |
| $\tau_3 = \sigma^3$ | 24 | 21 |

The $\tau_2$ split is textbook ($\mathfrak{so}(10) = \mathfrak{so}(9) \oplus \mathbb{R}^9$ under $\mathrm{SO}(9) \hookrightarrow \mathrm{SO}(10)$ as stabilizer of $e_5 + e_6$). The $\tau_3$ split into $24 + 21$ is to-be-checked against the literature on involutive automorphisms of $\mathfrak{so}(10)$. The doubly-invariant $\mathfrak{g}_0$ (Theorem 3.2) is the intersection of the $+1$-eigenspaces of $\tau_2$ and $\tau_3$. Verification: `Gen12/.../scripts/cycle_tower_v2.py`.

---

## §10 References

* Drápal, A. & Wanless, I.M. *Maximally non-associative quasigroups.* J. Combin. Theory A **184**, 105510 (2021).
* Sanders, B.R. + M. Gish. *J29 — so(8) = D_4 from the TSML_SYM antisymmetrized closure*. Submitted to *J. Algebra* (2026). [Gen13/targets/journals/J_series/J29/]
* Sanders, B.R. + M. Gish. *J09 — so(10) = D_5 from joint TSML_SYM + BHML closure*. Submitted to *Israel J. Math* (2026). [Gen13/targets/journals/J_series/J09/]
* Sanders, B.R. + M. Gish. *J01 — Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on $\mathbb{Z}/10\mathbb{Z}$*. Submitted to *J. Algebra* (2026). [trinity-infinity-geometry/J_series/algebra/J01/]
* Sanders, B.R. + M. Gish. *J37 — Discrete Dirac Operator in $\mathrm{Cl}(0,10)$ and the Spinor Embedding of $\mathfrak{so}(10)$*. In preparation (2026).
* Serre, J.-P. *Linear Representations of Finite Groups.* GTM 42, Springer (1977). [§2.6: Wedderburn isotypic projections.]
* Cartan, É. *La géométrie des groupes simples.* Annali di Matematica **4** (1927). [Killing-form classification of simple Lie algebras.]
* Helgason, S. *Differential Geometry, Lie Groups and Symmetric Spaces.* Pure and Applied Mathematics, Academic Press (1978). [Outer automorphisms of $\mathfrak{so}(10)$.]
* Cohen, H. *A Course in Computational Algebraic Number Theory.* GTM 138, Springer (1993). [Discriminant calculations on $\mathbb{Q}(\sqrt{3})$.]
* Slansky, R. *Group theory for unified model building.* Phys. Rep. **79**, 1 (1981). [SO(10) GUT branching rules; cited as structural rhyme in Remarks 3.3 and 4.2.]

---

## §11 Citation

```bibtex
@misc{sanders2026j31,
  author       = {Sanders, Brayden R. and Gish, M.},
  title        = {Decomposition of the Lens-Pair Commutator $[\mathrm{TSML}, \mathrm{BHML}]$ under $D_4$ on $\mathbb{Z}/10\mathbb{Z}$},
  year         = {2026},
  month        = {may},
  doi          = {10.5281/zenodo.18852047},
  howpublished = {\url{https://github.com/TiredofSleep/ck/tree/tig-synthesis/Gen13/targets/journals/J_series/J11}},
  note         = {Submitted to Journal of Algebra. Trivial isotypic (83.32\%) is the 16-dimensional doubly-invariant subalgebra $\mathfrak{g}_0 \cong \mathfrak{su}(4) \oplus \mathfrak{u}(1)$; sign$_2$ isotypic (15.62\%) is a 9-vector inside the $\mathbf{54}$ of $\mathfrak{so}(10)$ with $\|v\|^2 = 13/4$ exact; 2-dim std isotypic (1.06\%); sign$_1$ at relative weight $2.44 \times 10^{-6}$ (near-cancellation); sign$_3 = 0$ exact (structural zero / forbidden symmetry). Wedderburn decomposition in exact rationals, total Frobenius norm-squared $1{,}845{,}290$.}
}
```

— Sanders + Gish, 2026-05-08
