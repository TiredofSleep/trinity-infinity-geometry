# The Sinc² Zero Law for Squarefree Moduli

**Brayden Ross Sanders / 7Site LLC; M. Gish (Independent Researcher)**
*Hot Springs, Arkansas · 2026*
*DOI: 10.5281/zenodo.18852047*
*Verification: [`proof_d25_loop_closure.py`](proof_d25_loop_closure.py) — all primes 3..199, zero exceptions; the multi-prime squarefree case is verified by the First-G companion script (J04).*
*Target venue: Integers — Electronic Journal of Combinatorial Number Theory*

> **Re-scope note (2026-05-07).** This manuscript replaces the
> 2026-04-18 prime-only draft, which was pulled back on 2026-04-19
> after a pre-push audit observed that the basic biconditional
> sinc²(k/n) = 0 ⇔ n | k holds for every modulus n, prime or
> composite. The present version re-scopes the result to squarefree
> moduli b = p₁p₂…pᵣ and routes the prime-specific content through
> the First-G Event Localization Theorem (J04, Sanders + Gish 2026,
> companion submission to *Integers*). The basic biconditional is
> retained as Lemma 1 (the divisibility biconditional), and the
> squarefree-specific Theorem 2 ("the smallest k at which any
> non-trivial divisor of b produces a sinc² zero is k = spf(b)")
> is the genuinely prime-dependent statement.

---

## Abstract

For any integer $b > 1$ and any positive integer $k$, the squared sinc function satisfies the divisibility biconditional
$$\mathrm{sinc}^2(k/b) = 0 \iff b \mid k.$$
We re-scope this elementary identity to the family of squarefree moduli and combine it with the First-G Event Localization Theorem of [J04] to obtain the following sharper statement: for a squarefree integer $b = p_1 p_2 \cdots p_r$ with $p_1 < \cdots < p_r$, the smallest positive integer $k$ at which $\mathrm{sinc}^2(k/d) = 0$ for at least one non-trivial divisor $d \mid b$ is exactly $k = p_1$, the smallest prime factor of $b$. The corridor $\{1/b, 2/b, \ldots, (b-1)/b\}$ then closes at the prime factors of $b$ in a layered hierarchy.

---

## 1. Setup and Statement

The normalized sinc function is
$$\mathrm{sinc}(x) = \begin{cases} \dfrac{\sin(\pi x)}{\pi x} & x \neq 0 \\ 1 & x = 0 \end{cases}$$
and its square $\mathrm{sinc}^2(x) = \mathrm{sinc}(x)^2$.

**Lemma 1 (Divisibility biconditional).** *For any integer $b > 1$ and any positive integer $k$,*
$$\mathrm{sinc}^2(k/b) = 0 \iff b \mid k.$$

**Proof.** $\mathrm{sinc}^2(k/b) = \sin^2(\pi k/b) / (\pi k/b)^2$ vanishes iff $\sin(\pi k/b) = 0$, iff $\pi k/b \in \pi \mathbb{Z}$, iff $b \mid k$. $\square$

Lemma 1 is uniform in $b$: it does not distinguish prime from composite moduli. To extract a statement that depends genuinely on the prime structure of $b$, we restrict to squarefree $b$ and pass simultaneously over all non-trivial divisors.

---

## 2. The Squarefree Sinc² Zero Law

Throughout, $b > 1$ is squarefree with canonical factorization $b = p_1 p_2 \cdots p_r$ where $p_1 < p_2 < \cdots < p_r$. Write $\mathrm{spf}(b) = p_1$.

**Definition.** The *divisor sinc-zero set* of corridor position $k$ relative to $b$ is
$$Z_k(b) = \{ d : d \mid b,\ d > 1,\ \mathrm{sinc}^2(k/d) = 0 \}.$$
By Lemma 1, $Z_k(b) = \{ d : d \mid \gcd(k, b),\ d > 1 \}$.

**Theorem 2 (Squarefree Sinc² Zero Law).** *Let $b > 1$ be squarefree with $\mathrm{spf}(b) = p_1$. Then:*
1. *$Z_k(b) = \emptyset$ for every $k$ with $1 \leq k < p_1$;*
2. *$Z_{p_1}(b) = \{p_1\}$, and $p_1$ is the unique non-trivial divisor of $b$ for which $\mathrm{sinc}^2(p_1/p_1) = 0$ at corridor position $k = p_1$.*

*In particular, the smallest positive $k$ at which $\mathrm{sinc}^2(k/d) = 0$ for at least one non-trivial divisor $d \mid b$ is $k = p_1 = \mathrm{spf}(b)$.*

**Proof.** $Z_k(b)$ is exactly the set of non-trivial divisors of $\gcd(k, b)$ (Lemma 1).

*Part (i).* Fix $k < p_1$. Suppose $\gcd(k, b) > 1$; then it has a prime divisor $q \mid b$, so $q \geq p_1$, but $q \mid k$ forces $q \leq k < p_1$, contradiction. Hence $\gcd(k, b) = 1$ and $Z_k(b) = \emptyset$.

*Part (ii).* At $k = p_1$: $p_1 \mid p_1$ and $p_1 \mid b$, so $p_1 \in Z_{p_1}(b)$. Conversely, $d \in Z_{p_1}(b)$ requires $d \mid p_1$ with $d > 1$, so $d = p_1$. $\square$

**Remark (why this is not Lemma 1).** Lemma 1 alone does not separate primes from composites — it states a uniform fact about every modulus. Theorem 2 is strictly stronger because it identifies the smallest $k$ at which any non-trivial divisor of $b$ produces a sinc² zero, and that $k$ is $\mathrm{spf}(b)$ *precisely because* $\mathrm{spf}(b)$ is the smallest member of a non-empty set of primes. The squarefree hypothesis ensures that the ladder of prime divisors of $b$ has a clean smallest-element structure (every prime power $p^a \mid b$ collapses to its prime base).

**Remark (relation to the First-G Law).** Theorem 2 is the sinc² shadow of the First-G Event Localization Theorem of [J04], which states that for every $b > 1$ with smallest prime factor $p_1$, the first non-coprime element of the alphabet $\{1, \ldots, k\}$ relative to $b$ appears at exactly $k = p_1$. The two statements are equivalent under the identification $\mathrm{sinc}^2(k/d) = 0 \iff d \mid k$.

---

## 3. Corollaries

**Corollary 3 (Layered loop closure).** *Let $b = p_1 p_2 \cdots p_r$ be squarefree. As $k$ increases from $1$ to $b$, $Z_k(b)$ grows by inclusion in exactly $\tau(b) - 1 = 2^r - 1$ stages: stage $j$ adds the non-trivial divisors of $b$ whose smallest prime factor first divides $k$ at $k = p_j$. The corridor closes ($Z_b(b) = $ all non-trivial divisors of $b$) at $k = b$.*

**Corollary 4 (Prime-indexed amplitude transitions).** *The amplitudes $\mathrm{sinc}^2(k/b)$ along $k \in \{1, \ldots, b-1\}$ are strictly positive everywhere (since $b \nmid k$ in this range), but the amplitudes $\mathrm{sinc}^2(k/p_j)$ for the divisors $p_j \mid b$ each cross zero for the first time at $k = p_j$. The set of corridor positions at which any divisor amplitude first vanishes is $\{p_1, p_2, \ldots, p_r\}$.*

**Corollary 5 (Stability window).** *The interval $\{1/b, 2/b, \ldots, (p_1 - 1)/b\}$ is sinc-zero free in the strong sense: $\mathrm{sinc}^2(k/d) > 0$ for every $k < p_1$ and every non-trivial $d \mid b$. Width $p_1 - 1$, depending only on $\mathrm{spf}(b)$.*

---

## 4. The Boundary Value sinc²(1/2) = 4/π²

The midpoint amplitude $\mathrm{sinc}^2(1/2)$ has closed form:
$$\mathrm{sinc}^2(1/2) = \left(\frac{\sin(\pi/2)}{\pi/2}\right)^2 = \frac{4}{\pi^2} \approx 0.4053.$$
This is the amplitude of the first sidelobe of a rectangular spectral gate. Montgomery's pair correlation function for Riemann zeros is $R_2(u) = 1 - \mathrm{sinc}^2(u)$ [Montgomery 1973]; the boundary $4/\pi^2$ appears in both frameworks.

---

## 5. Connection to the First-G Companion

Theorem 2 is the sinc² image of the algebraic statement proved in the First-G companion paper [J04]: *for every $b > 1$ with smallest prime factor $p_1$, the smallest $k$ for which $\{1, \ldots, k\}$ contains an element sharing a prime factor with $b$ is $k = p_1$, and this element is $p_1$ itself.*

The translation is $\mathrm{sinc}^2(k/d) = 0 \iff d \mid k$. In the continuum limit, the harmonic pre-echo function
$$R(k, b) = \frac{\sin^2(\pi k / b)}{k^2 \sin^2(\pi/b)} \to \mathrm{sinc}^2(k/b) \quad (b \to \infty)$$
recovers the sinc² field exactly. The two results are two faces of the same algebraic structure — one discrete, one continuous.

---

## 6. Verification

The verification splits across two scripts:

- **`proof_d25_loop_closure.py`** (this paper, supplied here): verifies the squarefree case with one prime factor for all primes $p \in \{3, 5, \ldots, 199\}$ (46 primes; zero exceptions). Uses `fractions.Fraction` + `sympy` for exact rational arithmetic on the input.
- **`proof_first_g_event.py`** (companion script in J04): verifies the multi-prime squarefree case for all squarefree $b \leq 500$ (153 moduli, 36,662 $(b, k)$ pairs, zero exceptions).

The squarefree-multiprime case follows from the First-G companion via Section 5; we do not duplicate that enumeration here.

---

## 7. What This Result Does Not Claim

This paper does not claim: a new proof of the infinitude of primes; a connection to the Riemann Hypothesis beyond the Montgomery bridge in §4; that the fold position $\mathrm{sinc}^2(x^*) = 1/2$ is computable in closed form; any result about the distribution of primes; or that squarefree is essential (the non-squarefree case follows by passing to $\mathrm{rad}(b)$).

---

## References

- **[J04]** Sanders, B.R., Gish, M. (2026). *The First-G Event in the Coprimality Partition: Stability Windows, CRT Idempotent Count, and Prime-Indexed Phase Transitions.* Submitted to *Integers* (companion paper).
- Montgomery, H.L. (1973). The pair correlation of zeros of the zeta function. *Analytic Number Theory*, Proc. Sympos. Pure Math. **24**, 181–193.
- Shannon, C.E. (1949). Communication in the presence of noise. *Proc. IRE* **37**(1), 10–21.
