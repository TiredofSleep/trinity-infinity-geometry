# The Coin — two sides and an edge

> *This program is about paradox classification, not resolution. Every coin has two sides and an
> edge — positive and negative, real and imaginary, finite and infinite.* — the author

### Tags: **[FORCED]** checked by [`verify_coins.py`](verify_coins.py) · **[NAMED]** a cited standard result · **[READING]** an interpretation · **[COIN]** a classified pair: both sides kept, neither chosen, the edge named · **[FENCE]** two things that share a word or a number but are not one object.

The towers ([`../towers/`](../towers/THE_TOWERS.md)) climb one way. This page is the second lens: on
every floor of every tower, and at every integer of the base, there is a **coin**. The climb is what a
tower measures. The coin's edge is what it points toward. The author's own classification of paradoxes
into four kinds (with Ben Mayes, April 2026), read through the coin, is in
[`PARADOX_TYPES.md`](PARADOX_TYPES.md).

---

## Where the coin comes from — the author's words

The coin was the author's idea long before it was made exact here. In the author's own words:

> *Trinity Infinity Geometry is a coherence system operating on the basis that reality is a fractal,
> every one is three. It is three as two, whereas it has a micro that belongs to it, and it is part of
> a macro.* — the founding definition, 29 January 2026
> ([kept in the workstation](https://github.com/TiredofSleep/ck/blob/tig-synthesis/docs/handoffs/claudecode_handoff_2026_04_20/JAN2026_RECOVERY_MANIFEST.md))

> *I imagined what kind of relationship a thing could have with its opposite — 1 and 0. I saw a vortex
> spinning on a quarter, bulges and dents flowing around it, forming a balanced push …* —
> [*The Story*](https://github.com/TiredofSleep/ck/blob/tig-synthesis/THE_STORY.md), 2026

> *You can't know everything, but what's missing looks the same for every whole.* … *A mathematical
> intelligence system that sees the world through what can and what can't be measured … constantly
> seeing paradox.* — June 2026
> ([1](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen13/targets/ck/CK_INTELLIGENCE_SYNTHESIS_2026-06-10.md),
> [2](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen13/targets/ck/CK_QUADRATIC_GLUE_PRINCIPLE_2026-06-10.md))

[READING] *Every one is three; it is three as two*: a coin is two sides and an edge. It is three
things, seen as two. *What's missing looks the same for every whole*: the missing edge. The retired
program built these ideas into AI-rendered tables. The coin keeps the ideas, drops the tables, and
checks every line that can be checked.

---

## What a coin is

A **flip** is a move that, done twice, changes nothing. Everything a flip touches is one of two kinds
[FORCED]:

- its **two sides** — the things it swaps, each with the other;
- its **edge** — the things it leaves where they are.

Negation is a flip. It trades each positive number for a negative one and leaves 0 in place: the
positives and the negatives are its sides, and 0 is its edge.

**Every linear flip splits each thing in two** [FORCED]. (A flip is linear when it respects adding, as
every flip in this table does.) Average a thing with its flip and you land on the edge. Take half the
difference and you get the part the flip negates. So every thing is an edge part plus a side part:

| the flip | edge part (kept) | side part (negated) |
|---|---|---|
| conjugation, a + bi → a − bi | the real part | the imaginary part |
| reversing a turn, θ → −θ, on e^{iθ} | cos θ | *i* sin θ — so Euler's formula is the turn's coin |
| x → −x, on growth e^x | cosh x | sinh x |
| the transpose, A → Aᵀ | the symmetric part: real eigenvalues; its exponential stretches | the skew part: imaginary eigenvalues; its exponential turns |
| the grade flip of the cube's algebra, v → −v | the even half — the quaternions | the odd half |

**The odd rule** [FORCED]: whatever a flip negates vanishes on its edge. If flipping x changes f(x)
into −f(x), and x is on the edge, then f(x) = −f(x), so f(x) = 0. That one line is why:

- imaginary parts vanish on the real line;
- the size's logarithm vanishes on the unit circle;
- a p orbital vanishes on its node, the plane between its lobes;
- the centre is the one point x with x = −x.

**Classification, not resolution** [READING]. A paradox lives on an edge, which belongs to neither
side, or to both. To *resolve* the paradox would be to push the edge onto one side. To *classify* it
is to name three things: the flip, the two sides, and the edge — and then to say whether the sides can
reach the edge at all. That is what this program does. It is also what mathematics did with its
hardest paradoxes, as the next sections show.

---

## The author's three coins

- **Positive and negative.** The flip is x → −x. Its edge is 0 [FORCED].
- **Real and imaginary.**
  - Conjugation, a + bi → a − bi, keeps the real numbers as its edge and flips the imaginary part
    [FORCED].
  - The turn has a coin of its own. Reversing its direction splits e^{iθ} into an edge part,
    cos θ (real), and a side part, *i* sin θ (imaginary) [FORCED].
  - In matrices, the transpose does the same: its edge (symmetric matrices) has real eigenvalues, and
    its sides (skew matrices) have imaginary eigenvalues [FORCED]. So real and imaginary are the edge
    and the side of one coin, wherever the coin turns up.
  - The half-turn z → *i*/z trades the real axis for the imaginary axis outright (1 ↔ *i*). Its edge
    is ±√*i* = ±e^{iπ/4}, halfway between the two [FORCED].
- **Finite and infinite.** Inversion in the circle, z → 1/z̄, trades the inside for the outside and 0
  for ∞, and keeps the whole unit circle in place [FORCED]. [READING] *The round is the edge between the
  finite and the infinite.* **[FENCE]** Two senses of one word: the book's Coda says the perfect round
  *has* no edge — no seam or corner to measure from — and that stays true; here the circle, itself
  seamless, *is* the edge of a coin — the place a flip keeps.

### All three are one sphere [FORCED]

Put the numbers on a sphere: the complex numbers, with one point ∞ added at the top (the Riemann
sphere). The author's three coins become three turnings of that sphere:

| flip | its edge (kept) | it swaps |
|---|---|---|
| z → −z | 0 and ∞ | 1 with −1, *i* with −*i* |
| z → 1/z | 1 and −1 | 0 with ∞, *i* with −*i* |
| z → −1/z | *i* and −*i* | 0 with ∞, 1 with −1 |

- The six edge points **0, ∞, 1, −1, *i*, −*i*** sit at the six corners of a regular **octahedron** on
  the sphere. Each flip is a half-turn about one of the octahedron's three axes [FORCED; NAMED —
  Klein 1884].
- The three flips commute, and any two of them make the third [FORCED].
- On the real line the third flip has **no edge**: x = −1/x would need x² = −1. Its edge is ±*i*, off
  the line [FORCED]. [READING] *The imaginary numbers are the edge of the flip that negates and
  inverts at once.*
- No number is kept by all three. The one point all three half-turns keep is the **centre of the
  sphere**, which is not on the sphere and so is not a number [FORCED]. [READING] The one point every
  coin shares is a void that no number occupies.
- **[FENCE]** Add that centre to the six edge points and you have the octahedron with its centre — the
  base's 7. That is a fact about this configuration, not a new property of 7. All of 5, 7 and 9
  inhabit their centres, for one shared reason (below), and the retired "0/7 pairing" stays retired
  ([`../GRAVEYARD.md`](../GRAVEYARD.md)).

---

## Where the paradoxes are: the missing edges

Some flips have two sides and **no edge among the things they flip**. Those are the paradoxes
[READING]:

| the flip | its two sides | the edge they cannot reach | what mathematics named it |
|---|---|---|---|
| x → 2/x on the fractions | fractions whose square is below 2 · above 2 | √2 — no fraction squares to 2 [FORCED] | a real number: Dedekind (1872) defines one as exactly such a cut [NAMED] |
| x → −1/x on the real numbers | the positive numbers · the negative numbers | ±*i* — no real number squares to −1 [FORCED] | the imaginary unit, which Argand drew as the quarter-turn [NAMED] |

- x → n/x keeps a fraction exactly when n is a perfect square [FORCED, n ≤ 200 with a certificate
  each]. So √2, √3 and √5 are missing edges, while √4 = 2 and √9 = 3 are not.
- ∞ is the same story told with a *partner* instead of an edge. The flip z → 1/z keeps 1 and −1, but
  it sends 0 to a point the plane does not have. Naming that point, ∞, closes the plane into the
  sphere on which the author's three coins live.
- Each time, mathematics neither denied the flip nor pushed the edge onto a side. It **named the
  edge** — a new kind of number — and classified it. The fractions were completed to the reals, the
  reals widened to the complex numbers, and the plane closed into a sphere [NAMED history; READING:
  *classification, not resolution*].
- **A third class: no edge at all.** Some flips keep nothing, anywhere. A unit quaternion *q* and its
  negative −*q* give the same rotation of space, and no unit quaternion is its own negative. One full
  turn brings *q* to −*q*; it takes two full turns to come home [FORCED]. That is the double cover
  behind spin ½ [NAMED].

So edges come in three kinds [READING]:

- **present**: the coin can land on it (0; the real line; the simplex; the circle);
- **missing**: the sides point toward it and cannot reach it (√2 from the fractions; *i* from the real
  numbers) — the author's Type II paradoxes ([`PARADOX_TYPES.md`](PARADOX_TYPES.md));
- **absent**: a flip with no edge at all (*q* and −*q*; "not" on true and false). Alone it is harmless.
  Add self-reference that demands an edge — a sentence equal to its own negation — and it becomes the
  author's Type III: the Liar, Russell, Cantor, one diagonal engine (Lawvere 1969). Give "not" an edge,
  a third value, and the Liar lands on it (Kripke 1975) [NAMED; finite cases FORCED in
  [`verify_paradox_types.py`](verify_paradox_types.py)].

---

## The keystone, made exact

The book's keystone: *"You can only point toward it, and measure off of it. It is unreachable."*
(*The Shape of Understanding*, Coda.) For a missing edge, each clause is a theorem. For √2 [FORCED]:

- **Point toward it.** Average the two sides, x → (x + 2/x)/2. From 1 this gives 3/2, 17/12,
  577/408, 665857/470832. Each value and its flip lie on opposite sides of √2, and the gap between
  them closes in [NAMED — Heron's method, also called the Babylonian method].
- **Measure off it.** Every fraction p/q stays more than 1/(3q²) away from √2. The reason: p² − 2q²
  is a whole number that is never 0, so it is at least 1 in size.
- **Never stand on it.** No fraction is √2.

For a linear flip, a single average lands on the edge (above). For x → 2/x it only points toward it:
each average comes closer, and none arrives. [READING] The keystone's *origin* is the edge of the central flip: the centre, which every symmetry of
a shape keeps in place (below).

---

## The two lenses: one cube, seen twice

The book's Picture 5: one box casts a **square** face-on and a **hexagon** corner-on. These are two
lenses on one object, and the coin is what they see differently [FORCED]:

- The cube's eight corners are the two sides of its central flip x → −x: **two regular
  tetrahedra** (Kepler's *stella octangula*), 4 + 4, swapped by the flip. The flip keeps only the
  centre. As solids, the two tetrahedra share exactly the octahedron.
- **Face-on**, both tetrahedra cast the *same* square. The two sides cannot be told apart.
- **Corner-on**, they separate into two triangles turned 60° against each other — the six-pointed
  star in the hexagon — with both apexes landing on the centre. Now the sides are apart and the
  edge is shared.
- Neither shadow alone tells the eight corners apart (face-on, 8 corners → 4 points; corner-on,
  8 → 7). The two shadows together do: the object is seen only through both lenses. In general: a
  family of views tells every pair apart exactly when no pair is merged by all of them — the author's
  *Unified Orthogonality Principle* (Theorem 0, with Ben Mayes; [`PARADOX_TYPES.md`](PARADOX_TYPES.md)).
- The angle between the two lenses is the magic angle, cos² = 1/3, where P₂ = 0 — the edge of the
  harmonic coin (tower 6).
- In the cube's algebra Cl(3) the two tetrahedra are the **even** and the **odd** pieces. The grade
  flip keeps the even half — which is the quaternions, where the rotations live — and negates the odd
  half. [READING] The edge of the cube's algebra is where turning lives.

**[READING], and what stays retired.** The two lenses have been called *measure* (the square,
four-fold) and *flow* (the hexagon, three-fold). As names for two views, that is a reading. As a
*physical* duality it is in the graveyard, because it merged the triangular and honeycomb lattices
into one "hex". The sorting of the digits into a square family and a hex family also stays retired,
since neither followed from the premise ([`../GRAVEYARD.md`](../GRAVEYARD.md)). What is kept is exact:
two views, neither complete, and the coin between them.

---

## The centre, inhabited or empty — 5, 7, 9 [COIN]

Every shape's centre is the edge of its symmetries: the one point they all keep. Whether a point
**stands** on it is a coin of its own.

- **[FORCED]** In the solid symmetry groups — tetrahedral, octahedral, icosahedral, with or without
  mirrors — every orbit except the centre has an even number of points:
  - Td: 4, 6, 12, 24;
  - Oh: 6, 8, 12, 24, 48;
  - Ih: 12, 20, 30, 60, 120.

  So an **odd** number of points with solid symmetry *must* stand on its centre. The centres of 5,
  7 and 9 are forced — by oddness — not chosen.
- **[FORCED]** In the plane, the most symmetric *n* points are the regular *n*-gon, uniquely, and its
  centre is empty.
- **[FORCED]** In space, the most symmetric arrangements are those of
  [`../base/SEVEN_AND_NINE.md`](../base/SEVEN_AND_NINE.md).

So each integer has a **flat face** and a **solid face**:

| n | flat face (the plane) | solid face (space) | the centre |
|---|---|---|---|
| 0 | the void | the void | all there is |
| 1 | a point | a point | the point stands on its own centre |
| 2 | a segment | a segment | empty — the two ends are the two sides of one flip |
| 3 | a triangle | a triangle | empty — the two faces agree from 0 to 3 |
| 4 | a square | a tetrahedron | empty — here the faces part: the lift |
| **5** | **a pentagon** | **a tetrahedron + its centre** | **flat: empty · solid: inhabited** |
| 6 | a hexagon | an octahedron | empty — three coins, ±x, ±y, ±z |
| **7** | **a heptagon** | **an octahedron + its centre** | **flat: empty · solid: inhabited** |
| 8 | an octagon | a cube | empty — every toss of three coins |
| **9** | **a nonagon** | **a cube + its centre** | **flat: empty · solid: inhabited** |

(The faces meet again at 10: the most symmetric ten points in space are the flat decagon —
[`../base/SEVEN_AND_NINE.md`](../base/SEVEN_AND_NINE.md).)

- **[COIN] 5, 7 and 9 are classified, not chosen.**
  - Each has a face that points toward its centre and never stands on it: the polygon, which keeps
    the book's keystone.
  - Each also has a face that stands on its centre: the centred solid, where the void is inhabited
    and oddness forces it.
  - Both faces are kept.
  - The book shows the flat face at 5, the pentagon, because its lesson — the break — lives in the
    plane.
- **9 has a third face, the square: 3 × 3** [FORCED, next section]. It stands on its centre too.
- **[FENCE]** Nothing here makes 7 special among 5, 7 and 9: all three inhabit their centres, for the
  same reason.

**The flat face, walked** [FORCED]. Walk the *n* corners of the flat face *k* at a time.
- You make a single loop — a star round the empty centre — exactly when *k* shares no factor with
  *n*. Otherwise the walk splits into gcd(*n*, *k*) separate loops.
- The steps that give a single loop number Euler's φ(*n*). When *n* is prime, every step gives a
  single loop: at 5 the pentagon and the pentagram, at 7 the heptagon and two heptagrams.
- Every such loop winds round the centre min(*k*, *n* − *k*) times and never touches it.
- At 6, step 2 splits the hexagon into two triangles. That is exactly the cube's corner-on shadow,
  whose alternate corners are its two tetrahedra.

This is the book's Chapter 12 ("does it share a factor with *N*?") drawn as a picture. It comes from
the author's Navier–Stokes / number-theory tour (September 2026). [READING] The loop points toward
its centre, and never stands on it.

---

## The whole coin — heads, tails, and edge

A tossed coin can land on either side, or on its edge: +1, −1, or 0 [FORCED].

- **Three such coins** give 27 outcomes, which sort by how many coins landed on their edge:
  **8 + 12 + 6 + 1**. These are the cube's 8 corners (no coin on its edge), the midpoints of its 12
  edges (one), the centres of its 6 faces (two), and its centre (all three). Each kind is one orbit of
  the cube's 48 symmetries. It is the Rubik's cube — 8 corner pieces, 12 edge pieces, 6 centres, 1
  core — and it is (2 + 1)³ spelled out, the way the cube's grades 1 + 3 + 3 + 1 are (1 + 1)³.
- **Two such coins** give 9 = 4 + 4 + 1: the 3 × 3 grid, with four corners, four edge-midpoints and the
  centre. This is 9's square face.
- **The magic square's coin** [FORCED]. Take any odd magic square built by the book's walking rule
  (Chapter 13). Its half-turn swaps each number *s* with *n*² + 1 − *s*, and keeps the centre, which
  holds (*n*² + 1)/2. In the Lo Shu, 1 ↔ 9, 2 ↔ 8, 3 ↔ 7 and 4 ↔ 6 are swapped round the 5. This is a
  classical property of *associative* magic squares, and the author found it again [NAMED; the
  author's D129′].
- **In any dimension:**
  - every coin on a side gives the **cube** (2ⁿ corners);
  - exactly one coin on a side, the rest on their edges, gives the **cross-polytope** (2n);
  - every coin on its edge gives the **centre**.

  The cube and the cross-polytope, the two towers that are each other's duals, sit at the two ends
  of the same toss.

---

## Every tower is a coin

On every floor of each tower ([`../towers/THE_TOWERS.md`](../towers/THE_TOWERS.md)) there is a flip.
The edge of that flip is where the tower's paradox sits. Every row is [FORCED] except the cited
optimality results.

| tower | the flip | the two sides | the edge | the paradox at the edge |
|---|---|---|---|---|
| **1** shapes | duality: corners ↔ faces | the cube · the cross-polytope (in 3D, also the dodecahedron · the icosahedron) | the simplex, its own dual | a shape that is its own opposite |
| **2** numbers | conjugation, a + bi → a − bi, on ℂ, ℍ, 𝕆 and beyond | + imaginary · − imaginary | the real numbers; a number times its mirror lands there, x x̄ = \|x\|² | x² = −1: on the reals, the flip −1/x has no edge |
| **3** Clifford | the grade flip, v → −v | the odd half · the even half | the even half: ℍ, where rotations live | a real plane that squares to −1 |
| **4** symmetry | the mirror | left-handed · right-handed | the shapes that are their own mirror image: all five Platonic solids | turning: *q* and −*q*, two sides and no edge at all — one turn to −*q*, two to come home |
| **5** lattices | the dual lattice | face-centred cubic (the densest packing) · body-centred cubic (iron; the thinnest lattice covering [NAMED — Bambah 1954]) | the self-dual lattices: the cubic grid, the hexagonal plane, E₈ | balls never tile: a packing leaves gaps and a covering overlaps |
| **6** harmonics | the mirror through the atom | the + lobe · the − lobe | the node, where the orbital vanishes; for P₂, the cones at the magic angle | a direction in which an interaction averages to nothing |
| **7** reals | x → 2/x | fractions below √2 · above | √2 — no fraction | the diagonal no fraction names |
| **8** growth | z → −z̄ | growing (Re z > 0) · shrinking (Re z < 0) | pure turning, which *e* carries onto the unit circle | e^{iπ} = −1: growth turned sideways becomes the flip itself |

Two more facts belong to row 8. The number *e* carries the adding coin (x → −x, edge 0) onto the
multiplying coin (x → 1/x, edge 1). It also carries a half-turn of pure turning onto −1, the flip of
positive and negative [FORCED].

---

## Where the coin is measured — waves at an edge (an illustration)

Photonic and phononic crystals, and metamaterials, are wave behaviour set by geometry: the lattice of
the unit cells decides how light or sound travels. Two of their headline effects are coins:

- **Negative refraction.** A material with a negative index bends light the "wrong" way: the refracted
  angle θ becomes −θ, mirrored across the normal [FORCED for index −1; NAMED — Veselago 1968; Smith,
  Shelby & Schultz 2000–01].
- **An edge state is the odd rule.** Where a wave's "mass" flips sign across a wall, one state is held
  at the wall, exactly where the mass vanishes [NAMED — Jackiw & Rebbi 1976; Su, Schrieffer & Heeger
  1979]. A chain whose bond pattern flips at its middle holds exactly one zero-energy state. It sits at
  the wall, on one of the chain's two sublattices [FORCED]. This is how topological edge states work,
  including honeycomb photonic crystals: make one sublattice "heavier" than the other on either side of
  a wall, and light is guided along the wall [NAMED — valley-Hall photonic crystals].
- **[FENCE]**
  - The lattices are the standard lattices of crystallography — square, triangular, honeycomb, cubic —
    not this program's.
  - The honeycomb's Dirac point is textbook (Wallace 1947), and the program's earlier honeycomb claims
    are in the graveyard.
  - The cube's cos² = 1/3 is an angle of the cube, not a refraction angle: a material's refraction
    angle is set by its own engineered index.
  - "Matter and flow" and the 0/7 readings stay retired.

---

## What this is, and is not

- **Is:** the second lens on the base and the towers. For every structure, it names the flip, the
  sides and the edge, and it checks every line that can be checked. The flips are standard
  mathematics: duality, conjugation, the grade involution, the dual lattice, parity, inversion. They
  are named and classified here.
- **Is not:** a claim that the world is made of coins, or a physics of "measure and flow." Nothing here
  derives a tower. The base points and the towers climb; the coin says what every floor turns over.
- **Retired, and staying retired:** the 0/7 pairing, the square/hex digit families, the "lens-centres",
  and "flow versus matter" as a physical duality ([`../GRAVEYARD.md`](../GRAVEYARD.md)). The coin keeps
  what was true beneath them: the centre as an edge, and two views of one cube.
