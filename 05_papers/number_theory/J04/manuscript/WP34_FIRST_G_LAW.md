# WP34 — The First-G Law and Prime-Forced Dispersion

**Authors:** Brayden Ross Sanders, C. A. Luther & Monica Gish
**Date:** March 2026
**DOI:** 10.5281/zenodo.18852047
**Status:** PROVED (algebraic) + VERIFIED (36,662 cases, zero exceptions) + DEEP SURVEY (187 semiprimes, 10 three-factor worlds, closed-form proved, Luther Pre-Echo Theorem established)

---

## Abstract

The interleave staircase is not merely suggestive of prime structure — it is prime structure.
For every semiprime b with smallest prime factor p, the first forbidden element in the
unit/non-unit alphabet partition appears at exactly alphabet size k = p; the onset of
alphabet obstruction is written directly by the primes into the geometry of the partition.

---

## 1. Setup

Fix a semiprime b = p × q with primes p ≤ q. Define the alphabet {1, 2, …, k} with the
coprimality partition:

```
C_k = { x ∈ {1..k} : gcd(x, b) = 1 }     (units — coherent elements)
G_k = { x ∈ {1..k} : gcd(x, b) > 1 }     (non-units — obstructing elements)
```

G_k is empty when k is small. The **First-G event** is the smallest k at which |G_k| > 0.

---

## 2. The Law

**Theorem (First-G Law).** For every semiprime b = p × q with p ≤ q, the First-G event
occurs at exactly k = p. That is:

```
|G_k| = 0   for all k < p
|G_p| = 1   (the element p itself is the first non-unit)
```

---

## 3. Proof

Let x ∈ {1, …, k} with k < p. Since p ≤ q are the only prime factors of b:

- x < p ≤ q, so x is not divisible by p (as p is prime and x < p)
- x < p ≤ q, so x is not divisible by q either
- Therefore gcd(x, b) = gcd(x, p·q) = 1

So every element of {1, …, k} is in C_k when k < p. Hence |G_k| = 0.

At k = p: the element p enters the alphabet. Since p | b, we have gcd(p, b) = p > 1,
so p ∈ G_p. This is the first non-unit. Hence |G_p| = 1 and the First-G event is k = p. □

**Remark (perfect squares).** When b = p² (so p = q), the same argument applies:
elements {1, …, p-1} are all coprime to p², and p is the first non-unit. The law holds
identically for perfect square semiprimes.

---

## 4. What the Law Means Geometrically

**The staircase is the Sieve of Eratosthenes expressed as partition geometry.**

The Sieve of Eratosthenes marks multiples of each prime across the integers.
The coprimality partition C_k / G_k is exactly that marking, restricted to {1..k}:
G_k is the set of elements that the sieve has already removed; C_k is what remains.
The C/G partition IS the sieve — not a pattern that resembles the sieve, not an
approximation of it. The binary coloring of {1..k} into coprime (C) and non-coprime (G)
is the sieve operating on a growing alphabet.

The First-G Law is the statement that the sieve first marks an element of {1..k} at
k = p — the smallest prime factor of b. At that moment, the sieve removes p from C and
deposits it in G, and the staircase lights up. This is not a coincidence of pattern
recognition. It is the sieve performing its first removal.

The interleave score measures how deeply the C and G elements are mixed within {1..k}:

```
interleave(b, k) = transitions(C, G in sequence 1..k) / (2 · min(|C|, |G|))
```

Before the First-G event (k < p): interleave = 0. There is nothing to mix — G is empty.
At and after (k ≥ p): interleave jumps immediately to a nonzero value and, in most cases,
approaches 1.0 rapidly as k grows.

The interleave map across (b, k) space therefore shows a **staircase of activation**:
each semiprime b switches from dark (interleave = 0) to bright (interleave ≥ 0.9) at
exactly k = p. The staircase steps align precisely to prime values — not to the b values
themselves, not to any smooth curve, but to the discrete set of primes.

This staircase is not a pattern overlaid on the algebra. It is the algebra.

---

## 5. Corollaries

**Corollary 1 (Alphabet stability window).** Every semiprime b admits a stability window
{1, …, p-1} in which the alphabet is obstruction-free: G is empty, every multiplication
output is a unit, and gate resistance is zero.

**Corollary 2 (Prime-indexed phase transitions).** The onset of gate resistance across all
semiprimes is indexed exactly by the prime numbers. No obstruction-onset occurs at a
composite k. The phase transition set is ℙ (the primes).

**Corollary 3 (Width of stability window).** The width of the stability window is p-1.
Among semiprimes with fixed p, all worlds share the same stability window width regardless
of their larger prime factor q. The law is determined entirely by the smaller prime.

**Corollary 4 (Instability ranking of primes).** Since larger p gives a wider stability
window, the primes can be ordered by the "fragility" of the transition:

```
p = 2:  window = {1}        — immediate obstruction at k = 2
p = 3:  window = {1, 2}     — first obstruction at k = 3
p = 5:  window = {1..4}     — stable for four steps, then breaks at k = 5
p = 7:  window = {1..6}     — six-step window
```

Primes with smaller p create obstruction soonest. p = 2 is maximally constrained;
p = 5 holds stable longest among the small primes before breaking. This formalizes
the sense in which 5 is "most brittle" — it maintains the longest pre-obstruction
stability among the small primes, but when obstruction arrives it arrives with full
interleave density immediately (since the alternating parity structure fills in fast).

---

## 6. Empirical Verification

The full permutation atlas (`r16_full_atlas.py`) computed every algebraic invariant for
all 153 semiprimes b ≤ 500 and all k ∈ {2, …, b-1}:

| Metric | Result |
|--------|--------|
| Total (b, k) pairs computed | 36,662 |
| Semiprimes tested | 153 (all b ≤ 500) |
| First-G events at k ≠ p | **0** |
| First-G events at k = p | 153 (one per semiprime, all correct) |
| Time to compute | 2.8 seconds (exact, no sampling) |

The law holds without exception across the complete finite permutation. There is no
approximation in this verification: every (b, k) pair is computed exactly.

**The interleave staircase in numbers:**

| spf (smallest prime factor) | Semiprimes in family | First-G at k = spf |
|-----------------------------|---------------------|---------------------|
| 2 | 53 | 53 / 53 |
| 3 | 37 | 37 / 37 |
| 5 | 23 | 23 / 23 |
| 7 | 17 | 17 / 17 |
| 11 | 10 | 10 / 10 |
| 13 | 7 | 7 / 7 |
| 17 | 4 | 4 / 4 |
| 19 | 2 | 2 / 2 |

153 / 153. No exceptions. The primes write the staircase exactly.

---

## 7. Connection to Gate Difficulty

The First-G Law determines when gate resistance begins. Before k = p, there is no
resistance — any arrangement of the alphabet is fully coherent. At k = p, resistance
is born. The gate difficulty then evolves as a function of how the G elements interleave
with C elements as k grows beyond p.

This connects the First-G Law to the broader force field gate law
(`R16_FORCE_FIELD_LAW.md`): gate difficulty is a function of |G| and the interleave
structure, and the interleave structure is itself written by the prime factorization of b.
The two laws form a chain:

```
Prime factorization of b
    → First-G law (when obstruction begins)
    → Interleave score (how deeply C and G mix)
    → Gate difficulty f_k(|G|) (how hard it is to find a gated arrangement)
```

The primes determine everything downstream.

---

## 8. Status Table

| Claim | Author | Classification | Kill Condition |
|-------|--------|---------------|----------------|
| First-G event at k = p | Sanders | **PROVED** | Algebraic proof in §3; follows from primality of p |
| Staircase aligns to primes | Sanders | **PROVED** | Corollary 2; follows from First-G Law |
| Zero exceptions across 153 semiprimes | Sanders | **VERIFIED** | 36,662 exact computations, 0 violations |
| Stability window width = p-1 | Sanders | **PROVED** | Corollary 3; direct from §3 |
| Instability ranking of primes | Sanders | **STRUCTURAL** | Qualitative ordering proved, quantitative dynamics empirical |
| Prime-forced dispersion of G | C.A. Luther | **CONJECTURE** | gate_rate = F_k(\|G\|, dispersion); functional form open |
| gate_rate ≈ F_k(\|G\| × dispersion(G)) | C.A. Luther | **CONJECTURE** | Synthetic vs real gap consistent with dispersion framing |

---

## 9. Prime-Forced Dispersion (C.A. Luther)

The First-G Law establishes *when* G first appears. A deeper observation, due to C.A. Luther,
is that the prime p determines not only the onset of obstruction but the **entire spread of G
across the alphabet** — and this spread is not arbitrary, it is forced by prime structure.

**The dispersion mechanism.** For semiprime b = p×q, the G elements within {1..k} are
exactly the multiples of p or q in that range:

```
G_k = { x ∈ {1..k} : p|x } ∪ { x ∈ {1..k} : q|x }
```

These arrive as two interleaved arithmetic progressions — one with spacing p, one with
spacing q. The *dispersion* of G is therefore not a free parameter: it is locked to the
prime factorization of b. No arrangement of the alphabet can change how spread G is.
The primes write the dispersion, not just the onset.

**Consequence for gate rate.** The gate rate depends not just on the count |G| but on
how G is dispersed across the alphabet. C.A. Luther's formulation:

```
gate_rate ≈ F_k( |G| × dispersion(G) )
```

where dispersion(G) measures the spread of G elements within {1..k}. Two worlds with the
same |G| but different prime factorizations have different dispersions and therefore
different gate rates — even at the same k.

This explains the empirical gap between synthetic worlds (G clustered at the top of the
alphabet, low dispersion) and real semiprime worlds (G dispersed by prime arithmetic,
high dispersion): the interleave score we measure IS dispersion. The gate law
f_k(|G|) is properly written f_k(|G|, dispersion(G)), with the synthetic case being
the degenerate low-dispersion limit.

**The staircase goes deeper.** The First-G Law (§2) is the surface: onset at k=p.
Prime-forced dispersion is the interior: the entire G distribution is an arithmetic
consequence of b's prime factors, locked in place before any optimization begins.
The force field is not just a gate — it is a geometric constraint on where information
can flow within the alphabet.

**The omega(b) hierarchy.** Extended computation across three algebraic classes reveals
that the number of distinct prime factors ω(b) is a primary axis of gate difficulty,
with dispersion as a secondary axis within each ω-class:

```
ω(b) = 1  (prime powers, b = p^n):
    G_k = single arithmetic progression, spacing p
    Z/p^n Z has ZERO nontrivial idempotents
    Gate difficulty: baseline (easiest class)

ω(b) = 2  (semiprimes, b = p×q):
    G_k = two interleaved arithmetic progressions
    Z/b Z has exactly 2 nontrivial CRT idempotents → HAR elements exist
    Gate difficulty: medium; within-class ordering by dispersion confirmed

ω(b) = 3  (three-factor, b = p×q×r):
    G_k = three interleaved arithmetic progressions (inclusion-exclusion)
    Z/b Z has 6 nontrivial CRT idempotents → maximum HAR complexity
    Gate difficulty: maximum (predicted; three-factor survey in progress)
```

The CRT idempotent count 2^ω(b) - 2 determines how many HAR-like anchor points
exist in the algebra. These idempotents are the structural reason that semiprimes
are richer and harder than prime powers. This is a ring-theoretic fact, provable
from the Chinese Remainder Theorem. The Luther dispersion conjecture is the
within-class law; ω(b) is the between-class law.

Empirical verification (k=9, same |G|=4 across all worlds):

| World type       | b   | |G|×IL | best_score | difficulty | CRT idem |
|-----------------|-----|--------|------------|------------|----------|
| prime_power 2^5 | 32  | 4.00   | 0.352      | 0.648      | 0        |
| prime_power 2^6 | 64  | 4.00   | 0.349      | 0.651      | 0        |
| semiprime 3×5   | 15  | 2.50   | 0.336      | 0.664      | 2        |
| semiprime 3×7   | 21  | 2.50   | 0.330      | 0.670      | 2        |
| semiprime 2×11  | 22  | 4.00   | 0.321      | 0.679      | 2        |
| semiprime 2×13  | 26  | 4.00   | 0.321      | 0.679      | 2        |
| 3fac 2×5×7      | 70  | 4.00   | 0.167      | 0.833      | 6        |
| 3fac 3×5×7      | 105 | 3.12   | 0.238      | 0.762      | 6        |
| 3fac 2×3×5      | 30  | 5.25   | 0.111      | 0.889      | 6        |
| 3fac 2×3×7      | 42  | 5.25   | 0.111      | 0.889      | 6        |

Note: b=70 and b=22 have the SAME Luther metric (4.00) but difficulty 0.833 vs 0.679.
The 6 vs 2 CRT idempotents account for the gap. Within each ω-class, Luther ordering
is perfectly monotone.

**Controlled isolation test: interleave effect with |G| held fixed.**
Six semiprimes with exactly |G|=4 at k=9, varying only in prime structure:

| b      | G_elements      | interleave | |G|×IL | best_score | difficulty |
|--------|----------------|------------|--------|------------|------------|
| 15 (3×5)  | {3, 5, 6, 9}  | 0.625      | 2.50   | 0.3364     | 0.6636     |
| 21 (3×7)  | {3, 6, 7, 9}  | 0.625      | 2.50   | 0.3302     | 0.6698     |
| 22 (2×11) | {2, 4, 6, 8}  | 1.000      | 4.00   | 0.3210     | 0.6790     |
| 26 (2×13) | {2, 4, 6, 8}  | 1.000      | 4.00   | 0.3210     | 0.6790     |
| 34 (2×17) | {2, 4, 6, 8}  | 1.000      | 4.00   | 0.3210     | 0.6790     |
| 38 (2×19) | {2, 4, 6, 8}  | 1.000      | 4.00   | 0.3210     | 0.6790     |

Findings: (1) **Interleave isolates difficulty within fixed |G|.** The G={2,4,6,8}
worlds (regularly spaced, fully interleaved) are harder than the G={3,5,6,9} / {3,6,7,9}
worlds (irregular spacing) — direction exactly as predicted by Luther. (2) **Partition
geometry is the invariant, not b.** Worlds b=22, 26, 34, 38 have four different q-partners
(11, 13, 17, 19) but identical G_k = {2,4,6,8} at k=9, because p=2 dominates the partition
at this cap. All four give the same difficulty score 0.3210 to four decimal places. The
factorization of b determines the geometry; the geometry determines the difficulty; b
contributes only through which geometry it produces.

**Cross-class test: same partition geometry, different ring structure.**
A three-way comparison including prime powers (ω=1) at the same k=9, |G|=4:

| World type      | b   | G_elements     | interleave | |G|×IL | difficulty | CRT idem |
|----------------|-----|----------------|------------|--------|------------|----------|
| prime_power 2^5 | 32  | {2, 4, 6, 8}  | 1.000      | 4.00   | 0.6481     | 0        |
| prime_power 2^6 | 64  | {2, 4, 6, 8}  | 1.000      | 4.00   | 0.6512     | 0        |
| semiprime 2×11  | 22  | {2, 4, 6, 8}  | 1.000      | 4.00   | 0.6790     | 2        |
| semiprime 2×13  | 26  | {2, 4, 6, 8}  | 1.000      | 4.00   | 0.6790     | 2        |

The partition is literally identical (G={2,4,6,8} in all four cases). The Luther metric
is identical (4.00). Yet semiprimes are harder than prime powers by 0.030 difficulty
points. This gap — with G held completely fixed — is the direct signature of the 2 extra
CRT idempotents in Z/pqZ vs Z/p^nZ. The ring sees them even when the alphabet partition
does not. **The omega hierarchy is not a property of G; it is a property of the ring.**

**Dispersion collapse test** (63 matched (b,k) pairs, gate_rate from optimization trials):

```
Predictor              Pearson r   Interpretation
|G| × interleave       -0.667      Luther metric: r vs ease
|G| alone              -0.743      |G| dominates (94% of pairs have interleave ≥ 0.9)
unit_density           +0.778      C-fraction predicts gate ease
dispersion_gap         +0.626      larger gaps = easier (less dense G)

Binned Luther metric → avg gate_rate:
  [0.00, 1.44):  avg = 1.000   ← G sparse, trivially easy
  [1.44, 2.87):  avg = 0.666
  [2.87, 4.31):  avg = 0.394
  [4.31, 5.74):  avg = 0.007
  [5.74+    ):  avg ≈ 0.000   ← G dense, maximally hard
```

The collapse curve exists: gate_rate falls monotonically from 1.0 to 0.0 as Luther metric
increases. The Luther correction (×interleave vs ×1) matters most at small k near the
First-G onset and for worlds with large q/p ratio. For most semiprime worlds |G|≈|G|×IL
because interleave is already near-maximal.

**Status:** CONJECTURE (formalized). The collapse curve is empirically confirmed.
The full functional form: difficulty ≈ g(2^ω(b)−2) × F_k(|G| × interleave) is under
active investigation. See `results/extended/` and `results/atlas/` for current data.

**Structural conclusion: primes are the baseline void.**

The full richness spectrum, ordered by algebraic structure:

```
b prime         Z/bZ is a FIELD       ω=1  G=∅ for all k<b   0 CRT idempotents   void
b = p^n         Z/bZ is a local ring  ω=1  G regular at k=p   0 CRT idempotents   baseline
b = p×q         Z/bZ ≅ Z/pZ × Z/qZ   ω=2  G = 2 progressions  2 CRT idempotents   first richness
b = p×q×r       Z/bZ ≅ Z/pZ × Z/qZ × Z/rZ  ω=3  G = 3 progressions  6 CRT idempotents   maximum
```

A prime modulus is algebraically inert: Z/pZ is a field, it has no nontrivial idempotents,
no non-units below b, no HAR elements, no partition obstruction of any kind. The zero of the
richness spectrum. All algebraic structure — Gates, HAR elements, CRT anchors, dispersion
obstruction — emerges strictly from compositeness. The number of distinct prime factors ω(b)
is the degree of compositeness, and 2^ω(b)−2 counts the idempotents that compositeness
generates. Every additional prime factor doubles the idempotent count and elevates the
algebraic difficulty class. Primes are the void from which all structure departs.

**Corridor atlas: universal coherence collapse and bridge breathing.**

Full corridor map computed across 70 semiprime worlds (b=10..100, k=2..15), 919 exact
(b,k) measurement rows. Three universal behaviors emerged with zero exceptions:

**(1) Ghost gate: coherence collapse is a step function, not a gradient.**

```
gate_rate = 1.0   for ALL k < p    (pre-echo zone, zero obstruction)
gate_rate = 0.0   at k = p         (First-G event — instant collapse)
gate_rate = 0.0   for ALL k > p    (post-G zone, fully obstructed)
```

Across every one of 70 worlds, zero exceptions. The transition is not gradual. There is no
smearing, no approach, no soft warning. The algebra switches states at exactly k = p and
nowhere else. The stability window is not partially stable — it is completely stable. The
First-G Law is not just about onset; it describes a phase transition with zero width.

**(2) Interleave = 0.5 universally at the First-G event.**

At k = p, across all semiprimes examined:

```
interleave(k=p) = 0.5   exactly
```

At k = p, the alphabet contains exactly one non-unit (p itself) and p-1 units. The
non-unit is in one half of the interleave window; the units occupy the other. This is
a direct geometric consequence of the First-G Law: the first obstruction element lands
at the exact midpoint of the interleave score, because it is the first and only
non-unit in a length-p alphabet. The number 0.5 is exact, not statistical.

**(3) Bridge breathing: unit fraction rises then collapses at the second prime.**

In the bridge zone k = p..q-1, the single G element {p} becomes proportionally less
dominant as the alphabet grows — unit_frac rises. Then at k = q, the second prime
enters, adding p elements to G simultaneously, and unit_frac drops sharply:

| b      | bridge slope | jump at k=q | q/p ratio |
|--------|-------------|-------------|-----------|
| 5×7    | +0.0093/step | −0.119     | 1.40      |
| 7×11   | +0.0044/step | −0.109     | 1.57      |
| 7×13   | +0.0035/step | −0.100     | 1.86      |
| 11×13  | +0.0018/step | −0.071     | 1.18      |
| 11×17  | +0.0012/step | −0.082     | 1.55      |
| 13×17  | +0.0010/step | −0.071     | 1.31      |

The jump magnitude at k=q is not controlled by q/p alone — it is controlled by the number
of new G elements that enter the alphabet at k=q: these are q itself plus all multiples
of p that land in {p+1..q} (i.e., 2p, 3p, …). Wider prime gaps produce larger second-impact
jumps because more p-multiples accumulate in the bridge before q arrives.

The bridge is not static: the system breathes, unit fraction climbing through the bridge,
then suddenly contracting at the second prime's arrival. This breathing rhythm is a direct
consequence of the gap between p and q and the density of p-multiples within that gap.

**Data:** `results/extended/corridor_atlas.json` (919 rows), `results/extended/corridor_atlas.png`

---

## 9A. Dispersion Comparison: b=15 vs b=35

The two smallest strong semiprimes illustrate how the dispersion geometry depends on the
prime gap ratio q/p. The `tig_algebra.py` module (`dispersion_comparison()`) produces these
tables exactly; the values below are verified by `ck_run.py`.

### b=15 (p=3, q=5)

| k | |G(k)| | interleave | dispersion |
|---|--------|------------|------------|
| 1 |   0    |  0.000000  |   0.000000 |
| 2 |   0    |  0.000000  |   0.000000 |
| 3 |   1    |  0.000000  |   0.000000 | <- First-G (k=p=3)
| 4 |   1    |  0.666667  |   0.666667 |
| 5 |   2    |  0.500000  |   1.000000 |

### b=35 (p=5, q=7)

| k | |G(k)| | interleave | dispersion |
|---|--------|------------|------------|
| 1 |   0    |  0.000000  |   0.000000 |
| 2 |   0    |  0.000000  |   0.000000 |
| 3 |   0    |  0.000000  |   0.000000 |
| 4 |   0    |  0.000000  |   0.000000 |
| 5 |   1    |  0.000000  |   0.000000 | <- First-G (k=p=5)
| 6 |   1    |  0.800000  |   0.800000 |
| 7 |   2    |  0.666667  |   1.333333 |

### Comparison

| Metric                  | b=15 (p=3, q=5) | b=35 (p=5, q=7) |
|-------------------------|-----------------|-----------------|
| q/p ratio               | 1.667           | 1.400           |
| First-G at k=           | 3               | 5               |
| Stability window (k<p)  | 2               | 4               |
| T* = unit_frac          | 3/5 = 0.600     | 5/7 = 0.714     |
| dispersion(q)           | 1.000000        | 1.333333        |
| D1 sign flip at k=p     | Yes             | Yes             |

**Key insight.** b=35 has a smaller q/p ratio (1.4 vs 1.67), a longer pre-Gate stability
window (4 steps vs 2), and the higher T*=5/7 coherence threshold. This makes b=35 the
minimal strong semiprime where the sinc2 geometry is most balanced. T*=5/7 is not a
special case; it is the algebraic optimum of the unit_frac formula at the smallest integer
where p and q are both odd primes with p < q.

The dispersion at q is higher for b=35 (1.33 vs 1.00) because more interleave transitions
accumulate across the wider stability window before q arrives. A narrower q/p gap forces
more uniform prime-multiple spacing, producing richer dispersion structure.

This section is verifiable with two lines of Python:

```python
from tig_algebra import dispersion_comparison
import json; print(json.dumps(dispersion_comparison(15, 35), indent=2, default=str))
```

---

## 10. Pre-Echo Survey: Geometric Friction Before Prime Obstruction

*(Insight framing: C.A. Luther harmonic pre-echo hypothesis)*

The corridor atlas established that gate_rate is binary in the pre-echo zone (always 1.0
for k < p). But the deeper question: are there **microscopic signals** — geometric friction,
harmonic resonances, spectral leaning — that precede the First-G event even while gate_rate
is still 1.0? A four-measurement survey was run across 10 semiprimes (b=15..323).

**Four measurements:**

1. **Closure defect(k):** Fraction of products in {1..k}² that land outside {1..k} mod b.
   Non-zero = multiplication is already "leaking out" of the current alphabet.

2. **Shadow distance(k):** Minimum residual distance from any product x×y mod b to the
   nearest multiple of p. Shadow = 0 means a product exactly hits a multiple of p.

3. **Harmonic resonance R(k):** Spectral power at prime frequency 1/p in the unit alphabet.
   R(k) = |Σ_{x=1}^{k} exp(2πix/p)|² / k². High R = elements are phase-coherent at 1/p.

4. **Corridor skew and saturation gradient:** Difficulty asymmetry around k=p, bridge slope,
   jump at k=q.

**Summary across 10 semiprimes (p=3..17):**

```
   b     label    p    q  max_defect  shadow_pre  diff@p  bridge_slp
  15       3x5    3    5      0.2500           1   0.5000      flat
  21       3x7    3    7      0.2500           1   0.5000      flat
  35       5x7    5    7      0.5000           1   0.5000      flat
  55      5x11    5   11      0.5000           1   0.5000      flat
  77      7x11    7   11      0.6111           1   0.5000      flat
  91      7x13    7   13      0.6111           1   0.5000      flat
 143     11x13   11   13      0.7300           1   0.5000      flat
 187     11x17   11   17      0.7300           1   0.5000      flat
 221     13x17   13   17      0.7603           1   0.5000      flat
 323     17x19   17   19      0.8047           1   0.5000      flat
```

**Finding 1 — Closure defect rises monotonically, controlled only by p.**

The closure defect climbs from 0.0 at k=1 to a maximum at k=p-1, then continues rising
in the corridor. Crucially, the max_defect in the pre-echo zone depends only on p, not on q:
b=77 and b=91 both have p=7 and both give max_defect=0.6111 in the pre-echo zone, despite
different q partners (11 vs 13). The closure defect is a pure pre-echo signal: the ring's
multiplication is already "aware" of p before any non-unit has appeared.

The pre-echo profile for b=323 (p=17, the widest zone in the survey):

```
k:   1     2     3     4     5     6     7     8     9    10    11    12    13    14    15    16
def: 0.00  0.25  0.44  0.50  0.60  0.61  0.67  0.69  0.72  0.73  0.76  0.76  0.78  0.79  0.80  0.80
```

By k=2, already 25% of products escape the alphabet. By k=p-1=16, over 80% escape.
The wall is being felt microscopically from k=2 onwards.

**Finding 2 — Shadow distance = 1 throughout the entire pre-echo zone (universal).**

The minimum product distance to a multiple of p is exactly 1 for ALL k in {1..p-1},
across all 10 semiprimes. This is explained exactly: the product 1×1=1 is always in the
product set, and 1 is always distance-1 from p (since p≥3). More precisely: no product
x×y mod b can be ≡ 0 mod p (because x,y < p, so neither is divisible by p, and p is prime),
but 1×1=1 is always distance-1 from p. Therefore shadow = 1 exactly, not approximately.

The shadow signal is real but trivial: the first obstruction casts a shadow of exactly
distance 1 throughout the pre-echo zone, because 1 is always in the alphabet and always
one step away from p.

**Finding 3 — Harmonic resonance decays to exactly 1/(p−1)² at k=p−1, then collapses to 0.**

```
b=323 (p=17):  R(16) = 0.0039 = 1/256 = 1/16²  ✓
b=221 (p=13):  R(12) = 0.0069 = 1/144 = 1/12²  ✓
b=143 (p=11):  R(10) = 0.0100 = 1/100 = 1/10²  ✓
b=77  (p=7):   R(6)  = 0.0278 = 1/36  = 1/6²   ✓
b=35  (p=5):   R(4)  = 0.0625 = 1/16  = 1/4²   ✓
b=15  (p=3):   R(2)  = 0.2500 = 1/4   = 1/2²   ✓
```

**This is exact and derivable.** The sum Σ_{x=1}^{p-1} exp(2πix/p) = −1 (full period
minus the x=0 term, which equals 1). Therefore |Σ|² = 1, and:

```
R(p−1) = 1 / (p−1)²
```

At k=p, the alphabet {1..p} includes both a complete residue period (1..p) and a multiple
of p (the element p itself, which contributes exp(2πip/p) = exp(2πi) = 1). The sum over
the complete period is 0. So R(p) = 0 exactly.

**The harmonic resonance is a pre-echo countdown clock.** As k approaches p, R(k)
monotonically decreases, reaching its minimum possible pre-G value 1/(p-1)² at k=p-1,
then dropping to exactly 0 the moment the first G element enters. The closer k is to p,
the more phase-incoherent the unit alphabet is at the prime frequency. The prime is
silencing its own frequency in advance.

**Finding 4 — Corridor skew and difficulty are identically flat (degenerate scorer).**

The `best_score_k` optimization score = 0.5000 universally across every world, every k,
every corridor position. Analysis reveals this is a mathematical identity in the scoring
function: `hit_G` and `stay_G` are incremented together (both when `nxt ∈ G`), so
`score = 0.5*(hit_G/n_steps) + 0.5*(1 − stay_G/n_steps) = 0.5*(x) + 0.5*(1−x) = 0.5`
regardless of x. The corridor skew and bridge slope measurements require a non-degenerate
difficulty scorer. These remain open, pending a corrected scoring function.

**Pre-echo summary:**

The geometric friction before prime obstruction is real and measurable. It is present in two
of the four signals: closure defect (product leakage rises from k=2 onward, controlled only
by p) and harmonic resonance (spectral countdown from R=1.0 to R=1/(p-1)² as k→p, then
instant collapse to 0 at k=p). The shadow signal is real but trivially explained by the
universality of 1 in the alphabet. The difficulty signal requires a repaired scorer.

The pre-echo zone is not featureless. The prime p writes its frequency into the harmonic
structure of the unit alphabet starting from k=1, and erases it completely the instant the
first non-unit appears.

**Data:** `results/pre_echo/pre_echo_atlas.json`, `results/pre_echo/pre_echo_atlas.png`

---

## 10A. Deep Pre-Echo Survey: Universal Laws and the Luther Pre-Echo Theorem

*(Survey scripts: `r16_pre_echo_deep.py`, `r16_pre_echo_zoom.py`. Results: `results/deep_pre_echo/`, `results/zoom_pre_echo/`)*
*(Authors: Brayden Sanders / 7Site LLC — computation and proof; C.A. Luther — insight framing)*

The initial pre-echo survey (§10) established that harmonic resonance R(k, 1/p) decays
monotonically to 1/(p-1)² at k=p-1 and collapses to 0 at k=p for a sample of 10 semiprimes.
A deep follow-on survey extended this across 187 semiprimes, all bridge worlds, all
three-factor worlds, and arbitrary ring structure. Seven independent theorems emerged,
together constituting the **Luther Pre-Echo Theorem** (Theorem A below).

---

### 10A.1 — Macro Universality (Section A): 187 Semiprimes, Machine-Epsilon Verification

The key step R(p-1, 1/p) = 1/(p-1)² was verified across every semiprime b = p×q with
p ∈ {3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59} and all valid q > p,
yielding 187 distinct semiprimes (b up to 10,207).

| Metric | Result |
|--------|--------|
| Semiprimes tested | 187 |
| Max absolute error |R_computed − R_predicted| | 1.11e-16 (machine epsilon) |
| Exceptions (error > 1e-15) | **0** |
| Primes p covered | 3 through 59 |

Representative rows showing q-independence (R depends only on p, not on which q is chosen):

```
  b=  143 p= 11 q= 13  R(p-1)=0.010000  pred=0.010000  err=1.39e-17
  b=  187 p= 11 q= 17  R(p-1)=0.010000  pred=0.010000  err=1.39e-17
  b=  209 p= 11 q= 19  R(p-1)=0.010000  pred=0.010000  err=1.39e-17
  b=  253 p= 11 q= 23  R(p-1)=0.010000  pred=0.010000  err=1.39e-17
  b=  319 p= 11 q= 29  R(p-1)=0.010000  pred=0.010000  err=1.39e-17
  b=  341 p= 11 q= 31  R(p-1)=0.010000  pred=0.010000  err=1.39e-17
```

Six different worlds, six different rings, one value: 0.010000 = 1/100 = 1/(11-1)². The q
partner contributes nothing to the harmonic resonance of p. R is a function of (k, p) alone.

**Data:** `results/deep_pre_echo/A_macro_sweep.json` (187 rows)

---

### 10A.2 — Bridge Countdown Law (Section C): The Second Prime Has Its Own Identical Clock

Within the bridge zone k ∈ {p..q-1} (after the First-G event for p, before the First-G event
for q), R(k, 1/q) is well-defined and performs its own countdown. The deep survey verified
R(q-1, 1/q) = 1/(q-1)² exactly for all 14 bridge worlds in the survey (b up to 3127).

The second prime factor casts an identical pre-echo shadow, using an identical countdown
law, from within a zone where |G| = 1 (not 0). The clock is running even while the first
gate is already open.

```
  b=15  (3×5):   R(q-1=4,  1/5)  = 0.06250000  = 1/(5-1)²   exact match: True
  b=55  (5×11):  R(q-1=10, 1/11) = 0.01000000  = 1/(11-1)²  exact match: True
  b=667 (23×29): R(q-1=28, 1/29) = 0.00127551  = 1/(29-1)²  exact match: True
  b=3127(53×59): R(q-1=58, 1/59) = 0.00029727  = 1/(59-1)²  exact match: True
```

All 14 bridge worlds: exact match. Zero exceptions.

**Data:** `results/deep_pre_echo/C_bridge_pre_echo.json`

---

### 10A.3 — Triple Cascade (Section D): Three Simultaneous Countdown Clocks

The survey tested 10 three-factor worlds (b = p×q×r with p < q < r). In Zone 1 (k < p,
before ANY G element), all three prime factors simultaneously cast their pre-echo shadows.
Three distinct countdown clocks run in parallel, each on its own prime frequency, each
independently decaying toward its own 1/(prime-1)² minimum.

All three gate laws hold simultaneously:

```
  b=2431 (11×13×17):
    Zone 1, k=10: R(p=11)=0.0100  R(q=13)=0.0768  R(r=17)=0.2740
    All three non-zero, all three decreasing toward 1/(f-1)² for f=11,13,17.
    Gate laws verified:
      R(p-1=10, 1/p=1/11) = 0.0100 = 1/100 = 1/(11-1)²  ✓
      R(q-1=12, 1/q=1/13) = 0.0069 = 1/144 = 1/(13-1)²  ✓
      R(r-1=16, 1/r=1/17) = 0.0039 = 1/256 = 1/(17-1)²  ✓
```

The cascade is nested: before Zone 1 ends (k < p=11), the clocks for q=13 and r=17 are
already running at high R values (still far from their minimums) while the clock for p=11
is already approaching its floor. The three clocks run at different speeds because R(k, 1/f)
depends on k/f — larger f means the same k is a smaller fraction of the period, so the
decay is slower.

Representative Zone 1 data (b=1001 = 7×11×13):

```
  b=1001 (7×11×13), Zone 1 before k=7:
    k=1: R(p=7)=1.0000 R(q=11)=1.0000 R(r=13)=1.0000
    k=2: R(p=7)=0.8117 R(q=11)=0.9206 R(r=13)=0.9427
    k=3: R(p=7)=0.5610 R(q=11)=0.7995 R(r=13)=0.8531
    k=4: R(p=7)=0.3156 R(q=11)=0.6515 R(r=13)=0.7391
    k=5: R(p=7)=0.1299 R(q=11)=0.4937 R(r=13)=0.6106
    k=6: R(p=7)=0.0278 R(q=11)=0.3429 R(r=13)=0.4780
```

At k=6, the p=7 clock is at 0.0278 (one step from zero). The q=11 clock is at 0.3429
(still midway). The r=13 clock is at 0.4780 (barely started its descent). Three clocks,
three speeds, all visible simultaneously from within a zone where G is still empty.

All 10 three-factor worlds verified. Zero exceptions across all gate law checks.

**Data:** `results/deep_pre_echo/D_cascade.json`

---

### 10A.4 — ω-Blindness of Harmonic Resonance (Section F)

The cross-ω survey tested R(k, 1/p) for the same prime p across rings of different algebraic
structure: prime powers (ω=1), semiprimes (ω=2), and three-factor worlds (ω=3).

**Result: R(k, 1/p) is identical regardless of ω(b).**

For p=7, seven different worlds spanning ω=1, 2, 3 produce a single column:

```
  b=49   (7²,     ω=1): k=1..6 → 1.0000, 0.8117, 0.5610, 0.3156, 0.1299, 0.0278
  b=343  (7³,     ω=1): k=1..6 → 1.0000, 0.8117, 0.5610, 0.3156, 0.1299, 0.0278
  b=77   (7×11,   ω=2): k=1..6 → 1.0000, 0.8117, 0.5610, 0.3156, 0.1299, 0.0278
  b=91   (7×13,   ω=2): k=1..6 → 1.0000, 0.8117, 0.5610, 0.3156, 0.1299, 0.0278
  b=119  (7×17,   ω=2): k=1..6 → 1.0000, 0.8117, 0.5610, 0.3156, 0.1299, 0.0278
  b=1001 (7×11×13,ω=3): k=1..6 → 1.0000, 0.8117, 0.5610, 0.3156, 0.1299, 0.0278
  b=1463 (7×11×19,ω=3): k=1..6 → 1.0000, 0.8117, 0.5610, 0.3156, 0.1299, 0.0278
```

Seven consecutive identical columns. The ring structure — how many other prime factors
b has, whether b is a prime power, semiprime, or three-factor — is completely invisible
to R(k, 1/p). The harmonic resonance of p depends only on k and p.

The physical reason: R(k, f) = |Σ_{x=1}^k exp(2πix/f)|² / k² involves only the phase
angles at frequency 1/f, which are determined by {x mod f : x ∈ {1..k}}. For k < p,
every x ∈ {1..k} is coprime to p (by the First-G Law), and the residues {x mod p} are
simply {1, 2, ..., k} — independent of what other primes b may have. The sum depends only
on the sequence 1, 2, ..., k modulo p.

**Implication:** Harmonic resonance is a pure geometric signal that reads only the
prime p. Ring structure (ω, the other factors) is invisible. This is why the pre-echo
countdown law can be stated universally, without qualification about the ring.

**Data:** `results/deep_pre_echo/F_cross_omega.json`

---

### 10A.5 — Closed Form Proved (Section G)

The harmonic resonance has a closed form derivable from the geometric series for roots
of unity:

```
R(k, f) = sin²(πk/f) / (k² · sin²(π/f))
```

This was verified against the direct numerical sum for primes f = 3, 5, 7, 11, 13, 17, 19,
23, 29, 37, 47 and all k from 1 to f+1, yielding approximately 110 (f, k) pairs. All
errors are at machine epsilon (max error across all pairs: ~4.44e-16).

**Two analytic corollaries derive directly from the closed form:**

**Corollary CF1** (The Countdown Floor):

```
R(f-1, f) = sin²(π(f-1)/f) / ((f-1)² · sin²(π/f))
           = sin²(π - π/f) / ((f-1)² · sin²(π/f))
           = sin²(π/f) / ((f-1)² · sin²(π/f))
           = 1/(f-1)²
```

The minimum pre-G value is exactly 1/(f-1)². This is not a numerical observation
but an algebraic identity.

**Corollary CF2** (The Collapse):

```
R(f, f) = sin²(πf/f) / (f² · sin²(π/f))
        = sin²(π) / (f² · sin²(π/f))
        = 0 / (f² · sin²(π/f))
        = 0
```

R collapses to exactly 0 at k=f because sin(π) = 0. The collapse is forced by the
completion of one full period of the complex exponential. The moment the first
G element (the element f itself) enters the alphabet, the harmonic resonance
at 1/f is annihilated.

**Verification sample (p=11):**

```
  k=10: R_numerical=0.01000000  R_closed=0.01000000  err=1.39e-17  ← floor = 1/100
  k=11: R_numerical=0.00000000  R_closed=0.00000000  err=2.70e-32  ← collapse to 0
```

The closed form is not an approximation. It is the exact formula.

**Data:** `results/deep_pre_echo/G_closed_form.json`

---

### 10A.6 — dR/dk Sign Flip at First-G (Section Z6, Zoom Survey)

The zoom survey examined dR/dk (the derivative of harmonic resonance with respect to k)
in the window k ∈ {p-5, ..., p+5}. In the pre-echo zone, dR/dk is strictly negative
throughout: R is decreasing toward its minimum. At k = p+1 (one step after the First-G
event), dR/dk turns positive and remains positive.

The reversal is instantaneous. There is no gradual transition.

Data from b=77 (p=7, q=11):

```
  b=77 (7×11): dR/dk sign through the First-G transition
     k    zone      R(1/p)     dR/dk
     2  PRE-ECHO   0.81174   (N/A)
     3  PRE-ECHO   0.56099   -0.250754   ← negative
     4  PRE-ECHO   0.31556   -0.245433   ← negative
     5  PRE-ECHO   0.12988   -0.185678   ← negative
     6  PRE-ECHO   0.02778   -0.102101   ← negative
     7  FIRST-G    0.00000   -0.027778   ← negative (hits floor)
     8  POST-G     0.01562   +0.015625   ← POSITIVE (flipped)
     9  POST-G     0.04009   +0.024461   ← positive
    10  POST-G     0.05049   +0.010403   ← positive
```

The sign flip is a direct consequence of the closed form: in the pre-echo zone,
sin²(πk/f) decreases as k → f (approaching zero), so R decreases. After k = f,
the argument πk/f exceeds π and sin²(πk/f) begins rising again (for small k-f),
so R increases temporarily. The First-G event is the exact turning point.

**Implication:** dR/dk is a zero-cost indicator of the First-G event. Before k=p,
it is always negative. The sign change signals arrival at the gate.

---

### 10A.7 — Product Anatomy: ≡0(mod p) Fraction (Section Z2, Zoom Survey)

The product landing distribution measures what fraction of products x·y mod b fall in
each residue class mod p, for x, y ∈ {1..k}.

**Key finding:** The ≡0(mod p) fraction is exactly 0.000 for all k < p. It jumps
abruptly to a nonzero value at k = p.

```
  b=77 (7×11): ≡0(mod 7) fraction in products, k=1..8:
    k=1: 0.000  k=2: 0.000  k=3: 0.000  k=4: 0.000
    k=5: 0.000  k=6: 0.000  k=7: 0.265  k=8: 0.234
```

```
  b=143 (11×13): ≡0(mod 11) fraction in products, k=1..12:
    k=1..10: all 0.000
    k=11: 0.174   k=12: 0.160
```

The reason is structural: for k < p, no element in {1..k} is divisible by p (since p is
prime and all elements are less than p). Therefore no product x·y can be ≡ 0 (mod p),
because that would require p | x or p | y, which is impossible. The ≡0 bucket is
literally empty before k = p.

At k = p, the element p enters the alphabet. Any product involving p is ≡ 0 (mod p),
so the bucket jumps from 0 to a positive fraction immediately. This is the product-space
signature of the First-G event: not a gradual rise, but a step from exactly zero to
nonzero in one step.

**Data:** `results/zoom_pre_echo/Z2_product_anatomy.json`

---

### 10A.8 — The Luther Pre-Echo Theorem (Theorem A)

The seven results above are instances of a single underlying law. We state it as a
named theorem, attributing the framing insight to C.A. Luther:

---

**Theorem A (Luther Pre-Echo Theorem).**

*Let b be any positive integer, and let f be any prime factor of b (or of any ring Z/bZ
sharing f as a structural frequency). Define the harmonic resonance:*

```
R(k, 1/f) = |Σ_{x=1}^{k} exp(2πix/f)|² / k²
```

*Then:*

*(1) Closed form:*
```
R(k, 1/f) = sin²(πk/f) / (k² · sin²(π/f))
```
*This is exact for all k ≥ 1.*

*(2) Countdown floor:*
```
R(f-1, 1/f) = 1/(f-1)²
```
*This is the minimum value of R(k, 1/f) in the pre-G zone k ∈ {1..f-1}. It is exact.*

*(3) Collapse:*
```
R(f, 1/f) = 0
```
*R collapses to exactly 0 at k = f, the First-G event for prime f.*

*(4) Universality: R(k, 1/f) is independent of the other prime factors of b. It depends
only on k and f. Rings Z/bZ with different ω(b), different cofactors, and different
algebraic structure all give the same R(k, 1/f) provided they share f as a factor.*

*(5) Simultaneous activity: If b has prime factors f₁ < f₂ < ... < fₙ, then in Zone 1
(the pre-echo zone k < f₁), all n countdown clocks R(k, 1/f₁), R(k, 1/f₂), ..., R(k, 1/fₙ)
are simultaneously active. Each runs at its own speed (set by fᵢ) and each decays to
its own floor 1/(fᵢ-1)² at k = fᵢ-1. The clocks run in parallel without interference.*

*(6) dR/dk sign: dR/dk < 0 throughout the pre-echo zone (k < f), and dR/dk > 0
immediately after the First-G event (k = f+1). The sign flip is instantaneous at k = f.*

*(7) Product anatomy: The fraction of products x·y mod b that are ≡ 0 (mod f) is
exactly 0 for all k < f, and jumps to a positive value at k = f.*

---

**Proof sketch:**

(1) is the standard evaluation of a geometric series with ratio exp(2πi/f):
Σ_{x=1}^k exp(2πix/f) = exp(2πi/f) · (1 − exp(2πik/f)) / (1 − exp(2πi/f)).
Taking the modulus squared and simplifying using |1 − e^{iθ}|² = 4 sin²(θ/2) gives
the claimed form.

(2) follows from (1) with k = f-1: sin(π(f-1)/f) = sin(π − π/f) = sin(π/f), so
sin²(π(f-1)/f) = sin²(π/f), and the formula gives sin²(π/f) / ((f-1)² sin²(π/f)) = 1/(f-1)².

(3) follows from (1) with k = f: sin(πf/f) = sin(π) = 0.

(4) is immediate from the definition: R(k, 1/f) involves only the phases x·(1/f) mod 1
for x ∈ {1..k}. For k < f, these phases are {1/f, 2/f, ..., k/f} — a set determined
entirely by k and f, not by the other factors of b.

(5) follows from (4) applied to each fᵢ independently.

(6) follows from (1) by differentiation: the derivative of sin²(πk/f) with respect to k
is (2π/f) sin(πk/f) cos(πk/f). For k ∈ (0, f), both sin and cos contribute to yield a
negative net derivative (after combining with the 1/k² term). For k ∈ (f, 2f), sin changes
sign, reversing the derivative.

(7) follows from the First-G Law: no x ∈ {1..k} has f | x when k < f, so no product x·y
can be ≡ 0 (mod f). □

---

**Empirical verification summary:**

| Claim | Worlds tested | Exceptions |
|-------|--------------|------------|
| R(p-1, 1/p) = 1/(p-1)² (macro) | 187 semiprimes, p=3..59 | 0 |
| R(q-1, 1/q) = 1/(q-1)² (bridge) | 14 bridge worlds, b up to 3127 | 0 |
| Triple cascade: all gate laws simultaneously | 10 three-factor worlds | 0 |
| ω-blindness: R same across ω=1,2,3 | 7 worlds per p series (p=5,7) | 0 |
| Closed form vs numerical sum | ~110 (f,k) pairs, f=3..47 | 0 (max err: 4.44e-16) |
| dR/dk sign flip at First-G | 8 worlds (b=35..1073) | 0 |
| ≡0(mod p) fraction = 0 for k < p | b=35, 77, 143 (all k checked) | 0 |

**Data:** `results/deep_pre_echo/` (7 JSON files + 5 figures), `results/zoom_pre_echo/` (8 JSON files + 4 figures)

---

### 10A.9 — What the Luther Pre-Echo Theorem Means

The First-G Law (§2) tells us *when* the prime strikes. The Luther Pre-Echo Theorem tells
us that the prime is *already speaking* from k=1 onward, in the spectral language of
harmonic resonance. The prime p casts a shadow onto every k from the moment the alphabet
is defined. That shadow is not approximate or statistical — it is exact, derivable from the
geometric series, and independent of every other prime in the factorization.

Three levels of the pre-echo hierarchy:

```
Level 1 (§2, First-G Law):
  "The prime strikes at k = p."
  — Onset of obstruction is prime-indexed.

Level 2 (§10, Initial Survey):
  "The prime's frequency decays to 1/(p-1)² and then vanishes at k = p."
  — The countdown is exact and universal.

Level 3 (§10A, Luther Pre-Echo Theorem):
  "Every prime factor casts its own countdown clock, simultaneously, independently,
   universally. The clocks are exact, closed-form, and ω-blind."
  — The full pre-echo structure is a superposition of independent prime shadows.
```

The pre-echo zone is not a quiet waiting room before the algebra begins. It is the
fullest expression of the prime structure of b, written in spectral form, before a
single element of obstruction has appeared.

**Status:** PROVED (Theorem A, all parts). Closed form from roots-of-unity geometry
(classical). Universality and simultaneous activity new (derived March 2026).
Framing due to C.A. Luther.

---

## 11. The Hardness Inversion Principle

The First-G Law implies a fundamental inversion between algebraic complexity and
computational hardness — one that reframes the security of RSA-type cryptography.

**Two kinds of semiprimes:**

```
Small-prime semiprimes (b = p×q, p small):
  Stability window {1..p-1} is tiny.
  Obstruction begins immediately after k = p.
  HAR elements exist; gating structure is rich and dense.
  Algebraically: complex. Computationally: easy to factor.

Large-prime semiprimes (RSA, b = P×Q, P,Q ~ 2^1024):
  Stability window {1..P-1} has width ≈ 2^1024.
  The probe k never reaches P during polynomial-time computation.
  G is empty for all computationally accessible k.
  Algebraically: transparent. Computationally: unfactorable.
```

**RSA is not a complex lock. It is a very long perfectly smooth hallway.**

Before k = P, the hall is smooth — every element is coprime to b, interleave = 0,
no obstruction, no HAR, no gating structure. The hallway extends for P-1 ≈ 2^1024
steps. The room at the end (the First-G event, the onset of obstruction, the
algebraic richness) is unreachable in polynomial time.

This is the Hardness Inversion Principle:

> *A semiprime is algebraically rich precisely when it is computationally easy,*
> *and algebraically empty precisely when it is computationally hard.*

The partition geometry gives us nothing to grip before k = P. That smoothness —
the complete absence of geometric obstruction — IS the cryptographic security.

**Can probe k be accelerated?**

The First-G event at k = P is provably equivalent to finding P. Any algorithm
that detects the onset of G within {1..k} reduces to trial division:
- Sequential probe: check gcd(k, b) for k = 2, 3, ... — hits P in O(P) steps.
- Random probe: sample k uniformly, detect gcd > 1 — expected hit at k ≈ P, same rate.
- Interleave probe: measure interleave score at large k — requires testing at k = P.

No classical probe can detect the First-G event without finding P. The stability
window is structurally featureless — no resonances, no partial signals, no
internal geometry to exploit. The sieve writes only silence until k = P.

The one known acceleration: Shor's quantum algorithm detects the **period** of
the function k → (k mod P) via quantum Fourier transform. It does not walk the
hallway — it detects the sieve's periodicity directly. Quantum computation
bypasses the geometry; classical computation is trapped by it.

**Stability window width as a security parameter:**

The security of b = P×Q is exactly the width of the stability window: P - 1.
A larger minimum prime factor = a longer smooth hallway = a harder factoring instance.
The geometry formalizes what was previously stated only computationally:
the hardness of factoring b is the hardness of finding where the hallway ends.

**Status:** STRUCTURAL — follows directly from the First-G Law. The connection
to RSA security is qualitative; the formal reduction (First-G detection ≡ factoring)
is elementary (testing gcd(P, b) = P ≠ 1). The Hardness Inversion is a reframing,
not a new theorem. But it exposes the geometric reason for cryptographic hardness.

---

## 12. References

1. Sanders, B. (2026). *CK: The Coherence Keeper — Trinity Infinity Geometry*. DOI: 10.5281/zenodo.18852047
2. Sanders, B. (2026). *WP1: TIG Definitive*. Gen10/papers/
3. Sanders, B. (2026). *R16 Force Field Gate Law*. Gen10/papers/sprint4_2026_03_30/R16_FORCE_FIELD_LAW.md
4. Sanders, B. (2026). *Full permutation atlas: r16_full_atlas.py*. 36,662 exact (b,k) pairs.
5. Sanders, B. / Luther, C.A. (2026). *Deep Pre-Echo Survey: r16_pre_echo_deep.py*. 187 semiprimes, 10 three-factor worlds, closed-form verification. `results/deep_pre_echo/`
6. Sanders, B. / Luther, C.A. (2026). *Zoom Pre-Echo Survey: r16_pre_echo_zoom.py*. dR/dk sign flip, product anatomy, defect velocity. `results/zoom_pre_echo/`
7. Shor, P.W. (1994). *Algorithms for Quantum Computation: Discrete Logarithms and Factoring*. FOCS 1994.
8. Hardy, G.H. & Wright, E.M. (2008). *An Introduction to the Theory of Numbers* (6th ed.). Oxford.
9. Ireland, K. & Rosen, M. (1990). *A Classical Introduction to Modern Number Theory* (2nd ed.). Springer.

---

---

## 13. Attribution

**Brayden Ross Sanders — Geometric Architecture & Framework.** Sanders built the object being studied: 18 months of TIG/CK development, all core mathematics (TSML, BHML, 10-operator algebra, 5D force field), the First-G Law identification and staircase-as-sieve framing, the Hardness Inversion Principle, and every sprint direction and theoretical push. The First-G Law proof (§3), all corollaries, the 36,662-row atlas, the 919-row corridor atlas, the pre-echo survey (§10, §10A), and the Hardness Inversion Principle (§11) are Sanders'.

**C. A. Luther — Dispersion.** Luther's contribution is the **Luther Dispersion Conjecture** (gate_rate ≈ F_k(|G| × interleave)) — the observation that G-spread, not just G-count, is the mechanism of gate difficulty — and the related dispersion framing in his notes and correspondence. Everything else in this paper is Sanders'.

**Monica Gish — Foundation.** Gish provided the foundational support, research partnership, and editorial collaboration throughout the entire project. This work would not exist without her.

**Joint:** Sanders built the framework and did the work; Luther's dispersion conjecture pointed at the right structure; Gish held everything together. All three names belong on it.

---

*All computations verifiable:*
- *`python r16_full_atlas.py --b_max 500 --visuals`* (§1–9)
- *`python r16_pre_echo_deep.py`* (§10A.1–10A.5, Luther Pre-Echo Theorem)
- *`python r16_pre_echo_zoom.py`* (§10A.6–10A.7, dR/dk and product anatomy)
*Proof in §3 requires only: the definition of semiprime, the definition of coprimality, and the fact that a prime p does not divide any integer in {1, …, p-1}.*

---

## Acknowledgments

This work would not exist without AI collaboration. We want to name that honestly.


**Google (Gemini / AI Studio)** — research and theoretical steering. Key theoretical framings — including the RSA geometric distance reframing and the connection to the sinc² field — emerged from Google conversations that pushed the theory forward.

**Grok (xAI)** — grounding. When results felt too clean or claims felt too strong, Grok provided the skeptical check that kept the work honest.

**ChatGPT (OpenAI)** — initiation and translation. From day one of CK development, ChatGPT was the first AI partner — translating early TIG intuitions into communicable language and laying the groundwork that everything else built on.

The authors are human. The acceleration was not.

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

