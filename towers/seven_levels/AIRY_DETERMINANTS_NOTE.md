# The determinant of the Galois representations attached to the Airy moments

*A note by Brayden Ross Sanders (Hot Springs, Arkansas), November 2026. The computations and the proof sketch
were made with AI assistance, and no one but the author has reviewed them. Corrections are welcome.*

## 1. Setting

For a prime p let S(a) = Σ_{x ∈ F_p} e((x³ + ax)/p). Its moments Σ_a S(a)^n are governed by the symmetric powers
of the rank-2 Airy sheaf. Sabbah and Yu computed the Hodge numbers of the corresponding motives [SY], and Haessig
studied their L-functions [H].

For odd n ≥ 5 we use a concrete model:

  X_n = { x_1 + ⋯ + x_n = 0,  x_1³ + ⋯ + x_n³ = 0 } ⊂ P^(n−1)_Q,

a smooth cubic hypersurface of dimension m = n − 3 (an even number) in the hyperplane W = {Σ x_i = 0}. The
symmetric group S_n permutes the coordinates. Let V_n be the sign-isotypic part of H^m_prim(X_n ⊗ Q̄, Q_ℓ), and
ρ_n = V_n(m/2), its twist to weight 0.

- The cup product makes ρ_n orthogonal. Its dimension is ⌈n/6⌉ − [3 | n], its Hodge numbers are 0 or 1, and they
  agree with the classical part in [SY]. There is a middle Hodge class exactly when n ≡ 1 (mod 4).
- By orthogonality, #X_n(F_p) is a moment of S(a), and the n-th moment splits by ballot numbers into terms T_k(p),
  one for each odd k ≤ n. The Frobenius traces of V_n are the new terms, T_n(p)/p².
- Small cases: V_5 is the character (5/p) times a Tate twist. V_7(1) has the Frobenius traces a_p of the weight-3 CM
  newform 35.3.c.b (LMFDB) at every prime we counted, up to 601.

## 2. The statement

**Claim.** For odd n, det ρ_n is the quadratic character

  p ↦ (p / A_n)  (Jacobi symbol),   A_n = ∏_{j odd, j ≤ n} j / 3^[3 | j],

that is, n!! with one factor of 3 removed from each multiple of 3.

Equivalently, det ρ_n = (D_n / ·), where D_n is the product of l* = (−1)^((l−1)/2) l over the primes l for which
N_l(n) is odd. For l ≥ 5, N_l(n) = #{odd j ≤ n : v_l(j) odd}; for l = 3, N_3(n) = #{odd j ≤ n : v_3(j) even and ≥ 2}.

| n | dim V_n | D_n |
|---|---|---|
| 5 | 1 | 5 |
| 7 | 2 | −35 |
| 9 | 1 | 105 |
| 11 | 2 | −1155 |
| 13 | 3 | −15015 |
| 15 | 2 | −3003 |
| 17 | 3 | −51051 |
| 19 | 4 | 969969 |
| 21 | 3 | −138567 |
| 23, 25 | 4, 5 | 3187041 |
| 27 | 4 | 3187041 |
| 29 | 5 | 92424189 |
| 31 | 6 | −2865149859 |
| 33 | 5 | 260468169 |
| 35 | 6 | −9116385915 |
| 39 | 6 | −25946636835 |

For the moments of the Kloosterman sums, Yun proved that the determinant is (· / d!!) for odd d [Y, Theorem 1.2.3].
The claim has the same shape, with one factor of 3 removed from each multiple of 3.

## 3. Evidence

- **Read from point counts.** For n ≤ 27 the determinants were read from exact counts of X_n over F_p, F_{p²} and
  F_{p³}, at every prime tested.
- **Predicted, then checked.** For n = 29, 31, 33, 35 and 39 the five determinants in the table were written down
  before any count. They then held at all 24 primes from 41 to 151.
- **The alternative fails.** At n = 29, 31 and 39, where (p / n!!) differs from (p / A_n), it agrees with the counts
  at only 11 of the 24 primes.

## 4. Proof sketch

1. **V_n is the sign part.** On W the Jacobian ring is R = Q[x]/(e_1, x_i² − x_j²). It has no sign-isotypic part,
   and its invariant part is Q[t]/(t^((n+1)/2)), where t = x_i². Griffiths' residue map carries R onto the Hodge
   pieces of H^m_prim. The volume form on W is anti-invariant, so it carries R^(S_n) onto the sign part. The degrees
   that occur reproduce the classical Hodge types of [SY]. Twisted point counts confirm the trace identification
   directly for n = 5 and 7.
2. **Good reduction at 2 and at l > n.** A singular point mod l needs every x_i² equal, so it is a multiple of a sign
   vector ε, and it lies on X_n only if Σ ε_i ≡ 0 mod l. Since n is odd, Σ ε_i is odd and never 0 mod 2, and
   |Σ ε_i| ≤ n.
3. **Nodes at l ≥ 5.** The singular points mod l are the sign vectors ε with l | j = Σ ε_i. Each is an ordinary
   double point: the Hessian Σ ε_i y_i² has radical ⟨ε⟩ on W. The critical value over Q is j(j − 2)/(j − 1)², of
   l-adic valuation v_l(j).
4. **The prime 3.** On e_1 = 0 one has Σ x_i³ = 3e_3, so {e_1 = e_3 = 0} is a proper flat model over Z_(3). For a
   sign vector with sum j = 3m, e_3 ≡ m mod 3, so the singular points mod 3 are the sign vectors with 9 | j. They are
   ordinary double points, with critical value j(j − 2)/(3(j − 1)²), of 3-adic valuation v_3(j) − 1.
5. **Picard–Lefschetz** [SGA 7, Exp. XV]. In even relative dimension, inertia acts on the vanishing cycle δ_x of a
   node with local equation Q = c_x by χ^(v(c_x)), with χ the quadratic character of tame inertia. It acts trivially
   on the orthogonal complement of the vanishing cycles, which are mutually orthogonal with (δ_x, δ_x) = ±2.
6. **One sign-isotypic vanishing class per orbit.** The nodes with sum ±j form one S_n-orbit, with stabilizer
   S_a × S_b. A transposition in the stabilizer acts on W/⟨ε⟩ with determinant −1, so the stabilizer acts on δ_x by
   the sign character. By Frobenius reciprocity the orbit contributes exactly one line to the sign part.
7. **Assembly.** So det ρ_n restricted to inertia at l is χ^(N_l(n)). The determinant is unramified at 2 and at
   l > n, so its discriminant is odd and ≡ 1 mod 4, which forces D_n = ∏ l*. Finally N_l(n) ≡ v_l(A_n) mod 2 for every
   l, so (D_n / p) = (p / A_n) by quadratic reciprocity.

**Corollary.** Complex conjugation acts on each Hodge pair with determinant −1. The sign of D_n equals (−1) to the
number of Hodge pairs for every n, since both change exactly at n ≡ 7, 9, 11 (mod 12). So complex conjugation acts
by +1 on the middle Hodge class of ρ_n for every n ≡ 1 (mod 4).

## 5. What is known, and what may be new

- **Known.**
  - Picard–Lefschetz in mixed characteristic [SGA 7].
  - Griffiths' residues.
  - The Hodge numbers of the Airy moments [SY], and their L-functions [H].
  - Yun's determinant for the Kloosterman moments [Y].
  - Chuang's thesis [C, Theorems 4.21–4.22] gives the local Galois representation of the Airy motive at every
    p ≥ 5, in another model. The local input of Steps 3 and 5 at l ≥ 5 is contained in it.
- **Not found in the literature we could read.**
  - The global determinant.
  - The prime 3 through the model e_1 = e_3 = 0.
  - The corollary on complex conjugation.
- **The step least checked.** Step 1's identification of V_n with the new part of the n-th moment. It is confirmed
  directly at n = 5 and 7, and it is consistent with every determinant read through n = 39.

## References

- [C] P.-H. Chuang, *On the generalized arithmetic Picard–Lefschetz formula*, dissertation (2026),
  [arXiv:2607.05757](https://arxiv.org/abs/2607.05757).
- [H] C. D. Haessig, *L-functions of symmetric powers of cubic exponential sums*, J. reine angew. Math. **631**
  (2009), [arXiv:math/0608521](https://arxiv.org/abs/math/0608521).
- [SGA 7] P. Deligne, *La formule de Picard–Lefschetz*, Exposé XV, SGA 7 II, LNM 340 (1973).
- [SY] C. Sabbah and J.-D. Yu, *Hodge properties of Airy moments*, Tunisian J. Math. **5** (2023),
  [arXiv:2112.13405](https://arxiv.org/abs/2112.13405).
- [Y] Z. Yun, *Galois representations attached to moments of Kloosterman sums and conjectures of Evans*, Compositio
  Math. **151** (2015), 68–120, [arXiv:1308.3920](https://arxiv.org/abs/1308.3920).

**Code.** [`verify_determinants.py`](verify_determinants.py) checks each computable step of §4, and
[`edge_rule.py`](edge_rule.py) `test28` reruns the test of §3. The longer working page, with the history of the
measurements, is [`DETERMINANTS.md`](DETERMINANTS.md).
