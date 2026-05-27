# Physics papers — HOLD plan pending experimentalist collaborator

**Status**: Proposed hold plan, awaiting approval.

The TIG main README's §3.5 ("Distribution stance: why submissions are on hold")
already states the project's submission posture. The physics papers
in `05_papers/physics/` make the highest-stakes claims and are the most
sensitive to that posture. This plan formalizes which physics papers should
move from `05_papers/` to `_staging/` (held but visible) until an experimental
collaborator is named OR the framing is moved to "predicted invariant / open
question" rather than "result".

## Candidates

| J# | Title | Current status | Hold reason |
|----|----|----|----|
| **J36** | Empirical Fits of CKM and PMNS Mixing Angles to Substrate-Algebra Primitives | REVISED | Tier-E parametric fits framed as "results"; needs an experimentalist or framing pivot |
| **J39** | NV S₄ Synthesis: Substrate-Operator-Driven NV-Center Qutrit Predictions | R1 | Pre-registered prediction; needs an NV-center experimentalist to validate the protocol |
| **J49** | Microtubule Q_c = T*: A Falsifiable Substrate-Algebra Prediction | DRAFT | Same — needs terahertz microtubule experimentalist |
| **J40** | Logarithmic Nonlinearity (BB reading) | R1 | Less risky — could go to JMP standalone; evaluate. |

## Recommendation per paper

### J36 (CKM/PMNS) — HOLD or reframe

The 17-parameter fit to CKM/PMNS angles using substrate-algebra primitives is a strong-claim physics paper. Without a particle-physics collaborator who can vouch for the fit's significance vs the appropriate null distribution, this risks the "Tier-E numerology" criticism.

**Two paths**:
- **Path A**: hold in `_staging/J36_HOLD/` until particle-physics collaborator.
- **Path B**: reframe as "*Empirical invariants of substrate primitives that happen to match CKM/PMNS to 17 parameters: an observation pending physical interpretation*" — explicitly NOT a "result", but an "observation". This is honest and publishable in a venue like Annales Henri Poincaré Section 'Speculations and Conjectures'.

Recommendation: **Path B** (reframe). The numbers are real; the interpretation requires collaboration.

### J39 (NV qutrit) — HOLD strictly

The six-pulse microwave synthesis is a concrete experimental prediction (a protocol that, if executed, would either confirm or refute S₄ symmetry on an NV center). Without an NV experimentalist who agrees to run the experiment, the paper is in suspended-prediction limbo.

Recommendation: **HOLD in `_staging/J39_HOLD/`** with clear banner: "*This prediction is pre-registered. Experimental run pending NV-center collaborator. Contact: brayden@7site.co*".

The R1 referee report should be addressed in the staged version; once an experimentalist signs up, the paper can be quickly promoted.

### J49 (microtubule Q_c) — HOLD or downgrade

Already addressed in `04_RETIRE_to_meta.md`. Recommendation: Path A (HOLD in `_staging/`).

### J40 (logarithmic nonlinearity) — REVIEW first

J40 reads the Bialynicki-Birula 1976 result on logarithmic nonlinearity through the substrate lens. This is more mathematical than experimental — it's a "structural rhyme" paper, not a falsifiable prediction.

Recommendation: **leave in `05_papers/physics/` but submit to JMP rather than PRD**. The math claim (BB's uniqueness theorem applies to the substrate-derived nonlinearity) is defendable; the physical-interpretation claim should be modest.

## Net effect

| Paper | Action | Destination |
|---|---|---|
| J36 | Reframe + stay | `05_papers/physics/J36/` with revised abstract |
| J39 | Hold | `_staging/J39_HOLD/` |
| J49 | Hold | `_staging/J49_HOLD/` (per Retire plan) |
| J40 | Leave as JMP submission | `05_papers/physics/J40/` |
| J45, J48 | Retire | per Retire plan |

## What this protects

- **Credibility**: high-claim physics papers either have experimental backing or are reframed as observations. No "claimed result" without a path to falsification.
- **Optionality**: held papers can be revived instantly when collaboration appears.
- **Honest distribution stance**: matches the main README's §3.5 posture.

## What this does NOT do

- Doesn't delete anything. Every paper stays accessible.
- Doesn't censor speculation. Reframing makes the tier discipline explicit, doesn't suppress.

## Action checklist (if approved)

- [ ] J36: write abstract reframe; keep in physics/ with new framing
- [ ] J39: create `_staging/J39_HOLD/` with banner; mirror current content
- [ ] J49: same treatment as J39
- [ ] J40: confirm venue (JMP) and submit per existing draft
- [ ] Update `05_papers/physics/` README

**Estimated effort**: 4 hours total (mostly framing language for J36, banners for J39/J49).
