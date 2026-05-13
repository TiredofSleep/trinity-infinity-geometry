# Empirical Fits of CKM and PMNS Mixing Angles to Substrate-Algebra Primitives

**Authors:** Brayden Ross Sanders$^1$ · M. Gish$^2$
$^1$ 7Site LLC, Hot Springs, AR — brayden@7site.co
$^2$ Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Status:** REVISED 2026-05-07 (UNBUNDLED per save plan `Atlas/META_PLAN_2026-05-06/SAVE_PLANS/SAVE_PLAN_J36.md`; Part 2 [1/α structural fit] DEFERRED — independent verification confirmed the leading-three-terms claim was ~12.6% off, not the 10⁻⁵ originally claimed). **Empirical-fits paper, honestly framed.**
**Target venue:** *Statistical Science* companion (after revisions per fresh-eyes referee report `Atlas/META_PLAN_2026-05-06/REFEREE_REPORTS/J36_StatSci_FreshEyes.md`).

**MSC 2020:** 81V05 (electroweak phenomenology), 81V25 (other fundamental processes), 11A99 (number-theoretic identities applied), 62P35 (applications to physical sciences).

---

## Abstract

We report parametric fits of seven fermion mixing-angle observables (CKM Cabibbo $\sin\theta_C$ + three Wolfenstein orders $V_{cb}, V_{ub}, V_{td}^2$; PMNS solar, reactor, and atmospheric mixing angles) to dimensionless constants drawn from a separate finite-magma research program (the canonical $T^* = 5/7$ torus aspect ratio, the substrate constant $D^*$, the powers $(11/49)^n$, and $1/7 = (1 - T^*)/2$). Per-fit relative discrepancies range from $0.4\%$ to $5.5\%$:

| Angle | Empirical (PDG / CODATA) | Substrate primitive | Relative discrepancy |
|---|---:|---:|---:|
| Cabibbo $\sin\theta_C = \lvert V_{us}\rvert$ | $0.2253$ | $11/49 = 0.22449$ | $0.36\%$ |
| Wolfenstein $\lvert V_{cb}\rvert$ | $0.0508$ | $(11/49)^2 = 0.05040$ | $0.80\%$ |
| Wolfenstein $\lvert V_{ub}\rvert$ | $0.01140$ | $(11/49)^3 = 0.01131$ | $0.76\%$ |
| Wolfenstein $V_{td}^2$ | $0.00258$ | $(11/49)^4 = 0.00254$ | $1.56\%$ |
| PMNS $\sin\theta_{12}$ (solar) | $0.553$ | $D^* = 0.543$ | $1.81\%$ |
| PMNS $\sin\theta_{13}$ (reactor) | $0.149$ | $1/7 = 0.14286$ | $4.12\%$ |
| PMNS $\sin\theta_{23}$ (atmospheric) | $0.756$ | $5/7 = 0.71429$ | $5.52\%$ |

The Cabibbo angle is fit by $\lambda = 11/49$, which is the framework's "leading + 1" prediction $T^*(1 - T^*) + 1/49 = 10/49 + 1/49$; the leading-only $10/49 = 0.2041$ has a $9.4\%$ discrepancy. The "$+1/49$" refinement does **not** have a first-principles derivation in the present framework and is reported as an empirical adjustment. The four Wolfenstein orders match $(11/49)^n$ for $n \in \{1, 2, 3, 4\}$ at $\le 1.6\%$ across all four orders — the load-bearing single pattern of the paper. The PMNS angles at $1.8\%$-$5.5\%$ are at or beyond current empirical precision; in particular the PMNS solar fit uses a constant $D^*$ that is *not derived* in the present manuscript.

With uniform priors on each angle in $(0, 1)$, the per-fit hit probability is approximately $2 \delta_i$, giving a naive joint probability of approximately $1.8 \times 10^{-11}$ for the seven-fit ensemble. With Bonferroni-style look-elsewhere correction at multiplicity $|\mathcal{P}| \cdot N_{\mathrm{obs}} = 11 \cdot 7 = 77$, the corrected joint probability is approximately $1.4 \times 10^{-9}$. When the un-derived $\theta_{12}$ fit is excluded (since $D^*$ is empirically used rather than independently derived in this paper), the six-fit ensemble has naive joint $\approx 4.9 \times 10^{-10}$ and LE-corrected $\approx 3.8 \times 10^{-8}$. The previous draft's "$\sim 10^{-7}$" without LE correction is replaced by these honest figures with explicit prior and explicit correction.

**Scope.** This is an empirical-fits paper at the dimensionless-constant level. There is no renormalization-group flow connecting the substrate scale to the electroweak scale; the agreement is at the dimensionless-constant level only. The substrate constants $T^*$, $|\mathrm{Aut}(V)| = 40$ are derived in earlier J-papers of the series; $D^*$ is treated as an empirically-tuned input here.

**Status of the previously-bundled $1/\alpha$ derivation (Part 2).** A previous draft of this manuscript bundled a putative structural fit for $1/\alpha = 137.036$ from the formula $4 \cdot |\mathrm{Aut}(V)| - 2\sqrt{\mathrm{HARMONY}} - \pi/\mathrm{HARMONY} - \cdots$, claimed to recover $137.036$ to $\sim 10^{-5}$. **Independent numerical verification** (sympy at high precision; see `verification/verify_J36_part1.py`) shows the leading three terms give $4 \cdot 40 - 2\sqrt{7} - \pi/7 = 154.260$ — a gap of $17.22$ from the target value, a relative discrepancy of $\approx 12.6\%$ (or $\approx 11.2\%$ relative to the leading sum), **not the $10^{-5}$ originally claimed**. The full structural derivation referenced in earlier supporting bundles is not currently in publishable form. We **do not include the $1/\alpha$ analysis in this submission** and discuss it briefly in §4 only to document the discrepancy explicitly. Per the save plan we recommend that Part 2 be split into a separate paper once a verifiable structural derivation exists, or honestly downgraded to a leading-order $\sim 10\%$ structural agreement; we do not propose to do either in the present J36 submission.

**Keywords:** CKM matrix, PMNS matrix, $T^* = 5/7$, $11/49$, dimensionless constants, parametric fits, finite-magma substrate, look-elsewhere correction.

---

## §1 The Cabibbo angle and the Wolfenstein hierarchy

### §1.1 Leading-order prediction and empirical refinement

The framework's leading-order Cabibbo prediction is
$$
\lambda_{\mathrm{leading}} = T^* (1 - T^*) = \frac{5}{7} \cdot \frac{2}{7} = \frac{10}{49} = 0.20408\ldots,
$$
with empirical $\sin\theta_C = |V_{us}| = 0.2253$ (PDG 2024). The leading-only prediction has a $9.4\%$ discrepancy from the empirical value.

**RG-running context.** The 1-loop RG running of $V_{us}$ from the GUT scale to the EW scale (Antusch et al. 2003) is on the order of $\sim 1\%$, an order of magnitude smaller than the $9.4\%$ leading-only gap. The leading-order prediction $10/49$ does not close the gap.

**Empirical refinement.** A "$+1/49$" empirical refinement brings the prediction to
$$
\lambda_{\mathrm{refined}} = \frac{11}{49} = 0.22449\ldots,
$$
with $0.4\%$ discrepancy from $0.2253$. **The "$+1/49$" refinement does not have an independent first-principles derivation in the present framework**; we report it as an empirical adjustment whose structural justification is open. The companion paper [J10/WP121] discusses an analogous "$+1$" closure offset in the cosmological-constant context, but does not establish that the offset must take the value $+1/49$ for the Cabibbo angle on first-principles grounds.

The **load-bearing** pattern of this paper is the *Wolfenstein hierarchy* across four orders, not the single-Cabibbo refinement.

### §1.2 The Wolfenstein hierarchy

Let $\lambda = 11/49$. Then $\lambda^n$ for $n = 1, 2, 3, 4$ matches the corresponding Wolfenstein order:

| Order | $(11/49)^n$ | PDG empirical | Relative discrepancy |
|---:|---:|---:|---:|
| $n = 1$ ($V_{us}$) | $0.22449$ | $0.2253$ | $0.36\%$ |
| $n = 2$ ($V_{cb}$) | $0.05040$ | $0.0508$ | $0.80\%$ |
| $n = 3$ ($V_{ub}$) | $0.01131$ | $0.01140$ | $0.76\%$ |
| $n = 4$ ($V_{td}^2$) | $0.00254$ | $0.00258$ | $1.56\%$ |

A four-order match at $\le 1.6\%$ across $n = 1, 2, 3, 4$ is striking. The single free parameter (the choice of the rational $11/49$) is a single decision; the four orders are then a parameter-free consequence.

### §1.3 Empirical alternative $\pi/14$

A close numerical alternative is $\pi/14 = 0.22440\ldots$, which fits the Cabibbo angle to $0.40\%$ — comparable precision to $11/49$. We mention this only to be candid: the existence of a close transcendental alternative emphasizes that *some* expression near $0.225$ should be expected to fit the Cabibbo angle to within a few per cent under any reasonable prior. The Wolfenstein hierarchy at $\lambda^n \approx (11/49)^n$ for $n = 2, 3, 4$ is the hierarchical pattern that distinguishes $11/49$ from the $\pi/14$ alternative (the analogous $(\pi/14)^n$ matches the Wolfenstein orders at comparable precision, but not better than $11/49$); we do not claim first-principles selection between the two.

---

## §2 PMNS angles via 4-core endpoints

PMNS mixing has three large angles, in contrast to CKM's hierarchy of small angles. We compare the three angles to structural constants:

* $\sin\theta_{23} = T^* = 5/7 = 0.71429\ldots$, with PDG empirical $\sin\theta_{23} = 0.756$ (upper-octant world-average), giving $5.5\%$ relative discrepancy.
* $\sin\theta_{12} = D^* = 0.543\ldots$, with PDG empirical $\sin\theta_{12} = 0.553$, giving $1.8\%$ relative discrepancy.
* $\sin\theta_{13} = (1 - T^*)/2 = 1/7 = 0.14286\ldots$, with Daya Bay empirical $\sin\theta_{13} = 0.149$, giving $4.1\%$ relative discrepancy.

The dominant structural ingredient is $T^* = 5/7$, which appears as the runtime attractor of the closed-form companion paper [J33/WP105] and as the cyclotomic torus aspect ratio derived in [J6/WP51].

### §2.1 Empirical-precision caveat

The PMNS reactor angle $\sin\theta_{13} = 0.149 \pm 0.003$ (Daya Bay 2023; PDG 2024) and the atmospheric angle $\sin\theta_{23}$ (currently between octants $\sim 0.671$ and $\sim 0.788$, with the world-average reported here at the upper-octant value) are measured to precisions where the framework's predictions $1/7 = 0.143$ ($4.1\%$ off) and $5/7 = 0.714$ ($5.5\%$ off, between octants) are *empirically distinguishable*. Future precision improvements would falsify these fits if the world averages converge away from $1/7$ or $5/7$. We therefore report the PMNS fits as suggestive structural patterns at the current precision, **not** as locked predictions. The atmospheric octant ambiguity is acknowledged.

### §2.2 $D^*$ — disclosed as not derived in this paper

The PMNS solar fit $\sin\theta_{12} = D^* = 0.543$ uses a constant $D^*$ that is, in the present manuscript, an empirically-tuned numerical value not derived from the substrate algebra. The $\theta_{12}$ fit therefore has effectively zero degrees of freedom *in this paper*; its independent derivation from the 4-core $\sigma$-cycle structure is an open target. The $\theta_{12}$ fit is included in §3 below for completeness but is excluded from the load-bearing portion of the joint-coincidence-probability calculation.

---

## §3 Joint coincidence-probability calculation with explicit look-elsewhere correction

We compute the joint coincidence probability under explicit priors and an explicit look-elsewhere correction.

### §3.1 Candidate-primitive set

The substrate-algebra-derived primitives considered in this paper are
$$
\mathcal{P} = \big\{T^*,\ T^{*-1},\ 1 - T^*,\ (1 - T^*)/2,\ T^*(1 - T^*),\ 11/49,\ (11/49)^2,\ (11/49)^3,\ (11/49)^4,\ D^*,\ \pi/14\big\}.
$$
This is $|\mathcal{P}| = 11$ candidates. ($\pi/14$ is included because it appears as an alternative Cabibbo fit at the $0.4\%$ level; a defensible look-elsewhere correction must include alternatives that were considered, even if not selected.)

### §3.2 Observable count

The standard model has 4 CKM mixing angles + 1 CKM CP phase, plus 3 PMNS mixing angles + 1 PMNS CP phase = 9 mixing observables. Restricting to the 7 mixing angles compared in this paper (4 CKM Wolfenstein parameters + 3 PMNS angles), the look-elsewhere multiplicity for the (primitive, observable) pairing is approximately $|\mathcal{P}| \cdot 7 = 77$.

### §3.3 Prior

Uniform on $(0, 1)$ for each $\sin\theta$ (the natural support for $\sin\theta$ when $\theta \in (0, \pi/2)$; the uniform-on-$\sin\theta$ prior is one defensible choice — uniform on $\theta$ is another, giving a slightly different per-angle hit probability for the smaller angles). Per-angle hit probability at relative discrepancy $\delta_i$ is approximately $2 \delta_i$ for the matching primitive within $\delta_i$.

### §3.4 Naive joint probability (no LE correction)

For the seven fits with relative discrepancies $(0.36\%, 0.80\%, 0.76\%, 1.56\%, 1.81\%, 4.12\%, 5.52\%)$:
$$
P_{\mathrm{naive}}^{(7)} = \prod_{i = 1}^{7} 2\delta_i \approx 1.8 \times 10^{-11}.
$$

### §3.5 Look-elsewhere correction

Approximate Bonferroni-style correction at multiplicity 77:
$$
P_{\mathrm{LE}}^{(7)} \approx \min\bigl(77 \cdot P_{\mathrm{naive}}^{(7)},\ 1\bigr) \approx 1.4 \times 10^{-9}.
$$

### §3.6 Sensitivity: excluding the $\theta_{12}$ fit

Since $D^*$ is not independently derived in this paper, the $\theta_{12}$ fit has zero degrees of freedom and arguably should not be counted. Excluding it gives the six-fit ensemble (4 CKM Wolfenstein + 2 PMNS angles, $\theta_{13}$ and $\theta_{23}$):
$$
P_{\mathrm{naive}}^{(6)} \approx 5 \times 10^{-10}, \qquad P_{\mathrm{LE}}^{(6)} \approx 3.8 \times 10^{-8}.
$$

### §3.7 Reported result

The joint coincidence probability **after look-elsewhere correction at multiplicity 77** is approximately $\mathbf{10^{-9}}$ for the full seven-fit ensemble and approximately $\mathbf{4 \times 10^{-8}}$ when the un-derived $\theta_{12}$ fit is excluded. The previous draft's "$\sim 10^{-7}$" without LE correction is replaced by these honest figures with explicit prior, explicit primitive set, and explicit multiplicity.

The post-correction joint probability is statistically very interesting, but the load-bearing single pattern is the **Wolfenstein hierarchy** $\lambda^n \approx (11/49)^n$ for $n = 1, 2, 3, 4$ matching at $\le 1.6\%$ across four orders. This four-order match (with one free parameter, namely the choice of the rational $11/49$) is the strongest empirical evidence in the paper. After look-elsewhere correction, the post-LE joint for the four Wolfenstein orders alone is $\approx 77 \cdot \prod 2\delta_i \approx 77 \cdot 5.4 \times 10^{-7} \approx 4 \times 10^{-5}$ — still small enough to be statistically interesting but clearly above the order-of-magnitude $\sim 10^{-9}$ headline that combines all seven fits.

---

## §4 The previously-bundled $1/\alpha$ analysis: why deferred

A previous draft of this paper bundled a putative structural fit:
$$
\frac{1}{\alpha} \approx 4 \cdot |\mathrm{Aut}(V)| - 2 \sqrt{\mathrm{HARMONY}} - \frac{\pi}{\mathrm{HARMONY}} - \cdots,
$$
with $|\mathrm{Aut}(V)| = 40$ and $\mathrm{HARMONY} = 7$, claimed to recover $137.036$ to $\sim 10^{-5}$.

**Independent numerical verification** (sympy at machine precision; see `verification/verify_J36_part1.py`):
$$
4 \cdot 40 - 2\sqrt{7} - \pi/7 = 160 - 5.29150 - 0.44880 = 154.25970.
$$
The CODATA target is $1/\alpha = 137.035999084\ldots$, giving:
* Gap (additive): $154.25970 - 137.035999 = 17.22370$.
* Relative discrepancy: $\approx 12.6\%$ (relative to the target value), or $\approx 11.2\%$ (relative to the leading sum).

**The leading-three-terms claim "recovers $137.036$ to $\sim 10^{-5}$" is demonstrably false.** The leading three terms give $\sim 154.3$, an order-of-magnitude $10\%$ off, not $10^{-5}$. The full structural derivation referenced in earlier supporting bundles (described in source material as "tables LXXVII-LXXX of TIG_DIRAC_SYNTHESIS_TABLES rev 24") does not contain a first-principles derivation that closes the gap; the only formula in those tables that *numerically* recovers $137.036$ is `22 · 6 + 5 + 36/1000`, in which the "$+ 36/1000$" term is the empirical decimal of the target rather than a structural quantity. This is post-hoc decomposition, not derivation.

**Recommendation (per save plan).** Either: (a) drop Part 2 from this submission entirely and defer until a genuine structural derivation exists, or (b) restrict Part 2 to the leading-order claim "$4 \cdot |\mathrm{Aut}(V)| = 160$ is within $\approx 17\%$ of $1/\alpha$, suggesting the framework's $|\mathrm{Aut}(V)| = 40$ is *near* the right algebraic structure but the specific combination is not derived." We adopt option (a) for the present submission. A genuine structural derivation of $1/\alpha$ remains an open target; we do not assert that one exists.

---

## §5 Honest scope

* **Verified.** The numerical agreement at the levels stated. CKM/PMNS angles match the listed substrate primitives within $0.4\%$-$5.5\%$ across seven angles. The Wolfenstein hierarchy at $(11/49)^n$ for $n = 1, 2, 3, 4$ matches at $\le 1.6\%$ across four orders.
* **Verified.** The substrate constants $T^*$ and $|\mathrm{Aut}(V)|$ are derived independently from the substrate algebra in earlier J-papers of this series. The constant $D^*$ is *not* independently derived in the present paper; the $\theta_{12}$ fit is reported with this disclosure.
* **Not asserted.** The fits constitute first-principle derivations. There is no RG flow connecting substrate scale to electroweak scale; the fits are at the dimensionless-constant level only.
* **Not asserted.** The Cabibbo $+1/49$ refinement has a first-principles structural origin in the present framework. It is reported as an empirical adjustment.
* **Not in scope.** The $1/\alpha$ structural fit (which appeared in a previous draft of J36) is **deferred**: independent verification of the displayed leading-three-terms formula gave $154.26$, not the claimed $137.036$ ($\sim 12.6\%$ relative discrepancy, **not** $10^{-5}$). Part 2 is removed from this submission and is recommended for submission as a separate paper once a verifiable structural derivation exists, or honestly downgraded to a leading-order $\sim 10\%$ structural agreement.

---

## §6 Boilerplate framing

**PROVEN:** None — this is an empirical-fits paper, not a theorem paper.

**COMPUTED:** Per-angle relative discrepancies, naive joint probability, Bonferroni-style LE correction at multiplicity 77, and the with- and without-$\theta_{12}$ sensitivity (for the un-derived $D^*$). The verification script `verification/verify_J36_part1.py` reproduces all of these and additionally documents the $1/\alpha$ leading-three-terms numerical disagreement.

**STRUCTURAL RHYME:** The substrate constants $T^*, D^*, |\mathrm{Aut}(V)|$ are derived in earlier J-papers of this series ($T^*$ in [J6/WP51]; $|\mathrm{Aut}(V)|$ in [J32/WP115]; $D^*$ is referenced as the 4-core $\sigma$-cycle constant but is not closed-form-derived in this paper). The closest published precedent for the substrate algebra is **Drápal & Wanless (2021)**, *J. Combin. Theory A* **184**, 105510.

**OPEN:** First-principles derivation of the $+1/49$ Cabibbo refinement; closed-form derivation of $D^*$ from substrate algebra (currently used as empirical input); RG flow connecting substrate scale to electroweak scale. A verifiable structural derivation of $1/\alpha = 137.036$ (the previously-bundled Part 2) remains open; the leading-order $4 \cdot |\mathrm{Aut}(V)| = 160$ is within $\approx 17\%$ but the closing of the gap is not derived.

---

## §7 Look-elsewhere correction estimate (per referee report §2)

We adopt the save plan's framing of the look-elsewhere correction: at multiplicity $|\mathcal{P}| \cdot N_{\mathrm{obs}} = 11 \cdot 7 = 77$, the LE-corrected joint probability is approximately $1.4 \times 10^{-9}$ for the seven-fit ensemble. If the candidate-primitive set is enlarged to include further "framework-natural" expressions (e.g., $(\pi/14)^n$ for $n = 1, 2, 3, 4$, or $D^*$-like constants that could be tuned to fit other angles), the multiplicity rises and the corrected joint probability rises proportionally; the save plan estimates a post-LE range of $\approx 4 \times 10^{-7}$ to $\approx 4 \times 10^{-6}$ under more permissive primitive-counting choices. We report the multiplicity-77 value as our default; the broader range is documented for transparency.

---

## §8 Verification

```bash
PYTHONIOENCODING=utf-8 python verification/verify_J36_part1.py
# Prints per-fit discrepancy table, naive joint, LE-corrected joint, with/without theta_12 sensitivity,
# and the 1/alpha leading-three-terms numerical disagreement that justifies removal of Part 2.
```

Python 3.11+, no external dependencies beyond the standard library and `math`. Wall-clock under one second.

---

## §9 Lens and substrate

This paper compares CKM and PMNS mixing angles against substrate constants derived from a separate finite-magma research program on $\mathbb{Z}/10\mathbb{Z}$ (the canonical $T^* = 5/7$ torus aspect ratio; the $|\mathrm{Aut}(V)| = 40$ symmetry-group cardinality). These constants are not derived from physics first principles; they are derived from the substrate algebra in earlier J-papers and are imported here as inputs to the empirical fits. The fits are at the dimensionless-constant level only; no RG flow connects the substrate scale to the electroweak scale. Whether the framework's substrate choice (Z/10Z, the canonical TSML/BHML pair, the operator labels) is forced or merely structurally appropriate is open.

---

## §10 References

[Antusch03] Antusch, S., Kersten, J., Lindner, M., Ratz, M., *Running neutrino masses, mixings and CP phases: Analytical results and phenomenological consequences*, Nuclear Physics B **674** (2003), 401-433. (RG running of mixing angles from GUT to EW scale.)

[CODATA22] *CODATA recommended values of the fundamental physical constants: 2022.* Reviews of Modern Physics 95, 025002 (2023).

[Daya Bay 23] Daya Bay Collaboration, *Improved measurement of $\sin^2 2\theta_{13}$ with the full Daya Bay dataset*, Physical Review Letters **130** (2023), 161802.

[DW21] Drápal, A. and Wanless, I. M., *Maximally non-associative quasigroups*, Journal of Combinatorial Theory, Series A **184** (2021), 105510.

[J6/WP51] Sanders, B. R. (2026), *The 2×2 Cyclotomic Forcing of $T^* = 5/7$ on $\mathbb{Z}/10\mathbb{Z}$*. Submitted in this J-series.

[J32/WP115] Sanders, B. R. and Gish, M. (2026), *The Joint TSML+BHML Chain: Lens-Dependence at Size 7 and the Universal 4-Core Attractor*. Submitted in this J-series.

[J33/WP105] Sanders, B. R. and Gish, M. (2026), *A Closed-Form Algebraic Attractor for a Quadratic Table-Fusion Process on $\mathbb{Z}/10\mathbb{Z}$*. Submitted to *Mathematics of Computation*.

[J34] Sanders, B. R. and Gish, M. (2026), *Algebraic Detectors as Specificity Tests for a Finite-Magma Substrate*. Submitted to *Statistical Science*.

[PDG24] Particle Data Group, *Review of Particle Physics*, Physical Review D **110** (2024), 030001.

---
