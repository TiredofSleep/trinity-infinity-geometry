# Seven and nine — one rule for the whole realization

### Tags: **[FORCED]** checked by [`verify_one_rule.py`](verify_one_rule.py) (or, where marked, [`../coin/verify_coins.py`](../coin/verify_coins.py)) · **[NAMED]** a cited standard result · **[READING]** an interpretation · **[COIN]** a classified pair: both faces kept, neither chosen.

---

## The question

[`THE_INTEGERS.md`](THE_INTEGERS.md) left one question open: **is there one natural rule that
realizes all ten integers?** The book realizes 0–6 and 8; 7 and 9 have no realization in it.
This note tests the candidate rules at 7 and 9 — and whether any of them carries all ten.

## The rule the book already uses

The book does not define its ladder by equal distance alone. It defines it by symmetry:

> "Given *n* points in the most symmetric arrangement — all mutually equidistant … — they form
> the regular (*n*−1)-simplex." — *The Shape of Understanding*, Ch. 1 §1.1

Equal distance is what "most symmetric" looks like while each new point still has a new
dimension to rise into. So the natural test is to **keep the book's rule and stay in
three-dimensional space**:

> **Rule.** Arrange *n* points so that their symmetry group — every rotation and reflection that
> carries the arrangement onto itself — is as large as possible, with the points **not all on one
> line**.

The clause matters for every *n* ≥ 3: points on a line can spin freely about it, so a line is
infinitely symmetric and would otherwise win every time. For 1 and 2 points there is only one
arrangement anyway.

## The result [FORCED]

| n | the most symmetric arrangement | symmetries |
|---|---|---|
| 0 | the void (no points) | — |
| 1 | a point | every rotation |
| 2 | a segment | infinitely many |
| 3 | a triangle | 12 |
| 4 | a tetrahedron | 24 |
| 5 | **a tetrahedron with its centre** | 24 |
| 6 | an octahedron | 48 |
| **7** | **an octahedron with its centre** | 48 |
| 8 | a cube | 48 |
| **9** | **a cube with its centre** | 48 |

**Every answer is unique** (up to size and orientation). So the book's rule, carried past four
points in three-dimensional space, realizes all ten integers: **7 is the octahedron with its
centre filled, and 9 is the cube with its centre filled.**

**Why — and why the check is complete.** Every symmetry group of a finite set of points in
three-dimensional space (not on a line) is one of the classified *point groups* [NAMED: the
classification of the finite symmetry groups of 3-space — Klein 1884 for the rotation groups;
see Coxeter, *Regular Polytopes*]: the seven polyhedral groups and seven families built
around one axis. The point set is made of *orbits* — sets of points the symmetries carry into one
another — so its size is a sum of orbit sizes.

- The icosahedral group (120 symmetries) has orbits of 1, 12, 20, 30, 60, 120 points — nothing
  between 2 and 11 except the centre alone.
- The octahedral group (48) has orbits of 1, 6, 8, 12, 24, 48: that gives 6 (the octahedron),
  **7 = 6 + the centre**, 8 (the cube) and **9 = 8 + the centre**.
- The tetrahedral group (24) has orbits of 1, 4, 6, …: that gives 4 and **5 = 4 + the centre**.
- A group built around one axis has at most 4*k* symmetries and needs a ring of *k* points off the
  axis, which keeps it below the tetrahedral and octahedral groups for every *n* from 4 to 9. (At
  3 the winner, the triangle, is itself one of these axial groups.)

The script builds every point group that can matter for *n* ≤ 13 — the seven polyhedral groups
and the axial families up to a 16-fold axis. It then searches every union of orbits of each
size, and confirms both the winners and their uniqueness.

## The edge at ten [FORCED]

At 10 the rule leaves the family. The most symmetric 10-point arrangement is the flat **regular
decagon** (40 symmetries); 11 is the regular hendecagon (44); 12 is the icosahedron (120), and 13
the icosahedron with its centre.

The edge itself is partly a matter of size: the family's largest member, the cube with its
centre, has 9 points. **The substantive fact runs the other way — at every n from 0 to 9 the most
symmetric arrangement is in the family** (a simplex, or a tetrahedron, octahedron or cube, alone
or with its centre), and never a flat polygon: the pentagon, heptagon and nonagon all lose. A
stricter variant, which asks the points to fill as many dimensions as they can, agrees at 5, 7
and 9 and also leaves the family at 10 and 11 (octagonal and nonagonal bipyramids).

**[READING]** So the rule's run of solids is exactly the ten digits — a geometric edge that does
not depend on writing numbers in base ten. It is recorded as a fact about this rule, not as a
claim about why we count in tens.

**Where the base hands off.** The family does not end at 10 so much as open upward. Its three
solids — the tetrahedron, the octahedron and the cube — are the three-dimensional floors of the
only three regular shapes that exist in every dimension (the simplex, cross-polytope and cube
towers), and 12, the icosahedron, is where the five-fold line of the break rises. See
[`../towers/THE_TOWERS.md`](../towers/THE_TOWERS.md).

## The pattern: the odd numbers fill the centre

- **[FORCED]** 5 = 4 + centre, 7 = 6 + centre, 9 = 8 + centre. The even ones — 4, 6, 8 — are the
  three Platonic solids with at most eight corners: the tetrahedron, octahedron and cube.
- **[FORCED — `verify_coins.py`] Why the odd ones must.** In every solid symmetry group
  (tetrahedral, octahedral, icosahedral, with or without mirrors), every orbit except the centre
  has an even number of points. So an odd number of points with solid symmetry has to put one on the
  centre. The centre at 5, 7 and 9 is forced by oddness. It is not chosen, and it needs no ring or
  modular closing.
- **[READING]** Each odd integer from 5 on is the one before it with its void filled. This is the
  book's "the void is the fullest point" (§1.6b) made literal — and the book already reads 1 this
  way ("the point, 1, is the void made visible"). The pattern does not reach 3: a segment with its
  centre is three points on a line, which the rule excludes, so 3 is the triangle.

## Where these shapes are measured [NAMED — illustration, not derivation]

- **5** — methane, CH₄: a carbon with four hydrogens at the corners of a tetrahedron. And every
  atom of **diamond** with its four nearest neighbours [FORCED: the diamond lattice's nearest
  shell is a tetrahedron].
- **7** — sulfur hexafluoride, SF₆: a sulfur with six fluorines at the corners of an octahedron.
  And every site of the **simple cubic** lattice with its six neighbours [FORCED].
- **9** — the **body-centred cubic** cell, as in iron at room temperature: an atom at the centre of
  a cube of eight [FORCED: the nearest shell of body-centred cubic is a cube].
- The remaining cubic lattice, **face-centred cubic**, gives 1 + 12 = 13 — past the digits.

And in the Pythagorean tradition of *figurate numbers*, the book's oldest inspiration, 5, 7 and 9
are the second **centred tetrahedral, centred octahedral and centred cube numbers** (1, 5, 15, 35…;
1, 7, 25, 63…; 1, 9, 35, 91…) [FORCED].

## The rival rules [FORCED]

| rule | 5 | 7 | 9 | verdict |
|---|---|---|---|---|
| equal distance | — | — | — | stops at 4 (five equal points need a fourth dimension) |
| spreading on a sphere | triangular bipyramid (12) | pentagonal bipyramid (20) | triaugmented triangular prism (12) | realizes 7 and 9, but gives the square antiprism, not the cube, at 8 |
| perpendicular build | — | — | — | only 1, 2, 4, 8 |
| regular polygon | pentagon (20) | heptagon (28) | nonagon (36) | flat; gives the square at 4 and the hexagon at 6, not the solids |
| **most symmetric** | **tetrahedron + centre (24)** | **octahedron + centre (48)** | **cube + centre (48)** | **realizes all ten; agrees with the book at 0–4, 6 and 8** |

(Symmetry counts in parentheses.)

## What this settles, and how 5, 7 and 9 are classified

- **Settled:** one rule — the book's own — realizes every integer from 0 to 9, each uniquely, and
  stops at 10. It fills the book's gap at 7 and 9: **7 is the octahedron with its centre, 9 the
  cube with its centre.**
- **[COIN] Classified, not chosen.** The program classifies paradoxes; it does not resolve them.
  So 5, 7 and 9 are not decisions between rivals. Each integer is a coin with two faces, and both
  are kept:
  - **the flat face** — the most symmetric arrangement *in the plane*: the pentagon, the heptagon,
    the nonagon. Its centre is empty. It points toward the void and never stands on it.
  - **the solid face** — the most symmetric arrangement *in space*: the tetrahedron, octahedron or
    cube with its centre. Its centre is inhabited, forced by oddness.
  - **9 has a third face**, the square 3²: the 3 × 3 grid (16 symmetries in space), which is two
    whole coins — heads, tails or edge — tossed together.
  - The edge between the faces is the centre itself. See
    [`../coin/THE_COIN.md`](../coin/THE_COIN.md) for the classification and its checks.
- **The book** shows the flat face at 5, the pentagon, because its lesson — the break — lives in the
  plane. It teaches 0–6 and 8. The solid faces stay here, behind the wall, unless the author moves
  them.
