# The J series, read again (2026-10-25)

In September 2026 a census of the 56 archived papers found ten whose mathematics does not use the
retired tables and stands: J05, J14, J20, J24, J26, J27, J29, J34, J35 and J43. It judged none of them
new ([`DRIFT_CENSUS.md`](https://github.com/TiredofSleep/trinity-infinity-geometry/blob/archive-2026-09-24/04_meta/DRIFT_CENSUS.md)).
On 2026-10-25 those ten were read again, with J03 and J56, by three independent audits. Each asked one
question: what here is worth bringing into the flagship, and what exactly is wrong with the rest?

Each audit:
- re-ran the papers' own scripts;
- wrote fresh code for every claim;
- checked the literature;
- broke its own scripts on purpose, to make sure they can fail.

The scripts in this folder are that fresh code, and each `.log` is its output from the run of
2026-10-25.

## What came in

Nine pages, each with its source's errors corrected and checked by its own script. Seven are classical
mathematics; the last two are small new results:

| page | what it teaches | from |
|---|---|---|
| [`towers/THE_BALANCE_POINT.md`](../../towers/THE_BALANCE_POINT.md) | walk a polygon and average where you have been: Fejér's kernel, then sinc² | J24, J26 |
| [`towers/THE_TWO_FACES_OF_S4.md`](../../towers/THE_TWO_FACES_OF_S4.md) | the tetrahedron's group and the cube's rotations are one group acting two ways | J43, label corrected |
| [`towers/THE_SPINOR_FLOOR.md`](../../towers/THE_SPINOR_FLOOR.md) | Cl(2n) is every operator on 2ⁿ spinors; both Pascal rows, and the cube's two tetrahedra | J20, "coincidence" explained |
| [`coin/THE_TRANSPOSE_COIN.md`](../../coin/THE_TRANSPOSE_COIN.md) | odd symmetric Latin squares put every symbol on the diagonal: round-robin byes, the Lo Shu mod 3, Ryser | J29 |
| [`coin/TWO_READINGS_OF_ZN.md`](../../coin/TWO_READINGS_OF_ZN.md) | when residues, orbits and the mirror tell ℤ/n apart; the trap at n = 15 | J27, J34, J35, theorems corrected |
| [`towers/laws_of_a_table/THE_LAWS_OF_ZN.md`](../../towers/laws_of_a_table/THE_LAWS_OF_ZN.md) | which short laws x + y and −(x + y) obey mod n: four operations see only the moduli 1 to 4 | J05, corrected |
| [`coin/THE_MIRROR.md`](../../coin/THE_MIRROR.md) | the transpose on laws: 84 laws on its edge, 2,305 pairs on its sides | the ETP database |
| [`towers/laws_of_a_table/STEINER_SYSTEMS.md`](../../towers/laws_of_a_table/STEINER_SYSTEMS.md) | **new, small:** every Steiner triple system obeys the same 382 short laws | the ETP database, corrected |
| [`towers/laws_of_a_table/EIGHT_SPECIMENS.md`](../../towers/laws_of_a_table/EIGHT_SPECIMENS.md) | **new, small:** eight closures of 14 laws all have finite type specimens, with their smallest orders | J03, corrected |

## What stays archived, and the evidence

The census called the ten correct. Read again, every one of them contains at least one false or unsupported
statement.

| paper | finding | evidence |
|---|---|---|
| J24 | Its identities are Fejér's; "First-G", the "spectral product" and the 2ʲ − 1 count restate definitions | `check_j24_j26.py` |
| J24 | **False:** "sinc² is concave near ½" (Remark 7.4). It is convex there; the inflection is at t ≈ 0.4148 | `check_j24_concavity.py`; `towers/verify_balance_point.py` B9 |
| J24 | **Misstated:** Montgomery's pair correlation, 1 − sinc², is his conjecture; he proved it only for Fourier support in (−1, 1), assuming the Riemann hypothesis | Montgomery 1973 |
| J26 | **Off by a factor *k*:** the continuum limit on ℤ/N is (k/N)·sinc²(t), not sinc²(t)/N. Its "finite uncertainty product" is asserted, never proved | `check_j24_j26.py`; `towers/verify_balance_point.py` B10 |
| J20 | **Not a coincidence:** Pascal's rows 2n and n grade Cl(2n) and its spinors. Its open question O1 has the answer no: the tensor powers of a commutative algebra cannot map one-to-one onto Cl(2n) and keep multiplication | `towers/verify_spinor_floor.py` |
| J43 | **Mislabelled:** it computes the standard representation [3,1] and calls it [2,1,1]; under that label its own Theorem 2.1 fails | `check_j43.py`; `towers/verify_two_faces_of_s4.py` |
| J43 | **Its pulse table misses its target** (best residual 1.27 over all pulse orders). The angles are right, but the phases are wrong and a diagonal factor is missing. Its "24-element closure" check computes V⁻¹(VMV⁻¹)V − M, which is zero for any V. Its transitions are magnetic-dipole, not electric-dipole, and its Raman pulse is not required | `check_j43.py`, `check_j43_pulses.py` |
| J14 | Its bound, Nσ < 2 for square-free N, is correct but elementary: one clash between two absorbing elements carries the whole rate. **False:** "square-free is essential to the Echo lemma" (the count is φ(N) for every N), and the note that the DIS = 0 count at the primorials is N (it is φ(N)). The operation copies the retired table's rule pattern | `check_j14.py` |
| J14, bundled WP101 | "Its operad is free" cannot follow from a finite count, and N = 7 already misses: 75 of 105 at n = 5 | `check_wp35_wp101.py` |
| J27 | **Backwards:** the "Crossing Lemma". The truth is g ≡ 1 mod n/d, and the printed form is wrong on 10,680 of 12,284 cases | `check_j27_j34_j35.py`; `coin/verify_two_readings.py` |
| J29 | Correct, and classical; κ is a characteristic-polynomial coefficient, and "mod 3 is special" holds only for the moduli tried (the Lo Shu is mixed mod 6 too). Its diagonal lemma came in | `check_j29.py` |
| J34 | **False:** Theorem A (n = 15, g = 2, h = 11), Theorem 4.1 for general maps, and Lemma 4.2, which is inverted. Theorem D's witness is void | `check_j27_j34_j35.py`; `coin/verify_two_readings.py` |
| J35 | **False:** the first form of Theorem 3.1. The pair ⟨7⟩, ⟨11⟩ on ℤ/30 is mislabelled (M3 for M1), and its minimal-view invariant is trivial | `check_j27_j34_j35.py` |
| J56 | Its four types are the authors' paradox types, mapped onto standard ideas in machine learning. **Not reproducible:** its test sets are seeded by a memory address. **Its 125× comes from the suite's construction:** 84% of the baseline's error lies in the drift channels, and the router's feature library contains the hidden features; without them its Type II error returns to the baseline's | `check_j56_router.py` |
| J56 | Its reservoir uses the retired tables, and random commutative tables did as well or better in 16 of 18 runs | `check_j56_reservoir.py` |

### The papers on the Equational Theories Project

The checks for these are in [`etp/`](etp/). They share one engine, `etp/etpcore.py`, which rebuilds the
ETP's catalog of 4,694 laws from its definition. `etp/check_catalog.py` checks it against the real
catalog: 17 well-known equation numbers, 72 equation texts copied from the ETP, and OEIS A376640. The
archive's own scripts for these papers cannot run, because each imports a tool from an ETP checkout that
was never committed.

| paper | finding | evidence |
|---|---|---|
| J05 | **False:** its conjecture "294 laws for every n ≥ 4", since −(x + y) mod 6 obeys 297. Also false: (2x + 2y) mod 3 obeys 179 laws (it obeys 382), and (3, 7, 0) mod 10 is not a quasigroup (it is one) | `etp/check_j05_linear.py`, `etp/check_zn_gaps.py`; `towers/laws_of_a_table/verify_zn_laws.py` |
| J05 | **False:** "294 = the 32 laws of ℤ/n plus 262 extras" (the two sets share only 14), and "the smallest commutative profile at order 3 is 29" (it is 14, for 120 tables). "At least 23 profile-14 families" undercounts (order 3 alone has 82), and #40 is a second two-variable anchor. Its σ_n^min is generic: 10 of 10 random commutative tables of order 10 give the same 14 laws | `etp/check_census.py`, `etp/check_j05_j03_misc.py` |
| J03 | **False:** Theorem 5. Law #4295 has a 6-element type specimen, and the bound "at least 261 laws" fails at order 3, where a model obeys 122. Its proof's dichotomy is false too: 36 of the 45 order-3 models depend on both arguments. "No order-3 table realizes Family C" is false. Its σ, BHML, CL_STD and TSML items use the retired tables | `etp/check_j03_4295.py`, `etp/check_census.py`; `towers/laws_of_a_table/verify_eight_specimens.py` |
| ETP database | Its order-3 and order-5 censuses reproduce exactly, but they are raw data. **False:** "every commutative quasigroup of order ≥ 5 realizes Family C" (240 of the 720 at order 5 do not), and "the 13-point system and PG(3,2) obey only 342 laws" (they obey 382). Its Lean scaffold formalizes the false Theorem 5 | `etp/check_j05_j03_misc.py`, `etp/check_steiner_database.py`; `towers/laws_of_a_table/verify_steiner.py` |
| ETP database, OEIS drafts | None of the four is worth submitting. The count of commutative tables with profile exactly 14 has a(4) = 587,316 and a(5) ≈ 2.6 × 10¹⁰, not 480, because the draft counted only quasigroups. The count of distinct profile sizes is not a natural statistic; the list of Family C equations has errors in its comments; and the closure-anchor draft asserts the false Theorem 5 | `etp/check_oeis_commutative14.py` |

## Run it

```
python -I check_j24_j26.py        # each check prints its claims and exits 1 on any failure
python -I check_j24_concavity.py
python -I check_j43.py            # check_j43_pulses.py needs scipy
python -I check_j14.py            # about 90 seconds
python -I check_j27_j34_j35.py
python -I check_j29.py
python -I check_wp35_wp101.py
```

The two J56 checks import J56's own code, so they need a checkout of the archive tag. From the root of
this repository:

```
git worktree add ../tig-archive archive-2026-09-24
cd graveyard/j_series_reread
python -I check_j56_router.py ../../../tig-archive/05_papers/interdisciplinary/J56/manuscript/verification
python -I check_j56_reservoir.py ../../../tig-archive/05_papers/interdisciplinary/J56/manuscript/verification
```

The ETP checks run from `etp/`. Three of them compare against the archived database, so they take its
path:

```
cd etp
python -I check_catalog.py ../../../../tig-archive/etp_database
python -I check_j05_linear.py
python -I check_zn_gaps.py
python -I check_census.py ../../../../tig-archive/etp_database
python -I check_j03_4295.py            # about 2.5 minutes
python -I check_steiner_database.py ../../../../tig-archive/etp_database
python -I check_oeis_commutative14.py  # about 80 seconds
python -I check_j05_j03_misc.py
```
