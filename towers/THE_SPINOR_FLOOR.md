# The spinor floor — Cl(2n) is every operator on 2ⁿ states

*A floor of the Clifford tower, between "Cl(n) has 2ⁿ pieces" and Bott's clock at the top. The tower
names spinors as where it goes; this floor builds them. Everything here is classical. It comes from
auditing the archived
[J20](https://github.com/TiredofSleep/trinity-infinity-geometry/tree/archive-2026-09-24/05_papers/algebra/J20),
which found both Pascal rows below and called the second one a coincidence. Every [FORCED] claim is
checked by [`verify_spinor_floor.py`](verify_spinor_floor.py) (23 checks, about a second).*

Tags: **[FORCED]** proved here and checked by the script · **[NAMED]** a classical result, cited ·
**[READING]** an interpretation · **[FENCE]** a physics reading, not a claim.

---

## The floor below

The perpendicular build gives Cl(*m*): *m* directions that square to 1 and anticommute. It has 2ᵐ
pieces, graded by Pascal's row *m* ([`THE_TWO_BUILDS.md`](THE_TWO_BUILDS.md)). This floor takes an even
number of directions, *m* = 2n, and asks what Cl(2n) **acts on**.

## What is forced

- **[FORCED] Two directions per switch.** Take *n* two-state switches. Their joint states are the
  *n*-bit strings, 2ⁿ of them: the corners of the *n*-cube. With the Pauli matrices X, Y, Z, put

  > γ_{2j−1} = Z ⊗ … ⊗ Z ⊗ X ⊗ 1 ⊗ … ⊗ 1,   γ_{2j} = Z ⊗ … ⊗ Z ⊗ Y ⊗ 1 ⊗ … ⊗ 1,

  with j − 1 factors Z in front (Jordan and Wigner, 1928). These 2n matrices, each 2ⁿ × 2ⁿ, satisfy
  γ_aγ_b + γ_bγ_a = 2δ_ab. They are 2n perpendicular directions, the generators of Cl(2n). [checked for
  n = 1 … 5]

- **[FORCED] The algebra is every operator on the states.** The 4ⁿ products γ_S, one for each subset S
  of the generators, form an orthogonal basis of **all** 2ⁿ × 2ⁿ complex matrices. So over ℂ, Cl(2n) is
  the full matrix algebra on the 2ⁿ states, and

  > 4ⁿ = (2ⁿ)².

  The 2ⁿ states are the **spinors**. The products of *k* generators number C(2n, k): Pascal's row 2n
  grades the algebra, as on the floor below. [checked for n = 1 … 5; NAMED in general: Brauer and Weyl
  1935, Chevalley 1954, Lawson and Michelsohn Ch. I]

- **[FORCED] Pascal's row n grades the spinors.** The switch operators a_j = (γ_{2j−1} + iγ_{2j})/2 obey
  a_i a_j† + a_j† a_i = δ_ij and a_i a_j + a_j a_i = 0. Their count N = Σ a_j†a_j reads off the number of
  1s in a string. The states with *k* ones number C(n, k), and they are built from 00…0 by *k* raising
  steps; this is the exterior power Λᵏ(ℂⁿ) of the classical construction [NAMED: Chevalley 1954].

  So **both** Pascal rows belong to Cl(2n): row 2n counts the algebra's pieces by grade, and row n counts
  the spinors by their number of 1s.

- **[FORCED] Two half-spinors, and the coin.** The chirality Γ = (−i)ⁿ γ₁γ₂⋯γ_{2n} equals Z ⊗ Z ⊗ … ⊗ Z.
  It is +1 on strings with an even number of 1s and −1 on the odd ones, so it splits the spinors into two
  halves of 2ⁿ⁻¹ states.
  - Γ anticommutes with every generator, so conjugation by Γ is the **grade flip** v → −v: the Clifford
    tower's coin.
  - The even part of the algebra keeps each half, and each odd element swaps them.

  *Proof of the formula:* γ_{2j−1}γ_{2j} = i Z_j, and the product of these n pairs is iⁿ Z ⊗ … ⊗ Z.

- **[FORCED] On the cube (n = 3).** The 8 spinor states are the cube's corners, 000 to 111, and Cl(6)
  acts on them.
  - Their layers by number of 1s are 1, 3, 3, 1: the cube's layers, seen down its long diagonal.
  - The two half-spinors are {0, 3, 5, 6} and {1, 2, 4, 7}. Each is a regular tetrahedron, with all
    distances √2: the cube's two tetrahedra.
  - The central inversion b → 111 − b swaps them.

  So the cube's two tetrahedra appear twice on this tower: as the even and odd pieces of Cl(3), which is
  the ground floor's coin, and as the two half-spinors of Cl(6).

- **[NAMED] Over the reals, Bott decides.** With eᵢ² = +1:

  | | Cl(2,0) | Cl(4,0) | Cl(6,0) | Cl(8,0) |
  |---|---|---|---|---|
  | algebra | ℝ(2) | ℍ(2) | ℍ(4) | ℝ(16) |

  Cl(2,0) = ℝ(2) is checked here, since X and Z are real [FORCED]. With 2n directions the real algebra
  is a full real matrix algebra, ℝ(2ⁿ), when 2n ≡ 0 or 2 (mod 8), and quaternionic, ℍ(2ⁿ⁻¹), when
  2n ≡ 4 or 6 (mod 8). That is Bott's eight-step clock: see [`bott_periodicity.md`](bott_periodicity.md).
  Over ℂ the square law above holds for every *n*.

- **[FENCE] A physics reading.** The switches are fermion occupation numbers: the spinor space is the
  state space of *n* fermion modes, and the γ's are its Majorana operators (Jordan and Wigner, 1928). This
  is a reading, not a claim of this floor. Readings of n = 5 as grand unification stay archived.

## Where it came from

J20 counted the 4ⁿ basis lines of a tensor power by 2n bits, which gives Pascal's row 2n, the grades of
Cl(2n). It counted its 2ⁿ "coarse cells" by n bits, which gives row n. It called the n = 5 numbers
1, 5, 10, 10, 5, 1 a binomial coincidence. They are not a coincidence:
- row 2n grades the algebra;
- row n grades its spinors;
- [READING] the coarse cells are the 2ⁿ columns of the 2ⁿ × 2ⁿ matrices, each a copy of the spinor
  space, once each slot's four basis lines are named by a pair of bits, one for the row and one for the
  column. (Every column of a full matrix algebra is kept by left multiplication; checked for n = 3.)

J20's own 4-dimensional algebra, from the archived table program, plays no part: any 4-dimensional space
gives the same counts. Its open question O1 asked for a structure-preserving map from the tensor power of
that algebra to Cl(2n). None can keep multiplication and be one-to-one. The algebra is commutative, by
J20's own description, so its tensor powers are commutative too. They have dimension 4ⁿ, the same as
Cl(2n), so such a map would be onto, and Cl(2n) would be commutative, which it is not.

## Sources

- P. Jordan and E. Wigner, "Über das Paulische Äquivalenzverbot", *Z. Phys.* **47** (1928) 631–651.
- R. Brauer and H. Weyl, "Spinors in n dimensions", *Amer. J. Math.* **57** (1935) 425–449.
- C. Chevalley, *The Algebraic Theory of Spinors*, Columbia University Press (1954).
- H. B. Lawson and M.-L. Michelsohn, *Spin Geometry*, Princeton University Press (1989), Ch. I (the
  classification, and Cl_{2m} ⊗ ℂ ≅ ℂ(2ᵐ)).
- J. Baez and J. Huerta, "The algebra of grand unified theories", *Bull. AMS* **47** (2010) 483–552,
  arXiv:0904.1556: the 32 = 1 + 5 + 10 + 10 + 5 + 1 split of the Spin(10) spinor. It is cited only to show
  that J20's "coincidence" is classical; its physics stays out of this repository.
