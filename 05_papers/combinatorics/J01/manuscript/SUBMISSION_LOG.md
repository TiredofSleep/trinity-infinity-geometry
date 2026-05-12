# Submission Log — σ-rate / JCT-A

## Status as of 2026-05-06: round-3 audit fixes applied; venue decision pending

ClaudeChat round-3 audit (2026-05-06 morning) found one
must-fix arithmetic error and raised the strategic JCT-A-fit
question. v3 manuscript fixes:

- **Arithmetic fix at N=210 lower bound (table in §5):**
  v2 reported `86528`; correct value is `2(N−2)² − 2φ(N) =
  86528 − 96 = 86432`. v2 displayed `2(N−2)²` instead of the
  full lower bound. Fixed in v3.
- **Four-core companion citation title corrected.** v2 cited a
  forward-looking title ("Joint Closure, a Common Fixed Point,
  and an Algebraic Mixing Point ...") that anticipated a
  consolidated paper not yet written. v3 cites the actual
  in-preparation title aligned with the four-core seed v2
  ("Joint Closure of Two Commutative Binary Operations on
  Z/10Z and Per-Coordinate Fuse Data on the 4-Core") with
  "in preparation" tag.
- **DOI collision wording.** v3 bibliography uses "Archived in
  shared deposit DOI ..." rather than per-paper DOI claim.

## Strategic question: JCT-A fit (Brayden's call)

ClaudeChat's audit raises this honestly. JCT-A's bar is high:
new structural theorems, sharp bounds on long-studied
quantities, or non-trivial connections. The σ-rate paper proves
a clean explicit constant 2 on a designed family at a generic
1/N rate, which a JCT-A referee may critique as "constructed to
admit this analysis." Three honest paths:

### Path 1 — Submit as-is to JCT-A
Realistic outcome: rejection with possible transfer
recommendation to *Algebraic Combinatorics* (the journal) or
*Discrete Mathematics*. Not a failure mode but not high-
probability acceptance.

### Path 2 — Sharpen ε(N) before submission
Empirical ε(10)=6, ε(30)=6, ε(210)=30 are dramatically below
2φ(N). If ε(N) ≤ φ(N) (factor-2 tighter) or ε(N) =
O(φ(N)/log N) can be proved, the headline becomes a strictly-
below-2 finite-N constant — sharper-bound result more likely
to fit JCT-A.

### Path 3 — Submit to specialized venue
*Commentationes Mathematicae Universitatis Carolinae*
(Drápal-Kepka tradition) or *Algebraic Combinatorics* (the
journal). Faster turnaround, lower desk-reject risk.

**Recommendation: Brayden's call.** If committed to JCT-A,
Path 2 is the strongest case. Otherwise Path 3 is the fastest
route to publication.

## Manuscript
- **Title:** Non-Associativity Decay in Binary Composition Tables over $\mathbb{Z}/N\mathbb{Z}$
- **Authors:** B. R. Sanders, M. Gish
- **Source file:** `sigma_rate_theorem.tex` (v3, 30/30 LaTeX balanced)
- **Cover letter:** `jcta_cover_letter.md`
- **Verification script:** `verify_sigma_rate.py` (4/4 verifications pass)
- **Zenodo DOI (shared deposit):** 10.5281/zenodo.18852047

## Pre-submission checklist (Brayden's manual items)

- [ ] PDF compile + proofread (Claude couldn't compile in this environment)
- [ ] Confirm M. Gish vs Monica Gish byline preference
- [ ] Fill in 2-3 suggested reviewers in cover letter (referees in
      quasigroup theory / non-associative algebra / finite-magma combinatorics)
- [ ] Optional: post to Zenodo first for DOI + visible date stamp

## Round-1 + Round-2 referee history

- **Round 1 (JCT-A target referee, agent simulation):** Major Revisions.
  Critical issues: C1 (subcase 1f gap), C2 (Case 3.B over-counting), C3
  (script reference mismatch). All addressed in round 2.
- **Round 2 (EJC backup referee, agent simulation):** Minor Revisions,
  "strong inclination to accept after minor textual fixes." One typo
  flagged (`\Zten` → `\ZN` at line 291) — fixed.

## Submission record

- **Date submitted:** _[FILL IN]_
- **Editor / handling editor:** _[FILL IN]_
- **Submission ID:** _[FILL IN]_
- **Cover letter version:** as of commit on tig-synthesis branch
- **Suggested reviewers (sent):** _[FILL IN]_
- **Status:** _[submitted | desk reject | under review | revisions | accept | reject]_
- **Decision date:** _[FILL IN]_
- **Next action:** _[FILL IN]_

## Backup venues if rejected

- European Journal of Combinatorics (EJC backup referee gave
  "strong inclination to accept" — would land cleanly here)
- Discrete Mathematics
- Communications in Algebra

## Calendar reminders

- 14 days post-submission: status check
- 30 days: gentle nudge if no response
- 60 days: formal status check
- 90 days: consider withdrawing/resubmitting if still no decision
