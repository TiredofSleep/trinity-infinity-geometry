# Trinity Infinity Geometry

**The geometric realization of the integers 0–9** — the research that extends the book
*[The Shape of Understanding](https://github.com/TiredofSleep/shape-of-understanding)*.

**Author:** Brayden Ross Sanders / 7SiTe LLC · Hot Springs, Arkansas
**License:** [CC BY-SA 4.0](LICENSE) for content, [GPL-3.0-or-later](LICENSE) for code

---

## The premise

Read an integer as a configuration of points, and ask what shape the configuration is forced to
take. (This is the book's Chapter 1: *integers are shapes*.)

- **0 — the void.** The empty centre: the one point nearest to all the points at once.
- **1, 2, 3, 4 — point, segment, triangle, tetrahedron.** Keep every point the same distance from
  every other, and each new point must rise into a new dimension — and doubles the number of
  pieces. Three-dimensional space holds four equal points and no more.
- **The tetrahedron's number, 1/3.** Seen from the centre, its corners are at cos θ = −1/3
  (109.47°). The same 1/3 relates the cube's two shadows and sets the tetrahedron's tiling gap.
- **5 — the break.** The pentagon: the first rotation that cannot tile.
- **6 — the round.** The octahedron: six points spread evenly on a sphere.
- **8 — the cube.** Three perpendicular directions, 2³ corners, two tetrahedra — and the algebra
  of three-dimensional space, Cl(3), whose two shadows are the square and the hexagon.

## What this repository adds

| | |
|---|---|
| [`integers/THE_INTEGERS.md`](integers/THE_INTEGERS.md) | **Start here.** All ten integers, each with the rule that picks its shape — and what is forced, what is chosen, and what is open. |
| [`integers/SEVEN_AND_NINE.md`](integers/SEVEN_AND_NINE.md) | **One rule for all ten** — the book's own "most symmetric arrangement", kept in 3-space: 7 is the octahedron with its centre, 9 the cube with its centre. |
| [`integers/integers_as_geometric_entities.md`](integers/integers_as_geometric_entities.md) | The ladder and the tetrahedral 1/3, with where that geometry is measured in the world. |
| [`integers/P2_clifford_cube_skeleton.md`](integers/P2_clifford_cube_skeleton.md) | The cube and its Clifford algebra. |
| [`integers/THE_TWO_BUILDS.md`](integers/THE_TWO_BUILDS.md) | Equal distance lifts; perpendicularity doubles. |
| [`integers/THE_ONE_THIRD_AND_THE_FOLD.md`](integers/THE_ONE_THIRD_AND_THE_FOLD.md) | The 1/3 as lift, fold and gap. |
| [`integers/bott_periodicity.md`](integers/bott_periodicity.md) | Where the perpendicular build goes after the cube. |

## One rule for all ten

Beyond four points the simpler rules part ways: spreading points on a sphere forces the
octahedron at 6, perpendicularity forces the cube at 8. But the book's own rule — **the most
symmetric arrangement** — kept in three-dimensional space, realizes every integer from 0 to 9,
each uniquely: the void, point, segment, triangle, tetrahedron, tetrahedron + centre, octahedron,
**octahedron + centre (7)**, cube, **cube + centre (9)** — checked over every symmetry group of
3-space ([`integers/SEVEN_AND_NINE.md`](integers/SEVEN_AND_NINE.md)). It fills the book's gap at 7
and 9, and at 10 it leaves the family. It differs from the book at 5 (the tetrahedron with its
centre, not the pentagon) — a choice for the author.

## Check it

```
pip install numpy
cd integers
python verify_integers.py
python verify_one_rule.py
python verify_forced_chain.py
python verify_two_builds.py
python verify_one_third_fold.py
python bott_verify.py
```

Every claim tagged **[FORCED]** has a line in one of these scripts.

## What was archived, and why

Until 2026-09-24 this repository held a much larger program built on three 10×10 composition
tables that AI had constructed from verbal descriptions of ten operators — 56 manuscripts, a
canon of results, and readings of those tables as physics, cosmology and biology. An audit found
that the three tables disagree on half their cells, and that none of the results specific to them
survived testing: each was generic, a restatement of how the tables were built, numerology, or
computed on a transcription error. The author has no ties to the tables, and all of it was
archived — unchanged, at the tag
[`archive-2026-09-24`](https://github.com/TiredofSleep/trinity-infinity-geometry/tree/archive-2026-09-24).
[`GRAVEYARD.md`](GRAVEYARD.md) records what was archived and the evidence for it.

## Lab

[`lab/`](lab/) — authorship and collaboration policy.

## Citation

See [`CITATION.cff`](CITATION.cff). The project DOI
[10.5281/zenodo.18852047](https://doi.org/10.5281/zenodo.18852047) is the umbrella for all
versions; the v1.0.0 DOI (10.5281/zenodo.20149181) is a snapshot of the earlier, archived program.
