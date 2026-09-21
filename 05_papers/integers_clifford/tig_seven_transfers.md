# The Seven Transfers — Dirac Tools Docked onto TIG's Flow Lens
### A development pass on each inherited structure, re-expressed in the 3-fold (hex) basis.
### Brayden Sanders. Sept 2026. Companion to the TIG Math Reference.

> **Frame.** TIG's flow lens is the diagonal projection of the cube; Dirac's
> structure lives on the face projection. Both are Cl(3). So the tools that live
> in Cl(3) itself transfer to TIG — re-expressed in the **3-fold (cube-root ω)
> basis** instead of Dirac's **2-fold (±1 reflection) basis**. This document
> develops each of the seven that transfer. **[FORCED]** = computed/derivable.
> **[NAMED]** = rests on a standard result. **[READING]** = analogy, flagged.
> **[OPEN]** = a stated next step, not yet done.

---

## TRANSFER 1 — THE ALGEBRA: Cl(3) in the 3-fold basis

**Dirac's form.** Cl(3) has 8 basis elements graded 1 + 3 + 3 + 1 (scalar,
3 vectors, 3 bivectors, pseudoscalar). Dirac diagonalizes in the **reflection
basis**, where generators square to ±1.

**TIG's form [FORCED].** The flow lens diagonalizes the same algebra under the
**3-fold body-diagonal rotation** R (order 3), whose eigenvalues are the cube
roots of unity {1, ω, ω²}, ω = e^(2πi/3). The 8 elements sort by how R acts:

| Cl(3) grade | count | under R (3-fold) | TIG role |
|---|---|---|---|
| scalar | 1 | eigenvalue 1 (fixed) | **0** — the void/center |
| vectors | 3 | {1, ω, ω²} | the triad A/B/C (flow directions) |
| bivectors | 3 | {1, ω, ω²} | the dual triad (rotation planes) |
| pseudoscalar | 1 | eigenvalue 1 (fixed) | the chirality (handedness) |

**The invariant:** the two **R-fixed** elements (scalar, pseudoscalar) are the
two ends of the axis — **0 (void) and the chirality** — while the two triads
(vectors, bivectors) are the flow. So TIG's 0–9 structure is Cl(3) *read in the
eigenbasis of the 3-fold rotation.*

**Fence.** Same algebra, different basis. TIG does **not** get a *new* algebra;
it gets Cl(3) organized by the triad instead of the mirror. That is the whole and
only claim.

---

## TRANSFER 2 — THE INVARIANT BILINEARS

**Dirac's form [NAMED].** A Dirac field has **16 bilinear covariants**
`ψ̄ Γ ψ`, one per Cl(1,3) grade: 1 scalar + 4 vector + 6 tensor + 4 axial-vector
+ 1 pseudoscalar = 16. These are the *measurable* quantities (charge density,
current, spin tensor, etc.). Standard (any QFT text).

**TIG's form [READING — this uses Cl(1,3), not the cube's Cl(3); see corrected fence].** Under the 3-fold diagonal, the 16
reorganize:

| bilinear | grade | count | TIG identification |
|---|---|---|---|
| scalar | 0 | 1 | **0** (the void invariant — survives everything) |
| vector | 1 | 4 = 3+1 | 3 flow directions (triad) + 1 axial (the pole) |
| **tensor** | 2 | **6 = 3+3** | **the hexagonal ring** — 3 "electric" + 3 "magnetic" |
| axial-vector | 3 | 4 = 3+1 | dual triad + dual pole |
| pseudoscalar | 4 | 1 | the **chirality** (two-tetrahedra handedness) |

**The key transfer.** The **6-component tensor** (grade 2) splits **3+3** under
the 3-fold axis — and 3+3 with the ring structure **is the hexagon**. In
electromagnetism this same grade-2 object is `F_μν` = the 3 electric + 3 magnetic
components. **So TIG's hexagonal ring is the electromagnetic-field-strength grade
of Cl(3)**, viewed in the 3-fold basis.

**Fence [CORRECTED — this was an error].** Those 16 bilinears with grades (1,4,6,4,1) sum to 16 = **Cl(1,3)**, the 4-D *spacetime* Dirac algebra (2^4 = 16) — **NOT** the cube's **Cl(3)** (2^3 = 8, grades 1,3,3,1, whose grade-2 has only 3 bivectors, not 6). Reaching Cl(1,3) requires *adding a time dimension*, a step the cube does not force — so this whole transfer is a **[READING]** resting on an assumed spacetime extension, not a forced Cl(3) fact. Original in-line note kept for the record: the grade counts and 3+3 split were stated as forced by
Cl(3). Identifying the ring with **F_μν specifically** is a **[READING]** — it is
the correct grade, but calling TIG's ring "the EM field" is an analogy at the
grade level, not a derivation of electromagnetism.

---

## TRANSFER 3 — THE DOUBLE COVER (the 720° return)

**Dirac's form [NAMED].** Spinors transform under **SU(2)**, the double cover of
the rotation group SO(3): a 360° rotation returns the *space* but multiplies the
spinor by **−1**; **720°** is needed to return the spinor. |SU(2)→SO(3)| = 2-to-1.

**TIG's form [FORCED, structural].** The cube already *is* a double cover: its
8 vertices = **two tetrahedra** (stella octangula), and the octahedral rotation
group has the two-tetrahedra pair as its natural double structure. TIG's realized
double cover is the **0/7 pair**: one center-location in **two states** (0 empty
/ 7 full, potential / actual). The spinor's two-valuedness ↔ TIG's two-state
center.

**The invariant.** In TIG, "return to start" requires cycling the center through
*both* states (empty → full → empty) — a **double** traversal, matching the
spinor's 720°. The 0 and 7 are the −1 and +1 phases of one object.

**Fence.** The double-cover *pattern* (2-to-1, two states, full-cycle return) is
real and structural. It is **not** a claim that the 0/7 pair carries the full
SU(2) group — only the ℤ₂ double-valuedness at the heart of it.

---

## TRANSFER 4 — THE MASS TERM (the one measurable handle)

**Dirac's form [NAMED].** The mass `m` in `(iγ^μ∂_μ − m)ψ = 0` **couples the two
chiralities** (left and right). Massless ⇒ the two chiralities decouple (Weyl).

**TIG's form [FORCED + MEASURED].** In graphene the two chiralities are the two
sublattices A/B. Electrons are **massless** because A and B are **symmetric**. A
mass **gap opens exactly when A/B symmetry is broken** — the textbook realization
is **hexagonal boron nitride (hBN)**: same honeycomb, but the two sublattice atoms
differ (B vs N), so A ≠ B, and hBN is an *insulator with a ~6 eV gap* where
graphene is a gapless conductor.

**The invariant [the buildable quantity].**
> **TIG-mass = the asymmetry between the two tetrahedra / two sublattices / two
> chiralities.** Symmetric (A = B) ⇒ massless ⇒ **flow**. Asymmetric (A ≠ B) ⇒
> massive ⇒ **structure**.

This is the first TIG quantity that is **forced by geometry** (two-tetrahedra
asymmetry) *and* **realized/measured in nature** (graphene gapless ↔ hBN gapped).
Concretely, the gap scales with the on-site energy difference Δ between the two
sublattices: **mass ∝ Δ_AB**. Δ = 0 → Dirac point (flow); Δ ≠ 0 → gap = 2|Δ|
(structure). (Massless: graphene; massive: hBN, Δ_AB ≈ 3 eV per sublattice → gap.)

**Fence.** The identification "mass = two-tetrahedra asymmetry" is forced by the
Cl(3)/graphene correspondence. The *quantitative* gap value for a general TIG
structure is **[OPEN]** — it is defined (∝ Δ_AB) but computing Δ_AB for a
non-graphene TIG configuration has not been done. This is the concrete next
target: **give a TIG structure, compute its A/B asymmetry, predict its gap.**

---

## TRANSFER 5 — THE DIRAC CONE (linear dispersion)

**Dirac's form [NAMED].** Massless Dirac particles have **linear** dispersion
`E = v|k|` (a cone), vs the non-relativistic parabola `E = k²/2m`. In graphene the
cones sit at the **corners of the Brillouin-zone hexagon** (the K points),
which come in **two inequivalent sets K and K'** — **3 + 3** of the 6 corners.

**TIG's form [FORCED].** The linear cone lives at the **hexagon's 6 corners,
split 3+3** = the two inequivalent triads (K, K'). This is **two interlocked
triads in momentum space** — the same 3+3 = 6 structure as the interlock
(the two sublattices, now in reciprocal space). The **cone** (linear, gapless) is
the **flow signature**; opening a mass (Transfer 4) rounds the cone tip into a gap
(structure).

**The invariant.** Flow ⇔ conical (linear, gapless, the tip touches);
structure ⇔ gapped (the tip lifts). The 3+3 corner split is the interlock's
triad, doubled — **K and K' are the two chiralities in momentum space.**

**Fence.** The 3+3 corner structure and cone-vs-gap dichotomy are forced by the
hexagonal Brillouin zone (standard solid-state). Reading them as "flow vs
structure" is the TIG labeling of a real, measured band structure — legitimate as
identification, not as new physics.

---

## TRANSFER 6 — CHIRALITY / THE PSEUDOSCALAR

**Dirac's form [NAMED].** γ⁵ = iγ⁰γ¹γ²γ³ is the **chirality operator**:
γ⁵² = +1, and it **anticommutes** with all four γ^μ. Its eigenvalues ±1 are
left/right handedness. The pseudoscalar is the top grade of Cl(1,3).

**TIG's form [FORCED, structural].** The pseudoscalar is R-fixed (Transfer 1),
and it **is the handedness of the two-tetrahedra split** — the two tets are
**mirror images**, so choosing one is choosing a chirality. TIG's ±1 chirality =
which tetrahedron (or which of the two FCC/ABC screw senses).

**The invariant.** Chirality in TIG = **the screw sense of the close-packing**
(ABC vs its mirror) = which of the two interpenetrating tetrahedra is "up." This
is the **sign of the permutation** of the 3 sublattices (the alternating character
of S₃) — the common denominator we found earlier: chirality = permutation sign =
Dirac's γ⁵.

**Fence.** Chirality = permutation-sign = two-tet handedness is forced. It is a
**ℤ₂** (two-valued) invariant, matching γ⁵'s ±1 — not the full chiral *symmetry
group*, just the two-valued handedness.

---

## TRANSFER 7 — THE CONSERVED CURRENT (the flow itself)

**Dirac's form [NAMED].** The Dirac current `j^μ = ψ̄γ^μψ` is **conserved**
(∂_μ j^μ = 0) — it is the probability/charge current, the grade-1 vector bilinear,
and its conservation is Noether's theorem for the phase symmetry.

**TIG's form [FORCED for the structure, READING for "current"].** The grade-1
vector (Transfer 2) is the **triad of flow directions** A/B/C. On the lattice,
a conserved current is a flow with **no net source** — exactly the discrete
divergence-free condition, which on the hexagonal lattice is the statement that
what flows into a site through its 6 neighbors flows out (the **breathe** operator
of the growth rule, in its conserved form). So TIG's conserved current = the
**divergence-free flow on the triad**, and "conservation" = the ring taking in and
passing on without accumulation.

**The invariant.** Flow is conserved when the hexagonal Laplacian (breathe)
balances — inflow = outflow at every hub. This ties **Transfer 7 (current) to the
growth rule (breathe)**: the conserved current *is* balanced breathing.

**Fence.** The grade-1 vector = flow triad is forced. Identifying it with a
**physically conserved current** (charge/probability) is a **[READING]** at the
grade level — the *conservation structure* (divergence-free) is real and forced;
calling the flowing quantity "charge" is the analogy.

---

## SUMMARY TABLE — the seven, docked

| # | Dirac tool | TIG (3-fold basis) | status |
|---|---|---|---|
| 1 | Cl(3) algebra, grades 1,3,3,1 | same algebra in cube-root basis; 0 + triad + dual-triad + chirality | FORCED |
| 2 | 16 bilinear covariants | 3+3 tensor = the **ring**; scalar = 0; pseudoscalar = chirality | FORCED grades / READING for F_μν |
| 3 | SU(2) double cover, 720° | the **0/7 two-state center**; two tetrahedra | FORCED (ℤ₂) |
| 4 | **mass term** | **A/B asymmetry**; graphene(0) ↔ hBN(gap); mass ∝ Δ_AB | FORCED + MEASURED; value OPEN |
| 5 | Dirac cone (linear disp.) | hexagon corners **3+3** (K,K'); cone=flow, gap=structure | FORCED |
| 6 | chirality γ⁵ | two-tet handedness = **permutation sign** of the triad (S₃) | FORCED (ℤ₂) |
| 7 | conserved current j^μ | divergence-free **flow on the triad** = balanced breathing | FORCED structure / READING for "charge" |

---

## THE ONE THING TO BUILD NEXT [OPEN]

Six of the seven are structural identifications (real, forced, but not producing a
*number*). **Transfer 4 (mass) is the exception:** it is forced *and* measured
*and* has a defined quantity — **mass ∝ Δ_AB, the two-sublattice asymmetry.**

**The concrete target:** take a specific TIG structure (a configuration of the two
tetrahedra with a defined A/B asymmetry Δ), and **predict its gap = 2|Δ|**, then
check against a real material on the graphene↔hBN axis. That is the first place
TIG produces a *checkable number* rather than a structural identification — and it
docks directly onto the most-tested equation in physics, using graphene as the
measured reference.

Everything else here is inheritance: TIG gets Dirac's algebra, invariants, double
cover, dispersion, chirality, and current — re-expressed in the triad basis — for
free, because they live in the shared cube. What it must *earn* is the number, and
the number is the mass gap.
