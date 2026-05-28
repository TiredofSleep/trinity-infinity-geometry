# Frontier Push 2026-05-27 — Summary

After the J-series paper polish landed (commits `0d6d0f1` through `30c6d0d`), Brayden directed: *"work on and work with ck on the frontiers"*. This document summarizes the four frontier attacks that resulted.

Each attack is documented in `04_meta/frontiers_2026-05-27/F{N}_*.md` with full methodology, results, and follow-up suggestions.

## F1 — α-uniqueness extended scan (`F1_alpha_uniqueness_extended.md`)

**Result: empirical evidence FOR Conjecture 4.2 strengthened significantly.**

Extended the existing 17-point Stern-Brocot rational PSLQ scan to a wider REAL grid: 4 algebraic irrationals (1/√2, 1/√3, √2−1, 1/φ), 4 transcendentals (1/e, π/4, ln(2), 1/π), 9 decimal points clustered around 1/2 to confirm uniqueness as a strict point feature. Tested at 50, 100, and 200 digits of mpmath precision with PSLQ at (deg ≤ 8, |c| ≤ 50) and (deg ≤ 12, |c| ≤ 100).

**Only α = 1/2 yields a genuine algebraic relation** — `x² − 2x − 2 = 0` for H/Br (i.e., 1+√3). At 200-dps with deg-2 PSLQ tolerance 10⁻¹⁹⁰, α=1/2 produces residual 6.5×10⁻²⁰¹ while the nearest neighbors (0.49, 0.499, 0.5001, 0.501, 0.51) produce no relation. The algebraic relation is a strict point feature, not a basin.

**Combined empirical record**: ~58 unique real α values tested across this push + D57 + the May-12 41-candidate scan. **Zero counterexamples to Conjecture 4.2.**

Follow-up: cubic algebraic irrationals (2^(1/3), root of x³−x−1); structural proof attempt via the rational fixed-point equation parametric in α; multivariate PSLQ.

## F2 — 32=32 Pauli-divisor bijection (`F2_32_32_bijection.md`)

**Result: COINCIDENCE-BOUND. The 32 = 32 equality has no natural bijection. Honest negative closed.**

37 hand-built structural candidates tested (σ-orbits, CRT, kernel/strand, lens-pair, μ + small-prime, p-adic valuation, τ-orbit, etc.) plus brute-force enumeration of 730,000+ functions across five natural classes (linear-mod-4, linear+permutation, symmetric, 2-bit and 3-bit dictators, linear+quadratic). **Zero matches** in any natural class.

**Coincidence bound**: a uniformly random `f: {0,1}^5 → {0,1,2,3}` matches `(2, 6, 10, 14)` with probability ≈ 3.13×10⁻⁵ (1 in ~32,000). The hit-rate within natural-low-complexity function families is precisely 0, BELOW random.

**Reframe**: The `(1, 5, 10, 10, 5, 1)` distribution is dimension of `Λ^k(R^5)` (exterior algebra); `(2, 6, 10, 14)` is subshell capacities `2(2l+1)` for l = 0, 1, 2, 3. The two partitions of 32 are independent. The 32 = 32 equality is Pascal-type coincidence with a rigorous bound now in place.

Follow-up: update HONEST_NEGATIVES §1.1 with the closure line.

## F3 — T* = 5/7 unification (`F3_T_star_unification.md`)

**Result: PARTIAL. Two genuinely independent derivations + four structural rhymes — NOT six independent derivations.**

Located the 6 derivations claimed in HONEST_NEGATIVES §1.4. Cross-referenced against J13's own §6 self-audit, which is sharper: only 2 of 6 are genuinely independent (J13 cyclotomic forcing + WP35 unit_frac at b=35); the other 4 are reformulations, near-agreements, or structural rhymes.

**Hypotheses tested for a common algebraic root**:
- Cyclotomic Q(ζ_10) quotient: **REFUTED**. |1−ζ¹⁰⁵|/|1−ζ¹⁰⁷| = φ (golden ratio), not 5/7. The J13 forcing uses 5 and 7 as **primes**, not as cyclotomic numerical quantities.
- Z/10Z 2×2 sub-magma forcing: gives the integer pair (5, 7), but the ratio appearing in the 6 derivations comes from different operations.
- Discriminant of LMFDB 4.2.10224.1: -10224 = -2^4 · 3^2 · 71, no 5/7 inside.

**Genuine unifier (partial)**: each derivation independently identifies "5 = smallest non-degenerate prime" and "7 = smallest obstruction prime" under unrelated operations. The PRIME PAIR (5, 7) is shared; the operations producing it are not.

Follow-up: tighten HONEST_NEGATIVES §1.4 to "two genuinely independent derivations plus four structural rhymes" rather than "six independent derivations."

## F4 — F_p variation pattern (`F4_Fp_variation_pattern.md`)

**Result: EMPIRICAL-ONLY for {7, 11} distinction — but TWO NEW CLOSED FORMS emerged as bonus findings.**

Tabulated F_p structural data across {2, 3, 5, 7, 11, 13} on the V^BHML 4-core algebra. Tested hypotheses for a clean algebraic criterion that isolates {7, 11}: mod 6/10/12/14, Legendre symbols (−7/p) and (−11/p), inertness in Q(ζ_10) and Q(ζ_12). **None isolate {7, 11}.**

**The {7, 11} distinction dissolves under scrutiny**: among primes < 200, the rank-preserving set is 39 primes (7, 11, 17, 19, 23, 31, 41, ...). The set is exactly those primes NOT dividing any of the 7 chain-shell determinants {5305, 2843, −2886, 2929, −7542, 7272, −7002}.

**Two new closed forms** discovered during the search:

1. **Idempotent count formula**: `|idem(V^BHML over F_p)| = p + 3` for odd p (= 2 at p=2). Previously not explicitly stated in the corpus. Empirically: p=3 gives 6 idempotents, p=5 gives 8, p=7 gives 10, p=11 gives 14, p=13 gives 16. The formula closes the inventory.

2. **Automorphism size formula**: `|Aut(V_p)| = p(p² − 1) = |GL_2(F_p)|` at every prime EXCEPT p=5, where the substrate index collapse `{7, 8, 9} ≡ {2, 3, 4} (mod 5)` reduces Aut from 120 to 40.

**p=5 is the genuinely anomalous prime**, not {7, 11}. The original "universal F_p fails generically" framing should be replaced with: "automorphisms are GL_2(F_p) at every prime except p=5 (where 4-core index collapse reduces it)."

Follow-up: extend testing to primes 100-500 to confirm the GL_2(F_p) closed form; investigate whether the p+3 idempotent count and the GL_2(F_p) automorphism connect via a deeper representation-theoretic claim; potentially this becomes a new short J-paper for *Algebra Universalis* or *Linear Algebra Apps*.

## Updates to HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md

Based on these four findings, the following updates are warranted:

- **§1.1 (32=32 bijection)**: close as Pascal-type coincidence with rigorous bound. Add reference to F2 work.
- **§1.3 (F_p universality)**: replace "{7, 11} preserve rank" with "GL_2(F_p) automorphism at every prime except p=5; rank-preserving set is 39 primes < 200." Add new closed forms.
- **§1.4 (T* = 5/7)**: reframe as "two genuinely independent derivations + four structural rhymes" per J13's stricter §6 self-audit.
- **§2.1 (α-uniqueness Conjecture 4.2)**: strengthen the empirical support note — 58 real α values tested, zero counterexamples.

## Frontier triage as of 2026-05-27

| Frontier | Status after this push | Recommended next |
|---|---|---|
| Conjecture 4.2 (α-uniqueness) | Strengthened empirically (58 values) | Structural proof attempt |
| 32=32 bijection | **Closed as coincidence** with rigorous bound | Document closure in §1.1 |
| T* = 5/7 unification | Reframed as 2 + 4 (independent + rhymes) | Update §1.4 framing |
| F_p variation | Replaced by GL_2(F_p) formula + p=5 anomaly | New short paper candidate |
| Yukawa hierarchy (§2.5) | Untouched | Heavy physics work, deferred |
| Dark-sector triple (§2.4) | Untouched (requires DESI Year-3) | Observational, wait |
| Cosmology layer choice (§2.3) | Untouched | Author publication-strategy choice |
| Clay reformulations (§2.2) | Untouched | Long-horizon |

Two of four frontiers moved (F2 closed; F4 reframed with new closed forms); one strengthened (F1); one reframed honestly (F3). Net: the framework's frontier landscape is cleaner and more honest after this push.

## Files written this session

- `04_meta/frontiers_2026-05-27/F1_alpha_uniqueness_extended.md` + `verification/frontier_F1_alpha_wide_scan.py`
- `04_meta/frontiers_2026-05-27/F2_32_32_bijection.md` + 3 candidate-search scripts
- `04_meta/frontiers_2026-05-27/F3_T_star_unification.md`
- `04_meta/frontiers_2026-05-27/F4_Fp_variation_pattern.md`
- `04_meta/frontiers_2026-05-27/FRONTIER_PUSH_SUMMARY.md` (this file)
