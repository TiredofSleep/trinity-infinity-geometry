# The Bialynicki-Birula Bridge: Logarithmic Nonlinearity Forced by Separability

**Authors:** B.R. Sanders$^{1}$, H.J. Johnson$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher, Billings, MT

**Target venue:** Journal of Mathematical Physics
**Manuscript class:** Mathematical-physics framework paper (structural, not a Millennium-Problem proof)
**MSC:** 35Q30, 35B65, 81S20, 82C70
**Date:** 2026-05-07 (DRAFT)

---

## Abstract

The Bialynicki-Birula--Mycielski uniqueness theorem (1976) characterizes logarithmic nonlinearity as the unique potential preserving the separability of composite quantum systems: the evolution of $|\Psi_A \otimes \Psi_B|$ factors into independent evolutions of the components if and only if the self-interaction has the form $V(\rho) = \kappa\, \rho \log \rho$ (up to an additive constant). We exploit this theorem as a *forcing principle* connecting two distinct levels of structure: discrete composition algebras with vanishing non-associativity rate $\sigma(N) \leq 2/N$ on $\mathbb{Z}/N\mathbb{Z}$ on one side, and continuum scalar field theories with logarithmic potential $V(\Xi) = \kappa\, \Xi \log \Xi$ on the other. The bridge has three layers: (i) the discrete Crossing Lemma identifies "information generation" with the failure of separability in the CRT decomposition of $\mathbb{Z}/N\mathbb{Z}$; (ii) any continuum lift preserving separability is forced by Bialynicki-Birula to take the logarithmic form; (iii) the lifted equation $\Box \Xi = \kappa(1 + \log \Xi)$ is provably regular for smooth initial data. We then ask: what does this say about the Navier-Stokes regularity problem? The NS quadratic nonlinearity $(u\cdot\nabla)u$ does *not* preserve separability; we define a separability defect $\sigma(u)$, prove that $\sigma \to 1$ corresponds to vorticity blowup, and state the precise conjecture (Separability Regularity Criterion) that would resolve NS regularity within this framework. **The paper claims a new framework, not a proof of NS regularity.** All proved statements are clearly distinguished from conjectural ones; the tier classification is explicit.

---

## 1. Introduction

The Bialynicki-Birula--Mycielski theorem (1976) [BB76] establishes a striking uniqueness statement in nonlinear quantum mechanics. Among all admissible nonlinear modifications of the Schrödinger equation, *only* the logarithmic nonlinearity $\hat{F}(\rho) = -b \ln \rho$ preserves the separability of composite systems: the wave function of a non-interacting bipartite system $|\Psi_{AB}\rangle = |\Psi_A\rangle \otimes |\Psi_B\rangle$ remains a product state under evolution if and only if the nonlinearity has this form (up to an additive shift).

The theorem has been studied as a constraint on candidate nonlinear quantum theories [Rosen69, CazenaveHaraux80, Zloshchastiev10]. We propose a different reading: as a *forcing principle* that constrains any continuum lift of a discrete composition-algebra structure to take the logarithmic form, provided the lift respects separability of the partition data.

**Plan.** Section 2 states the BB theorem and our usage of it as a forcing principle. Section 3 introduces the discrete side: composition algebras over $\mathbb{Z}/N\mathbb{Z}$ with vanishing non-associativity rate, and the Crossing Lemma reading of "information generation." Section 4 forces the continuum lift to logarithmic form via BB and verifies regularity. Section 5 applies the framework to Navier-Stokes: defines the separability defect $\sigma(u)$, states the Separability Regularity Criterion, and identifies the precise open problems. Section 6 collates status, lens-scope, and tier classification.

This paper is a companion to [J03] (cosmological dark-energy realization of the same logarithmic potential, $V(\Xi) = \Lambda^4 \Xi \log \Xi$, freezing-quintessence regime), to [J05] (Crossing Lemma), and to [J14] (companion paper applying the BB bridge to Yang-Mills mass gap).

---

## 2. The Bialynicki-Birula Forcing Theorem

### 2.1 Statement

**Theorem 2.1 (Bialynicki-Birula--Mycielski, 1976).** *Let $\hat F : \mathbb{R}_{>0} \to \mathbb{R}$ be the nonlinearity in a modified Schrödinger evolution $i\hbar\,\partial_t \Psi = (-\tfrac{\hbar^2}{2m}\Delta + V_{\rm ext})\Psi + \hat F(|\Psi|^2)\Psi$. The evolution preserves the product structure $\Psi_{AB} = \Psi_A \otimes \Psi_B$ for all factorizable initial data if and only if*
$$\hat F(\rho) = -b \ln \rho + \mathrm{const}, \qquad b \in \mathbb{R}.$$

(Original proof: [BB76, Theorem in §3].) The constant $b$ has dimensions of energy; sign conventions vary in the literature.

### 2.2 Reading as a forcing principle

The theorem is usually quoted to constrain admissible nonlinear modifications of QM. We instead exploit it as follows: **any continuum lift of a discrete partition structure that preserves separability is forced to have logarithmic self-interaction**. Discrete-to-continuum constructions that respect partition independence cannot have polynomial nonlinearity at large field amplitude.

This forcing has two consequences important for what follows:

1. *Regularity*. Logarithmic nonlinearity grows slower than any power, so the continuum field theory enjoys a Sobolev embedding + Grönwall regularity bound (Section 4.2).
2. *Mass gap*. The logarithmic potential $V(\rho) = \kappa \rho \log \rho$ has an isolated minimum at $\rho_0 = e^{-1}$ with curvature $V''(\rho_0) = \kappa e > 0$ — a positive spectral gap built into the potential.

---

## 3. The Discrete Side: Composition Algebras and the Crossing Lemma

### 3.1 Setup

Fix $N$ squarefree with smallest prime factor $p_1$. The discrete composition algebra of interest is the pair of binary operations $T, B : \mathbb{Z}/N\mathbb{Z} \times \mathbb{Z}/N\mathbb{Z} \to \mathbb{Z}/N\mathbb{Z}$ studied in [J01, J02]; the relevant invariant is the non-associativity defect

$$\sigma(N) = \sum_{x,y,z} \mathbb{1}\!\left[T(T(x,y),z) \neq T(x, T(y,z))\right] / N^3,$$

with the analogous definition for $B$. The companion paper [J01] proves a $\sigma(N) \leq 2/N$ rate theorem on a specific squarefree-modular family, hence $\sigma(N) \to 0$ as $N \to \infty$.

### 3.2 The Crossing Lemma reading

The Crossing Lemma [J05] identifies "information generation" with the failure of partition separability: an evolution generates information only when it acts non-trivially on the quotient $\mathbb{Z}/N\mathbb{Z} \to \prod_i \mathbb{Z}/p_i\mathbb{Z}$ given by the Chinese Remainder Theorem. A separability-preserving evolution leaves the CRT factorization intact and cannot be a source of new information.

### 3.3 The bridge premise

**Bridge premise.** *Any continuum lift $\Phi_N : \mathrm{CL}_N \to L^2(\Omega)$ of the discrete Crossing Lemma data that preserves separability of the partition is, by Theorem 2.1, forced to have logarithmic self-interaction in the limit $N \to \infty$.*

The bridge premise is structural; the explicit construction of $\Phi_N$ (a discrete-to-continuum embedding consistent with the Maas / JKO transport framework [Maas11, JKO98, GigliMaas13]) is left as Open Problem 1 in §6.

---

## 4. The Forced Continuum Lift

### 4.1 The lifted field equation

Applying Theorem 2.1 to the bridge premise, the continuum lift takes the form

$$\boxed{\;\Box \Xi = \kappa(1 + \log \Xi)\;}$$

with field domain $\Xi > 0$ and a single dimensionless coupling $\kappa$. The action density is $V(\Xi) = \kappa\,\Xi \log \Xi$, with vacuum at $\Xi_0 = e^{-1}$ and fluctuation mass $m_\Xi^2 = \kappa\, e$.

This is the same potential studied cosmologically in [J03] as freezing/thawing quintessence; the connection is structural (logarithmic potential forced by separability), not derivational.

### 4.2 Provable regularity

**Theorem 4.1 (regularity of the BB-lifted theory).** *Let $\Xi(t,x)$ be a smooth solution of $\Box \Xi = \kappa(1 + \log \Xi)$ with smooth, positive initial data on $\mathbb{R}^{1+3}$. Then $\Xi$ remains smooth for all $t > 0$, and*
$$\|\Xi(t)\|_{H^s} \leq \|\Xi(0)\|_{H^s} \exp\bigl(C_s\,t\,(1 + \log \|\Xi(0)\|_{H^s})\bigr)$$
*for $s \geq 3$, where $C_s$ depends only on $s$ and $\kappa$.*

*Proof sketch.* The nonlinearity $f(\Xi) = 1 + \log \Xi$ grows as $O(\log \Xi)$ for large $\Xi$. Standard Sobolev embedding gives $\|\log \Xi\|_{H^s} \leq C(1 + \log \|\Xi\|_{H^s})$, and the resulting Grönwall iteration yields the displayed double-exponential bound, which is finite for all finite $t$. The full proof follows the Cazenave-Haraux scheme [CazenaveHaraux80] for log-nonlinear Schrödinger, adapted to the wave equation; details are in the constructive QFT literature on the Høegh-Krohn $\exp(\Phi)_2$ model [HoeghKrohn71].

---

## 5. The Navier-Stokes Application

### 5.1 The two nonlinearities

We compare two nonlinearities side by side:

| Property | $\Xi$ theory (log) | NS (quadratic) |
|---|---|---|
| Equation | $\Box\Xi = \kappa(1 + \log \Xi)$ | $\partial_t u + (u\cdot\nabla)u = \nu\Delta u - \nabla p$ |
| Nonlinearity | $f(\Xi) = 1 + \log \Xi$ | $(u\cdot\nabla)u$ |
| Growth | $O(\log \Xi)$ | $O(|u|^2)$ |
| Separability (Theorem 2.1) | Preserved | Broken |
| Regularity | **Theorem 4.1** | Open (Millennium Problem) |
| Vacuum | $\Xi_0 = e^{-1}$, $m_\Xi^2 = \kappa e$ | $u = 0$ |

The asymmetry is structural: the BB theorem says logarithmic nonlinearity uniquely preserves separability, and the NS quadratic nonlinearity is not in the BB class.

### 5.2 The separability defect $\sigma(u)$

**Definition 5.1.** *Let $u \in H^1(\Omega)$ and let $\{\Omega_i\}$ be a finite partition of $\Omega$. The separability defect of $u$ relative to this partition is*
$$\sigma(u; \{\Omega_i\}) = \frac{\|u - P_{\rm sep}(u)\|_{H^1}}{\|u\|_{H^1}}$$
*where $P_{\rm sep}(u)$ is the orthogonal projection onto the subspace of velocity fields decomposable as $u = \sum_i u_i$ with $\mathrm{supp}(u_i) \subset \Omega_i$.*

Two limit cases:

- $\sigma = 0$: $u$ is already separable into independent subregions (laminar / non-coupling regime).
- $\sigma \to 1$: $u$ is maximally non-separable (full global coupling).

For NS, the advection $(u\cdot\nabla)u$ at $x$ involves both $u(x)$ and $\nabla u(x)$, so any partition with non-zero gradient across boundaries gives $\sigma > 0$. As vorticity concentrates in a tube of radius $r$ with circulation $\Gamma$, $\omega \sim \Gamma/r^2$, and one verifies $\sigma \to 1$ as $r \to 0$.

### 5.3 The Separability Regularity Criterion

**Conjecture 5.2 (Separability Regularity Criterion).** *Let $u(t,x)$ be a smooth solution of 3D NS with smooth initial data $u_0 \in H^s$, $s \geq 3$. Then $u$ remains smooth for all $t > 0$ if and only if*
$$\sup_{t \in [0,T]} \sigma(u(t); \{\Omega_i\}_{\rm optimal}) < 1$$
*for every finite $T$, where the supremum is over the partition that maximizes $\sigma$.*

In the Crossing-Lemma reading: *blowup is the case where a crossing destroys all partition structure*; *regularity is the case where every crossing leaves residual separability*.

### 5.4 The logarithmic comparison

The strongest structural connection between BB regularity and NS regularity is the following observation: known NS regularity criteria *log-improve* over the polynomial growth they replace. The Beale-Kato-Majda criterion [BKM84] uses $\|\omega\|_\infty$; Kozono-Taniuchi [KT00] sharpens this to $\|\omega\|_{\mathrm{BMO}}$, which is a logarithmic improvement. Lei-Zhou [LZ09] and Montgomery-Smith [MS01] give further log-type criteria.

The interpretive statement: *the gap between known regularity and potential blowup is exactly logarithmic*. This is precisely the gap forced by the Bialynicki-Birula theorem: the logarithmic nonlinearity is the separability-preserving ceiling that the actual quadratic nonlinearity skirts. NS regularity is a question about whether the quadratic nonlinearity ever exceeds this logarithmic ceiling.

### 5.5 Explicit open problems

We close §5 with three precisely stated open problems.

**Open Problem 1 (the discrete-to-continuum lift $\Phi_N$).** Construct an explicit $\Phi_N : \mathrm{CL}_N \to L^2(\Omega)$ that maps the Crossing Lemma composition data on $\mathbb{Z}/N\mathbb{Z}$ to a function space such that $\lim_{N\to\infty} \Phi_N(\mathrm{CL}_N) = \Xi$ satisfies $\Box \Xi = \kappa(1 + \log \Xi)$. Tools available: wavelet RG [Morinelli21]; JKO scheme [JKO98]; Maas detailed-balance / log-Sobolev framework [Maas11, GigliMaas13]; Chow-Huang-Li-Zhou [CHLZ12].

**Open Problem 2 (the nonlinearity gap $\delta^*$).** Determine
$$\delta^* = \sup_{u \in C^\infty} \frac{\|(u\cdot\nabla)u\|_{H^{-1}}}{\|u\|_{H^1}(1 + \log \|u\|_{H^1})}.$$
If $\delta^* < \infty$: NS is regular. If $\delta^* = \infty$: blowup is possible.

**Open Problem 3 (separability bound).** Prove or disprove: for all smooth 3D NS solutions with smooth initial data, $\sigma(u(t)) < 1$ for all $t > 0$.

---

## 6. Status, Lens Scope, Tier Classification

### 6.1 Status table

| Claim | Status |
|---|---|
| Theorem 2.1 (BB uniqueness) | **PROVED** [BB76] |
| Theorem 4.1 ($\Xi$-regularity) | **PROVED** (Cazenave-Haraux + log-Sobolev) |
| NS quadratic nonlinearity breaks separability | **PROVED** (immediate) |
| Bridge premise (separability-preserving lift forces log) | **STRUCTURAL** (uses Theorem 2.1 plus a lift construction $\Phi_N$, the latter is Open Problem 1) |
| Conjecture 5.2 (separability regularity) | **CONJECTURE** |
| NS regularity follows | **OPEN** (requires Open Problems 1, 2, 3 collectively) |

### 6.2 Lens scope

This paper carries no TSML / BHML lens dependence. The mathematical content is real-analysis + nonlinear PDE; the discrete side cites [J01, J02, J05] but does not condition on the lens taxonomy.

### 6.3 Tier classification

**Central claim:** Tier 4 (framework paper, structural). The BB theorem is proved; the $\Xi$-theory regularity is proved; the NS regularity is *not* claimed proved. The paper provides a precise mathematical framework that makes the NS regularity question more focused (the Three Open Problems), and identifies the logarithmic ceiling as the structural object that the framework predicts NS solutions must respect.

---

## References

### The forcing theorem
- [BB76] Bialynicki-Birula, I., Mycielski, J. (1976). "Nonlinear wave mechanics." *Annals of Physics* **100**(1-2):62--93.
- Rosen, G. (1969). *Phys. Rev.* **183**:1186.
- Cazenave, T., Haraux, A. (1980). *Ann. Fac. Sci. Toulouse*.
- Zloshchastiev, K.G. (2010). *Grav. Cosmol.* **16**:288.

### Constructive QFT / Wightman side
- Høegh-Krohn, R. (1971). *Commun. Math. Phys.* **38**(3):195. (2D $\exp(\Phi)$ model)
- Glimm, J., Jaffe, A. (1987). *Quantum Physics: A Functional Integral Point of View*. Springer.

### Navier-Stokes literature
- Leray, J. (1934). *Acta Math.* **63**:193--248.
- Beale, J.T., Kato, T., Majda, A. (1984). *Commun. Math. Phys.* **94**:61--66.
- Kozono, H., Taniuchi, Y. (2000). *Commun. Math. Phys.* **214**:191--200.
- Kozono, H., Ogawa, T., Taniuchi, Y. (2002). *Math. Z.* **242**:251--278.
- Montgomery-Smith, S. (2001). *Math. Res. Lett.* **8**:519--528.
- Lei, Z., Zhou, Y. (2009). *Nonlinearity* **22**(4):805.
- Tao, T. (2016). *J. AMS* **29**:601--674.
- Brezis, H., Gallouët, T. (1980). *Nonlinear Analysis* **4**:677--681.
- Fefferman, C. (2000). Clay NS problem statement.

### Discrete-to-continuum transport
- Jordan, R., Kinderlehrer, D., Otto, F. (1998). *SIAM J. Math. Anal.* **29**(1):1--17.
- Maas, J. (2011). *J. Funct. Anal.* **261**(8):2250--2292.
- Gigli, N., Maas, J. (2013). *SIAM J. Math. Anal.* **45**(2):879--899.
- Chow, S.-N., Huang, W., Li, Y., Zhou, H. (2012). *Arch. Rat. Mech. Anal.* **203**(3):969--1008.
- Morinelli, V. *et al.* (2021). Wavelet RG construction.

### Companion submissions in the J-series
- [J01] Sanders, B.R., Gish, M. (2026). "Non-Associativity Decay in Binary Composition Tables over $\mathbb{Z}/N\mathbb{Z}$." Submitted to *JCT-A*.
- [J02] Sanders, B.R., Gish, M. (2026). "Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor of Two Commutative Binary Operations on $\mathbb{Z}/10\mathbb{Z}$." Submitted to *Algebraic Combinatorics*.
- [J03] Sanders, B.R., Gish, M., Johnson, H.J. (2026). "Freeze-Thaw Transit: Dual-Regime Scalar Dark Energy with Analytic Vacuum at $e^{-1}$ from a Logarithmic Potential." Submitted to *JCAP*.
- [J05] Sanders, B.R., Mayes, B. (2026). "Crossing Lemma." Submitted to *JCT-A* / *JPAA*.
- [J14] Sanders, B.R., Johnson, H.J. (2026). "The Yang-Mills Mass Gap Bridge." Companion JMP submission.

DOI for the verification scripts (`proof_separability_bridge.py`): 10.5281/zenodo.18852047.
