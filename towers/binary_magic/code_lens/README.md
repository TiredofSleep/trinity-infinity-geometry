# code_lens/: magic squares through the tesseract code, tested

Read `PREREG.md`. Every prediction was written there before its test ran, and the score table at the bottom
was added after. Losses are kept.

| script | what it tests |
|---|---|
| `code_lens.py` | Round 1: the 880 squares on the [[16,6,4]] tesseract code (A1–A8), plus asserted post hoc findings P1–P4 |
| `order8_lens.py` | Round 2: fresh order-8 data (O1–O5), plus null-model diagnoses of the two losses |
| `fold_mechanism.py` | Round 3: does "every shuffle of 4 is affine" explain the fold? (necessary, not sufficient) |
| `fold_pull.py` | Round 5: the magic condition pulls toward mirror folds, replicated on a fresh family, with the mechanism |
| `fold_needs.py` | Round 6: the semi-magic world (549,504); the fold needs only Nimm0 + diagonal cells at 60 |
| `nimm0_coupling.py` | Round 6b/c: pairwise-balanced planes + magic lines force Nimm0 and the fold (18,432 systems) |
| `antinomy.py` | the F2 antinomy detector: contexts + parity demands → consistent, or clash + smallest certificate |
| `phase_a_capacity.py` in the [earth-house-kit](https://github.com/TiredofSleep/earth-house-kit) repo | Test C: how many on/off factors the 16-panel plot can screen |

**Status of the main results** (rescoped against Fitting 1931 on 2026-10-24: see `../NOVELTY.md`)
- Every row and column of every 4×4 square is a minimum-weight logical of the tesseract code. *Nimm0
  restated (known, Conway–Norton–Ryba / Fitting).*
- Parallel rows and parallel columns ⟺ affine at order 4, false at order 8. *Proved (order 4); counterexamples
  (order 8). Elementary, probably known; not checked.*
- The diagonal pair is a check exactly for Fitting's 528, and otherwise a logical whose class fixes the carry
  corner. *Exhaustion; found post hoc.*
- At most 4 of 6 two-factor interactions can be balanced in all 8 lines (144 squares, all affine). *Exhaustion.*
- 16 panels can screen at most 9 balanced on/off factors (only affine squares reach it), or 8 with lime × RHA
  reserved. *Exhaustion; a standard saturated row-column design.*
- The fold at 4×4 needs two size-4 coincidences: balanced rows of 4 are affine, and the two diagonals form
  one Walsh pattern. Restoring the first by hand at order 8 leaves 68 of 600 bi-affine magic squares with no
  fold. *Tested (Round 3).*
- Magic pulls toward mirror folds, about 5× in two families (p < 10⁻³³), because a mirror fold ties the two
  diagonals together (88.8% vs 15.5% conditional hit rate). *Replicated (Round 5); mechanism post hoc.*
- **The fold theorem without citing Nimm0:** four bit planes with eight 1s each, pairwise balanced, all 10
  lines at 30 ⇒ a mirror fold. 18,432 systems, Nimm0 derived by exhaustive search. *Computer-assisted.*
- **Sharper for squares:** Nimm0 + the 8 diagonal cells summing to 60 ⇒ mirror fold (106,368 semi-magic
  arrangements). *Proved given Nimm0; exhaustively confirmed.*
