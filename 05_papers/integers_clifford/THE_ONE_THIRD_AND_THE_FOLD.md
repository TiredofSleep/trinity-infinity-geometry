# The 1/3 and the Fold — the tetrahedral 1/3 across the Clifford tower

## Spine-B frontier note (behind the wall — NOT curriculum). Companion to P2 and THE_TWO_BUILDS.
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
- **[FENCE]** Do NOT weld framework-8 (cube = 2³, a **dimension**) to the 7-simplex (8 equal
  points, needs 7D) — same count 8, different object. (Same fence as P2/THE_TWO_BUILDS.)

## 2. One number, three faces — the 1/3 is lift, fold, and gap  [FORCED]

| face | quantity | value |
|---|---|---|
| **lift** | tetrahedron vertex angle | cos θ = **−1/3** (θ = 109.47°) — forces the 4th point up |
| **fold** | cube body-diagonal | cos² = **1/3** — the deepest crease of the fold |
| **gap** | tetrahedron dihedral angle | arccos(1/3) = **70.53°**; 360/70.53 = 5.10 (not integer) → regular tetrahedra do **not** tile 3D (a 7.35° gap) |

## 3. The 1/3 fractures — conserved and redistributed up the tower ℝ → ℂ → ℍ

*[FORCED] for the numbers; [READING] for "conserved invariant."*

- **REAL (at rest, ℝ):** cos θ = **−1/3** — the whole fraction, a direction cosine.
- **COMPLEX (one rotation, ℂ):** put the angle on the unit circle, e^{iθ} with θ = arccos(−1/3).
  It **splits**: real part **−1/3**, imaginary part **√8/3**, and (−1/3)² + (√8/3)² = **1**
  (conserved, on the circle). [READING] the real part is the *fold* (1/3); the imaginary part
  carries the *8* (the cube).
- **QUATERNION (ℍ, the double cover):** the half-angle brings the 1/3 **back** —
  cos²(θ/2) = (1 + cos θ)/2 = (1 − 1/3)/2 = **1/3** exactly.
- **[READING]** the 1/3 is a *conserved invariant* wearing real / complex / quaternion masks as
  rotation deepens; not "more complex," the **same 1/3 redistributed** (the fold and the cube —
  the 1/3 and the 8 — are the two halves of one rotation).

## Boundary
**[FORCED]:** the three distances, the three angles, the tiling gap, and the trigonometric
identities of §3. **[READING]:** "fold," "crease," "conserved invariant," the real/complex
carry of fold/cube. **[FENCE]:** no welding framework-8 to the 7-simplex or to Bott-8 (see
[`bott_periodicity_2x3.md`](bott_periodicity_2x3.md)); this is a structural observation, not a
derivation of anything physical.
