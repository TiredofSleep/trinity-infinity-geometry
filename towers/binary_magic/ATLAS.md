# Atlas: the triad of 4×4 magic squares

All 880 magic squares on 0–15 (Frénicle), organized by the three trefoil regions and read through three lenses.
Every number here is reproduced by `triad_atlas.py`. The `README.md` is the working log; this page is the map.

## The three lenses

| Lens | What it reads | Where it lives in a square |
|---|---|---|
| **Bits** | which of the three carries (1s→2s, 2s→4s, 4s→8s) the diagonals use | values, along the diagonals |
| **Folds** | XOR symmetries: a mirror or shift of positions that turns every value n into n XOR b | positions ↔ values |
| **Signs** | determinant, Takemura's degree, the binary (Walsh) spectrum | the alternating sum over permutations |

## The triad

| Region | Bits (carry corner) | Folds | Signs | Dudeney groups |
|---|---|---|---|---|
| **Center** (576) | none (000): 528 · all three (111): 48 | complement fold (b = 1111) in every square; 432 are affine and have all 15 folds | degree 4, all singular | 304 (240), 96 ×2, 48 ×3 |
| **Petals** (192) | exactly one: 64 / 64 / 64 | 3-bit folds only (b flips three bits) | degree 3, all invertible | 56 ×4 |
| **Crossings** (112) | two adjacent: 56 / 56 (the third pair is forced empty) | complement fold 64 · 3-bit fold 48 | 3-bit → degree 3 (48) · complement → degree 4 (48) or ∞ (16) | 304 (64), 56 ×4 (32), 8 ×2 (16) |

**In one line:** the bits choose the region; the folds choose the signs; the crossings are where both kinds of fold meet.

### Inside each region
- **Center:** 432 affine squares (each value bit is an XOR of position bits; the spectrum is 15 single spikes) · 96 complement-folded but not affine · 48 whole-only squares (the full carry ripple 0111 + 1 = 1000; the only squares that knot, as trefoils).
- **Petals:** one carry, which breaks two adjacent bit planes. The 3-bit fold always skips one of the two balanced planes.
- **Crossings:** carries 1→2 + 2→4 or 2→4 + 4→8; 1→2 + 4→8 is impossible. The fold type decides everything on the sign side.

## Rules and their status

| Rule | Status |
|---|---|
| Rows and columns never carry (rows/columns XOR to 0) | known: Fitting 1931 §III; Conway–Norton–Ryba 2017 |
| Carries are contiguous, at most once each, all the same sign; 1→2 + 4→8 alone is impossible | known: Fitting 1931 §II (his B- and C-forms, Satz 4–5); restated here as carries, with a line-arithmetic proof |
| Plane k is balanced exactly when the carries on both sides of it are unused | **proved** (from the carry equations, which are Fitting's) |
| Takemura degree 3 ⟺ invertible (APD₃ = 24·det/s) | **proved** |
| Even complement rearrangement ⟹ even degree ⟹ singular; odd ⟹ odd degree | **proved** |
| A complement fold (b = 1111) is an even rearrangement, so it forces a singular square | **proved** |
| A fold that swaps the diagonals flips every carrying plane | **proved** |
| Any XOR symmetry zeroes every spectrum entry with u·a ≠ v·b (at least half) | **proved** |
| Every bit plane has four 1s among corners + center (diagonals cancel plane by plane) | known: Fitting 1931, Satz 3 (a stronger form); a new proof given Nimm0 in `FOLD_PROOF.md`, step 3 |
| Degree ∞ ⟺ rows (or columns) pair by single Walsh patterns plus one linear condition | **proved** (the ⟸ direction and the condition); that no other mechanism occurs is by exhaustion |
| Every square folds (has a mirror XOR symmetry) | **proved** given Nimm0 (`FOLD_PROOF.md`) |
| Singular ⟺ complement fold; invertible ⟺ 3-bit fold | exhaustion only (⟸ of the first is proved) |
| Petals never have a complement fold; center always does | exhaustion only |
| The split 528 / 192 / 112 / 48 by carrying layers | known: Fitting 1931 §I–II (see `NOVELTY.md`) |
| 432 affine squares; per-corner counts 64 / 56 / 48 | enumeration; the 432 are exactly 9 of Fitting's 11 quadruples of magic layers |

## Scripts

| Script | What it does |
|---|---|
| `binary_magic.py` | enumerates the 880 squares and balance levels; writes `squares_4x4.json` |
| `split_check.py` | Dudeney groups, the carry cube, the forced-empty corner |
| `trefoil_view.py` | the carry cube seen down its diagonal as a trefoil |
| `knot_check.py` | over/under from carry signs, checked with the Kauffman bracket |
| `takemura_cross.py` / `degree_explained.py` | Takemura's classification and the proofs |
| `fourier_check.py` | wave, Walsh and full S-box spectra; folds; affine squares |
| `triad_atlas.py` | this page's table and rule checks |
| `fold_proof_check.py` | checks every step of `FOLD_PROOF.md` |
| `order8/` | annealers (C), order-8 tests, exact affine counts |
| `dirac_tower.py`, `residue_test.py`, `semimagic_test.py`, `metasurface_check.py` | Clifford/Dirac reading, residue tests, metasurface tiles |

## Order 8: what survives (`order8/`)
| Test | Order 4 | Order 8, general (2,000 annealed) | Order 8, rows/columns forced bit-balanced (30 annealed) |
|---|---|---|---|
| rows/columns bit-balanced | always | never | forced in |
| any XOR symmetry (fold) | always | never | never |
| diagonals cancel plane by plane | always | never | 1 of 30 |
| carries contiguous, same sign, size 1 | always | often broken; sizes up to 3 | often broken |
| singular | 640 of 880 | none | none |

- **Affine fully binary squares do exist at order 8, and they all fold:** exactly 12,631,127,040 up to
  rotation/reflection (`affine_count.py`; the same count gives 432 at order 4).
- **Fitting's 1931 family folds too:** every member has half-shift XOR symmetries (2,000 random members
  checked in `order8/order8_families.py`), and almost none is affine. Fitting counts 106,420,469,760 of them.
- **Binary balance does not force a fold:** a fully binary 8×8 square (every layer balanced on every
  line) with no XOR symmetry at all exists. It is printed by `order8/order8_families.py`.
- So at order 8 the structure is a family, not a law. The proof breaks at step 1: on 8 cells only
  14 of the 70 balanced rows are single Walsh patterns.
- The annealed samples are not uniform. "Never" means none in the sample, not a proof.

## Quantum
- The 4×4 squares can't be contextuality grids: lines of 4 are longer than the largest commuting
  set of two-qubit operators (3).
- Exactly one 3×3 square is both a magic square (sum 30) and a Mermin–Peres square:
  `XY YZ ZX / ZZ XX YY / YX ZY XZ`. In base 4 it is Lo Shu's Latin structure on the digits {1, 2, 3}.
- One qutrit: the KCBS pentagram, classical 2 vs quantum √5.
- Two qutrits: no 3×3 commuting grid exists at all (**proved**). The last row needs a = b and the last
  column needs a = −b; in binary these agree (the Mermin square), in base 3 they force a = b = 0 and
  nine cells cannot fit in a plane of eight.

## Open
1. ~~Read Fitting (1931)~~ Done 2026-10-22: see `NOVELTY.md`. His 8×8 families are different from the affine count.
2. Fold recipes: Fitting's prime terms already generate all 880 from 14 types. Reproduce them, then ask what the folds add.
3. Order 8: which squares fold? Not "affine or close to it": Fitting's family folds and is almost never affine, and full binary balance does not force a fold.
4. Read Conway–Norton–Ryba (2017) before claiming anything new.
