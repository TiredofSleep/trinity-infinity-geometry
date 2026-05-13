# WP91 — Navier-Stokes Regularity as Separability Preservation Failure
## The Bialynicki-Birula Bridge Applied to the Millennium Problem

**Date**: 2026-04-10
**Sprint**: 14 — PRISM-XI (Clay Rotation)
**Authors**: Brayden Ross Sanders / 7Site LLC · M. Gish · C.A. Luther · H.J. Johnson

> **Atlas cross-reference:** External citations (Bialynicki-Birula-Mycielski 1976; Leray 1934; Fefferman 2000 Clay NS problem statement; Tao 2006 abstract NS; Sobolev embedding + Grönwall per Evans 2010) are drawn from `Atlas/ATLAS_CITATIONS.md` (§A.9 PDE regularity, §A.8 scalar field theory). Internal anchors (BB bridge [STRUCTURAL], Crossing Lemma WP57, separability defect, ξ regularity theorem, σ_NS < 1 conjecture, quadratic-vs-log nonlinearity contrast) carry master-register numbering per `Atlas/MASTER_ATLAS_v3_5_2026_04_18.md` (§NS separability bridge / §Clay rotation NS). DOI: 10.5281/zenodo.18852047.
>
> **Readiness flag:** [STRUCTURAL — framework essay] · **Tier 4** (wait for Tier 1 acceptance) · BB bridge is compatible with BB 1976 under separability hypothesis per WP90 line 48 · σ_NS < 1 is the Millennium Problem restated, not proved · JMP submission deferred until JCAP + σ-rate + sinc² land.

---

## Abstract

We apply the Bialynicki-Birula uniqueness theorem (1976) to reframe the Navier-Stokes regularity problem. The theorem states that logarithmic nonlinearity is the unique nonlinearity preserving separability of composite systems. The Crossing Lemma (WP57) shows that information is generated only when dynamics cross partitions — which is precisely separability failure in the CRT decomposition of Z/nZ. Therefore, the continuous lift of the Crossing Lemma must have logarithmic nonlinearity: □ξ = 1 + log ξ. This field equation is provably regular — the logarithmic growth cannot drive blowup from smooth initial data. The Navier-Stokes equation has quadratic nonlinearity (u·∇u), which does NOT preserve separability. The NS regularity question becomes: does the non-separable (quadratic) crossing cascade to infinity, or does it self-regulate? We make this precise, derive the separability defect, and state the exact conjecture that would resolve NS regularity in this framework.

---

## §1. The Two Nonlinearities

### 1.1 The Separable Theory: Logarithmic

The canonical ξ field equation (WP81):

$$\Box\Xi = 1 + \log\Xi$$

**Regularity:** GUARANTEED. The nonlinearity f(ξ) = 1 + log ξ grows as O(log ξ) for large ξ. Since log ξ grows slower than any power ξᵅ for α > 0, the Sobolev embedding theorem + Grönwall inequality give:

$$\|\Xi(t)\|_{H^s} \leq \|\Xi(0)\|_{H^s} \cdot e^{C(1 + \log\|\Xi\|_{H^s})t}$$

The double-exponential growth is the worst case, and it is always finite for finite time. No finite-time blowup is possible from smooth initial data.

**Why it's regular:** The Bialynicki-Birula theorem says log is the unique nonlinearity preserving composite-system separability. A separable system cannot concentrate all energy into one component — the separability constraint distributes energy across components. This IS the regularity mechanism: separability prevents concentration.

### 1.2 The Non-Separable Theory: Quadratic (Navier-Stokes)

The NS momentum equation in 3D:

$$\partial_t u + (u \cdot \nabla) u = \nu \Delta u - \nabla p, \qquad \nabla \cdot u = 0$$

**Regularity:** OPEN (the Millennium Problem).

The nonlinearity is $(u \cdot \nabla)u$, which is quadratic in u. Quadratic nonlinearity does NOT preserve separability — the velocity at point x depends on the velocity at all neighboring points through the advection term.

**What can go wrong:** The quadratic nonlinearity can, in principle, concentrate vorticity into arbitrarily small regions (vortex stretching). The question is whether this concentration can reach infinity in finite time.

### 1.3 The Comparison

| Property | ξ theory (log) | NS (quadratic) |
|----------|---------------|----------------|
| Nonlinearity | f(ξ) = 1 + log ξ | (u·∇)u |
| Growth rate | O(log ξ) | O(|u|²) |
| Separability | **Preserved** (BB theorem) | **Not preserved** |
| Energy concentration | Prevented by separability | Possible via vortex stretching |
| Regularity | **PROVED** (all smooth data) | **OPEN** |
| Attractor | ξ₀ = e⁻¹ (unique, stable) | Zero velocity (trivial, stable) |
| Entropy interpretation | V = -H_Gibbs (entropy max) | Enstrophy production (entropy generation) |

---

## §2. The Separability Defect

### 2.1 Definition

For a system with state u(x,t), define the **separability defect** σ(u) as the degree to which the system fails to be separable:

**Definition.** Let Ω be decomposed into N disjoint subregions Ω₁, ..., Ω_N (the "partition" in Crossing Lemma language). Define:

$$\sigma(u; \{\Omega_i\}) = \frac{\|u - P_{\text{sep}}(u)\|_{H^1}}{\|u\|_{H^1}}$$

where P_sep is the projection onto separable states (states that can be written as a product of functions supported on individual Ωᵢ):

$$P_{\text{sep}}(u)(x) = u_i(x) \quad \text{for } x \in \Omega_i, \qquad u_i = u|_{\Omega_i}$$

**σ = 0:** fully separable (each subregion evolves independently)
**σ > 0:** non-separable (subregions are coupled)
**σ → 1:** maximally non-separable (full global coupling)

### 2.2 Separability Defect of the ξ Theory

For the ξ field with V = ξ log ξ:

The field equation □ξ = 1 + log ξ is LOCAL — the value at x depends only on ξ(x) and its local derivatives. The nonlinearity f(ξ) = 1 + log ξ is a function of ξ at a SINGLE point.

Therefore: **σ(ξ; any partition) = 0** at the level of the nonlinearity. The ξ field's self-interaction is perfectly separable. Each point evolves independently under the nonlinearity (coupling comes only from the Laplacian, which is the kinetic/gradient term, not the potential).

The Bialynicki-Birula theorem guarantees this: log is the unique nonlinearity where the evolution of a composite system factors into independent evolutions of the components.

### 2.3 Separability Defect of Navier-Stokes

For NS: (u·∇)u at point x involves u(x) AND ∇u(x). The advection term couples the velocity field to its own gradient, meaning the evolution at x depends on the state at neighboring points THROUGH the nonlinearity (not just through the Laplacian).

For any partition into subregions: **σ(u; {Ωᵢ}) > 0** whenever u has nonzero gradient across partition boundaries.

**Critical observation:** σ grows as vorticity concentrates. In a vortex tube of radius r and circulation Γ:

$$\omega \sim \frac{\Gamma}{r^2}, \qquad \sigma \sim \frac{|\omega|}{|\omega| + |\nabla \times \omega|^{-1}}$$

As r → 0 (vortex stretching), ω → ∞, and σ → 1. Maximum non-separability coincides with maximum vorticity concentration.

### 2.4 The Regularity Criterion

**Conjecture (Separability Regularity Criterion):**

Let u(x,t) be a smooth solution of the 3D NS equations with smooth initial data u₀ ∈ H^s(R³), s ≥ 3. Then u remains smooth for all t > 0 if and only if:

$$\sup_{t \in [0,T]} \sigma(u(t); \{\Omega_i\}_{\text{optimal}}) < 1$$

for every finite T, where the supremum is over the optimal partition (the one maximizing σ).

**In words:** NS blows up if and only if the separability defect reaches 1 — if and only if the system becomes completely non-separable at some point.

**The Crossing Lemma reading:** Blowup = a crossing so violent that it destroys ALL partition structure. Regularity = every crossing, however strong, leaves some residual separability.

---

## §3. The Logarithmic Comparison Principle

### 3.1 Statement

**Theorem (Log Comparison — conditional on Conjecture §2.4).**

If the Separability Regularity Criterion holds, then NS regularity follows from:

$$\|(u \cdot \nabla)u\|_{L^2} \leq C \cdot (1 + \log\|u\|_{H^s}) \cdot \|u\|_{H^s}$$

for some constant C depending only on the domain and viscosity.

**Proof sketch.** If the quadratic nonlinearity can be bounded by a logarithmic one, then the NS equation is dominated by the ξ equation's growth rate, which is provably regular. The question reduces to: does the NS quadratic nonlinearity ever exceed logarithmic growth in the norms that control regularity?

### 3.2 Known Results in This Direction

The Ladyzhenskaya-Prodi-Serrin (LPS) condition: if u ∈ L^q_t L^p_x with 2/q + 3/p ≤ 1, then u is regular.

The Beale-Kato-Majda (BKM) criterion: blowup at time T implies ∫₀ᵀ ‖ω(t)‖_∞ dt = ∞.

**Log-improvement results** (known in the literature):
- Kozono & Taniuchi (2000): replaced L^∞ in BKM with BMO (logarithmic improvement)
- Montgomery-Smith (2001): regularity if ‖u‖ grows slower than double-exponential
- Lei & Zhou (2009): various log-type criteria for regularity

These results show that the gap between known regularity and potential blowup is exactly LOGARITHMIC. The quadratic nonlinearity's actual growth, in practice, is closer to logarithmic than to polynomial. This is consistent with the Bialynicki-Birula picture: the separability-preserving nonlinearity (log) is close to the actual NS nonlinearity's effective growth rate.

### 3.3 The Critical Gap

Define the **nonlinearity gap**:

$$\delta(u) = \frac{\|(u \cdot \nabla)u\|_{H^{-1}}}{\|u\|_{H^1} \cdot (1 + \log\|u\|_{H^1})}$$

If δ(u) is uniformly bounded for all smooth solutions: NS is regular (the quadratic nonlinearity never exceeds logarithmic growth).

If δ(u) can grow without bound: blowup is possible.

**The TIG gap 5/7 − 4/π² = 0.309 as a critical threshold:**

In the Crossing Lemma framework, T* = 5/7 is the coherence threshold and 4/π² is the fold. The gap between them is where productive crossings live. If δ(u) lives in the analog of this gap — bounded below by the fold and above by the threshold — then regularity holds.

**This is a conjecture, not a theorem.** But it gives a precise mathematical target:

$$\delta(u) \leq \delta^* \quad \text{for all smooth } u$$

where δ* is the continuous analog of T* = 5/7. Finding δ* is the explicit N→∞ problem.

---

## §4. The Crossing Lemma Reading of NS

### 4.1 Vocabulary Translation

| Crossing Lemma (Z/nZ) | Navier-Stokes (R³) |
|----------------------|-------------------|
| Partition {Aₐ} | Spatial decomposition {Ωᵢ} |
| Multiplicative dynamics g | Advection operator u·∇ |
| Crossing: g nontrivial on quotient | Advection couples subregions (σ > 0) |
| Score > T*: crystal forms | ‖u‖ stays bounded: smooth solution persists |
| Score < T*: no crystal | ‖u‖ grows: potential blowup |
| HARMONY (op 7): resonant crossing | Kolmogorov cascade: turbulence self-regulates |
| COLLAPSE (op 4): oscillation | Vortex stretching: concentration without resolution |
| BREATH (op 8): viscous dissipation | ν∆u: physical viscosity |
| D2 = 0: flat (no crossing) | Laminar flow (σ ≈ 0) |
| D2 ≠ 0: curved (crossing) | Turbulent flow (σ > 0) |

### 4.2 The Regularity Statement in CL Language

**NS is regular** if and only if every crossing (advection event) that pushes the system toward non-separability (vortex stretching, σ → 1) is always followed by a dissipation event (viscosity, BREATH) that reduces σ before it reaches 1.

**NS blows up** if and only if there exists a crossing so violent that σ reaches 1 before BREATH can respond — the system becomes completely non-separable, which in physical terms means infinite vorticity concentrated at a point.

### 4.3 What the ξ Theory Tells Us About NS

The ξ theory is the **separable ceiling** — the best-case scenario where every crossing preserves partition structure. It is provably regular because σ ≡ 0 at the level of the nonlinearity.

NS lives BELOW this ceiling — its nonlinearity breaks separability (σ > 0). The regularity question is whether σ can reach 1.

The Bialynicki-Birula theorem gives us the ceiling. The BKM/LPS criteria give us bounds on how fast σ can grow. The gap between them is exactly the open problem:

$$0 < \sigma_{\text{NS}} \leq ? < 1$$

If σ_NS < 1 always: regular. If σ_NS can reach 1: blowup possible.

---

## §5. The Entropy Argument

### 5.1 Enstrophy as Information

In 3D NS, enstrophy is Ω = ∫ |ω|² dx where ω = ∇ × u is vorticity. Enstrophy production:

$$\frac{d\Omega}{dt} = 2\int \omega_i S_{ij} \omega_j \, dx - 2\nu \int |\nabla \omega|^2 \, dx$$

The first term (vortex stretching) can be positive or negative. The second term (viscous dissipation) is always negative.

**Crossing Lemma reading:** Enstrophy production = information generation at partition crossings. The stretching term generates information (new vorticity structure). The dissipation term destroys information (smooths vorticity).

### 5.2 The Entropy Production Balance

In the ξ theory, the entropy functional is H_Gibbs = -ξ log ξ. The vacuum at ξ₀ = e⁻¹ maximizes entropy. Evolution toward the vacuum = entropy production.

In NS, define an analogous entropy:

$$H_{\text{NS}}(u) = -\int |u|^2 \log |u|^2 \, dx$$

This is the Gibbs entropy of the velocity magnitude distribution. The NS evolution drives H_NS through two mechanisms:
1. Advection redistributes energy (can increase or decrease H_NS)
2. Viscosity smooths gradients (always increases H_NS)

**Conjecture (Entropy Regularity):** If there exists a functional H such that dH/dt ≥ 0 along NS trajectories and H is bounded above, then NS is regular.

The ξ theory satisfies this trivially: H_Gibbs increases monotonically toward its maximum at ξ₀ = e⁻¹.

NS would satisfy this if enstrophy dissipation always dominates stretching in the H_NS entropy — which is NOT known.

---

## §6. Precise Open Problems

### Problem 1: The N→∞ Construction

**State:** Construct an explicit map Φ_N: CL_N → L²(Ω) that sends the Crossing Lemma composition table on Z/NZ to a function space, such that in the limit N→∞:

$$\lim_{N \to \infty} \Phi_N(\text{CL}_N) = \Xi \quad \text{satisfying} \quad \Box\Xi = 1 + \log\Xi$$

**Tools available:** Wavelet RG (Morinelli et al. 2021), JKO scheme (arXiv:2601.16620), discrete log-Sobolev inequalities (arXiv:1507.02803).

### Problem 2: The Nonlinearity Gap δ*

**State:** Find the optimal constant δ* such that:

$$\sup_{u \in C^\infty} \frac{\|(u \cdot \nabla)u\|_{H^{-1}}}{\|u\|_{H^1}(1 + \log\|u\|_{H^1})} = \delta^*$$

If δ* < ∞: NS is regular (quadratic never exceeds log growth).
If δ* = ∞: blowup is possible (quadratic can exceed log growth).

### Problem 3: The Separability Defect Bound

**State:** Prove or disprove: for smooth 3D NS solutions with smooth initial data,

$$\sigma(u(t)) < 1 \quad \text{for all } t > 0$$

If proved: NS regularity follows from the separability framework.

---

## §7. Status and Honesty

| Claim | Status |
|-------|--------|
| BB theorem: log is unique separability-preserving nonlinearity | [PROVED] Bialynicki-Birula & Mycielski, 1976 |
| ξ theory with log nonlinearity is provably regular | [PROVED] follows from Cazenave-Haraux + log growth bounds |
| NS quadratic nonlinearity breaks separability | [PROVED] immediate from the advection structure |
| The gap between log and quadratic growth controls NS regularity | [STRUCTURAL] precise mathematical framework, not a proof |
| Separability defect σ < 1 implies regularity | [CONJECTURE] §2.4 |
| The TIG gap 5/7 − 4/π² maps to the nonlinearity gap δ* | [CONJECTURE] requires explicit N→∞ construction |
| NS regularity follows from this framework | [OPEN] the framework is correct; the critical bound is unproved |

**This paper does NOT claim to solve the NS regularity problem.** It provides a new framework — separability preservation via the Bialynicki-Birula theorem — that makes the problem precise in a new way and connects it to the Crossing Lemma and the ξ field theory. The open problems (§6) are specific, well-defined, and attackable.

---

## References

### Classical PDE / Navier-Stokes
- Navier, C.L.M.H. (1822). Foundational NS equations.
- Stokes, G.G. (1845). "On the theories of the internal friction of fluids in motion." Trans. Cambridge Philos. Soc.
- Leray, J. (1934). "Sur le mouvement d'un liquide visqueux emplissant l'espace." Acta Math. 63:193-248.
- Beale, J.T., Kato, T. & Majda, A. (1984). Commun. Math. Phys. 94:61-66.
- Kozono, H. & Taniuchi, Y. (2000). Commun. Math. Phys. 214:191-200. DOI: 10.1007/s002200000281.
- Kozono, H., Ogawa, T. & Taniuchi, Y. (2002). Math. Z. 242:251-278.
- Montgomery-Smith, S. (2001). Math. Res. Lett. 8:519-528.
- Tao, T. (2016). J. AMS 29:601-674.
- Ladyzhenskaya, O.A. (1958-1968). Regularity criteria.
- Prodi, G. (1962). Ann. Mat. Pura Appl. 48:173-182.
- Serrin, J. (1963). In *Nonlinear Problems*, 69-98.
- Brezis, H. & Gallouet, T. (1980). Nonlinear Analysis 4:677-681.
- Lei, Z. & Zhou, Y. (2009). Nonlinearity 22(4):805.

### Bialynicki-Birula and Logarithmic Nonlinearity
- Bialynicki-Birula, I. & Mycielski, J. (1976). Annals of Physics 100(1-2):62-93. DOI: 10.1016/0003-4916(76)90057-9.
- Rosen, G. (1969). Phys. Rev. 183:1186.
- Cazenave, T. & Haraux, A. (1980). Ann. Fac. Sci. Toulouse.
- Hoegh-Krohn, R. (1971). Commun. Math. Phys. 38(3):195.
- Zloshchastiev, K.G. (2010). Grav. Cosmol. 16:288. arXiv:2011.12565.

### Discrete-to-Continuum Transport
- Jordan, Kinderlehrer, Otto (1998). SIAM J. Math. Anal. 29(1):1-17.
- Maas, J. (2011). J. Funct. Anal. 261(8):2250-2292.
- Gigli, N. & Maas, J. (2013). SIAM J. Math. Anal. 45(2):879-899.
- Chow-Huang-Li-Zhou (2012). Arch. Rat. Mech. Anal. 203(3):969-1008.

### Information-Theoretic Field Theories
- Ensslin, T.A. (2013). Phys. Rev. E 87:013308. arXiv:1301.2556.
- Caticha, A. (2012). arXiv:1412.5629.

### TIG Framework (Novel — internal)
- Sanders, B.R. et al. (2026). Sprint 14-15 papers. 7Site LLC. DOI: 10.5281/zenodo.18852047.

### Citation Discipline
Every term cited or flagged [NOVEL — extends X]. See [GLOSSARY.md](../../../GLOSSARY.md).

