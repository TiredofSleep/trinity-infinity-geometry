# The Wigner negativity of qudit T states, and of the polynomial phase gates above them

*A note by Brayden Ross Sanders (Hot Springs, Arkansas), November 2026. The computations were made with AI assistance,
and no one but the author has reviewed them. Corrections are welcome.*

## 1. Setting

Let p ≥ 5 be prime and ω = e^(2πi/p). For a function f: F_p → F_p, the phase state is

  ψ_f = U_f|+⟩ = p^(−1/2) Σ_x ω^f(x) |x⟩,   U_f = diag(ω^f(x)).

When f is a polynomial of degree d < p, U_f lies in the d-th level of the Clifford hierarchy [CGK]. Degree 3 gives the
Howard–Vala T gates [HV]. Gross's Wigner function [G] of ψ_f is

  W_f(q, s) = p^(−2) Σ_y ω^(f(q + y/2) − f(q − y/2) − sy).

The measure here is the Wigner norm S(f) = Σ_(q,s) |W_f(q, s)|. Its logarithm is the mana [VMGE], and (S − 1)/2 is
the sum negativity. Cauchy–Schwarz gives S ≤ √p.

## 2. Statements

**(1) T states.** For f = cx³ + b₂x² + b₁x with c ≠ 0, W_f(q, s) = S_t(f′(q) − s)/p², where t = c/4 and S_t(a) =
Σ_x ω^(tx³ + ax) is a Birch sum.
- So S = p⁻¹ Σ_a |S_t(a)|. It depends only on the cubic class of c, matching the three Clifford classes of T gates
  when p ≡ 1 (mod 3) [FL25].
- By the equidistribution of Birch sums [L, K], S/√p → 8/(3π) = 0.848826.

**(2) Random states.** A phase-point operator has (p + 1)/2 eigenvalues +1 and (p − 1)/2 eigenvalues −1. So for a
Haar-random pure state, W(u) = (2X − 1)/p with X ~ Beta((p + 1)/2, (p − 1)/2), and

  E[S] = p·E|2X − 1|  →  √(2/π)·√p = 0.797885·√p,

Wilson and White's limit [WW]. It is approached from above: 0.8385√p at p = 5, and 0.7981√p at p = 1009.

**(3) Higher degrees.** f(q + y/2) − f(q − y/2) is an odd polynomial in y, of degree 2m + 1 when d = 2m + 1 or
d = 2m + 2. When d is even its leading coefficient is a multiple of q, so the one row q = 0 has lower degree (for
f = x^d it is a single positive point).
- For an odd polynomial g of degree 2m + 1 and p large, the family a ↦ Σ_y ω^(g(y) + ay) has geometric monodromy
  group Sp(2m) [K]. We rely on this; the numbers in §3 agree with it.
- Deligne's equidistribution theorem then gives

  S/√p → κ_m := E|tr U|,  U Haar-random in USp(2m).

| degree d | group | κ_m |
|---|---|---|
| 3, 4 | USp(2) = SU(2) | 8/(3π) = 0.848826 |
| 5, 6 | USp(4) | 0.790497 |
| 7, 8 | USp(6) | 0.798491 |
| 9, 10 | USp(8) | 0.79781 |
| → ∞ | Gaussian | √(2/π) = 0.797885 |

- The values are computed from the Weyl integration formula and confirmed by Monte Carlo on Haar-random symplectic
  matrices.
- The sequence is not monotone, and κ₂ < √(2/π). The trace on USp(4) has the Gaussian's second and fourth moments, 1
  and 3, but a smaller mean absolute value.
- So among polynomial phase gates, the cubic level is the only one whose magic states are asymptotically more
  Wigner-negative than random states. Degrees 5 and 6 are less negative than random states.
- The hierarchy's higher levels also contain gates with p^m-th-root phases [CGK]. They are not covered here.

**(4) Small p, exhaustively.** Every f is a polynomial of degree at most p − 1, and terms of degree at most 2 are
Clifford.
- Over all p^(p−3) classes, all 25 at p = 5 and all 2401 at p = 7, the largest S belongs to a T state: S = 1 + 2/√5 at
  5, and 2.450304 at 7.
- At p = 11 a degree-10 phase beats the T state: 2.877321 against 2.827479, found in a random sample of 10⁶ classes.
- For comparison:
  - Li and Luo showed that the qutrit T gate is optimal among diagonal gates for Wigner negativity [LL].
  - Feng and Luo found 500 ququint diagonal gates, with phases outside the fifth roots of unity, that beat the T gate
    [FL26].
  - The statements here concern phases that are p-th roots of unity only.

**(5) Moments.** Σ_(q,s) W^n = p^(1−2n) Σ_a S_t(a)^n.
- Averaged over the three classes, these are point counts of Livné's cubics {Σ x_i = Σ x_i³ = 0} [L]. For p ≡ 2
  (mod 3) every class equals the average.
- For example, for p ≡ 2 (mod 3) the seventh moment is (14 + 6(p/5))/p⁹ + a_p/p¹⁰. Here a_p are the coefficients of
  the weight-3 newform 35.3.c.b, by Chênevert's identification [C].
- For p ≡ 1 (mod 3) the third moment of each class is Σ W³ = p⁻⁴·g(3, 3t)², with g(3, b) = Σ_x ω^(bx³). This is Zhu,
  Mao and Yi's Lemma 24, read through the Wigner function [ZMY].
- The fourth moment, (2p − 1)/p⁵, is the same for all three classes.

**(6) Beyond p-th roots** (round 30).
- With phases that are p²-th roots of unity, every g: F_p → Z/p² is allowed. Each such gate lies in the
  hierarchy [CGK], and the qutrit T gate is one of them, with ninth roots.
- At 5, 129 500 of the 390 625 states (g(0) = 0) beat the T state, and the best reaches S = 1.969982. The best
  diagonal state with arbitrary phases, found from 300 random starts, has 1.977576 = 0.884√5. Feng and Luo's
  optimal gates beat T at 5 [FL26], and twenty-fifth roots come within 0.4% of them.
- At 7, 400 optimizations over arbitrary phases found nothing above the T state, S = 2.450304. Their best is the
  T state itself, with phases (0, 5, 6, 6, 1, 1, 2)/7, that is, f = 4x³ + x. So, numerically, the T gate is optimal
  among all diagonal gates at 7, as at 3 [LL] and unlike 5 [FL26].

**Theorem (p = 7; computer-assisted, with rigorous bounds).** Every diagonal state has S ≤ 2.4503041185…, the T
state's value. Equality holds only at the T states of the best class (c ∈ {3, 4}, so t = c/4 = 1).
- **The proof** is a branch and bound over the torus of phases φ(1..6), reduced by the 49 Clifford phases to the box
  [−π/7, π/7]² × [0, 2π]⁴.
- **It examined 47 136 512 boxes in 9.7 minutes.** A box is discarded in one of three ways:
  - by an upper bound. Each W(q, s) depends on three angles through disjoint coordinates, so its range is exact;
    the terms that keep their sign are linearized together;
  - by monotonicity, where S is smooth and a partial derivative cannot vanish;
  - or inside the two cubes of half-width 0.004 around the maximizers, where S is certified concave. The Hessian's
    eigenvalues there are −0.769 (five times) and −0.110.
- **Rigor.** The first program ran in double precision with margins of 10⁻⁹. A second one,
  [`t7_rigorous/`](t7_rigorous/RIGOROUS.md), redoes the same branch and bound with rigorous bounds.
  - Every rounding error is enclosed, and cos and sin come from its own interval enclosures, not from a library.
  - The constants and the lemmas at the maximizers are proved in exact rational arithmetic.
  - It discarded every one of its 47 174 654 boxes in 37 minutes ([`t7_rigorous.log`](t7_rigorous/t7_rigorous.log)).
  - Two later programs prove it again: the generalized prover below, and a second proof in Arb's ball arithmetic.
  - Nothing is formally verified in a proof assistant.
- **The control.** The float prover at p = 5 fails at once, finding a state above the T state, as Feng and Luo's
  result requires ([`t_optimal_7.py`](t_optimal_7.py), [`t_optimal_7.log`](t_optimal_7.log)).
- Random p²-th-root phases have the random-state value: 0.79801√p against 0.79816√p from 500 to 1000.

**Theorem (p = 5; computer-assisted, with rigorous bounds).** Every diagonal state on five levels has
S ≤ S*₅ = 1.97757582130854208841…, with equality exactly on one orbit of 500 states, which are not T states.
- The 500 match Feng and Luo's count [FL26]. The maximizer's only symmetry is an antiunitary reflection, and
  re-centred it is odd. No integer polynomial of degree at most 24 fits S*₅.
- The proof generalizes the p = 7 program. The program certifies the boxes around the 20 maximizers in D itself:
  every E keeps its sign, the interval Hessian is negative definite, a Krawczyk test finds exactly one critical
  point, and the symmetries map one certified point into every other box. It examined 629 676 boxes in 11 seconds
  ([`diagonal_optimum/OPTIMUM.md`](diagonal_optimum/OPTIMUM.md)).
- The same program reproduces Li and Luo's theorem at 3 [LL], and the theorem at 7 without the hand-proved cube
  lemma. So at 3, 5 and 7 the most Wigner-negative diagonal state is known exactly: the T gate at 3 and 7, and an
  orbit of 500 at 5.
- **A second proof.** A separate program, [`arb_check.py`](diagonal_optimum/arb_check.py), proves all three again.
  - It works in Arb's ball arithmetic, with Arb's own cos and sin, and none of the first program's arithmetic.
  - It examined 780 204 boxes at 5 and 100 185 058 at 7 ([`arb5.log`](diagonal_optimum/arb5.log),
    [`arb7.log`](diagonal_optimum/arb7.log)).
  - At 5 it encloses S*₅ in [1.97757582130854207, 1.97757582130854211].
  - The candidates' symmetries, which neither program checks, are checked separately in integer arithmetic
    ([`symmetry_check.log`](diagonal_optimum/symmetry_check.log)).

**(7) A pattern by p mod 3, and where it ends** (rounds 31 and 32). One fixed search ran at every prime: L-BFGS on
a smoothed Wigner norm, from about 650 starts, some random and some near the T states. Through p = 23 the T gate is
the most Wigner-negative diagonal gate exactly when p = 3 or p ≡ 1 (mod 3). From 29 on it is beaten everywhere:

| p | p mod 3 | best T state, S/√p | best diagonal state found, S/√p |
|---|---|---|---|
| 3 | 0 | 0.9158 | the T state [LL] |
| 5 | 2 | 0.8472 | 0.8844 [FL26] |
| 7 | 1 | 0.9261 | the T state |
| 11 | 2 | 0.8525 | 0.8776 |
| 13 | 1 | 0.8888 | the T state |
| 17 | 2 | 0.8493 | 0.8803 |
| 19 | 1 | 0.8886 | the T state |
| 23 | 2 | 0.8470 | 0.8860 |
| 29 | 2 | 0.8561 | 0.8692 |
| 31 | 1 | 0.8734 | 0.8800 |
| 37 | 1 | 0.8740 | 0.8775 |
| 43 | 1 | 0.8756 | 0.8759 |

- When p ≡ 2 (mod 3) the beating states are explicit, so that side is decisive. When p ≡ 1 the search returned only
  the T state, which is numerical evidence and not a proof.
- When p ≡ 1 (mod 3) the T gates form three Clifford classes [FL25]. The best class sits near 0.889√p, above the
  roughly 0.88√p that other diagonal states reach. When p ≡ 2 there is one class, near 0.85√p.
- The best class tends to 8/(3π)√p (§2(1)). The pattern ends where it falls below the other states, after 19: at 31,
  37 and 43 the search beats it. This was predicted before the search, and the 43 margin is thin.

**(8) What the winners share** (round 33).
- The T state's Wigner function has 2p affine symmetries, or 6p when p ≡ 1 (mod 3):
  - the p shears (q, s) ↦ (q + d, s + 6cdq + 3cd²);
  - the reflection (q, s) ↦ (−q, s), which is complex conjugation with parity, since cx³ is odd;
  - the dilations by cube roots of unity, when they exist.
- The states that beat it keep at most one of these, the reflection, which makes them odd phase functions after a
  Clifford phase. They do at 5, 11, 37, 41 and 43, and nearly at 31 and 47, but not at 17, 23 and 29.
- At 5 the optimum is a single state, odd, with phases (0, 0.7514, 0.7881, 0.2119, 0.2486) turns after removing
  ω^(x²). Its orbit under the diagonal Clifford group (20 affine maps times 25 quadratic phases) has 500 members,
  the count of optimal gates in [FL26].
- No common closed form was found. Two registered guesses about the winners' structure failed at 41 and 47.

## 3. Evidence

The predictions were registered, with the script, before any value above p = 29 was computed
([`PREREG.md`](PREREG.md), rounds 29 to 33).

| quantity | range | prediction | measured |
|---|---|---|---|
| T state, mean S/√p | every class, primes 1000–3000 (516 states) | 8/(3π) ± 0.003 | 0.84890 |
| T state above the Haar mean | every class, every prime 31–5000 | yes | yes |
| degrees 5, 6 (x⁵, x⁶, one random each), mean S/√p | primes 700–1500 | κ₂ ± 0.004, below the Haar mean | 0.78989 to 0.79067, below the Haar mean at every prime |
| degrees 7, 8, mean S/√p | primes 700–1500 | κ₃ ± 0.004 | 0.79785 to 0.79857 |
| the best phase state at p = 7 | all 2401 classes | not a T state (a guess) | a T state: the guess failed |
| a fine phase beats T at p = 5 | all 390 625 | yes | yes: 129 500 do; the best is 1.969982 |
| the best fine phase vs arbitrary phases at p = 5 | 300 optimizations | ≥ 99% | 99.6% (1.969982 against 1.977576) |
| arbitrary phases beat T at p = 7 | 400 optimizations | yes (a guess) | no: the best found is the T state; the guess failed |
| the T state is the optimum at p = 7 | branch and bound over all phases | (a theorem, not a prediction) | proved: every box discarded, 47 136 512 in floating point and 47 174 654 with rigorous bounds |
| the optimum at p = 5 | branch and bound over all phases | (a theorem, not a prediction) | proved: one orbit of 500 states, S*₅ = 1.9775758213085… |
| random p²-th-root phases, mean S/√p | primes 500–1000 | the Haar mean ± 0.002 | 0.79801 against 0.79816 |
| T optimal at 13, 19 (≡ 1 mod 3) | ~690 optimizations each | nothing above T | nothing above T |
| T beaten at 17, 23 (≡ 2 mod 3) | ~630 optimizations each | a state above T | 0.8803 and 0.8860, against 0.8493 and 0.8470 |
| the pattern ends: T beaten at 31, 37, 43 (≡ 1) | ~690 optimizations each | a state above the best T class | 0.8800, 0.8775 and 0.8759, against 0.8734, 0.8740 and 0.8756 |

- For one class, the deviation of S/√p from 8/(3π) is about 5·10⁻⁴ for p from 1000 to 5000.
- For p ≡ 1 (mod 3), the spread between the three classes shrinks like p^(−1/2).

## 4. A consequence

In quasi-probability simulation the number of samples grows with the square of the product of the Wigner norms [PWB].
So each T state multiplies the cost by about (64/(9π²))·p ≈ 0.72p, against (2/π)·p ≈ 0.64p for a random state.

## 5. What is known, and what may be new

- **Known.**
  - The Howard–Vala gates and the diagonal Clifford hierarchy [HV, CGK].
  - Gross's Wigner function, negativity and mana [G, VMGE].
  - The Haar-random mana [WW].
  - The Airy analogy for the qudit T gate's Wigner function [KL].
  - The equidistribution of Birch sums [L, K], Katz's monodromy theorems [K], and Deligne's equidistribution theorem.
  - The optimality results of Li, Feng and Luo, and the three Clifford classes of T gates [LL, FL24, FL25, FL26].
  - Zhu, Mao and Yi's third moments [ZMY].
- **Not found in the literature we could read.**
  - The limit S/√p → 8/(3π) for T states, and its comparison with random states.
  - The ladder κ_m, and in particular that quintic and sextic phase states are less negative than random states.
  - The exhaustive maxima at p = 5 and 7 for phases that are p-th roots of unity. The case p = 5 may be implicit in
    [FL26].
  - The pattern by p mod 3, and its end: the T gate is the most negative diagonal gate at p = 3, 7, 13 and 19, and is
    beaten at 5, 11, 17, 23, 29, 31, 37 and 43.
  - The theorem at p = 7, which answers [FL26]'s open question there.

## References

- [C] G. Chênevert, *Exponential sums, hypersurfaces with many symmetries and Galois representations*, PhD thesis,
  McGill University (2008).
- [CGK] S. X. Cui, D. Gottesman and A. Krishna, Diagonal gates in the Clifford hierarchy, *Phys. Rev. A* **95**,
  012329 (2017).
- [FL24] L. Feng and S. Luo, Optimality of the Howard–Vala T-gate in stabilizer quantum computation, *Phys. Scr.* (2024),
  doi:10.1088/1402-4896/ad80e7.
- [FL25] L. Feng and S. Luo, Clifford equivalence of Howard–Vala T-gates, *Eur. Phys. J. Plus* (2025),
  doi:10.1140/epjp/s13360-025-06394-x.
- [FL26] L. Feng and S. Luo, Optimal ququint diagonal gates for generating Wigner negativity, *Phys. Rev. A* **113**,
  042434 (2026).
- [G] D. Gross, Hudson's theorem for finite-dimensional quantum systems, *J. Math. Phys.* **47**, 122107 (2006).
- [HV] M. Howard and J. Vala, Qudit versions of the qubit π/8 gate, *Phys. Rev. A* **86**, 022316 (2012).
- [K] N. M. Katz, On the monodromy groups attached to certain families of exponential sums, *Duke Math. J.* **54**
  (1987).
- [KL] L. Kocia and P. Love, Stationary phase method in discrete Wigner functions and classical simulation of quantum
  circuits, *Quantum* **5**, 494 (2021).
- [L] R. Livné, The average distribution of cubic exponential sums, *J. reine angew. Math.* **375/376** (1987).
- [LL] X. Li and S. Luo, Optimal diagonal qutrit gates for creating Wigner negativity, *Phys. Lett. A* (2023),
  doi:10.1016/j.physleta.2022.128620.
- [PWB] H. Pashayan, J. J. Wallman and S. D. Bartlett, Estimating outcome probabilities of quantum circuits using
  quasiprobabilities, *Phys. Rev. Lett.* **115**, 070501 (2015).
- [VMGE] V. Veitch, S. A. H. Mousavian, D. Gottesman and J. Emerson, The resource theory of stabilizer quantum
  computation, *New J. Phys.* **16**, 013009 (2014).
- [WW] J. Wilson and C. D. White, Mana in Haar-random states, arXiv:2011.13937.
- [ZMY] H. Zhu, C. Mao and C. Yi, Third moments of qudit Clifford orbits and 3-designs based on magic orbits,
  arXiv:2410.13575 (2024).

**Code.** [`one_wheel.py`](one_wheel.py) has three modes:
- `calibrate`: the identities of §2 and the constants κ_m ([`one_wheel_calibrate.log`](one_wheel_calibrate.log));
- `test`: the registered predictions of §3 ([`one_wheel_test.log`](one_wheel_test.log));
- `reads`: the analysis after the test ([`one_wheel_reads.log`](one_wheel_reads.log)).

[`fine_phases.py`](fine_phases.py) runs round 30 ([`fine_phases_calibrate.log`](fine_phases_calibrate.log),
[`fine_phases_test.log`](fine_phases_test.log)). Its calibration reproduces Li and Luo's optimum at p = 3.
[`diagonal_coin.py`](diagonal_coin.py) runs round 31 ([`diagonal_coin_calibrate.log`](diagonal_coin_calibrate.log),
[`diagonal_coin_test.log`](diagonal_coin_test.log), [`diagonal_coin_edge.log`](diagonal_coin_edge.log)).
[`winners.py`](winners.py) runs round 33 ([`winners_explore.log`](winners_explore.log),
[`winners_test.log`](winners_test.log)). [`t_optimal_7.py`](t_optimal_7.py) proves the theorem at p = 7
([`t_optimal_7_check.log`](t_optimal_7_check.log), [`t_optimal_7.log`](t_optimal_7.log),
[`t_optimal_7_control.log`](t_optimal_7_control.log)). [`diagonal_optimum/`](diagonal_optimum/OPTIMUM.md) proves the
theorem at 5 ([`bb5.log`](diagonal_optimum/bb5.log)), and [`arb_check.py`](diagonal_optimum/arb_check.py) proves
the theorems at 3, 5 and 7 again in Arb ([`arb3.log`](diagonal_optimum/arb3.log),
[`arb5.log`](diagonal_optimum/arb5.log), [`arb7.log`](diagonal_optimum/arb7.log)).
[`t7_rigorous/`](t7_rigorous/RIGOROUS.md) proves the theorem at 7 again with rigorous bounds ([`constants.log`](t7_rigorous/constants.log), [`selftest.log`](t7_rigorous/selftest.log),
[`t7_rigorous.log`](t7_rigorous/t7_rigorous.log)).
