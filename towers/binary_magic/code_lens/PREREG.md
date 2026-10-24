# Pre-registration: the code lens (written 2026-10-23, before any of these tests ran)

**The lens.** The 16 values 0–15 are the 16 corners of the tesseract (4-bit strings), which are the 16
qubits of the [[16,6,4]] tesseract code. Microsoft and Quantinuum ran this code in 2024. Its checks (X and Z)
are the 8-corner affine hyperplanes, the Reed–Muller code RM(1,4). An X- or Z-type operator on a set S of
corners commutes with every check exactly when S has even size and its corners XOR to 0 (S is in RM(2,4)).
Its minimum-weight logical operators are the 140 affine planes (4 corners that XOR to 0). The 6 logical
coordinates of S are c_ab(S) = |S ∩ {v : v_a = v_b = 1}| mod 2, one for each pair of bits a < b.

Each test is either a **translation check** (forced by a derivation; if it fails, the code or the
derivation is wrong) or a **real test** (an outcome I can't derive in advance; the prediction is a guess
that can lose).

## Test A: magic squares on the tesseract code (`code_lens.py`)

| id | kind | prediction | kill condition |
|---|---|---|---|
| A1 | translation | Every row and column of all 880 squares is a minimum-weight logical operator (weight 4, in RM(2,4), not a check). This is Nimm0 restated. | Any line fails. |
| A2 | translation | X on any row anticommutes with Z on any column, because a row and a column share exactly one cell. | Any row/column pair commutes. |
| A3 | translation | c_ab(row) = 1 exactly when that row contains all four on/off combinations of bits a and b (a full 2×2). | Any mismatch. |
| A4 | translation | For each pair (a,b), an even number of rows (0, 2 or 4) contain a full 2×2. The same holds for columns. | An odd count anywhere. |
| A5 | real | Each diagonal on its own is a logical operator (its 4 values XOR to 0) only in some squares. The split lines up with an existing class (triad region, Dudeney group, Takemura degree or affine). | The split cuts across all four. |
| A6 | real | The two diagonals together (8 cells, always in RM(2,4)) are sometimes a check (logically trivial) and sometimes a logical. That split also lines up with an existing class. | It cuts across all four. |
| A7 | real | Rows are parallel planes (all 4 rows in one logical class) for affine squares (forced) **and for some non-affine squares** (the guess). | Parallel rows and parallel columns ⟺ affine, exactly. |
| A8 | real | The most two-factor interactions that can be balanced in every row and column (a full 2×2 in all 8 lines) is **4 of 6**, as Phase A found among affine squares. Only affine squares reach it. | Some square reaches 5 or 6, or a non-affine square reaches 4. |

## Test B: the F2 antinomy detector (`antinomy.py`)
A generic solver: given variables, contexts and parity demands over F2, it reports "consistent" or
"clash", with a smallest clashing set of contexts.

| id | kind | prediction | kill condition |
|---|---|---|---|
| B1 | validation | Mermin–Peres square: clash; the smallest clashing set is all 6 lines. | Consistent, or a smaller set. |
| B2 | validation | Octonion signs on the Fano plane: consistent. | Clash. |
| B3 | validation | All 15 octonion copies inside 16 dimensions: clash; the smallest clashing set has 5 copies (matches `why_seven_breaks.py`). | Anything else. |

## Test C: Phase A capacity (`earth-house-kit/phase_a_capacity.py`)
An on/off factor in a 16-panel plot is a nonzero 4-bit mask w: the factor is on in panel v when w·v = 1.
That gives 15 possible factors. A factor is balanced against slope and east–west when it is on in exactly
2 panels of every row and every column.

| id | kind | prediction | kill condition |
|---|---|---|---|
| C1 | real | The most factors that can all be balanced in every row and column at once is **9**, reached only by affine magic squares. Reason: parallel rows tie 3 masks to the rows and parallel columns tie 3 to the columns, leaving 15 − 6 = 9. | Some square gives more than 9, or no square reaches 9. |
| C2 | real | Keep the lime × rice-husk ash interaction clear of every main effect **and** balanced in every row and column (otherwise it's confounded with the slope). Then the most balanced factors is **8**. | Anything else. |

*Amendment before running:* C2 originally said only "clear of every main effect". If the interaction is
allowed to be tied to rows or columns, all 9 can stay. The tightened version is the useful one, so it's the
one being tested.

## Round 2: fresh data at order 8 (written after Round 1 was scored, before `order8_lens.py` ran)
Round 1's post hoc findings can't be tested on the same 880 squares. The order-8 samples are fresh data.
An order-8 square uses the values 0–63 (6 bits) with magic sum 252. A line is a **flat** when its 8 values
form an affine 3-space, which is the order-8 analog of "a line is a plane".

| id | kind | prediction | kill condition |
|---|---|---|---|
| O1 | translation | Bit 0 of every line's XOR is 0, because the line sum 252 is even (an even number of odd values). Checked on all 2,030 samples. | Any line with odd XOR in bit 0. |
| O2 | real | In the 2,000 annealed squares, lines XOR to 0 at about the chance rate for the 5 free bits: **3.1% ± 0.5%**. | Outside 2.6–3.6%. |
| O3 | translation | In the 30 bit-balanced squares, every line XORs to 0 (4 ones per bit plane per line). | Any line that doesn't. |
| O4 | real | Even so, few lines in the bit-balanced squares are flats: **under 5%**. | 5% or more. |
| O5 | real | P4 does **not** carry over to order 8. There are non-affine 8×8 magic squares whose rows are all parallel flats and whose columns are all parallel flats. Reason: only 1,344 of the 40,320 ways to shuffle 8 things are affine (AGL(3,2) vs S8), unlike at order 4 where all 24 are. Method: shuffle the rows and columns of an affine square at random and keep the shuffles that leave both diagonals at 252. | No such square in 2 × 10⁵ shuffles. That would weaken the prediction, not kill it. |

*Amendment before running:* the magic sum was first written as 260, which is the sum for 1–64. On 0–63 it is 252. Every
prediction is unchanged (252 is also even). "Line" means all 18: rows, columns and both diagonals.

---
# Scores (filled in after running; predictions above are unchanged)

| id | kind | result | outcome |
|---|---|---|---|
| A1–A4 | translation | all four hold on all 880 squares | **held** |
| A5 | real | 528 squares have both diagonals logical, 352 have neither. That cuts across region, Dudeney group, degree and affine | **lost** |
| A6 | real | the diagonal pair is a check in the same 528 and a logical in the other 352. Also cuts across all four | **lost** |
| A7 | real | parallel rows and columns ⟺ affine, exactly (432 = 432) | **lost** |
| A8 | real | at most 4 of 6 interactions are balanced in all 8 lines; 144 squares reach it, all affine | **held** |
| B1–B3 | validation | Mermin: clash using all 6 lines. Fano: consistent. 15 copies: clash, 5-copy certificate | **held** |
| C1 | real | at most 9 factors are balanced at once; 432 squares reach it, all affine | **held** |
| C2 | real | 8 factors with lime × RHA balanced and clear of main effects | **held** |
| O1 | translation | bit 0 is 0 on all 36,540 lines | **held** |
| O2 | real | 7.23% of annealed lines XOR to 0, not 3.1% | **lost** |
| O3 | translation | rows and columns 480/480; diagonals 1/60 | **lost** (scope error, see below) |
| O4 | real | 0.37% of bit-balanced lines are flats | **held** |
| O5 | real | 1,253 non-affine squares with parallel flat rows and columns, out of 1,342 diagonal-preserving shuffles | **held** |

**Tally.** Translation checks: 5 of 6 held. Validations: 3 of 3. Real predictions: 5 of 9 held. The ones that held
had a derivation behind them (C1, C2, O5) or were near-derivations (A8, O4). The ones lost were guesses (A5–A7)
or a bad chance model (O2).

**What the losses taught (post hoc, asserted in the scripts; not evidence until retested on fresh data):**
- **A5/A6:** the diagonal split lines up exactly with the **carry corner** (000 vs the rest), which I didn't list.
  In Fitting's 528 the two diagonals are parallel planes, so together they form a check. In the other 352 the
  diagonal pair is a weight-8 logical, and its class (12 occur) determines the carry corner. All 48 trefoils
  sit in one class, (1,1,1,0,0,0).
- **A7:** parallel rows and parallel columns force affine at order 4. Every shuffle of 4 things is affine
  (AGL(2,2) = S4, both of order 24). At order 8 only 1,344 of 40,320 shuffles are, and O5 found 1,253
  non-affine examples. This is a **candidate mechanism** for "a law at 4×4, a family at 8×8". It is shown for
  this one property, not for the fold.
- **O2:** the sum constraint pulls the low bits' parities toward 0, so the right null model is "random
  8-sets with sum 252". That gives 7.25% ± 0.17%, and the annealed squares (7.23%) match it. In XOR terms the
  annealed squares are random.
- **O3:** the samples are bit-balanced in rows and columns only. The derivation holds on those 16 lines; my
  registered "all 18" was wrong.

---
## Round 3: does "every shuffle of 4 is affine" explain the fold? (written before `fold_mechanism.py` ran)
The fold proof (`../FOLD_PROOF.md`) has two steps that only work at size 4:
- **Step 1:** every balanced row of 4 cells is a single Walsh pattern, so every 4-cell balanced row is
  affine. This is the "every shuffle of 4 is affine" coincidence.
- **Step 3:** the two diagonals of a 4×4 grid together form exactly one Walsh pattern, χ₁₁(i)·χ₁₁(j).

Hypothesis: Step 1 is necessary but not sufficient, and Step 3 is a second, independent coincidence. To test
it, restore Step 1 by hand at order 8 and see whether the fold comes back.

In this language a bit plane is **bi-affine** when it is affine along every row and every column:
f(i,j) = iᵀQj + u·i + w·j + c, where i and j are the row and column bits and Q is a matrix over F2.

| id | kind | prediction | kill condition |
|---|---|---|---|
| R1 | translation | Every bit plane of every 4×4 magic square is bi-affine (Nimm0 + Step 1). | Any plane that isn't. |
| R2 | translation | A position shift (r, c) folds a 4×4 square ⟺ Q_k·c = 0 and Q_kᵀ·r = 0 for all 4 planes. Checked against direct folds, 880 × 15. | Any mismatch. |
| R3 | translation | Order 4: the diagonals' indicator = (1 + χ₁₁(i)χ₁₁(j))/2. Order 8: the diagonals' indicator is not (1 ± χ)/2 for any Walsh pattern χ. | Either fails. |
| R4 | real | Bi-affine 8×8 magic squares (Step 1 restored, built by bilinear shears) mostly have **no** left–right or top–bottom mirror fold: more than half lack one. | Every one has a mirror fold, which would mean Step 1 alone carries the law. |
| R5 | real | Most of them have **no fold of any kind** (none of the 63 position shifts): more than half. | Every one folds somehow. |

The real uncertainty: building a bijection by shears needs I + M(i) to be invertible for every i. That
constraint might force the M's to share a kernel, which would make folds common and sink R4/R5.

### Round 3 scores
| id | result | outcome |
|---|---|---|
| R1 | every plane of all 880 squares is bi-affine | **held** |
| R2 | the Q-kernel criterion matches every fold (880 × 15; it also matches every order-8 fold) | **held** |
| R3 | order 4: the diagonals are one Walsh pattern; order 8: they are not | **held** |
| R4 | 267 of 600 (44.5%) bi-affine 8×8 magic squares have a mirror fold | **held** (under half, narrowly) |
| R5 | 68 of 600 (11.3%) have no fold at all | **lost** (predicted over half) |

*Method change before scoring R4/R5:* the first sampler drew shear matrices at random and found 1 square in
400,000 draws, too few to score. I replaced it with an exact list of all 109,823 valid shear structures,
sampled uniformly, one magic square per structure. The predictions were not changed.

**Verdict on the hypothesis.** "Every shuffle of 4 is affine" (Step 1) is **necessary but not sufficient**.
Restore it by hand at order 8 and 68 bi-affine magic squares still have no fold of any kind, and 333 of
600 have no mirror fold. The diagonal coincidence (Step 3) also fails at order 8. So the order-4 law rests
on at least two separate size-4 coincidences.

**Post hoc (needs a fresh test):** the magic condition strongly selects folded shears. Over all 109,823
structures, 10.5% have a mirror fold and 36.4% have no fold. Over the 600 that carry a magic square, it's
44.5% and 11.3%. The diagonals pull toward folding at order 8 but don't force it.

---
## Round 5: does the magic condition pull toward folding? (written before `fold_pull.py` ran)
Round 3's post hoc finding: shear structures that carry a magic square fold far more often than shear
structures in general (no fold: 11% vs 36%; mirror fold: 44.5% vs 10.5%). This round tests it on a family
those numbers never touched.

**Fresh family: two-sided shears.** Ψ(i,j) = ((I + N(j))·i, (I + M(i))·j), with M and N each drawn from the
109,823 valid shear triples, kept only when Ψ is a bijection. A pilot draw (used only to check the family is
non-empty, before any fold or magic count) gave 85 bijections in 20,000 draws, all with neither rows nor
columns parallel. That makes it a different family from Round 3's one-sided shears, which always have
parallel rows or parallel columns.

**A confound to remove.** A structure can only carry a magic square if it can carry one balanced in every row
and column (semi-magic). If folding just tracks that ability, the "pull" would be about balance, not the
diagonals. So the comparison is made **among semi-magic-capable structures only**: those that also carry
a magic square vs those that don't, under the same search (40 random output maps × 64 constants per structure).

| id | kind | prediction | kill condition |
|---|---|---|---|
| T1 | translation | Every bijective two-sided shear has bi-affine planes, and its folds are exactly the shifts (r, c) with M(r) = 0, N(c) = 0, N_k·r = 0 and M_k·c = 0 for all k. | Any mismatch. |
| F1 | real | Among semi-magic-capable two-sided shears, the magic-carrying ones have a **smaller no-fold share**, with Fisher's exact test p < 0.01. | The share isn't smaller, or p ≥ 0.01. |
| F2 | real | They also have a **larger mirror-fold share** (left–right or top–bottom), p < 0.01. | The share isn't larger, or p ≥ 0.01. If no structure has a mirror fold at all, F2 is uninformative, not lost. |
| F3 | real | Re-run Round 3's shears with the same semi-magic baseline, and the pull **survives**: same direction, p < 0.01, for both shares. | It vanishes. Then Round 3's finding was the balance confound. |

### Round 5 scores
| id | result | outcome |
|---|---|---|
| T1 | bi-affine planes and the fold criterion hold for all 2,500 two-sided shears, none with parallel rows or columns | **held** |
| F1 | no fold: 12.9% of magic-carrying vs 20.4% of semi-magic-only (p = 0.015) | **lost** (right direction, missed p < 0.01) |
| F2 | mirror fold: 47.8% vs 9.8% (p = 6 × 10⁻³⁴) | **held** |
| F3 | Round 3's family with the new baseline: no fold 11.4% vs 36.9% (p = 4 × 10⁻¹⁴); mirror 44.3% vs 8.5% (p = 9 × 10⁻³⁵) | **held** |

**Verdict.** The pull replicates on fresh data, and it's specifically a pull toward **mirror** folds: about
5× in both families, at a huge significance level. The pull away from "no fold at all" is weaker and missed the
threshold in the fresh family. Round 3's result was not the balance confound: it survives the semi-magic
baseline.

**Post hoc mechanism (asserted in the script; derivable, but found after scoring):** a left–right mirror
fold with mask b makes the anti-diagonal equal to the main diagonal XOR b. Once one diagonal hits 252, the
other follows 88.8% of the time with a mirror fold, against 15.5% without (150 structures each). A mirror
fold turns magic's two diagonal conditions into roughly one. That is why magic squares cluster on mirror
folds. A reading, not a proof: at order 4 this cheap route may be the only one there's room for, which would
fit the fold theorem.

---
## Round 6: what the fold actually needs, and whether Nimm0 can be dropped (written before `fold_needs.py` ran)
**Fresh data:** all 4×4 **semi-magic** squares on 0–15 (rows and columns sum to 30; diagonals free). This
world has never been looked at in this project. OEIS A271103 gives 68,688 up to rotation and reflection.

**The two steps of the fold proof that touch the diagonals.**
- Nimm0 (cited from Conway–Norton–Ryba and Fitting, never proved here) is where they rule out carries in
  rows and columns.
- Step 3 uses the diagonals only through their **combined** sum: the 8 diagonal cells total 60.

So if the proof is right, the fold needs only *Nimm0 + diagonal cells sum to 60*, not full magic. The real
question is the other half: what forces Nimm0?

| id | kind | prediction | kill condition |
|---|---|---|---|
| H1 | literature | Exactly 549,504 semi-magic arrangements (68,688 × 8, OEIS A271103). | Any other count. |
| H2 | translation | Exactly 7,040 of them are magic (880 × 8), all satisfy Nimm0, and all have a mirror fold. | Any mismatch. |
| H3 | translation of the proof | Every semi-magic square with Nimm0 whose 8 diagonal cells sum to 60 has a mirror fold. This is a **sharper theorem** than the published fold, if it holds. | A counterexample, which would mean the proof uses more than I think, or is wrong. |
| H4 | real | Without Nimm0 it fails: some semi-magic squares with diagonal cells summing to 60 have no mirror fold. | None exist. |
| H5 | real | Most semi-magic squares (over half) violate Nimm0, so it's the diagonals that buy it. | Half or fewer violate it. |
| H6 | real | The weaker condition (diagonal cells sum to 60) does **not** force Nimm0. | Every such square satisfies Nimm0, which would make Step 3's single number enough. |
| H7 | real (the proof route) | Nimm0 does **not** survive the "independent planes" relaxation. In it each bit plane is any 0/1 matrix with eight 1s, the planes are tied together only by the 10 line sums, and distinct values are not required. Prediction: count patterns that carry in a row or column exist. | No such pattern exists. Then Nimm0 follows from counting alone, with a short proof, and the fold theorem stands without citing anyone. |

### Round 6 scores
| id | result | outcome |
|---|---|---|
| H1 | 549,504 arrangements | **held** |
| H2 | 7,040 magic, all Nimm0, all mirror-folded, identical to `binary_magic.py`'s 880 × 8 | **held** |
| H3 | Nimm0 + diagonal cells at 60 ⇒ mirror fold: 106,368 squares, no exceptions | **held** |
| H4 | 24,832 carrying squares have diagonals at 60 and no mirror fold | **held** |
| H5 | 44.0% violate Nimm0 (420 of 954 base squares) | **lost** (predicted over half) |
| H6 | 24,832 squares with diagonals at 60 still carry | **held** |
| H7 | 26,632 of 26,673 count patterns carry; counting alone doesn't give Nimm0 | **held** |

**The sharper fold theorem (H3):** the fold needs only Nimm0 plus "the 8 diagonal cells sum to 60". That
covers 106,368 arrangements, 15× the 7,040 magic ones. *Proved given Nimm0 (the existing proof never uses
more); exhaustively confirmed.*

**Post hoc:** among squares with diagonals at 60, mirror fold ⟺ Nimm0, exactly (106,368 vs 0, and 0 vs
24,832). One direction is immediate: a left–right fold makes every row {x, y, x⊕b, y⊕b}, which XORs to 0.

## Round 6b: how much coupling between bit planes forces Nimm0? (written before the hierarchy ran)
H7 showed that independent planes aren't enough. Real squares couple their planes completely: all 16 bit
combinations appear exactly once. In between:
- **pairwise:** any two planes show each of the 4 combinations 4 times. This is exactly what the fold
  proof's Step 2 (Parseval) uses.
- **triple-wise:** any three planes show each of the 8 combinations twice.

| id | kind | prediction | kill condition |
|---|---|---|---|
| H8 | real | Pairwise coupling with magic line sums still allows carries in rows or columns. | No carries. Then Nimm0 would follow from the same Walsh/Parseval machinery as the fold, and the whole theorem could be proved in one framework. |
| H9 | real | Triple-wise coupling still allows carries; only full distinctness kills them. | No carries at triple-wise. |
| H10 | translation | Full coupling gives exactly 7,040 plane systems (one per magic arrangement), none carrying. | Any other count. |

### Round 6b scores
| id | result | outcome |
|---|---|---|
| H8 | pairwise: 18,432 plane systems with magic line sums, **none** carry | **lost**, in the useful direction |
| H9 | triple-wise: 7,296 systems, none carry | **lost** |
| H10 | full: exactly 7,040, none carry | **held** |

**Result:** Nimm0 follows from pairwise-balanced bit planes plus the 10 magic line sums. This is an exhaustive
search over the relaxation, so a computer proof independent of Conway–Norton–Ryba and Fitting. It covers
18,432 plane systems, of which only 7,040 are actual squares.

## Round 6c (written before the check ran)
| id | kind | prediction | kill condition |
|---|---|---|---|
| H11 | translation of the proof | All 18,432 pairwise systems fold: there's a left–right or top–bottom mirror under which every bit plane is symmetric or antisymmetric. The fold proof uses only Nimm0 (now derived), pairwise orthogonality and the diagonal sum. | Any exception. |

### Round 6c score
| id | result | outcome |
|---|---|---|
| H11 | all 18,432 pairwise systems fold plane-wise | **held** |

## Where Rounds 6–6c leave the fold theorem
- **Fold theorem, self-contained.** Any 4×4 system of four bit planes, each with eight 1s, every pair of planes
  balanced, and all 10 lines summing to 30, has a left–right or top–bottom mirror fold. Nimm0 is now
  **derived** inside the proof (an exhaustive search over the relaxation), not cited. The statement covers
  18,432 systems, 2.6× the 7,040 real squares. *Computer-assisted proof: hand proof of Steps 2–5, exhaustion
  for Nimm0.*
- **Sharper for real squares.** Nimm0 + diagonal cells at 60 already force the fold: 106,368 semi-magic
  arrangements, 15× the magic ones.
- **What a hand proof of Nimm0 must use.** In Walsh terms (F = 15 − 2A), the two diagonals are two separate
  conditions: F̂(11,11) = 0 and F̂(01,01) + F̂(10,10) = 0 (checked on all 549,504). The fold proof's Step 3 uses
  only the first. H6 shows the first alone allows carries, so any hand proof of Nimm0 has to use the second,
  together with pairwise orthogonality (H7: without coupling, carries survive).
- **Overlap with the literature is unknown:** Conway–Norton–Ryba's proof of Nimm0 is still unread.

## Round 7: the void at 7.5 (written before `void_fold.py` ran, 2026-10-24)
**Prompt.** The atlas's "Center" region (576 squares, all singular) is the region whose fold is the complement
n -> 15 - n, i.e. the point reflection through 7.5, the value no cell holds. Question: is that why they are
singular, and does the same picture prove the other half (3-bit fold => invertible)?

**Derivation (by hand, before running).** Let H be the 4x4 Walsh matrix, columns chi_00, chi_01, chi_10, chi_11,
and J the column reversal j -> 3 - j. J fixes chi_00 and chi_11 and negates chi_01 and chi_10.
- *Complement fold, left-right:* M J = 15E - M. Apply to chi_11 (J chi_11 = chi_11, E chi_11 = 0):
  M chi_11 = -M chi_11, so **M chi_11 = 0**. The kernel is chi_11 = (1,-1,-1,1), explicitly. (Top-bottom: chi_11^T M = 0.)
  This is a one-line special case of degree_explained.py's P2; what is new is the explicit kernel.
- *3-bit fold with kept bit k:* n XOR b = (15 - 2^k + 2^(k+1) n_k) - n, a reflection through 7.5 - 2^(k-1) or
  7.5 + 2^(k-1) depending on bit k. It is the only kind of fold that misses the void. Then
  M chi_11 = 2^k B_k chi_11 = 2^(k+1) sigma, where sigma = +-chi_r* for one r* (the kept plane's rows are +-chi_11).
- *Centered at the void:* N = M - 7.5E = -(1/2) sum_m 2^m F_m with F_m = 1 - 2B_m. det M = 120 * det W'(N) / 256,
  where W' is the 3x3 Walsh block over r, c in {01, 10, 11}. Under a 3-bit fold the column-11 entries of W' vanish
  except at r*, so det M is +-2^(k+3) times a 2x2 minor built from the three flipped planes.

| id | kind | prediction | kill condition |
|---|---|---|---|
| V1 | translation | Every square with a left-right complement fold has M chi_11 = 0; every one with a top-bottom complement fold has chi_11^T M = 0. | Any exception. |
| V2 | translation | Every 3-bit fold (kept bit k) gives M chi_11 = 2^(k+1) sigma (or the transpose), sigma = +-chi_r* for a single r*. | Any exception. |
| V3 | real | The only fold masks among the 880 are 1111 and the four weight-3 masks. No weight-1 or weight-2 fold occurs. | Any other mask. |
| V4 | real | No square has both a complement fold and a 3-bit fold. | One that does. |
| V5 | real | The 2-adic valuation of det M over the 3-bit-fold squares depends only on the kept bit k. | Two squares with the same k and different valuations. |
| V6 | real (the hand-proof route) | The lowest flipped plane alone certifies invertibility: its 2x2 minor, halved, has odd determinant for every 3-bit-fold square. If this held, "3-bit fold => invertible" would have a mod-8 hand proof. | Any square where it is even. |
| V7 | translation | The atlas's counts re-derive: 528 / 64 / 64 / 64 / 56 / 56 / 0 / 48 by carry corner; 432 affine; singular <=> complement fold on all 880. | Any mismatch. |

### Round 7 scores (after running; predictions above unchanged)
| id | result | outcome |
|---|---|---|
| V1 | every left-right complement fold has M chi_11 = 0, every top-bottom one chi_11^T M = 0 (304 squares) | **held** |
| V2 | every 3-bit fold gives M chi_11 = 2^(k+1) sigma, sigma = +-chi_r* for one r* | **held** |
| V3 | weight-2 masks occur: 480 left-right/top-bottom folds have weight 2 (304 have weight 4, 624 weight 3) | **lost** |
| V4 | no square has both a complement and a 3-bit left-right/top-bottom fold | **held** |
| V5 | v2(det) takes several values for the same k (k = 0: 6, 7 and 9) | **lost** |
| V6 | the lowest flipped plane's minor has even determinant in all 240 invertible 3-bit-fold squares | **lost** (uniformly: the leading 2-adic term always cancels) |
| V7 | counts and affine total re-derive (528 / 64 / 64 / 64 / 56 / 56 / 0 / 48; 432), but "singular <=> complement fold" fails: 336 singular squares have no left-right or top-bottom complement fold | **lost as registered**: my registration narrowed "complement fold" to the two mirrors. The atlas computes it over every XOR translation of the cell address (`atlas_data.py`, last field). Scope error in the registration, not in the atlas; rechecked as V7b below. |

## Round 7b (written after the Round 7 scores, before the follow-up ran)
**Derivation (by hand).** Let a = (a_r, a_c) be any nonzero XOR translation of the cell address, with
M[i ^ a_r][j ^ a_c] = 15 - M[i][j]. Walsh characters diagonalise XOR translations, so on the 3x3 block
W[r][c] (1 + chi_r(a_r) chi_c(a_c)) = 0. W vanishes wherever chi_r(a_r) chi_c(a_c) = +1:
- a_r = 0: one whole column of W vanishes (c is the nonzero character orthogonal to a_c), kernel chi_c;
- a_r, a_c both nonzero: W vanishes at (r0, c0) and on the 2x2 block of the other two r's and c's. The two
  remaining rows are proportional, so rank W <= 2.

Either way M is singular. **A complement symmetry of any kind is a reflection through 7.5, and it forces a
kernel.**

| id | kind | prediction | kill condition |
|---|---|---|---|
| V7b | translation (re-verifies the atlas's exhaustion row) | With "complement" taken over all 15 translations: singular <=> some complement XOR symmetry, on all 880. | Any mismatch. |
| V8 | translation of the derivation | Every complement symmetry zeroes W exactly on {(r,c) : chi_r(a_r) chi_c(a_c) = +1}, and the stated kernel vector is in ker M. | Any exception. |
| V9 | real | The 480 weight-2 mirror folds all sit on singular squares (squares that also have a complement symmetry). | A weight-2 fold on an invertible square. |
| V10 | real | On every invertible square, every XOR symmetry (all translations) has a weight-3 mask. | Some other weight. |
| V11 | exploratory, not a prediction | For each invertible square, record which flipped planes (if any) certify det != 0 by the mod-2 minor test. Post hoc; a pattern found here needs a fresh test. | -- |

### Round 7b scores (after running; predictions above unchanged)
| id | result | outcome |
|---|---|---|
| V7b | singular <=> some complement XOR symmetry, on all 880 (640 singular: 304 by a mirror, 288 by a row/column swap, 48 by the half-turn, which are the 48 associative squares) | **held** |
| V8 | every complement symmetry zeroes W on its predicted set, and the stated kernel vector is in ker M | **held** |
| V9 | all 480 weight-2 mirror folds sit on singular squares | **held** |
| V10 | invertible squares also have weight-1 and weight-2 XOR symmetries under non-mirror shifts (128 each); only their *mirror* folds are all weight 3 | **lost** |
| V11 | exploratory: no single flipped plane certifies det != 0 on any of the 240 invertible squares | (not scored) |

**Why V6 and V11 had to fail (post hoc, by hand).** A flipped plane's rows are +-chi_01 or +-chi_10, in two
balanced classes. If the classes split 2/2, the two rows of each class differ by the same index d (the four
indices XOR to 0), so both minor columns are nonzero at the same two r's: identical columns mod 2. If one class
has all four rows, its entries are +-4 before halving, so even. Either way the single-plane determinant is
even. A 2-adic proof of "no complement => invertible" has to mix planes.

## Where Round 7 leaves the atlas
- **Proved, by hand:** every XOR mask b is a reflection n -> c - n about 7.5 +- 2^(q-1) +- ... over the bits q
  that b keeps; only b = 1111 reflects through 7.5 itself. A complement symmetry under *any* of the 15 shifts
  zeroes the Walsh block wherever the shift fixes the character, giving an explicit kernel (chi_11 for the
  left-right mirror). This is the direct form of `degree_explained.py`'s P2.
- **Still exhaustion:** the converse, no complement symmetry => invertible (240 squares). The single-plane
  2-adic route is closed (above).
- **Atlas corrections made (live page, version 5, 2026-10-24):** the Center row said "complement fold" under
  a definition of fold as a mirror, but only 240 of 576 center squares have a complement *mirror*; the readout
  appended "complement fold" to non-complement masks; the knot row is relabelled "By construction"; "folds by
  a half-shift" now reads "XOR symmetry under a half-shift"; the exhaustion row is split as above. New script
  `mermin_28.py` reproduces the 28-labelings and sum-30 uniqueness claims, which had no script.
- **Running record (real predictions): 21 of 39 held** (Round 7/7b: V4 and V9 held; V3, V5, V6 and V10 lost).

## Round 7: the literature gate and an independent check (Claude Code, 2026-10-24; the scores above are unchanged)
- **Independent check:** `void_fold_check.py` is a second implementation that shares no code with
  `void_fold.py` or `atlas_data.py`. It recomputes the reflection identity, the singular classes, the region rows
  of atlas version 5 and the mirror-fold weights: 22 of 22 checks pass.
- **The classes are Dudeney's types.** Each singular square has exactly one complement shift.
  - VI (304) is complement under a one-sided mirror (Staab et al.'s B_J).
  - IV and V (96 each) are complement under a one-sided swap K or L (B_K, B_L).
  - I, II and III (48 each) are complement under (K,K), (L,L) and (J,J) (A_K, A_L, A_J).
  - VII-XII (240) have none, and all are invertible. No mixed shift such as (K,L) occurs.
- **Known:**
  - singular <=> Dudeney I-VI (Trigg 1948, by computation, as reported in arXiv:1007.3239);
  - the singular direction in general (Mattingly 2000 for regular squares; Staab et al. 2010, Theorems 12-13,
    for types A and B of every even order).
  - Wikipedia's source for the associative case is Lee, Love, Narayan, Wascher & Webster, Linear Algebra
    Appl. 437 (2012) 1346-1355. Note that arXiv:1007.3239 is Staab et al., not Lee et al.
- **Not found in those papers:** one Walsh argument for all six types with explicit null vectors (Staab et al.
  give none), and the closed single-plane 2-adic route (V6, V11).
- **The converse** (no complement => invertible) is known only by computation, so the open target stands as
  "a hand proof".
- **Enumerated:** the 336 squares complemented by a swap or the half-turn (types I-V) are all affine.
- **Atlas file:** `artifact/atlas.html` is now version 5 as served, minus the publishing wrapper, and
  `artifact/atlas_template.html` was rebuilt from it. Injecting `atlas_data.json` into the template
  reproduces `atlas.html` byte for byte.
