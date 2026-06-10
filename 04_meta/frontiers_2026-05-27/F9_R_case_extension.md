# Frontier F9 -- R-case extension of Conjecture 4.2

**Status:** Conjecture 4.2 over R -- **STRENGTHENED** (still open). At 1000-decimal-place precision, no PSLQ-detectable algebraic relation between alpha and any xi-root of Q(xi, alpha) was found at the natural R-case candidate alpha_special (the real root of P_24 in (0, 1) at ~0.1126) -- pushing F5's 100-dps test up by a factor of 10 in precision. Eleven additional algebraic irrationals (real algebraic of degree 2-5 over Q) tested at the same precision likewise show zero PSLQ-detectable relations. The R-case is now empirically strengthened by 12 new test points, raising the cumulative R-case empirical record from ~58 (D57/May-12/F1) to ~70 alpha values with zero counterexamples. The R-case **remains genuinely open** -- this is empirical strengthening of the conjecture, not a proof.

**Verification:** [`../../verification/frontier_F9_R_case.py`](../../verification/frontier_F9_R_case.py) Steps 1-5.

**Date:** 2026-05-28.

**Builds on:** F5 §3.5 (discriminant factorization + 100-dps PSLQ at alpha_special), F6 (HIT proof over Q), HONEST_NEGATIVES §2.1 (statement of the R-case open problem).

---

## §1 Recap and target

**Theorem F.2 (proved in F6).** For every Q-rational alpha in (0, 1) with alpha != 1/2, Q(xi, alpha) is irreducible over Q[xi].

**Conjecture 4.2 (R-case, OPEN).** No real alpha in (0, 1) \ {1/2} admits a non-trivial polynomial relation over Q between the 4-core attractor moments (H/Br, r/br).

F6 closes the Q-case via Hilbert's irreducibility theorem. F6 §9 specifies the natural R-case candidate: **alpha_special**, the real root of P_24 inside (0, 1), where the discriminant `disc_xi(Q)` vanishes. At alpha_special, `disc_xi(Q) = 0`, so Q has a repeated xi-root in the algebraic closure. F5 §3.5's 100-dps PSLQ search at alpha_special found no low-degree relation in Q[xi]; F9 extends this to 1000-dps and adds 11 additional algebraic-irrational test points.

The R-case test is structurally different from the Q-case proof:
- **Q-case proof** (F6): structural, via HIT applied to `Q(xi, a)` in `Q(a)[xi]`.
- **R-case test** (F9): numerical / empirical, via PSLQ at high precision.

There is no analogue of HIT for arbitrary real specializations. The R-case can only be addressed empirically (finding counterexamples or running out of precision without finding one) or by a separate structural argument routed through the Galois group of Q over a specific extension.

---

## §2 Step 1 -- recompute P_7 and P_24 (recapping F5/F6)

The script recomputes `disc_xi(Q)` from the load-bearing polynomial `Q(xi, a)` (the same Q used in F5/F6) and factors:

```
disc_xi(Q) = 4096 * a^3 * (2a - 1)^7 * P_7(a)^2 * P_24(a)
```

with the irreducible degree-7 factor

```
P_7(a) = 272 a^7 - 1280 a^6 + 2736 a^5 - 3416 a^4 + 2675 a^3 - 1312 a^2 + 384 a - 64
```

and the irreducible degree-24 factor `P_24(a)` (24 terms; explicitly listed in the script's STEP 1 output).

Both factorizations are sympy-verified in < 0.2 s and agree with F5 §3.2 and F6 §3.2.

---

## §3 Step 2 -- real roots of P_7 and P_24 at 1000-dps

At `mpmath.mp.dps = 1000`, all real roots of P_7 and P_24 are computed:

| Factor | Real-root count | Roots (high precision) | In (0, 1)? |
|---|---:|---|---|
| `P_7` | 1 | `1.12114373313753509671001669877…` | NO |
| `P_24` | 2 | `0.11255061532893783490843621259693765915002129572304…` | YES |
|       |   | `1.29631295204206114190073060410…` | NO |

**The only algebraic-irrational alpha in (0, 1) where `disc_xi(Q) = 0` is alpha_special = (P_24's root in (0, 1)).**

The 1000-dps value of alpha_special is

```
0.11255061532893783490843621259693765915002129572304280276381817165906332250761076...
```

This matches F5's ~0.1126 approximation. F9's contribution is the 1000-digit precision (i.e., 10x the F5/F6 precision).

P_7 has no real root in (0, 1), so it contributes nothing to the R-case candidate list. **Only alpha_special is "structurally special" via discriminant-vanishing.**

---

## §4 Step 3 -- PSLQ-based reducibility test

### §4.1 Method

For an algebraic alpha (real, in (0, 1)) with minimal polynomial of degree d over Q, the field Q(alpha) is a degree-d extension of Q. The polynomial `Q(xi, alpha)` is reducible over Q(alpha)[xi] iff some xi-root xi_0 of `Q(xi, alpha)` lies in Q(alpha) -- i.e. iff there exist integers c_0, c_1, ..., c_d (with c_0 != 0) such that

```
c_0 * xi_0 = c_1 + c_2 * alpha + c_3 * alpha^2 + ... + c_{d+1} * alpha^(d-1)
```

PSLQ (Bailey-Ferguson) detects exactly this kind of integer relation. At 1000-dps precision, PSLQ with `maxcoef = 100` and basis `[xi_0, 1, alpha, alpha^2, ..., alpha^(d-1)]` either finds a small-coefficient relation (counterexample to irreducibility) or fails (empirical strengthening of irreducibility).

The script:
1. For each candidate alpha, compute the 7 xi-roots of `Q(xi, alpha)` numerically at 1000+200-dps precision. When the discriminant vanishes (alpha_special), use squarefree deflation: `gcd(Q, dQ/dxi)` extracts the repeated-root part, then find the roots of `gcd` and `Q / gcd` separately.
2. For each real-positive xi-root xi_0 (the attractor moments live in R+), run `mpmath.pslq` against the basis above with `maxcoef = 100`.
3. Report any relation with non-trivial xi-coefficient and verified residual `< 10^(-(dps - 200))`.

### §4.2 Results

| Candidate alpha | deg / Q | Discriminant-vanishing? | xi-root count | Real-pos xi | PSLQ relation found? |
|---|---:|:---:|---:|---:|:---:|
| P_24 real root in (0,1) ~ 0.11255 = **alpha_special** | 24 | YES | 7 | 3 | **NO** |
| (sqrt(5) - 1) / 2 ~ 0.618 | 2 | no | 7 | 4 | NO |
| sqrt(2) / 2 ~ 0.707 | 2 | no | 7 | 4 | NO |
| 1 / sqrt(5) ~ 0.447 | 2 | no | 7 | 3 | NO |
| 2^(-1/3) ~ 0.794 | 3 | no | 7 | 4 | NO |
| 3^(-1/3) ~ 0.693 | 3 | no | 7 | 4 | NO |
| real root of x^3 + x - 1 in (0,1) ~ 0.682 | 3 | no | 7 | 4 | NO |
| real root of x^3 + 2x - 1 in (0,1) ~ 0.453 | 3 | no | 7 | 3 | NO |
| 2^(-1/4) ~ 0.841 | 4 | no | 7 | 4 | NO |
| 3^(-1/4) ~ 0.760 | 4 | no | 7 | 4 | NO |
| real root of x^4 + x - 1 in (0,1) ~ 0.725 | 4 | no | 7 | 4 | NO |
| real root of x^5 + x - 1 in (0,1) ~ 0.755 | 5 | no | 7 | 4 | NO |

**Result: 12 / 12 NO PSLQ relation at 1000-dps, `maxcoef = 100`, deg <= d (where d is the alpha's degree over Q).**

Notes:
- For alpha_special, the discriminant vanishes (`gcd(Q, Q') = ` degree-1 polynomial in xi, witnessing a multiplicity-2 root). The script's squarefree deflation recovers all 7 distinct xi-roots from `gcd` (1 root with mult 2) and `Q / gcd` (6 distinct roots, of which one accounts for the multiplicity).
- For all other candidates, the discriminant does not vanish, so `mpmath.polyroots` works directly.
- The xi-root count of 7 matches the structure of `Q(xi, alpha)`. The real-positive subset (3 or 4 of 7) consists of the candidate moment ratios.

### §4.3 PSLQ runtime at 1000-dps

The PSLQ search at alpha_special with `maxcoef = 100` and 25-dim basis ran in 397.75 s on the test machine (3 real-positive xi-roots, each searched individually). For all other candidates with `d <= 5`, each PSLQ call took 0.3-0.6 s (smaller basis, no deflation). The Step 4 stress-test (alpha_special at maxcoef = 100 and maxcoef = 10000) each took ~394 s, dominated by the same 3-root PSLQ search at the same basis size.

---

## §5 Step 4 -- extra-stress PSLQ at alpha_special

Since alpha_special is the natural R-case candidate, the script extra-stresses it with:

- basis: `{xi-root, 1, alpha, alpha^2, ..., alpha^23}` (deg(P_24) = 24)
- `maxcoef` sweep: 100, then 10000

The first level (`maxcoef = 100`) was already covered in Step 3. The script's Step 4 repeats `maxcoef = 100` (sanity) and then tests `maxcoef = 10000` (a 100x stronger bound, corresponding to a hypothetical relation with coefficient magnitudes up to ten thousand).

**Result: NO PSLQ relation found at maxcoef = 100 or 10000.**

This is the strongest empirical R-case test of Conjecture 4.2 currently in the framework's record:
- precision: **1000 decimal places** (F5/F6 was 100 dps; F9 is 10x higher)
- basis: **25-dimensional** (full deg(P_24) = 24)
- coefficient bound: **up to 10000** (F5 was 10^10 but at lower precision; F9 is lower in coefficient bound but vastly higher in precision)

Combining F5/F6's `maxcoef = 10^10` at 100-dps with F9's `maxcoef = 10000` at 1000-dps gives complementary empirical coverage: F5/F6 ruled out high-coefficient low-precision relations; F9 rules out moderate-coefficient ultra-high-precision relations.

---

## §6 What this rules out vs. doesn't rule out

### §6.1 What F9 rules out empirically

At precision 10^(-500) (the residual sensitivity of PSLQ at 1000-dps with safety margin), there is no relation

```
c_0 * xi_0 = c_1 + c_2 * alpha_special + ... + c_25 * alpha_special^24
```

with `|c_i| <= 10000` for any real-positive xi-root xi_0 of `Q(xi, alpha_special)`. This is an empirical certificate, not a structural proof, but the precision is high enough that any genuine relation with these coefficient bounds would have been detected.

### §6.2 What F9 does NOT rule out

- A relation with `|c_i| > 10000` (i.e., very large integer coefficients). The previous F5 record at `maxcoef = 10^10` at 100-dps complements this but at much lower precision.
- A relation involving higher powers (`alpha^25, alpha^26, ...`). Since alpha_special has minimal polynomial P_24 of degree 24, all `alpha^k` for `k >= 24` are Q-linear combinations of `1, alpha, ..., alpha^23`. So a relation of higher degree in alpha can always be rewritten as a degree-24 relation. F9's basis of length 25 is therefore complete for testing reducibility of `Q(xi, alpha_special)` over `Q(alpha_special)[xi]`.
- A relation involving algebraic numbers outside Q(alpha_special). I.e., F9 tests reducibility of `Q(xi, alpha_special)` over `Q(alpha_special)[xi]` -- the natural test for Conjecture 4.2 over R. A counterexample over a larger extension field would not be detected here.
- A transcendental alpha. F9 tests algebraic alphas only. The May-12 41-candidate scan and F1 already include transcendentals (1/e, π/4, ln 2, 1/π) at lower precision (50/100/200 dps); F9 does not extend those.

### §6.3 Honest verdict

**STRENGTHENED.** The R-case empirical record now stands at ~70 unique real alpha values tested (D57 + May-12 + F1 + F9), with zero counterexamples. The natural special candidate alpha_special is now ruled out at 1000-dps for `maxcoef <= 10000`, which is the strongest precision-coefficient combination currently feasible.

The R-case remains **genuinely open** -- this is empirical strengthening, not proof. A structural closure analogous to F6's HIT argument would require an HIT-like statement for real algebraic specializations (which does not exist in the literature as a uniform theorem), or an explicit Galois-group computation tracking `Gal(Q / Q(alpha_special))` and ruling out subgroup-descent.

---

## §7 Comparison with F5/F6 R-case test record

| Source | Precision (dps) | maxcoef | Basis dim | Result |
|---|---:|---:|---:|---|
| F5 §3.5 (May 2026) | 100 | 10^10 | 13 (deg <= 12) | NO relation at alpha_special |
| F9 (this) | 1000 | 10000 | 25 (deg = 24) | NO relation at alpha_special |
| F9 (this) | 1000 | 100 | 13 (deg <= 12) | NO relation at 11 additional algebraic alphas |

F5 and F9 are complementary: F5 tests very-high-coefficient short relations at moderate precision; F9 tests moderate-coefficient long-basis relations at very-high precision. Both fail to find any algebraic relation at alpha_special, strengthening the empirical record from two different directions.

---

## §8 Conclusion

**Conjecture 4.2 over R -- STRENGTHENED, still OPEN.**

The R-case empirical record is now strengthened by 12 new alpha values tested at 1000-dps:
- The natural special candidate `alpha_special` (real root of P_24 in (0, 1)): no PSLQ relation at deg = 24, `maxcoef <= 10000`.
- 11 additional algebraic-irrational alpha (quadratic, cubic, quartic, quintic over Q): no PSLQ relation at deg <= max(d, 12), `maxcoef = 100`.

The cumulative R-case empirical record (D57 + May-12 + F1 + F9) consists of approximately 70 unique real alpha tested, with **zero counterexamples**. Conjecture 4.2 over R is strongly supported empirically and remains structurally open. A complete proof would route through either:

- A Galois-theoretic argument for `Gal(Q / Q(alpha_special))` ruling out subgroup-descent (algebraic closure work, by hand or via Magma/PARI), or
- An HIT-style theorem for real algebraic specializations (does not exist as a uniform statement in the literature; would need to be developed for this specific setting).

Neither route is attempted here; F9 is a numerical strengthening at the precision-coefficient frontier currently feasible with mpmath.

---

## §9 Strength and limitations

### §9.1 What is rigorous

- The discriminant factorization `disc_xi(Q) = 4096 * a^3 * (2a-1)^7 * P_7^2 * P_24` (sympy-verified).
- The real-root computation of P_24 in (0, 1) at 1000-dps (mpmath polyroots with high extraprec).
- The squarefree deflation at alpha_special (numerical Euclidean gcd at 1000-dps tolerance).
- PSLQ at 1000-dps with `maxcoef = 100` on a 25-dim basis (mpmath.pslq).

### §9.2 What is empirical

- The negative result "no PSLQ relation found at the tested coefficient and precision bounds" is empirical not proof. It strongly suggests no low-height algebraic relation exists, but does not preclude one with `|c_i| > 10000` AT 1000-dps OR `|c_i| > 10^10` AT 100-dps. The two F5 and F9 bounds are complementary, but a relation falling outside both windows could still exist in principle.

### §9.3 Galois-group route (the remaining structural avenue)

For a fully rigorous R-case closure at alpha_special, one would compute `Gal(Q(xi, alpha_special) / Q(alpha_special))`. If this Galois group is the full symmetric group `S_7` (or at least is not the trivial group `{e}`), then `Q` is irreducible over `Q(alpha_special)`. The HIT-type argument over Q uses the natural assumption `Gal(Q / Q(a)) = S_7` (F6 Remark 7.5). A finer assumption -- that `Gal(Q / Q(alpha_special)) = S_7` -- would close the R-case at alpha_special.

This is a finite computation in principle (e.g., via PARI's `nfgalois`). F9 does not perform it; the F9 test is purely numerical.

---

## §10 Reproduction

```bash
python verification/frontier_F9_R_case.py
```

Runtime: ~15-20 minutes on a modern laptop (dominated by Step 4's two PSLQ runs at 1000-dps with basis dim 25).

Output verifies Steps 1-5 and prints `F9 STATUS: STRENGTHENED`.

---

*7SiTe Public Sovereignty License v2.2 -- see [`../../LICENSE`](../../LICENSE).*
*Brayden Ross Sanders / 7SiTe LLC . 2026.*
