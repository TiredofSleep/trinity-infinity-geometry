# P3 — the "gap = 2Δ" data table, honestly tested

*Data pull + honest test for the P3 experiment tagged `Testable-pending-data` in
`verify_forced_chain.py`. Assembled by Claude Code, 2026-09-22. Companion to
`P3_mass_sublattice_skeleton.md`. No claim is upgraded here; the point is to hold the
published numbers against P3's **actual** statement and report what they do and do not
show. Discipline: `[MEASURED]` (cited experiment), `[NAMED]` (cited standard result),
`[verify]` (value technique-dependent / not pinned — range given, not a fabricated point).*

---

## 0. One-line finding (read this first)

**The task framed the test as "superconducting gap ratios 2Δ/(k_B T_c) across
materials." P3 does not make that claim.** P3's "gap = 2Δ" is a **honeycomb Dirac
*band-structure* law** — Δ is the on-site A/B **sublattice energy asymmetry** (eV), and
the "gap" is a **semiconductor/insulator band gap** (graphene → hBN), *not* a
superconducting pairing gap. The BCS relation `2Δ/k_B T_c = 3.53` is a **different Δ and
a different physical law**. Superconductivity in this paper set lives in **P4**, which is
an explicit `[FRAME]` and states **no** `2Δ/k_B T_c` law at all.

So this note does two things honestly:
- **Table A** — the requested superconducting `2Δ/k_B T_c` ratios (real, cited data). It
  is included because it was asked for and is legitimate, **but it does not test P3.**
- **Table B** — P3's *actual* domain (honeycomb band gaps vs sublattice asymmetry),
  which is what *would* test P3 — and why even that test is under-specified as P3 stands.

---

## 1. P3's exact claim (quoted, not paraphrased)

From `P3_mass_sublattice_skeleton.md`, Abstract and §2 (verbatim):

> "the band gap at the Dirac point is **exactly 2Δ**, where Δ is the on-site A/B energy
> difference … This is *linear in the asymmetry, with slope 2, passing through the
> origin*, and it is the paper's falsifiable claim."

> "H = [[Δ, v k], [v k\*, −Δ]] … Eigenvalues: **E = ±√((v|k|)² + Δ²).** At the Dirac
> point (k = 0): **E = ±Δ**, so **gap = 2Δ.** [FORCED — this is the exact gapped-Dirac
> result, standard.]"

> "**The mass identification:** TIG-mass ≡ Δ = the sublattice asymmetry. Massless
> (Δ = 0) ⇔ A = B; massive (Δ ≠ 0) ⇔ A ≠ B."

The experiment P3 states (§4, verbatim):

> "**Claim to test:** across honeycomb and honeycomb-derived materials, the band gap is a
> linear function of the effective sublattice asymmetry Δ_eff, slope 2, through the
> origin."

And the check itself, from `verify_forced_chain.py` (lines 80–85):

```python
def gap(D): return 2*abs(D)
for D in [0,0.5,1.0,3.0]:
    ok(f"gap(Delta={D}) = 2*Delta = {2*D}", abs(gap(D)-2*D)<1e-12)
ok("gap law is linear, slope 2, through origin", gap(0)==0 and abs((gap(2)-gap(1))-2)<1e-12)
#   OPEN: the (gap, Delta_eff) data table across honeycomb materials is NOT
#         run here -- that is the experiment. see P3 skeleton section 4.
```

**Δ here has units of eV and is a sublattice on-site energy.** Nowhere does P3 mention
T_c, k_B, Cooper pairs, or a superconducting gap. Confirmed by grep over the whole
`integers_clifford/` folder: `T_c`, `BCS`, `2Δ/k_BT_c`, `Cooper`, `Nb3Sn`, `MgB2` appear
**only** in P4 (`P4_duality_coin_skeleton.md`) and `what_is_tig_deep.md`'s P4 section —
never in P3.

## 2. Two different "2Δ" — the category distinction (the crux)

| | P3's "gap = 2Δ" | BCS "2Δ = 3.53 k_B T_c" |
|---|---|---|
| what Δ is | on-site **sublattice energy asymmetry** (a band-structure parameter) | **superconducting pairing gap** (Cooper-pair binding) |
| what "gap" is | **band gap** of a honeycomb semiconductor/insulator | **pair-breaking energy** 2Δ of a superconductor |
| the "2" | forced by diagonalizing a 2×2 Hamiltonian: E = ±Δ ⇒ span 2Δ | just "twice the gap" (two quasiparticles) |
| the law's content | gap **∝ Δ_eff**, slope 2, across honeycomb materials | 2Δ **∝ T_c**, universal slope **3.53** (not 2), across BCS materials |
| materials | graphene, hBN, silicene, germanene, TMDs | Al, Sn, Nb, Pb, Nb₃Sn, MgB₂, cuprates |
| in this paper set | **P3** (a testable structural law) | **P4** — and P4 is `[FRAME]`, states **no** ratio law |

The two share the string "2Δ" and nothing else. A test that pours superconducting
`2Δ/k_B T_c` numbers into P3's slot is a **category error**; it neither confirms nor
refutes P3. It is reported below anyway (it was requested, and it is honest data), but
labelled for what it is.

---

## 3. Table A — superconducting gap ratios 2Δ/(k_B T_c)  *(requested; does NOT test P3)*

Ratios are **technique- and sample-dependent**; the literature genuinely scatters (e.g.
Nb has been reported from ~2.8 to ~4.1). Point values are the commonly-cited central
figures; ranges reflect real spread. `[verify]` marks values I did not pin to one
canonical measurement.

| material | T_c (K) | 2Δ/k_B T_c | coupling / notes | source |
|---|---|---|---|---|
| **BCS weak-coupling (s-wave)** | — | **3.53** (=2π/e^γ=3.528) | the universal reference | BCS 1957 [NAMED] |
| **BCS weak-coupling (d-wave)** | — | **≈4.28** | reference for cuprates, not 3.53 | Won–Maki 1994 [NAMED] |
| Al | 1.2 | ~3.3–3.4 | weak coupling, ≈ BCS | Tinkham textbook [NAMED] |
| Sn | 3.7 | ~3.5–3.6 | near BCS, slightly above | Richards–Tinkham 1960 [MEASURED] |
| In | 3.4 | ~3.6 (some ~4.1) | moderate; real spread | Richards–Tinkham 1960 [MEASURED] |
| Nb | 9.3 | ~3.6–3.8 (lit. 2.8–4.1) | moderate–strong; wide spread | tunneling/far-IR [MEASURED] |
| Pb | 7.2 | ~4.3 (4.1–4.5) | **strong coupling**, clearly > 3.53 | Richards–Tinkham 1960; tunneling [MEASURED] |
| Nb₃Sn | ~18 | ~4.2–4.8 | **strong coupling** A15; 2nd gap debated | Godeke 2006 review [MEASURED] |
| MgB₂ (σ band) | 39 | ~4–5 | **two-gap**; σ is strong-coupling | Souma 2003; Iavarone 2002 [MEASURED] |
| MgB₂ (π band) | 39 | ~1.1–2 | **two-gap**; π is *below* BCS | Souma 2003; Iavarone 2002 [MEASURED] |
| YBCO (YBa₂Cu₃O₇) | ~92 | ~2.5–6 across Fermi surface | **d-wave, anisotropic** | ARPES reviews [MEASURED] `[verify]` |
| Bi2212 / BSCCO | ~85–95 | ~5–9 (nodal plateau ≈ 8.5) | **d-wave**; ≈2× d-wave weak-coupling | Vishik/Nat.Comms 2013 [MEASURED] |
| LSCO (La₂₋ₓSrₓCuO₄) | ~38 | ~4–6 | **d-wave**, doping-dependent | cuprate reviews `[verify]` |

**What Table A shows (on its own terms, not as a P3 test):**
- The "universal" `3.53` holds only for **weak-coupling s-wave**. Real materials span
  **~1.1 → ~9** — a factor of ~8.
- Strong coupling (Pb, Nb₃Sn, MgB₂-σ) sits systematically **above** 3.53 (Eliashberg
  corrections); MgB₂-π sits **below** it; cuprates (d-wave, whose own weak-coupling
  reference is 4.28) sit far above.
- There is **no** single ratio, and certainly no "slope 2." If one *insisted* on reading
  this as a "gap = 2Δ, universal" law, the data **strains/refutes** it — but that law is
  a strawman P3 never asserted.

Simple statistics on the s-wave/compound set {Al 3.35, Sn 3.55, In 3.6, Nb 3.7, Pb 4.3,
Nb₃Sn 4.5, MgB₂-σ 4.5} (central values; cuprates and MgB₂-π excluded as different
symmetry / second band): **mean ≈ 3.93, sample std ≈ 0.45, range 3.35–4.5.** The mean
sits above 3.53 (strong-coupling materials pull it up); the spread is real; **none of
this is 2, and none of it is P3.**

---

## 4. Table B — P3's ACTUAL domain: honeycomb band gap vs sublattice asymmetry

This is the table §4 of P3 actually calls for. `Δ_eff` is the effective on-site A/B
asymmetry, which — **P3 concedes this explicitly** — TIG does *not* supply; it must come
from tight-binding fits or DFT. That concession is the whole problem for testing (see §5).

| material | bond | measured band gap | Δ_eff (independent input needed) | source |
|---|---|---|---|---|
| graphene | C–C | **0** (Dirac semimetal) — anchor | 0 (A = B) | Novoselov–Geim 2005 [MEASURED] |
| silicene | Si–Si | ~1.5 meV (SOC-induced) | ≈0 (SOC, not sublattice) | Liu 2011 [NAMED] `[verify]` |
| germanene | Ge–Ge | ~24 meV (SOC) | ≈0 (SOC) | Liu 2011 [NAMED] `[verify]` |
| MoS₂ (TMD) | Mo–S | ~1.8 eV (monolayer, direct) | large — but d-orbitals + strong SOC break the simple 2-band picture | Mak 2010 [MEASURED] |
| hexagonal BN | B–N | ~6 eV | large (far anchor) | Cassabois 2016 [MEASURED] |

**What Table B shows:** the **sign/direction** is confirmed and undisputed — symmetric
sublattice (graphene, A=B) ⇒ gapless; asymmetric (hBN, B≠N) ⇒ large gap. P3 already lists
this as `[MEASURED]` §3. The tiny silicene/germanene gaps are **spin-orbit**, not
sublattice asymmetry, so they do not sit on the P3 line (P3 flags this caveat itself).

## 5. Honest assessment — does the data support P3?

**Primary finding — wrong instrument (domain mismatch).** The requested superconducting
`2Δ/k_B T_c` table (Table A) **does not test P3.** P3 is a honeycomb band-gap law; the SC
ratio is a different Δ and a different relation (and belongs, in this set, to the P4
`[FRAME]`, which asserts no such ratio). So on the literal task framing, the verdict is
**not "support/neutral/strain" but "not applicable — the data measures a different
quantity."**

**On the SC data read as a universality claim:** it **strains** any "single/universal gap
ratio" reading — `2Δ/k_B T_c` runs from ~1.1 (MgB₂-π) to ~9 (cuprates), is 3.53 only for
weak-coupling s-wave, and is never 2. (This is the well-known strong-coupling +
d-wave story; cuprates famously deviate, exactly as the task anticipated.)

**On P3's *actual* claim, assessed on its own terms — the honest core:**
1. The **form** "gap = 2Δ" is an **exact algebraic identity**, not an empirical law:
   diagonalizing `[[Δ, vk],[vk*, −Δ]]` gives `±Δ` at `k=0`, span `2Δ`, for *any* Δ. It is
   true by construction of the model and so is **not falsifiable** as a "law." The verify
   script's P3 block confirms only this identity (`gap(D)=2*|D|`) — i.e. arithmetic, not
   a data test.
2. The **empirical** content P3 wants — *gap ∝ Δ_eff, slope 2, through the origin, across
   materials* — is **under-specified**: P3 itself states TIG does not supply `Δ_eff`
   (§4 step 2, §5). Without an **independent** `Δ_eff` (from DFT/tight-binding, *not* from
   the gap), the slope-2 test is **circular** — setting `Δ_eff := gap/2` makes slope 2
   true trivially, and any independently-fit `Δ_eff` inherits the electronic
   renormalization (~2× in hBN) that P3 concedes lives *below* the geometry.
3. The available band-gap data (Table B) confirms only the **sign** (symmetric → gapless,
   asymmetric → gapped), which is already textbook and already tagged `[MEASURED]` in P3.
   It does **not** establish the quantitative slope-2 linearity, because the independent
   `Δ_eff` column does not yet exist.

**Verdict:** **The data does not yet support the P3 linearity claim, and P3 as stated is
under-specified.** This is exactly the paper's own `[OPEN]` tag, now made concrete: the
`2Δ/k_B T_c` superconducting numbers are the wrong instrument (a different Δ); and P3's
own honeycomb law cannot be tested as a *prediction* until an independent `Δ_eff` dataset
(literature tight-binding or DFT on-site energies) is assembled — at which point the real
risk is that the test collapses to an identity. **Honest status: NOT-YET-TESTABLE /
UNDER-SPECIFIED**, tending to **STRAINED** if forced into the superconducting framing.
Preferred next step: either (a) drop the "falsifiable slope-2 across materials" language
and state "gap = 2Δ" as the exact model identity it is, or (b) actually assemble the
independent `Δ_eff` column of Table B and confront the circularity head-on.

---

## References (cited values above)

- J. Bardeen, L. N. Cooper, J. R. Schrieffer, *Phys. Rev.* **108**, 1175 (1957) — BCS;
  weak-coupling ratio 2Δ/k_BT_c = 3.528.
- M. Tinkham, *Introduction to Superconductivity*, 2nd ed., McGraw-Hill (1996) — textbook
  gap-ratio table (Al, Sn, In, Nb, Pb weak/strong-coupling values).
- P. L. Richards, M. Tinkham, *Phys. Rev.* **119**, 575 (1960) — far-IR energy gaps in
  In, Sn, Hg, Ta, V, Pb, Nb. https://link.aps.org/doi/10.1103/PhysRev.119.575
- H. Padamsee, J. E. Neighbor, C. A. Shiffman, *J. Low Temp. Phys.* **12**, 387 (1973) —
  elemental gap ratios / strong-coupling α-model context.
- K. S. Novoselov, A. K. Geim et al., *Nature* **438**, 197 (2005) — graphene Dirac
  fermions (gapless anchor).
- C.-C. Liu, W. Feng, Y. Yao, *Phys. Rev. Lett.* **107**, 076802 (2011) — silicene/
  germanene SOC gaps (~1.5 meV / ~24 meV).
- K. F. Mak, C. Lee, J. Hone, J. Shan, T. F. Heinz, *Phys. Rev. Lett.* **105**, 136805
  (2010) — MoS₂ monolayer direct gap ~1.8 eV.
- G. Cassabois, P. Valvin, B. Gil, *Nature Photonics* **10**, 262 (2016) — hBN gap ~6 eV.
- A. Godeke, *Supercond. Sci. Technol.* **19**, R68 (2006), arXiv:cond-mat/0606303 —
  Nb₃Sn strong-coupling review. https://arxiv.org/pdf/cond-mat/0606303
- S. Souma et al., *Nature* **423**, 65 (2003) — MgB₂ multiple gaps (photoemission).
  https://pubmed.ncbi.nlm.nih.gov/12721624/
- M. Iavarone et al., *Phys. Rev. Lett.* **89**, 187002 (2002) — MgB₂ two-gap tunneling.
- I. M. Vishik et al. / "Relation between nodal and antinodal gap and T_c in Bi2212,"
  *Nature Communications* **4**, 2459 (2013) — nodal 2Δ/k_BT_c ≈ 8.5.
  https://www.nature.com/articles/ncomms2805
- A. Damascelli, Z. Hussain, Z.-X. Shen, *Rev. Mod. Phys.* **75**, 473 (2003) — ARPES on
  cuprates (YBCO/Bi2212/LSCO gap anisotropy and ratios).
- H. Won, K. Maki, *Phys. Rev. B* **49**, 1397 (1994) — d-wave weak-coupling ratio ≈4.28.
- Review context on elemental/compound ratios: *Superconductivity in the elements, alloys
  and simple compounds*, arXiv:1502.04724. https://arxiv.org/pdf/1502.04724

*Cuprate point values (YBCO, LSCO) are marked `[verify]`: they are strongly
technique- and doping-dependent and anisotropic (d-wave), so a single number is not
meaningful — the ranges above are the honest representation.*
