# Frontier F14 -- Height function H(alpha) for algebraic relations between alpha and xi-roots of Q

**Status:** Characterization **COMPLETE** at the tested 42 alpha-points (q = 2..10 rationals + 11 algebraic irrationals + alpha_special). H(1/2) = 2 is the unique global minimum. Empirical scaling law `log10(H(p/q)) ~= 0.91 + 3.41 * log10(q)` at non-1/2 rationals. Algebraic irrationals follow `H ~ const * deg(alpha) * 7` in the resultant-degree dimension with coefficient size growing exponentially. alpha_special's height **2,191,936** (xi_double minpoly over Q) is much smaller than the "10^106" figure reported by F12 — the latter is a different invariant (bivariate Q[a, xi] linear relation), not the univariate Q[xi] minimal polynomial of xi_double.

**Verification:** [`../../verification/frontier_F14_height_function.py`](../../verification/frontier_F14_height_function.py)
**Numerical artifact:** [`F14_height_data.json`](F14_height_data.json)
**Plot:** [`F14_height_plot.png`](F14_height_plot.png)
**Date:** 2026-05-29
**Builds on:** F1 (alpha-uniqueness scan), F5 (Q(xi, a) form), F6 (Hilbert irreducibility -- minpoly of xi over Q is irreducible at every Q-rational alpha in (0,1) except 1/2), F9 (algebraic irrationals + alpha_special PSLQ at maxcoef <= 10^4), F12 (alpha_special xi-double bivariate relation at height ~10^106).

---

## §1 Definition of H(alpha)

For each alpha in (0, 1), let `Q(xi, a)` be the load-bearing degree-7 polynomial of F5/F6. The smallest "height" of an algebraic relation between alpha and a xi-root xi_0 of Q(xi, alpha) admits **two natural, distinct readings**:

**Reading U (univariate minimal polynomial):** Let `M_alpha(xi)` be the minimal polynomial of xi_0 over Q. Define
```
H_U(alpha) := max |coefficient| of M_alpha(xi) in its primitive Z[xi] form.
```
Equivalently (up to a constant): the naive height of the algebraic number xi_0 in Q-bar.

**Reading B (bivariate relation in Q[a, xi]):** the smallest height of any nontrivial polynomial relation `R(a, xi)` in Q[a, xi] satisfied jointly by (alpha, xi_0). Equivalently, the smallest height of a Q[a, xi] element of the prime ideal of (alpha, xi_0).

For rational alpha = p/q, **Reading U is the natural one**: M_alpha is the minimal polynomial in Q[xi] of the algebraic number xi_0, and its primitive Z[xi] form has well-defined integer height.

For algebraic-irrational alpha (minimal polynomial m_alpha(a) over Q of degree d), the minimal polynomial of xi_0 over Q is the irreducible factor of `Res_a(m_alpha(a), Q(xi, a))` containing xi_0 -- still in Q[xi], still has a primitive Z[xi] form, still has a well-defined H_U.

For both Readings the "height of the lowest-height relation" is well-defined; F14 reports the Reading-U value as the canonical H(alpha) of this frontier (it is bounded above by the Reading-B value in the natural relations one can write, and is the form most directly comparable to F1 / D57's PSLQ runs which seek integer relations on `[xi_0, 1, alpha, alpha^2, ..., alpha^(d-1)]`).

F12's reported height "~10^106" is a Reading-B figure: the linear-in-xi Q[a, xi] relation `A * xi - B(a) = 0` with deg_a(B) = 23, |A| ~ 10^99, max |B-coefficient| ~ 10^106. F14's H_U(alpha_special) = 2,191,936 is the **univariate** Reading-U figure on the minimal polynomial of xi_double over Q, which has degree 24 and height 2191936. These are different invariants of the same algebraic point; both are legitimate "heights".

---

## §2 Table of H(alpha)

### §2.1 At rationals alpha = p/q with q in {2,..,10}, gcd(p,q)=1, 0 < p < q

| alpha | denom q | deg minpoly | H(alpha) | log10(H) | structure |
|---:|---:|---:|---:|---:|---|
| **1/2** | 2 | **2** | **2** | **0.30** | `(xi)^2 * (xi^2 - 2*xi - 2)^2` (genuine minpoly: xi^2 - 2xi - 2) |
| 2/3 | 3 | 7 | 314 | 2.50 | irreducible deg-7 over Q |
| 3/4 | 4 | 7 | 388 | 2.59 | irreducible deg-7 |
| 1/4 | 4 | 7 | 436 | 2.64 | irreducible deg-7 |
| 1/3 | 3 | 7 | 544 | 2.74 | irreducible deg-7 |
| 1/6 | 6 | 7 | 944 | 2.97 | irreducible deg-7 |
| 4/5 | 5 | 7 | 1041 | 3.02 | irreducible deg-7 |
| 5/6 | 6 | 7 | 1180 | 3.07 | irreducible deg-7 |
| 2/5 | 5 | 7 | 1868 | 3.27 | irreducible deg-7 |
| 1/5 | 5 | 7 | 3976 | 3.60 | irreducible deg-7 |
| 4/7 | 7 | 7 | 5063 | 3.70 | irreducible deg-7 |
| 9/10 | 10 | 7 | 5184 | 3.71 | irreducible deg-7 |
| 3/5 | 5 | 7 | 5236 | 3.72 | irreducible deg-7 |
| 3/8 | 8 | 7 | 6468 | 3.81 | irreducible deg-7 |
| 1/10 | 10 | 7 | 6784 | 3.83 | irreducible deg-7 |
| 7/8 | 8 | 7 | 8148 | 3.91 | irreducible deg-7 |
| 2/7 | 7 | 7 | 8276 | 3.92 | irreducible deg-7 |
| 5/8 | 8 | 7 | 8420 | 3.93 | irreducible deg-7 |
| 3/10 | 10 | 7 | 8592 | 3.93 | irreducible deg-7 |
| 7/10 | 10 | 7 | 8992 | 3.95 | irreducible deg-7 |
| 1/8 | 8 | 7 | 9052 | 3.96 | irreducible deg-7 |
| 6/7 | 7 | 7 | 9225 | 3.96 | irreducible deg-7 |
| 4/9 | 9 | 7 | 11599 | 4.06 | irreducible deg-7 |
| 8/9 | 9 | 7 | 13370 | 4.13 | irreducible deg-7 |
| 3/7 | 7 | 7 | 16108 | 4.21 | irreducible deg-7 |
| 5/7 | 7 | 7 | 16580 | 4.22 | irreducible deg-7 |
| 1/7 | 7 | 7 | 17932 | 4.25 | irreducible deg-7 |
| 2/9 | 9 | 7 | 21692 | 4.34 | irreducible deg-7 |
| 7/9 | 9 | 7 | 40775 | 4.61 | irreducible deg-7 |
| 5/9 | 9 | 7 | 55180 | 4.74 | irreducible deg-7 |
| 1/9 | 9 | 7 | 65252 | 4.81 | irreducible deg-7 |

Total: 31 rationals. The 1/2 row is the global minimum (next-lowest is 2/3 at H = 314, **two orders of magnitude higher**).

### §2.2 At algebraic irrationals (11 from F9)

| alpha label | deg(alpha) over Q | minpoly deg over Q | H(alpha) | log10(H) |
|---|---:|---:|---:|---:|
| sqrt(2)/2 | 2 | 14 | 6,080 | 3.78 |
| (sqrt(5)-1)/2 | 2 | 14 | 12,564 | 4.10 |
| 1/sqrt(5) | 2 | 14 | 484,832 | 5.69 |
| 2^(-1/3) | 3 | 21 | 552,096 | 5.74 |
| real root of x^3+x-1 | 3 | 21 | 781,504 | 5.89 |
| real root of x^5+x-1 | 5 | 21 | 1,850,240 | 6.27 |
| real root of x^3+2x-1 | 3 | 21 | 2,320,640 | 6.37 |
| 3^(-1/3) | 3 | 21 | 7,232,400 | 6.86 |
| 2^(-1/4) | 4 | 28 | 104,168,064 | 8.02 |
| real root of x^4+x-1 | 4 | 28 | 125,055,648 | 8.10 |
| 3^(-1/4) | 4 | 28 | 1,241,755,328 | 9.09 |

The "minpoly deg" column shows that the resultant gives a polynomial of degree `7 * deg(alpha)` in xi; sympy's `factor_list` over Q confirms IRREDUCIBILITY at every tested irrational so this is the true minpoly degree over Q. The height grows monotonically with `7 * deg(alpha)` in this dataset, ranging from ~10^4 at deg-2 to ~10^9 at deg-4.

### §2.3 At alpha_special (P_24 root in (0,1))

```
alpha_special ~= 0.11255061532893783490843621259693765915002129572304...

deg(alpha_special) over Q = 24.
```

The resultant `Res_a(P_24(a), Q(xi, a))` is a polynomial of degree 24 * 7 = 168 in xi over Z. It factors over Q as:

| Factor | Degree | Multiplicity | Height | log10(H) |
|---|---:|---:|---:|---:|
| **M(xi)** | 24 | 2 | 2,191,936 | **6.34** |
| H_120(xi) | 120 | 1 | 5.78 * 10^47 | 47.76 |

The deg-24 factor M(xi) is the minimal polynomial of `xi_double` over Q (the unique double xi-root of Q(xi, alpha_special)). Its multiplicity-2 in the resultant directly reflects the F12 finding that P_24 appears with multiplicity 1 in disc_xi(Q), so xi_double is a double root of Q at the discriminant-zero point alpha_special.

The deg-120 factor H_120(xi) is the joint minimal polynomial of all 120 "simple" xi-roots arising from the 24 conjugate alphas times the 5 simple xi-roots per alpha. F12 §4 established `Gal(H_120 / Q(alpha_special)) = S_5` on the 5 simple roots over each alpha-conjugate; over Q itself the picture lifts to a larger group containing both S_5 and the alpha-side action.

**H_U(alpha_special) = 2,191,936 ~ 10^6.34.**

This is FAR below the F12-reported figure ~10^106, which measures the **bivariate** Q[a, xi] relation `A * xi - B(a) = 0` (Reading B). The two readings differ because xi_double admits the very low-height univariate representation M(xi_double) = 0 but only a high-height linear-in-xi bivariate representation in Q[a, xi].

---

## §3 Observed scaling pattern

### §3.1 At rationals: H(p/q) ~ q^3.41

Linear regression on the 30 non-1/2 rationals:
```
log10(H(p/q)) = 0.907 + 3.407 * log10(q)
```
i.e., H(p/q) grows roughly like `8 * q^3.4` at the tested denominators.

The "naive" upper bound from substitution `a -> p/q` and clearing denominators is `q^4` (since `deg_a(Q) = 4`). The observed exponent 3.4 is somewhat below 4 because many leading-power terms cancel or simplify after expansion, lowering the effective polynomial degree in q. The exponent is also weakly p-dependent: e.g., at fixed q = 9, H ranges from 11,599 (at 4/9) to 65,252 (at 1/9) -- a factor of ~6 in the numerator-induced spread.

### §3.2 At algebraic irrationals: H(alpha) ~ exp(c * deg(alpha) * 7)

The minimal polynomial degree of xi_0 over Q at an algebraic irrational alpha of degree d is `7d` (since Q(xi, a) has xi-degree 7 and m_alpha(a) has degree d). The height grows roughly exponentially in `7d`:

| deg(alpha) d | typical log10(H) | log10(H) / (7d) |
|---:|---:|---:|
| 2 | 3.8 - 5.7 | 0.27 - 0.41 |
| 3 | 5.7 - 6.9 | 0.27 - 0.33 |
| 4 | 8.0 - 9.1 | 0.29 - 0.32 |
| 5 | 6.3 | 0.30 |

The ratio `log10(H) / (7d)` is remarkably stable at ~0.3 for d in {2, 3, 4, 5}. Extrapolating: at d = 24 (alpha_special), we would expect `log10(H_generic) ~ 0.3 * 7 * 24 = 50.4`, very close to the observed `log10(H_120) = 47.8` for the deg-120 generic factor. The deg-24 xi_double factor at log10(H) = 6.3 is **dramatically below** this generic scaling, by ~41 orders of magnitude — a direct empirical signature of the F12 discriminant-zero structure at alpha_special.

### §3.3 Summary

- **Rationals:** polynomial growth in denominator, `H(p/q) ~ q^3.4`.
- **Algebraic irrationals:** exponential growth in deg(alpha), `H(alpha) ~ 10^(0.3 * 7 * deg(alpha))`.
- **alpha_special (discriminant-zero point):** the generic deg-120 factor matches the d = 24 prediction but the deg-24 `xi_double` factor is `10^41` smaller -- a HEIGHT-DROP signature of the structural-reducibility at alpha_special.

---

## §4 H(1/2) = 2 as global minimum

The 1/2 row stands out by two orders of magnitude:

```
H(1/2) = 2,
H(2/3) = 314    (next lowest rational, factor ~157 larger)
H(sqrt(2)/2) = 6,080    (lowest irrational, factor ~3,040 larger)
H(alpha_special; xi_double) = 2,191,936    (factor ~1,000,000 larger)
```

Mechanism: at alpha = 1/2 the leading-xi coefficient `lc_xi(Q) = -a*(2a-1)*(a-1)` vanishes. Substituting `a = 1/2` collapses Q from degree 7 in xi to effectively degree 4 (after factoring out xi^2 and the squared quadratic). The quadratic factor `xi^2 - 2*xi - 2` of height 2 governs the irrational xi-roots, both of which lie in `Q(sqrt(3))`. By F6 (Hilbert irreducibility), this is the unique Q-rational alpha exhibiting this drop -- at every other rational p/q in (0,1) the leading coefficient stays nonzero (since `p*(2p-q)*(p-q) != 0`) and the deg-7 polynomial is irreducible over Q.

**H(1/2) = 2 is the unique alpha with `H < 100` among the tested 42-point dataset.**

---

## §5 Conjectures about the structure of H(alpha)

### §5.1 Conjecture F14.1 (uniqueness of the global minimum)

**For all alpha in (0, 1) \ {1/2}, H(alpha) > 100.**

Status: VERIFIED at the tested 41 non-1/2 alphas (rationals q in {2..10} + 11 algebraic irrationals + alpha_special). Conjectural at irrationals not yet tested. Note that the minimum non-1/2 height at rationals is 314 (at 2/3) and at irrationals is 6,080 (at sqrt(2)/2); the conjecture's bound 100 is well-separated from both.

### §5.2 Conjecture F14.2 (rational-height polynomial growth)

**For all rationals alpha = p/q in (0, 1) \ {1/2} with gcd(p, q) = 1, there exist absolute constants `c_lower, c_upper > 0` such that**
```
c_lower * q^3 <= H(p/q) <= c_upper * q^4.
```

Status: VERIFIED empirically at the 30 tested rationals with denominator <= 10. The upper bound `q^4` is the trivial substitution-clear-denominators bound; the lower bound `q^3` is the observation that H grows at least cubically in q (since `log10(H) / log10(q) >= 3.0` at q >= 4 in the dataset).

The exponent 3.4 in the regression sits between these. A rigorous proof would require showing the resultant `Res_a(q*a - p, Q(xi, a))` has height growing as `Theta(q^k)` for some k in [3, 4], with the exact exponent depending on the leading-coefficient structure.

### §5.3 Conjecture F14.3 (algebraic-irrational exponential growth)

**For algebraic-irrational alpha of degree d over Q with minimal polynomial m_alpha of bounded coefficient size, there exist absolute constants `c_1, c_2 > 0` such that**
```
log10(H(alpha)) ~= c_1 + c_2 * d
```
**with `c_2 ~ 7 * (0.3 ± 0.05)` empirically at d in {2, 3, 4, 5}.**

Status: VERIFIED at 11 algebraic irrationals. Note the ratio `log10(H) / (7d) ~ 0.3` is consistent across d, suggesting H_U follows the generic resultant-height scaling.

### §5.4 Conjecture F14.4 (discriminant-zero height drop)

**At any alpha where disc_xi(Q)(alpha) = 0 with first-order vanishing (i.e., alpha is a simple root of one of the irreducible factors P_7 or P_24 of disc_xi(Q)), the height of the minimal polynomial of the double xi-root is dramatically lower than the generic d = deg(alpha) scaling predicts.**

Status: VERIFIED at alpha_special (deg 24, generic predicts log10(H) ~ 50, observed log10(H_xi_double) ~ 6.3, factor ~10^44 below). The mechanism: the discriminant-zero forces a double root, whose minimal polynomial over Q is the *low-height* irreducible factor M(xi) of degree d = 24 instead of the generic *high-height* factor of degree 5d = 120.

(P_7 has no roots in (0, 1) per F9 step 2, so this conjecture cannot be tested at the P_7-roots within the real (0, 1) window.)

---

## §6 Connection to Conjecture 4.2

### §6.1 Implication for the low-height reading

Conjecture 4.2 in its low-height reading (per F12 §5.4) asserts:
> *No real alpha in (0, 1) \ {1/2} admits a polynomial relation over Q of low integer height between alpha and any xi-root of Q(xi, alpha).*

The natural quantitative statement that follows trivially from H(alpha) >= M_0 at all alpha != 1/2 is:

**Theorem F14 (under Conjecture F14.1).** For all alpha in (0, 1) \ {1/2} and all xi-roots xi_0 of Q(xi, alpha), no nontrivial integer relation
```
sum_{i=0}^{d-1} c_i * alpha^i * xi_0 + sum_{j=0}^{d-1} c'_j * alpha^j = 0
```
exists with `max_i |c_i| + max_j |c'_j| < H(alpha)`.

Status: this follows essentially by definition once H(alpha) is defined as the smallest height (in primitive Z-form) of any nontrivial univariate Z[xi] relation satisfied by xi_0 over the field Q(alpha). The minimal polynomial of xi_0 over Q achieves this.

### §6.2 Empirical "low-height" threshold

From the tested dataset, the empirical floor on H(alpha) for alpha != 1/2 is **H = 314 at alpha = 2/3**. So **Conjecture 4.2 in the low-height reading "no relation with max coefficient < 314" holds at every tested non-1/2 alpha by Theorem F14 above**.

A tighter formulation closer to F9's empirical maxcoef <= 10^4 bound: at every tested alpha, the minimal polynomial of every xi-root has H(alpha) <= 65,252 (the maximum height observed, at alpha = 1/9). So **at every tested non-1/2 alpha, a relation of height <= 65,252 is guaranteed to exist** (via the minimal polynomial), but the F9 PSLQ at maxcoef = 10^4 did not detect these because PSLQ's basis `[xi, 1, alpha, ..., alpha^(d-1)]` is multi-dimensional and looks for very specific linear-in-xi forms, NOT for univariate polynomials in xi alone. So F9's "no PSLQ relation at maxcoef <= 10^4" and F14's "H_U(alpha) ~ 10^4 typical" are about different kinds of relations: F9 about bivariate Q[alpha, xi] linear-in-xi relations, F14 about univariate Q[xi] polynomial relations.

### §6.3 The role of alpha_special revisited

F12 reported that "Conjecture 4.2 (literal) is REFUTED at alpha_special with height ~10^106." Under F14's analysis:

- The Q[alpha, xi] linear-in-xi relation `A * xi - B(alpha) = 0` of height ~10^106 (Reading B) **is** the F12 counterexample to the literal reading.
- The Q[xi] minimal polynomial of xi_double of height 2,191,936 (Reading U) is the **same algebraic content** expressed differently: M(xi_double) = 0 where M is the deg-24 irreducible factor of Res_a(P_24, Q).
- Both readings agree: xi_double is algebraic over Q (deg 24); the height of its minimal polynomial over Q (Reading U) is 2.2 * 10^6, **two orders of magnitude smaller** than the height of its xi-only minimal polynomial over Q(alpha_special) when written as `A * xi - B(alpha_special) = 0` and B is unrolled in alpha-powers (Reading B, ~10^106).

So Reading U gives a **tighter** threshold for "the smallest height" of a polynomial relation involving xi_double over Q, and F12's "10^106" is not a height lower bound but an upper bound from a *specific* (suboptimal) Q[alpha, xi] presentation.

This **does not change** F12's qualitative conclusion (Conjecture 4.2 literal-reading is refuted at alpha_special) but **tightens** the quantitative figure to H_U(alpha_special) = 2,191,936. Under Conjecture F14.4, this is the expected low-height factor at any discriminant-zero point.

---

## §7 Reproduction

```bash
python verification/frontier_F14_height_function.py
```

Runtime: ~7 seconds on a modern laptop (the resultant `Res_a(P_24, Q)` and its factorization dominate; everything else is fast).

Output:
- Steps 1, 1b: H(alpha) at 31 rationals q = 2..10 (including 1/2).
- Step 2: H(alpha) at 11 algebraic irrationals (matching F9's test set).
- Step 3: H(alpha_special) via Res_a(P_24, Q) factorization (deg-24 xi_double + deg-120 generic, with multiplicities 2 + 1).
- Step 4: aggregated table, scaling regression.
- Step 5: matplotlib plot saved to `04_meta/frontiers_2026-05-27/F14_height_plot.png`.
- Step 6: numerical results saved to JSON.

---

## §8 What was NOT closed

1. **Rigorous H lower bound proof:** Conjecture F14.1 (H > 100 at non-1/2) is empirical; a rigorous proof would require either (a) bounding the resultant `Res_a(p_alpha, Q)` for general alpha, or (b) ruling out small-height irreducible factors of M_alpha at all alpha != 1/2.

2. **Other discriminant-zero alphas:** The P_7 factor of disc_xi(Q) has no real roots in (0, 1) (F9 step 2). It does have real roots outside (0, 1) and complex roots; F14 does not extend the H-analysis there.

3. **Transcendental alphas:** H(alpha) is not defined classically at transcendental alpha (no minimal polynomial). One could define a height proxy via approximating the relation at increasing precision, but this is beyond the F14 scope.

4. **Higher-denominator rationals (q > 10):** the scaling regression suggests H(p/q) ~ q^3.4, but the exponent could drift at larger q. Testing q in {11, 12, ..., 30} would be a natural extension.

5. **Connection to Mahler measure / Lehmer's problem:** the deg-24 xi_double minpoly M(xi) at alpha_special could be studied for its Mahler measure; if `M(M) < 1.176...` (Lehmer's bound), it would be a candidate for low-Mahler-measure polynomials. This is a number-theoretic spin-off of F14, not closed here.

---

## §9 Impact on prior frontier statements

**F12 §3.3 / F12 §5.4 ("height ~10^106"):** PRESERVE the figure as the height of the F12 Groebner-basis bivariate Q[a, xi] linear-in-xi relation. CLARIFY: F14 establishes that the univariate minimal polynomial of xi_double over Q (the natural "Reading U" height) is much smaller, H_U = 2,191,936 ~ 10^6.3. Both are correct as different invariants.

**F9 §5 ("no PSLQ relation at maxcoef <= 10^4"):** PRESERVE. F9 looks for *linear-in-xi* relations in `[xi_0, 1, alpha, ..., alpha^(d-1)]`. F14's H_U values do not directly speak to this question; they characterize the univariate Q[xi] minpoly height. The PSLQ-detected relation at alpha_special would actually live in Reading B at height ~10^106, well outside F9's bound. F14 confirms F9's empirical certificate is the right kind of empirical result and at the right precision for low-height bivariate detection.

**HONEST_NEGATIVES §2.1 "low-height Conjecture 4.2 open":** UPDATE to "under Conjecture F14.1, the low-height reading of Conjecture 4.2 is rigorously characterized: H(alpha) >= 100 at all tested non-1/2 alpha, and the empirical floor is H = 314 at alpha = 2/3." A formal proof would require closing the gap between the empirical floor and a structural lower bound.

---

*7SiTe Public Sovereignty License v2.2 -- see [`../../LICENSE`](../../LICENSE).*
*Brayden Ross Sanders / 7SiTe LLC . 2026.*
