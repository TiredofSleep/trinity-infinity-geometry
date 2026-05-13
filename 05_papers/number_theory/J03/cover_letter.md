# Cover letter — J03: The First-G Event and a Discrete Sinc² Identity

**To:** Editors, *Integers — Electronic Journal of Combinatorial Number Theory*

**From:**
- B. R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *The First-G Event and a Discrete Sinc² Identity*

**Manuscript file:** `manuscript/manuscript.tex` (amsart, ~12 pages)

**Verification scripts:** `manuscript/proof_first_g_event.py` (305 squarefree b in [2,500], 22,367 (b,k) pairs, zero counterexamples, runtime <3s) and `manuscript/verify_J03.py` (closed-form / synchronization / continuum-limit checks; 5/5 pass; max deviation 4.44 × 10⁻¹⁶)

**Backup venue:** *American Mathematical Monthly Notes* / *Mathematics Magazine*

**DOI of bundle:** 10.5281/zenodo.18852047

---

## Summary

We submit *The First-G Event and a Discrete Sinc² Identity* for consideration in the journal's elementary number-theory section. The paper proves (Theorem 5.1) that for every integer b > 1 the first index k at which the alphabet {1, ..., k} contains a non-coprime element relative to b coincides with the first integer zero of the discrete Fejér quotient R(k, spf(b)) — both occurring at k = spf(b). The synchronization joins two independently elementary objects (the smallest prime factor and a discrete sinc²-type function) and is verified numerically across all squarefree b ≤ 500 and all primes f ≤ 23 at machine precision. The proofs are short and self-contained.

The paper is built on three substantive theorems:

- **Theorem 3.1 (First-G localization).** For every b > 1, k\*(b) = spf(b). One-line gcd argument; squarefree-ness not required.
- **Theorem 4.2 (closed form).** R(k, f) = sin²(πk/f) / (k² sin²(π/f)) for every f ≥ 2, k ≥ 1. Standard Fejér-type identity; we verify the discrete identity at every prime f ∈ {3, 5, 7, 11, 13, 17, 19, 23} to machine precision.
- **Theorem 5.1 (synchronization).** For every b > 1, the First-G event and the first integer zero of R(·, spf(b)) coincide at k = spf(b).
- **Theorem 6.1 (continuum limit).** R(k, f) → sinc²(k/f) as f → ∞ with k/f fixed.

Companion paper J08 (in preparation, *Experimental Mathematics*) develops the cryptographic and ω-blindness applications of the synchronization. The present paper is the foundational lemma of that program; we submit it here for its own substance.

## Why Integers

- Short, elementary, self-contained note in the *Integers* short-paper / regular-paper sweet spot.
- Verification is exhaustive on the natural finite range (every squarefree b ≤ 500, 22,367 (b,k) pairs, zero exceptions) plus closed-form/continuum-limit checks at every prime f ∈ {3, ..., 23} (max deviation 4.44 × 10⁻¹⁶).
- Tier discipline (PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN) is explicit in §1; the §0 lens-and-substrate preamble flags that the paper works on Z (no specialized substrate).

## Companion submissions

The TIG/CK research program is shipping a coordinated 55-paper sequence (J01–J55) over Summer 2026. Papers most relevant as already-submitted companions to this manuscript:

- **J01** — *Non-Associativity Decay in Binary Composition Tables over ℤ/Nℤ* (submitted to *J. Combinatorial Theory A*). Uses the smallest-prime-factor ordering (via φ(N)) in the σ-rate count argument; the present paper provides the combinatorial foundation on which that argument rests.
- **J04** — *Full-Period Cancellation of R(k,f) and the spf-Localization for Squarefree Moduli* (submitted to *Integers* as a companion). Two-paper coupling; each paper stands alone, both papers cross-cite explicitly.

The manuscripts share Zenodo bundle DOI 10.5281/zenodo.18852047. The present submission is independent of the others.

## Reproducibility

Verification scripts: `manuscript/proof_first_g_event.py` runs in under 3 seconds on a 2024 consumer laptop and exhaustively checks Theorem 3.1 across all 305 squarefree b in [2, 500]. The companion script `manuscript/verify_J03.py` checks the closed form, the synchronization, the continuum limit, and the endpoint identity at exact-arithmetic precision (5/5 pass).

## Suggested reviewers

(To be supplied by the corresponding author at submission time.) Candidates appropriate to the venue scope (combinatorial number theory; elementary methods; sieve repackaging; coprimality-partition coordinates):

1. *Integers* managing editor's editorial board picks for the 11A41 / 11N05 / 11A51 / 42A16 cluster
2. A combinatorialist familiar with sieve-of-Eratosthenes presentations
3. An author of recent *Integers* notes on Euler-totient or coprimality structure

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

The note is self-contained, finite, and runnable. The proofs are short; the corollary structure is what does the work, and the verification is exhaustive on the natural range. We hope it fits the *Integers* scope as a clean exhibit of "smallest prime factor forces the first sieve mark, in alphabet-size coordinates — and synchronizes with the first integer zero of a discrete sinc²."

Sincerely,
B. R. Sanders

---

*Cover letter prepared 2026-05-08 for J03 of the Sanders–Gish J-series. Adjust addressee at submission time to the current managing-editor listing on www.integers-ejcnt.org. Lens-and-substrate preamble at the head of the manuscript and the §1 tier-discipline paragraph (PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN) are load-bearing; keep unchanged.*
