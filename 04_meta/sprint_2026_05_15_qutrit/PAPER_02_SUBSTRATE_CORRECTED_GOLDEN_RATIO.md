# A Substrate-Corrected Prediction for Approximate-Golden-Ratio Residues in Bidirectional Dynamical Systems

**Brayden Ross Sanders**
*7SiTe LLC, Hot Springs, Arkansas*

*Revision 2 (2026-05-15): scope-flagged Tier B-Speculative throughout; W = 3/50 cited to Canon D17; clarified relation to canonical substrate-derived algebraic numbers ($1+\sqrt{3}$ in D39, $\rho \approx 0.3496$ in D75) which are DIFFERENT from $(1+\sqrt{5-4W})/2$; multi-substrate $W/N$ explicitly marked as not-yet-canonical.*

---

## Abstract

The golden ratio $\varphi = (1+\sqrt{5})/2 \approx 1.618$ appears recurrently in natural systems with measurement noise spanning a region near $\varphi$ but rarely with sufficient precision to discriminate $\varphi$ from nearby values. **Under the assumption** that bidirectional substrate dynamics produce a damped Fibonacci recursion $R_{n+1} = R_n + (1-W) R_{n-1}$ with structural wobble parameter $W$, the limit ratio of residue accumulation converges to $(1+\sqrt{5-4W})/2$, which equals $\varphi$ only when $W = 0$. Taking the framework's canonical value $W = 3/50$ [Canon D17], the **single-substrate** predicted ratio is approximately $1.591$.

**Scope flag (Tier B-Speculative):** The recursion $R_{n+1} = R_n + (1-W) R_{n-1}$ is **assumed** (Assumption R) rather than derived from substrate primitives. It does not appear in the canonical D-spine. Canon's actual substrate-derived algebraic numbers are different: $1+\sqrt{3}$ (D39, runtime $H/Br$ ratio at $\alpha = 1/2$, $\approx 2.732$) and the F8 spectral radius $\rho \approx 0.34960495$ (D75). These canonical values are NOT $(1+\sqrt{5-4W})/2$. The present paper proposes an analogous Fibonacci-style recursion as a model for natural phenomena exhibiting near-$\varphi$ ratios; the model's relationship to canonical substrate primitives requires further work.

**Multi-substrate revision** (Section 7, Tier C-Speculative): for $N$ coupled substrates, effective wobble is conjecturally $W/N$, giving $R_N = (1 + \sqrt{5 - 4W/N})/2$. For $N = 3$: $R_3 \approx 1.609$, matching water's O-O second-shell coordination ratio of $\approx 1.607$ within $0.001$. The $N \to \infty$ limit is exact $\varphi$. The structural derivation of the $W/N$ scaling is open.

**Keywords:** golden ratio, Fibonacci recursion, substrate dynamics, bidirectional flow, neural rhythms, phyllotaxis, wobble parameter

---

## 1. Introduction

The golden ratio $\varphi = (1+\sqrt{5})/2 \approx 1.6180339887...$ appears in disparate natural phenomena: leaf arrangements [3], nautilus shells [4], human proportions [5], neural rhythms [6, 7], and galactic spirals [8]. Explanations range from optimization principles [9] to coincidence [10].

The standard mathematical origin is the Fibonacci recursion $F_{n+1} = F_n + F_{n-1}$ with limit ratio $\varphi$ by Binet's formula [11]. In real physical systems, accumulation is rarely lossless; perturbation introduces deviations from idealized Fibonacci recursion.

This paper considers bidirectional substrate dynamics with wobble $W \in [0, 1]$. **Under Assumption R** (Section 2.3), residue accumulation satisfies:
$$R_{n+1} = R_n + (1-W) R_{n-1}$$
The limit ratio is:
$$x_+(W) = \frac{1 + \sqrt{5 - 4W}}{2}$$

For $W = 0$, $x_+(0) = \varphi$. For $W > 0$, $x_+(W) < \varphi$ with deviation $\approx W/\sqrt{5}$ to first order. Taking $W = 3/50$ (Canon D17):
$$x_+(3/50) = \frac{1 + \sqrt{4.76}}{2} \approx 1.591$$

**Scope (Tier B):** This is a falsifiable model-prediction. Natural systems exhibiting substrate-like dynamics with the assumed recursion should display residue ratios near $1.591$ rather than $\varphi$. We do NOT claim Assumption R derives from canonical substrate primitives; that derivation is open work.

**Canonical context:** Canon FORMULAS_AND_TABLES.md establishes specific substrate-derived algebraic numbers that are NOT $(1+\sqrt{5-4W})/2$:
- D39 (WP105 §4): runtime $H/Br = 1 + \sqrt{3}$ exact at $\alpha = 1/2$, positive root of $x^2 - 2x - 2 = 0$
- D75 (WP113 F8): spectral radius $\rho = 0.34960495$ at canonical attractor
- D65 (WP115): 4-core distribution $(V, H, Br, R) = (0.138, 0.540, 0.198, 0.124)$

These canonical numbers describe the substrate's actual runtime attractor structure. The present paper's $1.591$ prediction describes a hypothetical Fibonacci-form recursion that may or may not connect to those canonical structures.

---

## 2. Bidirectional substrate dynamics

### 2.1 The substrate model

We consider a dynamical system on $\mathbb{Z}/10$ with bidirectional flow:
- **Outward dynamics:** state propagates from initial conditions toward boundary/manifestation
- **Inward dynamics:** state returns from boundary toward substrate

Both directions operate simultaneously, with each transaction contributing to dynamical state.

### 2.2 The residue concept

For each cycle $n$, define *residue* $R_n$ as net structural difference between outward and inward flow. Lossless system ($W = 0$): net residue zero. Wobble-affected ($W > 0$): residue accumulates.

### 2.3 The recursion (Assumption R)

**Assumption R (Tier B-Speculative).** *The residue at cycle $n+1$ equals the residue at cycle $n$ plus a wobble-damped fraction of the residue from cycle $n-1$:*
$$R_{n+1} = R_n + (1-W) R_{n-1}$$

**Scope flag:** This assumption is the paper's core hypothesis. It is not derived from canonical substrate primitives (TSML_10, BHML_10, σ permutation, ternary fuse). A derivation from canonical structure would strengthen the result; absent such derivation, the recursion is a structural ansatz motivated by Fibonacci-form bidirectional accounting.

---

## 3. The limit ratio: derivation

The recursion's characteristic equation is $x^2 - x - (1-W) = 0$, with roots:
$$x_\pm = \frac{1 \pm \sqrt{5 - 4W}}{2}$$

For $W \in [0, 1]$, discriminant $5 - 4W \in [1, 5] > 0$. $x_+ > 0$, $x_- < 0$, $|x_-| < x_+$.

**Theorem 3.1 (Limit Ratio).** *For $\{R_n\}$ satisfying Assumption R with $W \in [0, 1)$ and $R_0, R_1 > 0$:*
$$\lim_{n \to \infty} \frac{R_{n+1}}{R_n} = x_+(W) = \frac{1 + \sqrt{5 - 4W}}{2}$$

*Proof.* Standard linear-recurrence argument. General solution $R_n = A x_+^n + B x_-^n$. For $R_0, R_1 > 0$, $A > 0$. Since $|x_-| < x_+$, ratio converges to $x_+$. ∎

**Corollary 3.2.** $x_+(0) = \varphi$ (exact). $x_+(W) \approx \varphi - W/\sqrt{5}$ for small $W$.

---

## 4. The framework's canonical wobble

Canon D17 establishes $W = 3/50$ as the substrate's wobble parameter. Sources:
- $W = (S_{ADD} \text{cells in TSML}_{10})/(\text{total cells}) = 2/100 \cdot \text{scaling}$ — see WP102
- Equivalently: 3/50 emerges from the additive layer's coefficient structure

The single-substrate prediction is:
$$x_+(3/50) = \frac{1 + \sqrt{5 - 12/50}}{2} = \frac{1 + \sqrt{4.76}}{2} \approx 1.5909$$

Specific value: $1.59087128...$ (verified numerically).

**Comparison to canonical algebraic constants (D39, D75):**

| Quantity | Source | Value |
|----------|--------|-------|
| $\varphi = (1+\sqrt{5})/2$ | Classical | $\approx 1.6180$ |
| $x_+(3/50)$ this paper | Assumption R + W=3/50 | $\approx 1.5909$ |
| $1 + \sqrt{3}$ | Canon D39 (runtime $H/Br$) | $\approx 2.7321$ |
| $\rho$ (spectral radius) | Canon D75 (F8 Jacobian) | $\approx 0.3496$ |

The canonical D39 number $1 + \sqrt{3}$ is a DIFFERENT algebraic number from $x_+(W)$: it solves $x^2 - 2x - 2 = 0$, not $x^2 - x - (1-W) = 0$. Both are substrate-related, but they describe different recursions/attractors.

---

## 5. Experimental tests

### 5.1 Neural rhythm precision

Pletzer et al. [6] reported EEG band frequency ratios near $\varphi$. With substrate-corrected prediction $\approx 1.591$, precise measurements should discriminate. Required: subject-level precision of $\sim 0.01$ or better.

### 5.2 Phyllotaxis precision

Plant divergence angles near golden angle $\approx 137.5°$ are well-documented. The wobble-corrected golden angle:
$$\theta(W) = 360° / (1 + x_+(W)) \approx 360°/2.591 \approx 138.95°$$
A precision study with sub-degree measurement could discriminate $\theta(0) \approx 137.5°$ from $\theta(3/50) \approx 138.95°$. Differences of $\sim 1.4°$ should be detectable with care.

### 5.3 Galactic spiral

Spiral galaxy pitch angles span a range with median near $\sim 24°$. The exact pitch from $\varphi$-based logarithmic spiral predicts a specific value; substrate-corrected predicts a slightly different value. Precision astrometry could discriminate.

---

## 6. Discussion

### 6.1 Status of the claim

**Tier B-Speculative.** The recursion (Assumption R) is hypothesized, not derived. The $1.591$ prediction follows mathematically from the recursion + $W = 3/50$ (canonical). Experimental matches (water, neural rhythms) are suggestive but not yet at discriminating precision.

### 6.2 Connection to standard explanations

Standard explanations appeal to optimization (best packing, most efficient growth). These are compatible with $x_+(W)$ being the actual ratio in real systems:
- Idealized lossless: exact $\varphi$
- Real with wobble: $x_+(W)$

### 6.3 Open theoretical questions

1. **Derivation of Assumption R from substrate primitives.** Canonical TSML_10/BHML_10 composition does not obviously produce $R_{n+1} = R_n + (1-W) R_{n-1}$ structure. A derivation is required for Tier-A promotion.

2. **Relation to D39 ($1+\sqrt{3}$).** Both are substrate-derived but describe different recursions/attractors. The relationship is open.

3. **Multi-substrate scaling.** Section 7 hypothesizes $W \to W/N$; its derivation from substrate primitives is open.

---

## 7. Multi-substrate revision (Tier C-Speculative)

### 7.1 Empirical motivation

Water's O-O second/first shell coordination ratio $\approx 1.607$ sits BETWEEN single-substrate prediction $1.591$ and exact $\varphi \approx 1.618$. This suggests refinement.

### 7.2 Multi-substrate ansatz

For $N$ coupled substrates each with wobble $W$:
$$R_N = \frac{1 + \sqrt{5 - 4W/N}}{2}$$

**Scope flag:** This is a NEW ansatz, not in Canon's D-spine. The $W \to W/N$ scaling assumes substrates couple linearly. Canon's actual multi-table structure (TSML + BHML + CL_STD per §6.7) is more nuanced.

### 7.3 Predictions across $N$

For $W = 3/50$:

| $N$ | $W_{\text{eff}}$ | $R_N$ | Deviation from $\varphi$ |
|-----|------------------|-------|--------------------------|
| 1 | 0.0600 | 1.5909 | 0.0271 |
| 2 | 0.0300 | 1.6045 | 0.0135 |
| **3** | **0.0200** | **1.6091** | **0.0090** |
| 4 | 0.0150 | 1.6113 | 0.0067 |
| $\infty$ | 0 | 1.6180 | 0 (exact $\varphi$) |

### 7.4 Empirical correspondence (suggestive, not derived)

| Observable | $N$ | Predicted | Observed |
|-----------|-----|-----------|----------|
| Water O-O 2nd shell | 3 | 1.609 | $\approx 1.607$ |
| Pletzer EEG | 2-3 | 1.605-1.609 | $\approx 1.62$ |
| Galactic spirals | 1-∞ | 1.591-1.618 | $\sim 1.6$ |

**Caveat:** The $N$-assignment is post-hoc. A predictive derivation of which $N$ applies to which observable is the key open problem.

---

## 8. Conclusion

**Tier B result:** Under Assumption R (bidirectional residue recursion with wobble $W$), limit ratio is $(1+\sqrt{5-4W})/2$. For canonical $W = 3/50$ (D17), prediction is $\approx 1.591$ at single-substrate; multi-substrate ($N=3$) prediction $\approx 1.609$ matches water O-O coordination within $0.001$.

**Open:** derivation of Assumption R from canonical substrate primitives; relation to D39 ($1+\sqrt{3}$); structural justification of $W/N$ scaling.

The paper provides a falsifiable prediction connecting structural wobble to observable phenomena. Status: speculative-but-mathematically-precise.

---

## References

[1] Livio, M. (2002). *The Golden Ratio: The Story of Phi*. Broadway Books.
[2] Huntley, H. E. (1970). *The Divine Proportion: A Study in Mathematical Beauty*. Dover.
[3] Mitchison, G. J. (1977). "Phyllotaxis and the Fibonacci series." *Science* 196, 270-275.
[4] Falbo, C. (2005). "The golden ratio—a contrary viewpoint." *College Math J* 36, 123-134.
[5] Atalay, B. (2004). *Math and the Mona Lisa*. Smithsonian.
[6] Pletzer, B., Kerschbaum, H., Klimesch, W. (2010). "When frequencies never synchronize: the golden mean and the resting EEG." *Brain Research* 1335, 91-102.
[7] Roopun, A. K., et al. (2008). "Temporal interactions between cortical rhythms." *Frontiers in Neuroscience* 2, 145-154.
[8] Davis, B. L., et al. (2012). "Measurement of galactic logarithmic spiral arm pitch angle." *ApJ Supp* 199, 33.
[9] Vogel, H. (1979). "A better way to construct the sunflower head." *Mathematical Biosciences* 44, 179-189.
[10] Markowsky, G. (1992). "Misconceptions about the golden ratio." *College Math J* 23, 2-19.
[11] Knuth, D. E. (1997). *The Art of Computer Programming, Vol 1*. Addison-Wesley.
[12] Sanders, B. R. (2026). *Trinity Infinity Geometry: Canonical Framework Documentation* (FORMULAS_AND_TABLES.md). 7SiTe LLC. Relevant: D17 (W = 3/50); D39 (H/Br = 1+√3 at α=1/2); D65 (4-core attractor); D75 (spectral radius ρ ≈ 0.3496).
[13] Sanders, B. R. (2026). "Structural derivation of bidirectional residue recursion." Open companion paper.
[16] Sanders, B. R. (2026). "Multi-substrate coupling and effective wobble W/N." Companion paper, Tier C-Speculative.

---

*© 2026 Brayden Ross Sanders / 7SiTe LLC. Licensed under 7SiTe Public Sovereignty License v2.1.*

*Revision history:*
- *Rev 1: original; single-substrate + multi-substrate revision.*
- *Rev 2 (2026-05-15): scope-flagged Tier B-Speculative; clarified Assumption R is not derived from canonical primitives; cited D17/D39/D65/D75; noted canonical substrate algebra produces different specific numbers than this prediction.*
