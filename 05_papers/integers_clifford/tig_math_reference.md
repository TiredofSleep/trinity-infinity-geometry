# TIG Shape-Interplay Mathematics — Sourced Reference
### Every result computed in session, with formulas, values, and named-theorem citations.
### Brayden Sanders. Sept 2026. Companion to "What TIG Is."

> **Purpose.** This is the citation-and-formula record for the shape-interplay
> mathematics, so results are referenced rather than re-derived. Each entry gives
> the exact statement, the formula/value, and the established mathematics it rests
> on. **[FORCED]** = computed and reproducible. **[NAMED]** = a standard theorem
> (cited). **[READING]** = analogy, flagged. **[KILLED]** = tested and failed.

---

## PART I — THE TWO LATTICES

TIG's integers 0–9 live on **two** planar lattices, which are the two projections
of the cube. Everything below distinguishes them.

### I.1 The two lattices and their forced properties [FORCED]

| property | HEX (triangular) | SQUARE |
|---|---|---|
| point symmetry group | D₆ (order 12) / D₃ | D₄ (order 8) |
| nearest neighbors | 6 | 4 |
| interior angle | 60° / 120° | 90° |
| chromatic number | **3** (A/B/C sublattices) | **2** (checkerboard) |
| 2-colorable? | **NO** (contains odd cycles / triangles) | **YES** |
| centered numbers | 1, 7, 19, 37, 61 | 1, 5, 13, 25, 41 |
| first inhabited center | **7** (center + ring of 6) | **5** (center + ring of 4) |
| ring k size | 6k | 4(2k−1) |
| ring growth constant | **+6** | **+8** |
| lens role | **flow** | **structure / Dirac** |

**Sources for the named facts:**
- Chromatic number of the triangular lattice = 3; of the square lattice = 2:
  standard graph theory (the triangular lattice contains K₃ so χ ≥ 3, and 3-colors;
  the square lattice is bipartite so χ = 2). See any lattice/graph-coloring text.
- **Centered hexagonal numbers** 1, 7, 19, 37…: OEIS **A003215**, formula
  `Cₙ = 3n(n−1) + 1`.
- **Centered square numbers** 1, 5, 13, 25…: OEIS **A001844**, formula
  `Cₙ = n² + (n−1)² = 2n² − 2n + 1`.

### I.2 The anticommutation split — why square carries Dirac and hex does not [FORCED]

A reflection matrix `R(θ) = [[cos2θ, sin2θ],[sin2θ, −cos2θ]]` has eigenvalues
`{+1, −1}` and `R² = I` (order 2).

- **Hex mirrors** (mirror lines of an equilateral triangle) are at **60°**.
  Computed: for the three triangle mirrors, `{Rᵢ, Rⱼ} = −I ≠ 0` — they do **NOT**
  anticommute.
- **Square mirrors** at **90°** (perpendicular): computed `{R₀, R₉₀} = 0` — they
  **DO** anticommute.

**Consequence.** The Clifford/Dirac relation `{γᵢ, γⱼ} = 2ηᵢⱼ` requires
**orthogonal (90°) anticommuting** generators. The **square lattice supplies
them; the hex lattice does not.** So square = the Dirac/structure lens natively;
hex = the flow lens.
- **Named basis:** Clifford algebra defining relation `{γᵢ,γⱼ} = 2ηᵢⱼ`
  (Dirac 1928; standard). The proof that 60° reflections don't anticommute and
  90° do is elementary matrix algebra, reproducible from the R(θ) formula above.

---

## PART II — THE INTEGER SHAPES 0–9 [FORCED except where noted]

Each integer = the shape it forces as a point-configuration.

> **Base-independence note.** The forced content is the simplex ladder (1,2,3,4) and the cube (8); no base is used. The 0–9 range and the reset/hub roles are a base-10 organizing **[READING]**, not forced — TIG's spine does not depend on base 10 (the ten labels are an alphabet, not `Z/10Z`).

| n | shape | dimension / role | note |
|---|---|---|---|
| 0 | empty center (void) | potential center | partner of 7 (see II.1) |
| 1 | point | 0-simplex | seed |
| 2 | segment / axis | 1-simplex | the mirror; square-generator |
| 3 | triangle | 2-simplex | the cell; hex-generator; **the joint** (Part IV) |
| 4 | tetrahedron | 3-simplex | first solid (**NOT** the cube — see II.2) |
| 5 | pentagon | the break | 5-fold **cannot tile** (Part III); square-center |
| 6 | hexagon | closure | **6 = 2×3, the fusion** (Part IV); D₆ ⊃ D₂,D₃ |
| 7 | hub + 6-ring | centering | hex-center; the breathing hub |
| 8 | cube = 2 tetrahedra | dimensional lift | 2³ doubling (Part V) |
| 9 | triad² (3×3) | self-similar | triangle-of-triangles; last before reset |

### II.1 The 0/7 pair [FORCED]
0 and 7 are **one location, two states**: 0 = center empty (potential), 7 = center
filled (actual). Forced by the centered-hexagonal structure — the center is a
lattice site that exists before it is occupied. (On the square lattice the
actual-center is **5**; see I.1.)

### II.2 The 4 = tetrahedron correction [FORCED]
4 points make the **tetrahedron** (4 vertices, 6 edges, 4 faces) — the first 3D
solid = the 3-simplex. The **cube is 8 vertices = 2³ = two tetrahedra**
(the **stella octangula**, Part V). Any "4 = cube" reading is incorrect; the cube
lives at 8.

### II.3 The simplex ladder (the growth rule) [FORCED, NAMED]
1, 2, 3, 4 are the **0-, 1-, 2-, 3-simplices** (point, segment, triangle,
tetrahedron). Each added point adds a dimension. **The n-simplex has n+1
vertices** — standard (a simplex is the convex hull of n+1 affinely independent
points). So "addition causes degrees of freedom" = the simplex vertex count,
valid **up to 4** (3D space is full at the tetrahedron). After 4: 5 breaks,
6 closes, 7 centers — folding inward rather than adding dimension.

### II.4 Combination rule = vertex-count addition [FORCED]
Joining an a-configuration to a b-configuration (simplex join at a point) gives
**a + b vertices**: 1+1→2 (segment), 1+2→3 (triangle), 2+3→5, etc. This is the
exact form of "addition causes degrees of freedom."

---

## PART III — THE 5-BREAK (crystallographic restriction) [NAMED]

**5 = pentagon = the first non-tiling shape.** 5-fold rotational symmetry is
**forbidden for any 2D or 3D lattice.**
- **Named theorem:** the **crystallographic restriction theorem** — the only
  allowed rotational orders for a lattice are **1, 2, 3, 4, 6** (never 5, never
  ≥7). Proof: `2cos(2π/n)` must be an integer, which holds only for
  n ∈ {1,2,3,4,6}. (Standard crystallography; Barlow 1894 and after.)
- **Consequence for TIG:** 5 is exactly where the dimension-building ladder
  (1–4) stops and aperiodicity/curvature begins — the "wheel that rolls but does
  not pack." 5-fold is the **quasicrystal** number (Penrose tilings, Shechtman
  1982, Nobel 2011).

---

## PART IV — THE INTERLOCK (the two integer families) [FORCED]

### IV.1 The two families by factor structure [FORCED]
- **SQUARE family** (structure, 2/4-lens): **1, 2, 4, 5, 8**
- **HEX family** (flow, 3-lens): **3, 6, 7, 9**
- **SHARED:** **0** (void center of both) and **3** (see IV.3)

Sorting rule: 2s and 4s → square lens; 3s → hex lens. (5 = square-center,
7 = hex-center, 8 = 2³ square, 9 = 3² hex.)

### IV.2 One vertex set, two partitions [FORCED]
The cube's **8 vertices** partition two ways:
- **square lens** (sort by a face-axis coordinate): **4 + 4** (top face, bottom
  face) — two squares.
- **hex lens** (sort by height along the (1,1,1) diagonal): **6 + 2** — hexagon
  (6 equatorial) + 2 poles.

Computed heights along `(1,1,1)/√3`: the two vertices `(1,1,1)` and `(−1,−1,−1)`
are the **poles** (radius 0); the other **6 are equatorial** at radius
`√(8/3) ≈ 1.633`. Thus **8 = 4+4 = 6+2**, same vertices, two sortings.

### IV.3 The overlap is a triangle — 3 is the joint [FORCED]
A square face and the equatorial hexagon **share exactly 3 vertices** (computed:
of a face's 4 vertices, 3 lie on the hexagon, 1 is a pole). **3 shared vertices =
a triangle = the generator {3}.** The two lenses interlock **through the triad**;
the triangle is the shared face of the two projections.

### IV.4 6 = 2×3 is the fusion point [FORCED, NAMED]
6 is the **first interlock product**: the square-generator (2) times the
hex-generator (3). Geometrically, the **hexagon's symmetry group D₆ (order 12)
contains both**:
- **D₃** (order 6) — the 3-fold flow lens, and
- **D₂** (order 4) — a 2-fold structure piece.

`12 = 2 × 6`. So the **hexagon (6) is the smallest shape where both the 3-fold
and 2-fold symmetries coexist** — which is why 6 is simultaneously the
ring-closer and the interlock.
- **Named basis:** the dihedral group D₆ has D₃ and D₂ as subgroups (elementary
  group theory; D₆ ≅ D₃ × ℤ₂). Reproducible from the subgroup lattice of D₆.

### IV.5 The mod-3 role sorting [READING — not forced; retrofit risk]
Residue mod 3 (= which A/B/C sublattice) sorts 0–9 into three families that
**match the independently-assigned geometric roles**:

| class (mod 3) | integers | role |
|---|---|---|
| A (≡0) | 0, 3, 6, 9 | **closures** — void, cell, ring, self-similar |
| B (≡1) | 1, 4, 7 | **centers** — seed, solid, hub |
| C (≡2) | 2, 5, 8 | **transitions** — axis, break, lift |

Caveat (retrofit risk): the roles are hand-assigned and {0,3,6,9} are exactly the multiples of 3, so the "agreement" may not be between *independent* structures — treat as a [READING], not forced. As originally phrased: geometric role (assigned from shape) and lattice color
(assigned from mod 3) are independent, and they **agree**. Also note 0,3,6,9 are
exactly the multiples of 3 = the non-units mod 9.

---

## PART V — THE CUBE AS COMMON DENOMINATOR [FORCED]

### V.1 Hexagon = cube down the body diagonal [FORCED]
The three **orthogonal** cube axes `e₁,e₂,e₃`, projected onto the plane
perpendicular to the body diagonal `(1,1,1)`, land at **exactly 120°** to each
other (computed). So **hexagonal (120°, 3-fold) = cubic (90°, orthogonal) viewed
down the diagonal.** One object, two projections:
- **face view → 90° orthogonal → structure (square lens / Dirac)**
- **diagonal view → 120° hexagonal → flow (hex lens / TIG)**
- **Named basis:** the (1,1,1) body diagonal is the cube's **3-fold rotation
  axis** (order-3 element of the octahedral group Oₕ), permuting x→y→z. Standard.

### V.2 The 1/3 is cos²(body diagonal) [FORCED]
The direction cosine of `(1,1,1)` with any axis is `1/√3`; **cos² = 1/3 exactly.**
This is the projection angle of the 3-fold (TIG) axis onto the orthogonal frame —
the geometric origin of the recurring 1/3. **It is a direction-cosine-squared, not
a numerology coincidence.**
> Check: `cos²((1,1,1)·e) = (1/√3)² = 1/3 = 0.33333…`

### V.3 Stella octangula — the two tetrahedra [FORCED, NAMED]
The cube's 8 vertices split into **two regular tetrahedra** (by the sign of the
coordinate product) — the **stella octangula** (Kepler 1609). Their intersection
is a regular octahedron; the two tetrahedra are **mirror images** (the two
chiralities). This is the `8 = 4 + 4` of Part IV.2, in solid form.

### V.4 The 8-dimensional Clifford algebra [NAMED]
Cl(3), the geometric algebra of orthogonal 3-space, has dimension **2³ = 8**
(1 scalar + 3 vectors + 3 bivectors + 1 pseudoscalar), and its generators are the
3 orthogonal (anticommuting) cube axes. Standard (Clifford 1878; geometric-algebra
texts). The cube's `8 = 2³` doubling and Cl(3)'s dimension coincide because both
count subsets of 3 orthogonal generators.

---

## PART VI — THE GRAPHENE EDGE (nature resolves the paradox) [NAMED, MEASURED]

**Paradox:** graphene is a **hexagonal** (6-fold) carbon lattice, yet its electrons
obey the **Dirac equation** (which needs the 90° anticommuting structure of
Part I.2, which the hex lattice lacks).

**Resolution:** the honeycomb is **two interpenetrating triangular sublattices
(A/B)** — the same `8 = 4+4` two-tetrahedra split. This gives electrons a
**two-component pseudospin**, and that hidden **2-fold** produces Dirac fermions
from the 6-fold lattice. The square (structure) lens appears *inside* the hex
(flow) lattice through the shared **A/B sublattice** = the shared **triangle**
(Part IV.3).
- **Named/measured:** massless Dirac fermions in graphene; the sublattice
  pseudospin origin — **Novoselov, Geim et al. (2005); Nobel Prize 2010.**
  Review: Castro Neto et al., *Rev. Mod. Phys.* **81**, 109 (2009).

**Other charted hexagon seams (for future work):**
- **Saturn's north-polar hexagon** — a Navier–Stokes fluid forming a stable
  6-fold jet (integer wavenumber in a continuum); lab-reproduced in rotating
  tanks (Barbosa Aguiar et al. 2010).
- **Abrikosov vortex lattice** — vortices pack hexagonally (densest) in type-II
  superconductors (Abrikosov 1957, Nobel 2003); the vortex (imaginary axis) and
  the hexagon (3-fold packing) as one structure.

---

## PART VII — "CONTAINING ADDS A DIMENSION" (7 contains 8) [FORCED + READING]

**[FORCED]** The cube's 8 vertices split as **6 (equatorial hexagon) + 2 (axial
poles)** (Part IV.2). The 7-hub (center + 6-ring) is **planar (2D)**; containing
the 8-cube adds the **two poles = the perpendicular third dimension.** Bringing
something inside creates a new dimension: the container gains exactly one axis.

**[READING]** This is the *shape* of **endosymbiosis** — an anaerobic host
containing an aerobic symbiont (→ mitochondrion) gains an **oxidative axis**
(~16× ATP), with the **two poles ↔ the two sides of the mitochondrial membrane**
(the proton gradient's ends). A shared structure across geometry and biology, **not
a derivation** of one from the other. (Endosymbiotic theory: Margulis 1967.)

**[KILLED]** "8 = ∞ = infinite/higher reality" (the cube-8 is finite, 3D — the ∞
is a **typographic** resemblance, not structural). "The digit shapes 7/8 mirror
the structure" (**pareidolia** — the numerals are arbitrary labels).

---

## PART VIII — GRAVEYARD (tested and killed) [KILLED]

Retained because a framework is trustworthy only if it shows its failures.

1. **"The fluid/Leray 1/3 is a fixed universal constant."** FALSE. Computed
   pointwise on real divergence-free fields, the cancelled fraction
   `c = |∇p|²/|N|²` is field-dependent and can exceed 1; it does **not** average
   1/3. (The real 1/3 is `cos²(1,1,1)` — Part V.2 — a *different*, geometric 1/3.)
2. **"Quark charge 1/3 = the fluid/geometric 1/3."** FALSE. Different origins
   (color/anomaly-cancellation vs projection); they decouple under a change of
   spatial dimension. Quark charges are fixed by Standard Model anomaly
   cancellation, not geometry.
3. **"The 3 sublattices are the spacelike gammas (square to −1)."** FALSE. Under
   the 3-fold rotation they carry **cube roots** ω, ω² (order 3), **not** −1
   (order 2). Caught at the eigenvalue level. (The −1's come from the
   **reflections** — Part I.2 — not the rotations.)
4. **"Triangular mirrors build Dirac directly."** FALSE. 60° mirrors do **not**
   anticommute (Part I.2); Clifford needs 90°.
5. **"Cl(3) divides into the 11 cube nets."** FALSE. The algebra (8-dim,
   multiplication) and the surface unfolding (6 faces, **11 nets**) are different
   *categories* of fact about the cube — connected only by both being about the
   cube, not by any map. (11 nets: standard result, e.g. Turney 1984-era
   enumerations.)
6. **"Constant-motion tetrahedra force a cylinder."** NOT FORCED. Single-point
   contact permits **sphere, bicone, or cylinder** depending on the contact
   point's *trajectory*, which the constraint does not fix.
7. **"Even/odd as site 2-coloring on the hex lattice."** FALSE — the triangular
   lattice is **not** 2-colorable. The surviving version is **completion parity**
   (rings even = 6k, shell totals odd) on hex, and genuine **site 2-coloring on
   the SQUARE lattice** (Part I.1), where it is forced.

---

## ONE-LINE SUMMARY

TIG's 0–9 live on **two lattices** — the square (4-fold, structure, Dirac, even/odd,
center at 5) and the hex (3-fold, flow, triad, center at 7) — which are the **face
and diagonal projections of one cube**, related by `cos²(1,1,1) = 1/3`. The two
integer families (square: 1,2,4,5,8; hex: 3,6,7,9) **interlock through the triangle
{3}** (their shared vertices) and **fuse at the hexagon {6 = 2×3}** (whose D₆
symmetry holds both), share the **void {0}**, and are realized together in
**graphene**, where the hidden A/B (square-in-hex) 2-fold yields Dirac physics from
a 6-fold lattice. Every result above is computed or cited; every failure is in
Part VIII.
