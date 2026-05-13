# Cover letter — J03: The First-G Event and a Discrete Sinc² Identity

**To:** Editors, *Integers — Electronic Journal of Combinatorial Number Theory*

**From:**
- B. R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *The First-G Event and a Discrete Sinc² Identity*

**Manuscript file:** `manuscript/manuscript.tex` (amsart, ~12 pages)

**Verification scripts:** `manuscript/proof_first_g_event.py` (305 squarefree b in [2,500], 22,367 (b,k) pairs, zero counterexamples, runtime <3s) and `manuscript/verify_J03.py` (closed-form / synchronization / continuum-limit / **spectral-product obstruction-zero correspondence** / **asymptotic-density** checks; 7/7 pass; max deviation 4.44 × 10⁻¹⁶ for the closed form; 900/900 cells match the boolean equivalence $f_b(k)=0 \Leftrightarrow \gcd(k,b)>1$ for squarefree $b \le 50$ and $k \le 30$)

**Backup venue:** *American Mathematical Monthly Notes* / *Mathematics Magazine*

**DOI of bundle:** 10.5281/zenodo.18852047

---

## Summary

We submit *The First-G Event and a Discrete Sinc² Identity* for consideration in the journal's number-theory section. The paper establishes a **spectral characterization of the obstruction sequence** of an integer b > 1: for every b with distinct prime factors $p_1 < \cdots < p_r$, the product
$$f_b(k) := \prod_{j=1}^{r} R(k, p_j), \qquad R(k,f) := \tfrac{\sin^2(\pi k/f)}{k^2 \sin^2(\pi/f)},$$
of discrete Fejér quotients vanishes at an integer $k \ge 1$ if and only if $\gcd(k, b) > 1$ (Theorem 5.2). The integer zero set of $f_b$ in $\mathbb{N}$ is therefore exactly the union of arithmetic progressions $\bigcup_j p_j\mathbb{N}$ — a single, naturally-defined product spectral function that acts as a continuous-in-$k$ indicator for the obstruction event. The synchronization theorem (5.1, the smallest spectral zero localizes at $\mathrm{spf}(b)$) and the asymptotic density theorem (Corollary 5.4, the spectral zero density equals $1 - \varphi(\mathrm{rad}(b))/\mathrm{rad}(b)$) are the natural corollaries.

The paper's theorems:

- **Theorem 3.1 (First-G localization).** For every b > 1, $k^{\star}(b) = \mathrm{spf}(b)$. One-line gcd argument.
- **Theorem 4.2 (closed form).** $R(k, f) = \sin^2(\pi k/f)/(k^2 \sin^2(\pi/f))$ for every $f \ge 2$, $k \ge 1$. Standard Fejér-type identity; verified at every prime $f \in \{3, 5, 7, 11, 13, 17, 19, 23\}$ to machine precision.
- **Theorem 5.1 (synchronization).** For every $b > 1$, the First-G event and the first integer zero of $R(\cdot, \mathrm{spf}(b))$ coincide at $k = \mathrm{spf}(b)$.
- **Theorem 5.2 (obstruction-zero correspondence).** $f_b(k) = 0$ iff $\gcd(k, b) > 1$. The zero set of $f_b$ in $\mathbb{N}$ equals $\bigcup_{p \mid b} p\mathbb{N}$.
- **Corollary 5.3 (inclusion-exclusion identity).** $|G_k(b)| = \#\{j \le k : f_b(j) = 0\} = -\sum_{d \mid \mathrm{rad}(b),\, d>1} \mu(d) \lfloor k/d \rfloor$.
- **Corollary 5.4 (asymptotic zero density).** $\lim_{K \to \infty} (1/K) \#\{j \le K : f_b(j) = 0\} = 1 - \varphi(\mathrm{rad}(b))/\mathrm{rad}(b)$.
- **Theorem 6.1 (continuum limit).** $R(k, f) \to \mathrm{sinc}^2(k/f)$ as $f \to \infty$ with $k/f$ fixed.

The substantive contribution is the spectral characterization in Theorem 5.2: the divisibility structure of $b$ is encoded in the zero locus of a single naturally-defined product of discrete Fejér quotients, with the synchronization (5.1) the smallest-zero special case and the asymptotic density (5.4) the multiplicative-density corollary. Companion paper J08 (in preparation, *Experimental Mathematics*) develops cryptographic applications of the synchronization side.

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

Verification scripts: `manuscript/proof_first_g_event.py` runs in under 3 seconds on a 2024 consumer laptop and exhaustively checks Theorem 3.1 across all 305 squarefree b in [2, 500]. The companion script `manuscript/verify_J03.py` (7/7 PASS) checks the closed form, the synchronization, the continuum limit, the endpoint identity, **the obstruction-zero correspondence (Theorem 5.2: 900/900 cell-level boolean matches for squarefree b ≤ 50, k ≤ 30)**, and **the asymptotic density (Corollary 5.4: Euler product matches observed density for b up to 2310 over K = 100,000 within 6 × 10⁻⁶)**.

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
