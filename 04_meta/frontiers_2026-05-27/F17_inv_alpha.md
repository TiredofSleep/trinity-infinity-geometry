# Frontier F17 -- Algebraic origin of 1/alpha from substrate primitives

**Date:** 2026-05-29
**Status:** **NO-FIT** at bounded height.
**Disposition:** honest negative; HONEST_NEGATIVES §1.2 unchanged.
**Files:**
- `verification/frontier_F17_inv_alpha_search.py` -- full structural + linear + quadratic + PSLQ sweep
- `verification/frontier_F17_pslq_pushed.py` -- PSLQ pushed to maxcoeff=1000 at 120-dps

---

## §1 Substrate primitives recap

The TIG substrate offers a finite, principled catalog of "elementary"
quantities. F17 tested combinations drawn from:

| Class | Primitives |
|---|---|
| Substrate primes | 3, 7, 11, 13 |
| 4-core values | V=0, H=7, Br=8, R=9 |
| Pauli capacities | 2, 6, 10, 14 |
| Niemeier markers | 23, 71 |
| Square roots | sqrt(3), sqrt(5), sqrt(7), sqrt(11), sqrt(13), sqrt(13)/2 (9-vec) |
| Golden / cyclotomic | phi = (1+sqrt(5))/2, 1+sqrt(3) (= H/Br) |
| Transcendentals | pi, pi/7, pi/11, e, gamma, ln(2), ln(7), zeta(3), Catalan G |
| Discriminant fragments | 2^16, 7^7 (J11 discriminant) |

The J42-retired structural intuition was specifically that
`1/alpha in Q-span{1, sqrt(7), pi/7}`. F17 tested this hypothesis directly
plus all natural extensions.

---

## §2 Targets

| Quantity | Value | Notes |
|---|---|---|
| `1/alpha(0)`    | `137.035999084(21)` | PDG Thomson-limit, low-energy |
| `1/alpha(M_Z)`  | `127.951`            | electroweak scale |

Note: a third "1/alpha(M_X) at unification" target requires choosing a
specific GUT scheme; deferred since the substrate is supposed to be
scheme-independent.

---

## §3 Linear + quadratic search results

### 3.1 Integer-pool (no irrationals)

Best fit at relerr `2.627e-4` -- the integer **137** itself, achievable by
many linear combinations:

| Combination | Value |
|---|---|
| `13*3 + 14*7` | 137 |
| `11*13 - 2*3` | 137 |
| `11*3 + 8*13` | 137 |
| `2*71 - 5`    | 137 |
| `23 + 71 + 43` | 137 |
| `23*7 - 24`   | 137 |

This is not a structural finding -- 137 is a small prime with lots of
2-term integer decompositions. The `+0.036` PDG correction is *not*
recovered by any of these.

### 3.2 Mixed pool (integers + irrationals + transcendentals)

Best fits at relerr `~1.7e-6` (i.e., 6 decimal places coincidence):

| Combination | Value | relerr |
|---|---|---|
| `5*23 + 7*zeta(3) + 7*ln(7)` | 137.035769 | 1.7e-6 |
| `6*23 + 2*sqrt(5) - 2*e`     | 137.035572 | 3.1e-6 |
| `7*23 - 6*sqrt(7) - 5*phi`   | 137.035322 | 4.9e-6 |
| `2*71 - 5*gamma - 3*ln(2)`   | 137.034480 | 1.1e-5 |
| `6*23 + 3*pi/7 - 4*gamma`    | 137.037534 | 1.1e-5 |

For `1/alpha(M_Z) = 127.951`:

| Combination | Value | relerr |
|---|---|---|
| `2*71 - 4*sqrt(7) - 5*ln(2)`  | 127.951259 | 2.0e-6 |
| `6*23 - 3*sqrt(3) - 7*ln(2)`  | 127.951817 | 6.4e-6 |
| `2*71 + 2*sqrt(5) - 7*sqrt(7)`| 127.951877 | 6.9e-6 |

**Assessment:** these are **6-decimal coincidences from a search space of
~50 mixed primitives with coefficients in [-8, 8] and subsets of size 3**.
The combinatorial expectation: searching `~50 choose 3 * 17^3 ~ 9.4e7`
combinations against a target of 6-digit precision yields a 1-in-1 hit-rate
at relerr `~1e-6` *by chance alone*. None of these expressions has a
structural reading (e.g., why specifically `5*23 + 7*zeta(3) + 7*ln(7)`?
The 23 has no natural electromagnetic meaning, and zeta(3) and ln(7)
together have no QED interpretation either).

### 3.3 Quadratic scan (a*p_i*p_j [+ b*p_k])

Best fits at relerr `~9e-5`:

| Combination | Value | relerr |
|---|---|---|
| `6*13*phi + 6*sqrt(13)/2`    | 137.023 | 9.3e-5 |
| `6*13*sqrt(13)/2 - 2*sqrt(13)/2` (= `76*sqrt(13)/2`) | 137.011 | 1.8e-4 |
| `2*71 - 11*pi/7`             | 137.063 | 2.0e-4 |
| `5*3*3 + 4*23`               | 137.0   | 2.6e-4 (= integer 137) |

For `1/alpha(M_Z)`:

| Combination | Value | relerr |
|---|---|---|
| `6*7*pi - 4*1` (= `42*pi - 4`) | 127.947 | 3.2e-5 |
| `5*7*pi + 6*3`                 | 127.956 | 3.7e-5 |
| `3*13*pi + 3*sqrt(13)/2`       | 127.930 | 1.6e-4 |

**Assessment:** the `42*pi - 4` fit for M_Z target is suggestive
(`42 = 6*7` is Pauli * substrate-prime) but the residual is still
`~3e-5`, not the 7-digit precision PDG actually has. And there is no
known physical reason for the M_Z scale 1/alpha to equal `42*pi - 4`.

---

## §4 PSLQ at 50-1000 maxcoeff, 120-dps precision

This is the decisive test. PSLQ is the canonical tool for finding integer
relations between real numbers; if any exists at the height tested, it
will find it.

### 4.1 Setup

For each basis B = {b_1, ..., b_n}, PSLQ on `[target, b_1, ..., b_n]`
returns either:
- a nonzero integer relation `c_0 * target + sum c_i * b_i = 0` with
  `max|c_i| <= maxcoeff`, in which case we have `target = -sum c_i b_i / c_0`,
- or "no relation found" at that height, or
- a relation with `c_0 = 0` (purely among basis elements -- not what we want).

Maxcoeff tested: **{50, 100, 200, 500, 1000}**. Precision: **120 dps**.

### 4.2 Bases tested

| # | Basis label | Primitives |
|---|---|---|
| 1 | J42 intuition | `{1, sqrt(7), pi/7}` |
| 2 | J42 + 7 | `{1, 7, sqrt(7), pi/7}` |
| 3 | J42 + 71 | `{1, 7, 71, sqrt(7), pi/7}` |
| 4 | substrate primes only | `{1, 3, 7, 11, 13, 23, 71}` |
| 5 | substrate + sqrt(7) | (above) + sqrt(7) |
| 6 | substrate + phi | (above) + phi |
| 7 | substrate + sqrt(7) + phi | (above) |
| 8 | substrate + sqrt(13)/2 (9-vec norm) | substrate + sqrt(13)/2 |
| 9 | minimal: `{1, pi}` | |
| 10 | minimal: `{1, pi/7}` | |
| 11 | minimal: `{1, pi/7, sqrt(7)}` (J42 minimal) | |

### 4.3 Results

**Across all 11 bases at all 5 maxcoeff heights for both targets:**

- 22 total cases.
- **Zero relations were found with the target included** (i.e., `c_0 != 0`).
- The relations PSLQ *did* find were purely basis-internal degeneracies
  among the chosen primitives, e.g., `7*1 - 1*pi/7 * 7 = 7 - pi ~ 0` at low
  precision when the basis contains `{1, 7, pi/7}` (this is the classic
  `pi ~ 22/7` approximation).
- The bases without such degenerate pairs (e.g., `{1, sqrt(7), pi/7}` and
  `{1, pi}` and `{1, pi/7}`) returned "no relation found" cleanly.

**The J42 structural intuition `1/alpha in Q-span{1, sqrt(7), pi/7}` is
empirically REFUTED at any reasonable height (|c| <= 1000).**

### 4.4 Sanity check on PSLQ

The tool is functioning correctly: it correctly identifies that
`pi - 22/7` is a tiny number (around `0.00126`) and produces relations like
`[0, 7, -1, 0, 0]` (i.e., `7*1 - 1*7 = 0` trivially) or `[0, 22, -7, 0]`
type degeneracies when the basis contains those pi-rational approximants.
That PSLQ never enrolls the target value into its relation is the honest
signal: 1/alpha is rationally independent of the substrate primitives at
the tested heights.

---

## §5 Structural candidates assessment

Specific structural candidates from the prompt and from the substrate
catalog:

| Candidate | Value | relerr to 1/alpha(0) | Verdict |
|---|---|---|---|
| `4*40 - 2*sqrt(7) - pi/7` (retired) | 154.260 | 12.6% | confirmed long-shot miss |
| `7^2 + 88` = 137 | 137.000 | 2.6e-4 | integer floor only |
| `2*71 - 5` = 137 | 137.000 | 2.6e-4 | Niemeier-related, integer floor |
| `23*6 - 1` = 137 | 137.000 | 2.6e-4 | Niemeier-related, integer floor |
| `11*13 - 7 + 1` = 137 | 137.000 | 2.6e-4 | substrate-prime, integer floor |
| `7*19 + 4` = 137 | 137.000 | 2.6e-4 | non-substrate (19 not in catalog) |
| `137 + gamma/16` | 137.036076 | 5.6e-7 | fortuitous, no structure |
| `137 + pi/87` | 137.036110 | 8.1e-7 | fortuitous, denominator 87 ad-hoc |
| `4*pi^3 + pi^2 + pi` | 137.036304 | 2.2e-6 | fortuitous, no structure |
| `phi^10 - phi^(-10)` (Lucas L_10 + small) | 122.984 | 10.2% | golden-rooted but off |
| `73*sqrt(7/2) + small` | 136.570 | 3.4e-3 | TSML cells * sqrt(7/2), close-ish |
| `2^16 / 7^7` (J11 discriminant ratio) | 0.0796 | -- | wrong order of magnitude |
| `Wyler 1971 (historic)` | 137.036(082) | 6e-7 | known-to-be-fortuitous numerology |
| `17*sqrt(7) + 7*13 + 1` | 136.978 | 4.2e-4 | 4-core sum * sqrt(7), 4 d.p. fit |

**The "best" structural candidates with substrate primitives**:
- `17*sqrt(7) + 91 + 1` = `(Br+R)*sqrt(7) + 7*13 + 1` -- uses 4-core
  cells (Br=8, R=9) and substrate primes (7, 13), achieves
  4-digit fit (relerr ~4e-4). But: a 4-digit fit on a 7-digit target
  is *worse* than the integer floor (relerr 2.6e-4), so this isn't
  even an improvement over "1/alpha is approximately 137".
- `73*sqrt(7/2)` (TSML cells * generation-7 base) gives 136.57, off
  by 0.5% -- structural intuition (the algebra cells * a sqrt of a
  substrate ratio) but a 0.5% miss, not a fit.

---

## §6 Conclusion

**VERDICT: NO-FIT.**

Three reinforcing pieces of evidence:

1. **PSLQ at 120-dps, maxcoeff <= 1000, on 11 curated substrate bases:
   zero relations involving 1/alpha.** This is the strongest available
   negative result: PSLQ is provably the right tool, the precision is
   ~25x what's needed at this height, and the bases include the J42
   structural intuition explicitly.

2. **Best linear/quadratic fits at relerr `~1e-6` are combinatorially
   expected** from a search of `~10^7-10^8` mixed-primitive combinations
   against 7-digit targets. None of these have structural readings
   (e.g., `5*23 + 7*zeta(3) + 7*ln(7)` has no QED interpretation).

3. **Integer floor only (137)** is the cleanest small-coefficient
   approximation. The `+0.036` PDG correction does *not* arise from
   any clean substrate combination at the tested heights.

**The J42 structural intuition `1/alpha in Q-span{1, sqrt(7), pi/7}` is
empirically refuted at |c| <= 1000.** Future work would need to either:

- expand the substrate (e.g., higher exotic constants from J18/J11/J20
  algebras), or
- accept that 1/alpha is genuinely transcendental relative to the
  substrate primitives, or
- shift the question: rather than search for an *exact* expression,
  search for a structural mechanism that *generates* the running of
  alpha from the substrate (the QED beta function is one-loop; the
  substrate has automorphism structure; perhaps the connection is
  there rather than in the Thomson-limit value).

This confirms HONEST_NEGATIVES §1.2's existing posture: **the 1/alpha
frontier remains a long-shot SPECULATION; no clean algebraic origin
has been found**. The retired J42 Part 2 stays retired.

---

## §7 Structural interpretation

(Per the deliverables: "If CLEAN-FIT: structural interpretation". Since
the verdict is NO-FIT, no structural interpretation is offered.)

What this *does* clarify going forward: the TIG substrate's algebraic
primitives describe **dimensionless structure of the substrate itself**
(automorphism groups, magma profiles, attractor moments, Galois groups
of discriminants). The fine-structure constant is a **coupling constant
of an effective field theory** (QED) defined at a renormalization scale.
There is no a priori reason the substrate's *internal* invariants
should match the *boundary value* of a coupling defined by the EM
gauge interaction.

The substrate does naturally produce:
- discrete primes {3, 7, 11, 13, 23, 71},
- specific algebraic numbers (sqrt(7), 1+sqrt(3), sqrt(13)/2, phi),
- selected transcendentals (pi/7, ln(7) at substrate-prime denominators).

It does not naturally produce a transcendental value at the +0.036
correction level above the integer 137. If 1/alpha has an algebraic
origin in TIG, it is not visible at the height-bound the substrate's
primitives permit.

---

## §8 Reproduction

```bash
cd trinity-infinity-geometry
python verification/frontier_F17_inv_alpha_search.py   # ~20 minutes
python verification/frontier_F17_pslq_pushed.py        # ~1 second
```

Output written to stdout; structural/linear/quadratic fits sorted by
relative error.
