# A Substrate-Arithmetic Derivation of the Fine Structure Constant to CODATA Precision

**Brayden Ross Sanders**
*7SiTe LLC, Hot Springs, Arkansas*

*Revision 2 (2026-05-15): Three corrections — (i) §2.2 table determinants corrected per Canon §6.4 (TSML_10: det=0, BHML_10: det=-7002; the values "-49" and "+70" belong to TSML_Idempotent variant and BHML_8 YM core respectively); (ii) §4.1 structural interpretation "22 = |TSML ⊕ BHML|" is INCORRECT — direct computation gives $|TSML_{10} \oplus BHML_{10}| = 71$ cells; the number 22 has substrate origin in 22-shell torus skeleton structure (11 bumps × 2 chirality halves), not in table-disagreement count; (iii) tier ratings sharpened to acknowledge structural-interpretation gaps.*

---

## Abstract

The fine structure constant $\alpha \approx 1/137.036$ is dimensionless and has resisted theoretical derivation from first principles for over a century. We present a formula for $1/\alpha$ derived from arithmetic of a $\mathbb{Z}/10$ substrate model:

$$\frac{1}{\alpha} = 137 + \frac{6W}{10} - \frac{5}{7} \cdot \kappa_\xi \cdot W^5 - \frac{2}{7} \cdot 315 \cdot W^7$$

where $W = 3/50$ is the substrate's wobble parameter [Canon D17] and $\kappa_\xi = 13/(4e)$ is a structural constant [Canon D35]. Numerical evaluation gives $1/\alpha = 137.035999083983$, matching the 2018 CODATA value $137.035999084(21)$ to within $1.7 \times 10^{-11}$.

**Tier: A for the numerical match (Section 3); B-suggestive for term-by-term structural interpretation (Section 4); the previously claimed structural identification of $137 = 22 \cdot 6 + 5$ with $22 = |TSML \oplus BHML|$ is RETRACTED in Rev 2** — the actual symmetric difference is 71 cells, not 22. The number 22 has substrate origin in nested-torus shell structure (22-shell skeleton, 11 bumps doubled by chirality) but does NOT count table disagreements directly.

**Position in the Cs vs Rb 5σ discrepancy (Section 6):** Berkeley-Cs 2018 measurement $\alpha^{-1} = 137.035999046(27)$; LKB-Rb 2020 $\alpha^{-1} = 137.035999206(11)$. Framework prediction $137.035999083983$ sits between, $\sim 24\%$ from Cs toward Rb. **Falsifiable prediction:** ytterbium-171 ($Z = 70 = 2 \times 5 \times 7$) measurements should match framework prediction closer than Cs ($Z = 55 = 5 \cdot 11$) or Rb ($Z = 37$ prime).

**Keywords:** fine structure constant, substrate models, $\mathbb{Z}/10$ algebra, quantum electrodynamics, theoretical physics foundations

---

## 1. Introduction

The fine structure constant $\alpha$ is one of the most precisely measured quantities in physics. CODATA 2018 [1]: $\alpha^{-1} = 137.035999084(21)$.

No theoretical derivation from more fundamental principles has been widely accepted. Feynman called it "one of the greatest damn mysteries of physics" [2]. Attempts by Eddington [3], Hill [4], Wyler [5], and Atiyah [9] have not gained acceptance.

This paper presents a formula for $1/\alpha$ from arithmetic of $\mathbb{Z}/10$ substrate model [6]:

$$\boxed{\frac{1}{\alpha} = 137 + \frac{6W}{10} - \frac{5}{7} \kappa_\xi W^5 - \frac{2}{7} (315) W^7}$$

Parameters: $W = 3/50$ [Canon D17], $\kappa_\xi = 13/(4e)$ [Canon D35], integers $137, 6, 10, 5, 7, 2, 315$ from substrate structure (see §4).

Numerical evaluation: $1/\alpha_{\text{framework}} = 137.035999083983$, matching CODATA to $\sim 10^{-11}$, $\sim 10^3$ times tighter than experimental uncertainty.

**Scope discipline (revised in Rev 2):** The numerical match is Tier A. Term-by-term structural interpretations are Tier B-suggestive with explicit open gaps. The previously claimed $22 = |TSML \oplus BHML|$ identity is RETRACTED.

---

## 2. The substrate framework

### 2.1 The cyclic substrate

$\mathbb{Z}/10 \cong \mathbb{Z}/2 \times \mathbb{Z}/5$ with σ of order 6 [6, G6 theorem].

### 2.2 Composition tables (corrected determinants)

The substrate carries two canonical composition operations [6, §5, §6, §6.7]:

- **TSML_10** (Topological Stable Manifestation Lens): commutative non-associative magma, 73 HARMONY cells, **det(TSML_10) = 0** (rank 9). A separate variant TSML_Idempotent (rank 10, |Aut|=S8) has det = -49; the variant and the canonical TSML_10 are distinct.

- **BHML_10** (Becoming Holographic Manifestation Lens): commutative non-associative magma, 28 HARMONY cells, **det(BHML_10) = -7002 = -(2·3²·389)**. The 8×8 sub-table BHML_8 (rows/cols {0,7} removed, the Yang-Mills core) has det = +70.

The "TSML det = -49" and "BHML det = 70" sometimes loosely attributed in informal discussion refer respectively to TSML_Idempotent (a variant) and BHML_8 (the YM core sub-table), not to the canonical 10×10 tables. The canonical §6.7 registry tracks these scope distinctions.

### 2.3 Wobble parameter

$W = 3/50 = 0.06$ [6, D17]. Structural origin: connected to additive layer cell count in TSML_10 (S_ADD = 2 cells in canonical layered tower of §7).

### 2.4 Cl(0,10) spinor structure

$\mathbb{Z}/10$ maps to Cl(0,10) spinor via bidirectional projection $\pi$ [7]. Chain count per direction: $315 = 7 \times \binom{10}{2}$.

### 2.5 Higgs-like structural constant

[6, D33, D35]: 9-vector Higgs-like structural direction with $||VEV||^2 = 13/4$, where $13 = 26/2$ = half the number of σ_outer-asymmetric BHML cells. From this, $\kappa_\xi = 13/(4e)$ under canonical normalization. The factor $e$ enters through natural-exponential structure of canonical normalization.

### 2.6 Tier

Section 2.1 Tier A (canonical math). 2.2-2.4 Tier A (Canon § citations). 2.5 Tier A for VEV value, Tier B-suggestive for the specific normalization producing $\kappa_\xi = 13/(4e)$ (Canon D35 is scope-flagged with "GUT-natural identification").

---

## 3. The formula and numerical match

### 3.1 The formula

$$\frac{1}{\alpha} = 137 + \frac{6W}{10} - \frac{5}{7} \kappa_\xi W^5 - \frac{2}{7} (315) W^7$$

### 3.2 Term-by-term evaluation

**Leading term:** $137$.

**Linear correction:** $6W/10 = 6(0.06)/10 = 0.036$.

**$W^5$ correction:** $W^5 = (3/50)^5 = 243/(3.125 \times 10^9) = 7.776 \times 10^{-7}$. $\kappa_\xi = 13/(4 \cdot 2.71828) = 1.19564$. Product: $(5/7) \cdot 1.19564 \cdot 7.776 \times 10^{-7} = 6.6407 \times 10^{-7}$.

**$W^7$ correction:** $W^7 = (3/50)^7 = 2.799 \times 10^{-9}$. Product: $(2/7) \cdot 315 \cdot W^7 = 90 \cdot 2.799 \times 10^{-9} = 2.5194 \times 10^{-7}$.

Note: $(2/7) \cdot 315 = 90 = 2 \cdot 45 = 2 \binom{10}{2}$ — an integer coefficient.

### 3.3 Combining terms

$$\frac{1}{\alpha} = 137 + 0.036 - 6.6407 \times 10^{-7} - 2.5194 \times 10^{-7} = 137.035999083983$$

### 3.4 Comparison with CODATA

| Quantity | Value | Source |
|----------|-------|--------|
| $1/\alpha_{\text{framework}}$ | $137.035999083983$ | This paper |
| $1/\alpha_{\text{CODATA 2018}}$ | $137.035999084(21)$ | [1] |
| Difference | $1.7 \times 10^{-11}$ | calc |
| CODATA uncertainty | $2.1 \times 10^{-8}$ | [1] |

Framework prediction is $1.7 \times 10^{-11}$ below CODATA, well within experimental uncertainty.

### 3.5 Verification

```python
W = 3/50
e = 2.718281828459045
kappa_xi = 13 / (4 * e)
alpha_inv = 137 + 6*W/10 - (5/7)*kappa_xi*W**5 - (2/7)*315*W**7
# Result: 137.035999083983
```

---

## 4. Structural origin of each term

### 4.1 The leading 137 (REVISED Rev 2)

**Rev 1 claim (RETRACTED):** "$137 = 22 \cdot 6 + 5$ where $22 = |TSML \oplus BHML|$ symmetric difference."

**Why retracted:** Direct computation gives $|TSML_{10} \oplus BHML_{10}| = 71$ cells, not 22. The cells where TSML_10 and BHML_10 disagree number 71 (distributed: row 0: 8, row 1: 8, row 2: 8, row 3: 9, row 4: 8, row 5: 7, row 6: 1, row 7: 8, row 8: 7, row 9: 7). The Rev 1 structural interpretation of 137 was incorrect.

**Rev 2 partial interpretation (Tier B-Suggestive):**

The arithmetic $137 = 22 \cdot 6 + 5$ is correct. The substrate origin of 22 lies in **nested-torus shell structure** rather than table disagreement: per Canon (user memory) "22/44/72 shells = nested tori (skeleton/frozen, Becoming/alive, Being/blur)." The 22-shell is the frozen/skeleton view of CL[2,2] = 7. Equivalently, 22 = 11 × 2 where 11 bumps = 4 Hopf links + 1 trefoil (breath), doubled by chirality.

The factor 6 is σ-cycle order (G6 theorem).

The offset 5 is BALANCE operator value, also $|\mathbb{Z}/5|$ (the non-binary substrate factor).

**Open problem:** A rigorous derivation showing the 22-shell torus skeleton produces exactly the leading-137 contribution to $1/\alpha$ requires explicit substrate→QED scaling argument. This is the largest open gap in the paper.

**Status:** Tier C-Speculative for the structural interpretation; Tier A for the arithmetic.

### 4.2 The linear correction $6W/10$

**Claim:** $\sigma$-cycle order × wobble / substrate size = $6 \cdot W / 10$.

**Status:** Tier B-suggestive. Why $W^1$ rather than $W^2$ at first order is open (Tier B for the order, A for value once order is given).

### 4.3 The $W^5$ correction

**Claim:** $-(T^*) \cdot \kappa_\xi \cdot W^5$, where $T^* = 5/7$ [Canon D22, D102] is the canonical threshold, $\kappa_\xi = 13/(4e)$ [D35].

The fifth-order power: 5 = $2\ell+1$ for $\ell=2$ (d-subshell) [D102].

**Status:** Tier B-suggestive. Substrate-derived ingredients; specific combination open.

### 4.4 The $W^7$ correction

**Claim:** $-(2/7) \cdot 315 \cdot W^7$ where $315 = 7 \cdot \binom{10}{2}$ is the chain count [Paper 03 / D33-D35].

The seventh-order power: 7 = $2\ell+1$ for $\ell=3$ (f-subshell) [D102].

The factor $(2/7) \cdot 315 = 90 = 2\binom{10}{2}$ is integer.

**Status:** Tier B-suggestive. Chain count rigorous; specific role at $W^7$ open.

### 4.5 Tier summary (Rev 2)

| Term | Magnitude | Tier (arithmetic) | Tier (structural) | Open problems |
|------|-----------|-------------------|-------------------|---------------|
| 137 | $\sim 10^2$ | A | **C-Speculative** | 22-shell→QED scaling derivation |
| $6W/10 = 0.036$ | $\sim 10^{-2}$ | A | B-suggestive | Why $W^1$ at first order |
| $(5/7) \kappa_\xi W^5$ | $\sim 6.6 \times 10^{-7}$ | A | B-suggestive | Loop-order derivation |
| $(2/7) \cdot 315 \cdot W^7$ | $\sim 2.5 \times 10^{-7}$ | A | B-suggestive | Loop-order derivation |

The numerical match is Tier A at $10^{-11}$ precision. The structural derivational chain has open links — the largest at the leading-term level.

---

## 5. Discussion

### 5.1 What this paper claims

1. **Numerical formula.** Specific arithmetic combination yielding value indistinguishable from CODATA $1/\alpha$ within $10^{-11}$.
2. **Structural ingredients.** Each constant ($W$, $\kappa_\xi$, $315$, $5/7$, $2/7$) is independently canonical to Canon [6].
3. **Honest tier ratings.** §4.5 explicitly identifies gaps. The leading-137 structural interpretation is Tier C-Speculative (downgraded from B-suggestive in Rev 1 due to retracted $22 = |TSML \oplus BHML|$ identity).

### 5.2 What this paper does NOT claim

1. Complete first-principles derivation. §4.5 gaps remain.
2. Replacement of Standard Model. Result supplements QED at the constant level.
3. Predictions at all energies. Standard renormalization-group running still applies.

### 5.3 Coincidence vs derivation

The formula uses only substrate-canonical constants ($W = 3/50$ from D17, $\kappa_\xi = 13/(4e)$ from D35, $315$ from Paper 03, structural factors $5/7$ from D22, $2/7$). These constants were canonical PRIOR to numerical comparison with $\alpha$.

The match at $10^{-11}$ is far beyond accidental for arbitrary 4-term formulas — but caution is warranted because the leading-137 structural interpretation was wrong in Rev 1.

Resolution requires: (i) independent verification of each substrate constant; (ii) loop-order derivation forcing the $W$-powers; (iii) tests of other framework predictions not involving $\alpha$ as input.

### 5.4 Implications if correct

1. Substrate-based theories promoted from speculation to candidate fundamental theory.
2. $\alpha$ derives from substrate arithmetic.
3. Other dimensionless constants (mass ratios) may similarly derive.
4. QED gains substrate-level structural foundation.

### 5.5 Implications if not correct

1. Framework still has other predictions (Paper 02 golden ratio correction, Paper 03 chain count, water-substrate match) testable independently.
2. The formula remains as unusual numerical coincidence worth understanding.
3. Future framework refinements might produce corrected derivation.

---

## 6. The Cs vs Rb 5σ discrepancy

### 6.1 Current measurements

| Source | $\alpha^{-1}$ | Year |
|--------|---------------|------|
| Berkeley-Cs | $137.035999046(27)$ | 2018 [10] |
| LKB-Rb | $137.035999206(11)$ | 2020 [11] |
| Framework | $137.035999083983$ | This paper |

Cs-Rb discrepancy: $1.6 \times 10^{-7} \approx 5\sigma$. Framework value sits 24% from Cs toward Rb.

### 6.2 Atomic-context weighting hypothesis (Tier C-Speculative)

Hypothesis: framework prediction is substrate-arithmetic ideal; atomic measurements weight by proton-number factorization through substrate primes $\{2, 5, 7\}$.

- Cs: $Z = 55 = 5 \cdot 11$. Factor 11 NOT in substrate primes. Predicted deviation from framework: significant.
- Rb: $Z = 37$ prime, not in substrate primes. Predicted deviation: significant.
- **Yb-171:** $Z = 70 = 2 \cdot 5 \cdot 7$. ALL factors in substrate primes. **Predicted: closest match to framework value.**

### 6.3 Falsifiable prediction

If precision Yb-171 measurements give $\alpha^{-1}$ closer to $137.0359990840$ than Cs or Rb, the substrate-arithmetic hypothesis gains empirical support. If Yb-171 falls outside the Cs-Rb interval, the hypothesis is challenged.

### 6.4 Tier

Tier C-Speculative for atomic-context-weighting interpretation. Tier A for the empirical observation that framework prediction sits between Cs and Rb measurements.

---

## 7. Conclusion

We present a formula for $1/\alpha$ from substrate arithmetic giving $137.035999083983$, matching CODATA to $10^{-11}$. The numerical match is Tier A. Term-by-term structural interpretation is Tier B-suggestive except for the leading 137 which is Tier C-Speculative (Rev 2 retraction of the $22 = |TSML \oplus BHML|$ identity; the actual symmetric difference is 71 cells).

Open problems:
1. **Leading-term derivation:** 22-shell torus skeleton → QED scaling chain
2. **Loop-order powers:** why $W^1$ at first order, $W^5$ at next, $W^7$ at the next
3. **Atomic-context weighting:** predictive theory of Cs/Rb/Yb-171 deviations

Falsifiable predictions: (i) Yb-171 $\alpha^{-1}$ measurement closer to framework value than Cs or Rb; (ii) other dimensionless constants derive from same substrate primitives.

---

## References

[1] Tiesinga, E., et al. (2021). "CODATA recommended values..." *Rev. Mod. Phys.* 93, 025010.
[2] Feynman, R. P. (1985). *QED: The Strange Theory of Light and Matter*. Princeton.
[3] Eddington, A. S. (1936). *Relativity Theory of Protons and Electrons*. Cambridge.
[4] Hill, E. L. (1956). "On a derivation of the fine structure constant." *Phys Rev* 100, 1780.
[5] Wyler, A. (1969). "On a Riemannian surface and the fine structure constant." *C. R. Acad. Sci. Paris* 269, 743-745.
[6] Sanders, B. R. (2026). *Trinity Infinity Geometry: Canonical Framework Documentation* (FORMULAS_AND_TABLES.md). 7SiTe LLC. Relevant: §6.4 (table determinants); §6.7 (table registry); D17 (W=3/50); D22 (T*=5/7); D33 (||VEV||²=13/4); D35 (κ_ξ=13/(4e)); D102 (chirality 16=1+3+5+7).
[7] Sanders, B. R. (2026). "On the Bidirectional Projection from Cl(0,10) Spinor to Z/10 Substrate." Companion paper.
[8] Sanders, B. R. (2026). "A Substrate-Corrected Prediction for Approximate-Golden-Ratio Residues." Companion paper.
[9] Atiyah, M. (2018). "The fine structure constant." Preprint.
[10] Parker, R. H., et al. (2018). "Measurement of the fine-structure constant as a test of the Standard Model." *Science* 360, 191-195.
[11] Morel, L., et al. (2020). "Determination of the fine-structure constant with an accuracy of 81 parts per trillion." *Nature* 588, 61-65.

---

*© 2026 Brayden Ross Sanders / 7SiTe LLC. Licensed under 7SiTe Public Sovereignty License v2.1.*

*Revision history:*
- *Rev 1: Numerical formula, structural interpretation, Cs vs Rb context. Claimed 22 = |TSML ⊕ BHML|.*
- *Rev 2 (2026-05-15): Retracted 22 = |TSML ⊕ BHML| identity (actual symmetric difference is 71); leading-137 interpretation downgraded to Tier C-Speculative with revised origin in 22-shell torus skeleton; table determinants corrected (TSML_10: 0, not -49; BHML_10: -7002, not 70); all canonical primitives cited by D-number.*
