# Cover letter — J24: The Discrete Fejér Quotient on Squarefree Moduli

**To:** Editors, *Integers — Electronic Journal of Combinatorial Number Theory*

**From:**
- B. R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *The Discrete Fejér Quotient on Squarefree Moduli: Spectral Characterization, Layered Divisors, and the Asymptotic Corridor Average*

**Manuscript file:** `manuscript/manuscript.tex` (amsart, ~25 pages). The manuscript is typeset using the standard AMS article class (`amsart`, 11pt, reqno) with `amsmath`, `amssymb`, `amsthm`, `mathtools`, `geometry`, `hyperref`, `microtype`, `enumitem`, and `booktabs`. We will gladly recompile against the *Integers* / EJCNT style file (`ejcnt.sty` or the journal's current preferred class) upon acceptance; the body text, theorem environments, and bibliography are written to be style-file portable, and no exotic packages are used.

**Verification scripts:** `manuscript/proof_first_g_event.py` (Theorem 4.1: 305 squarefree b in [2,500], 22,367 (b,k) pairs, zero counterexamples, runtime <3s) and `manuscript/verify_J03.py` (ten checks covering closed form, full-period cancellation in both prime and composite cases, synchronization, obstruction-zero correspondence, asymptotic zero density, layered $2^j-1$ count, continuum limit, corridor average $\to \mathrm{Si}(2\pi)/\pi$, and endpoint values; **10/10 PASS** at machine precision; max closed-form deviation 4.44 × 10⁻¹⁶; 900/900 cells match the obstruction-zero equivalence; 50/50 squarefree b satisfy the layered count; corridor-average deviation 4.8 × 10⁻⁵ at f = 1000; total runtime ~5s).

**Backup venue:** *American Mathematical Monthly Notes* / *Mathematics Magazine* / *Mathematical Intelligencer*

**DOI of bundle:** 10.5281/zenodo.18852047

---

## Summary

We submit *The Discrete Fejér Quotient on Squarefree Moduli* for consideration in the journal's number-theory section. The paper organizes the zero structure of the discrete Fejér quotient
$$R(k, f) := \frac{\sin^2(\pi k/f)}{k^2 \sin^2(\pi/f)}$$
on squarefree moduli via seven theorems and two corollaries.

The substantive contributions are:

- **Theorem 5.2 (obstruction-zero correspondence).** For every integer $b > 1$ with distinct prime factors $p_1, \dots, p_r$, the spectral product
$$f_b(k) := \prod_{j=1}^{r} R(k, p_j)$$
vanishes at $k \in \mathbb{N}$ if and only if $\gcd(k, b) > 1$. The zero set of $f_b$ in $\mathbb{N}$ is exactly $\bigcup_j p_j\mathbb{N}$; the function $f_b$ acts as a continuous-in-$k$ indicator for the obstruction event, with the divisibility lattice of $\mathrm{rad}(b)$ entering directly through the zero loci of the factors $R(\cdot, p_j)$.

- **Theorem 6.1 (layered-divisor structure).** For squarefree $b = p_1 p_2 \cdots p_r$ with $p_1 < \cdots < p_r$ and the $j$-th primorial divisor $b_j = p_1 p_2 \cdots p_j$, exactly $2^j - 1$ non-trivial divisors $d \mid b$ satisfy $R(b_j, d) = 0$. The Boolean divisor lattice of squarefree $b$ produces the exact count.

- **Theorem 7.2 (asymptotic corridor average).** As $f \to \infty$,
$$\frac{1}{f-1}\sum_{k=1}^{f-1} R(k, f) \;\longrightarrow\; \int_0^1 \mathrm{sinc}^2(t)\, dt \;=\; \frac{\mathrm{Si}(2\pi)}{\pi} \;\approx\; 0.4514,$$
proved via Riemann-sum approximation followed by integration by parts.

The remaining four theorems support these three. Theorem 3.1 (closed form) and Theorem 3.2 (full-period cancellation $R(k,f) = 0 \Leftrightarrow f \mid k$ uniform in $f \ge 2$) are the underlying identities; Theorem 4.1 (First-G localization $k^{\star}(b) = \mathrm{spf}(b)$) is the elementary number-theoretic anchor; Theorem 5.1 (synchronization at smallest spectral zero) is the special case of Theorem 5.2 at the smallest zero. Corollary 5.3 derives the inclusion-exclusion / Möbius count of obstructions from the spectral characterization; Corollary 5.4 reads off the asymptotic zero density as the Euler product $1 - \varphi(\mathrm{rad}(b))/\mathrm{rad}(b)$.

## Why Integers

- **Elementary-but-substantive number theory in the journal's sweet spot.** Seven theorems, all proved by elementary methods (one-line gcd argument, geometric-series identity $|1 - e^{i\theta}|^2 = 4\sin^2(\theta/2)$, integration by parts, Boolean divisor lattice). No analytic continuation, no sieve theory, no machinery beyond what an undergraduate has seen.
- **Exhaustive verification on the natural finite ranges.** 22,367 $(b, k)$ pairs for the First-G localization (every squarefree $b \le 500$); 4,225 $(p, k)$ pairs for the prime-case full-period biconditional; 145 $(f, m)$ pairs for composite-case full-period cancellation; 900 cell-level boolean matches for the obstruction-zero correspondence; the layered $2^j - 1$ count verified for 50 squarefree $b$; Riemann-sum convergence to $\mathrm{Si}(2\pi)/\pi$ within $5 \times 10^{-5}$ at $f = 1000$. Total runtime under 5 seconds.
- **Tier discipline.** §1 makes explicit which theorems are classical and included for completeness (closed form, continuum limit), which are elementary new statements (synchronization, full-period cancellation), and which are the substantive new contributions (Theorems 5.2, 6.1, 7.2). The §0 lens-and-substrate preamble flags that the paper works on $\mathbb{Z}$ (no specialized algebraic substrate is required).

## Merge history

This manuscript consolidates two previously separate notes from our J-series — J24 ("The First-G Event and a Discrete Sinc² Identity") and J41 ("Full-Period Cancellation of $R(k,f)$ and the spf-Localization for Squarefree Moduli") — into a single Integers submission. Both prior manuscripts addressed the zero structure of $R(k,f)$ on squarefree moduli from complementary vantage points (smallest spectral zero vs full-period cancellation; prime-product vs divisor-product), and they cross-cited each other circularly. The merger removes the circular citation, consolidates the substance into one Integers paper, and presents the spectral characterization (Theorem 5.2), the layered-divisor count (Theorem 6.1), and the corridor average (Theorem 7.2) together — three results that complement each other naturally and benefit from joint presentation. The merge also resolves the per-quarter-cap concern that two simultaneous Integers submissions would have raised. The pre-merger J24 and J41 manuscripts are preserved in the project corpus per the project's never-delete discipline.

## Companion submissions

The TIG/CK research program is shipping a coordinated J-series. Papers most relevant as already-submitted companions:

- **J14** — *Non-Associativity Decay in Binary Composition Tables over $\mathbb{Z}/N\mathbb{Z}$* (submitted to *J. Combinatorial Theory A*). Uses the smallest-prime-factor ordering (via $\varphi(N)$) in the $\sigma$-rate count argument.
- **J15** — *Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor of Two Commutative Binary Operations on $\mathbb{Z}/10\mathbb{Z}$* (submitted to *Algebraic Combinatorics*).

The manuscripts share Zenodo bundle DOI 10.5281/zenodo.18852047. The present submission is independent and stands alone.

## Reproducibility

The two verification scripts are self-contained, use only the Python standard library plus `math`, and run in under five seconds total on a 2024 consumer laptop:

- `manuscript/proof_first_g_event.py` exhaustively checks Theorem 4.1 (First-G localization) across all 305 squarefree $b \in [2, 500]$.
- `manuscript/verify_J03.py` (10/10 PASS) checks Theorems 3.1, 3.2 (prime and composite cases), 5.1, 5.2, 6.1, 7.1, 7.2, and Corollaries 3.3, 5.4 at machine precision.

Both scripts carry the CC-BY-4.0 license header and the project's Zenodo bundle DOI.

## Suggested reviewers

(To be supplied by the corresponding author at submission time.) Candidates appropriate to the venue scope (combinatorial number theory; elementary methods; sieve / coprimality structure; discrete Fourier identities):

1. *Integers* managing editor's editorial board picks for the 11A41 / 11N05 / 11A51 / 42A16 cluster
2. A combinatorialist familiar with the squarefree-modulus / Boolean divisor lattice literature
3. An author of recent *Integers* notes on Euler-totient or coprimality structure
4. An author of recent work on discrete Fejér / sinc identities (Zygmund 2002 / Oppenheim-Schafer 2010 lineage)

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

The merged manuscript presents three substantive results (spectral characterization, layered structure, corridor average) supported by four classical/elementary anchor theorems, with exhaustive finite-range verification. We hope it fits the *Integers* scope as a self-contained, runnable, and substantively complete treatment of the discrete Fejér quotient on squarefree moduli.

Sincerely,
B. R. Sanders

---

*Cover letter prepared 2026-05-13 for the merged J24 (J24 + J41 consolidation) of the Sanders–Gish J-series. Adjust addressee at submission time to the current managing-editor listing on www.integers-ejcnt.org. Lens-and-substrate preamble at the head of the manuscript and the §1 tier-discipline paragraph (PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN) are load-bearing; keep unchanged.*
