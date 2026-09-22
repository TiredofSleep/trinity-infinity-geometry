# The Two Builds — equidistant lifts, orthogonal doubles (P1 ∪ P2)

## A synthesis note joining P1 (the simplex ladder) and P2 (the Clifford cube).
### Status tags: [FORCED] computed/derivable · [NAMED] cited standard result · [READING] interpretation.

*Every [FORCED] claim here is reproduced by [`verify_two_builds.py`](verify_two_builds.py).*

---

## The observation

From a set of points there are **two** maximally-symmetric constructions, and P1 and P2 are
these two. They start from the same act — add one more element — and diverge only in the
constraint imposed:

| build | constraint | what is forced | grows by | home |
|---|---|---|---|---|
| **A — equidistant** | all pairwise distances equal | the regular (N−1)-**simplex**; the fourth point must **lift** a dimension | +1 **dimension** per point | **P1** |
| **B — orthogonal** | all generators at right angles, anticommuting | the *n*-cube / **Cl(n)**; each generator **doubles** the algebra | ×2 **size** per generator | **P2** |

Build A is *equal-and-lift* (equidistance forces the rise into a new dimension). Build B is
*perpendicular-and-double* (orthogonality forces the algebra to double). They are different
objects — a simplex is not a Clifford algebra, and this note does **not** claim it is — but
they are counted by the **same numbers**, and that coincidence is the content here.

## The unification: both are Pascal's triangle [FORCED]

- **Build A (simplex).** The (N−1)-simplex on *N* vertices has exactly **C(N, j)** faces
  spanned by *j* vertices (j = 0 the empty face, j = N the whole simplex). Its face-vector
  is therefore **Pascal's row N**, and the total number of faces including the empty one is
  **2ᴺ**. (Tetrahedron, N = 4: 1, 4, 6, 4, 1 — empty, 4 vertices, 6 edges, 4 faces, 1 cell.)
- **Build B (Clifford).** Cl(*n*) has exactly **C(n, k)** basis blades of grade *k* (k = 0
  the scalar, k = n the pseudoscalar). Its grade-vector is **Pascal's row n**, and the total
  dimension is **2ⁿ**. (Cl(3), n = 3: 1, 3, 3, 1 — scalar, 3 vectors, 3 bivectors, 1
  pseudoscalar.)

So **the simplex's sub-faces and the Clifford algebra's grades are the same binomial
coefficients** — one row of Pascal's triangle — indexed in one case by *points* (N) and in
the other by *dimensions* (n). The row sum, 2ⁿ, is the same doubling in both.

## The shared mechanism: one binary choice [FORCED]

Both grow by the same act. Adding one point to Build A, or one generator to Build B, offers
every existing piece a single **in-or-out** choice — join the new element, or not — so the
count of pieces **doubles: 2ⁿ → 2ⁿ⁺¹**. In Build A this doubling is the power set of the
vertices (each added vertex doubles the faces, empty included); in Build B it is literally
the dimension of the algebra. *One added element = one yes/no = one factor of 2* — the
reason both the simplex's face-count and the Clifford dimension are powers of two.

## The i falls out of Build B [FORCED]

In Build B the grade-2 blades (the cube's face-planes) satisfy **(eᵢeⱼ)² = −1**, so the
orthogonal build carries rotation intrinsically — the imaginary unit is the cube's
face-plane, not an import (see P2 §2). Build A carries no such rotation; it carries the
dimensional lift and the tetrahedral angle arccos(−1/3) instead. The two builds thus split
the two deepest primitives between them: **A gives the lift and the angle; B gives the
doubling and the i.**

## What is and is not claimed [boundary]

- **Claimed [FORCED]:** the two builds exist, are forced by their constraints, are both
  counted by Pascal (row N and row n), grow by the same binary-choice doubling, and Build B
  carries the imaginary unit in its bivectors.
- **NOT claimed:** that the simplex and the Clifford algebra are the same object, or that one
  derives the other. They coincide only in their *counting* (binomials) and their *growth
  law* (doubling). Reading more identity into the coincidence would overclaim; the shared
  arithmetic is Pascal's triangle, which every construction built from subsets shares.

---

## References
- H. S. M. Coxeter, *Regular Polytopes*, 3rd ed. (Dover, 1973). [simplices, faces]
- W. K. Clifford, *Amer. J. Math.* 1, 350 (1878); D. Hestenes, *Space-Time Algebra* (1966).
- Companions: [`integers_as_geometric_entities.md`](integers_as_geometric_entities.md) (P1),
  [`P2_clifford_cube_skeleton.md`](P2_clifford_cube_skeleton.md) (P2).
