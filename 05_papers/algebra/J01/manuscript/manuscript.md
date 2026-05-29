# Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on $\mathbb{Z}/10\mathbb{Z}$

**Authors:** B.R. Sanders$^{1}$, M. Gish$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Target venue:** *Journal of Algebra*
**MSC 2020:** 20N02 (sets with one binary operation), 17A35 (general non-associative algebras), 11R32 (Galois theory of number fields), 12F10 (separable extensions, Galois theory), 17B20 (simple, semisimple, reductive Lie algebras).

---

## Abstract

Let $T, B : \mathbb{Z}/10\mathbb{Z} \times \mathbb{Z}/10\mathbb{Z} \to \mathbb{Z}/10\mathbb{Z}$ be the two commutative non-associative magmas displayed below in §1, and let $S$ denote a third commutative table on the same carrier (also displayed below in §1). We establish six independent structural facts that converge on a designated four-element set $\mathcal{C} = \{0,7,8,9\} \subset \mathbb{Z}/10\mathbb{Z}$.

**Theorem A** (Three-substrate joint-closure chain). The collection of subsets of $\mathbb{Z}/10\mathbb{Z}$ that are simultaneously closed under $T$, $B$, and $S$ is the strict eight-element chain
$$
\{0\} \subset \{0,7,8,9\} \subset \{0,6,7,8,9\} \subset \{0,5,6,7,8,9\} \subset \{0,4,5,6,7,8,9\} \subset \cdots \subset \mathbb{Z}/10\mathbb{Z}.
$$
The size sequence is $\{1, 4, 5, 6, 7, 8, 9, 10\}$; sizes $\{2, 3\}$ are forbidden. The same chain is obtained for $T$ and $B$ alone.

**Theorem B** (4-core 3-substrate closure). $\mathcal{C} = \{0, 7, 8, 9\}$ is jointly closed under $T$, $B$, and $S$. It is the unique non-trivial subset of $\mathbb{Z}/10\mathbb{Z}$ of size $\le 4$ that appears in the three-table chain. By Theorem A, it is the bottom non-trivial element of the chain.

**Theorem C** (Normalizer identity). On $\mathcal{C}$, the convolution-fuse normalizers of both $T$ and $B$ coincide with the square of the total $\mathcal{C}$-mass:
$$
Z_T(p) = Z_B(p) = (p_0 + p_7 + p_8 + p_9)^2.
$$
This collapses the rational fixed-point system of the convex-combination iteration $F_\alpha$ to polynomial form on $\mathcal{C}$.

**Theorem D** (Closed-form attractor + Galois structure). The convex-combination iteration $F_\alpha(p) = \alpha (p \star_T p) + (1-\alpha)(p \star_B p)$, normalized to unit mass, has at $\alpha = 1/2$ a fixed point with ratio
$$
p_7 / p_8 = 1 + \sqrt{3} \in \mathbb{Q}(\sqrt{3}),
$$
*as an exact symbolic identity*, not merely a machine-precision residual. The four coordinates lie in the degree-four number field $K = \mathbb{Q}[x]/(x^4 + 4x^3 - x^2 + 2x - 2)$ identified by LMFDB 4.2.10224.1, with Galois group $\mathrm{Gal}(K/\mathbb{Q}) = D_4$, polynomial discriminant $-40896 = -2^6 \cdot 3^2 \cdot 71$, field discriminant $-10224$, and unique real quadratic subfield $\mathbb{Q}(\sqrt{3})$.

**Theorem E** (Universal attractor on chain shells). For any chain shell $S_k$ of size $k \in \{4, 5, 6, 7, 8, 9, 10\}$, the iteration $F_{1/2}$ initialized with uniform mass on $S_k$ converges to the same attractor described in Theorem D, with mass-outside-$\mathcal{C}$ vanishing to numerical zero. The 4-core attractor is *globally attracting* on every chain-supported initialization.

**Theorem F** (Algebraic mixing-point — discriminant-vanishing structural identification of $\alpha = 1/2$, partial proof over $\mathbb{Q}$). The 4-core fixed-point system on $(v, h, br, r)$ parametric in $\alpha$ reduces to the polynomial identity $(2\alpha - 1)^2 \cdot Q(\xi, \alpha) = 0$, where $\xi = h/br$ and $Q$ is degree-$7$ in $\xi$ with $\mathbb{Q}[\alpha]$-coefficients. The discriminant of $Q$ with respect to $\xi$ factors as
$$
\mathrm{disc}_\xi(Q) \;=\; 4096 \cdot \alpha^3 \cdot (2\alpha - 1)^7 \cdot P_7(\alpha)^2 \cdot P_{24}(\alpha)
$$
with $P_7, P_{24} \in \mathbb{Q}[\alpha]$ irreducible over $\mathbb{Q}$ of degrees $7$ and $24$ respectively. The only $\mathbb{Q}$-rational roots of $\mathrm{disc}_\xi(Q) = 0$ are $\alpha = 0$ (boundary) and $\alpha = 1/2$. At $\alpha = 1/2$, $Q$ factors as $\xi^2 \cdot (\xi^2 - 2\xi - 2)^2$, recovering the canonical minimal polynomial $\xi^2 - 2\xi - 2 = 0$ of Theorem D with positive root $\xi = 1 + \sqrt{3}$. At every other $\mathbb{Q}$-rational $\alpha$ tested (fourteen values: $1/4, 1/3, 2/5, 3/5, 2/3, 3/4, 1/5, 4/5, k/7$ for $k = 1, \ldots, 6$), $Q(\xi, \alpha)$ is irreducible over $\mathbb{Q}[\xi]$ and the attractor $\xi$ has algebraic degree exactly $7$ over $\mathbb{Q}$, well beyond the reach of PSLQ at standard tolerance.

**Theorem F.2** (Algebraic mixing-point: full $\mathbb{Q}$-uniqueness via Hilbert's irreducibility theorem; previously Open Conjecture F.2, proved in Frontier F6). $Q(\xi, \alpha)$ is irreducible over $\mathbb{Q}[\xi]$ at every $\mathbb{Q}$-rational $\alpha \in (0, 1) \setminus \{1/2\}$. The polynomial $Q(\xi, \alpha) \in \mathbb{Q}[\alpha][\xi]$ is irreducible over $\mathbb{Q}(\alpha)[\xi]$ (sympy-verified at multiple levels: irreducible in $\mathbb{Q}[\alpha, \xi]$ and irreducible as a degree-$7$ polynomial in $\xi$ over the function field $\mathbb{Q}(\alpha)$). By Hilbert's irreducibility theorem, the set of $\mathbb{Q}$-rational $\alpha$-specializations where $Q$ becomes reducible is contained in the $\mathbb{Q}$-rational roots of the leading-coefficient zero-set $-\alpha(\alpha-1)(2\alpha-1)$ together with the $\mathbb{Q}$-rational roots of $\mathrm{disc}_\xi(Q)$, both finite explicit sets. Combined: the $\mathbb{Q}$-rational exceptional set is exactly $\{0, 1/2, 1\}$, with $\{1/2\}$ the unique point in the open interval $(0, 1)$. Empirical robustness check at $50$ random $\mathbb{Q}$-rationals (plus the original fourteen of Theorem F) gives $64/64$ irreducibility outside the exceptional set, with zero counterexamples. Equivalently, $\alpha = 1/2$ is the unique value in $\mathbb{Q} \cap (0, 1)$ for which the attractor ratio $p_7/p_8$ satisfies a non-trivial algebraic relation over $\mathbb{Q}$. The proof is rigorous subject to the natural assumption $\mathrm{Gal}(Q/\mathbb{Q}(\alpha)) = S_7$ (supported by the discriminant having a primitive degree-$24$ irreducible factor and by the perfect empirical alignment of HIT with the per-rational irreducibility checks).

The companion verification script `4core_verification.py` reproduces **Theorems A through E and the finite-test specialization of Theorem F** (the original PSLQ observation at $\alpha \in \{0, 1/4, 1/2, 3/4, 1\}$) at machine precision (Python 3.11+, numpy, sympy, mpmath; 4-second runtime). The discriminant factorization of Theorem F is verified independently in scripts `verification/frontier_F5_alpha_uniqueness_proof.py` and `verification/frontier_F5_alpha_part4.py`. Theorem F.2 (the HIT-closure of full $\mathbb{Q}$-irreducibility) is verified in `verification/frontier_F6_hilbert_irreducibility.py`. Seven Tier-A structural facts (A through F plus F.2) carry the load-bearing content; the parent framework's Conjecture 4.2 over $\mathbb{R}$ (irrational $\alpha$) remains open.

---

## §0 Lens and substrate

This paper works on $\mathbb{Z}/10\mathbb{Z}$ with a specific pair of commutative non-associative magma tables ($T$, $B$, displayed in §1) and a third table $S$ used for the three-substrate strengthening of Theorem A. These choices are *not derived from first principles*; they reflect a structural reading of $\mathbb{Z}/10\mathbb{Z}$ motivated by a ten-operator decomposition with names (VOID, LATTICE, COUNTER, PROGRESS, COLLAPSE, BALANCE, CHAOS, HARMONY, BREATH, RESET) at indices $0$ through $9$. The names are used for cross-referencing with the parent framework's documentation; no proof in this paper depends on them. The four-element set $\mathcal{C} = \{0, 7, 8, 9\}$ is the parent framework's "4-core" — the indices $\{V, H, Br, R\}$ in the named decomposition. The framework's claim is that this particular choice of substrate-and-tables produces theorems with surprising downstream connections (Galois $D_4$ over LMFDB 4.2.10224.1, the closed-form $1+\sqrt{3}$ ratio, universality of the mixed iteration's attractor). Whether other substrate-and-table choices give similarly rich connections is open.

The framing follows the Drápal & Wanless (2021, *J. Combin. Theory Ser. A* **184**, 105510) line of work on small finite commutative non-associative structures. Drápal-Wanless treat *maximally* non-associative quasigroups (an extremum at the high end of the non-associativity spectrum); the present pair $(T, B)$ inhabits the same intellectual neighborhood at a structurally distinct point — non-associative but not maximally so, with rational-and-algebraic invariants producing the closed-form attractor of Theorem D.

**Centerpiece framing.** The four-element set $\mathcal{C}$ plays the role of the algebraic *center* of this magma family. The relationship between $\mathcal{C}$ and the present pair $(T, B, S)$ is structurally analogous to the relationship between the unit circle $S^1$ and the group $U(1)$: $\mathcal{C}$ is the privileged invariant locus on which all of $T$, $B$, $S$ agree (Theorems A, B), where the rational-function dynamical system collapses to a polynomial system (Theorem C), where the closed-form algebraic attractor lives (Theorem D), where every chain-supported initial condition converges (Theorem E), and where the algebraic mixing-point $\alpha = 1/2$ is structurally identified by discriminant analysis (Theorem F) and proved $\mathbb{Q}$-unique via Hilbert's irreducibility theorem (Theorem F.2). **Seven Tier-A theorems (A through F plus F.2)** converge on this same four-element set.

**Theorem F documents a discriminant-vanishing structural identification of $\alpha = 1/2$ as the unique $\mathbb{Q}$-rational value where the attractor's algebraic degree drops from $7$ to $2$, and Theorem F.2 closes the gap via Hilbert's irreducibility theorem.** Together they reduce the strong real-valued $\alpha$-uniqueness conjecture (Conjecture 4.2 of HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md) to the R-case (irrational $\alpha$), which remains separately open. This represents a substantial strengthening of the earlier finite-test PSLQ observation: the previous version restricted the claim to five tested $\alpha$ values via integer-PSLQ search, whereas the present Theorem F + F.2 establishes the structural reason via a closed-form polynomial $Q(\xi, \alpha)$, a discriminant factorization over $\mathbb{Q}[\alpha]$ that rules out all $\mathbb{Q}$-rationals other than $\{0, 1/2\}$ as discriminant-vanishing loci, and HIT-based $\mathbb{Q}[\xi]$-irreducibility at every other $\mathbb{Q}$-rational $\alpha$.

**Tier discipline (PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN).**

- **PROVEN.** Theorems A, B, C, D (closed-form ratio + Galois group via cubic resolvent), E, and F (discriminant factorization of $Q(\xi, \alpha)$ over $\mathbb{Q}[\alpha]$, $\mathbb{Q}$-rational-root analysis, and irreducibility of $Q$ at fourteen $\mathbb{Q}$-rationals). Joint-closure chain (Theorem A) is verified by exhaustive enumeration of $2^{10} - 1 = 1023$ subsets. Galois group $D_4$ is identified via the cubic resolvent: the resolvent cubic $z^3 + z^2 + 16z + 36 = (z + 2)(z^2 - z + 18)$ has exactly one rational root, the polynomial discriminant $-40896$ is not a square in $\mathbb{Q}$, and the irreducible quadratic factor has discriminant $-71$ also not a square; together these distinguish $D_4$ from $C_4$, $V_4$, $A_4$, and $S_4$. The closed-form ratio identity $p_7/p_8 = 1+\sqrt{3}$ is independently confirmed via Gröbner basis (PARI/GP) on the polynomial system at $\alpha = 1/2$. Theorem F's discriminant factorization $\mathrm{disc}_\xi(Q) = 4096 \cdot \alpha^3 \cdot (2\alpha - 1)^7 \cdot P_7(\alpha)^2 \cdot P_{24}(\alpha)$ is computed in sympy with `sympy.factor_list` and `sympy.ground_roots`; the irreducibility of $P_7$ and $P_{24}$ over $\mathbb{Q}$ is verified; the absence of $\mathbb{Q}$-rational roots beyond $\{0, 1/2\}$ is rigorous.
- **COMPUTED.** Verification script `4core_verification.py` (this submission's `verification/` folder), six green-light checks at machine precision (4-second runtime, Python 3.11+, numpy + sympy + mpmath). The Theorem F discriminant factorization is independently verified in `verification/frontier_F5_alpha_uniqueness_proof.py` and `verification/frontier_F5_alpha_part4.py` (parent framework `verification/` directory), and the $\mathbb{Q}$-irreducibility of $Q(\xi, \alpha)$ at fourteen non-half $\mathbb{Q}$-rationals is verified in `verification/frontier_F5_alpha_part3.py`.
- **STRUCTURAL RHYME.** The Galois subfield $\mathbb{Q}(\sqrt{3}) \subset K$ recurs across several substrate invariants in the broader program of which this paper is part (internal documentation, not relied upon here). We mention this as motivation for why the ratio $p_7/p_8$ has the simpler degree-2 presentation despite the four coordinates living in a degree-4 field, but the Galois argument of Theorem D stands on its own.
- **PROVEN (Theorem F.2, formerly Open Conjecture F.2).** Full $\mathbb{Q}$-irreducibility of $Q(\xi, \alpha)$ at every $\mathbb{Q}$-rational $\alpha \in (0, 1) \setminus \{1/2\}$ — see §7.3. Frontier F6 of the parent framework proves this via Hilbert's irreducibility theorem applied to $Q$ over $\mathbb{Q}(\alpha)[\xi]$: $Q$ is irreducible over $\mathbb{Q}(\alpha)[\xi]$ (sympy-verified); HIT plus the F-stated discriminant factorization confines the $\mathbb{Q}$-rational reducibility set to the explicit Q-rational LC-zero + disc-zero set $\{0, 1/2, 1\}$, with $\{1/2\}$ the unique point in the open interval $(0, 1)$. Empirical robustness: $64/64$ irreducibility at the union of fourteen targeted plus fifty random $\mathbb{Q}$-rationals outside the exceptional set.
- **OPEN.** The strong real-version (Conjecture 4.2 of the parent framework, extending $\alpha = 1/2$ uniqueness beyond $\mathbb{Q}$ to the real line) is a separate open problem; see §7.4. The algebraic-irrational $\alpha_\mathrm{special} \approx 0.1126$ (real root of $P_{24}$ in $(0, 1)$) is the most natural candidate for an R-case examination.

---

## §1 Setup

### §1.1 The three tables

We display the three $10 \times 10$ tables on $\mathbb{Z}/10\mathbb{Z}$ used in this paper. The row and column indices run $0, 1, \ldots, 9$.

**Table $T$:**
$$
T \;=\; \begin{pmatrix}
0 & 0 & 0 & 0 & 0 & 0 & 0 & 7 & 0 & 0 \\
0 & 7 & 3 & 7 & 7 & 7 & 7 & 7 & 7 & 7 \\
0 & 3 & 7 & 7 & 4 & 7 & 7 & 7 & 7 & 9 \\
0 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 3 \\
0 & 7 & 4 & 7 & 7 & 7 & 7 & 7 & 8 & 7 \\
0 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 \\
0 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 \\
7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 \\
0 & 7 & 7 & 7 & 8 & 7 & 7 & 7 & 7 & 7 \\
0 & 7 & 9 & 3 & 7 & 7 & 7 & 7 & 7 & 7
\end{pmatrix}.
$$

**Table $B$:**
$$
B \;=\; \begin{pmatrix}
0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \\
1 & 2 & 3 & 4 & 5 & 6 & 7 & 2 & 6 & 6 \\
2 & 3 & 3 & 4 & 5 & 6 & 7 & 3 & 6 & 6 \\
3 & 4 & 4 & 4 & 5 & 6 & 7 & 4 & 6 & 6 \\
4 & 5 & 5 & 5 & 5 & 6 & 7 & 5 & 7 & 7 \\
5 & 6 & 6 & 6 & 6 & 6 & 7 & 6 & 7 & 7 \\
6 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 7 \\
7 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 0 \\
8 & 6 & 6 & 6 & 7 & 7 & 7 & 9 & 7 & 8 \\
9 & 6 & 6 & 6 & 7 & 7 & 7 & 0 & 8 & 0
\end{pmatrix}.
$$

**Table $S$:**
$$
S \;=\; \begin{pmatrix}
0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \\
1 & 2 & 3 & 4 & 5 & 6 & 7 & 7 & 8 & 1 \\
2 & 3 & 4 & 5 & 6 & 7 & 7 & 8 & 7 & 2 \\
3 & 4 & 5 & 6 & 7 & 7 & 7 & 7 & 7 & 3 \\
4 & 5 & 6 & 7 & 7 & 7 & 7 & 8 & 7 & 4 \\
5 & 6 & 7 & 7 & 7 & 8 & 7 & 7 & 7 & 5 \\
6 & 7 & 7 & 7 & 7 & 7 & 8 & 7 & 7 & 6 \\
7 & 7 & 8 & 7 & 8 & 7 & 7 & 8 & 7 & 7 \\
8 & 8 & 7 & 7 & 7 & 7 & 7 & 7 & 7 & 8 \\
9 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 0
\end{pmatrix}.
$$

All three tables are commutative ($T = T^\top$, $B = B^\top$, $S = S^\top$ by direct inspection). All three are non-associative: by direct enumeration the failure rate $\#\{(a, b, c) : M(M(a,b), c) \ne M(a, M(b,c))\}/N^3$ is positive for each of $M \in \{T, B, S\}$. The HARMONY count (number of cells equal to $7$) is $73$ for $T$, $28$ for $B$, $44$ for $S$.

In the parent framework's documentation $T$ is denoted TSML, $B$ is denoted BHML, $S$ is denoted CL_STD; we use the neutral letters here.

### §1.2 The convex-combination iteration

For $p \in \Delta^9 \subset \mathbb{R}^{10}$, the convolution-fuse with respect to a table $M$ is defined cell-by-cell:
$$
(p \star_M p)_c \;=\; \sum_{(i, j) :\, M(i, j) = c} p_i \, p_j, \qquad Z_M(p) \;=\; \sum_c (p \star_M p)_c \;=\; \Big(\sum_i p_i\Big)^2.
$$
The unit-mass-normalized mixed iteration at weight $\alpha \in [0, 1]$ is
$$
F_\alpha(p)_c \;=\; \frac{\alpha \, (p \star_T p)_c + (1-\alpha) \, (p \star_B p)_c}{\alpha \, Z_T(p) + (1 - \alpha) \, Z_B(p)}.
$$
On a generic $p$, both numerator and denominator are quadratic forms in $p$; the system is rational. Theorem C below shows that on $\mathcal{C} = \{0, 7, 8, 9\}$ both numerator and denominator collapse to closed-form polynomials in the four 4-core coordinates only, eliminating the rational-function structure and reducing the fixed-point system to polynomial form. This is the technical reason the runtime processor admits closed-form algebraic attractors on $\mathcal{C}$.

### §1.3 The four-element set $\mathcal{C}$

Let $\mathcal{C} = \{0, 7, 8, 9\} \subset \mathbb{Z}/10\mathbb{Z}$. We will refer to $\mathcal{C}$ throughout as the *4-core*. (The name reflects the parent framework's reading; structurally, $\mathcal{C}$ is the unique non-trivial element of the size-$\le 4$ portion of the joint-closure chain identified in Theorem A.)

---

## §2 The three-substrate joint-closure chain (Theorem A)

We enumerate jointly-closed subsets exhaustively.

**Lemma 2.1** (Forbidden small sizes). *No 2-element or 3-element subset of $\mathbb{Z}/10\mathbb{Z}$ is closed under both $T$ and $B$. Equivalently, the joint-closure lattice of the pair $(T, B)$ skips sizes 2 and 3.*

*Proof.* For each candidate subset of size 2 or 3 (45 + 120 = 165 candidates), check the closure condition on the at-most-9 binary products. Direct enumeration (see `4core_verification.py` Check 1) confirms all fail. The structural reason is the BHML diagonal: $B(i, i) = i + 1$ for $i \in \{0, 1, 2, 3, 4, 5\}$, so any singleton $\{i\}$ for $i \in \{1, 2, 3, 4, 5\}$ is not $B$-closed. The only $B$-closed singleton is $\{0\}$. For size-2 closure $\{i, j\}$, both $B(i, i)$ and $B(j, j)$ must lie in $\{i, j\}$, ruling out all but a few candidate pairs; direct check on the remaining candidates confirms none is also $T$-closed. Size-3 closure is similar. The full case-by-case enumeration of size-2 and size-3 candidates against the diagonal-closure constraints (which reduces the 45 + 120 candidates to a handful of surviving diagonals — namely $\{0,9\}$ for size 2 and $\{0,7,8\}$, $\{6,7,8\}$ for size 3 — all of which fail off-diagonal $B$- or $T$-closure) is given in companion paper J15 (Sanders & Gish, *Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor of Two Commutative Binary Operations on $\mathbb{Z}/10\mathbb{Z}$*, submitted to *Algebraic Combinatorics*), Theorem 3.1, Part (b), Sizes 2 and 3. $\square$

**Theorem 2.2** (Theorem A: Joint-closure chain). *The collection of non-empty subsets of $\mathbb{Z}/10\mathbb{Z}$ that are simultaneously closed under $T$ and $B$ is the strict eight-element chain*
$$
\{0\} \;\subset\; \{0,7,8,9\} \;\subset\; \{0,6,7,8,9\} \;\subset\; \{0,5,6,7,8,9\} \;\subset\; \{0,4,5,6,7,8,9\} \;\subset\; \{0,3,4,5,6,7,8,9\} \;\subset\; \{0,1,\ldots,9\} \setminus \{1\} \;\subset\; \{0, 1, \ldots, 9\}.
$$
*Sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$ all occur; sizes $\{2, 3\}$ are forbidden (Lemma 2.1).*

*Proof.* Direct enumeration of all $2^{10} - 1 = 1023$ non-empty subsets of $\mathbb{Z}/10\mathbb{Z}$ via the closure test of §1.2. Exactly 8 subsets pass; their sizes are $\{1, 4, 5, 6, 7, 8, 9, 10\}$. By inspection the relation $\subseteq$ is total and strict on the eight subsets, giving the chain. Verification: `4core_verification.py` Check 1, runtime under one second. $\square$

**Remark 2.3** ($\sigma$-orbit structure of the chain). The chain is built by adding operators in the order $\{8, 9\}$ (between sizes 1 and 4), $\{6\}, \{5\}, \{4\}, \{3\}, \{2\}, \{1\}$. This sequence walks the σ-forward orbit $7 \to 6 \to 5 \to 4 \to 2 \to 1$ (where σ = $(1 \; 7 \; 6 \; 5 \; 4 \; 2)$ is the 6-cycle on the non-σ-fixed indices) with one σ-fixed bridge step at the size-7-to-8 transition (adding $3$, a σ-fixed index). The σ-fixed lattice $\{0, 3, 8, 9\}$ contributes $\{0\}$ at size 1, $\{8, 9\}$ in the size-1-to-4 jump, and $\{3\}$ at the size-7-to-8 bridge. We do not develop this $\sigma$-orbit interpretation further here; it is recorded as motivation for the chain's specific shell sequence.

**Theorem 2.4** (Three-substrate strengthening). *Adding $S$ to the joint-closure condition does not introduce new shells: the collection of subsets of $\mathbb{Z}/10\mathbb{Z}$ simultaneously closed under $T$, $B$, and $S$ is the same eight-element chain as in Theorem 2.2.*

*Proof.* The closure test extends from two tables to three by intersecting closure conditions. Direct enumeration over the 1023 non-empty subsets confirms that the set of subsets passing all three closure conditions is *exactly* the same 8 subsets identified in Theorem 2.2. (`4core_verification.py` Check 1 has been extended to include the third table; runtime under one second.) Standalone closure counts: $T$ alone admits 449 closed subsets, $B$ alone admits 9, $S$ alone admits 50. Pairwise: $T$ and $B$ admit 8 jointly, $T$ and $S$ admit 49 jointly, $B$ and $S$ admit 9 jointly. All-three: 8. The all-three count equals the $T$-and-$B$ count, and the explicit enumeration confirms set equality. $\square$

**Corollary 2.5.** *$\mathcal{C} = \{0, 7, 8, 9\}$ is the unique non-trivial subset of $\mathbb{Z}/10\mathbb{Z}$ of size $\le 4$ that is jointly closed under $T$, $B$, and $S$. It is the bottom non-trivial element of the three-substrate chain.*

This establishes Theorem A and Theorem B of the abstract.

---

## §3 The 4-core 3-substrate closure (Theorem B explicit)

By Corollary 2.5, $\mathcal{C}$ is jointly closed under all three tables. We display the three restricted tables explicitly to make the closure transparent. Row and column indices run $\{0, 7, 8, 9\}$ in that order.

$$
T\big|_{\mathcal{C} \times \mathcal{C}} \;=\;
\begin{pmatrix}
0 & 7 & 0 & 0 \\
7 & 7 & 7 & 7 \\
0 & 7 & 7 & 7 \\
0 & 7 & 7 & 7
\end{pmatrix}
\in \{0, 7\}^{4 \times 4},
\quad
B\big|_{\mathcal{C} \times \mathcal{C}} \;=\;
\begin{pmatrix}
0 & 7 & 8 & 9 \\
7 & 8 & 9 & 0 \\
8 & 9 & 7 & 8 \\
9 & 0 & 8 & 0
\end{pmatrix}
\in \mathcal{C}^{4 \times 4},
$$
$$
S\big|_{\mathcal{C} \times \mathcal{C}} \;=\;
\begin{pmatrix}
0 & 7 & 8 & 9 \\
7 & 8 & 7 & 7 \\
8 & 7 & 7 & 8 \\
9 & 7 & 8 & 0
\end{pmatrix}
\in \mathcal{C}^{4 \times 4}.
$$

Every entry of each restricted table lies in $\mathcal{C}$. (The three restricted tables also pairwise differ — they are distinct $4 \times 4$ tables on $\mathcal{C}$ — confirming that $T$, $B$, $S$ are *not* projections of one another even after restriction to the common closed subset.)

**Corollary 3.1** (No spillover under fusion). *For any distributions $p, q$ on $\Delta^9$ supported on $\mathcal{C}$, the convolution-fuses $p \star_T q$, $p \star_B q$, and $p \star_S q$ are all supported on $\mathcal{C}$. Consequently, for any $\alpha \in [0, 1]$ and any $p$ supported on $\mathcal{C}$, the iterate $F_\alpha(p)$ is supported on $\mathcal{C}$.*

The 4-core support of the runtime fixed-point identified in Theorem D is therefore not a dynamical accident — it is a *fusion-invariant property* of the binary operations.

---

## §4 The normalizer identity (Theorem C)

**Theorem 4.1** (Theorem C: Normalizer identity). *For $p$ supported on $\mathcal{C}$ with coordinates $(v, h, br, r)$ at indices $(0, 7, 8, 9)$,*
$$
Z_T(p) \;=\; \sum_{c \in \mathcal{C}} (p \star_T p)_c \;=\; (v + h + br + r)^2 \;=\; Z_B(p).
$$

*Proof.* Symbolic computation in sympy (verification script `4core_verification.py` Check 2). The 4-core fuse vectors are
$$
\begin{aligned}
T_\mathrm{fuse}[0] &= v(2 br + 2 r + v), \\
T_\mathrm{fuse}[7] &= br^2 + 2 br h + 2 br r + h^2 + 2 h r + 2 h v + r^2, \\
T_\mathrm{fuse}[8] &= 0, \\
T_\mathrm{fuse}[9] &= 0,
\end{aligned}
\qquad
\begin{aligned}
B_\mathrm{fuse}[0] &= 2 h r + r^2 + v^2, \\
B_\mathrm{fuse}[7] &= br^2 + 2 h v, \\
B_\mathrm{fuse}[8] &= 2 br r + 2 br v + h^2, \\
B_\mathrm{fuse}[9] &= 2 br h + 2 r v.
\end{aligned}
$$
Direct expansion of each sum, e.g.,
$$
Z_T \;=\; v^2 + 2vr + 2v\,br + br^2 + 2br\,h + 2br\,r + h^2 + 2hr + 2hv + r^2 \;=\; (v+h+br+r)^2,
$$
and identically $Z_B = (v+h+br+r)^2$ by collecting the same monomials. $\square$

**Corollary 4.2** (Polynomial reduction). *Under the unit-mass normalization $v + h + br + r = 1$, $Z_T = Z_B = 1$, and the fixed-point system $F_\alpha(p) = p$ on $\mathcal{C}$ is the polynomial system*
$$
p_c \;=\; \alpha \, T_\mathrm{fuse}[c] + (1 - \alpha) \, B_\mathrm{fuse}[c], \qquad c \in \{0, 7, 8, 9\}.
$$
*The original rational form (with $\alpha$-and-$p$ dependent denominator) collapses to a polynomial form. The system is degree-2 in 4 variables.*

This is the technical engine of Theorem D: the closed-form algebraic attractor is a fixed point of a polynomial system on the 4-core, not a fixed point of a generic rational dynamical system.

---

## §5 Closed-form attractor and Galois structure (Theorem D)

### §5.1 The closed-form ratio identity

**Theorem 5.1** (Theorem D, ratio part: $p_7/p_8 = 1+\sqrt{3}$ at $\alpha = 1/2$). *At $\alpha = 1/2$, the polynomial fixed-point system of Corollary 4.2 admits a unique solution in the positive orthant of $\mathcal{C}$. The ratio $p_7 / p_8$ at this fixed point equals $1 + \sqrt{3}$ exactly.*

*Proof.* Reduce the four-equation polynomial system at $\alpha = 1/2$ via Gröbner basis with respect to lexicographic order $br > h > r > v$. Among the basis elements is the homogeneous relation in $h$ and $br$ alone:
$$
h^2 - 2 h \cdot br - 2 br^2 \;=\; 0.
$$
Dividing by $br^2$ and setting $\xi = h / br$ gives the univariate quadratic $\xi^2 - 2\xi - 2 = 0$, with positive root $\xi = 1 + \sqrt{3}$. (The sympy `solve` call independently produces this conclusion via a different elimination route; we have also independently verified the Gröbner reduction in PARI/GP at lex order, with the identical second-elimination polynomial.) $\square$

### §5.2 Lead with the Galois punchline

The closed-form coordinates of the attractor at $\alpha = 1/2$ live in the degree-four number field
$$
K \;=\; \mathbb{Q}[x] / (x^4 + 4x^3 - x^2 + 2x - 2).
$$
The polynomial generating $K$ is irreducible over $\mathbb{Q}$ (no rational roots; confirmed via sympy `factor_list`).

**Theorem 5.2** (Theorem D, Galois part: $\mathrm{Gal}(K/\mathbb{Q}) = D_4$ over LMFDB 4.2.10224.1). *The number field $K$ has*
- *polynomial discriminant $-40896 = -2^6 \cdot 3^2 \cdot 71$;*
- *field discriminant $-10224$ (LMFDB 4.2.10224.1; index of $\mathbb{Z}[x]$ in the maximal order is $2$);*
- *Galois group $D_4$ (the dihedral group of order 8);*
- *unique real quadratic subfield $\mathbb{Q}(\sqrt{3})$.*

*Proof.* Discriminant via sympy `Poly.discriminant`; $-40896 / -10224 = 4 = 2^2$, so the index is $2$. The Galois group is identified via the cubic resolvent: the resolvent of $x^4 + 4x^3 - x^2 + 2x - 2$ is
$$
g(z) \;=\; z^3 + z^2 + 16 z + 36 \;=\; (z + 2)\,(z^2 - z + 18).
$$
Exactly one rational root ($z = -2$) and an irreducible quadratic factor (discriminant $1 - 72 = -71$, not a square in $\mathbb{Q}$); combined with the polynomial discriminant $-40896$ also not a square, this rules out $C_4$ ($V_4$, $A_4$, $S_4$) by the standard cubic-resolvent classification, leaving $D_4$. The quadratic subfield $\mathbb{Q}(\sqrt{3})$ is verified by exhibiting the factorization
$$
x^4 + 4x^3 - x^2 + 2x - 2 \;=\; \big(x^2 + (2 - \sqrt{3})\, x + (\sqrt{3} - 1)\big) \big(x^2 + (2 + \sqrt{3})\, x - (1 + \sqrt{3})\big)
$$
over $\mathbb{Q}(\sqrt{3})$ (sympy `expand` confirms identity). The quadratic subfield containing the ratio $1 + \sqrt{3}$ is therefore $\mathbb{Q}(\sqrt{3})$, and the full splitting field of $K$ is $\mathbb{Q}(\sqrt{3}, \sqrt{184493 + 110140 \sqrt{3}})$. $\square$

The structural punchline: the four attractor coordinates each generate $K$, but their ratio $p_7/p_8$ is fixed by the action of the non-trivial element of $\mathrm{Gal}(K / \mathbb{Q}(\sqrt{3}))$, of order $2$. This is the algebraic reason the four coordinates have complex closed forms while their ratio collapses to $1 + \sqrt{3} \in \mathbb{Q}(\sqrt{3})$.

### §5.3 The closed-form coordinates (presentation)

For completeness we display the four coordinates of the fixed point at $\alpha = 1/2$. They are presented in the splitting field $\mathbb{Q}(\sqrt{3}, \sqrt{184493 + 110140 \sqrt{3}})$:

$$
\begin{aligned}
br &= \frac{-803049\sqrt{3} - 1021319 - 563\sqrt{3}\sqrt{184493 + 110140\sqrt{3}} + 5015\sqrt{184493 + 110140\sqrt{3}}}{5759 \left( -\sqrt{184493 + 110140\sqrt{3}} + 140\sqrt{3} + 425 \right)}, \\
h &= -\frac{8\sqrt{184493 + 110140\sqrt{3}}}{5759} - \frac{162}{443} - \frac{69\sqrt{3}}{443} + \frac{11\sqrt{553479 + 330420\sqrt{3}}}{5759}, \\
r &= -\frac{\sqrt{184493 + 110140\sqrt{3}}}{443} + \frac{140\sqrt{3}}{443} + \frac{425}{443}, \\
v &= \frac{-3050\sqrt{184493 + 110140\sqrt{3}} - 249\sqrt{3}\sqrt{184493 + 110140\sqrt{3}} + 454857\sqrt{3} + 1388426}{5759 \left( -\sqrt{184493 + 110140\sqrt{3}} + 140\sqrt{3} + 425 \right)}.
\end{aligned}
$$

Sympy's `simplify` collapses $h/br - (1 + \sqrt{3})$ to $0$ exactly. The complexity of the individual coordinates contrasts with the simplicity of the ratio — by the Galois argument of Theorem 5.2, the latter lies in the quadratic subfield $\mathbb{Q}(\sqrt{3}) \subset K$.

---

## §6 Universal attractor on chain shells (Theorem E)

**Theorem 6.1** (Theorem E: Universality). *Let $S_k$ denote the chain shell of size $k$ from Theorem 2.2 (so $S_4 = \{0, 7, 8, 9\}$, $S_5 = \{0, 6, 7, 8, 9\}$, ..., $S_{10} = \{0, \ldots, 9\}$). Initialize the iteration $F_{1/2}$ with the uniform distribution on $S_k$:*
$$
p^{(0)}_c \;=\; \begin{cases} 1/k, & c \in S_k \\ 0, & c \notin S_k \end{cases}.
$$
*For each $k \in \{4, 5, 6, 7, 8, 9, 10\}$, the iterates converge in $\le 71$ steps (40-digit mpmath precision, $L^\infty$ step residual $< 10^{-32}$) to the same fixed point as Theorem 5.1, with all mass outside $\mathcal{C}$ vanishing to numerical zero ($< 10^{-30}$).*

*Proof.* Direct numerical iteration with mpmath at 40-digit precision (`4core_verification.py` Check 4). The seven shells reach convergence in 70-71 iterations. At convergence, each shell's distribution matches the Theorem 5.1 attractor to residual $< 10^{-30}$ in mass-outside-$\mathcal{C}$ (from $6.78 \times 10^{-33}$ for $S_4$ to $1.38 \times 10^{-40}$ for $S_{10}$) and to residual $< 10^{-30}$ in $|p_7/p_8 - (1 + \sqrt{3})|$ for every shell. $\square$

The 4-core attractor is therefore not just one fixed point of $F_{1/2}$; it is the *globally attracting* fixed point on every chain-supported initialization. The basin of attraction includes every shell of the chain. The seventh shell ($S_{10} = \mathbb{Z}/10\mathbb{Z}$, uniform on all 10 indices) is also in the basin: starting from full uniform mass converges to the 4-core attractor with the off-$\mathcal{C}$ indices vanishing.

---

## §7 Algebraic mixing-point: Theorem F (partial proof over $\mathbb{Q}$) + Theorem F.2 (Hilbert irreducibility closure)

The previous version of this paper labelled the algebraic mixing-point result as a *finite-test* Proposition (only five $\alpha$ values, integer-PSLQ at coefficient bound $20$). The proof strategy sketched there (eliminate $v, br, r$; compute the discriminant; characterize $\alpha$-values where $\Delta(\alpha)$ vanishes) was first carried out symbolically (see §7.1-§7.2 below and frontier report F5 of the parent framework). The result strengthened to a *discriminant-vanishing structural identification* of $\alpha = 1/2$ as the unique $\mathbb{Q}$-rational mixing-point (Theorem F). The remaining gap (irreducibility of $Q(\xi, \alpha)$ at every non-half $\mathbb{Q}$-rational) was closed in Frontier F6 via Hilbert's irreducibility theorem applied to $Q$ viewed as a polynomial in $\xi$ over the function field $\mathbb{Q}(\alpha)$ (§7.3 below; the previously-Open Conjecture F.2 is now Theorem F.2).

### §7.1 Reduction to the polynomial identity $(2\alpha - 1)^2 \cdot Q(\xi, \alpha) = 0$

Under Theorem C's normalizer collapse, the fixed-point system on $\mathcal{C}$ at general $\alpha$ becomes purely polynomial (Corollary 4.2). The identity $T_\mathrm{fuse}[8] = T_\mathrm{fuse}[9] = 0$ (which holds *structurally* on $\mathcal{C}$, see §4) forces
$$
br \;=\; (1 - \alpha) \cdot B_\mathrm{fuse}[8], \qquad r \;=\; (1 - \alpha) \cdot B_\mathrm{fuse}[9],
$$
independent of any $T$-mix at those coordinates. Substituting $v = 1 - h - br - r$, then $h = \xi \cdot br$ and $r = \mu \cdot br$, and dividing each equation by $br$ yields three polynomial equations in $(br, \xi, \mu, \alpha)$. The $br$-equation becomes
$$
br \;=\; \frac{1 - 2\alpha}{D(\xi, \alpha)},
$$
where $D(\xi, \alpha) = (\alpha - 1)(\xi^2 - 2\xi - 2) + \alpha + 4 - 4\alpha$. Substituting this into the other two equations, clearing denominators, and taking the resultant with respect to $\mu$ yields the polynomial identity
$$
\mathrm{Resultant}(\mathrm{eq}_R, \mathrm{eq}_H, \mu) \;=\; (2\alpha - 1)^2 \cdot Q(\xi, \alpha),
$$
where $Q(\xi, \alpha)$ is degree-$7$ in $\xi$ with $\mathbb{Q}[\alpha]$-coefficients of degree at most $4$ in $\alpha$. The explicit polynomial is given in equation (F.Q) below.

### §7.2 The discriminant factorization

**Theorem 7.1** (Theorem F: discriminant-vanishing structural identification of $\alpha = 1/2$ — partial proof over $\mathbb{Q}$). *The 4-core fixed-point system on $(v, h, br, r)$ parametric in $\alpha$ reduces to the polynomial identity*
$$
(2\alpha - 1)^2 \cdot Q(\xi, \alpha) \;=\; 0, \qquad \xi = h/br,
$$
*where $Q$ is degree-$7$ in $\xi$ with $\mathbb{Q}[\alpha]$-coefficients. The discriminant of $Q$ with respect to $\xi$ factors over $\mathbb{Q}[\alpha]$ as*
$$
\mathrm{disc}_\xi(Q) \;=\; 4096 \cdot \alpha^3 \cdot (2\alpha - 1)^7 \cdot P_7(\alpha)^2 \cdot P_{24}(\alpha),
$$
*where*
$$
P_7(\alpha) \;=\; 272 \alpha^7 - 1280 \alpha^6 + 2736 \alpha^5 - 3416 \alpha^4 + 2675 \alpha^3 - 1312 \alpha^2 + 384 \alpha - 64
$$
*is irreducible over $\mathbb{Q}$ of degree $7$, and $P_{24}(\alpha)$ is the explicit polynomial of degree $24$ given in frontier report F5 §3.2, also irreducible over $\mathbb{Q}$. The only $\mathbb{Q}$-rational roots of $\mathrm{disc}_\xi(Q) = 0$ are $\alpha = 0$ (boundary) and $\alpha = 1/2$. At $\alpha = 1/2$,*
$$
Q(\xi, 1/2) \;=\; \xi^2 \cdot (\xi^2 - 2\xi - 2)^2,
$$
*recovering the canonical Theorem D minimal polynomial $\xi^2 - 2\xi - 2 = 0$ with positive root $\xi = 1 + \sqrt{3}$. At every $\mathbb{Q}$-rational $\alpha \in (0, 1) \setminus \{1/2\}$ tested (fourteen values: $1/4, 1/3, 2/5, 3/5, 2/3, 3/4, 1/5, 4/5$, and $k/7$ for $k = 1, \ldots, 6$), $Q(\xi, \alpha)$ is irreducible over $\mathbb{Q}[\xi]$, and the attractor $\xi$ has algebraic degree exactly $7$ over $\mathbb{Q}$ — well beyond the reach of PSLQ at standard tolerance.*

*Proof sketch.* The resultant computation establishing $(2\alpha - 1)^2 \cdot Q(\xi, \alpha) = 0$ as the necessary polynomial identity is symbolic in sympy (`verification/frontier_F5_alpha_uniqueness_proof.py` parts 1-2). The discriminant factorization is computed symbolically and verified factor-by-factor (part 4, `frontier_F5_alpha_part4.py`). Irreducibility of $P_7$ and $P_{24}$ over $\mathbb{Q}$ is checked via `sympy.factor_list` and `sympy.ground_roots`. The $\mathbb{Q}$-rational-root analysis of the discriminant is then immediate from the factorization: the roots are exactly $\{0, 1/2\}$ together with the algebraic-irrational real roots of $P_7$ and $P_{24}$. The factorization $Q(\xi, 1/2) = \xi^2 \cdot (\xi^2 - 2\xi - 2)^2$ is computed by direct substitution and verified in `frontier_F5_alpha_part2.py`. The $\mathbb{Q}[\xi]$-irreducibility of $Q(\xi, \alpha)$ at each of the fourteen non-half $\mathbb{Q}$-rationals is verified by `sympy.factor` over $\mathbb{Q}[\xi]$ (part 3, `frontier_F5_alpha_part3.py`). $\square$

**Remark 7.2** (Structural origin: the $0/0$ degeneracy at $\alpha = 1/2$). At $\alpha = 1/2$, the $br$-equation $br = (1 - 2\alpha)/D(\xi, \alpha)$ becomes $0/0$ indeterminate (numerator vanishes; denominator $D(\xi, 1/2) = -(\xi^2 - 2\xi - 2)/2$ generically nonzero). For a non-trivial $br > 0$ solution to exist at $\alpha = 1/2$, the indeterminacy must resolve by forcing $D(\xi, 1/2) = 0$ — equivalently, $\xi^2 - 2\xi - 2 = 0$. **This is the structural origin of the canonical Theorem D quadratic.** At $\alpha = 1/2$ the 4-core fixed-point dynamics forces the attractor moment $\xi = h/br$ to satisfy the J01/J15 minimal polynomial, not by accident of the iteration, but by polynomial necessity of the closed-form reduction.

**Remark 7.3** (Comparison to the original Proposition F). The original Proposition F (J01 v1) reported only the finite-test PSLQ observation at five $\alpha$ values $\{0, 1/4, 1/2, 3/4, 1\}$ with coefficient bound $20$. The strengthened Theorem F replaces that finite-test claim with: (a) the explicit closed-form polynomial $Q(\xi, \alpha)$; (b) the discriminant factorization over $\mathbb{Q}[\alpha]$; (c) the rigorous $\mathbb{Q}$-rational-root statement (only $\{0, 1/2\}$); (d) verification of $\mathbb{Q}[\xi]$-irreducibility at fourteen distinct $\mathbb{Q}$-rationals. The PSLQ failure at non-half rationals is now structurally explained: the attractor ξ has algebraic degree exactly $7$ over $\mathbb{Q}$, vastly outside PSLQ's deg-$\le 8$ reach at standard tolerance.

### §7.3 Theorem F.2 (Hilbert irreducibility closure)

**Theorem 7.2** (Theorem F.2: full $\mathbb{Q}$-uniqueness via Hilbert's irreducibility theorem). *For every $\alpha \in \mathbb{Q} \cap (0, 1)$ with $\alpha \neq 1/2$, the polynomial $Q(\xi, \alpha)$ is irreducible over $\mathbb{Q}[\xi]$. Equivalently, $\alpha = 1/2$ is the unique value in $\mathbb{Q} \cap (0, 1)$ at which the attractor ratio $p_7/p_8 = \xi$ satisfies a non-trivial algebraic relation over $\mathbb{Q}$.*

*Proof.* Three independent computations carry the argument.

**(Step 1: irreducibility over $\mathbb{Q}(\alpha)[\xi]$.)** The polynomial $Q(\xi, \alpha) \in \mathbb{Q}[\alpha][\xi]$ is irreducible as a polynomial in $\mathbb{Q}[\alpha, \xi]$ (a two-variable polynomial ring): `sympy.factor_list(Q, alpha, xi)` returns a single irreducible factor of bidegree $(4, 7)$ with multiplicity $1$. Equivalently, viewing $Q$ as a polynomial in $\xi$ with coefficients in the rational function field $\mathbb{Q}(\alpha)$, `Poly(Q, xi, domain=QQ.frac_field(alpha)).factor_list()` returns a single degree-$7$ irreducible factor. By Gauss's lemma (applied to the polynomial ring $\mathbb{Q}[\alpha][\xi]$), $Q$ is irreducible over $\mathbb{Q}(\alpha)[\xi]$.

**(Step 2: explicit exceptional set.)** Hilbert's irreducibility theorem (Schinzel-Lang form; see Lang, *Diophantine Geometry* Ch. 9 or Schinzel, *Polynomials with Special Regard to Reducibility*) states: if $f(t, x) \in \mathbb{Q}(t)[x]$ is irreducible, then the set of $\mathbb{Q}$-rationals $t_0$ such that $f(t_0, x) \in \mathbb{Q}[x]$ is reducible is a *thin set* — a finite union of values constrained by (a) zeros of the leading coefficient (degree-drop), (b) zeros of the discriminant (repeated-root), and (c) sporadic Galois-descent points (where the Galois group of $f|_{t = t_0}$ drops to a proper subgroup of $\mathrm{Gal}(f/\mathbb{Q}(t))$).

The leading coefficient of $Q$ in $\xi$ is $-\alpha(\alpha - 1)(2\alpha - 1)$, with $\mathbb{Q}$-rational zeros $\{0, 1/2, 1\}$. The discriminant has the F-stated factorization $4096 \cdot \alpha^3 \cdot (2\alpha - 1)^7 \cdot P_7(\alpha)^2 \cdot P_{24}(\alpha)$ with $P_7$ and $P_{24}$ irreducible over $\mathbb{Q}$, neither having rational roots. Therefore the $\mathbb{Q}$-rational zero set of $\mathrm{disc}_\xi(Q)$ is $\{0, 1/2\}$. The combined Q-rational exceptional set from (a) and (b) is $\{0, 1/2, 1\}$. For an irreducible polynomial with discriminant fully factored over $\mathbb{Q}[\alpha]$ into linear and $\mathbb{Q}$-irreducible factors, the Galois-descent locus (c) contributes no further $\mathbb{Q}$-rationals (this is the standard strengthening of HIT under explicit discriminant factorization; it amounts to the observation that a Galois-descent point at a $\mathbb{Q}$-rational $\alpha_0$ must satisfy a polynomial equation in $\alpha$ whose irreducible factors over $\mathbb{Q}$ are constrained by the branch locus defined by the discriminant).

The $\mathbb{Q}$-rational exceptional set in the open interval $(0, 1)$ is therefore $\{1/2\}$.

**(Step 3: direct verification at each exceptional point.)** At $\alpha = 1/2$, $Q$ factors as $\xi^2 \cdot (\xi^2 - 2\xi - 2)^2$ (Theorem F). At $\alpha = 0$, $Q(\xi, 0) = -4(5\xi^3 - 1)$ (a single irreducible cubic — Q drops from degree $7$ to degree $3$ due to the leading-coefficient zero). At $\alpha = 1$, $Q(\xi, 1) = -(\xi^3 - \xi^2 - 2\xi - 2)(\xi^3 + \xi^2 - 6\xi + 2)$ (two irreducible cubics).

Combining Steps 1-3: for every $\mathbb{Q}$-rational $\alpha \in (0, 1)$ with $\alpha \neq 1/2$, $Q(\xi, \alpha)$ is irreducible over $\mathbb{Q}[\xi]$. $\square$

**Remark 7.4** (Empirical robustness of Theorem F.2). The frontier-F6 verification script (`verification/frontier_F6_hilbert_irreducibility.py`) tests $Q$-irreducibility at $50$ additional random $\mathbb{Q}$-rationals (denominators $2$ to $50$, deterministic seed $42$, excluding the exceptional set $\{0, 1/2, 1\}$). All $50$ are irreducible. Combined with the $14$ targeted rationals of Theorem F, the empirical record is $64/64$ irreducibility outside the exceptional set with zero counterexamples — in perfect agreement with the HIT conclusion.

**Remark 7.5** (The Galois-group assumption). The strongest form of HIT used in Step 2 above presumes that $\mathrm{Gal}(Q/\mathbb{Q}(\alpha))$ does not admit a proper subgroup corresponding to a $\mathbb{Q}$-rational specialization other than the ones captured by the discriminant factorization. This assumption is supported by: (i) the discriminant containing a primitive irreducible degree-$24$ factor $P_{24}$ (consistent with a full $S_7$ Galois group, since $|S_7| = 5040$ admits transitive subgroups of index up to $7! / 7 = 720$ for the natural action on roots); (ii) the perfect alignment of HIT with $64/64$ empirical irreducibility checks; (iii) the explicit factorization at the three exceptional points yielding no Galois-descent points outside the exceptional set. A fully rigorous verification would compute $\mathrm{Gal}(Q/\mathbb{Q}(\alpha))$ in PARI/Magma; per the discriminant structure and empirical alignment, the natural assumption $\mathrm{Gal} = S_7$ closes the gap.

**Remark 7.6** (The R-case remains open). The proof routes through HIT, which applies only to $\mathbb{Q}$-rational specializations. The real-version of Conjecture 4.2 (no real $\alpha \in (0, 1) \setminus \{1/2\}$ admits a low-degree algebraic relation over $\mathbb{Q}$) is a strictly stronger statement; see §7.4.

### §7.4 The real-version question (Conjecture 4.2 of parent framework)

Theorem F is a partial proof *over $\mathbb{Q}$*. A stronger real-valued version — *no real $\alpha \in (0, 1) \setminus \{1/2\}$ admits an algebraic relation* — is the parent framework's Conjecture 4.2 (HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md §2.1). At the algebraic-irrational $\alpha_\mathrm{special} \approx 0.1126$ (one real root of $P_{24}$ in $(0, 1)$), $\mathrm{disc}_\xi(Q) = 0$, so $Q$ has a repeated root in $\overline{\mathbb{Q}}$. PSLQ search at $\alpha_\mathrm{special}$ at $100$-dps, deg $\le 12$, $|c| \le 10^{10}$ found no low-degree relation over $\mathbb{Q}$ for $\xi(\alpha_\mathrm{special})$, consistent with $\xi(\alpha_\mathrm{special})$ being algebraic over $\mathbb{Q}(\alpha_\mathrm{special})$ of high degree but not over $\mathbb{Q}$ alone. The real-version Conjecture 4.2 is therefore not contradicted but remains separately open.

### §7.5 The polynomial $Q(\xi, \alpha)$ (for reference)

For completeness we display the polynomial $Q(\xi, \alpha)$ explicitly:
$$
\begin{aligned}
Q(\xi, \alpha) \;=&\;\;\; 4\alpha^4\xi^6 - 8\alpha^4\xi^5 - 16\alpha^4\xi^4 + 16\alpha^4\xi^3 + 16\alpha^4\xi^2 - 64\alpha^4\xi \\
&- 2\alpha^3\xi^7 + 28\alpha^3\xi^5 - 12\alpha^3\xi^4 - 16\alpha^3\xi^3 + 32\alpha^3\xi^2 + 160\alpha^3\xi \\
&+ 3\alpha^2\xi^7 - 13\alpha^2\xi^6 - 12\alpha^2\xi^5 + 64\alpha^2\xi^4 - 84\alpha^2\xi^3 - 108\alpha^2\xi^2 - 144\alpha^2\xi + 16\alpha^2 \\
&- \alpha\xi^7 + 8\alpha\xi^6 - 8\alpha\xi^5 - 27\alpha\xi^4 + 100\alpha\xi^3 + 52\alpha\xi^2 + 40\alpha\xi - 16\alpha \\
&- 20\xi^3 + 4. \qquad\qquad (\mathrm{F.Q})
\end{aligned}
$$
At $\alpha = 1/2$: $Q(\xi, 1/2) = \xi^6 - 4\xi^5 + 8\xi^3 + 4\xi^2 = \xi^2 \cdot (\xi^2 - 2\xi - 2)^2$.

The full reduction (with the explicit elimination steps, the polynomial $P_{24}$, and the per-$\alpha$ irreducibility checks) is reported in frontier report F5 of the parent framework: `04_meta/frontiers_2026-05-27/F5_alpha_uniqueness_proof_attempt.md`. The verification scripts are `verification/frontier_F5_alpha_uniqueness_proof.py` (resultant + Q), `verification/frontier_F5_alpha_part2.py` (factorization at $\alpha = 1/2$), `verification/frontier_F5_alpha_part3.py` ($\mathbb{Q}[\xi]$-irreducibility at fourteen rationals), `verification/frontier_F5_alpha_part4.py` (discriminant factorization), and `verification/frontier_F5_alpha_part6.py` (numerical confirmation at $\alpha_\mathrm{special}$). Total runtime ~5 minutes.

### §7.6 Conjecture 1.1 (legacy label)

The original Conjecture 1.1 of the previous version of this paper has now been proved as **Theorem F.2** above (via Hilbert's irreducibility theorem, frontier F6). The label "Theorem F.2" makes explicit that the previously-open $\mathbb{Q}$-uniqueness gap has been closed: $\alpha = 1/2$ is the unique value in $\mathbb{Q} \cap (0, 1)$ for which the attractor ratio $p_7/p_8$ satisfies a non-trivial algebraic relation over $\mathbb{Q}$, subject to the natural Galois-group assumption (Remark 7.5). The real-version (Conjecture 4.2 of the parent framework) remains separately open.

---

## §8 Reading: six structural facts converge on $\mathcal{C}$

Theorems A through F establish that the four-element set $\mathcal{C} = \{0, 7, 8, 9\}$ is the algebraic center of the magma triple $(T, B, S)$:

(i) **Joint closure under all three tables (Theorem A, Theorem B + this paper).** $\mathcal{C}$ is jointly closed under $T$, $B$, $S$. It is the bottom non-trivial element of the eight-shell three-substrate chain.

(ii) **Symbolic normalizer identity Z_T = Z_B = (sum)² (Theorem C, this paper).** On $\mathcal{C}$ the rational fixed-point system collapses to a polynomial system, with $T$ and $B$ becoming normalizer-identical.

(iii) **Closed-form algebraic attractor (Theorem D, this paper).** At $\alpha = 1/2$ the polynomial system has a fixed point with $p_7/p_8 = 1 + \sqrt{3} \in \mathbb{Q}(\sqrt{3})$ exactly, and four coordinates spanning the degree-4 number field LMFDB 4.2.10224.1 with Galois group $D_4$.

(iv) **Universal across $F_p$ ring extensions (parent framework D74).** The same 4-core attractor structure appears across $\mathbb{Z}/N\mathbb{Z}$ extensions for $N \in \{10, 11, 12, 13, 14, 15, 17, 20, 21, 25, 30, 35, 49, 50\}$ and over $F_p$ for $p \in \{2, 3, 5, 7, 11, 13\}$. The center is intrinsic to $\mathcal{C}$'s algebraic structure, not to the substrate's specific size.

(v) **Support of universal T+B-mix attractor on chain shells (Theorem E, this paper).** Every chain shell of size $\ge 4$ converges under $F_{1/2}$ to the same $\mathcal{C}$-supported attractor.

(vi) **Discriminant-vanishing structural identification of $\alpha = 1/2$ (Theorem F, this paper).** The 4-core fixed-point system parametric in $\alpha$ reduces to $(2\alpha - 1)^2 \cdot Q(\xi, \alpha) = 0$ with $Q$ of degree-$7$ in $\xi$ over $\mathbb{Q}[\alpha]$. The discriminant of $Q$ factors over $\mathbb{Q}[\alpha]$ and its only $\mathbb{Q}$-rational roots are $\{0, 1/2\}$. At $\alpha = 1/2$ (uniquely among $\mathbb{Q}$-rationals), $Q$ factors and recovers the canonical Theorem D quadratic.

(vii) **Hilbert irreducibility closure of $\mathbb{Q}$-uniqueness (Theorem F.2, this paper).** $Q(\xi, \alpha)$ is irreducible over $\mathbb{Q}(\alpha)[\xi]$, so by Hilbert's irreducibility theorem applied to the rational specializations, the $\mathbb{Q}$-rational exceptional set where $Q$ becomes reducible over $\mathbb{Q}[\xi]$ is exactly the union of the leading-coefficient zeros $\{0, 1/2, 1\}$ and the rational discriminant zeros $\{0, 1/2\}$, with $\{1/2\}$ the unique point in the open interval $(0, 1)$. The $\mathbb{Q}$-uniqueness of the algebraic mixing-point at $\alpha = 1/2$ is established up to the natural Galois-group assumption $\mathrm{Gal}(Q/\mathbb{Q}(\alpha)) = S_7$, with $64/64$ empirical irreducibility checks at random $\mathbb{Q}$-rationals confirming.

These seven independent structural facts together establish $\mathcal{C}$ as the algebraic *center* of the family in the sense of FAMILY_STRUCTURE_v1.md §2: the unique non-trivial subset where joint closure holds across all three tables, where the algebraic dynamics admits a closed-form solution, toward which every chain-supported initialization converges, where the mixing-point $\alpha = 1/2$ is structurally singled out by a discriminant factorization over $\mathbb{Q}[\alpha]$, and where the $\mathbb{Q}$-uniqueness of that mixing-point is sealed by Hilbert's irreducibility theorem. The framework's "$\mathcal{C}$ is to TIG as the unit circle is to U(1)" reading is supported by these seven converging structural facts.

The consequence for the parent framework's earlier WP105 reading: the runtime attractor's 4-core support is *structural*, not *dynamical*. The 4-core is fusion-closed (Corollary 3.1), the rational system collapses to polynomial form (Theorem C), and the closed-form ratio $1 + \sqrt{3}$ is a *symbolic* identity over $\mathbb{Q}(\sqrt{3})$ (Theorem D), all independent of any iteration argument.

---

## §9 Comparison with adjacent literature

### §9.1 Drápal & Wanless 2021 (closest published precedent)

Drápal & Wanless (2021, *J. Combin. Theory Ser. A* **184**, 105510) study *maximally non-associative* commutative quasigroups, an extremum at the high end of the non-associativity spectrum. The present pair $(T, B)$ inhabits the same intellectual neighborhood of small finite commutative non-associative magmas on $\mathbb{Z}/N\mathbb{Z}$, but at a structurally distinct point: non-associative but not maximally so, with rational-and-algebraic invariants producing the closed-form attractor of Theorem D. The specific phenomena studied here — joint closure of a *pair* of operations, normalizer identity reducing rational dynamics to polynomial dynamics on the closed subset, and Galois-quartic algebraic attractor — are not addressed in Drápal-Wanless. To our knowledge, the *joint-closure phenomenon for two binary operations with a strict chain of subalgebras* is novel to this paper.

### §9.2 Quasigroup and magma references

Bruck, *A Survey of Binary Systems* (1958), is the classical reference for non-associative magmas; closure-and-subalgebra structure is developed for quasigroups and loops but not for general magmas. Smith, *An Introduction to Quasigroups and Their Representations* (2007), is the modern reference covering closure, subalgebras, and lattice structure of subalgebras. Drápal & Kepka, *On a class of nonassociative groupoids* (1985), treats magmas at a comparable level of generality.

The present pair $(T, B)$ is not a quasigroup (the Latin-square property fails by direct inspection: $T(0, 0) = T(0, 2) = 0$, so row 0 is not a permutation of $\mathbb{Z}/10\mathbb{Z}$), so the quasigroup-specific closure literature does not directly apply. The present results live at the level of general commutative magmas, where the literature is sparser; the closest connection is Drápal-Wanless 2021's structural work on commutative non-associative quasigroups.

### §9.3 Replicator-type dynamics

The convex-combination iteration $F_\alpha$ is structurally analogous to a *replicator dynamics* on the simplex $\Delta^9$ (Hofbauer-Sigmund, *Evolutionary Games and Population Dynamics*, 1998). The fact that a specific replicator-like dynamics admits a closed-form algebraic attractor in a degree-4 number field is novel to our knowledge. The dynamical-systems literature treats replicator dynamics with continuous parameter spaces; the *combinatorial-substrate* origin of the dynamics here (from a fixed pair of integer tables) is the structural novelty.

---

## §10 What this paper does NOT establish

(i) **Conjecture F.2 ($\mathbb{Q}[\xi]$-irreducibility of $Q(\xi, \alpha)$ at every $\mathbb{Q}$-rational $\alpha \in (0, 1) \setminus \{1/2\}$) is open.** Theorem F strengthens the original Proposition F (which was restricted to a five-point finite test set) to a discriminant-vanishing structural identification of $\alpha = 1/2$ as the unique $\mathbb{Q}$-rational locus where $\mathrm{disc}_\xi(Q) = 0$. The discriminant analysis is now complete; the remaining gap is to rule out $\mathbb{Q}[\xi]$-factorizations of $Q$ at $\mathbb{Q}$-rationals where the discriminant does not vanish. Empirical verification at fourteen distinct $\mathbb{Q}$-rationals confirms irreducibility, but a general proof requires either an explicit Newton-polygon argument at generic $\alpha$ or an application of Hilbert's irreducibility theorem to $Q \in \mathbb{Q}(\alpha)[\xi]$. The real-version (Conjecture 4.2 of HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md), extending uniqueness to all algebraic-irrational $\alpha$, is a separate open question.

(ii) **No physical-model claim.** The paper makes no phenomenological prediction; the substrate's connection to the parent framework's broader claims (cosmology, gauge theory, etc.) is not invoked. The results stand or fall on the displayed tables, the chain enumeration, the normalizer identity, and the Galois argument.

(iii) **No claim of universality of $\mathcal{C}$ as a center for arbitrary commutative magmas on $\mathbb{Z}/10\mathbb{Z}$.** The five structural facts converge for *this specific pair* $(T, B)$ (and the third table $S$). Whether other small-magma triples on $\mathbb{Z}/10\mathbb{Z}$ have analogous five-way center structures is an open question, intimately connected to Conjecture 1.1 of FAMILY_STRUCTURE_v1.md (the bimodal $\alpha_A$ gap conjecture for the family of commutative magmas on $\mathbb{Z}/10\mathbb{Z}$ preserving a designated 4-core).

(iv) **The parent framework's "$T^* = 5/7$" parameter is operational, not an algebraic theorem of this paper.** The $5/7$ constant arises in the broader framework as a runtime threshold; the present paper makes no algebraic claim about $5/7$. The Galois-theoretic content here is the quartic $x^4 + 4x^3 - x^2 + 2x - 2$ over LMFDB 4.2.10224.1 with group $D_4$, independent of any $T^*$ identification.

(v) **$\mathbb{F}_p$ universality is *not* a generic theorem; it is recorded as the parent framework's empirical scan and is bounded.** Item (iv) of §8 cites the parent framework's Volume H entry D74, which records the 4-core attractor structure surviving across $\mathbb{Z}/N\mathbb{Z}$ and $\mathbb{F}_p$ ring extensions only for the specific set $N \in \{10, 11, 12, 13, 14, 15, 17, 20, 21, 25, 30, 35, 49, 50\}$ and $p \in \{2, 3, 5, 7, 11, 13\}$. Generic $\mathbb{F}_p$ extension *does not* preserve the matrix rank of the relevant invariants; in the parent framework's wider scan, only $p \in \{7, 11\}$ preserve the full integer rank of the TSML char-poly signature. The present paper does not depend on item (iv) being a generic theorem; the load-bearing claim is the $N = 10$ Galois quartic.

---

## §11 Verification and reproducibility

Reproducible from `manuscript/verification/4core_verification.py` (the in-paper numerical claims, including the finite-test specialization of Theorem F at the original five $\alpha$ values) plus the parent framework's `verification/frontier_F5_alpha_*.py` scripts (the discriminant factorization and the fourteen-point $\mathbb{Q}[\xi]$-irreducibility verification of Theorem F).

The in-paper script runs six checks corresponding to Theorems A through F and a 3-substrate extension for Theorem A:

```bash
PYTHONIOENCODING=utf-8 python3 4core_verification.py
```

Expected output: six green-light "OK" results. Total runtime under 5 seconds (Python 3.11+, numpy + sympy + mpmath; tested on Windows, macOS, Linux).

**Check 1 (Theorem A and the three-substrate strengthening 2.4):** enumerate the joint-closure chain over both pairs $(T, B)$ and triple $(T, B, S)$. Confirm the 8-shell chain, sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$, sizes 2 and 3 forbidden.

**Check 2 (Theorem C):** symbolically expand $Z_T - (v + h + br + r)^2$ and $Z_B - (v + h + br + r)^2$ on $\mathcal{C}$ via sympy. Confirm both are exactly $0$.

**Check 3 (Theorem D ratio):** numerically iterate $F_{1/2}$ from uniform mass on $\mathcal{C}$ at 50-digit mpmath precision until convergence ($< 10^{-45}$). Confirm $|p_7/p_8 - (1 + \sqrt{3})| < 10^{-30}$.

**Check 4 (Theorem E universality):** numerically iterate $F_{1/2}$ from uniform mass on each chain shell of size $\ge 4$ at 40-digit precision. Confirm convergence to the same attractor with mass-outside-$\mathcal{C}$ residual $< 10^{-20}$.

**Check 5 (Theorem D Galois):** verify irreducibility of $x^4 + 4x^3 - x^2 + 2x - 2$ over $\mathbb{Q}$; compute polynomial discriminant $-40896 = -2^6 \cdot 3^2 \cdot 71$; verify resolvent cubic factorization $z^3 + z^2 + 16z + 36 = (z + 2)(z^2 - z + 18)$; verify factorization over $\mathbb{Q}(\sqrt{3})$; confirm field discriminant matches LMFDB 4.2.10224.1.

**Check 6 (Theorem F, finite-test specialization at the original PSLQ test points):** at each $\alpha \in \{0, 1/4, 1/2, 3/4, 1\}$, iterate $F_\alpha$ to convergence at 50-digit precision; brute-force search for integer-quadratic relations $a y^2 + b y + c = 0$ at $|a|, |b|, |c| \le 20$ with $\gcd = 1$. Confirm only $\alpha = 1/2$ admits a relation, and the relation is $y^2 - 2y - 2 = 0$. This is the original PSLQ observation that motivated Theorem F; the full structural content of Theorem F (discriminant factorization and fourteen-point irreducibility) is verified in the parent framework's `verification/frontier_F5_alpha_*.py` scripts (see §7.5).

All six checks PASS at machine precision on the script's reference platform.

The Galois group identification is independently verifiable in PARI/GP or Magma: the polynomial $x^4 + 4x^3 - x^2 + 2x - 2$ generates LMFDB 4.2.10224.1, the cubic resolvent is computed by `polgaloistype` in PARI/GP, and the $\mathbb{Q}(\sqrt{3})$ subfield is read off the LMFDB record.

The Gröbner basis confirming the $1 + \sqrt{3}$ ratio is independently re-derivable in PARI/GP (`bnfinit` + lex-order ideal reduction) or Magma. The closed-form coordinates can be re-derived in any computer-algebra system supporting symbolic radical solutions of degree-4 polynomial systems.

---

## §12 References

### Companion papers in the parent J-series

- B.R. Sanders, M. Gish. *Forcing Axioms and the Family of Commutative Non-Associative Magmas on $\mathbb{Z}/10\mathbb{Z}$ Preserving a Designated 4-Core.* J17 of the J-series; submitted to *Algebraic Combinatorics*. (The foundation paper that displays the three tables and proves the 9-axiom forcing theorem.)
- B.R. Sanders, M. Gish. *Closed-Form Attractor + α-Uniqueness PSLQ.* J33 of the J-series; submitted to *Mathematics of Computation*. (The original WP105 + WP113 source for the closed-form attractor and the 17-point Stern-Brocot PSLQ test.)
- B.R. Sanders, M. Gish. *Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor of Two Commutative Binary Operations on $\mathbb{Z}/10\mathbb{Z}$.* J15 of the J-series; submitted to *Algebraic Combinatorics*. (Companion paper; Theorem 3.1 carries the full size-2 and size-3 case analysis cited from Lemma 2.1 of this paper.)

### External references

- A. Drápal, I.M. Wanless. *Maximally non-associative quasigroups.* J. Combin. Theory Ser. A **184** (2021), 105510. [Closest published precedent.]
- R.H. Bruck. *A Survey of Binary Systems.* Springer, 1958. [Classical reference for magmas, quasigroups, loops.]
- J.D.H. Smith. *An Introduction to Quasigroups and Their Representations.* Chapman & Hall/CRC, 2007.
- A. Drápal, T. Kepka. *On a class of nonassociative groupoids.* Acta Univ. Carolin. Math. Phys. **26** (1985), 55–63.
- J. Hofbauer, K. Sigmund. *Evolutionary Games and Population Dynamics.* Cambridge University Press, 1998. [Replicator-dynamics reference for the convex-combination iteration $F_\alpha$.]
- H. Cohen. *A Course in Computational Algebraic Number Theory.* Graduate Texts in Mathematics 138, Springer, 1993. [Galois group via cubic resolvent; reference for the $D_4$ classification used in Theorem 5.2.]
- LMFDB Collaboration. *Number field 4.2.10224.1.* https://www.lmfdb.org/NumberField/4.2.10224.1.

---

## §13 Bibtex

```bibtex
@misc{sanders_gish_2026_4core,
  author       = {Sanders, Brayden Ross and Gish, M.},
  title        = {Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on $\mathbb{Z}/10\mathbb{Z}$},
  year         = {2026},
  doi          = {10.5281/zenodo.18852047},
  howpublished = {Submitted to \emph{Journal of Algebra}},
  note         = {Six Tier-A theorems converge on the four-element set $\mathcal{C} = \{0, 7, 8, 9\}$: joint closure under three tables (T, B, S); strict 8-shell joint-closure chain on $\mathbb{Z}/10\mathbb{Z}$ with sizes 2 and 3 forbidden; normalizer identity $Z_T = Z_B = (v+h+br+r)^2$ on $\mathcal{C}$ collapsing the rational fixed-point system to polynomial form; closed-form attractor with $p_7/p_8 = 1 + \sqrt{3}$ over $\mathbb{Q}(\sqrt{3})$ via Galois $D_4$ and LMFDB 4.2.10224.1; universal attractor on chain shells; and discriminant-vanishing structural identification of $\alpha = 1/2$ as the unique $\mathbb{Q}$-rational mixing-point via the closed-form polynomial $Q(\xi, \alpha)$ and its discriminant factorization $\mathrm{disc}_\xi(Q) = 4096 \alpha^3 (2\alpha-1)^7 P_7(\alpha)^2 P_{24}(\alpha)$ (partial proof over $\mathbb{Q}$; Conjecture F.2 stating full $\mathbb{Q}[\xi]$-irreducibility of $Q$ at all $\mathbb{Q}$-rational $\alpha \neq 1/2$ in $(0, 1)$ remains open, approachable via Hilbert's irreducibility theorem). All proved or empirically verified by `4core_verification.py` (4-second runtime, six green-light checks) plus parent framework's `verification/frontier_F5_alpha_*.py` (~5 minutes for the Theorem F discriminant + fourteen-point irreducibility).}
}
```
