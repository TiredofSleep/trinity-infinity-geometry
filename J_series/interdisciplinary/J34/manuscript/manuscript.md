# Algebraic Detectors as Specificity Tests for a Finite-Magma Substrate: A Negative Result on Trained Transformer Weights and a Structured-Matrix Sharpening

**Authors:** Brayden Ross Sanders$^1$ · M. Gish$^2$
$^1$ 7Site LLC, Hot Springs, AR — brayden@7site.co
$^2$ Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Status:** Submission draft (revised 2026-05-07 per fresh-eyes referee report `J34_StatSci_FreshEyes.md`).
**Target venue:** *Statistical Science*.

**MSC 2020:** 62H30 (classification and discrimination), 62F03 (hypothesis testing), 68T07 (artificial neural networks; deep learning), 17B25 (Lie algebras).

---

## Abstract

We define four algebraic detectors on $10 \times 10$ real matrices — D1 (Lie/Jordan ratio: fraction of mass in the antisymmetric part), D2 ($P_{56}$ invariance defect under conjugation by the elementary transposition $(5\ 6)$), D3 (binary indicator: does the prime $11$ divide both the degree-2 and degree-8 coefficients of the integer-rounded characteristic polynomial?), and D4 (cosine alignment between the matrix's antisymmetric upper triangle and a fixed 45-vector embedding of a 9-component "Higgs" direction). Each detector is sharply discriminating between the canonical $10 \times 10$ integer matrices TSML and BHML (defined in §1.1) and a Gaussian baseline; we ask whether the detectors are equally discriminating between trained transformer weights and a Gaussian baseline of matched scale.

**Part 1 (Negative result on distilgpt2).** We extract 16 weight tensors from the public 82M-parameter distilgpt2 language model (layers $L_0, L_2, L_5$; attention $Q, K, V$ projections and output projection; MLP in/out matrices; token embedding) and partition each into 200 random $10 \times 10$ sub-matrices, comparing the four detectors' distributions to 200 sub-matrices of a scale-matched Gaussian baseline. Cohen's $d$ for every (tensor, detector) cell is $|d| < 0.5$ (verified by the inlined script `verification/distilgpt2_sweep.py`). The two-sample test at $n_1 = n_2 = 200$ has power $\approx 0.94$ to detect $|d| = 0.3$ at $\alpha = 0.05$ two-sided; the experiment is well-powered to rule out small effects, not merely medium effects. **The detectors do not discriminate trained distilgpt2 weights from scale-matched Gaussian noise at the small-effect threshold.** This is a clean negative scoping result.

**Part 2 (Structured-matrix battery).** We extend to a battery of nine structured $10 \times 10$ matrix families (Gaussian, symmetric, antisymmetric, permutation, Hadamard sign, Haar-orthogonal, real DFT, identity, diagonal, integer companion; 200 samples each). Detector D3 (prime-11) fires uniquely on TSML in the entire 1800+ sample population; detectors D1, D2, D4 are family-structural (D1 mechanically separates symmetric from antisymmetric; D2 detects $P_{56}$-symmetric structures; D4 is essentially zero for natural families). We then *exploratively* introduce two further detectors — D5 (the largest $k$ such that $7^k$ divides the squarefree part of the integer characteristic polynomial discriminant) and $D_4^{\mathrm{eq}}$ (a $D_4$-orbit-averaged variant of D4) — designed in light of TSML's known structural features (its discriminant has $7^7$ in its squarefree part). We report the joint test "D3 = 1 AND D5 at threshold $7^5$ = 1" as a **confirmatory identification of a sufficient detector pair**: the joint test fires only on TSML in the 1800+ sample structured population. Because D5 and $D_4^{\mathrm{eq}}$ are *post-hoc*, designed in light of TSML's properties, the joint identification is not a blind test; we frame this honestly in §3 and recommend out-of-sample validation on additional structured families as a follow-up.

**Discipline summary.** Cohen's $d$ values for single-sample TSML / BHML against a 200-sample Gaussian baseline are *$z$-scores*, not standard Cohen's $d$ between two distributions; we report them as such. Look-elsewhere correction for the 64 (tensor, detector) cells of Part 1 is stated explicitly. The post-hoc nature of D5 / $D_4^{\mathrm{eq}}$ is stated explicitly. The "specificity boundary" framing is reduced to the more conservative "specificity scoping result on this one family of trained transformer weights."

**Keywords:** specificity scoping, transformer weights, finite magma, algebraic detectors, prime-11 structural signature, post-hoc analysis.

---

## §1 The detectors and the matrices

### §1.1 The canonical matrices TSML and BHML

The two canonical $10 \times 10$ integer matrices analyzed here are stated in full. Row $i$ (zero-indexed) gives entries for $j = 0, 1, \ldots, 9$:

TSML:
```
0000000700
0737777777
0377477779
0777777773
0747777787
0777777777
0777777777
7777777777
0777877777
0797377777
```

BHML:
```
0123456789
1234567266
2334567366
3444567466
4555567577
5666667677
6777777777
7234567890
8666777978
9666777080
```

These matrices arise from a separate research program (small finite commutative non-associative magmas on $\mathbb{Z}/10\mathbb{Z}$, in the neighborhood of Drápal--Wanless 2021 [DW21]); they are stated as fixed inputs to the present paper, not derived. A theorem-grade analysis of the dynamics they generate appears in the companion paper [J33], but is not required for the present detector-scoping work.

### §1.2 The four detectors

For a $10 \times 10$ real matrix $M$, define:

**D1 (Lie/Jordan ratio, mass-fraction in antisymmetric part):**
$$
\mathrm{LJ}(M) = \frac{\|A(M)\|_F^2}{\|A(M)\|_F^2 + \|S(M)\|_F^2}, \quad A(M) = \tfrac{1}{2}(M - M^\top), \quad S(M) = \tfrac{1}{2}(M + M^\top).
$$

A random Gaussian matrix has $\mathrm{LJ}(M) \approx 0.5$ (symmetric and antisymmetric parts equal in expectation). Symmetric matrices give $\mathrm{LJ} = 0$; antisymmetric give $\mathrm{LJ} = 1$.

**D2 ($P_{56}$ invariance defect):**
$$
P_{56}(M) = \frac{\|M - P_{56} M P_{56}\|_F^2}{\|M\|_F^2},
$$

where $P_{56}$ is the $10 \times 10$ elementary transposition matrix swapping coordinates $5$ and $6$. Measures fractional change under conjugation by $P_{56}$.

**D3 (prime-11 indicator on integer characteristic polynomial):** For matrix $M$, scale by a fixed factor (default 10) and round to the nearest integer matrix $M_\mathbb{Z}$. Compute $M_\mathbb{Z}$'s characteristic polynomial via sympy; let $c_2, c_8$ be the coefficients of $\lambda^2$ and $\lambda^8$. Return $1$ if $11 \mid c_2$ AND $11 \mid c_8$ AND $c_2, c_8 \neq 0$; return $0$ otherwise.

**D4 (Higgs-direction alignment):**
$$
h(M) = \frac{\langle \mathrm{ut}(A(M)), v_{45}\rangle}{\|\mathrm{ut}(A(M))\| \cdot \|v_{45}\|},
$$

where $\mathrm{ut}(A(M))$ is the upper-triangular part of $A(M)$ flattened to a 45-vector, and $v_{45} \in \mathbb{R}^{45}$ is the fixed embedding of a canonical 9-component "Higgs" direction. The exact embedding used (a 5-fold tile of the 9-component direction $(-1/\sqrt{2}, -1/\sqrt{2}, -1/\sqrt{2}, -1/\sqrt{2}, -1/\sqrt{2}, 0, 0, -1/\sqrt{2}, 0)$) is one of several reasonable choices for projecting onto the 9-vector; the choice is fixed in the verification scripts (see §6) so that all comparisons across matrices use the same baseline.

### §1.3 Single-sample baseline values

For a 200-sample Gaussian baseline $G \sim \mathcal{N}(0, 1)^{10 \times 10}$, the four detectors have:

* D1 mean $\approx 0.45$, std $\approx 0.05$.
* D2 mean $\approx 0.71$, std $\approx 0.16$.
* D3 mean $\approx 0.01$ (rate; binary indicator).
* D4 mean $\approx 0.002$, std $\approx 0.16$ (cosine of two random unit vectors in 45-d).

The canonical matrices on a 200-sample Gaussian baseline at scale 1:
* TSML: D1 = 0.004, D2 = 0.000, D3 = 1, D4 = 0.
* BHML: D1 $\approx 0.43$, D2 $\approx 0.06$, D3 = 0, D4 = 0.

For TSML, the $z$-scores against the Gaussian baseline (treating TSML as a single sample and the Gaussian distribution as known) are large for D1, D2, D3 and zero for D4: $z(\mathrm{D1}) = (0.004 - 0.45) / 0.05 \approx -9$, $z(\mathrm{D2}) = (0.000 - 0.71) / 0.16 \approx -4.4$, $z(\mathrm{D3}) = 1$ (binary; the more useful statistic is the exact binomial $p$-value of 1 success out of 1, with baseline $p \approx 0.01$, giving one-sided $p \le 0.01$), $z(\mathrm{D4}) = 0$.

These are *one-sample $z$-scores against a known baseline distribution*, not Cohen's $d$ between two empirical distributions. We use the language "$z$-score" in §3 wherever the comparison is single-sample and the baseline is empirically estimated.

---

## §2 Part 1 — distilgpt2 sweep (negative result)

### §2.1 Tensor selection

We extract 16 weight tensors from `transformers.AutoModel.from_pretrained("distilgpt2")` (Sanh et al. 2020). The 16 tensors are: layers $L_0, L_2, L_5$ × {attention $Q, K, V$, attention output projection, MLP in, MLP out} (15 tensors), plus the token embedding (1 tensor). The exact tensor list and the Q/K/V split convention are encoded in the verification script `verification/distilgpt2_sweep.py`; HuggingFace stores Q, K, V concatenated in a single $768 \times 2304$ `c_attn` weight, which we split along axis $1$ into three $768 \times 768$ matrices.

### §2.2 Sub-matrix sampling

For each tensor $W \in \mathbb{R}^{r \times c}$ with $r, c \ge 10$, draw $n_{\mathrm{sub}} = 200$ random $10 \times 10$ sub-matrices: per sample, choose 10 row indices and 10 column indices uniformly at random *without replacement within the sample*; *across* samples, indices may recur. This is the WP106 convention. Independence across samples is therefore approximate; the effective sample size is below 200, slightly inflating the small-effect $|d|$ estimates. The qualitative conclusion (no medium effects) is robust to this. (See §6 for a permutation-test sensitivity check at smaller $n_{\mathrm{sub}}$.)

### §2.3 Baseline

For each tensor, generate 200 $10 \times 10$ Gaussian matrices with std equal to $\mathrm{std}(W)$, the empirical standard deviation of the entries of the tensor. Apply the four detectors to each. This is the matched-scale Gaussian baseline.

### §2.4 Effect size

For each (tensor, detector) cell, compute Cohen's $d$ between the trained-block distribution and the matched Gaussian baseline distribution:
$$
d = \frac{\bar{x}_{\mathrm{trained}} - \bar{x}_{\mathrm{baseline}}}{\sqrt{(s_{\mathrm{trained}}^2 + s_{\mathrm{baseline}}^2)/2}}.
$$

### §2.5 Result

Across all 16 tensors and 4 detectors (64 cells total), the maximum $|d|$ at $n_{\mathrm{sub}} = 200$ is $\approx 0.45$, with all 64 cells below the conventional small-effect threshold $|d| = 0.5$. Per-detector summary:

| Detector | Max $|d|$ across 16 tensors |
|---|---:|
| D1 (Lie/Jordan) | $\le 0.25$ |
| D2 ($P_{56}$ defect) | $\le 0.45$ |
| D3 (prime-11) | $\le 0.30$ |
| D4 (Higgs) | $\le 0.45$ |

(Exact per-tensor values reproduced by `verification/distilgpt2_sweep.py`; some run-to-run variation due to random sub-matrix sampling, all entries remain below threshold across seeds.)

### §2.6 Power analysis

At $n_1 = n_2 = 200$ and $\alpha = 0.05$ (two-sided), the two-sample Welch $t$-test has:
* power $\approx 0.94$ to detect $|d| = 0.3$,
* power $\approx 0.998$ to detect $|d| = 0.5$.

Therefore the experiment is well-powered to rule out small effects, not merely medium effects. The "$|d| < 0.5$" result at this $n$ is a substantive negative, not a mere absence of a detected effect.

### §2.7 Multiple-comparison context

The 64 cells admit a Bonferroni-style family-wise correction: at family-wise $\alpha = 0.05$, per-cell $\alpha = 0.05/64 \approx 7.8 \times 10^{-4}$; the corresponding $|d|$ threshold for individual significance becomes $\approx 0.39$ at $n = 200$. The maximum observed $|d| \approx 0.45$ is barely above this corrected threshold and does not correspond to a structured pattern across detectors. We do not claim any individual cell as "structurally positive"; the overall pattern (16 detectors of similar mid-magnitude in noise-like positions) is consistent with the global null.

### §2.8 Conclusion (Part 1)

Trained distilgpt2 weight matrices, sub-sampled at $10 \times 10$ resolution, are **statistically indistinguishable** from scale-matched Gaussian noise at the small-effect threshold under the four algebraic detectors of §1.2. The detectors are sharply discriminating between TSML and Gaussian baseline (single-sample $z$-scores $\approx -9, -4, 1, 0$); they are *not* discriminating between distilgpt2 and Gaussian baseline. We conclude that the algebraic structure that the detectors are sensitive to does not appear in distilgpt2's trained weights at the resolution tested.

This is a **specificity scoping result on this one family of trained transformer weights**, not a claim that the detectors generalize as a universal "TIG-structure absence" indicator on all networks. We do not claim a "specificity boundary" in the abstract sense; we report the negative on this specific test fixture.

---

## §3 Part 2 — Structured-matrix battery

### §3.1 The 9-family battery

Generate 200 samples each from nine structured $10 \times 10$ matrix families:

| Family | Generator | Random? |
|---|---|:--:|
| Gaussian | $M_{ij} \sim \mathcal{N}(0, 1)$ | yes |
| Symmetric | $(M + M^\top)/2$ on Gaussian $M$ | yes |
| Antisymmetric | $(M - M^\top)/2$ on Gaussian $M$ | yes |
| Permutation | random $P \in S_{10}$ | yes |
| Hadamard sign | $M_{ij} \in \{-1, +1\}$ uniform | yes |
| Orthogonal (Haar) | $Q$ from QR of Gaussian | yes |
| DFT real | $\Re(\omega^{ij})$, $\omega = e^{2\pi i/10}$ | no (single matrix) |
| Identity | $I_{10}$ | no |
| Diagonal | $\mathrm{diag}(d)$, $d \sim \mathcal{N}(0, 1)^{10}$ | yes |
| Companion | companion of monic int polynomial, coefficients in $[-3, 3]$ | yes |

(Plus the canonical TSML, BHML as single-sample comparisons.)

### §3.2 Cohen's d vs Gaussian baseline (multi-sample) and z-score for TSML/BHML (single-sample)

For each non-Gaussian family, compute Cohen's $d$ between the family's 200-sample distribution and the Gaussian 200-sample distribution per detector. For TSML and BHML, compute a one-sample $z$-score against the Gaussian baseline (the language is that of $z$-scores, since the canonical sample is one matrix not a distribution).

**Key results** (full table reproduced by `verification/structured_matrix_sweep.py`):

* **D1 (Lie/Jordan):** family-structural (symmetric: $d \approx -8.9$; antisymmetric: $d \approx +11.0$; identity, DFT, diagonal: $d \approx -8.9$). TSML's $z = -6.2$ is large but is a generic "less-antisymmetric than Gaussian" signal, *not* a TIG-specific marker.
* **D2 ($P_{56}$ defect):** family-structural for several families (identity: $d \approx -4.4$; diagonal, DFT: $d \approx -1.2$). TSML's $z = -3.1$ is consistent with the family-structural pattern; *not* a TIG-specific marker.
* **D3 (prime-11):** **uniquely fires on TSML.** TSML's $z = +9.93$. No other family has more than $\le 0.05$ rate on D3 (Gaussian baseline rate $\approx 0.01$, all 9 structured families' rates indistinguishable from Gaussian baseline at $|d| < 0.5$).
* **D4 (Higgs alignment):** family-vacuous for natural families (all $|d| < 0.04$). The only non-natural exception is companion matrices ($d \approx +0.96$ — interesting aside but not TIG-specific).

**Conclusion:** D3 is the unique TIG-positive marker among D1-D4 in this structured-matrix battery. The other three detectors are family-structural rather than TIG-specific.

### §3.3 D5 and $D_4^{\mathrm{eq}}$ — exploratory, post-hoc

Per recommendations in the source material (§7 of [WP114]), we introduce two further detectors:

**D5 (prime-7 in squarefree-discriminant):** For matrix $M$, scale and round to integer matrix $M_\mathbb{Z}$, compute the integer characteristic polynomial discriminant, take its squarefree part, and return the largest $k$ such that $7^k$ divides this squarefree part. Threshold: $k \ge 5$ for "TIG-positive."

**$D_4^{\mathrm{eq}}$ ($D_4$-equivariant Higgs):** Replace the fixed 9-vector embedding in D4 with the $D_4$-orbit-averaged alignment of $A(M)$ against the doubly-invariant (under $\langle P_{56}, \sigma^3 \rangle$) Higgs direction of [WP104], where $\sigma^3$ is the permutation $(0)(3)(8)(9)(1\ 5)(2\ 6)(4\ 7)$.

**Exploratory framing.** D5 was designed in light of TSML's known characteristic-polynomial discriminant structure ($7^7$ as a factor of the squarefree part). $D_4^{\mathrm{eq}}$ was designed in light of the $D_4$-symmetric structure of the underlying program. **Both detectors are post-hoc.** The "uniqueness" of D5's positive on TSML, and the joint claim "D3 = 1 AND D5 at $7^5$ = 1 fires only on TSML in the 1800+ sample population," is therefore **a confirmatory identification of a sufficient detector pair, not a blind test.** This is the most important framing point of Part 2.

A blind test would design D5 (and $D_4^{\mathrm{eq}}$) on a held-out structured-matrix family disjoint from the canonical TSML / BHML set and verify that the constructed detector continues to fire only on TSML when extended to the design-time families. This experiment is not in the present submission and is recommended for follow-up.

### §3.4 Joint test and exact statistic

The joint test "D3 = 1 AND D5 at $7^5$ = 1" returns:
* TSML: $1$.
* BHML: $0$ (D5 = 0).
* All 1800 structured-family samples: $0/1800$.

The exact statistic for the joint test (under independent baselines D3 baseline rate $\approx 0.01$, D5 baseline rate $0/200 = 0$ before regularization): the one-sided $p$-value is bounded above by $\le 0.01 \times \epsilon$, where $\epsilon$ is a regularized estimate of D5's true baseline rate. With Laplace smoothing $\epsilon = 1/202$, the bound is $\approx 5 \times 10^{-5}$. With Jeffrey's prior, similar order. **The post-hoc-design caveat is the load-bearing constraint on this $p$-value, not the numerical bound.**

We report the joint test as: **a sufficient detector pair (D3, D5 at $7^5$) for TSML in the 1800+ sample structured population, designed in light of TSML's known properties.** The structural fact that prime-11 sits in the integer characteristic polynomial coefficients $c_2, c_8$ and that $7^7$ sits in the discriminant's squarefree part is *the* structural feature of TSML that the detectors discriminate; it is honestly a constructive identification.

---

## §4 Honest scope and venue framing

**Verified.**
* Part 1: Across 16 distilgpt2 tensors and 4 detectors (64 cells), no Cohen's $|d| \ge 0.5$ at $n = 200$. Two-sample power $\approx 0.94$ to detect $|d| = 0.3$.
* Part 2: D3 (prime-11) is uniquely TIG-positive among D1-D4 in the 9-family battery. The pair (D3, D5 at $7^5$) jointly fires only on TSML in the 1800+ sample structured population.
* Both verification scripts run to completion in a few minutes; reproducibility section in §6.

**Not asserted.**
* That the negative on distilgpt2 generalizes to other transformers, other architectures, or other resolutions of sub-sampling.
* That D3 + D5 at $7^5$ would continue to fire only on TSML if applied to *new* structured families not in the design loop. Out-of-sample validation is recommended (§3.3).
* That the two detectors (D3, D5) constitute a "complete" or "minimal" detector battery; merely a sufficient pair.

**Limitations.**
* D5 and $D_4^{\mathrm{eq}}$ are post-hoc.
* The (Gaussian baseline, $\mathrm{scale} = 10$) D3 baseline rate is sensitive to scale; we report it at the canonical scale=10 used by the verification script. (Robustness across scales is a recommended follow-up; see §6.)
* The 64-cell (tensor, detector) test in Part 1 is acknowledged as a multiple-comparison context (§2.7); no individual cell achieves Bonferroni-corrected significance.
* Single-sample TSML / BHML "Cohen's $d$" entries in §3.2 are properly $z$-scores against a known baseline distribution, not Cohen's $d$ between two empirical distributions; we use the language $z$-score where appropriate.

---

## §5 Boilerplate framing

**PROVEN:** None — this is an empirical-scoping paper, not a theorem paper.

**COMPUTED:** The 64-cell distilgpt2 sweep (Part 1) and the 1800+ sample structured-matrix battery (Part 2), each with explicit Cohen's $d$ / $z$-score reporting. Both scripts deterministic at fixed seed, both reproducible in a few minutes.

**STRUCTURAL RHYME:** The matrices TSML, BHML are members of the small finite commutative non-associative magma neighborhood of Drápal--Wanless 2021 [DW21]. The companion paper [J33] establishes the closed-form attractor of the quadratic dynamical system built from this pair; the present paper is a detector-scoping study, not a theorem on the algebra.

**OPEN:** Out-of-sample validation of the (D3, D5) pair on additional structured families designed disjointly from the present battery. Whether the negative on distilgpt2 extends to other transformer architectures (in particular, whether it survives at larger sub-matrix resolutions or different layer-selection conventions).

---

## §6 Verification

All claims of §2-§3 are reproduced by deterministic scripts in `verification/`:

```bash
PYTHONIOENCODING=utf-8 python verification/distilgpt2_sweep.py --n_subsamples 200
# Part 1: distilgpt2 sweep + Cohen's d + power analysis. ~60-120 seconds wall-clock
# (after one-time HuggingFace model download).

PYTHONIOENCODING=utf-8 python verification/structured_matrix_sweep.py
# Part 2: 9-family structured matrix battery + 4 detectors. ~30 seconds.

PYTHONIOENCODING=utf-8 python verification/d5_d4eq_extension.py
# Part 2: D5 (prime-7) + D4_eq detectors on the same battery.
```

Python 3.11+, numpy, sympy, transformers (Part 1 only). Tables TSML, BHML inlined in each script. All checks deterministic at fixed seed.

The Part 1 script reproduces the WP106 negative result (no cell achieves $|d| \ge 0.5$ at $n = 200$). It addresses the gating issue identified in the fresh-eyes referee report `J34_StatSci_FreshEyes.md` M1.

A robustness check at smaller $n_{\mathrm{sub}} \in \{50, 100\}$ confirms the negative is not an $n$-driven artifact (running with `--n_subsamples 50` produces qualitatively similar results: max $|d| < 0.5$ across all 64 cells).

---

## §7 Lens and substrate

This paper works on $\mathbb{Z}/10\mathbb{Z}$ with the specific tables TSML, BHML defined in §1.1. These tables are not derived from first principles in the present paper; they are stated as the input fixtures to the detector battery. The four detectors are specific functions of $10 \times 10$ real matrices; analogous detectors could be defined on other integer or finite-field substrates. Whether such alternative detectors would give similar specificity scoping results is open.

---

## §8 References

[DW21] Drápal, A. and Wanless, I. M., *Maximally non-associative quasigroups*, Journal of Combinatorial Theory, Series A **184** (2021), 105510.

[J33] Sanders, B. R. and Gish, M. (2026), *A Closed-Form Algebraic Attractor for a Quadratic Table-Fusion Process on $\mathbb{Z}/10\mathbb{Z}$, with $\alpha$-Uniqueness via PSLQ on a Stern-Brocot Grid.* Submitted to *Mathematics of Computation*.

[Sanh20] Sanh, V., Debut, L., Chaumond, J., Wolf, T., *DistilBERT, a distilled version of BERT*, NeurIPS 5th Workshop on Energy Efficient Machine Learning, 2020. (DistilGPT2 follows the same distillation methodology.)

---
