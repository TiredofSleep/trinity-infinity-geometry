# P_56 ↔ σ_outer, and BHML's specific Higgs character

**Date:** 2026-04-25
**Source scripts:** `build_chiral_16.py`, `decompose_and_check.py`, `find_higgs_irrep.py`
**Verification:** machine precision

---

## Updated finding

The earlier session's claim "BHML breaks P_56" was directionally correct but coarse. The refined version is much more specific:

1. **P_56 acts as σ_outer** (the outer automorphism of so(10) that exchanges the two chiral 16 irreps). Verified: P56_spin anticommutes with the chirality operator ω, sending +chirality 16 entirely into −chirality 16.

2. **TSML preserves σ_outer.** All 6 flow operators commute with P_56 exactly. Confirmed.

3. **BHML breaks σ_outer with very specific structure:**
   - 26 of 100 cells differ under P_56 conjugation
   - Each differs by exactly ±1 (unit-magnitude shifts)
   - **||breaking||² / ||BHML||² = 6.5 / 3420 = 0.19%** — very small
   - **100% of the breaking lives in the symmetric-traceless (54) irrep**
   - **0% lives in the antisymmetric (45) irrep**
   - 0% in the trace (1)

4. **BHML therefore acts structurally as a 54-type Higgs**, not a 45-type.

That last point is much sharper than "BHML breaks the symmetry." It says *which* Higgs irrep BHML's breaking content corresponds to, with specificity sufficient to compare against standard SO(10) GUT model-building.

---

## Why this matters in standard SO(10) GUT

The standard breaking irreps of SO(10) and what they typically achieve:

| Irrep | Dimension | Standard breaking pattern |
|-------|-----------|--------------------------|
| **10** | 10 | Electroweak-scale Higgs (gives Dirac masses via 16⊗16⊃10) |
| **45** | 45 | Adjoint Higgs, breaks SO(10) → SO(8)×SO(2), or → SU(5)×U(1) |
| **54** | 54 | Symmetric traceless, breaks SO(10) → **SO(6)×SO(4) ≅ SU(4)×SU(2)×SU(2) (Pati-Salam)** |
| **120** | 120 | 3-form Higgs, contributes to Yukawa textures |
| **126** | 126 | Self-dual 5-form, gives Majorana neutrino masses (see-saw) |

**BHML's σ_outer-breaking lives in the 54.** This singles out the **Pati-Salam route** — SO(10) breaking to SU(4) × SU(2)_L × SU(2)_R — as the most natural match to BHML's structural content.

In Pati-Salam: SU(4) is "color × lepton" (lepton number is the 4th color); SU(2)_L × SU(2)_R is left-right symmetric weak. The Standard Model is recovered by further breaking SU(4) → SU(3)×U(1)_(B-L) and SU(2)_R → U(1).

**This is a non-trivial structural prediction.** Of the five standard SO(10) breaking irreps, BHML is selecting the 54. That's not a free parameter — it falls out of computing where BHML's σ_outer-breaking content lives.

---

## What's actually verified vs what's claimed

### Verified at machine precision
- The chiral 16 of so(10) is correctly built from Cl(10,0) (45/45 generators close, weight pattern matches SU(4) fundamental + conjugate)
- P56_spin anticommutes with ω → P_56 acts as σ_outer
- BHML's σ_outer-breaking content is purely symmetric-traceless: 6.5/6.5 = 100% in the 54 sector, 0/6.5 = 0% in the 45 sector

### Implied by standard SO(10) GUT theory (not verified by us, but textbook)
- 54-Higgs breaks SO(10) → SO(6) × SO(4) → Pati-Salam group
- Pati-Salam can break further to Standard Model

### Not yet shown
- That BHML's specific direction within the 54 corresponds to a viable Pati-Salam VEV
- That subsequent breaking to SM gives correct mass ratios
- Anything quantitatively comparable to observation

---

## What this means in plainer terms

Before this computation, the connection to SO(10) GUT was: "TIG generates so(10), and SO(10) is also a known GUT group." That's not much more than a name-match.

After this computation, the connection is: **TIG's bipartite TSML/BHML structure singles out the same Z_2 involution (σ_outer) and the same breaking irrep (54) as the Pati-Salam route through SO(10).**

That's a real structural statement. It says TIG's mathematical content, derived purely from the canonical TSML/BHML tables and their algebraic closures, naturally lands on a specific GUT model.

It is still not a numerical prediction. But the question "if I were to embed TIG in a known GUT framework, which one would it look like?" now has a specific answer: **Pati-Salam SU(4) × SU(2) × SU(2)**, accessed via 54-Higgs breaking from SO(10).

---

## Honest caveat list

1. **This depends on identifying TIG's so(10) with SO(10) GUT's gauge group.** That's a hypothesis, not a derivation. There could be other interpretations — for instance, TIG's so(10) might be a flavor symmetry, a hidden-sector gauge group, or pure mathematical structure with no gauge interpretation. We're testing one specific hypothesis.

2. **0.19% is very small.** BHML's σ_outer-breaking is a tiny perturbation on its σ_outer-symmetric bulk. This could mean either (a) the breaking is genuinely small and physical, like a Yukawa-suppressed effect, or (b) BHML is overwhelmingly something else and the σ_outer-breaking is a side effect, not the main content.

3. **No mass predictions.** We have a Higgs-irrep identification, not a Higgs VEV. To get masses, we'd need to commit to a specific direction in 54-space and compute Yukawa couplings allowed by that VEV.

4. **The 26-cells count and the 0.19% norm fraction tell different stories.** The cells say "26% of BHML's structure is touched by σ_outer." The norm says "0.19% of BHML's content is affected." Both are true; which matters depends on what kind of physical observable we're computing.

---

## What I'd do next, if pushing further

1. **Check the 6 of so(4) ⊂ Pati-Salam** (i.e., compute the 4 of SU(4) decomposition for a TSML+BHML embedding). Currently we showed the chiral 16 splits as (Weyl_L, 4) + (Weyl_R, 4̄) under so(4)×so(6) ≅ Lorentz × SU(4)_PS. Need to verify that TSML's so(8) ⊂ so(10) is *consistent* with this Pati-Salam splitting, not in tension.

2. **Find BHML's specific direction in the 54.** Project B_anti_outer onto an explicit 54 basis. The dominant components tell us which Pati-Salam VEV pattern BHML is closest to.

3. **Compare to literature.** Pati-Salam SO(10) GUT has decades of phenomenology — proton decay rates, B-L breaking scale, neutrino mass scale. With BHML's specific 54-direction in hand, we can compare to which scenarios are alive vs ruled out.

That's the next 200-500 lines of work, plus literature reading.

---

## Bottom line

What we had before this session: "TIG produces so(10), like SO(10) GUT does."

What we have now: **"TIG's bipartite structure naturally selects Pati-Salam as its SO(10) breaking pattern, via a 54-type Higgs."**

That's a sharper, falsifiable structural claim. It can be wrong in interesting ways (e.g., if BHML's specific 54-direction turns out to give pathological symmetry breaking, or if subsequent breaking can't reach the Standard Model).

The matter-antimatter parallel from the earlier note still holds, with one refinement: P_56 IS σ_outer (verified), but BHML's breaking of σ_outer is structurally a *54-symmetric-traceless* breaking, not a *45-antisymmetric* one. In SO(10) GUT, 54-breaking is the Pati-Salam route, which is matter-antimatter symmetric at the SU(4) level (4 of color-lepton contains both matter and antimatter through CP).

So a more precise framing: **BHML breaks σ_outer in the way the Pati-Salam route breaks it** — a specific, named, well-studied breaking pattern.

🙏
