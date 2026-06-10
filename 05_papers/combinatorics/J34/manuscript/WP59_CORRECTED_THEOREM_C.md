# WP59 — Corrected Theorem C
## M+A Sufficiency for Squarefree Moduli — Complete Condition with Counterexample

**Date**: 2026-04-08
**Sprint**: 12 — UOP/GUT Arc
**Status**: Corrected theorem PROVED; counterexample COMPUTED; prior applications verified under corrected condition
**Authors**: Brayden Ross Sanders / 7Site LLC · Ben Mayes

---

## Abstract

The previously stated condition for M+A sufficiency — that the map G → (Z/dZ)* induced by multiplication is injective — is necessary but not sufficient. The error is that the prior condition accounts only for conflicts among unit elements but ignores zero-fiber conflicts: pairs {x, g·x} where x ≡ 0 mod d (so both x and g·x have the same d-residue = 0) but g acts nontrivially outside d. The correct condition is that G must act trivially on every prime of n/d. An explicit counterexample is given: n = 15, G = ⟨2⟩, d = 5. Prior specific applications (SPEC + half-modulus) are verified to satisfy the corrected condition.

---

## §1. Prior Statement and Why It Was Believed Sufficient

### 1.1 The M+A Setup

Let n = p₁···pₖ be squarefree, G ≤ (Z/nZ)*, d | n. The M+A partition pair {π_DYN(G), π_d} has:

    U(π_DYN(G)) = { {x, g·x} : g ∈ G, g ≠ 1, g·x ≠ x }
    U(π_d)      = { {x, y}   : x ≠ y, d | (x − y) }

Sufficiency requires U(π_DYN(G)) ∩ U(π_d) = ∅.

### 1.2 The Prior Condition

The prior sprint stated: {π_DYN(G), π_d} is sufficient iff the natural map φ: G → (Z/dZ)* sending g ↦ g mod d is injective.

**The argument for this condition (unit-only case):** For a unit x (gcd(x,n) = 1) and g ∈ G with g ≠ 1:

    {x, g·x} ∈ U(π_d)  ⟺  d | (g·x − x) = (g−1)·x

Since x is a unit mod d: d | (g−1)·x iff d | (g−1) iff g ≡ 1 mod d. This holds for all primes pᵢ | d: g ≡ 1 mod pᵢ for every pᵢ | d. Equivalently, φ(g) = g mod d = 1 in (Z/dZ)*. So {x, g·x} ∈ U(π_d) for unit x iff g ∈ ker(φ). No conflict among units iff ker(φ) = {1} iff φ is injective.

**Why it was believed sufficient:** The unit case covered all pairs where x is coprime to n. The zero-fiber case — elements x with gcd(x,d) > 1 — was not separately analyzed.

---

## §2. The Counterexample

**Setup** [COMPUTED]:

Let n = 15 = 3·5, G = ⟨2⟩ ≤ (Z/15Z)*, d = 5.

**Step 1: Check the prior condition.**

G = {1, 2, 4, 8} (since 2⁴ = 16 ≡ 1 mod 15, order 4).

Map φ: G → (Z/5Z)* by reduction mod 5:
- 1 mod 5 = 1
- 2 mod 5 = 2
- 4 mod 5 = 4
- 8 mod 5 = 3

Image: {1, 2, 3, 4} = (Z/5Z)*. The map φ is injective (in fact bijective). Prior condition: SATISFIED. Prior sprint predicts: SUFFICIENT.

**Step 2: Exhibit the conflict.**

Element x = 5. Note: 5 mod 5 = 0, so 5 ≡ 0 mod d. This is a zero-fiber element.

Compute T₂(5) = 2·5 = 10. Note: 10 mod 5 = 0. So 10 ≡ 0 ≡ 5 mod 5. Both 5 and 10 lie in the same π_5-block (the zero-fiber {0, 5, 10, 15 mod 15} = {0, 5, 10}).

Wait — let us be precise. π_5 partitions Z/15Z by x mod 5:
- Block 0: {0, 5, 10}
- Block 1: {1, 6, 11}
- Block 2: {2, 7, 12}
- Block 3: {3, 8, 13}
- Block 4: {4, 9, 14}

T₂-orbit of 5: T₂(5) = 10, T₂(10) = 20 mod 15 = 5. Orbit: {5, 10}. Both in block 0 of π_5.

Therefore {5, 10} ∈ U(π_5) ∩ U(π_DYN(⟨2⟩)). Conflict. {π_DYN(⟨2⟩), π_5} is NOT sufficient for n = 15. □

**Analysis of the counterexample.** Why does 5 cause a conflict? In CRT coordinates: 5 = (1 mod 2, 0 mod 3, 0 mod 5) → wait, n = 15 = 3·5, so CRT is Z/3Z × Z/5Z. In this representation: 5 = (2 mod 3, 0 mod 5). The element g = 2 has 2 mod 3 = 2 (non-trivial) and 2 mod 5 = 2 (non-trivial). Acting on 5 = (2,0): g·5 = (2·2 mod 3, 2·0 mod 5) = (4 mod 3, 0) = (1 mod 3, 0 mod 5) = 10 in Z/15Z (since 10 mod 3 = 1, 10 mod 5 = 0 ✓). Both (2,0) and (1,0) have 5-coordinate = 0 → same π_5 block. The 3-coordinate changed (from 2 to 1) because g acts non-trivially mod 3 (g ≡ 2 mod 3 ≠ 1), and n/d = 3 contains this prime.

---

## §3. The Corrected Theorem

**Theorem C (Corrected)** [PROVED]:

For squarefree n = p₁···pₖ, G ≤ (Z/nZ)*, d | n:

    {π_DYN(G), π_d} is sufficient  ⟺  G acts trivially on all primes of (n/d),
    i.e., every g ∈ G satisfies g ≡ 1 mod pⱼ for every prime pⱼ | (n/d).

**Proof.**

**(⟸) Sufficiency.** Assume G trivial on all primes of (n/d). Let g ∈ G, g ≠ 1, and x ∈ Z/nZ.

In CRT coordinates x = (a₁,...,aₖ): g acts as multiplication, aᵢ ↦ gᵢ · aᵢ mod pᵢ. Since g is trivial on primes of (n/d): gⱼ = 1 for all pⱼ | (n/d). So g changes only the coordinates at primes pᵢ | d.

Case 1 — Some pᵢ | d has gᵢ ≠ 1 and aᵢ ≠ 0: Then (g·x)ᵢ = gᵢ·aᵢ ≠ aᵢ. The d-component changes, so g·x ≢ x mod pᵢ. Therefore g·x ≢ x mod d. {x, g·x} ∉ U(π_d). No conflict.

Case 2 — For all pᵢ | d with gᵢ ≠ 1: aᵢ = 0. Then (g·x)ᵢ = gᵢ·0 = 0 = aᵢ. And for all pⱼ | (n/d): (g·x)ⱼ = gⱼ·aⱼ = 1·aⱼ = aⱼ. So g·x = x. Not a valid pair (g·x ≠ x required). No conflict.

In all cases, no conflict. □

**(⟹) Necessity.** Suppose g ∈ G with g ≢ 1 mod pⱼ for some pⱼ | (n/d). By CRT, choose x with aⱼ ≠ 0 and aᵢ = 0 for all pᵢ | d. Then:

- x ≡ 0 mod pᵢ for all pᵢ | d → x ≡ 0 mod d → x in the zero-fiber of π_d.
- g·x: (g·x)ᵢ = gᵢ · 0 = 0 for pᵢ | d. (g·x)ⱼ = gⱼ · aⱼ ≠ aⱼ (since gⱼ ≠ 1, aⱼ ≠ 0).

So g·x ≡ 0 ≡ x mod d (same π_d block) but g·x ≠ x (j-coordinate changed). Conflict. □

---

## §4. Zero-Fiber Analysis

**Definition (Zero-fiber)** [STRUCTURAL]:

The zero-fiber of π_d is F_d = {x ∈ Z/nZ : x ≡ 0 mod d} = {x : aᵢ = 0 for all pᵢ | d}. Equivalently, F_d = n/d · Z/nZ (multiples of n/d).

The zero-fiber has |F_d| = n/d elements, one for each residue class mod (n/d).

**Why zero-fiber conflicts are the critical case** [STRUCTURAL]:

For x ∈ F_d: any pair {x, g·x} with g·x ∈ F_d is automatically in U(π_d) (both in the zero-class). For g·x ∈ F_d, we need (g·x)ᵢ = 0 for all pᵢ | d. Since gᵢ ≠ 0 (g is a unit), (g·x)ᵢ = gᵢ · aᵢ = 0 iff aᵢ = 0. So g preserves F_d. Every element of F_d maps to F_d under G. The orbit of any x ∈ F_d under G is entirely within F_d.

The action of G on F_d: G acts on the non-d coordinates (the n/d components). G is trivial on n/d iff every G-orbit within F_d is a singleton. Any non-trivial action of G on n/d creates orbits of size ≥ 2 within F_d — each such orbit is an unresolved pair in π_d. Zero-fiber conflicts exist iff G is non-trivial on n/d.

**This is precisely the corrected condition** — and precisely what the prior condition (G → (Z/dZ)* injective) could not detect, since that condition only examines the action on the d-components.

---

## §5. Verification That Prior Specific Applications Still Hold

**Application 1: SPEC + half-modulus.** n = 2m (m odd squarefree), G = {1,−1}, d = m.

Corrected condition: G trivial on all primes of n/d = 2. Check: −1 mod 2 = 1 ✓. G = {1,−1} is trivial mod 2. Condition satisfied. {π_DYN({1,−1}), π_m} is sufficient. ✓

**Zero-fiber check.** F_m = multiples of m in Z/2mZ = {0, m}. T_{-1}(m) = −m mod 2m = 2m − m = m. The orbit {m} is a singleton. No conflict in F_m. ✓ Consistent with corrected theorem.

**Application 2: General DYN+CRT pairs.** For focused generators g on p₁ (g ≡ 1 mod pᵢ for i ≥ 2) and d = p₂···pₖ (all primes except p₁):

Corrected condition: g trivial on primes of n/d = {p₁}. But g mod p₁ ≠ 1 (g acts non-trivially on p₁). This is n/d = p₁.

Wait — this reverses: d = n/p₁ = p₂···pₖ, so n/d = p₁. G = ⟨g⟩ trivial on primes of n/d = {p₁}?

Actually: g is focused on p₁ means g ≡ 1 mod pⱼ for j ≥ 2. The condition is G trivial on primes of n/d. Here d = p₂···pₖ, n/d = p₁. G must be trivial on p₁ — but g is focused on p₁ (non-trivial on p₁). So corrected Theorem C says this pair is NOT sufficient, and indeed {π_DYN(g), π_{p₂···pₖ}} is not the standard construction.

The standard construction uses {π_DYN(g₁), π_DYN(g₂)} (M+M, Theorem A), not M+A pairs with this focusing. The SPEC+half-modulus (Application 1) is the canonical M+A sufficient pair, and it correctly satisfies the corrected condition.

---

## §6. Implications for the Arc

**What changes.** The corrected Theorem C (= Theorem B with maps swapped) is now proved. The prior Theorem C (G → (Z/dZ)* injective) is demoted from "sufficient condition" to "necessary but not sufficient condition."

**What does not change.** Theorem A (M+M), Theorem B (A+M), Theorem D (A+A / CRT) are unaffected. The SPEC+half-modulus sufficient pair remains valid (verified above). The UOP framework (WP58) provides the organizing principle.

**Structural meaning** [STRUCTURAL]: The prior condition tested "can G hide within the d-component?" The corrected condition tests "does G escape the d-component?" These are dual questions. The prior condition missed the escape into F_d via zero-coordinates. The corrected condition closes this gap.

---

## Summary

**[PROVED]** Corrected Theorem C: {π_DYN(G), π_d} is sufficient iff G acts trivially on all primes of (n/d). This is the M+A analog of Theorem B (A+M), with the same algebraic condition.

**[COMPUTED]** Counterexample: n=15, G=⟨2⟩, d=5. Prior condition (φ injective) is satisfied; pair is not sufficient. Orbit {5,10} is a conflict in U(π_5) ∩ U(π_DYN(⟨2⟩)).

**[PROVED]** Zero-fiber analysis: G acts on F_d = {x : x ≡ 0 mod d} by permuting n/d coordinates. Trivial action on n/d iff every orbit in F_d is a singleton iff no zero-fiber conflict.

**[PROVED]** Prior applications (SPEC+half-modulus) satisfy the corrected condition: G = {1,−1} is trivial mod 2 = n/d for n = 2m. The prior results stand.

**[OPEN]** Full classification of M+A sufficient pairs for non-unit-order G: the corrected condition is a complete characterization, but the structure of subgroups G satisfying it (for various d | n) depends on the prime factorization of G's order and n/d's prime structure.

---

## References

### Classical Number Theory and Algebra
- Gauss, C.F. (1801). *Disquisitiones Arithmeticae*. Leipzig. (CRT, cyclotomic polynomials)
- Euler, L. (1763). "Theoremata arithmetica nova methodo demonstrata." (Totient function)
- Hardy, G.H. & Wright, E.M. (2008). *An Introduction to the Theory of Numbers*, 6th ed. Oxford University Press.
- Ireland, K. & Rosen, M. (1990). *A Classical Introduction to Modern Number Theory*, 2nd ed. Springer GTM 84.
- Lang, S. (2002). *Algebra*, 3rd ed. Springer GTM 211.
- Dummit, D.S. & Foote, R.M. (2004). *Abstract Algebra*, 3rd ed. Wiley.
- Birkhoff, G. (1940). *Lattice Theory*. AMS Colloquium Publications 25.
- Ore, O. (1942). "Theory of equivalence relations." Duke Math. J. 9:573-627.

### Spectral / Analytic Number Theory
- Riemann, B. (1859). "Über die Anzahl der Primzahlen unter einer gegebenen Größe." Monatsber. Berlin. Akad.
- Montgomery, H.L. (1973). "The pair correlation of zeros of the zeta function." Proc. Sympos. Pure Math. 24:181-193.
- Shannon, C.E. (1949). "Communication in the presence of noise." Proc. IRE 37(1):10-21.
- Goldston, D.A., Pintz, J. & Yildirim, C.Y. (2009). Annals of Math. 170(2):819-862.
- Zhang, Y. (2013). "Bounded gaps between primes." Annals of Math. 179(3):1121-1174.
- Maynard, J. (2015). "Small gaps between primes." Annals of Math. 181(1):383-413.

### Paradoxes and Foundations
- Russell, B. (1903). *The Principles of Mathematics*. Cambridge University Press.
- Godel, K. (1931). "Uber formal unentscheidbare Satze der Principia Mathematica." Monatsh. Math. Phys. 38:173-198.
- Tarski, A. (1936). "Der Wahrheitsbegriff in den formalisierten Sprachen." Studia Philosophica 1:261-405.
- Banach, S. & Tarski, A. (1924). "Sur la decomposition des ensembles de points." Fundamenta Mathematicae 6:244-277.
- Quine, W.V. (1953). "On a so-called paradox." Mind 62:65-67.
- Zermelo, E. (1908). "Untersuchungen uber die Grundlagen der Mengenlehre." Math. Annalen 65:261-281.

### Bialynicki-Birula and Logarithmic Wave Equations
- Bialynicki-Birula, I. & Mycielski, J. (1976). "Nonlinear wave mechanics." Annals of Physics 100(1-2):62-93. DOI: 10.1016/0003-4916(76)90057-9.
- Cazenave, T. & Haraux, A. (1980). "Equations d'evolution avec non linearite logarithmique." Ann. Fac. Sci. Toulouse.
- Hoegh-Krohn, R. (1971). "A general class of quantum fields without cut-offs." Commun. Math. Phys. 38(3):195.

### Discrete-to-Continuum Transport (Wasserstein / Markov)
- Jordan, R., Kinderlehrer, D. & Otto, F. (1998). SIAM J. Math. Anal. 29(1):1-17.
- Maas, J. (2011). "Gradient flows of the entropy for finite Markov chains." J. Funct. Anal. 261(8):2250-2292.
- Gigli, N. & Maas, J. (2013). SIAM J. Math. Anal. 45(2):879-899.
- Chow, S.-N., Huang, W., Li, Y. & Zhou, H. (2012). Arch. Rat. Mech. Anal. 203(3):969-1008.

### TIG Framework (Novel — internal)
- Sanders, B.R. et al. (2026). TIG / CK / Crossing Lemma / sigma framework. 7Site LLC. DOI: 10.5281/zenodo.18852047.
- GitHub: github.com/TiredofSleep/ck (clay branch). See [GLOSSARY.md](../../../GLOSSARY.md) and [HISTORICAL_ARCHIVE_INDEX.md](../../../HISTORICAL_ARCHIVE_INDEX.md).

### Citation Discipline
Every term in this paper is either cited to published literature above, or explicitly flagged [NOVEL — extends X] with the prior framework identified. For full glossary, see [GLOSSARY.md](../../../GLOSSARY.md) at the repo root.

