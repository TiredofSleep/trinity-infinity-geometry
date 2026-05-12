# Cover letter — J20: Mathieu M_22 Substrate-Prime: Order-Factorization Coincidences

**To:** Editors, *American Mathematical Monthly*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *Mathieu M_22 Substrate-Prime: Order-Factorization Coincidences*

---

## Summary

We document a quantitative non-genericity phenomenon between the sporadic Mathieu group M_22 (order 443,520 = 2^7 · 3^2 · 5 · 7 · 11) and a discrete substrate (Z/10Z, σ, W) of independent algebraic interest. The substrate distinguishes the prime set {2, 3, 5, 7, 11} — the same primes (with the same multiplicities) appearing in |M_22|. The paper's main result (Theorem on non-genericity): of M_22's 12 irreducible representations, exactly 10 have dimensions whose only prime factors lie in {2, 3, 5, 7, 11} with at most one factor of 2; equivalently, seven non-trivial irrep dimensions ({21, 45, 45, 55, 99, 231, 385}) factor strictly in {3, 5, 7, 11}, and two more (154 = 2·7·11 and 210 = 2·3·5·7) admit a single factor of 2. The observed concentration 10/12 ≈ 83% contrasts with the null-model density 67/385 ≈ 17.4% of integers in [1, 385] satisfying the same condition; under a uniform null on [1, 385], the concentration occurs with binomial p-value ≈ 1.19 × 10⁻⁶. A short backdrop section presents the standard parameters of the Steiner system S(3, 6, 22) (block count b = 77 = 7·11, replication r = 21 = 3·7, pair-replication λ_2 = 5, block size k = 6) with their substrate-prime decomposition, as the textbook context for the irrep-density observation. We do not claim a derivation of M_22 from the substrate.

## Why American Mathematical Monthly

- Audience fit: the paper is written for the *Monthly* readership. The Mathieu / Steiner content is laid out elementarily; the substrate side is sketched with no sporadic-group background beyond standard undergraduate group theory assumed; the main claim (a quantitative non-genericity result with a clean null-model p-value) is presented as a single section.
- Pedagogical hook: the result is one quantitative statement with a clean binomial-tail computation, not a list of decorative coincidences. A *Monthly* reader can verify every claim from the verification script and Conway-Sloane / ATLAS lookups in a single sitting.
- Length: 4-6 pages in amsart 11pt, suiting the *Monthly*'s expository-note format.

## Revision history

This is a Major-Revision resubmission following an external referee report (2026-05-07). The revision consolidates the previous catalog of six identities into a single non-genericity theorem (with an explicit binomial-tail null-model computation), corrects the previously misstated count (the original "six of twelve factor in {3,5,7,11} alone" was wrong; the correct strict count is seven non-trivial dimensions, with the original list silently omitting 45 with multiplicity 2 and incorrectly including 154 which has a factor of 2), inlines the substrate-prime distinction so each of the five primes is named from intrinsic substrate data, drops the arithmetic-tautology "231 identity," and consolidates the textbook Steiner-system parameters into a single backdrop table.

## Companion submissions

- J02 (*Algebraic Combinatorics*) — Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor of Two Commutative Binary Operations on Z/10Z. Defines the substrate (Z/10Z, σ, W) and its substrate-prime distinction. The present paper depends on J02 only for the algebraic foundations; the non-genericity theorem is verifiable from this paper's §3 plus the binomial-tail computation in §4.

## Reproducibility

Verification: `m22_decomposition.py` (factors each M_22 irrep dimension via `sympy.factorint`, classifies each by membership in the substrate-prime band, enumerates the band on [1, 385], and computes the binomial tail probabilities of the main theorem); `steiner_sigma_hexad.py` (Steiner-system parameters from b = C(v,t)/C(k,t), r = bk/v, λ_i recurrence). All scripts run in under 5 seconds with `numpy` and `sympy` as the only external dependencies. Scripts deposited at https://github.com/TiredofSleep/ck/tree/tig-synthesis (DOI 10.5281/zenodo.18852047).

## Suggested reviewers

- A specialist on the Mathieu groups and their Steiner-system designs (Conway-Sloane / Aschbacher lineage).
- A specialist on Mathieu moonshine (for the open-question footing connecting the present non-genericity to moonshine phenomena).
- A specialist on accessible expository number theory / combinatorics for the *Monthly*.

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

Sincerely,
B.R. Sanders
