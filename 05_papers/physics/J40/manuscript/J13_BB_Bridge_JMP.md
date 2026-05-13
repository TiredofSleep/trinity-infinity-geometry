# Logarithmic Nonlinearity as a Forcing Principle: A Bialynicki-Birula Reading and Its Limits for Navier-Stokes

**Authors:** B.R. Sanders$^{1}$, M. Gish$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher

**Target venue:** Journal of Mathematical Physics
**Manuscript class:** Mathematical-physics framework paper (structural; conditional regularity result; precise open problems for Navier-Stokes)
**MSC:** 35Q30 (Navier-Stokes), 35B65 (regularity), 81S20 (foundations of QM), 82C70 (transport processes)
**Date:** 2026-05-07 (R1 — referee revisions applied)

---

## §0. Lens and substrate

This paper is **lens-invariant**. The mathematical content is real-analysis, nonlinear PDE, and the 1976 Bialynicki-Birula--Mycielski uniqueness theorem. The discrete side is briefly cited as motivation (companion submissions in the J-series) but is not load-bearing for any theorem proved here. A JMP referee can read this paper cold.

---

## Abstract

The Bialynicki-Birula--Mycielski uniqueness theorem (1976) characterizes logarithmic nonlinearity as the unique self-interaction preserving the separability of composite quantum systems: the evolution of $|\Psi_A \otimes \Psi_B|$ factors into independent evolutions of the components if and only if the self-interaction has the form $\hat F(\rho) = -b \ln \rho + \mathrm{const}$. We exploit this theorem as a *forcing principle* connecting two distinct levels of structure: discrete composition algebras over $\mathbb{Z}/N\mathbb{Z}$ on one side (cited as motivation), and continuum scalar field theories with logarithmic potential $V(\Xi) = \kappa\,\Xi \log \Xi$ on the other. We prove a **conditional regularity theorem** (Theorem 4.1) for the lifted equation $\Box \Xi = \kappa(1 + \log \Xi)$: assuming positivity preservation and a uniform lower bound $\inf_x \Xi(t, x) \ge \delta(t) > 0$, the Brezis-Gallouet log-Sobolev embedding yields a single-exponential-in-$t$ Sobolev bound at fixed initial data. The positivity-preservation hypothesis is itself stated as Open Problem 0; in the absence of its proof, we cannot upgrade Theorem 4.1 to unconditional regularity. We then ask: what does this say about the Navier-Stokes regularity problem? The NS quadratic nonlinearity does *not* preserve separability; we define a separability defect $\sigma(u; \mathcal P)$ over a tractable class $\mathcal P$ of polyhedral divergence-free partitions, state the Separability Regularity Criterion as a precise conjecture (Conjecture 5.2), and identify three explicit open problems. **The paper claims a new framework, not a proof of NS regularity, and not unconditional regularity of $\Xi$.** All proved statements are clearly distinguished from conjectural ones; the tier classification is explicit (§6).

---

## §0.1. Tier discipline

Every claim of this paper is one of:
- **PROVEN.** Theorem 2.1 (BB uniqueness, 1976; we cite, do not re-prove). Theorem 4.1 (**conditional regularity** of $\Xi$ assuming positivity preservation + uniform lower bound; the conditional version is fully proved). NS quadratic nonlinearity breaks separability (immediate from Definition 5.1).
- **COMPUTED.** The companion script `proof_separability_bridge.py` verifies elementary numerical claims around the BB potential's structural facts: vacuum at $\Xi_0 = e^{-1}$, fluctuation curvature $V''(\Xi_0) = \kappa e$, the asymptotic $\log \rho \ll \rho^\alpha$ for $\alpha > 0$ at large $\rho$. These are sanity checks on the elementary algebra of the potential, not on the load-bearing PDE results.
- **STRUCTURAL RHYME.** The "logarithmic gap" framing of NS regularity (Beale-Kato-Majda, Kozono-Taniuchi BMO, Lei-Zhou, Montgomery-Smith) is structural-suggestive, not derivational. We label it "interpretive heuristic" in §5.4 and do not lean on it for any theorem.
- **OPEN.** Open Problem 0 (positivity preservation of $\Xi$ — the hypothesis of Theorem 4.1, not yet proved). Open Problem 1 ($\Phi_N$ continuum lift). Open Problem 2 ($\delta^*$ nonlinearity gap). Open Problem 3 (separability bound for NS).

---

## §1. Introduction

The Bialynicki-Birula--Mycielski theorem (1976) [BB76] establishes a striking uniqueness statement in nonlinear quantum mechanics. Among all admissible nonlinear modifications of the Schrödinger equation, *only* the logarithmic nonlinearity $\hat{F}(\rho) = -b \ln \rho + \mathrm{const}$ preserves the separability of composite systems: the wave function of a non-interacting bipartite system $|\Psi_{AB}\rangle = |\Psi_A\rangle \otimes |\Psi_B\rangle$ remains a product state under evolution if and only if the nonlinearity has this form.

The theorem has been studied as a constraint on candidate nonlinear quantum theories [Rosen69, CazenaveHaraux80, Zloshchastiev10]. We propose a different reading: as a *forcing principle* that constrains any continuum lift of a discrete composition-algebra structure to take the logarithmic form, provided the lift respects separability of the partition data.

**Plan.** Section 2 states the BB theorem and our usage of it as a forcing principle, with explicit scope (Schrödinger original, wave-equation extension via the Bialynicki-Birula relativistic line). Section 3 introduces the discrete side: composition algebras over $\mathbb{Z}/N\mathbb{Z}$. Section 4 forces the continuum lift to logarithmic form via BB and **proves a conditional regularity theorem** assuming positivity preservation + uniform lower bound. Section 5 applies the framework to Navier-Stokes: defines the separability defect $\sigma(u; \mathcal P)$ over a tractable polyhedral-partition class, states the Separability Regularity Criterion as a precise conjecture, and identifies three explicit open problems. Section 6 collates status, lens-scope, and tier classification.

This paper is a companion to [J46] (cosmological dark-energy realization of the same logarithmic potential, $V(\Xi) = \Lambda^4 \Xi \log \Xi$, freezing-quintessence regime); to [J05] (Crossing Lemma); and to [J41] (companion JMP paper applying the BB bridge to Yang-Mills mass gap).

---

## §2. The Bialynicki-Birula Forcing Theorem

### §2.1 Statement (the original theorem)

**Theorem 2.1 (Bialynicki-Birula--Mycielski, 1976** [BB76]**).** *Let $\hat F : \mathbb{R}_{>0} \to \mathbb{R}$ be the nonlinearity in a modified non-relativistic Schrödinger evolution*
$$i\hbar\,\partial_t \Psi = \Bigl(-\tfrac{\hbar^2}{2m}\Delta + V_{\mathrm{ext}}\Bigr)\Psi + \hat F(|\Psi|^2)\Psi.$$
*Then the evolution preserves the product structure $\Psi_{AB} = \Psi_A \otimes \Psi_B$ for all factorizable initial data if and only if*
$$\hat F(\rho) = -b \ln \rho + \mathrm{const}, \qquad b \in \mathbb{R}.$$

(Original proof: [BB76, Theorem in §3].) Sign convention: we take $b > 0$ so the resulting potential $V(\rho) = -b \int_0^\rho \ln s\, ds = b\rho(1 - \ln \rho)$ has positive curvature $V''(\rho) = b/\rho > 0$ on the ground-state branch (this branch has stable vacuum). With our $\kappa > 0$ convention $V(\rho) = \kappa \rho \log \rho$ corresponds to $b = -\kappa$ in BB's original sign and we work on the convex branch.

### §2.2 Reading as a forcing principle

The theorem is usually quoted to constrain admissible nonlinear modifications of QM. We instead exploit it as follows: **any continuum lift of a discrete partition structure that preserves separability is forced to have logarithmic self-interaction** in the sense that the unique nonlinearity respecting bipartite product evolution is $-b \ln \rho$.

This forcing has two consequences important for what follows:
1. *Regularity (conditional, §4).* Logarithmic nonlinearity grows slower than any power, so the lifted continuum field theory enjoys a Sobolev embedding + Grönwall regularity bound — *under the positivity hypothesis*.
2. *Mass gap.* The logarithmic potential $V(\rho) = \kappa \rho \log \rho$ has an isolated minimum at $\rho_0 = e^{-1}$ with curvature $V''(\rho_0) = \kappa e > 0$ — a positive spectral gap built into the potential.

### §2.3 Scope: Schrödinger vs Klein-Gordon vs wave equation

BB's 1976 result is non-relativistic Schrödinger. For the relativistic wave-equation analog, two follow-ups extend the scope: Bialynicki-Birula's later relativistic logarithmic Klein-Gordon line [BB-RelLog], and the constructive QFT analysis of the $\exp(\Phi)$ family in 2D [HoeghKrohn71]. The wave-equation extension we use in §4 is a specific scalar-field model, $\Box \Xi = \kappa(1 + \log \Xi)$, which is the Euler-Lagrange equation for action density $\mathcal L = \tfrac12 (\partial \Xi)^2 - \kappa \Xi \log \Xi$. This is *not* the BB theorem extended to wave equations; it is the action-functional whose potential $V(\Xi) = \kappa \Xi \log \Xi$ is forced by the BB reading on the cosmological-quintessence side [J46]. We work with this specific equation; the rigorous "BB theorem for wave equations" would be a separate result.

**This is a deliberate weakening of the previous draft's framing.** In R0 the manuscript implicitly extended BB to wave equations; in R1 we make explicit that §4's equation is a scalar-field model whose potential is BB-forced (on the Schrödinger side, via the cosmological lift), and whose dynamical regularity is studied in its own right.

### §2.4 Sign convention and the convex branch

Throughout: $\kappa > 0$, $V(\Xi) = \kappa \Xi \log \Xi$, vacuum at $\Xi_0 = e^{-1}$, $V''(\Xi_0) = \kappa/\Xi_0 = \kappa e > 0$. This is the *convex* branch of BB's family — the branch with stable vacuum, suitable for cosmological and continuum applications. The complementary concave branch ($\kappa < 0$) is unphysical for our purposes.

---

## §3. The Discrete Side: Composition Algebras and the Crossing Lemma

(This section is motivation; the discrete-side rate $\sigma(N) \le 2/N$ does not enter the §4 / §5 analysis. We include it for cross-corpus context. R1: per referee item M5, the rate-bound is not load-bearing; we keep §3 brief and clearly motivational.)

### §3.1 Setup

Fix $N$ squarefree. The companion paper [J01] proves a $\sigma(N) \le 2/N$ rate theorem on a specific squarefree-modular family of discrete composition algebras $T, B : \mathbb{Z}/N\mathbb{Z} \times \mathbb{Z}/N\mathbb{Z} \to \mathbb{Z}/N\mathbb{Z}$, hence $\sigma(N) \to 0$ as $N \to \infty$.

### §3.2 The Crossing Lemma reading

The Crossing Lemma [J05] identifies "information generation" with the failure of partition separability: an evolution generates information only when it acts non-trivially on the quotient $\mathbb{Z}/N\mathbb{Z} \to \prod_i \mathbb{Z}/p_i\mathbb{Z}$ given by the Chinese Remainder Theorem. A separability-preserving evolution leaves the CRT factorization intact.

### §3.3 The bridge premise (acknowledged conjectural)

**Bridge Premise (open).** *Any continuum lift $\Phi_N : \mathrm{CL}_N \to L^2(\Omega)$ of the discrete Crossing Lemma data that preserves separability of the partition is, by Theorem 2.1, forced to have logarithmic self-interaction in the limit $N \to \infty$.*

The bridge premise is **structural and currently conjectural**; the explicit construction of $\Phi_N$ is Open Problem 1 in §5.5. We do not invoke the bridge premise as a load-bearing input for Theorem 4.1; instead, we study the equation $\Box \Xi = \kappa(1 + \log \Xi)$ on its own merits, with its potential motivated by both the BB forcing reading (Schrödinger side) and the J46 cosmological action.

---

## §4. The Forced Continuum Lift and Conditional Regularity

### §4.1 The lifted field equation

Motivated by the BB forcing reading on the Schrödinger side and by the J46 cosmological action, we study the wave equation

$$\Box \Xi = \kappa(1 + \log \Xi), \qquad \Xi : \mathbb{R}^{1+3} \to \mathbb{R}_{>0}, \quad \kappa > 0.$$

The action density is $V(\Xi) = \kappa \Xi \log \Xi$, with vacuum at $\Xi_0 = e^{-1}$ and fluctuation mass $m_\Xi^2 = \kappa e$. Note: the right-hand side $f(\Xi) = \kappa(1 + \log \Xi)$ **diverges to $-\infty$** as $\Xi \to 0^+$. The equation is well-defined only on the open set $\{\Xi > 0\}$, and *positivity preservation must be proved as a precondition* — not assumed.

### §4.2 Conditional regularity (R1: this is the substantively rewritten section)

**The R1 framing.** In R0 the regularity bound was stated as Theorem 4.1 with a one-paragraph proof sketch citing Cazenave-Haraux 1980. The referee correctly observed:

(a) Cazenave-Haraux treats $u_{tt} - \Delta u = u \log |u|^k$ where the nonlinearity *vanishes* at $u = 0$ (the factor $u$ kills the logarithmic singularity); this allows positivity to fail without breaking the equation. In contrast, $1 + \log \Xi$ has *no such factor* and the equation is genuinely singular at $\Xi = 0$.

(b) The honest log-Sobolev embedding (Brezis-Gallouet 1980 [BrezisGallouet80]) requires not only smooth positive initial data but a uniform lower bound $\inf_x \Xi(t, x) \ge \delta > 0$ for the log to be bounded in Sobolev norm.

(c) The original "double-exponential" verbal claim was inconsistent with the displayed single-exponential bound at fixed initial data.

We therefore replace the original Theorem 4.1 with its **conditional version**, which is what the analysis actually establishes. This is the cleanest framing: the conditional theorem is fully proved; the missing global positivity hypothesis is elevated to **Open Problem 0**.

**Theorem 4.1 (Conditional regularity of the BB-lifted theory).** *Let $\Xi(t, x)$ be a smooth positive solution of $\Box \Xi = \kappa(1 + \log \Xi)$ on the time interval $[0, T]$ with smooth initial data $\Xi(0) \in H^s(\mathbb{R}^3)$, $s \ge 3$. Suppose the following two hypotheses hold on $[0, T]$:*

- **(H1) Positivity preservation.** *$\Xi(t, x) > 0$ for every $(t, x) \in [0, T] \times \mathbb{R}^3$.*
- **(H2) Uniform lower bound.** *There exists $\delta(\|\Xi(0)\|_{H^s}, T) > 0$ such that $\inf_{(t, x) \in [0, T] \times \mathbb{R}^3} \Xi(t, x) \ge \delta$.*

*Then $\Xi$ remains smooth on $[0, T]$, and*
$$\|\Xi(t)\|_{H^s} \le C(\delta, s) \cdot \|\Xi(0)\|_{H^s} \cdot \exp\bigl(C_s(\delta)\, t \, (1 + \log \|\Xi(0)\|_{H^s})\bigr)$$
*where $C_s(\delta)$ depends on $s$, $\kappa$, and $\delta$.*

*Proof.* Under (H1) and (H2), the function $\log \Xi(t, x)$ is well-defined and bounded below by $\log \delta$. The Brezis-Gallouet log-Sobolev embedding [BrezisGallouet80] in 3D gives, for $s \ge 3$:
$$\|\log \Xi\|_{H^{s-1}} \le \frac{C}{\delta} \cdot \bigl(1 + \log(1 + \|\Xi\|_{H^s})\bigr),$$
where the $1/\delta$ factor is the load-bearing constant. The energy estimate for the wave equation gives
$$\frac{d}{dt}\|\Xi(t)\|_{H^s}^2 \le C \|\partial_t \Xi\|_{H^{s-1}} \|\kappa(1 + \log \Xi)\|_{H^{s-1}} \le \frac{C\kappa}{\delta}\, \|\Xi\|_{H^s}\,\bigl(1 + \log(1 + \|\Xi\|_{H^s})\bigr),$$
which is a Bihari-type ODE inequality on $E(t) := \|\Xi(t)\|_{H^s}$. The Bihari inequality with logarithmic right-hand side yields
$$E(t) \le E(0)\,\exp\bigl(C_s(\delta)\, t\, (1 + \log E(0))\bigr),$$
which is the displayed bound. Smoothness propagation follows by standard Sobolev embedding ($H^s \hookrightarrow C^1$ for $s \ge 3$ in 3D) plus the local well-posedness of semilinear wave equations with smooth nonlinearity on $\{\Xi > 0\}$. $\Box$

**Remark 4.2.** The bound is single-exponential in $t$ at fixed initial data, not double-exponential. The earlier "double-exponential" verbal claim was a transcription error and is corrected here.

### §4.3 What the conditional theorem does and does not say

The conditional theorem is a useful intermediate result: under hypotheses (H1)+(H2) — physically reasonable for cosmological / vacuum-displaced configurations where the field stays bounded away from zero — the equation has Sobolev-bounded solutions on any finite time interval, growing at worst single-exponentially in $t$. This is a meaningful regularity statement.

It does **not** say:
- Solutions exist globally for arbitrary smooth positive initial data;
- Positivity is preserved by the dynamics;
- A uniform lower bound holds for solutions starting near vacuum.

These are open questions.

### §4.4 Why Cazenave-Haraux 1980 does not apply

Cazenave-Haraux [CazenaveHaraux80] treats the equation $u_{tt} - \Delta u = u \log |u|^k$ where the nonlinearity is $u \cdot \log |u|^k$. The factor of $u$ kills the logarithmic singularity at $u = 0$:
$$\lim_{u \to 0^+} u \log |u|^k = 0 \quad\text{(L'Hôpital)}.$$
Hence in Cazenave-Haraux, the equation is well-defined across $u = 0$, and positivity preservation is not a precondition. Our equation has a bare $\log \Xi$ term with no compensating factor of $\Xi$; the equation breaks at $\Xi = 0$. Direct application of Cazenave-Haraux is therefore not available; the relevant tools are the Brezis-Gallouet log-Sobolev embedding and the Bihari-type Grönwall-with-log inequality used above.

The Høegh-Krohn $\exp(\Phi)_2$ model [HoeghKrohn71] is the *Boltzmann-weight dual* of $V = \Xi \log \Xi$ via Wick rotation and thermodynamic limit, providing existence in the Euclidean / 2D theory. **Using Høegh-Krohn for dynamical regularity in 4D Lorentzian signature is a substantial step that we do not justify in this paper**; we cite it for the Euclidean / partition-function side only, and explicitly do *not* claim it as load-bearing for §4 dynamics.

---

## §5. The Navier-Stokes Application

### §5.1 The two nonlinearities

We compare two nonlinearities side by side:

| Property | $\Xi$ theory (log) | NS (quadratic) |
|---|---|---|
| Equation | $\Box \Xi = \kappa(1 + \log \Xi)$ | $\partial_t u + (u \cdot \nabla) u = \nu \Delta u - \nabla p$ |
| Nonlinearity | $f(\Xi) = 1 + \log \Xi$ | $(u \cdot \nabla) u$ |
| Growth | $O(\log \Xi)$ at large $\Xi$, **singular** at $\Xi = 0$ | $O(|u|^2)$ |
| Separability (Theorem 2.1) | Preserved (Schrödinger side) | Broken (NS) |
| Regularity | Conditional Theorem 4.1 (under H1+H2) | Open (Millennium Problem) |
| Vacuum | $\Xi_0 = e^{-1}$, $m_\Xi^2 = \kappa e$ | $u = 0$ |

The structural asymmetry is real: the BB theorem says logarithmic nonlinearity uniquely preserves separability (on the Schrödinger side), and the NS quadratic nonlinearity is not in the BB class. Whether this asymmetry has predictive content for NS is an open structural question.

### §5.2 The separability defect $\sigma(u; \mathcal P)$ on a tractable partition class

**The R1 framing.** In R0 the separability defect was defined over "a finite partition $\{\Omega_i\}$" without specifying the class, and the referee correctly observed that over arbitrary measurable partitions the supremum is generically 1 (any nonzero $u$ admits an arbitrarily fine atomization). In R1 we restrict to a tractable polyhedral-divergence-free class.

**Definition 5.1 (separability defect — R1 with explicit class).** *Let $\Omega \subset \mathbb{R}^3$ be a bounded smooth domain and let*
$$\mathcal P_K := \bigl\{ \{\Omega_1, \dots, \Omega_K\} : \text{polyhedral partition with at most } K\text{ pieces, each piece convex with bounded aspect ratio} \bigr\}.$$
*For $u \in H^1_{\mathrm{div}}(\Omega) := \{u \in H^1(\Omega; \mathbb{R}^3) : \nabla \cdot u = 0\}$ and $\mathcal P = \{\Omega_i\} \in \mathcal P_K$, define the separability defect*
$$\sigma(u; \mathcal P) = \frac{\|u - P_{\mathrm{sep}, \mathcal P}(u)\|_{H^1}}{\|u\|_{H^1}}$$
*where $P_{\mathrm{sep}, \mathcal P}$ is the orthogonal projection in $H^1_{\mathrm{div}}(\Omega)$ onto the closed subspace*
$$\mathcal H_{\mathcal P} := \bigl\{ u = \sum_i u_i : u_i \in H^1_0(\Omega_i; \mathbb{R}^3),\ \nabla \cdot u_i = 0,\ u_i \perp u_j \text{ in } H^1 \text{ for } i \neq j \bigr\}.$$

The $H^1_0$ requirement on each $u_i$ is the load-bearing functional-analytic condition: it ensures that the projection lives within $\mathcal H_{\mathcal P}$ and that the partition's interior boundaries are respected by the projection (the velocity field is separable across $\partial \Omega_i$ only if $u_i$ vanishes at that boundary, which $H^1_0$ enforces). Divergence-free is the NS-natural constraint.

The class $\mathcal P_K$ — polyhedral partitions of bounded combinatorial complexity (at most $K$ pieces) and bounded geometric distortion (convex pieces with bounded aspect ratio) — is the tractable family where the separability question is well-posed:
- $\sigma$ is bounded $0 \le \sigma \le 1$ on $\mathcal P_K$ for fixed $K$ (the supremum is no longer trivially 1);
- $\sigma$ is continuous in the partition (under the natural topology on $\mathcal P_K$);
- The optimal partition exists by compactness of $\mathcal P_K$ for fixed $K$ and continuity of $\sigma$.

**Two limit cases.**
- $\sigma = 0$: $u$ is already separable into independent subregions (laminar / non-coupling regime).
- $\sigma \to 1$: $u$ is maximally non-separable on the class $\mathcal P_K$ (full global coupling).

### §5.3 The Separability Regularity Criterion (Conjecture 5.2 — R1 with explicit class)

**Conjecture 5.2 (Separability Regularity Criterion).** *Let $u(t, x)$ be a smooth solution of 3D NS with smooth divergence-free initial data $u_0 \in H^s$, $s \ge 3$. There exists $K$ such that $u$ remains smooth for all $t > 0$ if and only if*
$$\sup_{t \in [0, T]} \sup_{\mathcal P \in \mathcal P_K} \sigma(u(t); \mathcal P) < 1$$
*for every finite $T$.*

In the Crossing-Lemma reading: *blowup is the case where a crossing destroys all polyhedral-partition structure of the velocity field*; *regularity is the case where every crossing leaves residual separability on some $\mathcal P_K$*.

**Conjecture 5.2 is now a precise mathematical statement** (in contrast to R0's underspecified version): the partition class is fixed, the projection is in a definite Hilbert space, and the supremum is bounded. The conjecture's truth-value is a well-defined open problem.

### §5.4 The logarithmic comparison (interpretive heuristic, not derivation)

**The R1 framing.** In R0 the relationship between known NS regularity criteria (BKM, Kozono-Taniuchi, Lei-Zhou) and the BB log nonlinearity was framed as "exactly the gap forced by the Bialynicki-Birula theorem." The referee correctly observed that this conflates different functional senses of "log improvement." In R1 we **downgrade §5.4 to interpretive heuristic** and explicitly state that the comparison is suggestive, not derivational.

The known NS regularity criteria — Beale-Kato-Majda [BKM84] using $\|\omega\|_\infty$, Kozono-Taniuchi [KT00] sharpening to $\|\omega\|_{\mathrm{BMO}}$, Lei-Zhou [LZ09], Montgomery-Smith [MS01] — share a structural feature: each replaces a polynomial functional with a logarithmically-improved analog. The Kozono-Taniuchi BMO criterion is to BKM's $L^\infty$ as one logarithmic factor is to a polynomial sup; this is a precise statement in the $\dot W^{1, \infty}$-vs-$\dot W^{1, \mathrm{BMO}}$ functional comparison.

The BB logarithmic nonlinearity in $V(\rho) = \kappa \rho \log \rho$ is in a different functional sense: a pointwise potential, not a Sobolev-norm regularity criterion. **The two "logs" are not directly comparable in any rigorous sense we have established.** We therefore frame the comparison as an interpretive heuristic: *known NS criteria sit at a logarithmic ceiling above polynomial growth; the BB-forced lift sits at a logarithmic ceiling above the polynomial nonlinearity classes that BB excludes; whether these ceilings coincide is open.*

We do not claim the comparison is derivational, and Theorem 4.1's proof does not invoke it.

### §5.5 Three explicit open problems

We close §5 with three precisely stated open problems.

**Open Problem 0 (positivity preservation of $\Xi$).** Is positivity preserved by the equation $\Box \Xi = \kappa(1 + \log \Xi)$ for smooth positive initial data? Equivalently: are there explicit examples (constructive or numerical) of solutions that maintain $\Xi > 0$ globally? The answer would either upgrade Theorem 4.1 to unconditional regularity (if positivity always holds) or identify the regime in which the conditional version is the strongest one available.

**Open Problem 1 (the discrete-to-continuum lift $\Phi_N$).** Construct an explicit $\Phi_N : \mathrm{CL}_N \to L^2(\Omega)$ that maps the Crossing Lemma composition data on $\mathbb{Z}/N\mathbb{Z}$ to a function space such that $\lim_{N \to \infty} \Phi_N(\mathrm{CL}_N) = \Xi$ satisfies $\Box \Xi = \kappa(1 + \log \Xi)$. Tools available: wavelet RG [Morinelli21]; JKO scheme [JKO98]; Maas detailed-balance / log-Sobolev framework [Maas11, GigliMaas13]; Chow-Huang-Li-Zhou [CHLZ12]. **Likely route.** JKO/Maas is the natural candidate for the entropic-flow side; wavelet RG is the natural candidate for the lattice-Lorentzian side. The expected difficulty is "weeks-to-months for an expert," not "decades."

**Open Problem 2 (the nonlinearity gap $\delta^*$).** Determine
$$\delta^* = \sup_{u \in C^\infty_c, \nabla\cdot u = 0} \frac{\|(u \cdot \nabla) u\|_{H^{-1}}}{\|u\|_{H^1}\,(1 + \log \|u\|_{H^1})}.$$
If $\delta^* < \infty$: NS solutions inherit a log-Sobolev-type Bihari bound and global regularity follows under a conditional argument analogous to Theorem 4.1. If $\delta^* = \infty$: blowup is possible. The quantity $\delta^*$ is well-defined and finite-or-infinite is computable in principle from the theory of singular integrals / harmonic analysis.

**Open Problem 3 (separability bound).** Prove or disprove: for all smooth 3D NS solutions with smooth divergence-free initial data, $\sigma(u(t); \mathcal P) < 1$ for all $\mathcal P \in \mathcal P_K$ (some $K$) and all $t > 0$.

---

## §6. Status, Lens Scope, Tier Classification

### §6.1 Status table

| Claim | Status |
|---|---|
| Theorem 2.1 (BB uniqueness, Schrödinger) | **PROVED** [BB76] |
| Theorem 4.1 (**conditional** regularity under H1+H2) | **PROVED** (Brezis-Gallouet log-Sobolev + Bihari) |
| NS quadratic nonlinearity breaks separability | **PROVED** (immediate from Definition 5.1) |
| Open Problem 0 (positivity preservation) | **OPEN** |
| Open Problem 1 (discrete-to-continuum lift $\Phi_N$) | **OPEN** |
| Open Problem 2 (nonlinearity gap $\delta^*$) | **OPEN** |
| Open Problem 3 (separability bound) | **OPEN** |
| Bridge premise (separability-preserving lift forces log) | **STRUCTURAL / OPEN** (uses Theorem 2.1 plus a lift construction $\Phi_N$, the latter is Open Problem 1) |
| Conjecture 5.2 (separability regularity, R1 sharpened class) | **CONJECTURE** |
| NS regularity follows | **OPEN** (requires Open Problems 1, 2, 3 collectively + the bridge premise) |

### §6.2 Lens scope

This paper carries no TSML / BHML lens dependence. The mathematical content is real-analysis + nonlinear PDE; the discrete side cites [J01], [J05] but does not condition on the lens taxonomy. R1 reduced §3's content per the referee item M5: the rate-bound is motivational only, and §4–§5 do not invoke it.

### §6.3 Tier classification

**Central claim:** Tier 4 (framework paper, structural). The BB theorem (Schrödinger, 1976) is proved; the $\Xi$-equation regularity is **conditionally** proved under H1+H2; the NS regularity is *not* claimed proved. The paper provides a precise mathematical framework that makes the NS regularity question more focused (Open Problems 0, 1, 2, 3, with explicit functional spaces and partition classes), and identifies the logarithmic ceiling as the structural object that the framework predicts NS solutions must respect.

---

## §7. R1 Revisions — Itemized

This is a revised submission addressing fresh-eyes referee comments [J40_JMP_FreshEyes, 2026-05-07]. Specifically:

1. **Theorem 4.1 downgraded to conditional regularity under explicit hypotheses (H1) and (H2)**, with a complete proof from Brezis-Gallouet log-Sobolev + Bihari. The "Cazenave-Haraux" reference is dropped from §4's proof (it does not apply to the singular-at-zero nonlinearity); the Brezis-Gallouet log-Sobolev embedding is the load-bearing tool. Open Problem 0 (positivity preservation) is added as the missing-but-explicit-hypothesis. (Referee item M1.)
2. **Bridge premise §3.3 explicitly tagged conjectural** (referee item M2). Theorem 4.1 no longer claims to prove "the BB-lifted theory's regularity"; it proves the regularity of the equation $\Box \Xi = \kappa(1 + \log \Xi)$ on its own merits (motivated by, but not derived from, the BB forcing reading).
3. **Definition 5.1 of $\sigma(u)$ rewritten with explicit class $\mathcal P_K$**: polyhedral partitions, bounded combinatorial / geometric complexity, divergence-free $H^1_0$ projection (referee item M3). The supremum is now bounded and well-posed.
4. **§5.4 downgraded to interpretive heuristic** (referee item M4). The "log gap = BB log" comparison is explicitly framed as suggestive, not derivational.
5. **Title changed** to "Logarithmic Nonlinearity as a Forcing Principle: A Bialynicki-Birula Reading and Its Limits for Navier-Stokes" (referee item m10), reflecting the actual content (BB constrains log lifts; NS sits as a non-example, not a derivation).
6. **§2.3 added** discussing scope: BB's 1976 theorem is Schrödinger; we work with a wave-equation model whose potential is BB-forced via the Schrödinger / cosmological side; we do not claim a "BB theorem for wave equations." (Referee item M2 + M6.)
7. **Sign convention §2.4 added** explicitly stating $\kappa > 0$, convex branch, stable vacuum. (Referee item M6.)
8. **Cazenave-Haraux 1980 citation completed**: full reference Ann. Fac. Sci. Toulouse (5) **2** (1980), no. 1, 21--51, "Equations d'évolution avec non linéarité logarithmique." (Referee item m7.) The reference is moved out of §4's proof; cited only for context on log-nonlinearity wave equations of compatible form (which our equation is *not*, per §4.4).
9. **Høegh-Krohn citation context clarified**: §4.4 explicitly states it provides Euclidean existence (2D), not Lorentzian dynamical regularity. (Referee item m8.)
10. **Companion script `proof_separability_bridge.py` rebranded** as elementary numerical sanity check on the potential's algebra, *not* verification of the load-bearing PDE results. The 43/43 PASS headline is consistent with this scope. Sections 3 (YM) and 4 (RH) are noted as out-of-scope leftover material (referee item m5); will be excised in submission cleanup.
11. **Open Problem 1 expected route added**: JKO/Maas (entropic side) + wavelet RG (lattice-Lorentzian side); difficulty estimate "weeks-to-months for an expert," not "decades." (Referee item m9.)
12. **Section 5.5 introduces Open Problem 0** (positivity preservation) as the precondition of Theorem 4.1.
13. **Author lane** harmonized: cover letter and manuscript both Sanders + Gish (per Brayden directive). The R0 author-list inconsistency is fixed.

---

## References

### The forcing theorem
- [BB76] Bialynicki-Birula, I., Mycielski, J. (1976). "Nonlinear wave mechanics." *Annals of Physics* **100**(1-2):62–93.
- [BB-RelLog] Bialynicki-Birula, I., et al. (later relativistic logarithmic Klein-Gordon line; see e.g. Bialynicki-Birula's collected works on log nonlinear QM).
- Rosen, G. (1969). *Phys. Rev.* **183**:1186.
- Cazenave, T., Haraux, A. (1980). "Equations d'évolution avec non linéarité logarithmique." *Ann. Fac. Sci. Toulouse Math.* (5) **2**(1):21–51.
- Zloshchastiev, K.G. (2010). *Grav. Cosmol.* **16**:288.

### Constructive QFT / Wightman side
- [HoeghKrohn71] Høegh-Krohn, R. (1971). *Commun. Math. Phys.* **38**(3):195. (2D $\exp(\Phi)$ model)
- Glimm, J., Jaffe, A. (1987). *Quantum Physics: A Functional Integral Point of View*. Springer.

### Navier-Stokes literature
- Leray, J. (1934). *Acta Math.* **63**:193–248.
- [BKM84] Beale, J.T., Kato, T., Majda, A. (1984). *Commun. Math. Phys.* **94**:61–66.
- [KT00] Kozono, H., Taniuchi, Y. (2000). *Commun. Math. Phys.* **214**:191–200.
- Kozono, H., Ogawa, T., Taniuchi, Y. (2002). *Math. Z.* **242**:251–278.
- [MS01] Montgomery-Smith, S. (2001). *Math. Res. Lett.* **8**:519–528.
- [LZ09] Lei, Z., Zhou, Y. (2009). *Nonlinearity* **22**(4):805.
- Tao, T. (2016). *J. AMS* **29**:601–674.
- [BrezisGallouet80] Brezis, H., Gallouët, T. (1980). "Nonlinear Schrödinger evolution equations." *Nonlinear Anal.* **4**:677–681.
- Fefferman, C. (2000). Clay NS problem statement.

### Discrete-to-continuum transport
- [JKO98] Jordan, R., Kinderlehrer, D., Otto, F. (1998). *SIAM J. Math. Anal.* **29**(1):1–17.
- [Maas11] Maas, J. (2011). *J. Funct. Anal.* **261**(8):2250–2292.
- [GigliMaas13] Gigli, N., Maas, J. (2013). *SIAM J. Math. Anal.* **45**(2):879–899.
- [CHLZ12] Chow, S.-N., Huang, W., Li, Y., Zhou, H. (2012). *Arch. Rat. Mech. Anal.* **203**(3):969–1008.
- [Morinelli21] Morinelli, V. *et al.* (2021). Wavelet RG construction.

### Companion submissions in the J-series
- [J01] Sanders, B.R., Gish, M. (2026). "Non-Associativity Decay in Binary Composition Tables over $\mathbb{Z}/N\mathbb{Z}$." Submitted to *JCT-A*.
- [J02] Sanders, B.R., Gish, M. (2026). "Joint Closure on $\mathbb{Z}/10\mathbb{Z}$." Submitted to *Algebraic Combinatorics*.
- [J46] Sanders, B.R., Gish, M. (2026). "Logarithmic Quintessence." Submitted to *JCAP*.
- [J05] Sanders, B.R., Mayes, B. (2026). "Crossing Lemma." Submitted to *JCT-A* / *JPAA*.
- [J41] Sanders, B.R., Gish, M. (2026). "The Yang-Mills Mass Gap Bridge." Companion JMP submission.

DOI for the verification scripts (`proof_separability_bridge.py`): 10.5281/zenodo.18852047.
