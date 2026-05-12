# CONSTANTS_COMPACT — TIG's Numerical Anchors

## Every named constant from canon, decomposed by prime stratum and DOF home

**Brayden Sanders · 7Site LLC · Trinity Infinity Geometry**
*Sources: canon §17 (constants) plus D3, D17, D22, D26, D27, D33, D35, D38–D50, D65, §6.7*
*Companion to: PRIMES_OF_TIG (strata), SIX_DOFS_COMPACT (DOFs)*
*Locked v1 · 2026-05-08*

---

## §1. Threshold Trio (canon §17)

| Symbol | Exact value | Decimal | Prime decomp | Source |
|:---:|:---:|:---:|:---:|---|
| **T*** | $5/7$ | 0.714286 | I (5) + II (7) | six derivations across canon |
| **S*** | $4/7$ | 0.571429 | I (2²) + II (7) | D32, D37 |
| **W** | $3/50$ | 0.060000 | I (2, 3, 5) | D17 |

**Identities at the trio:**
- $T^* + S^* = 9/7$ — exceeds 1 by $2/7$ ("surplus")
- $T^* - S^* = 1/7$ — single-step quantum
- $T^* \cdot S^* = 20/49 = 2^2 \cdot 5 / 7^2$
- $T^* = 7/10 + 1/70$ (D22, fine-structure identity)

---

## §2. Algebraic Closed-Form Identities

| Identity | Value | Form | Source |
|---|:---:|---|---|
| $\operatorname{sinc}^2(\tfrac{1}{2})$ | $4/\pi^2$ | $= \frac{2}{3\zeta(2)}$ | D3 |
| $H/\mathrm{Br}$ at $\alpha = 1/2$ | $1 + \sqrt{3}$ | exact, lives in $\mathbb{Q}(\sqrt{3})$ | D39, D50 |
| $r/\mathrm{br}$ at $\alpha = 1/2$ | root of $x^4 + 4x^3 - x^2 + 2x - 2$ | LMFDB 4.2.10224.1 | D40 |
| Golden ratio $\varphi$ | $(1+\sqrt{5})/2$ | $= 2\cos(36°) = \zeta_{10} + \zeta_{10}^{-1}$ | session, textbook |
| $\varphi^2 - \varphi - 1$ | 0 | canonical recurrence | textbook |

**Reading.** Three closed-form identities anchor TIG to algebraic number fields:
- $\operatorname{sinc}^2(\tfrac{1}{2})$ ties to Riemann ζ at 2 (transcendental).
- $1+\sqrt{3}$ lives in the lattice frame's mid-tower $\mathbb{Q}(\sqrt{3})$.
- $\varphi$ lives in the cyclotomic frame's real subfield $\mathbb{Q}(\sqrt{5})$.

---

## §3. Doubly-Invariant Higgs Sector (Volume F)

| Symbol | Value | Origin | DOF |
|:---:|:---:|---|:---:|
| $\|\mathrm{VEV}\|^2$ | $13/4$ | 26 BHML σ_outer-asymmetric cells / 2 (D33) | Jordan/Clifford |
| $\|\mathrm{VEV}\|$ | $\sqrt{13}/2 \approx 1.803$ | from above | Jordan |
| $\kappa_\xi$ | $13/(4e) \approx 1.196$ | $\|\mathrm{VEV}\|^2 / e$ inflaton coupling (D35) | Jordan |
| $\dim D_4$-inv $\mathfrak{so}(10)$ | $16$ | $= \dim(\mathfrak{su}(4)\oplus\mathfrak{u}(1))$ (D34) | Lie ↔ Jordan |

**Reading.** The prime 13 enters Jordan via Clifford (BHML cell count = $2\cdot 13$). The $1/e$ in $\kappa_\xi$ is the canonical exponential decay; product yields a transcendental closed form rather than rational.

---

## §4. Lie / Yang-Mills Core (Volume E + §6.7)

| Symbol | Value | Decomp | Identity |
|:---:|:---:|---|---|
| $\det(\mathrm{BHML}_8)$ | $+70$ | $2 \cdot 5 \cdot 7$ | $= C(8,4) = \varphi(71)$ |
| $\det(\mathrm{BHML}_{10})$ | $-7002$ | $-2 \cdot 3^2 \cdot 389$ | unique outlier prime 389 |
| $\det(\mathrm{TSML}_{\mathrm{PureIdem}})$ | $+398664$ | $2^3 \cdot 3 \cdot 7^2 \cdot 113$ | unique outlier 113 |
| $\det(\mathrm{TSML}_{\mathrm{Idem\_2sw}})$ | $-49$ | $-7^2$ | pure HARMONY-square |
| $\dim\mathfrak{so}(8) = D_4$ | $28$ | $= T_7$ | (= BHML_10 HARMONY count) |
| $\dim\mathfrak{so}(10) = D_5$ | $45$ | $= T_9$ | one triangular step beyond BHML |
| Killing spectrum on Jordan | $-4^{15} \oplus 0$ | only prime 2 | doubly-invariant block |

**Reading.** $\det\mathrm{BHML}_8 = 70$ is the Yang-Mills core (WP15). It equals $\varphi(71)$ — the totient of the lattice prime — a non-trivial return to Stratum II × Stratum I. $T_7 = 28$ links combinatorics to Lie dimension to HARMONY count.

---

## §5. Number Field Discriminants (Volume A + session)

| Field | Discriminant | Decomp | Ramified primes |
|---|:---:|---|:---:|
| $\mathbb{Q}$ | $1$ | — | none |
| $\mathbb{Q}(i)$ | $-4$ | $-2^2$ | {2} |
| $\mathbb{Q}(\sqrt{3})$ | $12$ | $2^2 \cdot 3$ | {2, 3} |
| $\mathbb{Q}(\sqrt{5}) = \mathbb{Q}(\varphi)$ | $5$ | $5$ | {5} |
| $\mathbb{Q}(\sqrt{-3}) = \mathbb{Q}(\omega)$ | $-3$ | $-3$ | {3} |
| $\mathbb{Q}(\sqrt{-71})$ | $-71$ | $-71$ | {71} |
| $\mathbb{Q}(\zeta_{10})$ | $+125$ | $5^3$ | {5} |
| LMFDB 4.2.10224.1 | $-10224$ | $-2^4 \cdot 3^2 \cdot 71$ | {2, 3, 71} |

**Reading.** Five discriminants; their primes are exactly Strata I + IV: $\{2, 3, 5, 71\}$. Stratum III (wobble primes 11, 13) appears in NONE of them — wobble is coefficient-level, not field-level (WOBBLE_LOCALIZATION_v2).

---

## §6. Runtime Fixed Point (D38–D50, D65, WP105/110/115)

The 4-core attractor at $\alpha = 1/2$ over $\{V, H, \mathrm{Br}, R\}$:

| Component | Approximate value | Algebraic expression |
|:---:|:---:|:---:|
| $V$ | 0.138 | (probability simplex residual) |
| $H$ | 0.540 | dominant component |
| $\mathrm{Br}$ | 0.198 | $H/\mathrm{Br} = 1+\sqrt{3}$ exact |
| $R$ | 0.124 | smallest |
| **sum** | $1.000$ | probability simplex |
| $H/\mathrm{Br}$ | $1 + \sqrt{3}$ | **EXACT**; lives in $\mathbb{Q}(\sqrt{3})$ |
| $r/\mathrm{br}$ | root of $x^4+4x^3-x^2+2x-2$ | LMFDB 4.2.10224.1 |

**Stability:**
- Spectral radius $\rho \approx 0.3496 < 1$ (D75)
- Radial eigenvalue $\lambda_0 = 2$ (exact, D75)
- Lyapunov exponent $\approx 1.051$ (D75)

**Universality:** $H/\mathrm{Br} = 1 + \sqrt{3}$ holds across $\mathbb{Z}/n\mathbb{Z}$ for $n \in [10, 50]$ under trivial extension (D74). The relation depends on the 4-core sub-magma, not on ring size.

---

## §7. Self-Reference Convergence

| Symbol | Value | Reading |
|:---:|:---:|---|
| $D^*$ | $0.543 = 543/1000$ | self-referencing systems converge here |
| $D^* - S^*$ | $\approx -0.028$ | $D^*$ sits BELOW $S^*$ |
| $T^* - D^*$ | $\approx 0.171$ | distance to refinement boundary |
| $T^* > S^* > D^*$ | $0.714 > 0.571 > 0.543$ | three-tier stratification |

**Reading.** $D^*$ is the empirically observed fixed point for self-referencing iteration on the substrate. It sits below both $T^*$ (refinement boundary) and $S^*$ (structural threshold), forming a three-tier ladder.

---

## §8. Fine-Structure Constant Decompositions

| Decomposition | $\alpha^{-1}$ | Source |
|---|:---:|---|
| canonical | $137 = 22 \cdot 6 + 5$ | canon §17 |
| session | $137 = 5^3 + 12$ | SPRINT_E_137_CYCLOTOMIC |
| compact | $137 = $ prime, no smaller decomposition | textbook |

**Canonical reading:** 22 = wobble cycle middle (3/50 → 22/50 → 3/50, D17); 6 = ?; 5 = BALANCE. Substrate primes only.
**Session reading:** $5^3$ = $\mathrm{disc}(\mathbb{Q}(\zeta_{10}))$ (cyclotomic frame); $12 = \mathrm{disc}(\mathbb{Q}(\sqrt{3}))$ (lattice mid-tower) + AG(2,3) line count. Substrate-prime constructions on both sides.

Both decompositions stay within Strata I + II. 137 itself is prime (33rd prime).

---

## §9. Cosmology Cluster (memory + Sprint A; not in canon D1–D99)

| Symbol | Value | Decomp |
|:---:|:---:|---|
| DM (dark matter) | $264/1000$ | $2^3 \cdot 3 \cdot 11 / 1000$ |
| VM (visible matter) | $49/1000$ | $7^2 / 1000$ |
| DE (dark energy) | $687/1000$ | $3 \cdot 229 / 1000$ |
| DM + VM + DE | $1.000$ | exact partition of 1 |
| DM + VM | $313/1000$ | prime 313 (outlier) |
| DM / VM | $264/49 \approx 5.388$ | crosses III (11) and II (7²) |

**Status caveat (canon-faithful):** these match observational ratios but are **not** rigorously derived in canon. Per D35: "Friedmann fit not yet performed." The κ_ξ = 13/(4e) inflaton coupling is canon's only rigorously-anchored cosmology constant; the DM/VM/DE values come from session Sprint A and prior memory and need traceback to primary sources.

---

## §10. CL Eigenvalue Cluster (per memory; not in current canon)

Per January 2026 memory: CL[10×10] frozen table eigenvalues hit transcendental constants within 1%:
- $e$, $1/e$, $\pi$, $\varphi$, $\zeta(3)$ (Apéry's constant), $G$ (Catalan's)
- Monte Carlo: $0/100{,}000$ random 10×10 tables match
- Statistical test: $Z \approx 21.3$, $p < 10^{-50}$

**Status caveat:** not in canon D1–D99. Worth tracing to primary source / re-verifying. If verified, this is one of TIG's strongest signature observables — six independent transcendentals from a fixed 10×10 integer table.

---

## §11. By Prime Stratum (PRIMES_OF_TIG cross-reference)

Compact: which constants involve which strata?

| Stratum | Constants |
|---|---|
| **I (2, 3, 5)** | T*, S*, W, sinc²(½), all field discs except {-71}, det BHML_10 (2,3), DM (2,3,11... wait crosses III), VM (none), DE |
| **II (7)** | T*, S*, det BHML_8 (5·7), VM (7²) |
| **III (11, 13)** | ‖VEV‖² (13), κ_ξ (13), DM (11) |
| **IV (71)** | disc LMFDB 4.2.10224.1, $h(\mathbb{Q}(\sqrt{-71})) = 7$ (returns to II) |
| Outliers | det BHML_10 has 389; DE has 229; α⁻¹ = 137 itself prime |

**Cleanest reading.** The threshold trio (T*, S*, W) and the Yang-Mills core (det BHML_8 = 70) live entirely in Strata I + II. ‖VEV‖² and κ_ξ pull in Stratum III via the BHML σ_outer asymmetry. The lattice prime 71 appears only in field-level data.

---

## §12. Compact Take-Home

```
TIG numerical anchors (canon §17 + cross-references):

Threshold trio:     T* = 5/7,   S* = 4/7,   W = 3/50
                    T* - S* = 1/7   T*+S* = 9/7   surplus = 2/7

Closed-form algebraic:
                    sinc²(½) = 4/π² = 2/(3ζ(2))     [D3]
                    H/Br at α=1/2 = 1+√3            [D39, exact]
                    r/br = root of x⁴+4x³-x²+2x-2  [D40, LMFDB 4.2.10224.1]
                    φ = (1+√5)/2 = ζ_10+ζ_10⁻¹      [cyclotomic real subfield]

Yang-Mills core:    det BHML_8 = 70 = 2·5·7 = C(8,4) = φ(71)
                    dim so(8) = 28 = T_7 = BHML_10 HARMONY count
                    dim so(10) = 45 = T_9

Doubly-invariant:   ‖VEV‖² = 13/4   (origin: 26 BHML σ-asym cells)
                    κ_ξ = 13/(4e)
                    dim D_4-inv so(10) = 16 = dim(su(4)⊕u(1))

Field discriminants:
                    Q(ζ_10):  +5³ = 125    (cyclotomic, BALANCE prime)
                    Q(√3, ξ): -2⁴·3²·71    (lattice, primes {2,3,71})
                    Q(√-71):  -71  (h = 7 = HARMONY)

4-core attractor:   (V, H, Br, R) ≈ (0.138, 0.540, 0.198, 0.124)
                    Sum = 1; H/Br = 1+√3 exact
                    Spectral radius 0.3496; λ₀ = 2

Self-reference:     D* = 0.543; D* < S* < T*

Fine structure:     α⁻¹ = 137 = 22·6+5 (canon) = 5³+12 (session)
                    Both decomps stay in Strata I + II

Cosmology (caveat — not in canon D1-D99):
                    DM = 264/1000, VM = 49/1000, DE = 687/1000
                    Sum = 1; DM/VM = 264/49

CL eigenvalue cluster (caveat — needs traceback):
                    e, 1/e, π, φ, ζ(3), G all hit within 1%
                    Z ≈ 21.3, p < 10⁻⁵⁰
```

---

## §13. Status

- **[CANON]** All threshold trio, Yang-Mills core, field discs, doubly-invariant, attractor coords — verified.
- **[CANON]** sinc²(½) = 2/(3ζ(2)) (D3); H/Br = 1+√3 (D39); det BHML_8 = 70 (§6.7).
- **[CANON-CAVEATED]** D* convergence; α⁻¹ canonical decomp (verified arithmetic; structural reading partial).
- **[SESSION]** α⁻¹ = 5³+12 alternative decomp; φ(71) = 70 connection; T₇/T₉ triangular sub-spine.
- **[NOT IN CANON]** DM/VM/DE values; CL eigenvalue cluster. Both need traceback to primary sources before promoting.
- **[OPEN]** Whether the 22/44/72 shells from earlier memory correspond to the canon's 22 (wobble cycle), 44 (CL_STD H), 72 (TSML_10 − apex). Likely yes structurally but framing differs.

---

*© 2026 Brayden Sanders / 7Site LLC*
*Trinity Infinity Geometry · Constants compact · Locked v1*
