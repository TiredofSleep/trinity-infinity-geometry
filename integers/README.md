# The integers 0–9 as shapes

The research in this repository: the **geometric realization of the integers 0–9** — the premise
of *[The Shape of Understanding](https://github.com/TiredofSleep/shape-of-understanding)* — and
what extends from it. The book teaches the core; these notes carry it further, and stay out of
the book.

> **Run the checks first** (Python 3.10+, numpy):
>
> ```
> python verify_integers.py       # which rule realizes which integer, 0–9
> python verify_one_rule.py       # one rule for all ten: the most symmetric arrangement
> python verify_forced_chain.py   # the simplex ladder, the tetrahedral 1/3, the cube = Cl(3)
> python verify_two_builds.py     # equal distance lifts; perpendicularity doubles
> python verify_one_third_fold.py # the 1/3 as lift, fold and gap
> python bott_verify.py           # the Clifford tower's period 8
> ```

## Reading order

| file | what it is |
|---|---|
| [`THE_INTEGERS.md`](THE_INTEGERS.md) | **Start here.** 0–9 one at a time, each with the rule that picks its shape: 0–4 forced by equal distance; 6 by spreading on a sphere; 8 by perpendicularity; 5, 7, 9 by other rules — and the one rule that realizes all ten (next row). |
| [`SEVEN_AND_NINE.md`](SEVEN_AND_NINE.md) | **One rule for all ten.** The book's own rule — the most symmetric arrangement — kept in 3-space realizes every integer 0–9 uniquely: **7 = octahedron + centre, 9 = cube + centre** (and 5 = tetrahedron + centre). Checked over every symmetry group of 3-space. At 10 it leaves the family. |
| [`integers_as_geometric_entities.md`](integers_as_geometric_entities.md) | **P1.** The ladder 1–4 and the tetrahedral 1/3 = 1/(N−1) at N = 4, with where that geometry is measured (the carbon bond angle, the NMR magic angle) and a recorded boundary of what does not follow. |
| [`P2_clifford_cube_skeleton.md`](P2_clifford_cube_skeleton.md) | **P2.** The cube: two tetrahedra; its three perpendicular axes generate Cl(3) (1 + 3 + 3 + 1; the bivectors square to −1); its two shadows, square and hexagon, joined by cos² = 1/3. |
| [`THE_TWO_BUILDS.md`](THE_TWO_BUILDS.md) | Equal distance (lifts a dimension) and perpendicularity (doubles the algebra): different objects, both counted by the same row of Pascal's triangle. |
| [`THE_ONE_THIRD_AND_THE_FOLD.md`](THE_ONE_THIRD_AND_THE_FOLD.md) | The cube as a fold of the unbuildable 8-point simplex; the tetrahedron's one number as lift, fold and tiling gap; its return up ℝ → ℂ → ℍ. |
| [`bott_periodicity.md`](bott_periodicity.md) | Where the perpendicular build goes after the cube: the Clifford types repeat with period 8 = 4 + 4, because ℍ ⊗ ℍ ≅ ℝ(4). |

## Tags

**[FORCED]** follows from the named rule and has a line in a verify script · **[RULE]** names the
rule that picks a shape · **[NAMED]** a cited standard theorem · **[READING]** an interpretation,
flagged · **[OPEN]** not settled · **[FENCE]** two things that share a number but are not one
object.

## Kept honest

Earlier versions of these notes carried claims that did not hold; they are recorded, with the
reasons, in [`../GRAVEYARD.md`](../GRAVEYARD.md) §2. The physics strands that used to sit here
(the honeycomb gap law, the duality classification, the Dirac transfers) are archived there too.
