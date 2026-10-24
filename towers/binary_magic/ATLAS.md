# Atlas: the triad of 4×4 magic squares

All 880 magic squares on 0–15 (Frénicle), organized by the three trefoil regions and read through three lenses.
Every number here is reproduced by `triad_atlas.py`, and the Round 7 numbers (2026-10-24) by `code_lens/void_fold.py`
and, independently, `code_lens/void_fold_check.py`. `WORKING_LOG.md` is the working log; this page is the map.

## The three lenses

| Lens | What it reads | Where it lives in a square |
|---|---|---|
| **Bits** | which of the three carries (1s→2s, 2s→4s, 4s→8s) the diagonals use | values, along the diagonals |
| **Folds** | XOR symmetries: a mirror or shift of positions that turns every value n into n XOR b | positions ↔ values |
| **Signs** | determinant, Takemura's degree, the binary (Walsh) spectrum | the alternating sum over permutations |

## The triad

| Region | Bits (carry corner) | Folds | Signs | Dudeney groups |
|---|---|---|---|---|
| **Center** (576) | none (000): 528 · all three (111): 48 | a complement symmetry (b = 1111) in every square, under a mirror in 240, a row or column swap in 288, the half-turn in 48; 432 are affine and have all 15 XOR symmetries | degree 4, all singular | 304 (240), 96 ×2, 48 ×3 |
| **Petals** (192) | exactly one: 64 / 64 / 64 | 3-bit mirror folds only (b flips three bits) | degree 3, all invertible | 56 ×4 |
| **Crossings** (112) | two adjacent: 56 / 56 (the third pair is forced empty) | complement mirror 64 · 3-bit mirror folds only 48 | 3-bit → degree 3 (48) · complement → degree 4 (48) or ∞ (16) | 304 (64), 56 ×4 (32), 8 ×2 (16) |

**In one line:** the bits choose the region; the folds choose the signs; the crossings are where both kinds of fold meet.

### Inside each region
- **Center:** 432 affine squares (each value bit is an XOR of position bits; the spectrum is 15 single spikes) · 96 more with no carries, not affine · 48 whole-only squares (the full carry ripple 0111 + 1 = 1000; drawn on the trefoil, theirs are the only knotted diagrams, by construction from Fitting's one-sign rule).
  The complement symmetry is a mirror in 240 of them (96 affine, the 96 non-affine, all 48 whole-only) and a swap or the half-turn in the other 336, which are all affine. The 48 under the half-turn are the 48 associative squares.
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
| A complement symmetry under any of the 15 cell shifts forces a singular square: the Walsh block vanishes wherever the shift fixes the character, which leaves an explicit kernel (χ₁₁ = (1, −1, −1, 1) for the left–right mirror) | **proved** (Round 7). The fact is known: Trigg 1948 (order 4, Dudeney's types I–VI), Mattingly 2000 (regular squares of even order), Staab et al. 2010 (their types A and B, every even order; they give no null vector) |
| A fold that swaps the diagonals flips every carrying plane | **proved** |
| Any XOR symmetry zeroes every spectrum entry with u·a ≠ v·b (at least half) | **proved** |
| Every bit plane has four 1s among corners + center (diagonals cancel plane by plane) | known: Fitting 1931, Satz 3 (a stronger form); a new proof given Nimm0 in `FOLD_PROOF.md`, step 3 |
| Degree ∞ ⟺ rows (or columns) pair by single Walsh patterns plus one linear condition | **proved** (the ⟸ direction and the condition); that no other mechanism occurs is by exhaustion |
| Every square folds (has a mirror XOR symmetry) | **proved** given Nimm0 (`FOLD_PROOF.md`) |
| Singular ⟺ a complement symmetry under some cell shift, which is exactly Dudeney's types I–VI | ⟸ proved (above). ⟹ known by computation (Trigg 1948; MathPages), with no hand proof; no single bit plane can certify it (Round 7, V6 and V11) |
| On an invertible square every mirror fold flips 3 bits | exhaustion only. The older row "invertible ⟺ 3-bit fold" was false: 288 singular squares have 3-bit mirror folds too |
| Petals never have a complement symmetry; the center always does (as a mirror in 240 of 576) | exhaustion only |
| The 336 squares complemented by a swap or the half-turn (Dudeney's types I–V) are all affine; the 48 under the half-turn are the associative squares | enumeration (`code_lens/void_fold_check.py`) |
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
| `code_lens/void_fold.py` · `code_lens/void_fold_check.py` | Round 7: every mask as a reflection about 7.5, the complement kernels, the singular classes; and a second implementation of all of it, with the Dudeney/Trigg/Staab correspondence |
| `mermin_28.py` | the 28 two-qubit labellings and the one magic Mermin square |
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
