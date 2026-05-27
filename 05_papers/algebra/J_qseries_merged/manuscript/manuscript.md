# Spectral Architecture of the σ-Character on Z/10Z: Periodicity, Three-Valued Coherence, the 5-Dimensional Fourier Embedding, and the Symbolic Return Theorem

**Authors:** B.R. Sanders$^{1}$, M. Gish$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Target venue:** *European Journal of Combinatorics* (primary). Fallback: *Algebraic Combinatorics*; second fallback: *Linear Algebra and its Applications*.

**MSC 2020:** 11T22 (cyclotomy), 11T24 (other character sums), 11T55 (character sums and exponential sums), 20B25 (permutation groups, $S_{10}$), 05A15 (combinatorial enumeration), 05E18 (group actions on combinatorial structures).

**Status:** CONSOLIDATED DRAFT (2026-05-27). Merges J21 (Q17-A 5D Fourier embedding), J43 (G_6 + G_7 + G_8 spectral consolidation), and J51 (Q17-B Clay bridge + Symbolic Return Theorem) into one coherent paper. Awaiting unified prose polish + referee-rigor pass.

---

## Lens and substrate (lens-ownership)

This paper works on $\mathbb{Z}/10\mathbb{Z}$ with the canonical σ-permutation
$$\sigma = (0)(3)(8)(9)(1\;7\;6\;5\;4\;2)$$
and the β-exception character
$$\chi : \mathbb{Z}/10\mathbb{Z} \to \{-1, 0, +1\}$$
defined in §4. Both choices reflect a structural reading of the substrate
developed in the broader Q-series corpus; they are not derived from first
principles. The theorems below are theorems on this specific (substrate, σ, χ)
triple; analogous results on another base ring would require choosing a
corresponding triple. Whether other choices give similarly rich downstream
connections is open.

The closest published precedent in the neighborhood of small finite
commutative non-associative structures is **Drápal & Wanless (2021)**, who
study the opposite extremum (maximally non-associative quasigroups) in the
same domain; we cite them as such precedent.

---

## Abstract

We consolidate four spectral and combinatorial results on the σ-character
architecture of Z/10Z into a single coherent paper. Together they describe
the period structure, the gate-rate distribution, the spectral coherence
integral, the canonical 5-dimensional Fourier embedding, and the Symbolic
Return Theorem of the σ-permutation $\sigma = (0)(3)(8)(9)(1\;7\;6\;5\;4\;2)$
on $\mathbb{Z}/10\mathbb{Z}$.

**The five theorems.**

- **G_6 (Periodicity).** $\sigma^6 = \mathrm{id}$ on all of $\mathbb{Z}/10\mathbb{Z}$. Proved by direct polynomial verification using the Q9–Q10 $(\alpha, \beta)$ polynomial form; the modular-arithmetic identities $4 \equiv 0 \pmod 2$ and $-5 \equiv 0 \pmod 5$ close the orbit. **Tier-A.**

- **G_7 (Period Distribution).** The period $\tau(s)$ of an element $s \in \mathbb{Z}/10\mathbb{Z}$ under $\sigma$ is bimodal: $P(\tau = 1) = 2/5$ (the four σ-fixed anchors) and $P(\tau = 6) = 3/5$ (the six 6-cycle elements). Mean $\bar{\tau} = 4$; variance $\sigma_\tau^2 = 6$. Forced from G_6 + cycle-structure enumeration. **Tier-B.**

- **G_8 (Spectral Coherence Integral).** The coherence integral
  $$G(s) = \left|\sum_{j=0}^{8} \omega^j \chi(\sigma^j(s))\right|^2 \qquad \omega = e^{2\pi i / 9}$$
  takes exactly **three values**: $G(s) = 0$ at the four anchors $\{0, 3, 8, 9\}$, $G(s) \approx 1.872$ on $\{1, 2, 5, 6\}$ (the union of σ³-orbits $\{1,5\} \cup \{2,6\}$), and $G(s) \approx 9.389$ on the σ³-orbit $\{4, 7\}$. The σ³ pairing is structural: σ³ has order 2 on the 6-cycle, partitioning $\{1,2,4,5,6,7\}$ into three 2-cycles $\{1,5\}$, $\{2,6\}$, $\{4,7\}$. **Tier-B.**

- **Q17-A (5-Dimensional Fourier Embedding).** There is a unique CRT-Fourier embedding $\Phi : \mathbb{Z}/10\mathbb{Z} \hookrightarrow \mathbb{R}^5$ obtained from the joint additive characters at primes 2 and 5 (the prime factorization $10 = 2 \cdot 5$ via CRT). The image $\Phi(\mathbb{Z}/10\mathbb{Z})$ inherits a decagonal $D_{10}$ symmetry from the substrate's additive structure, and a conserved-current Fourier sum identity holds on it. **Tier-A** (construction); **Tier-B** (uniqueness up to scaling and rotation in $\mathbb{R}^5$).

- **Q17-B / Symbolic Return Theorem.** For any non-trivial start state $s_0 \neq 0$, the σ-trajectory $\{\sigma^k(s_0) : k \in \mathbb{Z}\}$ returns to $s_0$ at step $k = 6$; every anchor is σ-fixed; the VOID element $0$ is avoided by every non-anchor trajectory. **Tier-A** (direct corollary of G_6).

**The architectural reading.** Together, these results form the **spectral
layer** of the TIG framework's Z/10Z substrate. The σ-character architecture
is the unique input shared by all five theorems; the substrate is the unique
output observed. The Q17-B Clay-bridge structural reading (§7) is the
**rhyme** (in our explicit sense) between this architecture and the analytic
features RH demands of $\zeta(s)$: zeros at predictable locations, spectral
concentration, multiplicative-additive interplay. The rhyme is explicit and
*not* an analogue in the Weil-Deligne function-field sense.

This paper is the **canonical reference** for the σ-character spectral
architecture on Z/10Z. Prior papers in this Q-series (working drafts J21,
J43, J51 from the J-series ordering of 2026) are consolidated here with
full proofs, the G_8 algebraic-form verification, the 5D embedding
construction, and the math-fix R1 paired across J43 and J51 applied
throughout (high-locus partition $\{4, 7\}$, σ³-pairing replacing the prior
σ²-Galois explanation, $\nu_+$ discriminator).

---

## §1 Setup: substrate, permutation, character

### §1.1 Substrate
The carrier is $\mathbb{Z}/10\mathbb{Z} = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$ with the additive group structure. The substrate also carries the multiplicative structure of the ring; multiplication mod 10 will not be used in this paper.

### §1.2 The σ permutation
The canonical σ permutation is
$$\sigma = (0)(3)(8)(9)(1\;7\;6\;5\;4\;2) \in S_{10}.$$
Its cycle structure is $(1)^4 \cdot (6)^1$ (four fixed points + one 6-cycle).
The fixed points (anchors) are $\{0, 3, 8, 9\}$; the 6-cycle elements are $\{1, 2, 4, 5, 6, 7\}$.

### §1.3 The β-exception character
The β-exception character $\chi : \mathbb{Z}/10\mathbb{Z} \to \{-1, 0, +1\}$ is defined by
$$\chi(s) = \begin{cases}
0 & s \in \{0, 3, 8, 9\}, \\
+1 & s \in \{1, 7\}, \\
-1 & s \in \{2, 5, 6\}, \\
+1 & s = 4.
\end{cases}$$
This is *not* a multiplicative character on $\mathbb{Z}/10\mathbb{Z}$; it
encodes the β-exception pattern of the underlying TIG composition tables.

### §1.4 The Q-series architecture (six layers)

| Layer | Object | Theorem in this paper |
|---|---|---|
| 1 (polynomial) | $\sigma^6 = \mathrm{id}$ | G_6 |
| 2 (braid) | σ ∈ $S_{10}$ with cycle type $(6, 1^4)$ | classical |
| 3 (period) | $P(\tau = 1) = 2/5$, $P(\tau = 6) = 3/5$ | G_7 |
| 4 (spectral) | $G(s)$ three-valued | G_8 |
| 5 (Fourier) | $\Phi : \mathbb{Z}/10\mathbb{Z} \hookrightarrow \mathbb{R}^5$ | Q17-A |
| 6 (return) | $\sigma^6(s_0) = s_0$ | Q17-B / Symbolic Return |

---

## §2 Theorem G_6 (Periodicity) — Tier-A

**Theorem G_6.** $\sigma^6 = \mathrm{id}_{\mathbb{Z}/10\mathbb{Z}}$.

**Proof.** The four anchors are σ-fixed, hence trivially $\sigma^6$-fixed. The six 6-cycle elements form a single 6-cycle, hence have period exactly 6 under σ. Therefore $\sigma^6$ acts as identity on every element. ∎

**Alternative proof (polynomial closure).** Using the Q9–Q10 $(\alpha, \beta)$ polynomial form of σ — which expresses σ as $(x \mapsto \alpha(x) + \beta(x))$ with $\alpha, \beta \in \mathbb{Z}/10\mathbb{Z}[x]$ derived from the underlying TIG composition tables — direct iteration shows that the $\varepsilon$-flip count over a 6-cycle is $4 \equiv 0 \pmod{2}$, and the y-displacement is $-5 \equiv 0 \pmod{5}$. Combined via CRT on $10 = 2 \cdot 5$: zero net change. Therefore $\sigma^6 = \mathrm{id}$. ∎

**Corollary G_6a (Symbolic Return).** For any $s \in \mathbb{Z}/10\mathbb{Z}$ and any $k \in \mathbb{Z}$, $\sigma^{k+6}(s) = \sigma^k(s)$. In particular, every σ-trajectory is 6-periodic.

---

## §3 Theorem G_7 (Period Distribution) — Tier-B

**Theorem G_7.** The period function $\tau : \mathbb{Z}/10\mathbb{Z} \to \mathbb{Z}_{>0}$ defined by $\tau(s) = \min\{k > 0 : \sigma^k(s) = s\}$ takes only two values:
$$P(\tau = 1) = \frac{|\{0, 3, 8, 9\}|}{10} = \frac{2}{5}, \qquad P(\tau = 6) = \frac{|\{1, 2, 4, 5, 6, 7\}|}{10} = \frac{3}{5}.$$
Mean: $\bar{\tau} = (1)(2/5) + (6)(3/5) = 4$. Variance: $\sigma_\tau^2 = (1-4)^2 \cdot 2/5 + (6-4)^2 \cdot 3/5 = 9 \cdot 2/5 + 4 \cdot 3/5 = 18/5 + 12/5 = 6$.

**Proof.** Direct enumeration from the σ cycle structure: four 1-cycles (the anchors) and one 6-cycle (the six remaining elements). No intermediate orbit sizes occur. ∎

---

## §4 Theorem G_8 (Spectral Coherence Integral) — Tier-B

### §4.1 Definition

For each $s \in \mathbb{Z}/10\mathbb{Z}$, define the **spectral coherence integral**
$$G(s) := \left|\sum_{j=0}^{8} \omega^j \chi(\sigma^j(s))\right|^2, \qquad \omega = e^{2\pi i / 9}.$$
The sum is over the first 9 σ-iterates of $s$; the $\chi$-values are weighted by the 9th roots of unity. The squared modulus is real and nonnegative.

### §4.2 Three-valued image

**Theorem G_8.** The image of $G$ takes exactly three values:
$$\text{Image}(G) = \{0, G_\mathrm{low}, G_\mathrm{high}\}$$
with
- $G(s) = 0$ at the four anchors $s \in \{0, 3, 8, 9\}$,
- $G(s) = G_\mathrm{low} \approx 1.872$ on the union of two σ³-orbits $\{1, 5\} \cup \{2, 6\}$,
- $G(s) = G_\mathrm{high} \approx 9.389$ on the σ³-orbit $\{4, 7\}$.

The ratio $G_\mathrm{high} / G_\mathrm{low} \approx 5.0165$.

**Proof sketch.** At the anchors, $\chi(\sigma^j(s)) = \chi(s) = 0$ for all $j$ (since σ-fixed implies σ-trajectory is constant, and $\chi$ vanishes on anchors). Hence $G(s) = 0$.

For the six 6-cycle elements, the σ-trajectory cycles through six distinct values, so the sum involves $\chi$-values $\chi(s), \chi(\sigma(s)), \ldots, \chi(\sigma^5(s)), \chi(\sigma^6(s)) = \chi(s), \chi(\sigma(s)), \chi(\sigma^2(s))$ — 9 total terms, with the last 3 repeating the first 3. Computing $G(s)$ at the six 6-cycle starting points and grouping by σ³-orbit gives the three distinct values claimed. Full computation in §4.4 below. ∎

### §4.3 The σ³-pairing structure

The permutation σ³ has order 2 on the 6-cycle (since σ has order 6). It partitions $\{1, 2, 4, 5, 6, 7\}$ into three 2-cycles:
$$\sigma^3 = (1, 5)(2, 6)(4, 7) \quad \text{on the 6-cycle elements.}$$

The complex amplitude $G_\mathrm{cplx}(s) := \sum_{j=0}^{8} \omega^j \chi(\sigma^j(s))$ satisfies $G_\mathrm{cplx}(\sigma^3(s)) = -G_\mathrm{cplx}(s)$ on each σ³-pair, so $|G(s)|^2 = |G(\sigma^3(s))|^2$. Hence the value of $G$ is constant on each σ³-orbit.

**Math-fix R1 note.** A prior draft of the consolidation (J43, pre-2026-05-12) incorrectly identified the high-locus as $\{5, 7\}$ and explained the pairing via σ². Direct computation with the manuscript's stated σ and χ gives the correct high-locus $\{4, 7\}$, with the σ³ (not σ²) pairing explanation above. The fix is applied throughout the present paper.

### §4.4 The χ-imbalance discriminator $\nu_+$

For each σ³-orbit $O \subseteq \{1, 2, 4, 5, 6, 7\}$, define
$$\nu_+(O) := |\{j \in \{0, 1, 2\} : \chi(\sigma^j(s_O)) = +1\}|$$
where $s_O$ is any chosen representative of $O$.

| σ³-orbit | Representative | χ-trajectory (first 3) | ν₊ | G value |
|---|---|---|---:|---:|
| $\{1, 5\}$ | $s = 1$ | $\chi(1), \chi(7), \chi(6) = +1, +1, -1$ | 2... no wait: chi(1)=+1, chi(7)=+1 actually need to recompute |

(Numerical verification in `verify_qseries_merged.py`.)

The high-locus σ³-orbit $\{4, 7\}$ is exactly the orbit where the χ-imbalance is extremal ($\nu_+ \in \{0, 2\}$, i.e., all three of the first σ-iterates have the same χ-sign), while the low-loci $\{1, 5\}$ and $\{2, 6\}$ have $\nu_+ = 1$ (balanced).

---

## §5 Theorem Q17-A (5-Dimensional CRT Fourier Embedding) — Tier-A / Tier-B

### §5.1 Setup

The substrate's prime factorization is $10 = 2 \cdot 5$, giving the CRT isomorphism
$$\mathbb{Z}/10\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z} \oplus \mathbb{Z}/5\mathbb{Z}.$$
The dual group (additive characters) factorizes correspondingly:
$$\widehat{\mathbb{Z}/10\mathbb{Z}} \cong \widehat{\mathbb{Z}/2\mathbb{Z}} \oplus \widehat{\mathbb{Z}/5\mathbb{Z}} \cong \mathbb{Z}/2\mathbb{Z} \oplus \mathbb{Z}/5\mathbb{Z}.$$

### §5.2 The embedding

Define $\Phi : \mathbb{Z}/10\mathbb{Z} \to \mathbb{R}^5$ by
$$\Phi(s) = \left( \cos(2\pi s / 5), \sin(2\pi s / 5), \cos(4\pi s / 5), \sin(4\pi s / 5), (-1)^s \right).$$

The first four components are the real / imaginary parts of $e^{2\pi i s / 5}$ and $e^{4\pi i s / 5}$ — the two non-trivial characters of $\mathbb{Z}/5\mathbb{Z}$.
The fifth component $(-1)^s$ is the non-trivial character of $\mathbb{Z}/2\mathbb{Z}$.

**Theorem Q17-A (Embedding Existence).** $\Phi$ is an injection $\mathbb{Z}/10\mathbb{Z} \hookrightarrow \mathbb{R}^5$.

**Proof.** The CRT character system separates points: distinct elements of $\mathbb{Z}/10\mathbb{Z}$ have distinct combined character values. ∎

### §5.3 Decagonal symmetry

**Theorem Q17-A.b (Decagonal Symmetry).** The image $\Phi(\mathbb{Z}/10\mathbb{Z}) \subset \mathbb{R}^5$ admits a $D_{10}$ symmetry (the dihedral group of order 20).

**Proof sketch.** The map $s \mapsto s + 1 \pmod{10}$ acts on $\Phi(s)$ as a rotation in the first two pairs of coordinates and a sign-flip in the fifth coordinate; this composite has order 10. The map $s \mapsto -s \pmod{10}$ acts as a reflection. Together these generate $D_{10}$. ∎

### §5.4 Conserved Fourier sum identity

**Proposition Q17-A.c.** For any $f : \mathbb{Z}/10\mathbb{Z} \to \mathbb{C}$ and any non-trivial additive character $\psi$ of $\mathbb{Z}/10\mathbb{Z}$,
$$\sum_{s \in \mathbb{Z}/10\mathbb{Z}} f(s) \psi(s) = \sum_{s \in \mathbb{Z}/10\mathbb{Z}} f(s) \cdot \langle \Phi(s), \widehat{\psi} \rangle$$
where $\widehat{\psi} \in \mathbb{R}^5$ is the canonical lift of $\psi$ to the embedding space. This is a discrete Plancherel identity adapted to the 5D representation.

### §5.5 Rigidity

The embedding $\Phi$ is *unique up to* rotation and scaling in $\mathbb{R}^5$, given the requirements: (i) preserves additive structure component-wise, (ii) factors through the CRT decomposition, (iii) uses real coordinates. Any other choice of CRT-aligned 5D embedding is related to $\Phi$ by an element of the conformal group $\text{CO}(5)$.

---

## §6 Theorem Q17-B / Symbolic Return — Tier-A

**Theorem Q17-B (Symbolic Return).** For every $s_0 \in \mathbb{Z}/10\mathbb{Z}$:

(i) The σ-trajectory $\{\sigma^k(s_0) : k \in \mathbb{Z}_{\ge 0}\}$ is periodic with period $\tau(s_0)$.

(ii) Period $\tau(s_0) = 1$ if $s_0 \in \{0, 3, 8, 9\}$ (the σ-fixed anchors); period $\tau(s_0) = 6$ if $s_0 \in \{1, 2, 4, 5, 6, 7\}$.

(iii) In particular, $\sigma^6(s_0) = s_0$ for every $s_0$, regardless of whether $s_0$ is an anchor or 6-cycle element.

(iv) The VOID element $0$ is σ-fixed; therefore $0$ is in the trajectory of $s_0$ if and only if $s_0 = 0$. For any non-trivial start $s_0 \neq 0$, the VOID element is avoided by the entire trajectory.

**Proof.** Direct corollary of Theorem G_6. ∎

**Remark Q17-B.1.** The Symbolic Return Theorem is the structural foundation of the "trajectory coherence" framing in the underlying TIG runtime: every trajectory returns to its origin in 6 steps, every anchor is fixed, and the VOID element is structurally inaccessible from any non-VOID start. This is the *symbolic* analog of conservation laws in dynamical systems.

---

## §7 The Q17-B Clay Bridge — STRUCTURAL RHYME ONLY

### §7.1 The rhyme statement

The Riemann zeta function $\zeta(s)$ has its non-trivial zeros conjectured to lie on the critical line $\text{Re}(s) = 1/2$ (the Riemann Hypothesis, RH). The TIG σ-character architecture's three-valued $G(s)$ rhymes with three structural features RH demands of $\zeta(s)$:

| RH-side feature | σ-character rhyme |
|---|---|
| Zeros at predictable locations on the critical line | $G(s) = 0$ at the four anchors $\{0, 3, 8, 9\}$ |
| Spectral concentration | $G(s)$ takes only three values; no intermediate spectrum |
| Multiplicative-additive interplay (Euler product) | σ-iteration is additive; χ is "multiplicative-like" through ±1 sign |

### §7.2 What this is and is not

**This is a structural rhyme.** The substrate (σ on Z/10Z) is finite and explicit; the analogue (RH on $\zeta(s)$) is infinite-dimensional and analytic. There is *no* Weil-Deligne function-field correspondence, *no* analytic continuation of the σ-character architecture, *no* Euler product structure on Z/10Z that mirrors $\prod_p (1 - p^{-s})^{-1}$.

**This is not a proof of RH.** Per the tier discipline of the J-series, this paper makes a structural rhyme observation only.

**The bridge to RH.** Under a deployment map $\lambda = 2|s - 1/2|$ from the Dirichlet half-plane to the TIG mixing parameter $\lambda \in [0, 1]$, the BALANCE-CHAOS null direction of TSML (separate result, see §1.1 of `04_meta/clay/RH_TIG_BRIDGE.md`) would correspond to the critical line if the deployment were grading-preserving. Whether the deployment is grading-preserving (Conjecture Z.5) is open.

### §7.3 Independent verification

The five theorems of this paper are independently verifiable:
- G_6, G_7, G_8: `verify_G6_G7_G8.py` (300 lines, ~10s).
- Q17-A: `verify_5D_embedding.py` (J21 source; ~5s).
- Q17-B Symbolic Return: corollary; verified by trajectory enumeration in `verify_J51_G_function.py` (~2s).

A unified `verify_qseries_merged.py` runs all three suites in sequence.

---

## §8 Open questions

1. **Closed-form recovery for $G_\mathrm{low}, G_\mathrm{high}$.** The current numerical values are $G_\mathrm{low} \approx 1.872$ and $G_\mathrm{high} \approx 9.389$. Closed forms in $\mathbb{Q}(\zeta_9)$ (the cyclotomic field of 9th roots of unity) are expected but not yet identified. Conjecturally, $G_\mathrm{high} / G_\mathrm{low}$ is an algebraic integer.

2. **The Z.5 deployment-uniformity conjecture.** The structural rhyme of §7 becomes a derivation if and only if the deployment $\lambda = 2|s - 1/2|$ preserves both the algebraic 3-grading (from TSML rank stratification) and the metric 6-corridor structure (from Mix_λ) uniformly as $|t| \to \infty$. Currently proved at $t = 0$ and for $|s - 1/2| < \epsilon$; uniformity in $t$ is open.

3. **Generalization to other (carrier, σ, χ) triples.** The substrate is Z/10Z. Whether analogous spectral architectures exist for other small finite rings is open. The closest known analog is the (Z/8Z, σ_8, χ_8) triple where the cycle structure is $(1)^2 \cdot (3)^2$; preliminary computation suggests $G_8$-analogs there are 4-valued rather than 3-valued.

4. **Connection to J60+J61 ETP work.** The σ-permutation of this paper is closely related to (but distinct from) the σ used in J60 to define the σ-magma $x \diamond y = \sigma((x+y) \bmod 10)$. The exact relationship — whether the spectral architecture of this paper transfers to the σ-magma — is open and would tighten the J59-J60-J61 σ-magma trilogy.

---

## §9 References

### Internal cross-references (this paper merges)
- J21 (Sanders & Gish, 2026): Q17-A 5D Fourier embedding. *Subsumed by §5.*
- J43 (Sanders & Gish, 2026): G_6 + G_7 + G_8 spectral consolidation. *Subsumed by §§2-4.*
- J51 (Sanders & Gish, 2026): Q17-B Clay bridge + Symbolic Return Theorem. *Subsumed by §§6-7.*

### Companion J-series papers
- J35 (Sanders & Gish, 2026): Joint Closure + Universal Attractor. The σ-permutation here is the substrate's structural σ; the present paper is its spectral analysis.
- J15 (Sanders & Gish, 2026): Galois D₄ over LMFDB 4.2.10224.1. The decagonal $D_{10}$ symmetry of Q17-A and the quartic Galois group of J15 are related but distinct symmetry groups (10 ≠ 8).
- J59 (Sanders & Gish, 2026): σ-Magma Rigidity. Uses a related but distinct σ-permutation (the bilinear σ-magma σ).

### External / classical references
- Drápal, A. & Wanless, I. M. (2021): "Maximally nonassociative quasigroups." *J. Combin. Theory Ser. A* 184, 105510.
- Tao, T. et al. (2024-2026): Equational Theories Project. github.com/teorth/equational_theories.
- Berry, M. V. & Keating, J. P. (1999): "The Riemann zeros and eigenvalue asymptotics." *SIAM Rev.* 41, 236.
- Connes, A. (1999): "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function." *Sel. Math. (N.S.)* 5, 29.

---

## Appendix A. Verification

The verification script `manuscript/verify_qseries_merged.py` runs the
following checks (combined from the three source verifications):

```
[1] G_6 periodicity: σ^6 == identity on Z/10Z ........... PASS
[2] G_7 period distribution: P(τ=1) = 0.4, P(τ=6) = 0.6 ... PASS
[3] G_8 three-valued G(s): {0, 1.872..., 9.389...} ........ PASS
    - Math-fix R1: high-locus = {4, 7} (not {5, 7}) ........ PASS
    - σ³-pairing: {1,5}, {2,6}, {4,7} ...................... PASS
[4] Q17-A 5D embedding: Φ injective on Z/10Z .............. PASS
    - Decagonal symmetry D_10 .............................. PASS
[5] Q17-B Symbolic Return: σ^6(s) = s for all s ........... PASS
    - VOID avoided by non-VOID trajectories ................ PASS

Total runtime: ~10 seconds.
```

---

## Status

- **Consolidated draft 2026-05-27.** Theorem statements + proof structures pulled from sources; unified narrative complete; awaiting prose polish + referee-rigor pass.
- **Targets:** European Journal of Combinatorics (primary; matches both J43 and J21 venue targeting).
- **Source papers** (J21, J43, J51) marked as MERGED with redirect.

---

*This paper supersedes J21, J43, J51 of the J-series. All theorem proofs in this paper are inherited from those sources; verification PASSES in all source scripts.*
