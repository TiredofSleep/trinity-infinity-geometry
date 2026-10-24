# Novelty check: what was already known

**First search: 2026-10-21, in the chat.** Fitting's papers and Conway–Norton–Ryba's chapter were
not read, so every "not found" was provisional.

**Second search: 2026-10-22, in Claude Code, with both of Fitting's papers read.** Much of what the
first search listed as probably new is in Fitting 1931. The tables below say where. Every Fitting
statement used here is checked on all 880 squares by [`fitting_crosscheck.py`](fitting_crosscheck.py).

## Fitting 1931 and 1933: read

- F. Fitting, "Rein mathematische Behandlung des Problems der magischen Quadrate von 16 und von 64
  Feldern", *Jahresbericht der Deutschen Mathematiker-Vereinigung* 40 (1931), 177–199.
- F. Fitting, "Die Komponenten magischer Quadrate und ihre Verwendung zur Konstruktion solcher
  Quadrate", *Jahresbericht der DMV* 42 (1933), 254–265.

Both are free to read, as scans with OCR text, at the Göttingen digital library (GDZ), volumes
`PPN37721857X_0040` and `PPN37721857X_0042`. Fitting credits the key idea, splitting a square into its
binary "components", to his son, then a student in Göttingen: Hans Fitting, the algebraist of the
Fitting subgroup and Fitting's lemma. The 1933 paper again credits most of its ideas to "Dr. H. Fitting".

| result here | where Fitting has it |
|---|---|
| Split a square into four 0/1 layers (bit planes); the 528 squares whose four layers are all magic | 1931, Part 1 §I. There are 16 magic "forms", 8 up to swapping 0 and 1. Two forms fit together when every combination of digits appears equally often (Satz 2a–2c), which is our orthogonality of planes. They make 11 quadruples, giving 11 · 4! · 2⁴ / 8 = 528 |
| Nimm0: every layer has two 1s in every row and column | 1931 §III: no "irregular" component exists. It is proved by a case analysis on a + 2b + 4c + 8d = 30 |
| The diagonals cancel layer by layer; four 1s on the corners and centre | 1931 Satz 3 and its Folgerung (p. 182). Each layer has two 1s on each of four sets of four cells: the corners, the centre, and the two sets of edge middles. A layer with a 1s on one diagonal has 4 − a on the other. This is stronger than our statement; [`FOLD_PROOF.md`](FOLD_PROOF.md) step 3 is a new proof of it |
| The carry formalism: carries of size 1, a contiguous chain, all of one sign; "1s→2s with 4s→8s" alone is impossible | 1931 §II. A-, B- and C-forms have 2, 3 or 4 ones on a diagonal. Satz 4: a non-magic layer forces a C-form. Satz 5: at most one C-form. His diagonal equations 2a = b, 2a = b − c and 2a = b − c − d are the carry equations, and he notes that "2a = b + c" has no solution in 1, 2, 4, 8. In carry language, each carry adds one B-form, and the one C-form sits at the bottom of the chain. Satz 5 is the empty corner |
| 528 / 192 / 112 / 48 by the number of carries | 1931 §I and §II a–c (0, 1, 2 or 3 B-forms) |
| The 48 "whole-only" squares | 1931 §II c: three B-forms and a C-form, with no magic layer |
| Generating all 880 | 1931 pp. 188–189, the "Primterme" (prime terms; his son's idea). All 880 come from 14 types under four operations: permute the prime terms; swap 0 and 1 inside a prime term (an XOR mask on its bits); exchange B-forms; and three cell transformations. 1933 Satz 1–2 generalize these to any order |
| 8×8 squares | 1931 Part 2, from magic components only. Satz I: n components fit when every n-digit binary number appears equally often. Satz II builds a new component from two halves, one the inverse of the other. One family has 11 · 1296² · 6! · 2⁶ / 8 = 106,420,469,760 squares up to rotation and reflection, and pandiagonal families follow (130,026,464,870,400 by one construction), with a general method for (4m)² |

## Other prior work (cite)

| result here | prior work |
|---|---|
| All 880 squares | Frénicle 1693; completeness proved by Fitting 1931; Bondi & Ollerenshaw 1982 analytically |
| Nimm0, restated | Conway, Norton & Ryba 2017. The chapter remarks that any proof must use the diagonals |
| 12 complement-pair patterns | Dudeney 1910/1917; proved complete by Bondi & Ollerenshaw 1982 |
| 640 singular, 240 invertible | MathPages, "The Determinants of 4x4 Magic Squares" (5,120 and 1,920 of 7,040) |
| The singular ones are exactly Dudeney's types I–VI | Trigg, "Determinants of fourth-order magic squares", *Amer. Math. Monthly* (1948): he worked out the determinant of every order-4 square, and types I–VI are 0 (as reported by Staab et al.; Trigg's paper itself is not read) |
| Complement-symmetric squares of even order are singular | Mattingly, "Even order regular magic squares are singular", *Amer. Math. Monthly* (2000), for the regular (associative) case. Staab, Fisher, Maggio, Andrade, Farrell & Schilling, arXiv:1007.3239 (2010), Theorems 12–13, for their types A (M + PMP = cE) and B (M + PM = cE) in every even order. Lee, Love, Narayan, Wascher & Webster, *Linear Algebra Appl.* 437 (2012) 1346–1355, is the source Wikipedia cites for the associative case |
| Degree classes 240 / 624 / 16 | Takemura, arXiv:2601.06131 (January 2026). His abstract says the classes refine the complement-pair ("link-line") types, so the Dudeney-to-degree correspondence is his observation. The companion paper, arXiv:2512.18169, gives closed forms for the first degree; neither abstract mentions determinants |
| The even/odd colouring of all 880 (the 1s layer only) | Fahimi, "Binary color-coded magic squares", *Discrete Mathematics* 347 (2024) 113708 |
| 10 two-qubit Mermin–Peres grids; the KCBS pentagram | standard quantum foundations |
| No quantum-only contextuality from odd-prime Pauli operators | Qassim & Wallman, arXiv:1911.11171; arXiv:2209.14018 |
| 1,105,920 bent-diagonal Franklin squares, 368,640 of them pandiagonal | Schindel, Rempel & Loly 2006 |

## What survives as probably new

All provisional until Conway–Norton–Ryba is read; most are small.
- **The fold theorem.** Every square has a left–right or top–bottom mirror with A(mirror x) = A(x) XOR b.
  It has a hand proof given Nimm0. Fitting has XOR operations that carry one square to another, not
  symmetries of a single square.
- **Degree 3 ⟺ invertible**, via APD₃ = 24·det(A)/s for any matrix with constant row sum s ≠ 0.
  Also **complement parity sets the degree's parity**, and the Walsh-pairing mechanism for degree ∞.
  All are elementary.
- **432 affine squares.** Six of Fitting's eight magic forms are affine, and the affine squares are
  exactly 9 of his 11 quadruples. A small refinement.
- **12,631,127,040 affine fully binary 8×8 squares.** Not among Fitting's counts, which are of other
  families.
- **Order 8.**
  - A fully binary 8×8 square exists with no XOR symmetry.
  - Every member of Fitting's family has half-shift symmetries (checked on 2,000 random members) and
    is almost never affine.
- **The magic Mermin square, sharpened.** `11 13 6 / 5 10 15 / 14 7 9` is the only 3×3 magic square
  (sum 30) whose rows and columns all XOR to 0. It is a Mermin–Peres square under exactly one of the
  28 qubit labellings.
- **No 3×3 two-qutrit grid.** Elementary, and consistent with the odd-prime results above.
- **The carry cube and its trefoil drawing.** A picture of Fitting's chain of B-forms, and an
  encoding.

## Downgraded on 2026-10-22, now known

- **The carry formalism and the forced-empty corner.** Fitting 1931 §II, Satz 4–5. The carry cube is
  a new way to draw it.
- **Diagonal cancellation layer by layer.** Fitting 1931, Satz 3. The Walsh proof here is new.

## Added 2026-10-24: the code lens and magic sets

Rescoped against Fitting, after reading his §III.
- **Pairwise-balanced bit planes plus the 10 line sums force Nimm0, and the fold** (`code_lens/`, 18,432
  plane systems; computer-assisted). Fitting's §III proves Nimm0 by hand for actual squares. His argument
  uses the numbers 0–15 themselves: the sets of odd numbers, of numbers with a 2 and with a 4, their sums,
  then explicit diagonal sets. So it depends on full distinctness.
  - The pairwise relaxation is **stronger than Fitting's statement**: probably new, pending Conway–Norton–Ryba.
  - A hand proof of the pairwise version is open.
- **Nimm0 plus diagonal cells summing to 60 forces a mirror fold, for semi-magic arrangements** (106,368).
  Fitting treats only magic squares and never states a fold. This is **not his**, so it is probably new,
  pending Conway–Norton–Ryba.
- **Parallel rows and columns ⟺ affine at order 4**, because every shuffle of 4 is affine (AGL(2,2) = S4).
  This is elementary, and probably known.
- **The magic pull toward mirror folds at order 8** is scoped to bi-affine shear families (replicated).
- **Graph-star magic sets** (`magic_sets/`): critical, genuine n-qubit sets with 3n + 1 observables for odd n.
  - The ring context is Waegell's (2014).
  - The completion, and the proofs of genuineness and criticality, were not found in the papers checked.
  - Semantic Scholar lists 14 papers citing Trandafir–Lisoněk–Cabello 2022 (October 2026). All were checked
    at abstract level, and none states the construction.
  - Not yet read in full: Zhao et al., arXiv:2512.16654 (stabilizer-testing games for GHZ and cyclic
    cluster states; the first 100,000 characters show no such construction), and the all-versus-nothing
    proofs for graph states that it cites.
  - **Waegell's thesis, arXiv:1307.6264, read from the PDF (Chapter 6, Tables 26–27):** its Star families put
    every observable in exactly two IDs. They therefore reduce to the square or the pentagram, and each with
    N ≥ 4 fits on fewer than N qubits (`magic_sets/waegell_stars.py`, `waegell_realize.py`). The odd-N Star has
    the same counts as the C_n graph star (3N + 1, N + 2) but a different hypergraph, and it is not genuine.
    This is not the construction here.
  - **The published "smallest" sets are not context-minimal** (16 of 18 hide a smaller clash, by Lemmas 1–2);
    the C_5 graph star is minimal in both senses. So "16 against 26" holds inside the paper's own class, and
    the lower bound covers context-minimal sets only.
- **Sedenions:** 8 of the 15 octonion-like sub-planes are octonions under the sedenions' own signs. That is
  Cawagas's (2004; Cawagas et al., arXiv:0907.2047). The maximum over all sign choices (8, in 135 ways) and
  the 5-plane minimal clash (`../planes_and_mirrors/why_seven_breaks.py`) are not checked against the literature.

## Added 2026-10-24 (Round 7): the fold through 7.5, against the literature

The chat's Round 7 (`code_lens/PREREG.md`) classified the 640 singular squares by their complement
symmetry: 304 under a mirror, 288 under a row or column swap, and 48 under the half-turn. Checked here by a
second implementation, `code_lens/void_fold_check.py` (22 checks), which also maps the classes onto the
literature.
- **These are Dudeney's types, exactly.** Each singular square has exactly one complement shift.
  - Type VI (304) is complement under a mirror on one side. That is Staab et al.'s type B_J.
  - Types IV and V (96 each) are complement under a neighbour swap or a half swap on one side: B_K and B_L.
  - Types I, II and III (48 each) are complement under the same swap on both sides: A_K, A_L and A_J. Type
    III, under the half-turn, is the regular (associative) squares.
  - Types VII–XII (240) have no complement symmetry, and all are invertible.
- **So "singular ⟺ complement symmetry" is known.** Trigg (1948) worked out every determinant. The singular
  direction is proved in general by Mattingly (2000) for regular squares and by Staab et al. (2010, Theorems
  12–13) for types A and B in every even order. The converse is known only by computation (Trigg; MathPages).
- **What Round 7 adds** (small; probably new, pending Conway–Norton–Ryba):
  - one Walsh-character argument for all six singular types at once, with explicit null vectors;
    Staab et al. give none, and their type-A proof goes through eigenvalue pairing;
  - the identity n XOR b = c − n with centre 7.5 ± 2^(q−1) per kept bit, which is elementary;
  - a closed door: no single bit plane can certify invertibility 2-adically (V6, V11, with a hand reason), so
    a hand proof of the converse has to mix planes.
- **Enumerated here:** the 336 squares complemented by a swap or the half-turn (types I–V) are all affine.
- **A correction to our own pages:** "invertible ⟺ 3-bit fold" was false. 288 singular squares have 3-bit
  mirror folds too, so only "invertible ⟹ every mirror fold flips 3 bits" holds. The atlas page (version 5,
  made live by the chat on 2026-10-24) and `ATLAS.md` now say so.

## Still to read

- **Conway, Norton & Ryba, "Frenicle's 880 Magic Squares".** In *The Mathematics of Various
  Entertaining Subjects*, vol. 2 (Princeton, 2017), pp. 71–82, DOI 10.1515/9781400889136-007.
  Paywalled. A library or interlibrary loan can supply it.
- **Trigg (1948) and Mattingly (2000)**, both in the *Monthly* (JSTOR). They are cited here through Staab et
  al., who describe what each proved.

## Sources

- Fitting 1931 and 1933: GDZ, https://gdz.sub.uni-goettingen.de/id/PPN37721857X_0040 and https://gdz.sub.uni-goettingen.de/id/PPN37721857X_0042
- Seipel, "880 magic squares of order 4 by Frenicle and Fitting" (Wolfram Community notebook): https://www.wolframcloud.com/statichtml/d7bb09e5-0989-4e0e-963e-d9071bcc33b0
- Conway, Norton & Ryba (2017), DOI 10.1515/9781400889136-007
- Futility Closet, "The Nimm0 Property": https://futilitycloset.com/2018/06/14/the-nimm0-property
- Takemura, arXiv:2601.06131 and arXiv:2512.18169
- MathPages, "The Determinants of 4x4 Magic Squares": https://mathpages.com/home/kmath310.htm
- Staab, Fisher, Maggio, Andrade, Farrell & Schilling, "The Magic of Permutation Matrices: Categorizing,
  Counting and Eigenspectra of Magic Squares", arXiv:1007.3239 (2010)
- Lee, Love, Narayan, Wascher & Webster, "On nonsingular regular magic squares of odd order", *Linear Algebra
  Appl.* 437 (2012) 1346–1355, doi:10.1016/j.laa.2012.04.004
- Fahimi, arXiv:2307.09996 (*Discrete Mathematics* 347, 2024)
- Barbero, Cerruti & Murru, "Squaring the magic squares of order 4", arXiv:1302.1163
- magictesseract.com, Order-4 Magic Squares: https://magictesseract.com/order-4_squares
- Science News, "Counting Franklin's magic squares" (2006): https://sciencenews.org/article/counting-franklins-magic-squares
- arXiv:2209.14018; Qassim & Wallman, arXiv:1911.11171
