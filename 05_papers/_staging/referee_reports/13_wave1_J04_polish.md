# Wave-1 polish — J04 (σ-magma rigidity, target *Semigroup Forum*)

**Date:** 2026-05-28
**Referee reference:** `02_ship_priority_J03_J04_J06.md` §J04 MINOR issues #1 (§6.1 narrative dilution) + cover-letter `\&` escape bug
**Files touched:**
- `05_papers/algebra/J04/manuscript/manuscript.md` (§6.1 reframe)
- `05_papers/algebra/J04/manuscript/manuscript.tex` (§6.1 reframe + LaTeX `\&` table-cell bugs)
- `05_papers/algebra/J04/cover_letter.md` (`&` → `\&` substitution)

The four theorems (Aut=1, simple, 5 sub-magmas, 2-generated) and their proofs are **untouched**. No new claims introduced; only language tightening.

---

## FIX 1 — §6.1 narrative tightening

The referee finding was that §6.1 opens with "uniquely indecomposable" then unwinds via the $\sigma_{10}^{\min}$ counterexample and "23+ distinct profile-14 families," landing on a "3-idempotents + 5-sub-magmas" refinement that feels ad hoc. The reframe lands §6.1 directly on a refined unicity statement labeled by explicit structural conditions (S1)–(S5), introduces $\sigma_{10}^{\min}$ as the reason the original framing fails for a wider class, and segregates the profile-14 family count as a separate combinatorial datum (relegated to §6.1.3, untouched).

### §6.1 BEFORE-state

**Opening sentence (manuscript.md line 241–243):**

> ### §6.1 Uniqueness conjecture (Tier C, REFUTED in strong form)
>
> We initially conjectured: "the σ-magma is, up to isomorphism, the unique commutative quasigroup of order 10 satisfying all four rigidity conditions." **This conjecture is FALSE in its strong form.**

**Closing sentences (manuscript.md line 262–264):**

> **Refined statement (Tier B, OPEN)**: among commutative quasigroups of order 10 with the σ-like cycle structure (some fixed points + one cycle), the multiset of (# idempotents, # sub-magmas) distinguishes the σ-magma from all other 14-equation members. The σ-magma is the unique such magma with (3 idempotents, 5 sub-magmas).
>
> The full classification of order-10 commutative quasigroups satisfying the 14-equation minimum is an open question for follow-up enumeration.

### §6.1 AFTER-state

**Opening sentences (rewritten):**

> ### §6.1 Refined uniqueness statement
>
> The σ-magma is, up to isomorphism, the unique commutative quasigroup of order 10 satisfying the conjunction of five structural conditions:
>
> > **(S1)** commutativity, **(S2)** quasigroup, **(S3)** identity-free, **(S4)** exactly three idempotents, **(S5)** exactly five sub-magmas (under the convention that the empty set is excluded).
>
> Conditions (S1)–(S5) are independent invariants of the magma. Given them, Theorems A–D … all hold and the σ-magma is the only object — among the commutative order-10 quasigroups we have enumerated — satisfying all five.

The $\sigma_{10}^{\min}$ magma is introduced **as evidence that the earlier "maximally indecomposable" framing was too coarse**, not as a counterexample requiring narrative navigation:

> A natural earlier framing was "the σ-magma is the unique maximally indecomposable commutative quasigroup of order 10," with no further structural conditions. This framing **fails**: the magma $\sigma_{10}^{\min}$ … is a *second* identity-free commutative quasigroup of order 10 with $|\mathrm{Aut}| = 1$, congruence-simple, 2-generated, and a unique non-trivial proper sub-magma $\{4, 9\}$. The two magmas are not isomorphic, and are distinguished precisely by the (S4)/(S5) counts …
>
> Thus the original "maximally indecomposable" wording was too coarse: it picks out a class of at least two magmas at order 10. Conditions (S4) and (S5) are the minimal structural refinements that single out the σ-magma within this class.

The profile-14 family count (the §6.1.3 datum) is acknowledged as a *separate* combinatorial fact, not as the refinement of uniqueness:

> A separate combinatorial datum, recorded for completeness in §6.1.3 below, is that both magmas share the *identical* 14-equation profile in Tao et al.'s Equational Theories Project (ETP); equational invariants alone cannot distinguish them. The discrimination is by sub-magma combinatorics, not by satisfied equations.

**Closing sentence (rewritten — numbered Theorem 6.1):**

> **Theorem 6.1 (Refined unicity).** *Within the class of commutative quasigroups of order 10 satisfying conditions (S1)–(S5) above, the σ-magma of §1.2 is unique up to isomorphism among the magmas we have enumerated. A full classification — proving uniqueness over all commutative order-10 quasigroups satisfying (S1)–(S5), rather than over enumerated candidates — remains open (Tier C).*

The same reframe is applied verbatim to `manuscript.tex` with the `theorem` environment from the document preamble (`\newtheorem{theorem}{Theorem}[section]`), giving the unicity statement a proper Theorem number automatically.

### Honesty discipline preserved

- Four PROVED theorems (A–D) are untouched and their proofs unchanged.
- (S1)–(S5) are *all* either basic invariants (commutative, quasigroup, identity-free) or counting invariants directly proven in §1.2 (idempotent count = 3) and §4 (sub-magma count = 5). No new claim is introduced; the conditions are just renaming-and-bundling existing claims.
- "Unique up to isomorphism among the magmas we have enumerated" stays cautious: no claim that (S1)–(S5) globally characterize the σ-magma over all commutative order-10 quasigroups (that's the open Tier C question).
- The 23+ profile-14 families (§6.1.3) and BHML/CL_STD identity discussion (§6.1.1) are unchanged.

---

## FIX 2 — Cover-letter LaTeX-style `&` escape

The cover letter is markdown but may pass through pandoc/LaTeX-aware renderers. A single unescaped `&` was present.

**`cover_letter.md` line 48 BEFORE:**

> The closest published precedent for the methodology is Drápal & Wanless (2021, *JCTA*) on maximally non-associative quasigroups …

**`cover_letter.md` line 48 AFTER:**

> The closest published precedent for the methodology is Drápal \\& Wanless (2021, *JCTA*) on maximally non-associative quasigroups …

(Other ampersand-free occurrences of "Drápal" already used "&" in the manuscript.tex bibliography but those were already properly escaped as `\&`.) Inline `$...$` math in the cover letter is fine — pandoc/LaTeX both accept the dollar-delimited form in markdown context.

### Bonus: LaTeX `\&` bugs in manuscript.tex tables (caught in scrutiny)

While re-reading manuscript.tex I noticed two table cells using `\&` (literal ampersand) where `&` (column separator) was needed inside the `\begin{array}` environments:

- Line 124 (main 10×10 multiplication table, row 9 — last data row): `9 \& 9 \& 0 \& 7 \& 1 \& 3 \& 2 \& 4 \& 5 \& 6 \& 8` → `9 & 9 & 0 & 7 & 1 & 3 & 2 & 4 & 5 & 6 & 8`
- Line 220 (Z/2 sub-magma table, row 6): `6 \& 6 \& 1` → `6 & 6 & 1`

These were latent compile-fail bugs the referee report didn't catch directly. The bibliography (`McKay … \&`, `Drápal \& Wanless`, `Burris \& Sankappanavar`) uses `\&` correctly as the *escaped literal ampersand* in text mode; only the in-array column separators were wrong.

---

## Summary of files touched

| File | Change | Lines |
|---|---|---|
| `J04/manuscript/manuscript.md` | §6.1 reframe (Theorem 6.1 numbered) | 241–264 |
| `J04/manuscript/manuscript.tex` | §6.1 reframe + 2 `\&` → `&` fixes | 124, 220, 306–335 |
| `J04/cover_letter.md` | `&` → `\&` (Drápal & Wanless) | 48 |

Four theorems unchanged. Verification script (`verify_J59.py`, 4/4 PASS) unchanged. Cover letter substance unchanged.

Ship-readiness: J04 now lands §6.1 on a clean numbered Theorem 6.1, no longer "unwinds." Ready for *Semigroup Forum* arXiv submission pending final pdf compile-check.
