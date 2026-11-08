# The sevenths

> *what if we made magic squares out of sevenths... what a rotation...* — the author, 7 November 2026
>
> *let's keep expanding into how unique a numbering system built on sevenths applied to classical math is*
> — the same day

### Tags: **[FORCED]** checked by [`verify_sevenths.py`](verify_sevenths.py) · **[NAMED]** a cited standard result · **[NEW]** not found in the literature we checked · **[READING]** an interpretation · **[COIN]** a classified pair: both sides kept, the edge named · **[FENCE]** two things that share a number but are not one object.

In the base, 7 is the octahedron with its centre ([`SEVEN_AND_NINE.md`](SEVEN_AND_NINE.md)). Counting in
sevenths draws the same picture a second way: six sevenths turning on one wheel, round a centre that is never
visited. This page builds the magic square the author asked for and finds what it pays for. Then it counts
with seven both ways the author asked: base 10 read through sevenths, and base 7. The two turn out to be the
two faces of the base's own coin at 7. Last, it sorts what belongs to 7 alone and what 7 shares.

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
- **Seven closes the wheel.**
  - Multiplying 142857 by 1 to 6 only turns it: 285714, 428571, 571428, 714285, 857142.
  - Multiplying by 7 lands on the centre: 142857 × 7 = 999999 = 10⁶ − 1. That is the wheel plus its flip,
    142857 + 857142, with every digit meeting its complement.
  - In decimals 7/7 = 1 = 0.999999…. **The centre is the one place where a seventh has two decimal faces**,
    1.000… and 0.999…. Every other k/7 has exactly one.
  - The same holds for every full wheel: 1/17's sixteen-digit wheel times 17 is sixteen 9s [NAMED: cyclic
    numbers].

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

### The modes, rolling in time [FORCED]

> *these transitions should read in fourier space?* · *imagine them as a dynamic integral rolling along a
> timeline, plotting their path* — the author, 7 November 2026

![Left: the digits of 1/7 plotted in time, one per turn of the wheel, with the smooth curve through them and the centre line at 4.5. Right: six paths in the complex plane, the running Fourier sums of the digits measured from 4.5, one for each frequency. The paths for frequencies 0, 2 and 4 return to the origin; frequency 3 runs straight along the real line to −11; frequencies 1 and 5 end at −5 ± 3√3 i.](../figures/the_wheel_in_time.svg)

- **The timeline.** Read the wheel as a signal in time, one digit per turn: 1, 4, 2, 8, 5, 7, 1, 4, …. The smooth
  curve through the digits is the sum of the wheel's six modes. Measured from 4.5, it turns over every three
  steps: half a turn later it is its own negative.
- **The integral, rolling.** At each frequency, add up the digits one turn at a time, each turned by that
  frequency's phase, and plot the running sum. The six modes are where the six paths arrive:
  - frequencies 0, 2 and 4 roll out and come back to 0. Those are the zeros the half turn pays for;
  - frequency 3, the half turn itself, rolls straight along the line to −11 = −11 × h(−7), the class number;
  - frequencies 1 and 5 land at −5 ∓ 3√3 *i*.
- **The same transitions, read on the seven levels.** Read on the seven levels with the seven-point Fourier
  transform of §6, the two faces trade places. The heptagon's turn becomes the clock, a phase on each mode, and
  the multiplying wheel runs backwards: the Fourier transform turns ×10 into ×5.

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

## 5. Two ways to count with seven [COIN]

The author asked for base 10 viewed in sevenths, and then added that base 7 may be an equally important
viewpoint. Both are kept. They turn out to be the two faces of one coin, and it is the base's own coin at 7.

![Two panels. Left: the seven remainders 0 to 6 on a heptagon, turned one step by adding 1, with the centre empty. Right: the six nonzero remainders on a hexagon, turned by multiplying by 10, with the squares 1, 2, 4 joined by a solid triangle and 3, 5, 6 by a dashed one, and 0 fixed at the centre.](../figures/the_two_sevens.svg)

### 5.1 Base 10, viewed in sevenths: multiplying turns the wheel [FORCED unless marked]

> *it's not base 7, it's base 10 viewed in sevenths... using the numerator* — the author, 7 November 2026

The author's system keeps base 10 and reads every number through sevenths, by its numerator.

- **The view.** Divide any whole number n by 7. The whole part counts the sevens in n. The tail is the wheel,
  turned by the numerator's remainder: 10/7 = 1.428571…, 100/7 = 14.285714…, 2026/7 = 289.428571…. When 7
  divides n the tail is empty: the centre. So in sevenths every number is a count of sevens and a place on the
  wheel, or the centre.
- **Multiplication becomes rotation.** The turns of a product are the sum of the turns, counted round the
  wheel of six. 2 is two turns and 3 is one, so 2 × 3 = 6 is three turns, half the wheel. Read this way, the
  remainders mod 7 carry a table of logarithms [NAMED: Gauss's indices, *Disquisitiones* §57].
- **The classical theorems become turns.**
  - Fermat: k⁶ leaves the remainder 1, because six turns are the whole wheel.
  - Euler: k³ leaves 1 when k is a square (an even number of turns: 1, 2, 4) and −1 otherwise. Three times an
    even turn is whole; three times an odd turn is a half.
  - Wilson: 1 × 2 × 3 × 4 × 5 × 6 leaves −1, because its turns add to 0 + 1 + 2 + 3 + 4 + 5 = 15, which is
    half a turn.
  - Orders: 3 and 5 turn the whole wheel, 2 and 4 go a third of the way round, and 6 goes halfway.
- **The base is a turn.** Multiplying by 10 is one turn, by 100 two, and by 1000 half the wheel: 1000 leaves
  −1. That is the old test for 7: alternate the signs of a number's three-digit blocks, and 7 divides the
  number exactly when it divides the result. The same test serves 11 and 13, because 1001 = 7 × 11 × 13.
  Among the primes whose reciprocals make a full decimal wheel, 7 is the only one whose half turn is a
  thousand.
- **Primes on the wheel** [FORCED: counted; NAMED: Dirichlet; Chebyshev's bias, Rubinstein and Sarnak 1994].
  Every prime except 7 lands on a turn. Below ten million the six turns hold almost equal shares, from
  110 653 to 110 815 primes each. Yet the odd turns (3, 5, 6) lead the even ones (1, 2, 4) at every
  checkpoint counted, every thousand up to ten million: the primes lean to the non-squares.
- **π in sevenths** [NAMED: Archimedes]. The continued fraction of π begins 3; 7, 15, 1, 292, …. So its first
  approximation is 3 + 1/7 = 22/7 = 3.142857 142857…: the wheel, unturned, just above π. This is a fact about
  π, whose first partial quotient happens to be 7. It is not a fact about sevenths.

### 5.2 Base 7: adding turns the heptagon [FORCED unless marked]

> *base 7 may be equally important a paradigm viewpoint* — the author, 7 November 2026

- **The view.** In base 7 the seven remainders are the digits 0 to 6. Adding 1 moves all seven one step round
  a single cycle, with nothing left in place: a heptagon turning, its centre empty. Here 0 is a digit like the
  others, out on the rim.
- **Base 7 is the sevenths view, repeated.** The last base-7 digit of a number is the remainder that the
  sevenths view reads. The other digits are its count of sevens, written the same way: 2026 is 5623 in base 7,
  and 2026 = 7 × 289 + 3. Base 10 viewed in sevenths reads one digit of base 7 and makes it a turn of the wheel;
  base 7 reads every digit as a place.
- **Its own tests.** Base 7 casts out sixes instead of nines: the digit sum tests 6. The alternating digit sum
  tests 8, as it tests 11 in base 10. Alternating pairs test 10, because 49 + 1 = 50. Alternating triples test
  43, because 343 + 1 = 344 = 8 × 43.
- **The mirror.** In base 7 the tenths make one wheel: 1/10 = 0.0462 0462…₇.
  - 1/10, 7/10, 9/10 and 3/10 are that wheel turned, because multiplying by 7 runs through the four remainders
    1, 7, 9, 3 that a tenth can have.
  - Half a turn is 7², which leaves −1 mod 10, so it complements the digits to 6: 0462 and 6204.
  - Each base sees the other's unit as one wheel. Among base 10's full wheels, the primes that turn both ways
    are 7, 17, 23, 47, 97, …, and 7 is the first.
- **The old theorems carry over.** Midy's complement is to 6 instead of 9. In Girstmair's formula 8 takes the
  place of 11: the alternating digit sum of 1/p in base 7 is −8·h(−p), and for 1/23 it is −24 = −8 × 3. The
  rank rule of §3 holds in base 7 too.
- **The first fully magic base-7 square** is at p = 10831, a square 10 830 digits wide. It was searched below
  20 000, setting aside the trivial 2 [NEW: not in OEIS, which lists bases 2, 3 and 10]. The same search finds
  the listed first cases of those bases: 59, 223 and 19.

### 5.3 The edge: where 0 sits [COIN; the group facts FORCED]

- The seven remainders carry two structures at once, and they are the two faces of the base's 7
  ([`SEVEN_AND_NINE.md`](SEVEN_AND_NINE.md)).
  - **The flat face, the heptagon.** Under adding, all seven sit round one circle and turn together, and the
    centre is empty. That is base 7.
  - **The solid face, the octahedron with its centre.** Under multiplying, 0 stays put, since 0 times anything
    is 0, and the other six turn round the octahedron's corners. That is the sevenths wheel.
- The edge between the faces is the field of seven elements, where adding and multiplying live together, joined
  by the distributive law. What moves between the faces is 0: on the rim when we add, at the centre when we
  multiply.
- **The same coin at 5** [FORCED]. Adding turns a pentagon, the book's flat 5. Multiplying by 2 turns 1, 2, 4, 3
  round 0, and a quarter turn with a mirror turns the tetrahedron's four corners in one cycle: the base's solid 5.
- **At 9 it breaks** [FORCED]. No symmetry of the cube has order 8, so nothing turns all eight corners round the
  centre. The cube's corners carry the field of eight elements another way, through their binary labels, with one
  corner, 000, fixed (the table below).
- **Two Fano planes** [FORCED]. The translates of the squares {1, 2, 4} make one Fano plane, and the translates of
  {3, 5, 6} make another; they share no line. Half a turn, x → −x, swaps them. A map x → ax + b keeps each plane
  when a is an even turn (1, 2, 4) and swaps them when a is an odd one.
- **The edge of swapping the bases** [FORCED]. A fraction ends in base 10 when its denominator divides a power of
  10, and in base 7 when it divides a power of 7. The only denominator that does both is 1. So swapping the base
  exchanges which fractions are wheels, and only the whole numbers stay put.
- [READING] So the author's two viewpoints are the base's coin at 7, made into arithmetic. The flat face counts,
  the solid face turns, and the coin's edge is 0, which sits on the rim of one and at the centre of the other.

### 5.4 How unique is each view? [COIN]

Base 10 can be viewed through any prime whose reciprocal makes a full wheel: 7, 17, 19, 23, 29, …. Ask two
questions of each feature. Is 7 alone in it? And does it need base 10 at all?

| the feature | standing | is 7 alone? | needs base 10? |
|---|---|---|---|
| One wheel through every remainder | [FORCED] | the smallest of base 10's full wheels | **yes.** In base *b*, sevenths make one wheel exactly when *b* leaves remainder 3 or 5 mod 7 |
| Multiplication becomes rotation; Fermat, Euler and Wilson become turns | [FORCED; NAMED: Gauss] | no: every full wheel does this | the turns are counted in powers of 10 |
| Half a turn is the flip: it complements the digits, and it is −1 | [FORCED; NAMED: Midy] | no: every full wheel | yes |
| **Half a turn is a thousand**, which gives the three-digit test for 7 | [FORCED] | **yes**: the only full wheel whose half turn is 10³ | yes |
| The square: rows and columns 27, diagonals 31 and 23, rank 4 | [FORCED] | no: every full wheel makes one, and 19 is the first fully magic | yes |
| **The squares (the even turns), {1, 2, 4}, form a projective plane**, the Fano plane: every nonzero difference occurs exactly once | [FORCED; NAMED: Paley's difference sets] | **yes.** For p ≡ 3 (mod 4) the squares repeat each difference (p − 3)/4 times, which is once only at p = 7 | no |
| The Fano plane multiplies the octonions: e_i e_(i+1) = e_(i+3), with indices mod 7. They are the last normed division algebra, and they give a cross product in 7 dimensions | [FORCED: norms multiply; NAMED: Hurwitz 1898, Massey 1983] | shared: cross products exist only in 3 and 7 dimensions | no |
| The same plane on the cube's corners: in 𝔽₈ the powers of one element run through the seven nonzero 3-bit strings, and α^i ⊕ α^(i+1) = α^(i+3). These are the binary labels of [`planes_and_mirrors`](../towers/planes_and_mirrors/README.md) | [FORCED] | (the same plane, labelled twice) | no |
| 168 symmetries: the Fano plane's, and Klein's quartic's | [FORCED: counted; NAMED: Klein 1878] | **yes.** 1/2 + 1/3 + 1/7 = 41/42 is the closest three unit fractions come to 1 from below. So a surface of genus *g* has at most 84(*g* − 1) symmetries [NAMED: Hurwitz 1893], which is 168 at genus 3 | no |
| The heptagon is the first regular polygon that straightedge and compass cannot draw; 2cos(2π/7) solves x³ + x² − 2x − 1 = 0 | [FORCED; NAMED: Gauss 1801, Wantzel 1837] | **yes**, as the first | no |
| ℚ(√−7) factors uniquely (class number 1), and shows as the −11 in the square | [FORCED; NAMED: Girstmair; Heegner, Stark, Baker] | shared: 19 gives −11 too, and eight fields in all have class number 1 | the factor 11 = 10 + 1 does |
| The primes lean to the odd turns | [FORCED: counted; NAMED] | no: Chebyshev's bias holds for every modulus | no |
| π ≈ 22/7 = 3.142857… | [NAMED] | a fact about π | — |
| The base's 7: the octahedron with its centre | [FORCED] | shared with 5 and 9 | no |
| Adding and multiplying are the base's two faces: a heptagon with its centre empty, and the octahedron turning round 0 | [FORCED; READING] | the octahedron is 7's own: at 5 the same coin gives the tetrahedron, and at 9 it breaks | no |
| Each base sees the other's unit as one wheel: 10 turns the units mod 7, and 7 turns the units mod 10 | [FORCED] | the first of 7, 17, 23, 47, 97, … | it is a relation between 10 and 7 |

**What it shows** [READING].
- In sevenths, base 10 becomes a wheel whose step is 10 itself. Multiplying becomes turning, and the classical
  theorems about remainders become statements about turns.
- In base 7, the same seven remainders are digits on a heptagon, and adding turns them. Each base sees the
  other's unit as one wheel.
- The two views are the base's coin at 7. The flat face counts, the solid face turns, and 0 is the edge: on the
  rim of one, at the centre of the other.
- The half turn is the flip in every guise:
  - the complement of the digits (to 9 in base 10, to 6 in base 7);
  - the inversion of the octahedron;
  - the −1 in Euler's and Wilson's theorems;
  - the thousand in the test for 7;
  - the swap of the two Fano planes.
- What belongs to 7 alone:
  - its wheel is the smallest, and its half turn falls at a thousand;
  - its multiplying face is the octahedron;
  - it has arithmetic no change of base can touch: the Fano plane, 168 and the heptagon.

## 6. On seven quantum levels

The author then asked how the two faces meet our space for quantum parts. A quantum system with seven levels
is indexed by the seven remainders, so both faces act on it: adding is the shift, multiplying is the multiplier,
and the Fourier transform joins them. Eight predictions were registered before the run, and seven held. The
eight measurement bases move like the cube's corners, and the "magic" subspace is Klein's space, where the
octahedron acts as it does on ours. One guess died: the Legendre state, the octahedron's height, is not the
most negative state. A second round found the state that beats it, by 0.0043. The Legendre state is odd under
the half turn, the wheel's flip, and the winner is even about its own centre. At the centre the flip decides
which way a state's quasi-probability goes: down to −1/7 for an odd state, up to +1/7 for an even one. A third
round settled both sides at seven by counting every case: the Legendre state is the deepest odd state, and the
even winner is the best state with any symmetry. At eleven the even side wins again. The
results are in [`../towers/seven_levels/`](../towers/seven_levels/README.md).

## What this page is, and is not

- **Is:** the author's sevenths made exact, and seven counted both ways the author asked: base 10 read through
  sevenths, and base 7. They are classified as the two faces of the base's coin at 7, neither chosen over the
  other. The known parts are credited, and each special-looking fact is sorted by whether 7 is alone in it and
  whether it needs base 10.
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
- C. F. Gauss, *Disquisitiones Arithmeticae* (1801), §57 for the indices; P. L. Wantzel (1837).
- M. Rubinstein and P. Sarnak, "Chebyshev's bias", *Experiment. Math.* **3** (1994): why the primes lean to the
  non-squares.
- Archimedes, *Measurement of a Circle*: π < 22/7.
- K. Heegner (1952), H. M. Stark (1967) and A. Baker (1966): the class-number-one fields.
