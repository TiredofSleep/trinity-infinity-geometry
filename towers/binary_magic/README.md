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

> **Run it** (Python 3.10+, numpy, sympy, scipy): `python run_all.py` runs all 39 scripts
> (about 12 minutes) and prints ALL GREEN. `magic_sets/` has its own `run_all.py` (10 scripts).

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
  (MathPages). They are exactly Dudeney's types I–VI, the squares that some cell shift complements:
  Trigg (1948) computed the determinants; Mattingly (2000) and Staab et al. (arXiv:1007.3239, 2010) prove
  the singular direction for every even order.

**Proved here** (hand proofs; each checked on all 880):
- **Every square folds** [FOLD_PROOF.md](FOLD_PROOF.md): a left–right or top–bottom mirror turns every
  value n into n XOR b for one mask b. The proof assumes Nimm0. Not found in Fitting; it is still
  provisional until Conway–Norton–Ryba is read.
- **Degree 3 means invertible:** APD₃ = 24·det(A)/s for any matrix with constant row sum s. An even
  complement rearrangement forces an even degree, so a singular square
  ([`degree_explained.py`](degree_explained.py)). Elementary, and not in Takemura's papers.
- The Walsh-pairing mechanism that gives degree ∞; any XOR symmetry zeroes at least half the binary
  spectrum.
- **A complement under any cell shift forces singularity, with an explicit kernel** (Round 7,
  [`code_lens/void_fold.py`](code_lens/void_fold.py); checked independently by
  [`code_lens/void_fold_check.py`](code_lens/void_fold_check.py)). Every mask b is a reflection n → c − n
  about 7.5, moved by ±2^(q−1) for each bit q it keeps. Only b = 1111 reflects through 7.5 itself, and under
  any shift it zeroes the Walsh block wherever the shift fixes the character. The fact is known (above); one
  Walsh argument for all six singular types, with explicit null vectors, is not in the papers checked.
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

**Only by exhaustion** (true for all 880, no hand proof yet): a square with no complement symmetry is
invertible (known by computation since Trigg 1948; no single bit plane can certify it, Round 7); on an
invertible square every mirror fold flips 3 bits; the centre always has a complement symmetry (a mirror in
240 of 576) and the petals never do; and degree 6 never occurs. (An earlier version said "invertible exactly
when there is a 3-bit fold". That was false: 288 singular squares have 3-bit mirror folds too.)

**Readings: fenced, never premises.**
- The trefoil is a drawing: the carry cube seen down its diagonal. Its knot encodes the rule that
  chained carries share a sign, and it is not a property of the squares. Only the 48-trefoil result
  survives a change of drawing convention.
- The Dirac/Clifford reading re-encodes XOR.
- The metasurface tiles are an analogy.
- Magic squares are not knots, particles or physics.

## Since 2026-10-24: the code lens, and magic sets

Two new folders from the same chat, both pre-registered: predictions were written before each test ran,
and the scores were added after, losses included.

**[`code_lens/`](code_lens/README.md): the squares through the [[16,6,4]] tesseract code.**
- **The fold theorem without citing Nimm0.** Take four bit planes with eight 1s each, every pair of planes
  balanced, and all 10 lines summing to 30. Such a system always has a mirror fold (18,432 systems). Nimm0 is
  derived along the way, by exhaustive search over this relaxation (*computer-assisted*).
  - Fitting's 1931 hand proof of Nimm0 (§III) uses the actual numbers 0–15: the sets of odd numbers and their
    sums, then explicit diagonals. So it depends on full distinctness.
  - The pairwise statement is therefore stronger than his. It is probably new, pending Conway–Norton–Ryba.
- **Sharper for squares:** Nimm0 plus "the 8 diagonal cells sum to 60" forces a mirror fold. This covers
  106,368 semi-magic arrangements, 15 times the magic ones (*proved given Nimm0*: the fold proof never uses
  more). Fitting treats only magic squares, so this extension is not his.
- **Order 8:** in two families of bi-affine shears, magic pulls squares toward mirror folds about 5 times
  (*replicated*). That is scoped to those families; Fitting's family behaves differently (above).

**[`magic_sets/`](magic_sets/README.md): the lens on an open problem.** Trandafir, Lisoněk and Cabello (PRL 2022)
asked for genuine n-qubit magic sets with few observables.
- **Graph stars.** For an odd cycle, they give a critical, genuine n-qubit magic set with 3n + 1 observables:
  16 at n = 5, where the published smallest has 26. They also give the first known sets for odd n ≥ 7.
  ([`magic_sets/THEOREM.md`](magic_sets/THEOREM.md), *proved*.)
- **Checked three ways:** by the chat's code, by an independent referee agent, and here by a third
  implementation, [`magic_sets/independent_star_check.py`](magic_sets/independent_star_check.py). Each
  shares no code with the others. The third enumerates every possible context, and solves for the whole
  space of commutation patterns.
- **Even n:** the members are genuine but not critical, so they are not fair records.
- **Lower bound** (context-minimal sets):
  - n = 5: **16 is the exact minimum.** All three cases with 15 or fewer observables are empty: C = 5 with V = 14
    and 15, and C = 6 with V = 15, the last by `magic_sets/lower_bound5.py` (24.7 million hypergraphs,
    computer-assisted). So the C5 graph star is optimal.
  - n = 4: no genuine set with at most 6 contexts of 3–5 observables, at any size (L4, held).
  - In every context-minimal clash the noncontextual bound is exactly C − 2 (Lemma 5). The published sets
    are not context-minimal: 16 of their 18 hide a smaller clash among their own contexts. In MS5-26, the
    published 5-qubit record, every one of its 3,051 minimal hidden clashes fits on at most 4 qubits
    ([`magic_sets/LOWER_BOUND.md`](magic_sets/LOWER_BOUND.md)).
- **Literature:**
  - All 14 papers that Semantic Scholar lists as citing the 2022 paper (October 2026) were checked at
    abstract level, and none states this construction.
  - Waegell's thesis (arXiv:1307.6264), Chapter 6, was read from the PDF. Its Star families put every
    observable in exactly two IDs, so they reduce to the square or the pentagram. Computed, each with N ≥ 4
    fits on fewer than N qubits. The odd-N Star shares the C_n graph star's counts but not its structure.
  - Still unread in full: the all-versus-nothing proofs for graph states.
- **Not sent:** a draft note to the authors, the author's decision. It is kept with his private papers, not here.

**[`void_lens/`](void_lens/README.md): squares measured from their unoccupied center (Round 8, 2026-10-24).**
Subtract the center value (n² + 1)/2 first, then count. The chat's referee checked it, and so did a second,
independent implementation here ([`void_lens/void_lens_check.py`](void_lens/void_lens_check.py), 15 of 15).
- **MATLAB's odd magic(n) has a closed-form determinant:**
  (−1)^((n−1)/2) · n^(n−1) · (n² + 1)/2 · ∏ (n^|O| − (−1)^|O|), over the orbits O of doubling mod n.
  - Exact for every odd n up to 101, so magic(n) is never singular, and n^(n−1) divides the determinant. That
    proves what Robert Israel observed on OEIS A160523 in 2015.
  - The closed form is *probably new*. That the squares are nonsingular follows, unstated, from Manjunath &
    Ambikasaran's 2022 eigenvalue bounds.
- **Why the doubly-even magic(n) has rank 3:** the tiled sign pattern (1, −1, −1, 1) times a rank-2 ramp. This is
  *known*: Manjunath & Ambikasaran 2022, Theorem 9, answered Moler's "I don't see how" from 2012.
- **Prime order:** p·π₁(L₁) + π₂(L₂) + 1, built from two cyclic Latin squares with any digit relabelings, is never
  singular. The proof uses valuations at (1 − ω), the technique behind Chebotarev's theorem.
  - So **every pandiagonal 5×5 magic square is nonsingular** (all 28,800).
  - The prime matters: there are singular members at n = 9.
  - *Probably new*, pending a fuller search. Lee et al. (2012) construct nonsingular regular squares of prime
    order by another route.
- **The void index:** a complement symmetry by involutions P and Q forces nullity ≥ |(f_P + f_Q)/2 − 1|.
  - It contains Staab et al.'s two theorems as special cases.
  - At order 4 it is exact. Dudeney's two groups of 8 have a complement symmetry of index 0 and stay invertible
    (atlas v6).
- **Where it stops:** at order 5, 5 of 19 sampled singular squares have no void at all. Their kernels are
  accidental.
- `void_lens/applications/` reproduces known theorems from four fields with the same counting. They are
  illustrations only, fenced in the folder's README.

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
| [`code_lens/`](code_lens/README.md) | the tesseract-code lens: pre-registered rounds 1–6c, the antinomy detector |
| [`magic_sets/`](magic_sets/README.md) | graph-star magic sets: theorem, pre-registration, lower bound, referee code, a third independent check |
| [`void_lens/`](void_lens/README.md) | Round 8: squares measured from their center. The odd MATLAB determinant, prime-order nonsingularity, the void index, an independent check, and fenced applications |
| [`HANDOFF_2026-10-24.md`](HANDOFF_2026-10-24.md) | the second handoff from the chat, as received |
| `artifact/` | the interactive atlas page; rebuild with `python artifact/atlas_data.py`, then put `atlas_data.json` into the template |
| `order8/` | samplers (C source for two; the JavaScript one runs with Node), data, and tests. The compiled binary in the handoff was not committed: compile the C source yourself |

## Open
1. **Read Conway–Norton–Ryba (2017).** It is paywalled, and it may contain the fold.
2. **Prove the exhaustion-only rules.** The fold is the lever. One step is easy: a complement fold whose
   shift keeps the main diagonal in place forces carry corner 000 (checked in `independent_check.py`).
   The hardest is "no complement symmetry ⟹ invertible" (240 squares). It is known by computation (Trigg
   1948), but no hand proof is known here, and Round 7 shows that any 2-adic proof has to mix bit planes.
3. **Recipes.** Fitting's "Primterme" already generate all 880 from 14 types under four operations.
   Reproduce his 14 types, then ask what the folds add.
4. **Order 8.** Which squares fold? Fitting's half-shift families do and the affine squares do, but none of
   the 17 annealed fully binary squares does. Find what decides it.
5. **A hand proof that pairwise balance forces Nimm0** (code_lens Round 6c). It must use the separate
   diagonal condition F̂(01,01) + F̂(10,10) = 0.
6. ~~The 5-qubit lower bound, case C = 6, V = 15.~~ Done 2026-10-24: empty, so 16 is the exact minimum
   among context-minimal sets ([`magic_sets/LOWER_BOUND.md`](magic_sets/LOWER_BOUND.md)). Still open: n = 4 beyond
   6 contexts of 3–5, n ≥ 6, and the published sets' wider class (sets that hide smaller clashes).
7. **A hand proof that no complement symmetry ⟹ invertible** (240 squares; known by computation since Trigg
   1948). It has to mix bit planes (Round 7).
7. **Finish the citation check** on Trandafir–Lisoněk–Cabello 2022 (full texts) before anything is sent.
