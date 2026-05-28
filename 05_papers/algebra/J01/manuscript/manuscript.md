# Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on $\mathbb{Z}/10\mathbb{Z}$

**Authors:** B.R. Sanders$^{1}$, M. Gish$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Target venue:** *Journal of Algebra*
**MSC 2020:** 20N02 (sets with one binary operation), 17A35 (general non-associative algebras), 11R32 (Galois theory of number fields), 12F10 (separable extensions, Galois theory), 17B20 (simple, semisimple, reductive Lie algebras).

---

## Abstract

Let $T, B : \mathbb{Z}/10\mathbb{Z} \times \mathbb{Z}/10\mathbb{Z} \to \mathbb{Z}/10\mathbb{Z}$ be the two commutative non-associative magmas displayed below in §1, and let $S$ denote a third commutative table on the same carrier (also displayed below in §1). We establish five independent structural facts plus a numerical observation (Proposition F) that converge on a designated four-element set $\mathcal{C} = \{0,7,8,9\} \subset \mathbb{Z}/10\mathbb{Z}$.

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

**Proposition F** (Algebraic mixing-point — finite-test partial uniqueness, **deliberately labelled Proposition rather than Theorem to signal its lower confidence level**). For $\alpha \in \{0, 1/4, 1/2, 3/4, 1\}$ tested by integer-PSLQ search at coefficient bound $20$ and 50-digit precision, only $\alpha = 1/2$ admits a small-coefficient quadratic relation between $p_7$ and $p_8$ at the attractor: the relation $y^2 - 2y - 2 = 0$. Verified empirically. We conjecture (Conjecture 1.1) that $\alpha = 1/2$ is the unique value in $\mathbb{Q} \cap (0, 1)$ at which $p_7/p_8$ admits an algebraic relation in any bounded degree-and-coefficient class. The general $\alpha$ symbolic uniqueness proof is open. **PSLQ establishes "no small-coefficient algebraic relation found within the tested precision," not algebraic-uniqueness proper; we therefore restrict the claim to the finite test set and demote the label from Theorem to Proposition.**

The companion verification script `4core_verification.py` reproduces **Theorems A through E and Proposition F** at machine precision (Python 3.11+, numpy, sympy, mpmath; 4-second runtime). The five Tier-A theorems (A-E) carry the load-bearing content; Proposition F is a finite-test empirical observation supporting the open Conjecture 1.1.

---

## §0 Lens and substrate

This paper works on $\mathbb{Z}/10\mathbb{Z}$ with a specific pair of commutative non-associative magma tables ($T$, $B$, displayed in §1) and a third table $S$ used for the three-substrate strengthening of Theorem A. These choices are *not derived from first principles*; they reflect a structural reading of $\mathbb{Z}/10\mathbb{Z}$ motivated by a ten-operator decomposition with names (VOID, LATTICE, COUNTER, PROGRESS, COLLAPSE, BALANCE, CHAOS, HARMONY, BREATH, RESET) at indices $0$ through $9$. The names are used for cross-referencing with the parent framework's documentation; no proof in this paper depends on them. The four-element set $\mathcal{C} = \{0, 7, 8, 9\}$ is the parent framework's "4-core" — the indices $\{V, H, Br, R\}$ in the named decomposition. The framework's claim is that this particular choice of substrate-and-tables produces theorems with surprising downstream connections (Galois $D_4$ over LMFDB 4.2.10224.1, the closed-form $1+\sqrt{3}$ ratio, universality of the mixed iteration's attractor). Whether other substrate-and-table choices give similarly rich connections is open.

The framing follows the Drápal & Wanless (2021, *J. Combin. Theory Ser. A* **184**, 105510) line of work on small finite commutative non-associative structures. Drápal-Wanless treat *maximally* non-associative quasigroups (an extremum at the high end of the non-associativity spectrum); the present pair $(T, B)$ inhabits the same intellectual neighborhood at a structurally distinct point — non-associative but not maximally so, with rational-and-algebraic invariants producing the closed-form attractor of Theorem D.

**Centerpiece framing.** The four-element set $\mathcal{C}$ plays the role of the algebraic *center* of this magma family. The relationship between $\mathcal{C}$ and the present pair $(T, B, S)$ is structurally analogous to the relationship between the unit circle $S^1$ and the group $U(1)$: $\mathcal{C}$ is the privileged invariant locus on which all of $T$, $B$, $S$ agree (Theorems A, B), where the rational-function dynamical system collapses to a polynomial system (Theorem C), where the closed-form algebraic attractor lives (Theorem D), and where every chain-supported initial condition converges (Theorem E). **Five Tier-A theorems (A through E) plus Proposition F** converge on this same four-element set. Proposition F (algebraic mixing-point) is a finite-test partial-uniqueness statement that empirically singles out $\alpha = 1/2$ among five tested values as the unique value admitting a small-coefficient algebraic relation between $p_7$ and $p_8$; the full-uniqueness claim is recorded as Conjecture 1.1 and remains open.

**Tier discipline (PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN).**

- **PROVEN.** Theorems A, B, C, D (closed-form ratio + Galois group via cubic resolvent), E. Joint-closure chain (Theorem A) is verified by exhaustive enumeration of $2^{10} - 1 = 1023$ subsets. Galois group $D_4$ is identified via the cubic resolvent: the resolvent cubic $z^3 + z^2 + 16z + 36 = (z + 2)(z^2 - z + 18)$ has exactly one rational root, the polynomial discriminant $-40896$ is not a square in $\mathbb{Q}$, and the irreducible quadratic factor has discriminant $-71$ also not a square; together these distinguish $D_4$ from $C_4$, $V_4$, $A_4$, and $S_4$. The closed-form ratio identity $p_7/p_8 = 1+\sqrt{3}$ is independently confirmed via Gröbner basis (PARI/GP) on the polynomial system at $\alpha = 1/2$.
- **COMPUTED.** Verification script `4core_verification.py` (this submission's `verification/` folder), six green-light checks at machine precision (4-second runtime, Python 3.11+, numpy + sympy + mpmath).
- **STRUCTURAL RHYME.** The Galois subfield $\mathbb{Q}(\sqrt{3}) \subset K$ recurs across several substrate invariants in the broader program of which this paper is part (internal documentation, not relied upon here). We mention this as motivation for why the ratio $p_7/p_8$ has the simpler degree-2 presentation despite the four coordinates living in a degree-4 field, but the Galois argument of Theorem D stands on its own.
- **OPEN.** Conjecture 1.1 ($\alpha = 1/2$ uniqueness across $\mathbb{Q} \cap (0,1)$) — see §6. The full symbolic-uniqueness proof requires a Gröbner-basis discriminant analysis at general $\alpha$, which sympy's default solver does not complete in reasonable time.

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

## §7 Algebraic mixing-point: Proposition F + Conjecture 1.1

WP105's original framing claimed the unique algebraic structure at $\alpha = 1/2$ as an open uniqueness statement. We sharpen the framing to *partial-uniqueness* + *open conjecture*.

**Proposition 7.1** (Proposition F: Partial uniqueness on a finite test set). *Among $\alpha \in \{0, 1/4, 1/2, 3/4, 1\}$, only $\alpha = 1/2$ admits a small-coefficient quadratic relation $a y^2 + b y + c = 0$ with $|a|, |b|, |c| \le 20$ at the attractor ratio $y = p_7/p_8$. The relation is $y^2 - 2y - 2 = 0$. **(Labelled Proposition rather than Theorem: PSLQ establishes "no small-coefficient algebraic relation found within the tested precision," not algebraic uniqueness proper.)***

*Proof.* Direct integer-PSLQ search at coefficient bound $20$, 50-digit mpmath precision (`4core_verification.py` Check 6). At $\alpha = 1/2$ the search finds $y^2 - 2y - 2 = 0$ to residual $< 10^{-25}$. At $\alpha \in \{0, 1/4, 3/4\}$ no relation is found within the bounds: the non-degenerate attractors have ratios $\approx 0.585, 1.462, 5.039$ respectively. At $\alpha = 1$ the iteration collapses to $\delta_H$ (no defined ratio). $\square$

**Conjecture 1.1** (Algebraic mixing-point: full uniqueness). *Among $\alpha \in \mathbb{Q} \cap (0, 1)$, $\alpha = 1/2$ is the unique value at which the attractor ratio $p_7/p_8$ admits any algebraic relation with rational coefficients of bounded degree-and-coefficient class.*

The proof strategy (sketched): (i) derive the BREATH equation closed form $\xi^2 \, br = 1/(1 - \alpha) - 2(r + v)$ with $\xi = h/br$; (ii) eliminate $v, br, r$ from the polynomial system to obtain a univariate polynomial $P(\xi; \alpha)$ over $\mathbb{Q}(\alpha)$; (iii) compute the discriminant $\Delta(\alpha) \in \mathbb{Q}(\alpha)$; (iv) characterize the $\alpha$ values at which $\Delta(\alpha)$ is a perfect square in $\mathbb{Q}$; (v) show $\alpha = 1/2$ is the unique such value in $(0, 1)$. Steps (ii)-(iii) require Gröbner basis computation at general $\alpha$; sympy's default solver does not complete them in available compute. Maple's `Groebner[Basis]` or Mathematica's `GroebnerBasis` with appropriate orderings is the natural next step. We leave this as the central open question of the paper.

A finer empirical test would extend the test set to $\alpha \in \{k/N : N \le 20, 0 < k < N\}$ (about 100 values), each tested at PSLQ bound $\ge 50$. This finer test is ~5 minutes of additional compute and would substantially strengthen the empirical evidence for Conjecture 1.1. We leave it for the next revision.

---

## §8 Reading: five structural facts converge on $\mathcal{C}$

Theorems A through F establish that the four-element set $\mathcal{C} = \{0, 7, 8, 9\}$ is the algebraic center of the magma triple $(T, B, S)$:

(i) **Joint closure under all three tables (Theorem A, Theorem B + this paper).** $\mathcal{C}$ is jointly closed under $T$, $B$, $S$. It is the bottom non-trivial element of the eight-shell three-substrate chain.

(ii) **Symbolic normalizer identity Z_T = Z_B = (sum)² (Theorem C, this paper).** On $\mathcal{C}$ the rational fixed-point system collapses to a polynomial system, with $T$ and $B$ becoming normalizer-identical.

(iii) **Closed-form algebraic attractor (Theorem D, this paper).** At $\alpha = 1/2$ the polynomial system has a fixed point with $p_7/p_8 = 1 + \sqrt{3} \in \mathbb{Q}(\sqrt{3})$ exactly, and four coordinates spanning the degree-4 number field LMFDB 4.2.10224.1 with Galois group $D_4$.

(iv) **Universal across $F_p$ ring extensions (parent framework D74).** The same 4-core attractor structure appears across $\mathbb{Z}/N\mathbb{Z}$ extensions for $N \in \{10, 11, 12, 13, 14, 15, 17, 20, 21, 25, 30, 35, 49, 50\}$ and over $F_p$ for $p \in \{2, 3, 5, 7, 11, 13\}$. The center is intrinsic to $\mathcal{C}$'s algebraic structure, not to the substrate's specific size.

(v) **Support of universal T+B-mix attractor on chain shells (Theorem E, this paper).** Every chain shell of size $\ge 4$ converges under $F_{1/2}$ to the same $\mathcal{C}$-supported attractor.

These five independent structural facts together establish $\mathcal{C}$ as the algebraic *center* of the family in the sense of FAMILY_STRUCTURE_v1.md §2: the unique non-trivial subset where joint closure holds across all three tables, where the algebraic dynamics admits a closed-form solution, and toward which every chain-supported initialization converges. The framework's "$\mathcal{C}$ is to TIG as the unit circle is to U(1)" reading is supported by these five converging structural facts.

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

(i) **Conjecture 1.1 ($\alpha = 1/2$ uniqueness across $\mathbb{Q} \cap (0, 1)$) is open.** Proposition F establishes partial uniqueness on the finite test set $\{0, 1/4, 1/2, 3/4, 1\}$. The full symbolic uniqueness proof is sketched in §7 but not carried out; the natural next step is a Gröbner-basis discriminant analysis at general $\alpha$ via Maple or Mathematica.

(ii) **No physical-model claim.** The paper makes no phenomenological prediction; the substrate's connection to the parent framework's broader claims (cosmology, gauge theory, etc.) is not invoked. The results stand or fall on the displayed tables, the chain enumeration, the normalizer identity, and the Galois argument.

(iii) **No claim of universality of $\mathcal{C}$ as a center for arbitrary commutative magmas on $\mathbb{Z}/10\mathbb{Z}$.** The five structural facts converge for *this specific pair* $(T, B)$ (and the third table $S$). Whether other small-magma triples on $\mathbb{Z}/10\mathbb{Z}$ have analogous five-way center structures is an open question, intimately connected to Conjecture 1.1 of FAMILY_STRUCTURE_v1.md (the bimodal $\alpha_A$ gap conjecture for the family of commutative magmas on $\mathbb{Z}/10\mathbb{Z}$ preserving a designated 4-core).

(iv) **The parent framework's "$T^* = 5/7$" parameter is operational, not an algebraic theorem of this paper.** The $5/7$ constant arises in the broader framework as a runtime threshold; the present paper makes no algebraic claim about $5/7$. The Galois-theoretic content here is the quartic $x^4 + 4x^3 - x^2 + 2x - 2$ over LMFDB 4.2.10224.1 with group $D_4$, independent of any $T^*$ identification.

(v) **$\mathbb{F}_p$ universality is *not* a generic theorem; it is recorded as the parent framework's empirical scan and is bounded.** Item (iv) of §8 cites the parent framework's Volume H entry D74, which records the 4-core attractor structure surviving across $\mathbb{Z}/N\mathbb{Z}$ and $\mathbb{F}_p$ ring extensions only for the specific set $N \in \{10, 11, 12, 13, 14, 15, 17, 20, 21, 25, 30, 35, 49, 50\}$ and $p \in \{2, 3, 5, 7, 11, 13\}$. Generic $\mathbb{F}_p$ extension *does not* preserve the matrix rank of the relevant invariants; in the parent framework's wider scan, only $p \in \{7, 11\}$ preserve the full integer rank of the TSML char-poly signature. The present paper does not depend on item (iv) being a generic theorem; the load-bearing claim is the $N = 10$ Galois quartic.

---

## §11 Verification and reproducibility

Reproducible from `manuscript/verification/4core_verification.py`. The script runs six checks corresponding to Theorems A through F and a 3-substrate extension for Theorem A:

```bash
PYTHONIOENCODING=utf-8 python3 4core_verification.py
```

Expected output: six green-light "OK" results. Total runtime under 5 seconds (Python 3.11+, numpy + sympy + mpmath; tested on Windows, macOS, Linux).

**Check 1 (Theorem A and the three-substrate strengthening 2.4):** enumerate the joint-closure chain over both pairs $(T, B)$ and triple $(T, B, S)$. Confirm the 8-shell chain, sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$, sizes 2 and 3 forbidden.

**Check 2 (Theorem C):** symbolically expand $Z_T - (v + h + br + r)^2$ and $Z_B - (v + h + br + r)^2$ on $\mathcal{C}$ via sympy. Confirm both are exactly $0$.

**Check 3 (Theorem D ratio):** numerically iterate $F_{1/2}$ from uniform mass on $\mathcal{C}$ at 50-digit mpmath precision until convergence ($< 10^{-45}$). Confirm $|p_7/p_8 - (1 + \sqrt{3})| < 10^{-30}$.

**Check 4 (Theorem E universality):** numerically iterate $F_{1/2}$ from uniform mass on each chain shell of size $\ge 4$ at 40-digit precision. Confirm convergence to the same attractor with mass-outside-$\mathcal{C}$ residual $< 10^{-20}$.

**Check 5 (Theorem D Galois):** verify irreducibility of $x^4 + 4x^3 - x^2 + 2x - 2$ over $\mathbb{Q}$; compute polynomial discriminant $-40896 = -2^6 \cdot 3^2 \cdot 71$; verify resolvent cubic factorization $z^3 + z^2 + 16z + 36 = (z + 2)(z^2 - z + 18)$; verify factorization over $\mathbb{Q}(\sqrt{3})$; confirm field discriminant matches LMFDB 4.2.10224.1.

**Check 6 (Proposition F):** at each $\alpha \in \{0, 1/4, 1/2, 3/4, 1\}$, iterate $F_\alpha$ to convergence at 50-digit precision; brute-force search for integer-quadratic relations $a y^2 + b y + c = 0$ at $|a|, |b|, |c| \le 20$ with $\gcd = 1$. Confirm only $\alpha = 1/2$ admits a relation, and the relation is $y^2 - 2y - 2 = 0$.

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
  note         = {Six independent structural facts converge on the four-element set $\mathcal{C} = \{0, 7, 8, 9\}$: joint closure under three tables (T, B, S); strict 8-shell joint-closure chain on $\mathbb{Z}/10\mathbb{Z}$ with sizes 2 and 3 forbidden; normalizer identity $Z_T = Z_B = (v+h+br+r)^2$ on $\mathcal{C}$ collapsing the rational fixed-point system to polynomial form; closed-form attractor with $p_7/p_8 = 1 + \sqrt{3}$ over $\mathbb{Q}(\sqrt{3})$ via Galois $D_4$ and LMFDB 4.2.10224.1; universal attractor on chain shells; partial $\alpha = 1/2$ uniqueness on a finite test set (Conjecture 1.1 stating full uniqueness across $\mathbb{Q} \cap (0, 1)$ remains open). All proved or empirically verified by `4core_verification.py` (4-second runtime, six green-light checks).}
}
```
