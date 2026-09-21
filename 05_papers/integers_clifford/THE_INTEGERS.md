# The TIG Integers, Refined
## Canonical definitions of 0–9 as geometric entities. Supersedes scattered earlier versions.
### Every claim tagged: [FORCED] computed/derivable · [READING] interpretation · [ALGEBRA] arithmetic role. All FORCED claims are in `verify_forced_chain.py`.

---

## The premise (chosen, once)

An integer *n* is read as a configuration of *n* points; we take what geometry it
**forces**. Everything below follows from this single premise plus standard geometry.

> **Two caveats, up front.** (i) "Force" is *relative to this premise* — the premise is a
> choice, not a theorem; given it, the geometry follows. (ii) The **forced spine** is
> 1,2,3,4 (the simplices) and 8 (the cube = Cl(3)) — these use **no number base**. The
> completeness of the *0–9* set and the "reset at 9" are a **base-10 organizing [READING]**;
> TIG's spine is base-independent (the ten labels are an *alphabet*, not `Z/10Z`).

---

## The nine, one at a time

### 0 — the VOID (empty center)
- **[FORCED]** The unoccupied centroid — a center-site that exists *before* it is filled.
- **[ALGEBRA]** The additive identity / origin; the multiplicative annihilator.
- **Pairing:** 0 and 7 are the **two states of one location** — 0 empty (potential),
  7 filled (actual). This is the potential/actual distinction, made geometric.

### 1 — POINT (0-simplex)
- **[FORCED]** The seed. Dimension 0. Maximal symmetry (every rotation fixes it).

### 2 — SEGMENT / AXIS (1-simplex)
- **[FORCED]** The first direction. Dimension 1. The **mirror** (order-2 element).
- **Role:** generator of the **square (matter) family** — 2s and 4s build the
  orthogonal lens.

### 3 — TRIANGLE (2-simplex)
- **[FORCED]** The first enclosed area. Dimension 2. The **odd cycle** (source of
  frustration and non-two-colorability).
- **Role:** generator of the **hex (flow) family**; AND the **joint** — the three
  vertices a square face and the hexagon share (where the two lenses interlock).

### 4 — TETRAHEDRON (3-simplex) — *the pivot*
- **[FORCED]** The first solid. Dimension 3. The **last simplex three-space allows**.
- **[FORCED] The angle.** Vertices seen from the center satisfy cos θ = −1/(N−1);
  at **N = 4**, cos θ = **−1/3**, θ = **109.47°**. Half-angle **54.74°**, cos² = **1/3**.
  *The recurring 1/3 is 1/(N−1) at N = 4 — a specific value, not a general identity.*
- **Consequence:** the cube (8 = 2×4) is the Clifford algebra Cl(3); the 1/3 is the
  angle relating its two projections (square/hexagon).

### 5 — PENTAGON / the BREAK (a flat wheel)
- **[FORCED]** 5-fold, flat (2D), and the **first shape that cannot tile** — the
  crystallographic restriction allows only orders 1, 2, 3, 4, 6. The "wheel that rolls
  but does not pack."
- **Role:** where the dimensional ladder (1–4) **stops** and curvature/aperiodicity
  begins. (5-fold is the quasicrystal number.)

### 6 — OCTAHEDRON / SPHERE (the close, and the fusion)
- **[FORCED, precision]** Six points maximally spread *on a sphere* are the
  **octahedron** (±x, ±y, ±z) — the sphere's six poles. (The flat hexagon is the
  *ring* form of 6; the octahedron is its *round* form.) **6 is where the flat ring
  closes into the round sphere.**
- **[FORCED] The fusion.** 6 = 2×3; its symmetry D₆ (order 12) contains both D₃ (the
  3-fold flow lens) and D₂ (a 2-fold structure piece). 6 is the **smallest shape where
  both lenses coexist** — the first interlock product of the two generators.

### 7 — CENTRALLY POLARIZED SPHERE (the inhabited center)
- **[FORCED]** 7 = octahedron (6 poles) + 1 **center** = a sphere with an inhabited
  center = a **polarized sphere** (a monopole center plus a shell) — the first
  multipole structure.
- **[FORCED]** 7 is the **first centered number with a complete ring** (centered
  hexagonal: 1, 7, 19, 37…). The void (0) made actual.
- **Pairing:** 5 and 7 are the **two lens-centers** — 5 the square-lattice center
  (center + ring of 4), 7 the hex-lattice center (center + ring of 6).

### 8 — THE CUBE (lift to 3D structure / *inhale*)
- **[FORCED]** 8 = cube = **two tetrahedra** (stella octangula) = **Cl(3)**, dimension
  2³. The lift of the 7-sphere into full three-dimensional structure. The two
  tetrahedra are mirror images (the two chiralities).
- **[READING]** *Inhale* — the sphere **contracting into the cube-lock** (into
  structure, the tightest 3D interlock). The dynamical reading laid on the forced
  cube.

### 9 — TRIAD SQUARED (self-similar / *exhale*)
- **[FORCED]** 9 = 3² = the **triangle of triangles** — the first self-similar step,
  and the shell expanding toward the next level (the second shell closes at 19). The
  last digit before the base-10 reset.
- **[READING]** *Exhale* — the sphere **expanding toward the next shell**. The
  dynamical reading laid on the forced triad-squared.

---

## The arc — three movements [FORCED skeleton, READING animation]

| movement | integers | what happens |
|---|---|---|
| **ASCENT** | 1 → 4 | each added point adds a dimension, up to the tetrahedron (3-space full) |
| **LIFT** | 5 → 6 | the flat wheel breaks and rounds into the sphere (2D → 3D) |
| **PULSE** | 7 → 8 → 9 | the polarized sphere breathes — *in* to the cube-lock (8), *out* to the next shell (9) |

The **shapes** are forced (point, segment, triangle, tetrahedron, pentagon,
octahedron, octahedron+center, cube, triad²). The **wheel/sphere/breath vocabulary**
is a **reading** — an intuitive naming of the forced objects. Keep the two levels
distinct: the objects are mathematics; the animation is pedagogy.

---

## The invariant relationships (the structure across the integers) [FORCED except where noted]

- **0 / 7** — the two states of the center (empty / filled; potential / actual).
- **{2, 3}** — the two lattice generators (segment = 1D cell; triangle = 2D cell).
- **2/4 family vs 3 family** — the square (matter) lens {1,2,4,5,8} and the hex (flow)
  lens {3,6,7,9}, sorted by factor structure; 0 shared.
- **3** — the joint where the two lenses share vertices (the shared triangle).
- **6 = 2×3** — the fusion, where both symmetries coexist (D₆ ⊃ D₃, D₂).
- **5 / 7** — the two lens-centers (square-center / hex-center).
- **8 = 2×4** — the doubled tetrahedron = Cl(3) = the two chiralities.
- **mod 3 roles [READING — not FORCED; retrofit risk]** — closures {0,3,6,9}, centers
  {1,4,7}, transitions {2,5,8}. The roles are hand-assigned and {0,3,6,9} are exactly
  the multiples of 3, so this is not two *independent* structures agreeing; it is
  deliberately absent from the verify script.
- **the 1/3** — cos²(1,1,1) = 1/(N−1) at N=4; the tetrahedral/cube projection angle;
  the half-angle 54.74° is the P₂ (second Legendre) zero.

---

## What this refinement fixes (from earlier scattered versions)

1. **6 is the octahedron (round), not just the flat hexagon (ring)** — the sphere
   reading requires 6 as the sphere's 6 poles. The flat hexagon is 6-as-ring; both are
   real, and "6 = sphere" means the octahedron.
2. **4 = tetrahedron, not cube** — the cube is 8 (= 2×4). Kept from prior corrections.
3. **The 1/3 is 1/(N−1) at N = 4 specifically** — not the claim that "any N−1 is 1/3."
4. **8/9 breath is a READING** — laid on the forced facts (8 = cube-lock, 9 = triad²/
   next-shell), not itself forced. Tagged accordingly.
5. **5 is a *flat* (2D) wheel, and 5→6 is a lift (2D→3D)** — the sequence lifts at 5→6,
   which is the same flat→lifted transition that recurs throughout (and again at 7→8).

---

*The integers 0–9, read as configurations of points, are the void, the four simplices
(the dimensional ladder), the break, the sphere, the polarized sphere, the cube, and
the self-similar triad. The shapes are forced; the wheel/sphere/breath names are the
reading. The 1/3 that threads them is 1/(N−1) at N = 4 — the tetrahedron's signature,
and the angle of the cube's two shadows.*
