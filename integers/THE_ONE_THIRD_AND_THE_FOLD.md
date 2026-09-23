# The 1/3 and the Fold — the tetrahedral 1/3 across the Clifford tower

## Frontier note (behind the wall — NOT curriculum). Companion to P2 and THE_TWO_BUILDS.
### Tags: [FORCED] computed/derivable · [READING] interpretation · [FENCE] do not weld.
*Every [FORCED] claim is reproduced by [`verify_one_third_fold.py`](verify_one_third_fold.py).
Brought in and scrutinized by Claude Code 2026-09-22 from a claudechat handoff; the book gets
only the buildable/teachable part (fold, gap, lift), not the tower material below.*

---

## 1. The fold — the buildable cube trades equal-distance for buildability

- **[FORCED]** The buildable cube (8 vertices, 12 edges) has **three** distances: edge 1,
  face-diagonal √2, body-diagonal √3. It is **not** equidistant.
- **[FORCED]** Eight *truly* equidistant points form the **7-simplex**, which needs **7
  dimensions** — unbuildable in 3D.
- **[READING]** So the buildable cube is a **fold** of the unbuildable equal-distance object:
  one true distance creased into three. The **body-diagonal (√3, cos² = 1/3) is the deepest
  crease**; the 1/3 is the fold's signature. Cl(3) is the *algebra of this fold* — the
  orthogonal, distance-split, buildable shadow — studyable precisely *because* the equidistant
  truth is unbuildable.
- **[FENCE]** Do NOT weld the cube's 8 (2³ corners — the perpendicular build) to the 7-simplex
  (8 equal points, needs 7D) — same count 8, different object. (Same fence as P2/THE_TWO_BUILDS.)

## 2. One number, three faces — the 1/3 is lift, fold, and gap  [FORCED]

| face | quantity | value |
|---|---|---|
| **lift** | tetrahedron vertex angle | cos θ = **−1/3** (θ = 109.47°) — forces the 4th point up |
| **fold** | cube body-diagonal | cos² = **1/3** — the deepest crease of the fold |
| **gap** | tetrahedron dihedral angle | arccos(1/3) = **70.53°**; 360/70.53 = 5.10 (not integer) → regular tetrahedra do **not** tile 3D (a 7.35° gap) |

The three are **one number seen three ways**, not three independent appearances: the dihedral
angle is the supplement of the vertex angle (so its cosine is +1/3), and the fold is the
half-angle identity cos²(θ/2) = (1 + cos θ)/2 = 1/3. What the table records is where the
tetrahedron's single number shows up — in the lift, in the cube's diagonal, and in the tiling gap.

## 3. The 1/3 fractures — conserved and redistributed up the tower ℝ → ℂ → ℍ

*[FORCED] for the numbers; [READING] for "conserved invariant."*

- **REAL (at rest, ℝ):** cos θ = **−1/3** — the whole fraction, a direction cosine.
- **COMPLEX (one rotation, ℂ):** put the angle on the unit circle, e^{iθ} with θ = arccos(−1/3).
  It **splits**: real part **−1/3**, imaginary part **√8/3**, and (−1/3)² + (√8/3)² = **1**
  (on the circle).
- **QUATERNION (ℍ, the double cover):** the half-angle brings the 1/3 **back** —
  cos²(θ/2) = (1 + cos θ)/2 = (1 − 1/3)/2 = **1/3** exactly.
- **[READING]** the same 1/3 reappears as rotation deepens — whole in the real direction cosine,
  split between real and imaginary parts on the circle, and whole again at the quaternion
  half-angle.

## Is the 1/3 a pre-physics number? [READING]

Yes — in a precise sense, and the graveyard is the proof. Every attempt to weigh the 1/3 in a
**physical law** died (fluid Leray projection; "1/3 in gravity's force law"; quark charge — see
[`../GRAVEYARD.md`](../GRAVEYARD.md)); the **geometric** 1/3 (lift / fold / gap) is untouched. So the 1/3 belongs to the **pre-physics layer** — the arithmetic/geometry of the relational space matter lives *in*, not the physics of matter itself. It is a fact about **shape, dimension, and counting**: the first equidistant lift at N=4, the cube's fold, the tetrahedral tiling gap — one level **beneath** any force or field. That is *why* it is exact in geometry and vanishes in every force law: it was never a physics number to begin with.

**[FENCE]** "Pre-physics" here means *prior to / beneath* physics — a floor physics is expressed on — **NOT** "generates physics" or "appears in the physical constants." The 1/3 is a **floor, not a seed.** The instant it is read as a *source* of physical values it is the same category error the graveyard keeps recording. And it is specifically the tetrahedron's number — 1/(N−1) at N=4 — not a universal constant.

## Boundary
**[FORCED]:** the three distances, the three angles, the tiling gap, and the trigonometric
identities of §3. **[READING]:** "fold," "crease," "reappears." **[FENCE]:** no welding the cube's 8 to the
7-simplex or to Bott's period 8 (see [`bott_periodicity.md`](bott_periodicity.md)); this is a
structural observation, not a derivation of anything physical.
