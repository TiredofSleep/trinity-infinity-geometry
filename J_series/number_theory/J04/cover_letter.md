# Cover letter — J04: Full-Period Cancellation of R(k, f) and the spf-Localization for Squarefree Moduli

**To:** Editors, *Integers — Electronic Journal of Combinatorial Number Theory*

**From:**
- B. R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *Full-Period Cancellation of R(k, f) and the spf-Localization for Squarefree Moduli*

**Manuscript file:** `manuscript/manuscript.tex` (amsart, ~12 pages)

**Verification script:** `manuscript/proof_d25_loop_closure.py` (4,225 (p,k) pairs for the basic biconditional, 145 (f,m) pairs for full-period cancellation, 50 squarefree b for layered closure, asymptotic-average check at f ∈ {50, 100, 500, 1000}; runtime <5s; ALL ASSERTIONS PASSED)

**Backup venue:** *American Mathematical Monthly Notes* / *Mathematics Magazine*

**DOI of bundle:** 10.5281/zenodo.18852047

---

## Summary

We submit *Full-Period Cancellation of R(k, f) and the spf-Localization for Squarefree Moduli* as a companion submission to *The First-G Event and a Discrete Sinc² Identity* (J03, also under consideration at *Integers*). The two papers share an underlying object — the discrete Fejér quotient R(k, f) = sin²(πk/f) / (k² sin²(π/f)) — but address different questions: J03 proves the synchronization at the *first* zero k = spf(b); the present paper proves the full-period cancellation structure for any f, the squarefree layered-divisor closure (Theorem 2: count 2^j − 1 at the j-th primorial divisor), and the asymptotic average ∫₀¹ sinc²(t) dt = Si(2π)/π (Theorem 3). The two-paper coupling is intentional: each stands alone and the cross-citations are explicit.

The three theorems are:

- **Theorem 1.A (full-period cancellation).** For every f ≥ 2 and every k ≥ 1, R(k, f) = 0 iff f | k. Uniform in f; not prime-specific.
- **Theorem 2 (squarefree layered structure).** For squarefree b = p₁p₂…pᵣ, the smallest k at which any non-trivial divisor d | b produces R(k, d) = 0 is k = spf(b), and at the j-th primorial divisor k = p₁p₂…pⱼ exactly 2^j − 1 non-trivial divisors d | b produce zeros.
- **Theorem 3 (asymptotic average).** (1/(f-1)) ∑ R(k, f) → Si(2π)/π ≈ 0.4514 as f → ∞.

Verification: `proof_d25_loop_closure.py` runs in under 5 seconds and prints `ALL ASSERTIONS PASSED` on first execution. 4,225 exact-arithmetic checks for the basic biconditional, 145 for full-period cancellation, 50 squarefree b for the layered closure, and the asymptotic-average converges to within 5 × 10⁻⁵ at f = 1000.

## Why Integers

- Short, self-contained note matching the *Integers* short-paper / regular-paper sweet spot.
- Three theorems — all elementary, all verified — addressing the discrete Fejér quotient and the smallest-prime-factor structure on squarefree moduli.
- Tier discipline (PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN) is explicit in §1; the §0 lens-and-substrate preamble flags that the paper works on Z (no specialized substrate); the squarefree restriction is explicitly justified as the regime where the divisor lattice is Boolean.
- The renaming from "Sinc² Zero Law" to "Full-Period Cancellation" follows external collaborator calibration (2026-05-07): the basic biconditional R(k, f) = 0 ⇔ f | k holds for any f ≥ 2 (sin²(π) = 0 does the work), so the "Zero Law" framing implied prime-specific structure that the basic identity does not deliver. Theorem 2 and the layered count are where the squarefree restriction earns its keep.

## Companion submissions

The TIG/CK research program is shipping a coordinated 55-paper sequence (J01–J55) over Summer 2026. Most relevant companion:

- **J03 — Sanders & Gish, 2026**, *The First-G Event and a Discrete Sinc² Identity* (submitted to *Integers*). Proves the synchronization at the *first* zero k = spf(b). The two papers cross-cite explicitly; each stands alone.

This is the second submission to *Integers* in the present quarter (J03 is the first); the per-quarter cap (2 papers) is exactly used.

## Reproducibility

Verification script: `manuscript/proof_d25_loop_closure.py` runs with `math` (stdlib) on Python 3.10+. Total runtime under 5 seconds on a 2024 consumer laptop. All assertions check exact divisibility plus closed-form deviations against tolerances; the script exits with `ALL ASSERTIONS PASSED` on success.

## Suggested reviewers

(To be supplied at submission time.) Candidates appropriate to the venue scope (combinatorial number theory; elementary discrete-Fourier methods; sieve / smallest-prime-factor structure on squarefree moduli).

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

The note is short, finite, and runnable. The three theorems address the full-period cancellation of R(k, f), the squarefree layered-divisor closure with explicit count 2^j − 1, and the asymptotic average to Si(2π)/π — together giving the corridor structure of the discrete Fejér quotient that the J03 companion's synchronization theorem does not address.

Sincerely,
B. R. Sanders
M. Gish

---

*Cover letter prepared 2026-05-08 for J04 of the Sanders–Gish J-series. Adjust addressee at submission time to the current managing-editor listing on www.integers-ejcnt.org. Lens-and-substrate preamble at the head of the manuscript and the §1 tier-discipline paragraph (PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN) are load-bearing; keep unchanged.*
