# The coin at 5 in the fifth moment, and the coins at 7 and 9

### Tags: **[FORCED]** checked by [`coin_at_five.py`](coin_at_five.py) · **[NAMED]** a cited result · **[measured]** computed exactly · **[READING]** an interpretation, not a claim · **[COIN]** a classified pair: flip, sides and edge.

> *1 and 2, J4's surface sum first* — the author, 14 November 2026. The "1" says yes to testing the reading that the
> fifth moment's split by (5|p) is the coin at 5.

Every coin has two sides and an edge (the author). [`../../base/SEVEN_AND_NINE.md`](../../base/SEVEN_AND_NINE.md)
classifies 5, 7 and 9 that way.
- **The flat face** is the regular polygon, with its centre empty.
- **The solid face** is the tetrahedron, octahedron or cube with its centre filled: 5 = 4 + centre, 7 = 6 + centre and
  9 = 8 + centre.
- **The edge** is the centre itself.

This page finds that coin in the arithmetic of the fifth moment, and follows it to 7 and 9. The tests are rounds 19
and 20 of [`PREREG.md`](PREREG.md).

## What stands

- **The dictionary** [FORCED]. The double octic behind the fifth moment I5 ([`TORUS_MOMENTS.md`](TORUS_MOMENTS.md)
  §8, Theorem 7) is the coin at 5.
  - The **solid face** is the five planes where one of the five points sits at the centre.
  - The **flat face** is Clebsch's cubic, which holds the regular pentagon.
  - The **edge** is their 15 common lines.
  - The **flip** is the sign of a permutation of the five points, and over Q it is √5 ↦ −√5. It is the (5|p) in I5.
- **The edge, in the moments** [measured; round 19]. I5's formula holds at the edge p = 5, where (5|5) = 0 averages
  its two sides. The registered claim that the parity-weighted moments do too died.
- **The coin at 7** [NAMED; measured, held blind]. The flat face at 7 is the cubic fourfold
  X7 = {x1 + ⋯ + x7 = x1³ + ⋯ + x7³ = 0}. Its point count is

    #X7(F_p) = 1 + p + p² + p³ + p⁴ + p²·(14 + 6(5|p)) + p·c(p),

  where |c(p)| is the coefficient of the weight-3 newform with complex multiplication by Q(√−35). The algebraic part
  sees only the pentagon's √5. The prime 7 enters only through the transcendental part, by √−35 = √5·√−7.
- **At 9** [measured, held blind]. In nine variables,

    #X9(F_p) = 1 + p + ⋯ + p⁶ + p³·(42 + 27(5|p) + (105|p)) + 8p²·c(p),

  with the same c. The one new character is (105|p) = (−3|p)(−35|p).
- **The counts add up.** The primitive middle cohomology has dimension 6 = 5 + 1 for Clebsch's cubic, 22 = 14 + 6 + 2
  for X7, and 86 = 42 + 27 + 1 + 8·2 for X9.

## 1. The dictionary [FORCED; [`coin_at_five_verify.log`](coin_at_five_verify.log)]

In the fifth moment the five points of the turning wheel have Cayley coordinates δ1, …, δ5 with Σδ_i = 0, so 0 is
their centre. The count behind I5 lives on the double octic w² = e3·e5 over P³ = {Σδ = 0}. That is the double cover
branched along e5 = 0 and e3 = 0.

| the coin at 5 | in the double octic | check |
|---|---|---|
| **solid face**: the tetrahedron with its centre filled | e5 = δ1δ2δ3δ4δ5 = 0, the five Sylvester planes. One point sits at the centre (δ_i = 0, the wheel's identity) and the other four sum to 0 round it | — |
| **flat face**: the pentagon, its centre empty | e3 = 0, Clebsch's diagonal cubic. It holds the regular pentagon (1, z, z², z³, z⁴), z⁵ = 1, which has e1 = ⋯ = e4 = 0 and e5 ≠ 0 | D1 |
| **edge** | the faces meet in 15 lines. On the plane δ5 = 0, e3 = −(δ1 + δ2)(δ1 + δ3)(δ2 + δ3), so each line is the centre with two opposite pairs, (0, a, −a, b, −b). All 15 are rational | D2, D3b |
| **flip** | the cubic's other 12 lines form a double six. Every even permutation of the five points keeps each six, and every odd one swaps them | D3c, D3d |
| **sides** | over Q the two sixes are conjugate under √5 ↦ −√5 [NAMED: Clebsch 1871]. So there are 27 lines over F_p when (5\|p) = 1 and 15 when (5\|p) = −1, and the cubic has p² + (6 + (5\|p))p + 1 points | D3a, D5 |
| **edge prime** | in characteristic 5, where (5\|p) = 0, the cubic gets exactly one singular point, the centre [1:1:1:1:1], where the five points coincide | D4a |

- **[COIN]** The flip is the sign of a permutation, equal on the double six to √5 ↦ −√5. The sides are the two sixes;
  for primes they are (5|p) = ±1. The fixed set is the edge: the 15 rational lines, and the prime 5.
- **The double cover needs both faces.** e3 and e5 have odd degree, and a double cover of 3-space must be branched in
  even degree. So the branch locus must hold both faces, and the level-10 form of I5 lives over both, with neither
  chosen.
- **In any number of variables** the cubic {Σx = Σx³ = 0} is singular over F_p, for p > 3, exactly at the sign vectors
  whose sum vanishes mod p (D4b). Its centre [1:⋯:1] is among them exactly when p divides the number of variables.
  - With 5 variables that happens at 5, and with 7 at 7.
  - With 9 variables it never happens for p > 3. 9's only prime is 3, and in characteristic 3 every one of these
    cubics degenerates, since the cubes sum to the cube of the sum.

## 2. The edge, in the moments [measured; round 19]

The registered test, C1 of round 19, put each formula at the edge primes. The Legendre symbol there is 0, the average
of its two sides, and each form enters with its coefficient at its bad prime. Those coefficients were computed before
the registration: a10(5) = 5 and a10(3) = −8 (the engine, with U_q); f15(5) = 5 and f15(3) = −3 (the eta products).

| moment | p | registered | the operators | |
|---|---|---|---|---|
| I5 (no flip) | 5 | 3504 | 3504 | held |
| I5 | 3 | 368 | 368 | held |
| J4 (Theorem 5) | 3 | 80 | 80 | held (C0) |
| J5 (with the flip P) | 5 | −930 | −1680 | **died** |
| J5 | 3 | −84 or −192 | 240 | **died** |
| J3 | 3 | −12 (the average) or 0 | 24 | **died** |

- So the edge-average reading holds for the moment without the flip, and dies for the parity-weighted ones. The
  death is kept in [`../../GRAVEYARD.md`](../../GRAVEYARD.md) with these values.
- [READING] At its edge, J3 does not average its sides. It is +2p(p + 1), the mirror of its (−3|p) = −1 side,
  −2p(p + 1).

## 3. The coin at 7 [NAMED; measured; rounds 19 and 20]

The dictionary's flat face at 7 is the analogue of Clebsch's cubic: X7 = {Σx = Σx³ = 0} in seven variables. The
author's coin holds at 7: the heptagon is its flat face, and the octahedron with its centre its solid face.
- **What was known** [NAMED].
  - X7 is the cubic fourfold that Laza and Zheng call X¹(A7). Koike calls it the Clebsch–Segre cubic.
  - The alternating group A7 acts on it symplectically. The odd permutations do not: they act by −1 on H^(3,1), the
    flip again.
  - Its transcendental lattice is −[[2, 1], [1, 18]], of discriminant 35 [Laza and Zheng, arXiv:1905.11547]. A
    two-dimensional transcendental part like this one is carried by a weight-3 form with complex multiplication, here
    by Q(√−35) [NAMED: the mechanism is Livné's, for singular K3 surfaces].
- **Registered (round 19, C2), and held.** The primitive trace t7 = #X7(F_p) − (1 + p + p² + p³ + p⁴) is divisible
  by p² at every one of the 37 primes from 11 to 397 that is inert in Q(√−35), and at none of the 37 split ones.
- **Measured.** The point count is exact:
  t7 = p²(14 + 6(5|p)) + p·c(p). Here |c(p)| is the CM form's coefficient:
  - 0 at the inert primes;
  - |2x² + 2xy − 17y²| = |π² + π̄²| when p = x² + xy + 9y² is the norm of π = x + y(1 + √−35)/2;
  - |u|, with u² + 35v² = 4p², when p = 3x² + xy + 3y², the other class of the class group of order 2.
  This was read after round 19 at the 74 primes from 11 to 397, and held blind at all 32 primes from 401 to 601
  (round 20, H1; [`coin_at_five_test20.log`](coin_at_five_test20.log)). The signs of c are not fixed here.
- So the algebraic part splits as 14 + 6(5|p): 14 classes fixed by Galois, and 6 on which Frobenius acts by (5|p).
  That is the same flip as Clebsch's double six, one dimension up.
- [READING] At 5 the flip's part of the cohomology is algebraic, and carries √5. At 7 it is transcendental, and
  carries √−35 = √5·√−7. √−7 is the heptagon's Gauss sum, Σ_a (a|7)e^(2πia/7), as √5 is the pentagon's. The coin at 7
  carries the coin at 5 inside it.

## 4. At 9, where the coin breaks [measured; rounds 19 and 20]

In base/SEVEN_AND_NINE.md 9 has a third face, the 3 × 3 grid: two coins of 3 tossed together.
- **Measured.** In nine variables the cubic sixfold X9 = {Σx = Σx³ = 0} has
  t9 = #X9(F_p) − (1 + p + ⋯ + p⁶) = p³(42 + 27(5|p) + (105|p)) + 8p²c(p), with X7's c.
  - Read after round 19 at the 74 primes from 11 to 397, it held blind at all 32 from 401 to 601 (round 20, H2).
  - The one new character, (105|p) = (−3|p)(−35|p), was found as a sign that the formula without it missed at half
    the primes. A search over quadratic characters found (21|p) for that sign, and no other.
- [READING] 9 = 3², and its one new character carries 3, the prime under 9: the triangle's (−3|p), tossed together
  with the field from 7. Nothing of conductor 9 appears.

## 5. Standing

- **Known, and credited** [NAMED].
  - The 27 lines of Clebsch's diagonal cubic, 15 over Q and 12 over Q(√5) (Clebsch 1871).
  - The cubic's icosahedral symmetry, and its place as the Hilbert modular surface of Q(√5) (Hirzebruch 1976).
  - X7 as X¹(A7), with its transcendental lattice (Laza and Zheng), and its equations and name (Koike).
  - Weight-3 CM forms for two-dimensional transcendental lattices (Livné 1995).
- **This repository's own, new as far as we checked.**
  - The dictionary between the author's coin at 5 and the fifth moment.
  - The exact point counts of X7, in particular the split 14 + 6(5|p) of its algebraic part, and of X9.
  - Web searches on 2026-11-14 found no point count, zeta function or Galois action for either cubic. They found the
    neighbours: the Fermat cubic fourfold's form of level 27, the census of cubic fourfolds over F₂, and the Segre
    cubic.
- **Open.**
  - The signs of c(p): which twist of the CM form.
  - Proofs of X7's and X9's counts. The S7 and S9 representations on the middle cohomology, and the moments of cubic
    exponential sums that count these points, are two ways in.
  - Whether the seventh moment I7 carries Q(√−35), as I5 carries √5.
  - The cubic in eleven variables, past the base's edge at 10.
- **Died:** C1's parity-weighted half (§2), kept in the graveyard.

## Run it

```
python coin_at_five.py           # the dictionary, D1 to D5: seconds
python coin_at_five.py test      # round 19: the edge, and the cubics to 397: about a minute, four processes
python coin_at_five.py test20    # round 20: the cubics at 401..601, blind: about a minute, four processes
```

## Sources

- A. Clebsch, "Ueber die Anwendung der quadratischen Substitution auf die Gleichungen 5ten Grades und die geometrische
  Theorie des ebenen Fünfseits", *Math. Ann.* **4** (1871).
- F. Hirzebruch, "The Hilbert modular group for the field Q(√5), and the cubic diagonal surface of Clebsch and Klein",
  *Russian Math. Surveys* **31** (1976).
- R. Laza and Z. Zheng, "Automorphisms and periods of cubic fourfolds", *Math. Z.* **300** (2022), 1455–1507,
  [arXiv:1905.11547](https://arxiv.org/abs/1905.11547).
- K. Koike, "Cubic fourfolds with symplectic automorphisms" (2024), [arXiv:2409.08448](https://arxiv.org/abs/2409.08448):
  equations for the six maximal cases, and their fields of definition.
- R. Livné, "Motivic orthogonal two-dimensional representations of Gal(Q̄/Q)", *Israel J. Math.* **92** (1995).
- K. Ireland and M. Rosen, *A Classical Introduction to Modern Number Theory*, 2nd ed., Springer (1990): Gauss and
  Jacobi sums.
