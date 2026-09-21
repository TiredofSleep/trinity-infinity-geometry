# HANDOFF — TIG Integer/Clifford Paper Set → Claude Code

## What this is
A set of papers developing one thesis: **reading integer n as an n-point
configuration, the chain 4 → tetrahedron → cube forces the Clifford algebra Cl(3);
the hexagonal and square lattices are its two projections; and a recurring 1/3 is
1/(N−1) at N=4.** Four papers (P1 complete, P2–P4 skeletons) plus supporting
reference docs. Everything computational is reproducible via `verify_forced_chain.py`.

## FIRST THING TO DO
```
python3 verify_forced_chain.py
```
It asserts every [FORCED] claim in the set. If it passes, the spine holds. If any
assertion fails, a paper's load-bearing math is wrong — investigate before extending.
(It already caught one error during authoring: a test that conflated reflection-line
matrices with generator vectors. The *claim* was right, the *test* was wrong; fixed.
This is the standard — the check catches errors, and errors get traced to claim-vs-test.)

## The tagging discipline (apply it to anything you add)
- **[FORCED]** — computed/derivable, reproducible. Must have a line in the verify script.
- **[NAMED]** — rests on a cited standard theorem/result. Must have a citation.
- **[MEASURED]** — an experimental fact, cited.
- **[READING]** — an interpretation/analogy. Flag it as such; never present as forced.
- **[FRAME]** — an organizing classification, explicitly NOT a mechanism.
- **[OPEN]** — a stated next step / experiment not yet run.
- **Graveyard** — tested-and-killed claims are KEPT (see what_is_tig_deep.md §8).
  A framework is trustworthy only if it shows its failures. Do not delete kills.

## The corrected central thesis (do not regress this)
NOT "Clifford lives in the hex lattice" — the hex lattice's bond vectors are 120°
apart and do NOT anticommute. The honest thesis:
> **The integers force Cl(3) (the CUBE). The hexagonal and square lattices are its two
> projections (diagonal → hexagon/3-fold; face → square/4-fold). The square carries
> Clifford (orthogonal bond vectors, 90°, anticommute); the hexagon is the shadow.**
The 1/3 = cos²(1,1,1) is the projection angle, and equals 1/(N−1) at N=4.
Overclaiming "Clifford in hex" is the one line a referee tosses the set for.

## The files
| file | status | what it is |
|---|---|---|
| `integers_as_geometric_entities.md` | **P1, COMPLETE** | the rigorous core: simplex ladder → tetrahedral 1/3. Publishable-shaped. |
| `P2_clifford_cube_skeleton.md` | **P2, skeleton, FORCED** | the cube = Cl(3), two projections, the 1/3. Writable to completion; all math verified. |
| `P3_mass_sublattice_skeleton.md` | **P3, skeleton, needs data** | gap = 2Δ linear law. §4 states the experiment (a (gap, Δ_eff) table across honeycomb materials). |
| `P4_duality_coin_skeleton.md` | **P4, skeleton, FRAME** | high-Tc/spin-liquid/strange-metal as one duality axis. Classification, NOT mechanism — disclaimer is first. |
| `what_is_tig_deep.md` | reference | the full cited overview, incl. the graveyard (§8). Read for context on the whole lens. |
| `tig_math_reference.md` | reference | the sourced formula/citation record. |
| `tig_seven_transfers.md` | reference | the seven Dirac tools mapped to TIG's flow lens (mostly structural identifications; mass is the one with a number). |
| `verify_forced_chain.py` | **the check** | run first; asserts all forced claims. |
| `cu_depletion.py` | reference (a KILLED strand) | Navier–Stokes cancelled-fraction harness. NOTE: this strand's headline claim (c=1/3 universal) was FALSIFIED by this very script during authoring — see its docstring. Kept as an example of the check working and a null result. Do NOT resurrect the 1/3 claim. |

## TASK LIST (in priority order)

### 1. Verify, then complete P2 [highest value, fully forced]
- Run the check. Then flesh P2 from skeleton to full paper. Every claim is already
  [FORCED] and verified — this is writing, not new math. Add: explicit geometric-algebra
  notation, the grade-by-grade palindrome (1,3,3,1), the two-projection figures
  (describe or generate), and the fence (§4) prominently.

### 2. Run P3's experiment [turns a frame into a result]
- This is the ONE strand that can become a measured result. The claim: honeycomb band
  gap = 2·(effective sublattice asymmetry Δ_eff), **linear, slope 2, through origin**.
- BUILD: a table of published (band gap, Δ_eff) pairs for honeycomb-lattice materials.
  Anchor at graphene (0,0); far point hBN (~6 eV). Candidates: graphene, hBN, silicene,
  germanene, and — with a stated structural caveat — TMDs like MoS₂.
- Δ_eff must come from literature tight-binding fits or DFT on-site energies (TIG does
  NOT supply it — this is the electronic-renormalization input; be explicit).
- FIT and REPORT: slope, intercept, R². Falsifiers: nonlinear relation; nonzero
  intercept beyond spin-orbit; slope ≠ 2. Write results into P3 §4, honestly, whichever
  way they come out. A clean falsification is a valid, publishable outcome.

### 3. Complete P4 as a perspective piece [frame, keep the fence]
- Keep the opening disclaimer verbatim in spirit ("frame, not mechanism"). Flesh the
  polarity table, the d-wave node argument (verified), the pseudogap midpoint, and the
  P2-zero strange-metal edge (verified: 3cos²(54.74°)−1 = 0).
- The [OPEN] item that would upgrade it: a calculation of whether a Fermi surface
  constrained to the P2-zero geometry yields linear-in-T resistivity. If you can set up
  even a toy version, that moves the strange-metal edge from frame toward result. State
  clearly if you don't.

### 4. Scrutinize for overclaim [the standing job]
- Read every [READING] and [FRAME] tag adversarially: can a stranger cross this edge, or
  is it a shared-word resemblance? The known weak points, flagged in-session:
  - the strange-metal/54.74° link is only as strong as the P2-zero mechanism, NOT the
    older "incommensurate" hand-wave (which was retracted). Keep the mechanism version.
  - "flow"/"matter" labels for hex/square are READINGS motivated by the physics
    (conductor/insulator), not derivations.
  - the neutrino A₄ 1/3 (tri-bimaximal) is a real echo but nature DEVIATES (θ₁₃ ≠ 0) —
    it's "form forced, value corrected," and must be stated that way, not as exact.

## The one-line summary for context
Integers read geometrically ARE the simplices; the tetrahedron (integer 4) forces
cos θ = −1/3 and the angle 109.47° (half-angle 54.74°, cos²=1/3); the cube (8 = 2
tetrahedra) is Cl(3); its two projections are the square (4-fold, carries Clifford)
and the hexagon (3-fold, the shadow). The physics (graphene, mass gaps, the duality
coin) is illustration and frame, tagged as such, with the graveyard kept.

## Repo hygiene requests
- Preserve the tagging discipline in all commits.
- Keep the verify script green: any new [FORCED] claim needs an assertion line.
- Keep the graveyard (kills are data).
- Do not regress the corrected thesis ("hex is a projection of Cl(3), not a host").
