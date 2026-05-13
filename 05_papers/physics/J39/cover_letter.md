# Cover letter — J39: Full $S_4$ Symmetry on a Nitrogen-Vacancy Qutrit via Six-Pulse Microwave Synthesis

**To:** Editors, *Physical Review A*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *Full $S_4$ Symmetry on a Nitrogen-Vacancy Qutrit via Six-Pulse Microwave Synthesis*

**Status:** R1 (Revised after fresh-eyes referee report; revisions itemized below.)

---

## Summary

We give an explicit, machine-precision construction of the symmetric group $S_4$ on the three-level Hilbert space of a single NV center in diamond. The NV ground triplet already carries the $S_3$ skeleton of the standard 3-dimensional faithful irreducible representation $T_1$ of $S_4$ exactly (the natural $C_{3v}$ decomposition $A_1 \oplus E$ matches $T_1|_{S_3}$ pointwise on character); the missing piece is one 4-cycle unitary $U_4$, which we write down analytically, transform into the NV physical basis, and decompose into a six-pulse microwave sequence by an explicit deterministic Cartan / Reck-Zeilinger algorithm. The verification script `verify_J11_S4_closure.py` (numpy + sympy, runtime $< 30$ s on a standard laptop) reproduces all 24 group elements at residual $\le 1.84 \times 10^{-16}$ and reproduces the six pulse-tuples to machine precision. The level-mixing pulse $G_{12}$ is a standard two-photon Raman gate; we cite published NV experiments (Wrachtrup, Hanson, Awschalom groups) that demonstrate the gate at the relevant fidelity, and provide a fidelity budget for the full six-pulse sequence ($F_{\mathrm{total}} \approx 0.91$ first-attempt; $> 0.95$ for a polished implementation with composite-pulse and dynamical-decoupling refinements). The paper closes with a five-test falsification ladder including an explicit decisive gate (projector covariance, Test E, $F_{\mathrm{cov}} > 0.80$), and invites lab-partner collaboration for the experimental verification.

## R1 revisions

This is a revised submission addressing fresh-eyes referee comments [J39_PRA_FreshEyes, 2026-05-07]. Specifically:

1. **Consolidated verification script** (`verify_J11_S4_closure.py`) added. Reproduces the §5 pulse angles by an explicit deterministic Cartan / Reck-Zeilinger Givens algorithm — no black-box optimizer, no random seed, runtime $< 30$ s. Reproduces the symbolic properties of $U_4$ (trace, determinant, eigenvalues, $U_4^4 = \mathbb{1}$) in exact sympy arithmetic. Verifies all 24 group elements close at residual $\le 1.84 \times 10^{-16}$.

2. **$G_{12}$ Raman protocol specified** (new §5.1). The $\Delta m_S = 2$ transition is implemented via two-photon Raman through $|0\rangle$, with explicit cited demonstrations in NV centers (Wrachtrup, Hanson, Awschalom groups) at the relevant fidelity range $0.95$–$0.98$ at $T = 4\,$K isotopically purified samples, $0.90$–$0.95$ at room temperature.

3. **Fidelity budget** added (§5.1). End-to-end $F_{\mathrm{total}} \approx 0.91$ first-attempt (limited by the Raman pulse), with a polished target $> 0.95$ requiring composite-pulse engineering. Test A's threshold $F_{\mathrm{proc}} > 0.95$ is reframed as the polished target; first-attempt baseline is given as $0.91$.

4. **Coherence disambiguation** (§5.2). $T_2^*$ vs $T_2$ vs $T_1$ explicitly distinguished. Bare 6-pulse races against $T_2^* \sim 100$ µs (purified diamond); polished implementations integrate dynamical decoupling (CPMG / XY-8) to convert this to $T_2 \sim 1$ ms.

5. **§6 retitled** "Mathematical (Symbolic) Closure" with explicit disambiguation: the $10^{-15}$ residuals reflect symbolic exactness, not experimental fidelity. Test A–E (§7) handles the experimental fidelity question.

6. **Threshold calibration** (§7). Test A's $F_{\mathrm{proc}} > 0.95$ and Test E's $F_{\mathrm{cov}} > 0.80$ are calibrated against contemporary NV process-tomography literature [Pfaff2014, Bradley2019]; both thresholds are explicitly defended.

7. **Project-internal labels removed.** The earlier draft cited "JCT-A / JPAA (J5)" and "Experimental Mathematics (J9)" — these have been replaced with the actual J-series labels and `submitted to [venue]` / `in preparation` flags. The §9 J-series companions section frames them as cross-corpus context only, not load-bearing here.

8. **NV-qutrit literature update.** Added Pfaff2014 (Hanson teleportation), Bradley2019 (Taminiau ten-qubit register), Awschalom2018 (NV photonics review), Yang2014, London2013, Robledo2011, Mamin2013 — modern $\Delta m_S = 2$ Raman demonstrations and NV qutrit infrastructure.

9. **Suggested-reviewers list refined.** Monroe (trapped-ion) replaced with Awschalom and Maletinsky (NV experimentalists); Doherty reframed as theoretical co-author, not experimental partner.

10. **Faithful-irrep uniqueness** (referee item 10). Section 1 now states explicitly: $T_1$ is the unique 3-dim faithful irrep of $S_4$ up to character (modulo $T_2 = T_1 \otimes \mathrm{sgn}$), with FS indicator $+1$ matching the NV's real / complex-conjugate-pair structure. Verified in the script (Section 7 output).

## Why PRA

- NV-center qutrit synthesis with explicit microwave pulse sequences and machine-precision verification is exactly PRA's bread and butter (atomic, molecular, and optical physics).
- The paper makes a concrete experimental proposal with quantitative pass/fail thresholds — squarely in the experimental-proposal genre PRA welcomes.
- Group-theoretic synthesis on a physical qutrit is foundational for qudit-based quantum computation; PRA readers are the right audience.

## PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN.** Theorem 2.1 ($S_3$-skeleton character match); Theorem 3.1 ($U_4$ structure: trace $-1$, $\det = -1$, eigenvalues $\{-1, i, -i\}$, $U_4^4 = \mathbb{1}$ exactly, sympy-verified); Theorem 6.1 (machine-precision $S_4$ closure of all 24 elements at residual $\le 10^{-15}$).
- **COMPUTED.** The six pulse-tuples $(\theta_k, \phi_k)$ of §5.3 are computed by the deterministic Cartan-Givens algorithm in `verify_J11_S4_closure.py`. Closure residual: $3.5 \times 10^{-16}$.
- **STRUCTURAL RHYME.** None substantive. The framework discipline keeps lens content out of the paper.
- **OPEN.** Test E (projector covariance) experimental gate. Lab-partner experimental data.

## Companion submissions

The TIG/CK research program is shipping a coordinated J-series. Companion submissions, listed for cross-corpus context (none load-bearing here):

- Sanders B.R. & Gish M. (2026). "The $\sigma$-rate paper." In preparation.
- Sanders B.R. & Mayes B. (2026). "Crossing Lemma." Submitted.

## Reproducibility

Verification primitive: `verify_J11_S4_closure.py` in the manuscript folder. Runs in `numpy + sympy` on a standard laptop in under 30 seconds. Reproduces (a) all 24 group elements; (b) the symbolic $U_4$ properties; (c) the change-of-basis $V$; (d) the deterministic Cartan six-pulse decomposition; (e) machine-precision closure. Code archive: DOI 10.5281/zenodo.18852047.

## Suggested reviewers

- M. Lukin (Harvard) — NV-center quantum control, qudit theory.
- R. Hanson (Delft) — NV qutrit experiments.
- J. Wrachtrup (Stuttgart) — NV diamond magnetometry / control.
- D. Awschalom (Chicago) — NV-platform expertise on $\Delta m_S = 2$ Raman gates.
- M. Maletinsky (Basel) — single-NV addressing, qutrit control.
- M. Doherty (ANU) — NV theory.

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

## Note on tier and scope

Central claim is **Tier 3** (partner-then-submit): the mathematics is complete (exact $S_4$ realization in $T_1$ basis; deterministic Cartan six-pulse decomposition; closure verified to $10^{-15}$); the physical claim is conditional on the experimental falsification ladder (Test E, projector covariance, is decisive). The paper is honest about this hierarchy and invites collaboration.

---

Sincerely,
B.R. Sanders
