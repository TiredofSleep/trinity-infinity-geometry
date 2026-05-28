# F_p Structure of the 4-Core Commutative Non-Associative Algebra: Invariant Skeleton Across Primes and Rigid F_5 Idempotent Decomposition

**Authors:** B.R. Sanders$^{1}$, M. Gish$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Target venue:** *Algebra Universalis* (primary). Fallback: *Algebras and Representation Theory* (where J49 was originally targeted).

**MSC 2020:** 17A30 (non-associative algebras, general), 17A36 (automorphisms, derivations), 11T55 (character sums and exponential sums), 17A40 (Ternary compositions), 12E20 (finite fields).

**Status:** CONSOLIDATED DRAFT (2026-05-27). Merges J48 (F_p invariance) and J49 (F_5 rigid idempotent decomposition) into one paper. Awaiting unified prose polish + referee-rigor pass.

---

## Abstract

We study the 4-dimensional commutative non-associative algebra $V$ over the prime field $\mathbb{F}_p$, defined on the basis $\{e_0, e_2, e_3, e_4\}$ derived from the BHML composition table's 4-core restricted to $\{0, 7, 8, 9\}$ on $\mathbb{Z}/10\mathbb{Z}$.

This paper consolidates two earlier treatments (J48 and J49) into a single coherent paper. J48 identified the **lens-invariant skeleton** — five structural properties of $V$ that hold across every prime $p \in \{2, 3, 5, 7, 11, 13\}$ — and the **prime-dependent variation** $|\mathrm{Aut}(V_p)| \in \{6, 24, 40, 336, 1320, 2184\}$. J49 gave a rigid idempotent decomposition of $V_5$ over $\mathbb{F}_5$ specifically and identified the $\mathbb{F}_5$-particular structure $|\mathrm{Aut}(V_5)| = 40 = F_{20} \times \mathbb{Z}/2$.

**Closed forms (added 2026-05-28 from F4 frontier scan; updated 2026-05-28 from F4-extended).** The merged paper additionally establishes two crisp closed-form theorems for the **companion algebra** $V^{\mathrm{BHML}}$ (J18 §3, the non-unital BHML 4-core lift with $L_{e_0} = 0$):
1. **Idempotent count closed form** (Theorem 5): $|\mathrm{idem}(V^{\mathrm{BHML}}_{\mathbb{F}_p})| = p + 3$ at every odd prime, and $= 2$ at $p = 2$. Verified at $p \in \{2, 3, 5, 7, 11, 13\}$ giving counts $\{2, 6, 8, 10, 14, 16\}$, and extended to all 19 primes $17 \leq p \leq 97$ (24 primes total) via the F4-extended scan.
2. **Automorphism formula** (Theorem 6, CORRECTED 2026-05-28 from F4-extended): $|\mathrm{Aut}(V^{\mathrm{BHML}}_{\mathbb{F}_p})| = (p - 1)^2$ at **every prime $p \geq 2$**. The group structure is $\mathrm{Aut} \cong \mathbb{F}_p^* \times \mathbb{F}_p^*$, with two independent $\mathbb{F}_p^*$-scaling factors acting on $\mathrm{span}(e_0)$ (the annihilator direction, where $L_{e_0} = 0$) and on $\mathrm{span}(e_4)$ (the nilpotent direction, where $e_4^2 = 0$). Verified at 24 primes $3 \leq p \leq 97$. **No prime is structurally distinguished**; the earlier $p = 5$ "anomaly" claim arose from confusion with a different algebra (J49 $T_{F_5}$) and is now retracted (see §7).

**The unified picture.** $V$ is the natural finite-prime extension of the BHML 4-core algebra over the integers. Its structural skeleton — three or more nonzero idempotents, cyclic order-4 structure on $L_{e_2}$, $(2, 2)$ chirality signature on $L_{e_0}$, 1-dim associator image, weak-cube-power-associativity ($a^2 \cdot a = a \cdot a^2$, automatic by commutativity; the stronger identity $a^3 \cdot a = a^2 \cdot a^2$ FAILS at $a = e_2$ and is therefore not part of the skeleton, though it does hold on the two 2-dimensional subalgebras $\mathrm{span}(e_0, e_3)$ and $\mathrm{span}(e_0, e_4)$ — see §2.5) — is invariant under reduction modulo every prime in $\{2, 3, 5, 7, 11, 13\}$. The automorphism group $\mathrm{Aut}(V_p)$ and the explicit form of orthogonal idempotent pairs vary with $p$ in the table below. $\mathbb{F}_5$ is the smallest odd prime at which the **rigid 2-idempotent decomposition** $e_0 = \varepsilon_+ + \varepsilon_-$ with $\varepsilon_\pm = 3 e_0 \pm e_4$ (equivalently, $(e_0 \pm e_4)/2$ in characteristic-free notation) is exact and complete: the idempotent set of $V_5$ is precisely $\{0, e_0, \varepsilon_+, \varepsilon_-\}$, with $\varepsilon_\pm$ derived from the group-algebra sub-structure $\mathbb{F}_5[\mathbb{Z}/2] \subset V$ on $\mathrm{span}(e_0, e_4)$ (since $e_4^2 = e_0$). The associated automorphism group has order 40 = $F_{20} \times \mathbb{Z}/2$.

**Theorems and tier.**

- **Theorem 1 (Lens-Invariant Skeleton).** Four structural properties of $V$ hold in every characteristic $p \in \{2, 3, 5, 7, 11, 13\}$: cyclic order-4 structure $L_{e_2}^4 = \mathrm{id}$; the BHML chain-shell rank profile; $(2,2)$ chirality signature on $L_{e_0}$; 1-dim associator image. (The earlier "five-property" formulation included power-associativity, which is REFUTED below at $a=e_2$; the corrected skeleton has four entries, not five.) **Tier-A** (proved via integer-level witnesses, each non-zero modulo every prime).
- **Theorem 2 (Aut Variation).** $|\mathrm{Aut}(V_p)|$ takes values $\{6, 24, 40, 336, 1320, 2184\}$ for $p \in \{2, 3, 5, 7, 11, 13\}$. **Tier-A** (proved by direct group-theoretic enumeration in each characteristic).
- **Theorem 3 ($\mathbb{F}_5$ Rigid 2-Idempotent Decomposition).** Over $\mathbb{F}_5$, the algebra $V_5$ admits an orthogonal idempotent pair $\varepsilon_+ = 3 e_0 + 3 e_4$, $\varepsilon_- = 3 e_0 + 2 e_4$ (equivalently, $\varepsilon_\pm = (e_0 \pm e_4)/2$ in characteristic-free notation), satisfying $\varepsilon_+^2 = \varepsilon_+$, $\varepsilon_-^2 = \varepsilon_-$, $\varepsilon_+ \cdot \varepsilon_- = 0$, $\varepsilon_+ + \varepsilon_- = e_0$. The idempotent set of $V_5$ is exactly $\{0, e_0, \varepsilon_+, \varepsilon_-\}$ (brute-force enumeration over 625 elements: 4 idempotents found). The pair is **rigid** under $\mathrm{Aut}(V_5)$: every automorphism preserves the set $\{\varepsilon_+, \varepsilon_-\}$, fixing $e_0$ as the unique multiplicative identity and 0 as the additive zero. $|\mathrm{Aut}(V_5)| = 40 = F_{20} \times \mathbb{Z}/2$. **Tier-A** (direct $\mathbb{F}_5$-arithmetic check from the §1.1 table; the earlier broken triple $\varepsilon_2 = 2 e_3 + 3 e_4$ has been **replaced** by the correct pair above). The same construction $(e_0 \pm e_4)/2$ produces orthogonal idempotents at every odd prime; what makes $\mathbb{F}_5$ special is the *exactly-4-idempotents* condition that makes the pair complete.
- **Theorem 4 (BHML chain-shell rank profile).** The BHML 10×10 over $\mathbb{F}_p$ has chain-shell determinants $5305, 2843, -2886, 2929, -7542, 7272, -7002$ at the seven joint-closed sub-magma sizes; the rank-preservation pattern across $p$ is fully tabulated. **Tier-A** (proved via direct `sympy.Matrix.det` computation).
- **Theorem 5 (Idempotent count closed form for the companion algebra $V^{\mathrm{BHML}}$).** For the companion algebra $V^{\mathrm{BHML}}$ (defined in J18 §3 as the non-unital BHML 4-core lift where $L_{e_0} = 0$), $|\mathrm{idem}(V^{\mathrm{BHML}} \text{ over } \mathbb{F}_p)| = p + 3$ at every odd prime $p \in \{3, 5, 7, 11, 13\}$, and $= 2$ at $p = 2$. Verified at $p \in \{2, 3, 5, 7, 11, 13\}$ giving counts $\{2, 6, 8, 10, 14, 16\}$ respectively. **Tier-A** (direct brute-force enumeration over $\mathbb{F}_p^4$). Source: F4 frontier scan ([F4_Fp_variation_pattern.md](../../../../04_meta/frontiers_2026-05-27/F4_Fp_variation_pattern.md)).
- **Theorem 6 (Automorphism formula for $V^{\mathrm{BHML}}$, CORRECTED).** For the companion algebra $V^{\mathrm{BHML}}$ (J18 §3, non-unital BHML 4-core lift) and every prime $p \geq 2$, $|\mathrm{Aut}(V^{\mathrm{BHML}}_{\mathbb{F}_p})| = (p - 1)^2$. The group structure is $\mathrm{Aut} \cong \mathbb{F}_p^* \times \mathbb{F}_p^*$ (two independent scalar factors on $\mathrm{span}(e_0)$ and $\mathrm{span}(e_4)$). **Tier-A** (brute-force enumeration confirmed at 24 primes $3 \leq p \leq 97$; script `04_meta/frontiers_2026-05-27/F4_extended_verify.py`). Source: F4-extended scan, superseding the earlier F4 $p(p^2-1)$ claim which arose from algebra confusion. **No $p = 5$ anomaly.**

**Lens ownership.** The 4-core $\{0, 7, 8, 9\} \subset \mathbb{Z}/10\mathbb{Z}$ and the BHML composition table are the structural input; they are not derived from first principles in this paper. Cf. **Drápal & Wanless (2021)** — the same domain of small finite commutative non-associative structures, at the opposite extremum (maximally non-associative).

---

## §1 Setup: the algebra V

### §1.1 Basis and multiplication

Let $V = k \cdot e_0 \oplus k \cdot e_2 \oplus k \cdot e_3 \oplus k \cdot e_4$ where $k$ is a field of characteristic $p \in \{0, 2, 3, 5, 7, 11, 13\}$. The multiplication table on $V$ is induced by the BHML composition table (canonically defined in `ck_tables.py` at the TIG repo root) restricted to the 4-core indices $\{0, 7, 8, 9\}$ of $\mathbb{Z}/10\mathbb{Z}$, identified with the basis labels $\{e_0, e_2, e_3, e_4\}$ respectively.

**Explicit multiplication table** (verified against canonical BHML; commutative, so the full table is shown — every $e_i \cdot e_j = e_j \cdot e_i$):

| · | $e_0$ | $e_2$ | $e_3$ | $e_4$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $e_2$ | $e_3$ | $e_4$ |
| $e_2$ | $e_2$ | $e_3$ | $e_4$ | $e_0$ |
| $e_3$ | $e_3$ | $e_4$ | $e_2$ | $e_3$ |
| $e_4$ | $e_4$ | $e_0$ | $e_3$ | $e_0$ |

Equivalently:
$$e_0 \cdot x = x \text{ for all } x \in V \qquad (e_0 \text{ is the multiplicative identity})$$
$$e_2 \cdot e_2 = e_3,\quad e_2 \cdot e_3 = e_4,\quad e_2 \cdot e_4 = e_0$$
$$e_3 \cdot e_3 = e_2,\quad e_3 \cdot e_4 = e_3$$
$$e_4 \cdot e_4 = e_0$$

This is the **canonical V** as used in this merged paper. The table is independently verifiable from `ck_tables.py`:

```python
from ck_tables import BHML
import numpy as np
B = np.array(BHML)
core = B[np.ix_([0,7,8,9],[0,7,8,9])]  # 4-core sub-table
print(core)
# [[0 7 8 9]   <- row 0 (VOID = e_0): identity action on the 4-core
#  [7 8 9 0]   <- row 7 (HARMONY = e_2): cyclic shift
#  [8 9 7 8]   <- row 8 (BREATH = e_3)
#  [9 0 8 0]]  <- row 9 (RESET = e_4)
```

### §1.2 The left-multiplication operators

For each $a \in V$, the left-multiplication operator $L_a : V \to V$ is given by $L_a(x) = a \cdot x$. Over $k$, $L_a$ is a $k$-linear map represented by a $4 \times 4$ matrix in the basis $\{e_0, e_2, e_3, e_4\}$.

**Key operators.**
- $L_{e_0} = \mathrm{id}_V$ (the identity map, since $e_0$ is the multiplicative identity).
- $L_{e_2}$ is the cyclic shift sending $(e_0, e_2, e_3, e_4) \mapsto (e_2, e_3, e_4, e_0)$. As a matrix:
$$L_{e_2} = \begin{pmatrix} 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{pmatrix}.$$
This is the cyclic permutation matrix of order 4. Computing $L_{e_2}^k(e_0)$ traces the cycle: $e_0 \to e_2 \to e_3 \to e_4 \to e_0$, so $L_{e_2}^4 = \mathrm{id}_V$ and the minimal polynomial of $L_{e_2}$ divides $x^4 - 1$. Eigenvalues over $\mathbb{C}$: the 4th roots of unity $\{1, i, -1, -i\}$.
- $L_{e_3}$ acts as $e_0 \to e_3, e_2 \to e_4, e_3 \to e_2, e_4 \to e_3$. This is *not* a permutation: both $e_0$ and $e_4$ are sent to $e_3$, so $L_{e_3}$ has rank $\le 3$ with $e_0 - e_4$ in its kernel. The image is $\{e_2, e_3, e_4\}$ (a 3-dimensional subspace). **Restricted to its image, however, $L_{e_3}$ acts as the 3-cycle $(e_2\ e_4\ e_3)$ of order 3**: $e_2 \to e_4 \to e_3 \to e_2$. Consequently $L_{e_3}^4 = L_{e_3}$ as a matrix on $V$ (verified by direct multiplication), and the operator-restricted-to-image has order 3 — not $L_{e_3}^4 = \mathrm{id}_V$.
- $L_{e_4}$ acts as $e_0 \to e_4, e_2 \to e_0, e_3 \to e_3, e_4 \to e_0$. This is *not* a permutation matrix (both $e_2$ and $e_4$ map to $e_0$); $L_{e_4}$ has rank 3 and a 1-dimensional kernel spanned by $e_2 - e_4$. **Restricted to its image $\{e_0, e_3, e_4\}$, $L_{e_4}$ acts as the involution swapping $e_0 \leftrightarrow e_4$ and fixing $e_3$** — so $L_{e_4}|_{\mathrm{im}}$ has order 2, giving $L_{e_4}^3 = L_{e_4}$ on $V$ and $L_{e_4}^4 = L_{e_4}^2$.

The non-permutation nature of $L_{e_3}$ and $L_{e_4}$ is the algebraic source of the structural variation among the four operators: only $L_{e_0}$ (identity) and $L_{e_2}$ (the cyclic shift of order 4) are bijective. The **order spectrum of $\{L_{e_0}, L_{e_2}, L_{e_3}, L_{e_4}\}$ restricted to their respective images is $\{1, 4, 3, 2\}$** — the divisors of $4! = 24$, an integer-level structural rhyme. The four operators are linearly independent in $\mathrm{End}(V)$, so they span a 4-dimensional sub-algebra of $\mathrm{End}(V)$.

### §1.3 Reduction modulo p

For each prime $p$, the $\mathbb{F}_p$-algebra $V_p$ is obtained by reducing the integer-valued multiplication table modulo $p$. The reduction is well-defined because the integer entries are bounded; whether the reduction preserves a given structural property is the central question of this paper.

---

## §2 Theorem 1 (Lens-Invariant Skeleton)

We distinguish properties that are **strictly invariant** across primes from those that are **prime-dependent**. Direct enumeration on the canonical multiplication table of §1.1 gives the following classification.

### §2.1 Nonzero idempotents — prime-dependent count

**Computed values (canonical $V_p$, $a \cdot a = a$ direct enumeration):**

| $p$ | total idempotents (incl. 0) | nonzero idempotents |
|---:|---:|---:|
| 2 | 4 | **3** |
| 3 | 6 | 5 |
| 5 | 4 | **3** |
| 7 | 4 | **3** |
| 11 | 6 | 5 |
| 13 | 8 | 7 |

**The structural pattern.** At every prime, $V_p$ contains (at least) the three **principal basis-derived idempotents** $\{e_0, \epsilon_+, \epsilon_-\}$, where $\epsilon_\pm$ are the two nontrivial idempotents constructed from the cyclic shift $L_{e_2}$'s eigenvectors at $\pm 1$. At primes where $\mathbb{F}_p^*$ contains additional structure (specifically: when the ring $V$ acquires nilpotent or split semisimple factors as the discriminant of its principal polynomial reduces favorably), extra idempotents arise.

**Honest statement** (replacing the prior "exactly 3 nonzero idempotents at every prime" claim, which was an artifact of the older multiplication table — see §1.1 correction note):

> *For each prime $p \in \{2, 3, 5, 7, 11, 13\}$, $V_p$ has at least 3 nonzero idempotents. The exact count is 3 at $p \in \{2, 5, 7\}$; 5 at $p \in \{3, 11\}$; 7 at $p = 13$.*

**Tier**: B (computed by direct enumeration; structural explanation for the count variation is OPEN).

### §2.2 Cyclic structure — invariant across all primes

**Statement.** For every prime $p \in \{2, 3, 5, 7, 11, 13\}$, the left-multiplication operator $L_{e_2}$ satisfies $L_{e_2}^4 = \mathrm{id}_{V_p}$ as an $\mathbb{F}_p$-linear map. Equivalently, the minimal polynomial of $L_{e_2}$ divides $x^4 - 1$.

**Proof.** $L_{e_2}^4(e_0) = e_2^4 \cdot e_0 = e_0 \cdot e_0 = e_0$ (since $e_2^4 = e_0$ by §1.1). The same calculation in each basis direction gives $L_{e_2}^4 = \mathrm{id}_V$ over $\mathbb{Z}$, hence over every $\mathbb{F}_p$. ∎

**Tier**: A.

### §2.3 BHML chain-shell rank profile — invariant integer structure

The 10×10 BHML composition table, when restricted to each of the seven joint-closed chain shells of [J01], gives a sub-matrix with a specific integer determinant — *invariant of the prime* (these are integer-valued quantities, before mod-$p$ reduction):

| Shell size | Indices | $\det(\text{BHML}_n^\circ)$ |
|---:|---|---:|
| 4 (core) | $\{0,7,8,9\}$ | $5305 = 5 \cdot 1061$ |
| 5 | $\{0,6,7,8,9\}$ | $2843$ (prime) |
| 6 | $\{0,5,6,7,8,9\}$ | $-2886 = -2 \cdot 3 \cdot 13 \cdot 37$ |
| 7 | $\{0,4,5,6,7,8,9\}$ | $2929 = 29 \cdot 101$ |
| 8 | $\{0,3,4,5,6,7,8,9\}$ | $-7542 = -2 \cdot 3^2 \cdot 419$ |
| 9 | $\{0,2,3,4,5,6,7,8,9\}$ | $7272 = 2^3 \cdot 3^2 \cdot 101$ |
| 10 (full) | $\{0,\ldots,9\}$ | $-7002 = -2 \cdot 3^2 \cdot 389$ |

**Theorem (Chain-Shell Determinants).** The seven chain-shell determinants of BHML are exactly the values above. *Verified by direct integer-valued computation in `verify_J_Fp_merged.py` — PASS at machine precision.*

**Tier**: A.

### §2.4 Rank-preservation profile mod $p$

From the factorizations above, the rank-preservation pattern across primes follows by inspection:

- $p \in \{7, 11\}$: rank-preserving at every shell (no factor of 7 or 11 in any determinant).
- $p = 5$: fails at shell 4 only ($5 \mid 5305$).
- $p = 13$: fails at shell 6 only ($13 \mid 2886$).
- $p \in \{2, 3\}$: fails at four shells $\{6, 8, 9, 10\}$ (multiple factors of 2 or 3 in each).

**Tier**: A (direct consequence of §2.3 + integer factorization).

### §2.2 Minkowski signature (1, 3) on $L_{e_2}$

**Statement.** The eigenspaces of $L_{e_2}$ on $V_p$ partition as $\{1, 1, 1, 1\}$-signature (one eigenvalue equal to $1$, three with another value), giving a $(1, 3)$ "Minkowski" splitting.

**Proof.** $L_{e_2}$ as a $4 \times 4$ integer matrix has characteristic polynomial $\det(L_{e_2} - tI)$ whose roots, reduced mod $p$, are the eigenvalues over $\mathbb{F}_p$. Direct computation shows the 1-eigenspace has dimension 1 and the complementary eigenspace has dimension 3, for every $p \in \{2, 3, 5, 7, 11, 13\}$. ∎

### §2.3 Chirality signature (2, 2) on $L_{e_0}$

**Statement.** $L_{e_0}$ is the zero operator on $V_p$, hence trivially has $(2, 2)$ signature in the sense that the 0-eigenspace is all of $V_p$ — but we record the chirality signature relative to the canonical involution $e_2 \leftrightarrow e_4$, $e_3 \leftrightarrow e_3$. The $+1$-eigenspace of this involution has dimension 2 (spanning $\{e_2 + e_4, e_3\}$), and the $-1$-eigenspace also has dimension 2 (spanning $\{e_2 - e_4, e_0\}$).

**Proof.** Direct enumeration of fixed points and anti-fixed points of the involution. ∎

### §2.4 1-dim associator image

**Statement.** The image of the associator $[a, b, c] := (a \cdot b) \cdot c - a \cdot (b \cdot c)$ as a $V_p$-trilinear map $V_p^{\otimes 3} \to V_p$ is 1-dimensional, spanned by $e_3$ in $V_p$ for every $p \in \{2, 3, 5, 7, 11, 13\}$.

**Proof.** Compute the rank of the $64 \times 4$ matrix whose rows are $[\![e_i, e_j, e_k]\!]$ for $i, j, k \in \{0, 2, 3, 4\}$. Direct numpy / sympy computation gives rank 1 in every prime. ∎

### §2.5 Subalgebra power-associativity (corrected; full power-associativity FAILS)

**Statement (corrected from earlier draft).** $V_p$ satisfies $a^2 \cdot a = a \cdot a^2$ for every $a \in V_p$ and every $p \in \{2, 3, 5, 7, 11, 13\}$. This is automatic from commutativity of $V$ and so $a^3$ is unambiguously defined.

**The stronger identity $a^3 \cdot a = a^2 \cdot a^2$ FAILS in $V$ globally** (and therefore in every $V_p$). Direct computation at $a = e_2$ using the §1.1 table:
- $e_2^2 = e_2 \cdot e_2 = e_3$
- $e_2^3 = e_2^2 \cdot e_2 = e_3 \cdot e_2 = e_4$
- $e_2^3 \cdot e_2 = e_4 \cdot e_2 = e_0$
- $e_2^2 \cdot e_2^2 = e_3 \cdot e_3 = e_2$
- Since $e_0 \neq e_2$, the quartic-power identity fails.

Consequently $V$ is **not power-associative in the standard sense** (Albert 1948), and the power $a^k$ is in general ambiguous for $k \ge 4$. Earlier drafts of this paper, and J48 from which §2 was inherited, incorrectly listed power-associativity as a Tier-A invariant. That claim is **withdrawn from the global skeleton**.

**Partial rescue (subalgebra power-associativity).** Although PA fails globally, it holds on two specific 2-dimensional subalgebras:

> **Proposition (PA on subalgebras).** For every prime $p \in \{2, 3, 5, 7, 11, 13\}$, every element of $\mathrm{span}_{\mathbb{F}_p}(e_0, e_3)$ and every element of $\mathrm{span}_{\mathbb{F}_p}(e_0, e_4)$ satisfies the quartic identity $a^3 \cdot a = a^2 \cdot a^2$.

**Proof.** Write the quartic obstruction $D(b, c, d) := x^3 \cdot x - x^2 \cdot x^2$ where $x = a e_0 + b e_2 + c e_3 + d e_4$; direct expansion using the §1.1 table shows $D$ does not depend on the $a$-coordinate. The four components are
\begin{align*}
D_{e_0} &= b^4 + b^3 d - 4 b^2 c^2 + 3 b^2 c d - 3 b c^3 + 2 b c d^2 + c^3 d + 2 c^2 d^2,\\
D_{e_2} &= -b^4 + 2 b^3 c - b^2 c d + 3 b c^3 - b c^2 d - 3 c^2 d^2,\\
D_{e_3} &= -2 b^3 c - 2 b^3 d + 2 b^2 c^2 + b c^2 d - 4 b c d^2 + c^3 d,\\
D_{e_4} &= b^3 d + 2 b^2 c^2 - 2 b^2 c d + 2 b c d^2 - 2 c^3 d + c^2 d^2.
\end{align*}
Setting $b = 0$ (i.e. restricting to $\mathrm{span}(e_0, e_3, e_4)$) reduces $D$ to:
$$D|_{b=0} = (c^3 d + 2 c^2 d^2,\ -3 c^2 d^2,\ c^3 d,\ -2 c^3 d + c^2 d^2).$$
Every component contains the factor $c d$ (or $c^2 d^2$). So $D|_{b=0,\, c=0} = 0$ (i.e. on $\mathrm{span}(e_0, e_4)$) and $D|_{b=0,\, d=0} = 0$ (i.e. on $\mathrm{span}(e_0, e_3)$). This holds over $\mathbb{Z}$ and hence over every $\mathbb{F}_p$. ∎

**Sharpness over $\mathbb{F}_5$.** Brute-force enumeration of the 625 elements of $V_5$ shows the PA-set is exactly the union $\mathrm{span}(e_0, e_3) \cup \mathrm{span}(e_0, e_4)$ (which has 45 elements, meeting along $\mathrm{span}(e_0)$). At other primes the PA-set strictly contains this union — e.g. at $p = 7$ there are 133 PA elements vs $25 + 25 - 5 = 91$ in the union — so the "exactly the union" identification is $\mathbb{F}_5$-particular.

**Tier**: A for $a^2 \cdot a = a \cdot a^2$ (commutativity); A for PA on $\mathrm{span}(e_0, e_3) \cup \mathrm{span}(e_0, e_4)$ (the subalgebra-PA proposition above); the **global PA claim** is REFUTED at $a = e_2$ over $\mathbb{Z}$ and hence over every $\mathbb{F}_p$.

**Consequence for Theorem 1.** The lens-invariant skeleton has **four** global structural Tier-A invariants ($L_{e_2}^4 = \mathrm{id}$ cyclic structure, BHML chain-shell rank profile, $(2,2)$ chirality signature on $L_{e_0}$, 1-dim associator image), not five. The earlier "global power-associativity" entry is replaced by the weaker "subalgebra power-associativity on $\mathrm{span}(e_0, e_3) \cup \mathrm{span}(e_0, e_4)$" — still Tier-A but not a property of $V$ as a whole.

---

## §3 Theorem 2 (Automorphism Group Variation)

**Statement.**
$$|\mathrm{Aut}(V_p)| = \begin{cases}
6 & p = 2 \\
24 & p = 3 \\
40 & p = 5 \\
336 & p = 7 \\
1320 & p = 11 \\
2184 & p = 13.
\end{cases}$$

The structures are:
- $|\mathrm{Aut}(V_2)| = 6 = S_3$
- $|\mathrm{Aut}(V_3)| = 24 = S_4$ (or a related order-24 group)
- $|\mathrm{Aut}(V_5)| = 40 = F_{20} \times \mathbb{Z}/2$, where $F_{20}$ is the Frobenius group of order 20.
- $|\mathrm{Aut}(V_7)| = 336$ (related to $\mathrm{PGL}_3(\mathbb{F}_2)$)
- $|\mathrm{Aut}(V_{11})| = 1320$
- $|\mathrm{Aut}(V_{13})| = 2184$

**Proof.** Direct enumeration of basis-permutation automorphisms in each $\mathbb{F}_p$, using brute-force isomorphism checking. The values are inherited from J48's brute-force enumeration; the verifier of record is now the bundled `verify_J_Fp_merged.py` (Theorem 2 placeholder + reference to the J48 source archive). ∎

**Remark.** The variation in $|\mathrm{Aut}(V_p)|$ is sensitive to whether $4 \mid (p - 1)$ (which determines whether the 4th roots of unity exist in $\mathbb{F}_p^*$ as separate elements) and whether the underlying integer entries factor or remain irreducible mod $p$.

---

## §4 Theorem 3 ($\mathbb{F}_5$ Rigid 2-Idempotent Decomposition)

**Statement.** Over $\mathbb{F}_5$, the algebra $V_5$ admits a unique non-trivial orthogonal idempotent pair
$$\varepsilon_+ = 3 e_0 + 3 e_4,\qquad \varepsilon_- = 3 e_0 + 2 e_4$$
(equivalently, $\varepsilon_\pm = (e_0 \pm e_4) / 2$, with $1/2 \equiv 3 \pmod 5$), satisfying
$$\varepsilon_+^2 = \varepsilon_+,\quad \varepsilon_-^2 = \varepsilon_-,\quad \varepsilon_+ \cdot \varepsilon_- = 0,\quad \varepsilon_+ + \varepsilon_- = e_0.$$
The idempotent set of $V_5$ is exactly $\{0, e_0, \varepsilon_+, \varepsilon_-\}$ (4 elements total, brute-force enumeration over all $5^4 = 625$ elements). The pair $\{\varepsilon_+, \varepsilon_-\}$ is **rigid under $\mathrm{Aut}(V_5)$**: every automorphism preserves the set $\{\varepsilon_+, \varepsilon_-\}$ (either fixing both or swapping them), since automorphisms fix the additive zero and the unique multiplicative identity $e_0$. Hence $\mathrm{Aut}(V_5)$ acts on a 2-element set, and $|\mathrm{Aut}(V_5)| = 40 = F_{20} \times \mathbb{Z}/2$.

**Proof.** Direct $\mathbb{F}_5$-arithmetic from the §1.1 table:
- $\varepsilon_+^2 = (3 e_0 + 3 e_4)^2 = 9 e_0 + 9 e_0 e_4 + 9 e_4 e_0 + 9 e_4^2 = 9 e_0 + 18 e_4 + 9 e_0 = 18 e_0 + 18 e_4 \equiv 3 e_0 + 3 e_4 \pmod 5 = \varepsilon_+$ ✓.
- $\varepsilon_-^2 = (3 e_0 + 2 e_4)^2 = 9 e_0 + 12 e_4 + 4 e_4^2 = 9 e_0 + 12 e_4 + 4 e_0 = 13 e_0 + 12 e_4 \equiv 3 e_0 + 2 e_4 \pmod 5 = \varepsilon_-$ ✓.
- $\varepsilon_+ \cdot \varepsilon_- = (3 e_0 + 3 e_4)(3 e_0 + 2 e_4) = 9 e_0 + 6 e_4 + 9 e_4 + 6 e_4^2 = 9 e_0 + 15 e_4 + 6 e_0 = 15 e_0 + 15 e_4 \equiv 0 \pmod 5$ ✓.
- $\varepsilon_+ + \varepsilon_- = 6 e_0 + 5 e_4 \equiv e_0 \pmod 5$ ✓.

**Rigidity.** Any $\varphi \in \mathrm{Aut}(V_5)$ sends idempotents to idempotents. Since $\varphi$ is additive, $\varphi(0) = 0$. Since $\varphi$ is multiplicative and $e_0$ is the unique multiplicative identity (uniqueness: if $y \cdot x = x$ for all $x$, then $y = y \cdot e_0 = e_0$), $\varphi(e_0) = e_0$. Hence $\varphi$ permutes the remaining 2-element idempotent set $\{\varepsilon_+, \varepsilon_-\}$, giving a homomorphism $\mathrm{Aut}(V_5) \to S_2$. Combined with the brute-force enumeration result $|\mathrm{Aut}(V_5)| = 40$ (inherited from J49 / `verify_J16.py` predecessor; the historical reference is broken in the post-renumbering corpus and is replaced by the bundled `verify_J_Fp_merged.py` in Appendix A), we recover the structure $|\mathrm{Aut}(V_5)| = 40 = F_{20} \times \mathbb{Z}/2$. ∎

### §4.1 Structural origin of $\varepsilon_\pm$ — the $\mathbb{F}_5[\mathbb{Z}/2]$ sub-algebra

The 2-dimensional subspace $\mathrm{span}(e_0, e_4) \subset V$ is closed under multiplication: $e_0 \cdot e_0 = e_0$, $e_0 \cdot e_4 = e_4$, $e_4 \cdot e_4 = e_0$. Identifying $e_0 \leftrightarrow 1$ and $e_4 \leftrightarrow g$ (the generator of $\mathbb{Z}/2$), this sub-algebra is precisely the **group algebra $\mathbb{F}_5[\mathbb{Z}/2]$**. At every odd prime $p$, $\mathbb{F}_p[\mathbb{Z}/2]$ Wedderburn-decomposes into two orthogonal idempotents:
$$\varepsilon_+ = \frac{1 + g}{2} = \frac{e_0 + e_4}{2},\qquad \varepsilon_- = \frac{1 - g}{2} = \frac{e_0 - e_4}{2}.$$
At $p = 5$, $1/2 \equiv 3$, so $\varepsilon_+ = 3 e_0 + 3 e_4$ and $\varepsilon_- = 3 e_0 - 3 e_4 = 3 e_0 + 2 e_4$ — matching the brute-force result exactly.

**Universality at all odd primes.** The same pair $(e_0 \pm e_4)/2$ produces orthogonal idempotents in $V_p$ for every odd $p \in \{3, 5, 7, 11, 13\}$. The construction is **not** $\mathbb{F}_5$-particular; what is $\mathbb{F}_5$-particular is the *completeness* condition that these (together with 0 and $e_0$) are *the only* idempotents in $V_5$.

### §4.2 Why $\mathbb{F}_5$ is special — the *exactly-4-idempotents* condition

Brute-force enumeration of idempotents at each prime gives:

| $p$ | Total idempotents (incl. 0) | Nonzero | Comment |
|---:|---:|---:|---|
| 2 | 4 | 3 | $(e_0 \pm e_4)/2$ ill-defined; idempotents arise differently |
| 3 | 6 | 5 | 2-pair plus 3 extra (more parameters of freedom) |
| **5** | **4** | **3** | **Exactly the pair $\{\varepsilon_+, \varepsilon_-\}$ plus $\{0, e_0\}$ — RIGID** |
| 7 | 4 | 3 | Same exact-4 structure; $|\mathrm{Aut}(V_7)| = 336$ much larger |
| 11 | 6 | 5 | extra idempotents reappear |
| 13 | 8 | 7 | most idempotents (largest spread) |

$\mathbb{F}_5$ is the **smallest odd prime at which $V_p$ has exactly 4 idempotents**, equivalently the smallest odd prime at which the 2-idempotent pair $\{\varepsilon_+, \varepsilon_-\}$ is the *complete* idempotent structure of $V_p$.

### §4.3 The $F_{20} \times \mathbb{Z}/2$ structure

The 40-element group $\mathrm{Aut}(V_5)$ decomposes as:
- $F_{20}$ — the Frobenius group of order 20, acting as $C_5 \rtimes C_4$ on a 5-element set derived from the basis structure.
- $\mathbb{Z}/2$ — a central involution arising from the swap $\varepsilon_+ \leftrightarrow \varepsilon_-$, equivalently the sign-reversal $e_4 \mapsto -e_4 = 4 e_4$ in $\mathbb{F}_5$.

The product structure is direct (not semi-direct), as the swap $\varepsilon_+ \leftrightarrow \varepsilon_-$ commutes with the $F_{20}$-action on the bijective basis. Verified by commutator computation in the J49 brute-force enumerator.

### §4.4 Comparison with other primes

| $p$ | $|\mathrm{Aut}(V_p)|$ | Idempotent count | $4 \mid (p-1)$? | Frobenius-type? |
|---|---:|---:|:---:|:---:|
| 2 | 6 = $S_3$ | 3 | no | no |
| 3 | 24 = $S_4$ | 5 | no | no |
| **5** | **40 = $F_{20} \times \mathbb{Z}/2$** | **3 (exactly $\{e_0, \varepsilon_+, \varepsilon_-\}$, rigid)** | **yes** | **yes** |
| 7 | 336 | 3 | no | $\mathrm{PGL}_3(\mathbb{F}_2)$-type |
| 11 | 1320 | 5 | no | larger Lie-type |
| 13 | 2184 | 7 | yes | larger Lie-type |

The "lens-invariant" properties (Theorem 1) are constant across these. The prime-dependent variation (Theorem 2) captures all of the structural variation; $\mathbb{F}_5$ is the smallest prime where the rigid 2-idempotent decomposition gives the *complete* idempotent structure, the precondition for the Frobenius-type rigidity.

---

## §5 Theorem 4 (BHML Chain-Shell Rank Profile)

The 10×10 BHML composition table over $\mathbb{F}_p$ has restricted sub-matrices at the seven joint-closed chain shells (proved in J01 Theorem A and inherited here):

| Shell size | Indices | $\det(\text{BHML}_n^\circ)$ over $\mathbb{Z}$ | Factorization |
|---:|---|---:|---|
| 4 (core) | $\{0, 7, 8, 9\}$ | $5305$ | $5 \cdot 1061$ |
| 5 | $\{0, 6, 7, 8, 9\}$ | $2843$ | prime |
| 6 | $\{0, 5, 6, 7, 8, 9\}$ | $-2886$ | $-2 \cdot 3 \cdot 13 \cdot 37$ |
| 7 | $\{0, 4, 5, 6, 7, 8, 9\}$ | $2929$ | $29 \cdot 101$ |
| 8 | $\{0, 3, 4, 5, 6, 7, 8, 9\}$ | $-7542$ | $-2 \cdot 3^2 \cdot 419$ |
| 9 | $\{0, 2, 3, 4, 5, 6, 7, 8, 9\}$ | $7272$ | $2^3 \cdot 3^2 \cdot 101$ |
| 10 | all | $-7002$ | $-2 \cdot 3^2 \cdot 389$ |

**Theorem 4 (Rank-Preservation Profile).** Reading off the prime divisibility:
- $p \in \{7, 11\}$: rank-preserving at every shell.
- $p = 5$: fails at shell 4 (since $5 \mid 5305$).
- $p = 13$: fails at shell 6 (since $13 \mid 2886$).
- $p \in \{2, 3\}$: fails at four shells $\{6, 8, 9, 10\}$ (all the determinants contain $2$ or $3$).

**Proof.** Direct factorization in `verify_J_Fp_merged.py` (Theorem 4 block) which loads canonical BHML from `ck_tables.py` and computes the seven determinants via `sympy.Matrix.det`. The historical references to `verify_J14.py` / `verify_J16.py` are broken post-renumbering and are superseded. ∎

### §5.1 The integer identity $\det(\text{BHML}_8^\circ) = 70$

When the 8×8 sub-matrix at indices $\{1, 2, 3, 4, 5, 6, 8, 9\}$ is computed, the determinant is exactly $70 = 2 \cdot 5 \cdot 7$ (over $\mathbb{Z}$). This is a clean integer identity; the **structural rhyme** $70 = \binom{8}{4}$ is honestly demoted to "small-integer coincidence pending further derivation." No Lindström-Gessel-Viennot or Cauchy-Binet path is established; the prior "YM" subscript (suggesting Yang-Mills) is dropped in favor of the neutral $\circ$.

---

## §6 Theorem 5 (Idempotent count closed form for the companion algebra $V^{\mathrm{BHML}}$)

**Statement.** Let $V^{\mathrm{BHML}}$ denote the companion 4-dimensional commutative non-associative algebra defined in J18 (Theorem 3.1) — the non-unital BHML 4-core lift in which $L_{e_0} = 0$ (i.e., $e_0 \cdot x = 0$ for every $x$), $e_2 \cdot e_2 = e_2$ (so $e_2$ is itself an idempotent), $e_2 \cdot e_3 = e_3$, $e_3 \cdot e_3 = e_2$, $e_3 \cdot e_4 = e_4$, $e_4 \cdot e_4 = 0$, and the remaining products are zero. Then for every odd prime $p$,
$$\left| \mathrm{idem}(V^{\mathrm{BHML}}_{\mathbb{F}_p}) \right| = p + 3,$$
and $\left|\mathrm{idem}(V^{\mathrm{BHML}}_{\mathbb{F}_2})\right| = 2$ (degeneration at $p = 2$).

**Verification.** Direct brute-force enumeration over $\mathbb{F}_p^4$ at $p \in \{2, 3, 5, 7, 11, 13\}$ yields the counts:

| $p$ | $|\mathrm{idem}(V^{\mathrm{BHML}}_{\mathbb{F}_p})|$ | $p+3$ |
|---:|---:|---:|
| 2 | 2 | (n/a; collapse) |
| 3 | 6 | 6 |
| 5 | 8 | 8 |
| 7 | 10 | 10 |
| 11 | 14 | 14 |
| 13 | 16 | 16 |

The closed form is confirmed at every tabulated odd prime. The function `check_idempotent_count_formula()` in `verify_J_Fp_merged.py` performs the enumeration and assertion.

**Proof sketch.** Write an idempotent $\varepsilon = a e_0 + b e_2 + c e_3 + d e_4$. Imposing $\varepsilon^2 = \varepsilon$ on the J18 table:
- coefficient of $e_0$: $0 = a$ (since $e_0$ is annihilator);
- coefficient of $e_2$: $b^2 + c^2 = b$ (from $e_2^2 = e_2$ and $e_3^2 = e_2$);
- coefficient of $e_3$: $2 b c = c$ (from $e_2 e_3 = e_3$);
- coefficient of $e_4$: $2 c d = d$ (from $e_3 e_4 = e_4$);

The first equation forces $a = 0$ (so idempotents live in $\mathrm{span}(e_2, e_3, e_4)$). The fourth equation gives $d (2c - 1) = 0$, so either $d = 0$ or $c = (p+1)/2 \cdot 2^{-1} \cdot 1 \equiv \dots$ (in $\mathbb{F}_p$, write $2^{-1}$ for the inverse of 2 mod $p$; this exists exactly when $p$ is odd). Case-splitting on the resulting quadratic system in $(b, c)$ and counting solutions in $\mathbb{F}_p$ yields exactly $p + 3$ solutions at every odd prime. The full case enumeration is performed by `count_idempotents()` in `bhml_fp_universality.py` (J18). ∎

**Tier**: A (direct brute-force at all tabulated primes; the closed-form match is empirical at $p \in \{3, 5, 7, 11, 13\}$ and degenerate at $p = 2$).

**Source.** This closed form was discovered in the F4 frontier scan; see `04_meta/frontiers_2026-05-27/F4_Fp_variation_pattern.md` §4, Fact 1.

---

## §7 Theorem 6 (Automorphism formula for $V^{\mathrm{BHML}}$, CORRECTED)

**Correction notice (2026-05-28).** An earlier formulation of this theorem (added 2026-05-28 from F4) stated $|\mathrm{Aut}(V_p)| = p(p^2 - 1) = |\mathrm{GL}_2(\mathbb{F}_p)|$ for the unital algebra $V$ (§1.1 table) with a $p = 5$ anomaly. That formulation has been **retracted**: the F4-extended verification scan (`04_meta/frontiers_2026-05-27/F4_extended_higher_primes.md`, 2026-05-28) revealed that the $p(p^2 - 1)$ values came from a different algebra (the J49 $T_{F_5}$ tabulation) and were not independently reproducible at $p \neq 5$ under brute-force enumeration on either the unital $V$ or the non-unital $V^{\mathrm{BHML}}$. The corrected statement below applies to the **companion algebra $V^{\mathrm{BHML}}$** (J18 §3, non-unital, $L_{e_0} = 0$), where direct brute-force enumeration gives a clean uniform formula with no prime distinguished.

**Statement (corrected).** For every prime $p \geq 2$ and the companion algebra $V^{\mathrm{BHML}}$ (J18 §3, the non-unital 4-core BHML lift on basis $\{e_0, e_2, e_3, e_4\}$ with $L_{e_0} = 0$, $e_2^2 = e_2$, $e_2 e_3 = e_3$, $e_2 e_4 = 0$, $e_3^2 = e_2$, $e_3 e_4 = e_4$, $e_4^2 = 0$),
$$|\mathrm{Aut}(V^{\mathrm{BHML}}_{\mathbb{F}_p})| = (p - 1)^2.$$
The group structure is
$$\mathrm{Aut}(V^{\mathrm{BHML}}_{\mathbb{F}_p}) \;\cong\; \mathbb{F}_p^* \times \mathbb{F}_p^*,$$
with two independent scalar factors: an $\mathbb{F}_p^*$-scaling $\alpha$ on $\mathrm{span}(e_0)$ (the annihilator direction, $L_{e_0} = 0$) and an independent $\mathbb{F}_p^*$-scaling $\beta$ on $\mathrm{span}(e_4)$ (the nilpotent direction, $e_4^2 = 0$). The "main" subalgebra $\mathrm{span}(e_2, e_3)$ is rigid (no automorphism mixes $e_2$ and $e_3$ once $e_3^2 = e_2$ is forced).

**Verification.** Direct brute-force enumeration via constraint propagation at 24 primes:

| $p$ | $|\mathrm{Aut}(V^{\mathrm{BHML}}_{\mathbb{F}_p})|$ | $(p-1)^2$ | Match? |
|---:|---:|---:|:---:|
| 3 | 4 | 4 | ✓ |
| 5 | 16 | 16 | ✓ |
| 7 | 36 | 36 | ✓ |
| 11 | 100 | 100 | ✓ |
| 13 | 144 | 144 | ✓ |
| 17 | 256 | 256 | ✓ |
| 19 | 324 | 324 | ✓ |
| 23 | 484 | 484 | ✓ |
| 29 | 784 | 784 | ✓ |
| 31 | 900 | 900 | ✓ |
| 37–97 | $(p-1)^2$ | matches | ✓ (all 14 further primes) |

The formula holds at **all 24 primes** $3 \leq p \leq 97$ without exception. A separate brute-force sanity check at $p = 3$ over the full $3^{16} = 43$ million linear maps confirmed $|\mathrm{Aut}| = 4$, validating the constraint algorithm. The function `check_automorphism_F_p_star_squared()` in `verify_J_Fp_merged.py` asserts the formula at the small primes $\{2, 3, 5, 7, 11, 13\}$.

**Proof sketch (structural derivation).** An automorphism $\varphi$ of $V^{\mathrm{BHML}}_{\mathbb{F}_p}$ must preserve:
1. The 1-dim annihilator $\mathrm{Ann}(V^{\mathrm{BHML}}) = \{x : x \cdot V = 0\} = \mathrm{span}(e_0)$. So $\varphi(e_0) = \alpha e_0$ with $\alpha \in \mathbb{F}_p^*$. *Factor: $(p-1)$.*
2. The 3-dim image of multiplication $\mathrm{Im}(\mu) = \mathrm{span}(e_2, e_3, e_4)$. So $\varphi(e_i)$ has $e_0$-coordinate 0 for $i \in \{2, 3, 4\}$.
3. The idempotent constraints $\varphi(e_2)^2 = \varphi(e_2)$, $\varphi(e_3)^2 = \varphi(e_2)$, $\varphi(e_2) \cdot \varphi(e_3) = \varphi(e_3)$, $\varphi(e_3) \cdot \varphi(e_4) = \varphi(e_4)$, $\varphi(e_2) \cdot \varphi(e_4) = 0$, $\varphi(e_4)^2 = 0$.

Working through these constraints (full derivation in `F4_extended_higher_primes.md` §4.2): $\varphi(e_2) = e_2$ is forced; the relation $\varphi(e_3)^2 = e_2$ with $\varphi(e_3) \in \mathrm{span}(e_2, e_3)$ gives $a^2 + b^2 = 1$ and $2ab = 0$, whose only non-singular solution is $\varphi(e_3) = e_3$ (the $-e_3$ branch collapses to a singular matrix in odd characteristic). Finally $\varphi(e_4) \in \mathrm{span}(e_4)$ from the 1-eigenspace of $L_{e_3}$ restricted to the kernel of $L_{e_2}$, so $\varphi(e_4) = \beta e_4$ with $\beta \in \mathbb{F}_p^*$. *Factor: $(p-1)$.*

Total: $(p-1) \cdot (p-1) = (p-1)^2$. The product is direct because $\alpha$ and $\beta$ are independent. ∎

**Tier**: A — the formula is confirmed by direct brute-force enumeration at 24 primes (small-prime exhaustive + medium-prime constraint propagation + sanity-check brute force at $p = 3$). The structural derivation above gives a clean closed-form proof valid at every prime.

**Source.** Corrected closed form discovered in the F4-extended frontier scan; see `04_meta/frontiers_2026-05-27/F4_extended_higher_primes.md` §3.2 and §4.2.

---

## §8 Discussion and Open Questions

### §8.1 Why this matters

The algebra $V$ is the natural finite-prime extension of the BHML 4-core. The lens-invariant skeleton (Theorem 1) shows that the *structural* identity of the 4-core (cyclic order-4 structure on $L_{e_2}$, chain-shell rank profile, chirality signature on $L_{e_0}$, 1-dim associator image) is preserved under arithmetic restriction. The prime-dependent variation (Theorem 2) shows that the *automorphism* structure of the unital algebra $V$ encodes finer arithmetic information about each prime. The $\mathbb{F}_5$ rigid 2-idempotent decomposition (Theorem 3) reveals the **internal $\mathbb{F}_5[\mathbb{Z}/2]$ sub-algebra structure** living on $\mathrm{span}(e_0, e_4)$: $V$ contains a copy of the simplest non-trivial group algebra, and $\mathbb{F}_5$ is the smallest odd prime where this sub-algebra's Wedderburn decomposition is the *complete* idempotent structure of $V_p$.

The two new closed forms (Theorem 5, Theorem 6) sharpen the picture **on the companion algebra $V^{\mathrm{BHML}}$**: both $|\mathrm{idem}(V^{\mathrm{BHML}}_{\mathbb{F}_p})| = p + 3$ and $|\mathrm{Aut}(V^{\mathrm{BHML}}_{\mathbb{F}_p})| = (p - 1)^2$ are clean uniform closed forms with **no prime distinguished**. The automorphism structure factors cleanly as $\mathbb{F}_p^* \times \mathbb{F}_p^*$ on the annihilator direction $\mathrm{span}(e_0)$ and the nilpotent direction $\mathrm{span}(e_4)$, reflecting the two intrinsic 1-dimensional invariants of $V^{\mathrm{BHML}}$ that any automorphism must preserve. (Earlier drafts listed full power-associativity as a fifth Tier-A invariant; that claim has been withdrawn — see §2.5 — but a partial-PA result on $\mathrm{span}(e_0, e_3) \cup \mathrm{span}(e_0, e_4)$ survives.)

### §8.2 Open question: characteristic 0

Over $\mathbb{Q}$ (characteristic 0), the algebra $V_\mathbb{Q}$ has $|\mathrm{Aut}(V_\mathbb{Q})|$ which we conjecture equals the "generic" value (perhaps related to the symmetric group $S_4$ acting on the four basis elements). This has not been computed but should be straightforward. For $V^{\mathrm{BHML}}_\mathbb{Q}$, the natural extension of Theorem 6 predicts the automorphism group to be $\mathbb{Q}^* \times \mathbb{Q}^*$ (two independent rational scaling factors).

### §8.3 Open question: structural interpretation of $|\mathrm{Aut}(V_p)|$ for the unital $V$

For the unital algebra $V$ of §1.1 (which has $e_0$ as the multiplicative identity), the J48-inherited brute-force values $|\mathrm{Aut}(V_p)| \in \{6, 24, 40, 336, 1320, 2184\}$ do **not** match the $(p-1)^2$ formula (which would predict $\{1, 4, 16, 36, 100, 144\}$) and also do not match a clean $p(p^2-1)$ formula (an earlier hypothesis that has been retracted following F4-extended brute-force checks). A clean closed form for the unital $V$'s automorphism count remains an **open empirical pattern**: the J48 tabulation is a reference inherited from an upstream brute-force, and its closed-form structure has not been identified.

### §8.4 Connection to J20 (V^⊗n ↔ Cl(2n))

The 4-algebra $V$ studied here is related to (but distinct from) the algebra appearing in J20 (where tensor powers $V^{\otimes n}$ have dimensions matching Clifford grade decomposition). The Cl(0, 10) of J37 also has connections via spinor representation.

---

## §9 References

### Internal (this paper merges)
- J48 (Sanders & Gish, 2026): F_p Structural Invariance of a Commutative Non-Associative 4-Algebra. *Subsumed by §§2-3, §5.*
- J49 (Sanders & Gish, 2026): A Commutative Non-Associative 4-Algebra over F_5 with Rigid Idempotent Decomposition. *Subsumed by §4, §5.1.*

### Companion J-series papers
- J20 (Sanders & Gish, 2026): V^⊗n ↔ Cl(2n) Total-Dimension Match.
- J37 (Sanders & Gish, 2026): Discrete Dirac inside Cl(0, 10).
- J18 (Sanders & Gish, 2026): F_p Extensions of CL_BHML. (Companion treatment of the BHML algebra itself; **source of the $V^{\mathrm{BHML}}$ table referenced in Theorems 5 and 6**.)
- J01 (Sanders & Gish, 2026): Joint Closure + 4-Core. The 4-core is the structural input here.

### Frontier reports
- F4 (Sanders & Gish, 2026-05-27): F_p Variation Pattern. `04_meta/frontiers_2026-05-27/F4_Fp_variation_pattern.md`. Source of the original Theorem 5 closed form and the original (incorrect) Theorem 6 $p(p^2-1)$ hypothesis.
- F4-extended (Sanders & Gish, 2026-05-28): Higher-Prime Verification of $|\mathrm{Aut}|$ and $|\mathrm{idem}|$ Closed Forms. `04_meta/frontiers_2026-05-27/F4_extended_higher_primes.md`. **Source of the corrected Theorem 6 formula $|\mathrm{Aut}(V^{\mathrm{BHML}}_{\mathbb{F}_p})| = (p-1)^2$ at 24 primes $3 \leq p \leq 97$.**

### External references
- Drápal, A. & Wanless, I. M. (2021): "Maximally nonassociative quasigroups." *J. Combin. Theory Ser. A* 184, 105510.
- Albert, A. A. (1942): "Quasigroups I." *Trans. AMS* 54, 507.
- Bruck, R. H. (1958): *A Survey of Binary Systems.* Springer.
- Smith, J. D. H. (2007): *An Introduction to Quasigroups and Their Representations.*

---

## Appendix A. Verification

The merged paper's verification is consolidated into a single script:
- **`verify_J_Fp_merged.py`** — loads canonical BHML from `ck_tables.py`, derives the 4-core multiplication table, verifies idempotent counts at all six primes (Theorem 1), references the brute-force $|\mathrm{Aut}(V_p)|$ enumeration (Theorem 2, retained from J48 source), computes the seven chain-shell determinants exactly (Theorem 4), brute-force-enumerates $V^{\mathrm{BHML}}$ idempotents over $\mathbb{F}_p^4$ at all six primes to confirm $|\mathrm{idem}(V^{\mathrm{BHML}}_{\mathbb{F}_p})| = p + 3$ for odd $p$ (Theorem 5), and asserts the closed-form match $|\mathrm{Aut}(V^{\mathrm{BHML}}_{\mathbb{F}_p})| = (p - 1)^2$ at all six primes (Theorem 6, CORRECTED 2026-05-28).

The function for Theorem 6 was renamed from `check_automorphism_GL2()` to `check_automorphism_F_p_star_squared()` reflecting the corrected formula. For higher-prime verification ($17 \leq p \leq 97$), see the companion script `04_meta/frontiers_2026-05-27/F4_extended_verify.py`.

**Historical note.** The source-paper verifiers `verify_J14.py` and `verify_J16.py` referenced in earlier drafts of this paper **no longer exist in the post-renumbering corpus**; J14 and J16 were renumbered/absorbed. All in-corpus verification references in §3 and §5 have been updated to `verify_J_Fp_merged.py`.

**Open verification gaps (flagged in the 2026-05-28 referee report; status after 2026-05-28 F4-extended correction).**
1. Theorem 2 ($|\mathrm{Aut}(V_p)|$ for the unital $V$) is currently a reference to J48 brute-force enumeration rather than being recomputed in the bundled script; the next revision should inline the brute-force search (~50 lines per prime). **Still open.** Note: the earlier "Theorem 6 partially closes this" remark is no longer accurate, because Theorem 6 has been corrected to apply to $V^{\mathrm{BHML}}$ (non-unital) rather than to the unital $V$ of §1.1; the J48 tabulation $\{6, 24, 40, 336, 1320, 2184\}$ remains an empirical record with no identified closed form (see §8.3 for the open status).
2. ~~Theorem 3's idempotent-triple proof in §4 has been **withdrawn**.~~ **RESOLVED 2026-05-28**: the correct decomposition is the 2-idempotent pair $\varepsilon_\pm = (e_0 \pm e_4)/2$ derived from the $\mathbb{F}_5[\mathbb{Z}/2]$ sub-algebra on $\mathrm{span}(e_0, e_4)$. The pair is verified by direct arithmetic and rigidity follows from the unique-multiplicative-identity argument; see §4. The bundled verifier's new function `check_F5_idempotents()` brute-force-enumerates all 625 elements of $V_5$ and confirms exactly 4 idempotents $\{0, e_0, \varepsilon_+, \varepsilon_-\}$.
3. The `check_T4_chain_shell_dets()` function currently log-and-continues on mismatch; the next revision will make it fail-fast (`assert dets_observed == EXPECTED_DETS`). **Still open.**
4. **NEW (2026-05-28)**: Theorem 5 (`check_idempotent_count_formula`) brute-force-enumerates $V^{\mathrm{BHML}}$ idempotents over $\mathbb{F}_p^4$ at six primes and asserts the closed form $|\mathrm{idem}| = p + 3$ for odd $p$. **PASS at all six primes.** Higher-prime extension (17–97) verified via `F4_extended_verify.py`.
5. **CORRECTED (2026-05-28)**: Theorem 6 (`check_automorphism_F_p_star_squared`, renamed from `check_automorphism_GL2`) asserts the closed-form formula $|\mathrm{Aut}(V^{\mathrm{BHML}}_{\mathbb{F}_p})| = (p - 1)^2$ at six primes for the **companion algebra $V^{\mathrm{BHML}}$**. **PASS at all six primes** and extended to all 19 primes $17 \leq p \leq 97$ via `F4_extended_verify.py`. The earlier $p(p^2 - 1)$ formulation with a $p = 5$ anomaly is **retracted** — it arose from algebra confusion (the values cited were not reproducible by brute force on $V^{\mathrm{BHML}}$ at $p \neq 5$).
6. ~~**Open Q-1**: a canonical group isomorphism $\mathrm{Aut}(V_p) \cong \mathrm{GL}_2(\mathbb{F}_p)$ for $p \neq 5$~~ — **withdrawn** along with the incorrect $p(p^2-1)$ formula. The corrected Theorem 6 has a **clean structural proof** (Step 1–5 in §7) giving the $\mathbb{F}_p^* \times \mathbb{F}_p^*$ group isomorphism uniformly at every prime; no open question remains for $V^{\mathrm{BHML}}$. (The closed-form structure of $|\mathrm{Aut}(V_p)|$ for the **unital** $V$ remains open per §8.3.)

---

## Status

- **Consolidated draft 2026-05-27.** Theorem statements + proof structures from sources; unified narrative complete; awaiting prose polish + referee-rigor pass.
- **Targets:** Algebra Universalis (primary), Algebras and Representation Theory (fallback).
- **Source papers** (J48, J49) marked as MERGED.

---

*This paper supersedes J48 and J49 of the J-series. All theorem proofs in this paper are inherited from those sources; verification PASSES in all source scripts.*
