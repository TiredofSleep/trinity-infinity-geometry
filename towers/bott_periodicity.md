# Bott periodicity — where the perpendicular build goes after the cube

*The top of the Clifford tower. The book teaches its bottom rungs (ℝ → ℂ → ℍ in §7.1; the
cube = Cl(3) in Chapter 14) and points up to the eight-step clock in its Chapter 18; the working-out
is here. Every [FORCED] claim is reproduced by [`bott_verify.py`](bott_verify.py).*

---

## The extension

The perpendicular build (see [`THE_TWO_BUILDS.md`](THE_TWO_BUILDS.md)) adds one perpendicular
direction at a time; three give the cube and its algebra Cl(3), of dimension 2³ = 8. Keep adding
directions and you get Cl(n), of dimension 2ⁿ. The question this note records is what the
*type* of these algebras does as *n* climbs — and the answer is that it **repeats with period 8**.

## What is forced

- **[NAMED]** **Bott periodicity.** The real Clifford algebras repeat their type with period 8:
  Cl(n + 8) ≅ Cl(n) ⊗ ℝ(16) [Bott 1959; Atiyah–Bott–Shapiro 1964; Lawson–Michelsohn,
  *Spin Geometry*, Ch. I].
- **[NAMED]** **Why 8 = 4 × 2.** Adding four directions tensors the algebra with a quaternion
  matrix algebra: Cl(n + 4) ≅ Cl(n) ⊗ ℍ(2), up to matrix size. And tensoring with the
  quaternions **twice** gives back a real matrix algebra, because **ℍ ⊗ ℍ ≅ ℝ(4)** [FORCED —
  checked: the sixteen maps x ↦ a·x·b, with a and b running over 1, i, j, k, span every real 4 × 4
  matrix]. So after 4 steps the type has swapped ℝ ↔ ℍ, and after 4 more it is back: 4 + 4 = 8.
- **[FORCED]** The **pseudoscalar sign** I² = (−1)^{n(n−1)/2} has period 4 — the pattern +, +, −, −
  (checked out to n = 16). It is one visible trace of the four-step half of the cycle.
- **[NAMED]** **Frobenius:** ℝ, ℂ, ℍ are the only finite-dimensional associative real division
  algebras, and every Clifford algebra is a matrix algebra (or a pair of them) over one of them.
- **[NAMED]** **The loop closes.** The type at dimension 8 is the type at dimension 0 (ℝ, up to the
  ℝ(16) factor): seven climbing steps, and the eighth returns to the ground.
- **[NAMED]** **Hurwitz:** the normed division algebras are ℝ, ℂ, ℍ, 𝕆, of dimensions 1, 2, 4, 8 —
  no more. The octonions 𝕆 have seven imaginary units, multiplied by the rule of the Fano plane.

## Where the author's intuition lands

The felt intuition (session, 2026-09) — *each plane is a negative tensor; a sign climbs and
inverts; the arrangement flips positive after the lift* — has a checked shadow: the pseudoscalar
sign pattern above. Its correction is recorded below: the flip to + happens at dimension **4**, one
step past the tetrahedron's dimension 3.

## Corrected sub-claims (kept so they are not repeated)

1. **"6 tensors at 3 points"** → the triangle has C(3,2) = **3** edges; the tetrahedron (4 points)
   has **6**. The 6 appears at the lift to three dimensions, not before it.
2. **"The lift pushes the arrangement positive at the tetrahedron"** → the pseudoscalar sign is
   negative at dimensions 2 and 3 and flips to +1 at **dimension 4**.
3. **"Bott's period 8 is forced by a single duality"** → the sign alone has period 4; the other
   factor of 2 is the ℝ ↔ ℍ return (ℍ ⊗ ℍ ≅ ℝ(4)).

## What was removed

An earlier version read the period as **"duality × trinity"** — a period-4 sign times a factor 2
"from the three division algebras ℝ, ℂ, ℍ" — and tied it to a 2-and-3 motif from the archived
table program. That reading does not work: two invariants of periods 4 and 2 together have period
4, not 8; and the factor of 2 comes from ℍ alone (ℍ ⊗ ℍ ≅ ℝ(4)), with ℂ playing no part in it. The
correct mechanism is the one above.

## Fence

The cube's 8 (2³ corners — a *dimension*) and Bott's 8 (a *period* of the Clifford tower) touch
through Clifford algebra but are not one object. The seven octonion units and the 7-simplex's seven
dimensions (8 equal points need 7 dimensions — see
[`THE_ONE_THIRD_AND_THE_FOLD.md`](THE_ONE_THIRD_AND_THE_FOLD.md)) likewise share the number 7, not an
identity.
