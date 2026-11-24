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

The registration was committed in `4ca6f7d`, and the run came after it. The logs are
[`../watkins_compute.log`](../watkins_compute.log) and [`../watkins_round.log`](../watkins_round.log).
- The run took 162 seconds on 2 workers, for 11 052 curves.
- Two independent points were not found for 75 of them, between 0 and 1.3% of each stratum, below the 5% rule.

| stratum | conductors | n | thin share (y ≥ 2) | y ≥ 4 | largest y | median Im τ |
|---|---|---|---|---|---|---|
| A | below 5 × 10⁵ | 1 052 | 0.1008 ± 0.0093 | 0.0029 | 4.49 | 1.31 |
| B | 10⁷ to 10⁸ | 1 998 | 0.0816 ± 0.0061 | 0.0030 | 5.95 | 1.35 |
| C | 9 × 10⁸ to 10⁹ | 1 985 | 0.0866 ± 0.0063 | 0.0030 | 4.77 | 1.33 |
| D | 9.9 × 10⁹ to 10¹⁰ | 1 974 | 0.0983 ± 0.0067 | 0.0020 | 5.21 | 1.35 |
| U | uniform below 10¹⁰ | 3 968 | **0.0917 ± 0.0046** | **0.0010** | 5.05 | 1.34 |
| Watkins (2006), the same 2 143 079 curves | | | **0.354** | **0.094** | 1.7% beyond 8 and 0.2% beyond 16 | |

- **W0 passes.** The Stein–Watkins curves below 5 × 10⁵ are exactly Cremona's 1 052. The shapes from PARI's
  generators agree with Cremona's tabulated generators to 4 × 10⁻¹⁶.
- **W1 misses.** U's thin share is 9.17% ± 0.46%, not between 32% and 39%.
  - 4 curves of 3 968 reach elongation 4, against Watkins's 9.4%.
  - None reaches 8, against his 1.7%.
- **W2 is not decided.** The share falls from A to B, then stays flat at 8–10% out to D. It neither falls further nor
  reverses.
- **The rival died.** D's share is 9.8%, not above 25%.
- **W3 misses.** At the same Im τ, the shares differ between A and D. In the lowest bin they are 0.8% against 7.6%
  (+7.7 s.e.); in the bin [2, 2.5) they are 28.6% against 13.0% (−3.4 s.e.). The period lattice predicts the shape
  strongly at small conductor and weakly at large.

**None of the predictions held, and W2 is undecided.** W0 is a check, and it passed.

## Read after the run (not registered)

- **The lattices are right at every conductor.** The BSD formula, with the regulator from these generators, gives
  an analytic order of Sha that is a perfect square, to 4 × 10⁻¹⁶, for 220 of 220 curves. A sublattice of index k
  would give 1/k² of that.
  - 20 of them lie near 10¹⁰: 10 at random and the 10 thinnest
    ([`../watkins_after.py`](../watkins_after.py), [`../watkins_after.log`](../watkins_after.log)).
  - 200 are drawn at random from U, with conductors from 922 619 to 10¹⁰
    ([`../watkins_bsd_check.py`](../watkins_bsd_check.py), [`../watkins_bsd_check.log`](../watkins_bsd_check.log)).
- **So the tension was never in the curves: Watkins's §6.4 figures do not reproduce on his own population.**
  - **The definitions agree.** He takes the point of smallest height as the unit vector and reduces the other
    generator into the fundamental domain with 0 ≤ x ≤ ½. Those are the coordinates used here. His reference
    values for the uniform law, 95.5% with y ≥ 1 and a 1/Y tail, are this page's too.
  - **The population agrees:** the count is the same, 2 143 079 classes.
  - **The failures cannot explain it.** If all 32 failures in U were thin, the share would be 9.9%.
  - **One guess was tested, and it died.** Taking the pairing as ĥ(P + Q) − ĥ(P) − ĥ(Q), without the ½, gives
    10.1% thin. Halving it gives 9.4%.
  - **The cause of the published figures is not known here.**
- **What stands, measured.**
  - For rank-2 curves of prime conductor, the thin share is about 8–10% at every conductor from 5 × 10⁴ to 10¹⁰.
    That is a fifth of the uniform law's 47.7%. Below 5 × 10⁴ it is 17%, in Cremona's 213 curves there.
  - The far tail is empty: the largest elongation among the 5 957 curves of strata B, C and D is 5.95.
  - The curves' own period lattices do not change shape with conductor either: the median Im τ is 1.31 to 1.35 in
    every stratum.
- **The horizontal skew.** Watkins's Table 1 has x leaning toward ½. U shows no clear lean: its tenths run from 0.107
  to 0.093, with a standard error near 0.005. Cremona's full tables do lean, as he reports: 258 819 curves of every
  conductor with y ≥ 1, rising from 0.087 to about 0.103.

## What this changes

- **The tension on the Part F page is resolved.** There is none in the data.
- **The author's sentence of rounds 1 and 2 held on Cremona's range.** For prime conductors the fall stops above
  10⁷: the thin share is flat out to 10¹⁰. By the registered rule that is "not decided", not a miss.
- **Watkins's §6.4 is a published figure that does not reproduce.** Whether to tell him is the author's call. The
  evidence above is the whole case.
