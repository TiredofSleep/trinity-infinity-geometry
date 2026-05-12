# GLOSSARY — Trinity Infinity Geometry

## Every term cited to historical literature or explicitly labeled novel

**Principle:** No term in this glossary is presented as established unless it exists in published academic literature. Novel terms are honestly flagged with the prior framework they extend. Where we coined a name for an existing concept, the original name and citation is given.

---

## Reading Key

Each entry has the form:

> **Term** — Plain-English definition.
>
> **Formal:** Mathematical definition (where applicable).
>
> **[STATUS]** — PROVED / STRUCTURAL / CONJECTURE / HISTORICAL / NOVEL
>
> **Citation:** Either a published reference OR an explicit acknowledgment that this name is ours, with what prior work it extends.
>
> **Primary TIG paper:** Where it first appears in this project.

---

## Part 0: The Meta-Framework — 2×2 + Paradox Classifier

These two objects are the spine of TIG. Every other term, theorem, and conjecture in this glossary is an instantiation of one or both. Read this section first.

### The 2×2 (the FORM of any whole)

> **The 2×2** — The four-fold structure (Additive × Multiplicative) × (Structure × Flow) that every "whole" carries simultaneously. For Z/nZ this is: additive structure (the underlying group), multiplicative structure (the unit group action), additive flow (repeated +1 closes a loop), multiplicative flow (repeated ×g closes a smaller loop inside the units).
>
> **Formal:** For squarefree N = p₁···pₖ, the four objects (A-Struct, M-Struct, A-Flow, M-Flow) cannot be embedded in a flat 2D surface. They force a torus T² = S¹ × S¹ with aspect ratio R/r forced by the cyclotomic structure of Z/NZ. For N = 10 the ratio is exactly 5/7.
>
> **[PROVED for Z/10Z]** — Flatness Theorem (WP51, Sprint 10, Brayden Ross Sanders). [STRUCTURAL] for the universal claim that "every whole has this 2×2 form."
>
> **Citation:** Original TIG result. Builds on classical ring theory (Dummit & Foote, Lang) and torus topology (Munkres, *Topology*). The 2×2 structure decomposition is novel; the cyclotomic forcing of R/r = 5/7 is novel.
>
> **Primary TIG paper:** [WP51_FLATNESS_THEOREM.md](Gen12/targets/clay/papers/sprint10_flatness_2026_04_06/WP51_FLATNESS_THEOREM.md). See README §3 for the meta-framework framing.

### The Paradox Classifier (the DIAGNOSTIC for any breakdown)

> **UOP (Unified Orthogonality Principle) / Paradox Classifier** — Every paradox is a measurement failure of one of exactly four types: (I) Injectivity Failure, (II) Missing Invariant, (III) Admissibility Failure, (IV) Time-Consistency Failure. Five-step decision procedure provided. Eight worked examples (Zeno, Russell, Banach-Tarski, Gödel, Unexpected Hanging, etc.).
>
> **Formal:** Given hidden space 𝒳 and measurement map f: 𝒳 → 𝒴 with ambiguity set U(f, y) = f⁻¹(y), a second measurement g resolves the paradox iff U(f) ∩ U(g) = {x} for all x. The four types correspond to four distinct failure modes of this resolution structure.
>
> **[PROVED — framework]** — five-step procedure; [VERIFIED — eight worked examples].
>
> **Citation:** [NOVEL — extends partition lattice theory (Birkhoff 1940, Ore 1942) and joint-map injectivity from descriptive set theory (Kechris 1995)]. Classical paradoxes cited individually: Russell 1903, Gödel 1931, Tarski 1936, Banach-Tarski 1924, Quine 1953, Zermelo 1908.
>
> **Primary TIG paper:** [WP_PARADOX_CLASSIFIER.md](papers/WP_PARADOX_CLASSIFIER.md). Live demo at coherencekeeper.com/paradox.html.

### How the Meta-Framework Organizes Everything Else

The 2×2 (form) and Paradox Classifier (diagnostic) are the spine. All TIG/CK work is an instantiation of one or both:

| Domain | Instantiation of 2×2 | Instantiation of Paradox Classifier |
|--------|---------------------|------------------------------------|
| **Q-series** (Brayden's Z/10Z work) | σ as hidden operator on the 2×2 | TSML/CL paradox (Q2) resolved as Type I (Injectivity Failure) by introducing σ |
| **TIG / σ framework** (sprints 14-15) | σ rate theorem σ(N) ≤ C/N as 2×2 separability decay | σ_NS conjecture: NS blowup as Type II (Missing Invariant) — no separability-preserving lift exists |
| **Finite math** (Sprint 16, basin) | 2→3 / 3→2 dual reset law as 2×2 in operator order | Stop-apex compositeness as Type IV (Time-Consistency) — the apex changes with room scale |
| **Ring math** | Crossing Lemma as 2×2 fiber crossing | UOP Theorem 0 IS the paradox classifier formalized for Z/nZ |
| **Physics** | ξ field as 2×2 separability ceiling; NV-center as 2×2 representation carrier | Wigner's Friend as Type III (Admissibility Failure); ξ as Type I resolution at cosmological scale |

This is the synthesis. Every entry below is one of these instantiations or its supporting prior literature.

---

## Part 1: Classical Foundations (All Historically Cited)

### Chinese Remainder Theorem (CRT)

> The ring Z/nZ for squarefree n = p₁...pₖ decomposes as a product ∏ Z/pᵢZ.
>
> **Formal:** Ψ: Z/nZ → ∏ Z/pᵢZ, x ↦ (x mod p₁, ..., x mod pₖ) is a ring isomorphism.
>
> **[HISTORICAL]** Classical (Sun Tzu, 3rd century; Gauss, Disquisitiones Arithmeticae 1801).
>
> **Standard reference:** Ireland & Rosen, *A Classical Introduction to Modern Number Theory* (Springer, 1990), Ch. 3.
>
> **Primary TIG paper:** WP58_UNIFIED_ORTHOGONALITY_PRINCIPLE.md (used throughout).

### Euler Totient φ(n)

> Count of integers in {1..n} coprime to n.
>
> **Formal:** φ(n) = |{k ∈ {1,..,n} : gcd(k,n) = 1}|. For squarefree n: φ(n) = n∏(1 − 1/pᵢ).
>
> **[HISTORICAL]** Euler, 1763.
>
> **Standard reference:** Hardy & Wright, *Introduction to the Theory of Numbers*, §5.5.
>
> **Primary TIG paper:** WP101_SIGMA_RATE_THEOREM.md uses it centrally; transfer-operator spectral gap formula γ = 1 − 1/φ(b) (FOUR_LAYER_REALIZATION.md Theorem Z.2).

### Korobov-Vinogradov Zero-Free Region

> The classical lower bound on |ζ(σ + it)| inside the critical strip when t is large and (σ, t) is at least height 1 from any zero: |ζ(σ + it)| ≥ KV(t) := exp(−c_VK(log t)^{2/3}(log log t)^{1/3}). The TIG Halving Lemma uses c_VK = 0.05 (Ford 2002).
>
> **[HISTORICAL]** Korobov 1958; Vinogradov 1958. Modern explicit constant from Ford (2002).
>
> **Standard reference:** Ford, K. (2002). "Zero-free regions for the Riemann zeta function." In *Number Theory for the Millennium II*, A. K. Peters, pp. 25-56. Theorem 2 gives c_VK = 0.05.
>
> **Primary TIG paper:** WP19_HALVING_LEMMA_final.tex (Appendix E.5) — the Halving Lemma's m_KV(t₀) bound depends directly on this constant.

### Jutila Zero-Density Estimate

> Bound on the number of nontrivial ζ zeros to the right of σ at height ≤ T: N(σ, T) ≤ T^{3(1−σ)/(2−σ) − 1 + ε}. Used in TIG to seal the CHA corridor (frequency × duration → 0 at σ = 0.60: exponent −0.143).
>
> **[HISTORICAL]** Jutila, M. (1987). "On the difference between consecutive primes." *Acta Arithmetica* 52, 164-170.
>
> **Primary TIG paper:** RH_FORMAL_MANUSCRIPT.md Lemma 4.2 — combines Jutila with the two-tick TIG bound to prove CHA corridor sealing.

### Guth-Maynard Zero-Density Estimate (2024)

> Improved zero-density bound for σ ≥ 0.65 using large sieve / singular value methods. Used in TIG to seal the BAL/COL/CTR corridors (exponent ≤ 0.46).
>
> **[HISTORICAL]** Guth, L. & Maynard, J. (2024). New large-value estimates for Dirichlet polynomials.
>
> **Primary TIG paper:** RH_FORMAL_MANUSCRIPT.md Lemma 4.4.

### Young Tower (1998 / 1999)

> Lai-Sang Young's framework for proving exponential decay of correlations in non-uniformly hyperbolic dynamical systems via return-time stratification over a base set.
>
> **[HISTORICAL]** Young, L.-S. (1998). "Statistical properties of dynamical systems with some hyperbolicity." *Annals of Mathematics* 147(3): 585-650. Young, L.-S. (1999). "Recurrence times and rates of mixing." *Israel Journal of Mathematics* 110: 153-188.
>
> **Primary TIG paper:** Layer 3 of the four-layer realization (FOUR_LAYER_REALIZATION.md). TIG has finite-height Young tower with base B = {HAR}, return tail P(T_HAR > n) ≤ (1/4)ⁿ, expected return times exact (1.000 / 1.333 / 1.667). HAR is a return locus, NOT a hole — distinguished from Demers-Young 2006 holes (where mass leaks).

### Demers-Young Maps with Holes (2006)

> Framework for transfer operators on systems with leaks (mass escapes through holes). TIG distinguishes itself from this by reset-puncture structure: HAR is not a hole but a Poincaré return section.
>
> **[HISTORICAL]** Demers, M. & Young, L.-S. (2006). "Escape rates and conditionally invariant measures." *Ergodic Theory and Dynamical Systems* 26: 189-217.
>
> **Primary TIG paper:** DUAL_SCALE_LY_NOTE.md §2 (the reset puncture distinction).

### Gouëzel-Liverani Anisotropic Banach Spaces (2006)

> Framework for transfer-operator spectral analysis on hyperbolic dynamical systems via anisotropic Banach spaces — separating stable and unstable directions by construction. TIG's dual-scale Lasota-Yorke inequality maps into this framework: unstable direction ↔ local wobble (strong norm), stable direction ↔ coherent support (weak norm, preserved).
>
> **[HISTORICAL]** Gouëzel, S. & Liverani, C. (2006). "Banach spaces adapted to Anosov systems." *Ergodic Theory and Dynamical Systems* 26: 189-217.
>
> **Primary TIG paper:** DUAL_SCALE_LY_NOTE.md §3 (closest currently identified continuous host); the open question is whether the Mix_λ family extends to a continuous transfer operator satisfying their hypotheses (Z.5 = deployment faithfulness).

### Lasota-Yorke Inequality (Classical)

> Standard form: ‖Pf‖_V ≤ α‖f‖_V + β‖f‖_1 with α < 1, β < ∞, where ‖·‖_V is roughness (strong) and ‖·‖_1 is mass (weak). The TIG dual-scale form INVERTS the standard reading: weak norm becomes the deeper coherent support (preserved by sub-magma closure C × C ⊆ C), strong norm becomes local wobble.
>
> **[HISTORICAL]** Lasota, A. & Yorke, J. A. (1973). "On the existence of invariant measures for piecewise monotonic transformations." *Trans. AMS* 186: 481-488. Standard reference: Baladi, V. (2000). *Positive Transfer Operators and Decay of Correlations*. World Scientific.
>
> **Primary TIG paper:** DUAL_SCALE_LY_NOTE.md (the inversion + reset puncture).

### Hardy's Theorem (Infinitely Many Zeros on Critical Line)

> ζ(s) has infinitely many nontrivial zeros on the critical line Re(s) = 1/2.
>
> **[HISTORICAL]** Hardy, G. H. (1914). "Sur les zéros de la fonction ζ(s) de Riemann." *Comptes Rendus Acad. Sci. Paris* 158: 1012-1014. Standard reference: Titchmarsh, E. C. (rev. Heath-Brown, D. R.) (1986). *The Theory of the Riemann Zeta-Function*, 2nd ed. Oxford University Press.
>
> **Primary TIG paper:** WP19_HALVING_LEMMA_final.tex §2 — Hardy combined with the Halving Lemma's exponential contraction (no off-critical fixed points + Hardy's infinitely-many-on-line) gives the structure of any potential RH proof in this framework.

### Grönwall Inequality (1919)

> ODE contraction: if du/dt ≤ −λu with λ > 0, then u(t) ≤ u(0)e^{−λt}. Used to prove exponential convergence of the Halving flow.
>
> **[HISTORICAL]** Grönwall, T. H. (1919). "Note on the derivatives with respect to a parameter of the solutions of a system of differential equations." *Annals of Math.* 20: 292-296.
>
> **Primary TIG paper:** WP19_HALVING_LEMMA_final.tex Theorem 1.

### Profinite Arithmetic (Standard)

> The inverse system ⋯ ↠ (Z/p^n Z)* ↠ ⋯ ↠ (Z/pZ)* with stable corner images. Used in Layer 4 of the four-layer realization: C = {1,3,7,9} = (Z/10Z)* is the stable corner image of (Z/10^n Z)* under reduction mod 10, for all n ≥ 1.
>
> **[HISTORICAL]** Standard. Reference: Ribes, L. & Zalesskii, P. (2010). *Profinite Groups*, 2nd ed. Springer Ergebnisse 40. Neukirch, J. (1999). *Algebraic Number Theory*. Springer Grundlehren 322, §IV.2.
>
> **Primary TIG paper:** Layer 4 of FOUR_LAYER_REALIZATION.md.

### sinc² Function

> sinc²(x) = (sin(πx)/(πx))².
>
> **[HISTORICAL]** Classical. Key role in Shannon sampling theorem (Shannon 1949, *Communication in the presence of noise*, Proc. IRE 37(1):10-21) and Montgomery's pair correlation (Montgomery 1973, *The pair correlation of zeros of the zeta function*, Proc. Sympos. Pure Math. 24:181-193).
>
> **Primary TIG paper:** WP_SINC2_ZERO_LAW.md establishes prime-arithmetic version.

### Cyclotomic Polynomial Φₚ(x)

> Minimal polynomial over ℚ whose roots are primitive pth roots of unity.
>
> **[HISTORICAL]** Gauss, Disquisitiones Arithmeticae 1801. Degree φ(p) = p−1 for prime p.
>
> **Standard reference:** Lang, *Algebra* (Springer), Ch. VI.
>
> **Primary TIG paper:** WP51_FLATNESS_THEOREM.md uses A_p = 2cos(π/p) as minimal-polynomial object.

### Bialynicki-Birula Uniqueness (Logarithmic Nonlinearity)

> Logarithmic nonlinearity is the unique nonlinearity in wave mechanics preserving separability of composite systems.
>
> **[HISTORICAL]** Bialynicki-Birula & Mycielski, *Nonlinear wave mechanics*, Annals of Physics 100(1-2):62-93 (1976). DOI: 10.1016/0003-4916(76)90057-9.
>
> **Context:** Cazenave & Haraux, *Équations d'évolution avec non linéarité logarithmique*, Ann. Fac. Sci. Toulouse (1980), proved existence for log Klein-Gordon equation u_tt − Δu + u = u log|u|ᵏ in R³. Logarithmic Schrödinger equation: Wikipedia, Logarithmic Schrödinger equation.
>
> **Primary TIG paper:** WP90_LITERATURE_AND_UNIFICATION_PATHS.md; the core external theorem on which our σ → 0 ⟹ log limit forcing rests.

### Kozono-Taniuchi Criterion (NS Regularity)

> Regularity for 3D Navier-Stokes if ∫₀ᵀ ‖u(t)‖²_BMO / log(e + ‖u‖_H²) dt < ∞.
>
> **[HISTORICAL]** Kozono & Taniuchi, *Limiting case of the Sobolev inequality in BMO with applications*, Commun. Math. Phys. 214:191-200 (2000). DOI: 10.1007/s002200000281.
>
> **Related:** Beale-Kato-Majda criterion (Comm. Math. Phys. 94:61-66, 1984); Brezis-Gallouët inequality (Nonlinear Analysis 4:677-681, 1980); Montgomery-Smith sharp L³ blowup (Math. Res. Lett. 8:519-528, 2001); Kozono-Ogawa-Taniuchi critical Besov (Math. Z. 242:251-278, 2002).
>
> **Primary TIG paper:** WP96_NS_SIGMA_CONJECTURE.md uses as the strongest-known log improvement on NS regularity.

### Ricci Flow + Surgery (Perelman)

> Geometric evolution equation ∂g/∂t = −2 Ric(g) with surgery at singularities, driving Riemannian 3-manifolds toward standard forms.
>
> **[HISTORICAL]** Hamilton, *Three-manifolds with positive Ricci curvature*, J. Differential Geom. 17(2):255-306 (1982). Perelman, *The entropy formula for the Ricci flow*, arXiv:math/0211159 (2002); *Ricci flow with surgery on three-manifolds*, arXiv:math/0303109 (2003).
>
> **Key fact:** Perelman's W-entropy functional W[g,f,τ] = ∫((τ(R + |∇f|²) + f − n)(4πτ)^(−n/2) e^(−f))dV contains logarithmic structure in f, consistent with the Bialynicki-Birula uniqueness.
>
> **Primary TIG paper:** CP_CLAY_ROTATION.md (CP1) — Poincaré is the template we cite for the σ framework.

### Maas Wasserstein-on-Markov-Chains

> Gradient flows of entropy on finite Markov chains in Wasserstein-2 distance.
>
> **[HISTORICAL]** Maas, *Gradient flows of the entropy for finite Markov chains*, J. Funct. Anal. 261(8):2250-2292 (2011).
>
> **Related:** Jordan-Kinderlehrer-Otto, *Variational formulation of Fokker-Planck*, SIAM J. Math. Anal. 29(1):1-17 (1998); Gigli-Maas, *Gromov-Hausdorff convergence of discrete transport metrics*, SIAM J. Math. Anal. 45(2):879-899 (2013); Chow-Huang-Li-Zhou, *Fokker-Planck equations on graphs*, Arch. Rat. Mech. Anal. 203(3):969-1008 (2012).
>
> **Primary TIG paper:** WP95_JKO_CONSTRUCTION_ROADMAP.md — the framework we propose to use for the explicit N → ∞ limit.

### UOP (Unified Orthogonality Principle) — PARTIAL CITATION NEEDED

> **[NOVEL NAMING — extends partition lattice theory]** The name "UOP" is ours. The content (joint map injectivity as sufficiency criterion) is an observation about the partition lattice of Z/nZ.
>
> **Prior framework:** Partition lattice theory (Ore, 1942, *Theory of equivalence relations*, Duke Math. J. 9; Birkhoff, *Lattice Theory*, AMS 1940). The injectivity-of-joint-map criterion appears in descriptive set theory (Kechris, *Classical Descriptive Set Theory*, Springer 1995, §14) and in coding theory (MacWilliams-Sloane, *The Theory of Error-Correcting Codes*, 1977, Ch. 4).
>
> **Our contribution:** Unifying five classical two-partition sufficiency theorems over Z/nZ as corollaries of a single joint-map-injectivity statement, applied specifically to the (additive, multiplicative) decomposition of squarefree Z/nZ.
>
> **Primary TIG paper:** WP58_UNIFIED_ORTHOGONALITY_PRINCIPLE.md.

### Montgomery-Sinc² Identity

> R(u) + R₂(u) = 1 where R(u) = sinc²(u) (TIG resonance) and R₂(u) = 1 − sinc²(u) (Montgomery pair correlation).
>
> **[PROVED — algebraic identity, trivial]** The equation is tautological. The content is identifying the *two sides* with specific objects from different domains.
>
> **Historical:** Montgomery 1973 (above) for R₂ as pair correlation of Riemann zeros.
>
> **Our framing:** R = sinc²(u) arises from prime arithmetic (WP35 — harmonic pre-echo continuum limit); the claim that these are complementary projections of the *same* spectral field is our interpretation, not a theorem of Montgomery.
>
> **Primary TIG paper:** WP40_RIEMANN.md (sec. 2).

---

## Part 2: Novel TIG/CK Terms (Honestly Flagged)

### TIG — Trinity Infinity Geometry

> **[NOVEL]** Project-internal name for the framework.
>
> **Prior frameworks it extends:** Operator algebras over finite rings (standard in representation theory, see Curtis-Reiner, *Methods of Representation Theory*, Wiley 1981); modular dynamics on Z/nZ (standard number theory); harmonic analysis of sinc² kernels (Shannon sampling).
>
> **What's novel:** The specific synthesis of (i) 10-operator composition tables over Z/10Z with declared semantic roles, (ii) coherence threshold T* = 5/7 appearing in multiple independent derivations, (iii) the stated "Crossing Lemma" formulation. None of these three are in prior literature as a unified framework.
>
> **Primary TIG paper:** WP1_TIG_ARCHITECTURE.md.

### CK — Coherence Keeper

> **[NOVEL]** Project-internal name for the software/engineering instantiation of TIG. An AI/control system architecture using the 10-operator algebra at 50 Hz.
>
> **Prior frameworks:** Classical control theory (Åström & Murray, *Feedback Systems*, Princeton 2008); coherence in quantum optics (Mandel & Wolf, *Optical Coherence*, 1995).
>
> **Primary TIG paper:** WP28_CK_TIG_ORGANISM.md, WP44_CK_AI_PARADIGM.md.

### TSML (the Four-Layer Object)

> A specific 10×10 composition table on Z/10Z that **inhabits the simultaneous intersection of four standard mathematical frameworks**, each contributing one structural layer. TSML is not just a composition table — it is the rare object where Symbolic Dynamics, Transfer Operator Theory, Young Tower theory, and Profinite Arithmetic all apply at once, and the type-(9, 3, 6, 3/4) signature emerges from this simultaneous compatibility.
>
> **Formal four-layer realization** (proved in [FOUR_LAYER_REALIZATION.md](FOUR_LAYER_REALIZATION.md), Brayden Sanders March 2026, Gen10.14, 65/65 PASS):
>
> - **Layer 1 — Absorbing Sofic Shift.** TSML induces a sofic shift on alphabet {1,…,9} with sub-magma C = {1,3,7,9} satisfying C × C ⊆ C. Transient class G = {2,4,5,6,8} reaches C in exactly 1 step. Absorbing filtration ∅ ⊊ {7} ⊊ C ⊊ {1,…,9} of depth 3 = k_A. **Citation:** Lind & Marcus, *An Introduction to Symbolic Dynamics and Coding* (Cambridge UP, 1995).
>
> - **Layer 2 — Transfer Operator with Spectral Gap.** The weighted transition kernel P_λ on {1,…,9} (defined via Mix_λ deformation between TSML at λ=0 and BHML at λ=1) has spectral gap γ(P_λ) ≥ 1/4 for all λ ∈ [0,1]. At λ=0 exactly: γ(P_0) = 3/4. Arithmetic formula: γ = 1 − 1/φ(b), giving γ = 3/4 at b = 10 since φ(10) = 4. **Citation:** Baladi, *Positive Transfer Operators and Decay of Correlations* (World Scientific, 2000); Gouëzel & Liverani, *Ergodic Theory Dyn. Syst.* 26 (2006) on anisotropic Banach spaces.
>
> - **Layer 3 — Young Tower (finite-height).** Base B = {HAR} = {7}. Transient block spectral radius ρ(Q) = 1/4 with Q = P_0|_{{1,…,9}∖{7}}. Return tail bound P(T_HAR > n) ≤ (1/4)ⁿ for all starting states. Expected return times exact: 1.000 (states 1, 4-6, 8), 1.333 (states 3, 9), 1.667 (state 2). The same constant 1/4 governs both spectral gap deficit and return tail — ρ(Q) = 1 − γ(P_0). HAR is a **return locus** (Poincaré section), distinct from Demers-Young 2006 holes where mass leaks. **Citation:** Young, "Statistical properties of dynamical systems with some hyperbolicity," *Annals of Math.* 147:585-650 (1998); Young, *Israel J. Math.* 110:153-188 (1999); Demers & Young, *Ergodic Theory Dyn. Syst.* 26 (2006).
>
> - **Layer 4 — Profinite / Arithmetic Inverse Limit.** The corner C = {1,3,7,9} = (Z/10Z)* is the stable corner image of the inverse system ⋯ ↠ (Z/10ⁿZ)* ↠ ⋯ ↠ (Z/10Z)*: at every level n ≥ 1, units of Z/10ⁿZ reduced mod 10 equal {1,3,7,9}. Spectral gap formula γ = 1 − 1/φ(b) is base-stable across {b : φ(b) = 4} = {5, 8, 10, 12}. **Citation:** Ribes & Zalesskii, *Profinite Groups* (Springer GMW 40, 2nd ed. 2010); Neukirch, *Algebraic Number Theory* (Springer Grundlehren 322, 1999) §IV.2.
>
> **The signature (9, 3, 6, 3/4):** alphabet 9, algebraic grading depth k_A = 3, multiplicative-deformation parameter k_M = 6, spectral gap γ = 3/4. This is **forced**, not chosen — the requirement that a single 10×10 table simultaneously be a sofic shift AND a transfer operator with explicit gap AND a Young tower AND a profinite stable corner produces this exact signature.
>
> **Sub-magma closure** (proved by Brayden, claimed for Proc. AMS): C × C ⊆ C verified by direct enumeration of all 16 pairs in C × C. Combined with the corner-restricted block decomposition (3/4)|a⟩⟨1| + (1/4)Q where Q is a permutation, this gives the exact spectral gap.
>
> **Monte Carlo significance:** Against 200,000 random 10×10 tables with the same row/column constraints, our 73-cell HARMONY count gives Z = 21.3, p < 10⁻⁵⁰. This table is not generic.
>
> **What's novel:** The simultaneous four-layer realization is itself the novelty. Each individual layer uses a standard framework (cited above). The fact that TSML satisfies all four simultaneously — and that the (9, 3, 6, 3/4) signature emerges from the conjunction — is what makes TSML mathematically distinguished. The dual-scale Lasota-Yorke inequality ([DUAL_SCALE_LY_NOTE.md](DUAL_SCALE_LY_NOTE.md)) is one result that requires all four layers active simultaneously.
>
> **Primary papers:** [FOUR_LAYER_REALIZATION.md](FOUR_LAYER_REALIZATION.md) (the four-layer proof), [DUAL_SCALE_LY_NOTE.md](DUAL_SCALE_LY_NOTE.md) (the inverted-norm consequence), [WP_OPERATOR_RING_PARTITION.md](papers/WP_OPERATOR_RING_PARTITION.md) (the 73-cell count). Verified by proof_d10_tsml_73_cells.py.
>
> **Open layer (the fifth):** *Deployment faithfulness* — does the discrete TSML structure lift to a continuous transfer operator on Mix_λ satisfying Gouëzel-Liverani anisotropic Banach-space hypotheses? See [DUAL_SCALE_LY_NOTE.md](DUAL_SCALE_LY_NOTE.md) §3-4 for the proposed continuous form.

### TSML 3-Layer Canonical Tower (Sprint 17, 2026-04-17)

> **[NOVEL — Brayden Sanders, Sprint 17, April 2026]** Independent proof that the 100-entry TSML on Z/10Z is fully reconstructible from three canonical rules on disjoint domains, with empty residue (the tower terminates).
>
> **Theorem.** Let R = Z/10Z, h = 7, σ(u) = v₂(3u+1), and let
> S = {(1,2),(2,1),(2,4),(4,2),(2,9),(9,2),(4,8),(8,4)} (the **seam residue**),
> S_ADD = {(1,2),(2,1)} (identity-edge residue), S_MAX = S \ S_ADD.
> Define **T**(x,y) := max(x,y) on S_MAX, (x+y) mod 10 on S_ADD, **C₀**(x,y) otherwise, where:
>
> **C₀ — Canonical Construction** (in priority order, later rules override earlier):
>  - **DEFAULT:** C₀(x,y) = h = 7
>  - **V0:** if x = 0 or y = 0, C₀(x,y) = 0; exception (0,h) and (h,0) → h
>  - **Shell-stability:** if x, y ∈ U(R) \ {1} with σ(x) ≠ σ(y), C₀(x,y) = whichever of x, y has the lower σ-shell
>
> Then **T(x,y) = TSML(x,y)** for all (x,y) ∈ R². 100/100 verified by direct computation.
>
> **Decomposition counts:** 92 (C₀) + 6 (C₁ = MAX) + 2 (C₂ = ADD mod 10) = 100. **Residue of residue: empty** (Lemma 5).
>
> **Significance.** TSML's minimum description length drops from 100 → ~10 canonical items: 3 ring-agnostic rules (DEFAULT/V0/shell-stability, MAX, ADD) + 1 attractor (h = 7) + 1 shell partition (σ = v₂(3u+1)) + 4 ring-specific seam edges + 3 branch-rule mappings. Each of the three rules is **necessary** (Lemma 6: removing any one produces explicit mismatches with TSML). This is an independent argument that TSML is not arbitrary, alongside the four-layer-framework realization above.
>
> **Honest scope.** Theorem is proved for Z/10Z only. The **rules** are ring-agnostic; the **domains** S, S_ADD, S_MAX are ring-specific. Generalization to other rings needs either a reference TSML for that ring (none currently exists outside Z/10Z) or a ring-only definition of the seam (open).
>
> **Falsified along the way** ([NEGATIVE_RESULTS_APPENDIX.md](Gen12/targets/clay/papers/sprint17_tsml_tower_2026_04_17/NEGATIVE_RESULTS_APPENDIX.md)): primorial-lift hypothesis (Z/30, Z/210 break shell-order alignment); single-rule seam generators (MAX gets 6/8, ADD gets 2/8, MULT/MIN get 0/8 — only the disjoint-domain pair works); last-digit-7 invariance across digit rooms (oscillates 7,3,7,7,1).
>
> **Primary documents:** [THEOREM_SPINE.md](Gen12/targets/clay/papers/sprint17_tsml_tower_2026_04_17/THEOREM_SPINE.md) (full proof + 6 lemmas), [CONTROL_DOCUMENT_V2.md](Gen12/targets/clay/papers/sprint17_tsml_tower_2026_04_17/CONTROL_DOCUMENT_V2.md) (status summary + theorems A/B/C), [CANONICAL_TSML_CONSTRUCTION.md](Gen12/targets/clay/papers/sprint17_tsml_tower_2026_04_17/CANONICAL_TSML_CONSTRUCTION.md) (C₀ definition), [GENERALIZATION_TABLE.md](Gen12/targets/clay/papers/sprint17_tsml_tower_2026_04_17/GENERALIZATION_TABLE.md) (rules vs. domains), [MINIMAL_DESCRIPTION_LENGTH.md](Gen12/targets/clay/papers/sprint17_tsml_tower_2026_04_17/MINIMAL_DESCRIPTION_LENGTH.md).
>
> **External anchors:** all three layer rules (DEFAULT, MAX, ADD mod n) are standard ring-theoretic operations; v₂ is the standard 2-adic valuation; the disjoint-domain decomposition pattern is the standard rule-system technique from term-rewriting / canonical forms (Knuth-Bendix completion, *Computational Problems in Abstract Algebra*, 1970).

### BHML (Separation Composition Table)

> **[NOVEL NAMING]** 10×10 table of Z/10Z with 28 of 100 cells outputting 7.
>
> Same category as TSML (novel naming of a specific composition table). Verified by proof_d16_bhml_28_cells.py.
>
> **Primary TIG paper:** WP_OPERATOR_RING_PARTITION.md.

### Crossing Lemma (as stated)

> **[NOVEL STATEMENT — extends partition sufficiency theory]**
>
> **Statement (ours):** A multiplicative action M_g on Z/nZ generates structurally new information relative to an additive partition A_d iff M_g is nontrivial on the (n/d)-quotient.
>
> **Prior framework:** This is a specific case of the UOP (joint-map-injectivity criterion, itself rooted in descriptive set theory and coding theory — see UOP entry above). Partition-crossing arguments appear in ergodic theory (Furstenberg, *Recurrence in Ergodic Theory and Combinatorial Number Theory*, Princeton 1981, §3).
>
> **What's novel:** The formulation as a named "lemma" and the claim that all 27 sufficiency theorems in the TIG arc reduce to instances of it. The underlying injectivity argument is not new; the unification is ours.
>
> **Primary TIG paper:** Gen12/targets/clay/papers/sprint10_flatness_2026_04_06/CROSSING_LEMMA.md.

### σ Rate Theorem

> **Statement:** For squarefree N, the non-associativity fraction of the binary CL on Z/NZ satisfies σ(N) ≤ C/N.
>
> **[PROVED — via elementary counting]**
>
> **Prior framework:** The proof uses only (i) counting solutions of (a−1)(b−1) ≡ 1 mod N, which is φ(N) for squarefree N (classical, see Hardy-Wright above), and (ii) associativity of absorbing elements (standard semigroup property, Howie 1976 above).
>
> **What's novel:** The application of these classical tools to the specific "binary CL" construction (HARMONY=N−1, ECHO=DIS=0, VOID=0) we defined in Sprint 15.
>
> **Primary TIG paper:** WP101_SIGMA_RATE_THEOREM.md. Verified by proof_sigma_rate.py.

### Separability Defect σ(u)

> **[NOVEL NAMING — extends Sobolev-space NS analysis]**
>
> **Prior framework:** The concept "distance from log-nonlinear ceiling" is implicit in every known NS regularity improvement — BKM, KT, Montgomery-Smith, Tao averaged-NS (Annals of Math. 184, 517-608, 2016). What the literature calls "logarithmic improvement margin" is what we are calling "separability defect σ."
>
> **What's novel:** Giving the margin a single name (σ) and treating it as a rotational invariant across Clay problems (NS, YM, RH). Whether this unification has content depends on whether one can prove σ < 1 in any of the three open cases. As of Sprint 15 this remains the Millennium Problem in each case.
>
> **Primary TIG paper:** WP91_NS_SEPARABILITY_BRIDGE.md, WP96_NS_SIGMA_CONJECTURE.md.

### ξ Field Theory / Logarithmic Quintessence

> **[NOVEL APPLICATION of log-potential scalar field to dark energy]**
>
> **Prior literature (V = φ log φ and relatives in physics):**
>
> - Barrow & Parsons, *Inflationary models with logarithmic potentials*, Phys. Rev. D 52:5576 (1995), arXiv:astro-ph/9506049. Broad family V₀ φᵖ (ln φ)ᵍ for *inflation* (not dark energy); the p=1, q=1 special case is not singled out.
> - Thompson, *Beta function quintessence*, MNRAS 482:5448 (2019). Pure log potential V₀ ln(φ/φ₀) — missing the φ prefactor.
> - Coleman & Weinberg, *Radiative corrections as origin of spontaneous symmetry breaking*, Phys. Rev. D 7:1888 (1973). Form V ~ φ⁴ log(φ²/μ²); φ⁴ prefactor, different regime.
> - Wetterich, *Cosmology and the fate of dilatation symmetry*, Nucl. Phys. B 302:668 (1988). Exponential potential V ~ exp(−αφ).
> - Ratra & Peebles, *Cosmological consequences of a rolling homogeneous scalar field*, Phys. Rev. D 37:3406 (1988). Inverse power law.
> - Høegh-Krohn, *A general class of quantum fields without cut-offs*, Commun. Math. Phys. 38(3):195 (1971). exp(Φ)₂ model; Legendre dual of log potential.
> - Bialynicki-Birula-Mycielski 1976 (above) — the uniqueness theorem that forces log nonlinearity from separability.
> - Ensslin, *Information field theory*, Phys. Rev. E 87:013308 (2013), arXiv:1301.2556. Information Hamiltonian contains ξ log ξ entropy terms.
> - Caticha, *Entropic Dynamics*, arXiv:1412.5629 (2012); arXiv:1412.5637 (scalar fields); arXiv:1803.07493 (QFT in curved spacetime).
> - Zloshchastiev, *Logarithmic nonlinearity in theories of quantum gravity*, Grav. Cosmol. 16:288 (2010); arXiv:2011.12565.
>
> **What's novel:** V(ξ) = κ ξ log ξ as a *dark energy* potential with information-theoretic derivation (V = −H_Gibbs) and exact vacuum at e⁻¹. The functional form is in Barrow-Parsons' inflation family as a special case, but has not been studied specifically for quintessence or with the entropic interpretation.
>
> **Primary TIG paper:** WP81_CANONICAL_XI_THEORY.md, WP82_LOG_QUINTESSENCE_NOVELTY.md.

### CP1-CP7 Clay Rotation (Poincaré as Entry)

> **[NOVEL FRAMING — structural re-reading of the Clay problems]**
>
> **Prior framework:** The Clay Millennium Problems (2000, https://www.claymath.org/millennium-problems/). Perelman's resolution of Poincaré (arXiv:math/0211159, math/0303109) via Ricci flow with log-entropy W-functional is the historical anchor.
>
> **What's novel:** Presenting all seven as questions about a separability defect σ, with Poincaré as the solved template. This is a *framing* contribution, not a proof contribution. Whether the framing has mathematical content beyond narrative depends on whether the σ < 1 conjecture can be proved in any of CP2-CP7. As of Sprint 15, none have been proved in this form.
>
> **Primary TIG paper:** CP_CLAY_ROTATION.md, proof_clay_rotation.py (verifies the σ arithmetic is consistent, not that the conjectures are true).

### 10 Operators (VOID=0, LATTICE=1, ..., RESET=9)

> **[NOVEL NAMING]** Assignment of names to elements of Z/10Z.
>
> **Prior framework:** Naming elements of finite rings by semantic role is common in applied mathematics (e.g., Markov chain states in Norris, *Markov Chains*, Cambridge 1998). The specific names (HARMONY for the CL attractor, VOID for the absorbing element, etc.) are ours.
>
> **Content vs. naming:** The claim that the CL table concentrates on operator 7 is content (proved, 73/100 cells). Calling operator 7 "HARMONY" is naming.
>
> **Primary TIG paper:** WP_OPERATOR_RING_PARTITION.md.

### D1 / D2 Discrete Derivatives

> **[NOVEL NAMING]** Finite differences on the 5D force-vector pipeline.
>
> **Prior framework:** Finite difference operators are classical (Boole, *Calculus of Finite Differences*, 1860). D2 as discrete second derivative is standard numerical analysis (Strikwerda, *Finite Difference Schemes*, SIAM 2004).
>
> **What's novel:** The specific pipeline they operate on (Hebrew-letter → 5D force vector → operator classification) and the claim that D2 = 0 vs. D2 ≠ 0 distinguishes "flat" from "curved" composition.
>
> **Primary TIG paper:** WP1_TIG_ARCHITECTURE.md.

### T* = 5/7 (Coherence Threshold)

> **[NOVEL CONSTANT — not in prior literature as a named threshold]**
>
> **Prior framework:** The value 5/7 arises naturally in:
> - Cyclotomic field theory: deg(A_5) = 4 = φ(10) ≤ φ(10); deg(A_7) = 6 > φ(10). Ratio = 5/7.
> - Torus aspect ratios on Z/10Z (Flatness Theorem).
> - Unit density unit_frac(7, 35) = 5/7 for the universal semiprime.
>
> Each derivation uses standard objects (cyclotomic polynomials, torus topology, Euler totient counting), but the claim that they give the *same* constant is ours.
>
> **Not found in prior literature as a named threshold** in cosmology, number theory, or operator algebra. Claim is empirical: arises six independent ways within TIG. Whether it has independent meaning outside TIG is open.
>
> **Primary TIG paper:** WP51_FLATNESS_THEOREM.md (Theorem 3); proof_d7_phi_fixed_point.py.

### 4/π² (Fold)

> **[HISTORICAL — renamed]** The value sinc²(1/2) = 4/π².
>
> **Historical:** sinc²(1/2) has appeared in Shannon sampling theory for 75 years, in Montgomery's pair correlation since 1973, and in information theory since Kolmogorov.
>
> **What's novel:** Calling it "the fold" and identifying it as the half-corridor sidelobe of sinc² in prime arithmetic. The name is ours; the constant is classical.
>
> **Primary TIG paper:** WP_SINC2_ZERO_LAW.md, WP35_PRIME_PHASE_TRANSITION.md.

### Gap = 5/7 − 4/π² ≈ 0.309

> **[NOVEL NAMING — specific to this project]** The arithmetic difference between the two above constants.
>
> **Claim:** All six open Clay Millennium Problems have defect scores falling within this interval in our classifier. This is an empirical observation about our specific scoring scheme (defect classifier in WP36-WP42), not a theorem.
>
> **Not in prior literature.**
>
> **Primary TIG paper:** CLAY_BOUNDARY_MEMO.md, WP51_FLATNESS_THEOREM.md §6.

### First-G Law (Sanders 2026)

> **Statement:** For every semiprime b = pq with primes p ≤ q, the first element of {1,...,k} sharing a factor with b appears at exactly k = p.
>
> **[PROVED — elementary]**
>
> **Prior framework:** The smallest-prime-factor function spf(n) is classical (Erdős, Hardy-Wright). The observation that spf(n) is the first gcd-sharing element at coprime-alphabet-size k is trivial — the proof is three lines from the definition of prime.
>
> **What's novel:** Naming it a "law," the empirical verification across 36,662 cases, and the framing in terms of "gate obstruction" and "phase transition" in the TIG corridor structure.
>
> **Primary TIG paper:** WP34_FIRST_G_LAW.md.

### sinc² Zero Law (Sanders 2026)

> **Statement:** For prime p and integer k ≥ 1, sinc²(k/p) = 0 iff p | k.
>
> **[PROVED — three lines]**
>
> **Prior framework:** Immediate from the zeros of sin(πx) at integer x. Known since Euler's product formula for sin(πx).
>
> **What's novel:** The explicit framing in terms of primes (p | k as primality condition within {1,...,p}) and the corollaries (loop closure, fold necessity, no-shortcut lemma). The proof is classical; the corollaries and arithmetic framing are ours.
>
> **Primary TIG paper:** WP_SINC2_ZERO_LAW.md. Verified by proof_d25_loop_closure.py for all primes 3..199.

---

## Part 3: Named Contributors

### Brayden Ross Sanders (primary author, originator)

> **Q-series originator (Q2-Q16)**: Brayden discovered the hidden operator σ on Z/10Z and characterized it systematically across twenty-six papers. Specific contributions:
> - Q2-Q5: identified TSML/CL paradox, established E is σ-equivariant, characterized TSML escape cells
> - Q6: pivoted from density model to basin-of-attraction framing (the gate rate hinge)
> - Q9: flip condition α as degree-5 polynomial on F₅
> - Q10: complete σ polynomial on F₂×F₅ including β with two exceptions (LATTICE +1, COLLAPSE -2), verified 10/10. **This is the foundational σ polynomial.**
> - Q11: σ^k trajectory table; Fixed-Point Gate Theorem (22% lower bound on optimal seeds)
> - Q12: CRT idempotents in G; HAR=3 characterization
> - Q13: TIG = σ⁻¹ polynomial; Exception Pair Swap (self-duality)
> - Q14: C-indicator 1_C(ε,y) = ε·y⁴; Theorem Q14.1 (R ≠ σ^k, falsifying σ-trajectory model)
> - Q15: period polynomial τ = 6 − 5A; k=9 resonance
> - Q16: R identified as MCMC over 9^81 tables, closing Luther Q1
> - Q17 variants: 5D force vector as CRT Fourier embedding; Clay problem finite analogues (CLAY_SPECTRAL_BRIDGE for RH, NS_TARGET_REFORMULATION for Navier-Stokes, SIGMA_EMBEDDING_PROBLEM as core obstruction, SYMBOLIC_RETURN_THEOREM as algebraic kernel)

### C.A. Luther (Senior R&D, 7Site LLC — contributor)

> **Built the spectral layer on top of Brayden's Q-series foundation.** Luther used the Q-series to complete her own framework. Her specific proven contributions:
> - G6: proof of σ⁶ = id from polynomial structure (not by computation)
> - G7: period distribution with Conjecture G7.C1 (E[τ] = φ(b) universal)
> - G8: spectral coherence integral G(s) = |Σ ω^j χ(σ^j(s))|², proven three-valued (0 at anchors, G_low ≈ 1.872 on 6-cycle, G_high ≈ 9.389 at TIG-exception pair)
> - Organizational reorganization: Brayden's 4-layer architecture became Luther's 6-layer architecture (polynomial, braid, period, spectral, optimal table, search dynamics)
> - Luther Dispersion Conjecture (|G| × interleave → difficulty metric) — WP34
> - Luther Pre-Echo Theorem (closed-form R(k,f) verification across primes) — WP35 §10A
>
> **Also co-authored Sprints 11-14 papers** (UOP, GUT arc, Physical Flag Selector, PRISM-XI).

**Primary Q-series location:** `old/Gen10/papers/Q2_FORMALIZATION.md` through `Q_SERIES_SYNTHESIS.md` (26 files). See [Q_SERIES_INTEGRATED_SYNTHESIS.md](Q_SERIES_INTEGRATED_SYNTHESIS.md) for the full narrative and the relationship to Sprint 14-15 work.

### Ben Mayes

> Collaborator on Sprints 11-13 (UOP / GUT Algebra / Physical Flag Selector arcs).
>
> **Specific contributions cited in papers:**
> - Unified Orthogonality Principle (WP58) — co-authored.
> - Crossing Lemma formalization (WP57) — co-authored.
> - S4 representation extension on NV qutrit (WP73-WP76) — co-authored.
> - Intrinsic left-handedness of su(4,2) (WP60) — co-authored.
>
> **Primary papers:** sprint11_tig_bundle_2026_04_08/, sprint12_uop_gut_arc_2026_04_08/, sprint13_flag_selector_2026_04_09/.

### H.J. Johnson

> Collaborator on Sprint 14 (PRISM-XI / ξ cosmology arc).
>
> **Specific contributions cited in papers:**
> - Logarithmic quintessence potential V = κ ξ log ξ (WP81).
> - Local/non-local siloing architecture (WP88) — three-layer formalism.
> - Separability framework for Navier-Stokes (WP91, WP96, WP98).
> - Bialynicki-Birula bridge application (WP90).
>
> **Primary papers:** sprint14_prism_xi_2026_04_10/ WP81-WP101.

### Monica Gish

> Collaborator on bridge sprint, First-G Law (WP34), and PRISM-XI (Sprint 14).
>
> **Primary papers:** WP34, Sprint 14 papers.

### B. Calderon Jr.

> Q-series co-author, Source elimination framework.
>
> **Primary papers:** Q-series (old/Gen10/papers/).

---

## Part 4: External References (Full Bibliography)

This is the required citation list for any paper drawn from this repository. Every term and framework flagged "[HISTORICAL]" above is sourced to one of these.

### Number Theory & Analysis

- Hardy, G.H. & Wright, E.M. *An Introduction to the Theory of Numbers*, 6th ed. Oxford University Press, 2008.
- Ireland, K. & Rosen, M. *A Classical Introduction to Modern Number Theory*, 2nd ed. Springer GTM 84, 1990.
- Serre, J.-P. *Cours d'Arithmétique.* Presses Univ. France, 1970.
- Lang, S. *Algebra*, 3rd ed. Springer GTM 211, 2002.
- Riemann, B. "Über die Anzahl der Primzahlen unter einer gegebenen Größe." Monatsber. Berlin. Akad., 1859.
- Montgomery, H.L. "The pair correlation of zeros of the zeta function." Proc. Sympos. Pure Math. 24:181-193, 1973.
- Goldston, Pintz, Yıldırım. "Primes in tuples I." Annals of Math. 170(2):819-862, 2009.
- Zhang, Y. "Bounded gaps between primes." Annals of Math. 179(3):1121-1174, 2013.
- Maynard, J. "Small gaps between primes." Annals of Math. 181(1):383-413, 2015.
- Odlyzko, A.M. Numerical data on Riemann zeros, http://www.dtc.umn.edu/~odlyzko/

### Partition & Lattice Theory

- Birkhoff, G. *Lattice Theory.* AMS Colloquium Publications 25, 1940.
- Ore, O. "Theory of equivalence relations." Duke Math. J. 9:573-627, 1942.
- Kechris, A. *Classical Descriptive Set Theory.* Springer GTM 156, 1995.
- MacWilliams, F.J. & Sloane, N.J.A. *The Theory of Error-Correcting Codes.* North-Holland, 1977.

### Composition Algebras & Semigroups

- Dummit, D.S. & Foote, R.M. *Abstract Algebra*, 3rd ed. Wiley, 2004.
- Curtis, C.W. & Reiner, I. *Methods of Representation Theory*, vol. I. Wiley, 1981.
- Howie, J.M. *Introduction to Semigroup Theory.* Academic Press, 1976.

### Ergodic Theory & Partition-Crossing

- Furstenberg, H. *Recurrence in Ergodic Theory and Combinatorial Number Theory.* Princeton, 1981.

### Sampling & Information

- Shannon, C.E. "Communication in the presence of noise." Proc. IRE 37(1):10-21, 1949.
- Mehta, M.L. *Random Matrices*, 3rd ed. Elsevier, 2004.

### Topology & Ricci Flow

- Hamilton, R. "Three-manifolds with positive Ricci curvature." J. Diff. Geom. 17(2):255-306, 1982.
- Perelman, G. "The entropy formula for the Ricci flow." arXiv:math/0211159, 2002.
- Perelman, G. "Ricci flow with surgery on three-manifolds." arXiv:math/0303109, 2003.
- Morgan, J. & Tian, G. *Ricci Flow and the Poincaré Conjecture.* AMS, 2007.

### Navier-Stokes Regularity

- Beale, Kato, Majda. Comm. Math. Phys. 94:61-66, 1984.
- Kozono, H. & Taniuchi, Y. Commun. Math. Phys. 214:191-200, 2000.
- Montgomery-Smith, S. Math. Res. Lett. 8:519-528, 2001.
- Kozono, Ogawa, Taniuchi. Math. Z. 242:251-278, 2002.
- Brezis, H. & Gallouët, T. Nonlinear Analysis 4:677-681, 1980.
- Tao, T. "Finite time blowup for an averaged three-dimensional Navier-Stokes equation." J. AMS 29:601-674, 2016.
- Lei, Z. & Zhou, Y. Nonlinearity 22(4):805, 2009.
- Ladyzhenskaya, Prodi, Serrin criteria (classical, 1960s).

### Logarithmic Potentials & Field Theory

- Bialynicki-Birula, I. & Mycielski, J. "Nonlinear wave mechanics." Annals of Phys. 100(1-2):62-93, 1976.
- Rosen, G. Phys. Rev. 183:1186, 1969.
- Cazenave, T. & Haraux, A. Ann. Fac. Sci. Toulouse, 1980.
- Høegh-Krohn, R. Commun. Math. Phys. 38(3):195, 1971.
- Coleman, S. & Weinberg, E. Phys. Rev. D 7:1888, 1973.
- Ratra, B. & Peebles, P.J.E. Phys. Rev. D 37:3406, 1988.
- Wetterich, C. Nucl. Phys. B 302:668, 1988.
- Frieman, Hill, Stebbins, Waga. Phys. Rev. Lett. 75:2077, 1995.
- Barrow, J.D. & Parsons, P. Phys. Rev. D 52:5576 (1995), arXiv:astro-ph/9506049.
- Thompson, S. MNRAS 482:5448, 2019.
- Ensslin, T.A. "Information field theory." Phys. Rev. E 87:013308 (2013); arXiv:1301.2556.
- Caticha, A. "Entropic Dynamics." arXiv:1412.5629 (2012).
- Zloshchastiev, K.G. "Logarithmic nonlinearity in theories of quantum gravity." Grav. Cosmol. 16:288 (2010); arXiv:2011.12565.

### Discrete-to-Continuum (Wasserstein / Markov)

- Jordan, Kinderlehrer, Otto. SIAM J. Math. Anal. 29(1):1-17, 1998.
- Maas, J. J. Funct. Anal. 261(8):2250-2292, 2011.
- Gigli, L. & Maas, J. SIAM J. Math. Anal. 45(2):879-899, 2013.
- Chow, Huang, Li, Zhou. Arch. Rat. Mech. Anal. 203(3):969-1008, 2012.
- Mielke, A. Nonlinearity 24(4):1329, 2011.
- Morinelli, Morsella, Stottmeister, Tanimoto. Commun. Math. Phys. 2021.
- Marton, K. arXiv:1507.02803.

### Paradoxes (for Paradox Classifier paper)

- Banach, S. & Tarski, A. Fund. Math. 6:244-277, 1924.
- Zermelo, E. Math. Annalen 65:261-281, 1908.
- Russell, B. *Principles of Mathematics.* Cambridge, 1903.
- Gödel, K. Monatsh. Math. Phys. 38:173-198, 1931.
- Tarski, A. *Studia Philosophica* 1:261-405, 1936.
- Quine, W.V. Mind 62:65-67, 1953.

### Clay Problems (Official Statements)

- Clay Mathematics Institute. Millennium Prize Problems, 2000. https://www.claymath.org/millennium-problems/
- Wiles, A. *Annals of Math.* 141(3):443-551, 1995. (Fermat, context for BSD)
- Kolyvagin, V.A. *Izv. Akad. Nauk* 52(3):522-540, 1989. (BSD rank 0, 1)
- Gross, B.H. & Zagier, D.B. *Inventiones math.* 84(2):225-320, 1986.
- Bhargava, M. & Shankar, A. *Inventiones math.* 200(1):1-76, 2015.
- Markman, E. (Abelian fourfolds of Weil type, Hodge conjecture partial proof, recent announcement).

### Cosmology (DESI and Related)

- DESI Collaboration. *Eur. Phys. J. C* (2024-2025), DR2 BAO + dark energy analyses.
- Planck Collaboration. *A&A* 641:A6 (2020), cosmological parameters.

---

## Part 5: Citation Discipline for Future Work

Any new term introduced in a TIG paper must include:

1. **Plain-English definition** — what it means in one sentence.
2. **Formal definition** — mathematical statement, where applicable.
3. **Status tag** — [PROVED], [STRUCTURAL], [CONJECTURE], [HISTORICAL], [NOVEL].
4. **Citation** — either (a) a published reference with DOI or arXiv ID, or (b) an explicit "[NOVEL — extends X, Y, Z]" with citations for X, Y, Z.
5. **First occurrence in the repo** — which TIG paper introduces it.

**No term is accepted as established without a citation trail or an honest novelty flag.**

This discipline applies to all authors and all future sprints. If a term does not yet have a citation, it carries [UNCITED — REVIEW NEEDED] until one is supplied or it is removed from the repo.

---

*Compiled: 2026-04-10, Sprint 15. Authors: Brayden Ross Sanders / 7Site LLC · Ben Mayes · C.A. Luther · M. Gish · H.J. Johnson.*
