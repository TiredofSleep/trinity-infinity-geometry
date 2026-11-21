# The circle operator stays inside the square-root limit [FORCED by a published theorem; measured; NAMED: Gurevich and Hadani, Kurlberg and Rudnick, Alon and Boppana, Terras]

> From the lens handoff of 20 November 2026 (Part A), a working session with the author. This page restates known
> mathematics in the vocabulary of Ramanujan graphs and measures it. It is not a new result.

## The operator

Use the conventions of [`TORUS_MOMENTS.md`](TORUS_MOMENTS.md) §1.
- **Phase-point operators.** ⟨a|A_(q,k)|b⟩ = [a + b = 2q] ω^(k(a − b)), with ω = e^(2πi/p). Each A_v is Hermitian,
  squares to the identity and has trace 1.
- **The circle.** Fix a quadratic non-residue δ and c ≠ 0. The circle C = {(q, k) : q² − δk² = c} has p + 1 points.
  It is an orbit of the non-split torus T, which is cyclic of order p + 1.
- **The circle operator** is S_C = Σ_(v in C) A_v, a Hermitian p × p matrix of trace p + 1. It is Theorem 3's
  operator in [`TORUS_MOMENTS.md`](TORUS_MOMENTS.md) §7.
- **The handoff's convention** puts ω^(2k(x − q)) where this page has ω^(k(a − b)), which is k → −k. Circles are
  symmetric under k → −k, so it is the same operator (check C1 below).

## The statement

> **For every circle of the non-split torus, every eigenvalue of S_C satisfies |λ| ≤ 2√p.** This follows from
> Gurevich and Hadani's Theorem 4.2 for p a sufficiently large prime. It is measured with no exception for every
> prime 5 ≤ p ≤ 997 (c = 1) and 5 ≤ p ≤ 397 (c = 1, 2, 3). The largest ratio |λ|/(2√p) is 0.99931, at p = 673.

**Why, in three steps.**
1. S_C commutes with the torus T, acting through the Weil representation, and the restriction of that
   representation to T is multiplicity-free [Gurevich, Hadani and Sochen]. So S_C is diagonal in T's eigenbasis, the
   oscillator states ψ_χ.
2. T moves any point v of C around the whole circle, and U_g A_v U_g† = A_(gv). So λ_χ = (p + 1)⟨ψ_χ|A_v|ψ_χ⟩, the
   same for every v in C (check C3).
3. A_v = π(2v) ρ(−I) is a displaced parity, −I lies in T, and |ψ_χ⟩⟨ψ_χ| = (1/(p + 1)) Σ_(B in T) χ̄(B) ρ(B). So
   λ_χ = (a unimodular constant) × Σ_(B in T) χ̄(B) Tr(ρ(B) π(2v)). Gurevich and Hadani's Theorem 4.2 bounds exactly
   this sum: |Σ_(B in T) Tr(ρ(B) π(ξ)) χ(B)| ≤ 2√p for every non-trivial ξ.

**The constant was the whole question,** and it comes out exactly.
- Gurevich and Hadani also state the bound as a matrix coefficient, |⟨ψ|π(ξ)ψ⟩| ≤ C_ξ/√p. For the non-split torus
  C_ξ = 2 (their §4.1, footnote 5).
- Through that form one gets only |λ| ≤ 2√p (1 + 1/p), which is above the limit. The handoff flagged exactly this.
- Their Theorem 4.2 states the bound before dividing by |T| = p + 1. The circle operator's eigenvalue is that sum
  itself, so the factor cancels.

**The hypothesis on p.** Gurevich and Hadani state the theorem for p a sufficiently large prime.
- Their footnote 4 says that what is needed is that ξ not be an eigenvector of the torus. That holds for every
  non-zero ξ when the torus is non-split.
- We have not checked their proof for small p. The measurements cover 5 ≤ p ≤ 997.

## Why the word Ramanujan [NAMED; READING]

- **The definition.** A (p + 1)-regular graph is Ramanujan when its non-trivial eigenvalues satisfy |λ| ≤ 2√p. By
  the Alon–Boppana theorem no infinite family does better, so the bound is a limit, and Ramanujan graphs sit at it.
- **S_C is not a graph's adjacency matrix.** Each A_v is the permutation x → 2q − x with phases, so S_C is a
  Hermitian weighted ("magnetic") adjacency operator of degree p + 1 on ℤ/p.
- **It has no trivial eigenvalue** ±(p + 1).
- **No zeta function is claimed here.** We did not check whether Ihara's determinant formula holds for such weighted
  operators.
- **The closest named relatives** are Terras's finite upper half plane graphs, which are Ramanujan by Katz's bound on
  Soto-Andrade sums, and the semicircle graphs of Forey, Fresán, Kowalski and Wigderson
  ([`LITERATURE_MAP.md`](LITERATURE_MAP.md)).
- **[READING]** [`TORUS_MOMENTS.md`](TORUS_MOMENTS.md) finds the eigenvalues filling the interval along a semicircle.
  That is proved through low moments and measured beyond. The bound says none leaves the interval. Together: the
  operator runs at the limit.

## What is known and what is not

- **Known:** the bound follows from Gurevich and Hadani's Theorem 4.2. This page restates it and measures it.
- **Our search** found no earlier statement of it in the vocabulary of Ramanujan graphs. That is a statement about
  the search, not a claim of novelty.
- **Earlier uses of the name in this project** (the handoff's Part C, checked 21 November 2026):
  - the Ramanujan–Petersson bound: J55 checks |a_p| ≤ 2p^(5/2) for its weight-6 form at every prime p ≤ 97;
  - Ramanujan sums: the April 2026 reflection audit writes its eigenvalues as c(j, 10), and J24 asks whether its
    spectral product has a Ramanujan-sum form.

  None of them uses the phrase "Ramanujan graph".
- **Not claimed:** nothing here bears on the Riemann hypothesis. "Ramanujan" is used in the graph-theory sense only.
- **Open (the handoff's Part E, not yet registered):** whether the top of the spectrum, 2 − max λ/√p, behaves like
  independent draws from the semicircle or like a random matrix. A pilot (20 November, not registered) found
  independent-draw statistics. A round on fresh primes 1000–3000 waits for the author.

## Checks ([`verify_circle_operator.py`](verify_circle_operator.py), [`verify_circle_operator.log`](verify_circle_operator.log))

| check | what | result |
|---|---|---|
| C1 | S_C is Hermitian with trace p + 1, and the handoff's convention gives the same matrix | 228 operators (5 ≤ p ≤ 397, c = 1, 2, 3), no failures |
| C2 | every eigenvalue satisfies \|λ\| < 2√p | p ≤ 397 with c = 1, 2, 3, and p ≤ 997 with c = 1; largest ratio 0.99931, at p = 673 |
| C3 | λ = (p + 1)⟨ψ\|A_v\|ψ⟩, the same at every point of the circle | p = 11, 31, 101: deviation 1.5·10⁻¹¹ |
| C4 | moments 2, 4, 6 of λ/√p at p = 251 | 1.004, 2.003, 4.943 (semicircle 1, 2, 5) |

## Sources

- S. Gurevich and R. Hadani, "Proof of the Kurlberg–Rudnick rate conjecture", arXiv:math-ph/0404074 (v7, 2006):
  Theorem 3.1, §4.1 (footnote 5: C_ξ = 2 for the non-split torus) and Theorem 4.2 (the sum bounded by 2√p).
- P. Kurlberg and Z. Rudnick, on the distribution of matrix elements of the quantum cat map (the rate conjecture).
- S. Gurevich, R. Hadani and N. Sochen, on the oscillator states (multiplicity-free restriction to a torus).
- A. Terras, *Fourier Analysis on Finite Groups and Applications* (finite upper half plane graphs; Katz's bound on
  Soto-Andrade sums).
- N. Alon (the Alon–Boppana bound); A. Lubotzky, R. Phillips and P. Sarnak (Ramanujan graphs).
