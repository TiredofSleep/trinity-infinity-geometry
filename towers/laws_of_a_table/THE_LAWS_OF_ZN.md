# What four operations can see of ℤ/n

*A page of [the laws of a table](README.md). Take the integers mod n as a table in two ways, and ask which
of the catalog's 4,694 short laws each one obeys. Everything here is known. It corrects the archived
[J05](https://github.com/TiredofSleep/trinity-infinity-geometry/tree/archive-2026-09-24/05_papers/algebra/J05),
whose conjecture and several counts were wrong. Every [FORCED] claim is checked by
[`verify_zn_laws.py`](verify_zn_laws.py) (23 checks, about ten seconds), and the counts again by
[`independent_check.py`](independent_check.py).*

Tags: **[FORCED]** proved here or checked by the script · **[NAMED]** a cited known result ·
**[READING]** an interpretation.

---

## Addition, x·y = x + y

- A term is the sum of its leaves. So a law holds in ℤ/n exactly when, for every variable, the number of
  times it occurs on each side agrees mod n. [FORCED]
- **The gap.** The gap of a law is the greatest common divisor of those differences. It is 0 when the
  counts agree exactly. [FORCED]
  - A law holds in ℤ/n exactly when n divides its gap.
  - Gaps 0, 1, 2, 3 and 4 occur, for 32, 4,003, 547, 28 and 84 laws.
- **The profiles.** [FORCED]
  - For n = 1, 2, 3 and 4, ℤ/n obeys 4,694, 663, 60 and 116 laws.
  - Every n ≥ 5 gives the same 32 laws.

## Negation, x·y = −(x + y)

- A leaf at depth d counts as (−1)ᵈ, and the same rule holds with these signed counts. [FORCED]
- **The gaps.** Gaps 0, 1, 2, 3 and 6 occur, for 294, 3,946, 366, 85 and 3 laws. [FORCED]
- **The profiles.** For n = 1 to 6 the table obeys 4,694, 663, 382, 294, 294 and 297 laws, and every n ≥ 7
  gives the same 294. [FORCED]
- **6 is the one exception.** Three laws have gap 6 [FORCED]:
  - #817, x = x·((x·x)·(x·x));
  - #2644, its mirror;
  - #3659, x·x = (x·x)·(x·x), whose signed counts are −2 against 4.

## Which laws these are

- **The 32 are the balanced laws:** each variable occurs equally often on both sides. [FORCED]
  - Sorting the leaves proves each of them in every commutative semigroup.
  - ℤ/5 is a commutative semigroup, and it fails every other law.
  - So the 32 are exactly the catalog laws of commutative semigroups.
- **The 294 are exactly the catalog laws of totally symmetric quasigroups,** the tables with x·y = y·x and
  x·(x·y) = y. [FORCED]
  - Rewriting with those two laws proves all 294.
  - −(x + y) mod 4 is such a quasigroup, and it obeys nothing else.
- **How the sets meet.** [FORCED]
  - The 32 and the 294 share exactly 14 laws, the consequences of commutativity.
  - The 294 lie inside the 382 laws that every Steiner triple system obeys
    ([`STEINER_SYSTEMS.md`](STEINER_SYSTEMS.md)). Mod 3, −(x + y) is the smallest of them, the 3-point line.
- [READING] In a short law the gap is never more than 4, so four operations can tell apart only the moduli
  1, 2, 3 and 4: 5 is the first modulus they cannot tell from the integers. The signs of negation add one
  exception, 6 = 2 · 3.

## Three archived statements, corrected

[FORCED]
- (2x + 2y) mod 3 is the 3-point Steiner system. It obeys 382 laws, not 179.
- −(x + y) mod 6 obeys 297 laws, so the conjecture "294 for every n ≥ 4" fails at n = 6.
- The 294 are not "the 32 laws of ℤ/n plus 262 extras". The two sets share only 14 laws; associativity, for
  example, holds in ℤ/n and fails for negation.

The archived paper's other statements stay archived, with the evidence, in
[`../../graveyard/j_series_reread/`](../../graveyard/j_series_reread/README.md).

## What is not claimed

- Nothing here is new.
  - It is classical that a law holds in all abelian groups of exponent n exactly when its exponent sums
    agree mod n.
  - The signed version is the same idea for the linear table −x − y. Linear tables are a standard tool of
    the ETP.
- The counts cover only laws with at most four operations. With more operations the gaps grow, and more
  moduli become visible.

## Sources

- H. Neumann, *Varieties of Groups*, Springer (1967): laws of abelian groups, and exponent sums.
- S. Burris and H. P. Sankappanavar, *A Course in Universal Algebra*, Springer (1981).
- The Equational Theories Project, arXiv:2512.07087 (2025), §5.2: linear tables x·y = ax + by as
  counterexamples.
