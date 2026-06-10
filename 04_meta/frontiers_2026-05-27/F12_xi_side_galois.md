# Frontier F12 -- xi-side Galois group: Gal(Q(xi, alpha_special)/Q(alpha_special))

**Status:** Conjecture 4.2 over R at alpha_special -- **NEEDS-REFINEMENT** (literal version refuted; low-height version unchanged).

Computing the xi-side Galois group of the F5/F6 polynomial Q(xi, a) specialized at alpha = alpha_special revealed two structurally distinct findings:

1. **Q(xi, alpha_special) is REDUCIBLE over Q(alpha_special)**: it factors as `c * (xi - xi_double)^2 * h(xi)` where `xi_double` is an explicit Q-rational polynomial expression in alpha_special of degree 23, with massive coefficients of magnitude ~10^106. This is a Tier-A finding via Groebner basis over Q[a, xi].

2. **Gal(h(xi) / Q(alpha_special)) = S_5** at Tier-A: the "remaining" degree-5 factor h(xi) over Q(alpha_special) has Galois group the full symmetric group on 5 elements, established via Frobenius cycle-type sampling at 2000 "special fiber" primes (chi-square distance 11.1 to S_5 theory, with all 7 cycle types observed including 3-cycles, 4-cycles, 5-cycles, and odd-parity permutations).

The structural reducibility at item 1 was *missed* by F9's PSLQ search at maxcoeff = 10000 because the integer relation `A * xi - B(alpha) = 0` has |coefficients| up to ~10^106 — 102 orders of magnitude above F9's PSLQ ceiling. F9's negative result is correct as an empirical certificate (no relation at maxcoeff ≤ 10000) but does not generalize to higher heights. F10's Tier-A closure relied on a structural assumption that fails (see §6 below).

**Verification:** [`../../verification/frontier_F12_xi_side_galois.py`](../../verification/frontier_F12_xi_side_galois.py) Steps 1-6.

**Date:** 2026-05-28.

**Builds on:** F5 (discriminant factorization, including foreshadowing in §3.5 that alpha_special is a place of double-root structure), F6 (HIT proof over Q), F9 (PSLQ R-case empirical), F10 (alpha-side S_24 Galois closure).

---

## §1 Q(xi, alpha_special) -- explicit form

The load-bearing polynomial `Q(xi, a)` from F5/F6 is

```
Q(xi, a) = 4*a^4*xi^6 - 8*a^4*xi^5 - 16*a^4*xi^4 + 16*a^4*xi^3 + 16*a^4*xi^2 - 64*a^4*xi
         - 2*a^3*xi^7 + 28*a^3*xi^5 - 12*a^3*xi^4 - 16*a^3*xi^3 + 32*a^3*xi^2 + 160*a^3*xi
         + 3*a^2*xi^7 - 13*a^2*xi^6 - 12*a^2*xi^5 + 64*a^2*xi^4 - 84*a^2*xi^3 - 108*a^2*xi^2 - 144*a^2*xi + 16*a^2
         - a*xi^7 + 8*a*xi^6 - 8*a*xi^5 - 27*a*xi^4 + 100*a*xi^3 + 52*a*xi^2 + 40*a*xi - 16*a
         - 20*xi^3 + 4.
```

It has degree 7 in xi over Q(a), with leading coefficient `lc_xi(Q) = -2*a^3 + 3*a^2 - a = -a*(2a-1)*(a-1)`. At alpha = alpha_special in (0, 1) \ {1/2, 1}, this leading coefficient is nonzero, so Q(xi, alpha_special) is genuinely of degree 7 in xi.

alpha_special is the unique real root of P_24 in (0, 1):
```
alpha_special = 0.11255061532893783490843621259693765915002129572304...
              (200-dps from F9 / F10, identical to F9 Step 2 output)
```

---

## §2 Irreducibility STATUS -- structural reducibility detected

**F5/F6 discriminant factorization:**
```
disc_xi(Q) = 4096 * a^3 * (2a-1)^7 * P_7(a)^2 * P_24(a).
```

At alpha = alpha_special, P_24(alpha_special) = 0, so `disc_xi(Q)(alpha_special) = 0`.

Since P_24 appears with multiplicity **1** (not 2) in disc_xi(Q), the discriminant of Q(xi, alpha_special) (viewed as a degree-7 polynomial in xi over Q(alpha_special)) vanishes to first order. By the standard theory of polynomial discriminants:

- `disc(f) = 0` iff `f` has a multiple root in the algebraic closure of its coefficient field.
- The order of vanishing equals (total multiplicity) - (number of distinct roots).
- First-order vanishing means exactly **one double root + 5 simple roots**, total `2*1 + 1*5 = 7`.

**Therefore Q(xi, alpha_special) has exactly 1 double xi-root and 5 simple xi-roots, hence is NOT separable as a degree-7 polynomial.** In characteristic zero, non-separable polynomials must factor (multiplicity > 1 in any irreducible factor over Q would contradict separability of the irreducible factor). So:

**Q(xi, alpha_special) is REDUCIBLE over Q(alpha_special).**

This was foreshadowed in F5 §3.5: *"The algebraic-irrational alpha_special is structurally identified as a place where Q has a repeated root in xi."* F5 noted this was not a counterexample to the Q-rational version of Conjecture 4.2 (since alpha_special is irrational), but did not check whether the double root xi_double lies in Q(alpha_special).

F12 closes that gap.

---

## §3 Galois group computation method -- Step A (double root locus)

### §3.1 Groebner basis extraction

We compute the lex Groebner basis (xi > a) of the ideal
```
I = (Q(xi, a), dQ/dxi(xi, a), P_24(a)) in Q[a, xi].
```

This ideal vanishes simultaneously when (i) Q(xi, a) has a multiple root in xi at the given alpha, and (ii) alpha is a root of P_24. Geometrically, this is the locus on the (alpha, xi)-plane where Q's "branched cover" of the alpha-line has a discriminant zero at alpha_special.

**Output (sympy, 1.4 s):** the Groebner basis collapses to exactly two generators:

| # | Form | Degree in xi | Degree in a |
|---:|---|---:|---:|
| 1 | `A * xi + B(a)` | 1 | 23 |
| 2 | `P_24(a)` | 0 | 24 |

where A is a positive 99-digit integer constant and B(a) is a polynomial in a of degree 23 with 99-106-digit integer coefficients.

**Tier-A consequence:** modulo P_24(a) = 0, the relation `A * xi + B(a) = 0` is forced. Therefore the double-root xi-value at alpha_special is
```
xi_double = -B(alpha_special) / A   in Q(alpha_special).
```

### §3.2 Numerical verification

| Method | xi_double (40 digits) | Residual |
|---|---|---|
| Direct: gcd(Q, dQ/dxi) at alpha_special at 200 dps | 5.7637921994924929178470812518559222609057... | -- |
| Via Groebner: -B(alpha_special) / A | 5.7637921994924929178470812518559222609057... | < 1e-30 |

The two values agree to 30+ decimal places. The Groebner-basis expression is the algebraic identification; the gcd computation is the numerical verification.

### §3.3 The constant A and polynomial B(a)

The integer constant A:
```
A = 148880526521725531642534638575984632189296653411916001813629270619819099994773492768304903785650000
  (99 decimal digits, 327 bits)
```

A factorization shows `A = 2^4 * 5^4 * ... * 17^7 * ...` (full factorization output omitted; checked via sympy.factorint to have all small prime factors).

The polynomial B(a) has 24 nonzero coefficients of magnitude 10^99 - 10^106, of which the largest is at `a^9` with absolute value ~2.02e+105. The integer relation
```
A * xi - B(alpha_special) = 0     <=>     xi_double = B(alpha_special) / A
```
is a polynomial-over-Q relation of total height O(10^106).

**This is the relation F9 could not find:** F9's PSLQ was set with `maxcoeff = 10000 = 10^4`, missing by 102 orders of magnitude.

---

## §4 Galois group result -- Step B (residual degree-5 factor h)

Having identified xi_double explicitly, we extract the residual degree-5 factor
```
h(xi) = Q(xi, alpha_special) / (xi - xi_double)^2
```
which is a polynomial of degree 5 in xi over Q(alpha_special).

### §4.1 Numerical structure of h

At alpha_special at 200 dps:
- h has degree 5 in xi (verified by polynomial division residual ~10^-191).
- The 5 xi-roots of h are: 1 real (~0.8898) and 2 complex-conjugate pairs (~-0.27 +- 0.43i and ~-1.19 +- 1.66i).

### §4.2 Galois group of h via Frobenius-cycle sampling

For each prime p that doesn't divide `lc(P_24) * disc(P_24)`, we factor `P_24 mod p` in F_p[a]. When a linear factor exists, we can substitute the corresponding `alpha_modp` into Q and look for a "special fiber" prime: one where Q(xi, alpha_modp) mod p has a double xi-root in F_p (i.e., the same "discriminant-zero locus" structure as alpha_special).

At each such special-fiber prime, we extract `xi_double_modp` (the unique double xi-root mod p), divide Q by `(xi - xi_double_modp)^2`, and factor the residual h_modp in F_p[xi]. The factorization pattern is the cycle type of the Frobenius element acting on the 5 xi-roots of h over Q(alpha_special).

**Sampling scope:** 2000 special-fiber primes found in 3210 processed primes (~62.3% hit rate). Runtime ~75 s on a modern laptop.

### §4.3 Observed cycle-type spectrum

The cycle-type spectrum of Frobenius acting on the 5 xi-roots of h, observed at 2000 special-fiber primes:

| Cycle type | Observed | Frequency | S_5 theory |
|---:|---:|---:|---:|
| `(1,1,1,1,1)` | 26 | 0.0130 | 0.0083 |
| `(1,1,1,2)` | 178 | 0.0890 | 0.0833 |
| `(1,1,3)` | 359 | 0.1795 | 0.1667 |
| `(1,2,2)` | 237 | 0.1185 | 0.1250 |
| `(1,4)` | 506 | 0.2530 | 0.2500 |
| `(2,3)` | 323 | 0.1615 | 0.1667 |
| `(5,)` | 371 | 0.1855 | 0.2000 |

Chi-square distance to S_5 theory: **11.145** (df = 6; critical chi^2 at p=0.05 is 12.59). Comfortable fit.

### §4.4 Tier-A deduction

**Step (a) Containment check:** Gal(h/Q(alpha_special)) is contained in...

| Group | Allowed cycle types | Compatible? |
|---|---|:---:|
| Z/5 | {e, (5)} | NO (extras: (1,1,2), (1,1,3), (1,2,2), ...) |
| D_5 | {e, (5), (1,2,2)} | NO (extras: (1,1,2), (1,1,3), (1,4)) |
| F_20 = AGL(1,5) | {e, (5), (1,2,2), (1,4)} | NO (extras: (1,1,2), (1,1,3), (2,3)) |
| A_5 | even-parity types | NO (extras: (1,1,2), (1,4), (2,3)) |
| S_5 | all | YES |

**Step (b) Parity:** 3 odd-parity cycle types observed `{(1,1,2), (1,4), (2,3)}`, with 1007 of 2000 primes (50.3%) carrying odd Frobenius. So Gal(h/Q(alpha_special)) is **NOT contained in A_5**.

**Step (c) Transitivity:** 5-cycle `(5,)` observed (371 times), so the action is transitive on the 5 xi-roots. (Note: transitivity also follows from the irreducibility of h over Q(alpha_special), which we are establishing simultaneously: the cycle-type spectrum forces all 5 xi-roots to be Galois-conjugate.)

**Step (d) Conclusion:** transitive + 5-cycle + 3-cycle + odd-parity rules out every proper transitive subgroup of S_5.

```
==> Gal(h(xi) / Q(alpha_special)) = S_5    (Tier-A).
```

---

## §5 R-case closure interpretation at alpha_special

### §5.1 What F12 proved

1. **Reducibility (Tier-A):** Q(xi, alpha_special) factors over Q(alpha_special) as
   ```
   Q(xi, alpha_special) = c * (xi - xi_double)^2 * h(xi)
   ```
   with `c = -2*alpha_special^3 + 3*alpha_special^2 - alpha_special` (the leading xi-coefficient of Q at alpha_special).

2. **Explicit double root (Tier-A):** `xi_double = -B(alpha_special) / A` is given by an explicit integer polynomial of degree 23 in alpha_special with integer coefficients of height ~10^106. Numerical value: `xi_double ~= 5.76379219949249291784708...`.

3. **Minimal polynomial of xi_double over Q (Tier-A):** the irreducible degree-24 factor of `Res_a(P_24(a), Q(xi, a))` in xi (denoted M(xi) here; with leading coefficient 5, constant term -16384). This is *not* equal to P_24, but generates *the same number field* (since both have degree 24 over Q and Q(xi_double) is a subfield of Q(alpha_special) and both have degree 24, so they coincide).

4. **xi-side Galois group of remaining roots (Tier-A):** `Gal(h(xi)/Q(alpha_special)) = S_5`.

5. **xi-roots of h NOT in Q(alpha_special):** since S_5 acts transitively on the 5 xi-roots with no fixed points (other than the trivial coset), none of the 5 simple xi-roots of Q(xi, alpha_special) lie in Q(alpha_special). Only xi_double does.

### §5.2 Reconciliation with F9 (PSLQ R-case test)

F9 found no PSLQ relation between alpha_special and any xi-root of Q(xi, alpha_special) at maxcoeff = 10000 and 1000-dps precision. F12 finds the relation has height ~10^106. So:

- **F9's empirical certificate stands at its stated coefficient bound:** no relation with |c_i| <= 10000 exists between alpha_special and any xi-root.
- **A relation does exist at |c_i| ~ 10^106**, courtesy of the structural double-root at alpha_special. F12 makes this explicit.

The two are not contradictory; F9's test was simply at the wrong height scale to detect the actual relation.

### §5.3 Reconciliation with F10 (alpha-side Galois closure)

F10 closed the alpha-side at Tier-A: Gal(P_24/Q) = S_24, so Q(alpha_special)/Q has no nontrivial proper subfields (other than the unique quadratic Q(sqrt(disc(P_24))) which doesn't lie inside Q(alpha_special) itself).

F10 §5.3's argument for R-case closure was:
> *"For xi_0 to live in Q(alpha_special), its minimal polynomial over Q would need degree d <= 7 (since xi_0 is a root of Q(xi, alpha_special), a deg-7 poly in xi) AND d | 24 (since Q(xi_0) is a subfield of Q(alpha_special), and S_24 has no proper subgroup between S_23 and S_24). The only d <= 7 with d | 24 is d = 1 (Q-rational), excluded by F5/F6. So xi_0 cannot live in Q(alpha_special)."*

**The flaw in this argument:** the claim "minpoly(xi_0) has degree <= 7 because xi_0 is a root of Q(xi, alpha_special)" is FALSE in general.

The minimal polynomial of xi_0 over **Q(alpha_special)** has degree dividing 7 (correct). But the minimal polynomial of xi_0 over **Q** can have *much higher* degree — namely, the degree of the irreducible factor of `Res_a(P_24, Q)` in xi that has xi_0 as a root. For xi_double, this irreducible factor has degree 24 (the irreducible deg-24 factor of `Res_a(P_24, Q)`, which we called M(xi) above).

So xi_double has minimal polynomial over Q of degree 24 — matching the degree of alpha_special, and indeed Q(xi_double) = Q(alpha_special). F10's degree-mismatch argument failed because it assumed xi-root degree over Q equals xi-root degree over Q(alpha_special), which is only true when the resultant Res_a(P_24, Q) is squarefree — but here it has a degree-24 factor with multiplicity 2 (the M(xi) factor squared) plus a degree-120 squarefree factor.

The presence of the multiplicity-2 factor is exactly the structural reflection of the double-root at alpha_special.

### §5.4 What this means for Conjecture 4.2 over R at alpha_special

There are two reasonable readings of Conjecture 4.2 over R:

**Reading 1 (literal):** "No real alpha in (0, 1) \ {1/2} admits a non-trivial polynomial relation over Q between alpha and the 4-core attractor moments (xi-roots of Q(xi, alpha))."

Under Reading 1, **F12 produces an explicit counterexample at alpha_special**: the integer polynomial relation
```
A * xi_double - B(alpha_special) = 0
```
with A and B explicit (height ~10^106) is a non-trivial polynomial relation. **Conjecture 4.2 in this literal reading is REFUTED at alpha_special.**

**Reading 2 (low-height):** "No real alpha in (0, 1) \ {1/2} admits a polynomial relation over Q of low integer height between alpha and any xi-root of Q(xi, alpha)."

Under Reading 2, F9 still stands as empirical evidence: no relation at maxcoeff <= 10000 exists at 1000-dps. **Conjecture 4.2 in this low-height reading remains intact** -- the actual relation is at height ~10^106, far above any "natural" low-height threshold and likely above all height bounds within physical-modeling relevance.

The framework's existing language sometimes adopts Reading 1 (strict) and sometimes Reading 2 (low-height empirical). F12 forces this distinction to become explicit. Whichever reading is preferred, F10's earlier statement of CLOSE-R-CASE-ENHANCED at alpha_special is now strictly incorrect under Reading 1, and is "empirically intact but no longer Tier-A structural" under Reading 2.

---

## §6 Conclusion -- NEEDS-REFINEMENT

**Headline:** The xi-side Galois group `Gal(Q(xi, alpha_special) / Q(alpha_special))` is NOT a single transitive group on 7 roots — it is the trivial group on the double-root xi_double (which lies in Q(alpha_special)) **direct-product** the full symmetric group **S_5** on the remaining 5 simple xi-roots. The "S_5 piece" is identified at Tier-A; the "Q(alpha_special) piece" is identified at Tier-A via explicit Groebner-basis polynomial expression.

**Summary table:**

| Component | Status | Method | Tier |
|---|---|---|---|
| Q(xi, alpha_special) reducible over Q(alpha_special) | PROVED | disc_xi(Q) vanishes to first order at alpha_special | A |
| Double xi-root xi_double in Q(alpha_special) | PROVED | Groebner basis, explicit polynomial expression | A |
| `Gal(h(xi) / Q(alpha_special)) = S_5` | PROVED | Frobenius cycle-types + Jordan + parity | A |
| 5 simple xi-roots of Q(xi, alpha_special) NOT in Q(alpha_special) | PROVED | S_5 transitivity on the 5 roots | A |
| Conjecture 4.2 (literal R-case) at alpha_special | REFUTED | explicit Q-polynomial relation, height ~10^106 | A |
| Conjecture 4.2 (low-height R-case at alpha_special) | unchanged | F9 PSLQ at maxcoeff <= 10000 still passes | empirical |

**Net F12 verdict:** **COUNTEREXAMPLE-FOUND** (literal reading) / **NEEDS-REFINEMENT** (with reading distinction made explicit).

The honest framework status:
- Conjecture 4.2 over R as previously written needs a height qualifier added (Reading 2).
- The Galois-structural closure of the alpha-side (F10) stands but its R-case implication (F10 §5.3) was based on a flawed degree-mismatch argument and must be retracted.
- The xi-side Galois group is "S_5 on the residual 5 roots, with the 7th and 8th 'roots' being the double xi-root that lives in Q(alpha_special)." This is a finer structure than naive 7-root analysis predicted.

---

## §7 Reproduction

```bash
python verification/frontier_F12_xi_side_galois.py
```

Runtime: ~80 seconds on a modern laptop (dominated by Step 4's 2000-prime Frobenius sampling at p ≤ 500000).

Output includes:
- the Groebner-basis double-root extraction (Step 3, sub-second);
- the cycle-type spectrum table on 2000 special-fiber primes;
- the Tier-A deduction `Gal(h/Q(alpha_special)) = S_5`;
- the structural reinterpretation of F10's R-case implication.

---

## §8 What was NOT closed

1. **xi-side group action structure beyond S_5:** the precise abstract group structure of the *full* Galois action on Q(xi, alpha_special)/Q(alpha_special) is the trivial group on the xi_double "factor" times S_5 on the h-factor — i.e., {1} × S_5 ~= S_5 in total. This is what F12 reports. But the *embedding* of S_5 into the deeper structure Gal(splitting_field(Q)/Q) over alpha-conjugates of alpha_special is a finer question (the deg-120 factor of Res_a(P_24, Q) has its own Galois group over Q, which by transitivity factors through S_24 on the alpha-fibers and "fiber-wise" something containing S_5).

2. **Other algebraic alphas:** F12 only analyzes alpha_special. The 11 other algebraic-irrational alphas tested by F9 do not have the discriminant-zero property (i.e., Q(xi, alpha) is separable in xi for them), so the F12 method (Groebner + cycle-type on the "special fiber") does not apply directly. Standard Frobenius-cycle on Q(xi, alpha_other) over Q(alpha_other) for those alphas would be a separate analysis.

3. **Transcendental alphas:** F12 says nothing about transcendentals. The earlier F1 / D57 scans address these empirically only.

4. **Existence of "low-height" R-case counterexamples beyond alpha_special:** F12 only finds the high-height (10^106) counterexample at alpha_special. F9's empirical scan at maxcoeff <= 10000 already rules out low-height counterexamples for the tested alpha set; F12 does not extend this.

---

## §9 Impact on prior frontier statements

**F10 §5.3 / F10 Verdict (CLOSE-R-CASE-ENHANCED at alpha_special):** RETRACT. F10's argument that "no irrational xi_0 of Q(xi, alpha_special) can lie in Q(alpha_special)" used a degree-mismatch argument that silently assumed disjoint minpoly degrees over Q vs over Q(alpha_special). The double-root xi_double has minpoly degree 24 over Q (matching alpha_special) and minpoly degree 1 over Q(alpha_special), so the argument's premise fails.

**F9 §6 / F9 Verdict (STRENGTHENED at maxcoeff <= 10000):** PRESERVE. F9's empirical certificate is correct at its stated coefficient bound; F12 simply shows that bound was too restrictive to detect the actual relation. F9 remains a valid empirical strengthening for "no LOW-height polynomial relation exists".

**F5 §3.5 "alpha_special is not a counterexample over Q":** PRESERVE. F5 correctly noted alpha_special is irrational (so it's not a Q-rational counterexample) and didn't claim more. The R-case identification of alpha_special as a place of double-root structure was correct; F12 closes the open question of whether the double root lies in Q(alpha_special).

**HONEST_NEGATIVES §2.1 (Conjecture 4.2 R-case open):** UPDATE. The status changes from "OPEN" to "literal reading REFUTED at alpha_special; low-height reading still OPEN".

---

*7SiTe Public Sovereignty License v2.2 -- see [`../../LICENSE`](../../LICENSE).*
*Brayden Ross Sanders / 7SiTe LLC . 2026.*
