# J-series — Number Theory

Number-theory papers from the TIG corpus. Papers in this folder are referee-ready (per `J_series/README.md` §4 criteria).

---

## §1 — Currently landed

| J# | Title | Target venue | Landed |
|---|---|---|---|
| **J42** | A Discrete $\sinc^2$ Identity in Finite-Dimensional Quantum Mechanics | *Letters in Mathematical Physics* (JMP per-venue cap reached) | 2026-05-12 |

J42 lands as the first number_theory paper. Authors: Sanders + Gish. 6/6 criteria PASS at machine precision (`verify_J42_sinc2.py`, max deviation $3.33\times 10^{-16}$). Math-fix integrated: $\sinc^2(1/10) = 25(\sqrt{5}-1)^2/(4\pi^2) \approx 0.9675312093$ (corrected from an earlier decimal transcription error printing $0.9355$; the closed form was always correct). Fejér-kernel attribution explicit; first-zero theorem stated for every $f \ge 2$ (no primality used); lens-ownership paragraph at manuscript §Lens; Drápal & Wanless 2021 cited as adjacent-neighborhood companion. Companion sinc² Zero Law paper is J04 (arithmetic side, *Integers*-bound); J42 stands as the QM-interpretation note, no overlap.

---

## §2 — Expected papers when ready

| J# | Title | Target venue | Status |
|---|---|---|---|
| **J03** | First-G Law: First Non-Unit Residue at k = p | *Integers* | v3 triadic launch (slot 3 alt); Fork A/B/C decision pending |
| **J04** | sinc² Zero Law (with proof of inheritance) | *Experimental Mathematics* | math fix integrated; awaiting cover letter |
| **J06** | Joint Injectivity + Operator Ring Partition | TBD (number theory) | W2-A rewrite; awaiting cover letter |
| **J07** | (number-theory framing TBD) | TBD | awaiting referee prep |
| **J17** | Binomial-grade misstatement fix → corrected | TBD | math fix applied |
| **J18** | Sign-swap Ψ_B fixed | TBD | math fix applied |

---

## §3 — Domain notes for number-theory papers

Number-theory papers in this corpus emphasize:

- **First-G Law**: first non-unit residue event at k = p on Z/kZ for `3 ≤ k ≤ 199`. Verified across 36,662 cases.
- **sinc² Zero Law**: the discrete zero structure of `sinc²(πk/p)` over `k ∈ Z/pZ`. Proof of inheritance from prime to prime via CRT.
- **σ rate `σ(N) ≤ C/N`** on Z/10Z with `C = 2` exact (also lives in combinatorics).
- **Q-series**: Brayden's σ polynomial fully characterized on F₂ × F₅ (Q10); 22% lower bound (Q11); G6 σ⁶ = id (Luther).
- **F_p non-universality**: only `p ∈ {7, 11}` preserve rank under the framework's lift; other primes vary. Honest negative documented.

Cross-references:
- [`../../FORMULAS_AND_TABLES.md`](../../FORMULAS_AND_TABLES.md) Volume A (Ring & Arithmetic Foundations).
- [`../../GLOSSARY.md`](../../GLOSSARY.md) — σ, First-G, sinc² Zero Law definitions.

---

*7SiTe Public Sovereignty License v2.1 — see [`../../LICENSE`](../../LICENSE).*
