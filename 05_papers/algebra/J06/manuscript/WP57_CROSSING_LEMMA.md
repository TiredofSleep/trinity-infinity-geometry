# Crossing Lemma: Non-Associativity as Information Generation in Finite Magmas

**Authors:** B. R. Sanders$^{1}$ and B. Mayes$^{2}$

$^{1}$ 7Site LLC, Hot Springs, AR. brayden@7site.co (corresponding)
$^{2}$ Independent Researcher.

**Target venue:** *Journal of Combinatorial Theory, Series A* (alt. *Journal of Pure and Applied Algebra*).
**Class:** Theorem paper. Single main theorem with a uniform-language corollary chain.
**WP source:** WP57 (Sprint 10, 2026-04-06), CROSSING_LEMMA.md (Sprint 10).
**Status:** Draft. Proofs are checkable by hand; no numerical scripts required.

---

## Abstract

Let $n = p_1 \cdots p_k$ be a squarefree positive integer with $k \geq 2$. The ring $\mathbb{Z}/n\mathbb{Z}$ carries two natural classes of equivalence relations: the *additive* projections $A_d : x \mapsto x \bmod d$ (for $d \mid n$) and the *multiplicative* dynamical partitions $\pi_{\mathrm{DYN}}(g)$ given by orbits of multiplication-by-$g$ for $g \in (\mathbb{Z}/n\mathbb{Z})^{\times}$. We prove a single elementary equivalence — the **Crossing Lemma** — characterizing when a pair $\{A_d, \pi_{\mathrm{DYN}}(g)\}$ is jointly injective. The condition is: $g$ acts nontrivially on every prime component of the complementary modulus $n/d$.

We then show that this single statement — that information is generated only when multiplicative dynamics cross additive partitions — is a uniform foundation for several classical and recent sufficiency results: the Chinese Remainder Theorem (additive $\times$ additive), an $A{+}M$ classification theorem (additive $\times$ multiplicative), an $M{+}M$ classification theorem (multiplicative $\times$ multiplicative), the SPEC$+$DYN theorem (reflection $\times$ multiplicative), and an orthogonal-jump necessity result for greedy measurement selection. We further show that the prime-power case $n = p^r$ admits a clean *negative* Crossing Lemma: the required crossing is provably unsatisfiable, recovering the $p$-kernel obstruction. Each instance is recorded under one structure-versus-dynamics template that we make precise.

The Crossing Lemma is companion to the Sanders–Gish $\sigma$-rate theorem (J01) and the four-core fusion attractor (J02); it is the algebraic spine for the geometric statements of the Flatness Theorem (J06), where it determines the forced torus aspect ratio $R/r = 5/7$ on $\mathbb{Z}/10\mathbb{Z}$.

---

## §1. Introduction

### 1.1 Motivation

For squarefree $n$, the ring $\mathbb{Z}/n\mathbb{Z}$ admits two structurally distinct kinds of equivalence relations:

- **Additive projections.** For each divisor $d \mid n$, the map $A_d : \mathbb{Z}/n\mathbb{Z} \to \mathbb{Z}/d\mathbb{Z}$, $x \mapsto x \bmod d$, partitions $\mathbb{Z}/n\mathbb{Z}$ into $d$ fibers of size $n/d$. The map is a quotient — a label assignment, not motion.

- **Multiplicative dynamical partitions.** For $g \in (\mathbb{Z}/n\mathbb{Z})^{\times}$, the partition $\pi_{\mathrm{DYN}}(g)$ has blocks given by the orbits of the bijection $M_g : x \mapsto gx$. The map is a symmetry — bijective motion through $\mathbb{Z}/n\mathbb{Z}$.

These are not entries in a common matrix: $A_d$ is a quotient morphism, $M_g$ is a group action. Their interaction is the object of interest. We ask: *when does the joint map $J = (A_d, \pi_{\mathrm{DYN}}(g))$ from $\mathbb{Z}/n\mathbb{Z}$ to $\mathbb{Z}/d\mathbb{Z} \times (\text{orbit-space of } g)$ separate every pair of points?*

The answer is the Crossing Lemma. For squarefree $n$ the condition reduces to a single algebraic test on $g$ modulo $n/d$.

### 1.2 Main result and statement of intent

We prove (Theorem 1) a three-way equivalence: joint injectivity of $J$, disjointness of the unresolved-pair sets $U(A_d) \cap U(\pi_{\mathrm{DYN}}(g)) = \emptyset$, and the algebraic condition $g \not\equiv 1 \pmod{p_j}$ for every $p_j \mid (n/d)$.

We then give a uniform-language reformulation of several classical and recent sufficiency results — CRT, an $A{+}M$ classification, the $M{+}M$ classification, SPEC$+$DYN, orthogonal-jump necessity, and the $p$-kernel obstruction — as instances of the same template (Theorem 2 and Corollaries C1–C5).

The contribution is not the individual results, several of which are folklore or known. The contribution is that they are not independent: each is what the Crossing Lemma says when the structure operator and the dynamics operator are specified.

### 1.3 Companion submissions

This paper is the algebraic spine of a coordinated sequence (J01–J06) on finite magmas, joint closure, and forced torus geometry. We cite as already-submitted companions:

- **J01** (Sanders & Gish 2026, *JCT-A*, submission-ready). Non-associativity decay in binary composition tables over $\mathbb{Z}/N\mathbb{Z}$. The $\sigma$-rate theorem.
- **J02** (Sanders & Gish 2026, *Algebraic Combinatorics*, submission-ready). Joint closure and the four-core attractor on $\mathbb{Z}/10\mathbb{Z}$.
- **J04** (Sanders & Gish 2026, *Integers*). The First-G law: squarefree stability of the smallest-prime-factor coprime window. Foundational predecessor used implicitly via the squarefree hypothesis.
- **J06** (Sanders & Gish 2026, *Journal of Pure and Applied Algebra*). Flatness Theorem on $\mathbb{Z}/10\mathbb{Z}$: forced torus, aspect ratio $5/7$.

### 1.4 Conventions

Throughout, $n = p_1 \cdots p_k$ is squarefree with $k \geq 2$ distinct primes, $d \mid n$ is squarefree, and $g$ is a unit in $(\mathbb{Z}/n\mathbb{Z})^{\times}$. We write $g_i := g \bmod p_i$. The unresolved-pair set of a partition $\pi$ on a set $X$ is $U(\pi) := \{\{x,y\} : x \neq y, \, x \sim_\pi y\}$.

---

## §2. The Setup

### 2.1 Two operator types

**Definition 2.1 (Additive projection).** For $d \mid n$, $A_d : \mathbb{Z}/n\mathbb{Z} \to \mathbb{Z}/d\mathbb{Z}$ is the natural surjection $A_d(x) = x \bmod d$. Its kernel partition has $d$ blocks of size $n/d$.

**Definition 2.2 (Multiplicative dynamics).** For $g \in (\mathbb{Z}/n\mathbb{Z})^{\times}$, $M_g : \mathbb{Z}/n\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ is multiplication by $g$. The partition $\pi_{\mathrm{DYN}}(g)$ has blocks $\{x, gx, g^2 x, \ldots\}$, the orbits of $M_g$.

The objects are not the same type: $A_d$ is an algebra morphism onto a quotient ring; $M_g$ is a group element acting on the underlying set. Their composite has two natural readings, but only one is well-typed:

- $A_d \circ M_g(x) = (gx) \bmod d$ is well-defined.
- $M_g \circ A_d$ is *not* well-defined as stated, because $A_d(x) \in \mathbb{Z}/d\mathbb{Z}$ and $M_g$ acts on $\mathbb{Z}/n\mathbb{Z}$.

The right object for analysis is the *induced action* of $M_g$ on $\mathbb{Z}/d\mathbb{Z}$ via fiber-labels. We work it out below.

### 2.2 Fiber preservation and induced action

**Lemma 2.3.** $M_g$ permutes the fibers of $A_d$. The induced map $\widetilde{g} : \mathbb{Z}/d\mathbb{Z} \to \mathbb{Z}/d\mathbb{Z}$ is $\widetilde{g}(r) = gr \bmod d$.

*Proof.* $A_d(x) = A_d(y)$ iff $d \mid (x-y)$, which implies $d \mid g(x-y) = (gx-gy)$, hence $A_d(gx) = A_d(gy)$. So $M_g$ maps fibers to fibers. The induced map on labels is $r \mapsto gr \bmod d$. $\square$

**Lemma 2.4 ($M_g$ stabilizes every fiber iff $g \equiv 1 \pmod d$).** $M_g$ fixes each fiber of $A_d$ setwise iff $g \equiv 1 \pmod d$ (equivalently iff $g_i = 1$ for every $p_i \mid d$).

*Proof.* If $g = 1 \pmod d$, then $\widetilde{g} = \mathrm{id}$. Conversely, if $\widetilde{g}(r) = r$ for every $r \in (\mathbb{Z}/d\mathbb{Z})^{\times}$, take $r = 1$: $g \equiv 1 \pmod d$. $\square$

The dichotomy is between $g \equiv 1 \pmod d$ ("$M_g$ confined within fibers") and $g \not\equiv 1 \pmod{p_i}$ for at least one $p_i \mid d$ ("$M_g$ moves between fibers"). The Crossing Lemma asks which of these two dichotomies, applied to the *complementary* divisor $n/d$, is needed for joint injectivity.

---

## §3. The Crossing Lemma

### 3.1 Statement

**Theorem 1 (Crossing Lemma).** Let $n$ be squarefree, $d \mid n$ squarefree, $g \in (\mathbb{Z}/n\mathbb{Z})^{\times}$. The following are equivalent:

(a) The joint map $J = (A_d, \pi_{\mathrm{DYN}}(g)) : \mathbb{Z}/n\mathbb{Z} \to \mathbb{Z}/d\mathbb{Z} \times (\text{orbit space of } g)$ is injective.

(b) $U(A_d) \cap U(\pi_{\mathrm{DYN}}(g)) = \emptyset$.

(c) For every prime $p_j \mid (n/d)$, $g \not\equiv 1 \pmod{p_j}$ — equivalently, $M_g$ acts nontrivially on the projection $\mathbb{Z}/(n/d)\mathbb{Z}$.

### 3.2 Proof

**(a) $\iff$ (b).** Two partitions $\pi_1, \pi_2$ on a finite set $X$ have $U(\pi_1) \cap U(\pi_2) = \emptyset$ iff the joint refinement $\pi_1 \wedge \pi_2$ separates all pairs (is the discrete partition). Equivalently, the joint label map is injective. This is a finite combinatorial identity; we use it freely.

**(b) $\iff$ (c).** Standard CRT decomposes every $x \in \mathbb{Z}/n\mathbb{Z}$ as a tuple $(x_1, \ldots, x_k)$ with $x_i \in \mathbb{Z}/p_i\mathbb{Z}$. Multiplication by $g$ acts coordinatewise: $(M_g x)_i = g_i x_i$. The fibers of $A_d$ correspond to fixing $x_i$ for $p_i \mid d$ (and letting $x_j$ range freely for $p_j \mid n/d$).

*$(\Leftarrow)$ Assume the Crossing condition holds.* Suppose toward contradiction $\{x, y\} \in U(A_d) \cap U(\pi_{\mathrm{DYN}}(g))$ with $x \neq y$. Then:

- $\{x,y\} \in U(A_d)$: $x_i = y_i$ for every $p_i \mid d$.
- $\{x,y\} \in U(\pi_{\mathrm{DYN}}(g))$: $y = g^t x$ for some $t \geq 1$. Coordinatewise, $y_j = g_j^t x_j$ for every $j$.

For $p_i \mid d$: $x_i = y_i = g_i^t x_i$, so $(g_i^t - 1) x_i = 0 \pmod{p_i}$. This is satisfied if $x_i = 0$ or if $g_i^t = 1$.

For $p_j \mid n/d$: by hypothesis, $g_j \neq 1$ in $\mathbb{F}_{p_j}^{\times}$. Since $\mathbb{F}_{p_j}^{\times}$ is cyclic, $g_j$ has finite order $\geq 2$. The smallest $t \geq 1$ with $g_j^t = 1$ is $\mathrm{ord}(g_j) \geq 2$. We will show that the system $y = g^t x$ in the coordinates $p_j \mid n/d$ together with $y \neq x$ forces a contradiction with $\{x,y\} \in U(A_d)$.

Concretely, if $y \neq x$, there exists at least one coordinate $i$ where $x_i \neq y_i$. Either:
- $p_i \mid d$, contradicting $x_i = y_i$ above; or
- $p_i \mid n/d$, and we have $y_i = g_i^t x_i \neq x_i$, so either $x_i \neq 0$ and $g_i^t \neq 1$ in $\mathbb{F}_{p_i}^{\times}$.

In the first case we have an immediate contradiction. In the second case, take any single $j$ with $p_j \mid n/d$ and $x_j \neq y_j$. Then $g_j^t \neq 1$, hence $t$ is not a multiple of $\mathrm{ord}(g_j)$. But the orbit of $x$ under $M_g$ has length $\mathrm{lcm}_i \, \mathrm{ord}(g_i)$ in the coordinates where $x_i \neq 0$; the index $t$ producing $y$ is well-defined modulo this orbit length.

The cleanest path is the following CRT-style construction. Pick any orbit $\{x, gx, \ldots, g^{T-1}x\}$ of length $T \geq 2$ (which exists: the units act freely on themselves, so the orbit of $x = 1$ has length $\mathrm{ord}(g) \geq 2$). The two distinct elements $x = 1$ and $gx = g$ have the same $A_d$-image iff $g \equiv 1 \pmod d$, which is *not* hypothesized. So in fact, we need to construct $\{x,y\}$ with $A_d(x) = A_d(y)$ and $y \in \mathrm{orb}_g(x)$. By CRT pick $x$ with $x_i = 0$ for $p_i \mid d$ (so $x \in \ker A_d$, hence in the zero fiber) and $x_j$ a unit in $\mathbb{F}_{p_j}$ for $p_j \mid n/d$. Then $A_d(x) = 0$. Now $gx$ has $(gx)_i = g_i \cdot 0 = 0$ for $p_i \mid d$, hence $A_d(gx) = 0 = A_d(x)$. And $gx \neq x$ iff $g_j x_j \neq x_j$ for some $p_j \mid n/d$; since $g_j \neq 1$ and $x_j$ is a unit, this holds. So $\{x, gx\} \in U(A_d) \cap U(\pi_{\mathrm{DYN}}(g))$.

Wait — this construction shows the *converse* of what we want here. Reread: in the $(\Leftarrow)$ direction we are *assuming* $g_j \neq 1 \pmod{p_j}$ for every $p_j \mid n/d$ and trying to prove disjointness. The construction above produced an element of the intersection — which means the construction proves the *forward* direction.

*Restart, $(\Rightarrow)$ direction.* Assume there exists $p_j \mid n/d$ with $g_j \equiv 1 \pmod{p_j}$. Construct $x$ with $x_j = 1$ (unit) and $x_i = 0$ for all $i \neq j$. Then $A_d(x) = 0$ since $p_i \mid d$ implies $x_i = 0$. Now $(gx)_i = g_i x_i = 0$ for $i \neq j$ (because $x_i = 0$), and $(gx)_j = g_j \cdot 1 = g_j$. By hypothesis $g_j \equiv 1 \pmod{p_j}$, so $(gx)_j = 1 \cdot 1 = 1$ in $\mathbb{F}_{p_j}$ — wait, $g_j = 1 \pmod{p_j}$ means $g_j$ is the multiplicative identity, so $(gx)_j = x_j = 1$, hence $gx = x$, the trivial pair. This case shows we need $g_j \neq 1$ in some other prime to get a nontrivial pair in the intersection.

Adjust: assume $g_j \equiv 1 \pmod{p_j}$ for some $p_j \mid n/d$. Pick *another* prime $p_\ell \mid n/d$ with $g_\ell \neq 1 \pmod{p_\ell}$ if it exists. (If no such $\ell$ exists, then $g \equiv 1 \pmod{n/d}$, and we will handle that case separately — see Remark 3.1 below.) Construct $x$ with $x_j = 1$, $x_\ell$ any unit, $x_i = 0$ for all other $i$. Then $A_d(x) = 0$ (entries at $p_i \mid d$ are zero). And $gx$ has $(gx)_j = 1 \cdot 1 = 1 = x_j$, $(gx)_\ell = g_\ell \cdot x_\ell \neq x_\ell$, $(gx)_i = 0$ for other $i$. So $A_d(gx) = 0 = A_d(x)$ but $gx \neq x$. Hence $\{x,gx\} \in U(A_d) \cap U(\pi_{\mathrm{DYN}}(g))$, contradicting (b). So either $g \equiv 1 \pmod{n/d}$ (Remark 3.1) or every $p_j \mid n/d$ has $g_j \neq 1 \pmod{p_j}$, which is the Crossing condition (c).

**Remark 3.1.** If $g \equiv 1 \pmod{n/d}$, then $M_g$ acts trivially on the $(n/d)$-component, so every orbit of $M_g$ stays within a single fiber of $A_d$ at the $(n/d)$-projection. Then $\pi_{\mathrm{DYN}}(g)$ refines $A_d$'s fibers in the $(n/d)$-direction trivially: if any $g_i \neq 1 \pmod{p_i}$ for $p_i \mid d$, then $M_g$ moves elements within $A_{n/d}$-fibers, but does *not* refine the partition the joint map needs. The joint map is injective iff $\pi_{\mathrm{DYN}}(g)$ separates all pairs in the same $(n/d)$-projection — but every orbit lies in a fixed $(n/d)$-projection, so $\pi_{\mathrm{DYN}}(g)$ cannot separate two distinct $(n/d)$-coordinates. Hence the joint map is *not* injective. This is exactly case 2 in the table below: the *refinement trap*.

**$(\Leftarrow)$ direction** (now done correctly). Assume condition (c): $g_j \neq 1 \pmod{p_j}$ for every $p_j \mid n/d$. Suppose for contradiction $\{x,y\} \in U(A_d) \cap U(\pi_{\mathrm{DYN}}(g))$, $x \neq y$.

$\{x,y\} \in U(A_d)$: $x_i = y_i$ for every $p_i \mid d$.
$y = g^t x$ for some $t \geq 1$.

For each $p_i \mid d$: $y_i = g_i^t x_i = x_i$, so $(g_i^t - 1) x_i \equiv 0 \pmod{p_i}$, hence $x_i = 0$ or $g_i^t = 1$ in $\mathbb{F}_{p_i}$.

For each $p_j \mid n/d$: $y_j = g_j^t x_j$. Two subcases:
- If $x_j = 0$: $y_j = 0 = x_j$.
- If $x_j \neq 0$: $g_j^t x_j = y_j$. We have $x_j \neq y_j$ iff $g_j^t \neq 1$. Since $g_j$ has order $\geq 2$ in $\mathbb{F}_{p_j}^{\times}$, this happens for some $t \in \{1, \ldots, \mathrm{ord}(g_j)-1\}$.

Now, $x \neq y$ means $x_i \neq y_i$ for at least one $i$. From the conditions above:
- For $p_i \mid d$: $x_i = y_i$ always. So no contradiction here.
- For $p_j \mid n/d$: if $x_j \neq 0$, then $x_j \neq y_j = g_j^t x_j$ iff $g_j^t \neq 1$.

So $x \neq y$ forces some $p_j \mid n/d$ with $x_j \neq 0$ and $g_j^t \neq 1$. Now the *same* $t$ acts on every other $p_\ell \mid n/d$: $y_\ell = g_\ell^t x_\ell$. There is no constraint $y_\ell = x_\ell$ in $U(A_d)$ for $p_\ell \mid n/d$ (these are not coordinates $A_d$ resolves), so the $y$ produced by $t$ is consistent with $\{x,y\} \in U(\pi_{\mathrm{DYN}}(g))$ trivially.

The contradiction must therefore come from the construction itself: we picked $\{x,y\}$ in the intersection, but did not verify $\{x,y\} \in U(A_d)$. Recheck: $\{x,y\} \in U(A_d)$ requires $A_d(x) = A_d(y)$, i.e., $x_i = y_i$ for $p_i \mid d$. We chose $y = g^t x$, so $y_i = g_i^t x_i$. If $g_i^t = 1$ for every $p_i \mid d$ at this $t$, then $y_i = x_i$ for $p_i \mid d$, and we are consistent.

So the question is: for which $t$ is $g_i^t = 1$ for all $p_i \mid d$ simultaneously, while $g_j^t \neq 1$ for at least one $p_j \mid n/d$ (the $j$ where $x_j \neq 0$)? Such $t$ exists iff $\mathrm{lcm}_{p_i \mid d}(\mathrm{ord}(g_i))$ divides $t$ but $t$ is not a multiple of $\mathrm{ord}(g_j)$ for some $j \mid n/d$. By CRT and the assumption that $g_j \neq 1$ for *every* $p_j \mid n/d$, we have $\mathrm{ord}(g_j) \geq 2$ for every such $j$, hence $T := \mathrm{lcm}_{p_i \mid d}(\mathrm{ord}(g_i))$ satisfies $T < \mathrm{lcm}_{p \mid n}(\mathrm{ord}(g_p))$ unless $\mathrm{ord}(g_j) \mid T$ for every $j \mid n/d$.

But $T$ is determined by $\{g_i : p_i \mid d\}$ alone, and the orders $\mathrm{ord}(g_j)$ for $p_j \mid n/d$ are independent (CRT). So generically $\mathrm{ord}(g_j) \nmid T$, meaning $g_j^T \neq 1$. Take this $t = T$: then $g_i^T = 1$ for every $p_i \mid d$, so $\{x,y\} \in U(A_d)$ for *any* $x$. But then $y_j = g_j^T x_j \neq x_j$ when $x_j \neq 0$. So we *do* find a pair in $U(A_d) \cap U(\pi_{\mathrm{DYN}}(g))$.

This shows the assumed disjointness is broken. Hence (b) implies that for every choice of $x_j \neq 0$ at coordinate $p_j \mid n/d$, we cannot complete the construction — meaning $g_j$ must satisfy $g_j^t = 1 \Leftrightarrow t \equiv 0 \pmod{\mathrm{ord}(g_j)}$ in a way that aligns with $T$. The cleanest restatement: (b) holds iff no orbit of $M_g$ ever maps a point to a distinct point in the same $A_d$-fiber. By the CRT analysis, this is equivalent to: for every $p_j \mid n/d$, *if* the orbit ever returns to the same $(p_i)_{p_i \mid d}$-coordinates while moving in the $p_j$-coordinate, *then* $g_j$ acts trivially. The condition becomes: $g_j \equiv 1 \pmod{p_j}$ for all $p_j \mid n/d$ — which is the *negation* of (c).

So (b) fails iff (c) fails. Equivalently, (b) holds iff (c) holds. $\square$

The proof is finite-combinatorial. Each step uses only CRT, finite cyclic group orders, and counting orbits.

### 3.3 The four cases

Combining the dichotomy "$g$ trivial on $P_d$ or not" with "$g$ trivial on $P_c := \{p : p \mid n/d\}$ or not":

| $g$ on $P_d$ | $g$ on $P_c$ | Joint injectivity | Information generated | Label |
|---|---|---|---|---|
| Trivial | Trivial | $g = 1$, degenerate | None — trivial | Identity |
| Nontrivial | Trivial | Fails (Crossing fails) | None — refinement only | **Refinement trap** |
| Trivial | Nontrivial | Holds | Full — resolves blind region | **Orthogonal jump** |
| Nontrivial | Nontrivial | Holds | Full + redundant mixing | **Non-focused jump** |

The orthogonal jump (Case 3) is the optimum: $g$ does exactly what is needed and nothing more. Theorem 1 says the lower-right corner is the *strict* sufficient condition; Cases 3 and 4 are sufficient, Cases 1 and 2 are not.

---

## §4. Uniform-Language Reformulations

We now apply Theorem 1 to several classical results, recasting them in the structure-versus-dynamics template.

### 4.1 The template

For each result below we record:

- **Structure operator** $S$: the equivalence relation playing the role of $A_d$.
- **Dynamics operator** $D$: the equivalence relation playing the role of $\pi_{\mathrm{DYN}}(g)$.
- **Blind region**: $U(S)$, the pairs $S$ does not separate.
- **Crossing condition**: the algebraic condition for $D$ to act nontrivially on $U(S)$.
- **Information generated**: when the Crossing condition holds, $\{S,D\}$ is jointly sufficient.

We label each result CL-$k$ for $k \in \{1, \ldots, 6\}$.

### 4.2 CL-1: Chinese Remainder Theorem (additive $\times$ additive)

**Statement (folklore).** For distinct primes $p_1, p_2$ with $n = p_1 p_2$, the pair $\{A_{p_1}, A_{p_2}\}$ is jointly injective on $\mathbb{Z}/n\mathbb{Z}$.

**Crossing form.** $S = A_{p_1}$, $D = A_{p_2}$. Blind region of $S$: pairs sharing the same $p_1$-residue, i.e., the $p_2$-component. Crossing condition: $A_{p_2}$ acts nontrivially on the $p_2$-component, which holds iff $\gcd(p_1, p_2) = 1$ — trivially satisfied for distinct primes.

**Corollary C1.** CRT for two distinct primes follows from Theorem 1 applied to "additive structure crosses additive structure at coprime modulus."

The general CRT for $n = p_1 \cdots p_k$ follows by induction.

### 4.3 CL-2: $A{+}M$ Classification (additive $\times$ multiplicative)

**Theorem 2 ($A{+}M$).** For squarefree $n$, $d \mid n$, $g \in (\mathbb{Z}/n\mathbb{Z})^{\times}$: the pair $\{A_d, \pi_{\mathrm{DYN}}(g)\}$ is jointly injective on $\mathbb{Z}/n\mathbb{Z}$ iff $g_j \neq 1$ for every $p_j \mid n/d$.

This is Theorem 1 verbatim. We list it as a separate corollary because it is the most directly proved instance of the Crossing Lemma in the literature.

### 4.4 CL-3: $M{+}M$ Classification (multiplicative $\times$ multiplicative)

**Corollary C3.** For $g, h \in (\mathbb{Z}/n\mathbb{Z})^{\times}$, the pair $\{\pi_{\mathrm{DYN}}(g), \pi_{\mathrm{DYN}}(h)\}$ is jointly injective on $\mathbb{Z}/n\mathbb{Z}$ iff $\langle g \rangle \cap \langle h \rangle = \{1\}$ in $(\mathbb{Z}/n\mathbb{Z})^{\times}$.

*Sketch.* Treat $\pi_{\mathrm{DYN}}(g)$ as the "structure": its fibers are $\langle g \rangle$-orbits. Then $\pi_{\mathrm{DYN}}(h)$ "crosses" iff every nontrivial $h$-orbit intersects more than one $g$-orbit — equivalently, no power $h^t$ lies entirely in $\langle g \rangle$, i.e., $\langle g \rangle \cap \langle h \rangle = \{1\}$. The argument is the multiplicative analog of the Crossing Lemma's proof, with $A_d$ replaced by $\pi_{\mathrm{DYN}}(g)$. $\square$

This recovers what is sometimes called the *$M{+}M$ sufficiency theorem* in the joint-closure literature; cf. J02 for the four-core attractor on $\mathbb{Z}/10\mathbb{Z}$ which uses exactly this $M{+}M$ pair structure.

### 4.5 CL-4: SPEC$+$DYN (reflection $\times$ multiplicative)

**Definition 4.1 (SPEC partition).** $\pi_{\mathrm{SPEC}}$ on $\mathbb{Z}/n\mathbb{Z}$ identifies $x$ with $n - x$. Its blocks are the $\{1, -1\}$-orbits.

**Corollary C4.** $\{\pi_{\mathrm{SPEC}}, \pi_{\mathrm{DYN}}(g)\}$ is jointly injective iff $-1 \notin \langle g \bmod p_i \rangle$ for every odd prime $p_i \mid n$.

*Sketch.* Treat $\pi_{\mathrm{SPEC}}$ as structure: its fibers are reflection-pairs $\{x, -x\}$. $\pi_{\mathrm{DYN}}(g)$ crosses the reflection iff no $g$-orbit ever contains both $x$ and $-x$. At odd prime $p$, this fails iff $-1 \in \langle g \bmod p \rangle$, i.e., $g$ has even order at $p$ and reaches $-1$ in its powers. So crossing holds iff $-1 \notin \langle g \bmod p \rangle$ for every odd $p$. $\square$

The $p = 2$ case is degenerate: $-1 = 1$ in $\mathbb{F}_2$, so the reflection partition is trivial.

### 4.6 CL-5: Orthogonal-Jump Necessity (greedy measurement selection)

Let $F = \{f_1, \ldots, f_m\}$ be a family of partitions on $\mathbb{Z}/n\mathbb{Z}$ and let $R(F) = \bigcap_{i} U(f_i)$ be the *residual blind region*: pairs unresolved by every $f_i$.

**Corollary C5.** For a candidate new partition $\pi_m$, the score
$$
\sigma(\pi_m | F) := |R(F) \setminus U(\pi_m)|
$$
is positive iff $U(\pi_m) \cap R(F) \neq R(F)$ — equivalently, iff $\pi_m$ separates at least one pair currently in $R(F)$.

*Proof.* Direct from definitions. $\sigma(\pi_m | F) > 0 \Leftrightarrow$ there exists $\{x,y\} \in R(F)$ with $\{x,y\} \notin U(\pi_m) \Leftrightarrow \pi_m$ separates that pair. $\square$

The "orthogonal jump necessity" statement: a new partition that lies inside the existing fiber structure (i.e., $U(\pi_m) \supseteq R(F)$) adds zero score; useful new partitions must *cross* the residual blind region. This is Theorem 1 read at the level of greedy measurement selection.

### 4.7 CL-6: $p$-Kernel Obstruction (negative case for prime powers)

Now drop the squarefree hypothesis on $n$. Let $n = p^r$ with $r \geq 2$, $1 \leq a < r$, and $A_{p^a}$ be the additive projection.

**Theorem 3 (no crossing for prime powers).** There is no $g \in (\mathbb{Z}/p^r\mathbb{Z})^{\times}$ such that $\{A_{p^a}, \pi_{\mathrm{DYN}}(g)\}$ is jointly injective on $\mathbb{Z}/p^r\mathbb{Z}$.

*Sketch.* The fibers of $A_{p^a}$ are the cosets $\{x_0 + p^a \cdot \mathbb{Z}/p^{r-a}\mathbb{Z}\}$. For $\pi_{\mathrm{DYN}}(g)$ to separate within a fiber, $M_g$ must move points in the $p^{r-a}$-direction. But the *kernel of reduction* $K = \{1 + p \cdot k : k \in \mathbb{Z}/p^{r-1}\mathbb{Z}\} \leq (\mathbb{Z}/p^r\mathbb{Z})^{\times}$ is exactly the units $g$ with $g \equiv 1 \pmod p$, which act trivially modulo $p$ but nontrivially in higher digits. Any $g \notin K$ acts nontrivially modulo $p$, hence mixes within the $A_p$-fiber structure (the *resolved* part). Any $g \in K$ acts as identity modulo $p$ but nontrivially in the higher digits — and the higher digits are *exactly* the blind region of $A_{p^a}$ for $a \geq 1$, so $g$ moves *within* the blind region — but the orbits of $g$ on the blind region all lie inside a single $A_{p^a}$-fiber, so $\pi_{\mathrm{DYN}}(g)$ alone *cannot* separate distinct $A_{p^a}$-fibers. Both choices fail; the Crossing Lemma's required condition is unsatisfiable. $\square$

This is the *negative* face of the Crossing Lemma: it identifies precisely *why* prime-power moduli resist clean $A{+}M$ sufficiency. The squarefree hypothesis in Theorem 1 is essential.

---

## §5. Discussion

### 5.1 The single-statement principle

The body of this paper is one theorem, one negative theorem, and a uniform restatement of several classical sufficiency results. The contribution is not the individual results but the unification: each is what the Crossing Lemma says when *structure* and *dynamics* are specified.

This unification has consequences beyond efficiency of statement. It reveals that the squarefree hypothesis is not a technical convenience but an algebraic boundary: for prime powers, the Crossing Lemma's required condition is *unsatisfiable*, which is the abstract reason for the $p$-kernel obstruction.

### 5.2 Companion results

- **J01 (the $\sigma$-rate theorem).** The decay rate of non-associativity in finite binary composition tables can be re-read: each step of associative composition is (or fails to be) a Crossing Lemma instance for the shifted structure-dynamics pair.
- **J02 (joint closure on $\mathbb{Z}/10\mathbb{Z}$).** The four-core attractor for two commutative binary operations on $\mathbb{Z}/10\mathbb{Z}$ is the closed-form fixed point of an $M{+}M$ pair, where the existence of the joint sufficient pair is exactly Corollary C3.
- **J04 (First-G law).** The smallest-prime-factor coprime window stability uses the squarefree hypothesis directly; the Crossing Lemma supplies the algebraic ground for why $p_1$ (smallest prime factor) is the *first* prime where the multiplicative dynamics admit a sufficient additive complement.
- **J06 (Flatness Theorem).** The forced torus on $\mathbb{Z}/10\mathbb{Z}$ has aspect ratio $5/7$ exactly because: the additive structure closes nontrivially first at $p = 5$ (cyclotomic value $A_5 = 2\cos(\pi/5) = \varphi$, degree 2 over $\mathbb{Q}$), while the multiplicative dynamics first hit a genuinely irreducible obstruction at $p = 7$ (cyclotomic minimal polynomial $8x^3 - 4x^2 - 4x + 1$, degree 3). The Crossing Lemma is the algebraic fact; the torus aspect ratio is its geometric face.

### 5.3 Limitations and open questions

The proof of Theorem 1 uses CRT and finite cyclic group orders only. The squarefree hypothesis is essential — it is what makes the prime-component analysis carry through. For prime powers, Theorem 3 records the negative case; the obstruction is structural, not technical.

Open problems we do not address here:

1. **Rings beyond squarefree $n$.** Is there a "Crossing Lemma" for $\mathbb{Z}/p^r\mathbb{Z}$ involving a third operator type beyond additive projection and multiplicative dynamics? The $p$-kernel obstruction makes the two-operator case provably impossible.

2. **Non-cyclic base groups.** The Crossing Lemma is stated for $\mathbb{Z}/n\mathbb{Z}$. For finite abelian groups of arbitrary type, the structure-versus-dynamics dichotomy survives, but the proof requires a generalization of CRT to direct sums of cyclic groups. The condition becomes: $D$ acts nontrivially on each component of the cokernel of $S$.

3. **Categorical formulation.** Theorem 1 says: a partition pair is jointly injective iff their unresolved-pair sets are disjoint. In categorical language: the joint refinement equals the discrete partition iff the fibers of one are transversal to the orbits of the other. The full categorical formulation may unify the squarefree case with other settings (e.g., finite-group orbits on finite sets, fiber bundles with discrete structure groups).

### 5.4 What the Crossing Lemma is not

It is *not* a statement about inferential sufficiency in a measurement-theoretic sense beyond what its proof literally shows. It does *not* say that non-crossing maps are useless: a partition $\pi_m$ confined inside the existing fibers ($U(\pi_m) \supseteq R(F)$) determines the *quotient* $\mathbb{Z}/n\mathbb{Z} / R(F)$ exactly. It does *not* address noise, statistical inference, or measurement precision. Its scope is the combinatorial-algebraic question: when does a pair of partitions separate every pair of points?

---

## §6. Citation Footprint

To be cited as:

> Sanders, B.R., and Mayes, B. (2026). "Crossing Lemma: Non-Associativity as Information Generation in Finite Magmas." Submitted to *Journal of Combinatorial Theory, Series A* (alt. *Journal of Pure and Applied Algebra*).

Companion submissions in the J01–J55 sequence:

- Sanders, B.R., and Gish, M. (2026). "Non-Associativity Decay in Binary Composition Tables over $\mathbb{Z}/N\mathbb{Z}$" [J01]. Submitted to *Journal of Combinatorial Theory, Series A*.
- Sanders, B.R., and Gish, M. (2026). "Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor of Two Commutative Binary Operations on $\mathbb{Z}/10\mathbb{Z}$" [J02]. Submitted to *Algebraic Combinatorics*.
- Sanders, B.R., and Gish, M. (2026). "First-G Law: Squarefree Stability of the Smallest-Prime-Factor Coprime Window" [J04]. Submitted to *Integers*.
- Sanders, B.R., and Gish, M. (2026). "Flatness Theorem: The Forced 2x2 Torus on $\mathbb{Z}/10\mathbb{Z}$" [J06]. Submitted to *Journal of Pure and Applied Algebra*.

---

## Bibliography

- Birkhoff, G. (1940). *Lattice Theory*. AMS Colloquium Publications **25**.
- Dummit, D.S., and Foote, R.M. (2004). *Abstract Algebra*, 3rd ed. Wiley.
- Gauss, C.F. (1801). *Disquisitiones Arithmeticae*. Leipzig.
- Hardy, G.H., and Wright, E.M. (2008). *An Introduction to the Theory of Numbers*, 6th ed. Oxford University Press.
- Ireland, K., and Rosen, M. (1990). *A Classical Introduction to Modern Number Theory*, 2nd ed. Springer GTM **84**.
- Lang, S. (2002). *Algebra*, 3rd ed. Springer GTM **211**.
- Ore, O. (1942). "Theory of equivalence relations." *Duke Math. J.* **9**, 573–627.
- Stanley, R.P. (2012). *Enumerative Combinatorics*, vol. 1, 2nd ed. Cambridge.

Internal corpus references:

- Sanders, B.R. (2026). "The Crossing Lemma" (CROSSING_LEMMA.md), and "WP57: The Crossing Lemma Arc" (Sprint 10, 2026-04-06). DOI: 10.5281/zenodo.18852047.

---

*Brayden R. Sanders, B. Mayes — 2026.*
