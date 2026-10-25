# The transpose's coin — byes in a round robin, and the Lo Shu mod 3

*A page of the coin. The transpose is a flip of a square table, and oddness puts every symbol on its
edge, by the same parity that puts 5, 7 and 9 on their centres. Everything here is classical. It comes
from the archived
[J29](https://github.com/TiredofSleep/trinity-infinity-geometry/tree/archive-2026-09-24/05_papers/algebra/J29)
("The Lo Shu D4 orbit modulo 3"), whose "diagonal lemma" is the order-3 case of the theorem below.
Every [FORCED] claim is checked by [`verify_transpose_coin.py`](verify_transpose_coin.py) (20 checks,
about eight seconds).*

Tags: **[FORCED]** proved here and checked by the script · **[NAMED]** a classical result, cited.

---

## 1. The coin

A **flip** pairs things up and leaves its **edge**, the fixed things, alone. So the number of things and
the number on the edge always have the same parity. [FORCED: the moved things come in pairs; checked for
every involution of an *n*-set, *n* = 1 … 8]

## 2. The theorem: oddness puts every symbol on the edge

The **transpose** is a flip of a square table: it swaps cell (*i*, *j*) with cell (*j*, *i*), and its edge
is the main diagonal. A table equal to its own transpose is **symmetric**; as a multiplication table,
that means *commutative*.

**Theorem** [FORCED; NAMED]. In a symmetric Latin square of odd order *n*, each symbol appears on the main
diagonal exactly once. In other words, the diagonal is a *transversal*.

*Proof.* A symbol *s* fills *n* cells, one in each row. The transpose keeps the set of *s*-cells, because
the square is symmetric, and off the diagonal those cells come in pairs. So the number of *s*-cells on the
diagonal has the parity of *n*, which is odd, so it is at least 1. There are *n* symbols and only *n*
diagonal cells, so each symbol appears there exactly once. ∎

- [FORCED] The theorem holds in every case tested: all 6 symmetric Latin squares of order 3 and all 720
  of order 5; 200 of orders 7 and 9 found by randomized search; 900 relabellings of the cyclic squares
  *a*(*x* + *y*) of orders 7, 9 and 11; and the Steiner quasigroup of the Fano plane.
- [FORCED] **Even order breaks it.** The Klein four-group's table has diagonal 0, 0, 0, 0, and the table
  of ℤ/4 has diagonal 0, 2, 0, 2.
- [FORCED] **The converse is false from order 5 on.** *x* + 2*y* (mod 5) has the transversal diagonal
  0, 3, 1, 4, 2 but is not symmetric. At order 3 alone, a Latin square is symmetric exactly when its
  diagonal is a transversal (all 12 checked).
- [NAMED] **The easy case of a famous open problem.** Ryser's conjecture (1967) says that every Latin
  square of odd order has a transversal. Best and Wanless, who translated Ryser's paper, note that the
  symmetric case is easy; this section is that proof. The general conjecture is still open. Montgomery
  (2023) proved that for large *n* every Latin square has a transversal of *n* − 1 cells.

## 3. Where you meet it: the bye in a round robin

Take an odd number *n* of teams. Each pair plays once, and in each round one team sits out. In row *i*,
column *j*, write the round in which *i* plays *j*; on the diagonal, write the round in which *i* sits
out. The result is a symmetric Latin square, and every symmetric Latin square of odd order is a schedule
like this. The theorem says that **every round has exactly one bye**. [NAMED: the classical link between
round robins, symmetric Latin squares and one-factorizations of the complete graph *K*ₙ₊₁; survey:
Mendelsohn and Rosa 1985]

Add one more team, which plays whoever has the bye. Each round becomes a perfect matching of *K*ₙ₊₁.
[FORCED] At order 5 with diagonal 0, 1, 2, 3, 4 there are exactly 6 such squares. They match the 6
one-factorizations of *K*₆ (OEIS A000438).

## 4. The Lo Shu mod 3

        2 7 6        mod 3       2 1 0
        9 5 1        ----->      0 2 1        = x − y + 2   (mod 3; x the row, y the column, from 0)
        4 3 8                    1 0 2

- [FORCED] The Lo Shu has 8 orientations: 4 turns, each with or without a flip. Reduced mod 3 they give
  exactly **4 tables**, each from two orientations: *x* − *y* + 2, which is the Lo Shu itself;
  *y* − *x* + 2, its transpose; *x* + *y*; and 1 − *x* − *y*. All four are Latin squares.
- [NAMED; FORCED] **Why Latin.** Subtract 1 and write the entries in base 3. The two digits form two
  orthogonal Latin squares (de La Hire 1705; Euler 1782; this is the book's §13.1), and the Lo Shu mod 3
  is 1 plus the low digit.
- [FORCED, by the theorem] **Why half of them cannot be commutative.** Four orientations keep the Lo Shu's
  main diagonal 2, 5, 8, which is 2, 2, 2 mod 3. A symbol repeated on the edge is exactly what an odd
  symmetric Latin square forbids, so none of those four tables is commutative.
- [FORCED] **The quarter turn.** A quarter turn moves the anti-diagonal 6, 5, 4 onto the diagonal, and mod
  3 that is 0, 2, 1, a transversal. All four of these tables are commutative: *x* + *y* and 1 − *x* − *y*.
  The quarter-turned Lo Shu, mod 3, is a three-team round robin, with one game and one bye in each round.
- [FORCED] The two non-commutative tables are each other's transposes.

## What this is, and is not

- **Is:** a classical theorem with a three-line proof, the same parity rule that already forces the
  centres of 5, 7 and 9 in [`THE_COIN.md`](THE_COIN.md). It comes with an everyday use (the bye), an open
  conjecture next door (Ryser), and the Lo Shu as a worked example.
- **Is not:** new. The theorem, the round-robin link and de La Hire's decomposition are all classical.
  What serves teaching is the arrangement as a coin.
- **The same flip on laws:** transposing a table mirrors every law it obeys. See
  [`THE_MIRROR.md`](THE_MIRROR.md).
- **Left behind from J29**, each checked
  ([`../graveyard/j_series_reread/`](../graveyard/j_series_reread/README.md)):
  - The "cumulant witness" κ = Tr(*M*²) − Tr(*M*)² = ±48. It is −2 times the sum of the principal 2 × 2
    minors, a coefficient of the characteristic polynomial. It separates the two halves of the orbit only
    because the halves are different matrices, and any diagonal statistic separates them as well: the sum
    of the squared diagonal is 93 against 77.
  - The Lo Shu's eigenvalues, 15 and ±2√6, which become 15 and ±2√6 *i* after a quarter turn. They are
    known (Loly, Cameron, Trump and Schindel 2009).
  - "Mod 3 is special": the Lo Shu is just as mixed mod 6, a modulus the paper did not try.
  - The random-matrix rates, which are not defined for matrices that are not magic.
  - The equational-theory counts (179, 60, 179 and 313 laws). They are correct, and the two commutative
    tables share exactly the 14 laws that follow from commutativity alone, which is true and tells nothing.

## Sources

- H. J. Ryser, "Neuere Probleme der Kombinatorik", *Vorträge über Kombinatorik*, Oberwolfach (1967)
  69–91: the conjecture.
- D. Best and I. M. Wanless, "What did Ryser conjecture?", arXiv:1801.02893 (2018): the translation, with
  the remark on the symmetric case.
- R. Montgomery, "A proof of the Ryser–Brualdi–Stein conjecture for large even *n*", arXiv:2310.19779
  (2023).
- E. Mendelsohn and A. Rosa, "One-factorizations of the complete graph — a survey", *J. Graph Theory*
  **9** (1985) 43–65.
- OEIS A000438, the number of one-factorizations of *K*₂ₙ: 1, 1, 6, 6240, …
- P. de La Hire (1705) and L. Euler (1782), magic squares from orthogonal Latin squares; see F. J. Swetz,
  *Legacy of the Luoshu*, 2nd ed., A K Peters (2008).
- P. D. Loly, I. Cameron, W. Trump and D. Schindel, "Magic square spectra", *Linear Algebra Appl.* **430**
  (2009) 2659–2680.
