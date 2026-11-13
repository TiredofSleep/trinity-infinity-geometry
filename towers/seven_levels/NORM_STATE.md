# The norm state on three wheels

> *you are only spinning one wheel... imagine a 10x10 of wheels or larger?* — the author, 9 November 2026

### Tags: **[FORCED]** proved here and checked by [`verify_norm_state.py`](verify_norm_state.py) · **[NAMED]** a cited standard result · **[READING]** an interpretation · **[measured]** a search result.

Round 9 found that on three wheels of 3 levels, the most negative state found is the norm state of the field with 27
elements, and that it sits on neither face of the coin ([README](README.md) §11). Round 10 took it to three wheels of
every prime (§12). This page proves the exact part:
- on three wheels of every odd prime p, the norm state is flat (Theorem 1);
- its Wigner function is made of Kloosterman sums (Theorem 2), so its negativity is known in closed form at every p.

Whether it is the most negative state is a different question, and only searches speak to it: yes as far as found on
three wheels of 3 and of 7, no on three wheels of 5.

## 1. The setting

- p is an odd prime, q = p³, and F is the field with q elements, written as F_p[t]/(f) for an irreducible cubic f.
  The element x = x₀ + x₁t + x₂t² is the basis state |x₀ x₁ x₂⟩ of three wheels of p levels.
- N(x) = x^(1 + p + p²) is the field's norm and Tr(x) = x + x^p + x^(p²) its trace. Both lie in F_p. ω = e^(2πi/p).
- The norm-type states: ψ_c = Σ_x ω^(c·N(x)) |x⟩ / √q, for c = 1, …, p − 1. ψ₋c is the complex conjugate of ψ_c.
- The Wigner function, as round 3 defines it on wheels: W(u, k) = (1/q) Σ_s ψ̄(u + s) ψ(u − s) ω^(2k·s), at the q²
  points (u, k), where k·s is the dot product of coordinates.
  - The trace form is nondegenerate, so there is a linear bijection k → κ of F with k·s = Tr(κs) for every s.
    Relabelling the momenta by κ moves the values without changing them. Below, W(u, κ) uses Tr(κs).
- The Kloosterman sum: K(m) = Σ_a ω^(a + m/a), over the nonzero a in F_p. It is real, |K(m)| ≤ 2√p (Weil), and the
  p − 1 sums for nonzero m add up to 1 [NAMED].

## 2. The two theorems

**Theorem 1 (flat)** [FORCED; registered before round 10's run, [`PREREG.md`](PREREG.md)]. For every c:
- ⟨ψ_c| Z^b X^a |ψ_c⟩ = 0 for a = 0 and b ≠ 0, and |⟨ψ_c| Z^b X^a |ψ_c⟩| = 1/√q for every a ≠ 0;
- no phase-point operator has ψ_c as an eigenstate, so ψ_c is even or odd about no centre;
- the half turn sends ψ_c to its complex conjugate.

**Theorem 2 (the Wigner values)** [FORCED; derived during round 10's run]. For every c, the Wigner function of ψ_c
takes the value −(p + 1)/p⁵ at q points, and the value K(m)/p⁵ at (p² + p + 1)q points for each nonzero m in F_p.
These are all q² points, and the values do not depend on c.

**Corollary.** The sum of sizes is

  Σ|W| = [(p + 1) + (p² + p + 1) Σ_m |K(m)|] / p²,

and the negativity is (Σ|W| − 1)/2. Against the ceiling (√q − 1)/2:

| p | Kloosterman sums K(1), …, K(p − 1) | negativity | share of the ceiling |
|---|---|---|---|
| 3 | −1, 2 | 17/9 = 1.888889 | 0.9003 |
| 5 | 0.381966, −3.236068, 1.236068, 2.618034 | 4.252724 | 0.8355 |
| 7 | 2.048917, −2.356896, −1.603875, −2.692021, 4.493959, 1.109916 | 7.902228 | 0.9021 |
| 11 | | 14.900798 | 0.8399 |
| 13 | | 18.887726 | 0.8235 |
| 17 | | 30.679376 | 0.8881 |

## 3. Proof of Theorem 2

Write x′ = x^p and x″ = x^(p²), so N(x) = x x′ x″ and Tr(y) = y + y′ + y″.

**Step 1: the cubic, split.** Multiplying out,

  N(u + s) = (u + s)(u′ + s′)(u″ + s″) = N(u) + Tr(s u′u″) + Tr(u s′s″) + N(s).

Replacing s by −s changes the sign of the odd terms, so

  N(u − s) − N(u + s) = −2 Tr(s u′u″) − 2 N(s).

The quadratic term cancels, and what is left is a linear term and N(s) itself. This is where three wheels matter: with
n wheels the norm has degree n, and from n = 4 on the difference keeps a cubic term that involves u.

**Step 2: one sum per point.** By Step 1,

  W(u, κ) = q⁻² Σ_s ω^(Tr(ws) − 2c·N(s)) = S(w)/q²,   where w = 2κ − 2c u′u″.

For fixed u, κ → w is a bijection of F. So the q² values of W are q copies of the q values S(w)/q².

**Step 3: w = 0.** The norm maps the nonzero elements of F onto the nonzero elements of F_p, each value taken by
(q − 1)/(p − 1) = p² + p + 1 elements [NAMED]. So

  S(0) = 1 + (p² + p + 1) Σ_t ω^(−2ct) = 1 − (p² + p + 1) = −p(p + 1),

summing over the nonzero t in F_p. That gives W = −p(p + 1)/p⁶ = −(p + 1)/p⁵, at q points: one w = 0 for each u.

**Step 4: w ≠ 0.** Replace s by s/w. Then Tr(ws) becomes Tr(s), and N(s) becomes N(s)/N(w). So

  S(w) = T(2c/N(w)),   where T(μ) = Σ_s ω^(Tr(s) − μ·N(s)).

**Step 5: T through Gauss sums.** For each multiplicative character χ of F_p, let g(χ) = Σ_t χ(t) ω^t, over the
nonzero t (so g = −1 for the trivial character). Expanding t → ω^(−μt) in characters,

  ω^(−μt) = (1/(p − 1)) Σ_χ χ(−μ) g(χ̄) χ(t),

so

  T(μ) = 1 + (1/(p − 1)) Σ_χ χ(−μ) g(χ̄) G(χ∘N),   where G(χ∘N) = Σ_s χ(N(s)) ω^Tr(s), over the nonzero s in F.

Two standard facts finish the step [NAMED]:
- Davenport and Hasse: G(χ∘N) = g(χ)³. For the trivial character both sides are −1.
- For a nontrivial χ, g(χ) g(χ̄) = χ(−1) p.

So the trivial character contributes 1, and every other χ contributes p χ(μ) g(χ)²:

  T(μ) = 1 + (1/(p − 1)) [1 + p Σ_(χ ≠ 1) χ(μ) g(χ)²].

**Step 6: the Kloosterman sum.** g(χ)² = Σ_(a,b) χ(ab) ω^(a + b), and Σ_χ χ(μab) is p − 1 when ab = 1/μ and 0
otherwise. So

  Σ_χ χ(μ) g(χ)² = (p − 1) Σ_a ω^(a + 1/(μa)) = (p − 1) K(1/μ).

Taking out the trivial character's term, which is g² = 1,

  T(μ) = 1 + (1/(p − 1)) [1 + p((p − 1) K(1/μ) − 1)] = p K(1/μ).

**End of the proof.** For w ≠ 0, S(w) = T(2c/N(w)) = p K(m) with m = N(w)/(2c), so W = p K(m)/p⁶ = K(m)/p⁵. For each
u and each nonzero m, exactly p² + p + 1 values of w have N(w) = 2cm. So each K(m)/p⁵ sits at (p² + p + 1)q points. ∎

The bookkeeping closes: q + (p − 1)(p² + p + 1)q = q² points, and the values add up to 1, since
−p(p + 1) + p(p² + p + 1) Σ_m K(m) = p³.

## 4. Proof of Theorem 1

- **Flat.** ⟨ψ_c| Z^b X^a |ψ_c⟩ is (1/q) times a character sum of c(N(x) − N(x + a)) plus a linear term in x. For
  a = 0 it is (1/q) Σ_x ω^(b·x), which is 0 unless b = 0.
  - For a ≠ 0, Step 1 (with u = x, s = a) makes the part of N(x + a) − N(x) that is quadratic in x the form
    Q(x) = Tr(a x′x″) = Tr(a^(p²) x^(p+1)). Its polar form is Tr(y (a^(p²) x′ + a′ x″)).
  - That form is degenerate only if a^(p²) x′ = −a′ x″ for some x ≠ 0. With z = x/a this says (z^(p−1))^p = −1, and so
    z^(p−1) = −1. Then the order of z divides 2(p − 1) but not p − 1, while it divides q − 1 = (p − 1)(p² + p + 1).
    That is impossible, because p² + p + 1 is odd.
  - A nondegenerate quadratic form plus a linear term on F, a space of dimension 3 over F_p, has a character sum of
    size p^(3/2) = √q [NAMED]. So |⟨ψ_c| Z^b X^a |ψ_c⟩| = √q/q = 1/√q.
- **On neither face.** ψ_c is an eigenstate of the phase-point operator at (u, k) only if ψ_c(u + x)/ψ_c(u − x) is a
  linear phase in x, times the eigenvalue ±1. Setting x = 0 shows the eigenvalue is +1, so c(N(u + x) − N(u − x))
  would be linear in x. By Step 1 it is 2c Tr(x u′u″) + 2c N(x), so N would be linear. But a nonzero linear map from
  F to F_p vanishes on p² elements, and N vanishes only at 0.
- **The half turn.** N(−x) = (−1)³ N(x) = −N(x), so ψ_c(−x) is the complex conjugate of ψ_c(x).

## 5. What the numbers do as p grows

- Write K(m) = 2√p cos θ_m. As p grows, the p − 1 angles θ_m become equidistributed for the Sato–Tate measure
  (2/π) sin²θ dθ [NAMED: Katz 1988]. Under it, |2 cos θ| has mean 8/(3π).
- So Σ_m |K(m)| is about (8/(3π))(p − 1)√p, and the share of the ceiling tends to 8/(3π) = 0.8488. The mean over the
  primes from 1 000 to 2 000 is 0.8489 (computed from the corollary; [`flat_states.log`](flat_states.log)).
- Below 2 000 only 3 and 7 reach 90% of the ceiling, and 7 reaches the most, 0.9021 (computed the same way).
- The average random state tends to √(2/π) = 0.798 of the ceiling ([README](README.md) §11).

## 6. What it says about the coin [READING]

- The norm state sits on neither face at every prime. Its edge is a flip between two states, ψ_c and its conjugate,
  not a fixed point.
- How strong that edge is depends on the prime's Kloosterman sums, not on any symmetry. At 3 and 7 they are large and
  the norm state wins every search; at 5 they are small (0.38, −3.24, 1.24 and 2.62, against Weil's bound 4.47) and a
  state near it wins instead, still on neither face ([README](README.md) §12).

## 7. Standing

- **Known, and credited** [NAMED]: the norm and trace of a finite field, the fibres of the norm, Gauss sums and
  g(χ) g(χ̄) = χ(−1)p (Lidl and Niederreiter, chapter 5); Davenport and Hasse's theorem on lifted Gauss sums (1935);
  Kloosterman sums (1926) and Weil's bound (1948); Katz's equidistribution of Kloosterman angles (1988); quadratic
  character sums; the discrete Wigner function (Wootters 1987; Gross 2006); and flat states for every pⁿ as fiducials
  of product Weyl–Heisenberg mutually unbiased bases (Alltop 1980; Klappenecker and Rötteler 2004; Damski, Bistroń,
  Ponterio, Czartowski and Życzkowski 2026).
- **Close kin, found on 2026-11-12** [NAMED]. The mechanism is not new. States fixed by a torus in the symplectic group
  have Wigner functions given by Gauss and Kloosterman-type sums: Gurevich and Hadani worked this out for the Hecke
  eigenstates of the quantized cat map, with the bound 2/√p, and for tori in higher dimensions; Kurlberg and Rudnick
  found Sato–Tate statistics there. The norm state is such a state: multiplication by the p² + p + 1 elements of norm 1
  fixes it, and in the language of the field with q elements it is built from the multiplicative-character states,
  the eigenvectors of a split torus. And because a group of Clifford operations fixes it and no other state, it is a
  stationary point of every magic measure (Erew and Goldstein 2025); round 10's kicks found it a local maximum.
- **This repository's own, new as far as we checked:** Theorems 1 and 2 for the norm-form state, read as magic: the
  negativity is an L1 norm of Kloosterman sums, and its limit 8/(3π) is the Sato–Tate mean of |2 cos θ|. The magic of
  states fixed by Clifford subgroups has been computed for single qudits of 2, 3 and 5 levels (Erew and Goldstein;
  Jain and Prakash), without this structure. Searches on 2026-11-10 and 12 found no use of the Gauss and Kloosterman
  machinery to compute magic. If a specialist knows one, the credit moves.
- **Not proved:** that ψ_c is the most negative state on three wheels of 3 or of 7. That is a search result
  ([README](README.md) §11 and §12). On three wheels of 5 it is not the most negative state.
- **Checked** by [`verify_norm_state.py`](verify_norm_state.py), whose output is in
  [`verify_norm_state.log`](verify_norm_state.log):
  - the whole statement, from the state itself, at p = 3, 5, 7, 11 and 13 and every c: the Wigner function computed
    as round 10 computes it, its values and their counts, the negativity, and the flatness;
  - each step of the proof at every odd prime up to 101, from the joint counts of (Tr(s), N(s)): the norm's fibres,
    S(0) = −p(p + 1), Davenport and Hasse's lifting for every character, and T(μ) = p K(1/μ) for every μ.

  [`verify_seven_levels.py`](verify_seven_levels.py) checks Theorems 1 and 2 at 3, 5 and 7 as well.

## Run it

```
python verify_norm_state.py     # about a minute (numpy)
```

## Sources

- H. D. Kloosterman, "On the representation of numbers in the form ax² + by² + cz² + dt²", *Acta Math.* **49**
  (1926).
- H. Davenport and H. Hasse, "Die Nullstellen der Kongruenzzetafunktionen in gewissen zyklischen Fällen", *J. reine
  angew. Math.* **172** (1935).
- A. Weil, "On some exponential sums", *Proc. Natl. Acad. Sci.* **34** (1948).
- N. M. Katz, *Gauss Sums, Kloosterman Sums, and Monodromy Groups*, Annals of Mathematics Studies **116** (1988).
- R. Lidl and H. Niederreiter, *Finite Fields* (1983), chapter 5: Gauss sums, and character sums of quadratic forms.
- W. K. Wootters, "A Wigner-function formulation of finite-state quantum mechanics", *Ann. Phys.* **176** (1987);
  D. Gross, "Hudson's theorem for finite-dimensional quantum systems", *J. Math. Phys.* **47** (2006).
- W. O. Alltop, "Complex sequences with low periodic correlations", *IEEE Trans. Inf. Theory* **26** (1980);
  A. Klappenecker and M. Rötteler, "Constructions of mutually unbiased bases", in *Finite Fields and Applications*,
  Lecture Notes in Computer Science **2948** (2004).
- B. S. Damski, R. Bistroń, D. Ponterio, J. Czartowski and K. Życzkowski, "Product Weyl–Heisenberg covariant mutually
  unbiased bases and extremal non-stabilizerness" (2026), [arXiv:2603.15550](https://arxiv.org/abs/2603.15550).
- S. Gurevich and R. Hadani, "Proof of the Kurlberg–Rudnick rate conjecture",
  [arXiv:math-ph/0404074](https://arxiv.org/abs/math-ph/0404074); "Bounds on certain higher-dimensional exponential
  sums via the self-reducibility of the Weil representation", [arXiv:math/0612765](https://arxiv.org/abs/math/0612765).
- P. Kurlberg and Z. Rudnick, "On the distribution of matrix elements for the quantum cat map", *Ann. of Math.*
  **161** (2005).
- M. Erew and M. Goldstein, "Extremizing measures of magic on pure states by Clifford-stabilizer states" (2025),
  [arXiv:2512.19657](https://arxiv.org/abs/2512.19657).
