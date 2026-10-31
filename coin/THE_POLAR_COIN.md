# The polar's coin — the cube, the octahedron and the round ball

*A page of the coin. Polarity turns a convex shape inside out: corners become faces and faces become
corners. Done twice it changes nothing, so it is a flip, and the base's own solids sit on it. The cube and
the octahedron are its two sides, the tetrahedron is two sides of the same shape, and the round ball is its
edge. What the coin measures, the volume product, is largest on the edge and smallest on the sides.
Everything in the plane and the symmetric case in space is classical. The rest is open, and two recent
claims are named as claims. Every [FORCED] line is checked by
[`verify_polar_coin.py`](verify_polar_coin.py) (26 checks, about forty seconds).*

Tags: **[FORCED]** proved here or computed by the script · **[NAMED]** a classical result, cited ·
**[OPEN]** not settled · **[COIN]** a classified pair: both sides kept, the edge named · **[READING]** an
interpretation.

---

## 1. The coin

Take a convex shape *K* with the origin inside it. Its **polar** is

> *K*° = every point *y* with *x* · *y* ≤ 1 for every *x* in *K*.

- [FORCED] **A face of *K* becomes a corner of *K*°**, and a corner becomes a face. The face of *K* on the
  plane *a* · *x* = 1 gives the corner *a* of *K*°. Corners and faces trade counts, and edges stay:
  - the cube's (8, 12, 6) becomes the octahedron's (6, 12, 8);
  - the icosahedron's (12, 30, 20) becomes the dodecahedron's (20, 30, 12);
  - the tetrahedron's (4, 6, 4) stays as it is.
- [NAMED; FORCED] **Done twice, it changes nothing:** *K*°° = *K* (the bipolar theorem). The script checks
  it on the five regular solids, the regular polygons with 3 to 12 sides, and 80 random shapes.
- [FORCED] **A bigger shape has a smaller polar:** (*tK*)° = *K*°/*t*. The octahedron sits inside the cube,
  and the cube's polar sits inside the octahedron's.

## 2. The base's shapes on the coin

- [FORCED] **The cube and the octahedron are each other's polars**, exactly as the base draws them. The cube
  [−1, 1]³ has polar the octahedron with corners ±*x*, ±*y*, ±*z*, and back.
- [FORCED] **The tetrahedron is two sides of the same shape.** The polar of the cube's even tetrahedron
  (corners whose signs multiply to +1) is exactly its odd tetrahedron, and a quarter turn carries one onto
  the other. These are the cube's two tetrahedra, the half-spinors of
  [`THE_SPINOR_FLOOR.md`](../towers/THE_SPINOR_FLOOR.md).
- [FORCED] **The icosahedron and the dodecahedron** are a pair of sides, the next pair past the base (12
  and 20).

**[COIN] What counts as "the same" decides the edge.** Only the round ball is its own polar exactly
[NAMED]. Allow a turn and a change of size, and the edge widens. The regular shapes then fall like this:

| where | on the edge (its own polar, turned) | on the sides (a pair) |
|---|---|---|
| the plane | **every** regular polygon [FORCED, *n* = 3 … 12: the *n*-gon's polar is the *n*-gon turned by π/*n*] | none |
| space | the tetrahedron | cube ↔ octahedron; dodecahedron ↔ icosahedron |
| four dimensions | the simplex; the 24-cell | tesseract ↔ 16-cell; 120-cell ↔ 600-cell |
| five and up | the simplex | cube ↔ cross-polytope |

[FORCED for the plane, space, four and five dimensions; NAMED: the duality of the regular polytopes,
Schläfli and Coxeter.] So polarity sends the base's three solid towers, the simplex, the cross-polytope and
the cube, into one coin in every dimension. The simplex tower stands on the edge, and the other two are its
sides.

## 3. What the coin measures

The **volume product** *P*(*K*) = |*K*| · |*K*°| is the same on both sides, because *K*°° = *K*. A linear map
does not change it either [FORCED: 12 random maps]. So it measures shape alone, not size or slant.

| shape | *P* | |
|---|---|---|
| triangle, measured from its centre | 27/4 = 6.75 | [FORCED] every triangle gives exactly this |
| square | 8 | |
| regular hexagon | 9 | |
| regular *n*-gon | *n*² sin²(π/*n*) | [FORCED] rising with *n* |
| disk | π² ≈ 9.87 | [FORCED: the 1000-gon is just below] |
| tetrahedron, from its centre | 64/9 ≈ 7.11 | [FORCED] every tetrahedron gives exactly this |
| cube = octahedron | 32/3 ≈ 10.67 | |
| icosahedron = dodecahedron | ≈ 14.08 | |
| round ball | 16π²/9 ≈ 17.55 | [FORCED: a 642-corner sphere gives 17.48] |

Rounder is larger.

## 4. Where the extremes sit

- **The maximum is on the edge** [NAMED: Blaschke 1917; Santaló 1949; equality Saint-Raymond 1981, Petty
  1985]. With the origin at the right centre (the Santaló point, which is the ordinary centre for a
  symmetric shape), *P*(*K*) ≤ *P*(ball). Equality holds only for ellipsoids, the ball under a linear map.
- **The minimum for symmetric shapes is on the sides.**
  - [NAMED] Mahler conjectured in 1939 that *P*(*K*) ≥ 4ⁿ/*n*! for every symmetric *K* in *n* dimensions.
    That is the cube's value, and so its polar's. Mahler proved the plane (1939). Iriyeh and Shibata proved
    space (2020), with equality only for the cube and the octahedron under a linear map.
  - [FORCED, measured] Consistent with these theorems, though no proof: 300 random symmetric polygons
    never go below 8; 300 random symmetric solids never go below 32/3; 100 small symmetric nudges of the cube
    all raise *P*.
  - [FORCED] From four dimensions on, more pairs tie at the bottom: the Hanner bodies, built from segments
    by products and joins. In four dimensions the octahedral prism and the cubic bipyramid are each other's
    polars, and with the tesseract and the 16-cell all four have *P* = 32/3 = 4⁴/4!.
  - [OPEN] Four dimensions and up. OpenAI's 2026 release claims every dimension, with equality exactly for
    the Hanner bodies (family 087; Lean-checked by its own account, not refereed).
- **The minimum for all shapes sits on two sides of the same shape.**
  - [NAMED] For a shape that need not be symmetric, put the origin at its best point. The conjectured bound
    is *P* ≥ (*n* + 1)ⁿ⁺¹/(*n*!)², the simplex's value. Mahler proved the plane, where the triangle is the
    minimum.
  - [FORCED] The tetrahedron's centre is its best origin (50 off-centre origins all give more), and there
    every tetrahedron gives 64/9. Random shapes with the origin optimized stay above 27/4 in the plane (60
    tried) and above 64/9 in space (40).
  - [OPEN] Space. Chen, Li, Xi and Xu claim it (preprint, 2026), and OpenAI's family 087 claims every
    dimension.

**[COIN] The classification.** In space:
- the maximum sits on the edge, the round ball;
- the symmetric minimum sits on the two sides, the cube and the octahedron (the base's 8 and 6);
- the general minimum sits on two sides of the same shape, the cube's two tetrahedra (the base's 4, twice).

In the plane, the symmetric minimum is the square, which is its own polar turned. So the coin's verdict at
the bottom moves from the edge to the sides between the plane and space.

## 5. Where you meet it

- **Norms.** The cube is the unit ball of the largest-coordinate norm, and the octahedron that of the
  sum-of-coordinates norm. Polarity is the duality of norms, the one behind |*x* · *y*| ≤ (Σ|*xᵢ*|) ·
  max|*yᵢ*| [NAMED].
- **Crystals.** A lattice's dual, the reciprocal lattice of X-ray diffraction, is the same idea for lattices.
  The face-centred cubic lattice and the body-centred cubic lattice are each other's duals, and that pair
  decides the energy contest in
  [`../base/SYMMETRY_AND_ENERGY.md`](../base/SYMMETRY_AND_ENERGY.md).
- **Counting lattice points.** Mahler introduced the product in 1939 to relate the lattice points of *K*
  and of *K*° [NAMED].

## What this is, and is not

- **Is:** classical in the plane and for symmetric shapes in space: the polar, the duality of the regular
  polytopes, Blaschke–Santaló, Mahler 1939 and Iriyeh–Shibata 2020. It is arranged as a coin for teaching,
  and every number is computed by the script.
- **Is not:** new, or settled from four dimensions on, or for general shapes in space. The general case in
  space is a 2026 preprint. The every-dimension claim is OpenAI's, in its repository
  [`openai/math`](https://github.com/openai/math), family 087. Its Lean statement leaves out the functional
  inequalities, and whether a Lean statement says what its paper says has to be checked by a person.
- **[READING]** The project's coin keeps both faces and names the edge. Here that habit lands on a
  classification the field already holds, and on the base's own shapes: the ball at the top, the
  cube–octahedron pair at the symmetric bottom, the tetrahedron at the bottom of everything.

## Sources

- R. T. Rockafellar, *Convex Analysis*, Princeton (1970): the polar and the bipolar theorem.
- H. S. M. Coxeter, *Regular Polytopes*, 3rd ed., Dover (1973): the duality of the regular polytopes.
- The upper bound and its equality case:
  - W. Blaschke, *Leipziger Berichte* **69** (1917): the plane and space.
  - L. A. Santaló, "Un invariante afin para los cuerpos convexos del espacio de *n* dimensiones",
    *Portugaliae Math.* **8** (1949): every dimension.
  - J. Saint-Raymond, "Sur le volume des corps convexes symétriques", *Séminaire d'Initiation à l'Analyse*
    (1980–81).
  - C. M. Petty, "Affine isoperimetric problems", *Ann. New York Acad. Sci.* **440** (1985).
- K. Mahler, "Ein Minimalproblem für konvexe Polygone", *Mathematica (Zutphen)* B **7** (1939) 118–127,
  and "Ein Übertragungsprinzip für konvexe Körper", *Časopis Pěst. Mat. Fys.* **68** (1939) 93–102.
- H. Iriyeh and M. Shibata, "Symmetric Mahler's conjecture for the volume product in the 3-dimensional
  case", *Duke Math. J.* **169** (2020) 1077–1134.
- O. Hanner, *Math. Scand.* **4** (1956) 65–87; A. B. Hansen and Å. Lima, *Acta Math.* **146** (1981) 1–23:
  the Hanner bodies.
- F. Nazarov, F. Petrov, D. Ryabogin and A. Zvavitch, "A remark on the Mahler conjecture: local minimality of
  the unit cube", *Duke Math. J.* **154** (2010) 419–430.
- S. Chen, Y. Li, D. Xi and Z.-F. Xu, "The Mahler conjecture in three dimensions", arXiv:2605.09334 (2026),
  preprint.
- OpenAI, *Mathematics manuscript collection*, https://github.com/openai/math (October 2026), family 087.
