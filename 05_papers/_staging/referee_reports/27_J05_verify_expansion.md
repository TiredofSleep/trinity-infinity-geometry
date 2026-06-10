# J05 verify script expansion (final-push commit)

**Date**: 2026-05-27
**Scope**: extend `05_papers/algebra/J05/manuscript/verification/verify_J60.py` to cover §4.7's Tier-A claims at orders 3 and 5.

## What changed

The verify script previously had 4 checks (C1–C4). Two new checks were added per the Wave 4 audit (`23_wave4_audit_J05_J07_J17_J22_J27.md` §J05):

### C5 (order-3 enumeration)

Exhaustive enumeration of all $729 = 3^6$ commutative order-3 magmas (symmetric 3×3 tables over Z/3Z). For each magma, compute the ETP equational profile via the cloned `equational_theories` catalog. Assertions:

- 120 magmas have profile 14 (Family C minimum).
- All 120 share the *identical* Family C equation set (commutativity closure).
- 0 magmas have profile < 14 (no sub-Family-C closures exist at order 3 among commutative tables).

### C6 (order-5 enumeration)

Exhaustive enumeration of all 720 symmetric 5×5 Latin squares (commutative quasigroups of order 5). Assertions:

- 480 have profile 14 (Family C minimum).
- All 480 share the identical Family C equation set.
- Profile distribution matches the manuscript §4.7 census: `{14: 480, 15: 120, 32: 30, 89: 24, 90: 30, 176: 6, 294: 30}`.

## Runtime

Per the updated docstring: ~5-6 minutes total (C5 ~2.5 min, C6 ~2.5 min, C1-C4 <1 min combined). Requires a clone of [github.com/teorth/equational_theories](https://github.com/teorth/equational_theories) accessible at `ETP_PATH`.

## Status

`verify_J60.py` now covers all six checks (C1–C6) matching the manuscript §4.7 Tier-A enumeration claims at orders 3 and 5. The Tier-A unsupported-in-deliverable gap flagged by the Wave 4 audit is closed.

## Honest scope note

The C5/C6 checks require the external ETP catalog as a dependency. Anyone reproducing the verification needs to clone the ETP repo and set `ETP_PATH`. This is the standard pattern for ETP-comparison papers and matches the J03 fossil-variety paper's verification approach.

## Files touched

- `05_papers/algebra/J05/manuscript/verification/verify_J60.py` — added C5 and C6 checks, updated docstring + main runner to include new checks in the summary table.
