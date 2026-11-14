# The torus states: exact third and fourth moments

> *write the proof and test the higher moments* — the author, 13 November 2026

### Tags: **[FORCED]** proved here and checked by [`verify_torus_moments.py`](verify_torus_moments.py) · **[NAMED]** a cited standard result · **[measured]** a computed result · **[READING]** an interpretation, not a claim.

**Keywords:** magic states · Wigner negativity · discrete Wigner function · qudits · Clifford hierarchy · Kloosterman sums · Sato–Tate law · Weil representation · quantum chaos · quantum cat map · Hecke eigenstates · Walsh spectra · bent functions · elliptic curves · finite fields · pre-registered predictions

Round 11 measured the magic of the oscillator states, the eigenvectors of the two tori of SL(2, p), at every prime up
to 401, and found the Sato–Tate law ([README](README.md) §13). One number in it came out exact: averaged over the
non-split torus's eigenvectors, the fourth-moment ratio of the Wigner values is 2p/(p + 1), to rounding, at every
prime tested. This page proves it (§2 to §4). Round 12 then tested the higher moments (§5), and the skew it
measured, about −1/√p, turned out exact as well: §6 proves the third moment.

## 1. The setting

- p is an odd prime. The phase-point operators are round 3's: ⟨a|A_(q,k)|b⟩ = [a + b = 2q] ω^(k(a − b)), with
  ω = e^(2πi/p). A state's Wigner function is W(u) = ⟨ψ|A_u|ψ⟩/p at the p² points u = (q, k). Each A_u is a Hermitian
  operator with A_u² = 1, and A_0 is the half turn P.
- The symplectic form is ⟨u, v⟩ = q_u k_v − k_u q_v. Every g in SL(2, p) has a unitary U_g with
  U_g A_u U_g† = A_(gu): the Weil representation [NAMED: Weil 1964].
- The non-split torus T is a cyclic subgroup of SL(2, p) of order p + 1, the turning wheel of §9 of the README.
  - Off the origin its orbits are p − 1 circles of p + 1 points: the level sets Q(v) = r, r ≠ 0, of a quadratic form Q
    that T keeps and that vanishes only at 0.
  - On the p-dimensional space of states the U_g, g in T, have p distinct characters [NAMED: Gurevich, Hadani and
    Sochen]. So they share one orthonormal eigenbasis ψ_1, …, ψ_p, the non-split oscillator states, each fixed by T up
    to a phase.
  - T contains −1, which acts as ± the half turn, so each ψ_j is even or odd, and W_j(0) = ±1/p.

## 2. The theorem

**Theorem** [FORCED]. Averaged over the eigenbasis,

  (1/p) Σ_j Σ_u W_j(u)⁴ = 1/p⁴ + 2(p − 1)/(p³(p + 1)²).

Every ψ_j has the same second moment off the origin (Σ W² = 1/p, and W(0)² = 1/p²). So, equivalently, the average over
the eigenbasis of μ4/μ2², the fourth moment of the Wigner values off the origin over the square of the second, is
exactly **2p/(p + 1)**.

## 3. Proof

**Step 1: constant on circles.** U_g ψ_j is a phase times ψ_j, so W_j(gu) = ⟨U_g† ψ_j|A_u|U_g† ψ_j⟩/p = W_j(u). So each
W_j is constant on each circle.

**Step 2: the torus average is diagonal.** Let Ā_u = (1/(p + 1)) Σ_(g in T) A_(gu). It commutes with every U_g, and the
U_g have p distinct characters, so Ā_u is diagonal in the eigenbasis. By Step 1 its entries are
⟨ψ_j|Ā_u|ψ_j⟩ = p W_j(u). Hence, for every power,

  Σ_j W_j(u)^(2k) = p^(−2k) Tr(Ā_u^(2k)).

So every even moment, averaged over the eigenbasis, is a trace.

**Step 3: four phase-point operators.** A_(q1,k1) A_(q2,k2) is a phase times X^(2(q1 − q2)) Z^(2(k1 − k2)), where
X|x⟩ = |x + 1⟩ and Z|x⟩ = ω^x |x⟩. Multiplying two such products and taking the trace,

  Tr(A_(u1) A_(u2) A_(u3) A_(u4)) = p ω^(−2⟨u1 − u2, u3 − u2⟩) if u1 − u2 + u3 − u4 = 0, and 0 otherwise.

The phase is the area of the parallelogram the four points make.

**Step 4: parallelograms on a circle.** Let C be a circle, m = p + 1 its number of points, and
Ā_C = (1/m) Σ_(v in C) A_v. By Step 3, Tr(Ā_C⁴) is (p/m⁴) times a sum, over the solutions in C of v1 + v3 = v2 + v4, of
the area phases.
- The solutions are exactly three families: v2 = v1 (and v4 = v3); v2 = v3 (and v4 = v1); v3 = −v1 (and v4 = −v2).
  For if s = v1 + v3 is not 0, the points v of C with s − v also on C satisfy Q(s) = 2B(s, v), where B is Q's bilinear
  form. That is a line, which meets C at most twice, so {v2, v4} = {v1, v3}.
- The first two families have area 0, phase 1. The third has phase ω^(4⟨v1, v2⟩).
- Each family has m² members. Each pair of families shares m members, all of area 0, and no solution lies in all three.
  So

  Tr(Ā_C⁴) = (p/m⁴)(2m² − 3m + Φ(C)),   where Φ(C) = Σ_(v1, v2 in C) ω^(4⟨v1, v2⟩).

**Step 5: the circle sums.** T acts on C transitively and keeps ⟨ , ⟩, so Φ(C) = m Σ_(v in C) ω^(4⟨v1, v⟩) for any
fixed v1 in C.
- Take w with ⟨v1, w⟩ = 1 and write v = λv1 + μw. On C, Q(v) = r λ² + 2bλμ + cμ² = r, where r = Q(v1).
- For fixed μ that is a quadratic in λ with 1 + η(δμ² + r²) roots. Here η is the Legendre symbol and δ = b² − rc. δ is
  minus the determinant of Q in a symplectic basis, the same for every circle, and a non-square because Q vanishes only
  at 0.
- So Σ_(v in C) ω^(4⟨v1, v⟩) = Σ_μ (1 + η(δμ² + r²)) ω^(4μ) = Σ_μ η(δμ² + r²) ω^(4μ).
- Each circle is one level r ≠ 0, so summing over the p − 1 circles sums over every nonzero r once. And
  Σ_(r ≠ 0) η(δμ² + r²) is p − 1 for μ = 0 and 0 otherwise, by two standard Legendre-symbol sums [NAMED]:
  Σ_x η(x² + c) = −1 for c ≠ 0, and η(δ) = −1. So Σ_C Φ(C)/m = p − 1, though each Φ(C) alone varies.

**Step 6: adding up.** By Step 5, Σ_C Φ(C) = m(p − 1). With Step 4,

  Σ_u Tr(Ā_u⁴) = Tr(P⁴) + m Σ_C Tr(Ā_C⁴) = p + (p/m³)[(p − 1)(2m² − 3m) + m(p − 1)] = p + 2p²(p − 1)/(p + 1)².

Dividing by p⁴ (Step 2 with k = 2) and by p (the average over the p states) gives the theorem. For the ratio: off the
origin every ψ_j has μ2 = (1/p − 1/p²)/(p² − 1) = 1/(p²(p + 1)), and the theorem gives the average
μ4 = 2/(p³(p + 1)³), so the average of μ4/μ2² is 2p/(p + 1). ∎

## 4. What it says

- As p grows, 2p/(p + 1) tends to 2, the fourth moment of the semicircle law, which is Sato–Tate's value. Here it comes
  out exactly, from a count of parallelograms on circles, not from statistics. Kurlberg and Rudnick computed fourth
  moments of matrix elements of Hecke eigenfunctions in the same spirit [NAMED].
- Step 2 holds for every power. Averaged over the eigenbasis, the 2k-th moment is a count of closed 2k-gons on the
  circles, each weighted by its area phase. For k = 2 the count is elementary; for k ≥ 3 the polygons can bend, and the
  count is a genuine character sum. Round 12 measured k = 3 and 4.
- Odd powers are traces too, and there every polygon counts: a product of an odd number of phase-point operators is
  again one, with trace 1. §6 counts the triangles.

## 5. The higher moments (round 12)

The theorem fixes one moment, and only on average. Round 12 tested the rest of the shape: registered before the run
([`PREREG.md`](PREREG.md)), with the script [`torus_moments.py`](torus_moments.py), on every one-line oscillator
state of round 11. Each state's Wigner values off the origin were centered and scaled to variance 1. All six
predictions held [measured, exact values]. At the primes from 211 to 401, over 20 056 states and 2.06 billion values:

| | 3rd moment | 4th | 6th | 8th | Kolmogorov distance |
|---|---|---|---|---|---|
| the oscillator states | −0.057 | 2.010 | 5.066 | 14.35 | — |
| semicircle (Sato–Tate) | 0 | 2 | 5 | 14 | **0.0072** |
| Gaussian (the average random state) | 0 | 3 | 15 | 105 | 0.0426 |
| arcsine (a uniform angle) | 0 | 1.5 | 2.5 | 4.375 | 0.0943 |

- The whole distribution is the semicircle, not only its first statistics. Its distance to the semicircle law is a
  sixth of its distance to the Gaussian.
- The non-split torus's states are closest. At every prime from 211 to 401 their basis averages lie within 0.024 of 5
  for the sixth moment and within 0.21 of 14 for the eighth. The split torus's states come up from above, more slowly:
  their tiny values on the two axes put extra weight near 0.
- The skew is small and shrinking: about −1/√p (for the non-split states −1.010/√p to −1.003/√p from 101 to 401).
  For the non-split states it is now a theorem (§6).
- After centering, the non-split states' average fourth moment lies within about 3/p² of 2.

So the Sato–Tate law holds for these states through the eighth moment at these sizes. Only the third and fourth
moments are proved (§2 and §6); the others are measured.

## 6. The third moment: the taper [FORCED]

> *it's not a single prime... in my mind it's the prime gradient... how they are spread, producing a compression and a
> taper* — the author, 14 November 2026

Round 12 measured a small negative skew, about −1/√p, which shrinks as the primes grow: the distribution tapers onto
the symmetric semicircle. The taper is exact.

**Theorem 2** [FORCED]. Averaged over the eigenbasis,

  (1/p) Σ_j Σ_u W_j(u)³ = 2/(p²(p + 1)).

Weighted by parity, with ε_j = p W_j(0) = ±1,

  Σ_j ε_j Σ_u W_j(u)³ = 1/p² if p ≡ 1 (mod 3),   and (1/p²)(1 − 2/(p + 1)) if p ≡ 2 (mod 3).

**Corollary: the taper** [FORCED]. Over all p² points every pure state has the same mean and variance, since Σ W = 1
and Σ W² = 1/p. So the average over the eigenbasis of the standardized third moment is exactly

  −(p + 2)/((p + 1)√(p − 1)) = −(1/√p)(1 + 3/(2p) − 1/(8p²) + …).

### Proof

**Step 1: odd powers are traces too.** Step 2 of §3 holds for every power, so Σ_j W_j(u)³ = p^(−3) Tr(Ā_u³). The
element −1 of T acts as ± the half turn P, so P is diagonal in the eigenbasis with entries ε_j, and
Σ_j ε_j W_j(u)³ = p^(−3) Tr(P Ā_u³).

**Step 2: three phase-point operators.** A product of three phase-point operators is another one times a phase,
A_(u1) A_(u2) A_(u3) = ω^(2⟨u2 − u1, u3 − u1⟩) A_(u1 − u2 + u3), and every A_u has trace 1. So
Tr(A_(u1) A_(u2) A_(u3)) = ω^(2⟨u2 − u1, u3 − u1⟩), and the exponent is twice the triangle's signed area.

**Step 3: triangles on a circle.** On a circle C, Ā_u is the same operator Ā_C for every u in C. By Step 2,
Tr(Ā_C³) = Θ(C)/m³, where Θ(C) sums ω^(2⟨v2 − v1, v3 − v1⟩) over the m³ ordered triangles with corners on C. At the
origin Ā_0 = P, and Tr P³ = Tr P = 1. So

  Σ_u Tr(Ā_u³) = 1 + Σ_C Θ(C)/m².

**Step 4: the circles as numbers.** Let ε be a non-square, F_p(√ε) the field of p² elements, and Im(x + y√ε) = y. In a
suitable basis of the phase plane, T acts by multiplication by the m elements μ of norm μμ̄ = 1, the circles are the
sets N(v) = r for r ≠ 0, and ⟨a, b⟩ = κ Im(ā b) for a fixed κ ≠ 0 [NAMED: the non-split tori are all conjugate, and
the alternating forms on the plane are the multiples of one]. Write the corners as a, aμ1 and aμ1μ2. Then

  ⟨v2 − v1, v3 − v1⟩ = κ r G(μ1, μ2),   where G(μ1, μ2) = Im μ1 + Im μ2 − Im(μ1μ2) and r = N(a).

So Θ(C) = m Σ_(μ1, μ2) ω^(2κ r G(μ1, μ2)). Summing over the circles sums over every r ≠ 0, and Σ_(r ≠ 0) ω^(2κ r G) is
p − 1 when G = 0 and −1 otherwise. Hence Σ_C Θ(C) = m(pZ − m²), where Z counts the pairs (μ1, μ2) with G = 0.

**Step 5: only degenerate triangles have area zero.** G = 0 says the triangle a, aμ1, aμ1μ2 has area zero, so its
corners lie on a line. A line meets a circle at most twice (§3, Step 4), so two corners coincide: μ1 = 1, μ2 = 1 or
μ1μ2 = 1. Each of the three gives m pairs, and any two share only the pair (1, 1), so Z = 3m − 2 = 3p + 1.
- The same count, explicitly: every μ ≠ 1 of norm 1 is (t + √ε)/(t − √ε) for exactly one t in F_p, and then
  G = −4ε(t1 + t2)/((t1² − ε)(t2² − ε)), which vanishes exactly when t1 + t2 = 0, that is when μ1μ2 = 1.
- [READING] This parametrization is the Smith chart, Γ(z) = (z − 1)/(z + 1) (the README's §15): μ = Γ(−z) with
  z = t/√ε. The pure reactances z go to the rim of the chart, which is the turning wheel, and two opposite reactances
  give conjugate reflections, whose product is 1.

**Step 6: adding up.** Σ_C Θ(C) = m(p(3p + 1) − m²) = (p + 1)(p − 1)(2p + 1), so
Σ_u Tr(Ā_u³) = 1 + (p − 1)(2p + 1)/(p + 1) = 2p²/(p + 1). Dividing by p³ (Step 1) and by p gives the theorem.

**Step 7: the hexagons.** For the parity split: at the origin Tr(P Ā_0³) = Tr P⁴ = p. Off it, §3's Step 3 with u1 = 0
gives Tr(P A_(v1) A_(v2) A_(v3)) = p ω^(2⟨v1, v3⟩) when v2 = v1 + v3, and 0 otherwise. So only the pairs v1, v3 on a
circle whose sum is on the circle too count.
- In the field, v3 = v1μ with N(1 + μ) = 1, that is μ + μ̄ = −1: μ is a primitive cube root of unity. Then v1,
  v1 + v3 and v3 are three consecutive corners of a hexagon inscribed in the circle, the orbit of v1 under the wheel's
  turn of order 6.
- The turning wheel holds the cube roots of unity exactly when 3 divides its number of points, p + 1, that is when
  p ≡ 2 (mod 3). Then each circle has 2m such pairs, and Σ_(u ≠ 0) Tr(P Ā_u³) = (p/m) Σ_(r ≠ 0) (ω^(cr) + ω^(−cr)) =
  −2p/(p + 1), for a fixed c ≠ 0.
- When p ≡ 1 (mod 3) there are none, and the sum is 0.

Dividing p − 2p/(p + 1), or p, by p³ gives the split. For the corollary: over all points each state has mean 1/p² and
variance (p − 1)/p⁴, so the average standardized third moment is
(2/(p⁴(p + 1)) − 3/p⁵ + 2/p⁶)/((p − 1)/p⁴)^(3/2) = −(p + 2)/((p + 1)√(p − 1)). ∎

### Off the origin, and round 12

Round 12 standardized each state's values off the origin. There a state's mean depends only on its parity,
(1 − ε_j/p)/(p² − 1), and its second moment is 1/(p²(p + 1)) for every state (§3, Step 6). The split fixes each
parity class's average third moment exactly. The average sums Σ_(u ≠ 0) W³ are:

| | p ≡ 1 (mod 3) | p ≡ 2 (mod 3) |
|---|---|---|
| the (p + 1)/2 even states | (p − 1)(2p + 1)/(p³(p + 1)²) | (2p² − 3p − 1)/(p³(p + 1)²) |
| the (p − 1)/2 odd states | (2p + 1)/(p³(p + 1)) | (2p − 1)/(p³(p − 1)) |

From them the average standardized third moment off the origin is exact too (`offorigin_skew` in
[`verify_torus_moments.py`](verify_torus_moments.py)). It reproduces all 77 of round 12's logged non-split averages,
from 5 to 401, to their six printed decimals: −0.402492 at 5, −0.100478 at 101, −0.050062 at 401. Expanded, it is
−(1/√p)(1 + 1/p − 1/p² − c/p³ − …), with c = 3 when p ≡ 1 (mod 3) and c = 9 when p ≡ 2. The hexagons first show in
the fourth term.

### What it says

- **The taper is exact.** Both proved moments taper onto the semicircle at known rates: the skew to 0 as −1/√p, and the
  fourth-moment ratio to 2 as 2 − 2/(p + 1). [READING] This is the taper of the author's prime gradient, on this floor:
  how the shape at each prime approaches its limit, prime by prime.
- **One fact closes both proofs.** The fourth moment needed parallelograms on a circle, the third needs triangles, and
  both close because a line meets a circle at most twice.
- **The odd moment sees the hexagon.** The parity split is a coin by p mod 3: whether the turning wheel holds a hexagon.
  Its two faces differ in the skew only from the fourth term on.
- **In quantum chaos** [NAMED]. The non-split oscillator states are the Hecke eigenstates of the quantum cat maps at
  the primes where the map's characteristic polynomial stays irreducible (Kurlberg and Rudnick 2000). For smooth
  observables, Kurlberg and Rudnick computed the second and fourth moments of the normalized matrix elements and
  conjectured a law of traces of random SU(2) matrices (2005), and Rosenzweig showed that the fifth centered moment
  vanishes in the semiclassical limit (2009). Here the observables are the phase-point operators, and the third moment
  is exact at every prime.

## 7. Standing

- **Known, and credited** [NAMED]: the Weil representation and its covariance (Weil 1964); the multiplicity-free action
  of a torus, and the oscillator states (Gurevich, Hadani and Sochen 2008); the algebra of phase-point operators
  (Wootters 1987; Gross 2006); conics over finite fields and the Legendre-symbol sums (Lidl and Niederreiter); the
  Hecke eigenstates of the quantum cat map (Kurlberg and Rudnick 2000), and the moments of their matrix elements for
  smooth observables: the second and fourth (Kurlberg and Rudnick 2005) and the fifth (Rosenzweig 2009).
- **This repository's own, new as far as we checked:** the two theorems, the exact average fourth moment (§2) and third
  moment with its parity split (§6) of the oscillator states' Wigner values, with these proofs, and the exact skew laws
  they give. Web searches on 2026-11-14 found the nearest work in Kurlberg and Rudnick's and Rosenzweig's papers;
  none computes a third moment of the Wigner function.
- **Checked** by [`verify_torus_moments.py`](verify_torus_moments.py), whose output is in
  [`verify_torus_moments.log`](verify_torus_moments.log). For §3: steps 1, 2, 3 and 6 with the operators themselves at
  every prime up to 31, and steps 4, 5 and the theorem by counting at every prime up to 101. For §6: the operator steps
  at every prime up to 31; the zero-area count, the Cayley formula, the triangle sums, the hexagons and both
  identities at every prime up to 101; and the off-origin skew against all 77 of round 12's logged values.
- **Measured, not proved:** the sixth and eighth moments and the whole distribution (§5;
  [`torus_moments_run.log`](torus_moments_run.log), [`torus_moments_combined.log`](torus_moments_combined.log)).

## Run it

```
python verify_torus_moments.py     # both proofs, step by step: about twenty seconds (numpy)
python torus_moments.py calibrate  # round 12: seconds
python torus_moments.py run        # about eleven minutes, one process
python torus_moments.py combine
```

## Sources

- A. Weil, "Sur certains groupes d'opérateurs unitaires", *Acta Math.* **111** (1964).
- S. Gurevich, R. Hadani and N. Sochen, "The finite harmonic oscillator and its associated sequences", *Proc. Natl.
  Acad. Sci.* **105** (2008), [PMC2481336](https://pmc.ncbi.nlm.nih.gov/articles/PMC2481336).
- P. Kurlberg and Z. Rudnick, "Hecke theory and equidistribution for the quantization of linear maps of the torus",
  *Duke Math. J.* **103** (2000).
- P. Kurlberg and Z. Rudnick, "On the distribution of matrix elements for the quantum cat map", *Ann. of Math.* **161**
  (2005), [arXiv:math/0302277](https://arxiv.org/abs/math/0302277).
- L. Rosenzweig, "On the fluctuations of matrix elements of the quantum cat map" (2009),
  [arXiv:0909.1410](https://arxiv.org/abs/0909.1410).
- W. K. Wootters, "A Wigner-function formulation of finite-state quantum mechanics", *Ann. Phys.* **176** (1987);
  D. Gross, "Hudson's theorem for finite-dimensional quantum systems", *J. Math. Phys.* **47** (2006).
- R. Lidl and H. Niederreiter, *Finite Fields* (1983): quadratic forms over finite fields and the sums of the Legendre
  symbol.
