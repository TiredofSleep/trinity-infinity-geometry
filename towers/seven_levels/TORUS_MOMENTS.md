# The torus states: exact third and fourth moments

> *write the proof and test the higher moments* — the author, 13 November 2026

### Tags: **[FORCED]** proved here and checked by [`verify_torus_moments.py`](verify_torus_moments.py) · **[NAMED]** a cited standard result · **[measured]** a computed result · **[READING]** an interpretation, not a claim.

**Keywords:** magic states · Wigner negativity · discrete Wigner function · qudits · Clifford hierarchy · Kloosterman sums · Sato–Tate law · Weil representation · quantum chaos · quantum cat map · Hecke eigenstates · Walsh spectra · bent functions · elliptic curves · finite fields · Calabi–Yau threefolds · double octics · Clebsch cubic surface · modular symbols · Hermitian Gauss sums · pre-registered predictions

Round 11 measured the magic of the oscillator states, the eigenvectors of the two tori of SL(2, p), at every prime up
to 401, and found the Sato–Tate law ([README](README.md) §13). One number in it came out exact: averaged over the
non-split torus's eigenvectors, the fourth-moment ratio of the Wigner values is 2p/(p + 1), to rounding, at every
prime tested. This page proves it (§2 to §4). Round 12 then tested the higher moments (§5), and the skew it
measured, about −1/√p, turned out exact as well: §6 proves the third moment. §7 says why the whole law is the
semicircle: every moment is a count of polygons, and only the non-crossing ones survive, as in free probability.
§8 makes the sixth moment and the fourth free cumulant exact, and modular forms appear in them.

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
  how the shape at each prime approaches its limit, prime by prime ([`../THE_STAIRCASE.md`](../THE_STAIRCASE.md)).
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

## 7. Every moment: the free picture [FORCED; measured; NAMED]

> *2 and 3* — the author, 14 November 2026, asked whether to try a proof of the whole semicircle through free
> probability

Round 12 found the semicircle through the eighth moment, and §2 and §6 prove the fourth and the third. This section
shows why the answer is a semicircle, and what a proof of every moment needs. Round 15, registered first, tests it
([`PREREG.md`](PREREG.md); [`free_moments.py`](free_moments.py)).

**Theorem 3** [FORCED; checked by `free_moments.py calibrate`]. Let S_C = Σ_(v in C) A_v be the sum of the
phase-point operators over a circle, and m = p + 1.

1. **The moments are counts on one circle.** Averaged over the eigenbasis,
   Σ_u W(u)^k = p^(−k−1) [Tr P^k + m^(1−k) Σ_C Tr S_C^k], and

     Σ_C Tr S_C^k = p(p Z_k − N_k) for even k,   p Z_k − m^k for odd k.

   Here N_k counts the closed k-gons with corners on one circle (u1 − u2 + u3 − … = 0; for odd k every k-tuple
   counts), and Z_k those whose phase Φ is 0. The first equation is Step 2 of §3. For the second: the circles are
   dilations of one another, by elements of the field with p² elements; a dilation multiplies every symplectic
   product by its norm; and summing ω^(sΦ) over the p − 1 norms s gives p[Φ = 0] − 1.
2. **The phase is a fan of triangles.** A product of k phase-point operators is a phase-point operator (k odd) or a
   shift (k even), times ω^Φ, with Φ = Σ 2⟨u_(2i) − w, u_(2i+1) − w⟩ along a fan (w is the running alternating sum).
   The shift has trace p exactly when the polygon closes.
3. **Non-crossing pairings give the Catalan numbers.** A pairing matches the corners in twos, equal when their signs
   in u1 − u2 + … are opposite and opposite when the signs agree, so every paired polygon closes. If the pairing does
   not cross, some matched corners are neighbours, and A_v A_v = 1 removes them; by induction the product is the
   identity, so Φ = 0. With the first corner fixed, each of the Cat(j) non-crossing pairings of 2j corners gives
   m^(j−1) polygons, and they overlap only in lower order. So in the normalized moment
   (1/(p − 1)) Σ_C (1/p) Tr (S_C/√m)^(2j) they contribute exactly Cat(j) in the limit: the semicircle's moments.
4. **Crossing pairings fall away.** On each crossing pairing the phase is not identically 0 (checked for all 10 at
   k = 6 and all 91 at k = 8). So it vanishes only on a lower-dimensional part, and each crossing pairing contributes
   O(1/p).
5. **What is left are the generic polygons**, the closed ones on no pairing. At k = 4 there are none (§3, Step 4),
   which is why the fourth moment came out exact. From k = 6 on they outnumber the paired ones, about p^(2j−3)
   against p^(j−1) with the first corner fixed. Their contribution is (p Z_gen − N_gen)/((p − 1) m^(j−1)), a sum of
   ω^(tΦ) over t ≠ 0 and over the generic polygons.

**Corollary: the free picture.** The oscillator states' Wigner values follow the semicircle in every moment exactly
when, for every j, the phases of the generic closed 2j-gons on a circle cancel: p Z_gen − N_gen = o(p^j).
- At 2j = 6 it is enough that the phase takes each of its p values equally often, to leading order (Lang and Weil's
  count of points would give it, if the generic hexagons and their zero-phase slice have matching components).
- From 2j = 8 on it needs square-root cancellation of Σ ω^(tΦ) over the generic polygons, which is the kind of bound
  Deligne's theorem gives for good families.
- [READING] This is free probability's mechanism. If the phase-point operators commuted, every pairing would count,
  and the moments would be the Gaussian's (2j − 1)!!. They do not commute: their commutation phase is a symplectic
  area, and on a crossing pairing it averages away. What is left is the semicircle of the free central limit theorem
  [NAMED: Voiculescu]. The q-Gaussians interpolate between the two by weighting each crossing with q [NAMED: Bożejko
  and Speicher 1991]; this floor sits at q = 0 to leading order.
- The odd moments are where the arithmetic shows. At k = 3 no generic triangle has phase 0, because a line meets a
  circle at most twice (§6); that small refusal of equidistribution is the −1/√p skew.
- Each Wigner value is also a Fourier transform on the torus: p W_χ(u) = (1/m) Σ_(g in T) χ̄(g) Tr(U_g A_u). So the
  semicircle at a fixed point u, as p grows, is an equidistribution theorem for Fourier transforms of trace functions
  on a commutative algebraic group, the setting of Forey, Fresán and Kowalski [NAMED]. That route is not attempted here.

### Round 15: the tests

Eight predictions were registered with [`free_moments.py`](free_moments.py) before the run ([`PREREG.md`](PREREG.md)),
and all eight held. The output is in [`free_moments_calibrate.log`](free_moments_calibrate.log) and
[`free_moments_run.log`](free_moments_run.log).

- **The sixth moment, taken apart** [measured, exact counts]. On one circle, with the first corner fixed, at every
  prime up to 101:

  | p | non-crossing | crossing | generic | p·Z_gen/N_gen |
  |---|---|---|---|---|
  | 31 | 4.814 | −0.209 | 0.023 | 1.027 |
  | 61 | 4.904 | −0.109 | 0.011 | 1.012 |
  | 101 | 4.941 | −0.067 | 0.028 | 1.029 |
  | the free limit | 5 | 0 | 0 | 1 |

  The non-crossing part falls short of 5 by about 6/p (its families overlap), and the crossing part is about −6.6/p.
  The generic part is about 0.9/p when p is 1 more than a multiple of 3 and 2.8/p when it is 2 more, where the
  turning wheel holds hexagons. So the generic phases cancel, to order 1/p.
- **The higher moments** [measured, exact values]: basis averages of each state's standardized values off the origin.

  | | 6th | 8th | 10th | 12th |
  |---|---|---|---|---|
  | p = 211 | 5.017 | 14.160 | 43.05 | 137.8 |
  | p = 1009 | 5.003 | 14.030 | 42.20 | 133.1 |
  | semicircle | 5 | 14 | 42 | 132 |
  | Gaussian | 15 | 105 | 945 | 10 395 |

- **The corrections are free** [measured; registered for the fifth moment, read after the run for the others]. Each
  odd moment over the third:

  | | m5/m3 | m7/m3 | m9/m3 | m11/m3 |
  |---|---|---|---|---|
  | p = 1009 | 5.014 | 21.01 | 83.8 | 328.7 |
  | free: non-crossing partitions into one triple and pairs | 5 | 21 | 84 | 330 |
  | classical: all such partitions | 10 | 105 | 1 260 | 17 325 |

  At 211 the four ratios are within 5% of the free counts, and at 1009 within 0.4%. So, to first order, the law is
  the semicircle perturbed by one free cumulant, κ3 = m3 ≈ −1/√p, with the next ones small: κ4 = m4 − 2 is 3/p² to
  the log's rounding, and m6 − 5 is close to the free value 3κ3².

### What it says

- **Why a semicircle.** Every moment is a count of polygons on the circles, weighted by their areas. The pairings that
  do not cross have area 0 and give the Catalan numbers. The crossing pairings and the generic polygons carry area
  phases that cancel. If the phase-point operators commuted, every pairing would count and the law would be the
  Gaussian. Their commutation phase, a symplectic area, is what makes the law free.
- **A proof of every moment needs one statement:** the phases of the generic closed 2j-gons on a circle cancel,
  p Z_gen − N_gen = o(p^j) with the first corner fixed. At 2j = 6 the measurements say they cancel to O(p²), which is
  more than enough.
- **The corrections are free too.** The odd moments follow the non-crossing counts, not the classical ones, to 0.4% at
  1009. [READING] The Wigner values at a point are the eigenvalues of S_C, a sum of symmetries, one for each point of a
  circle, and these add like free variables. The arithmetic, the circle's geometry and its hexagons, enters only
  through a few small free cumulants.

## 8. The exact sixth and fifth moments, and the fourth free cumulant: modular forms enter [FORCED in part; measured exactly; NAMED]

> *go after an exact formula for the 6th moment first.. The free fourth cumulant equals 3/p² to every digit the log
> keeps. Worth a short exact proof as a small theorem* — the author, 14 November 2026

Every moment is an integer in disguise. Let I_n = Σ_C Tr S_C^n and J_n = Σ_C Tr(P S_C^n), summed over the p − 1
circles. By §7's Theorem 3,

  (1/p) Σ_j Σ_u W_j(u)^n = p^(−n−1) [Tr P^n + m^(1−n) I_n],   (1/p) Σ_j ε_j Σ_u W_j(u)^n = p^(−n−1) [Tr P^(n+1) + m^(1−n) J_n].

§2 and §6 prove I3 = (p + 1)(p − 1)(2p + 1), I4 = 2p²(p − 1)(p + 1) and J3 = −2p(p + 1) when p ≡ 2 (mod 3), else 0;
and I2 = p(p² − 1), J2 = p² − 1. [`exact_moments.py`](exact_moments.py) reads all of them from the states, as
integers, at every prime up to 401.

**Theorem 4: the sixth moment** [FORCED; proved here, given one classical evaluation, NAMED].

  I6 = p [5p⁴ − p³ − 5p² − 1 + (p + 1)(b(p) − (−3|p) p²)],

where b(p) is the p-th coefficient of (η(τ)η(2τ)η(3τ)η(6τ))² = q − 2q² − 3q³ + 4q⁴ + 6q⁵ + …, the newform of weight 4
and level 6, and (−3|p) is 1 or −1 as p is 1 or 2 more than a multiple of 3. So the basis average of Σ_u W(u)⁶ is
p^(−7)[p + I6/(p + 1)⁵].
- **Proved.** I6 = p(pZ6 − N6), by §7. N6, the closed hexagons on a circle, is ((p + 1)⁶ + (p + 1)V6)/p², where
  V6 = Σ_a K(a)⁶ is the sixth moment of the Kloosterman sums. The reason is that a circle's Fourier transform is a
  Kloosterman sum: Σ over the v with N(v) = r of ψ(Tr(αv)) is −K(r N(α)). And V6 = 5p⁴ − 10p³ − (b(p) + 9)p² − 5p − 1
  [NAMED: Hulek, Spandaw, van Geemen and van Straten 2001; checked here at every prime from 7 to 199].
- **Proved below: the phase-0 count.** Z6, the closed hexagons whose phase is 0, number
  (p + 1)(6p² + (4 − (−3|p))p + 1). It was found first at the primes from 7 to 199, predicted without refitting at
  every prime from 211 to 401 (round 16), and then proved by the elementary count below.
- So the modular form enters only through the closed polygons. The phase-0 polygons are a polynomial count, and the
  p mod 3 that round 15 saw in the generic part is the (−3|p) here.

**Proof of the phase-0 count** [FORCED; each step checked by [`verify_sixth_moment.py`](verify_sixth_moment.py)].
1. **Two triangles.** The six operators split as (A1A2A3)(A4A5A6). Each triple is one phase-point operator times
   ω^(2A), with A(x, y, z) = ⟨y − x, z − x⟩, and the remaining pair has trace p exactly when the hexagon closes,
   v1 − v2 + v3 = v4 − v5 + v6 =: w. So the phase is 2A(v1, v2, v3) + 2A(v4, v5, v6), and Z6 counts pairs of triangles
   on the circle with the same alternating sum w and cancelling areas. Reversing a triangle, (x, y, z) → (z, y, x),
   keeps w and negates the area, so Z6 = Σ_w Σ_a n_w(a)², where n_w(a) counts the triangles with alternating sum w and
   area a.
2. **The area of an inscribed triangle.** Work in the field model of §6 (Step 4), on the circle N(v) = r. Given w and
   y on the circle, put s = y + w; then x + z = s.
   - If s ≠ 0, write x = sξ. Then z = sξ̄, with Tr ξ = 1 and N ξ = r/N(s), so there are two, one or no such triangles
     as 1 − 4r/N(s) is a non-square, zero, or a nonzero square. The area is A = κ(N(w) − r)·Im ξ.
   - If s = 0, which needs w on the circle, then z = −x for every x, and A = 2⟨w, x⟩.
3. **Three kinds of w.**
   - **w = 0.** Then N ξ = Tr ξ = 1, so ξ is a primitive sixth root of unity, the hexagons of §6. There are two
     triangles for each y when p ≡ 2 (mod 3), with the same two areas ±α for every y, and none when p ≡ 1. So
     Σ_a n_0(a)² = (1 − χ)m², with χ = (−3|p).
   - **w on the circle.** Every triangle with s ≠ 0 has area 0. These are the degenerate ones, x = y or z = y, by
     §3's chord argument, and there are Q = 2m − 3 of them. The family with s = 0 has areas 2⟨w, x⟩; the number with
     area a is B(a) = 1 + η(1 + εa²/(4κ²r²)), and Σ_a B(a)² = 2p + 1 + (−1|p). So
     Σ_a n_w(a)² = Σ_a B(a)² + 2B(0)Q + Q² = 4p² + 6p − 2 + (−1|p), for each of the m points w of the circle.
   - **Every other w,** with N(w) = ν ∉ {0, r}. A nonzero area ±a comes from the y with N(y + w) = σ(a), one value σ
     for each pair ±a, and σ runs over the values with σ(σ − 4r) a non-square. Area 0 comes from N(y + w) = 4r. The
     number of y on the circle with N(y + w) = σ is M = 1 − η((σ − r − ν)² − 4rν), and M² = 2 − 2η(·) − [· = 0].
     Taking r = 1, which dilation allows, the sums over ν ∉ {0, 1} come out as follows. Σ_ν M(4)² = 2p − 1. The sum of
     the η terms is −(p − 1)/2 + [χ = −1]: each inner sum is a Legendre symbol of a quadratic in ν over a whole line,
     −1 because its discriminant 16σ is not 0. The zeros number (p − 2 + (−1|p))/2 − [χ = −1]. So these w contribute
     m[2p² − 3p + 3 − (−1|p) − (1 − χ)].
4. **Adding up.** The (−1|p) terms cancel:
   Z6 = (1 − χ)m² + m(4p² + 6p − 2 + (−1|p)) + m(2p² − 3p + 3 − (−1|p) − (1 − χ)) = m(6p² + (4 − χ)p + 1). ∎

The modular form is in N6 alone. Step 3 shows why the phase-0 count escapes it. There each count is 0, 1 or 2, so its
square is a linear combination of Legendre symbols. N6 = Σ_w (Σ_a n_w(a))² squares sums of many counts, and the cross
terms carry the sixth moment of the Kloosterman sums.

**Theorem 5: the fourth free cumulant** [exact given one count].

  J4 = (3p + 1)(p² − 1) − 4p(p + 1) b²,

where p = a² + b² with b even when p ≡ 1 (mod 4), and b = 0 when p ≡ 3 (mod 4). Equivalently,
J4 = 2p³ − 3p − 1 − (−1|p)(p³ + p²) + p(p + 1)c(p), with c(p) = 2(a² − b²) the coefficients of η(4τ)⁶, the newform of
weight 3 with complex multiplication by the Gaussian integers. With Theorems 1 and 2 this makes the basis average of
the standardized fourth moment off the origin exact. Its free cumulant κ4 = m4 − 2 is

  κ4 = [P(p) + 16 b² (p² − 2p − 1)] / (p² (p − 3)² (p² − 1)),

with P(p) = 3p⁴ − 26p³ + 40p² − 6p − 11 when p ≡ 1 (mod 3) and 3p⁴ − 34p³ + 32p² + 34p + 29 when p ≡ 2 (mod 3).
- So κ4 = 3/p² + (16 sin²θ_p − 8 − 8[p ≡ 2 mod 3])/p³ + O(1/p⁴), where sin²θ_p = b²/p and θ_p is the angle of the
  Gaussian prime a + bi, Hecke's angle (0 when p ≡ 3 mod 4). The 3/p² the logs showed is the leading term, not the
  whole.
- **Proved:** the algebra from J4 to κ4. **Measured exactly, proof open:** J4, found at the primes from 5 to 199 and
  predicted at every prime from 211 to 401 (round 16).
- [READING] J4 + (p + 1)⁴ = p(p + 1)(p² + 6p + 1 − 4b²) counts the 4-tuples on a circle whose five-gon phase with the
  origin vanishes: points on a surface. Its count, p² + 6p + 1 − 4b², is that of a surface whose middle cohomology
  carries η(4τ)⁶, as for a K3 surface with complex multiplication by the Gaussian integers. Where 4 divides p + 1 the
  turning wheel holds the fourth roots of unity and the count is a polynomial, as the third moment's count was where 3
  divides p + 1.

### The fifth moments

> *1, apply the hexagon method to the fifth moments* — the author, 14 November 2026

Round 16's search fitted the fifth moments to nothing. The reason is that their forms were outside its library: a
polynomial with the characters of p mod 3 and mod 4, plus one or two of fourteen modular forms. It did hold the
level-15 form below, but not together with an elliptic curve. The hexagon method of Theorem 4 finds J5. A second
method, Gauss sums of Hermitian forms, finds I5, and it reduces every odd I_n and every even J_n to one count on the
turning wheel. The forms were named with [`modular_symbols.py`](modular_symbols.py), written for this after LMFDB
answered a burst of queries with a captcha. It reproduces the four weight-4 eta products of levels 5, 6, 8 and 9.
Every step below is checked by [`verify_fifth_moment.py`](verify_fifth_moment.py)
([`verify_fifth_moment.log`](verify_fifth_moment.log)).

**Theorem 6: J5** [FORCED, given Kloosterman's fifth moment, NAMED].

  J5 = p(p + 1)[f(p) − p·a_E(p) + (4(−3|p) − 3)p − 1].

- f(p) is the p-th coefficient of η(3τ)³η(5τ)³ + η(τ)³η(15τ)³, the newform of weight 3 and level 15. It has complex
  multiplication by Q(√−15).
- E is the elliptic curve y² = x(x − 4)(4x² − 52x + 9), and a_E(p) = p + 1 − #E(F_p).
- [measured] E's traces are those of the newform of weight 2 and level 150 with a(7), a(11), a(13) = −2, 2, −6, at
  every prime from 7 to 401. So, as far as traces can tell, E has conductor 150; Tate's algorithm was not run.

*Proof.*
1. **Split.** J5 = p(pZ − N) by §7, with six operators P A_v1 ⋯ A_v5. Split them as (P A_v1 A_v2)(A_v3 A_v4 A_v5).
   The hexagon closes when v2 − v1 = v3 − v4 + v5 =: w, and its phase is 2⟨v1, v2⟩ + 2A(v3, v4, v5). So Z counts
   pairs of a chord (v1, v2) of the circle and a triangle with the same w and cancelling areas.
2. **Chords.** Put ν = N(w). For a chord with v2 − v1 = w, v1·w̄ is a root of X² + νX + ν. So there are two chords,
   with areas ±Y where 4εY² = ν² − 4ν, when ν² − 4ν is a non-square. There is one, of area 0, when ν = 4, and none
   otherwise.
3. **Triangles.** By Step 2 of Theorem 4's proof, with σ = 4(ν − 1)²/(2ν + 1), the triangles with alternating sum w
   and area Y number 1 − η(4ν² − 52ν + 9), for ν ∉ {0, 1, 4, −1/2}. The special classes:
   - ν = 1 (w on the circle) gives 2(1 + (13|p)) when (−3|p) = −1, and nothing otherwise;
   - ν = 4 gives 1 − (−15|p);
   - 2ν + 1 = 0 gives 0.
4. **Adding up.** Each class has p + 1 points w. Over the other ν the count is
   Σ (1 − η(ν(ν − 4)))(1 − η(4ν² − 52ν + 9)). Its cross term is the curve's character sum, and the Legendre sums of
   the two quadratics are −1 each. The special classes' (13|p) and (−15|p) cancel against the terms the sum leaves
   out. So Z = (p + 1)(p + 2 + Σ_ν η(ν(ν − 4)(4ν² − 52ν + 9))) = (p + 1)·#E(F_p).
5. **The closed hexagons.** By the circle's Fourier transform, N = ((p + 1)⁵ − (p + 1)V5)/p². Here
   V5 = Σ_a K(a)⁵ = 1 + 4p + 5p² + 4(−3|p)p³ + p²f(p), the fifth moment of the Kloosterman sums [NAMED: Peters, Top
   and van der Vlugt 1992, through a K3 surface; checked at every prime to 199]. ∎

**Theorem 7: I5** [FORCED given one count; that count measured exactly].

  I5 = p(p + 1)[p³ + 4p² − (1 + (5|p))p − 4 + a(p)] − p⁵ − 1,

where a(p) is the p-th coefficient of the newform of weight 4 and level 10: a(7), a(11), a(13), a(17), a(19) = −4, 12,
−58, 66, −100. So the basis average of Σ_u W(u)⁵ is p⁻⁶[1 + I5/(p + 1)⁴].

1. **The phase as a form.** With u_i = (−1)^i v_i, the five-point phase is a constant times Σ_(i<j) Im(ū_i u_j). In
   the field model each u_i is a unit of F_p². So Z5 counts the common zeros of six quadrics: the five norms
   N(u_i) = 1, and the phase.
2. **Gauss sums of Hermitian forms.** Expand each condition in additive characters. The six quadrics combine into the
   Hermitian form diag(λ) + hK on F_p²⁵, where K_ij = ±1/(2√ε) is a scaled tournament matrix. A Hermitian form of rank
   r has Gauss sum (−p)^r p^(2(5 − r)).
3. **The rank.** For h ≠ 0 put δ = 2λ/h. The principal minors are the real and imaginary parts of the products
   Π_(i in S)(1 + √ε δ_i).
   - So the rank is 5 or 4: if every 4-subset's product were imaginary, all five factors would be equal and the whole
     product imaginary.
   - The rank is 4 exactly when Π(1 + √ε δ_i) lies in F_p.
   - Hence I5 = (p + 1)(p·N_V − N_W). N_W counts the δ in F_p⁵ whose product lies in F_p, and N_V those that also
     have Σδ_i = 0.
4. **N_W = (p⁵ + 1)/(p + 1).** Under the Cayley map δ ↦ (1 + √ε δ)/(1 − √ε δ), the condition says that five points of
   the turning wheel, none equal to −1, multiply to 1. Count them with the wheel's characters.
5. **N_V is a double octic.** On Σδ = 0 the condition reads e3 + εe5 = 0, in the elementary symmetric functions.
   - Over each point of P³ = {Σδ = 0}, the scalings that solve it number 1 − (−1|p)η(e3e5), with separate counts
     where e3 or e5 vanishes.
   - e5 = Πδ_i vanishes on the five Sylvester planes.
   - On Σδ = 0, e3 = (Σδ_i³)/3 vanishes on Clebsch's diagonal cubic surface. It has p² + (6 + (5|p))p + 1 points,
     because its 27 lines are 15 over Q and 12 over Q(√5) [NAMED].
   - The planes and the cubic share 15 lines, with 15p − 20 points.
   - So N_V = p³ + 10p² − (20 + (5|p))p − 4 − (−1|p)S, where S = Σ_([δ] in P³) η(e3(δ)e5(δ)) is the character sum of
     the double octic w² = e3e5. That is the double cover of 3-space branched along the Clebsch cubic and its
     pentahedron.
6. **The double octic** [measured]: (−1|p)S = 6p² − 19p − a(p), at every prime from 7 to 401
   ([`fifth_moments_collect.log`](fifth_moments_collect.log)). It held blind at every prime from 409 to 601 in round
   17, in exact arithmetic ([`fifth_moments_test.log`](fifth_moments_test.log)). With Step 5 this is Theorem 7. ∎
   given Step 6.
- Step 6 is the modularity of one threefold. Its count behaves like a rigid Calabi–Yau's: one non-CM form of weight
  4, with Sato–Tate statistics (the remainder's mean square is 0.99 and its kurtosis 2.1). Rigid Calabi–Yau threefolds
  over Q are modular [NAMED: Gouvêa and Yui 2011; Dieulefait and Manoharmayum 2003]. A proof here would still need
  rigidity, and a finite check by the Faltings–Serre method.

**Every odd I_n and even J_n is one count on the wheel.** Steps 2 to 4 work for any n:

  I_n = (p + 1)(p·N_V⁽ⁿ⁾ − (pⁿ + 1)/(p + 1)) for odd n,   J_n = pⁿ − 1 − p(p + 1)·N_V⁽ⁿ⁾ for even n,

where N_V⁽ⁿ⁾ counts the points g1, …, gn of the turning wheel, none equal to −1, with g1⋯gn = (−1)^(n+1) and
Σ(g_i − 1)/(g_i + 1) = 0: the points that multiply to ±1 and whose Cayley coordinates sum to 0.
- n = 3 gives N_V = 3p − 2, and §6's I3 again.
- n = 4 reduces J4 to a surface count: N_V⁽⁴⁾ = (p − 1)(p − 3) + 4b² [measured, by brute force to 29 and from round
  16's J4 to 401]. Pairing the four points two by two makes it one character sum [FORCED]. Put δ1 + δ2 = σ, and let
  A = 1 + εδ1δ2 and B = 1 + εδ3δ4, so the condition reads AB = εσ². Legendre sums then give
  N_V⁽⁴⁾ = (p − 1)² + 2 + (−1|p)p − T(p), where T(p) = Σ_(κ≠0) Σ_A η(κA(κ + 4 − 4A)((κ + 4)A − 4κ)) is the sum of an
  elliptic surface. So all that is open in Theorem 5 is one evaluation, T(p) = (2 + (−1|p))p − 4b², exact at every
  prime to 401 [measured]. The surface's middle cohomology should carry η(4τ)⁶.
- n = 5 is the double octic.
- n = 6 makes J6 a count on a fourfold, an integer at every prime to 401. A first look finds the Gaussian integers' CM
  form η(4τ)⁶ in it again, with more left over.

**What it says.**
- The moments of the oscillator states' Wigner values are point counts, and modular forms appear in them. From the
  sixth moment on there is a non-CM form of weight 4. It is the form of the Barth–Nieto quintic and of Kloosterman's
  sixth moment, and it also turns up in Feynman integrals (Broadhurst 2016). The parity-weighted fourth moment carries
  the Gaussian integers' CM form.
- The fifth moments carry three forms. J5 has an elliptic curve of conductor 150 and the CM form of level 15 that rules
  Kloosterman's fifth moment. I5 has the weight-4 form of level 10, through a double octic built from Clebsch's
  diagonal cubic, a surface known since 1871.
- The free picture holds at the fifth moment. In §7's normalization, I5/((p − 1)p(p + 1)^(5/2)), √p times the fifth
  moment tends to 5. That is what the free cumulants κ1 ≈ 1/√p and κ3 ≈ −1/√p give with no fifth cumulant (10κ1 + 5κ3).
  The level-10 form enters one order later, at 1/p.
- [READING] The author's "how primes form direction" appears here twice: in the Sato–Tate angles of b(p), and in the
  angle of the Gaussian prime a + bi, which tunes κ4's correction.
- The neighbourhood of these results, and who works there, is in [`LITERATURE_MAP.md`](LITERATURE_MAP.md).

## 9. Standing

- **Known, and credited** [NAMED]: the Weil representation and its covariance (Weil 1964); the multiplicity-free action
  of a torus, and the oscillator states (Gurevich, Hadani and Sochen 2008); the algebra of phase-point operators
  (Wootters 1987; Gross 2006); conics over finite fields and the Legendre-symbol sums (Lidl and Niederreiter); the
  Hecke eigenstates of the quantum cat map (Kurlberg and Rudnick 2000), and the moments of their matrix elements for
  smooth observables: the second and fourth (Kurlberg and Rudnick 2005) and the fifth (Rosenzweig 2009); free
  probability's central limit theorem (Voiculescu) and the q-Gaussians (Bożejko and Speicher 1991); equidistribution of
  Fourier transforms on commutative algebraic groups (Forey, Fresán and Kowalski 2021).
- **This repository's own, new as far as we checked:** the two theorems, the exact average fourth moment (§2) and third
  moment with its parity split (§6) of the oscillator states' Wigner values, with these proofs, and the exact skew laws
  they give. Web searches on 2026-11-14 found the nearest work in Kurlberg and Rudnick's and Rosenzweig's papers;
  none computes a third moment of the Wigner function. Also new as far as we checked: the reduction of every moment
  to polygon counts, with the split into non-crossing, crossing and generic polygons (§7), and round 15's
  measurements. Web searches on 2026-11-14 found no treatment of the phase-point operators as free variables. And
  the exact sixth moment and fourth free cumulant (§8), with the modular forms in them, and the elementary count of the
  phase-0 hexagons that completes Theorem 4. And the fifth moments (§8, Theorems 6 and 7): the curve of conductor 150
  in J5; the reduction of every odd I_n and even J_n to one count on the wheel, by Gauss sums of Hermitian forms; and
  the double octic over Clebsch's cubic and its pentahedron, whose count carries the weight-4 form of level 10.
  - Web searches on 2026-11-14 found no double octic built this way. The nearest are Meyer's computer search of
    S4-symmetric double octics (arXiv:1810.03659), whose tables were not checked for this one, and Schütt's rigid
    Calabi–Yau threefold of level 10, built another way (arXiv:math/0311106).
  - OpenAI's catalogue of 721 AI-written manuscripts (github.com/openai/math) has nothing on these topics.
- **Checked** by [`verify_torus_moments.py`](verify_torus_moments.py), whose output is in
  [`verify_torus_moments.log`](verify_torus_moments.log). For §3: steps 1, 2, 3 and 6 with the operators themselves at
  every prime up to 31, and steps 4, 5 and the theorem by counting at every prime up to 101. For §6: the operator steps
  at every prime up to 31; the zero-area count, the Cayley formula, the triangle sums, the hexagons and both
  identities at every prime up to 101; and the off-origin skew against all 77 of round 12's logged values. For §7:
  [`free_moments.py`](free_moments.py)'s calibrate step (the phase formula, one circle's counts against the states,
  the pairings) at the primes it names. For §8: [`exact_moments.py`](exact_moments.py), its blind test at 211 to 401
  and its check against the states at 503 to 1009 ([`exact_moments_test.log`](exact_moments_test.log)); and
  [`verify_sixth_moment.py`](verify_sixth_moment.py), each step of Theorem 4's proof
  ([`verify_sixth_moment.log`](verify_sixth_moment.log)). And [`verify_fifth_moment.py`](verify_fifth_moment.py),
  each step of Theorems 6 and 7 ([`verify_fifth_moment.log`](verify_fifth_moment.log)), with round 17's blind test
  at 409 to 601 ([`fifth_moments_test.log`](fifth_moments_test.log)).
- **Measured, not proved:** the moments above the fourth and the whole distribution (§5 and §7;
  [`torus_moments_run.log`](torus_moments_run.log), [`torus_moments_combined.log`](torus_moments_combined.log),
  [`free_moments_run.log`](free_moments_run.log)), including the generic hexagons' 1/p and the free counts of the
  odd moments. Also, from §8: J4's surface count, the double octic's count behind I5, and E's conductor. Each is
  exact at every prime to 401 (the octic and E to 601), but none is proved.

## Run it

```
python verify_torus_moments.py     # both proofs, step by step: about twenty seconds (numpy)
python torus_moments.py calibrate  # round 12: seconds
python torus_moments.py run        # about eleven minutes, one process
python torus_moments.py combine
python free_moments.py calibrate   # round 15's forced checks: seconds
python free_moments.py run         # round 15: about nine minutes, one process
python exact_moments.py collect    # round 16: the integers at 5..199, seconds
python exact_moments_fit.py        # the exact fits that found Theorems 4 and 5 (sympy), a minute
python exact_moments.py test       # round 16's blind test at 211..401 and the states at 503..1009, minutes
python verify_sixth_moment.py      # Theorem 4's proof, step by step: seconds
python modular_symbols.py          # the engine that names the forms, against four eta products: seconds
python fifth_moments.py collect    # the double octic's sums at 7..401: a minute
python verify_fifth_moment.py      # Theorems 6 and 7, step by step: under a minute
python fifth_moments.py test       # round 17's blind test at 409..601: minutes, four processes
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
- C. Peters, J. Top and M. van der Vlugt, "The Hasse zeta function of a K3 surface related to the number of words of
  weight 5 in the Melas codes", *J. reine angew. Math.* **432** (1992): the fifth moment of Kloosterman sums.
- K. Hulek, J. Spandaw, B. van Geemen and D. van Straten, "The modularity of the Barth–Nieto quintic and its
  relatives", *Adv. Geom.* **1** (2001): the sixth moment of Kloosterman sums and the newform of weight 4, level 6.
- D. Broadhurst, "Feynman integrals, L-series and Kloosterman moments" (2016),
  [arXiv:1604.03057](https://arxiv.org/abs/1604.03057).
- J. Fresán, C. Sabbah and J.-D. Yu, "Hodge theory of Kloosterman connections", *Duke Math. J.* **171** (2022),
  [arXiv:1810.06454](https://arxiv.org/abs/1810.06454).
- D. V. Voiculescu, K. J. Dykema and A. Nica, *Free Random Variables*, CRM Monograph Series 1, Amer. Math. Soc.
  (1992): the free central limit theorem.
- M. Bożejko and R. Speicher, "An example of a generalized Brownian motion", *Comm. Math. Phys.* **137** (1991):
  the q-Gaussians.
- A. Forey, J. Fresán and E. Kowalski, "Arithmetic Fourier transforms over finite fields: generic vanishing,
  convolution, and equidistribution" (2021), [arXiv:2109.11961](https://arxiv.org/abs/2109.11961).
- W. K. Wootters, "A Wigner-function formulation of finite-state quantum mechanics", *Ann. Phys.* **176** (1987);
  D. Gross, "Hudson's theorem for finite-dimensional quantum systems", *J. Math. Phys.* **47** (2006).
- R. Lidl and H. Niederreiter, *Finite Fields* (1983): quadratic forms over finite fields and the sums of the Legendre
  symbol.
- A. Clebsch, "Ueber die Anwendung der quadratischen Substitution auf die Gleichungen 5ten Grades und die
  geometrische Theorie des ebenen Fünfseits", *Math. Ann.* **4** (1871): the diagonal cubic surface.
- S. Cynk and T. Szemberg, "Double covers of P³ and Calabi–Yau varieties" (1999),
  [arXiv:math/9902057](https://arxiv.org/abs/math/9902057): double octics.
- C. Meyer, *Modular Calabi–Yau Threefolds*, Fields Institute Monographs **22** (2005); "Modularity experiments on
  S4-symmetric double octics", [arXiv:1810.03659](https://arxiv.org/abs/1810.03659).
- M. Schütt, "New examples of modular rigid Calabi–Yau threefolds" (2003),
  [arXiv:math/0311106](https://arxiv.org/abs/math/0311106): among them one of level 10.
- F. Gouvêa and N. Yui, "Rigid Calabi–Yau threefolds over Q are modular", *Expo. Math.* **29** (2011); L. Dieulefait
  and J. Manoharmayum, "Modularity of rigid Calabi–Yau threefolds over Q" (2003).
- L. Merel, "Universal Fourier expansions of modular forms", *On Artin's Conjecture for Odd 2-dimensional
  Representations*, LNM **1585** (1994): the Heilbronn matrices; W. Stein, *Modular Forms: A Computational Approach*,
  AMS (2007): modular symbols.
