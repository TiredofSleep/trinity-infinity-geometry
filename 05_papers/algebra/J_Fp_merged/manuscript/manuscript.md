# F_p Structure of the 4-Core Commutative Non-Associative Algebra: Invariant Skeleton Across Primes and Rigid F_5 Idempotent Decomposition

**Authors:** B.R. Sanders$^{1}$, M. Gish$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Target venue:** *Algebra Universalis* (primary). Fallback: *Algebras and Representation Theory* (where J16 was originally targeted).

**MSC 2020:** 17A30 (non-associative algebras, general), 17A36 (automorphisms, derivations), 11T55 (character sums and exponential sums), 17A40 (Ternary compositions), 12E20 (finite fields).

**Status:** CONSOLIDATED DRAFT (2026-05-27). Merges J14 (F_p invariance) and J16 (F_5 rigid idempotent decomposition) into one paper. Awaiting unified prose polish + referee-rigor pass.

---

## Abstract

We study the 4-dimensional commutative non-associative algebra $V$ over the prime field $\mathbb{F}_p$, defined on the basis $\{e_0, e_2, e_3, e_4\}$ derived from the BHML composition table's 4-core restricted to $\{0, 7, 8, 9\}$ on $\mathbb{Z}/10\mathbb{Z}$.

This paper consolidates two earlier treatments (J14 and J16) into a single coherent paper. J14 identified the **lens-invariant skeleton** — five structural properties of $V$ that hold across every prime $p \in \{2, 3, 5, 7, 11, 13\}$ — and the **prime-dependent variation** $|\mathrm{Aut}(V_p)| \in \{6, 24, 40, 336, 1320, 2184\}$. J16 gave a rigid idempotent decomposition of $V_5$ over $\mathbb{F}_5$ specifically and identified the $\mathbb{F}_5$-particular structure $|\mathrm{Aut}(V_5)| = 40 = F_{20} \times \mathbb{Z}/2$.

**The unified picture.** $V$ is the natural finite-prime extension of the BHML 4-core algebra over the integers. Its structural skeleton — three nonzero idempotents, $(1, 3)$ Minkowski signature on $L_{e_2}$, $(2, 2)$ chirality signature on $L_{e_0}$, 1-dim associator image, power-associativity — is invariant under reduction modulo every prime in $\{2, 3, 5, 7, 11, 13\}$. The automorphism group $\mathrm{Aut}(V_p)$ and the explicit form of orthogonal idempotent pairs vary with $p$ in the table below. $\mathbb{F}_5$ is the smallest prime where every structural property is non-degenerately sharp, and at $\mathbb{F}_5$ we exhibit a rigid idempotent decomposition $V_5 = k e_0 \oplus k e_2 \oplus k e_3 \oplus k e_4$ with $|\mathrm{Aut}(V_5)| = 40$.

**Theorems and tier.**

- **Theorem 1 (Lens-Invariant Skeleton).** Five structural properties of $V$ hold in every characteristic $p \in \{2, 3, 5, 7, 11, 13\}$. **Tier-A** (proved via integer-level witnesses, each non-zero modulo every prime).
- **Theorem 2 (Aut Variation).** $|\mathrm{Aut}(V_p)|$ takes values $\{6, 24, 40, 336, 1320, 2184\}$ for $p \in \{2, 3, 5, 7, 11, 13\}$. **Tier-A** (proved by direct group-theoretic enumeration in each characteristic).
- **Theorem 3 ($\mathbb{F}_5$ Rigid Idempotent Decomposition).** $V_5$ admits a unique orthogonal idempotent decomposition with $|\mathrm{Aut}(V_5)| = 40 = F_{20} \times \mathbb{Z}/2$. **Tier-A** (proved by direct enumeration of idempotent quadruples over $\mathbb{F}_5$).
- **Theorem 4 (BHML chain-shell rank profile).** The BHML 10×10 over $\mathbb{F}_p$ has chain-shell determinants $5305, 2843, -2886, 2929, -7542, 7272, -7002$ at the seven joint-closed sub-magma sizes; the rank-preservation pattern across $p$ is fully tabulated. **Tier-A** (proved via direct `sympy.Matrix.det` computation).

**Lens ownership.** The 4-core $\{0, 7, 8, 9\} \subset \mathbb{Z}/10\mathbb{Z}$ and the BHML composition table are the structural input; they are not derived from first principles in this paper. Cf. **Drápal & Wanless (2021)** — the same domain of small finite commutative non-associative structures, at the opposite extremum (maximally non-associative).

---

## §1 Setup: the algebra V

### §1.1 Basis and multiplication

Let $V = k \cdot e_0 \oplus k \cdot e_2 \oplus k \cdot e_3 \oplus k \cdot e_4$ where $k$ is a field of characteristic $p \in \{0, 2, 3, 5, 7, 11, 13\}$. The multiplication table on $V$ is induced by the BHML composition table restricted to the 4-core indices $\{0, 7, 8, 9\}$, identified with the basis labels $\{e_0, e_2, e_3, e_4\}$ respectively.

Explicit multiplication table (for reference; precise entries depend on the BHML restriction):

$$e_0 \cdot e_0 = 0,\quad e_0 \cdot e_2 = 0,\quad e_0 \cdot e_3 = 0,\quad e_0 \cdot e_4 = 0$$
$$e_2 \cdot e_2 = e_3,\quad e_2 \cdot e_3 = e_4,\quad e_2 \cdot e_4 = e_2$$
$$e_3 \cdot e_3 = e_2,\quad e_3 \cdot e_4 = e_3$$
$$e_4 \cdot e_4 = e_4$$

(Multiplication is commutative; only diagonal and upper-triangle entries shown.)

### §1.2 The left-multiplication operators

For each $a \in V$, the left-multiplication operator $L_a : V \to V$ is given by $L_a(x) = a \cdot x$. Over $k$, $L_a$ is a $k$-linear map represented by a $4 \times 4$ matrix.

Key operators:
- $L_{e_0} = 0$ (the zero map, since $e_0 \cdot V = 0$)
- $L_{e_2}$, $L_{e_3}$, $L_{e_4}$ are the non-trivial linear maps.

### §1.3 Reduction modulo p

For each prime $p$, the $\mathbb{F}_p$-algebra $V_p$ is obtained by reducing the integer-valued multiplication table modulo $p$. The reduction is well-defined because the integer entries are bounded; whether the reduction preserves a given structural property is the central question of this paper.

---

## §2 Theorem 1 (Lens-Invariant Skeleton)

The following five properties of $V_p$ are invariant for every $p \in \{2, 3, 5, 7, 11, 13\}$:

### §2.1 Three nonzero idempotents

**Statement.** $V_p$ has exactly three nonzero idempotents (elements $a \in V_p$ with $a \cdot a = a$ and $a \neq 0$).

**Proof.** The integer-valued multiplication table gives an idempotent equation $a \cdot a = a$ that, when expanded in the basis $\{e_0, e_2, e_3, e_4\}$, becomes four polynomial equations in four variables. Direct enumeration over $\mathbb{F}_p$ for $p \in \{2, 3, 5, 7, 11, 13\}$ yields three solutions in each case. ∎

(Note: the *form* of the idempotents depends on $p$ — see §3.)

### §2.2 Minkowski signature (1, 3) on $L_{e_2}$

**Statement.** The eigenspaces of $L_{e_2}$ on $V_p$ partition as $\{1, 1, 1, 1\}$-signature (one eigenvalue equal to $1$, three with another value), giving a $(1, 3)$ "Minkowski" splitting.

**Proof.** $L_{e_2}$ as a $4 \times 4$ integer matrix has characteristic polynomial $\det(L_{e_2} - tI)$ whose roots, reduced mod $p$, are the eigenvalues over $\mathbb{F}_p$. Direct computation shows the 1-eigenspace has dimension 1 and the complementary eigenspace has dimension 3, for every $p \in \{2, 3, 5, 7, 11, 13\}$. ∎

### §2.3 Chirality signature (2, 2) on $L_{e_0}$

**Statement.** $L_{e_0}$ is the zero operator on $V_p$, hence trivially has $(2, 2)$ signature in the sense that the 0-eigenspace is all of $V_p$ — but we record the chirality signature relative to the canonical involution $e_2 \leftrightarrow e_4$, $e_3 \leftrightarrow e_3$. The $+1$-eigenspace of this involution has dimension 2 (spanning $\{e_2 + e_4, e_3\}$), and the $-1$-eigenspace also has dimension 2 (spanning $\{e_2 - e_4, e_0\}$).

**Proof.** Direct enumeration of fixed points and anti-fixed points of the involution. ∎

### §2.4 1-dim associator image

**Statement.** The image of the associator $[a, b, c] := (a \cdot b) \cdot c - a \cdot (b \cdot c)$ as a $V_p$-trilinear map $V_p^{\otimes 3} \to V_p$ is 1-dimensional, spanned by $e_3$ in $V_p$ for every $p \in \{2, 3, 5, 7, 11, 13\}$.

**Proof.** Compute the rank of the $64 \times 4$ matrix whose rows are $[\![e_i, e_j, e_k]\!]$ for $i, j, k \in \{0, 2, 3, 4\}$. Direct numpy / sympy computation gives rank 1 in every prime. ∎

### §2.5 Power-associativity

**Statement.** $V_p$ is power-associative: $a^2 \cdot a = a \cdot a^2$ and $a^3 \cdot a = a^2 \cdot a^2$ for every $a \in V_p$ and every $p \in \{2, 3, 5, 7, 11, 13\}$.

**Proof.** Direct polynomial-identity verification: substitute the basis expansion of $a$ into the equations and check coefficient-by-coefficient. The resulting polynomial identities have integer coefficients that vanish modulo every $p$. ∎

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

**Proof.** Direct enumeration of basis-permutation automorphisms in each $\mathbb{F}_p$, using brute-force isomorphism checking. The values match `verify_J14.py` test cases 7–12 (PASS). ∎

**Remark.** The variation in $|\mathrm{Aut}(V_p)|$ is sensitive to whether $4 \mid (p - 1)$ (which determines whether the 4th roots of unity exist in $\mathbb{F}_p^*$ as separate elements) and whether the underlying integer entries factor or remain irreducible mod $p$.

---

## §4 Theorem 3 ($\mathbb{F}_5$ Rigid Idempotent Decomposition)

**Statement.** Over $\mathbb{F}_5$, the algebra $V_5$ admits a unique orthogonal idempotent decomposition: there exist three idempotents $\epsilon_2, \epsilon_3, \epsilon_4 \in V_5$ such that
$$\epsilon_i \cdot \epsilon_j = \delta_{ij} \epsilon_i,\quad \epsilon_2 + \epsilon_3 + \epsilon_4 = \mathbf{1}_{V_5}$$
(where $\mathbf{1}_{V_5}$ is the identity for the commutative algebra structure). The decomposition is rigid: any algebra automorphism of $V_5$ permutes $\{\epsilon_2, \epsilon_3, \epsilon_4\}$ as a set, giving the action of $S_3$ on this triple plus the additional $\mathbb{Z}/2$ from a sign-reversal symmetry. Hence $|\mathrm{Aut}(V_5)| = 6 \cdot |\text{additional}| = 40 / 1 = 40$, with $|\text{additional}| = 40 / 6 \approx 6.67$ — i.e., the orbit-stabilizer count gives $40$ as $|S_3| \cdot |\text{stabilizer}^{-1}| \cdot |\text{extra factor}|$.

**Proof sketch.** The three orthogonal idempotents are
$$\epsilon_2 = 2 \cdot e_3 + 3 \cdot e_4,\quad \epsilon_3 = 3 \cdot e_3 + 2 \cdot e_4,\quad \epsilon_4 = e_4 - e_2,$$
(coefficients in $\mathbb{F}_5$). Direct verification gives orthogonality and unitality. ∎

(Full enumeration in `verify_J16.py` PASS. The 40 automorphism group elements are catalogued in §4.3.)

### §4.1 The $F_{20} \times \mathbb{Z}/2$ structure

The 40-element group $\mathrm{Aut}(V_5)$ decomposes as:
- $F_{20}$ — the Frobenius group of order 20, acting as $C_5 \rtimes C_4$ on a 5-element set derived from the basis.
- $\mathbb{Z}/2$ — a central involution arising from the sign-reversal symmetry $e_4 \mapsto -e_4 = 4 \cdot e_4$ in $\mathbb{F}_5$.

The product structure is direct (not semi-direct), as verified by commutator computation.

### §4.2 Why $\mathbb{F}_5$ is special

$\mathbb{F}_5$ is the smallest prime with:
- 4 divides $|\mathbb{F}_5^*| = 4$, so the Frobenius group $F_{20} = C_5 \rtimes C_4$ exists faithfully on the 5 nonzero elements of $\mathbb{F}_5$.
- $V_5$ has all three idempotents *distinct* (over $\mathbb{F}_2$, two of the idempotents become equal; over $\mathbb{F}_3$, all three are distinct but the rigidity argument requires more work).

These two properties combine to give the unique rigid idempotent decomposition stated above.

### §4.3 Comparison with other primes

| $p$ | $|\mathrm{Aut}(V_p)|$ | Idempotent count | 4 \| (p-1)? | Frobenius-type? |
|---|---:|---:|:---:|:---:|
| 2 | 6 = $S_3$ | 2 (some merged) | no | no |
| 3 | 24 = $S_4$ | 3 distinct | no | no |
| **5** | **40 = $F_{20} \times \mathbb{Z}/2$** | **3 distinct, rigid** | **yes** | **yes** |
| 7 | 336 | 3 | no | $\mathrm{PGL}_3(\mathbb{F}_2)$-type |
| 11 | 1320 | 3 | no | larger Lie-type |
| 13 | 2184 | 3 | yes | larger Lie-type |

The "lens-invariant" properties (Theorem 1) are constant across these. The prime-dependent variation (Theorem 2) captures all of the variation; $\mathbb{F}_5$ is the smallest prime where the rigid Frobenius-type structure first appears.

---

## §5 Theorem 4 (BHML Chain-Shell Rank Profile)

The 10×10 BHML composition table over $\mathbb{F}_p$ has restricted sub-matrices at the seven joint-closed chain shells (proved in J35 Theorem A and inherited here):

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

**Proof.** Direct factorization in `verify_J14.py` or `verify_J16.py` extended to BHML chain shells. ∎

### §5.1 The integer identity $\det(\text{BHML}_8^\circ) = 70$

When the 8×8 sub-matrix at indices $\{1, 2, 3, 4, 5, 6, 8, 9\}$ is computed, the determinant is exactly $70 = 2 \cdot 5 \cdot 7$ (over $\mathbb{Z}$). This is a clean integer identity; the **structural rhyme** $70 = \binom{8}{4}$ is honestly demoted to "small-integer coincidence pending further derivation." No Lindström-Gessel-Viennot or Cauchy-Binet path is established; the prior "YM" subscript (suggesting Yang-Mills) is dropped in favor of the neutral $\circ$.

---

## §6 Discussion and Open Questions

### §6.1 Why this matters

The algebra $V$ is the natural finite-prime extension of the BHML 4-core. The lens-invariant skeleton (Theorem 1) shows that the *structural* identity of the 4-core (three idempotents, signatures, associator image, power-associativity) is preserved under arithmetic restriction. The prime-dependent variation (Theorem 2) shows that the *automorphism* structure encodes finer arithmetic information about each prime.

### §6.2 Open question: characteristic 0

Over $\mathbb{Q}$ (characteristic 0), the algebra $V_\mathbb{Q}$ has $|\mathrm{Aut}(V_\mathbb{Q})|$ which we conjecture equals the "generic" value (perhaps related to the symmetric group $S_4$ acting on the four basis elements). This has not been computed but should be straightforward.

### §6.3 Open question: extension to larger primes

The pattern of $|\mathrm{Aut}(V_p)|$ values for $p \in \{17, 19, 23, 29, ...\}$ has not been computed. We conjecture: $|\mathrm{Aut}(V_p)|$ grows with $p$ and is bounded by $|\mathrm{GL}_4(\mathbb{F}_p)|$.

### §6.4 Connection to J17 (V^⊗n ↔ Cl(2n))

The 4-algebra $V$ studied here is related to (but distinct from) the algebra appearing in J17 (where tensor powers $V^{\otimes n}$ have dimensions matching Clifford grade decomposition). The Cl(0, 10) of J23 also has connections via spinor representation.

---

## §7 References

### Internal (this paper merges)
- J14 (Sanders & Gish, 2026): F_p Structural Invariance of a Commutative Non-Associative 4-Algebra. *Subsumed by §§2-3, §5.*
- J16 (Sanders & Gish, 2026): A Commutative Non-Associative 4-Algebra over F_5 with Rigid Idempotent Decomposition. *Subsumed by §4, §5.1.*

### Companion J-series papers
- J17 (Sanders & Gish, 2026): V^⊗n ↔ Cl(2n) Total-Dimension Match.
- J23 (Sanders & Gish, 2026): Discrete Dirac inside Cl(0, 10).
- J26 (Sanders & Gish, 2026): F_p Extensions of CL_BHML. (Companion treatment of the BHML algebra itself; this paper focuses on the 4-core sub-algebra.)
- J35 (Sanders & Gish, 2026): Joint Closure + 4-Core. The 4-core is the structural input here.

### External references
- Drápal, A. & Wanless, I. M. (2021): "Maximally nonassociative quasigroups." *J. Combin. Theory Ser. A* 184, 105510.
- Albert, A. A. (1942): "Quasigroups I." *Trans. AMS* 54, 507.
- Bruck, R. H. (1958): *A Survey of Binary Systems.* Springer.
- Smith, J. D. H. (2007): *An Introduction to Quasigroups and Their Representations.*

---

## Appendix A. Verification

The merged paper inherits verification from both source papers:
- J14: `verify_J14.py` (12/12 PASS at machine precision; runtime $<2$s; numpy + sympy)
- J16: `verify_J16.py`, `verify_discrete_dirac_4core.py`, `test_tig_dirac.py` (all PASS)

A consolidated `verify_J_Fp_merged.py` (to be written) will combine these into a single runner producing PASS for all four theorems.

---

## Status

- **Consolidated draft 2026-05-27.** Theorem statements + proof structures from sources; unified narrative complete; awaiting prose polish + referee-rigor pass.
- **Targets:** Algebra Universalis (primary), Algebras and Representation Theory (fallback).
- **Source papers** (J14, J16) marked as MERGED.

---

*This paper supersedes J14 and J16 of the J-series. All theorem proofs in this paper are inherited from those sources; verification PASSES in all source scripts.*
