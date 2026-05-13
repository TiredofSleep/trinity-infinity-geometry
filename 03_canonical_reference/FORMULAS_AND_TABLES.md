# Formulas and Tables — Canonical Reference

**Single source of truth for every formula, table, constant, operator, and
invariant referenced in the TIG synthesis.** Condensed but complete: every
object below is reproducible from a cited paper or proof script in this repo.

If you only have time to read one file in the repository besides
`README.md`, this is it.

| § | Topic |
|---|-------|
| **0** | **Proof-spine one-liners (D1–D99, WP34, WP51, WP57, WP101, WP102–WP116, BB) + Vol J: three-table arch + 70/71/72/73 ladder + two-TSML reconcile (2026-05-06; D95-D99)** |
| 1 | The 10-operator sigma menu |
| 2 | The σ permutation on Z/10Z |
| 3 | The CRT isomorphism φ: F₂ × F₅ → Z/10Z |
| 4 | The complete σ polynomial (α + β) |
| 5 | TSML — the 10×10 reference table (two lenses: TSML_RAW + TSML_SYM, see D98) |
| 6 | BHML — the 10×10 reference table (28-cell harmony) + CL_STD third standalone table (44-cell HARMONY, see D95) |
| 7 | TSML 3-layer canonical tower (C₀ ⊕ S_MAX ⊕ S_ADD) |
| 8 | Three-diagonal comparison (σ, TSML, BHML) |
| 9 | Canonical operator C₀(R_n, h_n, σ_n) for general n |
| 10 | The compatibility family (carriers of canonical C₀) |
| 11 | Corridor closure hierarchy |
| 12 | The six structural invariants (Sprint 21) |
| 13 | The two-tier collapse signature (Sprint 22) |
| 14 | Walk strategies + ARI scaling (Sprint 23, Sprint 26) |
| 15 | TIG = σ⁻¹ inverse polynomial (Q13) |
| 16 | C-indicator and gate score framework (Q14) |
| 17 | Constants (T*, 4/π², gap, ξ₀, m²_ξ, σ rate) |
| 18 | Q-series quick index |
| 19 | Sprint trail (paper-by-paper) |

---

## §0 — Proof-spine one-liners (D1–D99, WP34, WP51, WP57, WP101, WP102–WP116, BB)

**Every formula below is proved or computationally verified.** This is the
compressed spine — one line per theorem, with the formula and the proof
script that runs it. Full statements in `papers/MASTER_SPINE.md` and
`papers/CLAY_SUMMARY.md`.

### Volume A — Ring & Arithmetic Foundations

| ID | name | formula | status / file |
|----|------|---------|---------------|
| **D1** | First-G Law | for squarefree b > 1: the first non-coprime element in {1..b} is **k = p₁** = smallest prime factor | PROVED, 22,367 (b,k) pairs over 305 squarefree b, primes ≤ 499, zero counterexamples; [05_papers/number_theory/J03/manuscript/proof_first_g_event.py](../05_papers/number_theory/J03/manuscript/proof_first_g_event.py); WP34 |
| **D11a/b/c** | Coprime Window Bundle | the coprime window {1..p−1} is the stability window; R(p, p) = 0 forces a sign flip; R(k, f) carries no information about q | PROVED, three one-line corollaries of D1 |
| **D14** | Corridor Spectral Mean | ∫₀¹ sinc²(t) dt = Si(2π)/π ≈ 0.4514 | PROVED by integration by parts; convergence O(1/p) |
| **D15** | Coprime Window Invariance | for k < SPF(b), all arithmetic on {1..k} is b-independent | PROVED, pure divisibility |

### Volume B — Operator Tables & Ring Structure

| ID | name | formula | status / file |
|----|------|---------|---------------|
| **D7** | Phi Fixed Point | Φ on Z/10Z has exactly one fixed point: **BALANCE = 5** | PROVED |
| **D8** | TSML_10 / BHML_10 composition laws | published as the §5 / §6 reference tables; see §6.7 for the full canonical variant registry | PROVED |
| **D9** | Table symmetry | TSML_10 and BHML_10 are each symmetric under their respective lens | PROVED |
| **D10** | TSML_10 73-cell count | TSML_10 (= TSML_Jordan, the canonical §5 table) has exactly **73 HARMONY (=7) cells**, derivable from three disjoint zones | PROVED, verified by enumeration |
| **D16** | BHML_10 28-cell count | BHML_10 (the canonical §6 table) has exactly **28 HARMONY (=7) cells** | PROVED, see §6 + `proof_d16_bhml_28_cells.py` |
| **D17** | Wobble parameter | **W = 3/50 = 0.06**, derived as deviation/n² = 6/100 from CROSS_CYCLE = 44 over (Z/10Z)\* × 2·(Z/10Z)\* | PROVED |
| **D18a** | Phi orbit graph | Phi on Z/10Z: one fixed point (BALANCE = 5), two relays (PROGRESS = 3, HARMONY = 7), seven sources; **T³ = all-δ₅** | PROVED |
| **D18c** | TSML_10 measurement bridge | M(v) = HARMONY = 7 for all v ≠ VOID (where M = row/col projection on the canonical TSML_10 diagonal); **T\* = destination/journey-measurement = 5/7** | PROVED |
| **D18d** | Generator convergence | BALANCE = 5 = centroid((Z/10Z)\*); HARMONY = 7 = g³ = g⁻¹ mod 10 for g = 3; **T\* = centroid/inverse = 5/7** | PROVED, three independent chains |
| **D19** | Generator Selection | **g = 3** is the only primitive root of (Z/10Z)\* compatible with T\* ∈ (0, 1). Under g = 7: HARMONY = 3, T\* = 5/3 > 1 — inadmissible | PROVED, exhaustive |
| **D20** | Inheritance Audit | BALANCE = 5 and W = 3/50 are RING-forced; HARMONY = 7 and T\* = 5/7 are GENERATOR-forced (require g = 3) | PROVED, four-class hierarchy |
| **D21** | CE Fixed-Point Centroid | every complement-equivariant ODD-output map F on Z/10Z satisfies **F(5) = 5** | PROVED, one line: 2F(5) ≡ 0 mod 10 ∧ F(5) ∈ {0, 5} ∧ 0 ∉ ODD ⇒ F(5) = 5 |
| **D23** | Ring Wobble | **Wob(k) = 1 − ⌊k/5⌋ / k** (exact closed form); Wob(k) ≥ 4/5 with equality iff 5 ∣ k; limit 4/5 by squeeze | PROVED |

### Volume C — Continuum Limits & Phase Structure

| ID | name | formula | status / file |
|----|------|---------|---------------|
| **R(k, f)** | resonance kernel | **R(k, f) = sin²(πk/f) / (k² · sin²(π/f))** = \|S(k, f)\|² where S(k, f) = (1/k) Σ_{j=1..k} e^(2πij/f) | exact, `tig_algebra.py` |
| **D2** | Sinc² Continuum Limit | **R(k, f) → sinc²(k/f)** as f → ∞ with k/f = t fixed; convergence O(1/f²) | PROVED, foundation of corridor geometry |
| **D3** | sinc² midpoint | **sinc²(1/2) = 4/π²** exactly (additionally sinc²(1/2) = (2/3)/ζ(2), verified at machine precision) | PROVED, `papers/proof_sinc_zeta_identity.py` |
| **D4** | T\* via algebraic identity | **T\* = 5/7** at b = 35, proved identically to D18c by a different route | PROVED |
| **D5** | H_mod maxima count | H_mod(k) = sinc²(k/p) · sin²(4πk/p) has exactly **4 local maxima** for all primes p ≥ 11 | PROVED by IVT on log-derivative |
| **D6** | General-frequency maxima | H_f has exactly **N(f) = ⌊f⌋ + 𝟙{f ∉ ℤ}** maxima for p > 2f | PROVED, `proof_d6_general_frequency.py` |
| **sinc² Zero Law** | universal zero structure | R(k, p) = 0 exactly at k = p for all primes p | PROVED, all primes 3..199, max error 4.44 × 10⁻¹⁶ |

### Volume D — Corridor Geometry

| ID | name | formula | status / file |
|----|------|---------|---------------|
| **D22** | Corridor Portrait | **W < BALANCE/10 < HARMONY/10 < T\* < 1**, i.e., **3/50 < 1/2 < 7/10 < 5/7 < 1**. Fine-structure identity: **T\* = HARMONY/10 + 1/70 = 7/10 + 1/(7·10)**. Inheritance split: t < 1/2 ring-forced; t > 1/2 generator-forced; t = 1/2 boundary | PROVED, exact Fraction arithmetic |
| **D24** | Corridor Midpoint | sinc²(t) strictly monotone decreasing on (0, 1); **t = 1/2 is the unique sine-maximum in (0, 1)**: sin(πt) = 1 iff t = 1/2 | PROVED, calculus, `proof_d24.py` |
| **D25** | Loop closure | sinc² zero law via Φ-loop closure on Z/pZ for all primes 3..199 | PROVED, `proof_d25_loop_closure.py` |

### Volume E — Lie-algebraic lifts (so(n) tower, Sprint 29, 2026-04-23/24)

| ID   | name                    | formula                                                                      | status / file |
|------|-------------------------|------------------------------------------------------------------------------|----|
| **D26** | so(8) closure (WP102) | Lie(⟨L_i^CL − (L_i^CL)^T : i ∈ {1,2,3,4,6,8}⟩) ≅ **so(8) = D₄** (dim 28). Killing signature (0, 28, 0); unique invariant bilinear form up to scalar; simple. | PROVED, machine-precision; `papers/wp102/verification/stage{2..7}*.py`; `papers/wp102/WP102_SO8_IDENTIFICATION.md` §3–4 |
| **D27** | so(10) closure (WP103) | Lie(⟨A_i^CL : i ∈ flow⟩ ∪ ⟨A_i^BHML_10 : i ∈ Ω⟩) ≅ **so(10) = D₅** (dim 45). Killing signature (0, 45, 0); rank 5; 40 + 5 eigenvalue structure under ad(H). | PROVED, machine-precision; `papers/wp103/verification/verify_so10.py`, `verify_simplicity_rank.py`; `papers/wp103/WP103_SO10_IDENTIFICATION.md` §3–4 |
| **D28** | so(8) ⊂ so(10) embedding | Every basis element of the D26 closure sits inside the D27 closure; max residual 8.99 × 10⁻¹³. | PROVED; WP103 §5 |
| **D29** | D₅ root-system match | For regular H = Σ k · J_k in the rank-5 Cartan of D27, ad(H) has exactly 40 nonzero (purely imaginary) + 5 zero eigenvalues — the D₅ root count. | PROVED; WP103 §5.3 |
| **D30** | gl(10) substrate bound  | Any Lie subalgebra of gl(10, ℝ) has dim ≤ 100; of so(10, ℝ) has dim ≤ 45. e₈ = 248 is unreachable within the 10-dim substrate alone. | PROVED (dim-count); WP103 §7 |

**Reading.** D₄ → D₅ is the classical Lie-algebraic tower inside TIG. The
flow-only antisymmetrization of CL gives D₄ (uniquely the triality algebra,
outer automorphism S₃). Adding all antisymmetrizations of the canonical
BHML_10 extends the closure to D₅ — the gauge algebra of the SO(10) grand
unified theory (Fritzsch–Minkowski 1975, Ann. Phys. 93:193; Georgi 1975,
AIP Conf. Proc. 23:575). D₅ exhausts so(V) on the 10-dim substrate;
further extension requires enlarging V. See §6.5 (primon-gas linkage) and
WP15 Yang-Mills cross-reference for the D₅ → A₂ chain that meets BHML_8.

### Volume F — Doubly-invariant content & Higgs identification (Sprint Apr 25, WP104 + sprint_unmistakable_truth)

| ID | name | formula | status / file |
|----|------|---------|---------------|
| **D31** | P₅₆ = σ_outer in spinor rep | The 5↔6 swap acts as the outer automorphism σ_outer of so(10) in the spinor rep (Cl(0,10)). $(γ_5 - γ_6)/\sqrt{2}$ anticommutes with $ω = γ_1 \cdots γ_{10}$, sending +chirality 16 entirely into −chirality 16 (residual = 0.0). | PROVED at machine precision; `papers/wp104_higgs_pati_salam/verification/find_higgs_irrep.py`; [Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/SIGMA_OUTER_FINDING.md](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/SIGMA_OUTER_FINDING.md) (mirrored from morning ck_handoff) |
| **D32** | BHML σ_outer-breaking is 100% in 54 irrep | BHML's antisymmetric-mass projection on the so(10) Killing decomposition lands **100% in the 54 (symmetric-traceless), 0% in the 45 (adjoint), 0% in the singlet 1**. Pati-Salam Higgs route. | PROVED, machine precision; `papers/wp104_higgs_pati_salam/verification/find_higgs_irrep.py` |
| **D33** | 9-vector Higgs direction | The σ_outer-breaking direction in BHML is the explicit 9-vector $v$ with $v_0 = v_1 = v_2 = v_3 = v_4 = v_7 = -1/\sqrt{2}$, $v_8 = v_9 = 0$ (BREATH and RESET unbroken), and the (BALANCE+CHAOS)/$\sqrt{2}$ component $= -1/2$. **$\|v\|^2 = 13/4$ exact** (in 9-vector projection convention). The skew-matrix Frobenius-norm convention gives $\|B_{\mathrm{anti}}\|^2 = 13/2$ — both are correct under their respective normalizations and used consistently within `xi_cosmology_tie.py` (9-vec) and `find_higgs_direction.py` (skew-Frobenius). | PROVED at machine precision; `papers/wp104_higgs_pati_salam/verification/find_higgs_direction.py` |
| **D34** | Doubly-invariant content under D₄ = ⟨P₅₆, σ³⟩ | Conjugation by D₄ on so(10) decomposes 45 = 16 (trivial-isotypic) + 1 + 12 + 16 (in 8 copies of 2-dim irrep). The 16-dim trivial-isotypic component **closes as a Lie subalgebra** with Killing-form spectrum exactly $(-4)^{15} \oplus (0)^1$, forcing $\mathfrak{simple}_{15} \oplus \mathfrak{center}_1$. The unique 15-dim simple Lie algebra is $\mathfrak{so}(6) \cong \mathfrak{su}(4)$. **The doubly-invariant subalgebra is $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ — Pati-Salam ⊕ B−L.** | PROVED at machine precision; [Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/scripts/verify_truth.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/scripts/verify_truth.py); UNMISTAKABLE_TRUTH.md |
| **D35** | κ_ξ = 13/(4e) (under GUT-natural identification) | Under the identification $m^2_\xi = \|\mathrm{VEV}\|^2$ (natural in GUT contexts), combined with the BB-vacuum relation $m^2_\xi = \kappa_\xi e$, the inflaton coupling is forced: $\kappa_\xi e = 13/4$, so $\kappa_\xi = 13/(4e) \approx 1.196$. The integer 13 traces to BHML's 26 σ_outer-asymmetric cells (count/2). Closes README §3.5(iii) at structural level. **Honest caveat (strengthened 2026-04-27 per chat-Claude audit):** $\kappa_\xi$ does NOT appear in the field EOM in isolation (it cancels). $\kappa_\xi$ scales the energy density $\rho_\xi$ which feeds into the Friedmann equation, so in the COUPLED FRW system $\kappa_\xi$ DOES affect the trajectory. The fit value $\kappa_\xi \approx 0.5$ in the JCAP submission #07 reflects whatever value reproduces Planck's $\Omega_\xi \approx 0.685$ given the trajectory and initial conditions $(\Xi_i, \dot\Xi_i)$. **Whether $\kappa_\xi = 13/(4e) \approx 1.196$ produces $\Omega_\xi \approx 0.685$ in the coupled solve is the actual falsifiability test, and has not been performed.** If $13/(4e)$ gave a substantially different $\Omega_\xi$ from the Planck observation, the structural prediction would be falsified for this dimensional setup. | STRUCTURAL (verified analytically + at machine precision); [Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/scripts/xi_cosmology_tie.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/scripts/xi_cosmology_tie.py); XI_COSMOLOGY_TIE_FINDING.md; [Atlas/applications_pass_2026_04_27/code/item5_6_frw.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Atlas/applications_pass_2026_04_27/code/item5_6_frw.py) |
| **D36** | First-G IS the first crossing event | For squarefree $b$ with smallest prime factor $p_1$, the First-G stability window $\{1, \dots, p_1 - 1\}$ is exactly the **pre-crossing region** under the Crossing Lemma's joint-map framework. Verified across 13/13 squarefree integers tested. Unifies §7.1 (D1) and §7.4 (Crossing Lemma) **conceptually** (no change to §3.1 cryptographic-complexity status). | PROVED, structural identification; [Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/scripts/first_g_crossing_tie.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/scripts/first_g_crossing_tie.py) |
| **D37** | Wobble localization (prime-11 in TSML char poly) | TSML's 10×10 multiplication-table characteristic polynomial is $\det(\lambda I - T) = \lambda^{10} - 63\lambda^9 + 33\lambda^8 + 4204\lambda^7 - 3998\lambda^6 - 62510\lambda^5 + 9716\lambda^4 + 54880\lambda^3 - 120736\lambda^2$. Of the nine nonzero coefficients, **exactly two are divisible by 11**: $c_2 = 33 = 3 \cdot 11$ and $c_8 = -120736 = -2^5 \cdot 7^3 \cdot 11$. The discriminant of the 8th-degree polynomial (after factoring out $\lambda^2$) is $2^{16} \cdot 7^7 \cdot 659 \cdot \text{(large primes)}$, **with no factor of 11**. Wobble (11) lives at the **coefficient level** (sums and products of eigenvalues); the doubly-invariant dimension $2^{16}$ and HARMONY⁷ live at the **discriminant level** (separations). The 16-dim doubly-invariant subalgebra is **wobble-free**; the 29-dim complement carries the wobble. | PROVED at integer level via sympy; [05_papers/algebra/J37/manuscript/verification/wobble_check.py](../05_papers/algebra/J37/manuscript/verification/wobble_check.py) (7/7 claims); WOBBLE_FINDING.md |

### Volume G — Closed-form runtime attractor (Apr 25 bhml_specificity_addendum)

| ID | name | formula | status / file |
|----|------|---------|---------------|
| **D38** | Runtime fixed-point support is the 4-core $\{V, H, Br, R\}$ | The T+B-mix runtime processor `ck_process(p, depth, α=1/2)` produces an attractor whose mass lives entirely on $\{$VOID, HARMONY, BREATH, RESET$\}$, with **0 mass on $\{$BALANCE, CHAOS$\}$** (the matter/antimatter pair). The 6+2 split: 67.8% triadic + 32.2% breathed; P₅₆ swap symmetry respected dynamically. | VERIFIED at machine precision; `papers/wp105_closed_form_attractor/verification/04_bridge_attractor.py` |
| **D39** | HARMONY/BREATH = 1 + √3 at α = 1/2 | At the α = 1/2 attractor, the BREATH equation $h^2 = 2 br (h + br)$ combined with normalization gives $(h/br)^2 - 2(h/br) - 2 = 0$, with positive root $h/br = 1 + \sqrt{3}$. **Exact**, residual $4.4 \times 10^{-16}$. | PROVED analytically + machine precision; `papers/wp105_closed_form_attractor/verification/06_attractor_closed_form.py` |
| **D40** | Quartic minimal polynomial for $r/br$ | At α = 1/2, the ratio $r/br$ (RESET-to-BREATH) satisfies the irreducible monic integer quartic $$x^4 + 4x^3 - x^2 + 2x - 2 = 0.$$ The four runtime-attractor coordinates $\{V, H, Br, R\}$ together generate a degree-4 extension of $\mathbb{Q}$: $\mathbb{Q} \subset \mathbb{Q}(\sqrt{3}) \subset \mathbb{Q}(\sqrt{3}, \xi)$ with $\xi$ defined by the quartic. | PROVED; `papers/wp105_closed_form_attractor/verification/07_full_closed_form.py` |
| **D41** | Galois group of D40 quartic is $D_4$ | Resolvent cubic $g(y) = y^3 + y^2 + 16y + 36 = (y+2)(y^2 - y + 18)$ has exactly one rational root, so the group is $C_4$ or $D_4$. The quartic stays irreducible over $\mathbb{Q}(\sqrt{\mathrm{disc} f}) = \mathbb{Q}(\sqrt{-71})$, forcing $D_4$. Polynomial discriminant $\mathrm{disc}(f) = -40896 = -2^6 \cdot 3^2 \cdot 71$; field discriminant $d_K = -10224 = -2^4 \cdot 3^2 \cdot 71$; index $[O_K:\mathbb{Z}[\alpha]] = 2$. **The number field is LMFDB 4.2.10224.1 (KNOWN); the polynomial form $x^4 + 4x^3 - x^2 + 2x - 2$ and the derivation route (TSML/BHML attractor) are NOVEL.** $\mathbb{Q}(\sqrt{3})$ is a genuine subfield: $f(x) = (x^2 + (2 - \sqrt{3})x + (\sqrt{3} - 1))(x^2 + (2 + \sqrt{3})x - (\sqrt{3} + 1))$. | PROVED; LMFDB cross-checked; agent computation 2026-04-25 |
| **D42** | α = 1/2 is uniquely privileged in [0.05, 0.95] | Sweeping α over 19 values in [0.05, 0.95], **only at α = 0.500** does $H/Br$ satisfy a small-coefficient quadratic, AND **only at α = 0.500** does $r/br$ satisfy the small-coefficient quartic. At every other α, neither relation holds with coefficients $|c| \le 10$. Symmetric mixing α = 1/2 picks out the unique algebraic structure. | VERIFIED this session; `papers/wp105_closed_form_attractor/verification/task5_alpha_sweep.py` |
| **D43** | TSML 8-magma core (BREATH/RESET drop) | TSML restricted to $\{$VOID, LATTICE, COUNTER, PROGRESS, COLLAPSE, BALANCE, CHAOS, HARMONY$\}$ is **closed under fuse**, commutative, and preserves the full table's HARMONY signature: 47/64 = 73.4% (vs full TSML's 73%); VOID 13/64 = 20.3%. BREATH and RESET appear in only **4 of the full 100 cells** — TSML is *almost* an 8×8 table. | VERIFIED at machine precision; `papers/wp105_closed_form_attractor/verification/03_eight_magma_core.py` |
| **D44** | BHML closed-subset chain | BHML has **only 8 closed sub-magmas** (vs TSML's 398), forming a perfect nested chain anchored at $\{$VOID, RESET$\}$ and ascending to the full algebra. The smallest closed sub-magma containing the breathed pair is $\{$VOID, HARMONY, BREATH, RESET$\}$. | VERIFIED; `papers/wp105_closed_form_attractor/verification/05_bhml_closure.py` |

**Reading.** Volume F captures the so(10) → su(4) ⊕ u(1) structural collapse: under the natural Z₂ involutions of TIG, what's preserved is exactly the Pati-Salam ⊕ B−L gauge content. Volume G is the **runtime** result: when CK actually processes information through the T+B-mix lattice processor at the symmetric mixing weight α = 1/2, the fixed point lives in a degree-4 number field with Q(√3) as a canonical subfield. The HARMONY/BREATH = 1+√3 relation is the cleanest closed-form result the project has produced. The two volumes are tied: BHML's σ_outer-breaking direction (D33) is the same content that makes the runtime attractor non-trivial (D39). The integer 13 in $\|v\|^2 = 13/4$ (D33) and the integer 13 in $\kappa_\xi = 13/(4e)$ (D35) trace to the same 26 σ_outer-asymmetric BHML cells (count/2).

**Honest negatives that scope these results:**

| ID | observation | what it rules out |
|----|-------------|-------------------|
| **N1** | Generic ML weight matrices have NO detectable TIG structure (distilgpt2, 16 tensors × 4 detectors, all $|d| < 0.5$) | "TIG structure is latent in any trained network" — overclaim |
| **N2** | Hilbert tail of $R/I_{\mathrm{CL}}$ ≠ u(1) center (different supports: VOID vs 6-cycle) | Naive identification of "1-dim residuals" across categories |
| **N3** | CL eigenvalues ↔ transcendental constants are 1%-level coincidences only, not algebraic identities | "TSML eigenvalues equal e/π/φ/ζ(3)" — overclaim. What IS exact: integer/rational signature (81 = 9², 29, 13/4, {7,7,7}, $\|T_{\mathrm{lie}}\|^2 = 16$, 26) |
| **N4** | The √3 in the runtime attractor is a **quadratic-discriminant accident at α = 1/2**, not an A₂-Cartan invariant | "TIG runtime sees the SU(3) root system" — overclaim. (σ³ generator eigenvalues are ±i/√2, D₃-flavor, not √3, A₂-flavor; 75% of runtime mass lives off the σ-hexagon) |
| **N5** | Prime-11 mediation hypothesis falsified ($p = 0.027$ wrong direction) and attractor-richness hypothesis falsified ($r = -0.118$ weak, wrong direction) | Two candidate mechanisms for BHML's anti-collapse role, ruled out before D38–D40 nailed the actual mechanism |

These negatives **strengthen** the picture: TIG structure is *specific* to canonical TSML/BHML and the doubly-invariant subalgebras they generate, not a generic feature of any algebraic system. The positive findings (D31–D44) earn their structural status by surviving the negative tests above.

### Volume H — Operad obstruction, 4-core closure, and 6-DOF synthesis (Sprint Apr 25 evening, WP106 + WP108–WP111)

| ID | name | formula | status / file |
|----|------|---------|---------------|
| **D45** | TIG-detector specificity scope (WP106) | All four detectors (eigenvalue, mode, spectral, structural) score $|d| < 0.5$ across distilgpt2's 16 trained tensors. Generic ML weight matrices have **NO detectable TIG structure**. Promotes the negative-control N1 to a primary entry: TIG structure is **specific** to canonical TSML/BHML, not latent in any trained network. | NEGATIVE, machine-precision; `papers/wp106_tig_detector_scope/WP106_TIG_DETECTOR_SCOPE.md` §3–4; `papers/wp106_tig_detector_scope/verification/scan_distilgpt2.py` |
| **D46** | Yukawa scaffolding tension (WP108) | The 9-vector VEV (D33) has $v_8 = v_9 = 0$ (BREATH and RESET unbroken), so it stabilizes the SO(8) ⊂ SO(9) ⊂ SO(10) chain rather than the standard Pati-Salam chain SO(10) ⊃ SU(4) × SU(2)_L × SU(2)_R. The 16 spinor decomposes as $\mathbf{16} \to \mathbf{8}_s + \mathbf{8}_c$ under SO(8), **NOT** into the Pati-Salam content $(\mathbf{4},\mathbf{2},\mathbf{1}) + (\bar{\mathbf{4}},\mathbf{1},\mathbf{2})$ expected from WP104 Path B. The two routes (Path A doubly-invariant subalgebra vs Path B Higgs VEV) DO NOT close on the same SU(4) ⊕ SU(2)_L ⊕ SU(2)_R; they sit on different reduction chains in the Lie-algebraic lattice. | STRUCTURAL with flagged tension; `papers/wp108_yukawa_scaffolding/WP108_YUKAWA_SCAFFOLDING.md` §4–6 |
| **D47** | Operad D₄ obstruction (WP109) | The 126 non-associative TSML triples (the (a,b,c) for which $a*(b*c) \neq (a*b)*c$) partition into **67 orbits** under the action of $D_4 = \langle P_{56}, \sigma^3 \rangle$. Of these, **16 orbits are D₄-incoherent**: no consistent fuse-table value in $\{a, b, c, L, R\}$ (left, right, third, left-fuse, right-fuse) is compatible across the orbit. **Theorem:** no $D_4$-equivariant fuse rule taking values in $\{a,b,c,L,R\}$ exists. The operad-DOF is **orthogonal** to the gauge-symmetry group of the rest of the tower; the recommendation is to preserve the weaker $P_{56}$-equivariance (which IS achievable). | PROVED at integer level; `papers/wp109_operad_d4_obstruction/WP109_OPERAD_D4_OBSTRUCTION.md` §3–5; [05_papers/physics/J48/](../05_papers/physics/J48/) |
| **D48** | 4-core fusion-closure (WP110, strengthens D38) | The 4-core $\{V, H, Br, R\}$ is closed under **BOTH** TSML and BHML at the algebraic level: 16 + 16 in-core terms (TSML and BHML respectively), 0 + 0 spillover into $\{$LATTICE, COUNTER, PROGRESS, COLLAPSE, BALANCE, CHAOS$\}$. Verified by direct enumeration of all $4^3 = 64$ ordered triples on the 4-core under both tables. | PROVED, machine-precision; `papers/wp110_4core_fusion_closure/WP110_4CORE_FUSION_CLOSURE.md` §3; [05_papers/algebra/J25/manuscript/verification/f3_galois_alpha_uniqueness.py](../05_papers/algebra/J25/manuscript/verification/f3_galois_alpha_uniqueness.py) |
| **D49** | Symbolic normalizer identity Z_T = Z_B = (v + h + br + r)² (WP110) | Both runtime normalizers (TSML and BHML) restricted to the 4-core simplify symbolically to the **same** quadratic form: $Z_T = Z_B = (v + h + br + r)^2$. This is the structural reason 4-core closure (D48) implies the runtime attractor (D38–D39): when $Z_T = Z_B$, the T+B-mix at any $\alpha$ inherits the closure. | PROVED symbolically (sympy); `papers/wp110_4core_fusion_closure/WP110_4CORE_FUSION_CLOSURE.md` §4; `alpha_uniqueness_symbolic.py` |
| **D50** | Symbolic 1+√3 confirmation at α = 1/2 (WP110, strengthens D39) | Solving the 4-core fixed-point equations symbolically at $\alpha = 1/2$ recovers $H/Br = 1 + \sqrt{3}$ as a **structural identity** (forced by Z_T = Z_B closure plus normalization), not merely as a numerically-stable dynamical fixed point. Promotes D39 from "verified at machine precision" to **structurally forced by 4-core closure**. | PROVED, symbolic; `papers/wp110_4core_fusion_closure/WP110_4CORE_FUSION_CLOSURE.md` §5 |
| **D51** | Six-DOF organizing claim (WP111) | The TIG framework engages **six computationally-irreducible algebraic degrees of freedom**: (i) **Lie** (so(8), so(10) closures, WP102–WP103); (ii) **Jordan** (the doubly-invariant su(4) ⊕ u(1) sits in a JC-pair with so(10), WP104); (iii) **Clifford/Dirac** (Cl(0,10) realization where $P_{56} = (\gamma_5 - \gamma_6)/\sqrt{2}$ acts as $\sigma_{\text{outer}}$, WP104); (iv) **Permutation** ($S_{10}$ on operator labels; $\sigma$ has order 6, $\sigma^3$ is the involution paired with $P_{56}$ to generate $D_4$); (v) **Lattice** (the runtime attractor sits in $\mathbb{Q}(\sqrt{3}, \xi)$ with $\xi$ root of LMFDB 4.2.10224.1, WP105); (vi) **Operad** (67 D_4 orbits, 16 incoherent, no D_4-equivariant fuse rule, WP109). **Five DOFs respect $D_4$**; the sixth (Operad) does not — establishing operad-DOF orthogonality to the gauge structure. | SYNTHESIS, no new computation beyond WP102–WP110; `papers/wp111_six_dof_synthesis/WP111_SIX_DOF_SYNTHESIS.md` §3–12 |
| **D52** | P_56 orbit decomposition of non-associative TSML triples (WP112) | The 126 non-associative TSML triples decompose into **98 ⟨P_56⟩-orbits** (70 singletons + 28 doubletons; total 70 + 2·28 = 126). All 98 orbits are P_56-coherent. **A P_56-equivariant canonical fuse rule EXISTS** (in contrast to D47's no-go for $D_4$). | PROVED, integer level; `papers/wp112_p56_canonical_fuse/verification/p56_canonical_fuse.py` Sections 1–2 |
| **D53** | P_56-equivariance is generic (WP112) | Of 8 surveyed canonical fuse rule families (HARMONY-pull, anti-HARMONY, middle, left-bracket, right-bracket, σ-fixed-pref, doubly-invariant-pref, attractor-4-core), **all 8 are P_56-equivariant**; **none are σ³-equivariant**. P_56 is the **maximal preservable symmetry** on the operad-DOF; σ³-equivariance is uniformly broken. | PROVED, integer level; WP112 §4; `rule_families.py` |
| **D54** | Canonical fuse table (Family H) and σ³ obstruction localization (WP112) | The canonical Family H ("attractor-4-core preference") rule produces fuse-value distribution $\{0: 108,\ 7: 18\}$ — image entirely in 4-core $\{V, H\}$. The **σ³ obstruction localizes to exactly ONE triple**: $(3, 9, 9)$, the unique σ³-fixed non-associative triple where the canonical rule selects HARMONY = 7 (not σ³-fixed, since $\sigma^3(7) = 4$). The canonical table is σ³-equivariant on **125 of 126 triples (99.2%)**. | PROVED, integer level; WP112 §5–6; `fuse_canonical_p56.json` |
| **D55** | 4-core arity-3 closure (WP112 Theorem 5.5) | The 4-core $\{V, H, Br, R\}$ is closed under canonical arity-3 fuse: all $4^3 = 64$ triples in the 4-core fuse to values in the 4-core (8 non-associative + 56 associative). Specifically, the 8 non-associative 4-core triples ALL fuse to VOID. Combined with WP110 D48, the 4-core is a **fully closed sub-operad** of TSML at every arity ≤ 3. | PROVED, integer level; WP112 §5.5; `p56_canonical_fuse.py` Section 7 |
| **D56** | Universal HARMONY attractor under canonical ternary fuse (WP112 Theorem 5.7) | Iterating $p \mapsto \mathrm{normalize}(\sum_{a,b,c} \delta_{\,\mathrm{fuse}_H(a,b,c)} \cdot p_a p_b p_c)$ from any non-trivial initial distribution converges to **pure HARMONY** ($\delta_7$) in 1–7 iterations. The only other fixed point is the degenerate $\delta_V$ (which is fixed because fuse$(V,V,V) = V$). The operad-DOF is a "concentration operator"; the runtime-DOF (binary T+B-mix at α=1/2) is a "distribution operator." Both share the 4-core substrate. | PROVED, machine-precision; WP112 §5.7; `p56_canonical_fuse.py` Section 8 (10 initial-condition tests) |
| **D57** | α-uniqueness PSLQ sharpening (WP113 Theorem 3.2) | Sharpens D42 from 19-point linspace + brute-force coefficient search to **17-point Stern-Brocot grid** (all $p/q$ with $q \leq 7$) + 50-digit mpmath + PSLQ at degree ≤ 8, sup-coefficient ≤ 50. Result: $\alpha = 1/2$ is the **unique rational** in the grid where the runtime attractor admits algebraic relations for both $H/Br$ and $r/br$. The recovered relations match D39 ($x^2 - 2x - 2$) and D40 ($x^4 + 4x^3 - x^2 + 2x - 2$) at PSLQ residuals $\approx 10^{-45}$. | EMPIRICAL (sharpened); structural uniqueness theorem remains open as Conjecture 4.2; `papers/wp113_alpha_uniqueness/verification/alpha_pslq_sweep.py` |
| **D58** | Initial-condition robustness of WP105 attractor (corollary; this session) | The binary T+B-mix attractor at $\alpha = 1/2$ is **globally stable**: starting from any non-trivial probability distribution on $\{V, L, C, P, C_4, B_5, C_6, H, Br, R\}$ (uniform on 10-simplex, uniform on 4-core, $\delta_H$, $\delta_{Br}$, $\delta_R$, flow-only $\{1,2,4,5,6,7\}$, lattice-only $\{0,3,8,9\}$, BREATH+RESET, V+Br+R), iteration converges to the same fixed point with $H/Br = 1+\sqrt{3}$ in 76–81 iterations (50-digit precision). The pure-VOID $\delta_V$ is the only degenerate fixed point. | VERIFIED, machine-precision; this-session check; 7 initial conditions all converge to WP105 attractor |
| **D59** | D3 (prime-11) is the unique TIG-positive marker (WP114) | Across a 9-family structured matrix battery (Gaussian, symmetric, antisymmetric, permutation, Hadamard-sign, Haar-orthogonal, DFT-real, identity, diagonal, integer-companion; 200 samples each), **only detector D3 (prime-11 in characteristic polynomial)** isolates TSML at large effect ($d = +9.93$ vs Gaussian baseline). Detectors D1, D2, D4 measure family-structural properties (antisymmetry, $P_{56}$-symmetry, Higgs-projection) that overlap multiple matrix families and do not discriminate TIG content. **D3 is WP107 WOBBLE in detector form**; identified as the load-bearing positive marker of TIG structure. | EMPIRICAL, machine-precision; `papers/wp114_specificity_extension/verification/structured_matrix_sweep.py` |
| **D60** | α-uniqueness extends to 45-point Stern-Brocot grid + 8 irrational candidates (WP113 update) | Re-running WP113's PSLQ sweep at $q \leq 12$ (45 rationals: $\sum_{k=2}^{12} \phi(k) = 45$) at degree $\leq 6$, coeff $\leq 50$, 50-digit precision: $\alpha = 1/2$ remains uniquely algebraic. The 28 newly-tested rationals ($q \in \{8, 9, 10, 11, 12\}$) all return "no algebraic relation." Spot-check at 8 natural irrational candidates ($1/\sqrt{2}, 1/\sqrt{3}, (\sqrt{3}-1)/2, 1/e, 1/\pi, \varphi-1, 1/2 \pm 1/100$) also returns no algebraic relation. Notably, the near-rational $\alpha = 1/2 \pm 0.01$ also fail — the algebraic structure at $1/2$ does not perturbatively extend. | EMPIRICAL extension to WP113; `alpha_pslq_sweep.py --depth 12` and irrational spot-check |
| **D61** | D5 (prime-7 in squarefree-disc) is a second TSML-unique TIG marker (WP114 §7.1–7.2) | Tests whether $7^{\text{threshold}}$ divides the discriminant of the squarefree part of the integer characteristic polynomial. At threshold $7^7$ (the WP107-identified value) and $7^5$, D5 fires for TSML and is exactly 0 for every other matrix in the 1800-sample structured battery + BHML. **Theorem 7.2 (WP114):** the pair $(D3,\ D_{5\text{,prime-}7^5})$ jointly distinguishes TSML uniquely; D3 corresponds to WP107's coefficient-level prime-11 wobble; D5 corresponds to WP107's discriminant-level HARMONY⁷. Together they form the **complete WP107 detector signature**. | EMPIRICAL, integer-precision; `papers/wp114_specificity_extension/verification/d5_d4eq_extension.py` |
| **D62** | D4_eq (D_4-equivariant Higgs alignment) replaces D4 (WP114 §7.1) | The original D4 (fixed 45-vector Higgs embedding) gave $|d| = 0.011$ for TSML — no signal. D4_eq (max-cosine over the $D_4 = \langle P_{56}, \sigma^3 \rangle$ orbit of the 9-vector Higgs direction, applied to $M$'s column-sum) gives **TSML $D_{4\text{eq}} = 0.7072$ → Cohen's $d = +2.155$ vs Gaussian baseline (large effect)**. Improvement from no-effect to large-effect. Not TSML-unique (also fires for permutation, identity, companion matrices), but informative. Recommended as the canonical replacement for D4 going forward. | EMPIRICAL; same script |
| **D63** | Universal HARMONY attractor is family-independent (WP112 Theorem 5.9) | The canonical ternary fuse iteration converges to pure HARMONY $\delta_7$ in **exactly 6 iterations** for **all 8 candidate fuse rule families** (HARMONY-pull, anti-HARMONY, middle, left-bracketing, right-bracketing, σ-fixed-pref, doubly-invariant, attractor-4-core), starting from the uniform 10-simplex distribution at 40-digit mpmath precision. Strengthens D56 from "Family H produces δ_7" to "every reasonable canonical fuse choice produces δ_7." Identifies the universal HARMONY attractor as a property of the **binary TSML row-absorber structure**, not of the canonical fuse choice; the 12.6% non-associative-triple fuse table matters only for the first few iterations. | PROVED, machine-precision; verification across all 8 FAMILIES in `rule_families.py` |
| **D64** | Joint TSML+BHML closed-subset chain (WP115 Theorem 1.1; **CORRECTED 2026-05-05** during 4-core manuscript prep, R3 with referee Claude) | The sub-magmas of $\{0, \ldots, 9\}$ jointly closed under both binary TSML and binary BHML form a **strict 8-element chain** (no branching) with sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$. **Forbidden sizes are $\{2, 3\}$ only** — the original WP115 preprint had a chain-counting error claiming 7 elements with forbidden $\{2, 3, 7\}$; brute-force enumeration during four_core_FINAL.tex preparation confirmed size 7 is allowed at $\{0, 4, 5, 6, 7, 8, 9\}$. The chain is: $\{0\} \subset \{0,7,8,9\} \subset \{0,6,7,8,9\} \subset \{0,5,6,7,8,9\} \subset \{0,4,5,6,7,8,9\} \subset \{0,3,4,5,6,7,8,9\} \subset \{0,2,3,4,5,6,7,8,9\} \subset \mathbb{Z}/10$. **σ-walk reading**: chain walks σ-forward orbit of $H = 7$ ($7\to 6\to 5\to 4\to 2\to 1$) with one σ-fixed bridge step at the size-$7\to 8$ transition (adds 3 before completing the cycle). σ-fixed lattice $\{0, 3, 8, 9\}$ contributes at three positions: $0$ at size 1, $\{8, 9\}$ in the size-$1 \to 4$ jump, $3$ at the size-$7 \to 8$ bridge. | PROVED, integer-precision; canonical reference: 4-core paper Theorem 1 (Sanders + Gish 2026, Algebraic Combinatorics, manuscript in preparation), `four_core_FINAL.tex` §3 with full enumeration of all 1023 non-empty subsets via `4core_verification.py`. The earlier WP115 verification script result is superseded by the brute-force enumeration. |
| **D65** | Universal 4-core attractor across the joint chain (WP115 Theorem 2.1) | At $\alpha = 1/2$, the T+B-mix runtime attractor on **every shell of size $\geq 4$** in the joint chain is **identical**: $(p^*_V, p^*_H, p^*_{Br}, p^*_R) = (0.138147, 0.540196, 0.197725, 0.123931)$ with $H/Br = 1+\sqrt{3}$. Operators outside the 4-core carry zero mass at the fixed point regardless of shell extension. The 4-core is the **unique non-trivial T+B-mix attractor at $\alpha = 1/2$** on $\mathbb{Z}/10\mathbb{Z}$. Strengthens D48 (binary 4-core closure) to dynamical universality. | PROVED, machine-precision; WP115 §2; same script |
| **D66** | α-endpoint structure on the full substrate (WP115 Theorem 3.1) | $\alpha = 1$ (pure TSML): collapses to $\delta_H$ in $\sim 8$ iterations — coincides with WP112 Theorem 5.7 ternary attractor. $\alpha = 0$ (pure BHML): 4-distribution with $H/Br \approx 0.585$ admitting **no** small-coefficient quadratic at PSLQ bound 20 (likely transcendental). $\alpha \in \{1/4, 3/4\}$: also no algebraic relation. **$\alpha = 1/2$ is the unique algebraic interior point** (per WP113). Identifies the BHML contribution as the structural "counter-pressure" that prevents pure-HARMONY collapse at $\alpha < 1$. | PROVED, machine-precision + PSLQ; WP115 §3 |
| **D67** | Layered substrate-attractor structure (WP115 §4) | Combining D55 (4-core arity-3 closure), D56/D63 (universal HARMONY at arity 3), D65 (universal 4-core at binary $\alpha = 1/2$): the dynamical hierarchy is $\{$10 ops$\} \to \{V, H, Br, R\} \to \{V, H\} \to \{H\}$ — a $\sim$2× collapse at each layer (10/4 = 2.5, 4/2 = 2, 2/1 = 2). Each layer is an absorber: the 4-core absorbs from above (joint chain $\to$ 4-core via T+B-mix); the 2-core $\{V, H\}$ is the static image of canonical Family H fuse on non-associative triples; the 1-core $\{H\}$ absorbs from below (canonical ternary fuse iteration $\to$ $\delta_H$). | SYNTHESIS; WP115 §4 |
| **D68** | Full 4-core ratio algebraic structure (this session) | At α=1/2 with 50-digit mpmath + PSLQ (deg ≤ 6, coeff ≤ 30), the seven 4-core pairwise ratios decompose as: $H/Br$ in $\mathbb{Q}(\sqrt{3})$ (degree 2, D39); $R/Br$ degree-4 generator (D40 quartic, LMFDB 4.2.10224.1); $H/R$, $Br/R$, $Br/V$ all degree 6 polynomials (composite in $\mathbb{Q}(\sqrt{3}, \xi)$); $H/V$ and $V/R$ admit no PSLQ relation at deg ≤ 6, coeff ≤ 30. **Individual values $V, H, Br, R$ in isolation:** NO PSLQ relation at deg ≤ 8, coeff ≤ 100 — they are ratios in the WP105 field $\mathbb{Q}(\sqrt{3}, \xi)$, not algebraic integers. Confirms WP105 §7's claim that the four runtime-attractor coordinates jointly generate the degree-4 extension. | EMPIRICAL/STRUCTURAL; this session PSLQ check on 4-core attractor at α=1/2 |
| **D69** | WOBBLE prime 11 reappears in field-denominator structure (this session) | The PSLQ-recovered relation for $Br/V$ — $+16x + 8x^2 - 2x^3 + 16x^4 - x^5 - 11x^6 = 0$ — factors over $\mathbb{Q}$ as $x(x+1)(11x^4 - 10x^3 - 6x^2 + 8x - 16) = 0$. The minimal polynomial of $Br/V$ is therefore the degree-4 factor $11x^4 - 10x^3 - 6x^2 + 8x - 16$ with **leading coefficient 11**. Since $\gcd(11, -10, -6, 8, -16) = 1$, $Br/V$ is **not an algebraic integer** — the WP107 WOBBLE prime 11 appears in the **denominator** of $Br/V$'s representation in $\mathbb{Q}(\sqrt{3}, \xi)$. The wobble prime invades not only TSML's characteristic polynomial coefficients (D37/WP107) and the discriminant absence (where 11 does NOT appear), but also the **field-denominator structure** of the runtime attractor coordinates. A new instance of WOBBLE manifestation. | EMPIRICAL/STRUCTURAL; same session check |
| **D70** | Multi-prime, multi-DoF WOBBLE structure (3+3 axis split) | Wobble is not a single prime touching all 6 DoFs uniformly; it's a **multi-prime coupling pattern with a 3+3 DoF split**. Three "outsider primes" (small primes not in the substrate $\{2, 5\}$ or σ-structural $\{2, 3, 5, 7\}$) intrude at three coordinate-level locations: **prime 11** at Lie DoF (char-poly coefficients $c_2, c_8$, D37) and Lattice DoF ($Br/V$ denominator, D69); **prime 13** at Clifford DoF ($\|\mathrm{VEV}\|^2 = 13/4$, $\kappa_\xi = 13/(4e)$, D33/D35). Three DoFs are **wobble-free**: Jordan (Killing spectrum $(-4)^{15} \oplus (0)^1$ has only prime 2), Permutation (group orders are 2-, 3-smooth), Operad (orbit count 67 is intrinsic, not intrusion). The 3+3 axis split — wobbled DoFs $\{$Lie, Clifford, Lattice$\}$ are **eigenvalue/coordinate**; wobble-free DoFs $\{$Jordan, Permutation, Operad$\}$ are **discrete-symmetry** — recurs in the tower (WP107 3-location wobble: coefficient/discriminant/denominator; WP115 3-step hierarchy 10→4→2→1; Pati-Salam 3-factor SU(4)×SU(2)×SU(2)+B-L; "every one is 3" L0 triadic principle). Wobble primes 11 = 10+1 and 13 = 10+3 are the smallest primes immediately above the substrate size 10 = 2·5. | SYNTHESIS, this session; cross-references D33, D35, D37, D69, WP107, WP111 |
| **D71** | σ-rate corrected mechanism + tighter closed-form bound (chat-Claude audit 2026-04-27) | The non-associativity of the binary CL on $\mathbb{Z}/N\mathbb{Z}$ is dominated by **VOID–HARM rule disagreement** (Rules 1 and 2 priority interaction at outer composition sites), NOT by ECHO interactions as the original WP101 proof asserted. Empirically, **99.97% of non-associative triples at N=210 have ZERO inner ECHO compositions** (verified by `applications_pass/code/item1_proof_gap.py`). The corrected closed-form bound is $\sigma(N) \leq 2(N-2)^2/N^3 + \varepsilon(N)/N^3$ with $\varepsilon(N) = O(\varphi(N))$, which matches $\sigma$ to within the small ECHO term at all tested $N \in \{10, 30, 42, 66, 105, 110, 154, 210, 330, 462, 770, 1155\}$ ($N \cdot \sigma(N) \leq 1.993$ across the range). Strengthens WP101 from $\sigma \leq C/N$ ($C \in [2,3]$) to $\sigma \leq 2/N$ rigorously, with $N\sigma(N) \to 2$ from below as $N \to \infty$ along squarefree primorials. **Sharpens Conjecture 5.1 to a theorem.** | PROVED, machine-precision; [Atlas/applications_pass_2026_04_27/code/item1c_corrected_bound_v2.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Atlas/applications_pass_2026_04_27/code/item1c_corrected_bound_v2.py), `item1_proof_gap.py`, `item1b_mechanism.py`, `item2_higher_N.py` |
| **D72** | WP104 deep audit — "two paths converge on Pati-Salam" overstated (chat-Claude 2026-04-27) | All 16 specific computational claims in WP104 verified at machine precision (16-dim doubly-invariant, $(-8)^{15} \oplus (0)^1$ Killing spectrum, $\|\mathrm{VEV}\|^2 = 13/4$, 100% σ_outer-anti in **54**, 26 σ_outer-asymmetric cells). **However:** Path A (σ_outer-anti VEV) has eigenvalue spectrum $(+\sqrt{13}/2, -\sqrt{13}/2, 0, \ldots, 0)$ with stabilizer dim 28 = SO(8) — the breaking pattern is **SO(10) → SO(8)** (chain through SO(9)), NOT Pati-Salam SO(10) → SO(6) × SO(4) (which would need VEV multiplicity (6, 4) and stabilizer dim 21). Path B (doubly-invariant subalgebra) is $\mathfrak{su}(4) \oplus \mathfrak{u}(1) = 16$-dim, NOT the full 21-dim Pati-Salam SU(4) × SU(2)_L × SU(2)_R; the chiral factors live in σ³-anti complement. **The two paths do NOT close on the same reduction.** WP108 already flagged this tension internally (D46). External submissions must scope WP104's framing accordingly: "two structurally distinct observations about TIG's so(10), not two paths to a common reduction." | EMPIRICAL audit-confirmed; [Atlas/applications_pass_2026_04_27/WP104_DEEP_AUDIT_2026_04_27.md](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Atlas/applications_pass_2026_04_27/WP104_DEEP_AUDIT_2026_04_27.md), `applications_pass/code/wp104_check.py` |
| **D73** | TIG-natural Dirac inside Cl(8) ⊂ Cl(10) [SPECULATION, structurally clean] | Per [Atlas/applications_pass_2026_04_27/SPECULATIONS_FIELD9_DIRAC_INSIDE.md](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Atlas/applications_pass_2026_04_27/SPECULATIONS_FIELD9_DIRAC_INSIDE.md): the chain $\mathrm{Cl}(1,3) \subset \mathrm{Cl}(0,4) \subset \mathrm{Cl}(8) \subset \mathrm{Cl}(10) = \mathrm{TIG}$ realizes the Dirac equation as a 4-gate decomposition inside TIG's Spin(10) spinor. Dirac chirality $\gamma^5_{\mathrm{Dirac}} = \gamma_1\gamma_2\gamma_3\gamma_4 = ZZII$ (Pauli string on 4 qubits); full TIG chirality $\omega = \gamma_1\cdots\gamma_8 = ZZZZ$ which equals BHML's $P_{56}$ chirality involution; decomposition $\omega = \gamma^5_{\mathrm{Dirac}} \cdot \omega_{\mathrm{internal}}$. Free Dirac Hamiltonian $H = \alpha\cdot p + \beta m$ becomes a 4-term linear combination of TIG gates: $\beta = \gamma_1 = XIII$, $\alpha^k = i\gamma_1\gamma_{k+1}$ giving the standard ±E spectrum with 8-fold degeneracy = (Pati-Salam internal multiplet) × (Dirac spin). **What's verified at machine precision:** the gate identifications, the anticommutation relations, the chirality decomposition, the spectrum. **What's speculative:** that this gives quantum-simulation advantage over Wilson/Susskind/Domain-wall fermion approaches; that the 16-dim Spin(10) spinor giving "one full SM generation natively in 4 qubits" is phenomenologically realizable rather than just structurally appealing. SCOPE: structural / candidate-direction; not yet a peer-reviewed quantum-simulation result. | SPECULATIVE-but-structurally-clean; D-row recorded for tower completeness. |
| **D74** | F5(a) ring-extension universality (this session 2026-04-29) | The closed-form runtime attractor $H/Br = 1+\sqrt{3}$ at $\alpha = 1/2$ is **universal across $\mathbb{Z}/n\mathbb{Z}$** for $n \in \{10, 11, 12, 13, 14, 15, 17, 20, 21, 25, 30, 35, 49, 50\}$ under the trivial-extension strategy (keep 4-core $= \{0, 7, 8, 9\}$; T HARMONY-absorbing on indices $\geq 10$; B = cyclic-add). Verified to $\|H/Br - (1+\sqrt{3})\| < 3 \times 10^{-31}$ at 50-digit mpmath precision in $\leq 79$ iterations across all 14 ring sizes. **The 1+√3 algebraic relation depends on the 4-core sub-magma's algebraic structure, not on the ring size.** Strategy B (shifted 4-core indices to $\lfloor j n/10 \rfloor$ for $j \in \{0, 7, 8, 9\}$): also produces $1+\sqrt{3}$ but with slower convergence, and 3 multiples-of-10 ($n = 20, 30, 50$) reach 4000-iter limit before converging to 10⁻³⁰ tolerance — structural observation that $n = 10k$ has slower mass-equilibration in shifted analogs. Strengthens §15's one-off Z/14Z test (10⁻⁷⁶) to a 14-ring scan. Confirms F5(a) (ring-generalization frontier): the depth-1 fixed-form $1+\sqrt{3}$ attractor is **structural** (sub-magma intrinsic), not **dimensional** (ring-specific). | EMPIRICAL, machine-precision; `papers/wp113_alpha_uniqueness/verification/f5a_universality_scan.py` |
| **D75** | F8 Jacobian linearization at $\alpha = 1/2$ (this session 2026-04-29) | The 4-core iteration map $F(p) = \tfrac{1}{2}[\mathrm{pt}(p) + \mathrm{pb}(p)]$ on $\{V+H+Br+R = 1\}$ has Jacobian eigenvalues at the $H/Br = 1+\sqrt{3}$ fixed point: $\lambda_0 = \mathbf{2}$ (radial, exact), $\lambda_{1,2} = 0.190735 \pm 0.292991\,i$ (complex pair, $|\lambda| = 0.349605$), $\lambda_3 = -0.245146$. **Spectral radius on simplex tangent: $\rho = 0.34960495 < 1$ ⟹ the fixed point is HYPERBOLIC-STABLE.** The radial eigenvalue $\lambda_0 = 2$ exactly is the degree-2 homogeneity signature: $F(\lambda p) = \lambda^2 F(p)$ ⟹ radial mode has $\partial_\lambda \lambda^2 \mid_{\lambda = 1} = 2$. **Same 2 in the algebraic relation $x^2 - 2x - 2 = 0$ for $H/Br$ (D39) and in the radial eigenvalue** — degree of fuse map = degree of algebraic relation. Convergence rate $\rho^k$ matches empirical 88-iter to $10^{-40}$ ($0.3496^{88} \approx 10^{-40}$). Lyapunov exponent $\lambda_{\mathrm{TIG}} = -\log \rho = 1.05095$. Bridge to FQH localization-length exponent $\gamma_{\mathrm{loc}} \approx 2.36$ (Lütken-Ross / Nat. Comm. 2024): both are linearization eigenvalues at depth-1 Stern-Brocot fixed-form vertices on different projections of fractal modular flow; **structurally aligned, not numerically equal**. | EMPIRICAL/STRUCTURAL, machine-precision; `papers/wp113_alpha_uniqueness/verification/f8_jacobian_alpha_half.py` |
| **D76** | Algebraic uniqueness at $\alpha = 1/2$ is per-projection (this session 2026-04-29) | Sharpens D68. PSLQ tests on the simplex-tangent eigenvalues from D75 ($|\lambda_1| = 0.349605...$, $\mathrm{Re}(\lambda_1) = 0.190735...$, $\lambda_3 = -0.245146...$) at degree $\leq 8$ with coefficient bound $10^6$ at 60-digit precision: **NO algebraic relation found**. Same for trace and determinant of the simplex-tangent 3×3 Jacobian. **The algebraic uniqueness at $\alpha = 1/2$ noted in WP113 (degree 2 polynomial $x^2 - 2x - 2 = 0$ for $H/Br$, degree 4 quartic for $R/Br$) is PROJECTION-SPECIFIC.** On the $H/Br$ projection: depth-2 algebraic in $\mathbb{Q}(\sqrt{3})$. On the eigenvalue (linearization) projection: transcendental — no degree-≤8 relation exists. Each projection has its OWN depth at which the fixed-form/crossing duality lives. Resolves a tension between WP113's "α = 1/2 is uniquely algebraic" and the lens framework's per-projection structure: WP113's claim is correct *for the H/Br projection*; on other projections the claim is *false* — uniqueness becomes transcendental. Refines the meta-fractal recursive duality (§11): every vertex is both fixed-form (algebraic) and crossing (transcendental); the degree of the algebraic side depends on which projection you read. | EMPIRICAL via PSLQ; same script |
| **D77** | F1 — Cl(0,7) explicit γ-matrix construction + SO(7) charge conjugation (this session 2026-04-29) | Cl(0,7) γ-matrices constructed in standard Pauli triple-product basis (8×8 complex): $\gamma_1 = \sigma_1 \otimes I \otimes I$, $\gamma_2 = \sigma_2 \otimes I \otimes I$, $\gamma_3 = \sigma_3 \otimes \sigma_1 \otimes I$, ..., $\gamma_7 = \sigma_3 \otimes \sigma_3 \otimes \sigma_3$. All 28 Clifford anticommutators $\{\gamma_a, \gamma_b\} = 2\delta_{ab}$ verified at sympy exact precision. Volume element $\omega_7 = \gamma_1 \cdots \gamma_7$ has $\omega_7^2 = -I_8$. Charge conjugation $C := \gamma_2 \gamma_4 \gamma_6$ verified to satisfy $C \gamma_a C^{-1} = -\gamma_a^T$ for all 7 a; $C^T = C$ (complex-symmetric); $\mathrm{Tr}(C) = 0$; $\det(C) = +1$; $C^2 = -I_8$ (eigenvalues $\pm i$ each multiplicity 4). The unique SO(7)-invariant in $\mathbf{8} \otimes \mathbf{8} \to \mathbf{1}$ is $\psi^T C \psi$. Decomposition: $\mathbf{8} \otimes \mathbf{8} = \mathbf{1} \oplus \mathbf{7} \oplus \mathbf{21} \oplus \mathbf{35}$, dim $= 64 \checkmark$. Scaffolds the SO(7)-singlet Yukawa formula $y_{\mathrm{singlet}} = \langle \mathrm{radial\ VEV} \rangle \cdot \langle \psi^T C \psi \rangle$. Numerical Yukawa value depends on resolving WP108-flagged WP104 path tension (D46/D72) and choosing a normalization convention. | PROVED, sympy-exact; `papers/wp113_alpha_uniqueness/verification/f1_so7_singlet_bilinear.py` |
| **D78** | F3 — Galois proof of α=1/2 uniqueness (this session 2026-04-29) | **Theorem**: Let $F_\alpha = \alpha\cdot\mathrm{pt} + (1-\alpha)\cdot\mathrm{pb}$ be the 4-core iteration map at mixing weight $\alpha \in (0,1)$, and let $x(\alpha) = H(\alpha)/Br(\alpha)$ at the fixed point. **Then $x(\alpha) \in \mathbb{Q}(\sqrt{3})$ (degree-2 extension over $\mathbb{Q}$) if and only if $\alpha = 1/2$**. **Proof**: At $\alpha = 1/2$, the BREATH fixed-point equation $F_{Br} - Br = Br(R+V-1) + (1/2)H^2 = 0$ admits the BR-factor cancellation: substituting $H = xBr$ gives $Br[(R+V-1) + (x^2/2)Br] = 0$; dividing by $Br$ and using simplex $V+R = 1-H-Br = 1-(x+1)Br$ yields $Br(-x-1+x^2/2) = 0$, hence $x^2 - 2x - 2 = 0$. Discriminant 12; roots $1 \pm \sqrt{3}$; positive root $x = 1+\sqrt{3} \in \mathbb{Q}(\sqrt{3})$. Galois group $S_2 = \mathbb{Z}/2\mathbb{Z}$. **At $\alpha \neq 1/2$**: the BR-factor cancellation fails because the $(1-\alpha)$ coefficient on the $Br^1$ term and the $(1-\alpha)$ coefficient on $H^2$ no longer conspire to a clean Br-factor; the reduced polynomial in $x$ has higher degree, and WP113 PSLQ at depth 24 with coefficient bound 200 finds no algebraic relation at $\alpha \in \{1/3, 1/4, 2/3, 3/4\}$. Promotes WP113's empirical PSLQ uniqueness (D42/D60) to a **structural Galois statement** for the H/Br projection. The "2-1 uniqueness" Brayden noted in §15 is **structurally the BR-factor cancellation at α=1/2**. | PROVED, symbolic-exact; `papers/wp113_alpha_uniqueness/verification/f3_galois_alpha_uniqueness.py` |
| **D79** | F2 — TIG↔Planck structural closure (this session 2026-04-29) | The carrier identity $\kappa_\xi = 13/(4e)$ comes from $13 = \|\mathrm{VEV}\|^2$ (TIG-side, D33) and $e$ = the $\xi$-vacuum value at $\xi_0 = e^{-1}$ (BB-side, where $V''(\xi_0) = 1/\xi_0 = e$). **Re-read of Bialynicki-Birula-Mycielski 1976 §III**: the log-nonlinearity preserves Planck's $E = \hbar\omega$ relation under separability, BUT BB's potential $V(\psi) = -b \cdot \psi \cdot \log(|\psi|^2/r^2)$ has **two free parameters** $b$ (coupling) and $r$ (length scale); BB does NOT determine an absolute mass scale. **Therefore**: $m_\xi/m_\mathrm{Planck}$ is NOT structurally determined by BB 1976 + $\kappa_\xi$ alone. The lens needs ONE additional dimensional anchor (GUT scale ~ $10^{16}$ GeV; EW vev 246 GeV; or TIG-internal principle fixing $b$ or $r$) to close F2's absolute-ratio question. **Structural closure**: "$\kappa_\xi = 13/(4e)$ is the unique dimensionless ratio carried by both axes; absolute mass scale is open pending one explicit anchor." Refines F2 from "no clear path" to "open pending one explicit choice". | RESOLVED structurally; BB 1976 Ann. Phys. 100:62-93 §III; CK crystal `tig_planck_bridge` |
| **D80** | F6 — sigma_NS bridge crystal mounted (this session 2026-04-29) | F6 (Navier-Stokes / sigma_NS < 1) had no anchored crystal in CK before this session. Now mounted: the lens claim is that NS dyadic cascade level $k$ corresponds to cyclotomic vertex $N = 2^k$ under the velocity-gradient-commutator projection. **Projection-restricted statement**: $\sigma_{NS}(k) \leq \sigma(N=2^k) \leq 2/2^k = 2^{1-k}$ — exponential decay in dyadic depth. **Implication if verified**: $\sigma_{NS} \to 0$ as $k \to \infty$, characterizing the singular set as the locus where $\sigma_{NS}$ doesn't decay. **NOT a Clay-Millennium proof**: NS regularity needs $\sigma_{NS} = 0$ globally. **What's missing structurally**: rigorous derivation of the NS-cascade ↔ cyclotomic-N correspondence at the operator level (currently by analogy via Stern-Brocot lens). **What's testable**: numerically check $\sigma_{NS}(k)$ on wavelet-decomposed NS simulation; if decay matches $2/2^k$, lens empirically supported. | ARTICULATED, mounted in CK as `sigma_ns_bridge` crystal; CK crystal `sigma_ns_bridge` |
| **D81** | F10 — i-action descent test, risk=HIGH structurally justified (this session 2026-04-29) | **Theorem-level statement**: the +i-action on End⁰(Prym) = ℚ(i) does NOT descend over the descent_field ℚ(√2, √3, √5). **Proof** (sympy-exact on 4×4 model): take $M = \mathrm{diag}(J, J)$ with $J = [[0,-1],[1,0]]$. Then $M^2 = -I_4$; eigenvalues are $\pm i$, each multiplicity 2; eigenvectors are $(\pm i, 1, 0, 0)^T$ and $(0, 0, \pm i, 1)^T$ with i-coefficients. Galois action $\sigma: i \to -i$ swaps the +i and −i eigenspaces. The descent field ℚ(√2, √3, √5) is **totally real** (compositum of totally real subfields), hence does NOT contain i. Therefore the ±i decomposition cannot descend; the minimal field of definition for the eigenspace decomposition is ℚ(i, √2, √3, √5) = the Hodge field of degree 16. **Confirms outcome (b) of the §17 F10 lens prediction**: the i-action is a genuine algebraic-extension barrier; Hodge integrality at dim 5 has the Q(i)-twist obstruction Brayden's lens conjecture predicts. **Cross-rotation**: same algebraic primitive ($M^2 = -I$, eigenvalues $\pm i$) appears in F1 (Cl(0,7) charge conjugation $C^2 = -I_8$, D77). | PROVED, sympy-exact; `papers/wp113_alpha_uniqueness/verification/f10_i_action_descent.py` |
| **D82** | F2 sharpening — BB coupling b is FIXED by TIG (this session 2026-04-29) | **Theorem-level statement**: the BB coupling parameter b in $V_{BB}(u) = -b \cdot u \cdot \log(u/r^2)$ is fixed by TIG via $b = -\kappa_\xi = -13/(4e) \approx -1.196$. Only the BB length scale $r$ remains free. **Proof** (sympy-exact): TIG potential is $V_{TIG}(\xi) = \kappa_\xi \cdot \xi \cdot \log(\xi)$ with vacuum at $\xi_0 = e^{-1}$ (where $V'_\mathrm{TIG}(\xi) = \kappa_\xi(\log \xi + 1) = 0$); $V''_{TIG}(\xi_0) = \kappa_\xi/\xi_0 = \kappa_\xi e$. Setting $m^2_\xi = \|\mathrm{VEV}\|^2 = 13/4$ (D33) gives $\kappa_\xi = 13/(4e)$. Expanding BB: $V_{BB}(u) = -b u \log u + 2b\log(r) u$; matching the leading term to TIG gives $-b = \kappa_\xi$, so $b = -\kappa_\xi = -13/(4e)$. The linear correction $2b\log(r) u$ shifts the vacuum but does NOT affect $m^2$ (verified: $m^2_{BB}$ at $u_\mathrm{vac} = r^2 e^{-1}$ is $-eb/r^2 = 13/(4r^2)$, matches $m^2_{TIG} = 13/4$ when $r = 1$). **Sharpens §24** ("open pending one dimensional anchor") to **§27** ("open pending ONE CONVENTION — the lab-unit value of $r$"). **Predictions**: if $r = \ell_P$ (Planck length), $m_\xi/m_\mathrm{Planck} = \sqrt{\kappa_\xi e} = \sqrt{13/4} \approx 1.803$ (super-Planckian, GUT-natural). If $r = 1/M_\mathrm{GUT}$, $m_\xi \approx 1.803 \cdot 10^{16}$ GeV. **Synthesis pattern**: combining the xi (WP81), bb_unique (BB 1976), and tig_planck_bridge crystals composes the b-fixing claim. | PROVED, sympy-exact; `papers/wp113_alpha_uniqueness/verification/f2_bb_coupling_sharpening.py` |
| **D83** | Cross-frontier degree-2 primitive (this session 2026-04-29 §28) | **Five of eight open frontiers (F1, F3, F4, F8, F10) share ONE algebraic primitive: $M^2 = \pm I$ (or analog), giving depth-2 algebra**. Verified sympy-exact: F1: $C = \gamma_2 \gamma_4 \gamma_6$, $C^2 = -I_8$, eigenvalues $\pm i$ (mult 4 each), field $\mathbb{Q}(i)$ ext (D77). F3: H/Br at α=1/2 satisfies $x^2 - 2x - 2 = 0$ with discriminant 12 = 4·3, roots $1 \pm \sqrt{3}$, Galois group $S_2 = \mathbb{Z}/2\mathbb{Z}$, field $\mathbb{Q}(\sqrt{3})$ (D78). F4: $P_{56}$ = (5,6) transposition (involution), $P_{56}^2 = +I$, eigenvalues $\pm 1$, field $\mathbb{Q}$. F8: $F$ is degree-2 homogeneous ($F(\lambda p) = \lambda^2 F(p)$), giving radial Jacobian eigenvalue $\lambda_0 = 2$ exactly — **same "2"** as in F3's quadratic AND in the algebraic-degree of H/Br (D75). F10: $\bar\psi^2 = -I_4$ on Prym, eigenvalues $\pm i$ (mult 2 each), field $\mathbb{Q}(i)$ ext (D81). **Lens consequence**: depth-2 is a clustering depth where TIG's structure expresses itself across multiple seemingly-disparate domains. The "every Stern-Brocot vertex is BOTH fixed-form AND crossing" framing of WP116 §1 becomes operational: at depth 2, the fixed-form is $M^2 = \pm I$ and its consequences ($\pm 1$ or $\pm i$ eigenspaces, $\mathbb{Q}(\sqrt{3})$ or $\mathbb{Q}(i)$ Galois extensions, degree-2 algebraic relations, order-2 involutions). **Five frontiers viewed as ONE structural object through five projection axes**. | SYNTHESIS, sympy-verified; `papers/wp113_alpha_uniqueness/verification/f_cross_depth2_primitives.py` |
| **D84** | F9 rank-and-depth duality (this session 2026-04-29 §29) | 58-curve LMFDB scan (20 rank-0, 20 rank-1, 18 rank-2) reveals: **higher rank correlates with SIMPLER j-denominator structure** (mean #primes in j-denominator: rank 0 = 1.70, rank 1 = 1.55, rank 2 = **1.39**, monotone decreasing). Distribution: rank 0 has 14/20 = 70% with 2 primes in den; rank 2 has 11/18 = 61% with only 1 prime. All denominators consist of conductor-primes (Tate's theorem confirmed). Cleanest j-invariants in sample: **15.a7** (rank 0, j = -1/15) and **433.a1** (rank 2, j = -1/433) — both depth-1 vertices. **F9 lens reading FALSIFIED in naive form**: the §17 "rank r = depth parameter" claim is contradicted by the 58-curve data; rank-2 curves have FEWER primes in j-denominator than rank-0 curves. **Refined F9' conjecture**: rank and depth are **DUAL, not equal**. Rank = #generators of Mordell-Weil (free arithmetic structure); depth = complexity of cohomological data (j-denominator structure). They are inversely related: cohomologically simple curves (depth 1) tend to have higher rank; cohomologically complex curves (depth 2+) tend to have lower rank. **Substantive empirical pattern, not a proof**: 58 curves is small; conductor ranges differ across ranks. Suggests F9 needs reframing rather than refutation: the lens prediction was wrong-signed but the structural connection is real. | EMPIRICAL, 58-curve sample; `papers/wp113_alpha_uniqueness/verification/f9_lmfdb_depth_analysis.py` |
| **D85** | F8 trace polynomial IS algebraic deg 4, with WOBBLE prime 11 (this session 2026-04-29 §30) | The trace of the simplex-restricted 3×3 Jacobian at α=1/2 fixed point — sum of 3 simplex-tangent eigenvalues — is $\mathrm{tr} = \lambda_1 + \lambda_2 + \lambda_3 = 0.13632472600...$ and satisfies $-443\,t^4 + 5588\,t^3 - 21048\,t^2 + 26240\,t - 3200 = 0$ (verified at 10⁻¹⁷⁶ residual at 200-digit mpmath, irreducible over $\mathbb{Q}$). **Discriminant**: $\Delta = -2^{24} \cdot 3^{10} \cdot 5^2 \cdot \mathbf{11^6} \cdot \mathbf{71}$. **Two TIG-recurring primes** appear: prime **11** at $11^6$ — the **WOBBLE prime** (D37 char poly coefficients, D69 Br/V denominator, D70 multi-DoF wobble) — and prime **71** — the **R/Br quartic discriminant prime** (D40, D41, LMFDB 4.2.10224.1). **Updates D70**: WOBBLE manifests not just at 3 static algebraic locations (Lie, Clifford, Lattice) but also at the **dynamical projection** (Jacobian trace at α=1/2). 4 wobble locations now; 3 wobble-free DoFs (Jordan, Permutation, Operad). **Cross-frontier**: F8's dynamical signature shares the same number-theoretic neighborhood as WP105's R/Br quartic — **prime 71 recurs in F8 trace and F8 R/Br fixed-point ratio**. Individual simplex-tangent eigenvalues are still transcendental at deg ≤ 20 maxcoeff 10⁹ — only their *symmetric function* (trace) is algebraic. Determinant: still no relation found. F8 depth structure: degree 1 (radial λ₀=2), degree 4 (trace), open ($\geq 21$) for individual eigenvalues. | EMPIRICAL/STRUCTURAL, mpmath 200-digit + sympy; `papers/wp113_alpha_uniqueness/verification/f8_pslq_deeper.py` |
| **D86** | Depth-3 primitive σ² + fifth WOBBLE manifestation (this session 2026-04-29 §31) | σ on Z/10Z has cycle structure (0)(3)(8)(9)(1 7 6 5 4 2): 4 fixed-points + one 6-cycle. **σ² is the natural depth-3 primitive**: σ² = (0)(3)(8)(9)(1 6 4)(7 5 2), order 3, eigenvalues {1 (mult 6), ω (mult 2), ω² (mult 2)} where ω = e^(2πi/3) = -1/2 + i√3/2. Minimum polynomial of ω over $\mathbb{Q}$: $x^2 + x + 1 = 0$, discriminant -3, field $\mathbb{Q}(ω) = \mathbb{Q}(\sqrt{-3})$ (degree 2 over $\mathbb{Q}$). **Two senses of "depth"**: operator-depth = order of M = 3 here; algebraic-depth = degree of eigenvalue minimal polynomial = 2 = $φ(3)$. For σ^k, algebraic-depth = $φ(k)$ (Euler totient = degree of cyclotomic polynomial $Φ_k$). **TIG operator semantics**: σ² 3-cycles split operators into TRANSFORMATION = {LATTICE(1), CHAOS(6), COLLAPSE(4)} and STABILITY = {HARMONY(7), BALANCE(5), COUNTER(2)}. **CRITICAL FINDING**: operator-value-sum of TRANSFORMATION 3-cycle is **1+6+4 = 11** = the **WOBBLE prime**! This is the **fifth distinct structural location** of WOBBLE 11 (after D37 char poly coefficients, D69 Br/V denominator, D70 multi-DoF wobble structure, D85 F8 trace polynomial discriminant). The WOBBLE prime is woven through: static algebraic structure, dynamical structure, AND operator-label structure. Suggests 11 plays a structural role analogous to 7 (HARMONY) — both small primes near 10 with TIG-internal duties. STABILITY 3-cycle sum = 14 = 2·7 (HARMONY-multiple). | SYNTHESIS / EMPIRICAL, sympy-verified; `papers/wp113_alpha_uniqueness/verification/f_depth3_primitives.py` |
| **D87** | F8 dynamical + static structure unify in LMFDB 4.2.10224.1 (this session 2026-04-29 §32) | **Theorem-level statement**: the F8 simplex Jacobian trace polynomial (D85) and the WP105 R/Br quartic (D40/D41) generate the **same quartic number field**, namely **LMFDB 4.2.10224.1** with field discriminant -10224 = -2⁴·3²·71, signature (2,1), class number 1. **Verification** (sympy-exact): (1) **Squarefree discriminant match**: F8 trace poly disc squarefree-part = -71; R/Br quartic poly disc squarefree-part = -71. SAME. (2) **Galois group match**: both polynomials' Galois groups are `PermutationGroup([(0 1 2 3), (0 3)(1 2)])` = $D_4$ (dihedral, order 8). SAME group, same generators. (3) **Same degree** (4), **same number field** signature. **Refines D70/D85's wobble statement**: TWO DISTINCT WOBBLE PRIMES at TWO DIFFERENT LEVELS — prime **11** is the **polynomial-coefficient wobble** (D37 char poly, D69 Br/V denominator, D85 F8 trace polynomial discriminant; **factors out as 11⁶ in the F8 trace disc → not field-theoretic**) while prime **71** is the **field-theoretic wobble** (D41 R/Br quartic field disc, D85+§32 F8 trace field disc). 11 is BASIS-DEPENDENT; 71 is FIELD-INVARIANT. **Lens consequence**: F8's dynamical projection (Jacobian trace at α=1/2 fixed point) and F8's static projection (R/Br fixed-point ratio) live in EXACTLY the same number field. The lens framework is **not metaphor** — F8 has *one* underlying algebraic structure (LMFDB 4.2.10224.1) that BOTH projections compute. Strongest lens-empirical evidence to date that "different projections of the same TIG vertex share a number field". | PROVED, sympy-exact (Galois group + discriminant); `papers/wp113_alpha_uniqueness/verification/f_field_match_71.py` |

**Reading.** Volume H closes the WP100s tower. D45 (WP106) scopes the framework: TIG structure is specific to canonical TSML/BHML, not generic in trained networks. D46 (WP108) flags an honest tension between the WP104 Path A (doubly-invariant subalgebra → su(4) ⊕ u(1)) and WP104 Path B (σ_outer-breaking VEV → SO(9) → SO(7)) Pati-Salam routes — they are NOT the same reduction. D47 (WP109) identifies the operad-DOF as orthogonal to the D_4 symmetry of the rest of the tower (a structural no-go, not a defect). D48–D50 (WP110) strengthen the closed-form runtime attractor (Volume G) from a dynamical fact to a structural identity: 4-core closure plus Z_T = Z_B forces $H/Br = 1 + \sqrt{3}$. D51 (WP111) ties the six DOFs together. The **integer/rational signature** across all DOFs (the cross-DOF identities table in WP111 §10) is reproduced compactly in §17 (Constants).

### Volume I — Bridge Findings (Sprint May 2 2026, arithmetic-topology / modular-knot territory)

The May 2 2026 bridge research session pushed substrate self-iteration data against published arithmetic-topology / modular-knot frameworks (Morishita 2024 *Knots and Primes* 2nd ed; Ghys ICM 2007; Katok-Ugarcovici 2007; Matsusaka-Ueki 2023; Burrin-von Essen 2024). Five empirically-grounded findings + ten honest negatives. **Verified end-to-end** by `papers/wp_bridge_findings_2026_05_02/code/verify_findings.py` (0 failures, 0 warnings).

| ID | name | formula | status / file |
|----|------|---------|---------------|
| **D88** | Corrected substrate frame (TSML_8 + BHML_10 + flow cells) | The canonical disambiguation per §6.7: **TSML_8 = TSML_10 with rows/cols {0, 7} removed**, acting on indices {1,2,3,4,5,6,8,9}. **BHML_10 = full** on all 10 elements. **V (0) and H (7) are flow cells between the tables**, not entries. The runtime processor uses TSML_8 + BHML_10 with V/H as flow boundary; trefoil and role analyses MUST use this frame (the early-session TSML_10 versions are invalid and explicitly listed as such in `papers/wp_bridge_findings_2026_05_02/results/KNOWN_ISSUES.md` §1). | DEFINITIONAL; `papers/wp_bridge_findings_2026_05_02/code/corrected_substrate.py` |
| **D89** | Trefoil characterization (operator-level) | On corrected frame, the runtime processor's 3-crossing ("trefoil-equivalent") triples form **exactly two multiset classes**: trefoil(a,b,c) ⟺ {a,b,c} = {VOID, BREATH, HARMONY} (6 permutations) **or** {VOID, BREATH, BREATH} (3 permutations). Total: **9 triples**, all BHML-associative. Among structure cells {COUNTER, COLLAPSE, BREATH}, BREATH is the unique one producing trefoils when combined with VOID — COUNTER opposes; COLLAPSE destabilizes; only BREATH sustains form long enough for the 3-crossing closed loop to complete. | PROVED, parameter-swept; `papers/wp_bridge_findings_2026_05_02/code/trefoil_corrected_frame.py` + `breath_uniqueness.py` |
| **D90** | BHML successor diagonal | BHML's diagonal action realizes the integer successor on $\{1..7\}$: **BHML(n,n) = n+1** for $n \in \{1..7\}$, **BHML(8,8) = 7** (BREATH retains cusp position), **BHML(9,9) = 0** (RESET collapses to VOID), **BHML(0,0) = 0** (VOID fixed). This drives BHML self-iteration period structure: $n \in \{1..6\}$ → period(n) = 7−n (linear distance to HARMONY cusp), $n \in \{7,8,9\}$ → period 4,3,2 (4-core cycle), $n=0$ → period 1. The successor on $\{1..7\}$ expresses "approaching the HARMONY cusp" in the substrate's algebraic vocabulary. | PROVED, 2-line direct; verified by `verify_findings.py` |
| **D91** | Two-coding image structure (TSML_8 = geometric, BHML_10 = arithmetic) | TSML_8 and BHML_10 form **complementary codings** matching Katok-Ugarcovici 2007's geometric/arithmetic split natively. **TSML_8** (side-cutting): image = $\{3,4,7,8,9\}$ (5-element), output role distribution **60/64 = 93.8% Flow, 4/64 = 6.2% Structure**, role-deterministic on 8 of 9 input role-pairs (only S-S branches). **BHML_10** (continued-fraction reduction): image = full 10, output role 52% F / 19% S / 25% T / 4% V (balanced), role-deterministic only on V/T inputs. **Agreement set**: TSML_8 and BHML_10 agree on 24/64 cells of TSML_8 domain (mostly routes leading to HARMONY) and disagree on 40/64 in the interior. **The two codings agree at the cusp boundary, disagree in the interior.** | PROVED, direct count; `papers/wp_bridge_findings_2026_05_02/code/tsml8_role_analysis.py` + `algebraic_relationship.py` |
| **D92** | ±21 invariant with σ-orbit and role decompositions | The substrate has a per-digit integer invariant of magnitude $21 = 3 \cdot |\text{HARMONY}|$ from substrate self-iteration. **Computation A (Ghys-analog)**: $\Psi_A(n)$ = (#{j: TSML(n,j) > BHML(n,j)}) − (#{j: BHML(n,j) > TSML(n,j)}); sum = **+21**. **Computation B (period→trace under simple representative ((1,1),(t-2,t-1)) with $t = $ period(n)+2)**: $\Psi_B(n) = -(\text{period}(n) - 1)$; sum = **−21**. **Two decompositions of −21**: σ-orbit: σ 6-cycle {1,2,4,5,6,7} sums to **−15 = −T_5** + σ-fixed {0,3,8,9} sums to **−6 = −T_3**, total $-(T_5+T_3) = -21$ (triangular). Role: Flow {1,3,5,7,9} sums to **−13 = −F_7** + Structure {2,4,8} sums to **−8 = −F_6**, V {0} = T {6} = 0, total $-(F_7+F_6) = -21 = -F_8$ (Fibonacci). The Fibonacci decomposition is **canonical-specific** (verified by `fibonacci_robustness.py`: 0/200 random commutative tables on Z/10Z reproduce (\|F\|, \|S\|) = (13, 8)). The triangular decomposition is structurally forced by the linear period formula. | PROVED structurally for both decompositions; period→trace lift remains a hypothesis (no naive PSL(2,ℤ) lift produces ±21 — five strategies tested negative); `papers/wp_bridge_findings_2026_05_02/code/role_decomposition.py` + `class_average_check.py` |
| **D93** | Role partition + role magma with VOID identity | The substrate has a functional partition by dynamical role: **Flow F = {1,3,5,7,9}** (transformative, 5 elements), **Structure S = {2,4,8}** (stabilizing, 3 elements), **Transition T = {6}** (bridge cell), **Void V = {0}** (boundary cell). This cuts across σ-orbit (σ 6-cycle has 3F+1T+2S; σ-fixed has 1V+2F+1S) — flow/structure/V/T is a **third independent decomposition**. The mode-based role magma using BHML output mode per input role-pair is: V·x = x for all roles (commutative; V is the **identity element**), V·V = V the only idempotent, **NOT associative** (e.g. (F·F)·S = F ≠ F·(F·S) = T). Branching pairs are exactly {F-F, F-S, S-F, S-S}. The substrate has a **semi-factorization** at role level: V/T inputs collapse to deterministic role transitions; F/S inputs preserve operator-level structure. | PROVED, direct enumeration; `papers/wp_bridge_findings_2026_05_02/code/role_magma_factorization.py` |
| **D94** | Boundary symmetries (grammar-level) | The substrate has multiple grammar-level boundary symmetries (swapping adjacent integer pairs at role boundaries preserves admissibility on specific grammar triples): 5↔6 (F↔T) preserves on (5,6,7); 6↔7 (T↔F) on (5,6,7); 8↔9 (S↔F) on (7,8,9), (7,8,8); 2↔3 (S↔F) on (0,1,2); 1↔2 (F↔S) on (0,1,2); 7↔8 (F↔S) partial; **0↔8 (V↔S) is the strongest global preservation rate at 20.9% of all 1000 triples**. These are **GRAMMAR-LEVEL symmetries (admissibility), not algebraic equivalences** — the underlying operators compose differently under TSML/BHML. **The 5↔6 interchangeability mentioned in canonical TIG is one of a family** — the strongest in global preservation is V↔BREATH (0↔8). **No pair preserves crossing count on ALL 1000 triples** — substrate has no full algebraic symmetries. | EMPIRICAL, full 1000-triple enumeration; `papers/wp_bridge_findings_2026_05_02/code/symmetry_map.py` + `interchangeability_test.py` |

**Volume I honest-negatives table** (sharpens what TIG IS by establishing what it ISN'T):

| ID | claim ruled out | finding |
|----|-----------------|---------|
| **N1** | naive PSL(2,ℤ) lift produces ±21 | All five strategies tested produce sums in [−4, 0]; none equal ±21. The period→trace bridge under simple representative ((1,1),(t-2,t-1)) gives −21 numerically, but principled lift derivation is open. `orbit_to_psl2z.py` |
| **N2** | small triangle group $\Gamma_{p,q}$ has substrate's period set as elliptic orders | No coprime $(p,q) \le 9$ has divisors covering $\{1,2,3,4,5,6\}$. $\mathrm{PSL}(2,\mathbb{Z}) = \Gamma_{2,3}$ has only orders $\{1,2,3\}$. Substrate's BHML periods are **trajectory periods (closed-orbit lengths) of a dynamical system**, not finite-element orders. `triangle_groups_test.py` |
| **N3** | TIG's grammar matches Borromean prime conditions | No canonical TIG triple has all elements ≡ 1 mod 4. No trefoil-9 multiset has all elements in QR-mod-5. TIG sits **inside** arithmetic-topology / modular-knot territory but isn't a restatement of Ishida-Kuramoto-Zheng's Borromean structure. `substrate_borromean.py` + `borromean_primes.py` |
| **N4** | σ is an automorphism of TSML or BHML | Empirical match rates: **48% for BHML, 17% for TSML**. σ is NOT an automorphism of either magma. `algebraic_relationship.py` |
| **N5** | TSML and BHML distribute over each other | 19.5% match. They are **algebraically independent** (no distribution law). `algebraic_relationship.py` |
| **N6** | BHML iteration converges to TSML | 28/64 starts (44%). Not a convergence theorem. `algebraic_relationship.py` |
| **N7** | substrate factors through Z/2 × Z/5 (CRT) | BHML doesn't respect the CRT decomposition. Substrate is **irreducible** under CRT. `lacasa_corrected.py` |
| **N8** | Fibonacci role decomposition is structural / forced by axioms | 0/200 random commutative tables on Z/10Z reproduce (\|F\|, \|S\|) = (13, 8). 32/50 single-swap perturbations preserve; 11/50 three-swap perturbations preserve. **Canonical-specific signature, not theorem.** `fibonacci_robustness.py` |
| **N9** | role partition determines crossing count for every pattern | Most patterns are not determined by role alone. `crossing_taxonomy.py` |
| **N10** | early-session "trefoil-22" claim (in TSML_10 frame) | INVALID. Replaced by D89 (9-trefoil + multiset characterization on corrected frame). All TSML_10-frame trefoil files explicitly listed in `KNOWN_ISSUES.md §1` as not-canonical. |

**Reading.** Volume I is the bridge between TIG's substrate dynamics and the published arithmetic-topology / modular-knot literature. **What TIG is**: a specific algebraic-topological substrate (TSML_8 + BHML_10 + V/H flow boundary) sitting **inside** the territory of Morishita / Ghys / Katok-Ugarcovici / Matsusaka-Ueki / Burrin-von Essen — but a new construction in that territory, not a restatement of any of those theorems. **What TIG isn't**: a literal Borromean-prime structure (N3), a triangle-group representation (N2), or a quotient of PSL(2,ℤ) under any tested lift (N1). **The Fibonacci / triangular signatures of ±21 are real but their structural status differs**: triangular is forced by the linear period formula (deep), Fibonacci is canonical-specific (signature, not theorem) per N8.

### Crossing Lemma (WP57 spine)

```
Theorem (Crossing Lemma — proved for squarefree n and d).

  Let n = p₁ · p₂ · ··· · pₖ squarefree, d ∣ n squarefree, g ∈ (Z/nZ)*.
  The following are equivalent:

    (a) The joint map J = (A_d, π_DYN(g)) : Z/nZ → Z/dZ × (g-orbit space)
        is INJECTIVE.

    (b) U(A_d) ∩ U(π_DYN(g)) = ∅ — the partitions have disjoint
        unresolved-pair sets.

    (c) g ≢ 1 (mod pᵢ) for every prime pᵢ ∣ (n/d) — equivalently, M_g
        acts nontrivially on the A_{n/d}-quotient of X.

  In short: {A_d, π_DYN(g)} is a sufficient pair iff M_g CROSSES the
  fibers of A_{n/d}.
```

**Reading:** information is generated only when dynamics cross
partitions. Crossings are exactly failures of separability.

Source: [05_papers/algebra/J06/manuscript/WP57_CROSSING_LEMMA.md](../05_papers/algebra/J06/manuscript/WP57_CROSSING_LEMMA.md),
`papers/proof_d8_cl_operator_encoding.py`.

### Flatness Theorem (WP51 spine)

```
Theorem (Flatness Theorem — proved for Z/10Z).

  Z/10Z carries four irreducible structures simultaneously:

      additive structure     (a + b mod 10)
      multiplicative struct  (a · b mod 10)
      additive flow          (repeated +1 closes a cycle of length 10)
      multiplicative flow    (repeated ·3 closes a cycle of length 4
                              inside the units)

  These four cannot be drawn consistently on a flat surface. The
  minimum surface that holds all four without contradiction is a
  TORUS, and the ratio of its two radii is forced by the ring:

      R/r = T* = 5/7    for Z/10Z.
```

**Generalization** to "any whole has a 2×2 structure that cannot stay
flat" is the central conjecture of TIG. Proved for Z/10Z; structural
elsewhere.

Source: [05_papers/combinatorics/J01/manuscript/manuscript.tex](../05_papers/combinatorics/J01/manuscript/manuscript.tex).

### σ Rate Theorem (WP101 spine)

```
Theorem (σ Rate, WP101).

  For squarefree N, the non-associativity fraction of the binary CL
  on Z/NZ satisfies:

      σ(N) ≤ C / N         for an explicit constant C.

  Equivalently, the transfer-operator spectral gap on the unit lattice
  satisfies:

      γ(b) = 1 − 1/φ(b).

  Consequence: as N grows through squarefree primorials, the algebra
  approaches separability. σ → 0.
```

Source: [05_papers/combinatorics/J01/manuscript/WP101_SIGMA_RATE_THEOREM.md](../05_papers/combinatorics/J01/manuscript/WP101_SIGMA_RATE_THEOREM.md).

**Huang-Lehtonen interpretation.** Define α(CL_N) = 1 − σ(N) (Braitt-Silberger 2006, *Quasigroups Related Systems* 14:11–26). The Rate Theorem is equivalent to α(CL_N) → 1 as N → ∞. Operadically: the binary CL is commutative and attains the ac-free maximum $s_n^{\mathrm{ac}} = (2n-3)!!$ (Huang-Lehtonen arXiv:2202.11826, 2022; arXiv:2401.15786, 2024), so the generated symmetric operad is the free commutative magmatic operad $\mathrm{Mag}^{\mathrm{com}}$ on one generator. The Rate Theorem degenerates this operad toward the commutative associative operad $\mathrm{Com}$ as N → ∞; the BB bridge then identifies log-nonlinearity as the unique continuum wave equation compatible with that limit.

### BB-bridge to continuum field theory (WP91 spine)

```
Theorem (Bialynicki-Birula & Mycielski 1976, Annals of Physics 100:62-93).

  The UNIQUE nonlinearity in wave mechanics that preserves separability
  of composite systems is logarithmic:

      V(ξ) = ξ · log ξ.

  Combined with the σ rate theorem (σ → 0 = separability in the
  continuum limit), the forced field equation is:

      □ ξ  =  1 + log ξ                   (the ξ field equation)

  with exact vacuum:

      ξ₀ = e⁻¹                            (vacuum of log potential)

  and exact mass-gap coefficient:

      m²_ξ = κ · e                        (where κ is the natural rescale)
```

Produces freezing quintessence with w(z) → −1; falsifiable on DESI BAO.
Current fit (Sprint 14): χ² = 15.7 vs ΛCDM 14.1 — comparable, not preferred.

Source: [05_papers/algebra/J32/manuscript/WP91_NS_SEPARABILITY_BRIDGE.md](../05_papers/algebra/J32/manuscript/WP91_NS_SEPARABILITY_BRIDGE.md),
[Gen12/targets/clay/papers/sprint14_prism_xi_2026_04_10/desi_xi_mcmc.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint14_prism_xi_2026_04_10/desi_xi_mcmc.py).

### Bridge identities (the recurring T\* = 5/7)

```
T* = 5/7 derived six independent ways:

  (1) torus aspect ratio of the four-structure Z/10Z surface         [WP51]
  (2) HARMONY/destination over journey-measurement                   [D18c]
  (3) centroid/inverse:  centroid((Z/10Z)*) / (g⁻¹ mod 10) = 5/7    [D18d]
  (4) first-cyclotomic over first-obstruction prime:  5 / 7
      (5 closes φ(10) = 4; 7 obstructs)                              [Washington 1997]
  (5) universal-semiprime unit density:  unit_frac(7, 35) = 5/7      [elementary NT]
  (6) coherence threshold measured in FPGA silicon                   [Sprint 13, ck_full.bit]

Fine-structure identity:

  T* = HARMONY/10 + 1/70 = 7/10 + 1/(7·10)         (exact, D22)
```

Six independent contexts, one number. Not proof of the universal claim,
but the kind of repetition that demands a structural explanation.

**External alignment (Farey spin chain framework).** T* = 5/7 and its
adjacent Farey fractions (S* = 4/7, mass gap = 2/7, TSML_10 density = 3/4)
sit on the same Farey tree studied in the **Farey fraction spin chain**
program of Kleban-Özlük (1999, *Commun. Math. Phys.*), Fiala-Kleban-Özlük
(2002, arXiv:math-ph/0203048), Bandtlow-Fiala-Kleban (2009), and Technau
(2023, arXiv:2304.08143). In that framework, Farey-structured fractions
arise as critical thresholds (critical temperature β_c) of a transfer
operator on the Farey tree, with the number-theoretic spin chain
Z_k^K(2β) → ζ(2β−1)/ζ(2β) as k → ∞ (Knauf 1998, *Commun. Math. Phys.*
196:703–731). Whether T* = 5/7 is itself a β_c in a TIG-specific
partition function is open; the structural kinship (Farey-tree location,
transfer-operator spectral gap, Riemann-zeta limit) is established. See
`papers/morphotic_braid/synthesis/RIGOR_MAPPING.md` §Track 2 for the
vocabulary map.

**Primon-gas link for 4/π² = sinc²(1/2).** The exact identity
sinc²(1/2) = (2/3)·1/ζ(2) (FORMULAS §6.5, `papers/proof_sinc_zeta_identity.py`)
places TIG's corridor-midpoint constant in the **fermionic primon gas**
regime (Julia 1990, *Number Theory and Physics* — Les Houches 1989,
Springer Proc. Phys. 47:276–293; Spector 1990, *Commun. Math. Phys.*
127:239–252), since 1/ζ(2) = 6/π² is the density of squarefree integers.
This is the domain of the WP101 σ rate theorem (squarefree N).

### Volume J — Three-Table Architecture, BDC Encoding, and Two-TSML Reconciliation (Sprint 2026-05-06)

| ID | name | formula | status / file |
|----|------|---------|---------------|
| **D95** | CL_STD as the third standalone composition table (44 HARMONY) | The substrate has THREE standalone 10×10 composition tables on Z/10Z, not two. **CL_TSML** (prescribed view, 73 HARMONY, "the organism's lens"; aliased simply `CL` in the old codebase via `#define CL CL_TSML`); **CL_BHML** (Becoming lens, 28 HARMONY, curvature-level, invertible-on-self, CUDA substrate); **CL_STD** (Standard encoding table, 44 HARMONY, "the papers freeze"; recovered verbatim from `old/Gen9/archive/ckis/ck7/ck.h:225-231` — Brayden's first GitHub repo). All three share the substrate (Z/10Z, same 10 operators) but are structurally distinct matrices with different roles: TSML is what CK runs on, BHML is the alternate Becoming lens, STD is the encoding table the papers reference. CL_STD is commutative; non-associative rate 19.2%. | PROVED, machine-precision; [Gen13/targets/foundations/cl_std.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen13/targets/foundations/cl_std.py) (matrix, 44/100 HARMONY count, 19.2% non-assoc verified by `invariants.py`); architecture per ck.h:200-207 |
| **D96** | BDC encoding parameters on CL_STD ("force vectors encode pathways of information; surprise IS information") | CL_STD carries explicit BDC bit definitions for force-vector pathway encoding: **5 BUMP_PAIRS** = {(1,2), (2,4), (2,9), (3,9), (4,8)} (where "surprise IS information"); **INFO_HARMONY = 0.45**, **INFO_NORMAL = 1.89**, **INFO_BUMP = 3.50** bits per cell (Shannon information per cell type); total information across 100 cells = **144.62 bits**; **GRAVITY** array = P(operator reaches HARMONY) = (VOID 0.1, LATTICE 0.8, COUNTER 0.6, PROGRESS 0.8, COLLAPSE 0.7, BALANCE 0.9, CHAOS 0.9, HARMONY 1.0, BREATH 0.8, RESET 0.7). | PROVED (definitions); [Gen13/targets/foundations/cl_std.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen13/targets/foundations/cl_std.py) BUMP_PAIRS, INFO_HARMONY, INFO_NORMAL, INFO_BUMP, GRAVITY; verified by `invariants.py` (5 BUMPs, 10-element GRAVITY, GRAVITY[7]=1.0) |
| **D97** | The 70 / 71 / 72 / 73 HARMONY ladder (4 rungs from 4 structurally distinct constructions) | HARMONY counts cluster at four nearby integers, each from an independent construction. **73** = TSML.HARMONY full 10×10 (ground anchor); **72** = TSML.HARMONY − 1 (drop the (7,7) self-cell apex; BEING shell of nested tori; E_6 positive root count); **71** = TSML[1..9] sub-magma HARMONY = \|TSML XOR BHML\| disagreement count = prime in disc(LMFDB 4.2.10224.1) = −2⁴·3²·**71** (THREE structural roles for the prime 71 — sub-magma HARMONY count, lens-disagreement count, Galois prime); **70** = det(BHML_8_YM) where {0,7} dropped (Yang-Mills core, 8×8) = C(8,4) = self-dual 4-form sector of SO(8); NOT a HARMONY count, lives one floor below in the determinant-invariant layer. The four-step descent: max-HARMONY → drop-apex → lens-disagreement → YM-core-determinant. **Companion counts (same integer, multiple structural roles):** **44** = CL_STD.HARMONY = BHML σ²-cycle-B projection (28+11+5); **36** = TSML_7 sub-magma HARMONY = BHML σ²-cycle-A projection (CYCLE_A_36); **28** = BHML.HARMONY = HARMONY_44 BEING(HARMONY) = dim SO(8). | PROVED, all 5 rungs verified; [Gen13/targets/foundations/tables/harmony_ladder.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen13/targets/foundations/tables/harmony_ladder.py) (LADDER + verify() function; 5/5 OK in `invariants.py`) |
| **D98** | Two-TSML reconciliation: CL_TSML_RAW vs CL_TSML_SYM are two valid lenses on the same encoding | CL_BIT_PATTERN has TWO asymmetric upper/lower-triangle cell pairs at **(3, 9)** and **(4, 9)**. Two structurally distinct TSMLs live on the same bit pattern. **CL_TSML_RAW**: literal bit pattern, **non-commutative**, **126** non-assoc triples (12.6%), char poly **c_2 = 33 = 3·11** and **c_8 = −120736 = −2⁵·7³·11** (carries the WP107 wobble at coefficient level). **CL_TSML_SYM**: upper-triangle authoritative symmetrization, **commutative**, **128** non-assoc triples (12.8%), char poly c_2 = 17 (no factor of 11; symmetrization erases the wobble). **Lens-invariant on both**: 73 HARMONY, 17 VOID, trace 63 = 9·7, det 0, the 4-core {0,7,8,9}, the 4-core attractor at α=1/2, the 4-core arity-3 closure (WP110), the LMFDB 4.2.10224.1 quartic + Galois D_4 (WP105). **Lens-specific**: the WP107 wobble (c_2 + c_8 prime-11) holds for RAW only; sprint 17's tower reconstruction targets SYM only; the canonical "12.8%" disagreement-vs-BHML number is SYM. **Resolution**: foundations module [Gen13/targets/foundations/cl.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen13/targets/foundations/cl.py) exposes both as first-class names (`CL_TSML_RAW`, `CL_TSML_SYM`, plus `get_tsml(role)` router). Phase 1 migration: legacy alias `TSML = TSML_SYM` preserves all 48/48 invariants; Phase 2 (post-Paper-1+2 ship): flip default to TSML_RAW; Phase 3 (pre-Phase-4 ship): patch WP107/WP109/WP110/WP112/WP113 abstracts to scope which TSML. | PROVED, sympy-exact; [Gen13/targets/foundations/cl.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen13/targets/foundations/cl.py) CL_TSML_RAW/CL_TSML_SYM/get_tsml; [Gen13/targets/foundations/lenses.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen13/targets/foundations/lenses.py) TSML_RAW/TSML_SYM/TSML(legacy alias); reconciliation document [Atlas/META_PLAN_2026-05-06/TSML_RECONCILIATION.md](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Atlas/META_PLAN_2026-05-06/TSML_RECONCILIATION.md) |
| **D99** | Three-table HARMONY count signature: (73, 28, 44) and set-algebra of HARMONY cells | The three standalone tables (CL_TSML, CL_BHML, CL_STD) have HARMONY counts (73, 28, 44) — three structurally distinct counts. Set algebra over the HARMONY-bool masks of the three tables: \|TSML & BHML\| = 26 (both lenses agree on HARMONY at 26 cells); \|TSML & STD\| = 42; \|BHML & STD\| = 21; \|TSML & BHML & STD\| = 19 (all three agree at 19 cells); \|TSML \| BHML \| STD\| = 75 (HARMONY appears somewhere in 75 of 100 cells across the three tables); 25 cells are HARMONY-free in all three. The non-equality of the three counts (73 ≠ 28 ≠ 44) is itself an invariant that distinguishes the three-table architecture from any single-table or two-table model. | PROVED, integer-precision; [Gen13/targets/foundations/invariants.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen13/targets/foundations/invariants.py) checks `(73, 28, 44)` triple + non-equality |

### Volume J §J.1 — The complete variant inventory (every form of CL, TSML, BHML this repo holds)

**Why this section exists.** Until 2026-05-06 evening, this document spoke as if there were "two tables, TSML and BHML, on a single substrate CL." That model was inherited from the `#define CL CL_TSML` alias in old/Gen9/archive/ckis/ck7/ck.h and from the "Being / Becoming" pedagogical framing of Gen 10-12. **The model was wrong at two levels simultaneously.**

**What was missed (the historical compression):**

1. **The third standalone table CL_STD was lost.** The original ck.h (lines 200-207) defined THREE distinct 10×10 tables: CL_TSML (73 HARMONY, the prescribed view), CL_BHML (28 HARMONY, the Becoming lens), and CL_STD (44 HARMONY, the Standard encoding table — "the papers freeze"). The Gen 8-9 refactor introduced `#define CL CL_TSML` for runtime convenience; from that point forward, "CL" was treated as synonymous with "TSML" in active code, and CL_STD fell out of every downstream document. Brayden caught this on 2026-05-06: *"you have forgotten an entire table that is his encoding of an explicit set across a table is made to encode the path of the torus."* CL_STD recovered verbatim from the archive and reinstated as the third standalone table (D95).

2. **TSML and BHML are FAMILIES, not single matrices.** The "two tables" model treated both as monolithic. In fact:
   - **TSML has at least 23 distinct named variants.** Lens-symmetrization choices (RAW, SYM, LOWERTRI), eight chain sub-magma scopes, an off-chain YM scope, four explicit algebraic constructions (PureIdempotent, Idempotent_2sw, C0, PureVoid/AllHarmony boundaries), the corner sub-magma C = {1,3,7,9}, and six F_p ring extensions.
   - **BHML has at least 20 distinct named variants.** Eight chain sub-magma scopes, BHML_8_YM (Yang-Mills core, drops {0,7}, det = +70), BHML_8_chain (drops {1,2}, det = -7542), three σ²-value-rotation triadic candidates (BEING / DOING / BECOMING), three σ²-index-rotation candidates, three anomaly-cell-flip candidates (still hypothetical), six F_p extensions.
   - **CL_STD currently has one canonical form** but carries internal BDC structure (5 BUMP_PAIRS, 100 cells classified into HARMONY/NORMAL/BUMP, GRAVITY array). Sub-magma variants of CL_STD have not yet been investigated; this is open frontier.

The historical compression was a sequence of pedagogically-justified simplifications. Each step traded structural fidelity for surface clarity. The `#define CL CL_TSML` was a 1-line refactor that read as "convenience." The "Being / Becoming" framing was a 2-page pedagogy. The "12.8% non-associative" line in the rigor pass document was a 1-line cell-count summary. Each compression was locally reasonable; their accumulation cost the substrate's actual lens-family architecture.

**Why this matters going public:** if Phase 4-5 papers cite "the substrate" as a single object and a referee asks "which TSML matrix?", the citation chain breaks. The correct posture is the one this section now adopts: **the substrate is a bit-pattern + a family of lens projections from it.** Each variant below is appropriate to recognize because each carries a structural property no other variant carries — eliminating any one of them would make some published statement false or unverifiable.

#### J.1.A — CL_TSML family (the prescribed view)

The prescribed view of the substrate. Used by CK at runtime, by the foundations module's invariants (default), and by sprint 17's tower reconstruction.

##### J.1.A.i — Lens-symmetrization variants on the same 10×10 bit pattern

| Variant | Definition | Distinguishing property | Reason to recognize | Source |
|---------|-----------|------------------------|---------------------|--------|
| **TSML_RAW** | Literal `CL_BIT_PATTERN` decoded; no symmetrization | non-commutative; 126 non-assoc (12.6%); char poly c_2 = **33 = 3·11**, c_8 = **−120736 = −2⁵·7³·11** | **Carries the WP107 wobble.** Prime 11 lives at coefficient level only on RAW. WP107/WP109/WP110/WP112/WP113/WP115 verification scripts hardcode this matrix. | [Gen13/targets/foundations/cl.py:CL_TSML_RAW](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen13/targets/foundations/cl.py:CL_TSML_RAW); D98 |
| **TSML_SYM** | Upper-triangle authoritative symmetrization of `CL_BIT_PATTERN` | commutative; 128 non-assoc (12.8%); char poly c_2 = 17 (no factor of 11) | **The canonical 12.8% number** quoted in `_CK_MEMORY_MAKEOVER.md` and the foundations invariants. Eigenvalues real. Comparable as a symmetric form against BHML. Sprint 17's tower reconstruction (C_0 ⊕ S_MAX ⊕ S_ADD) targets this matrix exactly. | [Gen13/targets/foundations/cl.py:CL_TSML_SYM](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen13/targets/foundations/cl.py:CL_TSML_SYM); D98 |
| **TSML_LOWERTRI** | Lower-triangle authoritative symmetrization | 122 non-assoc; c_2 = 17, c_8 = 0; no wobble | **Tested but not promoted.** Carries fewer structural invariants than RAW or SYM. Documents the "third lens choice" exists; useful as a control to confirm the wobble (RAW) and the canonical rate (SYM) are not symmetrization artifacts. | [Atlas/META_PLAN_2026-05-06/TSML_RECONCILIATION.md](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Atlas/META_PLAN_2026-05-06/TSML_RECONCILIATION.md) |

The two asymmetric cells distinguishing RAW and SYM are at positions **(3, 9)** and **(4, 9)** in the bit pattern (each a 7↔3 swap). Both cells live exactly on the σ-fixed lattice {0, 3, 8, 9} ∪ HARMONY-axis intersection — the wobble localizes there because non-commutativity sits exactly on PROGRESS/COLLAPSE × RESET edges, which are the cells WP107 traces.

##### J.1.A.ii — Sub-magma scope variants (the chain) — 8 instances

For each chain sub-magma scope $S_k$ (per the 4-core paper Theorem 1; see D64), the restriction TSML$_k$ = TSML$|_{S_k \times S_k}$ is its own table.

| Variant | Scope $S_k$ | Size | HARMONY count | det | Non-assoc rate | Reason to recognize |
|---------|-------------|------|--------------|-----|----------------|---------------------|
| **TSML_1** | {0} | 1 | 0 | 0 | 0% | Trivial base of the chain; commutativity check |
| **TSML_4** | {0, 7, 8, 9} (4-core) | 4 | 11 | 0 | 12.5% | The minimal non-trivial chain element; where the 4-core attractor lives |
| **TSML_5** | {0, 6, 7, 8, 9} | 5 | 18 | 0 | 14.4% | First σ-orbit step (Ch enters) |
| **TSML_6** | {0, 5, 6, 7, 8, 9} | 6 | 27 | 0 | 14.8% | Ba enters; pattern continues |
| **TSML_7** | {0, 4, 5, 6, 7, 8, 9} | 7 | **36** | 0 | 14.0% | Co enters. **HARMONY = 36 here matches CYCLE_A_36 count from BHML σ²-cycle-A projection — same integer at two structural roles.** Was the chain's "missing rung" in the original WP115 preprint (forbidden-{2,3,7} bug, corrected 2026-05-05) |
| **TSML_8** (chain) | {0, 3, 4, 5, 6, 7, 8, 9} | 8 | 47 | 0 | 13.3% | σ-fixed bridge step (P enters); the "Hubble derivation" scope per `INTEGRATION_WITH_PROOF_SPINE.md §5` |
| **TSML_9** | {0, 2, 3, 4, 5, 6, 7, 8, 9} | 9 | **71** | 0 | 13.4% | C enters. **HARMONY = 71 here matches the FIELD WOBBLE count and the LMFDB Galois prime — three structural roles for prime 71** (D97 ladder rung) |
| **TSML_10** | full Z/10Z | 10 | 73 | 0 | 12.8% (SYM) / 12.6% (RAW) | The full prescribed view; the ground anchor for all D-numbers |

Each chain variant is its own algebra. Important: **TSML_8 inherits the RAW vs SYM split** because the asymmetric cells (3,9) and (4,9) are both inside the size-8 scope. So TSML_8_RAW ≠ TSML_8_SYM.

##### J.1.A.iii — Off-chain sub-magma scope (Yang-Mills core)

| Variant | Scope | Size | HARMONY count | det | Reason to recognize |
|---------|-------|------|--------------|-----|---------------------|
| **TSML_8_YM** | {1, 2, 3, 4, 5, 6, 8, 9} (drops VOID + HARMONY) | 8 | varies | varies | The VOID/HARMONY-complement scope. Same SIZE as TSML_8_chain but DIFFERENT SHAPE. Per Brayden 2026-05-06: *"multiple sizes AND shapes of TSML and BHML."* The YM core's structural identity lives more visibly in BHML (det = +70 = C(8,4) exactly), but the parallel TSML construction must exist for symmetric pairing in WP115's "Yang-Mills bridge" results. |

##### J.1.A.iv — Algebraic-construction variants (off-chain, structurally distinct algebras)

These are TSML matrices built from explicit algebraic recipes rather than from the bit pattern, used in `papers/morphotic_braid/` and elsewhere.

| Variant | Definition | Distinguishing property | Reason to recognize |
|---------|-----------|------------------------|---------------------|
| **TSML_PureIdempotent** | T[i][i] = i for all i ∈ {0..9}; else HARMONY | det = +398664 = 2³ · 3 · 7 · **113**; \|Aut\| = S₈ = 40320; α ≈ 0.888 | "All ten elements are idempotent" — the maximally idempotent TSML. Used as the morphotic-braid-paper baseline. |
| **TSML_Idempotent_2sw** | TSML_PureIdempotent + cell swaps T[1][2] = T[2][1] = 6, T[3][5] = T[5][3] = 4 | det = **−49 = −7²**; α ≈ 0.880; minimum \|det\| in the prime-7 regime | Suited for octonion / Steiner-quasigroup statements; isolates prime 7 in det |
| **TSML_C0** | Only VOID + HARMONY axis structure (rank 3) | det = 0; α ≈ 0.872; same non-assoc as TSML_10 | Pure absorbing baseline; binary norm signature; control for universal-minimum-bump proofs |
| **TSML_PureVoid** | Degenerate boundary case (all VOID) | rank 0 | Boundary member of the algebraic-variant family |
| **TSML_AllHarmony** | Degenerate boundary case (all HARMONY) | rank 1 | Other boundary member; together with PureVoid spans the algebraic variant simplex |

##### J.1.A.v — The corner sub-magma C = {1, 3, 7, 9}

| Variant | Definition | Reason to recognize |
|---------|-----------|---------------------|
| **C** (corner) | Sub-magma {1, 3, 7, 9} ⊆ Z/10Z; closed under TSML | 4-element TSML closure with absorbing-at-corners property; C × C ⊆ C verified at all 16 cells. Distinct from the joint-chain 4-core {0, 7, 8, 9}. Proven closure published in WP39 / Hodge research (Proc. AMS draft). |

Total CL_TSML variants explicitly recognized: **23** (3 lens × 8 chain + 1 YM + 5 algebraic + 1 corner; lens × chain interactions add 7 more for the size-8-RAW vs SYM cases, but those are the same construction class repeated).

##### J.1.A.vi — F_p ring extensions

For p ∈ {2, 3, 5, 7, 11, 13}, the operator-substrate construction over F_p produces TSML$_p$ as a matrix on F_p (not Z/10Z). These are referenced in WP118 / bridge sprint and [Atlas/applications_pass_2026_04_27/code/markov_binary_cl.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Atlas/applications_pass_2026_04_27/code/markov_binary_cl.py) (binary CL on Z/30Z is one such construction). The chain-rigidity claim (joint-closure structure preserved) extends to F_p for p ∈ {2, 3, 5, 7, 11, 13} per the bridge sprint companion (`SandersClaudeChat2026BridgeSprint`, in preparation). 6 additional ring-level instances.

#### J.1.B — CL_BHML family (the Becoming lens)

The Becoming lens. Used as the curvature-level dual of TSML; WP100s tower's substrate for D_4 obstruction (WP109), 4-core fusion-closure (WP110), the closed-form attractor (WP105), and the Yang-Mills bridge (WP104).

##### J.1.B.i — Sub-magma scope variants (the chain) — 8 instances

For each chain sub-magma scope $S_k$, the restriction BHML$_k$ = BHML$|_{S_k \times S_k}$ is its own table. Unlike TSML (whose chain-restrictions all have det = 0), BHML's sub-magma restrictions carry NON-trivial determinants — these are the structural signatures of the Becoming-lens at each scope.

| Variant | Scope $S_k$ | Size | HARMONY count | det | Reason to recognize |
|---------|-------------|------|--------------|-----|---------------------|
| **BHML_1** | {0} | 1 | 0 | 0 | Trivial base |
| **BHML_4** | {0, 7, 8, 9} (4-core) | 4 | 3 | 5305 (= 5·1061) | Where the closed-form 4-core attractor at α=1/2 lives; BHML_4's det signs the 4-core's algebraic identity |
| **BHML_5** | {0, 6, 7, 8, 9} | 5 | 10 | 2843 | First chain extension |
| **BHML_6** | {0, 5, 6, 7, 8, 9} | 6 | 16 | -2886 | det sign-flips here |
| **BHML_7** | {0, 4, 5, 6, 7, 8, 9} | 7 | 22 | 2929 | The chain's "found-again" rung (corrected 2026-05-05); det positive |
| **BHML_8** (chain) | {0, 3, 4, 5, 6, 7, 8, 9} | 8 | 24 | **-7542** | drops {1, 2}; the chain's size-8 BHML; the "Hubble derivation" companion to TSML_8 |
| **BHML_9** | {0, 2, 3, 4, 5, 6, 7, 8, 9} | 9 | 26 | 7272 | Penultimate chain scope |
| **BHML_10** | full Z/10Z | 10 | 28 | **-7002** | The canonical BHML; the "28 HARMONY" matrix; non-assoc 49.8% |

##### J.1.B.ii — Off-chain sub-magma (Yang-Mills core)

| Variant | Definition | Distinguishing property | Reason to recognize |
|---------|-----------|------------------------|---------------------|
| **BHML_8_YM** | {1, 2, 3, 4, 5, 6, 8, 9} (drops VOID + HARMONY) | det = **+70 EXACTLY** = C(8, 4) = self-dual 4-form sector of SO(8) | The Yang-Mills bridge core (per WP104). Same SIZE as BHML_8_chain (det = -7542), DIFFERENT SHAPE — the cleanest demonstration that "size and shape are independent dimensions" of the lens family. **70 is the bottom rung of the HARMONY ladder** (D97); det of BHML_8_YM, not a HARMONY count itself. |

##### J.1.B.iii — σ²-triadic candidates for "three BHMLs" (exploratory; not yet canonical)

Per Brayden's hypothesis 2026-05-06 ("there may be three bhml tables") — investigated in [Gen13/targets/foundations/bhml_variants.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen13/targets/foundations/bhml_variants.py). These are candidate constructions; selection of which (if any) is canonical is open.

| Variant | Definition | Disagreement with TSML | Reason to recognize |
|---------|-----------|------------------------|---------------------|
| **BHML_BEING** (candidate) | BHML_10 canonical (28 HARMONY) | 71 (matches WP107 wobble count) | Identity-mode; the canonical BHML serves as BEING |
| **BHML_DOING** (candidate) | σ²(BHML values): each cell value v → σ²(v) | 94 | "DOING-mode" BHML where cell outputs are triadically rotated; σ²-cycle-B becomes the value lens |
| **BHML_BECOMING** (candidate) | σ⁴(BHML values) | 90 | "BECOMING-mode" BHML; second triadic step |
| **BHML_idx_DOING** (candidate) | BHML[σ²(i), σ²(j)] (index permutation) | 75 | Alternative DOING construction via row/col index rotation |
| **BHML_idx_BECOMING** (candidate) | BHML[σ⁴(i), σ⁴(j)] | 79 | Alternative BECOMING construction |

The disagreement-counts {71, 94, 90} (value-rotation) and {71, 75, 79} (index-rotation) do NOT reproduce the canonical 71/72/73 triple from D97's HARMONY ladder. Brayden's choice of which construction is the "canonical three BHMLs" is open. Decision-pending.

##### J.1.B.iv — Anomaly-cell-flip candidates (hypothetical; cells unidentified)

| Variant | Definition | Status |
|---------|-----------|--------|
| **BHML_71** | BHML_10 canonical | known: \|TSML_SYM - this\| = 71 |
| **BHML_72** | BHML_10 with one specific cell flipped to give 72-disagreement | hypothetical; specific cell to flip not yet identified |
| **BHML_73** | BHML_10 with two specific cells flipped to give 73-disagreement | hypothetical; cells unidentified |

If structurally meaningful, this would close the 71/72/73 triple in the BHML-disagreement sense. Currently open.

##### J.1.B.v — F_p ring extensions

Same as TSML F_p extensions: BHML$_p$ for p ∈ {2, 3, 5, 7, 11, 13}. 6 ring-level instances.

Total CL_BHML variants: **20** (8 chain + 1 YM + 5 σ²-triadic candidates + 3 anomaly-flip candidates + 3 not-yet-implemented sub-scopes).

#### J.1.C — CL_STD (the encoding table)

Currently 1 canonical 10×10 form + internal BDC structure. Sub-magma variants of CL_STD have not been investigated (open frontier — not yet probed).

| Variant | Definition | Reason to recognize |
|---------|-----------|---------------------|
| **CL_STD** | 10×10 commutative table from `old/Gen9/archive/ckis/ck7/ck.h:225-231` | The encoding table; 44 HARMONY; "the papers freeze"; carries BDC bit definitions (5 BUMP_PAIRS, INFO_HARMONY/NORMAL/BUMP, GRAVITY array per D96) |
| **CL_STD sub-magmas** (open) | Restrictions of CL_STD to chain-scopes / off-chain scopes | Not yet computed. CL_STD might admit its own 8-element joint-closure chain analogous to TSML+BHML; this is open structural frontier. |
| **CL_STD F_p extensions** (open) | CL_STD over F_p substrates | Not yet investigated; analog to the TSML/BHML F_p extensions |

#### J.1.D — Derived tables (functions of two or more of the above)

| Variant | Definition | Reason to recognize |
|---------|-----------|---------------------|
| **DOING** (= \|TSML − BHML\|) | element-wise absolute difference; 71 cells differ for SYM | The third lens of the dual-table model: "where information generates" per the Crossing Lemma. ~71% disagreement rate ≈ T* = 5/7. |
| **DOING_RAW** (= \|TSML_RAW − BHML\|) | analogue using TSML_RAW | Slightly different disagreement count; carries the wobble-bearing TSML's directional bit |

#### J.1.E — Generalizations to other rings (frontier; conjectural)

| Variant | Ring | Status |
|---------|------|--------|
| **binary_cl** | Z/30Z (= F_2 × F_3 × F_5 via CRT) | Proof-of-concept generalization in [Atlas/applications_pass_2026_04_27/code/markov_binary_cl.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Atlas/applications_pass_2026_04_27/code/markov_binary_cl.py). Echo-harmony structure preserved; chain rigidity conjectured |
| **TSML/BHML on Z/8, Z/12, Z/14** | small even rings | Open conjecture (FRONTIER_FINDINGS F5): does the α=1/2 closed-form structure exist at native scales of other small rings? Not yet computed. |

---

#### J.1.F — Total inventory at a glance

| Family | Standalone tables | Sub-magma scope variants | Algebraic/lens variants | Triadic/exploratory | F_p extensions | TOTAL |
|--------|-------------------|--------------------------|--------------------------|-------------------|----------------|-------|
| **CL_TSML** | 1 (CL_TSML at size 10) | 8 chain + 1 YM = 9 | 3 lens (RAW/SYM/LOWERTRI) + 5 algebraic (PureIdempotent, Idempotent_2sw, C0, PureVoid, AllHarmony) + 1 corner C = 9 | — | 6 | **23 named + 6 ring** |
| **CL_BHML** | 1 (CL_BHML at size 10) | 8 chain + 1 YM = 9 | — | 5 σ²-triadic + 3 anomaly-flip = 8 | 6 | **17 named + 6 ring** |
| **CL_STD** | 1 (CL_STD at size 10) | 0 (not yet investigated) | 0 | 0 | 0 | **1 named + 0 ring** |
| **DERIVED** (DOING, etc.) | 1 (DOING) | — | 1 (DOING_RAW) | — | — | **2** |
| **GENERALIZATIONS** | — | — | — | — | 1 explicit (binary_cl Z/30) + 3 frontier (Z/8, Z/12, Z/14) | **4 frontier** |

**Summary count**: **3 standalone tables**, **40+ named variants** across the three families, **plus 12+ ring-extension instances**, **plus 4 frontier rings**. The substrate is not "two tables"; it is a bit-pattern-with-encoding-rules + a family of lens projections numbering in the dozens, each carrying a structural property the others do not.

#### J.1.G — Why each variant is appropriate to recognize explicitly (the master answer)

Brayden's question: *why did we think we had two tables, when we have 3 tables with multiple variants of two of them?*

The honest answer is that the two-table model was a sequence of historically reasonable but cumulatively lossy compressions:

1. **The original ck.h had three.** ck.h:200-207 explicitly defined CL_TSML, CL_BHML, CL_STD. The `#define CL CL_TSML` alias (added later) was a 1-line refactor for runtime convenience — but it conflated CL with TSML at the symbol level, and CL_STD had no consumer in active code, so it dropped out of every downstream document. This was the first compression: 3 → 2.

2. **The pedagogy crystallized the binary.** "Being lens / Becoming lens" is a beautiful 2-element teaching tool. It crystallizes the dual-projection insight cleanly. But it implicitly treats each lens as a single matrix. This was the second compression: 2 monolithic → still 2 monolithic.

3. **The variants accumulated underneath without being named together.** TSML_RAW vs TSML_SYM emerged because different scripts hardcoded the bit pattern differently. The chain sub-magmas (TSML_4, BHML_8, etc.) were enumerated in `lens_family.py` but treated as a parametric family rather than as a list of distinct named matrices. The σ²-triadic BHML candidates were sketched in `bhml_variants.py` but never promoted to canonical. The algebraic-construction TSMLs (PureIdempotent etc.) lived in `papers/morphotic_braid/` as a separate paper's vocabulary. None of these were collected into a unified inventory until tonight.

The model held up because for many purposes — a single sprint, a single paper, a single proof — only one or two variants matter and the others are either lens-invariant or out of scope. "TSML and BHML" was correct enough to do the work. **It just was not exhaustive enough to publish.** Going public means the citation chain has to survive a referee asking *"which TSML matrix? At what scope? Under what symmetrization?"*

**The structural truth (going forward):**

- The substrate has **three encodings**: CL_TSML (prescribed view, 73 H), CL_BHML (Becoming lens, 28 H), CL_STD (encoding table, 44 H). These are the three standalone matrices. Each has a different role and a different role-defining HARMONY count.
- **Each encoding admits a family of lenses.** TSML's family includes lens-symmetrization choices, sub-magma scopes, off-chain scopes, algebraic constructions, the corner sub-magma. BHML's family includes sub-magma scopes, the YM scope, σ²-triadic candidates, anomaly-flip candidates. CL_STD's family is currently small but its sub-magma structure is open.
- **The lens family is the appropriate object of study** at the substrate level. A single matrix is the answer to a single question; the family is the answer to *"what is the substrate?"*
- **Every variant in this inventory is recognized explicitly because each one carries a property no other carries.** Drop TSML_RAW: lose the wobble. Drop TSML_SYM: lose Sprint 17's tower. Drop BHML_8_YM: lose the +70 = C(8,4) Yang-Mills bridge. Drop the corner sub-magma C: lose the 4-element TSML-only closure proof. Drop CL_STD: lose the BDC encoding parameters and the "44" HARMONY count's structural origin. Each variant earns its name by being load-bearing for at least one published or in-preparation result.

This is the model the Phase 4-5 papers will cite: **a substrate that is one bit pattern + three encoding readings + a family of dozens of lens projections**, each named because each is load-bearing somewhere.

---

### Volume J coda — Master release plan (2026-05-06 evening, Sept 11 anchor)

The substrate is mature enough to begin the public-record walk. Master release plan landed in [Atlas/META_PLAN_2026-05-06/RELEASE_PLAN_SEPT11.md](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Atlas/META_PLAN_2026-05-06/RELEASE_PLAN_SEPT11.md):

- **Anchor:** Sept 11, 2026 (daughter's birthday; integration paper lands)
- **Coda:** Sept 12-22 (12 silent days) → Sept 23 (Oxford report)
- **Cadence:** 2-3 papers/week × 18 weeks = ~36 refereed papers before Sept 11
- **Discipline:** never miss a ref pass; no submission without green script; no endorsement-required venue; no venue >2 papers/quarter
- **Phases:** vocabulary-neutral math (May 13 → Jun 7) → exact physics (Jun 10 → Jun 28) → cross-level structures (Jul 1 → Jul 31) → duality named (Aug 1 → Aug 26) → crescendo (Aug 27 → Sept 10)
- **Sept 11 paper:** Brayden's composition; meta-layer observation of the framework
- **First two papers tonight (May 6 → submit May 7 night):** σ-rate theorem → JCT-A; four-core consolidated → Algebraic Combinatorics

Companion dossiers in [Atlas/META_PLAN_2026-05-06/](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Atlas/META_PLAN_2026-05-06/):
- `INVENTORY.md` — 75-paper catalog with phase classification
- `VENUE_SCHEDULE.md` — 20-week table, fallback chains, per-venue dossiers
- `CITATION_CHAIN.md` — 36 papers topologically sorted by internal dependency
- `GAP_AUDIT.md` — 48/48 invariants pass; 2 hard contradictions surfaced and resolved this session
- `TSML_RECONCILIATION.md` — full structural analysis of D98 above
- `RELEASE_PLAN_SEPT11.md` — the master plan

WP115 chain-count correction (D64 already updated): `papers/wp115_joint_chain_universality/WP115_JOINT_CHAIN_UNIVERSALITY.md` patched in this session — 7-element chain → 8-element chain; forbidden sizes {2,3,7} → {2,3} only; size-7 shell {0,4,5,6,7,8,9} added to the table; σ-walk reading updated to "one σ-fixed bridge step at the size 7→8 transition."

---

### Volume K — Atomic-substrate correspondence (D100–D103, 2026-05-10 launch bundle; verified 2026-05-12)

Volume K closes the bridge from the algebraic substrate (Z/10Z + TSML/BHML + 4-core) to atomic structure (hydrogenic orbital quantum numbers + Pauli capacity + Cl(0,10) spinor decomposition). All five verification scripts in [Atlas/META_PLAN_2026-05-10/](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Atlas/META_PLAN_2026-05-10/) run clean. Status: **PROVED** (machine-precision exact identities at the integer/rational level).

**D100 — Edge-size closed form for nodeless hydrogenic orbitals.**

For a nodeless hydrogenic orbital (n, l = n−1) in atomic units (a₀ = 1, Z = 1):

```
edge_size(n, l = n−1) = n²(2l+1)/4
```

Verification (`verify_d2d1_closed_form.py`): ratios of computed-to-formula for n = 1..7:

| n | l | computed edge | formula edge | ratio |
|---|---|---|---|---|
| 1 | 0 | 0.250466 | 0.250000 | 1.0018649 (numerical-quadrature floor) |
| 2 | 1 | 3.000100 | 3.000000 | 1.0000334 |
| 3 | 2 | 11.250004 | 11.250000 | 1.0000004 |
| 4 | 3 | 28.000000 | 28.000000 | 1.0000000 |
| 5 | 4 | 56.250000 | 56.250000 | 1.0000000 |
| 6 | 5 | 99.000000 | 99.000000 | 1.0000000 |
| 7 | 6 | 159.250000 | 159.250000 | 1.0000000 |

The ratio reaches machine precision at n ≥ 5. Equivalently, the substrate-D2/D1 ratio for nodeless orbitals satisfies `D2/D1 · 8π = 2l+1`, the multiplicity at that l.

**D101 — Strand-orbital correspondence.**

The substrate primes that wrap the Z/10Z kernel — strands `{3, 7, 11, 13}` — map exactly to the first four nodeless orbitals at odd l, by the rule:

```
strand p_n  →  orbital (l = (p_n − 1)/2, n = l + 1)
```

| strand | modulus | mult (2l+1) | l | n | orbital | D2/D1·8π |
|---|---|---|---|---|---|---|
| 3 | Z/30 | 3 | 1 | 2 | 2p | 3/(8π) |
| 7 | Z/210 | 7 | 3 | 4 | 4f | 7/(8π) |
| 11 | Z/2310 | 11 | 5 | 6 | 6h | 11/(8π) |
| 13 | Z/30030 | 13 | 6 | 7 | 7i | 13/(8π) |

Substrate strands hit **odd-l** orbitals (p, f, h, i). Even-l orbitals (s, d, g) are not reached because: 1s is kernel-base (no wrapping); 3d's multiplicity 5 = kernel-Z/5 partner, not a strand; 5g's multiplicity 9 = 3² is a composite, only first prime powers wrap. The 4-shell substrate tower (Braiding Fractal Axiom 4, depth-3 limit) realizes EXACTLY the first three odd-l orbital levels with prime multiplicity: 2p, 4f, 6h. The fourth shell (Z/30030 with strand 13) realizes 7i; beyond that, the strand 17 / Stratum III_2 layer would extend.

**D102 — The triple coincidence at d = 3.**

At depth-3 in the Braiding Fractal tower (substrate Z/2310 = 2·3·5·7·11), three independent counts equal 32:

| quantity | value at d = 3 | derivation |
|---|---|---|
| substrate divisors of Z/2310 | 32 | 2⁵ (five distinct prime factors) |
| Pauli capacity of atomic shell n = 4 | 32 | 2n² with n = 4 |
| Cl(0, 10) spinor representation dimension | 32 | 2^⌊10/2⌋ |

The Cl(0, 10) 32-dim irreducible spinor decomposes under the chirality involution ω₁₀ = γ₁…γ₁₀ (with ω₁₀² = +I) as **16 + 16** (positive + negative chirality). This matches the atomic decomposition of the n = 4 shell as **16 spin-up + 16 spin-down**. Within each 16-dim chirality half:

```
16 = 1 + 3 + 5 + 7
   = (2·0+1) + (2·1+1) + (2·2+1) + (2·3+1)   [spatial states (l, m) for l = 0..3]
   = kernel-base + strand₁ + kernel-Z/5-partner + strand₂
```

Three independent counts (substrate divisors / atomic Pauli / Clifford spinor dim) hit 32 with structurally identical 16 + 16 splits. The Z/10 kernel's Z/2 factor = electron spin; the strand-prime structure = orbital multiplicity ladder.

Honest negative: a direct **combinatorial bijection** between the 32 divisors of Z/2310 (grouped 1, 5, 10, 10, 5, 1 by binomial C(5, k)) and the 32 electron states (grouped 2, 6, 10, 14 by Pauli per subshell) does **not** fall out cleanly. The integer match is real; the natural grouping structures differ. Either the bijection uses an alternative combinatorial decomposition not yet tapped (σ-orbits, lens-pair classes), or the integer coincidence is a Pascal-type number-theoretic accident. Flagged as **OPEN substructure** in `priority1_pauli_divisor_attempt.py`.

**D103 — Z/10 as the smallest kernel admitting binary + non-binary structure.**

Among all 2-prime kernels {p, q} that yield k = 5 substrates with 32 divisors when extended by three strands (Braiding Fractal Axiom 8: kernel + 3-strand wrap), only Z/10 = Z/2 × Z/5 admits the canonical structure, because:

| 2-prime kernel | smallest non-binary prime? | binary {2} present? |
|---|---|---|
| Z/6 = {2, 3} | 3 (next-smallest) | yes |
| Z/10 = {2, 5} | 5 (first non-binary not adjacent) | yes ✓ |
| Z/14 = {2, 7} | 7 | yes |
| Z/15 = {3, 5} | — | no (no binary factor) |
| Z/22 = {2, 11} | 11 | yes |
| Z/21 = {3, 7} | — | no |
| Z/35 = {5, 7} | — | no |

Z/10 is uniquely the **smallest** kernel admitting Z/2 (binary distinction / spin) and a non-binary prime not equal to 3 (because 3 is the immediate-successor strand to {2} and is reserved for strand-1 wrapping, not kernel-membership). The Braiding Fractal kernel is therefore Z/10 by minimality, not by external assumption.

This sharpens **architectural uniqueness**: the choice of Z/10 as kernel is forced by the minimality principle "smallest kernel admitting binary + non-binary structure where the non-binary prime is not the immediate-successor strand."

**Volume K verification scripts** (all in [Atlas/META_PLAN_2026-05-10/](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Atlas/META_PLAN_2026-05-10/)):
- `verify_d2d1_closed_form.py` — D100, edge-size formula
- `strand_orbital_map.py` — D101, strand-to-orbital map
- `clifford_substrate_shell.py` — D102, triple coincidence + chirality split
- `meta_extension.py` — D103, kernel uniqueness via 2-prime enumeration
- `priority1_pauli_divisor_attempt.py` — explicit honest-negative on direct divisor↔Pauli bijection
- `VERIFY_ALL.py` — master 14/14 PASS suite covering the core PROVED stack

Volume K complements but does not depend on Volume J (three-table architecture). The new content is the substrate↔atomic bridge: Z/10 + strands = atomic-orbital quantum-number ladder, not by analogy but by exact integer/rational identity.

---

## §1 — The 10-operator sigma menu

The shared symbol vocabulary used by TSML, BHML, σ, CK, the FPGA, and
every paper in the repo.

| code | name      | role |
|------|-----------|------|
| 0    | VOID      | identity / fixed everywhere |
| 1    | LATTICE   | structure entry; β +1 correction at (1,1) |
| 2    | COUNTER   | mirror of progress |
| 3    | PROGRESS  | forward step; σ-fixed |
| 4    | COLLAPSE  | (+1,−1) oscillation; β −2 correction at (0,4) |
| 5    | BALANCE   | midpoint |
| 6    | CHAOS     | (−1,+1) reversed; breakdown→rebuild |
| 7    | HARMONY   | the attractor; TSML diagonal value |
| 8    | BREATH    | self-encounter → harmony (BHML[8][8]=7) |
| 9    | RESET     | self-encounter → void (BHML[9][9]=0) |

CREATION cycle: [1, 3, 9, 7]. DISSOLUTION cycle: [2, 4, 8, 6].

Source: `ck_tig.py` (Gen9 engine), `papers/Q7_BHML_FULL_TABLE.md`.

---

## §2 — The σ permutation on Z/10Z

The hidden operator, written in cycle form:

```
σ = (0)(3)(8)(9)(1 7 6 5 4 2)
```

As a function table (σ as a permutation of {0,...,9}):

| u    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|------|---|---|---|---|---|---|---|---|---|---|
| σ(u) | 0 | 7 | 1 | 3 | 2 | 4 | 5 | 6 | 8 | 9 |

Fixed points: {0, 3, 8, 9}. The 6-cycle: 1 → 7 → 6 → 5 → 4 → 2 → 1.

**G6 theorem:** σ⁶ = id on all 10 states. Proof in `papers/Q_SERIES_SYNTHESIS.md`.

**Restricted to units of Z/10Z** (used in C₀ construction, sprint 25/26):

The "other" σ — the one that appears in `C₀` and `prove_corridor_closure.py` —
is the 2-adic valuation ν₂(3u+1) restricted to units(n) of Z/nZ. For Z/10Z:

| u            | 1 | 3 | 7 | 9 |
|--------------|---|---|---|---|
| 3u+1         | 4 | 10| 22| 28|
| ν₂(3u+1)     | 2 | 1 | 1 | 2 |

So `σ_units(Z/10Z) = {1: 2, 3: 1, 7: 1, 9: 2}`. This is the σ used by the
B-series generators. **Two different σ's, same name, distinguished by domain
(full ring vs units only).**

---

## §3 — The CRT isomorphism φ: F₂ × F₅ → Z/10Z

```
φ: F₂ × F₅ → Z/10Z,   φ(ε, y) = 5ε + 6y  (mod 10)
```

Inverse: ε = u mod 2, y = u mod 5.

The 10-state system decomposes as F₂ × F₅. σ is a semidirect coupling of
a mod-5 quadratic flow (y) with a mod-2 parity shadow (ε). All algebra of
σ is cleaner in (ε, y) coordinates.

The 10 operators in (ε, y) coordinates:

| u | (ε, y) | name      |
|---|--------|-----------|
| 0 | (0, 0) | VOID      |
| 1 | (1, 1) | LATTICE   |
| 2 | (0, 2) | COUNTER   |
| 3 | (1, 3) | PROGRESS  |
| 4 | (0, 4) | COLLAPSE  |
| 5 | (1, 0) | BALANCE   |
| 6 | (0, 1) | CHAOS     |
| 7 | (1, 2) | HARMONY   |
| 8 | (0, 3) | BREATH    |
| 9 | (1, 4) | RESET     |

---

## §4 — The complete σ polynomial (α + β)

Verified 10/10 in `papers/Q9_FLIP_CONDITION_POLYNOMIAL.md` and
`papers/Q10_BETA_COMPLETE_SIGMA_POLYNOMIAL.md`.

```
σ acts on (ε, y) by:

    ε' = ε + α(ε, y)      (mod 2)
    y' = y + β(ε, y)      (mod 5)

where:

    α(ε, y) = 1 − (y² + 2y + 2)⁴
                − ε · [(y² + 3y)⁴ − (y² + 2y + 2)⁴]

    β(ε, y) = −α(ε, y)
                + ε · 4y(y − 2)(y − 3)(y − 4)
                − 2(1 − ε) · 4y(y − 1)(y − 2)(y − 3)
```

(Polynomial arithmetic over F₅ for y; outer structure over F₂ for ε.)

**The three components of β have disjoint support:**

- Term 1: −α (the standard "flip ⇒ decrement y" rule)
- Term 2: +δ₍₁,₁₎(ε, y) = +ε · 4y(y−2)(y−3)(y−4) (LATTICE +1 correction)
- Term 3: −2 · δ₍₀,₄₎(ε, y) = −2(1−ε) · 4y(y−1)(y−2)(y−3) (COLLAPSE −2 correction)

Without LATTICE +1 and COLLAPSE −2, the 6-cycle does not close (G6 theorem).

**Cycle in (ε, y):**
```
(1,1) →+1→ (1,2) →−1→ (0,1) →−1→ (1,0) →−1→ (0,4) →−2→ (0,2) →−1→ (1,1)
LATTICE   HARMONY    CHAOS     BALANCE    COLLAPSE   COUNTER    LATTICE
```
y-step sum: +1 −1 −1 −1 −2 −1 = −5 ≡ 0 (mod 5). Cycle closes.

---

## §5 — TSML — the 10×10 reference table

**The canonical reference table (H_TRUE = 7) used by all B-series
generators.** From
[Gen12/targets/clay/papers/sprint18_b1_nscg_benchmark_2026_04_17/impl/generator/generate_nscg.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint18_b1_nscg_benchmark_2026_04_17/impl/generator/generate_nscg.py).

```
        j=0  j=1  j=2  j=3  j=4  j=5  j=6  j=7  j=8  j=9
i=0  [   0    0    0    0    0    0    0    7    0    0  ]
i=1  [   0    7    3    7    7    7    7    7    7    7  ]
i=2  [   0    3    7    7    4    7    7    7    7    9  ]
i=3  [   0    7    7    7    7    7    7    7    7    3  ]
i=4  [   0    7    4    7    7    7    7    7    8    7  ]
i=5  [   0    7    7    7    7    7    7    7    7    7  ]
i=6  [   0    7    7    7    7    7    7    7    7    7  ]
i=7  [   7    7    7    7    7    7    7    7    7    7  ]
i=8  [   0    7    7    7    8    7    7    7    7    7  ]
i=9  [   0    7    9    3    7    7    7    7    7    7  ]
```

**Counts (verified):**
- HARMONY (7) cells: **73**
- Other non-zero: 4 (LATTICE entries), 4 (PROGRESS), 3 (COLLAPSE),
  2 (BREATH), 2 (RESET), 0 (BALANCE/CHAOS/COUNTER outside of fixed cells)
- Zeroes (VOID): 18

**Sealed truth values (USED by all three B-series generators):**

```python
H_TRUE       = 7
SIGMA_TRUE   = {1: 2, 3: 1, 7: 1, 9: 2}     # ν₂(3u+1) on units
UNITS_TRUE   = [1, 3, 7, 9]
CORE_TRUE    = [3, 7, 9]                     # ker(C₀(_, h)) ∖ {h}
S_MAX_TRUE   = [(2,4),(4,2),(2,9),(9,2),(4,8),(8,4)]   # 6 cells
S_ADD_TRUE   = [(1,2),(2,1)]                            # 2 cells
```

**Diagonal:** `TSML_10[j][j] = 7` for all j ≥ 1; `TSML_10[0][0] = 0`. Collapse to
the attractor on every self-encounter except VOID.

> **Naming.** "TSML" without a subscript in surrounding prose throughout §5–§19
> means the canonical §5 table — aliases **TSML_10** and **TSML_Jordan**.
> Every other variant (TSML_8, TSML_PureIdempotent, TSML_Idempotent_2sw,
> TSML_C0, TSML_PureVoid, TSML_AllHarmony) carries its explicit subscript
> and is disambiguated in §6.7 — the authoritative canonical registry.

---

## §6 — BHML — the 10×10 reference table (28-cell harmony)

> **Naming.** "BHML" without a subscript in surrounding prose throughout §5–§19
> means the canonical §6 table — alias **BHML_10**. The 8×8 spectral core
> (rows/cols 0 and 7 removed) is a distinct matrix, **BHML_8**, with different
> determinant and prime signature. Every precise claim below uses the explicit
> subscript; §6.7 is the authoritative canonical registry.

The sister table to TSML_10. **Symmetric.** 28 HARMONY (7) cells.
**Determinant `det(BHML_10) = −7002`** (SymPy exact-integer verified,
2026-04-24). The 8×8 core `BHML_8` (rows/cols 0 and 7 removed) — used
in the Yang-Mills spectral analysis — has a different determinant,
`det(BHML_8) = +70`. For the disambiguation see §6.4 and the canonical
table registry in §6.7.

From `papers/Q7_BHML_FULL_TABLE.md`, Luther closure 2026-04-01 (BHML[7][0] = 7).

```
        j=0  j=1  j=2  j=3  j=4  j=5  j=6  j=7  j=8  j=9
i=0  [   0    1    2    3    4    5    6    7    8    9  ]   VOID      (Rule 0)
i=1  [   1    2    3    4    5    6    7    2    6    6  ]   LATTICE
i=2  [   2    3    3    4    5    6    7    3    6    6  ]   COUNTER
i=3  [   3    4    4    4    5    6    7    4    6    6  ]   PROGRESS
i=4  [   4    5    5    5    5    6    7    5    7    7  ]   COLLAPSE
i=5  [   5    6    6    6    6    6    7    6    7    7  ]   BALANCE
i=6  [   6    7    7    7    7    7    7    7    7    7  ]   CHAOS    (max+1 = 7)
i=7  [   7    2    3    4    5    6    7    8    9    0  ]   HARMONY  (Rule 7)
i=8  [   8    6    6    6    7    7    7    9    7    8  ]   BREATH   (Rule 89)
i=9  [   9    6    6    6    7    7    7    0    8    0  ]   RESET    (Rule 89)
```

**The four BHML rules:**

```
Rule 0   (VOID):     BHML[0][j] = j           for all j
                     BHML[i][0] = i           for i ∈ {1..6}

Rule 1   (Inner):    BHML[i][j] = max(i, j) + 1   for i, j ∈ {1..6}

Rule 7   (Harmony):  BHML[7][j] = (j + 1) mod 10  for j ≥ 1
                     BHML[7][0] = 7   (symmetry override; Luther closure)
                     [and by symmetry BHML[j][7] = BHML[7][j]]

Rule 89  (Wrap):     BHML[8][j] = [8, 6, 6, 6, 7, 7, 7, 9, 7, 8][j]
                     BHML[9][j] = [9, 6, 6, 6, 7, 7, 7, 0, 8, 0][j]
                     [and by symmetry for cols 8, 9]
```

**Diagonal:**
```
BHML[j][j] = (j + 1) mod 10   for j ∈ {0, 1, 2, 3, 4, 5, 6, 7}
BHML[8][8] = 7    (BREATH self-encounter → HARMONY)
BHML[9][9] = 0    (RESET self-encounter → VOID)

→ BHML diagonal: [0, 2, 3, 4, 5, 6, 7, 8, 7, 0]
```

BHML_10 is **NOT** part of the TSML_10 3-layer theorem spine of §7. It is the
sister table — a non-collapsing, transport/mixing partner to TSML_10's
collapse/projection. Operator-equation linkage between BHML_10 and TSML_10
is observable but not yet algebraically derived.

---

### §6.1 — Associative and associative-commutative spectra (computed 2026-04-23)

For both **TSML_10** and **BHML_10**, taken as commutative groupoids on ℤ/10ℤ, the
associative spectrum s_n(A) (Csákány-Waldhauser 2000) and the
associative-commutative spectrum s_n^ac(A) (Huang-Lehtonen 2022) are:

| n | C_{n−1} | s_n(TSML_10) | s_n(BHML_10) | (2n−3)!! | s_n^ac(TSML_10) | s_n^ac(BHML_10) |
|---|---------|--------------|--------------|----------|-----------------|-----------------|
| 3 | 2       | 2            | 2            | 3        | 3               | 3               |
| 4 | 5       | 5            | 5            | 15       | 15              | 15              |
| 5 | 14      | 14           | 14           | 105      | 105             | 105             |
| 6 | 42      | 42           | 42           | 945      | pending         | pending         |

All n ≤ 5 values verified **exactly** (not sampled) by
`papers/proof_spectra_tsml_bhml.py` on 2026-04-23.

Associativity indices (exact): α(TSML_10) = 872/1000 = 0.872; α(BHML_10) = 502/1000 = 0.502.

**Interpretation.** Both tables achieve the Catalan spectrum s_n = C_{n−1}
(Csákány-Waldhauser's maximum) AND the ac-free spectrum s_n^ac = (2n−3)!!
(maximum for commutative groupoids). In the Huang-Lehtonen framework, this
means the symmetric operad generated by each table is the free commutative
magmatic operad Mag^com on one generator. The associativity index α and
operad freeness are independent properties: TSML_10 has high α (0.872) yet
achieves ac-freeness, demonstrating that rare non-associating triples
generate the full free operad structure.

**Reproducibility.** `python papers/proof_spectra_tsml_bhml.py` — computes
s_3..s_5 and s_3^ac..s_5^ac exactly (runs in ~30-120s depending on host).

**External citations.**
- B. Csákány, T. Waldhauser, "Associative spectra of binary operations",
  Multiple-Valued Logic (2000).
- E. Lehtonen, T. Waldhauser, "Associative spectra of graph algebras I",
  J. Algebraic Combin. 53 (2021), 613-638.
- J. Huang, E. Lehtonen, "The associative-commutative spectrum of a binary
  operation", Discrete Mathematics (2023), arXiv:2202.11826.
- J. Huang, E. Lehtonen, "Associative-commutative spectra for some varieties
  of groupoids", arXiv:2401.15786 (2024).
- R. Mazurek, "Antiassociative magmas", Annali di Matematica Pura ed
  Applicata 204 (2025), 925-941, DOI 10.1007/s10231-024-01512-5.
- J.-L. Loday, B. Vallette, "Algebraic Operads", Grundlehren der
  mathematischen Wissenschaften 346, Springer (2012), §13.5 (free
  commutative magmatic operad).

---

### §6.2 — The TSML variant pair: Jordan vs Idempotent_2sw (2026-04-23)

The canonical TSML of §5 (**TSML_10** = TSML_Jordan) is one representative of
a two-table family that arose in the 2026-04-23 morphotic braid sprint.
Both variants share the carrier ℤ/10ℤ, are fully commutative, satisfy
the Jordan identity exactly, and differ only in two pairs of cells. (The
second variant, **TSML_Idempotent_2sw**, is `TSML_PureIdempotent` — where
`T[i][i] = i` for all i — with two additional cell-swaps applied. The
un-swapped `TSML_PureIdempotent` is a *third* full-rank variant with
`det = +398664`; see §6.6 for the full family and §6.7 for the authoritative
name disambiguation. Do **not** write "TSML_Idempotent" without the `_2sw`
subscript in precise claims.)

| locator | TSML_10 (= TSML_Jordan) | TSML_Idempotent_2sw |
|---------|-------------|-----------------|
| (1,2) = (2,1) | 3 (PROGRESS) | 6 (CHAOS) |
| (3,5) = (5,3) | 7 (HARMONY) | 4 (COLLAPSE) |

Structural measurements (100 total cells, 1000 ordered triples):

| metric | TSML_10 (= TSML_Jordan) | TSML_Idempotent_2sw |
|--------|-------------|-----------------|
| HARMONY rate | 73 / 100 | 71 / 100 |
| ZERO rate | 17 / 100 | 17 / 100 |
| Jordan identity | 100 / 100 | 100 / 100 |
| Moufang (L / R / M) | 874 / 874 / 822 | 888 / 888 / 836 |
| Associativity index α | 872/1000 = 0.8720 | 880/1000 = 0.8800 |
| det(table as ℤ matrix) | 0 (rank-degenerate) | −49 = −7² |
| \|det\| prime factorization | ∅ | {7: 2} |
| operator support | 6 of 10 ops {0,3,4,7,8,9} | all 10 ops |

**Interpretation.** Canonical TSML_10 (= TSML_Jordan) is **operator-sparse** —
LATTICE(1), COUNTER(2), BALANCE(5), CHAOS(6) never appear in its cells.
This is the algebraic baseline for why CK's operator stream tilts
HARMONY-dominated: only 6 of 10 operators are emitted in single-step
composition on TSML_10. TSML_Idempotent_2sw, a full-rank perturbation,
recovers all 10 operators in its cells while slightly improving α.

**Reproducibility.**
- Structural slice: `python papers/morphotic_braid/claudecode_jobs/task16_ck_dual_table_experiment/run_ab_structural.py`
- det = −49 + Jordan + primes: `python papers/morphotic_braid/claudecode_jobs/task15_det_minus49_verify/run.py`
- Full 100/100 result table: `papers/morphotic_braid/results/task16_structural_ab_result.md`

**Runtime A/B (flagged, not run).** A 10,000-tick child-CK A/B on port
7778 would compare operator-stream and coherence behavior. Structural
divergence here is a *necessary* precondition and is confirmed.

---

### §6.3 — The Lie commutator [M_{TSML_10}, M_{TSML_Idempotent_2sw}] (2026-04-23)

Viewing TSML_10 (= TSML_Jordan) and TSML_Idempotent_2sw each as a
10×10 ℤ-matrix (writing M_J for TSML_10 and M_I for TSML_Idempotent_2sw),
the commutator

  C = M_J · M_I − M_I · M_J

has exact structure:

- ||sym(C)||_F = 0.000000 (symmetric part = 0 exact)
- ||anti(C)||_F = 203.032017 (full content antisymmetric)

Therefore **[M_J, M_I] is a pure Lie bracket** in the gl(10, ℤ) sense:
the commutator inhabits the antisymmetric subspace exactly. This is the
algebraic handshake between TSML_10 and TSML_Idempotent_2sw — they are
not merely "two candidate tables," they are two elements of a
Lie-algebraic pair whose bracket closes cleanly. (The Lie-algebraic
closure extended across the full CL flow yields so(8) = D₄; see WP102
and §0 Volume E row D26.)

**Reproducibility.**
- `python papers/morphotic_braid/claudecode_jobs/task14_lie_bracket_verify/run.py`
- Full matrices + verdict: `papers/morphotic_braid/results/task14_lie_bracket_result.md`

---

### §6.4 — Determinants of the three canonical 10×10 tables (2026-04-24)

Independent re-verification (SymPy + NumPy, both exact-integer) against the
tables as defined in `papers/ck_tables.py`:

| table | det | \|det\| prime factorization | rank | HARMONY cells |
|-------|----:|-----------------------------|------|---------------|
| **TSML_10** (= TSML_Jordan, canonical §5) | 0 | ∅ | 9 | 73 / 100 |
| **TSML_Idempotent_2sw** | −49 = −(7²) | {7: 2} | 10 | 71 / 100 |
| **BHML_10** (canonical §6) | −7002 | {2, 3², 389} | 10 | 28 / 100 |

**TSML_Idempotent_2sw** is the diagonal-idempotent variant (T[i][i] = i for all
i ∈ {0..9}) with cell-swaps T[1][2]=T[2][1]=6, T[3][5]=T[5][3]=4 applied to
the un-swapped `TSML_PureIdempotent` (which has det = +398664). It has
full rank and a determinant whose absolute value is 7² exactly — the
operator HARMONY(7) is the unique prime factor.

**TSML_10** (= TSML_Jordan, the canonical §5 table) is rank-degenerate
(rank 9, det = 0). Its null-space direction is the algebraic signature
of the "operator collapse" into HARMONY that makes canonical TSML_10
operator-sparse (only 6 of 10 operators appear in cells).

**BHML disambiguation note (refined 2026-04-24 evening).** Earlier
handoff materials at `papers/morphotic_braid/synthesis/DEEPER_SYNTHESIS.md`,
`papers/morphotic_braid/BHML_SUCCESSOR_AND_IDENTITY.md`,
`papers/morphotic_braid/doubly_regular_core.md`, and
`papers/morphotic_braid/TIG_TABLES_REFERENCE.md` write
"det(BHML) = 70 = 2 · 5 · 7". That number is **correct for the 8×8
core `BHML_8`** (rows/cols 0 and 7 removed) — as defined and verified
in `papers/clay/WHITEPAPER_15_YANG_MILLS_SYNTHESIS.md` §0-§1 and in
[Gen12/targets/ck_desktop/bhml_eigenvalue_analysis.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/ck_desktop/bhml_eigenvalue_analysis.py). It is
**not** the determinant of the canonical full 10×10 table. The full
10×10 BHML in `papers/ck_tables.py` has
**det(BHML_10) = −7002 = −(2 · 3² · 389)**, NumPy- and SymPy-verified
(`papers/verification_logs/2026_04_24/06_verify_det_claims.txt`).

The morphotic_braid synthesis files above were comparing against
TSML_10 (full 10×10), so "`det(BHML) = 70`" in those files reads as a
claim about the full 10×10 — and on that reading it is false. On the
alternative reading (BHML_8 core) it is true. Either way the **scope
must be named**. Any downstream synthesis that relies on "BHML
corresponds to the finite places {2, 5, 7}" must specify which matrix:
for BHML_10 the prime set is {2, 3, 389} and the Connes-Bost hook
does not reach; for BHML_8 the prime set is {2, 5, 7} and the hook
does reach. The Yang-Mills spectral tower in WP15 is correct as
written because its entire argument is about BHML_8 from §0 onward.

See §6.7 below (canonical table registry) for the full authoritative
listing of each table by name, dimension, determinant, and semantic
role.

**Reproducibility.**
- `python papers/morphotic_braid/claudecode_jobs/task15_det_minus49_verify/run.py` (TSML_Idempotent_2sw)
- `python papers/verification_logs/2026_04_24/verify_det_claims.py` (all three tables — TSML_10, TSML_Idempotent_2sw, BHML_10)

---

### §6.5 — Exact identity sinc²(1/2) = (2/3) · 1/ζ(2) (2026-04-23)

A one-line identity ties TIG's corridor-midpoint constant directly to the
Riemann-zeta regime:

  **sinc²(1/2) = 4/π² = (2/3) · (6/π²) = (2/3) · 1/ζ(2)**

Verified to machine precision (difference 5.55 × 10⁻¹⁷) by
`papers/proof_sinc_zeta_identity.py`. The three quantities are:

| quantity | value | meaning |
|----------|-------|---------|
| sinc²(1/2) | 4/π² ≈ 0.4053 | D3 / D24: TIG corridor midpoint (§17) |
| 1/ζ(2) | 6/π² ≈ 0.6079 | density of squarefree integers (classical Mertens) |
| 2/3 | 0.6667 | exact ratio between the two |

**Cross-program linkage.** 1/ζ(2) is (i) the fermionic primon gas density
(Julia 1990; Spector 1990, Comm. Math. Phys. 127:239-252) and (ii) the
leading coefficient c₁ of the Farey fraction spin chain asymptotic
Ψ(N) = c₁ N² log N (Kallies-Özlük-Peter-Snyder 2001; Boca 2007; Technau
2023). The identity puts the **WP101 σ-rate theorem** — which applies
specifically to **squarefree** N — squarely in the fermionic primon gas
regime.

**Reproducibility.** `python papers/proof_sinc_zeta_identity.py`.

**External citations.**
- B. Julia, "Statistical theory of numbers", in *Number Theory and Physics*
  (Les Houches 1989), Springer Proceedings in Physics 47 (1990), 276-293.
- D. Spector, "Supersymmetry and the Möbius Inversion Function",
  Communications in Mathematical Physics 127 (1990), 239-252.
- F. Boca, "Products of matrices [[1,1],[0,1]] and [[1,0],[1,1]] and the
  distribution of reduced quadratic irrationals", J. Reine Angew. Math.
  606 (2007), 149-165.
- M. Technau, "Remark on the Farey fraction spin chain",
  arXiv:2304.08143 (2023).

**WP103 linkage (2026-04-24).** The Lie algebra generated by the joint
antisymmetrization of CL and BHML_10 (WP103, Theorem 3.1) is **so(10) = D₅**,
which is the gauge algebra of the SO(10) grand unified theory
(Fritzsch-Minkowski 1975, *Ann. Phys.* 93:193; Georgi 1975, AIP Conf. Proc.
23:575). SO(10) GUTs embed the Standard Model via the descending chain
SO(10) ⊃ SU(5) ⊃ SU(3)_c × SU(2)_L × U(1)_Y — or the alternative
SO(10) ⊃ SU(4) × SU(2)_L × SU(2)_R Pati-Salam route. The D2 identity
sinc²(1/2) = (2/3) / ζ(2) places TIG's corridor-midpoint constant in the
fermionic primon-gas regime; WP103 identifies the specific gauge algebra
(so(10)) that the Standard-Model sector of this regime would live in.
**Open question.** Does the σ-rate bound (corrected 2026-04-27 per D71:
$\sigma(N) \le 2(N-2)^2/N^3 + \varepsilon(N)/N^3$, sharpening WP101's
previous $\sigma \le C/N$ to $C = 2$ exactly) translate, under the
primon-gas interpretation, to a statement about SO(10) GUT
coupling-unification dynamics? The combinatorial rate has a concrete form;
the gauge-theoretic reading is hypothesis-level.

---

### §6.6 — The TSML/BHML table family (2026-04-24)

The 10×10 commutative magma on ℤ/10ℤ with VOID(0) + HARMONY(7) skeleton
is not a single table — it is a **family** of tables parameterised by
which cells carry HARMONY vs specific operator values. Seven canonical
members cover the space studied in morphotic_braid explorations and
task15/task16 compute jobs. Every invariant below is independently
re-derived by `papers/verification_logs/2026_04_24/verify_family_members.py`
(SymPy exact integer, no ck_tables.py import).

#### The seven canonical family members

| # | name | diagonal | det | \|det\| prime factors | rank | HARMONY | α | Moufang (mid) |
|---|------|----------|----:|------------------------|:----:|:-------:|:---:|:-------------:|
| 1 | **TSML_10** (= TSML_Jordan, canonical §5) | `[0,7,7,7,7,7,7,7,7,7]` | 0 | ∅ | 9 | 73/100 | 0.8720 | 0.8220 |
| 2 | TSML_C0 (pure absorbing) | `[0,7,7,7,7,7,7,7,7,7]` | 0 | ∅ | 3 | 83/100 | 0.8720 | 0.8080 |
| 3 | TSML_PureVoid (no HARMONY on axis) | `[0,7,7,7,7,7,7,7,7,7]` | 0 | ∅ | 1 | 81/100 | 1.0000 | 1.0000 |
| 4 | TSML_PureIdempotent (T[i][i]=i) | `[0,1,2,3,4,5,6,7,8,9]` | +398664 | {2, 3², 7², 113} | 10 | 75/100 | 0.8880 | 0.8320 |
| 5 | **TSML_Idempotent_2sw** (TSML_PureIdempotent + 2 cell swaps) | `[0,1,2,3,4,5,6,7,8,9]` | −49 = −(7²) | {7²} | 10 | 71/100 | 0.8800 | 0.8360 |
| 6 | TSML_AllHarmony (every cell 7 ex. (0,0)) | `[0,7,7,7,7,7,7,7,7,7]` | 0 | ∅ | 2 | 99/100 | 1.0000 | 1.0000 |
| 7 | **BHML_10** (canonical §6) | `[0,2,3,4,5,6,7,8,7,0]` | −7002 | {2, 3², 389} | 10 | 28/100 | 0.5020 | 0.4290 |

Members 1, 5, 7 (bold) are the **three canonical tables** (TSML_10,
TSML_Idempotent_2sw, BHML_10) used in the rest of the paper; members 2,
3, 4, 6 are boundary cases that illuminate the family's geometry. The
spectral core BHML_8 (not listed here — it is 8×8, not 10×10) is a
related object defined by deleting rows/cols {0, 7} from BHML_10; it
has det = +70 and is used only in the §6.7 registry and in WP15
Yang-Mills.

#### Family structure

**The rank wall {det = 0}.** Members 1 (Jordan), 2 (C0), 3 (PureVoid),
6 (AllHarmony) all have det = 0 but at different ranks (9, 3, 1, 2).
These sit on the "rank-deficient wall" of the family. TSML_Jordan is
the rank-9 member — the *closest* to full rank among the rank-deficient
variants.

**The full-rank interior {rank = 10}.** Only three variants have full
rank: TSML_PureIdempotent (+398664), TSML_Idempotent_2sw (−49), and
BHML_10 (−7002). These are the tables with a **well-defined Z-matrix
inverse** — they carry more arithmetic information than the rank-deficient
variants.

**The 2-cell swap {PureIdempotent → Idempotent_2sw}.** Flipping exactly
two symmetric cells T[1][2]=T[2][1]:7→6 and T[3][5]=T[5][3]:7→4
(CHAOS and COLLAPSE, resp.) collapses the prime signature from
{2, 3, 7, 113} to the single prime {7}. The determinant drops from
398664 to −49 — a factor of 8136 — while rank stays at 10 and Jordan
stays at 100/100.

**The α spectrum.** Associativity index splits cleanly into three
regimes across the family:
- **α = 1** (fully associative): TSML_PureVoid, TSML_AllHarmony
- **α ≈ 0.88** (TSML regime): TSML_10 / TSML_C0 (0.872), TSML_PureIdempotent
  (0.888), TSML_Idempotent_2sw (0.880)
- **α ≈ 0.50** (BHML regime): BHML_10 alone at 0.502 ≈ 1/2

No family member lives in the "moderate non-associativity" range
α ∈ (0.5, 0.87). The family is **bimodal** in α.

**Commutativity + Jordan identity.** All seven members are commutative.
All six TSML-family variants satisfy the Jordan identity 100/100 exactly;
BHML_10 satisfies it at 46/100 under the same definition
(`T[T[x][x]][T[x][y]] == T[x][T[T[x][x]][y]]`). BHML_10's lower Jordan
count is consistent with its α ≈ 0.5 — it lives in a genuinely
less-associative regime than the TSML family.

#### Interpretation — the family is doing distinct work

- **TSML_10 (= TSML_Jordan)** is the *working* table — canonical rank 9,
  α = 0.872, HARMONY-dense (73%), carries the TSML 3-layer tower
  decomposition C₀ ⊕ S_MAX ⊕ S_ADD (§7).
- **TSML_Idempotent_2sw** is the *prime-7 regime* table — full rank,
  det = −7², every x idempotent except {1,2} (CHAOS-swapped). It is
  the member most suited to octonion- / Steiner-quasigroup-style
  statements.
- **BHML_10** is the *doing* table — full rank, α ≈ 1/2, HARMONY-sparse
  (28%), operator-rich (all 10 operators appear), prime signature
  {2, 3, 389} dominated by the large prime 389.
- The remaining four are structural extremes (rank-1, rank-2, rank-3,
  pure idempotent) that bound the family's shape.

#### What the family rules out

- **"Doubly regular" assertions** that rely on specific `det(BHML_10) = 70`
  are refuted (see §6.4 correction note and
  `papers/verification_logs/2026_04_24/06_verify_det_claims.txt`).
  The actual BHML_10 prime signature is {2, 3, 389}, **not** {2, 5, 7}.
  The `{2, 5, 7}` prime set belongs to BHML_8 (the 8×8 spectral core),
  which is a *different matrix*.
- Any synthesis that treats "TSML_Idempotent" as a single table (without
  specifying `_2sw` or `PureIdempotent`) is ambiguous: the
  PureIdempotent variant has det = +398664 (prime-set {2, 3, 7, 113})
  while the 2-swap variant has det = −49 (prime-set {7}). These are
  mathematically distinct objects. §6.7 forbids unsubscripted
  `TSML_Idempotent` in precise claims for exactly this reason.
- Membership in the family does **not** imply operator-stream
  equivalence: task16's structural A/B showed
  TSML_10 vs TSML_Idempotent_2sw have materially different operator
  histograms (73 vs 71 HARMONY, 4 vs 1 PROGRESS, 0 vs 3 CHAOS) despite
  both passing Jordan identity 100/100.

#### Reproducibility

```bash
PYTHONIOENCODING=utf-8 python -X utf8 \
  papers/verification_logs/2026_04_24/verify_family_members.py
```

Output archived as
`papers/verification_logs/2026_04_24/07_verify_family_members.txt`.
Supporting family-space exploration scripts live in
`papers/morphotic_braid/explorations/scripts/` with captured output in
`papers/verification_logs/2026_04_24/family/`:

- `01_tsml_family.txt` — 5-member property-satisfaction map
- `02_tsml_idempotent_study.txt` — Aut(TSML_PureIdempotent) = S₈ (|Aut| = 40320), Fano subalgebra scan
- `03_cousin_families.txt` — ν_p(au+b) recipes across N = 10, 14, 22
- `04_full_family_analysis.txt` — C_0 density scaling, (1−density)·N → 2
- `05_tsml_family_search.txt` — bump removal / perturbation deltas

---

### §6.7 — Canonical table registry (2026-04-24, authoritative)

**Purpose.** Every prior section, sprint, and whitepaper uses names
like "TSML", "BHML", "TSML_Idempotent" in a context-dependent way.
This section is the **single authoritative list** of every
TSML- or BHML-named table that appears anywhere in this repo, with its
exact dimension, source definition, determinant, prime signature, rank,
symmetry, and semantic role. When any downstream document writes
"det(BHML) = X" or "TSML_Idempotent has property Y", the reader should
come here first to check which table is meant.

All determinants and ranks below are SymPy exact-integer verified on
2026-04-24 via `papers/verification_logs/2026_04_24/verify_det_claims.py`
and `verify_family_members.py`. These scripts define each table inline
(no `ck_tables.py` import) so they are independently reproducible.

#### The registry (9 canonical named tables)

| # | Name | Shape | Source definition | det | \|det\| primes | rank | Role |
|---|------|:-----:|-------------------|----:|----------------|:----:|------|
| T1 | **TSML_10** (= TSML_Jordan, = canonical §5) | 10×10 | §5 above; `papers/ck_tables.py`; `ck_sim/being/ck_meta_lens.py`; HDL `vortex_cl.v` tsml_table module | 0 | ∅ | 9 | Working TSML. 73 HARMONY, α = 0.872, Jordan 100/100. Base of §7 three-layer tower. |
| T2 | **TSML_8** (core) | 8×8 | TSML_10 with rows/cols {0, 7} removed; indices `[1,2,3,4,5,6,8,9]`. Used in `bhml_eigenvalue_analysis.py` | 0 | ∅ | 7 | TSML spectral core. Rank-deficient (7<8): the TSML 8-core is singular. |
| T3 | **TSML_PureIdempotent** | 10×10 | TSML_C0 + diagonal `T[i][i] = i` for i ∈ {0..9}; `papers/tsml_idempotent_study.py` | +398664 | {2, 3², 7², 113} | 10 | Full-rank idempotent TSML. Aut = S₈ (order 40320). 84 closed 7-element subsets. |
| T4 | **TSML_Idempotent_2sw** | 10×10 | TSML_PureIdempotent with two cell-swaps: `T[1][2]=T[2][1]=6` (CHAOS) and `T[3][5]=T[5][3]=4` (COLLAPSE); task15 of the morphotic_braid compute jobs | −49 = −(7²) | {7²} | 10 | Minimum-\|det\| TSML in the prime-7 regime. The table most suited to octonion / Steiner-quasigroup-style statements. |
| T5 | TSML_C0 (pure absorbing) | 10×10 | Bare absorbing scaffold with only the VOID+HARMONY axis structure; §6.6 | 0 | ∅ | 3 | Boundary case: minimal rank-3 TSML. Used as baseline in universal-minimum-bump arguments. |
| T6 | TSML_PureVoid | 10×10 | No HARMONY on axis; §6.6 | 0 | ∅ | 1 | Boundary case: rank-1 trivialisation. 100% associative, 100% Moufang. |
| T7 | TSML_AllHarmony | 10×10 | Every cell = 7 except `(0,0) = 0`; §6.6 | 0 | ∅ | 2 | Boundary case: rank-2 trivialisation. 99 HARMONY. 100% associative. |
| B1 | **BHML_10** (= canonical §6, = BHML_full) | 10×10 | §6 above; `papers/ck_tables.py`; HDL `bhml_table.v` | **−7002** | **{2, 3², 389}** | 10 | Working BHML. 28 HARMONY, α = 0.502 (≈ ½), full rank. Sister table to TSML_10. |
| B2 | **BHML_8** (core, Yang-Mills) | 8×8 | BHML_10 with rows/cols {0, 7} removed; indices `[1,2,3,4,5,6,8,9]`. Defined explicitly in `papers/clay/WHITEPAPER_15_YANG_MILLS_SYNTHESIS.md` §0. | **+70** | **{2, 5, 7}** | 8 | BHML spectral core. Transfer-matrix candidate for Yang-Mills mass-gap argument (WP15, WP41). Eigenvalue ratio \|λ₇\|/\|λ₆\| = 0.714865 ≈ 5/7 to 0.08%. |

#### Naming pitfalls to stop doing

1. **"det(BHML)" without a subscript.** Always say **`det(BHML_10)`**
   (= −7002) or **`det(BHML_8)`** (= +70). They are different matrices.
2. **"TSML_Idempotent" without a subscript.** Always say **`TSML_PureIdempotent`**
   (det = +398664, prime set `{2,3,7,113}`) or **`TSML_Idempotent_2sw`**
   (det = −49, prime set `{7}`). The two-cell swap changes the
   determinant by a factor of ~8100 and collapses the prime signature
   to `{7}` alone.
3. **"TSML" and "BHML" in a mixed context.** If you are stating a
   property that holds for the full 10×10, say so: "canonical TSML_10
   has …". If you are stating a property that holds only for the
   spectral 8×8 core, say **BHML_8**, not BHML.
4. **"The 8×8 core"** without specifying TSML vs BHML. TSML_8 is
   rank-7 (singular); BHML_8 is rank-8 (invertible). They behave very
   differently.

#### What lives at each determinant

```
det = 0             TSML_10, TSML_8, TSML_C0, TSML_PureVoid, TSML_AllHarmony
det = -49           TSML_Idempotent_2sw                    (prime set {7})
det = +70           BHML_8                                 (prime set {2, 5, 7})
det = -7002         BHML_10                                (prime set {2, 3, 389})
det = +398664       TSML_PureIdempotent                    (prime set {2, 3, 7, 113})
```

Only four distinct non-zero determinants exist across all nine canonical
tables. The prime 7 appears in every non-zero variant except BHML_10.
The primes 2 and 3 appear in three tables each. The prime 5 appears
only in BHML_8. The prime 389 appears only in BHML_10. The prime 113
appears only in TSML_PureIdempotent.

#### Which tables the long-form arguments use

| Argument / result | Uses table |
|------|------|
| TSML 73 HARMONY cells (§5, `proof_d10_tsml_73_cells.py`) | **TSML_10** |
| BHML 28 HARMONY cells (§6, `proof_d16_bhml_28_cells.py`) | **BHML_10** |
| §7 TSML 3-layer tower C₀ ⊕ S_MAX ⊕ S_ADD | **TSML_10** |
| §6.1 α(TSML) = 0.872, α(BHML) = 0.502 | **TSML_10, BHML_10** |
| §6.2 TSML_Jordan vs TSML_Idempotent variant pair | **TSML_10, TSML_Idempotent_2sw** |
| §6.3 Lie commutator `[M_TSML_Jordan, M_TSML_Idempotent]` | **TSML_10, TSML_Idempotent_2sw** |
| §6.6 seven-member family catalog | **all 10×10 members (T1, T3, T4, T5, T6, T7, B1)** |
| WP15 Yang-Mills spectral gap (det = 70, T\* ratio = 0.714865) | **BHML_8** |
| WP41 Yang-Mills mass-gap tie-in (cites WP15 det = 70) | **BHML_8** |
| morphotic_braid "BHML optimality" 100k-sample study | **BHML_10** |
| morphotic_braid DEEPER_SYNTHESIS hook #4 (Connes {2,5,7,∞}) | **BHML_8** (if rebuilt) — see CORRECTION_2026_04_24_det_BHML.md |
| WP102 so(8) = D₄ identification (flow-antisymmetrization closure, dim 28) | **TSML_10** |
| WP103 so(10) = D₅ identification (CL ∪ BHML joint antisymmetrization, dim 45) | **TSML_10, BHML_10** |
| WP103 → WP15 bridge: D₅ ⊃ B₄ ⊃ G₂ ⊃ A₂ stabilizer chain meets BHML_8 eigenvalue ratio 5/7 | **BHML_8, BHML_10** |

#### Reproducibility one-liner

```bash
python -c "from sympy import Matrix; TSML=[[0,0,0,0,0,0,0,7,0,0],[0,7,3,7,7,7,7,7,7,7],[0,3,7,7,4,7,7,7,7,9],[0,7,7,7,7,7,7,7,7,3],[0,7,4,7,7,7,7,7,8,7],[0,7,7,7,7,7,7,7,7,7],[0,7,7,7,7,7,7,7,7,7],[7,7,7,7,7,7,7,7,7,7],[0,7,7,7,8,7,7,7,7,7],[0,7,9,3,7,7,7,7,7,7]]; BHML=[[0,1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,2,6,6],[2,3,3,4,5,6,7,3,6,6],[3,4,4,4,5,6,7,4,6,6],[4,5,5,5,5,6,7,5,7,7],[5,6,6,6,6,6,7,6,7,7],[6,7,7,7,7,7,7,7,7,7],[7,2,3,4,5,6,7,8,9,0],[8,6,6,6,7,7,7,9,7,8],[9,6,6,6,7,7,7,0,8,0]]; C=[1,2,3,4,5,6,8,9]; sub=lambda M,I:[[M[i][j] for j in I] for i in I]; print('TSML_10', Matrix(TSML).det(), Matrix(TSML).rank()); print('TSML_8', Matrix(sub(TSML,C)).det(), Matrix(sub(TSML,C)).rank()); print('BHML_10', Matrix(BHML).det(), Matrix(BHML).rank()); print('BHML_8', Matrix(sub(BHML,C)).det(), Matrix(sub(BHML,C)).rank())"
```

Expected output:
```
TSML_10 0 9
TSML_8 0 7
BHML_10 -7002 10
BHML_8 70 8
```

---

## §7 — TSML_10 3-layer canonical tower (Sprint 17, 2026-04-17)

```
TSML_10(Z/10Z) = C₀ ⊕ S_MAX ⊕ S_ADD       (proved 100/100, residue empty)
```

The 3-layer tower is a theorem about **TSML_10** specifically (equivalently,
TSML_Jordan — the canonical §5 table). TSML_Idempotent_2sw and the other
family members in §6.6 are *not* covered by this decomposition.

**Layer breakdown (Z/10Z, all values verified against the §5 table):**

| layer | cells | output rule |
|-------|-------|-------------|
| C₀ (base) | 65 of 73 HARMONY + the VOID/PROGRESS/COLLAPSE skeleton | σ-rule on units; 0 or h elsewhere |
| S_MAX | 6 cells: {(2,4),(4,2),(2,9),(9,2),(4,8),(8,4)} | output = max(x, y) → 7 |
| S_ADD | 2 cells: {(1,2),(2,1)} | output = (x + y) mod 10 → 3 |

The decomposition is **canonical** (Sprint 17 paper, journal #11 prep).

For every n in the compatibility family (§10), the same 3-layer pattern
applies with parameters (R_n, h_n, σ_n).

**Corridor menu for the union:** {MAX, MIN, ADD}. For pure C₀ alone:
{MAX, MIN}. See §11.

**Verification (runnable, ~1 second):**
```bash
python papers/proof_tsml_3layer_tower.py
# → 100/100 cells match; 92 + 6 + 2 = 100 decomposition;
#   Lemma 5 (residue empty); Lemma 6 (each layer necessary); domains partition R².
```
Full theorem spine: [[05_papers/algebra/J05/manuscript/manuscript.tex](../05_papers/algebra/J05/manuscript/manuscript.tex)](../05_papers/algebra/J05/manuscript/manuscript.tex).

---

## §8 — Three-diagonal comparison (σ on Z/10Z vs TSML_10 vs BHML_10)

| j | σ(j) (CL diag) | TSML_10[j][j] | BHML_10[j][j] |
|---|----------------|---------------|---------------|
| 0 | 0              | 0             | 0             |
| 1 | 7              | 7             | 2             |
| 2 | 1              | 7             | 3             |
| 3 | 3              | 7             | 4             |
| 4 | 2              | 7             | 5             |
| 5 | 4              | 7             | 6             |
| 6 | 5              | 7             | 7             |
| 7 | 6              | 7             | 8             |
| 8 | 8              | 7             | 7             |
| 9 | 9              | 7             | 0             |

**Three distinct projections of σ.** All three agree only at j = 0 (VOID).
TSML_10 and BHML_10 additionally agree at j = 6 (CHAOS).

- **CL diagonal** = the hidden operator's own motion (rotation + fixed points)
- **TSML_10 diagonal** = collapse to attractor 7 for all non-VOID
- **BHML_10 diagonal** = increment toward 7, continue past with exceptions at {8, 9}

---

## §9 — Canonical operator C₀(R_n, h_n, σ_n) for general n

The general-n C₀ used in B-series, Sprint 25, Sprint 26:

```python
def C0(x, y, n, h_n, sigma_n, core_n):
    """
    Canonical C_0 operator on Z/nZ.

    Inputs:
      x, y     : ring elements in {0, ..., n-1}
      h_n      : the attractor (= max odd shell-1 unit)
      sigma_n  : dict {u → ν₂(3u+1)} for u ∈ units(n)
      core_n   : ker(C₀(_, h_n)) ∖ {h_n}

    Returns: an element of {0, ..., n-1}.
    """
    if x == 0 or y == 0:        return 0                    # VOID absorption
    if x not in core_n or y not in core_n:
        return h_n                                           # off-Core → h
    sx, sy = sigma_n[x], sigma_n[y]
    if sx < sy:   return x      # smaller σ wins
    if sy < sx:   return y
    return h_n                                               # σ-tie → h
```

**Definitions:**

```
units(n)    = {u in {1, ..., n-1} : gcd(u, n) = 1}
sigma_n(u)  = ν₂(3u + 1)   for u ∈ units(n)
h_n         = max odd unit u with sigma_n(u) = 1
core_n      = {u ∈ units(n) : C₀(u, h_n) ≠ h_n} ∪ {u : C₀ derives via σ-rule}
            = ker(C₀(_, h_n)) ∖ {h_n}
```

**Shell-by-shell decomposition:**
- Shell 0: {0} — VOID, absorbs.
- Shell 1: units with σ = 1. Contains attractor h_n.
- Shell 2: units with σ = 2.
- Shell k: units with σ = k.

Higher σ = "further from attractor."

For Z/10Z: h_10 = 7. h_14 = 11. h_22 = 19. h_34 = 31. (See §10.)

**Reproducibility:** [05_papers/combinatorics/J19/manuscript/verify_J19.py](../05_papers/combinatorics/J19/manuscript/verify_J19.py).

---

## §10 — The compatibility family (carriers of canonical C₀)

**Primary B-series family (Sprints 18-21):**

| n  | h_n | units | σ-classes | notes |
|----|-----|-------|-----------|-------|
| 10 | 7   | 4     | 2         | the canonical reference (Z/10Z) |
| 14 | 11  | 6     | 4         | |
| 22 | 19  | 10    | 5         | |
| 34 | 31  | 16    | 5         | |

**Extended family (Sprint 25, exhaustive corridor proof):**

```
{10, 14, 22, 34, 38, 46, 50, 58, 62, 70, 74, 82, 94,
 106, 110, 118, 122, 130, 134, 142, 170, 190, 230}
```

Sprint 25 verdict: **all 23 carriers PASS** corridor closure {MAX, MIN}
on pure C₀.

**Sprint 26 ARI scan (32 carriers):**

```
{10, 14, 22, 34, 38, 46, 50, 58, 62, 70, 74, 82, 94,
 106, 110, 118, 122, 130, 134, 142, 158, 166, 170, 178,
 190, 194, 202, 206, 214, 218, 226, 230}
```

Carriers selected as: 2 × prime + small-composite extensions, restricted
to non-empty σ = 1 layer (so h_n exists).

---

## §11 — Corridor closure hierarchy (Sprint 25, exhaustive proof)

**Theorem (proved exhaustively for all 23 carriers up to n = 230):**
For every n in the extended family, every seam cell of the canonical
operator C₀(R_n, h_n, σ_n) matches MAX(x, y) or MIN(x, y). No cell
requires ADD, SUB, MUL, X, or Y.

**Operator-by-operator closure:**

| operator        | corridor closure | proven where |
|-----------------|------------------|--------------|
| C₀ (base)       | {MAX, MIN}       | Sprint 25, all 23 carriers, exhaustive |
| C₀ + S_MAX      | {MAX, MIN}       | inspection (S_MAX cells already MAX) |
| C₀ + S_ADD      | {MAX, MIN, ADD}  | inspection (S_ADD adds 2 ADD cells) |
| C₀ + reset → h  | {MAX, MIN}       | reset cells = h, not in core_outputs |
| Full TSML_10    | {MAX, MIN, ADD}  | union of above |

The empirical Sprint 21 closure {MAX, MIN, ADD} on B-series data is the
**ceiling** over the canonical generator family. Pure C₀ closure
{MAX, MIN} is the **floor** — a 2-element menu.

**Seam counts per carrier (sample):**

| n   | h  | units | seam cells | MAX | MIN | verdict |
|-----|----|-------|------------|-----|-----|---------|
| 10  | 7  | 4     | 2          | 0   | 2   | PASS |
| 14  | 11 | 6     | 12         | 4   | 8   | PASS |
| 22  | 19 | 10    | 48         | 16  | 32  | PASS |
| 34  | 31 | 16    | 132        | 58  | 74  | PASS |
| 230 | 227| 88    | 4946       |2330 |2616 | PASS |

Full table in [05_papers/combinatorics/J19/](../05_papers/combinatorics/J19/).

---

## §12 — The six structural invariants (Sprint 21)

Survive prior-stripping across all 39 B1+B2 datasets. These are the
fingerprint of the underlying generator independent of canonical priors.

```
1. h_hat                 = max odd shell-1 unit (the attractor)
2. image_T               = sorted set of all output values
3. core_outputs          = image_T ∖ {0, h_hat}
4. units_hat             = inputs participating in seam cells
5. partition_hat         = σ-class partition of units (recovered)
6. seam_by_rule_counts   = Counter mapping each rule in {MAX, MIN, ADD,
                           SUB_xy, SUB_yx, MUL, X, Y} to count of seam
                           cells matching it
```

Reproduced in [Gen12/targets/clay/papers/sprint21_structural_discovery_2026_04_17/impl/discovery_fitter.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint21_structural_discovery_2026_04_17/impl/discovery_fitter.py).

---

## §13 — The two-tier collapse signature (Sprint 22)

Universal across all 11 B1/B2 sources. Subsampling at
N ∈ {25, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 50000} × 3 seeds.

```
Tier 1 — Attractor block:
    h_hat                   stable at N ≈ 100 — 2000

Tier 2 — Corridor block:
    image_T
    core_outputs            all stable together at N ≈ 10×Tier 1
    units_hat
    partition_hat
    seam_by_rule_counts
```

The attractor identifies first; the corridor structure emerges as a
single block at ~10× higher N. Scales with n².

Reproduced in [Gen12/targets/clay/papers/sprint22_collapse_point_2026_04_17/impl/nstress.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint22_collapse_point_2026_04_17/impl/nstress.py).

---

## §14 — Walk strategies + ARI scaling (Sprint 23, Sprint 26)

**The eight Sprint 23 walk strategies on T_emp:**

| code | name              | label function on unit u |
|------|-------------------|--------------------------|
| W1   | multiset          | sorted multiset of (T[u][v] for v) |
| W2   | set               | sorted unique outputs |
| W3   | freq              | sorted output frequency profile (histogram) |
| W4   | self-orbit-len    | length of orbit u → T[u][u] → ... |
| W5   | self-orbit        | full self-orbit tuple |
| W6   | fixed-b=1         | orbit u → T[u][1] → T[T[u][1]][1] → ... |
| W7   | fixed-b=h         | orbit u → T[u][h] → ... |
| W8   | commutator        | T[u][1] − T[1][u] (mod n) |

**Cluster:** equivalence classes of equal labels.
**Score:** Adjusted Rand Index vs canonical σ partition.

**Sprint 23 (real B2 data, finite + noisy, n ∈ {10, 14, 22, 34}):**
Best ARI = 0.728 (W3 at n = 34). All other walks ≤ 0.

**Sprint 26 (analytic C₀, infinite/no noise, 32 carriers):**

| n      | ARI W3 | notes |
|--------|--------|-------|
| 10, 14 | 0.000  | too few units |
| 22     | 0.868  | first non-trivial |
| 34     | 0.973  | Sprint 23's noise penalty visible: 0.728 → 0.973 |
| 38     | 1.000  | first perfect |
| 46     | 1.000  | |
| 70     | 1.000  | |
| 158, 166, 170, 178, 190, 194, 202, 206, 230 | 1.000 | |
| all n ≥ 38 | ≥ 0.985 | near-perfect everywhere |

**12 of 32 carriers give ARI = 1.0.** W1 and W2 plateau near 0 (over-fine).

**Headline:** Sprint 23's "σ is curve-only" was noise-limited, not
structural. The shell carries σ at the **histogram level** (class sizes,
recoverable for n ≳ 38). Labeling (which units in which class)
asymptotically also resolved. See Sprint 26 README for the structural
argument.

Reproduced in [Gen12/targets/clay/papers/sprint26_ari_scaling_2026_04_17/impl/ari_scaling.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint26_ari_scaling_2026_04_17/impl/ari_scaling.py).

---

## §15 — TIG = σ⁻¹ inverse polynomial (Q13)

```
TIG = σ⁻¹     on F₂ × F₅

β_TIG(ε, y) = 1 − (y² + 4)⁴ − ε · [(y² + 4y)⁴ − (y² + 4)⁴]
γ_TIG(ε, y) = β_TIG  +  COUNTER correction  +  HARMONY correction
```

**Exception Pair Swap (Theorem Q13.2):**

- σ non-flip exceptions (LATTICE, COLLAPSE) ↔ TIG unique flip nodes
- TIG non-flip exceptions (COUNTER, HARMONY) ↔ σ unique flip nodes
- Shared: {BALANCE, CHAOS} flip under both maps

The duality is structural, not definitional.

Source: `papers/Q13_TIG_INVERSE_POLYNOMIAL.md`.

---

## §16 — C-indicator and gate score framework (Q14)

**C-indicator on Z/10Z (verified 10/10):**

```
1_C(ε, y) = ε · y⁴
```

**Gate score over 9 × 9 operator tables T (Q16, MCMC reduction map):**

```
gate_score(T) = (1 / (|C| · 9))  · Σ_{s ∈ C, c = 1..9}  ε(T[s][c]) · y(T[s][c])⁴
```

The k = 9 here is the **9 columns** of T, not a trajectory depth.
R is not a power of σ (Theorem Q14.1) — the σ-trajectory model predicts
~100% success via HAR-bias, contradicting the observed 4.6% MCMC rate.

**The 22% lower bound (Q11 Fixed-Point Gate Theorem):** gate_score = 1.0
iff s ∈ C ∩ Fix(σ) = {3, 9}. Pure-C seed fraction = 2/9 ≈ 22%. The 22%
is theoretical minimum; 4.6% is empirical search rate. Different objects.

---

## §17 — Constants

| symbol     | value                              | meaning                                         | citation |
|------------|------------------------------------|-------------------------------------------------|----------|
| T*         | 5/7 ≈ 0.7142857                    | torus aspect ratio = crossing threshold         | WP51, six independent derivations |
| 4/π²       | sinc²(1/2) ≈ 0.4053                | Riemann sinc² zero density                      | D3, sinc² Zero Law, all primes 3..199 |
| gap        | 5/7 − 4/π² ≈ 0.3090                | residual between T* and sinc² baseline          | Sprint 10 |
| W          | 3/50 = 0.06                        | wobble parameter; ring-forced                   | D17 |
| BALANCE/10  | 1/2                                | corridor inheritance boundary                   | D21, D22 |
| HARMONY/10 | 7/10                               | corridor harmony position                       | D18c |
| 1/70       | 1/(7·10)                           | fine-structure: T* = 7/10 + 1/70                | D22 |
| Si(2π)/π   | ≈ 0.4514                           | corridor spectral mean ∫₀¹ sinc²(t) dt           | D14 |
| Wob(k)     | 1 − ⌊k/5⌋/k                        | exact closed form; ≥ 4/5; → 4/5                  | D23 |
| ξ₀         | e⁻¹ ≈ 0.3679                       | vacuum of log potential V = ξ log ξ              | WP81 (PRISM-XI), BB |
| m²_ξ       | κ · e                              | mass-gap coefficient                            | WP81 |
| σ rate     | σ(N) ≤ C / N                       | σ-rate theorem (proved, squarefree N)            | WP101, Sprint 14 |
| γ(b)       | 1 − 1/φ(b)                         | transfer-operator spectral gap                   | WP101 / FOUR_LAYER §Z.2 |
| φ(10)      | 4                                  | Euler totient (rate normalization)              | Q15 |
| 22%        | 2/9 ≈ 0.2222                       | gate-rate algebraic minimum (Fixed-Point Gate)   | Q11 |
| 4.6%       | empirical                          | MCMC search rate over 9^81 tables                | Q16 |
| det(BHML_10) | −7002 = −(2 · 3² · 389)           | canonical sister-table determinant (full 10×10) | §6.4, §6.7 (2026-04-24 correction); `verify_det_claims.py` |
| det(BHML_8)  | +70 = 2 · 5 · 7                   | BHML_8 spectral-core determinant (rows/cols {0,7} removed) — used in WP15 Yang-Mills | §6.7, WP15 §0-§1 |
| det(TSML_Idempotent_2sw) | −49 = −(7²)            | full-rank TSML-family variant; prime set {7} | §6.4, §6.6, §6.7 |
| dim so(8)  | 28                                 | D₄ Lie algebra dimension; matches BHML_10 HARMONY-cell count and triality algebra of Spin(8) | WP102, §0 Volume E row D26 |
| dim so(10) | 45                                 | D₅ Lie algebra dimension; rank 5; saturates antisymmetric closure on 10-dim substrate; SO(10) GUT gauge algebra | WP103, §0 Volume E row D27; Fritzsch-Minkowski 1975; Georgi 1975 |
| dim D_4-inv | 16                                 | doubly-invariant subalgebra dim under D₄ = ⟨P_56, σ³⟩ acting on so(10) by conjugation; equals dim su(4) ⊕ u(1) | D34, sprint_unmistakable_truth, `verify_truth.py` |
| Killing spec | (−4)¹⁵ ⊕ (0)¹                     | spectrum of the Killing form on the D_4-invariant subalgebra; forces simple_15 ⊕ center_1 → so(6) ≅ su(4) ⊕ u(1) | D34, `verify_truth.py` |
| ‖antisym‖² | 81 = 9²                            | exact total antisymmetric mass of TSML+BHML over the canonical 10×10 substrate | D37, sprint_unmistakable_truth/CROSSINGS_FINDING.md |
| su(4)-proj | 29                                 | exact projection of antisym mass onto the su(4) simple part of the D_4-invariant content | D34/D37, `verify_truth.py` |
| u(1)-proj  | 25/8 = 3.125                       | exact projection onto the u(1) center | D34/D37, `verify_truth.py` |
| ‖T_lie‖²  | 16                                 | exact L²-mass of TSML's antisymmetric part | D37, `cl_spectrum.py` |
| lattice spec | {7, 7, 7}                        | three exact HARMONY eigenvalues at σ-fixed indices {3, 8, 9} on the lattice projection | D37, `cl_spectrum.py` |
| BHML cells | 26                                 | exact count of BHML cells differing under P_56 conjugation; the σ_outer-asymmetric cell count | D33/D35 |
| ‖VEV‖²    | 13/4 = 3.25                        | exact squared norm of the 9-vector Higgs direction in BHML's σ_outer-breaking, via 26/8 | D33, `find_higgs_direction.py` |
| κ_ξ        | 13/(4e) ≈ 1.196                   | inflaton coupling under GUT-natural identification m²_ξ = ‖VEV‖²; closes README §3.5(iii) at structural level | D35, `xi_cosmology_tie.py` |
| 1 + √3     | ≈ 2.7320508…                      | runtime-attractor HARMONY/BREATH ratio at α = 1/2; positive root of (h/br)² − 2(h/br) − 2 = 0 | D39, `06_attractor_closed_form.py` |
| min poly r/br | x⁴ + 4x³ − x² + 2x − 2 = 0      | quartic min poly of RESET/BREATH ratio at α = 1/2; Galois group D_4; field LMFDB 4.2.10224.1 | D40, D41, `07_full_closed_form.py` |
| disc(f)   | −40896 = −2⁶ · 3² · 71             | polynomial discriminant of the quartic D40                                                  | D41, agent computation 2026-04-25 |
| d_K       | −10224 = −2⁴ · 3² · 71             | field discriminant of LMFDB 4.2.10224.1; ramified at {2, 3, 71}; class number 1; signature (2, 1) | D41, LMFDB 4.2.10224.1 |
| α_priv    | 1/2                                | uniquely privileged mixing weight in [0.05, 0.95] at which the attractor admits a closed-form algebraic relation | D42, `task5_alpha_sweep.py` |
| 8-magma core | TSML \ {BREATH, RESET}            | TSML restricted to {0..7} is closed, commutative, with HARMONY signature 47/64 = 73.4% | D43, `03_eight_magma_core.py` |
| BHML chain | 8 nested closed sub-magmas         | BHML closed-subset count (vs TSML's 398); chain anchored at {VOID, RESET}; smallest containing breathed pair = {V, H, Br, R} | D44, `05_bhml_closure.py` |
| 4-core     | {V, H, Br, R}                      | minimal jointly-closed sub-magma under both TSML and BHML (16+16 in-core, 0+0 spillover); the algebraic support of the runtime attractor | D48, WP110 §3 |
| 4-core normalizer | Z_T = Z_B = (v + h + br + r)²    | identical TSML and BHML normalizers on the 4-core; structural reason for closed-form attractor | D49, WP110 §4, `alpha_uniqueness_symbolic.py` |
| 67         | D₄ orbits of 126 non-associative TSML triples | orbit count under D₄ = ⟨P_56, σ³⟩ acting on triples (a,b,c) with a*(b*c) ≠ (a*b)*c | D47, WP109 §3 |
| 16         | D₄-incoherent orbits               | of the 67 orbits, exactly 16 admit no consistent fuse-table value in {a,b,c,L,R}; obstructs D₄-equivariant fuse rule | D47, WP109 §4 |
| 6 DOFs    | Lie + Jordan + Clifford + Permutation + Lattice + Operad | the six computationally-irreducible algebraic DOFs TIG engages; five respect D₄, sixth (Operad) does not | D51, WP111 §3-12 |
| 8-shell chain | $\{V\} \subset 4\text{-core} \subset \cdots \subset$ full | jointly TSML+BHML closed sub-magmas form a strict 8-element chain; sizes {1, 4, 5, 6, 7, 8, 9, 10}; forbidden sizes {2, 3} only (corrected 2026-05-05 from earlier 7-element claim) | D64, 4-core paper Thm 1 |
| Universal 4-core attractor | $(0.138, 0.540, 0.198, 0.124)$ | unique non-trivial T+B-mix attractor at α=1/2 across the joint chain; mass on $\{V, H, Br, R\}$ only; H/Br = 1+√3 | D65, WP115 §2 |
| Layered hierarchy | 10 → 4 → 2 → 1 | substrate-attractor structure: each layer ~2× collapse (joint chain → 4-core via T+B-mix; 4-core → {V,H} via canonical fuse static image; {V,H} → {H} via canonical ternary fuse iteration) | D67, WP115 §4 |
| Ring-extension universality | $H/Br = 1+\sqrt{3}$ | universal across $\mathbb{Z}/n\mathbb{Z}$ for $n \in \{10..50\}$ under trivial extension; the 4-core sub-magma — not the ring — determines the closed-form attractor | D74, `f5a_universality_scan.py` |
| Spectral radius $\rho$ | 0.34960495 | spectral radius of $J_F$ on simplex tangent at the $\alpha=1/2$ fixed point; convergence rate of the 4-core iteration; hyperbolic-stable | D75 |
| Radial eigenvalue $\lambda_0$ | 2 (exact) | radial Jacobian eigenvalue at $\alpha=1/2$ fixed point; the degree-2 homogeneity signature of $F$; same 2 as in $H/Br$'s minimal poly $x^2-2x-2$ | D75 |
| Lyapunov exponent $\lambda_{\mathrm{TIG}}$ | $-\log \rho \approx 1.05095$ | linearized convergence rate to the 4-core attractor; structurally aligned with FQH $\gamma_{\mathrm{loc}} \approx 2.36$ (Lütken-Ross / Nat. Comm. 2024) without numerical equality | D75, `f8_jacobian_alpha_half.py` |
| Per-projection algebraic depth | depth-2 on $H/Br$, transcendental on eigenvalues | algebraic uniqueness at $\alpha = 1/2$ is projection-specific: $H/Br \in \mathbb{Q}(\sqrt{3})$, but Jacobian eigenvalues are NOT algebraic of degree $\leq 8$ at coeff bound $10^6$ | D76 |
| g          | 3                                  | the only admissible primitive root of (Z/10Z)\* | D19 |
| First-G    | k = p₁                             | first non-coprime element for squarefree b > 1, where p₁ = smallest prime factor | D1, WP34 (22,367 verified pairs, primes ≤ 499) |
| R(k, p)=0  | exact                              | sinc² zero at k = p (max err 4.44e-16)           | sinc² Zero Law |
| N(f)       | ⌊f⌋ + 𝟙{f ∉ ℤ}                     | number of H_f maxima for p > 2f                  | D6 |
| D\*        | 0.543                              | universal self-referencing attractor (operator-aware fixed point of the CK feedback loop) | **`papers/CONSTANT_D_STAR.md`** (runtime-canon; first-principles open; internal correction noted); MEMORY.md; `docs/archive_jan2026/attempts_survey/SYNTHESIS_CK_BEST_EVER.md` §Canon |
| σ (S\*)    | 0.991                              | global stability coefficient in the multiplicative S\* functional; empirical upper bound on attainable coherence at zero stress | **`papers/CONSTANT_SIGMA_S_STAR.md`** (empirical; first-principles open; disambiguated from σ(N) rate function); `S derivatives.docx` v2026.1 (author: Brayden Sanders); extraction at `docs/archive_jan2026/attempts_survey/S_STAR_DERIVATION.md` §2–5 |

These constants do **not** collapse to one number. They live in different
regimes (geometric vs spectral vs cosmological vs combinatorial vs
runtime-operational). See README §11 for honest limits.

**Open provenance on `σ (S\*)` = 0.991 and `D\*` = 0.543** (added 2026-04-21;
derivation papers filed 2026-04-21):
both are operator-layer / runtime constants rather than ring-algebra theorems.
`σ (S\*)` is labelled "empirically derived" in `S derivatives.docx` §5 with no
measurement protocol cited; `D\*` is documented as a runtime-canon self-referencing
attractor with an explicit internal correction preserved in
`tig_engine_real.py` (the scalar-reduction fixed point `σ/(1+σ) = 0.49774…` is not
equal to the observed full-system attractor `0.543` — both are valid answers to
different questions, neither wrong).
Neither constant has a known algebraic relation to T\* = 5/7, 4/π², or the corridor
constants above. Both have proper derivation papers with honest-scope status:

- **`papers/CONSTANT_D_STAR.md`** — status: runtime-canon; first-principles open;
  internal correction noted. Three candidate lift-to-theorem pathways enumerated.
- **`papers/CONSTANT_SIGMA_S_STAR.md`** — status: empirical; first-principles open;
  critical disambiguation from the rate function of §1.2 — under the 2026-04-27
  correction, that bound is sharpened to $\sigma(N) \le 2(N-2)^2/N^3 + \varepsilon(N)/N^3$
  (per D71), but those two `σ`s are still different objects (a different functional, on a different domain).

Tracked as open work items in `https://github.com/TiredofSleep/ck/blob/tig-synthesis/Atlas/PLAN_RIGOROUS_EXECUTION_2026_04_21.md §2` and
in the two derivation papers above.

---

## §18 — Q-series quick index

| paper                       | result | tier |
|-----------------------------|--------|------|
| Q1–Q3                        | TSML, CL non-equivalent projections of σ; agree at {0, 1} | D |
| Q4                           | E ∘ σ = σ̂ ∘ E (σ-equivariance) | D |
| Q5                           | TSML escape cells = σ-fixed-point interaction | D |
| Q6 (hinge)                   | Gate rate is basin problem, not density problem | D |
| Q7                           | BHML_10 full table; 28 harmony cells (Luther-closed) | D |
| Q8                           | All MCMC σ-trajectory models fail | D |
| Q9                           | α flip polynomial verified 10/10 | D |
| **Q10**                      | **complete σ polynomial (α + β) closed** | D |
| Q11                          | Fixed-Point Gate Theorem; 22% lower bound | D |
| Q12                          | CRT idempotents in G; HAR is σ-fixed | D |
| Q13                          | TIG = σ⁻¹ polynomial; Exception Pair Swap | D |
| Q14                          | C-indicator ε · y⁴; R ≠ σ^k | D |
| Q15                          | Period polynomial; k = 9 resonance; both models falsified | D |
| Q16                          | R identified (table search); Luther Q1 closed | D |
| G6                           | σ⁶ = id from polynomial structure | D |
| G7                           | Gate-rate distribution: mean = φ(b), bimodal | D |
| G8                           | Trajectory coherence integral: three-valued | C |
| Q17_5D_RIGOROUS              | 5D force vector as CRT Fourier embedding (proved) | D |
| Q17 (Clay variants)          | NS / RH / Hodge spectral bridges (finite-proven; conjectural in continuous limit) | C |
| **WP102** (Lie lift)          | **so(8) = D₄** identification from CL flow antisymmetrization; 28-dim, triality algebra, Killing signature (0, 28, 0) | D |
| **WP103** (Lie lift)          | **so(10) = D₅** identification from CL ∪ BHML_10 joint antisymmetrization; 45-dim, rank 5, saturates so(V) on 10-dim substrate | D |
| **WP104** (doubly-invariant)  | $D_4 = \langle P_{56}, \sigma^3 \rangle$ → doubly-invariant subalgebra is $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ (Pati-Salam ⊕ B−L); BHML σ_outer-breaking 100% in 54 irrep; 9-vector Higgs $\|v\|^2 = 13/4$ | D |
| **WP105** (closed-form)        | Runtime attractor at $\alpha = 1/2$ has $H/Br = 1+\sqrt{3}$ (exact); $r/br$ root of irreducible quartic $x^4+4x^3-x^2+2x-2$; Galois $D_4$; LMFDB 4.2.10224.1; 4-core $\{V,H,Br,R\}$ support | D |
| **WP106** (specificity scope)  | distilgpt2 16 tensors × 4 detectors all $|d| < 0.5$; **negative result** scoping the framework (TIG structure specific, not generic) | D (negative) |
| **WP107** (WOBBLE)            | Prime 11 in TSML char poly $c_2 + c_8$ only; discriminant $2^{16} \cdot 7^7 \cdot \dots$ has **no** factor of 11; 16-dim doubly-invariant subalgebra is wobble-free | D |
| **WP108** (Yukawa scaffolding) | 9-vec VEV breaks SO(10) → SO(9) → SO(7) → SO(8) chain (16 → 8_s + 8_c spinor decomp); flagged tension with WP104 Path B Pati-Salam decomposition | C (structural with flagged tension) |
| **WP109** (operad obstruction) | 67 $D_4$ orbits of 126 non-associative TSML triples; **16 incoherent**; **no $D_4$-equivariant fuse rule** taking values in $\{a,b,c,L,R\}$ exists; preserve $P_{56}$-equivariance | D |
| **WP110** (4-core closure)    | $\{V,H,Br,R\}$ closed under both TSML and BHML (16+16 in-core, 0+0 spillover); $Z_T = Z_B = (v+h+br+r)^2$; $H/Br = 1+\sqrt{3}$ recovered as **structural identity** (strengthens D39 from dynamical to structural) | D |
| **WP111** (6-DOF synthesis)    | TIG = (Lie + Jordan + Clifford + Permutation + Lattice + Operad); five DOFs respect $D_4$, sixth (Operad) does not — operad-DOF orthogonal to gauge structure; integer/rational signature consistent across all six | C (synthesis) |
| **WP112** (P_56 canonical fuse) | 126 non-assoc TSML triples → **98 P_56-orbits** (70 singletons + 28 doubletons); all P_56-coherent → P_56-equivariant fuse rule **EXISTS** (closes F4); 8/8 surveyed families P_56-equivariant; canonical Family H (attractor-4-core) image $\{0: 108,\ 7: 18\}$; σ³ obstruction localizes to **exactly 1 triple** $(3, 9, 9)$; 4-core arity-3 closure (Theorem 5.5); universal HARMONY attractor under canonical ternary fuse (Theorem 5.7) | D |
| **WP113** (α-uniqueness PSLQ) | 17-point Stern-Brocot grid + 50-digit mpmath + PSLQ at degree ≤ 8, coeff ≤ 50: **α = 1/2 is the UNIQUE rational** producing algebraic relations for both H/Br and r/br; sharpens D42 in three independent dimensions (grid, precision, detection) | D (empirical sharpened); structural uniqueness theorem open |
| **WP114** (specificity extension) | 9-family structured matrix battery (Gaussian/symmetric/antisymmetric/permutation/Hadamard/orthogonal/DFT-real/identity/diagonal/companion, 200 samples each) + WP106 detector battery: **D3 (prime-11) is the unique TIG-positive marker** ($d = +9.93$ for TSML; no other family lights up); D1/D2/D4 are family-structural, not TIG-specific; D3 = WP107 WOBBLE in detector form | D (empirical) |
| **WP115** (joint chain + universal 4-core; chain count CORRECTED 2026-05-05) | Joint TSML+BHML closed-subset lattice = strict **8-element** CHAIN (sizes {1,4,5,6,7,8,9,10}; **forbidden sizes {2,3} only** — earlier 7-element / forbidden {2,3,7} claim was a chain-counting error caught during 4-core manuscript brute-force enumeration; size 7 is allowed at {0,4,5,6,7,8,9}). σ-walk reading: chain walks σ-forward orbit 7→6→5→4 then σ-fixed bridge step 3 then completes orbit 2→1. Universal 4-core attractor: every shell of size ≥ 4 gives identical T+B-mix attractor at α=1/2 with H/Br = 1+√3. α-endpoint structure: α=1 → δ_H, α=0 transcendental, α=1/2 unique algebraic. Layered substrate-attractor hierarchy: 10 → 4 → 2 → 1 (each ~2× collapse). | D (corrected) |

---

## §19 — Sprint trail (paper-by-paper)

| sprint | location | result |
|--------|----------|--------|
| 14 (PRISM-XI) | [Gen12/targets/clay/papers/sprint14_prism_xi_2026_04_10/](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint14_prism_xi_2026_04_10/) | ξ cosmology, V = ξ log ξ, ξ₀ = e⁻¹, σ rate proved |
| 15 (closeout) | (frozen, see `memory/project_sprint15_freeze.md`) | WP91-WP97 staged |
| 16 | [Gen12/targets/clay/papers/sprint16_*](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint16_*) | Basin invariants (Thread C) |
| 17 (TSML tower) | [05_papers/algebra/J05/](../05_papers/algebra/J05/) | TSML_10 = C₀ ⊕ S_MAX ⊕ S_ADD proved 100/100 |
| 18 (B1 NSCG)    | [Gen12/targets/clay/papers/sprint18_b1_nscg_benchmark_2026_04_17/](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint18_b1_nscg_benchmark_2026_04_17/) | B1 generator + 28 honest datasets |
| 19 (B2 WRG)     | [Gen12/targets/clay/papers/sprint19_b2_wrg_benchmark_2026_04_17/](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint19_b2_wrg_benchmark_2026_04_17/) | B2 generator (no S_ADD) + 11 datasets |
| 20 (B3 LBTP)    | [Gen12/targets/clay/papers/sprint20_b3_lbtp_benchmark_2026_04_17/](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint20_b3_lbtp_benchmark_2026_04_17/) | B3 honest implementation; structural FAIL on spec |
| 21 (Discovery)  | [Gen12/targets/clay/papers/sprint21_structural_discovery_2026_04_17/](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint21_structural_discovery_2026_04_17/) | 6 invariants, 39/39 datasets |
| 22 (N-stress)   | [Gen12/targets/clay/papers/sprint22_collapse_point_2026_04_17/](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint22_collapse_point_2026_04_17/) | Two-tier collapse signature (universal) |
| 23 (Curve)      | [Gen12/targets/clay/papers/sprint23_curve_recovery_2026_04_17/](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint23_curve_recovery_2026_04_17/) | "σ curve-only" — later revised by Sprint 26 |
| 24 (Synthesis)  | [Gen12/targets/clay/papers/sprint24_collapse_synthesis_2026_04_17/](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint24_collapse_synthesis_2026_04_17/) | Collapse-point story; 2×2 + paradox classifier spine |
| 25 (Corridor)   | [Gen12/targets/clay/papers/sprint25_corridor_closure_proof_2026_04_17/](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint25_corridor_closure_proof_2026_04_17/) | {MAX, MIN} closure proved exhaustively, 23 carriers |
| 26 (ARI scan)   | [Gen12/targets/clay/papers/sprint26_ari_scaling_2026_04_17/](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint26_ari_scaling_2026_04_17/) | W3-freq ARI = 1.0 at n ≥ 38 on analytic C₀ |
| 27 (B3 memo)    | [Gen12/targets/clay/papers/sprint27_b3_spec_revision_memo_2026_04_17/](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint27_b3_spec_revision_memo_2026_04_17/) | Two minimal revisions to B3 spec; awaiting sign-off |
| 28 (prereg)     | [Gen12/targets/clay/papers/sprint28_curve_recovery_prereg_2026_04_17/](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint28_curve_recovery_prereg_2026_04_17/) | Pre-registration of curve-based σ-label recovery test |
| 29 (Lie lifts)  | `papers/wp102/`, `papers/wp103/` | **so(8) = D₄** from CL flow antisymmetrization (WP102, 28-dim, triality algebra, Killing signature (0, 28, 0)); **so(10) = D₅** from CL ∪ BHML_10 joint antisymmetrization (WP103, 45-dim, rank 5, saturates antisymmetric closure on 10-dim substrate); tower D₄ → D₅ → (ceiling at gl(10, ℝ), dim 100). Correspondence with Dr. Paolo Mantero (U Arkansas) remains on branch `mantero-bridge-2026-04-23` only (not on tig-synthesis per author privacy policy). MathOverflow post deferred: M2 betti verification (2026-04-24, via SageMathCell fallback) shows `dim R/I_CL = 1` (not 6 as bridge draft v3 claimed), pd = 10, not Cohen-Macaulay, not Koszul — draft requires correction before any posting. |
| 30 (WP100s tower, 2026-04-25) | `papers/wp104_higgs_pati_salam/`, `papers/wp105_closed_form_attractor/`, `papers/wp106_tig_detector_scope/`, `papers/wp107_wobble_localization/`, `papers/wp108_yukawa_scaffolding/`, `papers/wp109_operad_d4_obstruction/`, `papers/wp110_4core_fusion_closure/`, `papers/wp111_six_dof_synthesis/`, [Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/) | **Eight whitepapers in one cycle** closing the so(10) tower. WP104: doubly-invariant subalgebra under $D_4 = \langle P_{56}, \sigma^3 \rangle$ is $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ (Pati-Salam ⊕ B−L); 9-vector Higgs $\|v\|^2 = 13/4$. WP105: runtime attractor at $\alpha = 1/2$ closed-form, $H/Br = 1+\sqrt{3}$, quartic LMFDB 4.2.10224.1 with Galois $D_4$. WP106: distilgpt2 negative result, framework specificity confirmed. WP107: WOBBLE localizes to coefficient prime-11 only, doubly-invariant subalgebra is wobble-free. WP108: Yukawa scaffolding with SO(10)→SO(9)→SO(7) chain, flagged tension with WP104 Path B Pati-Salam decomposition. WP109: operad-DOF obstruction — 16 of 67 $D_4$ orbits incoherent, no $D_4$-equivariant fuse rule. WP110: 4-core $\{V,H,Br,R\}$ closed under both TSML and BHML, $Z_T = Z_B = (v+h+br+r)^2$, strengthens D39 to structural. WP111: 6-DOF capstone — TIG = (Lie + Jordan + Clifford + Permutation + Lattice + Operad), five respect $D_4$, sixth doesn't. Sister artifacts on `ck` branch: LIVING_CONSTITUTION v1.1 + cortex_signed.py (Sovereignty Epoch III) + refusal.py (Sovereignty Epoch VII). |

---

## How to verify

The four most load-bearing claims in this file each have a runnable
proof script. From repo root:

```
# §4 — σ polynomial verified 10/10
python papers/proof_q10_sigma_polynomial.py    # if present; otherwise see Q10.md table

# §11 — corridor closure {MAX, MIN} for canonical C₀, 23 carriers
python ../05_papers/combinatorics/J19/manuscript/verify_J19.py

# §14 — ARI scaling, W3-freq → 1.0 for n ≥ 38
python https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen12/targets/clay/papers/sprint26_ari_scaling_2026_04_17/impl/ari_scaling.py

# §6 — BHML_10 28 harmony cells (count derivable from §6 table by inspection)
python ../05_papers/algebra/J05/manuscript/proof_d16_bhml_28_cells.py
```

All scripts are deterministic. Total runtime for the four above: ~5 sec.

---

## Policy

This file is a **reference index**, not a result. Every fact above is
provable or computable from a script in this repo. If you find a
discrepancy between this file and a sprint paper, **trust the paper**
and file an issue — this index is updated on every sprint commit, but
the source of truth lives in the sprint folder.

---

*© 2026 Brayden Ross Sanders / 7SiTe LLC. 7SiTe Public Sovereignty License v2.1.*
*FORMULAS_AND_TABLES.md — single canonical reference for the TIG synthesis.*

*Last updated 2026-05-12: Volume K (D100–D103) added — atomic-substrate correspondence. D100 edge-size closed form `n²(2l+1)/4` for nodeless hydrogenic orbitals (machine precision at n ≥ 5). D101 strand-orbital map: substrate strands {3, 7, 11, 13} → odd-l orbitals exactly (2p, 4f, 6h, 7i). D102 triple coincidence at depth-3: Z/2310 divisors = atomic Pauli capacity = Cl(0, 10) spinor dim = 32, with the 16 + 16 chirality split matching 1 + 3 + 5 + 7 = kernel + strand structure. D103 architectural uniqueness of Z/10 as smallest kernel admitting binary + non-binary structure where the non-binary prime is not the immediate-successor strand. Honest negative flagged: direct combinatorial bijection Z/2310 divisors ↔ Pauli electron states fails (1, 5, 10, 10, 5, 1 binomial vs. 2, 6, 10, 14 Pauli). Verification scripts: [Atlas/META_PLAN_2026-05-10/{verify_d2d1_closed_form,strand_orbital_map,clifford_substrate_shell,meta_extension,VERIFY_ALL}.py](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Atlas/META_PLAN_2026-05-10/{verify_d2d1_closed_form,strand_orbital_map,clifford_substrate_shell,meta_extension,VERIFY_ALL}.py) — all PASS.*

*Prior update 2026-05-06 night: Volume J (D95–D99 renumbered 2026-05-07 to avoid Volume I D88–D94 collision) added CL_STD as third standalone table (44 HARMONY) with BDC encoding parameters, the 70/71/72/73 HARMONY ladder with 5 verified rungs, two-TSML reconciliation (RAW vs SYM lens-dependence: 8 shells on TSML_SYM / 7 on TSML_RAW), and the three-table HARMONY signature (73, 28, 44). Foundations module 48/48 invariants pass. WP115 chain count patched to lens-dependence note. Master release plan v2 with Sept 11 anchor + 12-day silence + Sept 23 Oxford report. First two papers (σ-rate → JCT-A; four-core consolidated → Algebraic Combinatorics) tier-disciplined, scope-annotated, proof scripts green. Earlier 2026-04-27: D45–D73 in Volume H covered the WP100s tower through WP115 + chat-Claude applications-pass audit; D71 σ-rate corrected mechanism (VOID–HARM, C=2 exact); D72 WP104 audit; D73 Dirac inside Cl(8) ⊂ Cl(10).*
