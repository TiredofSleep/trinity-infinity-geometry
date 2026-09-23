# Trinity Infinity Geometry

**A new way to teach higher mathematics — by classifying its paradoxes, not resolving them.** The
base is the integers 0–9 read as shapes — the premise of the book
*[The Shape of Understanding](https://github.com/TiredofSleep/shape-of-understanding)*. Every shape of
the base points toward a **tower** of higher mathematics, climbing from something a child can build
with gumdrops and toothpicks to what a graduate student studies. And every shape, and every floor of
every tower, is a **coin**, with two sides and an edge.

**Author:** Brayden Ross Sanders / 7SiTe LLC · Hot Springs, Arkansas
**License:** [CC BY-SA 4.0](LICENSE) for content, [GPL-3.0-or-later](LICENSE) for code

---

## The idea

Higher mathematics is usually met as a stack of separate courses — linear algebra, group theory,
topology, analysis — each with its own language, joined by nothing a student can see. Here it is
met as **towers standing on one base**. The base is small enough to hold in one hand. Each tower
starts on it, and a learner who can stand on the base can see where every tower goes.

It is seen through **two lenses**. The towers are the climb. The **coin** is what every floor turns
over. A *flip* is a move that, done twice, changes nothing: its two sides are what it swaps, and its
edge is what it leaves in place. The paradoxes live on the edges — √2, which no fraction reaches, and
*i*, which no real number is — and mathematics did not resolve them. It named them and classified
them. That is the method here.

## The coin — [`coin/`](coin/README.md)

The name is the author's own idea of a coin: *"every one is three. It is three as two"* — the
founding definition of Trinity Infinity Geometry (January 2026). A coin is two sides and an edge:
three things, seen as two. The author's three coins — positive and negative, real and imaginary,
finite and infinite — are the three half-turns of the sphere of numbers about the axes of one
octahedron, whose corners are 0, ∞, 1, −1, *i*, −*i*. Every flip that respects adding splits each thing into an edge part and a side
part: real + imaginary, cos θ + *i* sin θ, symmetric + skew. Missing edges are where the paradoxes
live, and the book's keystone — *point toward it, measure off it, never stand on it* — holds there
exactly. The author's own classification of paradoxes into four kinds, with Ben Mayes (April 2026), is
read through the coin in [`coin/PARADOX_TYPES.md`](coin/PARADOX_TYPES.md). In it, insufficient coverage
calls for a second lens, a missing invariant is a missing edge, and a self-referential paradox is a flip
with no edge — the Liar, Russell and Cantor are one diagonal. Start with
[`coin/THE_COIN.md`](coin/THE_COIN.md).

## The base — [`base/`](base/README.md)

Read an integer as a configuration of points, and ask what shape it is forced to take. One rule —
the book's own, *the most symmetric arrangement* — realizes every integer from 0 to 9, each
uniquely:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| the void | point | segment | triangle | tetrahedron | tetrahedron + centre | octahedron | octahedron + centre | cube | cube + centre |

From 4 on, each integer is a coin with a **flat face** (the most symmetric arrangement in the
plane: the square, the pentagon, …) and a **solid face** (the table). At 5, 7 and 9 the coin is
whether the centre is inhabited. Every solid symmetry group has only even orbits besides the centre,
so an odd count in a solid must stand on its centre. The flat face never does. Both faces are kept:
the book's 5 is the flat pentagon, the "break". Start with
[`base/THE_INTEGERS.md`](base/THE_INTEGERS.md), then [`base/SEVEN_AND_NINE.md`](base/SEVEN_AND_NINE.md).

## The towers — [`towers/`](towers/README.md)

| from the base | the tower | where it reaches | its coin: sides · **edge** |
|---|---|---|---|
| 1–4, the simplices | the **simplex tower** | probability; algebraic topology | cube · cross-polytope · **the simplex, its own dual** |
| 8, the cube · 6, the octahedron | the **cube** and **cross-polytope towers** — with the simplex, the only regular shapes in every dimension | binary codes; sparsity; regular polytopes | (the same coin: duality) |
| 8, the cube's algebra Cl(3) | the **Clifford tower** | spinors; Bott's eight-step clock | odd · even · **the even half, ℍ** |
| turning, *i* | the **number tower** ℝ → ℂ → ℍ → 𝕆 | Hurwitz: division ends at 𝕆 | ± imaginary · **the reals** |
| the most symmetric arrangement; the break at 5 | the **symmetry tower** | A₅ and the unsolvable quintic; the quaternions over the rotations; Lie groups | left · right · **the Platonic solids**; *q* · −*q* · **no edge** |
| 5, 7, 9 — the centred shapes | the **lattice tower** | Kepler's packing; E₈ and the Leech lattice | face-centred · body-centred · **the self-dual: ℤⁿ, E₈** |
| the tetrahedron's 1/3 | the **harmonic tower** | spherical harmonics; the shapes of atomic orbitals | + lobe · − lobe · **the node (the magic angle)** |
| counting versus measuring, √2 | the **real-number tower** | the real line; transcendence of *e* and π | below √2 · above · **√2, missing** |
| growing, *e* | the **growth tower** | the exponential map from Lie algebras to Lie groups | growing · shrinking · **pure turning, the circle** |

The map, floor by floor: [`towers/THE_TOWERS.md`](towers/THE_TOWERS.md). The base does not prove
the towers; it points at them. For a learner, the book's last chapter, [*Where the towers go*](https://github.com/TiredofSleep/shape-of-understanding/blob/main/the_shape_of_understanding_BOOK.md#chapter-18--where-the-towers-go), points up each
one in plain words; this repository carries the detail and the checks.

## Check it

```
pip install numpy
cd base
python verify_integers.py
python verify_one_rule.py
python verify_forced_chain.py
cd ../coin
python verify_coins.py
python verify_paradox_types.py
cd ../towers
python verify_towers.py
python verify_two_builds.py
python verify_one_third_fold.py
python bott_verify.py
```

Every claim tagged **[FORCED]** has a line in one of these scripts; theorems at the tops of the
towers are cited.

## What was archived, and why

Until 2026-09-23 this repository held a much larger program built on three 10×10 composition
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
