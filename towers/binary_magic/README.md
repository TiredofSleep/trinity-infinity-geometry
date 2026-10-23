# Binary magic: the cube's corners, counted in binary

**A floor of the cube tower.** Number the cube's eight corners 000–111. The tesseract's sixteen are
0000–1111, and those sixteen numbers fill the 4×4 magic squares. Read each square one binary digit
at a time and it splits into four 0/1 layers, which turn out to share the magic between them. This
folder works that out for all 880 squares, and says plainly which parts were already known.

**Where it came from.** The author asked for *"a full binary matrix assembly for the whole world of
possible magic squares built by the cube's corners"*. His later directions steered it: *"every one is
three, then it's all the same again"*, the trefoil with petals, crossings and a central crossing, *"go
Fourier"*, *"fold recipes"*, and qubit against qutrit. Each became a test with a pass or a fail. The
work was done in a Claude chat on 2026-10-20 and 21 ([`HANDOFF_2026-10-22.md`](HANDOFF_2026-10-22.md)).
It was scrutinized, extended and checked against the literature in Claude Code on 2026-10-22. The
quotations are as given in the handoff and have not yet been checked against the chat.

**The key idea is ninety-five years old.** F. Fitting split the 4×4 magic squares into binary
"components" in 1931, and he credited the idea to his son, then a student in Göttingen: Hans
Fitting, the algebraist. Fitting's paper already has the layers, the cancellation along the
diagonals, the carry bookkeeping (as his A-, B- and C-forms), the 528 / 192 / 112 / 48 split, Nimm0
and large 8×8 families. [`NOVELTY.md`](NOVELTY.md) gives the section for each, and
[`fitting_crosscheck.py`](fitting_crosscheck.py) checks every one of his statements on all 880 squares.

> **Run it** (Python 3.10+, numpy, sympy, scipy): `python run_all.py` runs all 23 checks
> (about 4 minutes) and prints ALL GREEN.

## What holds, by status

**Known: cite, don't claim.** (Details and sources in [`NOVELTY.md`](NOVELTY.md).)
- The 880 squares (Frénicle 1693; proved complete by Fitting 1931), Dudeney's 12 groups, and the 48
  pandiagonal squares.
- Every layer has exactly two 1s in every row and column (Fitting 1931 §III; Conway–Norton–Ryba's
  "Nimm0", 2017).
- Each layer has two 1s on the corners and two on the centre, so the two diagonals cancel layer by
  layer (Fitting's Satz 3).
- On a diagonal, a layer can carry: two 1s become one 2. Carries are single, chained and of one
  sign, and "1s→2s with 4s→8s" never occurs alone. These are Fitting's B- and C-forms and his
  Satz 4–5. The counts by number of carries are 528 / 192 / 112 / 48, Fitting's §I–II.
- Takemura's degree classes, 240 / 624 / 16 (arXiv:2601.06131), and the 640 singular squares
  (MathPages).

**Proved here** (hand proofs; each checked on all 880):
- **Every square folds** [FOLD_PROOF.md](FOLD_PROOF.md): a left–right or top–bottom mirror turns every
  value n into n XOR b for one mask b. The proof assumes Nimm0. Not found in Fitting; it is still
  provisional until Conway–Norton–Ryba is read.
- **Degree 3 means invertible:** APD₃ = 24·det(A)/s for any matrix with constant row sum s. An even
  complement rearrangement forces an even degree, so a singular square
  ([`degree_explained.py`](degree_explained.py)). Elementary, and not in Takemura's papers.
- The Walsh-pairing mechanism that gives degree ∞; any XOR symmetry zeroes at least half the binary
  spectrum.
- **No two-qutrit grid:** no 3×3 grid of commuting two-qutrit operators with lines that multiply to
  the identity exists ([`qutrit_grids.py`](qutrit_grids.py)).

**Enumerated** (counts, no proof of why):
- 432 of the 880 are affine over GF(2). They are exactly 9 of Fitting's 11 quadruples, because 6 of
  his 8 magic layers are affine.
- 12,631,127,040 affine fully binary 8×8 squares, up to rotation and reflection.
- Exactly one 3×3 square that is magic (sum 30) has rows and columns that all XOR to 0:
  `11 13 6 / 5 10 15 / 14 7 9`. Read in base 4 with 1 = Z, 2 = X and 3 = Y, it is a Mermin–Peres square,
  under exactly one of the 28 ways of labelling two qubits.

**Order 8: the fold is not a law** ([`order8/order8_families.py`](order8/order8_families.py)):
- A fully binary 8×8 square can have **no XOR symmetry at all**, even though every one of its six
  layers is balanced on every line. All 17 squares found by
  [`order8/anneal8_fullbinary.js`](order8/anneal8_fullbinary.js) are like this (the sampler is not
  uniform). The first is printed by the script.
- Every square in Fitting's 1931 family folds by a half-shift (2,000 random members checked), and
  almost none is affine. So at order 8 folding is neither forced by binary balance nor confined to
  the affine squares.

**Only by exhaustion** (true for all 880, no reason yet): singular exactly when there is a
complement fold; invertible exactly when there is a 3-bit fold; the centre always has a complement
fold and the petals never do; and degree 6 never occurs.

**Readings: fenced, never premises.**
- The trefoil is a drawing: the carry cube seen down its diagonal. Its knot encodes the rule that
  chained carries share a sign, and it is not a property of the squares. Only the 48-trefoil result
  survives a change of drawing convention.
- The Dirac/Clifford reading re-encodes XOR.
- The metasurface tiles are an analogy.
- Magic squares are not knots, particles or physics.

## Second implementation, and the literature

| script | what it does |
|---|---|
| [`independent_check.py`](independent_check.py) | A second implementation written from the claims alone: 47 checks. It enumerates the 880 by a different method (row and column partitions), confirms they are the same squares as `squares_4x4.json`, and recomputes every count above, the order-8 count included. Standard library only |
| [`fitting_crosscheck.py`](fitting_crosscheck.py) | Fitting 1931, statement by statement, on all 880 squares |
| [`order8/order8_families.py`](order8/order8_families.py) | The three order-8 families: affine, Fitting's, and annealed fully binary |

## Files

| file | what it is |
|---|---|
| [`ATLAS.md`](ATLAS.md) | the map: the three regions (center, petals, crossings), seen three ways (bits, folds, signs), and the status of every rule |
| [`FOLD_PROOF.md`](FOLD_PROOF.md) | the fold theorem, step by step |
| [`NOVELTY.md`](NOVELTY.md) | what was already known, with sources; what survives as probably new |
| [`WORKING_LOG.md`](WORKING_LOG.md) | the chat's working log, in the order things were found (where its status notes differ from `NOVELTY.md`, `NOVELTY.md` is the later reading) |
| [`HANDOFF_2026-10-22.md`](HANDOFF_2026-10-22.md) | the handoff from the chat, as received |
| `artifact/` | the interactive atlas page; rebuild with `python artifact/atlas_data.py`, then put `atlas_data.json` into the template |
| `order8/` | samplers (C source for two; the JavaScript one runs with Node), data, and tests. The compiled binary in the handoff was not committed: compile the C source yourself |

## Open
1. **Read Conway–Norton–Ryba (2017).** It is paywalled, and it may contain the fold.
2. **Prove the exhaustion-only rules.** The fold is the lever. One step is easy: a complement fold
   whose shift keeps the main diagonal in place forces carry corner 000 (checked in
   `independent_check.py`).
3. **Recipes.** Fitting's "Primterme" already generate all 880 from 14 types under four operations.
   Reproduce his 14 types, then ask what the folds add.
4. **Order 8.** Which squares fold? Fitting's half-shift families do and the affine squares do, but
   none of the 17 annealed fully binary squares does. Find what decides it.
