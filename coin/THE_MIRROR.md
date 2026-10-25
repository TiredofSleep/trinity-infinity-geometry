# The mirror — reading a table the other way round

*A page of the coin, worked out on a finite catalog: the 4,694 short laws of the Equational Theories
Project (ETP), every law with at most four operations ([`../towers/laws_of_a_table/`](../towers/laws_of_a_table/README.md)).
It is the transpose of [`THE_TRANSPOSE_COIN.md`](THE_TRANSPOSE_COIN.md), seen on laws instead of on
cells. Nothing here is new about duality; the counts are computed here. Every [FORCED] claim is checked by
[`verify_mirror.py`](verify_mirror.py) (26 checks, about thirty seconds), and the counts again by
[`independent_check.py`](../towers/laws_of_a_table/independent_check.py).*

Tags: **[FORCED]** proved here or checked by the script · **[NAMED]** a cited known result ·
**[READING]** an interpretation.

---

## The flip

- The **opposite** of a table (M, ·) is the table with x ∘ y = y · x: its transpose. [NAMED]
- The **mirror** of a law reverses every product. For example, (x·y)·z = x becomes z·(y·x) = x.
- A table obeys a law exactly when its opposite obeys the mirror law. [NAMED] The ETP calls the mirror the
  "dual" law.
- Mirroring twice changes nothing, so it is a flip. [FORCED]

## Two sides and an edge

- **The edge.** 84 of the 4,694 laws are their own mirror. [FORCED]
  - By number of operations they split as 2, 3, 5, 12 and 62.
  - Examples: commutativity, x·y = y·x (#43); x·x = y·y (#40); and associativity (#4512).
- **The sides.** The other 4,610 laws form 2,305 mirror pairs. [FORCED] For example, x = x·y (#4) and
  x = y·x (#5).
- **Checked against the ETP.** The pairing agrees with the ETP's own list of duals at every point checked:
  nine of its named pairs, and eleven laws that its list leaves out as self-dual. [FORCED]
- [READING] The sides come one pair at a time. No rule picks the "heads" law in every pair, so the catalog
  does not split into two halves.

## Three levels, three edges

- **Tables.** At order 3 the transpose fixes the 729 commutative tables, and pairs the other 18,954 into
  9,477 pairs. [FORCED]
- **Profiles.** The *profile* of a table is the set of catalog laws it obeys.
  - The profile of the transpose is the mirror of the profile. [FORCED] This holds for all 16 tables of
    order 2 and all 19,683 of order 3.
  - Order 3 has 2,639 distinct profiles, and 101 of them are their own mirror. [FORCED]
- **The edge widens.** The 101 self-mirror profiles come from three sources. [FORCED]
  - 78 come from a commutative table.
  - 6 more come from a table that is isomorphic to its own transpose.
  - 17 come only from tables that are not. For example, the table [[0,0,0],[0,1,2],[2,1,2]] obeys 62 laws,
    and that set is its own mirror, yet no renaming of its elements turns it into its transpose.
- [READING] A profile forgets enough that some flipped pairs look the same. So the flip on profiles has a
  wider edge than the commutative tables alone would give.

## A worked case: the eight closures of 14 laws

- The consequences of a law's mirror are the mirrors of its consequences. [FORCED] This follows from the
  rule for the opposite table.
- The eight closures of [`EIGHT_SPECIMENS.md`](../towers/laws_of_a_table/EIGHT_SPECIMENS.md) sort onto the
  coin [FORCED]:
  - C1 (#40) and C2 (#43) lie on the edge;
  - C3 and C4, C5 and C7, and C6 and C8 are the two sides.
- Transposing a type specimen for one side gives a type specimen for the other. [FORCED]

## What is not claimed

- Nothing new about duality. The opposite table and the dual law are classical, and the ETP uses them
  throughout.
- The count of 84 self-dual laws is computed here. It follows from the ETP's published list of duals, and
  the ETP's paper does not state it, in the parts read for this page.
- Only laws with at most four operations.

## Sources

- The Equational Theories Project, "The Equational Theories Project: advancing collaborative mathematical
  research at scale", arXiv:2512.07087 (2025), §2 (duality).
- The ETP repository, [github.com/teorth/equational_theories](https://github.com/teorth/equational_theories):
  `data/dual_equations.md` and `data/duals.json`.
- OEIS A376640: the catalog's laws by number of operations, 2, 5, 39, 364 and 4284, which sum to 4,694.
