# What is new here

This page lists the project's own contributions, each with how firmly it stands and where its proof
and its checks live.
- **New** means we did not find it in the literature we checked. That is not a claim of priority; each
  entry names the sources we read.
- **Known** results that we re-derived are listed separately, with their authors.
- Every claim has a script that re-checks it. Most were checked twice, by implementations that share no
  code.

**Strength:**
- **proved**: a written proof, checked by computation;
- **computer-assisted**: exhaustive computation, calibrated against known cases;
- **enumerated**: an exact count;
- **measured**: a statistic on fresh samples.

---

## At the research frontier

| Result | Field | Strength | Where |
|---|---|---|---|
| **Small genuine magic sets for every odd number of qubits.** A "graph star" built on an odd cycle is a critical, genuine n-qubit magic set with 3n + 1 observables. That gives 16 observables at five qubits, where the published record is 26, and the first known sets for odd n ≥ 7. This answers part of the open problem posed by Trandafir, Lisoněk and Cabello (*PRL* 2022) | quantum foundations | proved; three independent implementations | [`towers/binary_magic/magic_sets/THEOREM.md`](towers/binary_magic/magic_sets/THEOREM.md) |
| **16 is the exact minimum at five qubits** for genuine sets that hide no smaller contradiction among their contexts. Four lemmas reduce the search to three cases, and all three are empty | quantum foundations | computer-assisted | [`…/magic_sets/LOWER_BOUND.md`](towers/binary_magic/magic_sets/LOWER_BOUND.md) |
| **A closed form for the determinant of MATLAB's odd magic squares,** (−1)^((n−1)/2) · n^(n−1) · (n²+1)/2 · ∏ (n^\|O\| − (−1)^\|O\|), over the doubling orbits O mod n. So these squares are never singular, and n^(n−1) divides the determinant, which Robert Israel had observed on OEIS A160523. Written up as a short note, with proposed OEIS lines ([`void_lens/paper/`](towers/binary_magic/void_lens/paper/README.md)) | linear algebra · number theory | proved; exact for every odd n to 101, checked twice | [`towers/binary_magic/void_lens/`](towers/binary_magic/void_lens/README.md) |
| **Every pandiagonal 5×5 magic square is invertible** (all 28,800). It follows from a prime-order theorem: a square built from two cyclic Latin squares of prime order is never singular, whatever relabelling its digits get. The prime matters, since singular ones exist at order 9 | combinatorics · algebraic number theory | proved; exhaustive at order 5 (3,686,400 matrices) | [`towers/binary_magic/void_lens/`](towers/binary_magic/void_lens/README.md) |

## Smaller results

| Result | Field | Strength | Where |
|---|---|---|---|
| **Every 4×4 magic square folds.** A left–right or top–bottom mirror turns every value n into n XOR b, for one mask b | combinatorics | proved, given Nimm0 | [`towers/binary_magic/FOLD_PROOF.md`](towers/binary_magic/FOLD_PROOF.md) |
| **Pairwise balance of the bit planes, plus the 10 line sums, already forces Nimm0 and the fold.** This is weaker input than full distinctness. It extends to 106,368 semi-magic arrangements | combinatorics | computer-assisted | [`towers/binary_magic/code_lens/`](towers/binary_magic/code_lens/README.md) |
| **The void index.** A complement symmetry by row and column involutions forces nullity ≥ \|(f_P + f_Q)/2 − 1\|, where f counts fixed lines. It contains Staab et al.'s two theorems as special cases, and at order 4 it is exact: it explains why Dudeney's two 8-square groups stay invertible | linear algebra | proved; checked on all 880 | [`towers/binary_magic/void_lens/`](towers/binary_magic/void_lens/README.md) |
| **One Walsh argument for all six singular types of 4×4 magic square,** with explicit null vectors. No single bit plane can certify invertibility | linear algebra · Boolean functions | proved | [`towers/binary_magic/code_lens/PREREG.md`](towers/binary_magic/code_lens/PREREG.md) |
| **Takemura degree 3 ⟺ invertible,** because APD₃ = 24·det/s for any matrix with constant row sum s | linear algebra | proved (elementary) | [`towers/binary_magic/degree_explained.py`](towers/binary_magic/degree_explained.py) |
| **Counts:** 432 affine 4×4 magic squares, which are 9 of Fitting's 11 quadruples; 12,631,127,040 affine fully binary 8×8 squares; fully binary 8×8 squares with no XOR symmetry at all | combinatorics | enumerated | [`towers/binary_magic/`](towers/binary_magic/README.md) |
| **The magic Mermin square.** `11 13 6 / 5 10 15 / 14 7 9` is the only 3×3 magic square (sum 30) whose rows and columns all XOR to zero. It is a Mermin–Peres square under exactly one of the 28 ways of labelling two qubits | combinatorics · quantum foundations | enumerated | [`towers/binary_magic/mermin_28.py`](towers/binary_magic/mermin_28.py) |
| **The published magic sets hide smaller contradictions.** By the paper's own tables, 16 of 18 do. In MS5-26, all 3,051 minimal hidden ones fit on at most 4 qubits | quantum foundations | proved; exhaustive on its printed data | [`…/magic_sets/LOWER_BOUND.md`](towers/binary_magic/magic_sets/LOWER_BOUND.md) |
| **Every Steiner triple system obeys the same 382 short laws.** Of the 4,694 laws with at most four operations in the Equational Theories Project's catalog, every Steiner quasigroup with at least 3 elements obeys exactly the same 382, the Fano plane among them. The shortest law that tells two Steiner systems apart is distributivity, with five operations | universal algebra · design theory | proved; the counts checked twice | [`towers/laws_of_a_table/STEINER_SYSTEMS.md`](towers/laws_of_a_table/STEINER_SYSTEMS.md) |
| **Eight closures of 14 laws all have finite type specimens.** An archived paper called six of them "fossils". Explicit specimens exist, and the smallest have 3, 3, 5, 5, 6 and 6 elements; the last two closures need between 7 and 32 | universal algebra | computer-assisted; one closure rests on the ETP's Lean proofs | [`towers/laws_of_a_table/EIGHT_SPECIMENS.md`](towers/laws_of_a_table/EIGHT_SPECIMENS.md) |
| **Where order-5 kernels come from.** Among singular 5×5 magic squares, 71% have a complementary pair of lines, 5% an off-centre pair, and 25% no structural cause. Those last occur 3× as often as chance predicts | combinatorics | measured (fresh samples of 40,000–65,000) | [`towers/kernel_ledger/`](towers/kernel_ledger/README.md) |

## For teaching: the frame itself

| Contribution | Where |
|---|---|
| **The base.** One rule, the most symmetric arrangement, realizes every integer from 0 to 9 as a unique shape. At 5, 7 and 9 it splits into a flat face and a solid face, and orbit parity forces the centre | [`base/`](base/README.md) |
| **The coin.** The author's three coins are the three half-turns of the number sphere about one octahedron's axes, and the edge of the third is *i*. Every involution is read as two sides and an edge | [`coin/THE_COIN.md`](coin/THE_COIN.md) |
| **Four kinds of paradox** (the author with Ben Mayes, April 2026), read through the coin. The Liar, Russell and Cantor are one diagonal | [`coin/PARADOX_TYPES.md`](coin/PARADOX_TYPES.md) |
| **The towers.** Nine climbs of established mathematics, each starting on the base, each with its coin | [`towers/THE_TOWERS.md`](towers/THE_TOWERS.md) |
| **A Ledger of Nothing.** One way to ask where any zero comes from (paid for by a count, or bought by a coincidence), run across six fields | [essay](towers/kernel_ledger/A_LEDGER_OF_NOTHING.md) |
| **The books.** *The Shape of Understanding* and *Two Sides and an Edge*, with every picture checked against its proof | [book repository](https://github.com/TiredofSleep/shape-of-understanding) |

## Read again: the J series (2026-10-25)

The archived J series was read again by three independent audits, with fresh code for every claim. No
paper carried a new result as written. Correcting them gave nine pages for the towers and the coin, each
checked by its own script: seven of classical mathematics, and the two small new results above.

| Page | What it teaches | From |
|---|---|---|
| [The balance point](towers/THE_BALANCE_POINT.md) | Walk a polygon and average where you have been. The average stands on the centre exactly at whole laps, and its squared distance is Fejér's kernel | J24, J26 |
| [The two faces of S₄](towers/THE_TWO_FACES_OF_S4.md) | The tetrahedron's group and the cube's rotations are one group acting two ways, and the central inversion turns one into the other | J43 |
| [The spinor floor](towers/THE_SPINOR_FLOOR.md) | Cl(2n) is every operator on 2ⁿ spinors. Pascal's row 2n grades the algebra and row n the spinors, and at n = 3 the half-spinors are the cube's two tetrahedra | J20 |
| [The transpose's coin](coin/THE_TRANSPOSE_COIN.md) | In a symmetric Latin square of odd order every symbol sits on the diagonal once: round-robin byes, the Lo Shu mod 3, and the easy case of Ryser's conjecture | J29 |
| [Two readings of ℤ/n](coin/TWO_READINGS_OF_ZN.md) | When residues, orbits and the mirror tell ℤ/n apart, settled level by level, with a trap at n = 15 | J27, J34, J35 |
| [The laws of ℤ/n](towers/laws_of_a_table/THE_LAWS_OF_ZN.md) | x + y mod n obeys 32 short laws for every n ≥ 5, and −(x + y) mod n obeys 294 for n ≥ 7, with one exception at 6: four operations see only the moduli 1 to 4 | J05 |
| [The mirror](coin/THE_MIRROR.md) | Reading a table the other way round is a coin on the laws: 84 on its edge, 2,305 pairs on its sides | the ETP database |
| [Steiner systems](towers/laws_of_a_table/STEINER_SYSTEMS.md) | new, above | the ETP database |
| [Eight specimens](towers/laws_of_a_table/EIGHT_SPECIMENS.md) | new, above | J03, and its correction in `ck` |

More than fifty false or unsupported statements turned up in the papers, far more than the September
census caught. Each is kept with its counterexample in [`graveyard/j_series_reread/`](graveyard/j_series_reread/README.md).

## Known: re-derived here and credited, not claimed

- **Fitting (1931)**: the binary layers of the 880 squares, the carries, Nimm0, and the 528 / 192 / 112 / 48
  counts.
- **Dudeney (1917) and Trigg (1948)**: a 4×4 magic square is singular exactly when it has a complement symmetry.
- **Mattingly (2000) and Staab et al. (2010)**: complement-symmetric squares of even order are singular.
- **Manjunath and Ambikasaran (2022)**: MATLAB's doubly-even magic squares have rank 3.
- **Waegell (2013)**: the Star families of parity proofs, which are degree-2 and reduce to the square or the
  pentagram.
- **Cawagas (2004)**: 8 of the sedenions' 15 octonion-like sub-planes are octonions.
- **Qassim and Wallman (2019–2022)**: odd-prime Pauli operators give no quantum-only contextuality, so no
  two-qutrit Mermin–Peres grid exists. The direct argument here is in
  [`towers/binary_magic/qutrit_grids.py`](towers/binary_magic/qutrit_grids.py).
- **Classical theorems** (Maxwell–Calladine, Lieb, Edmonds, Chebotarev) for Levels 0–2 of the kernel ledger.
- **The J-series pages**: Fejér's kernel (1900); the two faces of S₄; spinors (Jordan and Wigner, Brauer and
  Weyl, Chevalley); the symmetric case of Ryser's conjecture; exponent sums mod n; the duality of laws. Each
  page names its sources.

Each entry's evidence is in the folder's `NOVELTY.md` or `PREREG.md`.

## What did not survive

Every retracted claim is kept, with the evidence that killed it, in [`GRAVEYARD.md`](GRAVEYARD.md). How
the work is produced and checked, and what we learned doing it, is in [`HOW_WE_WORK.md`](HOW_WE_WORK.md).
