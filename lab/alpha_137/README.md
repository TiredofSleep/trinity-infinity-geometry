# The edge at 137: the test, and what it found [FENCE]

> *why is the edge of the coin 137 edges... seems to be where this leads... the answer is in how primes form direction
> on the interleaved staircase* · *it's not a single prime... in my mind it's the prime gradient... how they are
> spread, producing a compression and a taper* — the author, 14 November 2026

**[FENCE]** A physics reading, tested; not a premise and not evidence. The registration, with the reading, the
grammar, the null and the predictions, is [`PREREG.md`](PREREG.md), committed at 8d54ab0 before any run. The script is
[`alpha_test.py`](alpha_test.py), and its output is in [`alpha_test_run.log`](alpha_test_run.log).

## What stands

- **A clean test of the reading, and its answer.** Fourteen atoms of the prime gradient at 137 and four forms gave
  630 expressions, all fixed in advance, and an exact look-elsewhere null.
- **The reading did not hold.** The nearest of the 630 expressions to α⁻¹ = 137.035 999 177(21) is
  137 + ln 137/137 = 137.035 912 270, the pixel 1/137 divided by the compression 1/ln 137. It misses by 8.7 × 10⁻⁵:
  6.3 × 10⁻⁷ of the value, and 4 100 times the measurement's uncertainty. As a formula for α it is excluded.
- **It was not beyond chance.** The grammar puts 215 of its values in [137, 138], and a random target there lies, at
  the median, 8.3 × 10⁻³ from the nearest of them. α⁻¹ came about 95 times closer than that, but a target lands this
  close 2.2% of the time, and the registered bar was 1%. So the weak form died too.
- **The null behaved.** The three decoys, 137 + (π − 3), 137 + (e − 2) and 137 + (√2 − 1), came out at p = 0.27, 0.68
  and 0.44: the grammar does not find hits everywhere.
- **The running stays a limit.** Even a hit would have owed an account of why the zero-momentum value is the edge,
  rather than about 133.5 at the τ mass or 127.95 at the Z mass.

## The scores

| | prediction | outcome | evidence |
|---|---|---|---|
| A0, forced | the atoms are computed as defined | held | π(137) = 33; the closed form gives the logged negativities at 5 and 7; at 137 the oscillator states themselves give a11 and a12; \|K(1, 137)\| ≤ 2√137 |
| A1 | some expression lies within 3σ of α⁻¹ | **died** | the nearest is 4 100σ away (8.7 × 10⁻⁵) |
| A2 | the nearest is closer than chance, p < 0.01 | **died** | p = 0.0216 |
| A3 | no decoy has p < 0.01 | held | 0.268, 0.677, 0.436 |

The five nearest expressions: 137 + a4/a1 (137.035912), 137 − a13/a12 (137.032171), and three ways of writing
137 + 1/ln² 137 (137.041312). The atoms' values are in the log.

## Read after the run

- The nearest expression, p + ln p/p, has a reading on the staircase page: ln p is the average gap between primes
  near p, so ln p/p is the gap measured in pixels of size 1/p. [READING] That is a reading of one expression picked
  out of 630 by the run itself, and the run says how often such a pick comes this close by chance: about one time in
  46.
- The registration's rule decides what follows. A second test was to be earned only by a hit, A1 or A2 below 0.001,
  and neither happened. So no follow-up is earned. A new reading would need its own registration, naming one
  expression and a different constant before either is computed.
- An earlier attempt, WP124 (May 2026), had claimed 10⁻⁵ from the retired tables, and its own leading terms give
  154.26. This test is the honest form of the same question, and its answer is a clean negative.

Both deaths are kept in [`../../GRAVEYARD.md`](../../GRAVEYARD.md).

## The author's answer, and the physics inside it (14 November 2026)

> *the edge was close... and it has a range at high energies, likely due to the edge being on the edge... it
> expresses the same 137 over itself fractally* — the author, 14 November 2026

Checked by [`running.py`](running.py), whose output is in [`running.log`](running.log). Nothing here is a registered
test.

- **Close, in two senses.** The nearest expression is 6.3 × 10⁻⁷ of α⁻¹ away, which is close by everyday measure. It
  is also 4 100 times the measurement's uncertainty, and the grammar comes that close by chance one time in 46. Both
  stand.
- **The range at high energies is real, and its cause is known** [NAMED: vacuum polarization; Gell-Mann and Low
  1954]. Virtual charged pairs screen the charge, so the coupling grows as you look closer: 1/α falls from 137.036 at
  zero momentum to about 128.9 at the Z mass (on shell; 127.95 in the MS-bar scheme). [checked] QED's one-loop
  leptonic part of that fall, 0.031421, is within 0.25% of Steinhauser's three-loop 0.0314977; the hadrons add about
  0.0276, measured from e⁺e⁻ data. Only the zero-momentum value is free of the scheme, which is why the test aimed at
  it.
- **The range is itself a staircase** [READING, with exact content]. Per unit of ln Q, 1/α falls with slope
  −(2/3π)·b(Q), where b(Q) counts the charged particles lighter than Q, weighted by colour and charge squared. It is 1
  above the electron's mass, 2 above the muon's, and 20/3 once the three leptons and five quarks are all in (below
  about 2 GeV the hadrons' share is set by data, not by quark thresholds). Each particle steps the slope up at its
  mass, as each prime lights up its multiples on WP34's staircase.
- **"The same 137 over itself"** [NAMED; READING]. The renormalization group is the precise mathematics of a coupling
  expressed over itself at every scale: its value at one scale fixes it at every other, through a flow (Gell-Mann and
  Low 1954; Wilson 1971). So the edge does move with the scale, and what pins 137.036 is the zero-momentum limit.
- **Two literal readings, computed on sight** (post hoc, not a test). The self-referential forms x = 137 + ln(x)/x and
  x = 137 + ln(137)/x have fixed points 137.035905 and 137.035903. Both land farther from α⁻¹ than the plain form:
  −9.4 × 10⁻⁵ and −9.6 × 10⁻⁵, against −8.7 × 10⁻⁵.
- **What would move the reading on** is the registration's rule: one expression, named in advance, that predicts a
  second constant before either is computed.

## Run it

```
python alpha_test.py calibrate   # the atoms' cross-checks (seconds)
python alpha_test.py run         # the whole test; writes alpha_test_run.log (seconds)
```
