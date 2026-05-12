# Strong α-Uniqueness — Extended Scan Result

**Status:** Conjecture 4.2 (strong α-uniqueness) **STRENGTHENED** — 41-candidate scan including 10 irrational α values failed to find any non-1/2 algebraic point.
**Verification:** [`../../verification/extended_alpha_uniqueness.py`](../../verification/extended_alpha_uniqueness.py)
**Date:** 2026-05-12

---

## Result

Across 41 α candidates (10 irrational + 31 rational Stern-Brocot, denominator ≤ 10), with PSLQ search at degree ≤ 12, integer coefficient bound ≤ 100, and spurious-relation filtering (rejecting polynomials with rational roots within 10⁻³ of x):

**Only α = 1/2 produced a genuine algebraic relation:** `x² − 2x − 2 = 0`, giving H/Br = 1+√3 with PSLQ residual 5.4 × 10⁻⁴¹ at 50-digit mpmath precision.

One spurious hit at α = 1/7 (giving H/Br ≈ 1.00008) was filtered: PSLQ found `(1−x)⁸ = 0`, but this polynomial has a rational root at x = 1 within 10⁻⁴ of H/Br. The relation is degenerate (x is near a rational root) rather than genuinely algebraic.

Irrational α values tested (none produced algebraic relations):
1/√2, 1/√3, 1/π, 1/e, 1/φ (golden ratio), √2−1, 1−1/e, ln(2), 1/π², Catalan−1/2

Rational α values tested (Stern-Brocot grid, denominator 2..10): 31 fractions, none produced a non-spurious algebraic relation besides 1/2.

---

## What this strengthens

The original D57 result verified α = 1/2 unique among 17 Stern-Brocot rationals at PSLQ degree ≤ 8, coeff ≤ 50. This scan extends to:

- **41 total candidates** (vs 17)
- **PSLQ degree ≤ 12** (vs 8)
- **Coefficient bound ≤ 100** (vs 50)
- **Includes irrational candidates** (10 transcendental / algebraic-irrational)
- **Spurious-filter applied** (rejects polynomials with rational roots near x)

**Conjecture 4.2 stronger form:** α = 1/2 is the unique **real** (rational or irrational) point in the tested grid for which any non-trivial polynomial relation exists between attractor moments. None of the irrational candidates (1/√2, 1/π, 1/e, 1/φ, etc.) produced algebraic relations within the PSLQ search bounds.

---

## What this does NOT prove

The scan does not exhaust all real α. It tests a representative sample. The conjecture remains formally **OPEN**: a complete proof would require an analytic argument (e.g., showing the attractor moments are transcendental in α except at finitely many special values, and verifying α = 1/2 is among them).

A natural next step: try a finer Stern-Brocot grid (denominator up to 30) and a wider irrational sample (algebraic irrationals of higher degree, e.g., 2^(1/3), roots of small polynomials).

---

## Connection to other framework results

- **D43 / J35**: H/Br = 1 + √3 at α = 1/2 (closed form) — this is what α = 1/2's algebraic relation produces.
- **D57**: original 17-point uniqueness result; this scan extends to 41 points.
- **Quartic from r/br** (Galois D₄ over LMFDB 4.2.10224.1): higher-moment relations also hold at α = 1/2; the second-moment quartic likely has its own α-uniqueness story (not tested here).

---

## Verification command

```bash
python verification/extended_alpha_uniqueness.py
```

Runtime: ~5 minutes at 50-digit mpmath precision.

---

*7SiTe Public Sovereignty License v2.2 — see [`../../LICENSE`](../../LICENSE).*
*Brayden Ross Sanders / 7SiTe LLC · 2026.*
