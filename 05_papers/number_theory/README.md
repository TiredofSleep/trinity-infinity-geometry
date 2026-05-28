# J-series — Number Theory

Number-theory papers from the TIG corpus. Papers in this folder are referee-ready (per `J_series/README.md` §4 criteria).

---

## §1 — Currently landed

| J# | Title | Target venue | Landed |
|---|---|---|---|
| **J26** | A Discrete $\sinc^2$ Identity in Finite-Dimensional Quantum Mechanics | *Letters in Mathematical Physics* (JMP per-venue cap reached) | 2026-05-12 |
| **J24** | The Discrete Fejér Quotient on Squarefree Moduli: Spectral Characterization, Layered Divisors, and the Asymptotic Corridor Average (merged J24 + J41) | *Integers — Electronic Journal of Combinatorial Number Theory* | merged 2026-05-13 |
| ~~J41~~ | ~~Full-Period Cancellation of $R(k, f)$ and the spf-Localization for Squarefree Moduli~~ | ~~*Integers*~~ — **merged into J24 on 2026-05-13** (pre-merger files preserved per never-delete at `J41/`) | absorbed 2026-05-13 |

J26 lands as the first number_theory paper. Authors: Sanders + Gish. 6/6 criteria PASS at machine precision (`verify_J42_sinc2.py`, max deviation $3.33\times 10^{-16}$). Math-fix integrated: $\sinc^2(1/10) = 25(\sqrt{5}-1)^2/(4\pi^2) \approx 0.9675312093$ (corrected from an earlier decimal transcription error printing $0.9355$; the closed form was always correct). Fejér-kernel attribution explicit; first-zero theorem stated for every $f \ge 2$ (no primality used); lens-ownership paragraph at manuscript §Lens; Drápal & Wanless 2021 cited as adjacent-neighborhood companion. Companion sinc² result paper is J41 (arithmetic side, *Integers*-bound); J26 stands as the QM-interpretation note, no overlap.

J41 lands as the second number_theory paper. Authors: Sanders + Gish. 5/5 verifications PASS at machine precision (`proof_d25_loop_closure.py`, runtime <5s, `ALL ASSERTIONS PASSED`): 4,225 (p, k) pairs for Lemma 1 (basic biconditional, primes 3..199), 145 (f, m) pairs for Theorem 1.A (full-period cancellation), 50 squarefree b for Theorem 2 (layered-divisor closure, exact 2^j − 1 count at the j-th primorial divisor), and Riemann-sum convergence to $\Si(2\pi)/\pi \approx 0.4514$ for Theorem 3 (asymptotic average) at $f \in \{50, 100, 500, 1000\}$. Title renamed 2026-05-07 from "Sinc² Zero Law for Squarefree Moduli" — the basic biconditional $R(k,f) = 0 \iff f \mid k$ is uniform in $f$ (sin²(π) = 0 does the work for any $f \ge 2$); the "Zero Law" framing implied prime-specific structure the basic identity does not deliver. Theorem 2 (squarefree layered closure with explicit count $2^j - 1$) and Theorem 3 (asymptotic-average to $\Si(2\pi)/\pi$) are where the squarefree-modulus restriction and the divisor-lattice argument earn their keep. §0 lens-and-substrate preamble, §1 tier discipline (PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN), Drápal-Wanless 2021 referenced via J15 companion. Companion paper J24 (First-G synchronization, also *Integers*) cross-cited explicitly; per-quarter cap (2 *Integers* papers) exactly used.

J24 (merged) is the second number_theory paper — consolidates the previously separate J24 and J41 into a single Integers submission on 2026-05-13. Authors: Sanders + Gish. Title: *The Discrete Fejér Quotient on Squarefree Moduli: Spectral Characterization, Layered Divisors, and the Asymptotic Corridor Average*. ~25 pages amsart, 7 theorems + 2 corollaries. Two verification scripts PASS at machine precision: `verify_J03.py` **10/10 PASS** (closed form, full-period cancellation in prime and composite cases, synchronization, obstruction-zero correspondence, asymptotic zero density, layered $2^j-1$ count, continuum limit, corridor average $\to \mathrm{Si}(2\pi)/\pi$, endpoint values; max closed-form deviation 4.44 × 10⁻¹⁶; 900/900 cell-level matches on obstruction-zero; 50/50 squarefree b satisfy the layered count; corridor-average deviation 4.8 × 10⁻⁵ at f = 1000); `proof_first_g_event.py` zero counterexamples across 22,367 (b, k) pairs for 305 squarefree b ∈ [2, 500]. The substantive new contributions, in order: **Theorem 5.2 (obstruction-zero correspondence)** — for every b > 1 with distinct prime factors $p_1, \dots, p_r$, the spectral product $f_b(k) := \prod_{j=1}^r R(k, p_j)$ vanishes at integer $k \ge 1$ iff $\gcd(k, b) > 1$, so the zero set of $f_b$ in $\mathbb{N}$ equals $\bigcup_j p_j\mathbb{N}$ and $f_b$ acts as a continuous-in-$k$ indicator for the obstruction event; **Theorem 6.1 (squarefree layered-divisor structure)** — for squarefree $b = p_1 \cdots p_r$ and the $j$-th primorial divisor $b_j = p_1 \cdots p_j$, exactly $2^j - 1$ non-trivial divisors $d \mid b$ satisfy $R(b_j, d) = 0$; **Theorem 7.2 (corridor average)** — $\frac{1}{f-1}\sum_{k=1}^{f-1} R(k, f) \to \int_0^1 \mathrm{sinc}^2(t)\, dt = \mathrm{Si}(2\pi)/\pi \approx 0.4514$. Supporting theorems retained: 3.1 (closed form), 3.2 (full-period cancellation, uniform in $f \ge 2$), 4.1 (First-G localization), 5.1 (synchronization at smallest spectral zero), 7.1 (continuum limit $\to \mathrm{sinc}^2$); corollaries 3.3 (endpoint values) and 5.4 (asymptotic zero density via the Euler product). The merger resolves the per-quarter cap concern entirely — one Integers submission instead of two — and removes the circular citation between the pre-merger J24 and J41. The pre-merger J41 manuscript and verification scripts are preserved at `05_papers/number_theory/J41/manuscript/` per never-delete; the live submission is the merged J24.

---

## §2 — Expected papers when ready

| J# | Title | Target venue | Status |
|---|---|---|---|
| **J27** | Joint Injectivity + Operator Ring Partition | TBD (number theory) | W2-A rewrite; awaiting cover letter |
| **J33** | (number-theory framing TBD) | TBD | awaiting referee prep |
| **J20** | Binomial-grade misstatement fix → corrected | TBD | math fix applied |
| **J21** | Sign-swap Ψ_B fixed | TBD | math fix applied |

---

## §3 — Domain notes for number-theory papers

Number-theory papers in this corpus emphasize:

- **First-G Law**: first non-unit residue event at k = p on Z/kZ for `3 ≤ k ≤ 199`. Verified across 36,662 cases.
- **Full-period cancellation of R(k, f)**: the discrete Fejér quotient $R(k, f) = \sin^2(\pi k/f)/(k^2 \sin^2(\pi/f))$ vanishes precisely at $f \mid k$ (Theorem 1.A, J41). For squarefree $b = p_1 \cdots p_r$, the smallest non-trivial zero index is $\spf(b) = p_1$ and the j-th primorial divisor produces exactly $2^j - 1$ zero events (Theorem 2, J41). Corridor average tends to $\Si(2\pi)/\pi \approx 0.4514$ (Theorem 3, J41).
- **σ rate `σ(N) ≤ C/N`** on Z/10Z with `C = 2` exact (also lives in combinatorics).
- **Q-series**: Brayden's σ polynomial fully characterized on F₂ × F₅ (Q10); 22% lower bound (Q11); G6 σ⁶ = id (Luther).
- **F_p non-universality**: only `p ∈ {7, 11}` preserve rank under the framework's lift; other primes vary. Honest negative documented.

Cross-references:
- [`../../03_canonical_reference/FORMULAS_AND_TABLES.md`](../../03_canonical_reference/FORMULAS_AND_TABLES.md) Volume A (Ring & Arithmetic Foundations).
- [`../../GLOSSARY.md`](../../GLOSSARY.md) — σ, First-G, sinc² Zero Law definitions.

---

*7SiTe Public Sovereignty License v2.1 — see [`../../LICENSE`](../../LICENSE).*
