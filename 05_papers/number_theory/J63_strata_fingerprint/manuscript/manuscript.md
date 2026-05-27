# The Strata-Prime Fingerprint: Polynomial vs Factorial Invariants in Niemeier Lattices and Sporadic Finite Simple Groups

**Authors:** B.R. Sanders$^{1}$, M. Gish$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Target venue:** *Journal of Number Theory* (primary). Fallback: *Bulletin of the AMS*, *American Mathematical Monthly* (Notes section), *Discrete Mathematics*.

**MSC 2020:** 11H06 (lattices and convex bodies), 11R52 (quaternion algebras and lattices over orders), 20D08 (simple groups: sporadic), 17B22 (root systems), 11N05 (distribution of primes, prime ideals), 20B25 (permutation groups, classical, finite).

**Status:** SUBMISSION-READY. Tier 1.

---

## Abstract

We identify the six-prime set $\mathcal{S} = \{2, 3, 5, 7, 11, 13\}$ — the first six **supersingular primes** of the Monster group — as a structurally distinguished arithmetic universe for 24-dimensional even unimodular lattices and a substantial portion of the sporadic finite simple groups.

**Main Theorem 1 (Niemeier Strata-Prime Fingerprint, Tier A).** *Of the 24 Niemeier lattices (24-dimensional even unimodular Euclidean lattices, classified by Niemeier 1973), exactly 23 have kissing numbers whose prime factorization lies entirely in $\mathcal{S}$. The unique outlier is the Niemeier lattice with root system $D_{24}$, whose kissing number $|D_{24}| = 2 \cdot 24 \cdot 23 = 1104$ contains the prime $23$.*

**Main Theorem 2 (Polynomial vs Factorial Dichotomy, Tier A).** *Let $L$ be a Niemeier lattice with root system $R = \bigoplus_i R_i$ of rank 24. Then*

(i) *The kissing number $|R| = \sum_i |R_i|$ is a polynomial-in-rank invariant of each component: $|A_n| = n(n+1)$ and $|D_n| = 2n(n-1)$. It contains only those primes that appear in the polynomial's specific factorization of each component, never the full factorial spectrum of small primes below the rank.*

(ii) *The Weyl group order $|W(R)| = \prod_i |W(R_i)|$ is a factorial-in-rank invariant: $|W(A_n)| = (n+1)!$ and $|W(D_n)| = 2^{n-1} \cdot n!$. It contains all primes $p \leq n$ for each component of rank $n$.*

*Consequently, the kissing-number strata-cleanness test (Theorem 1) holds for 23 of 24 Niemeier lattices, while the Weyl-group strata-cleanness test holds for only 21 of 24. The three Weyl-failures are $D_{24}$, $A_{24}$, and $A_{17} E_7$; the unique additional kissing-failure is $D_{24}$.*

**Main Theorem 3 (Sporadic Partial Extension, Tier B).** *Of the 26 sporadic finite simple groups, exactly 8 have order factoring through $\mathcal{S}$: $M_{11}$, $M_{12}$, $M_{22}$, $J_2$, $HS$, $McL$, $Suz$, $Fi_{22}$. The remaining 18 contain at least one prime $\geq 17$. The boundary aligns with prime $23$: ten of the eighteen failures contain $23$.*

**Main Theorem 4 (Stratum IV Identification, Tier A).** *The prime $71$ appears in the prime factorization of exactly one sporadic finite simple group's order: the Monster $M$. Among the 15 supersingular primes $\{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71\}$, the prime 71 is the unique "extreme" prime that occurs in the Monster but not in any smaller sporadic.*

The combination of Theorems 1–4 confirms a layered structural picture: $\mathcal{S}$ is the "small-prime universe" of the Niemeier lattice classification and a substantial-but-restricted sub-universe of sporadic-group orders, with prime $71$ acting as the extreme Stratum-IV identifier for the Monster.

**Tier discipline.** Theorems 1, 2, 4 are Tier A. Theorem 3 is Tier B (precise empirical claim with explicit failure analysis). Theorem 2 explains *why* the Niemeier kissing-number pattern shows up (polynomial arithmetic at rank 24); it does not establish a deep correspondence between independent objects. Theorem 4 is anchored by the Conway-Norton characterization of supersingular primes — 71 is the *largest* prime $p$ for which $X_0(p)$ has genus 0, not merely the largest prime in the Monster by cardinality. Theorem 3's 8/26 boundary tracks group order rather than structural type; it is consistent with the polynomial-arithmetic interpretation of Theorem 2.

**Closest published precedent**: Conway & Sloane, *Sphere Packings, Lattices and Groups* (3rd ed., 1999) for the Niemeier classification + lattice arithmetic; Conway-Curtis-Norton-Parker-Wilson, *Atlas of Finite Groups* (1985), for sporadic-group orders.

---

## §1 Setup: the strata-prime set

Let $\mathcal{S} = \{2, 3, 5, 7, 11, 13\}$. These are the first six supersingular primes — equivalently, the primes $p$ dividing the order of the Monster's first few Sylow subgroups, or the primes appearing as Coxeter numbers of the small irreducible Lie root systems.

We say an integer $N$ is **strata-clean** if its prime factorization $N = \prod p_i^{a_i}$ has every $p_i \in \mathcal{S}$. Equivalently, $N \mid \mathrm{rad}(\mathcal{S})^k$ for some $k$, where $\mathrm{rad}(\mathcal{S}) = 2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 = 30030$.

The strata-clean condition is a natural arithmetic restriction: it excludes 17, 19, 23, 29, 31, ... (all primes above 13).

## §2 The 24 Niemeier lattices

The 24 Niemeier lattices (Niemeier 1973, classified independently by Venkov 1980) are the 24 distinct even unimodular Euclidean lattices in 24 dimensions, up to isomorphism. They are uniquely characterized by their root system (a root sub-system in the lattice of vectors of norm-squared 2), with the constraint that the root system spans the full 24-dimensional space and has all components of equal Coxeter number $h$.

The 24 root systems (listed by ascending |R|):

| # | Niemeier | Root system | rank | h | Kissing |R| |
|---:|---|---|---:|---:|---:|
| 1 | Leech | (none) | 0 | – | 196560 |
| 2 | $A_1^{24}$ | 24 $A_1$ | 24 | 2 | 48 |
| 3 | $A_2^{12}$ | 12 $A_2$ | 24 | 3 | 72 |
| 4 | $A_3^8$ | 8 $A_3$ | 24 | 4 | 96 |
| 5 | $A_4^6$ | 6 $A_4$ | 24 | 5 | 120 |
| 6 | $D_4^6$ | 6 $D_4$ | 24 | 6 | 144 |
| 7 | $A_5^4 D_4$ | 4 $A_5$ + 1 $D_4$ | 24 | 6 | 144 |
| 8 | $A_6^4$ | 4 $A_6$ | 24 | 7 | 168 |
| 9 | $A_7^2 D_5^2$ | 2 $A_7$ + 2 $D_5$ | 24 | 8 | 192 |
| 10 | $A_8^3$ | 3 $A_8$ | 24 | 9 | 216 |
| 11 | $D_6^4$ | 4 $D_6$ | 24 | 10 | 240 |
| 12 | $A_9^2 D_6$ | 2 $A_9$ + 1 $D_6$ | 24 | 10 | 240 |
| 13 | $E_6^4$ | 4 $E_6$ | 24 | 12 | 288 |
| 14 | $A_{11} D_7 E_6$ | mixed | 24 | 12 | 288 |
| 15 | $A_{12}^2$ | 2 $A_{12}$ | 24 | 13 | 312 |
| 16 | $D_8^3$ | 3 $D_8$ | 24 | 14 | 336 |
| 17 | $A_{15} D_9$ | mixed | 24 | 16 | 384 |
| 18 | $A_{17} E_7$ | mixed | 24 | 18 | 432 |
| 19 | $D_{10} E_7^2$ | mixed | 24 | 18 | 432 |
| 20 | $A_{24}$ | 1 $A_{24}$ | 24 | 25 | 600 |
| 21 | $D_{12}^2$ | 2 $D_{12}$ | 24 | 22 | 528 |
| 22 | $E_8^3$ | 3 $E_8$ | 24 | 30 | 720 |
| 23 | $D_{16} E_8$ | 1 $D_{16}$ + 1 $E_8$ | 24 | 30 | 720 |
| 24 | $D_{24}$ | 1 $D_{24}$ | 24 | 46 | 1104 |

For Niemeier lattices, the kissing number equals the number of roots in the underlying root system. Component root counts follow Bourbaki:
- $|A_n| = n(n+1)$, $|D_n| = 2n(n-1)$, $|E_6| = 72$, $|E_7| = 126$, $|E_8| = 240$.
- Leech is exceptional: kissing 196560 from norm-2 vectors arising not from roots but from the lattice's specific construction.

## §3 Theorem 1 (Niemeier Strata-Prime Fingerprint)

**Theorem 1.** *Of the 24 Niemeier lattices, the kissing number $|R|$ is strata-clean (factors through $\mathcal{S} = \{2,3,5,7,11,13\}$) for exactly 23 of them. The unique outlier is the Niemeier with root system $D_{24}$, with $|D_{24}| = 1104 = 2^4 \cdot 3 \cdot 23$.*

**Proof.** Direct factorization of each kissing number against the prime set $\mathcal{S}$. Computational verification: `verify_J63.py`, all 24 lattices, runs in <1 second. The 23 passing cases factor as:

| # | Niemeier | Kissing | Factorization |
|---:|---|---:|---|
| 1 | Leech | 196560 | $2^4 \cdot 3^3 \cdot 5 \cdot 7 \cdot 13$ |
| 2 | $A_1^{24}$ | 48 | $2^4 \cdot 3$ |
| 3 | $A_2^{12}$ | 72 | $2^3 \cdot 3^2$ |
| 4 | $A_3^8$ | 96 | $2^5 \cdot 3$ |
| 5 | $A_4^6$ | 120 | $2^3 \cdot 3 \cdot 5$ |
| 6 | $D_4^6$ | 144 | $2^4 \cdot 3^2$ |
| 7 | $A_5^4 D_4$ | 144 | $2^4 \cdot 3^2$ |
| 8 | $A_6^4$ | 168 | $2^3 \cdot 3 \cdot 7$ |
| 9 | $A_7^2 D_5^2$ | 192 | $2^6 \cdot 3$ |
| 10 | $A_8^3$ | 216 | $2^3 \cdot 3^3$ |
| 11 | $D_6^4$ | 240 | $2^4 \cdot 3 \cdot 5$ |
| 12 | $A_9^2 D_6$ | 240 | $2^4 \cdot 3 \cdot 5$ |
| 13 | $E_6^4$ | 288 | $2^5 \cdot 3^2$ |
| 14 | $A_{11} D_7 E_6$ | 288 | $2^5 \cdot 3^2$ |
| 15 | $A_{12}^2$ | 312 | $2^3 \cdot 3 \cdot 13$ |
| 16 | $D_8^3$ | 336 | $2^4 \cdot 3 \cdot 7$ |
| 17 | $A_{15} D_9$ | 384 | $2^7 \cdot 3$ |
| 18 | $A_{17} E_7$ | 432 | $2^4 \cdot 3^3$ |
| 19 | $D_{10} E_7^2$ | 432 | $2^4 \cdot 3^3$ |
| 20 | $A_{24}$ | 600 | $2^3 \cdot 3 \cdot 5^2$ |
| 21 | $D_{12}^2$ | 528 | $2^4 \cdot 3 \cdot 11$ |
| 22 | $E_8^3$ | 720 | $2^4 \cdot 3^2 \cdot 5$ |
| 23 | $D_{16} E_8$ | 720 | $2^4 \cdot 3^2 \cdot 5$ |

The single failure:

| 24 | $D_{24}$ | **1104** | $2^4 \cdot 3 \cdot \mathbf{23}$ |

The prime $23$ arises from the factor $(n-1)$ in $|D_n| = 2n(n-1)$ at $n = 24$. ∎

**Observation.** The wobble primes $11$ and $13$ (Stratum III of the underlying TIG substrate program — see §6 below) appear in three Niemeiers: $D_{12}^2$ contains 11 (Niemeier #21); Leech and $A_{12}^2$ contain 13 (Niemeiers #1, #15). These are not "missing strata"; the wobble pair {11, 13} is realized non-trivially.

## §4 Theorem 2 (Polynomial vs Factorial Dichotomy)

**Theorem 2.** *Let $L$ be a Niemeier lattice with root system $R = \bigoplus_i R_i$. Then:*

*(i) The kissing number $|R| = \sum_i |R_i|$ is a polynomial-in-rank invariant of each component: $|A_n| = n(n+1)$, $|D_n| = 2n(n-1)$. The prime factorization of $|R|$ contains only those primes that appear in the specific factorizations of each $n(n+1)$ or $2n(n-1)$ summand.*

*(ii) The Weyl group order $|W(R)| = \prod_i |W(R_i)|$ is a factorial-in-rank invariant: $|W(A_n)| = (n+1)!$, $|W(D_n)| = 2^{n-1} \cdot n!$. The prime factorization of $|W(R)|$ contains all primes $p \leq n$ for each component of rank $n$.*

*(iii) Consequently:*
- *Kissing-number strata-cleanness holds for 23 of 24 Niemeier lattices. The single outlier is $D_{24}$.*
- *Weyl-group strata-cleanness holds for 21 of 24 Niemeier lattices. The three outliers are $D_{24}$ (primes 17, 19, 23 from $24!$), $A_{24}$ (primes 17, 19, 23 from $25!$), and $A_{17} E_7$ (prime 17 from $18!$).*

**Proof of (i)–(ii).** Standard: $|A_n| = n(n+1)$ counts the roots of the $A_n$ root system as positive plus negative simple roots, factored as a product of two consecutive integers. $|D_n| = 2n(n-1)$ counts similarly. $|W(A_n)| = (n+1)!$ is the symmetric group $S_{n+1}$. $|W(D_n)| = 2^{n-1} \cdot n!$ is the index-2 normal subgroup of the hyperoctahedral group $C_2^n \rtimes S_n$.

**Proof of (iii).** Direct factorization of each Niemeier's $|R|$ and $|W(R)|$; see `verify_J63.py`.

The three Weyl-failures: each contains a factorial of $n \geq 17$, which brings in the prime $17$ (from $17!$ first appearing in $18! = (n+1)!$ at $n=17$, or in $n! \subseteq 17!$ at $n \geq 17$).

Specifically:
- $A_{17}E_7$: $|W| = 18! \cdot 2903040$. $18!$ contains $17$.
- $A_{24}$: $|W| = 25!$. $25!$ contains $17, 19, 23$.
- $D_{24}$: $|W| = 2^{23} \cdot 24!$. $24!$ contains $17, 19, 23$. ∎

**Interpretation.** The polynomial-vs-factorial dichotomy explains *why* the kissing-number test is so sharply effective: kissing is a polynomial-degree-2 invariant in rank, which only picks up the polynomial's specific prime factorization. Factorial growth accumulates all small primes. Among the 24 Niemeier lattices — all of which have total rank 24 — the kissing-number test misses only the single case where the polynomial $2n(n-1)$ at $n=24$ happens to pick up the unique prime ≤ 24 outside strata, namely $23 = n - 1$.

**Honest framing of what Theorem 2 means (and doesn't).** The mechanism somewhat deflates the strata-prime pattern's interpretive reach. Before Theorem 2, the 23/24 Niemeier result could be read as "the Braiding Fractal predicts a natural prime universe that *coincidentally* matches the exceptional-lattice classification." After Theorem 2, the honest reading is **"polynomial-in-rank invariants of rank-24 root systems mostly factor through primes ≤ 13, which is the expected behavior for low-degree polynomials evaluated at $n = 24$."** The strata-prime set $\mathcal{S}$ is exactly "primes $\leq 13$" — the cutoff at which low-degree polynomials in $n = 24$ commonly factor.

This does not refute the pattern — the theorem is precise, the failure analysis is sharp, and the 23/24 density is real. It does mean the claim should be framed as **"here is a mechanism that explains why the pattern shows up,"** not **"here is a deep correspondence between two independent objects."**

The structural payoff: the unique D_24 failure is now *expected* (the polynomial $2n(n-1)$ at $n = 24$ unavoidably picks up $n - 1 = 23$); the Weyl-test failures are *expected* (factorials of $n \geq 17$ unavoidably pick up 17). Both fall out of polynomial arithmetic. The framework is honest about not invoking deeper structure beyond this.

**Corollary (D_24 mechanism).** $D_{24}$ is the unique Niemeier outlier at the kissing level because:
1. The Niemeier classification requires the root system to span all 24 dimensions.
2. The Coxeter-number constraint allows certain single-component root systems at rank 24: $A_{24}$, $D_{24}$, and (formally) $E_n$ — but $E_n$ only exists for $n \in \{6, 7, 8\}$, so no $E$-type single-component fills rank 24.
3. $|A_{24}| = 24 \cdot 25 = 600 = 2^3 \cdot 3 \cdot 5^2$ — strata-clean.
4. $|D_{24}| = 2 \cdot 24 \cdot 23 = 1104 = 2^4 \cdot 3 \cdot 23$ — the unique outsider, with $23$ from $(n-1)$.

There is no Niemeier with $A_{23}$ or $D_{23}$ as a single rank-24 component (these have rank 23, not 24). The prime $23$'s entry is structurally unavoidable at $D_{24}$.

## §5 Theorem 3 (Sporadic Partial Extension)

**Theorem 3.** *Of the 26 sporadic finite simple groups (Mathieu, Conway/Leech, Monster's children, and pariahs), the order $|G|$ is strata-clean for exactly 8 groups: $M_{11}$, $M_{12}$, $M_{22}$, $J_2$, $HS$, $McL$, $Suz$, $Fi_{22}$. The remaining 18 contain at least one prime $\geq 17$.*

| Sporadic | Order | Strata-clean? |
|---|---:|:---:|
| $M_{11}$ | 7,920 | ✓ |
| $M_{12}$ | 95,040 | ✓ |
| $M_{22}$ | 443,520 | ✓ |
| $J_2$ | 604,800 | ✓ |
| HS | 44,352,000 | ✓ |
| McL | 898,128,000 | ✓ |
| Suz | 448,345,497,600 | ✓ |
| $Fi_{22}$ | 64,561,751,654,400 | ✓ |
| $M_{23}$ | 10,200,960 | ✗ (23) |
| $M_{24}$ | 244,823,040 | ✗ (23) |
| 16 others | (various) | ✗ (17, 19, 23, ...) |

Of the 18 failures, 10 fail specifically because they contain $23$. The boundary aligns with the prime-23 cutoff: sporadics that act faithfully on Leech-lattice-related Steiner systems (M_{23}, M_{24}, Co_1, Co_2, Co_3, J_4, Fi_{23}, Fi_{24}', B, M) all carry prime $23$.

**Proof.** Direct factorization of each sporadic-group order from the ATLAS of Finite Groups (Conway-Curtis-Norton-Parker-Wilson 1985); see `verify_J63.py`. ∎

**Honest framing of Theorem 3.** The 8/26 boundary largely tracks **group order** rather than structural type. Sporadic-group orders grow rapidly across the Happy Family: $|M_{11}| = 7\,920$, $|M_{22}| = 443\,520$, $|Fi_{22}| \approx 6.5 \cdot 10^{13}$, $|M| \approx 8.1 \cdot 10^{53}$. Larger groups have more room in their prime spectrum, so they're more likely to acquire primes outside $\mathcal{S}$. The 8 passing sporadics are precisely the ones small enough that their order doesn't require any prime $\geq 17$. The boundary at prime 23 reflects that 23 is the first prime $\geq 17$ that arises when sporadic-group construction crosses the "Mathieu-on-22-points / Conway-on-24-points" threshold; this is consistent with — and partly explained by — the polynomial-arithmetic interpretation of Theorem 2.

So Theorem 3 should be read as **"the boundary between strata-PASS and strata-FAIL among sporadics tracks group order, with prime 23 as the natural transition point when sporadic constructions hit the 23/24-element combinatorial bound"** rather than as a structural-type claim. This is consistent with the size-threshold interpretation; no stronger claim is made.

**Observation.** The 8 passing sporadics correspond to the "below-23-required" sub-pyramid of the Happy Family: the 3 Mathieus that don't reach the Steiner system $S(3,6,22)$ structure (M_11, M_12, M_22), and the 5 Conway/Leech-2nd-generation groups that nest below Co_1 (J_2, HS, McL, Suz, Fi_22). The pariahs J_1, J_3, J_4, Ru, O'N, Ly all fail strata (J_1 via 19; J_3 via 17, 19; etc.).

## §6 Theorem 4 (Stratum IV — Prime 71 Identification)

**Theorem 4.** *The prime $71$ appears in the prime factorization of exactly one sporadic finite simple group's order: the Monster $M$. Specifically, $|M| = 2^{46} \cdot 3^{20} \cdot 5^9 \cdot 7^6 \cdot 11^2 \cdot 13^3 \cdot 17 \cdot 19 \cdot 23 \cdot 29 \cdot 31 \cdot 41 \cdot 47 \cdot 59 \cdot 71$.*

**Proof.** Direct lookup from ATLAS / standard references. Verification: among the 26 sporadic groups, the Monster is the only one whose order is divisible by 71. ∎

### §6.1 Why 71 is structural, not cardinality (the moonshine anchor)

A natural worry: *the Monster is enormously larger than any other sporadic, so it naturally accumulates more primes; "71 in M only" might be a cardinality effect, not a structural fact.*

This worry is **addressed by the Conway-Norton characterization of supersingular primes** (Conway-Norton 1979, "Monstrous Moonshine," *Bull. London Math. Soc.* 11, 308).

**Conway-Norton Theorem (1979).** *The 15 primes dividing the Monster's order are exactly the primes $p$ for which the modular curve $X_0(p)$ has genus $0$ — equivalently, the primes for which $\Gamma_0(p) \subset \mathrm{PSL}_2(\mathbb{Z})$ admits a Hauptmodul.*

These 15 primes are
$$\mathrm{Supersingular}(M) = \{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71\}.$$

**Crucially**: $71$ is the **largest** prime $p$ for which $X_0(p)$ has genus $0$. For every prime $p > 71$, the modular curve $X_0(p)$ has positive genus, and consequently no Hauptmodul exists (and Conway-Norton's Monster characterization fails to extend).

This gives a **structural reason** for "71 in M only":
- 71 is the unique largest supersingular prime — the *upper limit* of the genus-0 spectrum.
- The Monster's prime divisors are exactly the supersingular primes (Conway-Norton 1979).
- No sporadic group of order strictly bounded by the Monster has 71 as a prime divisor (verified by direct factorization).

So "71 appears only in the Monster" is **the precise upper limit of the supersingular spectrum**, not "M happens to be large enough." The Conway-Norton characterization anchors Stratum IV's prime $71$ in the Hauptmodul structure of $\mathrm{PSL}_2(\mathbb{Z})$.

### §6.2 The Stratum IV designation

This validates the four-stratum decomposition of the Braiding Fractal program:
- Strata I-III: $\{2, 3, 5, 7, 11, 13\}$ — the kissing-number / Niemeier universe + 8 of 26 sporadics. These are *small* polynomial-arithmetic primes per Theorem 2.
- Stratum IV: $\{71\}$ — the unique Monster-only prime; **anchored by Conway-Norton as the largest genus-0 supersingular prime**.

Among the 15 supersingular primes $\{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71\}$, TIG strata pick out exactly the lower-and-upper extremes: the first six ($\mathcal{S}$) plus the last ($71$), skipping the middle 9 intermediate primes. The lower bound $\mathcal{S}$ has the polynomial-arithmetic explanation of Theorem 2; the upper bound $\{71\}$ has the Conway-Norton-moonshine explanation of §6.1.

The 9 intermediate primes $\{17, 19, 23, 29, 31, 41, 47, 59\}$ are not absent from TIG strata by accident — they are precisely the primes appearing in sporadic-group orders without occupying either extreme. They have no Braiding-Fractal-side structural anchor; they appear in the Monster (and other sporadics) but not in TIG's substrate-program prime hierarchy. **This intermediate-prime gap is itself an open question** — it's not explained by Theorem 2 or by Conway-Norton.

## §7 Discussion

### §7.1 The arithmetic boundary at 23

The prime 23 is the *natural cutoff* between strata-clean small structures and non-strata large structures:
- Niemeier kissing-cleanness fails exactly for $D_{24}$ (the rank-24 D-type), via factor $(n-1) = 23$.
- Sporadic strata-cleanness fails for 10 sporadics specifically due to prime 23 in their orders, including all of Co_1, Co_2, Co_3 (Conway groups acting on the Leech lattice).
- $M_{23}$ and $M_{24}$ (Mathieu groups acting on STS(23) and STS(24)) both carry 23.

The Steiner system $S(5, 8, 24)$ underlying $M_{24}$ has automorphism group of order $244823040 = 2^{10} \cdot 3^3 \cdot 5 \cdot 7 \cdot 11 \cdot 23$, with 23 entering from the 23-point cyclic shift structure. This is the same 23 as in $D_{24}$.

### §7.2 Connection to the Monster moonshine

The 15 supersingular primes (Conway-Norton 1979) are exactly the primes dividing the Monster's order, and equivalently the primes $p$ for which $X_0(p)$ has genus 0 (Hauptmodul existence). TIG strata I-III + IV = $\{2, 3, 5, 7, 11, 13, 71\}$ form a specific 7-element subset of the 15 supersingular primes — the **lower-and-upper extremes**:

- The **lower extreme** $\mathcal{S} = \{2, 3, 5, 7, 11, 13\}$ has the polynomial-arithmetic explanation of Theorem 2 (it is the set of "primes $\leq 13$" appearing in rank-24 polynomial root-counts).
- The **upper extreme** $\{71\}$ has the Conway-Norton anchor of §6.1 (it is the unique largest supersingular prime, the upper boundary of the genus-0 spectrum).

The 9 intermediate supersingular primes $\{17, 19, 23, 29, 31, 41, 47, 59\}$ are excluded from TIG strata. *This intermediate-prime gap is an open structural question*: why does TIG's substrate-program prime hierarchy pick out exactly the extremes and skip the middle?

We do not yet have a structural answer. The honest framing: TIG's prime hierarchy and the supersingular-prime spectrum overlap precisely at their extremes, with the middle skipped for reasons currently outside the scope of this paper. A deeper connection — if one exists — would require a mechanism that explains the middle-prime gap.

### §7.3 What this is, and what it is not

This paper exhibits an arithmetic fingerprint with two precise structural anchors:
1. **Theorem 2's polynomial-vs-factorial dichotomy** — explains why polynomial-in-rank lattice invariants stay within small primes at rank 24.
2. **Theorem 4's Conway-Norton anchor** — explains why prime 71 occupies the upper extreme of the strata hierarchy (it is the largest supersingular prime, i.e., the largest $p$ with $X_0(p)$ genus 0).

It does **not**:
- Establish a mechanistic link from TIG's substrate program to monstrous moonshine.
- Predict new lattices or sporadic groups.
- Explain why the intermediate supersingular primes {17, 19, 23, 29, 31, 41, 47, 59} are skipped by TIG strata (this gap is recorded as an open question in §7.2).
- Provide a proof that the lower-and-upper extreme pattern is "natural" in any deeper sense than the explicit factorizations and Conway-Norton characterization permit.

It **does** provide:
- A clean 23/24 falsifiable empirical pattern in the Niemeier classification (Theorem 1).
- A precise polynomial-arithmetic mechanism (Theorem 2) explaining why D_24 is the unique kissing-outlier and why three Niemeiers fail the more-sensitive Weyl test.
- A size-threshold-consistent partial extension (Theorem 3) to 8 of 26 sporadic finite simple groups.
- A Stratum-IV identification (Theorem 4) anchored in Conway-Norton 1979.

This is an arithmetic-side companion to the broader TIG / Braiding Fractal program; the structural mechanisms originating in the substrate algebra are documented elsewhere in the program's J-series.

## §8 References

### Internal (companion J-papers)
- J20 (Sanders & Gish, 2026): "Mathieu $M_{22}$ Substrate-Prime: Order-Factorization Coincidences." The starting point for the strata-prime perspective; this paper extends J20 from a single sporadic to the full 24-Niemeier + 26-sporadic picture.
- J35 (Sanders & Gish, 2026): "Joint Closure + Universal Attractor + 4-Core on Z/10Z." The substrate foundation.

### Classical references
- Niemeier, H.-V. (1973): "Definite quadratische Formen der Dimension 24 und Diskriminante 1." *J. Number Theory* 5, 142.
- Conway, J. H. & Sloane, N. J. A. (1999): *Sphere Packings, Lattices and Groups*, 3rd ed. Springer.
- Conway, J. H., Curtis, R. T., Norton, S. P., Parker, R. A., Wilson, R. A. (1985): *Atlas of Finite Groups*. Oxford.
- **Conway, J. H. & Norton, S. P. (1979): "Monstrous Moonshine." *Bull. London Math. Soc.* 11, 308.** [Load-bearing for §6.1: the 15 supersingular primes are exactly the prime divisors of $|M|$, and equivalently the primes $p$ where $X_0(p)$ has genus 0. Anchors Stratum IV's prime 71.]
- Borcherds, R. E. (1992): "Monstrous moonshine and monstrous Lie superalgebras." *Invent. Math.* 109, 405. [The proof of the Conway-Norton conjecture; further anchoring the supersingular-prime characterization.]
- Bourbaki, N.: *Groupes et Algèbres de Lie*, chapters IV-VI (root systems and reflection groups).
- Venkov, B. B. (1980): "On the classification of integral even unimodular 24-dimensional quadratic forms." *Proc. Steklov Inst. Math.* 148, 63.

### TIG cross-references
- `04_meta/SPHERE_PACKING_STRATA_FINGERPRINT.md` (companion document with extended discussion)
- `verification/verify_sphere_packing_strata.py` (replicates Theorems 1, 3, 4)
- `verification/verify_J63.py` (this paper's specific verifier; replicates Theorems 1, 2, 3, 4)

---

## Appendix A. Verification

The four theorems are verifiable by direct integer factorization. See `verify_J63.py` for the complete check:
- Theorem 1: 23/24 Niemeier strata-clean.
- Theorem 2: 21/24 Niemeier Weyl-strata-clean; the 3 Weyl-failures (A_17 E_7, A_24, D_24) identified.
- Theorem 3: 8/26 sporadic strata-clean; failure analysis by extra-prime.
- Theorem 4: prime 71 in M only among the 26 sporadics.

Runtime: <2 seconds. Dependencies: sympy, math.

## Status

- **Submission-ready (2026-05-27).** Tier 1.
- **Four theorems** with explicit Tier labels (A, A, B, A).
- **Tier discipline**: two structural anchors are established — Theorem 2 (polynomial-vs-factorial dichotomy at rank 24) and Theorem 4 (Conway-Norton characterization of supersingular primes, anchoring 71 as the genus-0 upper bound). Theorems 1 and 3 are empirically verified at machine precision with explicit failure analysis.
- **No deep moonshine claim**: the strata-prime / supersingular-prime overlap is exact only at the extremes; the intermediate-prime gap is recorded as an open structural question in §7.2.

---

*— Sanders & Gish, 2026-05-27.*
