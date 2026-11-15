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
   - Web searches on 2026-11-14 found no point count, zeta function or Galois action for this fourfold, nor for the
     nine-variable cubic sixfold. The nearest are the Fermat cubic fourfold's form of level 27, and a census of cubic
     fourfolds over F₂ that counts points to find Frobenius eigenvalues.
   - [READING] Laza and Zheng's classification comes from the Leech lattice. The point counts here see the same field
     from the other side, through Frobenius.
   - **The counts are Airy moments.** By orthogonality the cubics' counts are moments of the cubic exponential sums
     Σ_x e((x³ + ax)/p).
     - Haessig studied the L-functions of their symmetric powers: rationality, degree (k + 1)/2 for odd k, and p-adic
       bounds (J. reine angew. Math. 2009; with Rojas-León for the generalized family).
     - Sabbah and Yu computed the Hodge numbers of the complex analogue, the symmetric powers of the Airy equation:
       every one is 0 or 1, at rational exponents (Tunisian J. Math. 2023). The classical part, where the exponents
       are integers, has exactly the sizes the counts here need.
     - Neither identifies a piece. Here they are (5|p), LMFDB's 35.3.c.b, (105|p) and, at k = 11, a weight-3 CM form
       of Q(√−1155).
   - Rational weight-3 CM newforms need a class group of exponent at most 2 (Schütt's classification). Q(√−35) and
     Q(√−1155) both qualify, with one class in each genus.

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
  (COIN_AT_FIVE.md §6).
- Writing to any of them is the author's call. The note drafted earlier for Gurevich could be widened into one for this
  group. With Theorems 1 to 7 and rounds 15 to 17 it now has something specific to offer them: the oscillator states' Wigner
  values as a family whose monodromy they could identify.

## Sources

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
- R. Evans and J. Greene, "A quadratic hypergeometric ₂F₁ transformation over finite fields",
  [arXiv:1511.00020](https://arxiv.org/abs/1511.00020).
- J. H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed. (2009); K. Ireland and M. Rosen, *A Classical
  Introduction to Modern Number Theory*, 2nd ed. (1990).
- C. D. Haessig, "L-functions of symmetric powers of cubic exponential sums", *J. reine angew. Math.* **631** (2009),
  [arXiv:math/0608521](https://arxiv.org/abs/math/0608521); C. D. Haessig and A. Rojas-León, the generalized Airy family,
  [arXiv:1008.0408](https://arxiv.org/abs/1008.0408).
- C. Sabbah and J.-D. Yu, "Hodge properties of Airy moments", *Tunisian J. Math.* **5** (2023),
  [arXiv:2112.13405](https://arxiv.org/abs/2112.13405).
- M. Schütt, "CM newforms with rational coefficients", *Ramanujan J.* **19** (2009),
  [arXiv:math/0511228](https://arxiv.org/abs/math/0511228).
- The LMFDB Collaboration, newform 35.3.c.b, [lmfdb.org](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/35/3/c/b/).
