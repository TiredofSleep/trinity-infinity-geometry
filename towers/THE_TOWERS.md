# The Towers

*The base — the integers 0–9 as shapes, and the book's six pictures — is where higher
mathematics starts. Each base shape is the ground floor of a **tower**: a ladder of real
mathematics that climbs from something a child can build to what a graduate student studies. This
page is the map. Every **[FORCED]** floor is checked by [`verify_towers.py`](verify_towers.py); the
theorems at the tops are **[NAMED]** and cited, not reproved. The book's last chapter,
[*Where the towers go*](https://github.com/TiredofSleep/shape-of-understanding/blob/main/the_shape_of_understanding_BOOK.md#chapter-18--where-the-towers-go) (Chapter 18), points up each of these towers for a learner; this page is its detail.*

---

## How to read a tower

- **Ground floor** — the base shape or picture it rises from (in the book, and in
  [`../base/`](../base/README.md)).
- **Floors** — what you meet as you climb, each one a real piece of mathematics.
- **Top** — where the tower reaches in mathematics today, and the course where students meet it.

The base does not prove the towers. It points at them: you stand on the base, and the tower is what
the pointing reaches.

## The map

| the base | points toward |
|---|---|
| fair shapes — 1, 2, 3, 4 | **1** the simplex tower |
| the two-shadow box — the cube, 8, and its dual, the octahedron, 6 | **1** the cube and cross-polytope towers · **3** the Clifford tower |
| the break — 5 | **1** the exceptional shapes · **4** A₅ and the quintic |
| turning — *i* | **2** the number tower |
| the full middle — 0, and the centres of 5, 7, 9 | **4** the symmetry tower · **5** the lattice tower |
| the tetrahedron's 1/3 | **6** the harmonic tower |
| counting versus measuring — √2 | **7** the real-number tower |
| growing — *e* | **8** the growth tower |

---

## 1. The three towers that never end — simplex, cross-polytope, cube

**Ground floor:** 4, 6, 8 — the tetrahedron, the octahedron and the cube, the most symmetric
arrangements of 4, 6 and 8 points.

- **[FORCED]** Each is the three-dimensional floor of a shape that exists in every dimension *n*,
  and each grows by its own law. The **simplex** adds one corner per dimension (*n* + 1), the
  **cross-polytope** adds a pair (2*n* — the points ±eᵢ), and the **cube** doubles (2ⁿ). In three
  dimensions the three laws give 4, 6, 8.
- **[FORCED]** Their faces are counted by binomial coefficients (the simplex's are a row of
  Pascal's triangle), and on every floor the alternating sum of the face counts is 1 − (−1)ⁿ —
  Euler's relation. The cube and the cross-polytope are duals: the corners of one are the faces of
  the other.
- **[FORCED]** These three are the **only** regular shapes that exist in every dimension.
  Three-dimensional space has five regular solids; four-dimensional space has six; from five
  dimensions on there are exactly three — the simplex, the cube and the cross-polytope (Coxeter's
  criterion, checked). [NAMED: Schläfli 1852; Coxeter, *Regular Polytopes*]
- **The break points here too.** [FORCED] The two extra three-dimensional solids, the icosahedron
  and the dodecahedron, are the ones built on five-fold symmetry — the book's "break" at 5. Their
  line climbs one more floor (the 600-cell and the 120-cell, in four dimensions) and then ends.

**Top — where you meet it.** The simplex is where **probability** lives (every probability
distribution on *n* + 1 outcomes is a point of an *n*-simplex) and what **algebraic topology**
builds spaces from (simplicial complexes, homology). The cube is the space of **binary strings** —
Hamming distance, error-correcting codes, Boolean logic. The cross-polytope is the unit ball of the
ℓ¹ norm — **sparsity** and compressed sensing — and its symmetries are the signed permutations,
2ⁿ·*n*! of them (48 in three dimensions, the octahedron's and the cube's).

## 2. The number tower — ℝ → ℂ → ℍ → 𝕆

**Ground floor:** turning — the quarter-turn *i* (Picture 3). The book climbs this tower to ℍ in
§7.1.

- **[FORCED]** Doubling — the Cayley–Dickson construction — climbs 1 → 2 → 4 → 8 → 16, and each
  floor gives something up. ℂ gives up order. ℍ gives up commutativity (*ij* = −*ji*). The
  octonions 𝕆 give up associativity but keep a weaker law ("alternativity"). At 16 the sedenions
  give up division — two non-zero numbers can multiply to zero, for example
  (e₁ + e₁₀)(e₄ − e₁₅) = 0 — and size stops multiplying: |xy| = |x||y| fails.
- The doubling is the base's own: one more imaginary unit is one more yes/no, the lift of Picture 1.

**Top.** [NAMED — Hurwitz 1898] ℝ, ℂ, ℍ and 𝕆 are the only number systems in which size
multiplies: the tower of division ends at 𝕆. Where you meet it: complex analysis; quaternions in
rotation (computer graphics, spacecraft attitude); the octonions behind the exceptional Lie groups
(G₂ is the symmetry group of 𝕆).

## 3. The Clifford tower — the cube's algebra and its eight-step clock

**Ground floor:** the cube — three perpendicular directions generate the Clifford algebra Cl(3),
2³ = 8 pieces graded 1 + 3 + 3 + 1 (see [`P2_clifford_cube_skeleton.md`](P2_clifford_cube_skeleton.md)
and [`THE_TWO_BUILDS.md`](THE_TWO_BUILDS.md)).

- **[FORCED]** Each new perpendicular direction doubles the algebra — Cl(*n*) has 2ⁿ pieces, graded
  by Pascal's row *n* ([`verify_two_builds.py`](verify_two_builds.py)). Its planes square to −1, so
  rotations live inside it, and its first floors are ℂ and ℍ again: the number tower and the
  Clifford tower share a bottom ([`bott_verify.py`](bott_verify.py)).

**Top.** [NAMED — Bott 1959] the Clifford algebras repeat their type every eight steps — see
[`bott_periodicity.md`](bott_periodicity.md), where the mechanism (ℍ ⊗ ℍ ≅ ℝ(4)) is checked. Where
you meet it: spinors and the Dirac equation; K-theory; the topology of spheres.
**[FENCE]** Bott's 8 is a period; the cube's 8 is a count of corners.

## 4. The symmetry tower — from "most symmetric" to groups

**Ground floor:** the rule that realizes 0–9, *the most symmetric arrangement*
([`../base/SEVEN_AND_NINE.md`](../base/SEVEN_AND_NINE.md)) — and the full middle: the centre is the
one point every symmetry keeps fixed.

- **[FORCED]** The rotations of the Platonic solids form groups of 12 (the tetrahedron), 24 (the
  octahedron and the cube) and 60 (the icosahedron and the dodecahedron) — as groups, A₄, S₄ and A₅.
  [NAMED]
- A₄ and S₄ break into smaller pieces: they have normal subgroups, of size 4, and of sizes 4 and 12
  [NAMED]. **[FORCED]** A₅ does not — its conjugacy classes have sizes 1, 12, 12, 15, 20, and no
  union of them with the identity divides 60 — so A₅ is **simple**.
- **[NAMED — Abel–Ruffini; Galois]** Because A₅ is simple, the general equation of degree five has
  no formula in radicals. **The break at 5 in the base is also the break in solving equations.**
- **[FORCED]** Continuous symmetry: every unit quaternion *q* turns space by v ↦ qvq̄; *q* and −*q*
  give the same rotation, and multiplying quaternions composes rotations. The quaternions are the
  double cover of the rotations — SU(2) over SO(3).

**Top.** Lie groups and their representations; Galois theory; symmetry and conservation laws in
physics (Noether).

## 5. The lattice tower — from a centred shape to sphere packing

**Ground floor:** 5, 7, 9 — a shape with its centre filled: an atom with its nearest neighbours in
the diamond, simple cubic and body-centred cubic lattices
([`../base/SEVEN_AND_NINE.md`](../base/SEVEN_AND_NINE.md)).

- **[FORCED]** Balls packed on the cubic lattices fill π/6 ≈ 52.4 % (simple cubic), π√3/8 ≈ 68.0 %
  (body-centred) and π/√18 ≈ 74.0 % (face-centred) of space, with 6, 8 and 12 neighbours touching
  each ball.

**Top.**
- [NAMED — Kepler 1611; Hales 1998, formally verified 2017] no packing of equal balls in three
  dimensions beats 74.0 %.
- **[FORCED]** In eight dimensions the E₈ lattice gives every ball 240 touching neighbours;
  [NAMED — Viazovska 2016; Cohn, Kumar, Miller, Radchenko and Viazovska 2017] E₈ and the Leech
  lattice (24 dimensions) are the densest packings of their dimensions.

Where you meet it: crystallography and solid-state physics; error-correcting codes; number theory
(modular forms). **[FENCE]** E₈'s 8 is a dimension.

## 6. The harmonic tower — from the tetrahedron's 1/3

**Ground floor:** the tetrahedron's number — cos θ = −1/3; half-angle 54.74°, with cos² = 1/3
([`THE_ONE_THIRD_AND_THE_FOLD.md`](THE_ONE_THIRD_AND_THE_FOLD.md)).

- **[FORCED]** 54.74° is the zero of the Legendre polynomial P₂(x) = (3x² − 1)/2 — the "magic
  angle" at which NMR spectroscopy averages directional interactions away. The Legendre
  polynomials are orthogonal; the harmonic polynomials of degree ℓ in three variables number
  2ℓ + 1.

**Top.** Spherical harmonics — the angular shapes of atomic orbitals (s, p, d, f: 1, 3, 5, 7 of
each); representations of the rotation group; harmonic analysis on the sphere.
**[FENCE]** The counts 1, 3, 5, 7 belong to this tower; they are not a reading of the base's odd
numbers.

## 7. The real-number tower — from √2

**Ground floor:** counting versus measuring — the diagonal of the unit square, which no fraction
names (Picture 6; Pythagoras, Chapter 8).

- **[FORCED]** The best fractions for √2 — 1/1, 3/2, 7/5, 17/12, 41/29, 99/70 — each satisfy
  p² − 2q² = ±1 and come within 1/q² of √2, and none is exact.

**Top.** The real numbers as the completion of the fractions (Dedekind, Cantor); continued
fractions and Diophantine approximation; [NAMED — Hermite 1873, Lindemann 1882] *e* and π are
transcendental; measure theory.

## 8. The growth tower — from *e*

**Ground floor:** growth that feeds itself — *e* (Picture 4; Chapter 4).

- **[FORCED]** The exponential of a quarter-turn is a rotation: e^{θJ} is the rotation by θ —
  e^{iθ} written as a matrix. The exponential of any spinning motion (any skew matrix) is a
  rotation.

**Top.** The exponential map from a Lie algebra to its Lie group — how the infinitesimal turns of
towers 3 and 4 become finite ones; differential equations; dynamical systems.

---

## What is and is not claimed

- **Claimed:** each tower is established mathematics; its ground floor is a base shape or picture;
  its [FORCED] floors are checked by computation, and its tops are cited.
- **Not claimed:** that the base *derives* the towers. The integers do not prove Bott's theorem or
  Hurwitz's; they are where a learner can stand to see them. The base points; the towers are what
  it points at.
