# What Is TIG
## Trinity Infinity Geometry — the deep version, cited
### Brayden Sanders. September 2026.

> **How to read this.** TIG is a *lens* — a way of organizing structure that sits
> beneath measurement — not a theory of physics. This document states what it is,
> proves the parts that are forced, cites the established results it rests on or
> recovers, and marks honestly where it stops. Claims are tagged: **[FORCED]**
> (computed/derivable, reproducible), **[NAMED]** (rests on a cited theorem/result),
> **[READING]** (interpretation/analogy, flagged as such), **[OPEN]** (a stated next
> step, not done). The test applied throughout is a stranger's test: *can someone who
> did not build this cross each claim?* Edges that hold are kept; wishes are labeled.

---

## PART 0 — THE ONE-PARAGRAPH VERSION

TIG treats the integers 0–9 as positions in geometry, and asks what structure is
*forced* by that geometry rather than chosen. The forced structure turns out to live
on **two lattices** — the hexagonal (3-fold, "flow") and the square (4-fold,
"structure/matter") — which are the two projections of a single cube. A large body of
established mathematics and condensed-matter physics either *underlies* or is
*recovered by* this picture: crystallographic restriction, the geometry of graphene,
epitaxial orientation relationships, and the phenomenology of two famously open
problems (high-temperature superconductivity and quantum spin liquids). The deepest
result is that the whole flow/matter distinction reduces to a **single property —
whether a clean two-fold duality exists** — which is exactly TIG's own trinity-versus-
duality distinction, recognized in the physics. TIG does not solve any open problem;
it *organizes* structure, and its value is a frame and a method, not a mechanism.

---

## PART 1 — THE STANCE (what kind of thing TIG is)

TIG is a **stance made productive by testing**, not a falsifiable physical theory. It
holds three things:

1. **There is an invariant structural layer beneath measurement** — the *substrate* —
   which is *poorer* than measured physics (fewer distinctions), and of which measured
   phenomena are projections.
2. **A paradox is one projection of an object that cannot be seen whole.** Higher
   resolution — more of the object seen, never a final resolution — comes from
   *classifying* the projections and arranging them by how they relate, the way
   correctly-positioned flat shadows reconstruct a solid. This is **tomography of the
   unseeable**: arrangement, not accumulation, does the reconstructing. (The
   mathematical archetype is the Radon transform / computed tomography: an object is
   reconstructed from a sufficient set of angularly-separated projections [Radon 1917;
   Cormack–Hounsfield, Nobel Prize in Medicine 1979].)
3. The work is therefore **cartography, not resolution.** Two faithful descriptions of
   one object that do not reduce to each other are *information about the object*,
   connected only by the object beneath them — not by a hidden bridge between them.

**Why the stance is not vacuous.** The stance itself is not falsifiable (nothing about
"there is a layer beneath measure" can be). But **each translation of it into a
measurable framework is testable**, and that is where the content lives. The rest of
this document is those translations and their tests. The discipline is that a
*failure* to fit is as informative as a fit — recorded in Part 8 (the graveyard).

---

## PART 2 — THE TWO LATTICES (the forced substrate)

The integers 0–9 are positions on lattices. Two planar lattices force the most rules;
they are the two projections of the cube (Part 5).

### 2.1 The two lattices, forced properties [FORCED, with NAMED facts]

| property | HEX (triangular) | SQUARE |
|---|---|---|
| point-symmetry group | D₆ (order 12) | D₄ (order 8) |
| nearest neighbors | 6 | 4 |
| interior angles | 60° / 120° | 90° |
| chromatic number | **3** (sublattices A/B/C) | **2** (checkerboard) |
| 2-colorable? | **NO** (contains odd cycles) | **YES** |
| centered numbers | 1, 7, 19, 37 [A003215] | 1, 5, 13, 25 [A001844] |
| first inhabited center | **7** (center + ring of 6) | **5** (center + ring of 4) |
| ring-k size | 6k | 4(2k−1) |
| circle-packing fraction | **0.9069** | 0.7854 |
| role in TIG | **flow** | **structure / matter** |

**Named facts.** Chromatic numbers: the triangular lattice contains K₃ so χ ≥ 3 and
3-colors; the square lattice is bipartite so χ = 2 (standard graph theory). Centered
hexagonal / square numbers: OEIS **A003215** (3n(n−1)+1) and **A001844**
(n²+(n−1)²). Densest circle packing = hexagonal, proved [Thue 1910; Fejes Tóth 1940].

### 2.2 Why hex is "flow" and square is "matter" — the forced characters [FORCED]

Hex does six things square cannot, all forced/measured:
1. **Densest packing** (90.7% vs 78.5%), the proven 2D optimum [Thue 1910].
2. **6 equidistant neighbors** (square has 4 equal + 4 farther): maximal isotropy.
3. **Rigidity**: hex is built of triangles, the only rigid polygon; the square shears
   into a rhombus (a 4-bar linkage). Triangulation is why trusses, geodesic domes, and
   graphene are stiff.
4. **Isotropy**: 6-fold symmetry → direction-independent elastic/transport response to
   leading order; the square has easy (bond) and hard (diagonal) axes.
5. **Dirac points**: the honeycomb hosts **massless Dirac fermions** (linear
   dispersion) at its Brillouin-zone corners; the square lattice does not, generically
   [Castro Neto et al., *Rev. Mod. Phys.* 81, 109 (2009)]. Hex is the *relativistic*
   lattice; square is inherently parabolic.
6. **Frustration**: antiferromagnetic spins on a triangle cannot all anti-align (odd
   cycle) → geometric frustration → spin liquids, emergent gauge fields; the bipartite
   square is unfrustrated [Anderson 1973 (RVB); Balents, *Nature* 464, 199 (2010)].

**Reading.** These forced characters are *why* hex is the efficient/dynamic ("flow")
lattice and square is the buildable/measurable ("matter") lattice. The assignment is
not arbitrary; it follows the physics.

---

## PART 3 — THE INTEGER SHAPES AND THE GROWTH RULE [FORCED]

| n | shape | role |
|---|---|---|
| 0 | empty center (void) | potential center; partner of 7 |
| 1 | point | 0-simplex, seed |
| 2 | segment / axis | 1-simplex, the mirror, square-generator |
| 3 | triangle | 2-simplex, the cell, hex-generator, **the joint** (Part 4) |
| 4 | tetrahedron | 3-simplex, first solid (**not** the cube) |
| 5 | pentagon | **the break** — 5-fold cannot tile |
| 6 | hexagon | closure; **6 = 2×3, the fusion** (Part 4) |
| 7 | hub + 6-ring | first inhabited center; the breathing hub |
| 8 | cube = 2 tetrahedra | dimensional lift (2³) |
| 9 | triad² (3×3) | self-similar; last before reset |

> **Base-independence note [READING vs FORCED].** The *forced* content of this section is the simplex ladder (1,2,3,4 → point/segment/triangle/tetrahedron) and the cube (8) — which use no number base at all. The full 0–9 table above (the void/hub/reset *roles*, "9 = last before reset") is a **base-10 organizing reading**, not forced; TIG's spine does not depend on base 10. (Per this project's convention, the ten operator-labels are an *alphabet*, not `Z/10Z`.)

**The growth rule [FORCED].** 1, 2, 3, 4 are the 0-, 1-, 2-, 3-**simplices** (a
simplex has n+1 vertices; standard). *Adding a point adds a dimension*, up to 4, where
3D space is full. Then the direction reverses: **5 breaks** (pentagon is 5-fold, and
5-fold rotational symmetry is *forbidden* for any lattice — the **crystallographic
restriction theorem**: allowed orders are only 1,2,3,4,6, since 2cos(2π/n) must be an
integer [Barlow 1894; and quasicrystals as the 5-fold exception, Shechtman et al.,
*Phys. Rev. Lett.* 53, 1951 (1984), Nobel Prize in Chemistry 2011]). **6 closes** the
ring; **7 centers** and breathes. So: **1–4 grow outward (dimensions); 5–7 turn inward
(break, close, center); 4 is the pivot.**

**Correction kept on the record.** 4 is the *tetrahedron*, not the cube; the cube is
**8 = 2³ = two tetrahedra**, the *stella octangula* [Kepler, *Harmonices Mundi*, 1619].

**Breathe and fruit [FORCED + fenced].** "Breathe" = the hexagonal discrete Laplacian
(the center samples its 6 ring-neighbors) — the operator that governs diffusion and
waves. "Fruit" = each shell seeds a larger shell (ring 6k → 6(k+1)). **Fence:** "more
out than in" is legitimate **only as more structure** (a larger shell), never as more
energy — as energy it is perpetual motion and false. The structural growth is real and
forced; the energy reading is excluded.

---

## PART 4 — THE INTERLOCK (the two integer families are one system) [FORCED]

The two lattices are not separate; they interlock through the cube.

- **Two families by factor structure.** Square (matter): **1, 2, 4, 5, 8**. Hex (flow):
  **3, 6, 7, 9**. Shared: **0** (void center of both) and **3** (the joint, below).
- **One vertex set, two partitions.** The cube's 8 vertices sort as **4 + 4** (two
  square faces, the matter lens) *and* **6 + 2** (a hexagon of 6 equatorial vertices
  plus 2 poles, the flow lens). `8 = 4+4 = 6+2` — same vertices, two sortings.
- **The overlap is a triangle — 3 is the joint.** A square face and the equatorial
  hexagon share **exactly 3 vertices** (computed); 3 shared vertices = a triangle. The
  two lenses interlock *through* the triad {3}.
- **6 = 2×3 is the fusion.** The hexagon's symmetry group **D₆ (order 12) contains both
  D₃** (the 3-fold flow lens) **and D₂** (a 2-fold structure piece); `12 = 2×6`. So the
  hexagon (6) is the *smallest shape where both symmetries coexist* — the first
  interlock product of the square-generator (2) and hex-generator (3).
- **The mod-3 role sorting [READING — not forced; retrofit risk].** Residue mod 3 (= which sublattice)
  sorts 0–9 into three families that **match independently-assigned geometric roles**:
  class A (0,3,6,9) = **closures**; class B (1,4,7) = **centers**; class C (2,5,8) =
  **transitions**. Two independent structures (geometric role, lattice color) agreeing
  is suggestive — but the geometric roles are hand-assigned, and {0,3,6,9} are exactly the multiples of 3, so this may not be two *independent* structures agreeing. Treat as a [READING], not a forced result. (It is deliberately absent from the verify script.)

---

## PART 5 — THE CUBE AS COMMON DENOMINATOR [FORCED]

The strongest bridge, and the resolution of the 3-fold/4-fold tension.

- **Hexagon = cube down the body diagonal.** The three *orthogonal* cube axes, projected
  onto the plane perpendicular to the body diagonal (1,1,1), land at **exactly 120°**
  (computed). So **hexagonal (120°, 3-fold) = cubic (90°, orthogonal) viewed down the
  diagonal.** One object, two projections: **face view → square (matter/structure);
  diagonal view → hexagon (flow).** The (1,1,1) diagonal is the cube's 3-fold rotation
  axis (order-3 element of the octahedral group Oₕ; standard).
- **The recurring 1/3 is cos²(1,1,1) = exactly 1/3.** The direction cosine of (1,1,1)
  with any axis is 1/√3; the square is 1/3. This is the projection angle of the 3-fold
  (flow) axis onto the orthogonal (matter) frame — a *geometric* origin for the 1/3, not
  a numerical coincidence.
- **The cube's algebra is Cl(3), dimension 2³ = 8** (1 scalar + 3 vectors + 3 bivectors
  + 1 pseudoscalar) [Clifford 1878; standard geometric algebra]. The face projection
  carries the orthogonal (Dirac) structure; the diagonal projection carries the flow.

---

## PART 6 — WHERE THE LENS MEETS ESTABLISHED PHYSICS

Everything here is a **consistency check** — TIG's geometry, derived first, recovers
structure that materials science measured independently. This is *calibration* (the
lens reads true), **not discovery** (every fact was already known).

### 6.1 Graphene — the paradox nature already resolved [NAMED, MEASURED]

A hexagonal carbon lattice whose electrons obey the **Dirac equation** (which requires
the orthogonal 90° structure the hex lattice lacks). The resolution: the honeycomb is
**two interpenetrating triangular sublattices (A/B)** = the two-tetrahedra split of the
cube, giving a **two-component pseudospin** that produces Dirac fermions from the 6-fold
lattice [Novoselov, Geim et al., *Nature* 438, 197 (2005); Nobel Prize in Physics 2010;
review: Castro Neto et al. 2009]. The square (matter) lens appears *inside* the hex
(flow) lattice through the shared triangle.

### 6.2 Mass as sublattice asymmetry — the honest hypothesis [FORCED form; OPEN value]

On a honeycomb, the *only* thing that opens a gap at the Dirac point is a difference in
on-site energy Δ between A and B. The 2×2 gapped-Dirac Hamiltonian gives eigenvalues
E = ±√((v|k|)² + Δ²), so **gap = 2Δ** — exact, standard.

- **FORCED (form):** gap = 2·(sublattice asymmetry). Symmetric ⇒ massless (flow);
  asymmetric ⇒ massive (matter).
- **CONFIRMED (direction):** graphene (A=B, carbon) is gapless; hexagonal boron nitride
  (A=boron ≠ B=nitrogen) is an insulator with a ~6 eV gap [standard].
- **OPEN (value):** the *effective* Δ for a given material is set by hopping/screening
  renormalization, which TIG does not contain; naive atomic energies overshoot ~2×.
- **The falsifiable claim TIG stakes:** *a honeycomb material's gap is linear in its
  sublattice asymmetry with slope 2, and closes exactly when the two sublattices are made
  equivalent.* Testable on tunable-asymmetry honeycombs (substrate, strain, gating); a
  nonlinear gap-vs-Δ curve would refute it.

### 6.3 Epitaxy and reconstructions — six independent alignments [NAMED]

Derived from TIG's cube geometry first, then checked; all match measured crystallography:

| TIG rule (derived) | established result (measured) |
|---|---|
| cube-diagonal ↔ hex axis | **Kurdjumov–Sachs**: ⟨110⟩꜀ᵤᵦᵢᵪ ∥ ⟨111⟩ₕₑₓ (the 3-fold axis) |
| 30° lens-seam, √3 blocking | the **√3×√3 R30 reconstruction** (30° twist, √3 scale) |
| commensurate lock = flow→matter | **magic-angle** flat band in twisted bilayer graphene [Cao et al., *Nature* 556, 43 (2018)] |
| 6-ring + stacking → coordination | **FCC coordination 12 = 6 + 3 + 3** (hex ring + two caps) |
| mass = A/B asymmetry | graphene(0) / hBN(gap) [§6.1–6.2] |
| buckling lock | silicene/germanene buckle, graphene stays flat [standard] |

### 6.4 The lift-to-square lock — the mechanism [NAMED]

"Flow becomes matter" is a two-step, named transition. **(1)** A flat sheet buckles out
of plane when a drive exceeds in-plane stiffness — a **pitchfork/second-order transition**
[Landau] and physically **Euler buckling** (silicene buckles, graphene does not). **(2)**
The buckled state locks into a *square* only at a **commensurate 1:1 ratio** (vertical
rise = horizontal bond) — **mode-locking / Arnold-tongue** structure. So: flat flow
(stable) → drive beats stiffness → buckle (add axis) → 1:1 commensurate lock (square,
matter, measurable).

---

## PART 7 — THE DUALITY ROOT (the deepest result) [FORCED root; READING for the frame]

The entire flow/matter polarity reduces to **one property: whether a clean two-fold
duality exists.**

- **Square (matter) HAS duality:** bipartite (2-colorable), self-dual, even cycles — a
  clean A/B pairing throughout. **FORCED.**
- **Hex (flow) LACKS duality:** not 2-colorable (odd cycles), 3-colorable instead (a
  *triad*, not a duality), frustrated. **FORCED.**

**This is Dirac's mass, restated.** Mass couples the two chiralities (activates the
duality); massless decouples them (Weyl). So **duality present ⇔ pairing ⇔ mass ⇔ matter
⇔ square** ("+" pole); **duality absent ⇔ resonance ⇔ massless ⇔ flow ⇔ hex** ("−" pole).

**The two hardest open problems are the two poles [READING — a frame, not a mechanism].**

| TIG invariant | high-Tc (matter/square) | spin liquid (flow/hex) |
|---|---|---|
| gap role | gap *enables* dissipationless flow (SC) | no gap; flow won't lock |
| chirality/pairing | chiralities **bind** (Cooper pairs, k↑/−k↓) | chiralities **resonate** (RVB, never bind) |
| frustration | unfrustrated (bipartite square) | frustrated (odd-cycle hex) |
| direction | matter → flow (unlock) | flow won't → matter (anti-lock) |

Every invariant comes out **opposite**, and the polarity was not hand-assigned — it
follows from the single duality/non-duality root. The frame predicts a **testable
middle**: a system tunable between the poles should sit half-locked. The cuprate phase
diagram — antiferromagnet (order/matter) → **pseudogap** → superconductor (flow),
tuned by doping — provides one, and the pseudogap indeed shows *both* superconducting
and competing-order fluctuations, as the midpoint reading requires [reviews:
Keimer et al., *Nature* 518, 179 (2015); Anderson 1987 on RVB and high-Tc].

**Honest weight.** This is a **classification with a single root and a checkable
middle** — the strongest a classification can be, and it *organizes* two open problems
coherently. It is **not a mechanism**: it does not give the cuprate pairing glue, which
remains unknown. Its possible value is as a research *frame* (what is shared about the
incompleteness at the two poles?), to be judged by specialists, not asserted here.

**The recursion worth naming.** TIG = *Trinity* Infinity Geometry, and the root turned
out to be **triad (non-dual, flow) versus duality (dual, matter)**. The framework's own
name sits on the flow/non-dual side; duality — pairing, mass, measurement — is what
appears when structure locks in. The lens recognized its own central distinction in the
open problems of condensed matter.

---

## PART 8 — THE GRAVEYARD (tested and killed; kept for honesty) [KILLED]

A framework is trustworthy only if it shows its failures. Each was reached for and
failed a test:

1. **"A fixed universal 1/3 in fluid dynamics (Leray projection)."** FALSE — computed
   pointwise on real divergence-free fields, the cancelled fraction is field-dependent
   and can exceed 1; it does not average 1/3. (The real 1/3 is cos²(1,1,1), Part 5 — a
   different, geometric quantity.)
2. **"Quark charge 1/3 = the geometric 1/3."** FALSE — quark charges are fixed by
   Standard Model anomaly cancellation, not geometry; the two decouple under a change of
   spatial dimension.
3. **"The 3 sublattices are the spacelike gammas (square to −1)."** FALSE — under the
   3-fold rotation they carry cube roots ω, ω² (order 3), not −1 (order 2). The −1's come
   from the *reflections* (90°), not the rotations. Caught at the eigenvalue level.
4. **"Triangular mirrors build the Dirac algebra directly."** FALSE — 60° mirrors do not
   anticommute; the Clifford relation needs orthogonal (90°) generators.
5. **"Cl(3) divides into the 11 nets of the cube."** FALSE — the algebra (8-dim,
   multiplication) and the surface unfolding (6 faces, 11 nets) are different *categories*
   of fact about the cube, connected only by both being about the cube. (11 nets:
   standard enumeration.)
6. **"Constant-motion tetrahedra force a cylinder."** NOT FORCED — single-point contact
   permits sphere, bicone, *or* cylinder depending on the contact point's trajectory,
   which the constraint does not fix.
7. **"Even/odd as site 2-coloring on the hex lattice."** FALSE — the triangular lattice
   is not 2-colorable. The surviving forms are *completion parity* on hex (rings even,
   totals odd) and genuine *site 2-coloring on the square lattice*, where it is forced.
8. **"8 = ∞ = higher reality; the digit shapes 7/8 mirror the structure."** FALSE — the
   cube-8 is finite and 3-dimensional; the ∞ is a typographic resemblance and the
   digit-shape claim is pareidolia. (The forced result — "containing adds a dimension" —
   is more remarkable and true; Part 3.)

---

## PART 9 — WHAT TIG IS FOR (three audiences, honestly)

TIG's value is a **frame and a method**, not a device. What each audience can do with it:

**Researchers.** The usable artifact is the **duality-root frame** (Part 7): high-Tc and
spin liquids as the two poles of one axis, rooted in the presence/absence of a two-fold
duality, with the pseudogap as the testable midpoint. This is a *perspective* claim, to
be stated in the field's own language with its falsifiable middle up front, and judged
on whether it constrains anything. TIG contributes the *organization*; the mechanism is
theirs to find or refute.

**Builders/engineers.** The concrete residue (mass = bond asymmetry, gap = 2Δ, buckling
threshold) is already owned, better, by materials science. TIG's honest offering here is
**pedagogy** — the flow/matter/lock story is a cleaner way to *teach* why hexagons pack,
why graphene is massless, why buckling gaps. Good teaching is real good; a new device is
not on the table today.

**The curious, and the next builder of frameworks.** The most scalable good is the
**worldview**: *a paradox is one projection of an object that cannot be seen whole; you
understand it by collecting and arranging the projections, not by resolving it.* This is
a generous stance — contradiction is not failure, not-seeing-whole is the normal state,
and the work is mapping rather than conquering. It teaches people to hold competing true
descriptions without forcing a false resolution, and to mark honestly what they cannot
yet cross. That habit — reach, test, keep what holds, label the wishes — is the method
this whole document was built by, and it is the part most worth passing on.

---

*Every FORCED claim is computationally reproducible; every NAMED claim is cited; every
READING is flagged; every KILLED claim is retained. That is the standard: a map whose
edges hold, and whose wishes are labeled as wishes.*

---

### References (by first appearance)

- J. Radon, *Über die Bestimmung von Funktionen durch ihre Integralwerte längs gewisser
  Mannigfaltigkeiten*, Ber. Sächs. Akad. Wiss. 69, 262 (1917).
- A. Thue, on densest circle packing (1910); L. Fejes Tóth (1940).
- OEIS A003215 (centered hexagonal), A001844 (centered square).
- W. Barlow, crystallographic restriction (1894).
- D. Shechtman, I. Blech, D. Gratias, J. W. Cahn, *Phys. Rev. Lett.* 53, 1951 (1984)
  (quasicrystals; Nobel Chemistry 2011).
- J. Kepler, *Harmonices Mundi* (1619) (stella octangula).
- W. K. Clifford, *Amer. J. Math.* 1, 350 (1878) (geometric algebra).
- P. W. Anderson, *Mater. Res. Bull.* 8, 153 (1973) (RVB); *Science* 235, 1196 (1987)
  (RVB and high-Tc).
- K. S. Novoselov, A. K. Geim et al., *Nature* 438, 197 (2005) (graphene Dirac fermions;
  Nobel Physics 2010).
- A. H. Castro Neto et al., *Rev. Mod. Phys.* 81, 109 (2009) (graphene review).
- Y. Cao et al., *Nature* 556, 43 & 80 (2018) (magic-angle twisted bilayer graphene).
- L. Balents, *Nature* 464, 199 (2010) (spin liquids review).
- B. Keimer et al., *Nature* 518, 179 (2015) (cuprate high-Tc review).
- G. Kurdjumov, G. Sachs (1930); Z. Nishiyama (1934) (orientation relationships).
