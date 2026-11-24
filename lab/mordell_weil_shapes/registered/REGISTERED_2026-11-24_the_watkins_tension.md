# Registered before looking: the tension with Watkins (round 10)

Written 2026-11-24. No Mordell–Weil generator, height or lattice shape of any Stein–Watkins curve has been computed. The
script, [`../watkins_round.py`](../watkins_round.py), is committed with this page. Before the run it is exercised only
on Cremona curves already read and on timing calls that print no shape.

**The author's instruction (24 November 2026):** "go", choosing the full Stein–Watkins tables to test the tension.

## What is being tested

- **The tension.** Cremona's 1 052 rank-2 curves of prime conductor below 5 × 10⁵ are thin (elongation at least 2)
  in 10.1% of cases ([`../watkins_compare.log`](../watkins_compare.log)). Watkins (2006, §6.4) found 35.4% for the
  2 143 079 rank-2 curves of prime conductor below 10¹⁰ in the Stein–Watkins database. Both populations have
  |Δ| = N.
- **The author's sentence it puts at stake.** Rounds 1 and 2 registered the author's "Larger numbers make a long thin
  triangle less and less likely". Both passed on Cremona's tables, which end at conductor 5 × 10⁵. Watkins's figure
  suggests that, at least for prime conductors, the trend reverses somewhere between 5 × 10⁵ and 10¹⁰. The
  Stein–Watkins prime tables reach 20 000 times further out, so they can decide it.

## Data and sample

- **Data.** The Stein–Watkins database: the SageMath package `database_stein_watkins-20110713.tar.gz`, 2.64 GB, from a
  SageMath mirror, checked against the SHA-256 published in SageMath's `checksums.ini`. Only its prime-conductor
  tables are used, and from them only each isogeny class's analytic rank, its conductor and its first curve's
  coefficients. The generators are computed here.
- **Strata.** Isogeny classes of analytic rank 2, drawn at random with seed 20261124:
  - **A:** every class with N < 5 × 10⁵. These overlap Cremona's tables.
  - **B:** 2 000 classes with 10⁷ ≤ N < 10⁸.
  - **C:** 2 000 classes with 9 × 10⁸ ≤ N < 10⁹.
  - **D:** 2 000 classes with 9.9 × 10⁹ ≤ N < 10¹⁰.
  - **U:** 4 000 classes drawn uniformly from all of them, N < 10¹⁰. This is Watkins's population.
- **Per curve.**
  - PARI's `ellrank` finds independent points; if it finds fewer than two, it is called again with more effort.
  - The two points are saturated at every prime up to 100 with `ellsaturation`.
  - Then come the height Gram matrix and the shape (x, y), as in the rest of this folder, and the period lattice's
    shape τ.
- **Failures.** A curve where two independent points are not found is a failure. Failures are counted and kept,
  because a long generator is the hard one to find, so failures may lean thin. If they exceed 5% of a stratum, its
  criteria are scored twice, once with the failures counted as round and once as thin, and a criterion is decided
  only if both scorings agree.

**Before the run, read only:**
- **Counts:** the prime tables hold 2 143 079 classes of analytic rank 2, exactly Watkins's count, and 1 052 of
  them have N < 5 × 10⁵, exactly Cremona's count ([`../watkins_sample.log`](../watkins_sample.log)).
- **Timing:** eight curves near 10¹⁰ each took 0.02 to 0.1 s, with two points found
  ([`../watkins_timing.log`](../watkins_timing.log)). No shape was printed. That speed is why strata B, C and D were
  set at 2 000 curves each and U at 4 000, rather than the 600 and 1 200 of the first draft.

## Predictions

- **W0, a check of the pipeline, not a prediction.**
  - Every curve of stratum A must be among Cremona's prime-conductor rank-2 curves, matched by conductor and
    j-invariant. Cremona's tables are complete below 5 × 10⁵.
  - Each must have two points found, and its shape must match Cremona's to 10⁻⁶ in x and y.
  - How many of Cremona's curves the Stein–Watkins tables hold is recorded.
  - If W0 fails, the round stops.
- **W1, Watkins reproduced (Claude Code).** In U the share with elongation at least 2 lies between 0.32 and 0.39.
  **Miss** outside that window.
- **W2, the author's sentence carried out to 10¹⁰.** The thin share keeps falling as the conductor grows: A ≥ B ≥ C ≥ D,
  each step allowed one standard error of slack. **Miss** if D's share exceeds A's by more than three standard
  errors.
- **The rival (Claude Code, from Watkins's published figure).** The trend reverses: D's thin share is above 0.25.
- **W3, the mechanism (Claude Code; two-sided).** The shape law given the period lattice does not depend on the
  conductor.
  - The test uses τ-bins fixed now: Im τ in [0.866, 1.5), [1.5, 2), [2, 2.5), [2.5, 3.5) and [3.5, ∞).
  - In every bin holding at least 30 curves in both A and D, the two thin shares differ by at most three standard
    errors. **Miss** if any bin differs by more.
  - If W3 holds, any change in the overall share comes from a change in how elongated the curves' own period
    lattices are, not from a change in the law.

**Recorded, with no prediction.**
- Thin shares at 2, 4, 8 and 16 in every stratum, against Watkins's 35.4%, 9.4%, 1.7% and 0.2%.
- The distribution of Im τ in every stratum.
- The share of x in each tenth of [0, ½] for y ≥ 1, against Watkins's Table 1.
- The failure counts and the time per curve.

---

# Outcome

(Not yet run.)
