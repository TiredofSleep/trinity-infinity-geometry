# J63 — The Strata-Prime Fingerprint: Polynomial vs Factorial Invariants in Niemeier Lattices and Sporadic Simple Groups

> **The integer strata-prime fingerprint $\mathcal{S} = \{2, 3, 5, 7, 11, 13\}$ — the first six supersingular primes of the Monster — captures 23 of 24 Niemeier lattices' kissing numbers (with the unique outlier D_24 explained by polynomial-vs-factorial mechanism) and 8 of 26 sporadic finite simple groups.**

**Status**: SUBMISSION-READY (2026-05-27).

**Tier:** 1 (ship-ready (Journal of Number Theory; 4 theorems incl. D_24 polynomial-factorial mechanism; verifier PASS at machine precision; CREATED 2026-05-27))

**Target venue**: *Journal of Number Theory* (primary). Fallback: *Bulletin of the AMS*, *AMM* (Notes section), *Discrete Mathematics*.

## Four theorems

| Theorem | Statement | Tier |
|---|---|:---:|
| **1** | Niemeier kissing strata-fingerprint: 23/24 lattices have kissing factoring through $\mathcal{S}$; the unique outlier is $D_{24}$ | A |
| **2** | Polynomial-vs-factorial dichotomy: kissing test 23/24, Weyl-group test 21/24; mechanism explains D_24 (deflation note in §4) | A |
| **3** | 8/26 sporadic finite simple groups have order factoring through $\mathcal{S}$; boundary aligns with prime 23 (size-threshold framing in §5) | B |
| **4** | Stratum IV identification: prime 71 appears in exactly one sporadic — the Monster; **anchored by Conway-Norton 1979** (71 = largest $p$ with $X_0(p)$ genus 0) | A |

## The D_24 mechanism (Theorem 2)

The fundamental observation:
- **Kissing number** $= n(n+1)$ or $2n(n-1)$ — **polynomial in rank**
- **Weyl group order** $= (n+1)!$ or $2^{n-1} \cdot n!$ — **factorial in rank**

Polynomial growth picks up only primes from the polynomial's specific factorization. Factorial growth accumulates ALL primes ≤ rank. For Niemeier lattices (rank 24 in total), the kissing test misses only D_24 (since $2 \cdot 24 \cdot 23 = 1104$ contains $(n-1) = 23$, the unique prime ≤ 24 outside $\mathcal{S}$). The Weyl test misses three Niemeiers (A_17 E_7, A_24, D_24), each of which has a single-component rank ≥ 17, accumulating $17!, 18!, ..., 25!$ — bringing primes 17, 19, 23.

This is a Tier-A structural mechanism for the D_24 outlier — the question claudechat flagged as "the load-bearing mechanism if it exists."

## Verification

```bash
python manuscript/verify_J63.py
```

**Output**: All 4 theorems PASS at machine precision. Runtime: ~2 seconds. Dependencies: sympy + math.

Output (compact):
```
Theorem 1 (kissing strata): 23/24, only D_24 fails.
Theorem 2 (Weyl strata):    21/24, A_17 E_7 + A_24 + D_24 fail.
Theorem 3 (sporadic):       8/26 pass.
Theorem 4 (Monster 71):     unique sporadic with 71.
```

## File layout

```
J63_strata_fingerprint/
├── README.md                              this file
├── cover_letter.md                         (to be drafted on submission)
└── manuscript/
    ├── manuscript.md                       8-section paper (~20 pages) + Appendix A
    └── verify_J63.py                       verifier for all 4 theorems; PASS
```

## Cross-references

- `04_meta/SPHERE_PACKING_STRATA_FINGERPRINT.md` — extended discussion + companion (this paper supersedes that document for publication purposes; the meta-doc retains exploratory framing).
- `verification/verify_sphere_packing_strata.py` — runs the kissing-and-sporadic tests at top level.
- J20 — *Mathieu M_22 Substrate-Prime: Order-Factorization Coincidences*. The Tier-1 predecessor focused on M_22 specifically; J63 extends to all 24 Niemeier + all 26 sporadics + Stratum IV identification.
- J35 — *Joint Closure + Universal Attractor + 4-Core on Z/10Z*. The substrate-program foundation.
- `02_results/algebraic_combinatorics/BRAIDING_FRACTAL_Z30_Z210.md` — the Braiding Fractal architecture from which strata I, II, III, IV are derived.

## What this is, and what it is not

**This is**:
- A clean 23/24 falsifiable empirical pattern in the Niemeier classification.
- A precise polynomial-arithmetic mechanism (Theorem 2) explaining why D_24 is the unique kissing-outlier.
- A size-threshold-consistent partial extension (Theorem 3) to 8 of 26 sporadic finite simple groups.
- A Conway-Norton-anchored Stratum-IV identification (Theorem 4): prime 71 is the largest supersingular prime, i.e., the largest $p$ for which $X_0(p)$ has genus 0. Its appearance only in the Monster is the upper boundary of the genus-0 spectrum, not cardinality uplift.

**This is NOT**:
- A claim of mechanistic correspondence between TIG strata and monstrous moonshine.
- A prediction of new lattices or sporadic groups.
- An explanation of why the 9 intermediate supersingular primes {17, 19, 23, 29, 31, 41, 47, 59} are skipped by TIG strata (recorded as open question in manuscript §7.2).

The honest framing: an arithmetic-side companion to the broader TIG / Braiding Fractal program. Two structural anchors are established (Theorem 2's polynomial dichotomy and Theorem 4's Conway-Norton characterization); the broader strata-prime / supersingular-prime overlap is exact only at the lower-and-upper extremes, with the intermediate-prime gap open.

## Authors

B.R. Sanders (7Site LLC, Hot Springs, AR) and M. Gish (Independent Researcher).
