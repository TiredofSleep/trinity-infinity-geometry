# A Structural Rhyme between the σ-Character Spectrum on $\mathbb{Z}/10\mathbb{Z}$ and the Riemann Zeros

**Authors:** B.R. Sanders$^{1}$, M. Gish$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Target venue:** *Mathematical Intelligencer* (expository note).

**Status:** DRAFT (2026-05-27). Companion note to Sanders & Gish, *Spectral Architecture of the σ-Character on Z/10Z*, submitted to *European J. Combinatorics* [J07].

**MSC 2020:** 11M26 (nonreal zeros of $\zeta$ and $L$-functions), 11T22 (cyclotomy), 11T55 (character sums and exponential sums), 00A30 (philosophy of mathematics), 11Z05 (miscellaneous applications).

---

## Abstract

We describe a *structural rhyme* — in the Connes–Berry–Keating sense of an explicit, non-derivational comparison — between three features of the σ-character spectrum on $\mathbb{Z}/10\mathbb{Z}$ (defined in the companion paper [J07]) and three features that the Riemann Hypothesis demands of the Riemann zeta function $\zeta(s)$. The rhyme has three rungs: (i) vanishing of the spectral coherence integral on a distinguished subset of the substrate mirrors the predicted location of non-trivial zeros on the critical line; (ii) the three-valued image of that integral mirrors the spectral concentration that RH expresses; (iii) the σ-iteration's additive structure paired with the χ-character's $\pm 1$-valuation mirrors the multiplicative–additive interplay of the Euler product. We are explicit that this is a *rhyme*, not a proof, not an analogue in the Weil–Deligne sense, and not an analytic continuation of the finite spectral data. The rhyme would lift to a derivation only under a specific open conjecture (Z.5) about whether a candidate deployment map from the Dirichlet half-plane to the substrate is grading-preserving in a precise sense. The aim of the note is to record the rhyme honestly and locate the specific open problem whose resolution would convert observation into theorem.

---

## §1. The genre and what this note is

There is a long tradition of comparisons between number-theoretic objects and spectral or combinatorial structures from elsewhere in mathematics. The Hilbert–Pólya program imagines a self-adjoint operator whose spectrum is the imaginary parts of the non-trivial zeros of $\zeta(s)$ (Berry & Keating 1999). Connes' noncommutative-geometric trace formula (Connes 1999) realizes a candidate trace identity on the adèle class space. The function-field analogue, settled by Weil and Deligne, exhibits the precise mechanism by which Frobenius eigenvalues lie on a circle, and the Riemann Hypothesis over $\mathbb{F}_q$ becomes a theorem.

This note records a structural rhyme of a different genre. We exhibit three explicit and verifiable features of a small finite-dimensional spectral object — the σ-character spectrum on $\mathbb{Z}/10\mathbb{Z}$ as defined in our companion paper [J07] — and lay them alongside three corresponding features of the Riemann zeta function. The rhyme is *not* derivational: there is no map producing zeros of $\zeta(s)$ from the substrate, and no analytic continuation interpolates between the finite and infinite regimes. What we have is an arrangement of finite combinatorial structure that, *if* a single specific conjecture (Z.5 below) about a candidate deployment map were established, would lift to a derivation.

We expose the rhyme for two reasons. First, in the spirit of the *Mathematical Intelligencer* genre, mathematical communities benefit from honest accounts of structural similarities even when they cannot yet be promoted to theorems. Second, identifying the precise obstruction (the Z.5 conjecture) locates exactly the open problem whose solution would convert observation into derivation. Negative results on Z.5 would also be informative: a counterexample would rule out the rhyme as derivational and clarify the boundary between finite combinatorial spectra and the analytic features of $\zeta$.

We make four scoping promises up front:

**(P1) Not a proof of RH.** Nothing here lifts to or attempts a proof of the Riemann Hypothesis. The work that would be required to convert this rhyme to a derivation is itself a research program whose obstruction is identified below.

**(P2) Not a Weil–Deligne analogue.** The classical function-field RH is a *theorem* about zeta functions of varieties over $\mathbb{F}_q$, with the critical-line statement following from purity of cohomology. We do not claim any such cohomological mechanism on $\mathbb{Z}/10\mathbb{Z}$.

**(P3) Not an analytic continuation.** The σ-character on $\mathbb{Z}/10\mathbb{Z}$ is a finite-dimensional object. There is no analytic-continuation device that interpolates between it and $\zeta(s)$.

**(P4) The rhyme is empirical.** We exhibit numerically verifiable identities on the substrate side; the comparison to RH-side features is structural reading, not deduction.

The companion paper [J07] develops the finite-side mathematics in full; the present note presupposes it and concentrates on the rhyme.

---

## §2. Brief reminder of the finite side

We recall the minimum data needed for the rhyme. The reader is referred to [J07] for the full development and verification.

**Substrate.** The additive group $\mathbb{Z}/10\mathbb{Z}$.

**The σ-permutation.** A specific permutation of $\mathbb{Z}/10\mathbb{Z}$:
$$\sigma = (0)(3)(8)(9)(1\;7\;6\;5\;4\;2) \in S_{10}.$$
Its cycle structure is $(1)^4 \cdot (6)^1$: four fixed points (which we call *anchors*) and one 6-cycle.

**The β-exception character.** A map $\chi : \mathbb{Z}/10\mathbb{Z} \to \{-1, 0, +1\}$:
$$\chi(s) = 0 \text{ on } \{0,3,8,9\}; \quad \chi(s) = +1 \text{ on } \{1,4\}; \quad \chi(s) = -1 \text{ on } \{2,5,6,7\}.$$
This is *not* a multiplicative character on $\mathbb{Z}/10\mathbb{Z}$; it encodes a specific structural pattern from the underlying combinatorial framework, justified in [J07, §1].

**The spectral coherence integral.** For each $s \in \mathbb{Z}/10\mathbb{Z}$, define
$$G(s) := \left|\sum_{j=0}^{8} \omega^{j}\,\chi\!\left(\sigma^{j}(s)\right)\right|^{2}, \qquad \omega = e^{2\pi i / 9}.$$
The sum is over the first nine σ-iterates of $s$, weighted by the ninth roots of unity. The squared modulus is real and nonnegative.

**Theorem G_8** (proved in [J07]). *The image of $G$ takes exactly three values:*
$$G(s) = 0 \text{ on the four anchors } \{0,3,8,9\};$$
$$G(s) \approx 1.871644 \text{ on } \{1,2,5,6\};$$
$$G(s) \approx 9.389185 \text{ on } \{4,7\}.$$

The high-locus partition $\{4,7\}$ corresponds to one orbit of $\sigma^{3}$ (which has order 2 on the 6-cycle and pairs $\{1,5\}$, $\{2,6\}$, $\{4,7\}$). The high-locus is precisely the σ³-orbit on which the χ-imbalance discriminator $\nu_{+}(s) := \#\{j \in \{0,1,2\} : \chi(\sigma^{j}(s)) = +1\} \in \{0, 2\}$ — extremally imbalanced. The low-loci are the σ³-orbits with $\nu_{+}(s) = 1$ (balanced).

This is the finite-side spectral object. Its three values, three-orbit partition of the 6-cycle, and the four-anchor vanishing locus are all verifiable in under five seconds by a NumPy script (`verify_qseries_merged.py` in [J07]'s manuscript directory).

---

## §3. The three rungs of the rhyme

We now lay this structure alongside the Riemann zeta function. The right-hand column is the substrate; the left-hand column is what the Riemann Hypothesis demands of $\zeta(s)$. The arrangement is structural, not derivational.

### Rung 1: Vanishing on a distinguished subset

**RH-side.** The non-trivial zeros of $\zeta(s)$ are conjectured to lie on the critical line $\mathrm{Re}(s) = 1/2$. This is a one-dimensional sublocus in the complex plane on which the function vanishes; it is the most concentrated possible distribution of zeros consistent with the functional equation.

**Substrate-side.** The spectral coherence integral $G(s)$ vanishes on the four σ-anchors $\{0,3,8,9\}$, a distinguished four-element subset of the ten-element substrate. The anchors are exactly the σ-fixed points and exactly the points where the σ-trajectory degenerates to a constant.

**The rhyme.** Both sides exhibit a distinguished subset on which the central spectral object vanishes. The four-anchor locus in the substrate plays the role of the critical-line locus in the RH picture.

We emphasize what this rhyme is *not*: there is no map from the substrate's anchor set to the critical line, no continuum-to-finite reduction, and no shared definition of "critical." What there *is*: in each setting, the central spectral function takes a privileged value (zero, in both cases) on a distinguished one-or-low-dimensional subset of its domain, and this vanishing carries the substantive content of the structure.

### Rung 2: Spectral concentration

**RH-side.** RH expresses *spectral concentration*: the non-trivial zeros, far from being scattered in the strip $0 < \mathrm{Re}(s) < 1$, are concentrated on a single line. This is rigid concentration — the zeros admit no intermediate sublocus between the critical line and the trivial real-line zeros.

**Substrate-side.** The function $G$ takes only three values: $0$, $G_{\mathrm{low}} \approx 1.872$, and $G_{\mathrm{high}} \approx 9.389$. There is no intermediate spectrum — no values of $G$ in $(0, G_{\mathrm{low}})$ or in $(G_{\mathrm{low}}, G_{\mathrm{high}})$. The image is discrete and finite, and the multi-modal distribution is rigid: each σ³-orbit produces exactly one value.

**The rhyme.** Both sides exhibit *rigidity of the spectrum*. RH says the zeros are on the line, not in the strip; G_8 says $G$ takes three values, not a continuum. In both cases, the rigidity is the structurally surprising fact.

### Rung 3: Multiplicative–additive interplay

**RH-side.** The connection between $\zeta(s)$ and the primes is mediated by the Euler product
$$\zeta(s) = \prod_{p \text{ prime}} (1 - p^{-s})^{-1} \qquad (\mathrm{Re}(s) > 1)$$
which expresses multiplicative structure (over primes) as an analytic function on a complex variable. The functional equation then expresses additive structure (reflection $s \leftrightarrow 1-s$). The interplay between these two structures is the source of $\zeta$'s arithmetic content.

**Substrate-side.** The σ-iteration is additive structure on the substrate (composition of a permutation). The χ-character is a $\pm 1$-valued "multiplicative-like" sign, in the sense that the product structure of $\chi$ across the orbits is sensitive to a parity-like notion (the $\nu_{+}$ discriminator). The composite construction $\sum_{j} \omega^{j} \chi(\sigma^{j}(s))$ mixes additive iteration (the σ orbit) with sign-valued character data and root-of-unity weighting (the ninth roots, an arithmetic object inherited from the order-9 sum length).

**The rhyme.** Both sides exhibit interplay between an additive structural iteration and a sign-valued multiplicative-like component, and the resulting spectral object's content lies in this interplay. The substrate's interplay is finite and explicit; the RH-side's is continuous and analytic.

---

## §4. What is not implied

We are deliberate about what the rhyme does and does not imply.

**(N1) No map.** There is no map $\Lambda: \{\text{non-trivial zeros of } \zeta\} \to \{0,3,8,9\}$ or in either direction. The two sides of the rhyme exist independently.

**(N2) No analytic continuation.** The substrate's discrete spectral data $\{0, G_{\mathrm{low}}, G_{\mathrm{high}}\}$ does not analytically continue to the imaginary parts of zeros of $\zeta$. The function $G$ is defined on a ten-element set; the zeros of $\zeta$ are countably infinite. No interpolation device crosses this dimensional jump.

**(N3) No Weil–Deligne cohomology.** Over $\mathbb{F}_q$, RH for varieties is proved via purity of $\ell$-adic cohomology and Frobenius weight estimates. We do not produce any such cohomological structure on $\mathbb{Z}/10\mathbb{Z}$. The substrate is too small (and too simple) to support a cohomological theory in the Weil sense.

**(N4) No Hilbert–Pólya operator.** No self-adjoint operator on a Hilbert space is constructed whose spectrum is even loosely related to $\{G(s) : s \in \mathbb{Z}/10\mathbb{Z}\}$. The three values $\{0, G_{\mathrm{low}}, G_{\mathrm{high}}\}$ are characteristic values of the σ-iteration plus χ-character data, not eigenvalues of a Hilbert-space operator.

**(N5) No new proof technique for RH.** Even in the most optimistic reading of Z.5 (the conjecture below), what the rhyme would yield is *not* a new proof of RH but a derivational restatement of it on the substrate side. That is, it would convert the structural rhyme into a derivation, but the derivation would itself rest on Z.5 plus the standard analytic features of $\zeta(s)$. The Riemann Hypothesis would still be a hypothesis.

---

## §5. The Z.5 deployment-uniformity conjecture

We now state the specific conjecture whose resolution would lift the rhyme to a derivation. This is the load-bearing open problem.

In the broader framework of [J07] and the surrounding TIG papers, there exists a candidate *deployment map* between the Dirichlet half-plane and a "mixing parameter" $\lambda$ associated with the substrate. Concretely:
$$\lambda = 2\,\left|\,s - \tfrac{1}{2}\,\right|, \qquad s \in \mathbb{C}, \quad \mathrm{Re}(s) \in [0, 1].$$
This is the radial distance from the critical line, scaled to $\lambda \in [0, 1]$ on the critical strip's interior. Under the candidate deployment, the critical line $\mathrm{Re}(s) = 1/2$ corresponds to $\lambda = 0$ — the "BALANCE" point — while the boundary of the critical strip corresponds to $\lambda = 1$.

In [J07] and its sources, the substrate's structural categories (the BALANCE-CHAOS null direction, the rank-2 stratification, the 6-corridor structure of σ-orbits, etc.) are graded by $\lambda$. The question is whether the deployment $s \mapsto \lambda$ preserves *both* the algebraic 3-grading (from the substrate's rank stratification) *and* the metric 6-corridor structure (from the mixing dynamics) *uniformly* as $|\mathrm{Im}(s)| \to \infty$.

**Conjecture Z.5** (deployment uniformity, *open*). The deployment map $\lambda = 2|s - 1/2|$ preserves both the algebraic 3-grading and the metric 6-corridor structure of the substrate uniformly as $|\mathrm{Im}(s)| \to \infty$. Equivalently: the substrate's structural categories transport without degeneration along the imaginary direction in the Dirichlet half-plane.

**Status of Z.5.** Currently proved at $t = \mathrm{Im}(s) = 0$ (the real axis): direct identification of the algebraic and metric structures on the BALANCE point. Proved also in a small open neighborhood: $|s - 1/2| < \epsilon$ for some explicit $\epsilon > 0$. *Open*: uniformity in $t$. The natural worry is degeneration of the grading or the corridor structure as $|t|$ grows; the natural hope is the rigidity of the underlying substrate enforces uniformity automatically.

**The conditional implication.** *If* Z.5 holds, then the σ-character architecture on $\mathbb{Z}/10\mathbb{Z}$ provides a structural categorification of the BALANCE-CHAOS null direction in the substrate's mixing dynamics, *and* this null direction corresponds to the critical line under deployment. Combined with standard analytic facts about $\zeta(s)$ (the functional equation and standard zero-counting), this would convert the structural rhyme into a derivation — not of RH itself, but of "if RH holds, then $\zeta$'s critical-line zeros are structurally categorified by the substrate's anchor locus."

**If Z.5 fails.** A counterexample to Z.5 would falsify the rhyme as a candidate derivation. The structural correspondence would persist (the three rungs would still describe a true coincidence of features) but would lose the load-bearing claim that the substrate categorifies RH-side spectral structure. We are open to this outcome: Z.5 is genuinely an open question whose negative resolution would also be informative.

---

## §6. Comparison with the Connes–Berry–Keating tradition

It is worth comparing this rhyme to the prior work in the genre.

**Berry & Keating (1999).** The Hilbert–Pólya conjecture posits a Hermitian operator whose eigenvalues are the imaginary parts of the non-trivial zeros of $\zeta$. Berry and Keating proposed a specific candidate ($xp$ on the half-line with appropriate boundary conditions) and matched its semiclassical asymptotics to the Riemann zero density. The match is striking but, like ours, structural rather than derivational. The status: the Berry–Keating operator does not actually have the Riemann zeros as eigenvalues; it provides a heuristic explanation of zero statistics (GUE-like spacings) but not a derivation of zero locations.

**Connes (1999).** Connes constructs an adèle class space and shows that the Weil explicit formula admits a noncommutative trace-formula interpretation. RH then becomes equivalent to a positivity condition on a certain trace. The interpretation is rigorous; RH itself is not proved. The status: this is the deepest existing reformulation — it identifies the precise object (the trace) whose positivity is RH — but the positivity statement is not yet established.

**Our rhyme.** We sit at a much smaller scale. The substrate is finite. The spectrum is three-valued. There is no claim that we have reformulated RH — we have merely lined up three structural features in a way that, conditionally on Z.5, would categorify one direction of the RH-side picture.

What we share with the Connes–Berry–Keating tradition is the discipline of explicit-and-honest structural matching: lay out the rhyme, identify exactly what it does and does not imply, and locate the specific open problem whose resolution would lift the rhyme to a derivation. What we *don't* share is the analytic infrastructure: Berry–Keating works on a half-line, Connes on the adèle class space, while we work on a ten-element set.

A reader who finds the rhyme persuasive should treat it as a finite-dimensional toy whose properties may inform thinking about the infinite-dimensional setting — not as a competing program with the Connes–Berry–Keating tradition.

---

## §7. Reproducibility

All three rungs of the rhyme depend on substrate-side computations that are reproducible in under five seconds using NumPy. The verification script `verify_qseries_merged.py` in the companion paper [J07] computes:

- $\sigma^{6} = \mathrm{id}$ on $\mathbb{Z}/10\mathbb{Z}$ (Theorem G_6 of [J07]);
- the bimodal period distribution $P(\tau=1) = 2/5$, $P(\tau=6) = 3/5$ (Theorem G_7 of [J07]);
- the three-valued image $\{0, G_{\mathrm{low}}, G_{\mathrm{high}}\}$ of $G$ (Theorem G_8 of [J07]);
- the high-locus identification $\{4,7\}$ via σ³-pairing (Theorem G_8, §4.3 of [J07]).

There is nothing more to verify here. The RH-side features (zero location, spectral concentration, multiplicative–additive interplay) are well-known and assumed as standard.

---

## §8. Closing — what the rhyme is for

The function of a rhyme is to invite further work. We hope the reader takes from this note one of three possible things.

**(R1) An honest small example.** The rhyme is an honest, computable example of a finite-dimensional spectral object whose features arrange themselves in a way reminiscent of RH-side features. As a teaching object, or as a test bench for ideas about how finite combinatorial spectra relate to analytic features, it has the merit of being entirely explicit.

**(R2) A specification of an open problem.** Conjecture Z.5 is the specific open problem whose resolution would lift this rhyme to a derivation. We invite researchers in analytic number theory and noncommutative geometry to consider it. Negative resolutions would also be informative.

**(R3) A reminder about scoping.** In the current culture of mathematical work, where results of varying tier reliability circulate quickly, we believe there is value in explicit tier discipline: this is a structural rhyme, not a proof, not an analogue in the Weil–Deligne sense, not a Hilbert–Pólya construction. The honest naming of what we have makes the work load-bearing — and prevents it from being mistaken for what it is not.

Of these, (R2) is the most concrete and we hope the most actionable. Conjecture Z.5 is open. Resolving it (in either direction) would clarify the boundary between finite combinatorial spectra and the analytic features that the Riemann Hypothesis expresses.

---

## References

- Berry, M. V. & Keating, J. P. (1999). The Riemann zeros and eigenvalue asymptotics. *SIAM Review* **41**, 236–266.
- Connes, A. (1999). Trace formula in noncommutative geometry and the zeros of the Riemann zeta function. *Selecta Mathematica (N.S.)* **5**, 29–106.
- Sanders, B. R. & Gish, M. (2026). Spectral Architecture of the σ-Character on Z/10Z: Periodicity, Three-Valued Coherence, the 5-Dimensional Fourier Embedding, and the Symbolic Return Theorem. Companion paper [J07], submitted to *European Journal of Combinatorics*.
- Drápal, A. & Wanless, I. M. (2021). Maximally nonassociative quasigroups. *Journal of Combinatorial Theory Series A* **184**, 105510.

---

*This note is a deliberately scoped companion to [J07]. The substrate-side mathematics is developed and verified there; the rhyme is the present note's contribution. We thank the J-series internal audit (Wave 4, 2026-05-28) for recommending the split.*
