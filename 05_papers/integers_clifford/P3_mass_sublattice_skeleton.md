# P3 — Mass as Sublattice Asymmetry: A Falsifiable Linear Gap Law
## SKELETON. Companion to P1, P2. The one paper with a stated, runnable experiment.
### Status tags: [FORCED] · [NAMED] · [MEASURED] · [OPEN] = the experiment not yet run.

---

## Abstract (draft)

The two-tetrahedra structure of the Clifford cube (P2) descends, in its honeycomb
projection, to two triangular sublattices A and B. We identify the **Dirac mass** of a
honeycomb material with the **asymmetry between these sublattices**, and show — from
the standard two-band Hamiltonian — that the band gap at the Dirac point is
**exactly 2Δ**, where Δ is the on-site A/B energy difference. This is *linear in the
asymmetry, with slope 2, passing through the origin*, and it is the paper's
falsifiable claim. We state the experiment: across honeycomb (and honeycomb-derived)
materials, the measured gap should be a linear function of the effective sublattice
asymmetry, anchored at (0, 0) by graphene (A = B) and reaching ~6 eV for hexagonal
boron nitride (A = B, N). The *form* of the law is forced; its *slope* is the
prediction; a nonlinear gap-vs-asymmetry relation would refute it. What TIG does **not**
supply is the effective Δ for a given material — that is set by electronic
renormalization (hopping, screening) below the geometry, and must be taken from data
or first-principles calculation.

---

## 1. From the cube's two tetrahedra to the honeycomb A/B sublattices [FORCED → NAMED]

- P2: the cube = two mirror tetrahedra (two chiralities), dimension **2³ = 8** (the Cl(3) dimension); the two mirror tetrahedra are the doubling 8 = 2×4.
- In the honeycomb (three-fold projection of the cube), the structure is **two
  interpenetrating triangular sublattices A and B** — the two-tetrahedra split
  realized in 2D [NAMED: this is the standard honeycomb basis, Castro Neto et al. 2009].
- **The two sublattices = the two chiralities = the electron's pseudospin.** This is
  why honeycomb electrons obey a Dirac equation despite the three-fold lattice
  [NAMED: Novoselov–Geim 2005, Nobel 2010].

## 2. The forced gap law [FORCED]

- Near a Dirac point K, the two-band Hamiltonian is
  H = [[Δ, v k], [v k*, −Δ]], where Δ is the **on-site energy difference between A and
  B** (the sublattice asymmetry) and v k is the (linear) kinetic term.
- Eigenvalues: **E = ±√((v|k|)² + Δ²).** At the Dirac point (k = 0): **E = ±Δ**, so
  **gap = 2Δ.** [FORCED — this is the exact gapped-Dirac result, standard.]
- **The mass identification:** TIG-mass ≡ Δ = the sublattice asymmetry. Massless
  (Δ = 0) ⇔ A = B; massive (Δ ≠ 0) ⇔ A ≠ B.

| Δ (eV) | gap = 2Δ (eV) |
|---|---|
| 0.0 | 0.0 |
| 0.5 | 1.0 |
| 1.0 | 2.0 |
| 3.0 | 6.0 |

- **The law: gap = 2 × (sublattice asymmetry). Linear, slope 2, through the origin.**

## 3. Confirmation of the direction [MEASURED]

- **Graphene:** A = B (carbon–carbon), Δ = 0 ⇒ **gapless** (Dirac semimetal). ✓
- **Hexagonal boron nitride:** A = boron, B = nitrogen, Δ ≠ 0 ⇒ **insulator, gap ≈
  6 eV**. ✓ [NAMED]
- The *sign* of the effect — symmetric gapless, asymmetric gapped — is measured and not
  in doubt. What remains is the *quantitative linearity*.

## 4. THE EXPERIMENT [OPEN — stated, not yet run]

**Claim to test:** across honeycomb and honeycomb-derived materials, the band gap is a
linear function of the effective sublattice asymmetry Δ_eff, slope 2, through the
origin.

**Data required — a table of (gap, Δ_eff) pairs:**

| material | bond | measured gap | Δ_eff (to be sourced/computed) |
|---|---|---|---|
| graphene | C–C | 0 (anchor) | 0 |
| silicene | Si–Si | ~1.5 meV (SOC) | ~0 |
| germanene | Ge–Ge | ~24 meV | small |
| MoS₂ (and TMDs) | Mo–S | ~1.8 eV | large (structural caveat) |
| hexagonal BN | B–N | ~6 eV | large (far anchor) |

**Method [OPEN]:**
1. Collect published, well-established band gaps for a set of honeycomb-lattice
   materials.
2. Obtain each material's **effective on-site sublattice asymmetry Δ_eff** — either
   from tight-binding fits in the literature or from DFT on-site energies (this is the
   step TIG does not supply; it requires the electronic-structure input).
3. Plot gap vs Δ_eff. **TIG predicts a straight line of slope 2 through the origin.**
4. Report the fit: slope, intercept, R², and any systematic deviation.

**Falsifiers:**
- A clearly **nonlinear** gap-vs-Δ_eff relation refutes the linear law.
- A **nonzero intercept** (a gap at Δ_eff = 0, beyond spin-orbit effects) refutes the
  "gap closes iff A = B" claim.
- A **slope significantly different from 2** across materials (after honest Δ_eff
  determination) weakens the specific prediction.

**Caveats to state honestly in the paper:**
- Materials like MoS₂ have additional structure (transition-metal d-orbitals,
  spin-orbit coupling) that the simple two-band picture omits; they test the law only
  approximately and should be flagged.
- Spin-orbit coupling opens tiny gaps even at Δ = 0 (silicene); this sets the
  resolution floor and must be subtracted or noted.
- Δ_eff is renormalized from bare atomic values (~2× in hBN); the honest test uses the
  *effective* Δ, and the paper must be explicit that this is input, not TIG output.

## 5. What TIG does and does not claim [boundary]

- **[FORCED]:** the *form* — gap = 2Δ, linear, through the origin — from the geometry
  (two sublattices → pseudospin → gapped Dirac).
- **[OPEN, not TIG]:** the *value* of Δ_eff for any material, which is electronic
  renormalization below the geometry.
- **The paper's contribution** is therefore a **falsifiable structural law with a
  slope prediction**, testable on existing data, not a first-principles gap
  calculation. If the linearity holds across materials, the geometric identification of
  mass with sublattice asymmetry is supported; if not, it is refuted.

## 6. Conclusion (draft)

The mass of a honeycomb Dirac material is identified, from the two-tetrahedra structure
of the Clifford cube, with the asymmetry between its two sublattices; the band gap is
then forced to be **2Δ — linear in the asymmetry, slope 2, through the origin**. The
direction is confirmed (graphene gapless, hBN gapped); the linearity is a falsifiable
prediction testable on a table of published gaps against effective sublattice
asymmetries. TIG supplies the law's form, not the material-specific value, and the
paper is explicit about that boundary. This is the strand of the framework closest to a
measurable result rather than a frame.

---

## References
- A. H. Castro Neto, F. Guinea, N. M. R. Peres, K. S. Novoselov, A. K. Geim,
  *Rev. Mod. Phys.* 81, 109 (2009).
- K. S. Novoselov, A. K. Geim et al., *Nature* 438, 197 (2005).
- [to add on data pull: sources for hBN gap, silicene/germanene SOC gaps, TMD gaps, and
  tight-binding Δ_eff values.]
