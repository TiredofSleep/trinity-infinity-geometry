# One group, two faces — S₄ in space

*A floor of the symmetry tower. The tower names S₄ as the rotation group of the cube. This floor shows
that the tetrahedron's full symmetry group, mirrors included, is the same group acting on space in a
second way, and that the base's own central inversion turns one action into the other. Everything here
is classical. It comes from auditing the archived
[J43](https://github.com/TiredofSleep/trinity-infinity-geometry/tree/archive-2026-09-24/05_papers/physics/J43),
which computed one of the two faces and printed the other's name. Every [FORCED] claim is checked by
[`verify_two_faces_of_s4.py`](verify_two_faces_of_s4.py) (7 checks, about a second).*

Tags: **[FORCED]** proved here and checked by the script · **[NAMED]** a classical result, cited.

---

## Two shapes, one group

- **[FORCED] The tetrahedron's face.** Take the tetrahedron on alternate corners of the cube: (1,1,1),
  (1,−1,−1), (−1,1,−1) and (−1,−1,1). It has 24 symmetries, the group T_d:
  - 12 rotations;
  - 6 mirrors;
  - 6 rotary reflections, each a quarter-turn followed by a reflection.

  Each symmetry permutes the 4 corners, and each of the 24 permutations of 4 things happens exactly
  once. So T_d is S₄.
- **[FORCED] The cube's face.** The cube has 24 rotations, the group O. Each one permutes the cube's 4
  long diagonals, and again each permutation happens exactly once. So O is S₄ too.

One abstract group acts on space in two ways. In the first, the odd permutations are mirror-type and
reverse handedness (det = −1). In the second, every element is a rotation (det = +1).

## The twist between them

- **[FORCED] Keep the even symmetries of the tetrahedron, and compose each odd one with the central
  inversion x → −x.** The result is exactly the cube's rotation group. The base already meets this
  inversion: it is the flip that swaps the cube's two tetrahedra
  ([`../base/THE_INTEGERS.md`](../base/THE_INTEGERS.md)).
  - A mirror becomes a half-turn about an axis through the midpoints of two opposite edges of the cube.
  - A rotary reflection becomes a quarter-turn.

  *Proof.*
  - The inversion −I commutes with everything, and det is multiplicative, so g ↦ det(g)·g respects
    products.
  - Every twisted element has det = +1, so it is a rotation.
  - No two symmetries of the tetrahedron differ by the inversion, because the inversion carries the
    tetrahedron to the other one. So the 24 twisted elements are distinct, and they are all of O.
  - The inversion fixes every line through the centre, so a symmetry and its twist permute the four
    diagonals in the same way.

- **[FORCED] The two faces as characters.** Take traces on the classes e, (ij), (ijk), (ij)(kl), (ijkl):

  | face | traces | det | Young diagram |
  |---|---|---|---|
  | the tetrahedron's (T_d) | 3, 1, 0, −1, −1 | the sign of the permutation | [3,1], the standard representation |
  | the cube's (O) | 3, −1, 0, −1, 1 | +1 | [2,1,1] = [3,1] ⊗ sign |

## The coin [FORCED]

The **sign twist**, ρ ↦ sign ⊗ ρ, is a flip on representations. It multiplies the matrices of the odd
permutations by −1 and leaves the even ones alone.

- **The two sides** are the two faces: the tetrahedron's way and the cube's way of letting S₄ act on
  space.
- **The edge**, read on the group, is where the two faces agree: the 12 even permutations, A₄. These
  are the tetrahedron's rotations, and they act by the same matrices in both faces. On the 12 odd
  permutations the two faces are exact negatives.
- **On S₃,** the six permutations that fix one point, the two faces split differently. The
  tetrahedron's face splits as A₁ ⊕ E: the trivial representation plus the triangle's 2-dimensional
  one. The cube's face splits as A₂ ⊕ E: the sign plus the same 2-dimensional piece.
- **On all five irreducible representations of S₄,** the twist transposes the Young diagram. It swaps
  [4] ↔ [1,1,1,1] and [3,1] ↔ [2,1,1]. Its edge there is [2,2], the only one it fixes: the
  2-dimensional representation in which S₄ acts through the cube's three axes.

## Where you meet it

- **[NAMED] Chemistry's two names.** The three p-orbitals (x, y, z) are labelled T₂ in a tetrahedral
  molecule (T_d) and T₁ in an octahedral one (O; t₁ᵤ in O_h). Both labels name one representation, seen
  from the two faces. [FORCED: the traces of (x, y, z) match the T₂ row of the T_d table and the T₁ row
  of the O table, class by class]
- **[FORCED] Where J43 slipped.** J43 computed the tetrahedron's face, (3, 1, 0, −1, −1), and called it
  "[2,1²]", the cube's. Under that name its own Theorem 2.1 would fail, since [2,1,1] restricted to S₃
  is A₂ ⊕ E, not A₁ ⊕ E. The two faces are easy to confuse because the group is the same; what differs
  is the action.

## What is not claimed

Nothing here is new: the twist is a standard textbook construction (see *Octahedral symmetry* below).
J43's physics, an "S₄ synthesis" on a nitrogen-vacancy qutrit, stays archived:
- any three-level system with full control carries every 3-dimensional representation;
- its printed pulse table does not compile its own target (best residual 1.27 over all pulse orders);
- its "24-element closure" check is a round trip, V⁻¹(VMV⁻¹)V = M, which any change of basis passes;
- the transitions it calls "electric-dipole" are magnetic-dipole (spin resonance).

## Sources

- W. Fulton and J. Harris, *Representation Theory: A First Course*, Springer GTM 129 (1991), §2.3 (the
  character table of S₄; V and V ⊗ sign).
- J.-P. Serre, *Linear Representations of Finite Groups*, Springer GTM 42 (1977), §§5.8–5.9 (S₄, and the
  group of the cube).
- *Octahedral symmetry*, Wikipedia: <https://en.wikipedia.org/wiki/Octahedral_symmetry>. It builds T_d
  from the rotations T and the inversion, exactly as above.
- F. A. Cotton, *Chemical Applications of Group Theory*, 3rd ed., Wiley (1990), Appendix IIA (the T_d,
  O and O_h character tables).
