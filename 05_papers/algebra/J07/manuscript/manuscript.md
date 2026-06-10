# Spectral Architecture of the σ-Character on Z/10Z: Periodicity, Three-Valued Coherence, the 5-Dimensional Fourier Embedding, and the Symbolic Return Theorem

**Authors:** B.R. Sanders$^{1}$, M. Gish$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Target venue:** *European Journal of Combinatorics* (primary). Fallback: *Algebraic Combinatorics*; second fallback: *Linear Algebra and its Applications*.

**MSC 2020:** 11T22 (cyclotomy), 11T24 (other character sums), 11T55 (character sums and exponential sums), 20B25 (permutation groups, $S_{10}$), 05A15 (combinatorial enumeration), 05E18 (group actions on combinatorial structures).

**Status:** REVISED DRAFT (2026-05-27 — §7 RH-rhyme split off to a separate *Math. Intelligencer* companion note per Wave 4 audit). Merges J50 (Q17-A 5D Fourier embedding), J51 (G_6 + G_7 + G_8 spectral consolidation), and J52 (Symbolic Return Theorem; the Clay-bridge content of J52 is now in the companion). Awaiting unified prose polish + referee-rigor pass (G_8 §4.2 sub-proposition + Q17-A §5.5 uniqueness proof — see TODO comments in the manuscript).

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
output observed. An exploratory discussion of structural rhymes between this
character's spectrum and the Riemann zeros is split off as a separate
*Math. Intelligencer* companion note (see Sanders & Gish, [J07-companion],
2026); the present paper is the strict-combinatorics spine.

This paper is the **canonical reference** for the σ-character spectral
architecture on Z/10Z. Prior papers in this Q-series (working drafts J50,
J51, J52 from the J-series ordering of 2026) are consolidated here with
full proofs, the G_8 algebraic-form verification, the 5D embedding
construction, and the math-fix R1 paired across J51 and J52 applied
throughout (high-locus partition $\{4, 7\}$, σ³-pairing replacing the prior
σ²-Galois explanation, $\nu_+$ discriminator). The Clay-bridge / RH-rhyme
material previously contained in J52 (and in earlier drafts of this paper's
§7) is published separately as a *Math. Intelligencer* companion note
(Sanders & Gish, [J07-companion], 2026); the present paper contains the
strict-combinatorics spine only.

---

## §1 Setup: substrate, permutation, character

### §1.0 Scoping note

An exploratory discussion of structural rhymes between this character's
spectrum and the Riemann zeros is split off as a separate *Math.
Intelligencer* companion note (see Sanders & Gish, [J07-companion], 2026).
The present paper is the strict-combinatorics treatment of the σ-character
spectral architecture: periodicity (G_6), period distribution (G_7),
three-valued spectral coherence integral (G_8), 5-dimensional CRT-Fourier
embedding (Q17-A), and the Symbolic Return Theorem (Q17-B). No analytic
number theory appears in the body of this paper.

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
0 & s \in \{0, 3, 8, 9\} \quad (\text{the σ-fixed anchors}), \\
+1 & s \in \{1, 4\}, \\
-1 & s \in \{2, 5, 6, 7\}.
\end{cases}$$
This is *not* a multiplicative character on $\mathbb{Z}/10\mathbb{Z}$; it
encodes the β-exception pattern of the underlying TIG composition tables.
Among the six 6-cycle elements, two carry $\chi = +1$ and four carry $\chi = -1$.

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

<!-- TODO (Wave 4 audit, deferred to next revision): The G_8 proof below is
labeled "Proof sketch" because the σ³-pairing identity invoked in §4.3
(namely $G_\mathrm{cplx}(\sigma^3(s)) = -G_\mathrm{cplx}(s)$) is stated in
one sentence rather than verified cell-by-cell across the three σ³-orbits.
For EJC ship-readiness, promote §4.3's identity to an explicit sub-proposition
with per-orbit verification (3 cells × symbolic sign check), so this can
read "Proof" rather than "Proof sketch". Estimated work: 3-4 hours
(per `_staging/referee_reports/23_wave4_audit_J05_J07_J17_J22_J27.md` §J07 item a). -->

**Proof sketch.** At the anchors, $\chi(\sigma^j(s)) = \chi(s) = 0$ for all $j$ (since σ-fixed implies σ-trajectory is constant, and $\chi$ vanishes on anchors). Hence $G(s) = 0$.

For the six 6-cycle elements, the σ-trajectory cycles through six distinct values, so the sum involves $\chi$-values $\chi(s), \chi(\sigma(s)), \ldots, \chi(\sigma^5(s)), \chi(\sigma^6(s)) = \chi(s), \chi(\sigma(s)), \chi(\sigma^2(s))$ — 9 total terms, with the last 3 repeating the first 3. Computing $G(s)$ at the six 6-cycle starting points and grouping by σ³-orbit gives the three distinct values claimed. Full computation in §4.4 below. ∎

### §4.3 The σ³-pairing structure

The permutation σ³ has order 2 on the 6-cycle (since σ has order 6). It partitions $\{1, 2, 4, 5, 6, 7\}$ into three 2-cycles:
$$\sigma^3 = (1, 5)(2, 6)(4, 7) \quad \text{on the 6-cycle elements.}$$

The complex amplitude $G_\mathrm{cplx}(s) := \sum_{j=0}^{8} \omega^j \chi(\sigma^j(s))$ satisfies $G_\mathrm{cplx}(\sigma^3(s)) = -G_\mathrm{cplx}(s)$ on each σ³-pair, so $|G(s)|^2 = |G(\sigma^3(s))|^2$. Hence the value of $G$ is constant on each σ³-orbit.

**Math-fix R1 note.** A prior draft of the consolidation (J51, pre-2026-05-12) incorrectly identified the high-locus as $\{5, 7\}$ and explained the pairing via σ². Direct computation with the manuscript's stated σ and χ gives the correct high-locus $\{4, 7\}$, with the σ³ (not σ²) pairing explanation above. The fix is applied throughout the present paper.

### §4.4 The χ-imbalance discriminator $\nu_+$

For each starting state $s$ in the σ-6-cycle, define
$$\nu_+(s) := |\{j \in \{0, 1, 2\} : \chi(\sigma^j(s)) = +1\}|.$$
This is the count of $\chi = +1$ values in the first three positions of the σ-trajectory starting from $s$. It is a discrete invariant taking values in $\{0, 1, 2, 3\}$.

**Theorem (ν₊ Trichotomy on the 6-cycle).** For all six 6-cycle starting states, $\nu_+(s) \in \{0, 1, 2\}$:

| σ³-orbit | $s$ | $(s, \sigma(s), \sigma^2(s))$ | $(\chi(s), \chi(\sigma s), \chi(\sigma^2 s))$ | $\nu_+(s)$ | $G(s)$ |
|---|---:|---|---|---:|---:|
| $\{1, 5\}$ | 1 | $(1, 7, 6)$ | $(+1, -1, -1)$ | **1** | $1.871644$ |
| $\{1, 5\}$ | 5 | $(5, 4, 2)$ | $(-1, +1, -1)$ | **1** | $1.871644$ |
| $\{2, 6\}$ | 2 | $(2, 1, 7)$ | $(-1, +1, -1)$ | **1** | $1.871644$ |
| $\{2, 6\}$ | 6 | $(6, 5, 4)$ | $(-1, -1, +1)$ | **1** | $1.871644$ |
| $\{4, 7\}$ | 4 | $(4, 2, 1)$ | $(+1, -1, +1)$ | **2** | $9.389185$ |
| $\{4, 7\}$ | 7 | $(7, 6, 5)$ | $(-1, -1, -1)$ | **0** | $9.389185$ |

The **high-locus σ³-orbit $\{4, 7\}$** is exactly the orbit on which $\nu_+ \in \{0, 2\}$ (extremally χ-imbalanced in the first three positions). The **low-loci σ³-orbits $\{1, 5\}$ and $\{2, 6\}$** are exactly the orbits on which $\nu_+ = 1$ (χ-balanced).

The 9-step sum $G(s)$ visits the orbit's first three positions twice (since the σ-orbit has period 6 and the sum runs over $j = 0, \ldots, 8$ = 9 terms = $6 + 3$). The doubled weighting amplifies the first-three-position χ-imbalance, and the spectral content of the resulting 9-term complex sum varies as follows: at $\nu_+ = 1$ (balanced), partial cancellation gives $|G|^2 \approx 1.872$; at $\nu_+ \in \{0, 2\}$ (imbalanced), reinforcement gives $|G|^2 \approx 9.389$.

The ratio is $G_\mathrm{high} / G_\mathrm{low} \approx 5.0165$. Whether this ratio admits a closed form in $\mathbb{Q}(\zeta_9)$ is open (see §8 question 1).

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

<!-- TODO (Wave 4 audit, deferred to next revision): The uniqueness
statement below is asserted, not proved. For EJC ship-readiness, write the
explicit proof: dimension-count of the CRT character system + non-degeneracy
of the additive character pairing + standard rigidity argument that real-
coordinate embeddings of $\mathbb{Z}/n$ via characters are unique up to
$\text{CO}$ orthogonal change. Estimated work: 10-15 hours of careful
writing (per `_staging/referee_reports/23_wave4_audit_J05_J07_J17_J22_J27.md`
§J07 item b). -->

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

## §7 Independent verification

The five theorems of this paper are independently verifiable:
- G_6, G_7, G_8: `verify_G6_G7_G8.py` (300 lines, ~10s).
- Q17-A: `verify_5D_embedding.py` (J50 source; ~5s).
- Q17-B Symbolic Return: corollary; verified by trajectory enumeration in `verify_J51_G_function.py` (~2s).

A unified `verify_qseries_merged.py` runs all three suites in sequence.

---

## §8 Open questions

1. **Closed-form recovery for $G_\mathrm{low}, G_\mathrm{high}$.** The verified numerical values to 6 decimal places are $G_\mathrm{low} = 1.871644$ and $G_\mathrm{high} = 9.389185$ (run `verify_qseries_merged.py`). Their ratio is $5.01654...$. Closed forms in $\mathbb{Q}(\zeta_9)$ (the cyclotomic field of 9th roots of unity) are expected but not yet identified. Conjecturally, $G_\mathrm{high} / G_\mathrm{low}$ is an algebraic integer of degree ≤ 6 over $\mathbb{Q}$. Numerical PSLQ search at 50-digit precision against $\mathbb{Q}(\zeta_9)$ basis elements would either identify the closed form or rule out small algebraic combinations.

2. **Generalization to other (carrier, σ, χ) triples.** The substrate is Z/10Z. Whether analogous spectral architectures exist for other small finite rings is open. The closest known analog is the (Z/8Z, σ_8, χ_8) triple where the cycle structure is $(1)^2 \cdot (3)^2$; preliminary computation suggests $G_8$-analogs there are 4-valued rather than 3-valued.

3. **Connection to J05+J03 ETP work.** The σ-permutation of this paper is closely related to (but distinct from) the σ used in J05 to define the σ-magma $x \diamond y = \sigma((x+y) \bmod 10)$. The exact relationship — whether the spectral architecture of this paper transfers to the σ-magma — is open and would tighten the J04-J05-J03 σ-magma trilogy.

4. **Companion-note open problem.** A separate exploratory open question about the deployment map $\lambda = 2|s - 1/2|$ and its candidate uniformity (Conjecture Z.5) is recorded in the *Math. Intelligencer* companion note (Sanders & Gish, [J07-companion], 2026). That question is outside the strict-combinatorics scope of the present paper.

---

## §9 References

### Internal cross-references (this paper merges)
- J50 (Sanders & Gish, 2026): Q17-A 5D Fourier embedding. *Subsumed by §5.*
- J51 (Sanders & Gish, 2026): G_6 + G_7 + G_8 spectral consolidation. *Subsumed by §§2-4.*
- J52 (Sanders & Gish, 2026): Symbolic Return Theorem. *Subsumed by §6.* The RH-bridge content of J52 is split off into a separate *Math. Intelligencer* companion note (see below).

### Companion note (split off from earlier draft)
- Sanders, B. R. & Gish, M. (2026): "A Structural Rhyme between the σ-Character Spectrum on Z/10Z and the Riemann Zeros." [J07-companion]. Companion expository note, target *Mathematical Intelligencer*. Contains the structural-rhyme observation that earlier drafts placed in this paper's §7.

### Companion J-series papers
- J01 (Sanders & Gish, 2026): Joint Closure + Universal Attractor. The σ-permutation here is the substrate's structural σ; the present paper is its spectral analysis.
- J12 (Sanders & Gish, 2026): Galois D₄ over LMFDB 4.2.10224.1. The decagonal $D_{10}$ symmetry of Q17-A and the quartic Galois group of J12 are related but distinct symmetry groups (10 ≠ 8).
- J04 (Sanders & Gish, 2026): σ-Magma Rigidity. Uses a related but distinct σ-permutation (the bilinear σ-magma σ).

### External / classical references
- Drápal, A. & Wanless, I. M. (2021): "Maximally nonassociative quasigroups." *J. Combin. Theory Ser. A* 184, 105510.
- Tao, T. et al. (2024-2026): Equational Theories Project. github.com/teorth/equational_theories.

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

- **Revised draft 2026-05-27.** Theorem statements + proof structures pulled from sources; unified narrative complete; §7 RH-rhyme content split off to a separate *Math. Intelligencer* companion note (Sanders & Gish, [J07-companion], 2026); awaiting prose polish + referee-rigor pass on G_8 §4.2 sub-proposition and Q17-A §5.5 uniqueness proof (see manuscript TODO comments).
- **Targets:** European Journal of Combinatorics (primary; matches both J51 and J50 venue targeting). Companion note targets *Mathematical Intelligencer*.
- **Source papers** (J50, J51, J52) marked as MERGED with redirect; the RH-rhyme content of J52 lives in the companion note.

---

*This paper supersedes J50, J51, J52 of the J-series for their strict-combinatorics content. The RH-rhyme content of J52 is published as a separate companion note for *Math. Intelligencer*. All theorem proofs in this paper are inherited from those sources; verification PASSES in all source scripts.*
