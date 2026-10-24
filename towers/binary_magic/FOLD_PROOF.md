# Every 4×4 magic square folds

**Theorem.** Let A be a 4×4 magic square on 0–15 (all rows, columns and both diagonals sum to 30).
Then A has a left–right or a top–bottom mirror that turns every value into the same XOR of itself:
there is a mask b with A(i, 3−j) = A(i, j) ⊕ b for all cells, or A(3−i, j) = A(i, j) ⊕ b for all cells.

**Assumption N** (proved by Fitting 1931, §III; restated as "Nimm0" by Conway–Norton–Ryba 2017; also verified on all 880 here): in every 4×4 magic
square, every bit plane has exactly two 1s in every row and every column.

Checked step by step on all 880 squares by `fold_proof_check.py`.

## Setup
Index rows and columns 0–3 by 2-bit strings. The three nonconstant Walsh patterns are
χ₀₁ = (+,−,+,−), χ₁₀ = (+,+,−,−), χ₁₁ = (+,−,−,+). For bit plane k, write D_k = 1 − 2B_k (entries ±1)
and its spectrum M_k(r, c) = Σ D_k(i, j)·χ_r(i)·χ_c(j) for r, c ∈ {01, 10, 11}.

## Step 1: each plane's spectrum has one of two shapes
Under N, every row of D_k has two +1s and two −1s, so it is ±χ_a for one a (the row's *type*).
The same holds for columns. Rows with the same type come in opposite-sign pairs, because the column
sums are zero and the χ's are orthogonal. That leaves two possibilities:
- **Type I:** all four rows share one type. D_k = ±χ_r(i)χ_c(j) and the spectrum is a single ±16.
- **Type II:** two pairs of rows with types a ≠ b. The spectrum is a full 2×2 block of ±8s, on
  columns {a, b} and rows {r : r·p = 1}, where p is the XOR of the two row indices in a pair.

Spectrum columns are the row types; spectrum rows are the column types. Every axis entry is zero.

## Step 2: planes are orthogonal
The 16 values are distinct, so any two bits k ≠ l take each of the four combinations exactly four
times: Σ D_k·D_l = 0. By Parseval, the spectra have zero inner product: Σ M_k(r,c)·M_l(r,c) = 0.

## Step 3: every plane is zero at (11, 11)
The pattern χ₁₁(i)χ₁₁(j) is +1 on the corners and the central 2×2 (the two diagonals) and −1
elsewhere. The two diagonals together sum to 60, half the total, so the whole square's spectrum is zero
at (11, 11). Writing A = 7.5 − Σ 2^{k−1}·D_k gives Σ_k 2^k·n_k = 0 with n_k = M_k(11,11)/8 ∈ {0, ±1, ±2}.
- If some n_k = ±2, plane k is a lone spike at (11, 11). Another plane must also be nonzero there,
  because one nonzero term cannot sum to zero, and that plane cannot be orthogonal to a lone spike
  at the same spot. Contradiction.
- Otherwise every |n_k| ≤ 1, and the highest nonzero term outweighs all the lower ones together.
  So every n_k = 0.

*Bonus:* every bit plane has exactly four 1s among the corners and the centre. So the two diagonals
carry equal and opposite amounts in every plane. This is Fitting's Satz 3 (1931, p. 182), in a weaker form: he shows two 1s on each of the corners, the centre and the two sets of edge middles, by residues mod 2, 4, 8 and 16. The proof here, by spectra, is new.

## Step 4: when a plane survives a mirror
The left–right mirror j ↦ 3−j is j ↦ j ⊕ 11. It multiplies χ₀₁ and χ₁₀ by −1 and leaves χ₁₁
alone. So plane k is symmetric (if all its row types are 11) or antisymmetric (if all are in
{01, 10}) under it. The only way to fail is a plane whose spectrum columns mix 11 with 01 or 10.
Call it an **α plane**. Likewise top–bottom fails only on a plane whose spectrum rows mix 11 with
01 or 10, a **β plane**. Type I planes are never α or β.

## Step 5: α and β never meet
By Step 3, a Type II block cannot contain (11, 11). So
- an α plane has rows {01, 10} and columns {11, x}, and
- a β plane has rows {11, y} and columns {01, 10}.

Their supports meet in exactly one cell, (y, x), where both are ±8. Their inner product is ±64 ≠ 0,
which contradicts Step 2. So a square cannot contain both.

## Conclusion
Either no plane is α, so the left–right mirror works, or no plane is β, so the top–bottom mirror
works. The mask bit b_k is 1 exactly when plane k is antisymmetric under the mirror that works. ∎

## Scope: what the proof actually uses

Only three things:
- Nimm0;
- pairwise orthogonality of the planes (Step 2);
- the combined sum of the 8 diagonal cells (Step 3).

So the same proof covers every semi-magic arrangement with Nimm0 whose diagonal cells sum to 60: 106,368 of
them, checked in `code_lens/fold_needs.py`. It also covers every system of four pairwise-balanced planes
with magic line sums, once Nimm0 is derived for that system (`code_lens/nimm0_coupling.py`).

## What it unlocks
- "Every square folds" moves from exhaustion to proof, given N.
- The per-plane diagonal cancellation is proved (Step 3).
- With the earlier results: a complement fold (b = 1111) is an even rearrangement, so it forces
  a singular square (proved).

**Not proved here:** N itself, which is Fitting's theorem (1931, §III, a case analysis). **Still by exhaustion:** singular ⟹
complement fold, and petals never having a complement fold.

**Why it does not transfer to order 8:** Step 1 needs every balanced row to be a single Walsh
pattern. On 4 cells all 6 balanced rows are (±χ). On 8 cells only 14 of the 70 balanced rows are.
