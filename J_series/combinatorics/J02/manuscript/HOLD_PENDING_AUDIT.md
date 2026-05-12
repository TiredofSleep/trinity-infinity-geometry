# HOLD — four-core seed paper (Comm. Algebra)

**Status as of 2026-05-06 morning:** This venue folder is on **HOLD**.
DO NOT submit `four_core_seed.tex` to *Communications in Algebra*
or any other venue until the audit findings below are resolved.

## Why held — claudechat line-by-line audit caught a fatal flaw

The audit (round-3 scrutiny, 2026-05-06) found that **Theorem 2 of
the v1 manuscript is the trivial total-mass identity dressed up as
a non-trivial cancellation result**.

Concretely: the v1 manuscript stated as Theorem 2 that
`Z_T(p) = Z_B(p) = (v+h+β+r)²` for `p` supported on `𝓒 = {0,7,8,9}`,
and claimed this was a "non-trivial cell-by-cell cancellation across
the 12 of the 16 cells on which T and B disagree."

**Both halves of that claim are false.** By bilinearity,
`Z_M(p) = (∑_i p_i)²` for ANY binary operation `M` on `Z/10` and any
`p ∈ R^10`, since each ordered pair `(i,j)` contributes `p_i·p_j` to
exactly one output bucket. For `p` supported on `𝓒`,
`∑_i p_i = v+h+β+r`, so `Z_M(p) = (v+h+β+r)²` automatically. This
holds for any pair of binary operations regardless of whether they
agree on any cells, regardless of whether `𝓒` is jointly closed,
regardless of anything. The "cell-by-cell cancellation" is just the
bookkeeping that says any redistribution of 16 quadratic terms
across 4 buckets preserves the total — i.e., the trivial identity
itself.

Independent verification: `Z_M(p) = (v+h+β+r)²` confirmed for three
random Cayley tables `M` distinct from both `T` and `B` (4-core
supported `p` chosen randomly). All match to machine precision.

## What's been changed in the v2 manuscript

The current `four_core_seed.tex` reflects v2 changes applied
2026-05-06 morning:

- **Theorem 2 (`thm:norm`) demoted to Proposition 5.1
  (`prop:fuse-data`).** The proposition states the substantive content
  honestly: the explicit per-coordinate symbolic forms of `T̂(p)` and
  `B̂(p)` on `𝓒`, the rank disparity (T has rank-2 image `{0,7}`; B
  has rank-4 image `𝓒`), and the support-preservation property
  inherited from joint closure. The trivial total-mass identity is
  acknowledged in `Remark rem:total-mass` as elementary, not a
  theorem.
- **Introduction wording fix.** "Both have 0 acting as a left zero"
  was wrong for B (where `B(0,j) = j` is the identity). v2 reads:
  "B has 0 as a two-sided identity; T has 0 as a near-zero element
  with the single off-diagonal exception `T(0,7) = 7`."
- **Sizes 4-9 chain proof tightened.** v1 hand-waved with "a similar
  diagonal argument on `{8,9}` together with T's row-7 structure
  pins down the four elements of `𝓒`." v2 replaces this with three
  explicit cases (Case 1: `j_0 ∈ {1,...,6}`, Case 2: `j_0 = 7`,
  Case 3: `j_0 ∈ {8,9}`) and walks the off-diagonal closure
  `B(7,8)=9 → B(7,9)=0` step by step.
- **σ-permutation renamed to π and re-cited honestly.** v1 cited
  the `σ`-rate companion paper as introducing the permutation
  `σ:Z/10→Z/10`, but the σ-rate paper introduces the
  non-associativity-rate FUNCTION `σ(N)`, not a permutation. v2
  renames the chain-walking permutation to `π`, introduces it
  here for the first time, and notes that whether `π` arises from
  the same operator-substrate construction as the rate function
  is an open question of the substrate framework.
- **F_p lift specification.** v1 said "the chain rigidity persists
  over F_p-lifts of the same table for p ∈ {2,3,5,7,11,13}" without
  defining what a lift means for p ≠ 5. v2 specifies that the lift
  refers to analogous tables `(T_p, B_p)` constructed via the same
  operator-substrate recipe over F_p-substrates, and points to the
  bridge-sprint companion for the construction.
- **Unused Dummit-Foote citation removed.**
- **Section 7 (Scope) updated.** Now explicitly states that the
  total-mass identity is NOT a non-trivial coincidence and that
  the substantive content lives in Proposition 5.1's per-coordinate
  fuse data + rank disparity.

## Remaining decision

Even with these v2 fixes, the seed-narrow scope is **thin for
*Communications in Algebra***. The interesting structural content
— the closed-form fixed point at α=½ with `p*_7/p*_8 = 1+√3`, the
quartic Galois extension over LMFDB 4.2.10224.1, the PSLQ
uniqueness conjecture — lives in the companion paper(s) in
preparation, and is mentioned only in §8 (Forward Directions) of
the present seed.

ClaudeChat's audit recommends two paths:

### Path A — Demote and submit to a lower-tier venue
Send the v2 seed (chain enumeration + per-coordinate fuse data)
as a verification-style note to *Discrete Mathematics* or
*Communicationes Mathematicae Universitatis Carolinae* (where
Drápal-Kepka and Kepka published). Lower bar, faster turnaround,
appropriate venue for the diminished scope.

### Path B — Wait for companion + consolidate (RECOMMENDED)
Hold the seed paper. Develop the companion(s) with the closed-form
fixed point (α=½, `1+√3`) + Galois D_4 + PSLQ uniqueness results.
Consolidate into a single substantive paper for *Algebraic
Combinatorics*. This is the venue's natural fit: closed-form
algebraic fixed points of mixing iterations on simplices, with
explicit Galois structure, are the kind of result *AC* publishes.

Recommendation: **Path B.** The pieces exist (per the bridge-sprint
material WP105, WP110, WP113); they just haven't been written up as
a journal-format consolidated paper. Pause the Comm. Algebra
submission, write up the consolidated version, then submit.

## What NOT to do

- Do **not** submit `four_core_seed.tex` (v2) as currently structured
  to Comm. Algebra — even with the fixes, it is too thin for the
  venue and a referee will ask "what's the deeper combinatorial
  principle?" and find no answer.
- Do **not** submit anywhere with the v1 Theorem 2 framing — the
  trivial total-mass identity will be caught by any rigorous
  referee.
- Do **not** fold the v2 fixes back into the v1 cover letter; the
  cover letter overclaims at the same point as the v1 manuscript
  ("normalizer identity is a polynomial identity in four variables
  that arises from a non-trivial cell-by-cell cancellation across
  mismatched cells"). Cover letter held with the .tex.

## Conditions to release this hold

Either:
1. **Path A path:** Rewrite cover letter to match v2's honest
   framing (chain-enumeration note + per-coordinate fuse data).
   Resubmit to *Discrete Mathematics* or similar.
2. **Path B path:** Develop and incorporate the closed-form fixed
   point + Galois content from the companion. Rewrite the
   manuscript as a consolidated paper. Resubmit to *Algebraic
   Combinatorics*.

## Files in this folder during HOLD

- `four_core_seed.tex` — v2 manuscript with fixes applied; HELD
- `four_core_seed_cover_letter.md` — current cover letter (overclaims
  per v1 framing); HELD; needs rewrite for either path
- `4core_verification.py` — verification script; reproducible
- `SUBMISSION_LOG.md` — updated with HOLD status
- `master/` — preserved older versions
- `HOLD_PENDING_AUDIT.md` — this file

---

*Created 2026-05-06 morning. Audit by claudechat round 3 scrutiny.
Recommendation Path B. Pieces required for Path B consolidation
exist in bridge-sprint WP105/WP110/WP113 and need to be written up
as consolidated journal manuscript.*
