# Cover letter — J07

**Target journal:** *European Journal of Combinatorics*
**Date:** 2026-05-27
**Authors:** B.R. Sanders (corresponding) and M. Gish

---

Dear Editor,

We submit the manuscript *"Spectral Architecture of the σ-Character on Z/10Z: Periodicity, Three-Valued Coherence, the 5-Dimensional Fourier Embedding, and the Symbolic Return Theorem"* for consideration in the *European Journal of Combinatorics*.

The paper studies a specific permutation $\sigma$ on $\mathbb{Z}/10\mathbb{Z}$ with cycle type $(6, 1^4)$ and an associated $\{-1, 0, +1\}$-valued character $\chi$. From this (substrate, σ, χ) triple we prove **five theorems** that together describe the period structure, gate-rate distribution, spectral coherence integral, 5-dimensional CRT Fourier embedding, and the Symbolic Return Theorem:

- **G_6 (Periodicity, Tier-A):** $\sigma^6 = \mathrm{id}$ on all of $\mathbb{Z}/10\mathbb{Z}$.
- **G_7 (Period Distribution, Tier-B):** bimodal $P(\tau=1) = 2/5, P(\tau=6) = 3/5$; mean $\bar{\tau} = 4$, variance $6$.
- **G_8 (Three-Valued Coherence, Tier-B):** $G(s) := |\sum_{j=0}^8 \omega^j \chi(\sigma^j(s))|^2$ takes exactly three values $\{0, 1.871644, 9.389185\}$ with explicit $\sigma^3$-orbit partition and a $\nu_+$ discriminator characterization of the high-locus.
- **Q17-A (5D CRT Fourier Embedding):** a unique $\Phi : \mathbb{Z}/10\mathbb{Z} \hookrightarrow \mathbb{R}^5$ with $D_{10}$ symmetry inheriting from CRT factorization $10 = 2 \cdot 5$.
- **Q17-B (Symbolic Return Theorem, Tier-A):** corollary of G_6 — every cycle returns at step 6 from any non-trivial starting state.

The paper consolidates three formerly-separate working drafts (J50, J51, J52 of our J-series ordering) into a single coherent treatment, with all theorems verified by a 100-line NumPy script (`verify_qseries_merged.py`) that PASSES in ~5 seconds.

**Closest published precedent**: Drápal & Wanless (2021, *JCTA* 184, 105510) study the same neighborhood of small finite commutative non-associative structures at the *opposite* extremum (maximally non-associative); our results lie at a structurally distinct point in the same neighborhood.

**Tier discipline.** All five theorems carry explicit Tier-A or Tier-B labels; the §7 Q17-B Clay-bridge statement is explicitly labeled **structural rhyme, not analogue** to the Riemann Hypothesis — we do not claim any RH-derivation result; the Z.5 deployment-uniformity conjecture is identified as the load-bearing OPEN problem that would convert the rhyme to a derivation.

**Companion paper.** This paper is a consolidation of three earlier working drafts (J50, J51, J52); a related short note on the TSML 8×8 null space and the same RH structural rhyme appears as a companion submission (J02 in our series).

**Conflicts.** No conflicts of interest. No prior publication; the work is original.

**Suggested referees** (with no co-authorship conflict): I. Wanless (Monash), P. Vojtěchovský (Denver), T. Waldhauser (Szeged).

We hope you find the work suitable. We are available for revisions and clarifications.

Best regards,

Brayden R. Sanders (corresponding)
7Site LLC, Hot Springs, Arkansas, USA
brayden@7site.co

M. Gish
Independent Researcher, Hot Springs, Arkansas, USA
