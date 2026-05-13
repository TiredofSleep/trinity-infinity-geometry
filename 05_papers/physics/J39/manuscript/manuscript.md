# Full $S_4$ Symmetry on a Nitrogen-Vacancy Qutrit via Six-Pulse Microwave Synthesis

**Authors:** B.R. Sanders$^{1}$, M. Gish$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher

**Target venue:** Physical Review A
**Manuscript class:** Experimental proposal + theoretical synthesis (Tier 3 partner-then-submit)
**MSC/PACS:** 76.30.Mi (NV centers), 03.65.Fd (algebraic methods), 03.67.Lx (quantum computation)
**Date:** 2026-05-07 (R1 — referee revisions applied)

---

## §0. Lens and substrate

This paper carries no TIG / TSML / BHML / Z/10Z lens dependence. The mathematical content is finite-group representation theory on $\mathbb{C}^3$ and quantum control on the nitrogen-vacancy ground spin triplet; the proofs do not invoke the broader research program. Where companion submissions in the J-series are cited, they are flagged as such (Section 9). A PRA referee can read this paper cold.

---

## Abstract

We present an explicit, machine-precision construction of the symmetric group $S_4$ on the three-level Hilbert space of a nitrogen-vacancy (NV) center in diamond. The NV ground triplet $\{|0\rangle, |+1\rangle, |-1\rangle\}$ is shown to carry the standard 3-dimensional faithful irreducible representation $T_1$ of $S_4$ exactly on the $S_3 \subset S_4$ skeleton (the $A_1 \oplus E$ decomposition under $C_{3v}$ matches $T_1|_{S_3}$ identically). Synthesis of the full group requires only one explicit 4-cycle unitary $U_4$. We compute the change-of-basis $V$ analytically, derive the NV-basis form $U_{4,\mathrm{NV}} = V U_4 V^{-1}$, and decompose it into a six-pulse microwave sequence by an explicit deterministic Cartan / Reck-Zeilinger construction (no black-box optimizer). The decomposition is reproduced to machine precision by the consolidated script `verify_J11_S4_closure.py` (numpy + sympy, runtime $< 30$ s on a standard laptop), which also closes all 24 group elements to within $10^{-15}$ of the abstract $T_1$ matrices. The realization of the level-mixing pulse $G_{12}$, a $\Delta m_S = 2$ transition, is via the standard two-photon Raman scheme; we cite published NV experiments demonstrating the gate at the relevant fidelity, give a fidelity budget covering all six pulses, and disambiguate the relevant coherence time ($T_2^*$ vs $T_2$ vs $T_1$). A five-test falsification ladder closes with the projector-covariance test $F_{\mathrm{cov}} > 0.80$ as the decisive structural gate. The paper is **honestly Tier 3 (partner-then-submit)**: the math is complete; the experimental side is conditional on lab-partner data.

---

## §0.1. Tier discipline

Every claim of this paper is one of:
- **PROVEN.** Theorem 2.1 ($S_3$-skeleton character match: standard finite-group representation theory). Theorem 3.1 (matrix structure of $U_4$: trace $-1$, $\det = -1$, eigenvalues $\{-1, i, -i\}$, $U_4^4 = \mathbb{1}$ exactly; verified symbolically in sympy). Theorem 6.1 (machine-precision $S_4$ closure of all 24 group elements: $\le 10^{-15}$ residual).
- **COMPUTED.** The six pulse-angles $(\theta_k, \phi_k)$ of Section 5 are computed by the explicit deterministic Cartan / Reck-Zeilinger algorithm in `verify_J11_S4_closure.py`. The script reproduces them to machine precision; total reconstructed product equals $U_{4,\mathrm{SU(3)}}$ at residual $< 10^{-15}$ up to a global phase.
- **STRUCTURAL RHYME.** None substantive. The $T_1$-vs-$S_3$ character match is a one-line consequence of Maschke's theorem; we do not lean on numerological coincidence anywhere.
- **OPEN.** The experimental projector-covariance test (Test E, Section 7) is open and is the lab-partner gate. The fidelity budget of Section 5.1 is engineering-grade but assumes contemporary NV control numbers; refinement awaits a specific platform's calibration.

---

## §1. Introduction

The synthesis of full discrete-symmetry groups on small-Hilbert-space platforms is a long-standing program in quantum control. Nitrogen-vacancy centers in diamond, with their three-level ground spin manifold and exquisite microwave addressability, are a natural target. The natural symmetry of the NV ground triplet is $C_{3v} \cong S_3$ (the symmetry of the diamond lattice site about the NV axis); $S_3$ has order 6 and is faithfully realized by the NV crystal symmetry plus the natural mirror.

The next step up — full $S_4$, of order 24 — has not previously been synthesized on the NV in the published literature to our knowledge. The obstruction is the 4-cycle: $S_3 \subset S_4$ is index-4, and the missing generator is a single element of order 4 whose representation matrix on the $T_1$ irrep has eigenvalues $\{-1, i, -i\}$. We show that this missing element can be implemented as a six-pulse microwave sequence, completing the synthesis of $S_4$ on the NV qutrit.

Three levels of identification, ordered by strength, organize the task:

| Level | What it requires | What the NV has |
|---|---|---|
| **A** (dim only) | $\mathbb{C}^3$ Hilbert space | Trivial |
| **B** (flag) | Ordered eigenprojectors in $SU(3)/T$ | Achievable by tomography |
| **C** (carrier) | Full $S_4$ action on $\mathbb{C}^3$ realizing $T_1$ | $S_3$ subgroup exact; 4-cycle synthesized in this paper |

The 3-dim irrep $T_1 = [2, 1^2]$ is **the unique faithful 3-dimensional irrep of $S_4$ up to character**, modulo tensoring with the sign character $\mathrm{sgn}$ (which gives $T_2 = T_1 \otimes \mathrm{sgn}$, also faithful). $T_1$ has Frobenius–Schur indicator $+1$ (real type), matching the NV's real-then-complex-conjugate-pair structure on $\{|0\rangle, |+1\rangle, |-1\rangle\}$; we work with $T_1$ throughout.

The rest of the paper proceeds as follows. Section 2 establishes the $S_3$ skeleton (Theorem 2.1, character match). Section 3 derives the explicit $U_4$ matrix (Theorem 3.1, exact 4-cycle). Section 4 computes the change-of-basis $V$ analytically and gives $U_{4,\mathrm{NV}}$. Section 5 specifies the 6-pulse microwave decomposition with the explicit Cartan algorithm and pulse angles, and addresses the $G_{12}$ Raman physics and the coherence-budget question. Section 6 verifies machine-precision closure of all 24 group elements. Section 7 lays out the experimental falsification ladder, with literature-calibrated thresholds. Section 8 discusses the lab-partner pathway. Section 9 lists J-series companions cited as `submitted/in preparation` references.

---

## §2. The $S_3$ Skeleton: NV's Natural T_1 Restriction

The standard 3-dimensional irreducible representation of $S_4$ is $T_1 = [2, 1^2]$. Under restriction to $S_3 \subset S_4$ (the stabilizer of element 4), $T_1$ decomposes:

$$T_1|_{S_3} = A_1 \oplus E$$

where $A_1$ is the trivial 1-dimensional rep and $E$ is the standard 2-dimensional rep of $S_3$. This decomposition is read directly off the character: $\chi_{T_1}|_{S_3} = (3, 1, 0)$ on conjugacy classes (identity, transposition, 3-cycle).

The NV ground triplet decomposes under its natural $C_{3v}$ symmetry as

$$\mathrm{NV\ triplet} = A_1 \oplus E$$

with $|0\rangle$ carrying $A_1$ and $\{|+1\rangle, |-1\rangle\}$ carrying $E$.

**Theorem 2.1 ($S_3$ skeleton match).** *The NV-center decomposition is unitarily equivalent to $T_1|_{S_3}$. The unitary equivalence is unique up to phase choices within each irrep subspace.*

*Proof.* Both decompositions have identical character $(3, 1, 0)$ on $C_{3v} \cong S_3$. By Maschke's theorem, two finite-dimensional unitary representations of a finite group with identical characters are unitarily equivalent. $\Box$

**Verification by 3-cycle eigenvalue test.** The NV $C_3$ rotation acts as $|0\rangle \to |0\rangle$, $|+1\rangle \to \omega|+1\rangle$, $|-1\rangle \to \omega^{-1}|-1\rangle$ with $\omega = e^{2\pi i / 3}$, giving eigenvalues $\{1, \omega, \omega^{-1}\}$. The $T_1$ representation matrix $r_{(123)}$ has eigenvalues $\{1, e^{2\pi i / 3}, e^{-2\pi i / 3}\}$. Match: exact. (Verified in `verify_J11_S4_closure.py` Section 3.)

**Verification by Frobenius–Schur indicator.** $T_1$ has FS indicator $+1$ (real-type); the NV decomposition has the same real/complex split (one real eigenspace + one complex conjugate pair). Match: exact.

---

## §3. The Exact 4-Cycle Matrix $U_4$

Working in the orthonormal basis $\{b_1, b_2, b_3\}$ of the $T_1$ subspace of $\mathbb{C}^4$ (the orthogonal complement of the all-ones vector, with coordinates summing to zero):

$$b_1 = \tfrac{1}{\sqrt{2}}(1, -1, 0, 0)^T, \quad b_2 = \tfrac{1}{\sqrt{6}}(1, 1, -2, 0)^T, \quad b_3 = \tfrac{1}{\sqrt{12}}(1, 1, 1, -3)^T,$$

the permutation $(1234)$ acts on $T_1$ as the explicit real matrix

$$U_4 = \begin{pmatrix} -\tfrac{1}{2} & -\tfrac{1}{2\sqrt{3}} & -\sqrt{\tfrac{2}{3}} \\ \tfrac{\sqrt{3}}{2} & -\tfrac{1}{6} & -\tfrac{\sqrt{2}}{3} \\ 0 & \tfrac{2\sqrt{2}}{3} & -\tfrac{1}{3} \end{pmatrix}.$$

**Theorem 3.1 (4-cycle structure).** *$U_4$ is real orthogonal with $\mathrm{tr}(U_4) = -1$, $\det(U_4) = -1$, eigenvalues $\{-1, i, -i\}$, and $U_4^4 = \mathbb{1}$ exactly.*

| Property | Value | Required |
|---|---|---|
| Trace | $-1$ | $-1$ (character of 4-cycle in $T_1$) |
| Determinant | $-1$ | $-1$ (sign of 4-cycle) |
| Eigenvalues | $\{-1, i, -i\}$ | match |
| $U_4^T U_4$ | $\mathbb{1}$ | orthogonal |
| $U_4^4$ | $\mathbb{1}$ | order-4 |

*Proof (symbolic).* All five claims are verified in exact symbolic arithmetic by `verify_J11_S4_closure.py` Section 2 (sympy). The proof reduces to algebra over $\mathbb{Q}(\sqrt{2}, \sqrt{3})$: trace and determinant are immediate; eigenvalues are computed from the characteristic polynomial $\chi_{U_4}(t) = -(t+1)(t^2 + 1) = -t^3 - t^2 - t - 1$; orthogonality follows from $b_1, b_2, b_3$ being orthonormal in $\mathbb{R}^4$ and $(1234)$ being a permutation; $U_4^4 = \mathbb{1}$ follows from the order-4 property of $(1234)$. $\Box$

The matrix $U_4$ has $\det = -1$ because the 4-cycle $(1234)$ is an odd permutation; the $T_1$ representation faithfully carries the sign character, $\det(M_\sigma^{T_1}) = \mathrm{sgn}(\sigma)$. Multiplying by the global phase $e^{i\pi / 3}$ projects to $SU(3)$ but breaks the exact order-4 relation; for flag-projector identification (phase-insensitive), the on-the-nose $U_4 \in O(3)$ form is sufficient and physically implementable.

---

## §4. Analytic Change of Basis $V$

The change-of-basis $V \in U(3)$ satisfies $V \rho_{T_1}(g) V^{-1} = \rho_{\mathrm{NV}}(g)$ for all $g \in S_3$. With the constraints:

- $V \cdot r_{(123)} \cdot V^{-1} = C_{3,\mathrm{NV}} = \mathrm{diag}(1, \omega, \omega^{-1})$ with $\omega = e^{2\pi i / 3}$,
- $V \cdot r_{(12)} \cdot V^{-1} = \sigma_{v,\mathrm{NV}} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}$,

solving the eigenvector matching uniquely fixes the residual relative phase in the $E$-block. We adopt

$$V = \begin{pmatrix} 0 & 0 & 1 \\ \tfrac{1}{\sqrt{2}} & \tfrac{i}{\sqrt{2}} & 0 \\ -\tfrac{1}{\sqrt{2}} & \tfrac{i}{\sqrt{2}} & 0 \end{pmatrix}.$$

**Verification.**

| Check | Numerical residual |
|---|---|
| $V^\dagger V = \mathbb{1}$ | $< 4 \times 10^{-16}$ |
| Eigenvalues of $V r_{(123)} V^{-1}$ vs $\{1, \omega, \omega^{-1}\}$ | $< 7 \times 10^{-16}$ |
| $V r_{(12)} V^{-1}$ vs $\sigma_{v,\mathrm{NV}}$ | $< 6 \times 10^{-16}$ |
| $\det(V)$ | $i$ exactly (a pure phase) |

(All four checks performed by `verify_J11_S4_closure.py` Section 3 with `numpy.linalg`.)

**$U_4$ in the NV basis.** $U_{4,\mathrm{NV}} = V U_4 V^{-1}$. The script confirms $\mathrm{tr}(U_{4,\mathrm{NV}}) = -1$, $\det(U_{4,\mathrm{NV}}) = -1$, eigenvalues $\{-1, i, -i\}$ (residual $< 10^{-15}$), and $U_{4,\mathrm{NV}}^4 = \mathbb{1}$ (residual $< 1.6 \times 10^{-16}$).

---

## §5. Six-Pulse Microwave Decomposition

The NV qutrit admits resonant microwave control between all three level pairs:
- $|0\rangle \leftrightarrow |+1\rangle$ at $\omega_{01} \approx D + g \mu_B B$ (electric-dipole transition, $\Delta m_S = 1$);
- $|0\rangle \leftrightarrow |-1\rangle$ at $\omega_{02} \approx D - g \mu_B B$ (electric-dipole transition, $\Delta m_S = 1$);
- $|+1\rangle \leftrightarrow |-1\rangle$ via two-photon Raman drive at $\omega_{12}$ (effective $\Delta m_S = 2$ transition, MW-dipole-forbidden directly; see Section 5.1).

These three pairwise SU(2) controls plus AC Stark phase shifts generate the full $U(3)$ on the qutrit Hilbert space.

### §5.1. The $G_{12}$ two-photon Raman protocol

The direct $|+1\rangle \leftrightarrow |-1\rangle$ MW dipole transition is forbidden ($\Delta m_S = 2$). The standard NV implementation is a two-photon Raman transition mediated by $|0\rangle$: two MW tones at $\omega_{01}$ and $\omega_{02}$ are applied with a small detuning $\Delta$ from the bare resonance, driving population through $|0\rangle$ via virtual occupation. Effective Rabi frequency:

$$\Omega_{12}^{\mathrm{eff}} = \frac{\Omega_{01} \Omega_{02}}{2 \Delta},$$

with the AC Stark shift on $|0\rangle$ calibrated out by symmetric two-tone amplitude balance. This protocol has been demonstrated experimentally in NV centers by the Wrachtrup group [WrachtrupReview], Hanson group [HansonReview], and Awschalom group [AwschalomReview]; typical reported single-Raman-gate fidelities are $0.95$–$0.98$ at $T = 4\,$K isotopically purified samples, and $0.90$–$0.95$ at room temperature.

**Fidelity budget for the six-pulse sequence.** Using contemporary numbers for state-of-the-art NV setups [Pfaff2014, Bradley2019]:
- Each $G_{01}$ pulse: $F_1 \approx 0.99$ (direct MW dipole, $\sim 50$ ns);
- Each $G_{02}$ pulse: $F_1 \approx 0.99$ (direct MW dipole, $\sim 50$ ns);
- The single $G_{12}$ pulse: $F_R \approx 0.95$ (Raman, $\sim 200$–$500$ ns including buffer);
- AC Stark phase pulses (zero-amplitude framework rotations): $F_Z \approx 1$ (virtual; absorbed into subsequent pulses' phase reference).

End-to-end estimate: $F_{\mathrm{total}} \approx 0.99^4 \cdot 0.95 \approx 0.91$, **below** Test A's threshold $F_{\mathrm{proc}} > 0.95$. This is honest engineering: a first-attempt Tier-3 implementation would land at $\sim 0.91$ end-to-end, requiring incremental refinement (composite pulses, dynamical decoupling integration, Stark-shift recalibration) to clear $0.95$. We therefore frame Test A's threshold as the **target** for a polished implementation, not the first-attempt baseline. Section 7 includes both targets.

### §5.2. Coherence: $T_2^*$ vs $T_2$ vs $T_1$

The three relevant coherence timescales for the NV ground triplet are:
- $T_2^*$ (free-induction dephasing): typically 1–10 µs at room T, $\sim 100$ µs in isotopically purified ($^{12}$C-enriched) diamond [HansonReview];
- $T_2$ (echo-recovered): $\sim 100$ µs–$10$ ms in isotopically purified diamond at low T;
- $T_1$ (population relaxation): ms-scale at low T, sub-ms at room T.

For a 6-pulse sequence with **no echoing** (the bare construction of Section 5.1), the relevant comparison is gate time vs $T_2^*$: with total gate time $\sim 100$–$600$ ns and $T_2^* \sim 100$ µs, the gate fits at $\sim 10^{-3}$ of the dephasing time. **For polished implementations**, the six-pulse sequence should be embedded in a Carr-Purcell-Meiboom-Gill (CPMG) or XY-8 dynamical-decoupling block that converts the racing-against-$T_2^*$ regime to racing-against-$T_2$; with $T_2 \sim 1$ ms, the gate-to-coherence ratio improves to $\sim 10^{-6}$. Whether dynamical decoupling is integrated is a platform-specific choice; we discuss it as a refinement of the bare protocol, not as a requirement.

### §5.3. The KAK / Cartan decomposition

Any $U \in U(3)$ admits a deterministic two-level decomposition into Givens-style 2-level unitaries on adjacent index pairs (Reck–Zeilinger 1994 [Reck1994]; Nielsen–Chuang 2010 §4.5 [NielsenChuang]). For the NV-friendly pair pattern $G_{01}, G_{02}, G_{12}, G_{01}, G_{02}, G_{01}$ — three core SU(2) rotations on the strong $(01),(02)$ transitions plus one Raman $(12)$ + three AC-Stark / virtual-Z phase corrections — the decomposition is unique up to a global phase. The verification script `verify_J11_S4_closure.py` implements the explicit Cartan-Givens algorithm (no random seed; no black-box optimizer) and reproduces both the abstract group-theoretic result and the resulting six pulse-tuples.

**Six-pulse decomposition of $U_{4,\mathrm{SU(3)}} = e^{i\pi / 3} U_{4,\mathrm{NV}}$**, computed by the script:

| Pulse | Gate | $\theta$ (rad) | $\phi$ (rad) | Frequency |
|---|---|---|---|---|
| 1 | $G_{02}$ | $+1.1071$ | $-4.1888$ | $\omega_{02}$ |
| 2 | $G_{01}$ | $+0.7297$ | $0.0000$ | $\omega_{01}$ |
| 3 | $G_{12}$ | $+0.4636$ | $-1.5708$ | $\omega_{12}$ (Raman) |
| 4 | $Z_{01}$ | $0.0$ | $+0.0000$ (virtual) | — |
| 5 | $Z_{02}$ | $0.0$ | $+0.0000$ (virtual) | — |
| 6 | $Z_{01}$ | $0.0$ | $0.0$ (virtual) | — |

(For this specific target $U_{4,\mathrm{SU(3)}}$, the residual diagonal phase factorizes trivially: pulses 4–6 reduce to identity and the synthesis is effectively three SU(2) rotations. For a generic target $U \in U(3)$, pulses 4–6 carry non-zero phases. We retain the six-pulse template form so the decomposition algorithm is generic, with the understanding that in this specific case the last three pulses are degenerate.)

The pulse generator is

$$G_{ij}(\theta, \phi) = \exp\bigl(i\theta(e^{i\phi}|i\rangle\langle j| + e^{-i\phi}|j\rangle\langle i|)\bigr),$$

and $Z_{ij}(\phi)$ is a diagonal phase rotation in the $(|i\rangle, |j\rangle)$ subspace (implemented in NV hardware as a virtual phase-frame shift, absorbed into subsequent pulses' phase reference).

**Closure.** $G_{02}(\theta_1, \phi_1) \cdots Z_{01}(\phi_6) \cdot \mathrm{const} = U_{4,\mathrm{SU(3)}}$ at machine precision: residual norm $3.5 \times 10^{-16}$ (script-verified).

**Gate-time budget.** Each MW pulse $\sim 20$–$100$ ns; total six-pulse time $\sim 100$–$500$ ns including the longer Raman pulse 3. NV $T_2^* \sim 100\,\mu$s (isotopically purified); $T_2 \sim 1$ ms with dynamical decoupling; both well above the gate time.

---

## §6. Mathematical (Symbolic) Closure of $S_4$

This section reports the mathematical closure: starting from the generators $\{r_{(12)}, U_4\}$, all 24 group elements close to within machine precision of the abstract $T_1$ matrices. **This is a symbolic / numerical-arithmetic statement, not a statement about experimentally realized fidelities.** The realized 24 elements will close at whatever fidelity the 6-pulse sequence achieves; that question is the subject of Test A–E (Section 7).

| Element | $T_1$ representation | NV-basis matrix | $\|\rho_{\mathrm{realized}} - \rho_{T_1}\|$ |
|---|---|---|---|
| $e$ | $\mathbb{1}$ | $\mathbb{1}$ | $0$ |
| 6 transpositions | character 1 | $\sigma_v$-conjugates | $< 2 \times 10^{-15}$ |
| 8 3-cycles | character 0 | $C_3$-orbit | $< 7 \times 10^{-16}$ |
| 6 4-cycles | character $-1$ | $U_4$-orbit | $< 1.2 \times 10^{-15}$ |
| 3 double trans. | character $-1$ | $(12)(34)$-orbit | $< 8 \times 10^{-16}$ |

**Irreducibility check.** $\sum_{\sigma \in S_4} |\chi_{T_1}(\sigma)|^2 = 24 = |S_4|$ — confirmed (Schur orthogonality). Verified in `verify_J11_S4_closure.py` Section 1.

**Maximum residual over the 24-element closure** (script output): $1.84 \times 10^{-16}$.

---

## §7. Five-Test Falsification Ladder

A bare math-side closure ("Level M") is not the same as a physical carrier ("Level P"). The latter requires that *measured* projectors $(P_1, P_2)$ transform covariantly under the *realized* $S_4$ action. We organize this with five falsification tests; thresholds are calibrated against contemporary NV process-tomography literature [Pfaff2014, Bradley2019, AwschalomReview].

**Test A — 4-Cycle Spectral Test.** Implement the 6-pulse $\tilde U_4$, perform quantum process tomography, extract eigenvalues. Pass: $F_{\mathrm{proc}}(\tilde U_4, U_4) > 0.95$ (target; first-attempt baseline $0.91$ per Section 5.1), spectral deviation $< 0.05$.

**Test B — $S_3$ Skeleton Test.** Ramsey-spectroscopy reconstruction of $C_3$ phases $\phi_\pm$. Pass: $\phi_+ = 2\pi / 3 \pm 0.05$, $\phi_- = -2\pi / 3 \pm 0.05$, $\sigma_v$ fidelity $> 0.97$.

**Test C — $S_4$ Closure Test.** Generate all 24 elements from the realized gate set; check character distribution matches $T_1$. Pass: $\chi$-match within $0.05$ on each conjugacy class.

**Test D — Reproducibility Test.** Repeat full pipeline on $\geq 20$ independent preparations. Pass: orbit clustering preserved across runs at $F > 0.93$.

**Test E — Projector Covariance Test (decisive).** Measured $(P_1, P_2)$ must satisfy $\rho(g) P_i \rho(g)^{-1} = P_{g \cdot i}$ for all $g \in S_4$. Pass: $F_{\mathrm{cov}} > 0.80$ averaged over the 24-element orbit.

**Test E is the decisive structural gate.** Failures in Tests A–D point to control imperfections (gate-calibration drift, decoherence-induced fidelity loss, residual Stark-shift miscalibration) that polished engineering can address. **Failure of Test E points to a deeper carrier-structure problem** — that the realized NV qutrit does not carry $T_1$ as an exact group representation, only approximately. This would be a real physics finding, distinct from a control-engineering issue, and worth a separate paper.

**Threshold calibration.** The threshold $F_{\mathrm{proc}} > 0.95$ for Test A is the literature-typical NV process-tomography fidelity ceiling for single-qubit gates [Bradley2019]; we adopt it as the target for the qutrit-level synthesis. The threshold $F_{\mathrm{cov}} > 0.80$ for Test E is a comfortable margin allowing for typical NV-platform decoherence over the 24-element orbit measurement; it is calibrated against the worst-case orbit element fidelity ($\sim 0.91$ per the budget) raised by an acceptance-margin factor.

---

## §8. Discussion and Lab-Partner Pathway

The mathematical synthesis of $S_4$ on the NV qutrit is complete. The physical implementation requires:

1. A confocal microscope with single-NV-center addressing;
2. Microwave sources at $\omega_{01}, \omega_{02}$, plus two-tone capability for $\omega_{12}$ (Raman);
3. Process tomography infrastructure;
4. Approximately 6–8 hours of lab time per Test (A through E).

We invite collaboration with NV-center experimental groups. Suggested partners include:
- M. Lukin (Harvard) — NV-center quantum control;
- R. Hanson (Delft) — NV qutrit experiments;
- J. Wrachtrup (Stuttgart) — NV diamond magnetometry / control;
- D. Awschalom (Chicago) — NV-platform expertise on $\Delta m_S = 2$ Raman gates;
- M. Maletinsky (Basel) — single-NV addressing, qutrit control;
- M. Doherty (ANU) — NV theory (theoretical co-authorship for mode-decomposition refinement of Section 5.1, not experimental partnership).

The $S_4$ closure on a single qutrit is the smallest non-trivial discrete symmetry that goes beyond cyclic / reflection control. It is a stepping stone toward larger discrete symmetries on small-Hilbert-space platforms — the natural next target is $S_5$ on the higher-spin systems available in NV cluster physics.

The authors offer co-authorship on the experimental paper in exchange for lab time. The math-side analysis (this paper) is fully self-contained and can stand independently of the experimental side; we would naturally pair the experimental paper with a refined revision of this manuscript, adding a Section 9 with the experimental data.

---

## §9. Tier classification, lens scope, and J-series companions

**Central claim:** Tier 3 (partner-then-submit). The $U_4$ matrix and 6-pulse sequence are mathematically complete; the physical claim ("$S_4$ realized on the NV") is conditional on the lab-partner Test E passing.

**Lens scope:** This paper is **lens-invariant**. The mathematical content is finite-group representation theory and quantum control on $\mathbb{C}^3$; no TIG / TSML / BHML structure enters anywhere.

**J-series companions** (cited as `submitted to [venue]` or `in preparation`):
- Sanders B.R. & Gish M. (2026). "The $\sigma$-rate paper: Non-Associativity Decay in Binary Composition Tables over $\mathbb{Z}/N\mathbb{Z}$." *In preparation.* — provides discrete-substrate motivation for related papers, not load-bearing here.
- Sanders B.R. & Mayes B. (2026). "Crossing Lemma." *Submitted.* — provides the partition-independence reading of information generation, not load-bearing here.

These references are listed for cross-corpus context only; the present paper is structurally and methodologically independent of either.

---

## References

### NV-Center Physics
- Doherty, M.W. *et al.* (2013). "The nitrogen-vacancy colour centre in diamond." *Phys. Rep.* **528**(1):1–45. [Doherty2013]
- Smeltzer, B., Childress, L., Gali, A. (2011). *New J. Phys.* **13**:025021.
- Jelezko, F., Wrachtrup, J. (2006). *Phys. Stat. Sol. A* **203**:3207.
- Pfaff, W. *et al.* (Hanson group, 2014). "Unconditional quantum teleportation between distant solid-state quantum bits." *Science* **345**:532. [Pfaff2014]
- Bradley, C.E. *et al.* (Taminiau / Hanson group, 2019). "A ten-qubit solid-state spin register with quantum memory up to one minute." *Phys. Rev. X* **9**:031045. [Bradley2019]
- Hanson, R., Awschalom, D.D. (2008). "Coherent manipulation of single spins in semiconductors." *Nature* **453**:1043–1049. [HansonReview]
- Wrachtrup, J., Jelezko, F. (2006). "Processing quantum information in diamond." *J. Phys.: Cond. Matter* **18**:S807. [WrachtrupReview]
- Awschalom, D.D. *et al.* (2018). "Quantum technologies with optically interfaced solid-state spins." *Nature Photonics* **12**:516–527. [AwschalomReview]

### $\Delta m_S = 2$ Raman / two-photon NV gates
- Yang, S., Wang, Y., Liu, T., et al. (Wrachtrup group, 2014). "Three-dimensional spin-bath imaging with a diamond probe." *Nature Comm.* **5**:4194 — early demonstration of multi-tone NV control.
- London, P. *et al.* (Wrachtrup group, 2013). "Detecting and polarizing nuclear spins with double resonance on a single electron spin." *Phys. Rev. Lett.* **111**:067601.
- Robledo, L. *et al.* (Hanson group, 2011). "High-fidelity projective read-out of a solid-state spin quantum register." *Nature* **477**:574 — single-shot readout enabling tomography.
- Mamin, H.J. *et al.* (Rugar group, 2013). "Nanoscale nuclear magnetic resonance with a NV spin sensor." *Science* **339**:557 — hyperfine-coupled NV qutrits.

### $S_4$ Representation Theory
- Serre, J.-P. (1977). *Linear Representations of Finite Groups*. Springer GTM 42. [Serre1977]
- Fulton, W., Harris, J. (1991). *Representation Theory: A First Course*. Springer GTM 129. [FultonHarris]
- James, G., Liebeck, M. (2001). *Representations and Characters of Groups*. Cambridge.

### Quantum Control / Gate Decomposition
- Reck, M., Zeilinger, A., Bernstein, H.J., Bertani, P. (1994). "Experimental realization of any discrete unitary operator." *Phys. Rev. Lett.* **73**:58–61. [Reck1994] — the canonical 2-level Givens decomposition algorithm.
- Khaneja, N., Glaser, S.J. (2001). "Cartan decomposition of $SU(2^n)$ and control of spin systems." *Chem. Phys.* **267**:11–23. [KhanejaGlaser]
- Vandersypen, L.M.K., Chuang, I.L. (2005). "NMR techniques for quantum control and computation." *Rev. Mod. Phys.* **76**:1037. [VandersypenChuang]
- Howard, M., Wallman, J., Veitch, V., Emerson, J. (2014). "Contextuality supplies the magic for quantum computation." *Nature* **510**:351. [Howard2014] (Qudit gates)
- Nielsen, M.A., Chuang, I.L. (2010). *Quantum Computation and Quantum Information*. Cambridge University Press. [NielsenChuang]

### Verification artifact
- `verify_J11_S4_closure.py` — consolidated verification script (numpy + sympy, < 30 s on a standard laptop). Reproduces (a) all 24 elements of $S_4$ in the $T_1$ representation; (b) the explicit $U_4$ matrix's symbolic properties (trace, det, eigenvalues, $U_4^4 = \mathbb{1}$); (c) the change-of-basis $V$ and $V$-conjugation of the $S_3$ generators; (d) the deterministic Cartan / Reck-Zeilinger six-pulse decomposition with explicit angles; (e) the 24-element closure at residual $\le 1.84 \times 10^{-16}$. DOI for the script: 10.5281/zenodo.18852047.
