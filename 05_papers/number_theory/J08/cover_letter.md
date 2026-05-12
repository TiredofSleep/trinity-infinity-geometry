# Cover letter — J08: First-Coprime-Failure and the Discrete Fejér Kernel: A Coordinate Translation across Squarefree Bases

**To:** Editors, *Experimental Mathematics*

**From:**
- B. R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *First-Coprime-Failure and the Discrete Fejér Kernel: A Coordinate Translation across Squarefree Bases*

**Manuscript file:** `manuscript/manuscript.tex` (amsart, ~10–12 pages)

**Verification script:** `manuscript/verify_prime_phase_transition.py` (numpy + cmath + math; runtime under three minutes on a 2024 consumer laptop; **712 distinct algebraic checks** across 8 primes, 187 semiprimes, 6 ring structures, 3 continuum-limit witnesses; max error $1.11 \times 10^{-16}$, machine epsilon; zero exceptions).

**DOI of bundle:** 10.5281/zenodo.18852047

---

## Summary

For an integer $b > 1$ with smallest prime factor $p_1 = \mathrm{spf}(b)$, the First-G Localization Lemma of the companion submission J04 (manuscript in preparation, *Integers*) identifies $k = p_1$ as the smallest alphabet size at which the sieve of Eratosthenes marks an element of $\{1, \ldots, k\}$ as non-coprime to $b$. The present note records a companion harmonic identity, the discrete Fejér kernel at rational frequency, and the elementary fact that its first integer zero co-locates with the first-coprime-failure index — a coordinate translation between two reformulations of "smallest positive multiple of $p_1$ is $p_1$."

We record:
- **Lemma 3.1.** The discrete Fejér kernel closed form $R(k, f) = \sin^2(\pi k / f) / (k^2 \sin^2(\pi / f))$ (Fejér 1900; Apostol 1976 §11.5; Iwaniec–Kowalski 2004 §1.7).
- **Theorem 4.1.** Eratosthenes synchronization: the arithmetic gate at $k = p_1$ and the first integer zero of $R(\cdot, p_1)$ at $k = p_1$ are two reformulations of "smallest positive $k$ with $p_1 \mid k$."
- **Corollary 4.2.** $\omega$-blindness: $R(k, 1/p)$ depends only on $k$ and $p$, not on the modulus $b$, once $p \mid b$.
- **Theorem 5.1.** Continuum identification: $R(k, f) \to \sinc^2(k/f)$ as $f \to \infty$ along $k/f \to t$ fixed, with rate $\bigO(1/f^2)$.

The contribution of the paper is the *packaging* (collecting these four facts and identifying the synchronization between the arithmetic sieve and the harmonic kernel) plus the *verification harness* (712 distinct algebraic checks at machine precision, zero exceptions, runtime under three minutes). The closed form (Lemma 3.1) is standard; the synchronization (Theorem 4.1) is a tautology in two coordinate systems; the corollary and continuum identity are standard. We are explicit about this in the abstract and in §0, and we record honestly that the contribution is the packaging plus the harness.

## Why Experimental Mathematics

- **Self-aware tier discipline.** §0 of the manuscript carries a PROVEN/COMPUTED/STRUCTURAL RHYME/OPEN tier paragraph. The Fejér-kernel closed form is recorded as a known lemma, attributed; the synchronization is a coordinate translation, recorded as such; the harness is the computational object.
- **Computational + algebraic clarity.** $712$ distinct checks at machine epsilon, runtime under three minutes; the harness is itself a clean, self-contained Python script (≈200 lines) using only `numpy + cmath + math.gcd`. *Experimental Mathematics* is the right venue for this kind of "exhaustive verification of an elementary identity around a specific arithmetic event" packaging.
- **Honest framing.** The new title ("First-Coprime-Failure and the Discrete Fejér Kernel: A Coordinate Translation across Squarefree Bases") replaces the earlier "Prime Phase Transition" framing, which the fresh-eyes referee correctly noted overclaimed novelty. The Montgomery comparison in §6 is now a one-paragraph remark titled "The constant $4/\pi^2$ in $\sinc^2$ and in Montgomery's pair correlation: a rectangular-window remark" — explicitly recording the common rectangular-window origin and disclaiming the Riemann hypothesis.

## Companion submissions

- **J04 (manuscript in preparation, *Integers*)** — *The First-G Event in the Coprimality Partition*. The foundational localization lemma. The present J08 supplies the harmonic geometry of the approach (the discrete Fejér kernel at rational frequency).
- **The companion four-core paper (manuscript in preparation)** — algebraic substrate work on two specific commutative magmas on $\Z/10\Z$. **Structurally orthogonal** to the present paper, recorded as such in §0 of the J08 manuscript. The two share the broader research program's interest in prime-indexed phase transitions but otherwise stand independently.

## Reproducibility

Verification script: `manuscript/verify_prime_phase_transition.py` runs with `numpy + cmath + math` (Python 3.10+) on a standard laptop. The 712 checks: 106 closed-form $(f, k)$ pairs across 8 primes; 561 pre-collapse and gate evaluations across 187 semiprimes; 42 ring-structure cells for the $\omega$-blindness statement; 3 continuum-limit witnesses. Max error $1.11 \times 10^{-16}$ (machine $\epsilon$); zero exceptions; runtime under three minutes.

The script exhaustively checks all four headline claims and prints a per-claim summary table. It exits 0 if and only if every comparison falls below $10^{-10}$ (well above machine epsilon).

## Suggested reviewers

(To be supplied at submission time.) Candidates appropriate to the venue scope:
1. *Experimental Mathematics* editorial-board picks for the 11A41 / 11N05 / 42A16 cluster.
2. A combinatorialist with experience in discrete-to-continuum identities or discrete-Fejér methods.
3. A computational-number-theorist familiar with exhaustive-search verification frameworks.

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

The note is short, self-contained, and honest about the tier of its claims. The mathematics is correct; the contribution is the packaging plus the verification harness. We hope it fits the *Experimental Mathematics* scope as an exhibit of "Eratosthenes synchronization + 712 algebraic checks at machine precision."

Sincerely,
B. R. Sanders

---

*Cover letter prepared 2026-05-08 for J08 of the Sanders–Gish J-series. Revised to address the J08 fresh-eyes referee report (`Atlas/META_PLAN_2026-05-06/REFEREE_REPORTS/J08_ExpMath_FreshEyes.md`): Theorem 3.1 demoted to Lemma with attribution; Theorem 3.2 reframed as coordinate translation; §5 trimmed to one rectangular-window remark; 712 vs 36,662 reconciled in §0. Title and scope updated accordingly.*
