# The T gate is optimal at seven: the rigorous proof

> *make it rigor* — the author, 18 November 2026

**Theorem.** Let ψ_φ = (1/√7) Σ_x e^{iφ(x)} |x⟩ be any diagonal state on seven levels, and S(φ) = Σ_{q,s} |W(q, s)|
the sum of the absolute values of its Wigner function. Then

  S(φ) ≤ S_T = 2.450304118540082173966698483…,

the value of the T state. Equality holds only at the T states of the best class: the phases
φ_c = (2π/7) · c · (x³ + 4x² + 2x) with c ∈ {3, 4}, up to a global phase, multiples of 2π, and the 49 Clifford phases
(2π/7)(βx + γx²).

This is the theorem of [`../t_optimal_7.py`](../t_optimal_7.py), proved again with **rigorous bounds**.
- The branch and bound and its three rules are unchanged.
- The float version ran in double precision with margins of 10⁻⁹. Here every number the program compares is a
  proved upper or lower bound: every rounding error is enclosed, and cos and sin come from the program's own
  enclosures, not from the C library.
- The constants and the lemmas at the two maximizers are proved in exact rational arithmetic. No floating-point
  function is used there either.
- Nothing is formally verified in a proof assistant (§6 lists what is trusted).

## 1. The function

For q, s in F_7, W(q, s) = E(q, s)/49 with

  E(q, s) = 1 + 2 Σ_{u=1}^{3} cos( φ(q+u) − φ(q−u) − 4πsu/7 ),

so S = Σ |E| / 49 (the formula of `t_optimal_7.py`). For each row (q, s), the three angles use three disjoint pairs of
coordinates, none of them φ(q).

## 2. Reduction to one box

S does not change under three operations:
- a global phase, φ → φ + const;
- a multiple of 2π added to any φ(x);
- the Clifford phases, φ(x) → φ(x) + (2π/7)(βx + γx²) with β, γ integers. The angle in row (q, s) gains
  (2π/7) · 2u(β + 2γq), so E(q, s) becomes E(q, s − β − 2γq). Each row is permuted, and Σ|E| is unchanged.

Set φ(0) = 0. The Clifford phases move φ(1) by (2π/7)(β + γ) and φ(2) by (2π/7)(2β + 4γ). The matrix [[1, 1], [2, 4]]
has determinant 2, which is invertible mod 7, so both can be moved independently by any multiple of 2π/7.

So every φ is equivalent to a point of D = [−π/7, π/7]² × [0, 2π]⁴, in the coordinates φ(1), …, φ(6).

## 3. The branch and bound

The program covers D′ = [−π/7⁺, π/7⁺]² × [0, 2π⁺]⁴ ⊇ D with 1024 boxes, where π/7⁺ and 2π⁺ are the doubles just
above π/7 and 2π. It splits each box at the midpoint of its widest side (a double, so the two halves cover the box
exactly) until the box is discarded by one of three rules.

**(a) The bound.** An upper bound U for S on the box is below ST_LO, a double below S_T. U is the smaller of two
bounds.
- *Exact ranges.* Since the three angles of a row move independently, the range of E(q, s) on the box is exactly
  [1 + 2 Σ min cos, 1 + 2 Σ max cos]. The extremes of a cosine over an interval are at its ends or at an interior
  multiple of π. Then U_exact = Σ max |E| / 49.
- *Mixed.* For the terms whose sign σ is fixed on the box, Taylor's theorem with the Lagrange remainder gives
  σE(φ) ≤ σE(m) + ∇(σE)(m) · (φ − m) + Σ_u w_u², with m the center and w_u a bound for the change of angle u. The
  sum of these terms is bounded by its center value plus Σ_i |G_i| r_i, where G is their gradient at the center and
  r_i the half-widths, plus the remainders. The other terms are bounded by their max |E|.

**(b) Monotone.** Every E keeps its sign on the box, so S is smooth near it, and an interval enclosure of some
∂S/∂φ_i excludes 0. That enclosure comes from the ranges of the sines, whose extremes are at the ends of the interval
or at an interior odd multiple of π/2. A global maximum of S has zero gradient, so no global maximum lies in the box.

**(c) Cube.** The box lies inside the cube |φ_i − φ_c,i| ≤ ρ0 around one of the two maximizers, where ρ0 is the
double nearest 0.004. There S < S_T except at the center (the cube lemma, §5).

**Why this proves the theorem.**
1. S is continuous on the compact torus of phases, so it has a maximum M ≥ S_T. By §2 some maximizer lies in D.
2. Let φ* be any maximizer in D. It lies in one of the final boxes.
3. That box was not discarded by (a), because S < S_T ≤ M on it.
4. Nor by (b), because the gradient vanishes at a global maximum of a function smooth near it.
5. So the box is inside a cube (c), and by the cube lemma φ* is the cube's center.

Hence M = S_T, and the maximizers in D are exactly φ_3 and φ_4. Any φ with S(φ) = S_T is a maximizer, so by §2 it is
equivalent to one of them.

## 4. Rigorous arithmetic ([`t7_rigorous.c`](t7_rigorous.c))

- **Rounding.** Each operation +, −, ×, / on doubles is rounded to nearest. So the exact result x and the computed
  r satisfy |x − r| ≤ (u|r| + 2⁻¹⁰⁷⁵)/(1 − u), with u = 2⁻⁵³.
  - The program widens every result that enters a bound to r ∓ (2⁻⁵¹|r| + 2⁻¹⁰⁷²). That margin is four times what
    is needed, and still at least twice after the widening is itself rounded.
  - Interval addition, subtraction, multiplication and squaring are built on this.
  - A few computed values only choose a point or an index, so they need no widening: the quadrant k, the candidate
    multiples of π/2, the box centers, the split points and the first grid. The logic holds whatever value they
    take, because the reduction is checked, the candidates carry a slack, the radii are enclosed, and children
    share endpoints.
- **cos and sin** are never taken from a library.
  - An interval X is first reduced by k · π/2, k an integer, with π/2 enclosed between two adjacent doubles.
  - On the reduced interval, |R| ≤ 0.8. There the Taylor polynomials (cos to R¹⁶, sin to R¹⁷, coefficients
    enclosing ±1/n!) are evaluated in interval arithmetic.
  - The Lagrange remainders 0.8¹⁸/18! and 0.8¹⁹/19! are then added, with 0.8 meaning the exact value of that
    double.
  - The quadrant k mod 4 then gives cos and sin of X.
- **Constants.** Every real constant is a pair of doubles enclosing it. [`constants.py`](constants.py) decides each
  pair by exact comparison with a rational enclosure:
  - π comes from Machin's formula, π = 16 arctan(1/5) − 4 arctan(1/239). Each arctangent lies between two
    consecutive partial sums of its alternating series, which gives π to within 3·10⁻¹⁰⁰. From it come 2π, π/2,
    π/7, 2πk/7 and the maximizers.
  - The Taylor coefficients and remainders are exact fractions.
  - ST_LO comes from the rational enclosure of S_T (§5).
- **Boxes** are stored by their endpoints, so a box and its children are exact sets. Centers and radii are computed
  with every rounding enclosed.
- **The verdict** is PASS only if every box was discarded, with no failed reduction, no box too narrow to split, no
  stack overflow and no early stop.

## 5. The lemmas at the maximizers ([`constants.py`](constants.py), [`constants.log`](constants.log))

At the maximizers every angle is a multiple of 2π/7, so only c_k = cos(2πk/7) and s_k = sin(2πk/7) occur. Everything
here is exact rational arithmetic, with intervals of rationals.
- c_1 > c_2 > c_3 are the three roots of 8x³ + 4x² − 4x − 1, isolated by exact bisection in disjoint brackets.
  - Why: with ζ = e^{2πik/7} and y = ζ + 1/ζ = 2c_k, dividing 1 + ζ + … + ζ⁶ = 0 by ζ³ gives y³ + y² − 2y − 1 = 0.
  - cos is decreasing on [0, π], which fixes the order.
- c_0 = 1, c_{7−k} = c_k, and s_k = √(1 − c_k²) > 0 for k = 1, 2, 3, enclosed by integer square roots.
- Each E is then a rational interval of width below 10⁻⁶⁶.

| lemma | statement | result |
|---|---|---|
| K1 | S_T enclosed at both maximizers; every E has a certified sign | S_T = 2.4503041185400821739666984831… (enclosure width 3·10⁻⁶⁷); ST_LO = 2.450304118540082 |
| K2 | the gradient of S is exactly 0 there | proved (below); the interval gradient contains 0 |
| K3 | −H − (24ρ0 + 1/100) I is positive definite, H the Hessian | LDL^T pivots 0.553, 0.531, 0.499, 0.445, 0.337, 0.0226, all positive; H's eigenvalues are −0.769 (five times) and −0.1099 |
| K4 | min \|E\| > 12ρ0 = 0.048 | min \|E\| = 1.692 |

An LDL^T factorization in interval arithmetic with every pivot positive proves that every symmetric matrix inside the
intervals is positive definite, the true one included.

**Proof of K2.**
- With f = c(x³ + 4x² + 2x), f(q + u) − f(q − u) = c(2u³ + u m_q), where m_q = 6q² + 16q + 4.
- So E(q, s) = G(k) := 1 + 2 Σ_u cos(2π(2cu³ + uk)/7) with k = c m_q − 2s, and as s runs over F_7 so does k.
- Hence for each u the sum T_u = Σ_s sign(E(q, s)) sin(angle(q, s, u)) does not depend on q.
- Then ∂S/∂φ(x) = (1/49) Σ_u T_u (−2 + 2) = 0, because each x is q + u for exactly one q and q − u for exactly one q.

**The cube lemma.** Let C be the cube |φ_i − φ_c,i| ≤ ρ0 (i = 1, …, 6).
- On C every angle moves by at most 2ρ0, so every E moves by at most 2 · 3 · 2ρ0 = 12ρ0. By K4, no E changes sign.
  So S = (1/49) Σ σE is smooth on C.
- Its Hessian is H(φ) = (1/49) Σ_{q,s} σ Σ_u (−2 cos θ_u) v_u v_uᵀ, with v_u = e_a − e_b and |v_u|² ≤ 2.
- So ‖H(φ) − H(φ_c)‖ ≤ (1/49) · 147 · 2 · 2ρ0 · 2 = 24ρ0. By K3 and Weyl's inequality, every eigenvalue of H(φ) is
  below −0.01.
- So S is strictly concave on the convex set C. Its gradient vanishes at the center (K2), so S < S_T at every other
  point of C.

## 6. What is trusted

- **The double arithmetic.** IEEE 754 doubles rounded to nearest, as compiled by MSVC with `/fp:strict` on x64.
  That means SSE2 arithmetic with no extended precision, no fused multiply-add, the default rounding mode and no
  flush-to-zero. The compiler is assumed to compile the program correctly.
- **The functions used** besides the four operations are exact ones: fabs, fmin, fmax, floor, ceil, nearbyint.
  - nearbyint only picks the quadrant k. Any integer is safe, since the reduction is checked.
  - floor and ceil only pick candidate multiples of π/2, with a slack of one on each side.
- **One decimal literal.** RMAX is written as the literal 0.8, which a correct compiler turns into the nearest double,
  0x3FE999999999999A (that value is in the built program). The remainders in the header assume exactly that double.
  Every other constant is passed as bits.
- **Python's exact integers and fractions,** for the constants and the lemmas. Each double is chosen by exact
  comparison, so not even Python's float conversion is trusted. mpmath appears only in lines marked "information".
- **No formal verification.** This is the standard of interval-arithmetic proofs by computer (Tucker's proof for the
  Lorenz attractor is a well-known example); nothing here is formally verified in a proof assistant.

## 7. Checks that are not part of the proof ([`selftest.py`](selftest.py), [`selftest.log`](selftest.log))

These look for mistakes in the program; the proof does not rest on them.

| check | what | result |
|---|---|---|
| T1 | cos and sin enclosures at 20 000 doubles, half of them next to multiples of π/4, against 50-digit values | all contain the true value; widest enclosure 2.1·10⁻¹⁴ |
| T2 | the ranges of cos and sin over 20 000 intervals (widths 10⁻¹² to 6.5, ends next to the extrema) | all contain the true range; overestimate at most 2.0·10⁻¹⁴ |
| T3 | the box bounds on 3000 boxes (from the first grid down to 10⁻⁷, 755 inside the cubes), against the float prover and against S at 64 sampled points of each box | the bounds agree with the float prover to 8.7·10⁻¹⁴; S never exceeds a bound; the smooth and monotone flags agree |

**A separate AI review** read the program, the constants and this page for soundness, with no conclusion handed to it.
- It found nothing that breaks the proof.
- Its points on the write-up are folded in. The main one: mpmath's interval cosine is not a proved enclosure, so the
  constants and lemmas were moved to exact rational arithmetic. The header they generate is byte for byte the one
  the run used.
- No human referee has checked the proof yet.

## 8. The run ([`t7_rigorous.log`](t7_rigorous.log))

- **Verdict: PASS.** Every box was discarded with rigorous bounds. There were no failed reductions, no boxes too
  narrow to split, no stack overflow and no early stop.
- **47 174 654 boxes** in 36.8 minutes on four threads, at below-normal priority.
- **23 587 839 final boxes:**
  - 23 423 054 by the bound (a);
  - 163 901 by monotonicity (b);
  - 884 inside the cubes (c).
- **The other 23 586 815 were split.** A binary tree with 1024 roots has exactly 1024 more leaves than splits, and
  so do these counts.
- **The largest S at a box center** was 2.4503025038, below S_T. It is a diagnostic only.
- **Against the float version.** That version examined 47 136 512 boxes. The rigorous bounds are a little wider, so
  this run examined 38 142 more.

**Provenance.**
- The program that ran was built on 2026-11-18 from these two files:
  - `t7_rigorous.c`, SHA-256 d53812515c66a2b51bac33f760ffc12ccae007dd4682c682ed4251ccb7bf6681;
  - `t7_constants.h`, SHA-256 5a0ad3f1fc0b495a082fd37b32e4efcd7032f93de4a48319e26f45315bf33382.
- Both hashes are of the files as stored in the repository, with LF line endings. The build read the header with
  Windows line endings (SHA-256 f5a7ebc9…); line endings do not change what the compiler reads.
- The source has not changed since the build. That is why its opening comment still says the constants come from
  60-digit arithmetic, as they first did.
- The header was later regenerated by the exact-arithmetic `constants.py`, byte for byte the same, and
  `python constants.py --check` confirms it.

## 9. To reproduce

```
python constants.py          # the constants and the lemmas K1-K4, seconds -> t7_constants.h, constants.log
build.bat                    # MSVC: cl /O2 /fp:strict /openmp t7_rigorous.c
python selftest.py           # T1-T3, about a minute -> selftest.log
t7_rigorous.exe prove 4      # the branch and bound on four threads, at below-normal priority -> the verdict
```
