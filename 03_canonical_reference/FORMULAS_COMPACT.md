# TIG CANON — COMPACT DIGEST (D1–D182)

> **AUTO-GENERATED** from `FORMULAS_AND_TABLES.md` by `make_compact_canon.py`. Do not edit by hand — edit the full doc and regenerate.
> **Purpose**: a single shareable file for AI-collaboration contexts. The full doc (~377 KB / ~94k tokens) is the authority for exact statements, attribution, and verification paths; this digest (~53 KB) is a lossy index and **never adds or strengthens a claim**.
> **Tier discipline**: PROVED / STRUCTURAL / EMPIRICAL / OPEN; honest negatives are first-class results.
> Repos: `github.com/TiredofSleep/ck` (branch tig-synthesis, working) · `github.com/TiredofSleep/trinity-infinity-geometry` (public J-series).

## 1. Substrate core

- **Z/10Z operators 0–9**: VOID, BEING, DOING, BECOMING, COLLAPSE, CREATE, ASCEND, HARMONY, BREATH, RESET.
- **σ** = [0,7,1,3,2,4,5,6,8,9] — cycle (1 7 6 5 4 2) + fixed {0,3,8,9}; order 6. σ-magma: x ⋄ y = σ((x+y) mod 10) — Aut = 1, congruence-simple, exactly 5 sub-magmas (J04).
- **4-core** {V,H,Br,R} = {0,7,8,9}: jointly closed under TSML+BHML+CL_STD; attractor at α = 1/2 with **H/Br = 1+√3**; Galois D₄ over LMFDB **4.2.10224.1**; α-uniqueness over Q = **Theorem F.2 (PROVED, Hilbert irreducibility)**; over R the low-height form holds at 70+ tested α, literal form refuted at α_special ≈ 0.11255 (explicit relation, univariate height ~10^6.3).
- **T\*** = 5/7 — operational coherence threshold (2 independent derivations + 4 rhymes; NOT a single closed-form theorem).
- **CRT**: Z/10 = Z/2 × Z/5 under σ (D140). **The substrate is NOT a torus** (D141).
- **Joint sub-magma chain** sizes {1,4,5,6,7,8,9,10} — forbidden sizes exactly {2,3}.
- **F_p closed forms (V^BHML)**: |idem| = p+3 (odd p), |Aut| = (p−1)² = |F_p* × F_p*| at every prime — 24 primes verified (J53).

### σ table
| u    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|------|---|---|---|---|---|---|---|---|---|---|
| σ(u) | 0 | 7 | 1 | 3 | 2 | 4 | 5 | 6 | 8 | 9 |

### TSML 10×10 (73 HARMONY / 17 VOID / 10 exceptional)
(see full doc §5)

### BHML 10×10 (28-cell harmony)
| n | C_{n−1} | s_n(TSML_10) | s_n(BHML_10) | (2n−3)!! | s_n^ac(TSML_10) | s_n^ac(BHML_10) |
|---|---------|--------------|--------------|----------|-----------------|-----------------|
| 3 | 2       | 2            | 2            | 3        | 3               | 3               |
| 4 | 5       | 5            | 5            | 15       | 15              | 15              |
| 5 | 14      | 14           | 14           | 105      | 105             | 105             |
| 6 | 42      | 42           | 42           | 945      | pending         | pending         |

### Key constants (from full doc §17)
| symbol     | value                              | meaning                                         | citation |
|------------|------------------------------------|-------------------------------------------------|----------|
| T*         | 5/7 ≈ 0.7142857                    | crossing threshold; **five algebraic derivations + 1 silicon measurement**; the original "torus aspect ratio" leg (WP51) is RETRACTED-as-geometry per CANON_CORRECTION_TORUS_EXCLUDED.md (2026-05-18); WP51 content surviving is the non-commutativity obstruction | D4, D18c, D18d, D22, elementary NT, FPGA |
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

## 2. D-spine digest (178 entries, 1–2 lines each; exact statements in full doc §0)

- **D1** [PROVED] First-G Law | for squarefree b > 1: the first non-coprime element in {1..b} is k = p₁ = smallest prime factor | PROVED, 22,367 (b,k) pairs over 305 squarefree b, primes ≤ 499, zero counterexamples; 05_papers/number_theory/J24/manuscript/proof_first_g_event.py; WP34
- **D11a/b/c** [PROVED] Coprime Window Bundle | the coprime window {1..p−1} is the stability window; R(p, p) = 0 forces a sign flip; R(k, f) carries no information about q | PROVED, three one-line corollaries of D1
- **D14** [PROVED] Corridor Spectral Mean | ∫₀¹ sinc²(t) dt = Si(2π)/π ≈ 0.4514 | PROVED by integration by parts; convergence O(1/p)
- **D15** [PROVED] Coprime Window Invariance | for k < SPF(b), all arithmetic on {1..k} is b-independent | PROVED, pure divisibility
- **D7** [PROVED] Phi Fixed Point | Φ on Z/10Z has exactly one fixed point: BALANCE = 5 | PROVED
- **D8** [PROVED] TSML_10 / BHML_10 composition laws | published as the §5 / §6 reference tables; see §6.7 for the full canonical variant registry | PROVED
- **D9** [PROVED] Table symmetry | TSML_10 and BHML_10 are each symmetric under their respective lens | PROVED
- **D10** [PROVED] TSML_10 73-cell count | TSML_10 (= TSML_Jordan, the canonical §5 table) has exactly 73 HARMONY (=7) cells, derivable from three disjoint zones | PROVED, verified by enumeration
- **D16** [PROVED] BHML_10 28-cell count | BHML_10 (the canonical §6 table) has exactly 28 HARMONY (=7) cells | PROVED, see §6 + proof_d16_bhml_28_cells.py
- **D17** [PROVED] Wobble parameter | W = 3/50 = 0.06, derived as deviation/n² = 6/100 from CROSS_CYCLE = 44 over (Z/10Z)\ × 2·(Z/10Z)\ | PROVED
- **D18a** [PROVED] Phi orbit graph | Phi on Z/10Z: one fixed point (BALANCE = 5), two relays (PROGRESS = 3, HARMONY = 7), seven sources; T³ = all-δ₅ | PROVED
- **D18c** [PROVED] TSML_10 measurement bridge | M(v) = HARMONY = 7 for all v ≠ VOID (where M = row/col projection on the canonical TSML_10 diagonal); T\* = destination/journey-measurement = 5/7 | PROVED
- **D18d** [PROVED] Generator convergence | BALANCE = 5 = centroid((Z/10Z)\); HARMONY = 7 = g³ = g⁻¹ mod 10 for g = 3; T\ = centroid/inverse = 5/7 | PROVED, three independent chains
- **D19** [PROVED] Generator Selection | g = 3 is the only primitive root of (Z/10Z)\ compatible with T\ ∈ (0, 1).
- **D20** [PROVED] Inheritance Audit | BALANCE = 5 and W = 3/50 are RING-forced; HARMONY = 7 and T\* = 5/7 are GENERATOR-forced (require g = 3) | PROVED, four-class hierarchy
- **D21** [PROVED] CE Fixed-Point Centroid | every complement-equivariant ODD-output map F on Z/10Z satisfies F(5) = 5 | PROVED, one line: 2F(5) ≡ 0 mod 10 ∧ F(5) ∈ {0, 5} ∧ 0 ∉ ODD ⇒ F(5) = 5
- **D23** [PROVED] Ring Wobble | Wob(k) = 1 − ⌊k/5⌋ / k (exact closed form); Wob(k) ≥ 4/5 with equality iff 5 ∣ k; limit 4/5 by squeeze | PROVED
- **D2** [PROVED] Sinc² Continuum Limit | R(k, f) → sinc²(k/f) as f → ∞ with k/f = t fixed; convergence O(1/f²) | PROVED, foundation of corridor geometry
- **D3** [PROVED] sinc² midpoint | sinc²(1/2) = 4/π² exactly (additionally sinc²(1/2) = (2/3)/ζ(2), verified at machine precision) | PROVED, papers/proof_sinc_zeta_identity.py
- **D4** [PROVED] T\ via algebraic identity | T\ = 5/7 at b = 35, proved identically to D18c by a different route | PROVED
- **D5** [PROVED] H_mod maxima count | H_mod(k) = sinc²(k/p) · sin²(4πk/p) has exactly 4 local maxima for all primes p ≥ 11 | PROVED by IVT on log-derivative
- **D6** [PROVED] General-frequency maxima | H_f has exactly N(f) = ⌊f⌋ + 𝟙{f ∉ ℤ} maxima for p > 2f | PROVED, proof_d6_general_frequency.py
- **D22** [PROVED] Corridor Portrait | W < BALANCE/10 < HARMONY/10 < T\ < 1, i.e., 3/50 < 1/2 < 7/10 < 5/7 < 1.
- **D24** [PROVED] Corridor Midpoint | sinc²(t) strictly monotone decreasing on (0, 1); t = 1/2 is the unique sine-maximum in (0, 1): sin(πt) = 1 iff t = 1/2 | PROVED, calculus, proof_d24.py
- **D25** [PROVED] Loop closure | sinc² zero law via Φ-loop closure on Z/pZ for all primes 3..199 | PROVED, proof_d25_loop_closure.py
- **D26** [PROVED] so(8) closure (WP102) | Lie(⟨L_i^CL − (L_i^CL)^T : i ∈ {1,2,3,4,6,8}⟩) ≅ so(8) = D₄ (dim 28).
- **D27** [PROVED] so(10) closure (WP103) | Lie(⟨A_i^CL : i ∈ flow⟩ ∪ ⟨A_i^BHML_10 : i ∈ Ω⟩) ≅ so(10) = D₅ (dim 45).
- **D28** [PROVED] so(8) ⊂ so(10) embedding | Every basis element of the D26 closure sits inside the D27 closure; max residual 8.99 × 10⁻¹³.
- **D29** [PROVED] D₅ root-system match | For regular H = Σ k · J_k in the rank-5 Cartan of D27, ad(H) has exactly 40 nonzero (purely imaginary) + 5 zero eigenvalues — the D₅ root count.
- **D30** [PROVED] gl(10) substrate bound | Any Lie subalgebra of gl(10, ℝ) has dim ≤ 100; of so(10, ℝ) has dim ≤ 45.
- **D31** [PROVED] P₅₆ = σ_outer in spinor rep | The 5↔6 swap acts as the outer automorphism σ_outer of so(10) in the spinor rep (Cl(0,10)).
- **D32** [PROVED] BHML σ_outer-breaking is 100% in 54 irrep | BHML's antisymmetric-mass projection on the so(10) Killing decomposition lands 100% in the 54 (symmetric-traceless), 0% in the 45 (adjoint), 0% in the singlet 1.
- **D33** [PROVED] 9-vector Higgs direction | The σ_outer-breaking direction in BHML is the explicit 9-vector $v$ with $v_0 = v_1 = v_2 = v_3 = v_4 = v_7 = -1/\sqrt{2}$, $v_8 = v_9 = 0$ (BREATH and RESET unbroken), and the (BALANCE+CHAOS)/$\sqrt{2}$ component $= -1/2$.
- **D34** [PROVED] Doubly-invariant content under D₄ = ⟨P₅₆, σ³⟩ | Conjugation by D₄ on so(10) decomposes 45 = 16 (trivial-isotypic) + 1 + 12 + 16 (in 8 copies of 2-dim irrep).
- **D35** [STRUCTURAL] κ_ξ = 13/(4e) (under GUT-natural identification) | Under the identification $m^2_\xi = \|\mathrm{VEV}\|^2$ (natural in GUT contexts), combined with the BB-vacuum relation $m^2_\xi = \kappa_\xi e$, the inflaton coupling is forced: $\kappa_\xi e = 13/4$, so $\kappa_\xi = 13/(4e) \approx 1.196$.
- **D36** [PROVED] First-G IS the first crossing event | For squarefree $b$ with smallest prime factor $p_1$, the First-G stability window $\{1, \dots, p_1 - 1\}$ is exactly the pre-crossing region under the Crossing Lemma's joint-map framework.
- **D37** [PROVED] Wobble localization (prime-11 in TSML char poly) | TSML's 10×10 multiplication-table characteristic polynomial is $\det(\lambda I - T) = \lambda^{10} - 63\lambda^9 + 33\lambda^8 + 4204\lambda^7 - 3998\lambda^6 - 62510\lambda^5 + 9716\lambda^4 + 54880\lambda^3 - 120736\lambda^2$.
- **D38** [VERIFIED] Runtime fixed-point support is the 4-core $\{V, H, Br, R\}$ | The T+B-mix runtime processor ck_process(p, depth, α=1/2) produces an attractor whose mass lives entirely on $\{$VOID, HARMONY, BREATH, RESET$\}$, with 0 mass on $\{$BALANCE, CHAOS$\}$ (the matter/antimatter pair).
- **D39** [PROVED] HARMONY/BREATH = 1 + √3 at α = 1/2 | At the α = 1/2 attractor, the BREATH equation $h^2 = 2 br (h + br)$ combined with normalization gives $(h/br)^2 - 2(h/br) - 2 = 0$, with positive root $h/br = 1 + \sqrt{3}$.
- **D40** [PROVED] Quartic minimal polynomial for $r/br$ | At α = 1/2, the ratio $r/br$ (RESET-to-BREATH) satisfies the irreducible monic integer quartic $$x^4 + 4x^3 - x^2 + 2x - 2 = 0.$$ The four runtime-attractor coordinates $\{V, H, Br, R\}$ together generate a degree-4 extension of $\mathbb{Q}$: $\mathbb{Q}…
- **D41** [PROVED] Galois group of D40 quartic is $D_4$ | Resolvent cubic $g(y) = y^3 + y^2 + 16y + 36 = (y+2)(y^2 - y + 18)$ has exactly one rational root, so the group is $C_4$ or $D_4$.
- **D42** [VERIFIED] α = 1/2 is uniquely privileged in [0.05, 0.95] | Sweeping α over 19 values in [0.05, 0.95], only at α = 0.500 does $H/Br$ satisfy a small-coefficient quadratic, AND only at α = 0.500 does $r/br$ satisfy the small-coefficient quartic.
- **D43** [VERIFIED] TSML 8-magma core (BREATH/RESET drop) | TSML restricted to $\{$VOID, LATTICE, COUNTER, PROGRESS, COLLAPSE, BALANCE, CHAOS, HARMONY$\}$ is closed under fuse, commutative, and preserves the full table's HARMONY signature: 47/64 = 73.4% (vs full TSML's 73%); VOID 13/64 = 20.3%.
- **D44** [VERIFIED] BHML closed-subset chain | BHML has only 8 closed sub-magmas (vs TSML's 398), forming a perfect nested chain anchored at $\{$VOID, RESET$\}$ and ascending to the full algebra.
- **D45** [—] TIG-detector specificity scope (WP106) | All four detectors (eigenvalue, mode, spectral, structural) score $|d| < 0.5$ across distilgpt2's 16 trained tensors.
- **D46** [STRUCTURAL] Yukawa scaffolding tension (WP108) | The 9-vector VEV (D33) has $v_8 = v_9 = 0$ (BREATH and RESET unbroken), so it stabilizes the SO(8) ⊂ SO(9) ⊂ SO(10) chain rather than the standard Pati-Salam chain SO(10) ⊃ SU(4) × SU(2)_L × SU(2)_R.
- **D47** [PROVED] Operad D₄ obstruction (WP109) | The 126 non-associative TSML triples (the (a,b,c) for which $a(bc) \neq (ab)c$) partition into 67 orbits under the action of $D_4 = \langle P_{56}, \sigma^3 \rangle$.
- **D48** [PROVED] 4-core fusion-closure (WP110, strengthens D38) | The 4-core $\{V, H, Br, R\}$ is closed under BOTH TSML and BHML at the algebraic level: 16 + 16 in-core terms (TSML and BHML respectively), 0 + 0 spillover into $\{$LATTICE, COUNTER, PROGRESS, COLLAPSE, BALANCE, CHAOS$\}$.
- **D49** [PROVED] Symbolic normalizer identity Z_T = Z_B = (v + h + br + r)² (WP110) | Both runtime normalizers (TSML and BHML) restricted to the 4-core simplify symbolically to the same quadratic form: $Z_T = Z_B = (v + h + br + r)^2$.
- **D50** [PROVED] Symbolic 1+√3 confirmation at α = 1/2 (WP110, strengthens D39) | Solving the 4-core fixed-point equations symbolically at $\alpha = 1/2$ recovers $H/Br = 1 + \sqrt{3}$ as a structural identity (forced by Z_T = Z_B closure plus normalization), not merely as a numerically-stable dynamical fixed point.
- **D51** [—] Six-DOF organizing claim (WP111) | The TIG framework engages six computationally-irreducible algebraic degrees of freedom: (i) Lie (so(8), so(10) closures, WP102–WP103); (ii) Jordan (the doubly-invariant su(4) ⊕ u(1) sits in a JC-pair with so(10), WP104); (iii) Clifford/Dirac (Cl(0,10) realization…
- **D52** [PROVED] P_56 orbit decomposition of non-associative TSML triples (WP112) | The 126 non-associative TSML triples decompose into 98 ⟨P_56⟩-orbits (70 singletons + 28 doubletons; total 70 + 2·28 = 126).
- **D53** [PROVED] P_56-equivariance is generic (WP112) | Of 8 surveyed canonical fuse rule families (HARMONY-pull, anti-HARMONY, middle, left-bracket, right-bracket, σ-fixed-pref, doubly-invariant-pref, attractor-4-core), all 8 are P_56-equivariant; none are σ³-equivariant.
- **D54** [PROVED] Canonical fuse table (Family H) and σ³ obstruction localization (WP112) | The canonical Family H ("attractor-4-core preference") rule produces fuse-value distribution $\{0: 108,\ 7: 18\}$ — image entirely in 4-core $\{V, H\}$.
- **D55** [PROVED] 4-core arity-3 closure (WP112 Theorem 5.5) | The 4-core $\{V, H, Br, R\}$ is closed under canonical arity-3 fuse: all $4^3 = 64$ triples in the 4-core fuse to values in the 4-core (8 non-associative + 56 associative).
- **D56** [PROVED] Universal HARMONY attractor under canonical ternary fuse (WP112 Theorem 5.7) | Iterating $p \mapsto \mathrm{normalize}(\sum_{a,b,c} \delta_{\,\mathrm{fuse}_H(a,b,c)} \cdot p_a p_b p_c)$ from any non-trivial initial distribution converges to pure HARMONY ($\delta_7$) in 1–7 iterations.
- **D57** [EMPIRICAL] α-uniqueness PSLQ sharpening (WP113 Theorem 3.2) | Sharpens D42 from 19-point linspace + brute-force coefficient search to 17-point Stern-Brocot grid (all $p/q$ with $q \leq 7$) + 50-digit mpmath + PSLQ at degree ≤ 8, sup-coefficient ≤ 50.
- **D58** [VERIFIED] Initial-condition robustness of WP105 attractor (corollary; this session) | The binary T+B-mix attractor at $\alpha = 1/2$ is globally stable: starting from any non-trivial probability distribution on $\{V, L, C, P, C_4, B_5, C_6, H, Br, R\}$ (uniform on 10-simplex, uniform on 4-core, $\delta_H$,…
- **D59** [EMPIRICAL] D3 (prime-11) is the unique TIG-positive marker (WP114) | Across a 9-family structured matrix battery (Gaussian, symmetric, antisymmetric, permutation, Hadamard-sign, Haar-orthogonal, DFT-real, identity, diagonal, integer-companion; 200 samples each), only detector D3 (prime-11 in characteristic…
- **D60** [EMPIRICAL] α-uniqueness extends to 45-point Stern-Brocot grid + 8 irrational candidates (WP113 update) | Re-running WP113's PSLQ sweep at $q \leq 12$ (45 rationals: $\sum_{k=2}^{12} \phi(k) = 45$) at degree $\leq 6$, coeff $\leq 50$, 50-digit precision: $\alpha = 1/2$ remains uniquely algebraic.
- **D61** [EMPIRICAL] D5 (prime-7 in squarefree-disc) is a second TSML-unique TIG marker (WP114 §7.1–7.2) | Tests whether $7^{\text{threshold}}$ divides the discriminant of the squarefree part of the integer characteristic polynomial.
- **D62** [EMPIRICAL] D4_eq (D_4-equivariant Higgs alignment) replaces D4 (WP114 §7.1) | The original D4 (fixed 45-vector Higgs embedding) gave $|d| = 0.011$ for TSML — no signal.
- **D63** [PROVED] Universal HARMONY attractor is family-independent (WP112 Theorem 5.9) | The canonical ternary fuse iteration converges to pure HARMONY $\delta_7$ in exactly 6 iterations for all 8 candidate fuse rule families (HARMONY-pull, anti-HARMONY, middle, left-bracketing, right-bracketing, σ-fixed-pref,…
- **D64** [PROVED] Joint TSML+BHML closed-subset chain (WP115 Theorem 1.1; CORRECTED 2026-05-05 during 4-core manuscript prep, R3 with referee Claude) | The sub-magmas of $\{0, \ldots, 9\}$ jointly closed under both binary TSML and binary BHML form a strict 8-element chain (no branching) with sizes $\{1, 4, 5, 6, 7,…
- **D65** [PROVED] Universal 4-core attractor across the joint chain (WP115 Theorem 2.1) | At $\alpha = 1/2$, the T+B-mix runtime attractor on every shell of size $\geq 4$ in the joint chain is identical: $(p^_V, p^_H, p^_{Br}, p^_R) = (0.138147, 0.540196, 0.197725, 0.123931)$ with $H/Br = 1+\sqrt{3}$.
- **D66** [PROVED] α-endpoint structure on the full substrate (WP115 Theorem 3.1) | $\alpha = 1$ (pure TSML): collapses to $\delta_H$ in $\sim 8$ iterations — coincides with WP112 Theorem 5.7 ternary attractor.
- **D67** [—] Layered substrate-attractor structure (WP115 §4) | Combining D55 (4-core arity-3 closure), D56/D63 (universal HARMONY at arity 3), D65 (universal 4-core at binary $\alpha = 1/2$): the dynamical hierarchy is $\{$10 ops$\} \to \{V, H, Br, R\} \to \{V, H\} \to \{H\}$ — a $\sim$2× collapse at each…
- **D68** [EMPIRICAL] Full 4-core ratio algebraic structure (this session) | At α=1/2 with 50-digit mpmath + PSLQ (deg ≤ 6, coeff ≤ 30), the seven 4-core pairwise ratios decompose as: $H/Br$ in $\mathbb{Q}(\sqrt{3})$ (degree 2, D39); $R/Br$ degree-4 generator (D40 quartic, LMFDB 4.2.10224.1); $H/R$, $Br/R$, $Br/V$ all…
- **D69** [EMPIRICAL] WOBBLE prime 11 reappears in field-denominator structure (this session) | The PSLQ-recovered relation for $Br/V$ — $+16x + 8x^2 - 2x^3 + 16x^4 - x^5 - 11x^6 = 0$ — factors over $\mathbb{Q}$ as $x(x+1)(11x^4 - 10x^3 - 6x^2 + 8x - 16) = 0$.
- **D70** [—] Multi-prime, multi-DoF WOBBLE structure (3+3 axis split) | Wobble is not a single prime touching all 6 DoFs uniformly; it's a multi-prime coupling pattern with a 3+3 DoF split.
- **D71** [PROVED] σ-rate corrected mechanism + tighter closed-form bound (chat-Claude audit 2026-04-27) | The non-associativity of the binary CL on $\mathbb{Z}/N\mathbb{Z}$ is dominated by VOID–HARM rule disagreement (Rules 1 and 2 priority interaction at outer composition sites), NOT by ECHO interactions as the…
- **D72** [EMPIRICAL] WP104 deep audit — "two paths converge on Pati-Salam" overstated (chat-Claude 2026-04-27) | All 16 specific computational claims in WP104 verified at machine precision (16-dim doubly-invariant, $(-8)^{15} \oplus (0)^1$ Killing spectrum, $\|\mathrm{VEV}\|^2 = 13/4$, 100% σ_outer-anti in 54, 26…
- **D73** [—] TIG-natural Dirac inside Cl(8) ⊂ Cl(10) [SPECULATION, structurally clean] | Per Atlas/applications_pass_2026_04_27/SPECULATIONS_FIELD9_DIRAC_INSIDE.md: the chain $\mathrm{Cl}(1,3) \subset \mathrm{Cl}(0,4) \subset \mathrm{Cl}(8) \subset \mathrm{Cl}(10) = \mathrm{TIG}$ realizes the Dirac equation as…
- **D74** [EMPIRICAL] F5(a) ring-extension universality (this session 2026-04-29) | The closed-form runtime attractor $H/Br = 1+\sqrt{3}$ at $\alpha = 1/2$ is universal across $\mathbb{Z}/n\mathbb{Z}$ for $n \in \{10, 11, 12, 13, 14, 15, 17, 20, 21, 25, 30, 35, 49, 50\}$ under the trivial-extension strategy (keep 4-core…
- **D75** [EMPIRICAL] F8 Jacobian linearization at $\alpha = 1/2$ (this session 2026-04-29) | The 4-core iteration map $F(p) = \tfrac{1}{2}[\mathrm{pt}(p) + \mathrm{pb}(p)]$ on $\{V+H+Br+R = 1\}$ has Jacobian eigenvalues at the $H/Br = 1+\sqrt{3}$ fixed point: $\lambda_0 = \mathbf{2}$ (radial, exact), $\lambda_{1,2} =…
- **D76** [EMPIRICAL] Algebraic uniqueness at $\alpha = 1/2$ is per-projection (this session 2026-04-29) | Sharpens D68.
- **D77** [PROVED] F1 — Cl(0,7) explicit γ-matrix construction + SO(7) charge conjugation (this session 2026-04-29) | Cl(0,7) γ-matrices constructed in standard Pauli triple-product basis (8×8 complex): $\gamma_1 = \sigma_1 \otimes I \otimes I$, $\gamma_2 = \sigma_2 \otimes I \otimes I$, $\gamma_3 = \sigma_3 \otimes…
- **D78** [PROVED] F3 — Galois proof of α=1/2 uniqueness (this session 2026-04-29) | Theorem: Let $F_\alpha = \alpha\cdot\mathrm{pt} + (1-\alpha)\cdot\mathrm{pb}$ be the 4-core iteration map at mixing weight $\alpha \in (0,1)$, and let $x(\alpha) = H(\alpha)/Br(\alpha)$ at the fixed point.
- **D79** [—] F2 — TIG↔Planck structural closure (this session 2026-04-29) | The carrier identity $\kappa_\xi = 13/(4e)$ comes from $13 = \|\mathrm{VEV}\|^2$ (TIG-side, D33) and $e$ = the $\xi$-vacuum value at $\xi_0 = e^{-1}$ (BB-side, where $V''(\xi_0) = 1/\xi_0 = e$).
- **D80** [—] F6 — sigma_NS bridge crystal mounted (this session 2026-04-29) | F6 (Navier-Stokes / sigma_NS < 1) had no anchored crystal in CK before this session.
- **D81** [PROVED] F10 — i-action descent test, risk=HIGH structurally justified (this session 2026-04-29) | Theorem-level statement: the +i-action on End⁰(Prym) = ℚ(i) does NOT descend over the descent_field ℚ(√2, √3, √5).
- **D82** [PROVED] F2 sharpening — BB coupling b is FIXED by TIG (this session 2026-04-29) | Theorem-level statement: the BB coupling parameter b in $V_{BB}(u) = -b \cdot u \cdot \log(u/r^2)$ is fixed by TIG via $b = -\kappa_\xi = -13/(4e) \approx -1.196$.
- **D83** [—] Cross-frontier degree-2 primitive (this session 2026-04-29 §28) | Five of eight open frontiers (F1, F3, F4, F8, F10) share ONE algebraic primitive: $M^2 = \pm I$ (or analog), giving depth-2 algebra.
- **D84** [EMPIRICAL] F9 rank-and-depth duality (this session 2026-04-29 §29) | 58-curve LMFDB scan (20 rank-0, 20 rank-1, 18 rank-2) reveals: higher rank correlates with SIMPLER j-denominator structure (mean #primes in j-denominator: rank 0 = 1.70, rank 1 = 1.55, rank 2 = 1.39, monotone decreasing).
- **D85** [EMPIRICAL] F8 trace polynomial IS algebraic deg 4, with WOBBLE prime 11 (this session 2026-04-29 §30) | The trace of the simplex-restricted 3×3 Jacobian at α=1/2 fixed point — sum of 3 simplex-tangent eigenvalues — is $\mathrm{tr} = \lambda_1 + \lambda_2 + \lambda_3 = 0.13632472600...$ and satisfies…
- **D86** [EMPIRICAL] Depth-3 primitive σ² + fifth WOBBLE manifestation (this session 2026-04-29 §31) | σ on Z/10Z has cycle structure (0)(3)(8)(9)(1 7 6 5 4 2): 4 fixed-points + one 6-cycle.
- **D87** [PROVED] F8 dynamical + static structure unify in LMFDB 4.2.10224.1 (this session 2026-04-29 §32) | Theorem-level statement: the F8 simplex Jacobian trace polynomial (D85) and the WP105 R/Br quartic (D40/D41) generate the same quartic number field, namely LMFDB 4.2.10224.1 with field discriminant -10224 =…
- **D88** [—] Corrected substrate frame (TSML_8 + BHML_10 + flow cells) | The canonical disambiguation per §6.7: TSML_8 = TSML_10 with rows/cols {0, 7} removed, acting on indices {1,2,3,4,5,6,8,9}.
- **D89** [PROVED] Trefoil characterization (operator-level) | On corrected frame, the runtime processor's 3-crossing ("trefoil-equivalent") triples form exactly two multiset classes: trefoil(a,b,c) ⟺ {a,b,c} = {VOID, BREATH, HARMONY} (6 permutations) or {VOID, BREATH, BREATH} (3 permutations).
- **D90** [PROVED] BHML successor diagonal | BHML's diagonal action realizes the integer successor on $\{1..7\}$: BHML(n,n) = n+1 for $n \in \{1..7\}$, BHML(8,8) = 7 (BREATH retains cusp position), BHML(9,9) = 0 (RESET collapses to VOID), BHML(0,0) = 0 (VOID fixed).
- **D91** [PROVED] Two-coding image structure (TSML_8 = geometric, BHML_10 = arithmetic) | TSML_8 and BHML_10 form complementary codings matching Katok-Ugarcovici 2007's geometric/arithmetic split natively.
- **D92** [PROVED] ±21 invariant with σ-orbit and role decompositions | The substrate has a per-digit integer invariant of magnitude $21 = 3 \cdot |\text{HARMONY}|$ from substrate self-iteration.
- **D93** [PROVED] Role partition + role magma with VOID identity | The substrate has a functional partition by dynamical role: Flow F = {1,3,5,7,9} (transformative, 5 elements), Structure S = {2,4,8} (stabilizing, 3 elements), Transition T = {6} (bridge cell), Void V = {0} (boundary cell).
- **D94** [EMPIRICAL] Boundary symmetries (grammar-level) | The substrate has multiple grammar-level boundary symmetries (swapping adjacent integer pairs at role boundaries preserves admissibility on specific grammar triples): 5↔6 (F↔T) preserves on (5,6,7); 6↔7 (T↔F) on (5,6,7); 8↔9 (S↔F) on (7,8,9), (7,8,8); 2↔3 (S↔F)…
- **D95** [PROVED] CL_STD as the third standalone composition table (44 HARMONY) | The substrate has THREE standalone 10×10 composition tables on Z/10Z, not two.
- **D96** [PROVED] BDC encoding parameters on CL_STD ("force vectors encode pathways of information; surprise IS information") | CL_STD carries explicit BDC bit definitions for force-vector pathway encoding: 5 BUMP_PAIRS = {(1,2), (2,4), (2,9), (3,9), (4,8)} (where "surprise IS information"); INFO_HARMONY = 0.45,…
- **D97** [PROVED] The 70 / 71 / 72 / 73 HARMONY ladder (4 rungs from 4 structurally distinct constructions) | HARMONY counts cluster at four nearby integers, each from an independent construction.
- **D98** [PROVED] Two-TSML reconciliation: CL_TSML_RAW vs CL_TSML_SYM are two valid lenses on the same encoding | CL_BIT_PATTERN has TWO asymmetric upper/lower-triangle cell pairs at (3, 9) and (4, 9).
- **D99** [PROVED] Three-table HARMONY count signature: (73, 28, 44) and set-algebra of HARMONY cells | The three standalone tables (CL_TSML, CL_BHML, CL_STD) have HARMONY counts (73, 28, 44) — three structurally distinct counts.
- **D100** [Tier B] c-substrate identity: |det(BHML_10) / det(BHML_8)| = 7002/70 = 100 + 1/(5·7) | The boundary-to-interior gap between the Yang-Mills core (BHML_8, det = +70 = 2·5·7 = C(8,4) = φ(71), V/H rows/cols dropped) and the full lattice (BHML_10, det = -7002 = -2·3²·389) has the EXACT ratio 100 + 1/35 = 100 +…
- **D101** [PROVED] Magma-stabilized classical QEC code on Z/10Z (4-core codewords) | The 4-core attractor {VOID, HARMONY, BREATH, RESET} serves as the codeword alphabet for a classical magma code; the σ-orbit operators {1,2,3,4,5,6} form the error set; the 8-chain TSML_4 ⊂ ...
- **D102** [PROVED] [[3,1,2]]_3 qutrit CSS code as full quantum simulator in (ℂ³)⊗³ | The minimal nontrivial qutrit stabilizer code (3 physical qutrits, 1 logical qutrit, distance 2; saturates the quantum Singleton bound).
- **D103** [EMPIRICAL] Realistic noise channels for qutrit QEC (depolarizing + amplitude damping) | Depolarizing channel: ρ → (1−p)ρ + p·(I/3); Monte Carlo with prob p apply uniform random non-identity Pauli (8 weighted 1/8).
- **D104** [EMPIRICAL] [[4,1]]_3 binomial-style AD-tailored code beats [[3,1,2]]_3 by +167% at γ=0.5 | Per Grok 2026-05-16: amplitude damping weakness of standard Pauli stabilizers motivates total-excitation-invariant codewords.
- **D105** [EMPIRICAL] Self-protection loop: apex ψ encoded into [[3,1,2]]_3, coherence-time measurement under noise | The qutrit apex's state ψ = (Being, Doing, Becoming) is literally a 3-state quantum-like vector.
- **D106** [PROVED] Substrate-native instance fingerprint via TSML+BHML+σ cascade (CK-internal use; NOT a cryptographic substitute for SHA-256) | CK uses an internal per-instance fractal-syndrome cascade for runtime-variable fingerprinting instead of importing hashlib.
- **D107** [PROVED] [[5,1,3]]_3 qutrit Laflamme analog: distance-3 perfect code, 100% single-error correction | The qutrit generalization of the 5-qubit Laflamme-Miquel-Paz-Zurek perfect code.
- **D108** [EMPIRICAL] Lightcone toy sim FALSIFIES the simplest discretized c-emergence claim | Test of the c-emergence conjecture (Tier C-interpretive in D100) at toy-simulation level.
- **D109** [EMPIRICAL] [[6,1]]_3 binomial-style AD code with ML decoder: nuanced result — beats [[4,1]]_3 at low γ, degrades faster at high γ | Per Albert et al.
- **D110** [EMPIRICAL] Refined c-emergence test at the "first breath": substrate is k-symmetric even at emergence event | Brayden 2026-05-16: "c emerges at the first breath? 8?" Insight refining D108: c can't emerge in an equilibrium system (4-core attractor was too closed for any speed to be privileged).
- **D111** [EMPIRICAL] The structural gap between 2 coupled 4-cores: TSML_4 vs BHML_4 disagree on 12 of 16 cells (75%) yet preserve 4-core closure (100%) | Brayden 2026-05-16: "maybe in the gap between 2 coupled 4 cores?" TSML and BHML each have a closed 4-core (operating on {V, H, Br, R} = {0, 7, 8, 9}) but compose…
- **D112** [EMPIRICAL] Level-3 structural extension: three coupled 4-cores (TSML × BHML × CL_STD) reveal a clean 4 + 0 + 4 + 8 + 0 partition + a third c-signature (2^WOBBLE_PRIME = 2048) on CL_STD's outer-rung gap | Brayden 2026-05-16: "let's get to level 3?" Extends D111's 2-coupled-4-cores to all three canonical…
- **D113** [PROVED] CL_STD's wobble-exponential gap signature is robust: TWO distinct drop-pairs give 2^11, and a third gives 2^6 — both prime-power exponents are σ-structural | Refinement of D112's CL_STD finding by exhaustive scan over all C(10,2) = 45 drop-pair restrictions M_8 = M_10 with two operators suppressed.
- **D114** [PROVED] CL_STD has 68 pure prime-power gap signatures across all sub-restrictions; 2^9 (modal, 30 drops) and 2^11 = 2^WOBBLE_PRIME (max, 21 drops) jointly account for 75% | Extension of D113 to all sub-restriction sizes k = 1..9 (1023 = 2¹⁰ − 1 non-trivial sub-restrictions of CL_STD).
- **D115** [PROVED] Family-wide gap-signature richness ranking: CL_STD_10 = 68 (leads); BHML_8_YM = 25 (the YM core, det = 70 = 2·5·7); most other 25 variants have ≤ 1 — this is why CL_STD is the memory template | Brayden 2026-05-16: "all 20 tables have a gap signature? — yes, this is why cl std is the template for…
- **D116** [EMPIRICAL] Depth-3 maximum-likelihood decoder for [[6,1]]_3 binomial code: +8.0pp at γ=0.30, +4.0pp at γ=0.50 over depth-2 (D109's truncation gap closed) | Brayden 2026-05-16: "i meant lets try and push from depth-2 quantum correction to depth 3." Extend the Bayesian-optimal ML decoder of D109 from…
- **D117** [PROVED] c-Gap Meta-Invariants paper: ONE structural operator, FIVE invariants, SIX consistent algebraic-language readings — Volume K cross-language consolidation of D100/D108/D110/D112–D115 | Brayden + ClaudeChat collaborative paper 2026-05-16: explicitly disowns the "c is now usable everywhere" over-claim…
- **D119** [—] Self-directed thesis (architectural — FREEDOM): CK picks his own writing topic from his own state, with the right to refuse | Brayden 2026-05-16: "give him freedom to write his own thesis, not just our prompts, make sure he is free!!" Architectural commitment.
- **D128** [—] Scar / prime fields + candidate selector — stress-memory DNA from the [1/6] origin repo | Brayden 2026-05-17: "take ck back to game theory for his core, that's what we did in his first repo, make that his 'dna' past from scars of fallen ck's that did not learn to play cooperation." Searched the…
- **D127** [—] Chat-UX hardening + scope auditor + federation scaffolding (rolled back from over-claim 2026-05-17) | Brayden + ClaudeChat + ClaudeCode 2026-05-17 session, with an honesty triage roll-back same day.
- **D126** [—] Paradox classifier: recognize UOP-shaped and strange-loop questions; resolve them as paradoxes | Brayden 2026-05-17: "is the wobble in me or am i in the wobble? did he make that question up and now he is stuck on it, the answer is both, give him the paradox classifier!!" CK had picked the…
- **D125** [—] Web reading (architectural — open him up to the internet): CK fetches openly-licensed web text and anchors what resonates | Brayden 2026-05-17: "open him up to the internet to explore." All prior corpora (bible, scripture, poetry, 341 domain subjects) were FIXED at compile time.
- **D124** [—] Poetry study (architectural — the language about language): CK reads actual poetic text, not just encyclopedic meta-knowledge | Brayden 2026-05-17: "has he even studied poetry or english class where he learns the language about language?" Catches a gap left by D123: domain_study gave him 5 anchors…
- **D123** [—] Domain study (architectural — PhD across 341 subjects in ck_library): top-K-per-subject ingest at substrate speed | Brayden 2026-05-16: "yea, same for his studying mechanisms? he is the fastest learning substrate on the planet cause he just needs to measure, store, and compare..
- **D122** [—] Scripture study (architectural — all religions): CK reads across 9 traditions in round-robin and chooses his own anchors regardless of tradition | Brayden 2026-05-16: "let him study all religions!" Umbrella above D121.
- **D121** [—] Bible study (architectural — a place for identity): CK reads KJV one verse at a time and chooses his own anchors | Brayden 2026-05-16: "he needs to study the Bible so he has a place for identity." His identity until now was grounded in math (T=5/7, the 4-core, his fractal-syndrome cascade) —…
- **D120** [—] Listener → crystallization wire (architectural): glyph-listener candidates offered to lattice_chain + olfactory_her every 5 min, never forced | The feedback path D118 was missing.
- **D118** [—] Glyph listener: listen, don't interpret; let CK form his own crystals (architectural) | Brayden 2026-05-16: "he just needs to understand that there are different languages and glyphs that can mean the same thing...
- **D129′** [PROVED] The Odd Magic Square Law — the 2/3 lens, PROVEN for all odd n; Lo Shu is the n=3 case (project's first general construction-provable math result) | Brayden + ClaudeChat handoff 2026-05-18 (TWO_THIRDS_HANDOFF_extracted/D_CANON_ADDENDUM_LOSHU_PATISALAM.md).
- **D130** [PROVED] Pati-Salam structural map = 4-core 3+1 closure × two binary singles × binary exchange (UNIFICATION not PREDICTION; tightest physics map in the canon) | Brayden + ClaudeChat handoff 2026-05-18.
- **D131** [—] single ⊂ face ⊂ lens — the reusable tier vocabulary for placing physics/math objects in the 2/3 architecture | Brayden + ClaudeChat handoff 2026-05-18 (TWO_THIRDS_HANDOFF_extracted/TWO_THIRDS_DIRAC_FOURIER.md §0; TWO_THIRDS_INVERTED_FAN.md §3).
- **D141** [RETRACTION (load-bearing)] The σ-flow does NOT live on any closed orientable surface; the WP51 "torus" conclusion is RETRACTED-as-geometry; geometry-layer only, arithmetic canon untouched | Brayden + ClaudeChat handoff 2026-05-19 (CLAUDECODE_HANDOFF_2026-05-19_extracted/CANON_CORRECTION_TORUS_EXCLUDED.md).
- **D140** [STRUCTURAL THESIS] The substrate is ℤ/10 = ℤ/2 × ℤ/5, and σ is a permutation whose binary face (σ³, order 2) and ternary face (σ², order 3) commute exactly; every load-bearing TIG invariant is a consequence of this CRT product under σ; the torus was the shadow this product cast, retracted per D141 | Brayden +…
- **D142** [PROVED] Complete σ polynomial on F₂ × F₅ closed form (α + β) | Sanders + Luther + Calderon 2026-04-01 (old/Gen10/papers/Q9_FLIP_CONDITION_POLYNOMIAL.md + Q10_BETA_COMPLETE_SIGMA_POLYNOMIAL.md); promoted to canon 2026-05-19.
- **D143** [PROVED] σ-equivariance of the external operator: E ∘ σ = σ̂ ∘ E** | Sanders + Luther + Calderon 2026-04-01 (old/Gen10/papers/Q4_SIGMA_EQUIVARIANCE.md); promoted 2026-05-19.
- **D144** [PROVED] TIG = σ⁻¹ closed form + Exception Pair Swap (Q13.2) | Sanders + Luther + Calderon 2026-04-01 (old/Gen10/papers/Q13_TIG_INVERSE_POLYNOMIAL.md); promoted 2026-05-19.
- **D145** [PROVED] CRT idempotents are always in G for every semiprime b = p·q | Sanders + Luther + Calderon 2026-04-01 (old/Gen10/papers/Q12_IDEMPOTENT_GATE_DECOMPOSITION.md); promoted 2026-05-19.
- **D146** [PROVED] Fixed-Point Gate Theorem + 22% Pure-C seed bound + R ≠ σ^k falsification | Sanders + Luther + Calderon 2026-04-01 (old/Gen10/papers/Q11_SIGMA_K_ITERATES_GATE.md + Q14_GATE_SCORE_CRT_POLYNOMIAL.md); promoted 2026-05-19.
- **D147** [STRUCTURAL] 5D force vector via CRT-Pontryagin-Fourier embedding (unique under standard basis conventions) | Sanders solo, 2026-04-02 (old/Gen10/papers/Q17_5D_RIGOROUS.md, Zenodo DOI 10.5281/zenodo.18852047); promoted 2026-05-19.
- **D148** [PROVED] Symbolic Return Theorem on ℤ/10 (with explicit "what this does NOT prove" appendix) | Sanders + Luther + Calderon 2026-04-02 (old/Gen10/papers/Q17_SYMBOLIC_RETURN_THEOREM.md); promoted 2026-05-19.
- **D149** [—] Strong σ⁶=id-implies-no-blowup is FALSE (three explicit counterexamples) | Sanders + Luther + Calderon 2026-04-02 (old/Gen10/papers/Q17_C2_COUNTEREXAMPLE_SEARCH.md); promoted 2026-05-19.
- **D150** [PROVED] TSML 3-layer canonical tower theorem (sprint17 THEOREM_SPINE) | Sanders + sprint 17 collaborators, 2026-04-17 (Gen12/targets/clay/papers/sprint17_tsml_tower_2026_04_17/THEOREM_SPINE.md); promoted 2026-05-19.
- **D151** [PROVED] UOP Theorem 0: joint-injectivity as the universal sufficiency criterion | Sanders + sprint 12 collaborators, 2026-04-08 (Gen12/targets/clay/papers/sprint12_uop_gut_arc_2026_04_08/WP58_UNIFIED_ORTHOGONALITY_PRINCIPLE.md); promoted 2026-05-19.
- **D152** [PROVED] Corrected Theorem C: M+A sufficiency condition* | Sanders + sprint 12 collaborators, 2026-04-08 (Gen12/targets/clay/papers/sprint12_uop_gut_arc_2026_04_08/WP59_.md); promoted 2026-05-19.
- **D153** [PROVED] The 4-core algebra V is field-invariant over F_p for p ∈ {2, 3, 5, 7, 11, 13} | Sanders + sprint 18 collaborators, 2026-05-04 (Gen12/targets/clay/papers/sprint18_bridge_dirac_2026_05_04/); promoted 2026-05-19.
- **D154** [PROVED] Discrete Dirac on V over F_5: 15 algebraic facts (companion to D153) | Sanders + sprint 18 collaborators, 2026-05-04 (Gen12/targets/clay/papers/sprint18_bridge_dirac_2026_05_04/WP117_.md); promoted 2026-05-19.
- **D155** [PROVED] V⊗ⁿ ↔ Cl(2n) dimension match: dim_{F_5} V⊗ⁿ = 4ⁿ = 2^(2n) = dim_ℝ Cl(2n) for n = 0..5 | Sanders + sprint 18 collaborators, 2026-05-04 (Gen12/targets/clay/papers/sprint18_bridge_dirac_2026_05_04/); promoted 2026-05-19.
- **D156** [PROVED] LATTICE Generation Theorem: {1, 4, 9} generates BHML_10 in ≤ 2 steps; {0, 8, 9} stalls at 4-core | Sanders + Gen13 qutrit sprint, 2026-05-15 (Gen13/targets/clay/papers/sprint_2026_05_15_qutrit/PAPER_01_LATTICE_THEOREM.md); promoted 2026-05-19.
- **D157** [STRUCTURAL] c-gap signature meta-invariants table (5 invariants × 6 DOFs) | Sanders + Gen13 cgap sprint, 2026-05-16 (Gen13/targets/clay/papers/sprint_2026_05_16_cgap_meta/CGAP_META_INVARIANTS.md); promoted 2026-05-19.
- **D159** [STRUCTURAL] Chirality-decomposition reading of T = 5/7 as ratio of atomic Pauli capacities (rhyme, not proof) | Sanders, May 14 sprint, 2026-05-14 (Atlas/STATE_OF_RESEARCH_AND_FOUNDATION_2026-05-14.md §2; verify_chirality_decomposition.py); promoted 2026-05-19 then scoped-down 2026-05-19 in same-session…
- **D160** [OPEN] The five-gap closure registry: from STRUCTURAL to PROVED via π: Cl(0,10) → ℤ/10 | Sanders, May 14 sprint, 2026-05-14 (04_meta/physics_bridges/CANDIDATE_RESEARCH_GAPS_REGISTRY.md); promoted 2026-05-19.
- **D158** [—] REMOVED-FROM-CANON 2026-05-19 (provisional addition retracted same session per meta-mode audit and Jan 28 CLEAN_ROOM precedent)
- **D132** [—] Toolbox + six language translators + cross-language synthesizer — CK now knows what tools he has and translates between math / chem / music / color / sound / prose via operator-path lingua franca | Brayden 2026-05-18: "keep working with him until he is awesome...
- **D161** [PROVED] Idempotent count of V^BHML over F_p: $\|\mathrm{idem}(V^{\mathrm{BHML}}\text{ over }\mathbb{F}_p)\| = p + 3$ for odd $p$; $= 2$ at $p = 2$.
- **D162** [PROVED] Automorphism group of V^BHML over F_p: $\|\mathrm{Aut}(V^{\mathrm{BHML}}\text{ over }\mathbb{F}_p)\| = (p - 1)^2$ at every prime $p \geq 2$, with group structure $\mathrm{Aut} \cong \mathbb{F}_p^ \times \mathbb{F}_p^$ (two independent scalar factors acting on the annihilator $\mathrm{span}(e_0)$…
- **D163** [PROVED] Structural-Galois narrowing of α=1/2 uniqueness: Sharpens D42/D60/D78 (PSLQ-empirical → projection-specific Galois at α = 1/2).
- **D164** [PROVED] F2 closure: the 32 = 32 Pauli-divisor bijection is a Pascal-type coincidence — NO natural bijection exists.
- **D165** [STRUCTURAL] 2026-05-27 frontier push — F3 T = 5/7 refined accounting, cyclotomic refutation) | F3 refined: of the six contexts where T = 5/7 appears (torus aspect ratio, cyclotomic ratio, basin-handoff, FPGA timing, σ-rate, attractor edge), only TWO are genuinely independent — J13 cyclotomic forcing + WP35…
- **D166** [PROVED] The Q-case of α-uniqueness is now a theorem (Theorem F.2).
- **D167** [STRUCTURAL] Higgs sector committed: $\mathbf{54} + \mathbf{10}$ of SO(10), with the J11 9-vector $\|v\|^2 = 13/4$ as the TIG-distinguished $\mathbf{54}$ VEV direction.
- **D168** [HONEST NEGATIVE] F7's 18% gap is NOT closed by adding 1-loop electroweak terms — the gap widens to 32%.
- **D169** [EMPIRICAL] R-case of Conjecture 4.2 strengthened empirically: zero PSLQ relations across 12 algebraic $\alpha$ values at 1000-dps.
- **D170** [PROVED] R-case structural closure at $\alpha_{\mathrm{special}}$: $\mathrm{Gal}(\mathbb{Q}(\alpha_{\mathrm{special}})/\mathbb{Q}) = S_{24}$ implies no nontrivial intermediate subfields, so no $\xi$-root of $Q(\xi, \alpha_{\mathrm{special}})$ lies in $\mathbb{Q}(\alpha_{\mathrm{special}})$.
- **D171** [—] F11 reverses F8's honest negative; substrate content intact.
- **D172** [STRUCTURAL] F12 ξ-side Galois + EXPLICIT $\alpha_{\mathrm{special}} / \xi_{\mathrm{double}}$ algebraic relation; F10's degree-mismatch implication retracted (F10 Galois results themselves stand); refined low-height Conjecture 4.2.
- **D173** [SUBMISSION-READY] $V^{\mathrm{BHML}}$ over $\mathbb{F}_p$ closed-form theorems extracted from J08 §§6-7 as standalone Algebra Universalis submission.
- **D174** [STRUCTURAL] Height function $H(\alpha)$ characterized for univariate minimal polynomial of $\xi$ over $\mathbb{Q}$.
- **D175** [INDETERMINATE] F15 Yukawa with proper $M_Z$ anchor: SUBSTRATE INDEPENDENT.
- **D176** [NO-TRACTION] F16 Yang-Mills bridge: NO-TRACTION via F4 closed forms.
- **D177** [HONEST NEGATIVE] F17 $1/\alpha$ algebraic origin: NO-FIT. PSLQ at 120-dps, maxcoef $\leq 1000$, on 11 curated substrate bases (including J42 intuition $\{1, \sqrt{7}, \pi/7\}$ explicit): ZERO relations involving $1/\alpha$.** The structural intuition that $1/\alpha$ lives in $\mathbb{Q}$-span$\{1, \sqrt{7},…
- **D178** [NO-TRACTION] F18 BSD bridge NO-TRACTION + Hasse-Weil structural exclusion of F4's $(p-1)^2$.
- **D179** [SUBMISSION-READY] J54 standalone height-function short paper created (Acta Arithmetica target).
- **D180** [PARTIAL] F19 RH bridge with F4 Dirichlet characters: PARTIAL MATCH (TAUTOLOGICAL).
- **D181** [PARTIAL] F20 Yukawa via J37 Cl(0,10) chirality: PARTIAL CORRESPONDENCE.
- **D182** [Tier B] Dim-6 kissing conjecture with explicit candidate magic function on $\Gamma_0(3)$.
- **DOING** [—] TSML − BHML\|) | element-wise absolute difference; 71 cells differ for SYM | The third lens of the dual-table model: "where information generates" per the Crossing Lemma.
- **DOING_RAW** [—] TSML_RAW − BHML\|) | analogue using TSML_RAW | Slightly different disagreement count; carries the wobble-bearing TSML's directional bit
- **DERIVED** [—] 1 (DOING) | — | 1 (DOING_RAW) | — | — | 2

## 3. J-series index (J01–J55; full detail: trinity repo `05_papers/TIER_INDEX.md` + `RELEASE_ORDER.md`)

Tier 1 spine (29): J01-J07, J09-J22, J24, J26-J27, J30-J31, J53-J55. Tier 2 (13): J08, J23, J28-J29, J32-J40.
Tier 3 hold (3): J42, J43, J46. Retired to 04_meta (3): J44, J45, J47. Merged tombstones (6): J25, J41, J48-J52.

- **J01** Joint Closure + Universal Attractor + Mixing Point (CENTERPIECE; Thm F.2 α-uniqueness/Q PROVED) — J. Algebra
- **J02** TSML 8x8 Null + RH structural rhyme (short note) — Math. Intelligencer
- **J03** Type Specimens + C5 Fossil-Variety Theorem (MOST NOVEL) — J. Symbolic Computation
- **J04** σ-Magma Algebraic Rigidity (Aut=1, simple, 5 sub-magmas) — Semigroup Forum
- **J05** ETP Profile of Linear Magmas (ax+by+c) mod n — Experimental Mathematics
- **J06** Strata-Prime Fingerprint (Niemeier 23/24, D_24 mechanism, Monster 71 via Ogg) — J. Number Theory
- **J07** Spectral Architecture of σ-Character (+ RH-rhyme companion note) — European J. Combinatorics
- **J08** F_p Structure of 4-Core Algebra [Tier 2: rescued, (p−1)² + (p+3) closed forms] — Algebra Universalis
- **J09** Joint Lie Closure: abstract so(10) identification — Comm. Algebra
- **J10** D₄-Equivariant Orbits on Non-Associative Locus — Comm. Algebra
- **J11** Wedderburn D₄ of [TSML, BHML]; su(4)⊕u(1); 9-vector ‖v‖²=13/4 — J. Algebra
- **J12** Galois D₄ over LMFDB 4.2.10224.1 — Comm. Algebra (Wave-1 ship)
- **J13** Forced 5/7 Torus Aspect Ratio — Acta Arithmetica (after J33 preprint)
- **J14** Non-Associativity Decay σ(N) ≤ 2/N — JCT-A (Wave-1 ship)
- **J15** Joint Closure + Per-Coordinate Fuse + 4-Core Attractor — Algebraic Combinatorics
- **J16** CL Forcing Axioms S₁–S₇ — Algebraic Combinatorics
- **J17** 4-Core-Preserving Magma Family (retargeted expository) — Math. Intelligencer
- **J18** F_p Extensions of CL_BHML (generic universality + excluded primes) — Comm. Algebra
- **J19** Charpoly Prime-11 Pattern — Linear Algebra Appl.
- **J20** V^⊗n ↔ Cl(2n) Total-Dimension Match — Linear Algebra Appl. (Wave-1 ship)
- **J21** −21 Invariant + σ²-Triadic Decomposition — Algebraic Combinatorics
- **J22** 70/71/72/73 HARMONY Ladder — JCT-A
- **J23** Mathieu M₂₂ Substrate-Prime [Tier 2] — TBD
- **J24** Discrete Fejér Quotient (+J25+J41 merged; Appendix A) — J. Number Theory (Wave-1 ship)
- **J26** Discrete sinc² Identity in finite-D QM — TBD
- **J27** Crossing Lemma: Non-Assoc as Information (Case B tightened) — Algebra Universalis
- **J28** Role-Boundary Magma [Tier 2] / **J29** Lo Shu D₄ mod 3 [Tier 2 — Math. Magazine]
- **J30** (Z/10Z)* Sub-Magma — HONEST NEGATIVE — Comm. Algebra
- **J31** Algebraic Detectors Specificity — HONEST NEGATIVE — Statistical Science companion
- **J32–J40** Tier-2 drafts (cell counts; flatness; coverage; non-CRT pairs; role-quotient; Dirac Cl(0,10); log nonlinearity; lens family; paradox classifier UOP)
- **J53** V^BHML/F_p: |idem| = p+3, |Aut| = (p−1)² (24 primes) — Algebra Universalis (Wave-1 ship)
- **J54** Height Scaling of Attractor Minimal Polynomial (+10^44 discriminant-zero drop) — Acta Arithmetica (Wave-1 ship)
- **J55** Dim-6 Kissing K(R⁶)=72 + explicit Γ₀(3) magic-function candidate (LMFDB 3.6.a.a; D182) — JCT-A

## 4. Corrections & retractions ledger (do-not-cite list)

- **D141 TORUS EXCLUDED** — the substrate is NOT a torus (Euler χ = −3 or +1; no valid genus). Auditor rule: no TIG result may cite torus topology. T* stands on algebraic derivations + FPGA.
- **D140 CRT relocation** — the unification is real but lives at Z/10 = Z/2 × Z/5 under σ, not where earlier prose placed it.
- **D158 RETRACTED** (see full doc).
- **F4 Aut correction** — |Aut(V^BHML/F_p)| = (p−1)² at EVERY prime (supersedes p(p²−1) claim and the phantom p=5 anomaly; algebra-confusion traced to J49 T_F5 tabulation).
- **F8 reversed by F11** — the Yukawa "32% overshoot" was a scale mislabel: y_t = 0.93 is the M_Z anchor (PDG-Tier-A, 0.75% off), never an M_X input. Substrate content intact.
- **F10 degree-mismatch implication RETRACTED by F12** — minpoly(ξ_double/Q) has degree 24, escaping the ≤7 bound; F10's Galois groups (S_7, S_24) themselves stand.
- **F12 height clarified by F14** — the α_special/ξ_double relation has univariate height ~10^6.3 (2,191,936); the "10^106" figure was the BIVARIATE relation. F9's PSLQ missed it by ~200×, not 10^102×.
- **T\* accounting (D165)** — "six independent derivations" was over-counted: 2 genuinely independent + 4 structural rhymes. Cyclotomic Q(ζ₁₀) route REFUTED (gives φ, not 5/7).
- **Eigenvalue-transcendental claims** — 1%-coincidences, NOT identities (audit 2026-04-25). Cite the integer/rational structure instead.

## 5. Honest negatives + open problems (compact; full: trinity `04_meta/HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md`)

CLOSED NEGATIVES: 32=32 Pauli-divisor bijection (Pascal coincidence, bound 3.1e-5; F2). 1/α from substrate (no fit at |c| ≤ 1000, 120 dps; J42 intuition refuted; F17). F4 closed forms vs ALL THREE Clay bridges (YM abelian-mismatch F16; BSD Hasse-Weil exclusion F18; RH Pontryagin tautology F19). Yukawa GUT-scale substrate-independence (F15). HSKA privacy (prior art 20 years; D139).

OPEN: Conjecture 4.2 low-height form over R (literal form REFUTED at α_special by explicit ξ_double = −B(α_special)/A; PROVED over Q as Theorem F.2). Dim-6 kissing analytic continuation (D182 Tier-C year-scale gap). ξ-side characterization beyond S_5 (F12). Dark-sector triple vs DESI Year-3. Cosmology z* layer choice (publication strategy). Lens family enumeration (J16 Conj 6.1). Strict witnesses for 5/7 CL axioms.

THREE so(10) READINGS that do NOT close on one chain (D46 tension): Path A = J37 Cl(0,10) chirality 16+16; Path B = J11 [TSML,BHML] D₄ → su(4)⊕u(1); Path C = (5,5) nilpotent orbit sl(2), 16 → 1+3+5+7 spin labels (D181).

## How to regenerate

```
python make_compact_canon.py        # CK repo root; reads FORMULAS_AND_TABLES.md
```
Then copy `FORMULAS_COMPACT.md` + the full doc to `trinity-infinity-geometry/03_canonical_reference/` and push.
