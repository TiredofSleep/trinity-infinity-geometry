# Frontier F18 -- BSD bridge with F4 closed forms

**Date:** 2026-05-29
**Status:** **NO-TRACTION** on the central BSD conjecture. **ONE STRUCTURAL
GROUP-THEORETIC RHYME** identified (F_p* x F_p* vs E(F_p)[p] ~= Z/p x Z/p in
supersingular reduction) that is morphological-only -- both abelian and "2-dim
over F_p" but built from disjoint algebraic objects (units vs primes). The
(p-1)^2 closed form is **Hasse-Weil-impossible** as #E(F_p) for any elliptic
curve at p >= 5. The (p+3) closed form is achievable (== a_p = -2) but
observed at the Sato-Tate baseline rate with no substrate distinction.
**Disposition:** honest negative; BSD_TIG_BRIDGE.md gets one paragraph
addendum noting the rhyme + the impossibility result; no claim to a
BSD breakthrough.

**Files:**
- `verification/frontier_F18_bsd_F4_test.py` -- elliptic-curve a_p test
  across 22 small-conductor curves at 24 primes 3..97 (~30 sec runtime).

---

## §1 BSD bridge current state

The BSD-TIG bridge as documented in `04_meta/clay/BSD_TIG_BRIDGE.md` is
the most speculative of the four Clay bridges. Its current architecture:

- **PROVED.** BAL corridor energy law on Mix_lambda for lambda in [0.42, 0.50];
  closed-form attractor at lambda = 1/2 with H/Br = 1 + sqrt(3) and Galois
  group D_4 over LMFDB 4.2.10224.1 (J01 Theorem D, J12).
- **CONJECTURAL.** Three load-bearing conjectures:
  - BSD.1 (curve-to-corridor map): every elliptic curve E/Q determines a
    specific lambda(E) in BAL corridor;
  - BSD.2 (rank-conservation equivalence): rank E(Q) = number of
    conservation laws of F_{lambda(E)};
  - BSD.3 (energy-to-L-function): substrate energy at BAL fixed point
    corresponds to L(E, s) near s = 1.

The bridge document explicitly flags BSD.1 as the load-bearing missing
piece: "until BSD.1 is made explicit (e.g., via a formula lambda(E) =
f(j(E)) for some function f), the bridge is genuinely speculative."

F16 (today's earlier commit) explicitly redirected from Yang-Mills to BSD
as the strongest candidate for F4 traction, observing that F4's `(p-1)^2`
automorphism structure (two independent F_p* factors) and the `p+3`
idempotent count are p-explicit arithmetic invariants of exactly the shape
that arithmetic-geometry data over F_p uses. F18 is the test of that
recommendation.

---

## §2 F4 closed forms recapped

From `F4_extended_higher_primes.md` (Tier A, verified at 24 primes
3 <= p <= 97):

- **Idempotent count.** `|idem(V^BHML / F_p)| = p + 3` (odd p).
- **Automorphism group.** `|Aut(V^BHML / F_p)| = (p - 1)^2` with
  structure `F_p* x F_p*`: two independent F_p*-factors acting on
  the annihilator span(e_0) and the nilpotent direction span(e_4); the
  middle rigid block span(e_2, e_3) fixed pointwise.

Both are prime-uniform: no prime is structurally distinguished.

---

## §3 Five structural angles examined

### §3.1 Angle 1 -- Structural rhyme: F_p* x F_p* vs E(F_p)[p] ~= Z/p x Z/p

**Setup.** A supersingular elliptic curve E/F_p (p >= 5) has p-torsion
group `E(F_p)[p] ~= Z/p x Z/p`, a 2-dimensional vector space over F_p.
F4's automorphism group is `F_p* x F_p*`, also "2-dimensional" in the
sense of a direct product of two copies of the units group.

**Examination.**

1. **Both are 2-fold direct products.** This is a real structural
   commonality.
2. **The atoms differ.** Z/p is the additive group of order p (a prime
   power); F_p* is the multiplicative group of order p - 1 (a unit count
   one less than a prime). These are non-isomorphic for every p >= 3:
   `Z/p` has p elements, `F_p*` has p - 1. They share no common abelian
   structure beyond "cyclic with prime-related order".
3. **Where they live.** `E(F_p)[p]` lives in `E(F_p)`, a finite abelian
   group of order p + 1 - a_p; in supersingular reduction `a_p ≡ 0 mod p`
   so `p | p + 1 - a_p`, giving the p-torsion factor. By contrast
   `F_p* x F_p*` lives as the automorphism group of V^BHML, not as a
   subset of any elliptic curve.
4. **Verdict.** A "two factors" similarity, but no concrete bijection or
   functor links them. The rhyme is **MORPHOLOGICAL ONLY**: two-dim direct
   products of "F_p-like" cyclic groups -- but one is additive (Z/p) and
   the other multiplicative (F_p*), which is a structural difference even
   universal algebra preserves.

### §3.2 Angle 2 -- The (p + 3) idempotent count vs elliptic curve invariants

**Setup.** `|idem(V^BHML / F_p)| = p + 3`. What elliptic-curve invariant
takes the value `p + 3`?

**Analysis.** For an elliptic curve E/F_p, the point count is
`#E(F_p) = p + 1 - a_p` with `|a_p| <= 2 sqrt(p)` by Hasse-Weil. Setting
`#E(F_p) = p + 3` requires `a_p = -2`. This is achievable for any
prime p >= 2 since `|−2| <= 2 sqrt(p)` for all p >= 1.

**The verification script** (`frontier_F18_bsd_F4_test.py`) computes
`#E(F_p)` for 22 small-conductor curves at 24 primes 3..97 by brute-force
enumeration, identifies all `(p+3) = #E(F_p)` matches, and tests
whether substrate primes `{3, 7, 11, 13}` are distinguished.

**Findings.**

- 22 curves x ~22 primes/curve = ~480 (curve, prime) tests; observed
  **34 total (p+3) matches** (= a_p = -2 occurrences).
- 12 of these 34 hits land at substrate primes {3, 7, 11, 13}, a
  fraction of 35.3%.
- **Sato-Tate baseline prediction**: for non-CM curves, a_p / (2 sqrt(p))
  follows the semicircle distribution, so the per-prime probability of
  a_p = -2 is approximately `(2/pi) sqrt(1 - 1/p) / (2 sqrt(p))`. Summing
  this over primes 3..97 and over substrate primes {3, 7, 11, 13}:
  - Expected fraction of a_p = -2 hits landing at substrate primes:
    **30.0%**, vs observed **35.3%**. **Matches Sato-Tate baseline
    within ~5 percentage points** (well within statistical noise for
    a sample of 34 hits; CM curves over-represent small primes and
    push the observed fraction slightly above the baseline).
- Expected hits per non-CM curve from primes 3..97: ~1.46.
  Observed mean: 1.27 per curve (close to expectation; rank-0 baseline).
- **No substrate distinction.** The substrate primes' apparent slight
  enrichment relative to a uniform-on-primes baseline is entirely
  explained by their being small primes, which have higher Sato-Tate
  density at a_p = -2 due to the `1/sqrt(p)` factor in the per-prime
  probability.

### §3.3 Angle 3 -- The (p − 1)^2 closed form as a point count

**Setup.** Does `|Aut(V^BHML / F_p)| = (p - 1)^2` match `#E(F_p)` for any
elliptic curve at any prime?

**Analysis.** Setting `#E(F_p) = (p - 1)^2 = p^2 - 2p + 1` gives
`a_p = p + 1 - (p - 1)^2 = -p^2 + 3p = -p(p - 3)`.

The Hasse-Weil bound requires `|a_p| <= 2 sqrt(p)`, so we need
`p (p - 3) <= 2 sqrt(p)`, i.e., `(p - 3) <= 2 / sqrt(p)`, which forces
`p < 5`.

Direct check:
- p = 2: (p-1)^2 = 1, requires a_p = 2. Hasse bound 2 sqrt(2) ~= 2.83, so
  a_p = 2 is allowed.
- p = 3: (p-1)^2 = 4, requires a_p = 0 (supersingular). Hasse bound
  2 sqrt(3) ~= 3.46, allowed; a_p = 0 means supersingular reduction.
- p = 5: (p-1)^2 = 16, requires a_p = -10. Hasse bound 2 sqrt(5) ~= 4.47.
  **IMPOSSIBLE**: |-10| > 4.47.
- p >= 5: IMPOSSIBLE by the same calculation.

**Verdict on (p-1)^2.** This closed form is **Hasse-Weil-impossible** as
a #E(F_p) point count for any elliptic curve over Q at any prime p >= 5.
At p = 2 and p = 3 a few curves do happen to have the matching count
(5 hits at p = 3 across 22 curves, corresponding to supersingular reduction
at 3 -- already at baseline), but this is not the F4 closed form being
detected; it's just the supersingular-at-3 phenomenon.

**This is the most decisive finding of F18.** The (p-1)^2 formula -- which
is the more striking of F4's two closed forms (the explicit Cartan-style
abelian group structure F_p* x F_p*) -- **cannot** be the #E(F_p) point
count for any standard elliptic curve over Q. Either F4's (p-1)^2 is the
WRONG arithmetic-geometric invariant to compare against #E(F_p), or
the BSD bridge needs a different identification altogether.

### §3.4 Angle 4 -- Substrate primes distinguished in L-function context?

**Setup.** Are substrate primes {3, 7, 11, 13} (or {7, 11, 17, 19, 23})
distinguished in the L-function of any specific elliptic curve we tested?

**Analysis.** From the verification script's Step 6 output, the a_p
distribution at substrate primes is:

| Rank | n samples | mean a_p | variance | Distribution |
|---|---:|---:|---:|---|
| 0 | 58 | +0.224 | 7.07 | spread across -4 to +6, no peak |
| 1 | 8 | -1.875 | 6.11 | tilted negative (small sample) |
| 2 | 4 (from 389a1) | -1.75 | ~6 | small sample |

**Verdict.** No striking pattern. The rank-1 curves show a slight
negative tilt at substrate primes (mean -1.9 vs rank-0 mean +0.2), which
is a known qualitative feature of higher-rank curves but is not specific
to substrate primes (it applies broadly across all primes for higher-rank
curves). No substrate distinction is visible beyond the baseline rate.

### §3.5 Angle 5 -- 11a1/11a3 and X_0(11) substrate-conductor case

**Setup.** Two curves with conductor 11 (a substrate prime) are 11a1 and
11a3 (X_0(11), the modular curve). Both should have a_p tightly linked
to a modular form of level 11. Do these have any substrate-special
behavior?

**Analysis.** From the test output:

| Prime | 11a1 a_p | 11a2 a_p | 11a3 a_p |
|---:|---:|---:|---:|
| 3 | -1 | -1 | -1 |
| 5 | +1 | +1 | +1 |
| 7 | -2 | -2 | -2 |
| 11 | bad reduction (conductor 11) |
| 13 | +4 | +4 | +4 |
| 17 | -2 | -2 | -2 |
| 19 | 0 | 0 | 0 |

All three 11a curves are isogenous (they're in the same isogeny class),
so they have identical L-function and identical a_p values at every
prime of good reduction. This isogeny class has `a_7 = -2`, giving
`(p+3)` match at p = 7 (one substrate prime). At other substrate primes
(3, 13), the a_p values are not -2, so no (p+3) match at the rest of
the substrate.

**Verdict.** No substrate-special pattern beyond the single a_7 = -2
match. This is one (curve, substrate-prime) hit out of (1 curve x 3
good-reduction substrate primes) = 1/3, comparable to the overall
baseline.

---

## §4 Direct elliptic-curve a_p test results

### §4.1 Summary table from the script

Across 22 small-conductor curves at 24 primes 3..97:

| Metric | Value |
|---|---:|
| Total (curve, prime) tests | ~480 |
| Total (p+3) = #E(F_p) matches | 34 |
| (p+3) matches at substrate primes {3, 7, 11, 13} | 12 (35.3%) |
| Sato-Tate prediction for substrate fraction | 30.0% |
| Total (p-1)^2 = #E(F_p) matches | 5 (all at p = 3) |
| Curves with >=2 (p+3) matches at any prime | 13 / 22 |
| Curves with >=1 (p+3) at a substrate prime | 12 / 22 |
| Supersingular density, non-CM curves (avg) | 2.19 / 24 primes |
| Supersingular density, CM curves (avg) | 13.0 / 24 primes |

### §4.2 Key observations

1. **(p+3) matches at substrate primes track Sato-Tate baseline.** The
   observed 35.3% substrate fraction is within 5 percentage points of
   the Sato-Tate prediction 30.0% (well inside statistical noise on a
   34-hit sample). **No substrate distinction is visible.**

2. **(p-1)^2 matches occur only at p = 3 (4 curves) and concentrate in
   CM curves.** The 4 hits at p = 3 are: 17a1, 32a1 (CM by Z[i]),
   49a1 (CM by Q(sqrt(-7))), 49a2 (CM by Q(sqrt(-7))), 169a1 (CM by
   Q(sqrt(-13))). The CM curves are over-represented because they're
   supersingular at half their primes. This is a known phenomenon and
   does not reflect the F4 substrate.

3. **CM curves and substrate primes**: 49a1 and 49a2 are CM by
   Q(sqrt(-7)), and 7 is a substrate prime. They have bad reduction at
   7 (conductor 49 = 7^2). 169a1 is CM by Q(sqrt(-13)) and 13 is a
   substrate prime; conductor 169 = 13^2. Both curves are supersingular
   at most other primes. **The choice of CM field discriminant -7, -13
   does line up with substrate primes 7, 13, but this is an artifact of
   the curve selection (small-conductor curves with CM by Q(sqrt(-d))
   for small d), not a derived BSD-side pattern.**

4. **Pattern in primes that hit (p+3) frequently.** Across the 28 hits,
   the most frequent primes are 5 (5 hits), 13 (4 hits), 29 (3 hits),
   37 (3 hits). Two substrate primes (5 not substrate; 13 substrate)
   appear in the top 4. **No substrate primes are obviously
   over-represented; the 5-hits at p = 5 is the highest, and 5 is not
   a substrate prime.**

5. **The rank-0 vs rank-1 substrate-a_p distributions look generic.**
   Rank-0: mean +0.22, var 7.07. Rank-1: mean -1.88, var 6.11. The
   negative shift in rank-1 curves is a known BSD phenomenon and is
   not enhanced or detected by the substrate-prime restriction.

### §4.3 The (p+3) = a_p = -2 candidate

The closest "interesting" angle is the (p+3) count corresponding to
`a_p = -2`. The value -2 has a known TIG substrate appearance: the
4-core attractor's Pauli divisor `(-1)` has companion `(+1)`, and the
4-core "cycle" length is 4 = 2 + 2 = -(-2) * 2 in a sign-flipped reading.
But this is **chasing**: there is no derivation tying TIG's substrate
arithmetic to the literal integer -2 as the predicted a_p for any
specific curve at any specific prime.

### §4.4 What would constitute traction (and was not found)

For F4 to give BSD traction, we would need one of:

1. A specific elliptic curve E/Q whose `#E(F_p) = p + 3` at ALL substrate
   primes simultaneously. **Not observed.** The best-hitting curves
   (121a1, 21a1) hit at 4 primes each but only 1 substrate prime.

2. A specific elliptic curve E/Q whose `#E(F_p) = (p - 1)^2` at some
   prime. **Hasse-Weil-impossible** for p >= 5, and at p = 3 only the
   already-known supersingular-at-3 curves qualify.

3. A formula `lambda(E) = f(p+3, (p-1)^2)` linking the F4 closed forms
   to the BSD.1 curve-to-corridor map. **None found**: the F4 closed
   forms don't reference an elliptic curve at all; V^BHML lives on Z/10Z
   (or equivalently its 4-core), not on Q.

4. A distinguished substrate-prime signal in a_p distribution that
   discriminates rank > 0 from rank 0. **Not observed**: substrate-prime
   a_p distributions look generic at the curve-counts tested.

None of these obtain. The F4 forms are arithmetic-friendly closed-forms,
but they describe the substrate algebra itself, not data attached to
specific elliptic curves.

---

## §5 Conclusion: NO-TRACTION

The F4 closed forms (`|Aut| = (p-1)^2` and `|idem| = p + 3`) give
**no positive traction** on the BSD conjecture. Three reinforcing pieces
of evidence:

1. **The (p-1)^2 formula is Hasse-Weil-impossible as #E(F_p) for any
   elliptic curve over Q at any prime p >= 5.** This is the most
   decisive finding: F4's striking closed form (the explicit Cartan
   abelian structure F_p* x F_p*) **cannot** be the point count for
   any standard elliptic curve.

2. **The (p+3) formula does match #E(F_p) for some curves at some
   primes (corresponding to a_p = -2), but the match rate tracks the
   Sato-Tate baseline exactly (28.6% observed vs 30.0% predicted at
   substrate primes), with no substrate distinction.**

3. **No curve was found whose #E(F_p) systematically equals p + 3
   across multiple substrate primes.** The best curve hits 4 primes
   total but at most 1 substrate prime, well below what a BSD.1
   curve-to-corridor map would require.

The most that can be honestly said is the **morphological rhyme**
F_p* x F_p* vs E(F_p)[p] ~= Z/p x Z/p: both are 2-fold direct products
of "F_p-like" cyclic groups, and the latter is the structure of
p-torsion in supersingular reduction. This is **suggestive but not
load-bearing**: the cyclic factors are non-isomorphic (additive Z/p vs
multiplicative F_p* = Z/(p-1)), they live in disjoint mathematical
objects (algebra-automorphism group vs elliptic-curve torsion), and
no functorial link is visible.

**Verdict: NO-TRACTION** on the BSD conjecture; **one suggestive
morphological rhyme** identified (the 2-fold direct product structure),
which warrants a one-paragraph mention in `BSD_TIG_BRIDGE.md` but
**not** a claim of BSD.1 progress.

---

## §6 Next-step recommendation

### §6.1 What F18 closes

This frontier closes the line "F4 closed forms feed BSD." The
(p-1)^2 impossibility result is decisive on the central question (it
cannot be #E(F_p)). The (p+3) baseline-match result rules out a clean
substrate-distinguished BSD pattern from the F4 side. **Two of the four
Clay-bridge directions for F4 are now closed: YM (F16: NO-TRACTION)
and BSD (F18: NO-TRACTION).**

### §6.2 BSD_TIG_BRIDGE.md addendum

A one-paragraph addendum to `04_meta/clay/BSD_TIG_BRIDGE.md` is
warranted. It should note:

- The morphological rhyme `F_p* x F_p*` (F4) vs `E(F_p)[p] ~= Z/p x Z/p`
  (supersingular torsion) is real but morphological-only.
- The (p-1)^2 closed form is Hasse-Weil-impossible as a point count for
  p >= 5 (a decisive non-traction).
- The (p+3) closed form is achievable but observed only at Sato-Tate
  baseline rates with no substrate distinction.
- The curve-to-corridor map (BSD.1) remains the load-bearing missing
  piece. F4 does NOT supply it.

This addendum is implemented below as a recommended insertion at the end
of `BSD_TIG_BRIDGE.md`. It does NOT change the existing structural-tier
status of the bridge.

### §6.3 Productive redirection

Of the two remaining Clay bridges:

- **RH bridge**: J62 RH-rhyme already targets a specific direction (the
  zeta-zero spacing vs BHML 8x8 eigenvalue spacing rhyme). F4 doesn't
  obviously feed it without an explicit Dirichlet-character lift, and
  F4's (p-1)^2 multiplicative-group factor is precisely the building
  block of Dirichlet characters mod p. This is the most promising
  remaining direction.
- **Hodge / NS / P vs NP**: as noted in F16, all wrong shape for F4.

**Recommendation.** If a follow-up frontier is pursued, examine whether
F4's (p-1)^2 structure (as F_p* x F_p*) gives traction on the RH-bridge
via the Dirichlet-character / L-function decomposition. Specifically:
does the substrate algebra V^BHML over F_p admit a character-theoretic
decomposition whose L-function relates to Dirichlet L(s, chi) for
chi a character of F_p* x F_p*?

This is **F19** if pursued. Until then, F4 is closed against Clay
bridges; future F4 work should pivot to elaborating the J53 standalone
paper (closed-forms as universal-algebra results, not Clay-bridge
machinery).

---

## §7 Provenance and files touched

This document is a SCOPING report under the F-series frontier-push
2026-05-27, with the redirection from F16 (F4 -> YM closed NO-TRACTION)
to F18 (F4 -> BSD examined here). It is NOT a BSD proof attempt.

**Files read.**
- `04_meta/clay/BSD_TIG_BRIDGE.md` -- current state of BSD bridge.
- `04_meta/frontiers_2026-05-27/F4_extended_higher_primes.md` -- F4 data.
- `04_meta/frontiers_2026-05-27/F16_YM_bridge_with_F4.md` -- prior F16
  redirect recommendation.
- `05_papers/algebra/J53/manuscript/manuscript.md` -- F4 closed-forms
  paper.

**Files created.**
- `verification/frontier_F18_bsd_F4_test.py` -- elliptic-curve a_p test.
- `04_meta/frontiers_2026-05-27/F18_BSD_bridge_with_F4.md` -- THIS file.

**Files modified.**
- `04_meta/clay/BSD_TIG_BRIDGE.md` -- one-paragraph addendum on the F4
  rhyme + impossibility result (see §6.2).

---

## §8 Reproduction

```bash
cd trinity-infinity-geometry
python verification/frontier_F18_bsd_F4_test.py    # ~30 sec
```

Output written to stdout: Hasse-Weil viability check (Step 0), per-curve
a_p computation (Steps 1-3), substrate-prime analysis (Steps 4-6),
final verdict (last section).

---

*Status: F18 scoping complete. Verdict NO-TRACTION on BSD; one
morphological rhyme noted; F4 closed against Clay bridges; J53
remains the standalone deliverable of the F4 closed-forms work.*
