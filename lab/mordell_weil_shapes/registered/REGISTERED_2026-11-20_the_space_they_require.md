# Registered before looking: a lattice and its opposite, at rank 3

Written 2026-11-20, about 23:27 US Central. No rank-3 curve has been examined in this work.

**Question (Claude):** the opposite of a loop is a row of points and the opposite of that is a loop again;
what is its own opposite? **Answer (Brayden, 23:23):** "The space those points require."

**What is exact in it (classical).** In the sequence ℤ → ℝ → ℝ/ℤ the points (ℤ) and the loop (ℝ/ℤ) are dual
to each other and the space between them (ℝ) is dual to itself. The same holds for the rationals inside the
adeles, which is where the zeta function's flip s ↔ 1 − s comes from (Tate). For a Mordell–Weil lattice Λ
the space is E(ℚ) ⊗ ℝ with the height form; the room each point requires is the covolume, whose square is
the regulator; and the lattice's opposite is the dual lattice Λ*, with Gram matrix the inverse.

**Why rank 2 could not show this.** Every 2-dimensional lattice has the same shape as its dual. So in rank 2
packing density and dual packing density are identical, curve by curve. In rank 3 they differ: the dual of
the face-centred cubic lattice (the densest packing, 0.7405) is the body-centred cubic (0.6802).

**The test, and why it needs no null.** Taking duals preserves the natural uniform measure on lattice
shapes. So under any model that does not distinguish a lattice from its opposite, the packing density of Λ
and of Λ* have the same distribution, and the mean paired difference is zero.

- **Q1 (two-sided).** For rank-3 optimal curves in Cremona's tables, the mean of
  density(Λ) − density(Λ*) differs from zero by more than three standard errors.
- **Claude's expected direction, stated now:** positive. A floor on the height of a point keeps the shortest
  vector of Λ long; nothing comparable protects Λ*. Brayden gave no direction.
- **Sanity check to run alongside:** the same paired difference at rank 2 must be zero to rounding.
- **Miss:** within three standard errors of zero.

Density in dimension 3: (π/6) · m^(3/2) / √det, with m the minimum of the quadratic form.

---

# Outcome (`scripts/rank3_lattice_vs_dual.py`; registered 23:24 CST, computed after)

All 8 899 rank-3 optimal curves with conductor below 500 000. The shortest-vector routine (LLL, then all
coefficient vectors in [−4, 4]³) was cross-checked against brute force over [−9, 9]³ on every tenth curve,
for the lattice and its dual: 0 mismatches in 889. Rank-2 sanity check: density and dual density agree to
3 × 10⁻¹⁶ on 2 000 curves, as they must.

| | mean packing density |
|---|---|
| the Mordell–Weil lattice Λ | 0.3055 |
| its opposite Λ* | 0.3179 |
| paired difference | **−0.0123**, s.e. 0.0008, **−15.6 standard errors** |

- **Q1 (two-sided): pass.** The lattice and its opposite are not interchangeable.
- **Claude's stated direction: wrong.** The opposite lattice packs better, not worse. The lattice is the
  denser of the two in only 42.9% of curves.
- Stable across the tables: −0.0138, −0.0135, −0.0117 in three conductor ranges; −0.0120 for trivial
  torsion (8 411 curves), −0.0184 with torsion (488).

**Reading, formed after the result.** The dual lattice is the lattice of characters of the torus
(E(ℚ) ⊗ ℝ)/Λ, the "loop" side of the duality. Brayden's sentence two hours earlier was "angles don't pack,
only curves that can loop." Read through the duality, that sentence gives the direction that was observed
and that Claude bet against. He was not asked for a direction and gave none for this test, so this is a
fit noticed afterwards, not a prediction scored.

**What it means in standard terms.** Rank-3 Mordell–Weil lattices over ℚ lean toward shapes whose duals pack
well, that is, toward the body-centred side rather than the face-centred side. Equivalently they are
somewhat better at covering than at packing. A height floor alone predicts the opposite sign, which is why
the stated expectation failed; so this is a second observation the floor explanation does not produce.

**Next, to register:** (1) the same paired test at rank 4 (Cremona's tables have very few; LMFDB has more);
(2) the full shape distribution in rank 3 against the uniform measure, using covering density as well as
packing density; (3) whether the sign is predicted by the Park–Poonen–Voight–Wood model or by Delaunay's
heuristics, either of which may already imply an asymmetry between Λ and Λ*.
