# Every Steiner triple system looks the same to four operations

*A page of [the laws of a table](README.md), beside the Fano plane of
[`../planes_and_mirrors/`](../planes_and_mirrors/README.md). A small new observation, with a classical
method. It also corrects a verdict of the archived ETP database. Every [FORCED] claim is checked by
[`verify_steiner.py`](verify_steiner.py) (18 checks, about six seconds), and the counts again by
[`independent_check.py`](independent_check.py).*

Tags: **[FORCED]** proved here or checked by the script · **[NAMED]** a cited known result ·
**[READING]** an interpretation.

---

## The tables

A **Steiner triple system** puts every pair of points on exactly one 3-point line. Its **Steiner
quasigroup** is the table with x·x = x, where x·y, for x ≠ y, is the third point on the line through x and
y. These tables are exactly those that obey x·x = x, x·y = y·x and x·(x·y) = y. [NAMED]

- The smallest is the 3-point line, which is −(x + y) mod 3 ([`THE_LAWS_OF_ZN.md`](THE_LAWS_OF_ZN.md)).
- The Fano plane is the next. Label its 7 points by the nonzero 3-bit strings, as in `planes_and_mirrors`:
  the third point on the line through a and b is a ⊕ b. So for two different points, its table is the
  octonions' rule, e_a e_b = ±e_(a⊕b), with the sign forgotten. [FORCED — `independent_check.py`]

## The result

Every Steiner quasigroup with at least 3 elements obeys the same 382 of the catalog's 4,694 short laws.
[FORCED]
- **At least these 382.** Rewriting with the three axioms brings both sides of each of these laws to the same
  term.
- **At most these 382.**
  - Two points a ≠ b span the line {a, b, a·b}, a copy of the 3-point system.
  - A law that holds in a table holds in every part of it closed under the operation. So no Steiner
    quasigroup obeys a law that the 3-point line fails.
  - The 3-point line obeys exactly these 382.
- **Checked directly on eight systems** [FORCED]: the Fano plane (7 points), the affine plane AG(2,3) (9), a
  cyclic system on 13, PG(3,2) and a cyclic system on 15, a cyclic system on 19, AG(3,3) (27) and PG(4,2)
  (31).

## Five operations are the threshold

- The distributive law x·(y·z) = (x·y)·(x·z) has five operations. [FORCED]
  - It holds on the 3-point line, in AG(2,3) and in AG(3,3).
  - It fails in the Fano plane, in PG(3,2) and in the 13-point system.
- So the shortest law that tells two Steiner systems apart has exactly five operations. [FORCED]
- [READING] Up to four operations, every law about Steiner systems is already settled on one line.

## An archived verdict, corrected

[FORCED]
- The archived ETP database reported only 342 laws for the 13-point system and for PG(3,2), and called the
  40 missing laws "small-order coincidences".
- All 40 follow from the axioms. For example, #313, x·x = y·(x·y), holds because both sides equal x.
- All 40 also hold at every assignment in both systems, recomputed on the archive's own 13-point system.
  The reported split does not exist.

## What is not claimed

- Nothing about laws with five or more operations, where the systems do differ.
- The classical facts are named, not proved again: the axioms, the varieties of Steiner quasigroups
  (Quackenbush 1976), and the normal forms of their terms.
- We found no source that states this result, in the sources below or in searches on Steiner quasigroup
  identities. It is offered as a small new observation; its method, a bound from the 3-point line plus
  rewriting, is classical.

## Sources

- R. W. Quackenbush, "Varieties of Steiner loops and Steiner quasigroups", *Canad. J. Math.* **28** (1976),
  doi:10.4153/CJM-1976-118-1.
- C. J. Colbourn and A. Rosa, *Triple Systems*, Oxford University Press (1999).
- J. D. H. Smith, "Evans' normal form theorem revisited" (2007): normal forms for quasigroup varieties,
  Steiner triple systems among them.
- The Equational Theories Project, arXiv:2512.07087 (2025): the catalog. Steiner quasigroups do not appear in
  the parts read here.
