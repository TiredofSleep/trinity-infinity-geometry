# J-series — Number Theory

Number-theory papers from the TIG corpus. Papers in this folder are referee-ready (per `J_series/README.md` §4 criteria).

---

## §1 — Currently landed

| J# | Title | Target venue | Landed |
|---|---|---|---|
| **J42** | A Discrete $\sinc^2$ Identity in Finite-Dimensional Quantum Mechanics | *Letters in Mathematical Physics* (JMP per-venue cap reached) | 2026-05-12 |
| **J04** | Full-Period Cancellation of $R(k, f)$ and the spf-Localization for Squarefree Moduli | *Integers — Electronic Journal of Combinatorial Number Theory* | 2026-05-12 |

J42 lands as the first number_theory paper. Authors: Sanders + Gish. 6/6 criteria PASS at machine precision (`verify_J42_sinc2.py`, max deviation $3.33\times 10^{-16}$). Math-fix integrated: $\sinc^2(1/10) = 25(\sqrt{5}-1)^2/(4\pi^2) \approx 0.9675312093$ (corrected from an earlier decimal transcription error printing $0.9355$; the closed form was always correct). Fejér-kernel attribution explicit; first-zero theorem stated for every $f \ge 2$ (no primality used); lens-ownership paragraph at manuscript §Lens; Drápal & Wanless 2021 cited as adjacent-neighborhood companion. Companion sinc² result paper is J04 (arithmetic side, *Integers*-bound); J42 stands as the QM-interpretation note, no overlap.

J04 lands as the second number_theory paper. Authors: Sanders + Gish. 5/5 verifications PASS at machine precision (`proof_d25_loop_closure.py`, runtime <5s, `ALL ASSERTIONS PASSED`): 4,225 (p, k) pairs for Lemma 1 (basic biconditional, primes 3..199), 145 (f, m) pairs for Theorem 1.A (full-period cancellation), 50 squarefree b for Theorem 2 (layered-divisor closure, exact 2^j − 1 count at the j-th primorial divisor), and Riemann-sum convergence to $\Si(2\pi)/\pi \approx 0.4514$ for Theorem 3 (asymptotic average) at $f \in \{50, 100, 500, 1000\}$. Title renamed 2026-05-07 from "Sinc² Zero Law for Squarefree Moduli" — the basic biconditional $R(k,f) = 0 \iff f \mid k$ is uniform in $f$ (sin²(π) = 0 does the work for any $f \ge 2$); the "Zero Law" framing implied prime-specific structure the basic identity does not deliver. Theorem 2 (squarefree layered closure with explicit count $2^j - 1$) and Theorem 3 (asymptotic-average to $\Si(2\pi)/\pi$) are where the squarefree-modulus restriction and the divisor-lattice argument earn their keep. §0 lens-and-substrate preamble, §1 tier discipline (PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN), Drápal-Wanless 2021 referenced via J02 companion. Companion paper J03 (First-G synchronization, also *Integers*) cross-cited explicitly; per-quarter cap (2 *Integers* papers) exactly used.

---

## §2 — Expected papers when ready

| J# | Title | Target venue | Status |
|---|---|---|---|
| **J03** | First-G Law: First Non-Unit Residue at k = p | *Integers* | v3 triadic launch (slot 3 alt); Fork A/B/C decision pending |
| **J06** | Joint Injectivity + Operator Ring Partition | TBD (number theory) | W2-A rewrite; awaiting cover letter |
| **J07** | (number-theory framing TBD) | TBD | awaiting referee prep |
| **J17** | Binomial-grade misstatement fix → corrected | TBD | math fix applied |
| **J18** | Sign-swap Ψ_B fixed | TBD | math fix applied |

---

## §3 — Domain notes for number-theory papers

Number-theory papers in this corpus emphasize:

- **First-G Law**: first non-unit residue event at k = p on Z/kZ for `3 ≤ k ≤ 199`. Verified across 36,662 cases.
- **Full-period cancellation of R(k, f)**: the discrete Fejér quotient $R(k, f) = \sin^2(\pi k/f)/(k^2 \sin^2(\pi/f))$ vanishes precisely at $f \mid k$ (Theorem 1.A, J04). For squarefree $b = p_1 \cdots p_r$, the smallest non-trivial zero index is $\spf(b) = p_1$ and the j-th primorial divisor produces exactly $2^j - 1$ zero events (Theorem 2, J04). Corridor average tends to $\Si(2\pi)/\pi \approx 0.4514$ (Theorem 3, J04).
- **σ rate `σ(N) ≤ C/N`** on Z/10Z with `C = 2` exact (also lives in combinatorics).
- **Q-series**: Brayden's σ polynomial fully characterized on F₂ × F₅ (Q10); 22% lower bound (Q11); G6 σ⁶ = id (Luther).
- **F_p non-universality**: only `p ∈ {7, 11}` preserve rank under the framework's lift; other primes vary. Honest negative documented.

Cross-references:
- [`../../03_canonical_reference/FORMULAS_AND_TABLES.md`](../../03_canonical_reference/FORMULAS_AND_TABLES.md) Volume A (Ring & Arithmetic Foundations).
- [`../../GLOSSARY.md`](../../GLOSSARY.md) — σ, First-G, sinc² Zero Law definitions.

---

*7SiTe Public Sovereignty License v2.1 — see [`../../LICENSE`](../../LICENSE).*
