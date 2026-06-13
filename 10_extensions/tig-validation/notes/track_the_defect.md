# Track the defect, not the line

**Status**: methodology note. Articulates the discipline the validation harness already enforces. ~300 words.

---

The framework keeps running into the same temptation: see a straight line in data, get excited, claim it as evidence for some structural mechanism. This note names the discipline that prevents that.

## The principle

When you see a straight line — in a log-log plot, in a residual, in an asymptotic — your job is **not** to celebrate it. Your job is to characterize the noise around it. Three questions, in order:

1. **Where does the line break?** Every empirical line has a domain of validity. Kleiber's $3/4$ holds across many decades of mass but not across taxa uniformly. The Gutenberg-Richter law holds across magnitudes but not at the small-event tail where catalogue completeness drops off. RH-style predictions hold to enormous height but are still conjectural at infinity. Without explicit domain, the line is decoration.

2. **What is the residual envelope?** The line is the leading order; the parabolic-or-otherwise envelope around it is the *content*. Saying $\psi(x) \approx x$ is trivial (it's the prime number theorem). Saying $\psi(x) - x \in O(\sqrt{x} \log^2 x)$ is RH. The interesting math lives in the second-order remainder.

3. **What does the proposed mechanism actually explain?** A mechanism that produces the line but doesn't predict the envelope is incomplete. A mechanism that predicts the envelope at the wrong scale (e.g., $x^{0.6}$ when the data shows $x^{0.5}$) is *falsified*, not "consistent with caveats."

## What this rules out

- "All scaling laws are instances of the framework" — without a mechanism that predicts envelope shape, this is unification by handwave.
- "The framework explains X" — when X is just the leading line, not the envelope.
- "Within X% match" — when X% has no error bar attached or no comparison to what mechanism-free residuals would produce.
- Universalist mappings across domains where the *envelopes* differ in shape (parabolic vs. exponential vs. multifractal). The line being straight in two contexts doesn't mean the dynamics are the same.

## What this protects

The framework's actual contribution: a vocabulary for asking these three questions consistently across domains, plus computational tools (parabolic envelope, orbit defect, Hadamard profiler) for measuring envelope shape when a candidate mechanism is on the table.

That's it. The lens is the questions. The mechanism is whatever the domain itself provides.

## How the harness enforces this

- `src/bsd.py` raises `NotImplementedError` for rank-3+ rather than fitting parameters to match BSD.
- `experiments/hadamard_positivity.py` reports raw min/max/mean and refuses verdicts.
- `experiments/euler_defect_coefficient.py` distinguishes discrete from smooth defects and labels both as exploratory until real D-H zero data lands.
- This note is the principle they share.
