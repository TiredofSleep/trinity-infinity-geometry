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

## 3. Evidence

The predictions were registered, with the script, before any value above p = 29 was computed
([`PREREG.md`](PREREG.md), round 29).

| quantity | range | prediction | measured |
|---|---|---|---|
| T state, mean S/√p | every class, primes 1000–3000 (516 states) | 8/(3π) ± 0.003 | 0.84890 |
| T state above the Haar mean | every class, every prime 31–5000 | yes | yes |
| degrees 5, 6 (x⁵, x⁶, one random each), mean S/√p | primes 700–1500 | κ₂ ± 0.004, below the Haar mean | 0.78989 to 0.79067, below the Haar mean at every prime |
| degrees 7, 8, mean S/√p | primes 700–1500 | κ₃ ± 0.004 | 0.79785 to 0.79857 |
| the best phase state at p = 7 | all 2401 classes | not a T state (a guess) | a T state: the guess failed |

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
