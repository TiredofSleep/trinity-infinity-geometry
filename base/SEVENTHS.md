# The sevenths

> *what if we made magic squares out of sevenths... what a rotation...* — the author, 7 November 2026
>
> *let's keep expanding into how unique a numbering system built on sevenths applied to classical math is*
> — the same day

### Tags: **[FORCED]** checked by [`verify_sevenths.py`](verify_sevenths.py) · **[NAMED]** a cited standard result · **[NEW]** not found in the literature we checked · **[READING]** an interpretation · **[COIN]** a classified pair: both sides kept, the edge named · **[FENCE]** two things that share a number but are not one object.

In the base, 7 is the octahedron with its centre ([`SEVEN_AND_NINE.md`](SEVEN_AND_NINE.md)). Counting in
sevenths draws the same picture a second way: six sevenths turning on one wheel, round a centre that is never
visited. This page builds the magic square the author asked for and finds what it pays for. Then it sorts what
is special about sevenths into three kinds: what belongs to 7 in every base, what 7 shares with other numbers,
and what is only an accident of writing numbers in tens.

![The six sevenths on a hexagon, in the order 1, 3, 2, 6, 4, 5 that multiplying by 10 visits. Each is labelled with its repeating digits, all turns of 142857. Opposite corners are complements, such as 1/7 and 6/7. A solid triangle joins the squares mod 7 (1, 2, 4) and a dashed one joins 3, 5 and 6. The centre, 0/7, is never visited.](../figures/the_sevenths.svg)

---

## 1. The wheel [FORCED]

- 1/7 = 0.142857 142857 …. Its repeating block has six digits, the most a seventh can have, because 10 is a
  *primitive root* mod 7: the powers 1, 10, 100, 1000, … leave every remainder from 1 to 6 before they repeat.
- **Every seventh is the same wheel, turned.** Multiplying by 10 moves the decimal point one place. So k/7 is
  142857 started r places on, where 10^r leaves the remainder k: 3/7 = 0.428571… is one turn, 2/7 =
  0.285714… is two, and so on round the wheel 1 → 3 → 2 → 6 → 4 → 5 → 1.
- **Half a turn is the flip.** Three turns send k/7 to (7 − k)/7 = 1 − k/7, and every digit d to 9 − d:
  142 + 857 = 999 [NAMED: Midy's theorem, 1836]. Measured from 4.5, the middle of the digits, half a turn is
  negation. It is the coin z → −z, done by turning.

## 2. The square [FORCED]

Write the six sevenths as the rows of a square:

```
1 4 2 8 5 7    1/7
2 8 5 7 1 4    2/7
4 2 8 5 7 1    3/7
5 7 1 4 2 8    4/7
7 1 4 2 8 5    5/7
8 5 7 1 4 2    6/7
```

- Every row and every column adds to 27.
- **[COIN] The diagonals are a coin.** They add to 31 and 23. Row 7 − k is row k flipped, so each diagonal is
  the other's flip, entry by entry, and the two always average 27. The square would be fully magic only if a
  diagonal stood on that edge. For sevenths it misses by 4 on each side [NAMED: the 1/7 square is known in the
  literature of prime reciprocal magic squares].
- The same holds for every prime whose reciprocal has the full period: rows and columns agree, and the
  diagonals are each other's flips. This is checked for every such prime below 400.
- **The first prime that stands on the edge is 19**: its 18 × 18 square adds to 81 along every row, column and
  diagonal [NAMED: Andrews 1917]. Below 5000 the only other is 383. The list goes on 32327, 34061, …
  [NAMED: OEIS A072359; recomputed up to 40 000 by `verify_sevenths.py --long`].

## 3. What the half turn pays for

- **Two zeros** [FORCED]. The square has rank 4. Weight its six columns 0, 1, −1, 0, 1, −1, or
  2, −1, −1, 2, −1, −1, and they add to nothing. The half turn pays for both, as in
  [*A Ledger of Nothing*](../towers/kernel_ledger/A_LEDGER_OF_NOTHING.md): columns three places apart add to 9,
  so these weights cancel.
- **Measured from the centre, exactly half** [FORCED]. Subtract 4.5 from every digit and the rank falls to 3.
- **The wheel's six modes** [FORCED]. A wheel's square is a circulant matrix with its rows reordered, so its
  spectrum is the wheel's six Fourier modes: 27, 0, 0, −11 and −5 ± 3√3 *i*. The two zeros are the modes the
  half turn kills.
- **A class number inside** [FORCED; NAMED: Girstmair 1994]. The half-turn mode is the alternating digit sum,
  1 − 4 + 2 − 8 + 5 − 7 = −11. That is −11 times the class number of ℚ(√−7), which is 1. For every prime
  p ≡ 3 (mod 4) with a full decimal period, the alternating sum is −11·h(−p) (checked below 400).
- **Every full wheel, in every base** [FORCED for every case checked; NEW: not found stated in the literature
  we checked]. Let p be a prime and b a base in which 1/p has the full period p − 1. Then the
  (p − 1) × (p − 1) square of the base-*b* digits of k/p has rank exactly (p + 1)/2. Measured from its centre,
  its rank is exactly (p − 1)/2.
  - *Why.* Mode m of the wheel equals (b − ω⁻ᵐ)·B₁,χ. Here χ is the character of the units mod p with
    χ(b) = ωᵐ, and B₁,χ = (1/p) Σ x χ(x) [FORCED: the identity, checked numerically].
  - The trivial character gives the row sum. When χ is even and not trivial, B₁,χ = 0: those are the zeros
    the half turn pays for.
  - When χ is odd, B₁,χ is never 0. It is a factor of the class-number formula [NAMED: Washington,
    *Cyclotomic Fields*, ch. 4]. Equivalently, L(1, χ) ≠ 0, the fact Dirichlet needed for primes in
    arithmetic progressions. So no zero is ever bought.
  - Checked on 65 squares: in base 10 for every full-period prime below 200, and in bases 2, 3 and 7 below 150.
    The same rank, (p + 1)/2, is known for a different circulant built from primitive roots
    [NAMED: arXiv:2601.10757].

## 4. The wheel on the octahedron [READING; the group facts FORCED]

- Put the six sevenths on the six corners of an octahedron. One step of the wheel (×10) is a sixth of a turn
  about one axis followed by a mirror, the rotoreflection S₆. It visits all six corners in one cycle.
- Three steps make the octahedron's inversion through its centre. Opposite corners carry 1 and 6, 2 and 5,
  3 and 4: the pairs that add to 7.
- Two steps go round a triangle. The corners split into two opposite faces: 1, 2, 4, the squares mod 7, and
  3, 5, 6.
- The centre, 0/7, is never visited. That is the base's 7, the octahedron with its centre, and the author's early
  line: *"Primes are the void that never get touched"* (January 2026).
- [FENCE] In arithmetic mod 7, 7 and 0 are the same remainder by definition. That is not the retired "0/7
  pairing" of the table program, which stays retired ([`../coin/THE_COIN.md`](../coin/THE_COIN.md)). In the
  base, 7 is not special among 5, 7 and 9: all three fill their centres for one reason.

## 5. How unique is counting in sevenths? [COIN]

Ask two questions of every special-looking fact about sevenths. Is 7 alone in it? And would it survive a
change of base?

| the fact | standing | is 7 alone? | survives a change of base? |
|---|---|---|---|
| A full decimal wheel; 7 is the smallest prime with one | [FORCED] | the smallest, in base 10 | **no.** 7 has a full wheel in base *b* exactly when *b* leaves remainder 3 or 5 mod 7. In base 7, 1/7 = 0.1, and the wheel is gone |
| The sevenths square: rows and columns 27, diagonals 31 and 23, rank 4 | [FORCED] | no: every full wheel makes one (§2, §3) | the digits do not; the rank rule does |
| The units mod 7 make one cycle of 6 | [FORCED] | no: the units mod any prime make one cycle | yes |
| **The squares mod 7, {1, 2, 4}, form a projective plane** (the Fano plane): every nonzero difference occurs exactly once | [FORCED; NAMED: Paley's difference sets] | **yes.** For p ≡ 3 (mod 4) the squares repeat each difference (p − 3)/4 times, which is once only at p = 7 | yes |
| The Fano plane multiplies the octonions: e_i e_(i+1) = e_(i+3), with indices mod 7. They are the last normed division algebra, and they give a cross product in 7 dimensions | [FORCED: norms multiply; NAMED: Hurwitz 1898, Massey 1983] | shared: cross products exist only in 3 and 7 dimensions | yes |
| The same plane on the cube's corners: in 𝔽₈ the powers of one element run through the seven nonzero 3-bit strings, and α^i ⊕ α^(i+1) = α^(i+3). These are the binary labels of [`planes_and_mirrors`](../towers/planes_and_mirrors/README.md) | [FORCED] | (the same plane, labelled twice) | yes |
| 168 symmetries: the Fano plane's, and Klein's quartic's | [FORCED: counted; NAMED: Klein 1878] | **yes.** 1/2 + 1/3 + 1/7 = 41/42 is the closest three unit fractions come to 1 from below. So a surface of genus *g* has at most 84(*g* − 1) symmetries [NAMED: Hurwitz 1893], which is 168 at genus 3 | yes |
| The heptagon is the first regular polygon that straightedge and compass cannot draw; 2cos(2π/7) solves x³ + x² − 2x − 1 = 0 | [FORCED; NAMED: Gauss 1801, Wantzel 1837] | **yes**, as the first | yes |
| ℚ(√−7) factors uniquely (class number 1) | [FORCED below 200; NAMED: Heegner, Stark, Baker] | shared with 1, 2, 3, 11, 19, 43, 67 and 163 | yes |
| The base's 7: the octahedron with its centre | [FORCED] | shared with 5 and 9 | yes |

**Counting in base 7** [FORCED]. With 7 as the base, the roles change places.
- The sevenths terminate, and the wheels move to other primes. The first is 1/5 = 0.1254 1254 …₇, whose
  halves add to 66₇: Midy again, with 6 in place of 9.
- Every theorem above survives with 10 replaced by 7. The rank is still (p + 1)/2, and in Girstmair's formula 8
  takes the place of 11: the alternating digit sum of 1/p in base 7 is −8·h(−p). For 1/23 it is −24 = −8 × 3.
- **The first prime whose base-7 square is fully magic is 10831**, a square 10 830 digits wide (searched below
  20 000, setting aside the trivial 2) [FORCED; NEW: not in OEIS, which lists bases 2, 3 and 10]. The same
  search finds the listed first cases of those bases: 59, 223 and 19.

**What it shows** [READING].
- The decimal wheel is an accident of writing numbers in tens: in base 7 it vanishes.
- What belongs to 7 itself is its arithmetic. Its squares form the only projective plane that any prime's
  squares can make. That plane multiplies the octonions and has 168 symmetries. 7 sits at the edge of Hurwitz's
  triangle, and the heptagon is where straightedge and compass first fail.
- The two faces share an edge: the cycle of six, whose half turn is the flip in both. On one face it
  complements the digits; on the other it inverts the octahedron.

## What this page is, and is not

- **Is:** the author's sevenths made exact. The known parts are credited, and each special-looking fact is
  sorted by whether 7 is alone in it and whether it survives a change of base.
- **Is not:** a claim that 7 is special in some deeper sense. Small numbers turn up everywhere. This page keeps
  only what is forced or cited, and says for each fact who else shares it.

## Sources

- E. Midy, *De quelques propriétés des nombres et des fractions décimales périodiques*, Nantes (1836).
- W. S. Andrews, *Magic Squares and Cubes* (1917): the 1/19 square.
- OEIS [A072359](https://oeis.org/A072359) (base 10), A096339 (base 2), A096660 (base 3); Wikipedia,
  [Prime reciprocal magic square](https://en.wikipedia.org/wiki/Prime_reciprocal_magic_square).
- K. Girstmair, "A 'popular' class number formula", *Amer. Math. Monthly* **101** (1994); a worked check:
  arXiv:1502.04971.
- L. C. Washington, *Introduction to Cyclotomic Fields*, 2nd ed., Springer (1997), ch. 4.
- "Rank duality of circulant matrices from primitive roots", arXiv:2601.10757 (2026).
- R. E. A. C. Paley, "On orthogonal matrices", *J. Math. Phys.* **12** (1933): the quadratic-residue difference sets.
- A. Hurwitz (1898), the normed division algebras; W. S. Massey, "Cross products of vectors in higher
  dimensional Euclidean spaces", *Amer. Math. Monthly* **90** (1983); J. C. Baez, "The octonions", *Bull. Amer.
  Math. Soc.* **39** (2002), for the rule e_i e_(i+1) = e_(i+3).
- F. Klein (1878), the quartic; A. Hurwitz (1893), the bound 84(g − 1).
- C. F. Gauss, *Disquisitiones Arithmeticae* (1801); P. L. Wantzel (1837).
- K. Heegner (1952), H. M. Stark (1967) and A. Baker (1966): the class-number-one fields.
