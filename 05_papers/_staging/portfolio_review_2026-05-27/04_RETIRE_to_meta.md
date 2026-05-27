# Retire to `04_meta/` — speculation, redundancies, weak theorem hooks

**Status**: Proposed retirement plan, awaiting approval.

These papers either duplicate stronger papers, lack a clean theorem hook,
or fit the Tier-C speculation register better than the referee-grade `05_papers/`
register. Moving them to `04_meta/` preserves the work, signals the right
tier discipline to readers, and clears the shippable spine.

## Candidates

### J45 — *A Substrate-Derived FN Pattern with λ=10/49 and SU(5)-Rep Indexing*

**Current location**: `05_papers/physics/J45/`
**Reason to retire**: numerical-pattern paper with SU(5)-rep indexing as the structural claim. The λ=10/49 value comes from substrate combinatorics, but the structural identification with SU(5) reps is Tier-C ("structural rhyme") not Tier-A. Without a derivation from first principles, this is closer to speculation than theorem.

**Proposed action**: move to `04_meta/SPECULATION_J45_FN_pattern.md` with a wrapper header explaining the Tier-C status.

### J48 — *An Operadic Obstruction in a Bilinear-Closed Magma on Z/10Z: A Synthesis*

**Current location**: `05_papers/physics/J48/`
**Reason to retire**: this synthesis paper duplicates J32's "Operadic D₄ Orbits on the Non-Associative Locus" result. J32 has the same theorem with a cleaner proof; J48 doesn't add structural content beyond restating in different language.

**Proposed action**: merge any unique content from J48's exposition into J32; mark J48 as RETIRED-VIA-J32 with redirect.

### J56_DRAFT — *Atomic-Substrate Correspondence: D100–D104 Five Integer Identities*

**Current location**: `05_papers/interdisciplinary/J56_DRAFT/`
**Reason to retire**: the five integer identities between Z/2310 divisor lattice and atomic-shell capacities (D100–D104) are striking but the structural mechanism is speculative. Currently flagged as DRAFT; no clean theorem path to upgrade.

**Proposed action**: move to `04_meta/SPECULATION_J56_atomic_substrate.md`. The integer identities themselves can be cited from there as Tier-C observations.

### J49 — *Microtubule Q_c = T*: A Falsifiable Substrate-Algebra Prediction*

**Current location**: `05_papers/interdisciplinary/J49/`
**Reason for special handling**: NOT a retirement candidate per se — it's a falsifiable prediction. BUT: without an experimental collaborator who has pre-registered to look for Q_c ≈ 5/7 in microtubule terahertz coherence data, the prediction is currently un-testable in practice. This is the situation J34 (algebraic detectors — HONEST NEGATIVE) explicitly contrasts with.

**Two paths**:
- **Path A (HOLD)**: keep in `05_papers/` but flag as "PENDING EXPERIMENTAL COLLABORATOR". Move to `_staging/` with a hold note.
- **Path B (RETIRE)**: move to `04_meta/` as Tier-C structural prediction; resurrect if/when an experimentalist signs up.

Recommendation: **Path A** (HOLD in `_staging/`). The prediction is too clean to bury, but it shouldn't sit in `05_papers/` claiming submission-readiness without the collaboration channel.

### J04 — *(MERGED into J03 on 2026-05-13)*

**Current location**: `05_papers/number_theory/J04/`
**Reason for action**: already marked MERGED. Just formalize the cleanup.

**Proposed action**: keep folder for citation history; reduce `J04/` to a 5-line README pointing to J03; delete `J04/manuscript/` if it duplicates J03's content (CONFIRM J03 absorbed everything first).

## Summary of moves

| Paper | From | To | Action |
|---|---|---|---|
| J45 | `05_papers/physics/J45/` | `04_meta/SPECULATION_J45_FN_pattern.md` | Move + wrap |
| J48 | `05_papers/physics/J48/` | merged into J32 + tombstone in J48/ | Merge + tombstone |
| J56_DRAFT | `05_papers/interdisciplinary/J56_DRAFT/` | `04_meta/SPECULATION_J56_atomic_substrate.md` | Move + wrap |
| J49 | `05_papers/interdisciplinary/J49/` | `_staging/J49_HOLD/` (recommend Path A) | Move with HOLD banner |
| J04 | `05_papers/number_theory/J04/` | (stays, but reduced to tombstone) | Tombstone-only |

## What this changes

- **Tier 1 ("ship") set** is more clearly defined — no speculation papers in the shippable list.
- **04_meta/** picks up 2 substantial speculative papers, which is exactly its purpose.
- **J49** stays visible but explicitly held; prevents accidental submission.

## Action checklist (if approved, all five together)

- [ ] J45 → wrap and move to `04_meta/`
- [ ] J48 → merge unique content into J32, tombstone J48/
- [ ] J56_DRAFT → wrap and move to `04_meta/`
- [ ] J49 → move to `_staging/J49_HOLD/` with banner
- [ ] J04 → reduce to tombstone README
- [ ] Update `05_papers/algebra/`, `05_papers/physics/`, `05_papers/interdisciplinary/` READMEs
- [ ] Update top-level `README.md` directory tree

**Estimated effort**: 1 day total.
