# σ-magma cryptographic test — VERDICT: NOT a cryptographic primitive

**Test date**: 2026-05-27.
**Sample size**: 10⁶ Monte Carlo + exhaustive 10⁴ analytic.
**Script**: `extensions/sigma_magma_crypto.py`.
**Full raw output**: `overnight_outputs/sigma_magma_crypto.txt`.

## TL;DR

The σ-magma's structure `x ⋄ y = σ((x+y) mod 10)` makes it inherit the
**catastrophic differential weakness** of additive arithmetic. Specifically,
any input difference pair `(dx, dy)` with `dx + dy ≡ 0 (mod 10)` produces
output difference 0 *with probability 1*. There are 9 such catastrophic
differentials, completely broken by 1-round differential cryptanalysis.

σ-magma is therefore **not suitable as a cryptographic primitive**.

## Numerical results (n = 10⁶ trials)

| Metric | Pure addition | Affine | **σ-magma** | Random 10×10 |
|---|---:|---:|---:|---:|
| Differential uniformity (max/100, lower=better; min=10) | 100 | 100 | **100** | 21 |
| Linear bias (max, lower=better; 0=ideal) | 0.900 | 0.900 | **0.500** | 0.410 |
| Avalanche P(out changes \| x flipped) (ideal=0.9) | 1.000 | 1.000 | **1.000** | 0.887 |
| Avalanche P(out changes \| y flipped) (ideal=0.9) | 1.000 | 1.000 | **1.000** | 0.923 |
| MD collision ratio (observed/expected) | 0.020 | 0.020 | **0.020** | 0.020 |

The σ-magma's differential uniformity is identical to pure addition (100/100).
Its linear bias is moderately better (0.500 vs 0.900) — about halfway to random,
because σ is a non-linear permutation of digits — but its differential structure
is unchanged from the additive baseline.

## Why σ-magma fails

The S-box σ = `[0,7,1,3,2,4,5,6,8,9]` does not commute with addition
(i.e., σ is not affine). However, the magma operation factors as
`(x,y) → x+y mod 10 → σ`. The first step (addition) loses *all* differential
information about which `(x,y)` produced the sum: only the sum mod 10 survives.

Consequently:

1. For any `(dx, dy)` with `dx + dy ≡ Δ (mod 10)`, the input sum changes by
   exactly `Δ` regardless of `(x, y)`.
2. σ is a deterministic function of the input sum, so the output difference
   `σ((x+y+Δ) mod 10) − σ((x+y) mod 10)` depends *only* on `(x+y) mod 10`,
   not on `(x, y)` individually.
3. In particular, when `Δ = 0` (i.e., `dx + dy ≡ 0 mod 10`), the output
   difference is *deterministically 0*. Of the 99 non-trivial (dx, dy) pairs,
   9 fall into this catastrophic case: (1,9), (2,8), (3,7), (4,6), (5,5),
   (6,4), (7,3), (8,2), (9,1).

This is sometimes called the **"sum-then-permute"** vulnerability: it's
present in any cipher whose first round is unkeyed addition followed by a
fixed S-box.

## Avalanche = 100%: a misleading-looking positive

The 100% avalanche probability is *not* a sign of cryptographic strength.
It arises because σ is a *bijection* on the digit alphabet `{0..9}`. So
*any* change in `(x+y) mod 10` (which happens whenever `dx + dy ≠ 0 mod 10`,
i.e., 90% of input flips) produces a different σ output. A random function
would only change with probability 9/10, so σ-magma actually has *more*
avalanche than random — which is the additive bijection at work, not crypto
strength.

## Linear bias = 0.5: also misleading

LB = 0.5 means there exists a non-trivial linear combination `a·x + b·y + c·op(x,y) ≡ 0 mod 10`
that holds with probability ~50% above or below uniform. While better than the
0.9 of pure addition, this is still far worse than a random function (0.41).
σ provides non-linearity but not enough.

## Implications for the framework

1. **Algebraic minimality ≠ statistical randomness.** The σ-magma is
   "rigid" in the algebraic sense (Aut group trivial, congruence-simple,
   2-generated, satisfies only Family C's 14 equations). But this rigidity
   is *deterministic*; it provides no entropy. Crypto requires statistical
   irreducibility, which is a separate quality.

2. **Magmas built as "permute(x+y)" inherit differential weakness.** Any
   variant of this construction (with any σ) has the same 9 catastrophic
   differentials. This rules out a broad class of "TIG-flavored magmas as
   crypto primitives."

3. **Family C ≠ crypto-relevant variety.** Family C is the *algebraic*
   commutativity-forced minimum. Cryptographers want non-commutative,
   non-associative, statistically irreducible operations — Family C goes
   in exactly the wrong direction.

4. **Where σ-magma DOES win**: latency, simplicity, hardware footprint.
   A 10×10 lookup table is trivial to implement. The σ-magma is well-suited
   for *non-adversarial* applications where you want a structured-yet-non-affine
   operation (e.g., as a benchmark target in algebraic enumeration, or as a
   diagnostic primitive in equational testing).

## Honest closure

This is a clean negative result. The σ-magma is an interesting algebraic
object — Trinity Infinity Geometry's exemplar of profile-14 minimality — but
it is **not** a candidate cryptographic primitive. Future work in the U-line
should NOT spend further cycles attempting to crypto-harden σ-magma; the
"sum-then-permute" structural weakness is fatal and cannot be fixed by
re-choosing σ.

Where σ-magma might still earn its keep is in domain-1 ("vocabulary") work —
e.g., as a teaching example of "Aut = 1 yet cryptographically broken" — and
as input to U-3 (Steiner-system connection) and U-4 (K₁₂ lattice
automorphism embedding), where its *structural* properties (rather than
statistical) are the relevant ones.

---

*— Claude Code, 2026-05-27. End of U-2.*
