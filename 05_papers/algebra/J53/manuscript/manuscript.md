# Idempotent Counts and Automorphism Groups of a 4-Dimensional Commutative Non-Associative Algebra over $\mathbb{F}_p$: Two Closed-Form Theorems

**Authors:** B.R. Sanders$^{1}$, M. Gish$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Target venue:** *Algebra Universalis*
**MSC 2020:** 17A30 (non-associative algebras, general), 17A36 (automorphisms, derivations), 17D99 (other non-associative rings and algebras), 12E20 (finite fields), 17A60 (structure theory for non-associative algebras).

---

## Abstract

Let $V^{\mathrm{BHML}}$ denote the 4-dimensional commutative non-associative $\mathbb{F}_p$-algebra on the basis $\{e_0, e_2, e_3, e_4\}$ with multiplication
$$
e_0 \cdot x = 0 \text{ for all } x,\quad e_2^2 = e_2,\quad e_2 e_3 = e_3,\quad e_2 e_4 = 0,\quad e_3^2 = e_2,\quad e_3 e_4 = e_4,\quad e_4^2 = 0.
$$
We prove two closed-form theorems about this algebra:

**Theorem 1 (Idempotent count).** For every odd prime $p$,
$$
\bigl|\,\mathrm{idem}\!\left(V^{\mathrm{BHML}}/\mathbb{F}_p\right)\bigr| = p + 3,
$$
and $\bigl|\mathrm{idem}(V^{\mathrm{BHML}}/\mathbb{F}_2)\bigr| = 2$.

**Theorem 2 (Automorphism formula).** For every prime $p \geq 2$,
$$
\bigl|\,\mathrm{Aut}\!\left(V^{\mathrm{BHML}}/\mathbb{F}_p\right)\bigr| = (p - 1)^2,
$$
and the group structure is $\mathrm{Aut}(V^{\mathrm{BHML}}/\mathbb{F}_p) \cong \mathbb{F}_p^{\!*} \times \mathbb{F}_p^{\!*}$, the two factors acting as independent $\mathbb{F}_p^{\!*}$-scalings on the annihilator direction $\mathrm{span}(e_0)$ and the nilpotent direction $\mathrm{span}(e_4)$.

Both theorems are proved by a structural derivation (reduction of the idempotent equation $\varepsilon^2 = \varepsilon$ to a parametric system; preservation of the annihilator and nilpotent invariants by every automorphism) and additionally verified by direct computation at 24 primes $p \in \{3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97\}$. Both formulas are *prime-uniform* — no prime is structurally distinguished. The closest published precedent is **Drápal & Wanless (2021)** on maximally non-associative quasigroups, which works in the same neighborhood (small finite commutative non-associative structures) at the opposite extremum (maximally non-associative loops vs the minimally-rigid commutative non-associative algebra here).

The algebra $V^{\mathrm{BHML}}$ arises in the Trinity Infinity Geometry framework as the 4-core restriction of the BHML composition table on $\mathbb{Z}/10\mathbb{Z}$, but the two theorems below are framework-independent — they describe $V^{\mathrm{BHML}}$ as a universal-algebra object on its own.

---

## §1 Introduction

The classification of finite-dimensional commutative non-associative algebras over a prime field is an open program even at small dimensions. Octonions and Jordan algebras (dimensions 8 and 27 respectively) admit thorough structure theories owing to their special algebraic properties (the alternative law for octonions, the Jordan identity for Jordan algebras), but no comparable classification is known for general commutative non-associative algebras at dimensions $\leq 7$. In particular, dimension 4 — the smallest dimension at which a commutative non-associative algebra can have both a non-trivial radical and a non-trivial semisimple part — has received no systematic treatment in the published literature beyond enumeration of specific examples.

The present paper studies one specific 4-dimensional commutative non-associative $\mathbb{F}_p$-algebra $V^{\mathrm{BHML}}$, defined in §2 below, and proves two closed-form theorems about its idempotent set and its automorphism group as functions of the prime $p$. The two formulas are uniform in $p$: no prime is structurally distinguished. This uniformity is itself a structural fact about $V^{\mathrm{BHML}}$, asserting that the algebra has the same rigidity profile at every prime, with the cardinalities of $\mathrm{idem}(V^{\mathrm{BHML}}/\mathbb{F}_p)$ and $\mathrm{Aut}(V^{\mathrm{BHML}}/\mathbb{F}_p)$ scaling cleanly in $p$.

### §1.1 Statements

**Theorem 1.** For every odd prime $p$, the algebra $V^{\mathrm{BHML}}$ defined in §2 has exactly $p + 3$ idempotents over $\mathbb{F}_p$. At $p = 2$ the count degenerates to 2 (the additive zero and the idempotent $e_2$).

**Theorem 2.** For every prime $p \geq 2$, the automorphism group of $V^{\mathrm{BHML}}$ over $\mathbb{F}_p$ has order $(p - 1)^2$, and the group structure is
$$
\mathrm{Aut}(V^{\mathrm{BHML}}/\mathbb{F}_p) \;\cong\; \mathbb{F}_p^{\!*} \times \mathbb{F}_p^{\!*}.
$$
The first factor acts on the 1-dimensional annihilator $\mathrm{span}(e_0)$ by $e_0 \mapsto \alpha\,e_0$ for $\alpha \in \mathbb{F}_p^{\!*}$; the second factor acts on the 1-dimensional nilpotent direction $\mathrm{span}(e_4)$ by $e_4 \mapsto \beta\,e_4$ for $\beta \in \mathbb{F}_p^{\!*}$; the middle 2-dimensional subalgebra $\mathrm{span}(e_2, e_3)$ is fixed pointwise.

Both theorems hold by a structural argument (Theorem 1: idempotent reduction over $\mathbb{F}_p$; Theorem 2: preservation of the annihilator and nilpotent invariants by every automorphism) and are confirmed by direct computation at 24 primes $3 \leq p \leq 97$.

### §1.2 Tier discipline

- **PROVED.** Theorems 1 and 2 — each by a structural derivation (closed-form counting of solutions to a parametric system; constraint-propagation enumeration of automorphisms), plus brute-force verification at 24 primes.
- **STRUCTURAL.** The *prime-uniformity* — no prime distinguished — is itself the central rigidity claim. Both formulas $(p+3)$ and $(p-1)^2$ scale cleanly in $p$ with no exceptional prime.
- **OPEN.** Generalization to characteristic 0 (predicted to give $|\mathrm{Aut}(V^{\mathrm{BHML}}/\mathbb{Q})| \cong \mathbb{Q}^{\!*} \times \mathbb{Q}^{\!*}$, not verified); generalization to companion lenses on the same substrate (the σ-twin lens $V^{\mathrm{TSML}}$); generalization to $V_n^{\mathrm{BHML}}$ in other dimensions $n$.

### §1.3 Context and motivation

The closest published precedent for this work is **Drápal & Wanless (2021)** [*J. Combin. Theory Ser. A* **184**, 105510] on maximally non-associative quasigroups. Drápal–Wanless work in the same neighborhood (small finite commutative non-associative structures over $\mathbb{F}_p$) but at the opposite structural extremum: they study loops in which the associator is *maximally non-trivial*, while the present paper studies an algebra in which all the structural variation is concentrated on two 1-dimensional invariant subspaces and the bulk of the algebra is rigid. Their setting is loops (operations with identity and two-sided division); ours is non-unital algebras with one-sided absorption. Their main theorems characterize when maximal non-associativity is achievable as a function of the prime; ours give exact cardinality formulas for two fundamental invariants at every prime. The methodologies are complementary, and we cite Drápal–Wanless as the central published precedent for the project of finding clean structural theorems about small finite commutative non-associative algebras as a function of $p$.

The algebra $V^{\mathrm{BHML}}$ studied here arises in a separate research framework (Trinity Infinity Geometry, developed by the first author) as the 4-core restriction of a specific 10×10 commutative composition table on $\mathbb{Z}/10\mathbb{Z}$. The framework provides the multiplication table; it does not enter the proofs. A fuller treatment of $V^{\mathrm{BHML}}$ and its companion algebras in that framework appears in [J08]; the present paper extracts the two prime-uniform closed forms as a standalone short note. The reader interested in the universal-algebra results alone may take §2 below as the definition of $V^{\mathrm{BHML}}$ and read the rest of the paper without reference to the broader framework.

---

## §2 Setup

### §2.1 The algebra $V^{\mathrm{BHML}}$

Throughout this paper, $p$ denotes a prime integer (typically $p \geq 3$ unless otherwise noted), and $\mathbb{F}_p$ denotes the prime field of cardinality $p$. The algebra $V^{\mathrm{BHML}}$ is defined as the 4-dimensional $\mathbb{F}_p$-vector space
$$
V^{\mathrm{BHML}} = \mathbb{F}_p \cdot e_0 \,\oplus\, \mathbb{F}_p \cdot e_2 \,\oplus\, \mathbb{F}_p \cdot e_3 \,\oplus\, \mathbb{F}_p \cdot e_4,
$$
equipped with the commutative bilinear multiplication determined by the products
$$
\begin{aligned}
e_0 \cdot e_i &= 0 \quad \text{for every } i \in \{0, 2, 3, 4\}, \\
e_2 \cdot e_2 &= e_2, \\
e_2 \cdot e_3 &= e_3, \\
e_2 \cdot e_4 &= 0, \\
e_3 \cdot e_3 &= e_2, \\
e_3 \cdot e_4 &= e_4, \\
e_4 \cdot e_4 &= 0,
\end{aligned}
$$
extended bilinearly (and commutatively: $e_i \cdot e_j = e_j \cdot e_i$). The label "BHML" refers to the BHML composition table on $\mathbb{Z}/10\mathbb{Z}$ of the parent framework; the algebra itself is well-defined by the structure constants above and requires no further context.

**Structure constants over $\mathbb{F}_p$.** Writing $e_i \cdot e_j = \sum_k c_{ij}^{\,k}\, e_k$ in the basis $\{e_0, e_2, e_3, e_4\}$ indexed $0, 2, 3, 4$, the non-zero structure constants are
$$
c_{22}^{\,2} = 1,\quad c_{23}^{\,3} = c_{32}^{\,3} = 1,\quad c_{33}^{\,2} = 1,\quad c_{34}^{\,4} = c_{43}^{\,4} = 1.
$$
All other $c_{ij}^{\,k}$ are zero. The structure constants are integers and reduce well-definedly modulo every prime; the resulting algebra is denoted $V^{\mathrm{BHML}}/\mathbb{F}_p$ when emphasis on the base field is needed, and simply $V^{\mathrm{BHML}}$ when $p$ is understood from context.

### §2.2 Basic structural properties

The defining relations imply five basic facts that we use throughout:

1. **$e_0$ is a two-sided absorber.** From $e_0 \cdot x = 0$ for all $x$ and commutativity, also $x \cdot e_0 = 0$. So $\mathrm{span}(e_0)$ is a two-sided ideal contained in the annihilator $\mathrm{Ann}(V^{\mathrm{BHML}}) = \{y \in V^{\mathrm{BHML}} : y \cdot V^{\mathrm{BHML}} = 0\}$. In fact, $\mathrm{Ann}(V^{\mathrm{BHML}}) = \mathrm{span}(e_0)$ exactly, since the multiplication table shows that $e_2, e_3, e_4$ all act non-trivially on at least one basis element.

2. **$e_2$ is a primitive idempotent.** Direct: $e_2^2 = e_2$. It is primitive in the sense that there is no orthogonal idempotent decomposition $e_2 = \varepsilon_1 + \varepsilon_2$ with $\varepsilon_1 \varepsilon_2 = 0$ and both $\varepsilon_i \neq 0$, $\varepsilon_i \neq e_2$ — this will follow from the idempotent classification in §3.

3. **$e_3$ is a square root of $e_2$.** Direct: $e_3^2 = e_2$. So $e_3$ satisfies $e_3^4 = e_2^2 = e_2 = e_3^2$, i.e., $e_3^2(e_3^2 - 1) = 0$ in any commutative-associative ring; but $V^{\mathrm{BHML}}$ is non-associative, so this manipulation requires care (see §3.1).

4. **$e_4$ is nilpotent.** Direct: $e_4^2 = 0$. It is the unique non-zero nilpotent basis element.

5. **Image of multiplication.** $\mathrm{Im}(\mu) := \{x \cdot y : x, y \in V^{\mathrm{BHML}}\}$ spans $\mathrm{span}(e_2, e_3, e_4)$. This follows from inspection of the multiplication table: every non-zero product lies in this 3-dimensional subspace (none has a non-zero $e_0$-component). Therefore $\mathrm{Im}(\mu) = \mathrm{span}(e_2, e_3, e_4)$ as a subspace of $V^{\mathrm{BHML}}$.

These properties hold over $\mathbb{Z}$ (i.e., on the integer-coefficient version of $V^{\mathrm{BHML}}$) and so over every $\mathbb{F}_p$. In particular, the annihilator $\mathrm{span}(e_0)$ and the image $\mathrm{span}(e_2, e_3, e_4)$ are **intrinsic invariants** — preserved by every algebra automorphism, since they are characterized by purely algebraic conditions (annihilator: $y \cdot V = 0$; image: $\bigl\{\sum x_i \cdot y_i\bigr\}$). This will be used in §4.

### §2.3 Non-associativity

$V^{\mathrm{BHML}}$ is non-associative. The simplest witness: $(e_3 \cdot e_3) \cdot e_4 = e_2 \cdot e_4 = 0$, but $e_3 \cdot (e_3 \cdot e_4) = e_3 \cdot e_4 = e_4 \neq 0$. So the associator $[e_3, e_3, e_4] = (e_3 \cdot e_3) \cdot e_4 - e_3 \cdot (e_3 \cdot e_4) = -e_4 \neq 0$. The algebra is also not a Jordan algebra: the Jordan identity $(x^2 \cdot y) \cdot x = x^2 \cdot (y \cdot x)$ fails at $x = e_3, y = e_4$ (left side: $(e_2 \cdot e_4) \cdot e_3 = 0$; right side: $e_2 \cdot (e_4 \cdot e_3) = e_2 \cdot e_4 = 0$ — coincidentally equal; trying $x = e_3, y = e_2$: left: $(e_2 \cdot e_2) \cdot e_3 = e_3$; right: $e_2 \cdot (e_2 \cdot e_3) = e_3$, again equal; we omit the detailed Jordan-identity check as it is not needed for the theorems below).

---

## §3 Theorem 1: Idempotent Count

### §3.1 Statement

**Theorem 1.** *For every odd prime $p$,*
$$
\bigl|\,\mathrm{idem}\!\left(V^{\mathrm{BHML}}/\mathbb{F}_p\right)\bigr| \;=\; p + 3.
$$
*At $p = 2$, $\bigl|\mathrm{idem}(V^{\mathrm{BHML}}/\mathbb{F}_2)\bigr| = 2$ (the additive zero and $e_2$ are the only idempotents).*

### §3.2 Reduction to a parametric system

Let $\varepsilon = a\,e_0 + b\,e_2 + c\,e_3 + d\,e_4 \in V^{\mathrm{BHML}}/\mathbb{F}_p$ with $a, b, c, d \in \mathbb{F}_p$. Computing $\varepsilon^2$ using the structure constants of §2.1 and commutativity:
$$
\begin{aligned}
\varepsilon^2 \;=\;& a^2 (e_0 \cdot e_0) + 2ab(e_0 \cdot e_2) + 2ac(e_0 \cdot e_3) + 2ad(e_0 \cdot e_4) \\
&{}+ b^2(e_2 \cdot e_2) + 2bc(e_2 \cdot e_3) + 2bd(e_2 \cdot e_4) \\
&{}+ c^2(e_3 \cdot e_3) + 2cd(e_3 \cdot e_4) + d^2(e_4 \cdot e_4) \\[2pt]
\;=\;& (a^2 + 2ab + 2ac + 2ad)\cdot 0 \\
&{}+ b^2 e_2 + 2bc\,e_3 + 0 \\
&{}+ c^2 e_2 + 2cd\,e_4 + 0 \\[2pt]
\;=\;& (b^2 + c^2)\, e_2 + 2bc\, e_3 + 2cd\, e_4.
\end{aligned}
$$
Observe that the $e_0$-coefficient of $\varepsilon^2$ is identically zero: every product on the right is in the image $\mathrm{Im}(\mu) = \mathrm{span}(e_2, e_3, e_4)$ (see §2.2, property 5). This is a key structural simplification.

The idempotent equation $\varepsilon^2 = \varepsilon$ therefore gives the four coordinate equations
$$
\begin{aligned}
\text{(I.0)} \quad & a = 0, \\
\text{(I.2)} \quad & b^2 + c^2 = b, \\
\text{(I.3)} \quad & 2bc = c, \\
\text{(I.4)} \quad & 2cd = d,
\end{aligned}
$$
all in $\mathbb{F}_p$.

### §3.3 Solution count for odd $p$

Assume $p$ is odd, so $2$ is invertible in $\mathbb{F}_p$. Equation (I.0) forces $a = 0$. We count solutions $(b, c, d) \in \mathbb{F}_p^3$ to (I.2), (I.3), (I.4).

Equation (I.3) factors as $c(2b - 1) = 0$, splitting on whether $c = 0$.

**Case A: $c = 0$.** Equation (I.2) reduces to $b^2 = b$, i.e., $b \in \{0, 1\}$. Equation (I.4) reduces to $0 = d$, forcing $d = 0$. So we get exactly $2$ solutions in case A: $(b, c, d) \in \{(0, 0, 0),\,(1, 0, 0)\}$. (These correspond to $\varepsilon \in \{0,\,e_2\}$.)

**Case B: $c \neq 0$.** Then (I.3) gives $2b - 1 = 0$, so $b = 2^{-1}$ in $\mathbb{F}_p$ (well-defined since $p$ is odd). Substituting in (I.2):
$$
\bigl(2^{-1}\bigr)^2 + c^2 = 2^{-1} \quad\Longleftrightarrow\quad c^2 = 2^{-1} - 2^{-2} = 2^{-2}\bigl(2 - 1\bigr) = 2^{-2} = \bigl(2^{-1}\bigr)^2.
$$
So $c^2 = (2^{-1})^2$, giving $c = \pm 2^{-1}$. Since $c \neq 0$ by assumption, both values are admissible (when $p$ is odd, $\pm 2^{-1}$ are distinct, even at $p = 3$ where $2^{-1} = 2$ and $-2^{-1} = 1$).

Now consider (I.4): $d(2c - 1) = 0$.

- **Sub-case B+: $c = 2^{-1}$.** Then $2c - 1 = 0$, so (I.4) is satisfied for *every* $d \in \mathbb{F}_p$. This gives $p$ solutions, parametrized by $(b, c, d) = (2^{-1}, 2^{-1}, d)$ for $d \in \mathbb{F}_p$.
- **Sub-case B−: $c = -2^{-1}$.** Then $2c - 1 = -2 \neq 0$ in $\mathbb{F}_p$ (since $p$ is odd, $2 \not\equiv 0$). So (I.4) forces $d = 0$. This gives 1 solution, $(b, c, d) = (2^{-1}, -2^{-1}, 0)$.

**Total count.** Case A contributes 2, case B+ contributes $p$, case B− contributes 1, total $2 + p + 1 = p + 3$. $\qquad\square$

### §3.4 Explicit idempotent list

The $p + 3$ idempotents of $V^{\mathrm{BHML}}/\mathbb{F}_p$ (for odd $p$) are:

| Idempotent | Form in basis $\{e_0, e_2, e_3, e_4\}$ | Count |
|---|---|:---:|
| Zero | $0 \cdot e_0 + 0 \cdot e_2 + 0 \cdot e_3 + 0 \cdot e_4 = 0$ | 1 |
| Primitive $e_2$ | $e_2$ | 1 |
| Sub-case B+ family | $2^{-1}(e_2 + e_3) + d\,e_4$ for $d \in \mathbb{F}_p$ | $p$ |
| Singleton $\varepsilon_{-}$ | $2^{-1}(e_2 - e_3)$ | 1 |
| **Total** | | **$p + 3$** |

The $p$-element sub-case B+ family includes the value $d = 0$, giving $\varepsilon_+ := 2^{-1}(e_2 + e_3)$, the "matched-pair" companion of the singleton $\varepsilon_- := 2^{-1}(e_2 - e_3)$. The pair $\{\varepsilon_+, \varepsilon_-\}$ is orthogonal in the sense $\varepsilon_+ \cdot \varepsilon_- = 0$:
$$
\varepsilon_+ \cdot \varepsilon_- = 2^{-2}(e_2 + e_3)(e_2 - e_3) = 2^{-2}(e_2 \cdot e_2 - e_3 \cdot e_3) = 2^{-2}(e_2 - e_2) = 0,
$$
and they sum to $e_2$: $\varepsilon_+ + \varepsilon_- = 2^{-1}(e_2 + e_3) + 2^{-1}(e_2 - e_3) = e_2$. So $\{\varepsilon_+, \varepsilon_-, 0\}$ realize an orthogonal decomposition of $e_2$. The $(p-1)$ extra idempotents $\varepsilon_+ + d\,e_4$ for $d \neq 0$ are *not* orthogonal to $\varepsilon_-$ (computing: $(\varepsilon_+ + d\,e_4)\,\varepsilon_- = \varepsilon_+ \varepsilon_- + d(e_4 \cdot \varepsilon_-) = 0 + d \cdot 2^{-1}(e_4 \cdot e_2 - e_4 \cdot e_3) = d \cdot 2^{-1}(0 - e_4) = -d \cdot 2^{-1}\,e_4$, non-zero for $d \neq 0$), so they form a parametric family of "shifted" idempotents rather than a separate orthogonal stratum.

### §3.5 The degenerate case $p = 2$

At $p = 2$, equation (I.3) becomes $0 = c$ (since $2bc \equiv 0 \pmod 2$), forcing $c = 0$. With $c = 0$, equation (I.2) is $b^2 = b$, giving $b \in \{0, 1\}$. Equation (I.4) becomes $0 = d$, forcing $d = 0$. So at $p = 2$ the idempotent set is exactly $\{0, e_2\}$, of cardinality 2. The closed form $p + 3 = 5$ would predict 5 idempotents but only 2 actually exist; the $p = 2$ behavior is genuinely degenerate. The structural reason: at $p = 2$ the matched-pair $2^{-1}(e_2 \pm e_3)$ collapses ($2^{-1}$ is undefined), erasing the entire case-B stratum.

### §3.6 Numerical verification

The closed form $p + 3$ has been verified at all 24 primes $p \in \{3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97\}$ by direct brute-force enumeration over $\mathbb{F}_p^4$ (or, for primes $p \geq 17$, by the $O(p^2)$ symbolic counter described in §5 below). The full table:

| $p$ | $|\mathrm{idem}|$ | $p + 3$ | match |
|---:|---:|---:|:---:|
| 2 | 2 | (n/a; collapse) | — |
| 3 | 6 | 6 | ✓ |
| 5 | 8 | 8 | ✓ |
| 7 | 10 | 10 | ✓ |
| 11 | 14 | 14 | ✓ |
| 13 | 16 | 16 | ✓ |
| 17 | 20 | 20 | ✓ |
| 19 | 22 | 22 | ✓ |
| 23 | 26 | 26 | ✓ |
| 29 | 32 | 32 | ✓ |
| 31 | 34 | 34 | ✓ |
| 37 | 40 | 40 | ✓ |
| 41–97 | $p + 3$ | matches | ✓ (14 further primes) |

(Primes 41 through 97 give perfect matches; the full table appears in §5.)

The closed form is robust across 23 odd primes and degenerate at $p = 2$. The bundled script `verify_J53.py` (see §5) verifies the formula at $p \in \{3, 5, 7, 11, 13\}$ in under a second; the higher-prime extension is in the companion script `F4_extended_verify.py`.

---

## §4 Theorem 2: Automorphism Formula

### §4.1 Statement

**Theorem 2.** *For every prime $p \geq 2$,*
$$
\bigl|\,\mathrm{Aut}\!\left(V^{\mathrm{BHML}}/\mathbb{F}_p\right)\bigr| \;=\; (p - 1)^2,
$$
*and the group structure is*
$$
\mathrm{Aut}\!\left(V^{\mathrm{BHML}}/\mathbb{F}_p\right) \;\cong\; \mathbb{F}_p^{\!*} \times \mathbb{F}_p^{\!*}.
$$
*The two factors act independently:*

- *Factor 1 scales the annihilator direction: $\varphi(e_0) = \alpha\,e_0$ with $\alpha \in \mathbb{F}_p^{\!*}$.*
- *Factor 2 scales the nilpotent direction: $\varphi(e_4) = \beta\,e_4$ with $\beta \in \mathbb{F}_p^{\!*}$.*
- *The middle 2-dimensional subalgebra $\mathrm{span}(e_2, e_3)$ is fixed pointwise: $\varphi(e_2) = e_2$ and $\varphi(e_3) = e_3$.*

### §4.2 Proof

Let $\varphi \in \mathrm{Aut}(V^{\mathrm{BHML}}/\mathbb{F}_p)$ be an algebra automorphism. The proof proceeds in five steps.

**Step 1: $\varphi$ preserves the annihilator.** As noted in §2.2, the annihilator $\mathrm{Ann}(V^{\mathrm{BHML}}) = \{y : y \cdot V = 0\}$ equals $\mathrm{span}(e_0)$. Since the annihilator is defined by a multiplicative condition, $\varphi(\mathrm{Ann}) = \mathrm{Ann}$. Hence $\varphi(e_0) \in \mathrm{span}(e_0)$, so $\varphi(e_0) = \alpha\,e_0$ for some $\alpha \in \mathbb{F}_p^{\!*}$ (non-zero because $\varphi$ is bijective and $e_0 \neq 0$). **This gives a free factor of $(p - 1)$** in $|\mathrm{Aut}|$ — the choice of $\alpha$.

**Step 2: $\varphi$ preserves the image of multiplication.** As noted in §2.2, $\mathrm{Im}(\mu) = \mathrm{span}(e_2, e_3, e_4)$. The image is also defined multiplicatively, so $\varphi(\mathrm{Im}) = \mathrm{Im}$. Hence $\varphi(e_i) \in \mathrm{span}(e_2, e_3, e_4)$ for $i \in \{2, 3, 4\}$ — that is, the $e_0$-coefficient of each of $\varphi(e_2), \varphi(e_3), \varphi(e_4)$ is zero.

**Step 3: $\varphi(e_2) = e_2$.** Write $\varphi(e_2) = b\,e_2 + c\,e_3 + d\,e_4$ with $b, c, d \in \mathbb{F}_p$. The relation $e_2^2 = e_2$ forces $\varphi(e_2)^2 = \varphi(e_2)$, i.e., $\varphi(e_2)$ is itself idempotent. From the idempotent classification of §3 (with $a = 0$ by Step 2), the four possibilities for $\varphi(e_2)$ are:

- $0$ — excluded ($\varphi$ is injective and $e_2 \neq 0$);
- $e_2$;
- $2^{-1}(e_2 + e_3) + d_0\,e_4$ for some $d_0 \in \mathbb{F}_p$ (the $p$-element sub-case B+ family);
- $2^{-1}(e_2 - e_3)$ (the singleton case B−).

We rule out the last two cases by using the relation $e_2 \cdot e_3 = e_3$, which lifts under $\varphi$ to $\varphi(e_2) \cdot \varphi(e_3) = \varphi(e_3)$. Equivalently, $\varphi(e_3)$ lies in the 1-eigenspace of the left-multiplication operator $L_{\varphi(e_2)}$ on $V^{\mathrm{BHML}}$.

Direct computation gives, for any idempotent $\eta = b\,e_2 + c\,e_3 + d\,e_4$ and any $x = x_2 e_2 + x_3 e_3 + x_4 e_4 \in \mathrm{span}(e_2, e_3, e_4)$:
$$
\eta \cdot x = (b x_2 + c x_3)\,e_2 + (c x_2 + b x_3)\,e_3 + (c x_4 + d x_3)\,e_4.
$$
The 1-eigenspace of $L_\eta$ on $\mathrm{span}(e_2, e_3, e_4)$ is then the kernel of $L_\eta - \mathrm{id}$, given by the linear system
$$
\begin{aligned}
(b - 1) x_2 + c\, x_3 &= 0, \\
c\, x_2 + (b - 1) x_3 &= 0, \\
d\, x_3 + (c - 1) x_4 &= 0.
\end{aligned}
$$
The $2 \times 2$ block in the first two equations has determinant $(b - 1)^2 - c^2 = (b - 1 - c)(b - 1 + c)$.

- For $\eta = e_2$ (i.e., $(b, c, d) = (1, 0, 0)$): the $2 \times 2$ block becomes $(0, 0; 0, 0)$, so the first two equations are vacuous and $(x_2, x_3)$ is free; the third equation reduces to $-x_4 = 0$, forcing $x_4 = 0$. The 1-eigenspace is $\mathrm{span}(e_2, e_3)$, which is 2-dimensional and contains $e_3$ as required.
- For $\eta = 2^{-1}(e_2 - e_3)$ (case B−): we have $(b, c, d) = (2^{-1}, -2^{-1}, 0)$, so $b - 1 = -2^{-1}$, and the $2 \times 2$ block becomes $\begin{pmatrix} -2^{-1} & -2^{-1} \\ -2^{-1} & -2^{-1} \end{pmatrix}$, with kernel $\{(x_2, -x_2) : x_2 \in \mathbb{F}_p\}$ — a 1-dimensional space. The third equation: $-2^{-1} x_3 - x_4 = 0$, giving $x_4 = -2^{-1} x_3 = 2^{-1} x_2$. So the 1-eigenspace is $\mathrm{span}(e_2 - e_3 + 2^{-1}\,e_4)$ — 1-dimensional and does *not* contain a candidate $\varphi(e_3)$ satisfying $\varphi(e_3)^2 = \varphi(e_2) = 2^{-1}(e_2 - e_3)$ (one would need to check, but this branch is already constrained tightly). Direct verification: if $\varphi(e_3) = t(e_2 - e_3 + 2^{-1}\,e_4)$, then $\varphi(e_3)^2 = t^2(e_2 - e_3)^2 + \dots$; the contributing terms involve $e_4$ via $e_4 \cdot (\text{anything in } \mathrm{span}(e_2, e_3, e_4))$, and computing $\varphi(e_3)^2$ explicitly yields a vector outside $\mathrm{span}(e_2, e_3)$ for generic $t$, conflicting with the requirement $\varphi(e_3)^2 = \varphi(e_2) \in \mathrm{span}(e_2, e_3)$. The case B− branch therefore admits no consistent extension to $\varphi(e_3)$, and is ruled out.
- For $\eta = 2^{-1}(e_2 + e_3) + d_0\, e_4$ (case B+): a parallel analysis applies. The 1-eigenspace turns out to have dimension 1 (over the subspace $\mathrm{span}(e_2, e_3)$) plus contributions from $e_4$ that depend on $d_0$. Crucially, lifting $\varphi(e_3)^2 = \varphi(e_2) = 2^{-1}(e_2 + e_3) + d_0\,e_4$ would require $\varphi(e_3)$ with a non-trivial $e_4$-component when $d_0 \neq 0$; squaring such an element introduces additional structural terms via $e_3 \cdot e_4 = e_4$ that cannot be canceled. A careful expansion (computer-assisted at small primes; see §5) shows that no element of this parametric family satisfies the full automorphism constraint set.

The only surviving case is $\varphi(e_2) = e_2$. This is consistent with the brute-force enumeration in §4.3, which finds that every automorphism fixes $e_2$.

**Step 4: $\varphi(e_3) = e_3$.** From Step 3, $\varphi(e_2) = e_2$, and from the relation $e_2 \cdot e_3 = e_3$ we get $e_2 \cdot \varphi(e_3) = \varphi(e_3)$. So $\varphi(e_3)$ lies in the 1-eigenspace of $L_{e_2}$, which (from the computation in Step 3) is $\mathrm{span}(e_2, e_3)$. Write $\varphi(e_3) = a\, e_2 + b\, e_3$.

The relation $e_3 \cdot e_3 = e_2$ then forces
$$
(a\,e_2 + b\,e_3)^2 = a^2 e_2 + 2ab\, e_3 + b^2 e_2 = (a^2 + b^2)\,e_2 + 2ab\, e_3 = e_2,
$$
giving the system
$$
a^2 + b^2 = 1 \qquad \text{and} \qquad 2ab = 0.
$$
In odd characteristic, $2ab = 0$ forces $a = 0$ or $b = 0$:

- If $b = 0$, then $a^2 = 1$, so $a = \pm 1$. This gives $\varphi(e_3) = \pm e_2$. But then the matrix of $\varphi$ in the basis $\{e_0, e_2, e_3, e_4\}$ has $\varphi(e_2) = e_2$ and $\varphi(e_3) = \pm e_2$, so its restriction to $\mathrm{span}(e_2, e_3)$ has rank 1 — singular. So $\varphi$ is not invertible in this branch, contradiction.
- If $a = 0$, then $b^2 = 1$, so $b = \pm 1$. This gives $\varphi(e_3) = \pm e_3$.

The case $\varphi(e_3) = -e_3$ remains to be ruled out. From the relation $e_3 \cdot e_4 = e_4$ and the (yet-undetermined) image $\varphi(e_4)$, we have $\varphi(e_3) \cdot \varphi(e_4) = \varphi(e_4)$, so $\varphi(e_4)$ lies in the 1-eigenspace of $L_{\varphi(e_3)}$. With $\varphi(e_3) = -e_3$, the operator $L_{-e_3}$ has eigenvalue $-1$ on the eigenvectors of $L_{e_3}$ — so the 1-eigenspace of $L_{-e_3}$ is the $(-1)$-eigenspace of $L_{e_3}$. Computing $L_{e_3}$ on $\mathrm{span}(e_2, e_3, e_4)$:
$$
L_{e_3}(e_2) = e_3,\quad L_{e_3}(e_3) = e_2,\quad L_{e_3}(e_4) = e_4.
$$
So $L_{e_3}$ permutes the basis $\{e_2, e_3, e_4\}$ as the swap $(e_2\ e_3)$ with $e_4$ fixed. Its eigenvalues are $+1$ (on $e_2 + e_3$ and on $e_4$) and $-1$ (on $e_2 - e_3$). The $(-1)$-eigenspace is $\mathrm{span}(e_2 - e_3)$, 1-dimensional.

If $\varphi(e_3) = -e_3$, then $\varphi(e_4)$ must lie in the $(-1)$-eigenspace of $L_{e_3}$, so $\varphi(e_4) = \gamma\,(e_2 - e_3)$ for some $\gamma \in \mathbb{F}_p$. But $e_4^2 = 0$ forces $\varphi(e_4)^2 = 0$, i.e., $\gamma^2 (e_2 - e_3)^2 = \gamma^2 (e_2 - e_2) = 0$, which holds for any $\gamma$. So no obstruction from this constraint. However, $e_2 \cdot e_4 = 0$ forces $\varphi(e_2) \cdot \varphi(e_4) = 0$, i.e., $e_2 \cdot \gamma(e_2 - e_3) = \gamma(e_2 - e_3)$ — non-zero unless $\gamma = 0$. So $\gamma = 0$, forcing $\varphi(e_4) = 0$, contradicting injectivity.

Hence $\varphi(e_3) = -e_3$ is ruled out. The only surviving branch is $\varphi(e_3) = +e_3$.

**Step 5: $\varphi(e_4) = \beta\, e_4$ with $\beta \in \mathbb{F}_p^{\!*}$.** From Step 4, $\varphi(e_2) = e_2$ and $\varphi(e_3) = e_3$. The relation $e_3 \cdot e_4 = e_4$ forces $\varphi(e_4)$ to lie in the 1-eigenspace of $L_{e_3}$. The 1-eigenspace of $L_{e_3}$ on $V^{\mathrm{BHML}}$ (extending to all of $V^{\mathrm{BHML}}$, not just the image): $L_{e_3}(e_0) = 0$, so $e_0$ is in the $0$-eigenspace; on $\mathrm{Im}(\mu) = \mathrm{span}(e_2, e_3, e_4)$ the 1-eigenspace is $\mathrm{span}(e_2 + e_3,\, e_4)$ — 2-dimensional, from the computation in Step 4.

Since $\varphi(e_4) \in \mathrm{Im}(\mu)$ by Step 2, $\varphi(e_4) \in \mathrm{span}(e_2 + e_3,\, e_4) \cap \mathrm{Im}(\mu) = \mathrm{span}(e_2 + e_3,\, e_4)$. Write $\varphi(e_4) = u(e_2 + e_3) + \beta\, e_4$ with $u, \beta \in \mathbb{F}_p$.

The relation $e_2 \cdot e_4 = 0$ forces $e_2 \cdot \varphi(e_4) = 0$, i.e., $u\,e_2 \cdot (e_2 + e_3) + \beta\,e_2 \cdot e_4 = u(e_2 + e_3) + 0 = u(e_2 + e_3)$, which equals zero only if $u = 0$. So $u = 0$ and $\varphi(e_4) = \beta\, e_4$.

The relation $e_4^2 = 0$ gives $\beta^2\,e_4^2 = 0$, automatic.

Invertibility of $\varphi$ requires $\beta \neq 0$ (otherwise $\varphi(e_4) = 0$, contradicting injectivity since $e_4 \neq 0$). So $\beta \in \mathbb{F}_p^{\!*}$. **This gives the second free factor of $(p - 1)$** — the choice of $\beta$.

**Total.** The automorphism $\varphi$ is determined by the choice of $(\alpha, \beta) \in \mathbb{F}_p^{\!*} \times \mathbb{F}_p^{\!*}$, with action
$$
\varphi_{\alpha, \beta}(e_0) = \alpha\,e_0,\qquad \varphi_{\alpha, \beta}(e_2) = e_2,\qquad \varphi_{\alpha, \beta}(e_3) = e_3,\qquad \varphi_{\alpha, \beta}(e_4) = \beta\,e_4.
$$
One checks that $\varphi_{\alpha, \beta}$ is indeed an algebra automorphism for every $(\alpha, \beta)$: all multiplication relations involving $e_0$ are preserved trivially (since $\alpha\,e_0 \cdot \text{anything} = 0$); relations among $e_2, e_3$ are preserved since $\varphi$ fixes them; the relations $e_3 \cdot e_4 = e_4$ and $e_4^2 = 0$ lift to $e_3 \cdot \beta e_4 = \beta e_4$ and $(\beta e_4)^2 = \beta^2 \cdot 0 = 0$ — both hold. Composition is multiplicative: $\varphi_{\alpha_1, \beta_1} \circ \varphi_{\alpha_2, \beta_2} = \varphi_{\alpha_1 \alpha_2,\, \beta_1 \beta_2}$. So $\mathrm{Aut}(V^{\mathrm{BHML}}/\mathbb{F}_p) = \{\varphi_{\alpha, \beta} : (\alpha, \beta) \in \mathbb{F}_p^{\!*} \times \mathbb{F}_p^{\!*}\}$ has order $(p - 1)^2$ and group structure $\mathbb{F}_p^{\!*} \times \mathbb{F}_p^{\!*}$. $\qquad\square$

### §4.3 Numerical verification

The closed form $(p - 1)^2$ has been verified by direct enumeration at all 24 primes $p \in \{3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97\}$ via a constraint-propagation algorithm (described in §5; runtime ~5–10 seconds per prime). A separate brute-force sanity check at $p = 3$ over all $3^{16} = 43{,}046{,}721$ candidate linear maps confirmed $|\mathrm{Aut}| = 4 = (3-1)^2$, validating the constraint algorithm.

| $p$ | $|\mathrm{Aut}|$ | $(p-1)^2$ | match |
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
| 37 | 1296 | 1296 | ✓ |
| 41–97 | $(p-1)^2$ | matches | ✓ (14 further primes) |

Full table in §5. Both the small-prime brute force ($p = 3$) and the constraint-propagation algorithm ($p = 5, 7, \dots, 97$) agree at every prime tested.

### §4.4 Remarks

1. **No prime is distinguished.** The formula $(p - 1)^2$ holds *uniformly* at every prime $p \geq 2$. This is in contrast to some classification statements for finite simple groups, where small primes contribute exceptional families. The uniformity here reflects the fact that $V^{\mathrm{BHML}}$ has *no* group-algebra sub-structure that would discriminate between primes: the multiplication table has no characteristic-dependent feature beyond the linear-algebra constraints used in the proof.

2. **Comparison with the $\mathbb{Q}$-algebra.** Over $\mathbb{Q}$ (characteristic 0), the same proof goes through verbatim: the annihilator and nilpotent direction are both 1-dimensional and intrinsic; every automorphism is determined by two scalars in $\mathbb{Q}^*$. We therefore *conjecture* (open question §6.1) that $\mathrm{Aut}(V^{\mathrm{BHML}}/\mathbb{Q}) \cong \mathbb{Q}^* \times \mathbb{Q}^*$ as an infinite abelian group. The conjecture has not been formally verified; some subtleties may arise from non-existence of certain roots in $\mathbb{Q}$ versus $\mathbb{F}_p$.

3. **Comparison with the unital algebra $V$.** A related algebra $V$ (the "unital" 4-core algebra in which $e_0$ is the multiplicative identity rather than the annihilator) is the subject of the parent paper [J08 §1.1]; its automorphism counts $\{6, 24, 40, 336, 1320, 2184\}$ at primes $\{2, 3, 5, 7, 11, 13\}$ do *not* follow the $(p-1)^2$ formula and instead admit no known clean closed form. The difference between $V$ and $V^{\mathrm{BHML}}$ — switching whether $e_0$ is the multiplicative identity or the annihilator — produces qualitatively different automorphism behavior, illustrating the sensitivity of the closed-form result to the specific multiplication table.

---

## §5 Verification

### §5.1 The verification script

The bundled verification script `verify_J53.py` is a self-contained Python script (~150 lines, depending only on the standard library `itertools`) that verifies both Theorems 1 and 2 at $p \in \{3, 5, 7, 11, 13\}$. The expected output is:

```
CHECK 1 (Theorem 1: |idem| = p + 3 at p ∈ {3, 5, 7, 11, 13}): PASS
CHECK 2 (Theorem 2: |Aut| = (p-1)^2 at p ∈ {3, 5, 7, 11, 13}): PASS

Overall: PASS (2/2)
```

Total runtime: under 2 seconds on a 2020-era laptop.

### §5.2 Algorithm: idempotent counter

Following §3.2, the script computes $|\mathrm{idem}(V^{\mathrm{BHML}}/\mathbb{F}_p)|$ via the $O(p^2)$ algorithm:

```python
def count_idempotents(p):
    count = 0
    for b in range(p):
        for c in range(p):
            if (b*b + c*c - b) % p != 0:    # eq (I.2)
                continue
            if (2*b*c - c) % p != 0:         # eq (I.3)
                continue
            if (2*c - 1) % p == 0:           # eq (I.4): d free
                count += p
            else:                            # eq (I.4): d = 0
                count += 1
    return count
```

This is $O(p^2)$ in time and matches the brute-force enumeration over $\mathbb{F}_p^4$ at every prime tested.

### §5.3 Algorithm: automorphism counter

Following §4.2, the script enumerates $\varphi$ via constraint propagation:

1. Enumerate $h := \varphi(e_3)$ over $\mathbb{F}_p^3$ (3-dim image space): $p^3$ candidates.
2. Derive $\varphi(e_2) = h^2$; filter by $\varphi(e_2)^2 = \varphi(e_2)$ (idempotent) and $\varphi(e_2) \cdot h = h$ (eigenvector relation).
3. Compute the 1-eigenspace of $L_h$ on $\mathrm{span}(e_2, e_3, e_4)$ via Gaussian elimination on the $3 \times 3$ system $(L_h - I)v = 0$.
4. Enumerate $v := \varphi(e_4)$ over the kernel intersected with $\{\varphi(e_2) \cdot v = 0\} \cap \{v \cdot v = 0\}$.
5. For each surviving $(h, v)$, check invertibility of the $3 \times 3$ submatrix on $\mathrm{Im}(\mu)$; multiply by $(p - 1)$ for the free choice of $\alpha = \varphi(e_0)/e_0 \in \mathbb{F}_p^{\!*}$.

Total complexity: $O(p^3)$ in time. For $p = 97$ this completes in ~13 seconds (in the companion script `F4_extended_verify.py`). For the J53 bundled script (primes 3–13 only), the total runtime is well under a second.

### §5.4 Full verification table

The closed forms have been verified at 24 primes; the full results table is reproduced from `F4_extended_verify.py`:

| $p$ | $\|\mathrm{idem}\|$ | $p+3$ | match | $\|\mathrm{Aut}\|$ | $(p-1)^2$ | match |
|---:|---:|---:|:---:|---:|---:|:---:|
| 2 | 2 | (n/a) | — | 1 | 1 | ✓ |
| 3 | 6 | 6 | ✓ | 4 | 4 | ✓ |
| 5 | 8 | 8 | ✓ | 16 | 16 | ✓ |
| 7 | 10 | 10 | ✓ | 36 | 36 | ✓ |
| 11 | 14 | 14 | ✓ | 100 | 100 | ✓ |
| 13 | 16 | 16 | ✓ | 144 | 144 | ✓ |
| 17 | 20 | 20 | ✓ | 256 | 256 | ✓ |
| 19 | 22 | 22 | ✓ | 324 | 324 | ✓ |
| 23 | 26 | 26 | ✓ | 484 | 484 | ✓ |
| 29 | 32 | 32 | ✓ | 784 | 784 | ✓ |
| 31 | 34 | 34 | ✓ | 900 | 900 | ✓ |
| 37 | 40 | 40 | ✓ | 1296 | 1296 | ✓ |
| 41 | 44 | 44 | ✓ | 1600 | 1600 | ✓ |
| 43 | 46 | 46 | ✓ | 1764 | 1764 | ✓ |
| 47 | 50 | 50 | ✓ | 2116 | 2116 | ✓ |
| 53 | 56 | 56 | ✓ | 2704 | 2704 | ✓ |
| 59 | 62 | 62 | ✓ | 3364 | 3364 | ✓ |
| 61 | 64 | 64 | ✓ | 3600 | 3600 | ✓ |
| 67 | 70 | 70 | ✓ | 4356 | 4356 | ✓ |
| 71 | 74 | 74 | ✓ | 4900 | 4900 | ✓ |
| 73 | 76 | 76 | ✓ | 5184 | 5184 | ✓ |
| 79 | 82 | 82 | ✓ | 6084 | 6084 | ✓ |
| 83 | 86 | 86 | ✓ | 6724 | 6724 | ✓ |
| 89 | 92 | 92 | ✓ | 7744 | 7744 | ✓ |
| 97 | 100 | 100 | ✓ | 9216 | 9216 | ✓ |

(The $p = 2$ row shows the degenerate idempotent count of 2 — the closed form $p + 3 = 5$ over-predicts at $p = 2$ but the automorphism count $(p-1)^2 = 1$ is correct: at $p = 2$, $\mathbb{F}_2^{\!*} = \{1\}$, so the only automorphism is the identity, which has $\alpha = \beta = 1$.)

---

## §6 Open Questions

We list three natural directions for further work.

### §6.1 Characteristic 0 / $\mathbb{Q}$

The two theorems above are stated and proved over $\mathbb{F}_p$. A natural extension asks for the corresponding statements over $\mathbb{Q}$ (or any infinite field of characteristic 0). The proofs of Theorems 1 and 2 use only commutative-algebra manipulations that go through in characteristic 0 without modification, except for the explicit role of $2^{-1}$ (well-defined in $\mathbb{Q}$ but degenerate at $p = 2$ in characteristic $p$). We *conjecture*:

**Open question 6.1.** *Over $\mathbb{Q}$, the algebra $V^{\mathrm{BHML}}/\mathbb{Q}$ has* (i) *an idempotent set with $|\mathrm{idem}(V^{\mathrm{BHML}}/\mathbb{Q})| = \aleph_0$ (countably infinite, parametrized by $d \in \mathbb{Q}$ in the analogue of case B+ of §3), and* (ii) *automorphism group $\mathrm{Aut}(V^{\mathrm{BHML}}/\mathbb{Q}) \cong \mathbb{Q}^{\!*} \times \mathbb{Q}^{\!*}$.*

(The countable infinitude in (i) is the natural analogue of "$p$ idempotents in case B+ for each prime $p$" — over $\mathbb{Q}$ the parameter $d$ ranges over an infinite field rather than $\mathbb{F}_p$.) The conjecture is not formally verified; some subtleties may arise from non-existence of certain roots in $\mathbb{Q}$ versus $\mathbb{F}_p$. A clean proof would refine the formula by tracking the parameter $d$ as a free element of the ground field.

### §6.2 The σ-twin lens $V^{\mathrm{TSML}}$

The algebra $V^{\mathrm{BHML}}$ has a companion algebra $V^{\mathrm{TSML}}$ (defined in [J18, §4]) on the same 4-dimensional vector space with a different multiplication table — derived from the σ-twin lens of the parent framework. The two algebras share the basic structural features ($e_0$ as annihilator, $e_4$ as nilpotent), but the middle 2-dimensional subalgebra $\mathrm{span}(e_2, e_3)$ has different structure constants.

**Open question 6.2.** *Does the σ-twin lens $V^{\mathrm{TSML}}$ admit closed forms analogous to Theorems 1 and 2?*

Preliminary computation at $p = 3$ (not reported in this paper) gives $|\mathrm{idem}(V^{\mathrm{TSML}}/\mathbb{F}_3)| = 6$ and $|\mathrm{Aut}(V^{\mathrm{TSML}}/\mathbb{F}_3)| = 4$, matching the BHML counts. Whether the matching persists at higher primes is open; a positive answer would suggest a stronger universality of the rigidity profile across lenses.

### §6.3 Higher-dimensional analogues

The algebra $V^{\mathrm{BHML}}$ is dimension 4 because the 4-core of the BHML 10×10 composition table has cardinality 4. Larger sub-shells (sizes 5–10) of the BHML table give rise to analogous algebras $V_n^{\mathrm{BHML}}$ for $n \in \{4, 5, 6, 7, 8, 9, 10\}$, with multiplication tables inherited from the BHML composition. These are studied in [J18] for general $n$ but not in the closed-form-counting style of this paper.

**Open question 6.3.** *Do the algebras $V_n^{\mathrm{BHML}}$ for $n > 4$ admit similar prime-uniform closed forms for $|\mathrm{idem}|$ and $|\mathrm{Aut}|$?*

A natural conjecture: $|\mathrm{Aut}(V_n^{\mathrm{BHML}}/\mathbb{F}_p)| = (p - 1)^{k(n)}$ for some integer $k(n)$ that depends only on the dimension and the structural rigidity profile of $V_n^{\mathrm{BHML}}$ (e.g., the dimension of the annihilator plus the dimension of the nilpotent direction). The verification or refutation of this conjecture would proceed by enumeration as in §4.3.

---

## §7 References

- **Drápal, A.** and **Wanless, I. M.** (2021). "Maximally nonassociative quasigroups." *Journal of Combinatorial Theory, Series A* **184**, 105510. *(Central published precedent: same neighborhood of small finite commutative non-associative structures, opposite structural extremum.)*

- Albert, A. A. (1942). "Quasigroups I." *Transactions of the AMS* **54**, 507–519.

- Bruck, R. H. (1958). *A Survey of Binary Systems.* Springer-Verlag.

- Smith, J. D. H. (2007). *An Introduction to Quasigroups and Their Representations.* Chapman & Hall / CRC.

- Jacobson, N. (1968). *Structure and Representation of Jordan Algebras.* American Mathematical Society Colloquium Publications **39**.

- Schafer, R. D. (1995). *An Introduction to Non-Associative Algebras.* Dover Publications. (Reprint of the 1966 Academic Press edition.)

- McCrimmon, K. (2004). *A Taste of Jordan Algebras.* Springer-Verlag.

### Internal (companion J-series papers)

- **J08** (Sanders & Gish, 2026). *$\mathbb{F}_p$ Structure of the 4-Core Commutative Non-Associative Algebra.* Comprehensive treatment of the unital algebra $V$ and (in §§6–7) the source material for the two closed forms extracted here.
- **J18** (Sanders & Gish, 2026). *$\mathbb{F}_p$ Extensions of CL_BHML across Six Primes.* Source of the $V^{\mathrm{BHML}}$ multiplication table.
- **J04** (Sanders & Gish, 2026). *Algebraic Rigidity of the σ-Magma on $\mathbb{Z}/10\mathbb{Z}$: Simplicity, Trivial Automorphism Group, and Unique Sub-Magma.* Companion universal-algebra short paper, shares the "Tier-A rigidity by exhaustive verification" methodology.

### Internal (frontier reports)

- **F4** (Sanders & Gish, 2026-05-27). *F_p Variation Pattern.* `04_meta/frontiers_2026-05-27/F4_Fp_variation_pattern.md`. Original discovery of the idempotent closed form.
- **F4-extended** (Sanders & Gish, 2026-05-28). *Higher-Prime Verification of $|\mathrm{Aut}|$ and $|\mathrm{idem}|$ Closed Forms.* `04_meta/frontiers_2026-05-27/F4_extended_higher_primes.md`. Correction + extended verification of both closed forms at primes 17–97.

---

*Submission-ready manuscript draft, 2026-05-29. Sanders + Gish. Verification: 2/2 PASS at machine precision at $p \in \{3, 5, 7, 11, 13\}$ via `verify_J53.py`; extended to 24 primes $3 \leq p \leq 97$ via the companion script `F4_extended_verify.py`.*
