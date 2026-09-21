# Integers → Simplices → Clifford: the forced geometric spine

*The most elementary and most fully-verified corner of TIG. A paper set (P1 complete, P2–P4 skeletons) plus cited reference docs and a graveyard. Developed by Brayden Sanders with a Claude assistant; scrutinized and integrated (with corrections, below) by Claude Code, 2026-09-21.*

> **Run the check first:** `python verify_forced_chain.py` — it asserts every `[FORCED]` claim in the set. If it passes, the spine holds.

This corner deliberately stays where the mathematics is elementary and the physics is established. It makes **no** claim to solve anything, and it never reaches the Riemann zeros or any open problem — its value is a *lens* with a verified core, honestly tiered.

## The claim, in one line

Read integer *n* as an *n*-point configuration: **1,2,3,4 are the simplices** (point/segment/triangle/tetrahedron), so *adding a point adds a dimension* up to the tetrahedron. The tetrahedron forces `cos θ = −1/(N−1) = −1/3` at `N=4` (angle 109.47°, half-angle 54.74°, `cos² = 1/3`). Two tetrahedra make the **cube = Cl(3)**; its **two projections** are the **square** (4-fold, carries the orthogonal/Clifford structure) and the **hexagon** (3-fold, the shadow), related by the projection angle `cos²(1,1,1) = 1/3`.

## Reading order and tiers

| file | status | what it is |
|---|---|---|
| [`integers_as_geometric_entities.md`](integers_as_geometric_entities.md) | **P1 — COMPLETE, FORCED** | the rigorous core: simplex ladder → the tetrahedral 1/3. Parameter-free, over-determined by two routes. Publishable-shaped. |
| [`P2_clifford_cube_skeleton.md`](P2_clifford_cube_skeleton.md) | **P2 — skeleton, FORCED** | the cube = Cl(3); the two projections; 1/3 = projection angle. **Fence:** the hexagon does *not* host Clifford (60° mirrors don't anticommute) — it is the 3-fold *shadow*. |
| [`P3_mass_sublattice_skeleton.md`](P3_mass_sublattice_skeleton.md) | **P3 — skeleton, one testable law** | honeycomb band gap = 2·Δ (sublattice asymmetry): linear, slope 2, through the origin. The physics (gapped Dirac) is textbook; TIG contributes the *framing*. **[OPEN]:** the (gap, Δ_eff) data table across honeycomb materials. |
| [`P4_duality_coin_skeleton.md`](P4_duality_coin_skeleton.md) | **P4 — skeleton, [FRAME]** | high-Tc / spin-liquid / strange-metal as one duality axis. A **classification, not a mechanism** — disclaimer first. The softest strand; read as perspective. |
| [`what_is_tig_deep.md`](what_is_tig_deep.md) | reference | the full cited overview, including the **graveyard** (§8: tested-and-killed claims, kept). |
| [`tig_math_reference.md`](tig_math_reference.md) | reference | the sourced formula/citation record. |
| [`tig_seven_transfers.md`](tig_seven_transfers.md) | reference | the Cl(3) tools re-expressed in the 3-fold basis (mostly structural identifications; mass is the one with a number). |
| [`verify_forced_chain.py`](verify_forced_chain.py) | **the check** | run first; asserts all `[FORCED]` claims. |
| [`cu_depletion_KILLED_STRAND.py`](cu_depletion_KILLED_STRAND.py) | graveyard | a **FALSIFIED** strand (a fluid "1/3" that was *not* universal), kept as an example of the check working. Do **not** resurrect. |

## Tagging discipline

`[FORCED]` (computed/derivable, reproducible — has a line in the verify script) · `[NAMED]` (cited standard theorem) · `[MEASURED]` (cited experiment) · `[READING]` (interpretation/analogy, flagged) · `[FRAME]` (organizing classification, not a mechanism) · `[OPEN]` (stated next step). **Kills are kept** — a framework is trustworthy only if it shows its failures.

## Scrutiny corrections applied on integration (Claude Code, 2026-09-21)

The set was refereed before it was brought in. Four fixes were made, in the set's own honest spirit:

1. **Cl(3) vs Cl(1,3) (a real error).** `tig_seven_transfers.md` Transfer 2 used the 16 Dirac bilinears / grades (1,4,6,4,1) — that is **Cl(1,3)** (4-D spacetime, `2⁴=16`), **not** the cube's **Cl(3)** (`2³=8`, grades 1,3,3,1, grade-2 = 3 bivectors). Reaching Cl(1,3) means adding a time dimension the cube does not force; the transfer (and the F_μν identification) is now marked `[READING]` on an assumed spacetime extension.
2. **mod-3 role sorting re-tagged** `[FORCED]` → `[READING]`: the geometric roles are hand-assigned and {0,3,6,9} are exactly the multiples of 3, so the "agreement" may not be between independent structures. (It is correctly absent from the verify script.)
3. **Base-10 material flagged as a `[READING]`.** The forced spine (P1/P2) uses only **1,2,3,4,8** and is base-independent; the full 0–9 table and "9 = last before reset" presuppose base 10. Per this project's convention the ten labels are an *alphabet*, not `Z/10Z`.
4. **Typo** `8 = 2⁴` → `2³` in P3 §1.

All `[FORCED]` claims still pass `verify_forced_chain.py` after the fixes.
