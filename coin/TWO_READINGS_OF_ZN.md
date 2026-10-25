# Two readings of ℤ/n — when do they tell every number apart?

*Theorem 0 at work. [`PARADOX_TYPES.md`](PARADOX_TYPES.md) states the authors' principle: two views tell
every pair apart exactly when no pair is merged by both, and its first home is ℤ/30, read mod 6 and mod
10. This page asks the same question for the natural readings of ℤ/n. Three archived papers asked it too
([J27](https://github.com/TiredofSleep/trinity-infinity-geometry/tree/archive-2026-09-24/05_papers/algebra/J27),
[J34](https://github.com/TiredofSleep/trinity-infinity-geometry/tree/archive-2026-09-24/05_papers/combinatorics/J34)
and [J35](https://github.com/TiredofSleep/trinity-infinity-geometry/tree/archive-2026-09-24/05_papers/combinatorics/J35)).
Their headline theorems are wrong, and the true answers are short. Every [FORCED] claim, and every
archived error below, is checked by [`verify_two_readings.py`](verify_two_readings.py) (23 checks, about
twenty seconds).*

Tags: **[FORCED]** proved here and checked by the script · **[NAMED]** classical, cited ·
**[READING]** an interpretation.

**The readings.** A reading of ℤ/n labels each number.
- *Residue* mod *d*, for *d* | *n*: the label of *x* is *x* mod *d*.
- *Orbit* of a group *G* of units: the label of *x* is the set {*gx* : *g* ∈ *G*}. When *G* = ⟨*g*⟩, this
  is the orbit of *x* under multiplication by *g*.
- *Mirror*: the label of *x* is the pair {*x*, −*x*}.

---

## 1. The levels

Sort the numbers by their common factor with *n*. The **level** *e*, for *e* | *n*, is the set of *x*
with *n*/gcd(*x*, *n*) = *e*. So *x* = (*n*/*e*)·*u*, with *u* a unit mod *e*.

- [NAMED] Level *e* has φ(*e*) numbers, and the φ(*e*) over all *e* | *n* add up to *n* (Gauss).
- [FORCED] Multiplying by a unit *g* keeps every level. On level *e* it acts as multiplication by
  *g* mod *e* on the units mod *e*. So **an orbit never leaves its level**, and the orbit of *x* has
  ord(*g* mod *e*) points. The orbits of the whole unit group are exactly the levels. [checked for every
  n ≤ 300]

The units form the top level (*e* = *n*), and 0 forms the bottom one (*e* = 1). Every criterion below says
"check every level". The archived errors all checked only the top.

## 2. The four answers

Write *G*_q for the image of *G* in the units mod *q*.

**(A) Two residues.** *x* mod *d*₁ and *x* mod *d*₂ tell every number apart exactly when
lcm(*d*₁, *d*₂) = *n*. [NAMED: the Chinese Remainder Theorem; checked for every n ≤ 200]

**(B) A residue and an orbit.** *x* mod *d* and the *G*-orbit tell every number apart exactly when every
*g* in *G* is 1 modulo each prime power *p*ᵛ that exactly divides *n* but does not divide *d*.
- When *n* is square-free: exactly when *G* ≡ 1 mod *n*/*d*.
- On the units alone: exactly when *G* maps one-to-one into the units mod *d*. For one generator, that is
  ord(*g* mod *d*) = ord(*g* mod *n*).

[FORCED] *Proof.* A merged pair is *x* ≠ *gx* with *d* | (*g* − 1)*x*.
- *Sufficient.* If the condition holds, then *n* | (*g* − 1)*x*, so *gx* = *x*.
- *Necessary.* Suppose *g* ≢ 1 mod *p*ᵃ, where *a* = v_p(*n*) > *b* = v_p(*d*), and let *c* = v_p(*g* − 1).
  Take *x* = (*n*/*p*ᵃ)·*p*ᵗ with *t* = max(*b* − *c*, 0). Then *d* divides (*g* − 1)*x* and *n* does not,
  so the pair (*x*, *gx*) is merged. ∎

[checked: every n ≤ 200 and every one-generator *G*, 58,588 cases; every subgroup for n ≤ 40]

**(C) Two orbits.** The *G*-orbit and the *H*-orbit tell every number apart exactly when *G*_q and *H*_q
meet only in 1, for every prime power *q* dividing *n*.
- When *n* is square-free: exactly when gcd(|*G*_p|, |*H*_p|) = 1 for every prime *p* | *n*. For one
  generator each, that is gcd(ord_p *g*, ord_p *h*) = 1.
- On the units alone: exactly when *G* and *H* meet only in 1.

[FORCED] *Proof.* Two numbers sharing both orbits lie on one level *e*, as (*n*/*e*)*u* and (*n*/*e*)*u*′,
with *u*′/*u* in *G*_e ∩ *H*_e. So the readings separate exactly when *G*_e ∩ *H*_e = {1} for every
*e* | *n*.
- *Reduce to prime powers.* If *w* ≠ 1 lies in *G*_e ∩ *H*_e, then *w* ≢ 1 modulo some prime power *q*
  exactly dividing *e*, and *w* mod *q* lies in *G*_q ∩ *H*_q. Conversely, every prime power *q* | *n* is
  itself a level.
- *Square-free case.* The units mod *p* form a cyclic group, and two subgroups of a cyclic group, of
  orders *a* and *b*, meet in the subgroup of order gcd(*a*, *b*). ∎

[checked: all 245,920 ordered pairs of units for n ≤ 120, and all subgroup pairs for n ≤ 40]

**(D) The mirror and an orbit.** {*x*, −*x*} and the *G*-orbit tell every number apart exactly when −1 is
not in *G*_p for any odd prime *p* | *n*, nor in *G*₄ when 4 | *n*.

[FORCED] *Proof.* On level *e*, *x* ≠ −*x* exactly when *e* > 2, and −*x* = *gx* exactly when
*g* ≡ −1 mod *e*. Suppose −1 lies in *G*_e for some *e* > 2. Either *e* has an odd prime factor *p*, and
−1 lies in *G*_p; or *e* is 2ᵏ with *k* ≥ 2, and −1 lies in *G*₄. Conversely, *e* = *p* and *e* = 4 are
levels when they divide *n*. ∎

[checked: every n ≤ 300, 27,396 cases]

## 3. The trap at *n* = 15

Take *G* = ⟨2⟩ = {1, 2, 4, 8} and *H* = ⟨11⟩ = {1, 11}. They meet only in 1, so the two orbit readings
separate all eight units. [FORCED]

But on the level {5, 10}, where *e* = 3, both 2 and 11 act as −1 mod 3, so each swaps 5 and 10. Both
readings merge 5 with 10. [FORCED] Criterion (C) sees it: ord₃(2) = ord₃(11) = 2.

The same pair breaks *x* mod 5 with ⟨2⟩. The map from ⟨2⟩ to the units mod 5 is one-to-one, so the units
are separated, yet 5 ≡ 10 ≡ 0 mod 5. Criterion (B) sees it: 2 ≢ 1 mod 3.

[READING] In the authors' classification this is a Type I failure, of coverage. Each reading is sound,
and the pair {5, 10} is merged by both. The level picture teaches the lesson: the units said "enough",
and a lower level said no.

## 4. The archived errors, each with its counterexample

| archived statement | status | killed by |
|---|---|---|
| J27's "Crossing Lemma": *x* mod *d* and ⟨*g*⟩ separate ⟺ *g* ≢ 1 mod every *p* \| *n*/*d* | **backwards**; the truth is (B), *g* ≡ 1 mod *n*/*d* | *n* = 6, *d* = 2, *g* = 5: the orbit {1, 5} lies in one class mod 2. Wrong on 10,680 of 12,284 square-free cases with 1 < *d* < *n* ≤ 200 |
| J34 Theorem A and J35 Theorem 3.1: two orbits separate ⟺ ⟨*g*⟩ ∩ ⟨*h*⟩ = {1}, "equivalently" gcd(ord_p *g*, ord_p *h*) = 1 for all *p* | **false**: the two conditions are not equivalent, and only the second is right (C) | *n* = 15, *g* = 2, *h* = 11. The first condition misjudges 14,152 of 245,920 unit pairs (*n* ≤ 120) |
| J34 Theorem 4.1: if each prime is "resolved" by one of two maps, the maps separate | **false** for general maps | on ℤ/6, (*x* mod 2 + *x* mod 3) mod 2 and (*x* mod 3 − *x* mod 2) mod 3 resolve 2 and 3 respectively, yet both send 0 and 1 to the same labels |
| J34 Lemma 4.2: an orbit reading resolves *p* ⟺ *G* acts non-trivially mod *p* | **inverted**: it resolves *p* exactly when *G* ≡ 1 mod *p* | wrong in all 1,064 cases checked (square-free *n* ≤ 70) |
| J27's rewrite: separation by a residue and an orbit on all of ℤ/n "remains open" | **closed** by (B) | — |
| J27's rewrite: its hypothesis (i) is needed for the theorem on the units | **not needed**: hypothesis (ii), ord(*g* mod *d*) = ord(*g* mod *n*), is the whole criterion | 3,764 further cases where (ii) alone holds and the units are separated |
| J27's rewrite: "square-free is essential" to its theorems on the units | **false**: they hold for every *n* | (B) and (C) on the units |
| J35: the pair ⟨7⟩, ⟨11⟩ on ℤ/30 is mechanism (M3) | **mislabelled**: the supports {5} and {3} are disjoint, so it is (M1) by the paper's own definition | — |
| J34 and J35: "the minimum number of views for ℤ/n is 1" | **true but empty**: {*x* mod *p*, *x* mod *n*/*p*} already does it, by (A) | — |
| J34 Theorem D: the witness *y* = 1 + *pᵢ* at coordinate *i* | **void**: 1 + *pᵢ* ≡ 1 mod *pᵢ*, so *y* = *x* | — |

## What this is, and is not

- **Is:** four short criteria with proofs, a picture (the levels) that makes them clear, and one memorable
  trap. Together they are a worked instance of Theorem 0.
- **Is not:** new research. Each criterion is a few lines on top of classical facts: the gcd levels,
  Gauss's sum of φ, the Chinese Remainder Theorem, and the cyclic unit groups mod a prime. We found no
  published statement of (B)–(D) in this form, but they are exercises, and they are counted here as
  known, not as discoveries.

## Sources

- C. F. Gauss, *Disquisitiones Arithmeticae* (1801): the φ(*d*) over the divisors *d* of *n* add up to *n*.
- K. Ireland and M. Rosen, *A Classical Introduction to Modern Number Theory*, 2nd ed., Springer GTM 84
  (1990), Ch. 4: the structure of the units mod *n*.
- O. Ore, "Theory of equivalence relations", *Duke Math. J.* **9** (1942) 573–627: partitions and their
  meets, the setting of Theorem 0.
