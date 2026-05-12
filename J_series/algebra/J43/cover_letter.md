# Cover letter — J43: Spectral Layer Consolidation: $G_6$, $G_7$, $G_8$ from the Q-Series Architecture on $\mathbb{Z}/10\mathbb{Z}$

**To:** Editors, *European Journal of Combinatorics*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher

**Date:** 2026-09-06 (Phase 5)

**Manuscript title:** *Spectral Layer Consolidation: $G_6$, $G_7$, $G_8$ from the Q-Series Architecture on $\mathbb{Z}/10\mathbb{Z}$*

---

## Summary

We submit a **consolidation paper** establishing the canonical reference for three spectral / combinatorial results in the TIG framework on $\mathbb{Z}/10\mathbb{Z}$:

* **$G_6$ (Periodicity).** $\sigma^6 = \mathrm{id}$ on all of $\mathbb{Z}/10\mathbb{Z}$. Tier-A, proved by direct verification using the Q9–Q10 $(\alpha, \beta)$ polynomial form.
* **$G_7$ (Period Distribution).** Bimodal: $P(\tau = 1) = 2/5$, $P(\tau = 6) = 3/5$. $\bar{\tau} = 4$, $\sigma_\tau^2 = 6$. Tier-B, forced from $G_6$ + cycle enumeration.
* **$G_8$ (Spectral Coherence Integral).** $G(s) = |\sum_{j=0}^{8} \omega^j \chi(\sigma^j(s))|^2$ takes exactly three values: $0$ at the four anchors $\{0,3,8,9\}$, $G_\mathrm{low} \approx 1.872$ at $\{1, 2, 5, 6\}$, $G_\mathrm{high} \approx 9.389$ at the σ³-coherent pair $\{4, 7\}$. Tier-B, computational verification (`manuscript/verify_G6_G7_G8.py`). The pairing of $G$-values within the $\sigma^3$-orbits $\{1,5\}, \{2,6\}, \{4,7\}$ is a structural consequence of $\sigma^3$ having order 2 on the 6-cycle.

The three results, together, characterize the canonical $\sigma$-permutation completely at the spectral / period level. They form **Layer 4** of the 6-layer Q-series architecture and are foundational citations for the runtime attractor [J33], the Q17-B Clay-bridge essay [J51], the $\sigma$-rate theorem [J01] companion citations, and the WP100s tower's $D_4 = \langle P_{56}, \sigma^3 \rangle$ analysis.

This paper is the **canonical citation reference** for $G_6$, $G_7$, $G_8$ going forward. Prior corpus material (`papers/G6_*`, `G7_*`, `G8_*`) is consolidated here with full proofs.

## Why *European J Combin*

- **Spectral + permutation-group + cyclotomic combinatorics fit.** *EJC* publishes results that combine permutation-group structure ($S_{10}$ orbit analysis), cyclotomic character sums ($\omega = e^{2\pi i/9}$), and finite-substrate enumeration (period distributions on $\mathbb{Z}/10\mathbb{Z}$). All three results sit squarely in this register.
- **Combinatorial-spectral-bridge tradition.** *EJC* has published similar consolidation papers on substrate-level spectral signatures.
- **Audience.** Combinatorialists, finite-group theorists, and cyclotomic-arithmetic specialists.

## Per-venue cap note

This is the **3rd EJC submission** of the J-series program (after J12 Coordinate Coverage and J19 DKAN Two-Coding). Per `J_SERIES_ORDERING.md` §5, the per-venue cap of $\sim 2$/quarter is at risk. **Fallback venues** (in order): *Linear Algebra and its Applications*, *PLOS ONE*. The manuscript is structured so that the consolidation register is venue-agnostic; it can be redirected with minimal modification.

## Companion submissions

This paper is one of the J-series program's **foundation citations** (cited downstream by many later J-papers). Direct companion citations:

- **[J01]** — $\sigma$-rate theorem (JCT-A). Uses $\sigma^6 = \mathrm{id}$.
- **[J05]** — TSML 73 / BHML 28 (Exp Math). Layer 5 reference.
- **[J21]** — Q17-A 5D Force Vector (AMM). Direct citation.
- **[J33]** — Closed-form runtime attractor (Math of Comp). Layer 6 reference.
- **[J51]** — Q17-B Clay Bridge (L'Enseignement Math). Direct citation.
- **[J48]** — 6-DOF Synthesis (Notices AMS). Cross-reference.
- **[J49]** — Microtubule $Q_c = T^*$ (J Theor Biol). Cross-reference (period statistic feeds $T^*$ derivation).

## Reproducibility

Bundled verification: `manuscript/verify_G6_G7_G8.py` (single `python` script using `cmath` only; runtime $<2$ s on a laptop). Confirms:

* $G_6$: $\sigma^6 = \mathrm{id}$ on all 10 elements (direct iteration).
* $G_7$: bimodal period distribution $\{1: 2/5, 6: 3/5\}$ with $\bar\tau = 4$, $\sigma_\tau^2 = 6$.
* $G_8$: corrected three-valued partition: ZERO on $\{0,3,8,9\}$, LOW on $\{1,2,5,6\} \approx 1.872$, HIGH on $\{4,7\} \approx 9.389$.
* $\sigma^3$-pairing: $|G(s)|^2 = |G(\sigma^3(s))|^2$ algebraically (complex amplitudes anti-paired).
* $\nu_+$ discriminator: $\nu_+ \in \{0,2\}$ on $\{4,7\}$ vs $\nu_+ = 1$ on $\{1,2,5,6\}$.

A note on revision: an earlier draft swapped elements 4 and 5 in the partition (claiming HIGH = $\{5, 7\}$). The corrected partition above is what the verification script computes from the manuscript's stated $\sigma$ and $\chi$.

## Suggested reviewers

- A specialist in finite-permutation-group spectral analysis ($S_{10}$ adjacent).
- A combinatorialist with $\mathbb{Z}/N\mathbb{Z}$ orbit-structure or cyclotomic-character-sum experience.
- An algebraist familiar with finite-magma combinatorics and substrate algebras.
- A cyclotomic-arithmetic specialist who can evaluate the $\mathbb{Q}(\zeta_9)$ closed-form (open) question.
- A consolidation / expository referee for spectral combinatorics.

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

Sincerely,
B.R. Sanders
