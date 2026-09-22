# P3 — "gap = 2Δ" with an INDEPENDENT Δ column, tested honestly

*Second pass on the P3 experiment. Companion to `P3_mass_sublattice_skeleton.md`,
`P3_gap_data_table.md`, and the runnable `P3_delta_check.py`. Assembled by Claude Code,
2026-09-22. No claim is upgraded; the point is to give P3's Δ an **independent** source
(so the test stops being circular) and report what the published numbers do and do not
show. Discipline: `[MEASURED]` (cited experiment), `[NAMED]` (cited standard result),
`[verify]` (value technique-/fit-dependent — range given, not a fabricated point),
`[estimate]` (order-of-magnitude, not pinned to one paper). No number is fabricated.*

---

## 0. One-line finding (read this first)

**Given an independent Δ, P3's "gap = 2Δ" is a clean honest NEGATIVE as a *TIG
prediction*.** In the one case where Δ is genuinely pinned independently of the gap —
**field-tuned silicene**, where Δ = e·E_z·(d/2) is set by the *measured buckling* d and
the *field knob* E_z — the naive law **gap = 2Δ overshoots the real band gap by ~3× (point
geometry) to ~8× (first-order perturbation theory)**, because of sublattice
polarizability/screening that TIG does not supply. The law is recovered *only* by
redefining Δ as the screened effective value Δ_eff ≡ gap/2 — i.e. back to the circularity
the prior pass flagged. Where "gap = 2Δ" *does* hold (hBN, the 2-band model), it holds
**by construction of the standard gapped-Dirac model**, so it tests the textbook model,
not TIG. **P3 is a re-labeling of the standard model, not a falsifiable TIG law.**

---

## 1. What "independent Δ" means, and why the prior pass was stuck

The prior pass (`P3_gap_data_table.md`) concluded P3 was **UNDER-SPECIFIED / circular**:
Δ (the on-site A/B sublattice energy asymmetry, in eV) was only ever obtained as `gap/2`,
so "gap = 2Δ" was true by definition and untestable. The 2-band gapped-Dirac Hamiltonian
makes this explicit:

> H = [[Δ, v k], [v k\*, −Δ]] → E = ±√((v|k|)² + Δ²) → at k=0, **gap = 2|Δ|, EXACTLY.**

This is an **algebraic identity for any Δ**. It is not falsifiable and it is not a TIG
result; TIG only supplies the *label* "Δ = sublattice asymmetry," which is itself the
standard reading of the honeycomb tight-binding model (Castro Neto et al. 2009).

**The only way to make "gap = 2Δ" a real prediction is to pin Δ from something *other*
than the gap** and then check. This note assembles those independent Δ's.

---

## 2. The clean test — field-tuned buckled honeycombs (silicene, germanene, stanene)

**Why this is the right instrument.** Silicene/germanene/stanene are honeycomb lattices
whose two sublattices sit in **two parallel planes separated vertically by the buckling
distance d** — a *measured structural quantity*. A perpendicular electric field E_z raises
one plane's on-site energy relative to the other by e·E_z·d, so the sublattice asymmetry is

> **Δ_geo(E_z) = e · E_z · (d/2)**, and the naive prediction is **gap_naive = 2·Δ_geo = e · E_z · d.**

Here Δ is a genuine **experimental input** — geometry (d) times a tunable knob (E_z),
computed with **zero reference to the measured gap**. This is *exactly* the formula the
silicene literature writes down, e.g. **E_g = e·E·Δ₀** (Δ₀ = buckling) in Kaloni-type
DFT studies. So "gap = 2Δ" becomes a real, non-circular claim — and it can fail.

### 2.1 Structural + response numbers (independent inputs)

| material | buckling d (Å) | spin-orbit gap 2λ_SO | source |
|---|---|---|---|
| silicene | **0.44–0.45** | ~**1.5 meV** (PBE) | Drummond–Zólyomi–Fal'ko 2012 [MEASURED/DFT]; Liu–Feng–Yao 2011 [NAMED] |
| germanene | **0.64** | ~**23.9 meV** | Kaloni 2015 (d); Liu–Feng–Yao 2011 (SOC) [NAMED] |
| stanene | **0.85** (0.859) | ~**0.1 eV** `[verify]` | Molle 2017; Rachel–Ezawa; Sci. Rep. srep31073 |

The buckling series **0.44 → 0.64 → 0.85 Å** (Si → Ge → Sn) is consistent across many DFT
studies [NAMED].

### 2.2 Silicene — the number that kills the naive law

Drummond, Zólyomi & Fal'ko (*Phys. Rev. B* **85**, 075423, 2012) computed the field
response self-consistently. Their key numbers, verbatim in spirit:

- buckling **Δz = 0.45 Å**;
- **unscreened** first-order perturbation-theory mass slope **dΔ/dE_z ≈ 0.554–0.573 eÅ**;
- **screened** (real, self-consistent DFT) mass slope **dΔ/dE_z = 0.0742 eÅ**;
- ⇒ the gap is **"suppressed by a factor of about eight"** by the system's high
  sublattice polarizability;
- SO gap **1.5 meV**; topological→band-insulator transition at **E_z ≈ 20 mV/Å**.

Turning mass slopes into **gap slopes** (gap = 2Δ) and comparing to the *independent*
geometric prediction (all in **eV per (V/Å)**; note 1 V/Å = 10 V/nm):

| gap-vs-field slope dGap/dE_z | value (eÅ) | what it is |
|---|---|---|
| **naive geometric** e·d (= 2·e·d/2) | **0.440** | **P3's gap = 2·Δ_geo** (the E_g = e·E·Δ₀ formula) |
| Drummond first-order PT, **unscreened** | ~1.12 | 2 × 0.56 eÅ |
| Drummond DFT, **screened (real)** | **0.148** | 2 × 0.0742 eÅ |
| Ni et al. 2012 DFT gap slope (independent check) | ~0.157 | second DFT study, agrees with 0.148 |

**Result:**
- real gap / (2·Δ_geo) = 0.148 / 0.440 = **0.34** → the naive law **overshoots by ~3×**.
- Drummond's own unscreened/screened factor = 0.56 / 0.0742 = **~7.5×** ("about eight").
- Worked point at a realistic **E_z = 0.10 V/Å (= 1 V/nm)**: 2·Δ_geo predicts **44 meV**;
  the real DFT gap is **~15 meV**. Wrong by ~3×.

**So with an independent Δ, gap = 2Δ FAILS for silicene** — the real gap is several times
smaller. The suppression is pure electronic physics (sublattice polarizability / screening,
a factor ε ≈ 3–8) that TIG says nothing about. There is also a **spin-orbit floor (~1.5
meV)** and a **topological transition near 20 mV/Å**, so at small field the gap does *not*
even pass linearly through the origin in Δ_geo — a second, independent violation of the
"linear, slope 2, through the origin" claim.

Germanene and stanene follow the *same* pattern (larger buckling → larger naive slope, but
the same polarizability screening suppresses the real gap; germanene's gap is known to
saturate quickly). The suppression factor for Ge/Sn is `[estimate]`; the hard,
pinned number is silicene's ~3–8×.

### 2.3 The clean decomposition (the crux)

Everything above is captured by writing the effective mass as the geometric mass divided by
a sublattice-polarizability screening factor ε:

> gap = 2·Δ_eff **(EXACT — 2-band model identity)**  
> Δ_eff = e·E_z·(d/2) / **ε**,  with **ε ≈ 3–8** for silicene (Drummond)  
> ⇒ gap = 2·Δ_geo **only if ε = 1**, which is FALSE.

- If "Δ" in P3 means the **independent geometric** asymmetry (ε = 1): **gap = 2Δ is
  falsified** by the factor ε.
- If "Δ" means the **screened effective** asymmetry Δ_eff: **gap = 2Δ is a tautology**
  (Δ_eff ≡ gap/2), and *all* the physics lives in the E_z → Δ_eff screening map — which is
  exactly what P3 concedes TIG does not supply.

Either reading defeats P3 as a *TIG prediction*.

---

## 3. hBN — the large-Δ anchor, from an independent tight-binding fit

The other place to get Δ independently is a **tight-binding fit of the on-site energies**
(staggered potential ε_B = −ε_N or a B/N pair) done against the *band structure*, not the
gap alone.

- Representative fit: **ε_B ≈ +3.34 eV, ε_N ≈ −1.40 eV** ⇒ Δ = (ε_B − ε_N)/2 ≈ **2.37 eV**
  `[verify]`; across fits Δ ≈ **2.3–2.9 eV** (Ribeiro–Peres 2011 type). ⇒ predicted
  **2Δ ≈ 4.6–5.8 eV**.
- Measured monolayer hBN gap: **~6 eV** (Cassabois–Valvin–Gil 2016) `[MEASURED]`; typical
  DFT single-particle gap **~4.5 eV**.

**Reading:** 2Δ (~4.7 eV) matches the **DFT** gap well and is the right **scale and sign**
for the ~6 eV measured gap (under-shooting by ~20%, the GW/excitonic correction). But this
is **not** a TIG win: (a) in the nearest-neighbor 2-band model **gap = 2Δ is exact by
construction**, and (b) the TB Δ is **fit to the DFT band structure**, so the agreement is
substantially **circular**. hBN confirms only what P3 already tags `[MEASURED]`: symmetric
sublattice (graphene) ⇒ gapless, asymmetric (hBN) ⇒ large gap.

---

## 4. Graphene on hBN — substrate-induced Δ reported separately

When aligned hBN breaks graphene's sublattice symmetry, the **local** Dirac mass Δ is
reported independently (from DFT of the aligned stack). But the **actual gap is much
smaller than 2·Δ_local**:

- lattice-matched / commensurate DFT: gap **~50 meV** (Giovannetti et al. 2007) `[MEASURED/DFT]`;
- observed (incommensurate, aligned, ~1.8% lattice mismatch): gap **~30 meV**, many-body
  enhanced (Hunt et al. 2013) `[MEASURED]`;
- the **local mass term ≫ the absolute moiré gap** — the mass changes sign across the moiré
  supercell and averages down (Jung et al. 2015, "origin of gaps") `[NAMED]`.

**⇒ gap = 2·Δ_local FAILS here** — the gap is set by moiré averaging, not by 2Δ. Another
case where an independent Δ breaks the simple law.

---

## 5. MoS₂ / TMDs — honest breakdown of the 2-band picture

Monolayer MoS₂ has a direct gap **~1.8 eV** (Mak et al. 2010) `[MEASURED]`, but the band
edges are **Mo 4d orbitals** (not one p_z per site) and **spin-orbit coupling splits the
valence band by ~0.15 eV** (Zhu 2011; Xiao et al. 2012) `[NAMED]`. The two-band
`[[Δ, vk],[vk*, −Δ]]` Hamiltonian is **not the right model**, so there is no clean
independent-Δ test. TMDs are **flagged, not scored** — exactly as P3's own caveats warn.

---

## 6. Honest verdict

| case | independent Δ source | does gap = 2Δ hold? | what it tests |
|---|---|---|---|
| **silicene (field-tuned)** | Δ_geo = e·E_z·(d/2), d = 0.44 Å | **NO** — off ~3–8× (screening) | the clean test → **FAIL** for naive law |
| germanene, stanene | same (larger d) | **NO** — same screening | same as silicene `[estimate]` |
| **hBN** | TB on-site fit, Δ ≈ 2.3–2.9 eV | **~yes**, but by construction + circular | the standard 2-band model |
| graphene/hBN | DFT local mass | **NO** — moiré averaging | substrate/moiré physics |
| MoS₂ / TMDs | (not applicable) | n/a — wrong Hamiltonian | flagged |

**What this establishes for P3.** P3's "gap = 2Δ" is a **restatement of the standard
gapped-Dirac tight-binding model**. As an *identity* (gap = 2|Δ| for the 2×2 Hamiltonian)
it is exact and untestable. As an *empirical prediction* it becomes non-trivial only where
Δ is an **independent input** — and there (field-tuned silicene) the naive law is
**quantitatively wrong by ~3–8×** because of sublattice polarizability screening, a piece
of ordinary electronic physics that TIG explicitly does not provide. Where the law "works"
(hBN) the success belongs to the textbook model and is partly circular (Δ fit to the band
structure). TIG's sole contribution is the *framing* Δ = sublattice asymmetry — itself the
standard reading of the honeycomb model.

> **STATUS: HONEST NEGATIVE.** P3 as a *falsifiable TIG law* is **not supported**. It
> survives only as a re-labeling of the standard gapped-Dirac model. Recommended edit to
> the skeleton: **drop the "falsifiable slope-2 across materials" language** and state
> "gap = 2Δ" as the exact model identity it is; if the field-tuned prediction is kept, it
> must carry the screening factor (ε ≈ 3–8) as an *input*, at which point the prediction is
> the textbook one, not TIG's. This is a clean proven-dead-end: surface it as a first-class
> negative with the evidence (Drummond's ~8× suppression) that kills it.

---

## 7. Sources

- N. D. Drummond, V. Zólyomi, V. I. Fal'ko, "Electrically tunable band gap in silicene,"
  *Phys. Rev. B* **85**, 075423 (2012); arXiv:1112.4792. — buckling 0.45 Å; screened
  dΔ/dE_z = 0.0742 eÅ; unscreened ~0.554–0.573 eÅ; "suppressed by ~8×"; SO gap 1.5 meV;
  critical field ~20 mV/Å. `[MEASURED/DFT]`
- L. Ni, Y. Liu, Y. Tang et al., "Tunable Bandgap in Silicene and Germanene," *Nano Lett.*
  **12**, 113 (2012); DOI 10.1021/nl203065e. — gap linear in E_z; DFT gap slope ~0.157 eÅ
  (silicene); buckling. `[MEASURED/DFT]`
- C.-C. Liu, W. Feng, Y. Yao, "Quantum spin Hall effect in silicene and two-dimensional
  germanium," *Phys. Rev. Lett.* **107**, 076802 (2011). — SO gaps: silicene ~1.5 meV,
  germanene ~23.9 meV. `[NAMED]`
- T. P. Kaloni et al., "Tuning the electronic structure of silicene/germanene by biaxial
  strain and electric field," arXiv:1504.01157. — states **E_g = e·E·Δ₀** (naive law) and
  the screening/saturation caveat; germanene buckling 0.64 Å. `[NAMED]`
- A. Molle et al., "Buckled two-dimensional Xene sheets," *Nature Materials* **16**, 163
  (2017). — buckling series Si 0.44 / Ge 0.64 / Sn 0.85 Å. `[NAMED]`
- (stanene SO ~0.1 eV, buckling 0.859 Å) *Sci. Rep.* **6**, 31073 (2016) and stanene
  reviews. `[verify]`
- hBN tight-binding on-site / staggered potential: G. G. Ribeiro, N. M. R. Peres,
  *Phys. Rev. B* **83**, 235312 (2011) and later ab-initio TB fits (representative
  ε_B ≈ +3.34, ε_N ≈ −1.40 eV → Δ ≈ 2.37 eV). `[verify]`
- G. Cassabois, P. Valvin, B. Gil, "Hexagonal boron nitride is an indirect bandgap
  semiconductor," *Nature Photonics* **10**, 262 (2016). — hBN gap ~6 eV. `[MEASURED]`
- G. Giovannetti, P. A. Khomyakov, G. Brocks, P. J. Kelly, J. van den Brink, "Substrate-
  induced band gap in graphene on hexagonal boron nitride," *Phys. Rev. B* **76**, 073103
  (2007). — commensurate/lattice-matched graphene/hBN gap ~50 meV. `[MEASURED/DFT]`
- B. Hunt et al., "Massive Dirac fermions and Hofstadter butterfly in a van der Waals
  heterostructure," *Science* **340**, 1427 (2013). — observed graphene/hBN gap ~30 meV.
  `[MEASURED]`
- J. Jung, A. M. DaSilva, A. H. MacDonald, S. Adam, "Origin of band gaps in graphene on
  hexagonal boron nitride," *Nat. Commun.* **6**, 6308 (2015); arXiv:1403.0496. — local
  mass ≫ absolute moiré gap. `[NAMED]`
- K. F. Mak, C. Lee, J. Hone, J. Shan, T. F. Heinz, *Phys. Rev. Lett.* **105**, 136805
  (2010). — MoS₂ monolayer direct gap ~1.8 eV. `[MEASURED]`
- D. Xiao, G.-B. Liu, W. Feng, X. Xu, W. Yao, "Coupled spin and valley physics in
  monolayers of MoS₂...," *Phys. Rev. Lett.* **108**, 196802 (2012); Z. Y. Zhu et al.,
  *Phys. Rev. B* **84**, 153402 (2011). — Mo-d orbital character, SOC valence splitting
  ~0.15 eV. `[NAMED]`
- A. H. Castro Neto et al., *Rev. Mod. Phys.* **81**, 109 (2009). — standard honeycomb
  tight-binding / Δ = sublattice asymmetry. `[NAMED]`
