# The Integers 0–9 as Shapes

## The geometric realization of the integers — which shape, and by which rule

### Tags: **[FORCED]** follows from the named rule and is checked by a script · **[RULE]** names the rule that picks the shape · **[READING]** an interpretation · **[OPEN]** not settled. Every [FORCED] claim here is in [`verify_integers.py`](verify_integers.py), [`verify_forced_chain.py`](verify_forced_chain.py) or [`verify_one_rule.py`](verify_one_rule.py).

---

## The premise

Read an integer *n* as a configuration of *n* points, and ask what shape the configuration is
forced to take. This is the premise of *The Shape of Understanding* (Chapter 1: "Integers are
shapes").

One thing has to be said first, because the earlier versions of this page blurred it:
**"forced" is always relative to a rule for arranging the points.** Different rules give
different shapes, and beyond four points the natural rules disagree. So each integer below names
its rule.

---

## The ladder, 0–4 — forced by equidistance

**Rule: the points are all the same distance apart** (the book's "fair shapes from same-length
lines").

| n | shape | why |
|---|---|---|
| **0** | **the void** — the empty centre | the centroid of any configuration is the one point nearest to all its points at once [FORCED — for the tetrahedron its total distance to the corners is 6.93, less than a corner's 8.49, and no other point does better] |
| **1** | **point** | the 0-simplex |
| **2** | **segment** | the 1-simplex |
| **3** | **triangle** | the 2-simplex — the last equal-distance shape that stays flat |
| **4** | **tetrahedron** | the 3-simplex — the fourth point is forced up out of the plane |

- **[FORCED]** *n* mutually equidistant points need exactly *n* − 1 dimensions. So in
  three-dimensional space the equidistance rule builds exactly these four shapes and **stops**:
  five equidistant points need a fourth dimension.
- **[FORCED]** Each added point is one in/out choice for every piece already built, so the total
  number of pieces doubles: 2ᴺ. (The book's "the lift is a doubling".)
- **[FORCED]** The tetrahedron's angle: seen from the centre, cos θ = −1/(N−1), which at N = 4 is
  **−1/3** (109.47°); the half-angle is 54.74°, with cos² = **1/3**. The 1/3 is 1/(N−1) at N = 4 —
  the tetrahedron's own number, not a general identity.
- **[FORCED]** A second natural rule agrees on this range: spreading points as evenly as possible
  on a sphere (the Thomson problem) gives the segment (2), the triangle (3) and the tetrahedron (4).
  On 0–4 the realization does not depend on the choice.
- **[READING]** The void as "the fullest point" — nearest to everything by committing to nothing —
  is the book's reading (§1.6b) of the forced fact above.

---

## Beyond 4 — each integer by a named rule

Past the tetrahedron, equidistance runs out of room, and the rules part ways.

| n | shape used | rule | status |
|---|---|---|---|
| **5** | **pentagon** (flat) | regular polygon: the first whose rotation cannot tile — the lattice rotation orders are exactly 1, 2, 3, 4, 6 | [RULE] the book's "break"; [FORCED] that spreading 5 points on a sphere gives a **triangular bipyramid** instead |
| **6** | **octahedron** | points spread evenly on a sphere: the six poles ±x, ±y, ±z | **[FORCED]** by sphere-spreading — the book's "round" |
| **7** | **octahedron + its centre** (= 1 + 6, the centred hexagon) | a centred figure: a shape plus the filled centre | [RULE]; sphere-spreading gives the **pentagonal bipyramid** |
| **8** | **cube** | the perpendicular build: three perpendicular in/out choices, 2³ = 8 corners | **[FORCED]** by the perpendicular build; [FORCED] that sphere-spreading gives the **square antiprism**, not the cube |
| **9** | **3²** (a triangle of side 3 cut into 9 unit triangles; the 3 × 3 grid) | the square of three | [RULE] |

So the shapes in this table come from **more than one rule**:

- 0–4 are forced by equidistance, and sphere-spreading agrees;
- 6 is forced by sphere-spreading;
- 8 is forced by the perpendicular build;
- 5, 7 and 9 are realized by other rules (regular polygon, centred figure, square).

**One rule does realize all ten — see [`SEVEN_AND_NINE.md`](SEVEN_AND_NINE.md).** The book's own
rule, "the most symmetric arrangement" (Ch. 1 §1.1), kept in three-dimensional space with the
points not all on one line, gives a unique shape for every integer from 0 to 9 [FORCED,
exhaustively checked over all symmetry groups]: the void, point, segment, triangle, tetrahedron,
**tetrahedron + centre**, octahedron, **octahedron + centre**, cube, **cube + centre**. It fills
the book's gap: **7 is the octahedron with its centre, 9 the cube with its centre**. At 10 it
leaves this family.

**[OPEN] — the author's call.** The rule agrees with the table above at 0–4 and 6–8. It differs
at **5** (the tetrahedron with its centre, not the flat pentagon — which comes from the
regular-polygon rule and has less symmetry, 20 against 24) and at **9** (the cube with its centre,
not 3²). Which to adopt is the author's decision.

---

## The cube and its two tetrahedra [FORCED]

- The cube's eight corners split into **two regular tetrahedra** (Kepler's *stella octangula*),
  with 8 = 2 × 4.
- The two tetrahedra are swapped by the **central inversion** (x → −x).
- **Each tetrahedron is its own mirror image** — the reflection x ↔ y maps it onto itself — so the
  two are *not* "two chiralities". (Earlier versions said they were; that was wrong.)
- The cube's three perpendicular axes generate the Clifford algebra **Cl(3)**, of dimension
  2³ = 8, graded 1 + 3 + 3 + 1 — see [`../towers/P2_clifford_cube_skeleton.md`](../towers/P2_clifford_cube_skeleton.md)
  and [`../towers/THE_TWO_BUILDS.md`](../towers/THE_TWO_BUILDS.md).
- The cube's two shadows — a square down a face, a hexagon down a body diagonal — are related by
  cos²(1,1,1) = **1/3**, the tetrahedron's number again.

---

## Where each integer points

The base is the ground floor of the towers of higher mathematics — the map is
[`../towers/THE_TOWERS.md`](../towers/THE_TOWERS.md).

| n | shape | points toward |
|---|---|---|
| **0** | the void — the centre | the **symmetry tower**: the centre is the one point every symmetry keeps fixed |
| **1–4** | the simplices | the **simplex tower**: probability, algebraic topology |
| **4** | the tetrahedron's 1/3 | the **harmonic tower**: Legendre polynomials, spherical harmonics |
| **5** | the break (the pentagon) · the tetrahedron with its centre | the **exceptional shapes**, and **A₅ and the unsolvable quintic** · the **lattice tower** (diamond) |
| **6** | the octahedron | the **cross-polytope tower**: sparsity, signed permutations |
| **7** | the octahedron with its centre | the **lattice tower** (simple cubic) |
| **8** | the cube | the **cube tower** (binary strings, codes) · the **Clifford tower**, up to Bott's eight-step clock |
| **9** | the cube with its centre | the **lattice tower** (body-centred cubic), up to sphere packing and E₈ |

The book's other pictures are ground floors too: turning (*i*) → the **number tower**
ℝ → ℂ → ℍ → 𝕆; growing (*e*) → the **growth tower**; counting versus measuring (√2) → the
**real-number tower**.

---

## What earlier versions said, and why it was removed

Kept on record so it is not repeated (the full earlier text is in the archive — see
[`../GRAVEYARD.md`](../GRAVEYARD.md)):

- **[FORCED] on 0 and 5–9** → replaced by named rules; the rules differ.
- **"The two tetrahedra are the two chiralities"** → false: a regular tetrahedron is achiral.
- **"6 is the fusion, with symmetry D₆ ⊃ D₃, D₂"** → the octahedron's symmetry is not D₆ (that is
  the flat hexagon's); the claim mixed the two realizations of 6.
- **"0 and 7 are the two states of one location"**, **"the square (matter) family {1,2,4,5,8} vs
  the hex (flow) family {3,6,7,9}"**, **"5 and 7 are the two lens-centres"**, **the mod-3 roles**,
  **the "inhale / exhale" pulse of 7 → 8 → 9**, **"9 = the last digit before the base-10 reset"** →
  readings carried over from the archived table program, or sortings chosen after the fact; none
  follows from the premise.

---

*Read as configurations of points, the integers 0–4 are forced — the void and the four
simplices, by equal distance. Beyond four the simpler rules part ways, but the book's own rule —
the most symmetric arrangement — carries on alone: it realizes every integer to 9, with 7 the
octahedron and 9 the cube, each with its centre filled, and it leaves that family at 10.*
