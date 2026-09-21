# Integers as Geometric Entities
## The forced geometry of the first integers, and where it meets the physical world
### Brayden Sanders. September 2026.

---

## Abstract

We develop a single premise — that an integer *n* may be read as a configuration
of *n* points — and follow what geometry it *forces*, distinguishing at every step
what is compelled by the premise from what is interpretation. The first four
positive integers are shown to be the simplices (point, segment, triangle,
tetrahedron), so that *the addition of a unit is the addition of a dimension* up to
the tetrahedron, where three-dimensional space is full. A forced algebraic identity
— the angle between the vertices of a regular *N*-simplex, seen from its center, has
cosine −1/(*N*−1) — yields, for the tetrahedron (*N* = 4), the value **−1/3** and the
tetrahedral angle **arccos(−1/3) = 109.47°**, whose half-angle **arccos(1/√3) =
54.74°** satisfies **cos² = 1/3**. This recurring **1/3** is therefore not a
numerical coincidence but the reciprocal 1/(*N*−1) for *N* = 4. We then observe, as
*illustration and not as derivation*, that this same geometry organizes a striking
range of measured phenomena — the tetrahedral bond angle of carbon, the transition
between its flat (graphene) and lifted (diamond) forms, and the "magic angle" of
nuclear magnetic resonance at which directional (rank-2) structure vanishes. The
paper is explicit throughout about the boundary between forced mathematics and
interpretive framing, and records what does *not* follow.

---

## 1. The premise and the method

There is a long habit, older than formal mathematics, of seeing number and shape as
one thing: the Pythagorean figurate numbers (triangular, square, pentagonal) counted
dots arranged in patterns [Heath 1921]. We take up a disciplined version of that
habit and press it for exactly what it forces.

**Premise.** An integer *n* is read as a configuration of *n* points, and we ask what
geometric structure is *compelled* by that reading.

This premise is a *definition*, not a theorem; it is the one thing chosen. The method
is then strict: each subsequent claim is tagged **[forced]** (compelled by the
premise, computable, reproducible), **[named]** (resting on a cited standard result),
or **[interpretation]** (a reading laid over the mathematics, flagged as such). The
discipline is that a claim which does not survive this sorting is discarded, and the
discards are recorded (§7).

---

## 2. The first integers are the simplices [forced]

Given *n* points and no further structure, the configuration of *maximal symmetry* —
the one invariant under the largest group of permutations and rigid motions — is the
**regular (*n*−1)-simplex**, the convex hull of *n* affinely independent, mutually
equidistant points [Coxeter 1973, §7]. Thus:

| integer | configuration | dimension |
|---|---|---|
| 1 | point (0-simplex) | 0 |
| 2 | segment (1-simplex) | 1 |
| 3 | triangle (2-simplex) | 2 |
| 4 | tetrahedron (3-simplex) | 3 |

The content is immediate and forced: **each added point raises the dimension by one**,
and this can continue only to *n* = 4, because a regular 4-simplex requires four
dimensions and three-dimensional space is exhausted at the tetrahedron. The integers
1–4 are precisely the dimensional ladder; the tetrahedron is the last that space
permits. (Beyond 4 the reading changes character — the pentagon at *n* = 5 is the
first configuration whose natural symmetry cannot tile the plane, by the
crystallographic restriction theorem [Barlow 1894]; we return to this only briefly, in
§6.3, as it is not needed for the main result.)

---

## 3. The forced angle and the origin of 1/3 [forced]

The regular *N*-simplex carries a **forced internal angle**. Place its *N* vertices as
unit vectors from the centroid; by symmetry all pairwise dot products are equal, and
since the vectors sum to zero,

> 0 = |Σ vᵢ|² = Σ|vᵢ|² + Σ_{i≠j} vᵢ·vⱼ = N + N(N−1) cos θ,

whence

> **cos θ = −1/(N−1).**   *(the simplex angle)*

This is an exact identity, forced by the premise (the simplex is integer *n*) and
elementary algebra. Its values:

| *N* (vertices) | configuration | cos θ | θ |
|---|---|---|---|
| 2 | segment | −1 | 180° |
| 3 | triangle | −1/2 | 120° |
| **4** | **tetrahedron** | **−1/3** | **109.47°** |
| 5 | 4-simplex | −1/4 | 104.48° |

For the tetrahedron — integer 4, the first solid — the angle is **arccos(−1/3) =
109.47°**, and

> **the number 1/3 is exactly 1/(N−1) for N = 4.**

This is the central structural fact of the paper. Wherever this geometry appears, the
1/3 appearing with it is *this* 1/3 — the reciprocal of one less than the tetrahedron's
vertex count — not an accident. Its **half-angle**,

> θ/2 = **arccos(1/√3) = 54.7356°,   with cos² = 1/3,**

is the angle between one vertex direction and the axis toward the opposite face
center. In the language of the ladder, 109.47° is the *separation* of two vertex
directions (a "spread") and 54.74° is the *tilt* of a single direction off the central
axis (a "lift"). Both are forced from integer 4.

---

## 4. The tetrahedron sits inside the cube [forced]

The four vertices of a regular tetrahedron may be taken as **four alternating
vertices of a cube** (coordinates (±1, ±1, ±1) with an even number of minus signs)
[Coxeter 1973]. Two such tetrahedra, of opposite parity, compose the cube — Kepler's
**stella octangula** [Kepler 1619]. Thus **8 = 2 × 4**: the cube is the doubled
tetrahedron, and the two component tetrahedra are mirror images (opposite chiralities).

Two consequences are forced:

1. **The tetrahedral angle is the cube's alternating-vertex angle**, and the
   half-angle 54.74° is the angle between a **cube edge and the body diagonal (1,1,1)**.
   This gives a second, independent route to 54.74°: the direction cosine of the body
   diagonal with any axis is 1/√3, so its angle to an edge is arccos(1/√3). The two
   routes — half the tetrahedral angle, and the cube-diagonal angle — agree, because
   the tetrahedron is half the cube.

2. **The cube presents two natural projections.** Viewed along a face normal it is a
   **square** (four-fold, 90°); viewed along the body diagonal, its three orthogonal
   axes project to **three directions 120° apart — a regular hexagon** (three-fold).
   The projection angle relating the two is exactly cos²(1,1,1) = **1/3** again. So a
   single solid carries both the four-fold and three-fold planar symmetries as its two
   shadows, joined by the 1/3.

---

## 5. Why this is not numerology [methodological]

A recurring number invites suspicion, and rightly: any sufficiently flexible scheme
can manufacture a match to a favored constant [the classic caution is von Neumann's
elephant, and the historical record of "derivations" of the fine-structure constant].
Three features distinguish the present 1/3 from that failure mode.

- **It is parameter-free.** The identity cos θ = −1/(*N*−1) has no adjustable
  quantity; setting *N* = 4 (the tetrahedron, the first solid) *forces* 1/3. Nothing is
  tuned.
- **It is over-determined.** The value 54.74° is reached by two independent forced
  routes (§4) that must agree, and does not depend on which is taken.
- **It is falsifiable in the negative.** The scheme makes definite claims about what
  it does *not* produce: it yields no particle masses, no coupling constants, no
  dimensionless magnitude of physics — only *structure* (angles, dimensions, symmetry
  relations). Where a number from physics is dimensionful or contingent, the scheme is
  silent, and it says so. A framework that manufactured matches would not have this
  boundary; §7 records where the boundary bites.

The claim of this paper is therefore narrow and, within its range, exact: **the first
integers are the simplices; the tetrahedron forces the angle arccos(−1/3); and the
1/3 is 1/(N−1) for N = 4.** Everything beyond this — the following section — is
offered as *illustration that this geometry is physically instantiated*, not as
derivation of the physics.

---

## 6. Where the geometry meets the measured world [illustration; named/measured]

The following are established, independently measured facts. They are presented to
show that the forced geometry of §§2–4 is not idle — it is the geometry the physical
world repeatedly selects. None is claimed as a consequence of the premise; each is a
place the same shape appears.

### 6.1 Carbon: the tetrahedral bond and the two forms of an element [named]

Methane (CH₄) places four hydrogens at the vertices of a regular tetrahedron about a
central carbon; the measured H–C–H bond angle is **109.47° = arccos(−1/3)** — the
simplex angle of §3, forced here by the electron-pair repulsion that maximizes the
separation of four bonds (VSEPR; sp³ hybridization) [Pauling 1960]. The same element
also forms **flat, three-fold (sp²) sheets** — graphene — whose carbon atoms bond at
120° in hexagons, leaving a mobile π-electron. Thus a single element realizes both
projections of §4.2: the **lifted, four-fold, tetrahedral** form (diamond, an
insulator, electrons locked in bonds) and the **flat, three-fold, hexagonal** form
(graphene, a conductor of massless Dirac electrons) [Castro Neto et al. 2009]. The
angle separating a bond from the axis in the lifted form is the half-angle **54.74°**.
That one atom can occupy either geometry — and that they differ by the tetrahedral
lift — is a clean physical instance of the two shadows of the cube.

### 6.2 The magic angle: where directional structure vanishes [named]

In nuclear magnetic resonance, spinning a sample about an axis at **54.7356°** to the
external field averages the dominant anisotropic interactions (dipolar coupling,
chemical-shift anisotropy) to zero [Andrew, Bradbury & Eades 1959; Lowe 1959]. The
reason is exact: these interactions carry the factor **(3cos²θ − 1)**, which is the
second Legendre polynomial P₂(cos θ), and **54.74° is precisely its root**. The
half-tetrahedral angle is therefore the angle at which the **rank-2 (quadrupolar,
directional) part of any interaction vanishes** — the angle at which orientation-
dependence self-cancels and an anisotropic system reads as isotropic. This is the
deepest connection: the lift angle of §3 is not merely where a four-fold structure
tilts, but the exact angle at which *directionality itself goes to zero*.

### 6.3 Neutrino mixing: the same 1/3, in a tetrahedral symmetry [named; with a
correction from nature]

Independently of geometry, the leading approximation to the observed neutrino mixing
matrix — **tri-bimaximal mixing** — sets the solar mixing angle at **sin²θ₁₂ = 1/3**,
and is naturally derived from the symmetry group **A₄, the rotation group of the
tetrahedron** [Harrison, Perkins & Scott 2002; reviews King & Luhn 2013]. The same
1/3, and the same tetrahedral group, appear in the flavor structure of matter.
Honesty requires the correction that nature *deviates* from exact tri-bimaximal
mixing — the third angle θ₁₃, predicted zero by the simplest form, was measured
nonzero in 2012 [Daya Bay; RENO]. The tetrahedral 1/3 is thus the correct *leading
form*, corrected by the physics — precisely the pattern one should expect if geometry
supplies the shape and the contingent world supplies the deviations.

---

## 7. What does not follow [the boundary, recorded]

The discipline of §1 requires stating where the scheme stops. The following were
tested and do *not* hold; they are recorded so the boundary is visible.

- **The geometry produces no magnitude of physics.** It yields angles, dimensions,
  and symmetry relations — never a mass, a coupling, or a dimensionful constant. Any
  attempt to read a physical magnitude directly from the integers (for example, to
  identify the geometric 1/3 with a specific measured ratio elsewhere in physics)
  fails: the geometric 1/3 is 1/(*N*−1), a pure structural quantity, and its equality
  with any *contingent* value would be coincidence, not consequence.
- **The half-angle 54.74° explains transport only through a stated mechanism, not by
  resemblance.** Its physical relevance in §6.2 rests entirely on the P₂ root; absent
  such a mechanism, associating the angle with a phenomenon merely because both are
  "special" is not warranted.
- **Interpretive labels are not derivations.** Calling the flat form "flow" and the
  lifted form "structure" (as one naturally might, given conductor vs. insulator) is a
  *reading*; it organizes the facts of §6.1 but does not derive chemistry.
- **The scheme is a lens, not a physical theory.** It re-describes structure that is,
  in every case above, already known and measured. Its value is organizational —
  seeing disparate facts (a bond angle, a spinning-sample technique, a mixing angle)
  as one geometry — not predictive of anything the measuring sciences do not already
  possess.

---

## 8. Conclusion

Read as configurations of points, the first four integers are the simplices, and *the
addition of a unit is the addition of a dimension* until three-space is full at the
tetrahedron. The tetrahedron then forces, by a parameter-free identity, the angle
**arccos(−1/3)**, and with it the number **1/3 = 1/(N−1)** and the half-angle
**54.74°** at which **cos² = 1/3**. This small chain is exact and reproducible, and it
is over-determined by two independent routes. The same geometry is repeatedly
instantiated in the measured world — in the bond angle of carbon and the two forms it
takes, in the angle at which directional structure vanishes, and in the leading form
of neutrino mixing — but the paper claims these as *illustrations that the geometry is
real*, not as derivations of the physics, and it records precisely where that boundary
lies. The modest, defensible thesis is that **integers, read geometrically, are not a
metaphor: the first of them are literally the simplices, and the structure they force
— the dimensional ladder and the tetrahedral 1/3 — is exact, and recurs.**

---

## References

- W. Barlow, "Über die geometrischen Eigenschaften homogener starrer Strukturen,"
  Z. Kristallogr. 23, 1 (1894). [crystallographic restriction]
- E. R. Andrew, A. Bradbury, R. G. Eades, "Nuclear magnetic resonance spectra from a
  crystal rotated at high speed," *Nature* 182, 1659 (1958); I. J. Lowe, *Phys. Rev.
  Lett.* 2, 285 (1959). [magic-angle spinning]
- A. H. Castro Neto, F. Guinea, N. M. R. Peres, K. S. Novoselov, A. K. Geim, "The
  electronic properties of graphene," *Rev. Mod. Phys.* 81, 109 (2009).
- H. S. M. Coxeter, *Regular Polytopes*, 3rd ed. (Dover, 1973). [simplices, stella
  octangula]
- Daya Bay Collaboration, *Phys. Rev. Lett.* 108, 171803 (2012); RENO Collaboration,
  *Phys. Rev. Lett.* 108, 191802 (2012). [θ₁₃ ≠ 0]
- P. F. Harrison, D. H. Perkins, W. G. Scott, "Tri-bimaximal mixing and the neutrino
  oscillation data," *Phys. Lett. B* 530, 167 (2002).
- T. L. Heath, *A History of Greek Mathematics* (Oxford, 1921). [figurate numbers]
- J. Kepler, *Harmonices Mundi* (1619). [stella octangula]
- S. F. King, C. Luhn, "Neutrino mass and mixing with discrete symmetry," *Rep. Prog.
  Phys.* 76, 056201 (2013). [A₄ flavor models]
- L. Pauling, *The Nature of the Chemical Bond*, 3rd ed. (Cornell, 1960). [hybridization,
  VSEPR]
