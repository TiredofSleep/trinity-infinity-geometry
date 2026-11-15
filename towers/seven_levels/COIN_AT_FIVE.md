# The coin at 5 in the fifth moment, the coins from 7 to 27, and the edge

### Tags: **[FORCED]** checked by [`coin_at_five.py`](coin_at_five.py) or [`edge_rule.py`](edge_rule.py) · **[NAMED]** a cited result · **[measured]** computed exactly · **[READING]** an interpretation, not a claim · **[COIN]** a classified pair: flip, sides and edge.

> *1 and 2, J4's surface sum first* — the author, 14 November 2026. The "1" says yes to testing the reading that the
> fifth moment's split by (5|p) is the coin at 5.

> *1 and 2, the mirror rule first* — the author, 14 November 2026. The "1" says a coin on its edge shows the mirror;
> the "2" says go past the base, to eleven.

> *1 and 2, thirteen first* — the author, 14 November 2026. The "2": 9 is two coins of 3 tossed together, so 3 enters
> only at its square.

> *1 and 3, seventeen first* — the author, 15 November 2026. The "3" takes up the reading at 13: its piece is both
> faces at once.

> *2 and 3, 27 first* — the author, 15 November 2026. The "2" asks for the sharpened rule at 27, three coins of 3.

Every coin has two sides and an edge (the author). [`../../base/SEVEN_AND_NINE.md`](../../base/SEVEN_AND_NINE.md)
classifies 5, 7 and 9 that way.
- **The flat face** is the regular polygon, with its centre empty.
- **The solid face** is the tetrahedron, octahedron or cube with its centre filled: 5 = 4 + centre, 7 = 6 + centre and
  9 = 8 + centre.
- **The edge** is the centre itself.

This page finds that coin in the arithmetic of the fifth moment, and follows it to 7 and 9 (rounds 19 and 20 of
[`PREREG.md`](PREREG.md)), to its edge (round 21), past the base to 11, 13, 15, 17 and 21 (rounds 22 to 25), to
the prime 3 itself (round 25), and to 27 (round 26).

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

  where c(p) is the coefficient of LMFDB's newform 35.3.c.b, of weight 3, with complex multiplication by Q(√−35).
  The algebraic part sees only the pentagon's √5. The prime 7 enters only through the transcendental part, by
  √−35 = √5·√−7.
- **At 9** [measured, held blind]. In nine variables,

    #X9(F_p) = 1 + p + ⋯ + p⁶ + p³·(42 + 27(5|p) + (105|p)) + 8p²·c(p),

  with the same c. The one new character is (105|p) = (−3|p)(−35|p).
- **The counts add up.** The primitive middle cohomology has dimension 6 = 5 + 1 for Clebsch's cubic, 22 = 14 + 6 + 2
  for X7, and 86 = 42 + 27 + 1 + 8·2 for X9.
- **The edge** [FORCED; measured, held blind; §5]. On its edge a coin shows the fixed set of its flip.
  - J3's mirror at 3 is forced: there the two cube roots of unity merge into 1, and the hexagon's phase vanishes.
  - At every prime edge the mirror is exact, and at 9 it fails.
  - The cubics, counts without a phase, see the fixed set at their edge primes 5 and 7. That held blind at all five
    values, and in the 21 lines of Clebsch's cubic over F_5.
- **Where the counts come from** [FORCED; NAMED; §6].
  - The cubics' counts are the moments of the cubic exponential sums. So they split into the symmetric powers of the
    Airy sheaf, by ballot numbers, and each n brings one new piece.
  - The new pieces are (5|p) at 5, the form 35.3.c.b at 7, and (105|p) at 9.
  - The nodes of each cubic mod p count exactly the dimensions of these pieces that are ramified at p.
- **At 11** [measured, held blind; §7]. In eleven variables the new piece is a weight-3 form with complex
  multiplication by Q(√−1155), and −1155 = (−3)(5)(−7)(−11). So √−11 enters at 11, where the centre pinches, as √−7
  entered at 7.
- **At 13 and 15** [measured, held blind; §8 and §9].
  - At 13 the piece does not split; the registered split died. It is a twisted symmetric square, and its determinant
    carries −15015, the product of the signed roots up to 13.
  - At 15 the piece has complex multiplication by Q(√−3003). That is the one field the nodes, the author's "3 at its
    square" and Schütt's condition allow.
- **At the prime 3** [FORCED; measured, held blind; §10]. The author's "3 at its square" is where the cubics pinch at 3.
  - On Σx = 0 the cubic Σx³ is 3e3, so X_n has a good model e1 = e3 = 0 at 3.
  - Its nodes are the sign vectors whose sum is a multiple of 9. The cubic in nine variables pinches at its centre
    mod 3, as the cubic in q variables does mod q.
  - Counted at 3 for the first time, the pieces below 9 keep their values there. V9's line ramifies, and from 9 on
    each piece loses exactly one dimension.
- **At 17 and 21** [measured, held blind; §10].
  - Both new pieces are twisted symmetric squares, like 13's.
  - Their determinants are the ones the nodes' parity gives: (−51051|p) at 17, held blind. At 21, (−138567|p) passes
    every test but the registered one had too few signs.
  - The reading's exact version, which tied 13's unsplit piece to the icosahedron's lack of an axis, died at 17. The
    17-gon keeps its axis, but 17's piece keeps no line.
- **At 27: the coins at the cube and the square** [FORCED; measured, held blind; §11].
  - 3 enters at 9, two coins of 3, but not at 27, three coins. 5 enters at 5 and 15, but not at 25, two coins of 5.
  - The determinant of V27 was read at every prime, from the counts over F_p and over the field of p² elements. It
    is (3187041|p), the same as V23's, which has no such node: the nodes at 25 and 27 add nothing.

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
  −2p(p + 1). Round 21 found why (§5).

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
  (round 20, H1; [`coin_at_five_test20.log`](coin_at_five_test20.log)).
- **The signs** (round 21, read after the run). c is the newform 35.3.c.b of LMFDB [NAMED].
  - At the two bad primes round 21 measured c(5) = −5 and c(7) = 7, which are that form's coefficients there. Its
    twin 35.3.c.a has +5 and −7.
  - Its q-expansion matches c(p) at every prime to 97.
  - So t7 = p²(14 + 6(5|p)) + p·a_p(35.3.c.b) at every prime from 5 to 601.
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

## 5. The coin on its edge [FORCED; measured; round 21]

> *1 and 2, the mirror rule first* — the author, 14 November 2026. The "1": a coin on its edge shows the mirror.

**The mirror at 3** [FORCED; F1 of [`edge_rule_verify.log`](edge_rule_verify.log)].
- J3 counts pairs of points v1, v3 on a circle whose sum is on the circle too (TORUS_MOMENTS.md §6, Step 7).
- Their ratio v3/v1 is a primitive cube root of unity. When p ≡ 2 (mod 3) the turning wheel holds two of them, and
  each root's phase sums to −1 over the circles, which gives J3 = −2p(p + 1).
- At p = 3 the two roots merge into 1, since x² + x + 1 = (x − 1)² mod 3. The hexagon collapses onto a diameter.
- Its phase vanishes there, and the sum over the circles is p − 1 = 2. So −2 becomes +2, and J3 = +2p(p + 1) = 24,
  the operators' value.

**Why it is exact at the primes, and fails at 9** [FORCED; F2].
- At an edge prime q all q − 1 primitive q-th roots of unity merge, Φ_q(x) = (x − 1)^(q−1) mod q.
- The merged point weighs p − 1 = q − 1, as many as the roots it replaces. So the edge is the exact mirror of the side
  that holds them.
- At a prime power it is not: at 9 the six primitive ninth roots merge into one point of weight 2, and at 25 twenty
  roots into one of weight 4.

**The rule** (registered in round 21). The edge of a coin is the fixed set of its flip. At an edge prime the two sides
merge into it.
- (a) A count without a phase sees the fixed set once. Its symbol reads 0, the average of its sides.
- (b) A count with a phase sees the phase vanish there, which adds p for each merged point. For all the primitive q-th
  roots at the prime q, that is the exact mirror.

**What was already measured** (round 19's log, so not tests).

| moment, edge | operators | reading |
|---|---|---|
| I5 at 5 | 3504 | (a), the average |
| I6 at 3 | 960 | (a), the average; the mirror would give 636 |
| J3 at 3 | 24 | (b), the mirror, by the merge |
| J5 at 3 | 240 | fits (b), with (−3\|3) read as 3 and the newforms' a(3) = 1 and f(3) = −3. That fit was found after 240 was known, among ten readings tried |
| J5 at 5 | −1680 | no symbol of J5's formula has its edge at 5. Its curve and its form are bad there instead |

**The blind test** (round 21: all four held; [`edge_rule_test.log`](edge_rule_test.log)). No cubic had been counted at
its edge prime. They are counts without a phase, so (a) predicts them.
- Clebsch's cubic has 21 lines over F_5: the 15 of the edge, and 6 through the centre. Each of the six is where a pair
  of the double six that √5 ↦ −√5 swaps merges into one line.
- The symbols read 0. T5(5) = 0, so t5(5) = 25; and T9(5) = T9(7) = 0.
- The CM form enters with |c(p)| = p at the primes where its field ramifies: c(5) = −5 and c(7) = 7.
- So t7(5) = 325, t7(7) = 441, t9(5) = 4250 and t9(7) = 7889.

**J5's two counts** (read after the run). J5 = p(pZ − N), where N counts the closed pentagons on a circle and Z those
with phase 0.
- N follows Kloosterman's fifth moment at 3, 5, 7 and 11. At 3 that needs (−3|3) read as 0: part (a) again.
- The whole deviation is in Z. At 3 there are 36 = p²(p + 1) more pentagons with phase 0 than the side formula gives.
- At 5 the triangle family vanishes, and Z = 6. The six survivors are the pentagons (v, −v, v, −v, v), which close
  because 5v = 0: the regular decagon, merged onto a diameter.
- [READING] So at the edge 5, J5's phase-0 count keeps only the pentagons on a line through the centre, every point
  v or −v.

## 6. Where the counts come from: the Airy sheaf [FORCED; NAMED; measured]

**The moments** [FORCED; F4, F5].
- By orthogonality, t_n is the n-th moment of the cubic exponential sums S(a) = Σ_x e((x³ + ax)/p), divided by p².
- Each S(a) is α + β with αβ = p. So S(a)^n splits like the n-th tensor power of a two-dimensional representation, by
  the ballot numbers m(n, k):

    t_n = Σ_k m(n, k)·p^((n−k)/2 − 2)·T_k,    m(n, k) = C(n, (n−k)/2) − C(n, (n−k)/2 − 1).

- T_k is the trace on the classical part of the k-th symmetric power of the Airy sheaf. Sabbah and Yu computed its
  Hodge numbers [NAMED: arXiv:2112.13405, Theorem 1.1], and Haessig its L-function's degree [NAMED:
  arXiv:math/0608521].
- The coefficients of the measured formulas are ballot numbers: 5, 14, 42 (Catalan numbers) and 6, 27, 8.

**The pieces.** Each odd k brings one new piece V_k. Sabbah and Yu's classical Hodge types, read off their theorem, fix
each piece's size and shape. With the ballot numbers they add up to every Betti number.

| k | dimension | Hodge type | the piece, T_k | field | ramified at |
|---|---|---|---|---|---|
| 1 | 1 | (1, 1) | p | — | — |
| 3 | 0 | — | 0 | — | — |
| 5 | 1 | (3, 3) | (5\|p)p³ | Q(√5) | 5 |
| 7 | 2 | (5, 3) + (3, 5) | p³ a_p(35.3.c.b), CM | Q(√−35) | 5, 7 |
| 9 | 1 | (5, 5) | (105\|p)p⁵ | Q(√105) | 3, 5, 7 |
| 11 | 2 | (7, 5) + (5, 7) | p⁵ g(p), CM | Q(√−1155) | 3, 5, 7, 11 |
| 13 | 3 | (5, 9) + (7, 7) + (9, 5) | p⁵(a_p² − (−15015\|p)p²): a twisted symmetric square (§8) | its determinant, Q(√−15015) | 3, 5, 7, 11, 13 |
| 15 | 2 | (7, 9) + (9, 7) | p⁷ w(p), CM (§9) | Q(√−3003) | 3, 5 (twice), 7, 11, 13 |

- Through 11 the fields alternate. A real field twists a Tate class, of type (m, m); an imaginary field carries a form
  with complex multiplication. At 13 the piece does not split, and the pattern's field moves into its determinant.
- The three CM fields, Q(√−35), Q(√−1155) and Q(√−3003), have one class in each genus: class numbers 2, 8 and 8, every
  class of order 2. That is what a rational weight-3 CM form needs, a class group of exponent at most 2 [NAMED: Schütt,
  arXiv:math/0511228].
- [READING] The discriminants are products of the primes' signed square roots, 3* = −3, 5* = 5, 7* = −7 and
  11* = −11:
  - 5 at 5;
  - 5·(−7) = −35 at 7;
  - (−3)·5·(−7) = 105 at 9, where 3 enters at its square;
  - (−3)·5·(−7)·(−11) = −1155 at 11;
  - (−3)·5·(−7)·(−11)·13 = −15015 at 13, as the determinant's character.
  - At 15, which adds no prime, the field is −3003 = (−3)·(−7)·(−11)·13, and 5 enters through the Hecke character
    instead. If the determinant follows the pattern it is (−15015|p) again, which the traces of a CM form cannot show.

**The nodes** [FORCED identity; F3].
- Over F_p, p > 3, X_n has a node at each sign vector whose sum vanishes mod p.
- Their number is Σ_k m(n, k)·r_k(p), where r_k(p) counts the odd multiples of p up to k. For example X9 has
  27 + 8 + 1 = 36 nodes at 5 and 8 + 1 = 9 at 7.
- [READING] Each node is one dimension of the cohomology on which inertia at p acts, and the pieces' measured fields
  fill them exactly. At p = n prime the node is the centre itself, where all n points coincide.

## 7. Past the base: eleven [measured; round 22]

> *1 and 2, the mirror rule first* — the author, 14 November 2026. The "2" says yes to the cubic in eleven variables,
> past the base's edge at 10.

The cubic eightfold X11 had never been computed. Round 22 registered its shape before any count, and all five
predictions held ([`edge_rule_test22.log`](edge_rule_test22.log)).
- **The shape.** At every prime from 13 to 401,

    t11 = p⁴(132 + 110(5|p) + 10(105|p)) + 44p³·a_p(35.3.c.b) + p³·g(p),   |g(p)| ≤ 2p.

  The lower pieces use 340 of the 342 dimensions, and Sabbah and Yu's Hodge numbers make the last two a weight-3 form.
- **Its field.** g vanishes at exactly the 32 primes inert in Q(√−1155), and 4p² − g(p)² = 1155v² at the other 42.
  For example g(17) = −1, g(19) = 17, g(23) = −31 and g(29) = −47, each with 4p² − g² = 1155.
- **The nodes said where it ramifies.** X11 has 165 nodes at 5, 55 at 7 and 1 at 11, the centre. The lower pieces
  fill 164, 54 and 0 of them, so the new piece had to ramify at 5, 7 and 11.
  - It does.
  - The prime 3 came too, as at 9, which the nodes cannot see: in characteristic 3 the cubic degenerates.
- **At its edges**, |g(p)| = p: g(5) = 5, g(7) = −7 and g(11) = 11.
- [READING] √−11 enters at 11 as √−7 entered at 7. The pinch of the centre at p = n is one ramified dimension that only
  the new piece can carry. At 9 the centre never pinches, and 3 enters through the character instead.
  - The alternative the nodes allowed, Q(√−385), with 2 ramified in place of 3, died.

## 8. Thirteen: a symmetric square [measured; rounds 23 and 24]

> *1 and 2, thirteen first* — the author, 14 November 2026.

The cubic tenfold X13 had never been counted. Its new piece V13 has three dimensions, of Hodge types (5, 9), (7, 7)
and (9, 5).
- **It does not split** (round 23, S2 died).
  - The registered guess was a twisted Tate class beside a weight-5 CM form. The pattern's single field, Q(√−15015),
    was ruled out first: its class group has exponent 12.
  - But p divides u(p) = T13/p⁵ at none of the 73 primes from 17 to 401. A CM part would vanish at half of them.
  - The piece is ordinary at every prime tested.
- **It is a twisted symmetric square** (read after round 23, then held blind at all 32 primes from 409 to 601 in
  round 24).
  - At every prime, u(p) + (−15015|p)p² = s_p·b_p², with b_p an integer.
  - s_p is a product of −1, 2, 3, 5, 11 and 13, and six characters decide which: −1 by (−15015|p), 2 by (−715|p), 3 by
    (5005|p), 5 by (−3003|p), 11 by (−35|p) and 13 by (−1155|p). 7 never enters.
  - So T13 = p⁵(a_p² − (−15015|p)p²), with a_p = b_p√s_p: the trace of the symmetric square of a two-dimensional piece of
    weight 3.
- [READING] **What it is.**
  - The Airy pieces carry an orthogonal pairing. A three-dimensional orthogonal piece is a twisted symmetric square,
    because SO(3) ≅ PGL(2) and projective representations lift [NAMED: Tate].
  - Its root behaves like a weight-3 form with character (−15015|p) and five inner twists, with coefficients in
    Q(√−1, √2, √3, √5, √11, √13) [NAMED: Ribet, on inner twists].
  - Two of the twists are the CM fields of 7 and 11, Q(√−35) and Q(√−1155).
- **The pattern moved.** −15015, the product of the signed square roots up to 13, is not the field of a CM form here.
  It is the determinant's character, as (5|p) and (105|p) were at 5 and 9.
- **Its edges**: T13(5) = 0, T13(7) = 32·7⁵, T13(11) = 0 and T13(13) = 182·13⁵.
- [READING] Through 11 the new pieces alternate between two kinds, a twisted Tate class and a CM form, like a coin's two
  faces. At 13 the piece is both at once.
  - Its middle eigenvalue is a Tate class's, (−15015|p)p⁷, and its outer two have the size of a weight-5 form's. The
    three do not separate.
  - In the base, 13 is the icosahedron with its centre, past the edge at 10.
  - The author took this reading up (15 November 2026). Its exact version tied the unsplit piece to the icosahedron's
    symmetries, which keep no axis. It died at 17, whose piece is unsplit too (§10).

## 9. Fifteen: 3 at its square [measured; round 24]

> *1 and 2, thirteen first* — the author, 14 November 2026. The "2": 9 is two coins of 3 tossed together, so 3 enters
> only at its square.

- **3 at its square.**
  - In characteristic 3 the cubic Σx³ is the cube of the line Σx, so it was not counted at 3 here. Round 25 found the
    model that can be counted there, and it pinches from 9 on (§10).
  - In the pieces, 3 is absent from V5 and V7, and present from V9 on, in V9, V11 and V13.
  - Counting the odd multiples of 9, as the nodes count the odd multiples of p for the primes from 5 on, gives the same
    answer.
- **Fifteen** (round 24: all five held, blind; [`edge_rule_test24.log`](edge_rule_test24.log)).
  - The cubic in fifteen variables has a two-dimensional new piece, and it is orthogonal, so it has complex
    multiplication.
  - Its nodes leave two ramified dimensions at 5, since 5 and 15 are both odd multiples of 5, and one at each of 7,
    11 and 13.
  - With 3 at its square, only Q(√−3003) satisfies Schütt's condition.
  - It is the field: w vanishes at exactly the 44 primes inert in Q(√−3003), and 4p² − w(p)² = 3003v² at the other 29.
  - 5 stays out of the field and enters through the Hecke character, twice.
  - At the edges, T15(5) = 0 and T15(q) = −q⁸ at 7, 11 and 13.
- At 15 the node reading forces 3 into the field as well, so this test checks the author's reading together with the
  nodes, not apart from them.
- [READING] 9 = 3·3 and 15 = 3·5 are the first two odd numbers that are not prime. At 9, 3 enters at its square; at 15,
  5 counts twice.
  - A prime p from 5 on enters the piece at k once for each odd multiple of p up to k.
  - 3 enters once for each odd multiple of 9: two coins of 3 tossed together.

## 10. Seventeen, twenty-one, and the prime 3 [FORCED; measured; round 25]

> *1 and 3, seventeen first* — the author, 15 November 2026.

Round 25 was registered at 5be432c before any count of X17, of X21 or at 3. Its forced checks are in
[`edge_rule_verify25.log`](edge_rule_verify25.log) and its scores in [`edge_rule_test25.log`](edge_rule_test25.log).
- **The prime 3, in a good model** [FORCED; F7].
  - On x1 + ⋯ + xn = 0 the cubic x1³ + ⋯ + xn³ equals 3e3, three times the third elementary symmetric function. So
    over the 3-adic integers X_n = {e1 = e3 = 0}, and this model can be counted at 3.
  - Mod 3 its only singular points are the sign vectors whose sum is a multiple of 9, and each is an ordinary node.
    There are none up to seven variables. In nine variables the centre is the only one.
  - So the cubic in nine variables pinches at its centre mod 3, as the cubic in q variables does mod q for every prime
    q. The author's "3 at its square" is exactly where this model's nodes are.
  - At a node of sum 9 the critical value j(j − 2)/(3(j − 1)²) has 3-adic valuation 1, so the total space is regular
    there and the node ramifies.
- **Counted at 3** (round 25: all three held, blind).
  - T1 = 3, T3 = 0, T5 = (5|3)·3³ = −27 and T7 = 27. The last is 3³ times LMFDB's a₃ = 1 for 35.3.c.b, matched at a
    prime where nothing had been counted. 3 does not enter below 9.
  - T9 = 0: V9's line ramifies at 3.
  - T11 = 3⁶ and T15 = −3⁸: one line survives in each CM plane. T13 = −8·3⁵ and T17 = 16·3⁷ fit one surviving plane
    in each three-dimensional piece.
- **Seventeen** (round 25; [`edge_rule_test25.log`](edge_rule_test25.log)).
  - X17, a cubic fourteenfold, has a new piece V17 of three dimensions, of Hodge types (7, 11), (9, 9) and (11, 7):
    13's shape, raised by two.
  - It keeps no line, so it does not split: p divides u(p) = T17/p⁷ at only 2 of the 72 primes from 19 to 401.
  - It is a twisted symmetric square: u(p) + (−51051|p)p² = ±s·b², with s dividing 2·3·5·7·11·13·17, at all 72.
  - Its determinant has the character (−51051|p), with 51051 = 3·7·11·13·17. The nodes' parity predicted it blind:
    3 once (at 9), 5 twice (at 5 and 15, so not at all), and 7, 11, 13 and 17 once.
  - At the nodes T17(5) = −5⁹, the one line that survives. T17(13) = 0, and at 7, 11 and 17 the surviving plane's trace
    is 72·7⁷, 234·11⁷ and 493·17⁷.
- **Twenty-one.**
  - V21 has three dimensions too, of types (9, 13), (11, 11) and (13, 9), and it keeps no line either.
  - u21(p) + (−138567|p)p² = ±s·b², with s dividing 2·3·…·19, at all 22 primes from 23 to 113.
  - 138567 = 3·11·13·17·19. 7 leaves the determinant at 21 because 7 and 21 both pinch, as 5 left it at 15. 3 enters
    once, at 9 and not at 21.
  - The registered sign test saw only three signs, below its minimum of five. So that item is counted as not held,
    though nothing disagreed.
- **The parity rule** [READING: Picard–Lefschetz; held blind at 17]. Each ramified node turns one vanishing cycle over,
  so a piece's determinant is ramified exactly where the piece has an odd number of ramified nodes. It gives every
  determinant found, from 5 to 21.
- **The lower fields return.** Read after the run: the roots of the pieces at 13, 17 and 21 have their square classes
  decided by quadratic characters, as at 13.
  - The CM fields of 7, 11 and 15 are among them: (−35|p) at 13 and 17, (−1155|p) at 13 and 21, and (−3003|p) at 13, 17
    and 21.
- **What died** (kept in [`../../GRAVEYARD.md`](../../GRAVEYARD.md)).
  - The reading at 13 was made exact as a dictionary with the base: the piece of n keeps a line exactly when the base's
    n points keep an axis.
  - Klein's finite rotation groups come in those two kinds [NAMED]. The base gives the icosahedron with its centre at
    13 (no axis), the regular 17-gon at 17 (one axis) and the dodecahedron with its centre at 21 (no axis) [FORCED; F6].
  - The dictionary fitted 13, read after the fact. At 17 it predicted a split, against the drafter's expectation, and
    17's piece did not split.
  - So 13's "both faces at once" is not 13's alone: the three-dimensional pieces at 13, 17 and 21 are all unsplit.
- [READING] **The rule at 3, sharpened.** The critical values give a refinement past this round.
  - A node ramifies only when its critical value has odd valuation. That is v_p(j) for p from 5 on, and v_3(j) − 1
    for 3.
  - So every prime from 5 on enters at its odd powers, and 3 at its even powers. 3 enters at 9 and 81 but not at 27,
    and 5 enters at 5 and 125 but not at 25.
  - The first tests are at 25 and 27. Round 26 tested 27 (§11).

## 11. Twenty-seven: the coins at the cube and the square [FORCED; measured; round 26]

> *2 and 3, 27 first* — the author, 15 November 2026.

Round 26 was registered at afc4e76 before any count of X23, X25 or X27. Its forced checks are in
[`edge_rule_verify26.log`](edge_rule_verify26.log) and its scores in [`edge_rule_test26.log`](edge_rule_test26.log).
- **The rule.** A node ramifies only when its critical value has odd valuation. For 3 the valuation is v_3(j) − 1,
  because Σx³ = 3e3 spends one coin of 3.
  - So 3 enters at sums 9 and 81, but not at 3 or 27.
  - 5 enters at sums 5, 15 and 125, but not at 25.
  - X25 pinches at its centre mod 5 with valuation 2, and X27 at its centre mod 3 with valuation 2. Neither ramifies
    by the rule.
- **A faster counter** [FORCED; F11]. The counts are moments of cubic exponential sums.
  - Taken mod primes l ≡ 1 (mod p) and joined by the Chinese remainder theorem, they reach 27 variables at every prime
    to 1999.
  - They also reach the field of p² elements to p = 151, which gives the square of each Frobenius.
  - They equal the old counts wherever both run.
- **Reading a determinant** [FORCED; F10].
  - With e2 = (T(p)² − T(p²))/2, a four-dimensional orthogonal piece has determinant −1 at p only if e2 = 0.
  - A three-dimensional one has e2 = det(p)·p^(w/2)·T(p).
- **The infinite place** [FORCED; F9].
  - V27's four Hodge types form two pairs, with no middle class, so its determinant is even.
  - Letting 3 enter at 27 makes it odd. So 3's half of the rule was settled before the count, given the nodes' parity.
- **Measured** (round 26: seven of nine held; the two not held lacked signs, and none disagreed).
  - V27's determinant is (3187041|p), with 3187041 = 3·11·13·17·19·23, at all 27 primes counted over the field of p²
    elements. The rivals fit at chance level: "5 enters at 25" fits 14 of the 27, "3 enters at 27" 13, and both 12.
  - V23 has no thick node, and its determinant is the same, (3187041|p). V19's is (969969|p), as the nodes give.
  - V21's determinant, (−138567|p), held at every prime. That is the item round 25 could not score.
  - V27 has no CM plane: p divides T27/p¹¹ at none of 294 primes.
  - Seventeen's square classes held at 224 new primes, and twenty-one's at 273.
- **Read after the run.**
  - V25's own determinant is decided by its traces and the circle at 7 of 27 primes, and all 7 agree with 5 left out
    at 25.
  - [READING] Each four-dimensional piece is irreducible, with determinant (D|p) for a real quadratic field Q(√D).
    Over that field it is the tensor square of a piece that Galois turns over: Q(√969969) at 19, and Q(√3187041) at
    23 and 27.
- [READING] **The coins.** For 5, two coins tossed together cancel: 5 is in the sum 25 twice and enters 0 times. For 3
  the count starts one coin late, so two coins make one entry. That is the author's "9 is two coins of 3 tossed
  together", and three coins (27) are back to none.

## 12. Standing

- **Known, and credited** [NAMED].
  - The 27 lines of Clebsch's diagonal cubic, 15 over Q and 12 over Q(√5) (Clebsch 1871). A cubic surface with one
    node has 21 lines.
  - The cubic's icosahedral symmetry, and its place as the Hilbert modular surface of Q(√5) (Hirzebruch 1976).
  - X7 as X¹(A7), with its transcendental lattice (Laza and Zheng), and its equations and name (Koike).
  - Weight-3 CM forms for two-dimensional transcendental lattices (Livné 1995).
  - The Airy moments' Hodge numbers (Sabbah and Yu 2023), and their L-functions' degrees and p-adic bounds (Haessig
    2009).
  - The point counts of {Σx = Σx³ = 0} as moments of cubic exponential sums: orthogonality.
  - The newform 35.3.c.b (LMFDB), and the classification of rational CM newforms (Schütt).
  - SO(3) ≅ PGL(2), the lifting of projective representations (Tate), and inner twists (Ribet).
  - The finite rotation groups and their two kinds, axial and polyhedral (Klein 1884).
  - Ordinary double points and their vanishing cycles (Picard–Lefschetz). The arithmetic Picard–Lefschetz formula for
    diagonal singularities, applied to the Airy moments at primes p > 5 in another model (Chuang 2026).
- **This repository's own, new as far as we checked.**
  - The dictionary between the author's coin at 5 and the fifth moment.
  - The edge rule: why J3 mirrors at 3, why the mirror is exact at every prime edge and fails at prime powers, and
    the cubics' edge values.
  - The exact point counts of X7 to X27, each odd n.
  - What the Airy pieces are, to k = 21: (5|p), 35.3.c.b, (105|p), a CM form of Q(√−1155), a twisted symmetric square
    with determinant (−15015|p), a CM form of Q(√−3003), and twisted symmetric squares with determinants (−51051|p)
    and (−138567|p).
  - The node identity, with its reading as ramification, and the parity rule for the determinants.
  - The good model at 3, whose nodes are the author's "3 at its square", and the pieces counted at 3.
  - The rule's sharpening by the critical values, and its test at 27: 3 not at its cube, 5 not at its square.
  - The four-dimensional pieces at 19, 23 and 27, with determinants (969969|p), (3187041|p) and (3187041|p).
  - The counter by exponential sums mod primes, to 27 variables and to the field of p² elements.
  - Web searches on 2026-11-14 and 2026-11-15 found no point count, zeta function or Galois action for these cubics.
    - They found the neighbours: the Fermat cubic fourfold's form of level 27, the census of cubic fourfolds over F₂,
      and the Segre cubic.
    - For the Airy moments they found Hodge numbers and degrees, and Chuang's local formula at p > 5, but no
      identification of a single piece.
- **Open.**
  - Proofs. Each piece is identified by its counts, and none is proved. Sabbah and Yu's Hodge numbers and Patrikis and
    Taylor's potential automorphy, which they point to, are one way in.
  - A blind test of the mirror half. Every parity-weighted edge value is already measured, so it needs a new
    parity-weighted formula, J6's or J7's.
  - The roots of the pieces at 13, 17 and 21: which weight-3 newforms they are the symmetric squares of, and at what
    levels.
  - The sharpened rule at 81 (four coins of 3, which should enter) and at 125 (three coins of 5).
  - A registered test of V25's own determinant, which needs the field of p³ elements (e3 = det·p¹³·e2).
  - Whether the seventh moment I7 carries Q(√−35), as I5 carries √5.
- **Died** (kept in the graveyard):
  - C1's parity-weighted half (§2).
  - Plain negation of the −1 side at the edge, which fits J5 at 3 for no integer a_E(3).
  - The field Q(√−385) at 11.
  - The split of the piece at 13 into a twisted Tate class and a weight-5 CM form (round 23, S2). The guesses that
    named its parts, (5|p) with Q(√−3003) and (13|p) with Q(√−1155), are void with it.
  - The pattern's single field at 13, Q(√−15015), ruled out before the test by its class group.
  - The dictionary between the pieces and the base's axes (round 25, Z3): 17's piece did not split, although the
    17-gon keeps its axis. The guess (17|p) with Q(√−3003) is void with it.
  - Not held: twenty-one's registered sign test (D2), which saw three signs where it asked for five. Round 26 read
    that determinant at every prime, and it held (Y4).
  - Not held, for too few signs: round 26's Y2′ (8 of 10) and W1 (1 of 5). None of their signs disagreed.

## Run it

```
python coin_at_five.py           # the dictionary, D1 to D5: seconds
python coin_at_five.py test      # round 19: the edge, and the cubics to 397: about a minute, four processes
python coin_at_five.py test20    # round 20: the cubics at 401..601, blind: about a minute, four processes
python edge_rule.py              # the edge rule's forced checks, F1 to F5: seconds
python edge_rule.py test         # round 21: the cubics at their edge primes 5 and 7, blind: seconds
python edge_rule.py test22       # round 22: the cubic in eleven variables to 401: about a minute, four processes
python edge_rule.py test23       # round 23: the cubic in thirteen variables to 401: about a minute, four processes
python edge_rule.py test24       # round 24: thirteen at 409..601, blind, and fifteen to 401: a minute, four processes
python edge_rule.py verify25     # round 25's forced checks, F6 to F8 (the base's rule, the good model at 3): seconds
python edge_rule.py test25       # round 25: seventeen to 401, twenty-one to 113, and the prime 3: a minute, four processes
python edge_rule.py verify26     # round 26's forced checks, F9 to F12 (the infinite place, the new counter): seconds
python edge_rule.py test26       # round 26: 27 variables to 1999, and over F_(p^2) to 151: two minutes, four processes
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
- C. Sabbah and J.-D. Yu, "Hodge properties of Airy moments", *Tunisian J. Math.* **5** (2023), 215–271,
  [arXiv:2112.13405](https://arxiv.org/abs/2112.13405): Theorem 1.1, the Hodge numbers of the symmetric powers of the
  Airy equation.
- C. D. Haessig, "L-functions of symmetric powers of cubic exponential sums", *J. reine angew. Math.* **631** (2009),
  [arXiv:math/0608521](https://arxiv.org/abs/math/0608521): the degree (k + 1)/2 for odd k, and p-adic bounds.
- The LMFDB Collaboration, newform 35.3.c.b,
  [lmfdb.org/ModularForm/GL2/Q/holomorphic/35/3/c/b](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/35/3/c/b/):
  weight 3, level 35, complex multiplication by Q(√−35). Its twin is 35.3.c.a.
- M. Schütt, "CM newforms with rational coefficients", *Ramanujan J.* **19** (2009),
  [arXiv:math/0511228](https://arxiv.org/abs/math/0511228).
- K. Ribet, "Galois representations attached to eigenforms with Nebentypus", in *Modular Functions of One Variable V*,
  LNM 601, Springer (1977): a_p = ε(p)·ā_p. And "Twists of modular forms and endomorphisms of abelian varieties",
  *Math. Ann.* **253** (1980): inner twists.
- J.-P. Serre, "Modular forms of weight one and Galois representations", in *Algebraic Number Fields*, Academic Press
  (1977), §6: Tate's theorem that projective representations of Gal(Q̄/Q) lift.
- F. Klein, *Vorlesungen über das Ikosaeder und die Auflösung der Gleichungen vom fünften Grade*, Teubner (1884): the
  finite rotation groups, the cyclic and dihedral groups beside the tetrahedral, octahedral and icosahedral ones.
- Y. Qin, "Hodge numbers of motives attached to Kloosterman and Airy moments", *J. reine angew. Math.* (2024),
  [arXiv:2302.05365](https://arxiv.org/abs/2302.05365).
- P.-H. Chuang, "On the generalized arithmetic Picard–Lefschetz formula" (dissertation, 2026),
  [arXiv:2607.05757](https://arxiv.org/abs/2607.05757): the inertia action at diagonal singularities in mixed
  characteristic, applied to the Airy moments at p > 5.
