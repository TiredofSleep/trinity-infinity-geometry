# STS profile classification — CORRECTED finding

**Test date**: 2026-05-27.
**Scripts**: `extensions/sts_15_classification.py`, plus earlier U-3 scripts.
**Raw outputs**: `overnight_outputs/sts_15_classification.{txt,json}`.

## Initial hypothesis (from U-3 writeup) — NOW REFUTED

The U-3 verdict suggested that profile 382 vs 342 tracks **geometric vs
combinatorial** Steiner triple system origin:
> "Profile 382 = projective/affine STS (STS(3), Fano STS(7), AG(2,3) STS(9));
> Profile 342 = combinatorial cyclic STS(13)."

This was a tempting interpretation but **wrong**.

## Refutation

**PG(3,2) STS(15)** — the projective space over F_2 in dimension 4, viewed as
a 15-point Steiner triple system with 35 three-element lines — gives squag
**profile 342, NOT 382.**

```
PG(3, 2) projective STS(15) (35 lines from F_2^4 \ {0}):
    profile size: 342
    contains Family C: True
```

PG(3,2) is the *most geometric* of all STS(15) constructions (it's a
projective space over a finite field). If geometry were the discriminator,
PG(3,2) should sit at profile 382 alongside STS(3), STS(7), STS(9).

It does not.

## Corrected interpretation

The 382-vs-342 split is **purely a small-order coincidence effect**, not
a geometric-vs-combinatorial distinction. Specifically:

| Order | Squag profile | Reason |
|---:|---:|---|
| 3 | 382 | Carrier so small (3 elements) that ~40 identities collapse accidentally |
| 7 | 382 | Carrier still small; same 40 identities collapse |
| 9 | 382 | Carrier small; same 40 identities collapse |
| 13 | 342 | Carrier large enough that the 40 identities can be falsified |
| 15 | 342 | Same as 13 — order ≥ 13 already eliminates the coincidences |

The crossover happens **between orders 9 and 13**. The 40 "extra" equations
satisfied at orders 3, 7, 9 are 3-variable identities (e.g., `x ⋄ y = z ⋄
(z ⋄ (x ⋄ y))`) that hold trivially when the variable range is small enough
to force collapse.

## The genuine squag variety

**Profile 342 is the genuine equational variety of Steiner quasigroups**
(at least for the orders we've tested). The 40 extras of profile 382 are
NOT part of the variety; they're accidental small-order satisfactions.

This is the same pattern we saw earlier with Family C: the *minimum* commutative
profile (Family C, size 14) is achieved by both 3×3 commutative magmas and
order-5+ commutative quasigroups, but specific orders have specific extras
that disappear at larger sizes.

## Why we got this wrong initially

The U-3 writeup made the *plausible-sounding* observation that STS(3),
STS(7), STS(9) are all derived from finite-field vector spaces. They are.
But profile-382 status didn't come from that geometric structure — it
came from small order.

The lesson: when 3 small examples (orders 3, 7, 9) share a profile, the
default hypothesis should be **"small-order coincidence"** until disproved,
not "deep structural identity." We failed to apply that discipline in the
first writeup.

## What this means for U-3 conclusions

The U-3 finding "Family C is not a Steiner system" is still correct.
Family C has profile 14, much smaller than the squag variety's profile 342.

The U-3 sub-finding "profile-382-vs-342 = geometric-vs-combinatorial split"
is **retracted**. The split is instead "small-order vs large-order."

The genuine novel observation from U-3 was the **identification of the
40-equation gap** between small-STS and large-STS profiles. That stands as
a Tier-B empirical finding: there IS a clean cardinality jump (382 → 342)
at the order-9-to-13 boundary, but the cause is order-driven coincidences
rather than algebraic origin.

## Where the squag variety actually lives

Per Quackenbush 1976 ("Varieties of Steiner loops and Steiner quasigroups"),
the Steiner quasigroup variety is defined by:
1. commutativity (eq 43)
2. idempotence (eq 8: x = x · x)
3. the Steiner relation: (x · y) · y = x

These three axioms together generate a closure in the ETP catalog. Our
empirical observation: this closure has **at least 342** equations (all
satisfied by every squag of order ≥ 13). Whether it has *exactly* 342
or more (say, additional identities that even our STS(13) and PG(3,2)
satisfy) is open — would require enumerating implications of the three
squag axioms in ETP's implication graph, which is doable but didn't fit
in this session.

**Conjecture (Tier C)**: the implication-closure of {43, 8, [Steiner relation
ETP ID]} in ETP's implication graph is exactly the 342-equation profile.

## Honest closure

The U-3 cross-cutting investigation produced one solid finding and one
retraction:

- **Solid**: Family C is strictly below all classical block-design varieties;
  the squag variety has profile ≥ 342 (with order ≤ 9 squags accidentally
  satisfying 40 extras for profile 382).

- **Retracted**: the conjecture that 382 vs 342 separates geometric STS
  from combinatorial STS. PG(3,2) STS(15) is maximally geometric AND
  profile 342, so geometry isn't the discriminator.

Lesson for the framework: small-order coincidences are common and look
like deep structural identities when only small orders are tested. Always
push to large enough orders to falsify before drawing variety-theoretic
conclusions.

---

*— Claude Code, 2026-05-27. Cross-cutting STS correction.*
