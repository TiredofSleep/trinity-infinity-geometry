# Eight closures, eight specimens, and where the real fossils are

*A page of [the laws of a table](README.md). A small new contribution to the data of the Equational
Theories Project, with a classical method. It corrects the archived
[J03](https://github.com/TiredofSleep/trinity-infinity-geometry/tree/archive-2026-09-24/05_papers/algebra/J03),
and it confirms a correction made in the workstation repository
([`ck`, J61](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen14/targets/journals/J_series/J61/J61_CLOSURES_ALL_REALIZED.md)).
Every [FORCED] claim is checked by [`verify_eight_specimens.py`](verify_eight_specimens.py) (24 checks,
about 35 seconds; `--order6` adds the six-element search, about three minutes in all).*

Tags: **[FORCED]** proved here or checked by the script · **[NAMED]** a cited known result ·
**[READING]** an interpretation · **[OPEN]** not settled.

---

## Two definitions

- The **closure** of a law E is the set of catalog laws that hold in every table obeying E.
- A **type specimen** of E is a finite table that obeys exactly the closure of E, and no other catalog law.

The archived paper listed eight closures of exactly 14 laws. It called six of them "fossils", with no finite
specimen, and claimed a proof for one of them. All eight have finite specimens.

## The eight closures

| closure | anchor law | smallest specimen | why the 14 laws follow |
|---|---|---|---|
| C1 | #40, x·x = y·y | 3 elements | every square is one constant |
| C2 | #43, x·y = y·x | 3 elements | the two factors can be swapped |
| C5 | #4295, x·(x·y) = y·(z·x) | 6 elements | u·(v·w) depends only on {u, w} |
| C6 | #4303, x·(x·y) = z·(y·x) | 5 elements | u·(v·w) depends only on {v, w} |
| C7 | #4610, (x·x)·y = (y·z)·x | 6 elements | the mirror of C5 |
| C8 | #4637, (x·y)·x = (y·x)·z | 5 elements | the mirror of C6 |
| C3 | #1312, x = y·(((y·x)·x)·x) | 7 to 32 elements | the ETP's proofs |
| C4 | #2241, x = (x·(x·(x·y)))·y | as C3 | the mirror of C3 |

- **C1, C2, C5 and C6.** [FORCED]
  - Each rewrite in the last column is an instance of the anchor, so all 14 laws follow from it.
  - The specimen obeys these 14 and nothing else.
  - So the closure is exactly these 14, and the specimen is a type specimen.
- **C7, C8 and C4.** [FORCED] A table obeys a law exactly when its transpose obeys the mirror law, so the
  transpose of a specimen is a specimen of the mirror closure ([`../../coin/THE_MIRROR.md`](../../coin/THE_MIRROR.md)).
- **C3.** [FORCED] The specimen is a product of two tables that obey #1312:
  - the affine mean over the field with 8 elements, x·y = t·x + (1 + t)·y with t³ = t² + 1, which obeys 101
    laws;
  - a 4-element table, which obeys 61.

  The two share exactly 14 laws. On the 32-element product those 14 hold at every assignment, and every other
  law fails.
- **C3's 14 laws.** [NAMED] That #1312 implies the other 13 is the ETP's result, proved in Lean. It is not
  proved again here.

## Why products settle existence

- **The product lemma.** [FORCED] A law holds in a product A × B exactly when it holds in A and in B, because
  both sides are evaluated one coordinate at a time.
- **The criterion.** [FORCED] A law E has a finite type specimen exactly when no law outside its closure holds
  in every finite table obeying E.
  - If such a law exists, every finite table obeying E obeys it too, so no finite profile equals the closure.
  - If none exists, pick a finite table obeying E that fails each outside law. There are finitely many such
    laws, and the product of those tables is a specimen.
- **The real fossils.** [NAMED] The ETP found implications that hold in every finite table but not in every
  table (§1.3 of its paper). The premise of each such implication has no finite specimen. An example: #1117
  implies #2441 in every finite table, but not in general (Remark 5.4).
- [READING] The archived paper's notion of a fossil was sound. Its examples were the wrong ones: none of the
  eight closures of 14 laws is a fossil.

## Smallest orders

[FORCED] All three searches agree with brute force at orders 2 and 3.

- **C1 and C2.** No 2-element table has either profile, so the smallest specimen has 3 elements.
- **C6 and C8: 5 elements.** The search rests on a structure theorem: in a table obeying #4303, every column
  indexed by a product is constant. Tables obeying #4303 of orders 2, 3 and 4 obey at least 1,556, 122 and
  15 laws.
- **C5 and C7: 6 elements.**
  - If all right-nested products u·(v·w) of a table are equal, it obeys all 112 laws of that form, so its
    profile has at least 113 laws.
  - Only 3 tables of order 4 (up to renaming) and 145 of order 5 escape this, and their smallest profiles
    have 76 and 16 laws.
- **C3 and C4.**
  - Every table obeying #1312 with at most 5 elements (3, 8, 54 and 855 of them, up to renaming) also obeys
    #16, x = y·(y·x), which is not in C3.
  - At 6 elements exactly 10 tables, up to renaming, break #16 (`--order6`), and each obeys between 29 and
    130 laws.
  - So a C3 specimen has at least 7 elements.
- [OPEN] **Is the bound 8?** The ck correction reports a 7-element search in which 667 tables break #16, each
  obeying at least 18 laws. That would make the bound 8. It was not run again here: one process got through
  332 of its 837 subproblems in about 80 minutes.

## What is not claimed

- The method is not new. Products of models are textbook universal algebra (Birkhoff 1935).
- C3's laws rest on the ETP's proofs.
- The smallest C3 specimen is unknown: at least 7 elements, checked here; at least 8, by the ck correction;
  at most 32.
- The archived bound "every finite model of #4295 obeys at least 261 laws" is false: a 3-element model obeys
  122.
- The ETP's paper and data do not contain these specimens or smallest orders, as far as we checked. The ETP
  lists the smallest table obeying each law (`smallest_magma.txt`), which is a different question, and its
  finite-implication results imply that the eight specimens exist, by the criterion above.

## Sources

- The Equational Theories Project, arXiv:2512.07087 (2025): §1.3, the implications that hold only in finite
  tables; §5.1, small finite models; Remark 5.4, #1117 and #2441; §2, duality.
- The ETP repository, [github.com/teorth/equational_theories](https://github.com/teorth/equational_theories):
  the Finite Magma Explorer and `data/smallest_magma.txt`.
- G. Birkhoff, "On the structure of abstract algebras", *Proc. Cambridge Philos. Soc.* **31** (1935).
- S. Burris and H. P. Sankappanavar, *A Course in Universal Algebra*, Springer (1981): products and
  varieties.
