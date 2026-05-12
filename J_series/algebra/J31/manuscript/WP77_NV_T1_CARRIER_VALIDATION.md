# WP77 — NV T1 Carrier Validation
## 5-Test Falsification Ladder

**Date**: 2026-04-09
**Sprint**: 13 — Physical Flag Selector
**Authors**: Brayden Ross Sanders / 7Site LLC · Ben Mayes · C.A. Luther

---


## Block 1 — Three Levels: What Each Can and Cannot Establish

**Level M — Mathematical closure (already achieved)**

| What it proves | What it cannot prove |
|---|---|
| V exists and is unique (up to phase convention) | That pulse-synthesized gates have the right action |
| $V r_{123} V^{-1} = C_{3,\text{NV}}$ exactly | That realized projectors transform covariantly |
| $V r_{12} V^{-1} = \sigma_{v,\text{NV}}$ exactly | That measurement noise doesn't destroy carrier structure |
| 24-element closure with exact T₁ character table | — |
| Irreducibility: $\sum\|\chi\|^2 = 24$ exactly | — |

**Level C — Control-level closure**

| What it proves | What it cannot prove |
|---|---|
| Gate set physically synthesizable on NV | That imperfect gates still qualify as a T₁-carrier |
| Process fidelity places realized gates near targets | That projectors from state tomography are covariant |
| Realized orbit still clusters correctly at $F > 0.93$ | — |

**Level P — Physical carrier certification (required for honest claim)**

| What it proves (if passed) | What it requires |
|---|---|
| Measured projectors $(P_1, P_2)$ transform correctly under realized S₄ action | Projector covariance test under all 24 group elements |
| Flag is T₁-carrier-like, not merely a generic qutrit flag | Reproducibility across $\geq 20$ independent preparations |
| Covariance structure is physical, not mathematical | Orbit structure consistent with T₁ irrep |

**The hierarchy is strict.** Claiming Level P from Level M is not legitimate. The math guarantees: IF pulses are perfect AND tomography is perfect, the claim holds. But perfect is never physical. A Level P claim requires the falsification ladder below.

---

## Block 2 — Falsification Test Specifications

### Test A — 4-Cycle Spectral Test

**What it checks:** does the synthesized $\tilde{U}_4$ have the required spectral structure?

**Procedure:**
1. Implement the 6-pulse sequence for $U_{4,\text{NV}}$
2. Perform quantum process tomography (QPT): 9 input states × 8 expectation values = 72 measurements; total time ~72–720 ms
3. Extract effective $\tilde{U}_4$ from the reconstructed process matrix
4. Compute eigenvalues and verify order-4 relation

| Criterion | Pass (strong) | Pass (medium) | Fail |
|---|---|---|---|
| Process fidelity $F_{\text{proc}}(\tilde{U}_4, U_4)$ | $> 0.95$ | $> 0.90$ | $< 0.90$ |
| Spectral deviation $\max_k\|\tilde{\lambda}_k - \lambda_k\|$ against $\{-1, i, -i\}$ | $< 0.05$ | $< 0.10$ | $> 0.10$ |
| Order-4 residual $\|\tilde{U}_4^4 - e^{i\phi}\mathbb{1}\|$ | $< 0.10$ | $< 0.20$ | $> 0.20$ |

**What failure means:** the two-quantum $G_{12}$ pulse is the bottleneck. Fix: composite pulse sequences; lower temperature for longer $T_2$.

### Test B — S₃ Skeleton Test

**What it checks:** is the natural $C_{3v}$ structure correctly operational?

Note: the NV crystal $C_3$ rotation is not directly controllable as a gate. It is reconstructed from Ramsey free-precession spectroscopy: after free precession time $\tau = 1/(2D)$, the relative phase between $|+1\rangle$ and $|-1\rangle$ encodes the $C_3$ phase structure.

| Criterion | Pass | Fail |
|---|---|---|
| $C_3$ phase: $\phi_+$ | $2\pi/3 \pm 0.05$ | deviation $> 0.1$ |
| $C_3$ phase: $\phi_-$ | $-2\pi/3 \pm 0.05$ | deviation $> 0.1$ |
| $\sigma_v$ process fidelity | $> 0.97$ | $< 0.95$ |
| $A_1 \oplus E$ decomposition: $F_{\text{proj}}(|0\rangle\langle 0|, A_1)$ | $> 0.98$ | $< 0.95$ |

**What failure means:** the NV triplet is not operating as a clean qutrit. Possible causes: leakage to excited states, nuclear spin coupling ($^{14}$N or $^{13}$C), thermal population of $m_s = \pm 1$.

### Test C — S₄ Closure Test

**What it checks:** does the realized gate set generate 24 elements with the T₁ character distribution?

Target character distribution:

| Trace | Expected count | Pass range |
|---|---|---|
| $3.0$ | 1 | 1 ✓ |
| $1.0$ | 6 | 5–7 |
| $0.0$ | 8 | 6–9 |
| $-1.0$ | 9 | 7–11 |

| Criterion | Pass (strong) | Pass (medium) | Fail |
|---|---|---|---|
| Group size | 22–24 | 20–26 | $< 20$ or $> 28$ |
| $\sum\|\tilde{\chi}(g)\|^2$ | 22–26 | 18–30 | $< 18$ |
| Trace deviation per class | $< 0.10$ | $< 0.15$ | $> 0.20$ |
| All elements unitary $\|g^\dagger g - \mathbb{1}\|$ | $< 0.05$ | $< 0.10$ | — |

**Robustness note:** minimum pairwise distance between distinct S₄ elements is 2.0 (operator norm). At $F_{\text{proc}} = 0.95$, the error ball radius is $\approx 0.22$. The separation margin is $2.0/(2 \times 0.22) \approx 4.5$ — robust. Closure test remains reliable at $F_{\text{proc}} > 0.93$.

### Test D — Flag Stability Test

**What it checks:** are the measured projectors $(P_1, P_2)$ reproducible across independent preparations?

**Procedure:** prepare under fixed non-axial $H_{\text{NV}}$; perform state tomography $N = 20$ times; extract $(P_1, P_2, P_3)$ each time.

| Criterion | Pass | Fail |
|---|---|---|
| Pairwise projector fidelity $\langle F_{ij}\rangle_k$ | $> 0.95$ | $< 0.90$ |
| Preparation variance $\sigma(\text{Tr}(\tilde{P}_k))$ | $< 0.02$ | $> 0.05$ |
| Torus phase stability | NOT REQUIRED — phases may drift freely | — |

**Key point:** projector stability is required; eigenvector phase stability is not. This is the physical meaning of "torus-free flag."

### Test E — Projector Covariance Test (The Decisive Test)

**What it checks:** do the measured projectors transform correctly under the realized S₄ action, in the way T₁ predicts — not just in any way?

This is the test that distinguishes a T₁-carrier flag from a generic qutrit flag. A generic SU(3) action on a generic $\mathbb{C}^3$ will move projectors around SU(3)/T, but NOT with the specific T₁ orbit structure.

**Procedure:**
1. Prepare $\rho$ with known flag $F^* = (P_1, P_2, P_3)$
2. For each of the 24 realized group elements $\tilde{U}_{g_k}$:
   - Apply $\tilde{U}_{g_k}$ to $\rho$: $\rho_k = \tilde{U}_{g_k} \rho \tilde{U}_{g_k}^\dagger$
   - State tomography → $\tilde{\rho}_k$ → extract flag $\tilde{F}^*_k = (\tilde{P}_{1,k}, \tilde{P}_{2,k}, \tilde{P}_{3,k})$
   - Compare to predicted: $g_k \cdot F^* = (U_{g_k} P_i U_{g_k}^\dagger)_i$
   - Compute: $F_{\text{cov}}(g_k) = \text{Tr}(\tilde{P}_{1,k} \cdot U_{g_k} P_1 U_{g_k}^\dagger)$

| Criterion | Strong win | Medium win | Fail |
|---|---|---|---|
| Mean covariance fidelity $\mathbb{E}_g[F_{\text{cov}}(g)]$ | $> 0.90$ | $> 0.80$ | $< 0.70$ |
| Max covariance error $\max_{g,i}\|\tilde{P}_{i,g} - g \cdot P_i\|_{\text{op}}$ | $< 0.15$ | $< 0.25$ | $> 0.30$ |
| Orbit distinguishability: $\min_{k\neq l}\|F^*_k - F^*_l\|_F$ | $> 0.10$ | $> 0.05$ | $< 0.05$ (orbit collapsed) |

**Why this test is decisive:** (1) prepare a reference flag $F^*$; (2) the 24 group elements should move it to 24 DISTINCT positions in SU(3)/T, consistent with the T₁ orbit structure; (3) a generic qutrit gate set that happens to have 24 elements would produce an orbit but with the WRONG distances and WRONG conjugacy-class groupings; (4) only a T₁-carrier produces the specific orbit predicted by the T₁ representation.

Reference flag orbit: mathematically, all 24 orbit points are distinguishable with minimum pairwise distance $\approx 1.20$ in Frobenius norm — well above any noise threshold.

---

## Block 3 — Minimal Experimental Protocol

**Platform:** single NV-center in diamond  
**Setup:** room temperature (or 77K), B-field 30–50 mT at ~45° to NV axis (transverse component essential), strain $E \approx 1$–10 MHz  
**Total time:** ~6–8 hours in one lab day

| Step | Action | Duration | Pass criterion |
|---|---|---|---|
| **0** | System characterization: confocal identification, ESR spectroscopy, frequency calibration | ~1 h | Three-level structure verified, frequencies $\omega_{01}, \omega_{02}, \omega_{12}$ measured |
| **1** | Basis calibration: reconstruct effective $C_3$ via Ramsey free-precession; verify $A_1\oplus E$ decomposition | ~30 min | $\phi_\pm = \pm2\pi/3 \pm 0.05$ |
| **2** | $\sigma_v$ calibration: calibrate $|+1\rangle \leftrightarrow |-1\rangle$ swap gate; QPT | ~15 min | $F_{\text{proc}}(\tilde{\sigma}_v) > 0.97$ |
| **3** | U₄ pulse implementation: calibrate $G_{01}$, $G_{02}$, $G_{12}$ pulses; sequence the 6-pulse circuit | ~1 h | Individual pulse fidelity $> 0.99$ per $G_{01/02}$; $G_{12}$ fidelity $> 0.97$ |
| **4** | QPT of $U_4$: 9-input-state QPT; reconstruct $\tilde{U}_4$; Test A | ~2 h | $F_{\text{proc}}(\tilde{U}_4) > 0.95$; spectral deviation $< 0.05$ |
| **5** | State tomography for flag: non-axial $H_{\text{NV}}$; measure $\rho$; eigendecompose to $(P_1, P_2)$; $N=20$ repetitions; Tests B, D | ~30 min | Projector fidelity $> 0.95$; variance $< 0.02$ |
| **6** | Projector covariance test: apply all 24 realized group elements to $\rho$; state tomography for each; covariance fidelity; Test E | ~2 h | $\mathbb{E}_g[F_{\text{cov}}] > 0.90$ (strong) or $> 0.80$ (medium) |
| **7** | Closure reconstruction: generate orbit from realized generators; count elements; check character distribution; Test C | ~30 min | 22–24 elements; trace distribution matches T₁ |

**Step 3 specifics — two-quantum $G_{12}$ calibration:**

The $G_{12}$ gate couples $|+1\rangle$ and $|-1\rangle$ directly. This requires either:
- (a) **Two-tone MW drive:** simultaneous drives at $\omega_{01}$ and $\omega_{02}$ with appropriate amplitudes; the two-quantum Rabi frequency is $\Omega_{12}^{(2)} = \Omega_{01}\Omega_{02}/(2\Delta)$
- (b) **Composite single-quantum sequence:** $G_{12}(\theta, \phi) = G_{01}(\pi/2, 0) \cdot G_{02}(\theta, \phi) \cdot G_{01}(-\pi/2, 0)$ (decomposes the two-quantum gate into three single-quantum pulses)

Option (b) is simpler and avoids two-tone calibration. This replaces $G_{12}$ with 3 standard pulses, making the full $U_4$ sequence 8 pulses total. Fidelity is similar.

---

## Block 4 — Decision Point

| Outcome | Classification | Bridge use? |
|---|---|---|
| Tests A–E all pass (strong thresholds) | **Strong physical win** — NV is a certified T₁-carrier flag selector | Yes — measured $(P_1, P_2)$ are honest bridge flag selectors |
| Tests A–D pass; Test E passes medium threshold | **Medium physical win** — NV realizes projective T₁ carrier | Yes — projective covariance is sufficient; projectors are phase-free |
| Tests A–B pass; Tests C–E borderline | **Weak win** — NV has correct S₃-skeleton but T₁-carrier claim unverified | Partial — flag is valid, T₁-carrier label is not certified |
| Test A or E fails decisively | **No-go** — T₁-carrier claim not supported on this hardware | No — must improve gate fidelity or use different platform |

**What a no-go means:** the math is not wrong. The NV triplet still has the correct S₃-skeleton (Tests B and D likely still pass). The no-go means the 4-cycle synthesis on this specific NV sample is insufficient. Fixes: composite pulse sequences; dynamical decoupling during the 6-pulse sequence; lower operating temperature; choose an NV with longer $T_2$.

**The bridge implication of medium win:** the projector covariance test at the medium threshold ($> 0.80$) is sufficient for the bridge flag identification. The bridge flag $F^*$ is determined by the eigenSPACES (phase-free projectors), not by eigenVECTORS (phase-bearing). A projective T₁-carrier certification is the physically correct standard.

---

## The Falsification Ladder Summary

```
TEST B — S3 skeleton (NV natural symmetry)
  FAIL → fundamental NV characterization problem, not a carrier issue
  PASS ↓

TEST A — 4-cycle spectral structure (U4 synthesis)
  FAIL → pulse synthesis insufficient; fix calibration, then retry
  PASS ↓

TEST D — Flag stability (reproducibility)
  FAIL → state preparation problem, not a carrier issue
  PASS ↓

TEST C — S4 closure (24-element group structure)
  FAIL → gate fidelity insufficient for 24-element orbit; F_proc < 0.93
  PASS ↓

TEST E — Projector covariance (DECISIVE)
  FAIL → NOT a T1-carrier (even with closure); wrong orbit structure
  PASS STRONG  → Strong physical win: certified T1-carrier flag selector
  PASS MEDIUM  → Medium win: projective T1-carrier; sufficient for bridge
```

---

**The next hammer goes here: implement the 6-pulse $U_{4,\text{NV}}$ sequence on the NV qutrit and perform the projector covariance test (Test E) — apply all 24 realized S₄ group elements to a reference state, measure the 24 resulting flags by state tomography, and check whether the orbit structure and covariance fidelities are consistent with the T₁ representation, with pass threshold $\mathbb{E}_g[F_{\text{cov}}(g)] > 0.80$ for medium win and $> 0.90$ for strong win.**

---

## References

### NV-Center Physics
- Doherty, M.W., Manson, N.B., Delaney, P., Jelezko, F., Wrachtrup, J. & Hollenberg, L.C.L. (2013). "The nitrogen-vacancy colour centre in diamond." Physics Reports 528(1):1-45. **(Foundational NV physics reference)**
- Smeltzer, B., Childress, L. & Gali, A. (2011). New J. Phys. 13:025021.
- Jelezko, F. & Wrachtrup, J. (2006). Phys. Stat. Sol. A 203:3207.

### S4 Representation Theory
- Serre, J.-P. (1977). *Linear Representations of Finite Groups*. Springer GTM 42.
- Fulton, W. & Harris, J. (1991). *Representation Theory: A First Course*. Springer GTM 129.
- Curtis, C.W. & Reiner, I. (1981). *Methods of Representation Theory*, vol. I. Wiley.

### Lie Groups and Gate Decomposition
- Hall, B.C. (2015). *Lie Groups, Lie Algebras, and Representations*, 2nd ed. Springer GTM 222.
- Helgason, S. (1978). *Differential Geometry, Lie Groups, and Symmetric Spaces*. Academic Press.
- Khaneja, N. & Glaser, S.J. (2001). Chem. Phys. 267:11-23. (KAK decomposition for quantum control)

### Quantum Information and Process Tomography
- Nielsen, M.A. & Chuang, I.L. (2010). *Quantum Computation and Quantum Information*, 10th anniv. ed. Cambridge University Press.
- Chuang, I.L. & Nielsen, M.A. (1997). J. Mod. Opt. 44:2455-2467. (Process tomography)
- Poyatos, J.F., Cirac, J.I. & Zoller, P. (1997). Phys. Rev. Lett. 78:390.

### TIG Framework (Novel — internal)
- Sanders, Mayes, Luther (2026). Sprint 13 Physical Flag Selector papers. 7Site LLC. DOI: 10.5281/zenodo.18852047.

### Citation Discipline
Novel contribution: explicit synthesis of U4 (the 4-cycle matrix of S4 in the T1 representation) as a 6-pulse microwave sequence on the NV-center qutrit, with machine-precision closure verification. Extends Doherty et al. 2013 (NV physics) and Serre/Fulton-Harris (S4 representation theory). See [GLOSSARY.md](../../../GLOSSARY.md).

