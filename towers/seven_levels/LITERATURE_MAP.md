# The neighbourhood: who else works on this ground

> *find out who else is citing Forey, Fresán and Kowalski's equidistribution theory and let's see if it helps our
> expansion and synthesis* — the author, 14 November 2026

Tags: **[NAMED]** a cited result · **[READING]** an interpretation · **[OPEN]** a step not yet taken.

**Keywords:** trace functions · exponential sums · Kloosterman sums · equidistribution · Tannakian monodromy · Mellin
transform · generalized Jacobians · semicircle law · pseudorandom graphs · free probability · magic states · Wigner
function · modular forms · Kloosterman moments · Feynman integrals

**How this was found.** On 14 November 2026 the citation indexes Semantic Scholar and OpenAlex listed 17 works citing
A. Forey, J. Fresán and E. Kowalski, "Arithmetic Fourier transforms over finite fields: generic vanishing,
convolution, and equidistribution" (arXiv:2109.11961, 2021). The abstracts of the relevant ones were read from the
arXiv. A second search followed the modular form that turned up in the sixth moment
([`TORUS_MOMENTS.md`](TORUS_MOMENTS.md) §9) to the literature on moments of Kloosterman sums.

## What the neighbourhood gives this floor

1. **A route to the semicircle at every point** [NAMED; OPEN]. Each Wigner value of an oscillator state is a Fourier
   transform on the torus: p W_χ(u) = (1/m) Σ_(g in T) χ̄(g) Tr(U_g A_u) ([`TORUS_MOMENTS.md`](TORUS_MOMENTS.md) §7).
   The torus of norm-one elements is a connected commutative algebraic group, in fact the generalized Jacobian of a
   conic with a pair of conjugate points marked [NAMED: Rosenlicht; Serre, *Algebraic Groups and Class Fields*].
   Forey, Fresán and Kowalski prove that Fourier transforms of trace functions on such groups equidistribute, as the
   character χ varies, toward the Haar measure of a compact group, the Tannakian monodromy group; Zurbuchen (2026)
   proves this "in previously unavailable generality". If the monodromy group of our sheaf is SU(2), the oscillator
   states' Wigner values follow the semicircle at every point and in every moment. That would complete
   [`TORUS_MOMENTS.md`](TORUS_MOMENTS.md) §7, where the generic polygons' cancellation is the one step left. Identifying
   that monodromy group is the open step, and these authors' methods are built for it.
2. **Our operator has twins** [NAMED; READING]. Forey, Fresán, Kowalski and Wigderson (2025, 2026) build explicit
   graphs whose eigenvalues follow Wigner's semicircle law, from character sums on generalized Jacobians: graphs
   "spectrally indistinguishable from random graphs" whose local structure is far from random. The circle operator
   S_C of §7, the sum of the phase-point operators around one circle, is the same kind of object: in the torus's
   eigenbasis it is a weighted Cayley operator on the turning wheel, and its eigenvalues are character sums. So the
   oscillator states' semicircle and those graphs' semicircle look like one phenomenon, built once from quantum phase
   space and once from combinatorics.
3. **Rates** [NAMED]. Kowalski and Untrau (2025) turn the equidistribution theorems of Deligne and Katz into Wasserstein
   bounds. Sawin, Forey, Fresán and Kowalski's *Quantitative sheaf theory* (J. Amer. Math. Soc.) bounds the constants
   uniformly in the characteristic. The corrections measured here, the skew of −1/√p (proved, §6) and the 1/p terms of
   the sixth moment (§7, §9), are rates of exactly this kind.
4. **Independence across points** [NAMED; READING]. Rojas-León (2024) proves that Gauss sums attached to several
   monomials equidistribute independently, unless the obvious relations bind them. For this floor it is the expected
   independence of the Wigner values at different circles, the shape of Kurlberg and Rudnick's conjecture for smooth
   observables (a weighted sum of traces of independent SU(2) matrices).
5. **The moments carry modular forms** [NAMED]. The sixth moment brought in the newform of weight 4 and level 6,
   (η(τ)η(2τ)η(3τ)η(6τ))² (§9). It also governs:
   - the sixth moment of Kloosterman sums, and the Barth–Nieto quintic (Hulek, Spandaw, van Geemen and van Straten
     2001);
   - Bessel moments of Feynman integrals (Broadhurst 2016).

   Fresán, Sabbah and Yu built the Hodge theory of Kloosterman connections, the motives behind these moments, and proved
   the functional equations that Broadhurst and Roberts conjectured (2022); Yun attached Galois representations to the
   moments and proved Evans's conjectures (2015). The fourth cumulant brought in η(4τ)⁶, the form with complex
   multiplication by the Gaussian integers.
   - Its proof ([`TORUS_MOMENTS.md`](TORUS_MOMENTS.md), Theorem 5) uses only classical tools: a 2-isogeny over F_p,
     Landen's transformation (Silverman, III.4.5), and Jacobi sums of a character of order 4 (Ireland and Rosen,
     ch. 8). The same transformation, written for the finite-field hypergeometric function ₂F₁, is Evans and Greene's
     quadratic transformation (arXiv:1511.00020).
   - [READING] Fresán stands on both of the strands this floor crosses: equidistribution, and the motives of Kloosterman
     moments.
6. **The fifth moments live on a double octic** [NAMED; measured]. I5 reduces to the double cover of 3-space branched
   along Clebsch's diagonal cubic surface and its five Sylvester planes, and its count carries the weight-4 newform of
   level 10 ([`TORUS_MOMENTS.md`](TORUS_MOMENTS.md) §8, Theorem 7).
   - Double octics are the classical workshop for rigid Calabi–Yau threefolds and their modular forms. Cynk and
     Szemberg (1999) give their smooth models, and Meyer's book (2005) and his search of S4-symmetric double octics
     (arXiv:1810.03659) catalogue the forms. Whether this octic, which is S5-symmetric, is in Meyer's tables was not
     checked.
   - Schütt (2003) found a rigid Calabi–Yau threefold of level 10 another way, from a fibre product of elliptic
     surfaces. Whether it is birational to this double octic is open.
   - Rigid Calabi–Yau threefolds over Q are modular (Gouvêa and Yui 2011; Dieulefait and Manoharmayum 2003). A proof of
     the count would need the octic's rigidity, and a finite Faltings–Serre check.
   - J5 carries the curve of conductor 150 and the CM form of level 15 from Kloosterman's fifth moment (Peters, Top and
     van der Vlugt 1992).
   - [READING] Duco van Straten stands where these meet: on the Barth–Nieto quintic of the sixth moment (with Hulek,
     Spandaw and van Geemen), and on double octics (with Cynk).
7. **The coin at 5, and the cubics in 7, 9 and 11 variables** [NAMED; measured; [`COIN_AT_FIVE.md`](COIN_AT_FIVE.md)].
   - Clebsch's cubic is the flat face of the coin at 5. Its 27 lines (Clebsch 1871) and its icosahedral symmetry, as
     the Hilbert modular surface of Q(√5) (Hirzebruch 1976), are classical.
   - The cubic fourfold {Σx = Σx³ = 0} in seven variables is one of the six cubic fourfolds with a maximal group of
     symplectic automorphisms. It is X¹(A7) in Laza and Zheng's classification (Math. Z. 2022), with transcendental
     lattice of discriminant 35, and the Clebsch–Segre cubic in Koike's equations (arXiv:2409.08448).
   - A two-dimensional transcendental part is carried by a weight-3 CM form: Livné's mechanism for singular K3
     surfaces (1995). Here the field is Q(√−35).
   - **Corrected 2026-11-17.** Web searches on 2026-11-14 found no point count, zeta function or Galois action for
     this fourfold. They missed the source: these cubics are Livné's W_n. Livné (1987) introduced them to compute
     the moments of the cubic exponential sums Σ_x e((ax³ + bx)/p), and so proved Birch's conjecture on their
     average distribution. He also proved a 2-dimensional piece of the 10th moment modular, the first use of his
     2-adic criterion.
     - Chênevert's McGill thesis (2008) decomposed their cohomology under S_n (Prop. 3.5.1). It found the
       14 + 6(5|p) Tate part of X7 (Prop. 5.7.1), and it **proved** the sign part of X7 is the weight-3 newform
       of level 35 with character ε_35, 35.3.c.b (§5.7), by a Faltings–Serre criterion generalized to odd traces.
     - So the count of X7 and its form, rounds 19 to 21, were a rediscovery (GRAVEYARD.md).
     - Chênevert's outlook (p. 146) proposes the vanishing-cycle analysis that Theorem 8 carries out. It also
       asks whether X7 has a model with good reduction at 3, and e1 = e3 = 0 is one.
   - [READING] Laza and Zheng's classification comes from the Leech lattice. The point counts here see the same field
     from the other side, through Frobenius.
   - **The counts are Airy moments.** By orthogonality the cubics' counts are moments of the cubic exponential sums
     Σ_x e((x³ + ax)/p).
     - Haessig studied the L-functions of their symmetric powers: rationality, degree (k + 1)/2 for odd k, and p-adic
       bounds (J. reine angew. Math. 2009; with Rojas-León for the generalized family).
     - Sabbah and Yu computed the Hodge numbers of the complex analogue, the symmetric powers of the Airy equation:
       every one is 0 or 1, at rational exponents (Tunisian J. Math. 2023). The classical part, where the exponents
       are integers, has exactly the sizes the counts here need.
     - Neither identifies a piece; Chênevert did, at 7. Here they are (5|p), LMFDB's 35.3.c.b (Chênevert's), (105|p)
       and, at k = 11, a weight-3 CM form
       of Q(√−1155). At 13, 17 and 21 they are twisted symmetric squares, with determinants (−15015|p), (−51051|p) and
       (−138567|p), and at 15 a CM form of Q(√−3003). At 19, 23 and 27 they are four-dimensional, with determinants
       (969969|p), (3187041|p) and (3187041|p), read prime by prime, and at 25 five-dimensional, with (3187041|p),
       read from the cube of Frobenius.
     - Qin computed the Hodge numbers of the related motives in more variables, and found no identifications either
       (Crelle 2024).
     - Chuang's dissertation (arXiv:2607.05757, July 2026) gives an arithmetic Picard–Lefschetz formula for diagonal
       singularities and applies it to the Airy moments at primes p > 5. It uses another model,
       z³ = Σ(y³/3 − y), and it excludes 3 and 5. The good model at 3 here (e1 = e3 = 0), whose nodes are the author's
       "3 at its square", and the nodes' parity rule for the determinants are not in the parts of it read
       (2026-11-15). Read again on 2026-11-16: its Theorems 4.21 and 4.22 give the full local Galois representation
       of the Airy motive at every prime p ≥ 5 for odd k, in a model whose singularities are z³ plus squares, with
       the inertia invariants fixed by a condition on v_p. The classical part's local behaviour at l ≥ 5, which
       Theorem 8 (DETERMINANTS.md) uses, is contained in that description. The prime 3 and the global determinant
       are not there.
     - **The nearest precedent is Kloosterman's** (read 2026-11-15, for round 27). Yun attached Galois
       representations to the Kloosterman moments. For odd d he proved that their determinant is the Jacobi symbol
       (p/d!!) (Compositio 2015, Theorem 1.2.3).
       - He expected the three-dimensional cases to come from a quadratic character and a modular form, through
         O(3) ≅ PGL(2) × {±1}.
       - He expected the four-dimensional ones, when the determinant's field is real, to come from two Hilbert modular
         forms over it.
       - The Airy pieces here have the same shape.
         - Their determinant is (p/A_k), where A_k is k!! with each multiple of 3 divided by 3 once.
         - The three-dimensional pieces at 13, 17 and 21 are twisted symmetric squares.
         - The four-dimensional ones at 19, 23 and 27 have real quadratic determinant fields.
       - So the shape is known for Kloosterman sums. For the Airy moments, no search found the determinants or the
         cube's 3.
   - Rational weight-3 CM newforms need a class group of exponent at most 2 (Schütt's classification). Q(√−35),
     Q(√−1155) and Q(√−3003), the fields at 7, 11 and 15, all qualify, with one class in each genus. At 13,
     Q(√−15015) does not (exponent 12), and the piece there is a twisted symmetric square instead.
   - The step from a three-dimensional orthogonal piece to a symmetric square is SO(3) ≅ PGL(2) with Tate's lifting
     theorem (Serre 1977, §6). The root's inner twists are Ribet's (Math. Ann. 1980).

8. **The qudit direction: the magic state of a qudit T gate** [NAMED; checked 2026-11-17; not a round].
   - **The bridge, checked numerically** (p = 11, 13, 17, 19). A single-qudit cubic-phase state ψ(x) = ω^(cx³ + ⋯)/√p,
     the magic state of a qudit T gate, has every Wigner value equal to a Birch sum, S_t(a)/p² with t = c/4. Each
     value is taken exactly p times.
   - **What follows from known theorems.**
     - The state's integer-order Wigner moments are the moments of the Birch sums, and so point counts of Livné's
       W_n: exactly our counts when p ≡ 2 (mod 3), a cubic twist of them when p ≡ 1.
     - Its total negativity tends to (8/(3π))√p, by the semicircle law for Birch sums (Katz 1987, Theorem 19,
       monodromy SL₂ for p > 7; Livné 1987).
   - **Known, and credited.**
     - Kocia and Love (*Quantum* 2021, arXiv:1810.03622) call the qudit π/8 gate the discrete analogue of the Airy
       function. They write the qutrit magic state's Wigner function as a cubic sum mod 9, with qutrit examples only,
       no negativity against p, and no Sato–Tate.
     - Wilson and White (arXiv:2011.13937): Haar-random qudit states have mana ½ ln d − ½ ln(π/2), that is,
       negativity ≈ √(2/π)·√d.
     - Li and Luo (*Phys. Lett. A* 2022): the qutrit T gate is the optimal diagonal gate for Wigner negativity.
     - Feng and Luo (*Phys. Rev. A*, doi:10.1103/d36z-tb7h): at p = 5 the T gate is not optimal; 500 diagonal
       gates outside the Clifford hierarchy beat it.
     - Koukoulekidis and Jennings (*npj Quantum Inf.* 2022): bounds on distillation from the Rényi entropies of
       Wigner distributions.
     - Howard and Vala (2012): the qudit π/8 gates. Campbell, Anwar and Browne (2012): their distillation in every
       prime dimension.
     - Zhu, Mao and Yi (arXiv:2410.13575, 2024; found 2026-11-17, during round 29) study the third moments of qudit
       Clifford orbits. When p ≡ 1 (mod 3) they distinguish three types of T gates and magic states by cubic
       characters, use cubic Gauss and Jacobi sums, and cite Kummer's problem. Round 29's E5, the third Wigner moment
       of each class, 2p² + 2p·Re(χ(3t)G(χ)²) = p·g(3, 3t)², is their Lemma 24, κ(f, T) = g(3, ac)²/d². This was
       checked in the paper on 2026-11-17, with the author's permission to open it.
     - Feng and Luo (*EPJ Plus* 2025, doi:10.1140/epjp/s13360-025-06394-x): the Howard–Vala T gates form three
       Clifford classes exactly when p ≡ 1 (mod 3). Also Feng and Luo (*Phys. Scr.* 2024): for the L1 norm the T
       gate is optimal among diagonal gates in every prime dimension. Li and Luo (*Phys. Lett. A* 2023): the qutrit
       T gate is optimal for Wigner negativity.
     - Feng and Luo also show that for the L1 norm the T gate is optimal among all diagonal gates in every prime
       dimension; for Wigner negativity they leave it open beyond 3.
   - **Not found in what we could read.**
     - The bridge stated for every prime p.
     - The T state's total negativity (8/(3π))√p. It sits above the Haar-random √(2/π)·√p, so cubic-phase magic
       states are more negative than typical states.
     - The exact Wigner moments as point counts, with modular forms: Chênevert's level-35 form enters at n = 7.
   - **The caution.** At p = 5 the T gate is not the most negative diagonal gate, so the √p constant describes T-type
     states, not the best diagonal ones.
   - **The verdict.** This is a small connection between known results that the qudit-magic community may find
     useful. The next step is a question to an expert (Campbell, Howard or Jennings). The author lifted the grounding
     gate on 2026-11-17, and round 29 of [`PREREG.md`](PREREG.md) measures it: the T state against random states, and
     the ladder of higher levels.
   - **Round 29's answer** (2026-11-17, five of six held).
     - The T state's S/√p averages 0.84890 from 1000 to 3000, against 8/(3π) = 0.84883. Every class beats the exact
       Haar mean at every prime from 31 to 5000.
     - The higher levels do not climb. Degree-5 and degree-6 phase states sit at USp(4)'s 0.7905, below random, and
       degrees 7 and 8 at USp(6)'s 0.7985.
     - At 5 and 7 the T state is the most negative of all phase states with p-th-root-of-unity phases (exhaustive).
       That partly answers Feng and Luo's open question, for gates whose phases are p-th roots of unity.
     - Round 30 (three of four held). At 7, 400 optimizations over arbitrary phases found nothing above the T
       state, whose best class is optimal there, numerically. At 5, phases off the fifth roots beat it, as Feng and
       Luo found (our optimum 1.977576), and twenty-fifth roots come within 0.4%.
     - The short note in standard terms is [`QUDIT_NEGATIVITY_NOTE.md`](QUDIT_NEGATIVITY_NOTE.md).

## The works citing Forey, Fresán and Kowalski (as indexed on 2026-11-14)

| year | work | why it matters here |
|---|---|---|
| 2022 | W. Sawin, A. Forey, J. Fresán, E. Kowalski, *Quantitative sheaf theory*, J. Amer. Math. Soc. | uniform constants: rates |
| 2023 | A. Forey, J. Fresán, E. Kowalski, *Sidon sets in algebraic geometry*, IMRN | the same toolkit, on generalized Jacobians |
| 2023 | V. Blomer, M. Einsiedler, E. Kowalski, M. Viazovska, *Group Actions and Harmonic Analysis in Number Theory*, Oberwolfach report | the school's meeting |
| 2024 | A. Rojas-León, *Equidistribution and independence of Gauss sums*, Adv. Math. | independence across points |
| 2024–25 | B. Zurbuchen, *Hypergeometric sheaves with Tannakian monodromy group G2*, IMRN | computing monodromy groups |
| 2024, 2026 | G. P. Ribeiro, generic vanishing for holonomic D-modules; *A moduli space of character sheaves* | the theory's foundations |
| 2025 | E. Kowalski, T. Untrau, *Wasserstein metrics and quantitative equidistribution of exponential sums over finite fields*, arXiv:2505.22059 | rates |
| 2025 | A. Rai, K. V. Shuddhodan, *Generic vanishing on homogeneous spaces in arbitrary characteristic*, arXiv:2507.13452 | foundations |
| 2025 | A. Forey, J. Fresán, E. Kowalski, Y. Wigderson, *Spectrally indistinguishable pseudorandom graphs*, arXiv:2511.21351 | semicircle spectra from character sums |
| 2026 | L. Xie, *On a conjecture of Erdős over function fields*, Math. Z. | an application |
| 2026 | G. P. Ribeiro, *A moduli space of character sheaves*, arXiv:2602.02664 | foundations |
| 2026 | B. Zurbuchen, *Equidistribution for Tannakian monodromy groups*, arXiv:2602.21878 | the equidistribution theorem in full generality |
| 2026 | A. Forey, J. Fresán, E. Kowalski, Y. Wigderson, *Jacobian graphs*, arXiv:2603.13198 | semicircle spectra on generalized Jacobians |
| 2026 | A. Bah, K. V. Shuddhodan, *Uniform stratified vanishing and equidistribution on G_m^d*, arXiv:2608.00304 | equidistribution on higher-dimensional tori, the many-wheel case |

## Who to read first

- **Javier Fresán**, for both strands; **Emmanuel Kowalski**, for equidistribution and its rates; **Arthur Forey** and
  **Yuval Wigderson**, for the semicircle graphs. **Duco van Straten** and **Christian Meyer**, for the double octic and its form
  of level 10 (Theorem 7). **Claude Sabbah** and **Jeng-Daw Yu**, for the Airy moments behind the cubics
  (COIN_AT_FIVE.md §6). **Ping-Hsun Chuang**, for the Airy moments at their bad primes (COIN_AT_FIVE.md §10).
  **Zhiwei Yun**, whose determinant (p/d!!) for the Kloosterman moments is the shape of the rule here
  (COIN_AT_FIVE.md §12).
- Writing to any of them is the author's call. The note drafted earlier for Gurevich could be widened into one for this
  group. With Theorems 1 to 7 and rounds 15 to 17 it now has something specific to offer them: the oscillator states' Wigner
  values as a family whose monodromy they could identify.

## Sources

- L. Kocia and P. Love, "Stationary phase method in discrete Wigner functions and classical simulation of quantum
  circuits", *Quantum* **5** (2021) 494, [arXiv:1810.03622](https://arxiv.org/abs/1810.03622).
- J. Wilson and C. D. White, "Mana in Haar-random states", [arXiv:2011.13937](https://arxiv.org/abs/2011.13937).
- L. Feng and S. Luo, "Optimal ququint diagonal gates for generating Wigner negativity", *Phys. Rev. A*,
  [doi:10.1103/d36z-tb7h](https://journals.aps.org/pra/abstract/10.1103/d36z-tb7h).
- N. Koukoulekidis and D. Jennings, "Constraints on magic state protocols from the statistical mechanics of Wigner
  negativity", *npj Quantum Inf.* (2022), [arXiv:2106.15527](https://arxiv.org/abs/2106.15527).
- M. Howard and J. Vala, "Qudit versions of the qubit π/8 gate" (2012), [arXiv:1206.1598](https://arxiv.org/abs/1206.1598).
- N. Katz, "On the monodromy groups attached to certain families of exponential sums", *Duke Math. J.* **54** (1987).
- G. Chênevert, PhD thesis, McGill (2008),
  [PDF](https://www.math.mcgill.ca/goren/Students/Chenevert.thesis.pdf).

- A. Forey, J. Fresán and E. Kowalski, [arXiv:2109.11961](https://arxiv.org/abs/2109.11961) (2021).
- A. Forey, J. Fresán, E. Kowalski and Y. Wigderson, [arXiv:2511.21351](https://arxiv.org/abs/2511.21351) (2025) and
  [arXiv:2603.13198](https://arxiv.org/abs/2603.13198) (2026).
- E. Kowalski and T. Untrau, [arXiv:2505.22059](https://arxiv.org/abs/2505.22059) (2025).
- B. Zurbuchen, [arXiv:2602.21878](https://arxiv.org/abs/2602.21878) (2026).
- W. Sawin, A. Forey, J. Fresán and E. Kowalski, "Quantitative sheaf theory", *J. Amer. Math. Soc.* (2023),
  [doi:10.1090/jams/1008](https://doi.org/10.1090/jams/1008).
- A. Rojas-León, "Equidistribution and independence of Gauss sums", *Adv. Math.* (2024),
  [doi:10.1016/j.aim.2024.109762](https://doi.org/10.1016/j.aim.2024.109762).
- K. Hulek, J. Spandaw, B. van Geemen and D. van Straten, "The modularity of the Barth–Nieto quintic and its
  relatives", *Adv. Geom.* **1** (2001).
- D. Broadhurst, "Feynman integrals, L-series and Kloosterman moments" (2016),
  [arXiv:1604.03057](https://arxiv.org/abs/1604.03057).
- J. Fresán, C. Sabbah and J.-D. Yu, "Hodge theory of Kloosterman connections", *Duke Math. J.* **171** (2022),
  [arXiv:1810.06454](https://arxiv.org/abs/1810.06454).
- Z. Yun, "Galois representations attached to moments of Kloosterman sums and conjectures of Evans", *Compositio
  Math.* (2015), [arXiv:1308.3920](https://arxiv.org/abs/1308.3920).
- J.-P. Serre, *Algebraic Groups and Class Fields* (1988): generalized Jacobians.
- S. Cynk and T. Szemberg, "Double covers of P³ and Calabi–Yau varieties" (1999),
  [arXiv:math/9902057](https://arxiv.org/abs/math/9902057).
- C. Meyer, *Modular Calabi–Yau Threefolds*, Fields Institute Monographs **22** (2005); "Modularity experiments on
  S4-symmetric double octics", [arXiv:1810.03659](https://arxiv.org/abs/1810.03659).
- M. Schütt, "New examples of modular rigid Calabi–Yau threefolds" (2003),
  [arXiv:math/0311106](https://arxiv.org/abs/math/0311106).
- F. Gouvêa and N. Yui, "Rigid Calabi–Yau threefolds over Q are modular", *Expo. Math.* **29** (2011).
- C. Peters, J. Top and M. van der Vlugt, *J. reine angew. Math.* **432** (1992): Kloosterman's fifth moment.
- A. Clebsch, *Math. Ann.* **4** (1871): the diagonal cubic surface.
- F. Hirzebruch, *Russian Math. Surveys* **31** (1976): the Hilbert modular group of Q(√5) and Clebsch's cubic.
- R. Laza and Z. Zheng, "Automorphisms and periods of cubic fourfolds", *Math. Z.* **300** (2022),
  [arXiv:1905.11547](https://arxiv.org/abs/1905.11547).
- K. Koike, "Cubic fourfolds with symplectic automorphisms" (2024), [arXiv:2409.08448](https://arxiv.org/abs/2409.08448).
- R. Livné, *Israel J. Math.* **92** (1995): two-dimensional orthogonal motives and weight-3 CM forms.
- R. Livné, "The average distribution of cubic exponential sums", *J. reine angew. Math.* **375/376** (1987); "Cubic exponential sums and Galois representations", *Contemp. Math.* **67** (1987).
- G. Chênevert, *Exponential sums, hypersurfaces with many symmetries and Galois representations*, PhD thesis, McGill University (2008).
- R. Evans and J. Greene, "A quadratic hypergeometric ₂F₁ transformation over finite fields",
  [arXiv:1511.00020](https://arxiv.org/abs/1511.00020).
- J. H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed. (2009); K. Ireland and M. Rosen, *A Classical
  Introduction to Modern Number Theory*, 2nd ed. (1990).
- C. D. Haessig, "L-functions of symmetric powers of cubic exponential sums", *J. reine angew. Math.* **631** (2009),
  [arXiv:math/0608521](https://arxiv.org/abs/math/0608521); C. D. Haessig and A. Rojas-León, the generalized Airy family,
  [arXiv:1008.0408](https://arxiv.org/abs/1008.0408).
- C. Sabbah and J.-D. Yu, "Hodge properties of Airy moments", *Tunisian J. Math.* **5** (2023),
  [arXiv:2112.13405](https://arxiv.org/abs/2112.13405).
- Y. Qin, "Hodge numbers of motives attached to Kloosterman and Airy moments", *J. reine angew. Math.* (2024),
  [arXiv:2302.05365](https://arxiv.org/abs/2302.05365).
- P.-H. Chuang, "On the generalized arithmetic Picard–Lefschetz formula" (dissertation, 2026),
  [arXiv:2607.05757](https://arxiv.org/abs/2607.05757).
- M. Schütt, "CM newforms with rational coefficients", *Ramanujan J.* **19** (2009),
  [arXiv:math/0511228](https://arxiv.org/abs/math/0511228).
- The LMFDB Collaboration, newform 35.3.c.b, [lmfdb.org](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/35/3/c/b/).
