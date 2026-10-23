> **Working log of the chat, 2026-10-20 and 21, kept as written.** Its status notes predate the
> reading of Fitting 1931. Where they differ from [`NOVELTY.md`](NOVELTY.md) and [`ATLAS.md`](ATLAS.md),
> those files are the later reading. In particular, the carry rules and the layer-by-layer
> cancellation of the diagonals are Fitting's. Start at [`README.md`](README.md).

# Binary magic — every magic arrangement built from cube and tesseract corners

Run `python3 binary_magic.py` (about 4 seconds). It enumerates everything and asserts the known counts.

**Level 3 — the cube's corners 0–7 (3 bits).** No 2×2×2 magic cube exists. Exactly one 2×4 magic
rectangle does, up to order: its rows are forced to be the two interlocked tetrahedra
({0,3,5,6} and {1,2,4,7}, even vs odd number of 1-bits), and its columns are forced to be the
cube's four long diagonals (n, 7−n).

**Level 4 — the tesseract's corners 0–15 (4 bits).** All 7,040 magic squares, 880 essentially
different (Frénicle, 1693 — reproduced). Every square splits into four bit layers (0/1 grids).
- 528 are built purely from binary: every bit layer has exactly two 1s per row, column and
  diagonal, so the square is magic because each layer is.
- No square has exactly 3 balanced layers: three balanced layers force the fourth, because
  30 = 2 × (1 + 2 + 4 + 8).
- The 48 pandiagonal squares and the 48 associative squares (opposite cells are long diagonals,
  n and 15 − n) are all fully binary, and the two families never overlap. Dürer's 1514 square is
  associative.

`squares_4x4.json` holds all 880 squares with their features. Classical results (Frénicle's 880,
the 48 pandiagonal squares) are reproduced, not new; the bit-layer classification is the
computed contribution here. Next level up: 5 bits gives 32 corners — not a square number, so it
returns to a rectangle (4×8), exactly as 3 bits did.

## Cross-check with Dudeney's 12 groups (1917)
Grouping the 880 squares by where their complementary pairs (n, 15 − n) sit reproduces Dudeney's
12 groups exactly (sizes 304, 96, 96, 56 ×4, 48 ×3, 8, 8). Crossed with bit-layer balance:
- 96, 96 and the three 48-groups (including the pandiagonal and associative ones): all 4 layers balanced.
- the four 56-groups: 8 squares with 1 balanced layer, 48 with 2.
- the two 8-groups: 1 balanced layer each.
- **the 304-group is the only mixed one: 192 fully binary, 64 with one balanced layer, and 48 with
  none.** Bit layers refine Dudeney's largest group into three.

**The 48 "whole-only" squares** are magic even though not one of their four binary layers is balanced:
the balance exists only in the whole, never in any single shadow.
Novelty: not yet checked (OEIS blocks automated search) — check by hand before claiming it.

## The carry cube (`split_check.py`)
**Known ground first.** Conway, Norton & Ryba ("Frenicle's 880 Magic Squares", in *The Mathematics
of Various Entertaining Subjects* vol. 2, 2017) show every row and column of the 880 squares
(numbered 0–15) has nim-sum 0, and the two diagonals have equal nim-sums. With a line sum of 30,
nim-sum 0 forces exactly two 1s per bit layer. So **rows and columns never carry**: in all 880
squares, only the two diagonals ever break binary balance. Verified here, but it's their result.

**What the diagonals do.** On a line, write each layer's count minus 2. Because the line sums to
30, that imbalance is always a sum of three elementary carries: two 1s → one 2, two 2s → one 4,
two 4s → one 8. Each carry is used at most once, the two diagonals carry equal and opposite, and
which carries a square uses is a corner of a 3-bit cube:

| carries used (4→8, 2→4, 1→2) | squares | balanced layers |
|---|---|---|
| 000 | 528 | all four |
| 001 / 010 / 100 | 64 / 64 / 64 | {4s,8s} / {1s,8s} / {1s,2s} |
| 011 / 110 | 56 / 56 | 8s only / 1s only |
| 101 | **0** | — |
| 111 | 48 | none (the whole-only squares) |

By number of carries used (0, 1, 2, 3): **528, 192, 112, 48**.

Forced (provable by line arithmetic, no enumeration needed):
- Layer k is balanced exactly when the carries on both sides of it go unused.
- So a middle layer (2s or 4s) can never be the only balanced one, three balanced layers force the
  fourth, and the only possible balanced sets are the seven listed above.
- Corner 101 is empty: a line using 1→2 and 4→8 but not 2→4 has its 1s and 4s bits frozen, so
  its four different numbers are one of {0,2,8,10}, {1,3,9,11}, {4,6,12,14}, {5,7,13,15}, which sum
  to 20, 24, 36 and 40. Never 30.
- There is no fourth carry closing the ring 8s → 1s: two 8s make 16, not 1. The ring 0-1-2-3-0
  closes only mod 15. Over the integers the chain stays a line with three links.
- The carry corner is the diagonal nim-sum divided by 2. So this table is a re-reading of
  Conway–Norton–Ryba's diagonal nim-sum classes and **is probably already in their chapter.**
  Check it before calling any count new.

Counted (enumeration, not yet explained): 528 / 64 ×3 / 56 ×2 / 48.

**The whole-only squares are the odometer.** All 48 have the same signature: 8 lines perfectly
balanced, one diagonal with layer counts (0,1,1,3) and the other with (4,3,3,1). The low layers'
shortfall is 1+1+2+4 = 8, paid as one extra 8: that's 0111 + 0001 = 1000, the full carry ripple.

**Order 8 (0–63, lines of 8): the rule does not simply repeat.** Lines of 8 allow a layer count
of 0 or 8, so a carry can be used twice and the "middle layer can't balance alone" obstruction
disappears at the line level. Whether real 8×8 squares use that freedom is untested.

## The trefoil view (`trefoil_view.py`)
Look down the carry cube's body diagonal: 000 and 111 land on the same point, the three one-carry
corners form a triangle, and the three two-carry corners form a second triangle turned 60°. A
standard trefoil diagram has the same layout: three petals, three crossings sitting 60° between
them, one center. Each crossing sits between the two petals whose carries it combines.
- Petals (one carry): 64 / 64 / 64. Perfectly three-fold.
- Crossings (two carries): 56 / **0** / 56. The empty one combines 1s→2s with 4s→8s, two carries
  that never touch on the chain 1-2-4-8. Forced empty (see the carry-cube section).
- Center: 000 (528) stacked under 111 (48), the same point in this view.
- The big 304 group lives only on the crossings (32 + 32 = 64) and the center (192 + 48); its petals
  are empty. The petals are filled by the four 56-groups (16 / 16 / 16 each).
- Turning the picture 120° keeps the petals and breaks the crossings. The integers give a path of
  three carries, not a triangle; the triangle would close only mod 15 (two 8s = 16 ≡ 1).

## Does it knot? (`knot_check.py`)
The squares supply one signed quantity: each carry on the carrying diagonal is +1 or −1 (the other
diagonal is the exact opposite). Rule: a present crossing gets crossing sign = carry sign, applied
the same way at every crossing. Knot type is identified by the Kauffman bracket.

- **The drawing:** of the 8 over/under choices on the trefoil projection, exactly 2 are knotted:
  the two where all three crossings agree. The other 6 are unknots. (Standard, reproduced.)
- **The arithmetic:** neighbouring carries must share a sign. Opposite signs would need a layer
  count of 5 or −1 on a 4-cell line. So when all three crossings are present, they always agree:
  the 6 unknotted patterns cannot occur. **Forced.**
- **Result, rule 1** (a crossing is present when the two carries on either side of it are both used,
  as in the trefoil picture): exactly the 48 whole-only squares knot, all as trefoils. Everything
  else is an unknot or an unlink.
- **Result, rule 2** (each carry is one crossing): the same 48 trefoils. The 112 two-carry squares
  become a trefoil with one crossing missing: closed one way it's a Hopf link, the other way an
  unknot. That middle tier depends on the convention; the 48 do not.
- **Handedness:** 24 / 24 among the 880, and a quarter turn of any square flips every carry sign,
  mirroring its trefoil. Each trefoil is chiral; the squares have no preferred hand.
- **Fence:** the drawing comes from the cube view; only the crossing signs come from the squares.
  Flipping the sign convention swaps the two hands and changes nothing else.

The knot sits exactly at the full carry ripple, 0111 + 0001 = 1000.

## Cross-check with an independent classification (`takemura_cross.py`)
Takemura (arXiv:2601.06131, Jan 2026, unrefereed) sorts the 880 squares by the first degree m at
which the alternating power sum over permutations is nonzero: 240 at m = 3, 624 at m = 4, and 16
"complete alternating" squares where it never appears. That paper uses no binary. Counts reproduced here.
- Center (000 and 111): always m = 4 (all 576).
- Petals (one carry): always m = 3 (all 192).
- Crossings (two carries): mixed, 48 at m = 3, 48 at m = 4, 16 at m = ∞. All 16 complete-alternating
  squares sit on crossings, all inside Dudeney's 304 group.
Two independently defined classifications agree exactly on two of the three trefoil regions.
**Unexplained.** Proving why would be the first real theorem in this folder.

## Why the regions match Takemura's degree (`degree_explained.py`)
Write G(t) = Σ sgn(p)·e^{t·f(p)} over permutations p; it equals the determinant of the matrix of
e^{t·A_ij}. Takemura's degree is the order at which G first becomes nonzero.

**Proved by hand** (and checked on all 880):
- **P1.** For any 4×4 matrix with constant row sum s: APD₃ = 24·det(A)/s. Expand the determinant
  column by column: two all-ones columns kill a term, so the first surviving order is 3, and its
  coefficient is the sum of all cofactors, which is 4·det(A)/s. **Degree 3 ⟺ the square is invertible.**
  Takemura's 240 are exactly the 240 invertible squares.
- **P2.** Suppose rearranging rows by r and columns by c turns every number n into 15 − n. Then
  G(t) = sgn(r)·sgn(c)·e^{2st}·G(−t). An even rearrangement forces an even degree, so the square is
  singular. An odd one forces an odd degree.
- **P3.** If that rearrangement maps the main diagonal onto itself, the diagonal holds two
  complement pairs, so every bit appears twice on it: no carries (corner 000).
- **P4.** If the rows (or columns) pair up so that each pair differs by a nonzero multiple of a
  Walsh vector (h_a for one pair, h_b ≠ h_a for the other), then G ≡ 0 exactly when
  (A_i − A_k)·(h_a·h_b) = 0. This catches all 16 complete-alternating squares and nothing else.

**By exhaustion** (finite, so a proof, but it gives no reason):

| Dudeney group | complement rearrangement | degree | trefoil region |
|---|---|---|---|
| 304 | even, diagonal → anti-diagonal | 4 (288), ∞ (16) | center 240, crossings 64 |
| 96, 96 | even, diagonal → elsewhere | 4 | center |
| 48 ×3 | even, diagonal → diagonal | 4 | center (forced by P3) |
| 56 ×4 | none | 3 | petals 48, crossings 8 |
| 8 ×2 | odd | 3 | crossings |

Region by rearrangement type: **center = always even** (576), **petals = never any** (192),
**crossings = all three kinds** (64 even, 16 odd, 32 none).

**What it means:** carries don't cause the degree. Both are read off one object: where the
complement pairs sit (Dudeney's pattern). That pattern's parity sets the degree's parity (proved),
and its relation to the diagonals sets the carries (P3, plus exhaustion).

**Still only by exhaustion:** squares with no rearrangement or an odd one are invertible (degree 3,
never 5); even ones have degree 4 unless P4 applies (never 6); center squares always have an even
rearrangement and petal squares never have one.

**Novelty:** Takemura's paper does not connect the degree to the determinant, to complement parity,
or to Walsh structure. These identities are elementary, so check further before calling them new.

## Going Fourier (`fourier_check.py`)
Three Fourier transforms of a square, and what each of today's findings becomes:

| Finding | Fourier statement |
|---|---|
| rows and columns sum to 30 | wave spectrum (2D DFT) and binary spectrum (Walsh) are silent on both axes |
| two diagonals sum to 30 | the 3×3 Walsh block has M₃₃ = 0 and M₁₁ = −M₂₂ |
| determinant / Takemura degree 3 | det A = s·det(M)/64: invertible exactly when the Walsh block is |
| carry in bit plane k | −(trace of that plane's Walsh block)/8 |
| metasurface beams | squared DFT of each bit plane |
| Takemura's degree | first nonzero moment of the signed spectrum c_v, where G(t) = Σ c_v e^{tv} |

**The full binary Fourier transform.** Treat the square as a map from 4 position bits (row, column) to
4 value bits: a 4-bit S-box. Its complete Walsh table is the cryptographers' linear approximation table.
- **432 of the 880 squares are affine over GF(2)**: value = (fixed 0/1 matrix)·(position bits) XOR
  constant. Their binary spectrum is just 15 single spikes. All are fully binary (corner 000). They
  make up the two 96-groups, the three 48-groups, and 96 of the 304 group.
- **Every one of the 880 squares folds:** a left–right or top–bottom mirror maps every value n to
  n XOR b for one fixed mask b (b = 1111 is the ordinary complement). Checked by exhaustion.
- **Proved, given the fold:** if the fold swaps the two diagonals, every bit plane that carries must
  be flipped by b. A plane the fold leaves alone has the same count on both diagonals, and the
  diagonals are always opposite, so that plane must be balanced. So the fold's mask bounds the carries.
- **Proved:** every XOR symmetry A(x⊕a) = A(x)⊕b zeroes every Walsh entry with u·a ≠ v·b. So every
  magic square has at least half its binary spectrum exactly zero.

Novelty: these follow from standard S-box facts applied to magic squares. Conway–Norton–Ryba's
nim-sum treatment may already contain the fold. Check before claiming it.

## The fold, proved (`FOLD_PROOF.md`, `fold_proof_check.py`)
Given Nimm0, every 4×4 magic square has a left–right or top–bottom XOR fold. The proof uses the Walsh
spectrum of each bit plane (a lone spike or a full 2×2 block), the fact that bit planes are orthogonal,
and a binary-dominance argument showing every plane is balanced on corners + center. A side result:
the two diagonals cancel plane by plane. Every step is checked on all 880 squares.

## Order 8 (`order8/`)
- 2,000 annealed 8×8 magic squares on 0–63 (C sampler): no row/column bit balance, no XOR symmetry,
  no diagonal cancellation, carries up to size 3, none singular.
- 30 annealed squares with rows/columns forced bit-balanced: still no XOR symmetry; diagonals cancel
  in 1 of 30.
- Exact count of affine fully binary 8×8 magic squares: 12,631,127,040 up to rotation/reflection.
  All of them fold. The same method gives 432 at order 4.
- Verdict: at order 4 the fold is a law; at order 8 it belongs to a family. The proof's first step
  needs every balanced row to be a single Walsh pattern, which is true on 4 cells and false on 8.

## Quantum: qubit and qutrit (`context_check.py`, `quantum_check.py`, `mermin_magic.py`)
- **The 880 can't be contextuality grids.** At most 3 non-identity two-qubit operators commute, and the
  lines have 4, so only the row and column through 0 qualify. The same limit stops the Lo Shu as one qutrit.
- **Two qubits:** 15 commuting triples and 10 grids, every one a Mermin–Peres square (odd sign
  parity; classical best 8/9; quantum 9/9 with two Bell pairs). This reproduces known results.
- **A Mermin–Peres square that is also a magic square.** Over all 28 qubit labelings there is exactly
  one, up to rotation and reflection:
  `11 13 6 / 5 10 15 / 14 7 9` (sum 30), i.e. `XY YZ ZX / ZZ XX YY / YX ZY XZ`.
  In base 4 it is two orthogonal Latin squares on {1, 2, 3}: Euler's Lo Shu construction in the qubit
  alphabet (1 = Z, 2 = X, 3 = Y). Rows and columns have all-different digits, so they commute and
  XOR to 0 (1⊕2⊕3 = 0). Each diagonal has one digit position all the same, which leaves a residue,
  so the diagonals are not measurement sets. In base 3 (Lo Shu), "all the same" also balances
  (3x ≡ 0); in binary it doesn't. Novelty: not seen; check.
- **One qutrit:** the KCBS pentagram. Five measurements in a cycle, neighbours orthogonal. Classical
  maximum 2, quantum maximum √5 = 2φ − 1 (φ = golden ratio), which equals the Lovász theta of the pentagon.

## Two qutrits (`qutrit_grids.py`)
There is no 3×3 grid of two-qutrit operators at all: none with commuting rows and columns whose lines
multiply to the identity. Not even a non-paradoxical one. 320 such triples exist; none assemble.
**Proof:** the four corner cells fix the whole grid. Let a = [x01, x10] and b = [x00, x11]. The last
row commutes exactly when a = b; the last column exactly when a = −b. In binary +1 = −1, so a = b = 1
works, and that is the Mermin square. In base 3 the two conditions force a = b = 0. Then all nine cells
lie in one isotropic plane, which has only 8 non-identity operators, so nine distinct cells cannot fit.
The same enumerator finds exactly the 10 qubit grids, so the search is sound.
Reading (fenced): the paradox grid closes only where a thing equals its own opposite (1 = −1).
