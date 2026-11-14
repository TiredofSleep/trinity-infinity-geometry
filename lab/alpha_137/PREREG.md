# The edge at 137: a registered test (registered 2026-11-14, before any run)

> *why is the edge of the coin 137 edges... seems to be where this leads... the answer is in how primes form direction
> on the interleaved staircase* · *it's not a single prime... in my mind it's the prime gradient... how they are
> spread, producing a compression and a taper* — the author, 14 November 2026

**[FENCE]** This is a physics reading. It is not a premise and not evidence. It is tested here as a registered
prediction, judged against a look-elsewhere null, with everything fixed before anything is computed. The mathematics
it draws on is in [`../../towers/THE_STAIRCASE.md`](../../towers/THE_STAIRCASE.md) and
[`../../towers/seven_levels/TORUS_MOMENTS.md`](../../towers/seven_levels/TORUS_MOMENTS.md). The script is
[`alpha_test.py`](alpha_test.py), committed with this page.

## The reading

The inverse fine-structure constant, α⁻¹ = 137.035 999 177(21) (CODATA 2022), is the coin's edge, made by how the
primes are spread at 137. Its whole part is the prime 137: the phase-space pixel 1/p at p = 137, as the author put it
on 14 November 2026. Its remainder, 0.035 999 177, is a correction from the prime gradient: the compression, the
taper and the primes' directions.

## What came before: a proven dead end, kept

WP124 (May 2026) wrote 1/α ≈ 4·|Aut(V)| − 2√7 − π/7 − … from the retired tables. Its leading terms give 154.26, not
137.036, an 11% gap rather than the 10⁻⁵ it claimed. The audit of 2026-05-07 found this:
[`STATUS_REPORT_2026-05-07.md`](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Atlas/META_PLAN_2026-05-06/STATUS_REPORT_2026-05-07.md)
in the retired ck repository. Its lesson is the one this registration is built on. Given enough freedom in choosing
terms, some formula always lands near 137, so the freedom has to be fixed, and counted, before anything is computed.

## The target, and α's running

- **The target** is α⁻¹ at zero momentum transfer: 137.035 999 177, with standard uncertainty σ = 0.000 000 021
  (CODATA 2022).
- **α runs.** At the τ mass α⁻¹ is about 133.5, and at the Z mass about 127.95 (MS-bar scheme; PDG 2017). A number
  made from primes carries no energy scale, so even a match at 137.036 would owe an account of why the zero-momentum
  limit is the edge.
- **The grammar below is built on 137**, so it presupposes that limit. This is registered as a limit of the test. No
  hit counts as physics without a second registered test, on a different constant, predicted before it is computed.

## The grammar, fixed now

Fourteen atoms, each a pure number at x = p = 137. They come from the staircase page and from the qudit floor's
proved laws, and none has a free parameter.

| | atom | from |
|---|---|---|
| a1 | 1/ln 137 | the compression |
| a2 | 1/(137 ln² 137) | the compression's gradient (its size) |
| a3 | 1/√137 | the taper |
| a4 | 1/137 | the pixel |
| a5 | 1/137² | the pixel's area, one cell of the phase plane |
| a6 | 2e^(−γ) − 1 | the sieve's over-prediction (Mertens) |
| a7 | 1 − e^γ · ln 137 · Π_(p ≤ 137) (1 − 1/p) | Mertens' miss at 137 |
| a8 | (ψ(137) − 137)/137 | the weighted staircase's deviation from its line |
| a9 | (θ(137) − 137)/137 | the same, with primes only |
| a10 | 1 − π(137)/(li(137) − li(2)) | the compressed line's miss |
| a11 | (p + 2)/((p + 1)√(p − 1)) at p = 137 | the size of the oscillator states' skew, the taper theorem |
| a12 | 2/(p + 1) at p = 137 | the fourth moment's taper, 2 − 2p/(p + 1) |
| a13 | 8/(3π) − S/p^(3/2) at p = 137 | the norm state's distance from Sato–Tate (S = Σ\|W\|, by its closed form) |
| a14 | \|K(1, 137)\|/(2√137) | the direction of 137: its Kloosterman angle, \|cos θ\| |

Forms, with s = +1 or −1:
- F1: 137 + s·a_i (28 expressions);
- F2: 137·(1 + s·a_i) (28);
- F3: 137 + s·a_i·a_j for i < j, and 137 + s·a_i² (210);
- F4: 137 + s·a_i/a_j for i ≠ j (364).

So the grammar G has 630 expressions. F2 with a8 and a9 contains ψ(137) and θ(137) themselves.

The drafter knew the digits of α⁻¹, and the rough size of some atoms (1/ln 137 is about 0.2), when writing this list.
No expression was computed before this commit.

## The statistic and the null

- **The statistic**, d*, is the distance from α⁻¹ to the nearest expression in G.
- **The look-elsewhere null.** Draw a target T uniformly from [137, 138], "137 and a fraction", any of which the
  reading could equally have claimed. The p-value is the chance that T lies within d* of some expression in G. It is
  computed exactly, as the length of the union of the intervals [Q − d*, Q + d*] that lies inside [137, 138].
- **Decoys.** The same statistic for three targets with no physical meaning: 137 + (π − 3), 137 + (e − 2) and
  137 + (√2 − 1).

## The predictions

| | prediction | dies if |
|---|---|---|
| A0, forced | the atoms are computed as defined. π(137) = 33; the norm state's closed form gives the logged negativities at p = 5 and 7 (4.252724292100 and 7.902228372133); at p = 137 the oscillator states themselves give a11 and a12; and \|K(1, 137)\| ≤ 2√137 | any cross-check fails |
| A1, the reading (strong) | some expression in G lies within 3σ = 6.3 × 10⁻⁸ of α⁻¹ | no expression does |
| A2, the reading (weak) | the nearest expression is closer than chance: p-value below 0.01 | p ≥ 0.01 |
| A3, calibration | none of the three decoys has a p-value below 0.01 | a decoy does, which would show that the grammar finds "hits" anywhere |

**The drafter's expectation, registered:** A0 and A3 hold; A1 and A2 die.

## If it held

A hit, A1 or A2 at p < 0.001, would still not be a claim. It would earn a second registered test: the same grammar,
unchanged, applied to a second constant chosen before the run, such as the weak mixing angle or the proton-to-electron
mass ratio, with the running accounted for.

## Run

```
python alpha_test.py calibrate   # A0 only: the atoms' cross-checks; prints no distance to any target (seconds)
python alpha_test.py run         # everything; writes alpha_test_run.log (seconds)
```

## Sources

- The CODATA 2022 recommended values (NIST): α⁻¹ = 137.035 999 177(21);
  [NIST's table](https://www.physics.nist.gov/cuu/pdf/wallet_2022.pdf).
- Particle Data Group, *Review of Particle Physics* (2017), the electroweak review: α̂(M_Z)⁻¹ = 127.950 ± 0.017 and
  α̂(m_τ)⁻¹ = 133.471 ± 0.016 in the MS-bar scheme.

---

## Scores (added after the run, 2026-11-14)

Run by [`alpha_test.py`](alpha_test.py), committed with this registration at 8d54ab0, before the run; the output is
kept in [`alpha_test_run.log`](alpha_test_run.log). **A0 and A3 held; the reading's two predictions, A1 and A2,
died.**

| | outcome | evidence |
|---|---|---|
| A0, forced | held | every cross-check passed |
| A1 | **died** | the nearest expression, 137 + a4/a1 = 137 + ln 137/137 = 137.035912270, is 8.7 × 10⁻⁵ from α⁻¹: 4 100σ |
| A2 | **died** | its look-elsewhere p-value is 0.0216, above the registered 0.01 |
| A3 | held | the decoys' p-values are 0.268, 0.677 and 0.436 |

The results page is [`README.md`](README.md).
