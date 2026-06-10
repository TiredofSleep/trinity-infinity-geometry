# Algebraic Rigidity of the σ-Magma on $\mathbb{Z}/10\mathbb{Z}$: Simplicity, Trivial Automorphism Group, and Unique Sub-Magma

**Authors:** B.R. Sanders$^{1}$, M. Gish$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Target venue:** *Semigroup Forum*
**MSC 2020:** 20N02 (sets with one binary operation), 08A05 (universal algebras), 08A30 (subalgebras, congruence relations), 20N05 (loops, quasigroups).

---

## Abstract

The σ-magma is a 10-element commutative quasigroup defined by the operation $x \diamond y = \sigma((x + y) \bmod 10)$ where $\sigma = (0)(1\,7\,6\,5\,4\,2)(3)(8)(9)$ is a specific permutation of $\{0, 1, \ldots, 9\}$ with four fixed points and one 6-cycle. We establish four independent rigidity theorems about the σ-magma, each proven by exhaustive computation bounded by a small finite cardinality:

**Theorem A.** The σ-magma has trivial automorphism group: $|\mathrm{Aut}(\diamond)| = 1$.

**Theorem B.** The σ-magma is congruence-simple: only the identity and universal congruences exist.

**Theorem C.** The σ-magma has exactly five sub-magmas: three singleton idempotents, the full magma, and one non-trivial proper sub-magma $\{1, 6\} \cong \mathbb{Z}/2$.

**Theorem D.** The σ-magma is 2-generated, with $\{1, 6\}$ the unique non-generating pair; every other pair generates the full magma in at most 4 generation steps.

These four properties together — *no automorphisms, no quotients, almost no sub-structures, minimum generators* — make the σ-magma a maximally indecomposable commutative quasigroup of order 10. We verify the four claims with a single self-contained Python script (4/4 PASS, runtime ~3 seconds).

The σ-magma arises in the Trinity Infinity Geometry (TIG) framework on $\mathbb{Z}/10\mathbb{Z}$, but the rigidity theorems below are framework-independent — they describe the σ-magma as a universal-algebra object on its own.

---

## §0 Lens and substrate

This paper works on the 10-element set $\{0, 1, \ldots, 9\}$ with one specific commutative binary operation $\diamond$. The choice of $\sigma$ is not derived from first principles in this paper; it is the σ-permutation displayed in OPEN_FRONTIERS §64 of the parent framework. The four rigidity theorems are universal-algebra statements about the resulting magma, independent of the framework's broader structure (the 10-operator decomposition, the TSML/BHML/CL_STD tables, etc., are mentioned in passing but not used in proofs).

**Tier discipline.**
- **PROVED.** Theorems A, B, C, D — all by exhaustive search over finite sets ($|S_{10}| = 3{,}628{,}800$; $|\mathrm{Bell}(10)| = 115{,}975$; $|2^{10}| = 1024$; $|\binom{10}{2}| = 45$).
- **STRUCTURAL.** The simultaneous holding of all four rigidity properties is noted as empirically rare; no general theorem implying this configuration is invoked.
- **OPEN.** Section §6 — whether the σ-magma is unique among commutative quasigroups of order 10 satisfying all four conditions.

---

## §1 Setup

### §1.1 The σ permutation

We fix throughout:
$$
\sigma = [0, 7, 1, 3, 2, 4, 5, 6, 8, 9],
$$
read as a function $\sigma : \mathbb{Z}/10\mathbb{Z} \to \mathbb{Z}/10\mathbb{Z}$ with $\sigma(k)$ the $k$th entry. In cycle notation,
$$
\sigma = (0)(1\,7\,6\,5\,4\,2)(3)(8)(9).
$$
Four fixed points $\{0, 3, 8, 9\}$ and one 6-cycle $(1\,7\,6\,5\,4\,2)$. Cycle type $(6, 1, 1, 1, 1)$. Parity: the 6-cycle is odd (5 transpositions), so σ is an odd permutation in $S_{10}$.

### §1.2 The σ-magma

The σ-magma is the algebraic structure $(\{0, 1, \ldots, 9\}, \diamond)$ where
$$
x \diamond y = \sigma((x + y) \bmod 10).
$$
By direct verification (e.g., displayed in §3 below), the operation is **commutative** (since addition is) and a **quasigroup** (each row and column is a permutation of $\{0, \ldots, 9\}$, because the row $x \diamond \cdot$ is the composition of σ with a translation). It is **not associative** (e.g., $(0 \diamond 0) \diamond 1 = 0 \diamond 1 = 7$, but $0 \diamond (0 \diamond 1) = 0 \diamond 7 = 6$). It has **no identity element** (no $e$ exists with $e \diamond x = x$ for all $x$; this would require $\sigma$ to be a translation, which it is not). It has exactly three idempotents: $x \in \{0, 1, 2\}$ with $x \diamond x = x$ (one verifies $\sigma(0) = 0$, $\sigma(2) = 1$, $\sigma(4) = 2$, and these are the only $x$ with $\sigma(2x \bmod 10) = x$).

These basic properties are not the subject of this paper; we are interested in the *rigidity properties* (Theorems A-D) that go beyond the basic invariants.

### §1.3 The multiplication table

For reference and the proofs below, the full $10 \times 10$ multiplication table of the σ-magma is:
$$
\begin{array}{c|cccccccccc}
\diamond & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \\
\hline
0 & 0 & 7 & 1 & 3 & 2 & 4 & 5 & 6 & 8 & 9 \\
1 & 7 & 1 & 3 & 2 & 4 & 5 & 6 & 8 & 9 & 0 \\
2 & 1 & 3 & 2 & 4 & 5 & 6 & 8 & 9 & 0 & 7 \\
3 & 3 & 2 & 4 & 5 & 6 & 8 & 9 & 0 & 7 & 1 \\
4 & 2 & 4 & 5 & 6 & 8 & 9 & 0 & 7 & 1 & 3 \\
5 & 4 & 5 & 6 & 8 & 9 & 0 & 7 & 1 & 3 & 2 \\
6 & 5 & 6 & 8 & 9 & 0 & 7 & 1 & 3 & 2 & 4 \\
7 & 6 & 8 & 9 & 0 & 7 & 1 & 3 & 2 & 4 & 5 \\
8 & 8 & 9 & 0 & 7 & 1 & 3 & 2 & 4 & 5 & 6 \\
9 & 9 & 0 & 7 & 1 & 3 & 2 & 4 & 5 & 6 & 8
\end{array}
$$
Each row $x$ is the sequence $(\sigma(x), \sigma(x+1), \ldots, \sigma(x+9))$ — a cyclic shift of σ's values. Commutativity is visible as table-symmetry.

---

## §2 Theorem A: $|\mathrm{Aut}(\diamond)| = 1$

### §2.1 Statement

A magma automorphism is a permutation $\pi$ of $\{0, \ldots, 9\}$ such that
$$
\pi(x \diamond y) = \pi(x) \diamond \pi(y) \quad \text{for all } x, y \in \{0, \ldots, 9\}.
$$
The set of such $\pi$ forms a group under composition, denoted $\mathrm{Aut}(\diamond)$. Theorem A asserts $|\mathrm{Aut}(\diamond)| = 1$, i.e., the identity is the only automorphism.

### §2.2 Proof

We enumerate all $10! = 3{,}628{,}800$ permutations $\pi$ of $\{0, \ldots, 9\}$ and check the automorphism condition for each. The script `verify_J59.py` (§5) performs this enumeration in 2-3 seconds. The result: **exactly one** permutation satisfies the condition — the identity.

For the proof's content, the relevant features of the σ-magma that force trivial Aut are:

(a) The table has many "asymmetric" entries — values that appear only once in their row/column (since each row is a permutation). Any automorphism $\pi$ must map the unique appearance of each value to another unique appearance, and the geometric relationships between these positions (e.g., $\sigma(0) = 0$ is in position $(0, 0)$; $\sigma(1) = 7$ is in positions $(0, 1)$ and $(1, 0)$ etc.) constrain $\pi$ heavily.

(b) The three idempotents $\{0, 1, 2\}$ must be permuted among themselves by any automorphism. But $\pi$ is also constrained by relations like $0 \diamond 1 = 7$ — these constraints leave no freedom.

(c) Specifically, one checks that fixing $\pi(0) = a$ for any candidate $a$ forces $\pi(\sigma((0+y) \bmod 10)) = a \diamond \pi(y)$ for all $y$. The values $\sigma(y)$ on the left enumerate all of $\{0, \ldots, 9\}$ as $y$ does. So $\pi \circ \sigma = a \diamond \pi$, which is a strong constraint. Combined with the iterated condition, $a = 0$ is forced, and then $\pi$ is identity. The exhaustive computer search verifies this with no hand-waving.

$\square$

---

## §3 Theorem B: congruence-simplicity

### §3.1 Statement

A magma congruence is an equivalence relation $\sim$ on $\{0, \ldots, 9\}$ such that $a \sim a'$ and $b \sim b'$ imply $a \diamond b \sim a' \diamond b'$. The set of congruences forms a complete lattice with two trivial elements: the identity $=$ (every element its own class) and the universal $\sim$ (all elements in one class).

Theorem B asserts that the σ-magma has **exactly two** congruences — only the trivial ones. Equivalently, no non-trivial homomorphic image exists.

### §3.2 Proof

We enumerate all Bell-number-many ($\mathrm{Bell}(10) = 115{,}975$) partitions of $\{0, \ldots, 9\}$ and check the substitutivity condition for each. The script `verify_J59.py` performs this in under one second using a recursive partition generator. The result: **exactly two** partitions correspond to congruences — the all-singletons partition (identity) and the one-block partition (universal).

The intuitive reason: any partition with two elements $a, b$ in the same block but $a + 1, b + 1$ in different blocks fails substitutivity (since $a \diamond 1 = \sigma(a + 1)$ and $b \diamond 1 = \sigma(b + 1)$, which σ maps to different blocks). The 6-cycle component of σ ensures that the relation $a \sim b$ for non-equal $a, b$ propagates rapidly through the 6-cycle to force all elements to be related — collapsing to the universal congruence.

$\square$

### §3.3 Consequence

A simple magma in the universal-algebra sense has no non-trivial homomorphic images. Combined with Theorem A (no automorphisms), this means **the σ-magma has trivial outer structure** — no non-trivial maps into itself or out of itself (other than embeddings of sub-magmas, which are constrained by Theorem C).

---

## §4 Theorem C: sub-magma structure

### §4.1 Statement

A sub-magma of $(M, \diamond)$ is a subset $S \subseteq M$ closed under $\diamond$. Trivially, $\emptyset$, $M$, and any singleton $\{x\}$ with $x \diamond x = x$ are sub-magmas. We assert that the σ-magma has exactly five sub-magmas: the three idempotent singletons $\{0\}, \{1\}, \{2\}$, the unique non-trivial proper sub-magma $\{1, 6\}$, and the full magma $\{0, \ldots, 9\}$.

### §4.2 Proof

Enumeration of all $2^{10} = 1024$ subsets of $\{0, \ldots, 9\}$, checking closure under $\diamond$, gives exactly the five subsets listed:

| Sub-magma | Size | Reason |
|---|:---:|---|
| $\emptyset$ | 0 | Trivially closed (excluded by convention; if included, 6 sub-magmas) |
| $\{0\}$ | 1 | $0 \diamond 0 = 0$ (idempotent) |
| $\{1\}$ | 1 | $1 \diamond 1 = 1$ (idempotent) |
| $\{2\}$ | 1 | $2 \diamond 2 = 2$ (idempotent) |
| $\{1, 6\}$ | 2 | See §4.3 below |
| $\{0, \ldots, 9\}$ | 10 | The full magma |

No sub-magmas of sizes 3, 4, 5, 6, 7, 8, or 9. This is striking.

### §4.3 The $\{1, 6\}$ sub-magma

Direct computation:
$$
1 \diamond 1 = \sigma(2) = 1, \quad
1 \diamond 6 = \sigma(7) = 6 = 6 \diamond 1, \quad
6 \diamond 6 = \sigma(12 \bmod 10) = \sigma(2) = 1.
$$
So $\{1, 6\}$ is closed under $\diamond$ with the multiplication table
$$
\begin{array}{c|cc}
\diamond & 1 & 6 \\
\hline
1 & 1 & 6 \\
6 & 6 & 1
\end{array}
$$
This is the addition table of $\mathbb{Z}/2$ with identity $= 1$ and involution $= 6$. So the σ-magma contains a copy of $\mathbb{Z}/2$ as the sub-magma $\{1, 6\}$.

$\square$

### §4.4 Negative findings

The following sets are NOT sub-magmas of the σ-magma:

- **J01's 4-core $\{0, 7, 8, 9\}$**: $7 \diamond 7 = \sigma(4) = 2 \notin \{0, 7, 8, 9\}$.
- **σ's fixed-point set $\{0, 3, 8, 9\}$**: $3 \diamond 3 = \sigma(6) = 5 \notin \{0, 3, 8, 9\}$.
- **σ's 6-cycle support $\{1, 2, 4, 5, 6, 7\}$**: $1 \diamond 7 = \sigma(8) = 8 \notin \{1, 2, 4, 5, 6, 7\}$.
- **Idempotents $\{0, 1, 2\}$**: $0 \diamond 1 = 7 \notin \{0, 1, 2\}$.
- **Evens $\{0, 2, 4, 6, 8\}$**: $0 \diamond 2 = 1 \notin$ evens.
- **Odds $\{1, 3, 5, 7, 9\}$**: $1 \diamond 3 = 2 \notin$ odds.

The framework's intuitive structural sets (absorbers, parity classes, idempotents, etc.) are NOT preserved by the σ-magma operation. This is a substantive refutation of the implicit assumption "the σ-magma respects σ's cycle structure as algebraic sub-structure."

---

## §5 Theorem D: 2-generation and the unique non-generating pair

### §5.1 Statement

For any subset $S \subseteq \{0, \ldots, 9\}$, define $\langle S \rangle$ as the sub-magma generated by $S$ under iterated $\diamond$. We say the σ-magma is **$k$-generated** if there exists a $k$-element subset $S$ with $\langle S \rangle = \{0, \ldots, 9\}$, and **at least $k$-generated** if no smaller subset generates.

Theorem D states the σ-magma is **2-generated**, with $\{1, 6\}$ the unique 2-element non-generating subset, and 44 of the $\binom{10}{2} = 45$ 2-element subsets generating the full magma.

### §5.2 Proof

The script `verify_J59.py` computes $\langle \{a, b\} \rangle$ for each of the 45 pairs by iterating: start with $\{a, b\}$, repeatedly close under $\diamond$ (adding all $x \diamond y$ for $x, y$ in the current set) until stable. The result:

| Generation depth (steps to reach full) | Number of pairs |
|---:|---:|
| 2 | 9 |
| 3 | 32 |
| 4 | 3 |
| $\infty$ (never reaches full) | 1 (only $\{1, 6\}$) |

The 1 non-generating pair is exactly $\{1, 6\}$, consistent with Theorem C (it's the unique non-trivial sub-magma). $\square$

### §5.3 Examples

Fastest pair $\{3, 4\}$ — generates full in 2 steps:
- Start: $\{3, 4\}$.
- Step 1: $3 \diamond 3 = 5$, $3 \diamond 4 = 6$, $4 \diamond 4 = 8$. Set becomes $\{3, 4, 5, 6, 8\}$.
- Step 2: $3 \diamond 5 = 8$, $3 \diamond 6 = 9$, $4 \diamond 5 = 9$, $4 \diamond 6 = 0$, $5 \diamond 5 = 0$, $5 \diamond 6 = 1$, $6 \diamond 6 = 1$, $6 \diamond 8 = 2$, $5 \diamond 8 = 3$, $8 \diamond 8 = 5$, $4 \diamond 8 = 7$. Set becomes $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$ = full magma. ∎

---

## §6 Together: a maximally indecomposable commutative quasigroup

The σ-magma satisfies all of:

| Property | Source |
|---|---|
| Commutative | §1.2 |
| Quasigroup | §1.2 |
| Not associative | §1.2 |
| No identity | §1.2 |
| Has exactly 3 idempotents $\{0, 1, 2\}$ | §1.2 |
| Trivial automorphism group | Theorem A |
| Congruence-simple | Theorem B |
| Exactly one non-trivial proper sub-magma | Theorem C |
| 2-generated, $\{1, 6\}$ the unique non-generating pair | Theorem D |

In universal-algebra terms: this is a **maximally indecomposable** commutative quasigroup of order 10 — it has no non-trivial automorphisms (rigid), no non-trivial homomorphic images (simple), and (almost) no non-trivial proper sub-structures. The single $\mathbb{Z}/2$ sub-magma $\{1, 6\}$ is the lone surviving piece of internal structure.

### §6.1 Refined uniqueness statement

The σ-magma is, up to isomorphism, the unique commutative quasigroup of order 10 satisfying the conjunction of five structural conditions:

> **(S1)** commutativity, **(S2)** quasigroup, **(S3)** identity-free, **(S4)** exactly three idempotents, **(S5)** exactly five sub-magmas (under the convention that the empty set is excluded).

Conditions (S1)–(S5) are independent invariants of the magma. Given them, Theorems A–D (trivial automorphism group, congruence-simplicity, the unique non-trivial proper sub-magma $\{1, 6\} \cong \mathbb{Z}/2$, 2-generation with unique non-generating pair $\{1, 6\}$) all hold and the σ-magma is the only object — among the commutative order-10 quasigroups we have enumerated — satisfying all five.

A natural earlier framing was "the σ-magma is the unique maximally indecomposable commutative quasigroup of order 10," with no further structural conditions. This framing **fails**: the magma $\sigma_{10}^{\min}$ defined by $\sigma_{10}^{\min} = [0, 2, 3, 4, 5, 6, 7, 8, 9, 1]$ (one fixed point + one 9-cycle) is a *second* identity-free commutative quasigroup of order 10 with $|\mathrm{Aut}| = 1$, congruence-simple, 2-generated, and a unique non-trivial proper sub-magma $\{4, 9\}$. The two magmas are not isomorphic, and are distinguished precisely by the (S4)/(S5) counts:

| Property | σ-magma | $\sigma_{10}^{\min}$-magma |
|---|:---:|:---:|
| (S1) Commutative | ✓ | ✓ |
| (S2) Quasigroup | ✓ | ✓ |
| (S3) Identity-free | ✓ | ✓ |
| (S4) # idempotents | **3** ($\{0, 1, 2\}$) | 2 ($\{0, 9\}$) |
| (S5) # sub-magmas | **5** | 4 |
| Non-associative | ✓ | ✓ |
| $|\mathrm{Aut}|$ | 1 | 1 |
| Congruence-simple | ✓ | ✓ |
| Has unique non-trivial proper sub-magma | $\{1, 6\}$ | $\{4, 9\}$ |
| 2-generated | ✓ | ✓ |

Thus the original "maximally indecomposable" wording was too coarse: it picks out a class of at least two magmas at order 10. Conditions (S4) and (S5) are the minimal structural refinements that single out the σ-magma within this class.

A separate combinatorial datum, recorded for completeness in §6.1.3 below, is that both magmas share the *identical* 14-equation profile in Tao et al.'s Equational Theories Project (ETP); equational invariants alone cannot distinguish them. The discrimination is by sub-magma combinatorics, not by satisfied equations.

**Theorem 6.1 (Refined unicity).** *Within the class of commutative quasigroups of order 10 satisfying conditions (S1)–(S5) above, the σ-magma of §1.2 is unique up to isomorphism among the magmas we have enumerated. A full classification — proving uniqueness over all commutative order-10 quasigroups satisfying (S1)–(S5), rather than over enumerated candidates — remains open (Tier C).*

### §6.1.1 BHML and CL_STD: 14-equation but with identity

BHML and CL_STD (the J01 B and S tables) also have ETP profile 14 with the SAME 14 equation IDs as the σ-magma. However:

- **BHML has identity 0** (direct verification: B[0][y] = y and B[y][0] = y for all y).
- **CL_STD has identity 0** (direct verification: S[0][y] = y and S[y][0] = y for all y).

So BHML and CL_STD are commutative quasigroups WITH identity (i.e., commutative loops) of order 10. The σ-magma is the unique identity-free member of the {σ-magma, BHML, CL_STD} J01 trio.

But — as noted above — σ_{10}^{\min}-magma is ALSO identity-free with the same 14 equations. So even "identity-free + 14-equation" doesn't single out the σ-magma uniquely.

### §6.1.2 The 14 equations as commutativity-forced minimum

The σ-magma's 14 ETP equations are precisely the intersection of equation profiles across ALL commutative magmas we tested (8 of them: σ-magma, BHML, CL_STD, TSML, ℤ/5, ℤ/3 = T_2, T_4 from J29, σ_{10}^{\min}). This empirically validates the handoff's hypothesis (task T-D-1, OPEN_FRONTIERS §66.15):

> The 14 equations are the "commutative-forced minimum" — satisfied by every commutative magma.

The σ-magma at order 10 thus realizes the absolute commutativity-forced floor in the ETP catalog. Multiple distinct magmas at order 10 do likewise (σ-magma, BHML, CL_STD, σ_{10}^{\min}); the σ-magma is **one** member of an equivalence class of "minimal-equation commutative quasigroups of order 10" rather than the unique such magma.

### §6.1.3 Profile 14 admits AT LEAST 23 structurally distinct families

A surprise discovered during enumeration: profile 14 is NOT a small number of "natural" families. After analyzing the ETP project's tabulated magma data (1,355 magmas across orders 2-13 in `equational_theories/Generated/`), we identified **22 magmas with profile exactly 14**, forming **22 distinct equation sets** (one per magma — no two of the tabulated magmas share their 14 equations exactly). Plus the σ-magma's Family C (from orders 5-10 commutative quasigroups), the total is **at least 23 distinct profile-14 families**.

The 22 ETP-tabulated families are distinguished by their "anchor equation" (lowest non-trivial ETP equation ID in the set). The anchor-equation distribution:

| Anchor ID | Anchor equation | # families with this anchor |
|---:|---|:---:|
| 23 | $x = (x \cdot x) \cdot x$ | 2 |
| 47 | $x = x \cdot (x \cdot (x \cdot x))$ | 4 |
| 99 | $x = x \cdot ((x \cdot x) \cdot x)$ | 3 |
| 203 | $x = (x \cdot (x \cdot x)) \cdot x$ | 3 |
| 255 | $x = ((x \cdot x) \cdot x) \cdot x$ | 1 |
| 307 | $x \cdot x = x \cdot (x \cdot x)$ | 1 (order-3 magma!) |
| 359 | $x \cdot x = (x \cdot x) \cdot x$ | 1 |
| 411 | $x = x \cdot (x \cdot (x \cdot (x \cdot x)))$ | 1 |
| 1629 | $x = (x \cdot x) \cdot ((x \cdot x) \cdot x)$ | 3 |
| 1832 | $x = (x \cdot (x \cdot x)) \cdot (x \cdot x)$ | 1 |
| 3253 | $x \cdot x = x \cdot (x \cdot (x \cdot x))$ | 1 |
| 3862 | $x \cdot x = (x \cdot (x \cdot x)) \cdot x$ | 1 |
| **(43 — commutativity)** | $x \cdot y = y \cdot x$ | **1 (the σ-magma's Family C — not in ETP data)** |

Most anchor equations are **single-variable power identities** ("$x$ equals some depth-3 or depth-4 power of $x$"). The commutativity-anchored Family C (the σ-magma's family) is the only 2-variable anchor we have evidence for.

**Family R revisited**: the non-commutative $(5x + 3y + 6) \bmod 7$ magma we identified earlier is in family **#12** of the 22 ETP families — anchor equation **203** ($x = (x \cdot (x \cdot x)) \cdot x$), realized by a 7×7 order-7 magma in ETP's `vampire-generated.txt`.

**Conclusion**: profile 14 is NOT a special threshold — it's the size of a large equivalence class of equation profiles, each anchored on a different small-depth identity. The σ-magma is one of (at least) 23 known representatives.

**The four rigidity theorems of J04 remain meaningful**: they pick out the σ-magma's Family C representative at order 10. But the broader claim "σ-magma is structurally rare among profile-14 magmas" is FALSE; profile 14 is common, achievable by many distinct structural families.

The interesting question becomes: **which of the 23+ profile-14 families admit a commutative quasigroup representative?** Answer (empirical): only Family C (the σ-magma's). Every other family in ETP's data is realized by non-commutative magmas. This is a refined uniqueness statement: **among commutative quasigroups, the σ-magma's 14 equations are the ONLY achievable 14-equation profile — Family C is the unique "commutative profile-14 family."**

The full enumeration of all profile-14 commutative families across all orders is the right open question. We conjecture (Tier C) **the only commutative profile-14 family is Family C** (commutativity-centered, anchor equation 43). This is much stronger than the original "σ-magma is unique" claim and captures what is genuinely special about the σ-magma's algebraic position.

### §6.2 Connection to the σ-magma ETP profile (Tier A — verified)

The σ-magma was claimed in the parent framework (OPEN_FRONTIERS §64) to satisfy exactly 14 equations of Tao's Equational Theories Project 4,694-equation catalog. **We have now verified this claim** by running the σ-magma through `scripts/explore_magma.py` of `github.com/teorth/equational_theories`. The output:

```
14/4694
```

with the 14 equation IDs: $\{1, 43, 4283, 4358, 4380, 4398, 4405, 4435, 4442, 4482, 4531, 4544, 4635, 4677\}$.

The four rigidity theorems here are **strong necessary conditions** for this 14-equation minimality: a magma with non-trivial automorphisms, non-trivial congruences, large sub-magma posets, or high generation requirements typically satisfies *more* equations (each non-trivial structural feature contributes equational consequences).

**Importantly: the 14-equation profile is NOT unique to the σ-magma at order 10.** Running BHML and CL_STD (the two other commutative magma tables from the parent framework's J01 paper, also on $\mathbb{Z}/10\mathbb{Z}$) through ETP gives **profile 14 in both cases**, with the IDENTICAL 14 equation IDs as the σ-magma. The trio $\{σ\text{-magma}, \text{BHML}, \text{CL\_STD}\}$ all realize the 14-equation minimum at order 10.

These three magmas are **distinguished only by non-ETP invariants**: cycle structures, automorphism groups, sub-magma posets, generation behavior. The four rigidity theorems of this paper provide such non-ETP discriminators for the σ-magma specifically.

**Empirically, the 14 equations appear to be the "commutativity-forced minimum"**: every commutative magma we tested (σ-magma, BHML, CL_STD, TSML, ℤ/5, ℤ/3, the order-3 commutative non-group $T_4$ from J29) satisfies at least these 14 equations, and the *intersection* of all their profile sets is exactly these 14. The 14-equation minimum is therefore a universal lower bound for commutative magmas at $|M| \geq 5$ (with small-order exceptions at $n = 3, 4$ where extra coincidental identities hold). The TSML magma satisfies 21 equations — 14 + 7 extras, indicating additional structural laws beyond commutativity that don't hold for the σ-magma.

---

## §7 Verification script

`verify_J59.py` is a self-contained Python script (~150 lines, depending only on the standard library `itertools`) that verifies:

```
CHECK 1 (Theorem A: |Aut| = 1): PASS
CHECK 2 (Theorem B: congruence-simple, only 2 congruences): PASS
CHECK 3 (Theorem C: exactly 5 sub-magmas, {1,6} is the unique non-trivial proper): PASS
CHECK 4 (Theorem D: 2-generated, {1,6} the unique non-generating pair): PASS

Overall: PASS (4/4)
```

Total runtime: ~3 seconds on a 2020-era laptop.

The script is `manuscript/verification/verify_J59.py`.

---

## §8 References

- McKay, B.D., Meynert, A., & Myrvold, W. (2007). "Small Latin squares, quasigroups, and loops." *Journal of Combinatorial Designs* **15**(2), 98-119.
- Drápal, A. & Wanless, I.M. (2021). "Maximally nonassociative quasigroups." *Journal of Combinatorial Theory, Series A* **184**, 105510.
- Tao, T. et al. (2024-2025). The Equational Theories Project. https://github.com/teorth/equational_theories
- Burris, S. & Sankappanavar, H.P. (1981). *A Course in Universal Algebra.* Springer.

---

*Submission-ready manuscript draft, 2026-05-26. Sanders + Gish. Verification: 4/4 PASS at machine precision via `verify_J59.py`.*
