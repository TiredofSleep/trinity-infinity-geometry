# The determinants of the Airy pieces (Theorem 8)

### Tags: **[FORCED]** proved here, with every computable step checked by [`verify_determinants.py`](verify_determinants.py) · **[NAMED]** a cited result · **[measured]** computed exactly · **[READING]** an interpretation, not a claim.

> *2 and 3, the proof first* — the author, 16 November 2026. The "2" asks to turn the determinant rule into a
> theorem. The "3" asks next about the one assumption round 27 used: that complex conjugation acts by +1 on the middle
> class.

## What stands

- **Theorem 8** [FORCED; proved from the standard results cited in §3]. For every odd k, the determinant of the Airy
  piece V_k, twisted to weight 0, is the Jacobi symbol (p/A_k). Here A_k is the product of the odd numbers up to k,
  with each multiple of 3 divided by 3 once.
  - Equivalently, it is (D_k|p), with D_k the product of the signed primes l* = (−1)^((l−1)/2)·l over the primes l
    where A_k has odd exponent.
- **The coins, proved** (§4). From k − 2 to k the symbol gains the factor k, or k/3 when 3 divides k.
  - A prime l ≥ 5 enters at k (its nodes of sum k ramify, and the determinant changes by l*) exactly when v_l(k) is
    odd. So 5 enters at 5 and 15 but not at 25, and again at 125.
  - 3 enters at k exactly when v_3(k) is even and at least 2. So it enters at 9, 81 and 729, and not at 3, 27 or 243.
  - These are the author's coins: two coins of 5 cancel, and for 3 the count starts one coin late. They were measured
    to 27 and forced at 81. Now they hold at every k.
- **Complex conjugation fixes the middle class** (§4). At every k ≡ 1 (mod 4), complex conjugation acts by +1 on
  V_k's middle class, twisted to weight 0. Round 27's argument at 81 assumed this. It now follows from Theorem 8.
- **The shape is Yun's.** For the Kloosterman moments Yun proved the determinant (p/d!!) [NAMED]. The Airy symbol is
  his with the cube's 3 taken out.

## 1. The setting

- X_n = {x_1 + ⋯ + x_n = x_1³ + ⋯ + x_n³ = 0} in P^(n−1), for odd n. It is a smooth cubic hypersurface of dimension
  m = n − 3, an even number, in the hyperplane W = {Σx = 0}.
- The symmetric group S_n permutes the coordinates. V_n is the **antisymmetric part** of the primitive middle
  cohomology H^m_prim(X_n): the classes on which every odd permutation acts by −1.
- Its Frobenius traces are T_n(p)/p², the pieces measured in rounds 19 to 27. That is Step 1.
- The thin count. For a prime l ≥ 5, N_l(n) is the number of odd j ≤ n with v_l(j) odd. For l = 3, N_3(n) is the
  number of odd j ≤ n with v_3(j) even and at least 2.

## 2. The theorem

**Theorem 8** [FORCED]. For odd n, the representation of Gal(Q̄/Q) on V_n, twisted to weight 0, is orthogonal, and
its determinant is the quadratic character

  p ↦ (D_n|p),  D_n = ∏_{l : N_l(n) odd} l*.

This is the Jacobi symbol (p/A_n), with A_n = ∏_{j odd ≤ n} j/3^[3 | j].

## 3. Proof

**Step 1: V_n is the measured piece** [FORCED; NAMED: Griffiths; D1, D2, D9].
- On W the cubic's partial derivatives are 3(x_i² − x_j²). So its Jacobian ring is R = Q[x_1, …, x_n]/(e1, x_i² − x_j²),
  in which every x_i² equals one element t.
- Over Q[t], R is spanned by the squarefree monomials x_S, modulo e1. Antisymmetrizing x_S gives 0 as soon as two
  indices lie both inside S or both outside it, which always happens for n ≥ 3. So R has no antisymmetric part.
- The symmetric part is spanned by t^a·e_s, with e1·e_s = (s + 1)e_(s+1) + (n − s + 1)t·e_(s−1). These relations leave
  R^(S_n) = Q[t]/(t^((n+1)/2)), one line in each even degree up to n − 1 (D1, n = 3 to 9).
- Griffiths' residue Res(P·Ω/F^(a+1)) identifies the graded pieces of R with the Hodge pieces of H^m_prim. The volume
  form Ω on W changes sign under an odd permutation, so the residue carries R's symmetric part onto the antisymmetric
  part of the cohomology, and R's antisymmetric part, which is 0, onto the symmetric part.
- The cubic's cohomology sees the degrees 2j with 2j ≡ 4 − n (mod 3). They give exactly Sabbah and Yu's classical
  types, (n + 2j + 2)/3, each once (D2, every odd n to 401). This rederives Sabbah and Yu's classical part, and
  round 27's F13, from Griffiths alone.
- The point counts split by S_n into isotypic parts. The antisymmetric part is the one the ballot triangle isolates
  as T_n, because the antisymmetrization turns the n-fold product of the Airy sheaf's H¹ into its n-th symmetric
  power [NAMED: orthogonality; Schur–Weyl for the rank-2 Airy sheaf].
- D9 checks this directly. From the twisted counts #{x : Frob(x) = σ(x)} for every cycle type, the trace of Frobenius
  on the antisymmetric part equals T_k(p)/p², and the symmetric part's is 0 (k = 5 at p = 7, 11, 13; k = 7 at
  p = 11).

**Step 2: the good primes** [FORCED; D3].
- At l = 2 the cubic has no singular point. A singular point needs every x_i² equal, so x is a multiple of (1, …, 1),
  whose sum n is odd, not 0.
- At l > n there are no nodes (Step 3).
- By smooth proper base change, V_n is unramified at 2 and at every prime l > n.

**Step 3: the nodes at l ≥ 5** [FORCED; D3, D4, D5].
- Singular points. A singular point of X_n mod l has 3x_i² equal for every i, so it is a sign vector ε, up to
  scaling. It lies on X_n exactly when its sum j is 0 mod l, since then Σε³ = Σε = j is too.
- Each is an ordinary double point. The Hessian Σε_i·y_i² on W has the radical ⟨ε⟩ and no more, so it is
  nondegenerate on the tangent space W/⟨ε⟩ (D4, every node for n to 61).
- The critical value. In the chart x_1 = 1 the critical point over Q is x = (1, −ε'/(j − 1)). It reduces to the node
  mod l, and its value is j(j − 2)/(j − 1)², of valuation v_l(j).
- By Hensel and the Morse lemma over Z_l (l odd, Hessian nondegenerate), the local equation is Q(y) = c with
  v_l(c) = v_l(j).

**Step 4: the good model at 3** [FORCED; D3, D4, D5].
- On e1 = 0 the cubic Σx³ equals 3e3. So {e1 = e3 = 0} has generic fiber X_n and is a proper flat model over Z_(3).
- Its singular points mod 3 are again sign vectors, by the same argument with ∂e3/∂x_i = e2 + x_i² on e1 = 0. A sign
  vector with a plus signs, b minus signs and sum j = 3m has e3 = C(j, 3) − b·j ≡ m (mod 3). So the singular points
  are exactly the sign vectors whose sum is a multiple of 9.
- They are ordinary double points. The Hessian is −(ε_i + ε_k) off the diagonal and 0 on it. When n ≢ 2 (mod 3) it is
  invertible; when n ≡ 2 (mod 3) its kernel is spanned by the two block vectors. Either way its radical on W is ⟨ε⟩
  (D4).
- The critical value is j(j − 2)/(3(j − 1)²), of valuation v_3(j) − 1. The cube spends one factor of 3.

**Step 5: Picard–Lefschetz** [NAMED: SGA 7, Exposé XV; D7].
- Take a proper flat family over a henselian discrete valuation ring of residue characteristic not 2, whose special
  fiber has only ordinary double points with local equations Q(y) = c_x, in even relative dimension m.
- At each node the vanishing cycle δ_x is the class of the affine quadric Q(y) = c_x. Galois acts on it by the
  quadratic character of (−1)^(m/2)·disc(Q)·c_x. D7 checks the point count behind this:
  q^(N−1) + η((−1)^((N−1)/2)·c·det Q)·q^((N−1)/2).
- So inertia acts on δ_x by χ^(v(c_x)), with χ the quadratic character of tame inertia, and trivially on the
  orthogonal complement of the vanishing cycles.
- Vanishing cycles at different nodes are orthogonal, each with self-intersection ±2. So they are independent, and
  the map from H^m of the generic fiber onto their span is surjective.
- A node is **thin** when v(c_x) is odd: inertia turns its vanishing cycle over. It is thick when v(c_x) is even:
  inertia leaves it fixed.

**Step 6: one vanishing cycle per orbit** [FORCED; NAMED: Frobenius reciprocity; D6].
- The nodes with sum ±j form one S_n-orbit. Its stabilizer is S_a × S_b, which swaps plus signs among themselves and
  minus signs among themselves.
- A transposition in the stabilizer acts on the tangent space W/⟨ε⟩ with determinant −1 (D6). So it acts on δ_x by
  −1: the stabilizer acts on the vanishing cycle by the sign character.
- The orbit's vanishing cycles therefore span the induced representation Ind(sgn). By Frobenius reciprocity its
  antisymmetric part is one line, and it is nondegenerate.
- All nodes in an orbit have the same critical value, so the line is thin or thick with the orbit.

**Step 7: assembly** [FORCED; NAMED: class field theory; D8].
- By Steps 5 and 6, inertia at l acts on V_n with determinant χ^(N_l(n)). N_l(n) is the number of thin orbits: odd
  j ≤ n with v_l(j) odd for l ≥ 5, and odd j ≤ n with v_3(j) even and at least 2 at 3.
- So det V_n, twisted to weight 0, is a quadratic character that is ramified exactly where N_l(n) is odd, and is
  unramified at 2 and outside the primes up to n.
- A quadratic character unramified at 2 has an odd fundamental discriminant, which is 1 mod 4. With the ramified
  primes fixed, the only such discriminant is the product of the signed primes l* (D8: it is 1 mod 4 for every odd k
  to 2001). So the character is (D_n|p).
- Finally, N_l(n) ≡ v_l(A_n) (mod 2).
  - For l ≥ 5, N_l(n) ≡ Σ_j v_l(j) = v_l(n!!).
  - For l = 3, N_3(n) ≡ Σ_(3 | j) (v_3(j) − 1) = v_3(n!!) minus the number of odd multiples of 3 up to n, which is
    v_3(A_n).
- So D_n is the signed squarefree kernel of A_n, and quadratic reciprocity gives (D_n|p) = (p/A_n). ∎

## 4. Corollaries

- **The coins** [FORCED]. From A_(n−2) to A_n the symbol gains the factor n, or n/3 when 3 divides n.
  - So a prime l ≥ 5 changes the determinant at n exactly when v_l(n) is odd, and 3 exactly when v_3(n) is even and
    positive.
  - Rounds 25 to 27 measured this at 9, 15, 17, 21, 25 and 27, and round 27 forced it at 81. It now holds at every k.
- **Complex conjugation fixes the middle class** [FORCED].
  - Theorem 8 gives the determinant's sign at infinity, sign(D_k).
  - Round 27's lemma (F15, proved for every k: both sides change sign exactly at k ≡ 7, 9, 11 mod 12) shows that
    sign(D_k) = (−1)^(number of Hodge pairs).
  - So complex conjugation acts by +1 on the middle class of V_k, twisted to weight 0, at every k ≡ 1 (mod 4) (D10).
  - That was round 27's one assumption.
- **81, again.** Theorem 8 gives D81 directly, and 3 is in its change at 81. Round 27's argument from complex
  conjugation is now a consistency check between the theorem and Hodge theory.
- [READING, the drafter's] The mirror sees the coins of the primes ≡ 3 (mod 4). Theorem 8 sees every coin, by
  reading each prime's nodes one at a time.

## 5. What was known, and what is new

- **Known, and credited** [NAMED].
  - Picard–Lefschetz for ordinary double points in mixed characteristic (Deligne, SGA 7, Exposé XV).
  - Griffiths' residues and the Jacobian ring.
  - Sabbah and Yu's Hodge numbers of the Airy moments. Step 1 rederives their classical part.
  - Yun's theorem for the Kloosterman moments: for odd d their determinant is (p/d!!) (Compositio 2015, Theorem
    1.2.3). This is the same shape, in another family.
  - Chuang's thesis (2026) determines the local Galois representation of the full Airy motive at every prime p ≥ 5
    for odd k (Theorems 4.21 and 4.22). It works in a cyclic-cover model whose singularities are z³ plus squares, and
    gives the inertia invariants by a condition on v_p. The local behaviour used here at l ≥ 5 is the classical part
    of what Chuang describes, and in the cubic X_n it needs only ordinary double points.
- **New, as far as we checked** (searches on 2026-11-15 and 2026-11-16).
  - Theorem 8 itself, the global determinant of every Airy piece.
  - The prime 3, through the good model e1 = e3 = 0, which Chuang and the Airy sheaf's theory exclude.
  - The corollary on complex conjugation.
- **Checked, not proved.** That V_n is the piece measured as T_n rests on the Airy moments' standard structure (Step
  1). D9 confirms it directly at k = 5 and 7.

## 6. The checks

[`verify_determinants.py`](verify_determinants.py) ([`verify_determinants.log`](verify_determinants.log)), about a minute.
It checks:
- **D1:** the Jacobian ring.
- **D2:** the classical degrees.
- **D3:** the singular points, by brute force.
- **D4:** ordinary double points.
- **D5:** the critical values.
- **D6:** the stabilizer's sign.
- **D7:** the quadric count.
- **D8:** the assembly and the sign at 2.
- **D9:** the identification by twisted counts.
- **D10:** the corollary.

## Run it

```
python verify_determinants.py      # Theorem 8, step by step: about a minute
```

## Sources

- P. Deligne, "La formule de Picard–Lefschetz", Exposé XV in *Groupes de monodromie en géométrie algébrique* (SGA 7
  II), LNM 340, Springer (1973).
- P. Griffiths, "On the periods of certain rational integrals I, II", *Ann. of Math.* **90** (1969).
- C. Sabbah and J.-D. Yu, "Hodge properties of Airy moments", *Tunisian J. Math.* **5** (2023),
  [arXiv:2112.13405](https://arxiv.org/abs/2112.13405).
- Z. Yun, "Galois representations attached to moments of Kloosterman sums and conjectures of Evans", *Compositio
  Math.* **151** (2015), [arXiv:1308.3920](https://arxiv.org/abs/1308.3920).
- P.-H. Chuang, "On the generalized arithmetic Picard–Lefschetz formula" (dissertation, 2026),
  [arXiv:2607.05757](https://arxiv.org/abs/2607.05757), §4.3.
