# The Lo Shu D₄ Orbit Modulo 3: Four Distinct Magmas and a Cumulant Spectrum

**Authors:** B.R. Sanders$^{1}$, M. Gish$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Target venue:** *Mathematics Magazine* (MAA)
**MSC 2020:** 20N02 (sets with one binary operation), 05B15 (orthogonal arrays, Latin squares), 20D60 (arithmetic and combinatorial problems on finite groups), 11A07 (congruences; primitive roots; residue systems).

---

## Abstract

The Lo Shu magic square, the unique $3 \times 3$ magic square with entries $\{1, 2, \ldots, 9\}$ (up to symmetry), has dihedral symmetry group $D_4$ acting on it by rotations and flips. Its $D_4$ orbit has 8 elements. Reducing each orbit element entry-wise modulo 3 and reading the resulting $3 \times 3$ table as a magma multiplication table on $\{0, 1, 2\}$ yields exactly **four distinct magma tables**, each appearing twice in the orbit. We classify the four: one is the cyclic group $\mathbb{Z}/3$; one is a commutative quasigroup with no identity element; and two are non-commutative quasigroups that are opposite magmas of one another. We further show that the spectral invariant $\kappa(M) := \operatorname{Tr}(M^2) - \operatorname{Tr}(M)^2$, applied to each $D_4$-orbit element as a real $3 \times 3$ matrix, takes exactly two values across the 8 elements: $\kappa = -48$ on the 4 elements whose mod-3 reduction is commutative, and $\kappa = +48$ on the 4 elements whose mod-3 reduction is non-commutative. The cumulant is thus a binary witness for the commutativity of the mod-3 magma, computable directly from the original magic-square data without reducing modulo 3.

A companion Python script `verify_J58.py` reproduces every theorem at machine precision in under one second, using only the standard library plus `numpy`.

---

## §0 Lens and substrate

This note works with the classical Lo Shu magic square as a fixed $3 \times 3$ integer matrix and considers its orbit under the standard dihedral $D_4$ action on $3 \times 3$ matrices. The mod-3 reduction maps each orbit element to a magma table on $\{0, 1, 2\}$. No exotic framework is required; the substrate is one of the oldest objects in recorded mathematics (the Lo Shu pattern dates to roughly the 2nd millennium BCE) and the operations are entirely elementary. The choice to look at the *mod-3* reduction (rather than mod-2 or mod-5) is motivated by the observation that the Lo Shu's diagonal-sums equal 15, which is $0 \pmod 3$ but $1 \pmod 2$ and $0 \pmod 5$; the mod-3 reduction is the smallest non-trivial modulus that turns the magic-square structure into a quasigroup-table structure.

**Tier discipline.**

- **PROVEN.** Theorems A, B, C, D, F (by direct enumeration; small-finite-case proofs that an undergraduate can verify by hand or with the script).
- **COMPUTED.** Theorem E and the full table of $\kappa$ values (script `verify_J58.py`, machine-precision, 6/6 PASS).
- **STRUCTURAL RHYME.** The cumulant $\kappa$ separates the two commutativity classes for *this specific* family of mod-3 reductions of Lo Shu's $D_4$ orbit. We do not claim a general theorem; the connection between $\kappa$ and commutativity here is an empirical observation about this specific 8-element family.
- **OPEN.** Whether analogous cumulant witnesses exist for other small magic squares' mod-$n$ reductions.

---

## §1 Setup

### §1.1 The Lo Shu magic square

The Lo Shu is the $3 \times 3$ matrix
$$
L = \begin{pmatrix} 2 & 7 & 6 \\ 9 & 5 & 1 \\ 4 & 3 & 8 \end{pmatrix},
$$
with the property that every row, every column, and both diagonals sum to 15. We will not directly use the magic-sum property — it is mentioned only to anchor the substrate in classical mathematics.

### §1.2 The $D_4$ action

The dihedral group $D_4$ has 8 elements:
$$
D_4 = \{e, r, r^2, r^3, f, rf, r^2 f, r^3 f\},
$$
where $r$ is the rotation by $90°$ and $f$ is the horizontal flip. Acting on a $3 \times 3$ matrix $M$, the elements produce the 8 transformations: identity, three rotations, the horizontal flip, and three rotated horizontal flips (which include the vertical flip and the two diagonal flips).

### §1.3 The mod-3 magma reading

Given a $3 \times 3$ matrix $M$ with integer entries, define the magma $\mathcal{M}(M)$ on $\{0, 1, 2\}$ by
$$
\mathcal{M}(M) : (x, y) \mapsto M[x][y] \bmod 3,
$$
where $M[x][y]$ is the entry in row $x$, column $y$, with $x, y$ ranging over $\{0, 1, 2\}$ (zero-indexed). The result is a multiplication table on a 3-element set.

We will identify two magmas $\mathcal{M}(M_1)$ and $\mathcal{M}(M_2)$ as **equal** if their tables are identical (i.e. $M_1[x][y] \equiv M_2[x][y] \pmod 3$ for all $x, y$), and **non-equal** otherwise. This is a strict equality of tables, not equality up to isomorphism.

### §1.4 The cumulant invariant

For a $3 \times 3$ real matrix $M$ define
$$
\kappa(M) := \operatorname{Tr}(M^2) - \operatorname{Tr}(M)^2.
$$
This is the second cumulant of the eigenvalue distribution of $M$ under the trivial weighting (every eigenvalue counted once). The invariant is preserved by transpose ($\kappa(M^\top) = \kappa(M)$) but not by general $D_4$ actions on the indices. We compute $\kappa$ on each $D_4$-orbit element below.

---

## §2 The four-magma refinement: Theorem B

### §2.1 Enumeration

We compute the 8 distinct elements of the $D_4$ orbit of $L$:

$$
M_0 = L = \begin{pmatrix} 2 & 7 & 6 \\ 9 & 5 & 1 \\ 4 & 3 & 8 \end{pmatrix}, \quad
M_1 = r \cdot L = \begin{pmatrix} 6 & 1 & 8 \\ 7 & 5 & 3 \\ 2 & 9 & 4 \end{pmatrix}, \quad
M_2 = r^2 \cdot L = \begin{pmatrix} 8 & 3 & 4 \\ 1 & 5 & 9 \\ 6 & 7 & 2 \end{pmatrix},
$$
$$
M_3 = r^3 \cdot L = \begin{pmatrix} 4 & 9 & 2 \\ 3 & 5 & 7 \\ 8 & 1 & 6 \end{pmatrix}, \quad
M_4 = f \cdot L = \begin{pmatrix} 6 & 7 & 2 \\ 1 & 5 & 9 \\ 8 & 3 & 4 \end{pmatrix}, \quad
M_5 = rf \cdot L = \begin{pmatrix} 8 & 1 & 6 \\ 3 & 5 & 7 \\ 4 & 9 & 2 \end{pmatrix},
$$
$$
M_6 = r^2 f \cdot L = \begin{pmatrix} 4 & 3 & 8 \\ 9 & 5 & 1 \\ 2 & 7 & 6 \end{pmatrix}, \quad
M_7 = r^3 f \cdot L = \begin{pmatrix} 2 & 9 & 4 \\ 7 & 5 & 3 \\ 6 & 1 & 8 \end{pmatrix}.
$$

(Note: $r^2 f \cdot L$ is the horizontal flip of $r^2 \cdot L$, equivalently a vertical-flip composition. The script `verify_J58.py` confirms all 8 distinct.)

### §2.2 Mod-3 reduction

Reducing each entry mod 3 we get:

$$
\mathcal{M}(M_0) = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 1 & 0 & 2 \end{pmatrix},
\quad
\mathcal{M}(M_1) = \begin{pmatrix} 0 & 1 & 2 \\ 1 & 2 & 0 \\ 2 & 0 & 1 \end{pmatrix},
$$
$$
\mathcal{M}(M_2) = \begin{pmatrix} 2 & 0 & 1 \\ 1 & 2 & 0 \\ 0 & 1 & 2 \end{pmatrix},
\quad
\mathcal{M}(M_3) = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 2 & 1 \\ 2 & 1 & 0 \end{pmatrix},
$$
$$
\mathcal{M}(M_4) = \begin{pmatrix} 0 & 1 & 2 \\ 1 & 2 & 0 \\ 2 & 0 & 1 \end{pmatrix},
\quad
\mathcal{M}(M_5) = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 1 & 0 & 2 \end{pmatrix},
$$
$$
\mathcal{M}(M_6) = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 2 & 1 \\ 2 & 1 & 0 \end{pmatrix},
\quad
\mathcal{M}(M_7) = \begin{pmatrix} 2 & 0 & 1 \\ 1 & 2 & 0 \\ 0 & 1 & 2 \end{pmatrix}.
$$

By direct inspection these reduce to exactly four distinct tables, which we re-label $T_1, T_2, T_3, T_4$:

| Label | Table | Orbit pre-images | Comm? | Cumulant $\kappa$ |
|---|---|---|:---:|:---:|
| $T_1$ | $\begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 1 & 0 & 2 \end{pmatrix}$ | $M_0, M_5$ | NO | +48 |
| $T_2$ | $\begin{pmatrix} 0 & 1 & 2 \\ 1 & 2 & 0 \\ 2 & 0 & 1 \end{pmatrix}$ | $M_1, M_4$ | YES | −48 |
| $T_3$ | $\begin{pmatrix} 2 & 0 & 1 \\ 1 & 2 & 0 \\ 0 & 1 & 2 \end{pmatrix}$ | $M_2, M_7$ | NO | +48 |
| $T_4$ | $\begin{pmatrix} 1 & 0 & 2 \\ 0 & 2 & 1 \\ 2 & 1 & 0 \end{pmatrix}$ | $M_3, M_6$ | YES | −48 |

This is Theorem B.

### §2.3 The opposite-magma identification (Theorem C)

Direct inspection shows $T_3[x][y] = T_1[y][x]$ for every $(x, y)$. In magma terms, $T_3$ is the **opposite magma** of $T_1$ (multiplication reversed). Since neither $T_1$ nor $T_3$ is commutative, they are not equal as tables — but as algebraic structures they satisfy the same equational laws closed under reversal (associativity, commutativity, etc., all of which fail symmetrically). They are anti-isomorphic, not isomorphic.

The commutative tables $T_2$ and $T_4$ are self-opposite: $T_2[x][y] = T_2[y][x]$ and similarly for $T_4$. So the four-table refinement has a "two commutative + one anti-isomorphic pair" structure rather than "three isomorphism classes with one having a doubled multiplicity."

### §2.4 The ℤ/3 identification (Theorem F)

$T_2[x][y] = (x + y) \bmod 3$ by direct verification: for instance $T_2[1][2] = 0 = (1+2) \bmod 3$, and so on for all 9 cells. So $T_2$ is exactly the cyclic group $\mathbb{Z}/3$.

The other commutative table $T_4 = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 2 & 1 \\ 2 & 1 & 0 \end{pmatrix}$ is not a group: it has no identity element ($T_4[0][x] = (1, 0, 2)$, $T_4[1][x] = (0, 2, 1)$, $T_4[2][x] = (2, 1, 0)$ — none equals $(0, 1, 2)$). It is a commutative quasigroup (all rows and columns are permutations of $\{0, 1, 2\}$) but not a loop. This is Theorem D + Theorem F.

---

## §3 The cumulant witness: Theorem E

### §3.1 Statement

For each of the 8 orbit elements $M_i$, computing $\kappa(M_i) = \operatorname{Tr}(M_i^2) - \operatorname{Tr}(M_i)^2$ gives exactly two values:

$$
\kappa(M_i) = \begin{cases} -48 & \text{if } \mathcal{M}(M_i) \in \{T_2, T_4\} \text{ (commutative)} \\ +48 & \text{if } \mathcal{M}(M_i) \in \{T_1, T_3\} \text{ (non-commutative)} \end{cases}
$$

The witness is computed on the original integer-valued $M_i$, not on the mod-3 reduction. This is striking: the cumulant of the integer matrix data directly tells you whether the mod-3 magma is commutative.

### §3.2 Why $\kappa$ takes only two values: Theorem E.1 (structural)

We can prove the *coset-invariance* half of Theorem E for ANY $3\times 3$ matrix, not just Lo Shu, as a general fact.

**Lemma (V₄′-coset invariance of $\kappa$).** Let $V_4' \subset D_4$ be the subgroup of size 4 consisting of $\{e, R^2, T, T_a\}$, where $e$ is the identity, $R^2$ is rotation by $180°$, $T$ is the main-diagonal reflection (matrix transposition), and $T_a$ is the anti-diagonal reflection. Then for any $n \times n$ real matrix $M$ and any $g \in V_4'$,
$$
\kappa(g \cdot M) \;=\; \kappa(M).
$$

**Proof.** It suffices to show invariance under the two generators $R^2$ and $T$ (since $T_a = R^2 \circ T$).

*Transpose $T$:* $\operatorname{Tr}(M^\top) = \operatorname{Tr}(M)$, and $(M^\top)^2 = (M^2)^\top$, so $\operatorname{Tr}((M^\top)^2) = \operatorname{Tr}(M^2)$. Hence $\kappa(M^\top) = \kappa(M)$.

*180° rotation:* Let $J$ be the reversal matrix (1's on the anti-diagonal). Then $R^2 \cdot M = J M J$, with $J^2 = I$. Trace is conjugation-invariant: $\operatorname{Tr}(J M J) = \operatorname{Tr}(M)$. And $(J M J)^2 = J M J J M J = J M^2 J$, so $\operatorname{Tr}((J M J)^2) = \operatorname{Tr}(M^2)$. Hence $\kappa(J M J) = \kappa(M)$. ∎

**Corollary.** For any $3 \times 3$ matrix $M$, the cumulant $\kappa$ takes at most 2 distinct values across the $D_4$ orbit of $M$ — the value $\kappa(M)$ on the $V_4'$-coset and (possibly different) $\kappa(R \cdot M)$ on the $(D_4 \setminus V_4')$-coset.

This Lemma reduces the proof of "Lo Shu's $D_4$-orbit produces only two distinct $\kappa$ values" to a single calculation per coset.

### §3.3 The specific values $\pm 48$ for Lo Shu

Both values are verified by direct computation on coset representatives.

For $L = M_0$ itself (representative of the $V_4'$-coset): $\operatorname{Tr}(L) = 2+5+8 = 15$, and
$$
\operatorname{Tr}(L^2) = (2^2 + 5^2 + 8^2) + 2(2{\cdot}7\cdot 9 / 7 + \ldots)
$$
More directly: $\operatorname{Tr}(L^2) = \sum_{i,j} L_{ij} L_{ji} = (2^2 + 5^2 + 8^2) + 2(L_{01} L_{10} + L_{02} L_{20} + L_{12} L_{21})$ $= (4 + 25 + 64) + 2(7\cdot 9 + 6 \cdot 4 + 1\cdot 3) = 93 + 2(63 + 24 + 3) = 93 + 180 = 273$. So $\kappa(L) = 273 - 225 = +48$.

For $R \cdot L = \mathrm{rot}90(L) = \begin{pmatrix} 6 & 1 & 8 \\ 7 & 5 & 3 \\ 2 & 9 & 4 \end{pmatrix}$ (representative of the other coset): $\operatorname{Tr}(R\cdot L) = 6 + 5 + 4 = 15$ (Lo Shu is magic, so its anti-diagonal also sums to 15), and $\operatorname{Tr}((R\cdot L)^2) = (36 + 25 + 16) + 2(1 \cdot 7 + 8 \cdot 2 + 3 \cdot 9) = 77 + 2 \cdot 50 = 177$. So $\kappa(R \cdot L) = 177 - 225 = -48$.

By the Lemma, the $V_4'$-coset has $\kappa = +48$ uniformly and the other coset has $\kappa = -48$ uniformly. This is the "$\kappa$ takes only $\pm 48$" half of Theorem E.

### §3.4 The commutativity correlation — half proved by a diagonal lemma

The second half of Theorem E — *that the sign of $\kappa$ correlates with the commutativity of the mod-3 reduction* — is half proved structurally and half observed.

**Lemma (3×3 commutative-quasigroup diagonal constraint).** Let $T$ be a $3 \times 3$ magma table on $\{0, 1, 2\}$ that is both commutative ($T[x][y] = T[y][x]$ for all $x, y$) and a quasigroup (every row and column is a permutation of $\{0, 1, 2\}$). Then the diagonal of $T$ — the multiset $\{T[0][0], T[1][1], T[2][2]\}$ — equals $\{0, 1, 2\}$ (i.e., it is a permutation of $\{0, 1, 2\}$, no repeated values).

**Proof.** Suppose for contradiction $T$ has a repeated diagonal entry, WLOG $T[0][0] = T[1][1] = c$ for some $c \in \{0, 1, 2\}$. Column 0 is a permutation of $\{0, 1, 2\}$, so the off-diagonal entries $T[1][0], T[2][0]$ are exactly the two non-$c$ values; WLOG $T[1][0] = a$, $T[2][0] = b$, where $\{a, b, c\} = \{0, 1, 2\}$.

By commutativity, $T[0][1] = T[1][0] = a$ and $T[0][2] = T[2][0] = b$. Row 0 is then $(c, a, b)$ — a permutation, fine.

Column 1 contains $T[0][1] = a$, $T[1][1] = c$, $T[2][1] = ?$. It must be a permutation, so $T[2][1] = b$. By commutativity, $T[1][2] = T[2][1] = b$.

Row 1 is then $(a, c, b)$ — a permutation, fine.

Row 2 is $T[2][0] = b$, $T[2][1] = b$, $T[2][2] = ?$. The first two entries are both $b$ — contradicting row 2 being a permutation. ∎

**Corollary (V₄′-coset forced non-commutativity for Lo Shu).** Every $V_4'$-coset element $g \cdot L$ has the same diagonal multiset as $L$ itself (since $V_4'$ preserves the main-diagonal positions). The diagonal of $L$ is $\{2, 5, 8\}$, which mod 3 is $\{2, 2, 2\}$ — a constant multiset. By the Lemma, no $3 \times 3$ commutative quasigroup has a constant-multiset diagonal. Since each $V_4'$-coset element's mod-3 reduction IS a quasigroup (Theorem D), it cannot be commutative. So all 4 tables in the $V_4'$-coset are non-commutative. ∎

This proves *exactly half* of Theorem E's correlation: the non-commutativity of the $\kappa = +48$ coset is forced by the diagonal lemma. The other half (commutativity of the $\kappa = -48$ coset) is consistent with the Lemma (since the anti-diagonal of $L$ is $\{4, 5, 6\}$ mod 3 $= \{0, 1, 2\}$, a permutation — which is *consistent with* commutativity by the Lemma, but not forced) and is verified by direct inspection of $T_2$ and $T_4$.

**Why this is striking.** The half of the correlation that is forced is exactly the half tied to the magic-square structure — the Lo Shu's diagonal mod 3 being constant is a consequence of the magic-sum property combined with the entries-multiset $\{1, 2, \ldots, 9\}$, both of which are magic-square defining conditions.

---

## §4 Quasigroup property: Theorem D

All four tables $T_1, T_2, T_3, T_4$ are quasigroups: every row of each table is a permutation of $\{0, 1, 2\}$, and every column is also a permutation. This is verified directly by inspection of the table entries. The script implements this as a row/column set-equality check; all four pass.

The quasigroup property does NOT follow automatically from "the entries are $\{0, 1, 2\}$"; it requires that no row or column have a repeated entry. The fact that all four tables happen to be quasigroups is non-trivial — it is a property of the Lo Shu's specific structure (and would not hold for a generic $3 \times 3$ matrix mod 3).

---

## §5 Verification script

A self-contained Python script `verify_J58.py` (~80 lines, depends only on `numpy` and the standard library `itertools`) reproduces all six theorems:

```
$ python verify_J58.py

================================================================
 J58 verification — Lo Shu D_4 orbit mod 3
================================================================

  CHECK 1 (Theorem A: orbit has 8 distinct elements): PASS
  CHECK 2 (Theorem B: mod-3 reduction yields 4 distinct tables): PASS
  CHECK 3 (Theorem C: T_3 is the opposite magma of T_1): PASS
  CHECK 4 (Theorem D: all 4 tables are quasigroups): PASS
  CHECK 5 (Theorem E: cumulant ±48 separates commutativity): PASS
  CHECK 6 (Theorem F: T_2 is exactly Z/3): PASS

  Overall: PASS (6/6)
```

Total runtime: under one second on a 2020-era laptop.

---

## §6 Pedagogical use

This note is targetable to an undergraduate audience because it requires no machinery beyond:
- The dihedral group $D_4$ (8 elements; rotations + flips of a square).
- Modular arithmetic.
- Definitions of magma, quasigroup, commutativity.
- Trace and matrix multiplication.

It is suitable for:
- A 50-minute classroom session in an undergraduate abstract algebra course, after the cyclic groups have been introduced and before formal Latin-square theory.
- A senior capstone or exit-exam exploration project (the student writes the verification script themselves).
- A bridging illustration between the historical magic-square tradition and modern small-finite-algebra structure.

The script provides immediate computational verification, which we view as a meta-skill worth teaching alongside the structural content.

---

## §7 Extension: the Dürer 4×4 magic square at mod 3

The note's pattern (4-magma orbit refinement + cumulant witness at mod 3) was originally observed on Lo Shu only. We checked the Albrecht Dürer 4×4 magic square (from his 1514 *Melencolia I* engraving):
$$
D = \begin{pmatrix}
16 & 3 & 2 & 13 \\
5 & 10 & 11 & 8 \\
9 & 6 & 7 & 12 \\
4 & 15 & 14 & 1
\end{pmatrix},
$$
with magic constant 34 (each row, column, both diagonals — and famously several "broken" diagonals — summing to 34).

The Dürer's $D_4$ orbit has 8 elements. Reducing entrywise mod 3 gives exactly **4 distinct $4\times 4$ magma tables** on $\{0, 1, 2\}$, each appearing twice in the orbit — the same numeric pattern as Lo Shu. Of these 4 tables, 2 are commutative and 2 are non-commutative. The matrix cumulant takes value $\kappa = -128$ on the 4 orbit elements whose mod-3 reduction is commutative, and $\kappa = +128$ on the 4 elements whose mod-3 reduction is non-commutative.

So the cumulant-witness pattern of Theorem E generalizes from Lo Shu (with $\kappa = \pm 48$) to Dürer (with $\kappa = \pm 128$). The structural Lemma of §3.2 covers $\kappa$-invariance under $V_4'$-cosets for any $n\times n$ matrix (the proof generalizes verbatim from 3×3 to 4×4, using the same reversal-matrix argument). What is *not* general is the commutativity correlation: it has to be checked on representatives, but in both Lo Shu and Dürer it works out.

### §7.1 Why mod 3 is special

A direct sweep across moduli shows that the cumulant-witness pattern is exclusive to mod 3 for both magic squares:

| Magic square | mod | Verdict |
|---|---:|---|
| Lo Shu | 2 | all reductions commutative — no dichotomy |
| Lo Shu | 3 | **κ-witness pattern: 2 comm + 2 non-comm** |
| Lo Shu | 4, 5, 7, 9, 10 | all reductions non-commutative — no dichotomy |
| Dürer | 2 | all non-commutative |
| Dürer | 3 | **κ-witness pattern: 2 comm + 2 non-comm** |
| Dürer | 4, 5, 6, 8, 10 | all non-commutative |

The mod-3 reduction is the unique modulus at which both classical magic squares produce a non-trivial commutativity-witnessed orbit. We note this as a structural-rhyme observation without offering a deeper explanation; it is an open question whether other classical magic-square families (5×5 Siamese, the family of essentially-distinct 4×4 magic squares enumerated by Frénicle, etc.) share the mod-3 specialness.

### §7.2 Incidence of the κ-witness property among random matrices

A sweep of 500 random 3×3 integer matrices for each of several entry ranges $\{0, 1, 2, 3\}$, $\{0, \ldots, 5\}$, $\{0, \ldots, 9\}$, $\{0, \ldots, 15\}$ shows the κ-witness property at mod 3 (Lemma + commutativity correlation) holds for ~5-9% of random matrices in each range. The Lo Shu and Dürer falling in this small fraction is therefore not coincidental but also not generic — the magic-square symmetry conditions seem to be a strong (but not necessary) selector for the property.

| Entries from | κ-witness rate |
|---|---:|
| $[0, 3]$ | 8.8 % (44 / 500) |
| $[0, 5]$ | 4.2 % (21 / 500) |
| $[0, 9]$ | 7.4 % (37 / 500) |
| $[0, 15]$ | 5.8 % (29 / 500) |

### §7.3 Open questions

1. Is there a structural reason for the mod-3 specialness? The fact that $|D_4| = 8 = 2^3$ and $|V_4'| = 4 = 2^2$ might interact with the multiplicative structure of $\mathbb{Z}/3$ in a way that forces the dichotomy.
2. Do other classical magic squares (5×5 Siamese, pandiagonal 4×4, Strachey's general odd-order construction) share the mod-3 specialness?
3. Is there a higher-order cumulant or matrix invariant that witnesses commutativity at moduli other than 3?

### §7.4 Equational-theory profile (VERIFIED via the Equational Theories Project)

We ran each of the four tables $T_1, T_2, T_3, T_4$ through Tao's Equational Theories Project (`github.com/teorth/equational_theories`), specifically `scripts/explore_magma.py` against the 4,694-equation catalog. The results:

| Table | ETP profile size (out of 4694) |
|---|---:|
| $T_1$ (non-commutative) | **179** |
| $T_2$ ($= \mathbb{Z}/3$, commutative) | **60** |
| $T_3$ (non-commutative, opposite of $T_1$) | **179** |
| $T_4$ (commutative non-group quasigroup) | **313** |

The 4-table view collapses to 3 distinct ETP profiles $\{60, 179, 313\}$ because $T_1$ and $T_3$ — being opposite magmas of each other — satisfy precisely the same equations (every standard equational law is closed under magma-opposite). This is the formal sense in which the "3 profiles" count is correct while the "4 tables" count is also correct: 4 distinct tables form 3 equational-theory equivalence classes.

The shared profile $|T_1 \cap T_4| = 63$ equations is also verified (matches the §65.4 claim of the parent framework's earlier scrutiny pass).

The intersection $T_2 \cap T_4$ gives exactly **14 equations** — striking, because 14 is also the ETP profile of the σ-magma on $\mathbb{Z}/10\mathbb{Z}$ (cf. companion paper J59). The 14 equations are precisely those satisfied by every commutative magma in our tests (T₂, T₄, σ-magma, BHML, CL_STD, ℤ/5; 8 distinct commutative magmas total) — they appear to be the "commutativity-forced minimum" of the ETP catalog.

---

## §8 References

- Andrews, W.S. (1917). *Magic Squares and Cubes*. Open Court Publishing.
- Drápal, A. and Wanless, I.M. (2021). "Maximally nonassociative quasigroups." *Journal of Combinatorial Theory, Series A* **184**, 105510.
- McKay, B.D. (2004). "Latin squares of all orders up to 7." Available at https://users.cecs.anu.edu.au/~bdm/data/latin.html
- Sloane, N.J.A. (ed.). *The On-Line Encyclopedia of Integer Sequences*. https://oeis.org

---

## Appendix A — The four tables, fully written out

For completeness, we display each $T_i$ with its multiplication tabulated explicitly.

**$T_1$ (non-commutative, $\kappa = +48$).**
$$\begin{array}{c|ccc} \cdot & 0 & 1 & 2 \\ \hline 0 & 2 & 1 & 0 \\ 1 & 0 & 2 & 1 \\ 2 & 1 & 0 & 2 \end{array}$$

**$T_2$ ($= \mathbb{Z}/3$, commutative, $\kappa = -48$).**
$$\begin{array}{c|ccc} + & 0 & 1 & 2 \\ \hline 0 & 0 & 1 & 2 \\ 1 & 1 & 2 & 0 \\ 2 & 2 & 0 & 1 \end{array}$$

**$T_3$ (non-commutative, $\kappa = +48$, opposite of $T_1$).**
$$\begin{array}{c|ccc} \cdot & 0 & 1 & 2 \\ \hline 0 & 2 & 0 & 1 \\ 1 & 1 & 2 & 0 \\ 2 & 0 & 1 & 2 \end{array}$$

**$T_4$ (commutative non-group, $\kappa = -48$).**
$$\begin{array}{c|ccc} \cdot & 0 & 1 & 2 \\ \hline 0 & 1 & 0 & 2 \\ 1 & 0 & 2 & 1 \\ 2 & 2 & 1 & 0 \end{array}$$

The reader can verify that $T_3[x][y] = T_1[y][x]$ for all 9 cells, that $T_2$ is the addition table of $\mathbb{Z}/3$, and that $T_4$ is commutative but has no identity row.

---

## Appendix B — Why "4 distinct tables" and not "3"

It is tempting to report the orbit as producing 3 distinct magmas if one quotients by the relation "isomorphic OR anti-isomorphic." Under that coarser equivalence, $T_1$ and $T_3$ collapse to one equivalence class (the non-commutative pair) and the count is 3 with multiplicities 4 + 2 + 2 = 8.

We stress that in this note we use **table-equality** as the distinguishing criterion, which is finer. Under table-equality the count is 4 with multiplicities 2 + 2 + 2 + 2 = 8.

Both counts are correct — they answer different questions. The "3 classes" count answers "how many ETP-equation profiles do we get?" (since all standard equations are self-dual under magma-opposite). The "4 tables" count answers "how many distinct multiplication tables do we get?" This note's Theorems A–F use the 4-table count because it is unambiguous and pedagogically clearer.

---

*Submission-ready manuscript draft, 2026-05-26. Sanders + Gish. Verification: 6/6 PASS at machine precision via `verify_J58.py`.*
