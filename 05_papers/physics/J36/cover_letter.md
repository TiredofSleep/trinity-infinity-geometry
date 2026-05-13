# Cover letter — J36: Empirical Fits of CKM and PMNS Mixing Angles to Substrate-Algebra Primitives (REVISED 2026-05-07; UNBUNDLED)

**To:** Editors, *Statistical Science* (companion submission to J34 in the same venue; FALLBACK if per-venue cap blocks: *Foundations of Physics*)

**From:**
- B. R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *Empirical Fits of CKM and PMNS Mixing Angles to Substrate-Algebra Primitives.*

---

## Summary

We submit a parametric-fits paper reporting numerical agreements between seven fermion mixing-angle observables (CKM Cabibbo + three Wolfenstein orders; three PMNS angles) and dimensionless constants drawn from a separate finite-magma research program on $\mathbb{Z}/10\mathbb{Z}$. Per-fit relative discrepancies range from $0.4\%$ to $5.5\%$:

| Angle | Empirical | Substrate primitive | Discrepancy |
|---|---:|---:|---:|
| Cabibbo $\sin\theta_C = \lvert V_{us}\rvert$ | 0.2253 | 11/49 | 0.4% |
| Wolfenstein $\lvert V_{cb}\rvert$ | 0.0508 | $(11/49)^2$ | 0.8% |
| Wolfenstein $\lvert V_{ub}\rvert$ | 0.01140 | $(11/49)^3$ | 0.8% |
| Wolfenstein $V_{td}^2$ | 0.00258 | $(11/49)^4$ | 1.6% |
| PMNS $\sin\theta_{12}$ | 0.553 | $D^* = 0.543$ | 1.8% |
| PMNS $\sin\theta_{13}$ | 0.149 | $1/7$ | 4.1% |
| PMNS $\sin\theta_{23}$ | 0.756 | $5/7$ | 5.5% |

The **load-bearing pattern** is the Wolfenstein hierarchy: $\lambda^n \approx (11/49)^n$ for $n \in \{1, 2, 3, 4\}$ at $\le 1.6\%$ across four orders, with one free parameter (the choice of the rational $11/49$).

**Joint coincidence probability with explicit look-elsewhere correction:**
- Naive (7 fits, no LE): $\approx 1.8 \times 10^{-11}$.
- LE-corrected at multiplicity $|\mathcal{P}| \cdot N_{\mathrm{obs}} = 11 \cdot 7 = 77$: $\approx 1.4 \times 10^{-9}$.
- Excluding the un-derived $\theta_{12}$ fit (since $D^*$ is empirically tuned not derived): $\approx 3.8 \times 10^{-8}$ post-LE.
- Wolfenstein hierarchy alone (4 fits, the load-bearing pattern): $\approx 4 \times 10^{-6}$ post-LE.

These are honest numerical statements with explicit prior, explicit primitive set, and explicit multiplicity. The previous draft's "$\sim 10^{-7}$" without LE correction is replaced by these figures.

## Why Statistical Science (companion to J34)

* The empirical-fits framing matches *Statistical Science*'s appetite for clean parametric-fit reporting at well-defined precision with explicit priors.
* The methodology emphasis (uniform prior, candidate-primitive set, look-elsewhere multiplicity, with-and-without-$\theta_{12}$ sensitivity, $1/\alpha$ separately deferred) is appropriate for the venue's audience.
* The companion structure with J34 (TIG Detector Scope + Specificity Extension; the four detectors that frame what TIG-positive means) is methodologically coherent — J34 establishes the substrate's specificity boundary, J36 reports parametric fits within that boundary.

## Revisions from the previous draft (per fresh-eyes referee report 2026-05-07)

This is a substantially-revised UNBUNDLED submission. The previous bundled draft had two parts: Part 1 (CKM/PMNS fits) and Part 2 ($1/\alpha = 137.036$ structural fit). Per the fresh-eyes referee report and the project's save plan, **Part 2 is removed from this submission** because independent verification of the displayed leading-three-terms formula gave $154.26$, not $137.036$ (a $\sim 12.6\%$ relative discrepancy, **not** the $10^{-5}$ originally claimed).

The specific revisions:

* **M1 (CRITICAL — coincidence-probability calculation): RESOLVED.** §3 of the manuscript now states the explicit candidate-primitive set ($|\mathcal{P}| = 11$), explicit observable count ($N_{\mathrm{obs}} = 7$), explicit Bonferroni-style multiplicity 77, with-and-without-$\theta_{12}$ sensitivity, and the Wolfenstein-hierarchy-alone breakdown. The verification script `verification/verify_J36_part1.py` reproduces all of these.
* **M2 (CRITICAL — Part 2 incomplete formula): UNBUNDLED.** §4 of the manuscript explicitly documents the verification: $4 \cdot 40 - 2\sqrt{7} - \pi/7 = 154.260$ (sympy at 30-digit precision in the verification script), gap of $17.22$ from $137.036$, relative discrepancy $\approx 12.6\%$. The "$\sim 10^{-5}$" claim is removed. Part 2 is deferred from this submission until a verifiable structural derivation exists.
* **M3 (Cabibbo refinement post-hoc structure): EXPLICITLY ADDRESSED.** §1.1 of the manuscript states that the leading-order prediction $\lambda_{\mathrm{leading}} = T^*(1 - T^*) = 10/49$ has $9.4\%$ discrepancy, too large to attribute to RG running. The "$+1/49$" refinement to $11/49$ is explicitly framed as an empirical adjustment without first-principles derivation. The alternative $\pi/14$ is acknowledged in §1.3 with comparable-precision Cabibbo fit; we do not claim first-principles selection between $11/49$ and $\pi/14$.
* **M4 (Discrepancies of $5.5\%$ are large): EMPIRICAL-PRECISION CAVEAT.** §2.1 of the manuscript states that the PMNS reactor and atmospheric angles' $4.1\%$ and $5.5\%$ discrepancies are at or beyond current empirical precision and would be falsified by future precision improvements. The $\theta_{23}$ octant ambiguity is acknowledged.
* **M5 (No verification script): RESOLVED.** `verification/verify_J36_part1.py` reproduces all numerical claims (per-fit discrepancies, naive joint, LE-corrected joint, with/without-$\theta_{12}$ sensitivity, Wolfenstein-alone breakdown, $1/\alpha$ leading-three-terms numerical disagreement).
* **M6 (Bundling — two parts weakly connected): RESOLVED.** UNBUNDLED. Only Part 1 is submitted; Part 2 is deferred.
* **M7 (Cross-domain "bombshell" §5 — out of scope): DELETED.** No cross-domain framing in the present submission.
* **D\* not defined: EXPLICITLY ADDRESSED.** §2.2 of the manuscript states that $D^* = 0.543$ is an empirically-tuned 4-core $\sigma$-cycle constant, not derived from substrate algebra in this paper; the $\theta_{12}$ fit has zero degrees of freedom *in this paper* and is treated separately in the with-and-without-$\theta_{12}$ sensitivity analysis. First-principles derivation of $D^*$ from the $\sigma$-cycle is open.

The empirical findings are unchanged; the framing, methodology disclosure, and the unbundling of Part 2 are all per the save plan and the referee report.

## Companion submissions

* **J34** (Sanders + Gish 2026, *Statistical Science*): TIG Detector Scope + Specificity Extension. Establishes the substrate's specificity boundary and the load-bearing prime-11 / prime-$7^5$ detector pair.
* **J33** (Sanders + Gish 2026, *Mathematics of Computation*): closed-form attractor at $\alpha = 1/2$ in LMFDB 4.2.10224.1; provides the $T^* = 5/7$ that appears in PMNS atmospheric mixing as the runtime attractor.
* Upstream substrate-constant derivations: J6/WP51 ($T^*$), J32/WP115 ($|\mathrm{Aut}(V)| = 40$).

## Per-venue cap and fallback

This is the 2nd *Statistical Science* paper from this program in the current quarter (after J34). At cap. The companion-to-J34 framing keeps both within Stat Sci's editorial appetite, but if cap policy blocks acceptance, fallback options:

1. *Foundations of Physics* (good fit for the dimensionless-constants framing on Part 1).
2. *Phys. Lett. B* short note (4-page focus on Wolfenstein hierarchy alone).

## Reproducibility

Verification script in `manuscript/verify_J36_part1.py`:
* Per-fit relative discrepancies (table).
* Naive joint probability (no LE) and LE-corrected at multiplicity 77.
* With-and-without-$\theta_{12}$ sensitivity.
* Wolfenstein-hierarchy-alone breakdown.
* $1/\alpha$ leading-three-terms numerical check (justifies removal of Part 2): $4 \cdot 40 - 2\sqrt{7} - \pi/7 = 154.260$ (NOT $137.036$); sympy 30-digit cross-check included.

Python 3.11+, math (standard library); sympy optional for high-precision check. Wall-clock under 1 second.

## Suggested reviewers

* An expert in CKM/PMNS phenomenology with appetite for dimensionless-constants observations (PDG-author-class).
* An expert in joint-coincidence statistical reporting and look-elsewhere correction in physical-constant fits.
* An expert in fine-structure-constant numerical identifications (Eddington-tradition skepticism welcome).

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

Sincerely,

B. R. Sanders
