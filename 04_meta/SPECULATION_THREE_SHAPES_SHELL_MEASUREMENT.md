# SPECULATION_THREE_SHAPES_SHELL_MEASUREMENT

## Three orthogonal shape measures for hydrogenic shells, mapped to TIG measurement framework

**Status: SPECULATIVE / Tier C / clean computation, partial TIG match**

**Companions**:
- `SPECULATION_ELECTRON_BLACK_HOLE_BRIDGE.md` (electron-as-boundary-gate)
- `SPECULATION_SHELL_FISHER_INFORMATION.md` (substrate primes ↔ odd-l multiplicities)

**For ClaudeCode**: this doc proposes three independent shape measures that together characterize each hydrogenic shell. One is standard physics (edge size). Two are non-standard (intrinsic bump arc, tunneling fraction). The intent is to have a measurement framework that (a) confirms Brayden's "edge widening" intuition with rigor, (b) adds shape information beyond what `<r>` alone captures, (c) provides a σ-rate-like decay measure to test against TIG's σ(N) ≤ 2/N.

Locked 2026-05-08.

---

## §0. The three shapes

For each hydrogenic shell (n, l), define three independent measures of the radial probability density ρ(r) = r²|R_{n,l}(r)|²:

**SHAPE 1 — EDGE SIZE** (outer boundary sharpness)
```
edge_size(n, l) = 1 / I_r(n, l)
where  I_r = ∫₀^∞ (dρ/dr)² / ρ(r) dr   (Fisher information)
```
Brayden's intuition: outer shells have looser edges. Edge size grows with shell.

**SHAPE 2 — BUMP ARC** (intrinsic interior shape)
```
bump_arc(n, l) = arc_length[(u, ρ_norm) restricted to ρ_norm > 0.01] - (u_right - u_left)
where  u = r/<r>,  ρ_norm = ρ(r)/ρ_max
```
Arc length of the normalized density curve over its support, MINUS the support length itself. Isolates how much the curve "wiggles" beyond a flat line. A pure delta gives 2; a flat line gives 0.

**SHAPE 3 — TUNNELING FRACTION** (σ-rate analog)
```
tunnel(n, l) = ∫_{r_+}^∞ ρ(r) dr
where  r_+ = n² + n·√(n² - l(l+1))   (outer classical turning point)
```
Probability the electron is found beyond the classical extremum. Decreases with shell — analog of TIG's σ(N) ≤ 2/N decay.

These three shapes are independent: edge size grows monotonically with shell, bump arc varies by node count within shell, tunneling fraction decays with shell. Together they give a 3D characterization of "what an electron shell looks like."

---

## §1. Computed values (Z=1, atomic units)

```
shell    <r>     edge=1/I_r   bump_arc   tunnel
 1s      1.48      0.2506      0.8530    0.23810
 2s      6.00      1.0002      1.3512    0.18551
 2p      5.00      3.0001      0.8960    0.18923
 3s     13.50      2.2503      1.8309    0.15978
 3p     12.50      4.0500      1.5904    0.16018
 3d     10.50     11.2500      0.9523    0.16771
 4s     24.00      4.0004      2.2822    0.14373
 4p     23.00      6.0000      2.1240    0.14383
 4d     21.00     10.0000      1.7521    0.14499
 4f     18.00     28.0000      1.0029    0.15503
 5s     37.50      6.2505      2.7082    0.13245
 5p     36.50      8.5227      2.5929    0.13248
 5d     34.50     12.0192      2.3318    0.13284
 5f     31.50     19.8864      1.8762    0.13468
 5g     27.50     56.2500      1.0466    0.14646
 6s     54.00      9.0006      3.1123    0.12393
 6h     39.00     99.0000      1.0843    0.14019
 7s     73.50     12.2507      3.4985    0.11719
 7i     52.50    159.2500      1.1173    0.13535
```

(Full table for n=1..7 in `three_shapes_shell_measurement.py`.)

---

## §2. What's clean — Shape 1 (edge size)

**For s-orbitals (l=0):** edge_size = n²/4 EXACTLY.
```
1s: 0.25 = 1/4
2s: 1.00 = 4/4
3s: 2.25 = 9/4
4s: 4.00 = 16/4
5s: 6.25 = 25/4
6s: 9.00 = 36/4
7s: 12.25 = 49/4
```

**For max-l (nodeless) orbitals:** edge_size grows steeply.
```
1s: 0.25 = 1/4
2p: 3.00
3d: 11.25 = 45/4
4f: 28.00
5g: 56.25 = 225/4
6h: 99.00
7i: 159.25 = 637/4
```

The 1/4 prefactor and n² scaling are textbook hydrogenic Fisher information.

**TIG comparison**: the 4 in the denominator is suggestive (4-core {V, H, Br, R}, Braiding Fractal Axiom 7), but n²/4 is forced by Bohr scaling alone. No TIG-specific signature found in shape 1 beyond what's already in `SPECULATION_SHELL_FISHER_INFORMATION.md` (substrate primes ↔ odd-l multiplicities).

---

## §3. What's clean — Shape 2 (bump arc)

**Nodeless shells (l = n−1, single peak, no internal nodes):**
```
1s: 0.853
2p: 0.896
3d: 0.952
4f: 1.003
5g: 1.047
6h: 1.084
7i: 1.117
```
Slowly approaching a limit. Crosses 1.000 at n=4 (4f). Increment per shell: ~0.04, decreasing.

**s-orbitals (l = 0, maximum nodes = n−1):**
```
1s: 0.853   (0 nodes)
2s: 1.351   (1 node)
3s: 1.831   (2 nodes)
4s: 2.282   (3 nodes)
5s: 2.708   (4 nodes)
6s: 3.112   (5 nodes)
7s: 3.499   (6 nodes)
```
Each new node adds ~0.4-0.5 to the bump arc. Specifically, increments: 0.50, 0.48, 0.45, 0.43, 0.40, 0.39 — slowly decreasing.

**Per-node excess** (bump_arc - nodeless_arc) / n_nodes within each shell:

The per-node arc contribution is NOT constant across (n, l). For n=7:
- l=5 (1 node):  excess/node = 0.945
- l=4 (2 nodes): excess/node = 0.755
- l=3 (3 nodes): excess/node = 0.631
- l=2 (4 nodes): excess/node = 0.538
- l=1 (5 nodes): excess/node = 0.462
- l=0 (6 nodes): excess/node = 0.397

The first node added contributes the MOST; subsequent nodes contribute less. This is non-trivial structural information about how nodes pack into the orbital.

**TIG comparison attempted**:
- Per-node excess at the first-added node (l = n-2, 1 node) approaches 1 from below: 0.455, 0.638, 0.749, 0.830, 0.893, 0.945 across n=2..7. Asymptote unclear; could be 1 (saturation), could be (1+√3)/2 ≈ 1.366 ÷ something, could be something else.
- Nodeless asymptote (n→∞) appears to approach somewhere in [1.2, 2.0] — would need n=20+ to pin down. Candidates 4/π² + 1 ≈ 1.405, T* + 1/2 = 17/14 ≈ 1.214, 1+sqrt(3)/2 ≈ 1.866, or simply 2 (for a delta-function limit).

**No clean TIG match yet.** The shape information is real and non-standard, but the asymptotic constants don't snap to a TIG-significant number from §17 of `FORMULAS_AND_TABLES.md`. Open structural frontier.

---

## §4. What's NOT clean — Shape 3 (σ-rate analog)

**Tunneling fraction for s-orbitals:**
```
n=1: 0.23810
n=2: 0.18551
n=3: 0.15978
n=4: 0.14373
n=5: 0.13245
n=6: 0.12393
n=7: 0.11719
```
Monotone decreasing. Right qualitative shape for σ-rate analog.

**Power-law fit:** log(tunnel) = -1.434 - 0.365 log(n), so:
```
tunnel ≈ 0.238 · n^(-0.365)
```

**TIG comparison**: TIG's σ-rate is σ(N) ≤ 2/N — slope -1 in log-log. Observed slope is **-0.365, not -1**. The tunneling decay is much slower than the σ-rate.

**Explicit non-match**:
```
n=7: tunnel = 0.117  (observed)
     2/n    = 0.286  (TIG bound)
     2/√n   = 0.756  (n^(-1/2) decay)
     2/n^(0.365) = 0.469  (matches direction, off by 4×)
```

So **tunneling fraction does NOT track the σ-rate bound 2/N in any obvious way**. The structural shape (monotone decreasing with n) is right, but the rate of decay differs by a factor of 2.7× in the exponent. This is a real non-match, not a near-match.

**Possible interpretations:**

1. **Tunneling is the wrong σ-rate analog.** Some other monotone-decreasing quantity (binding energy, quantum defect, level spacing) might track 2/n more cleanly.
2. **TIG's σ-rate doesn't directly translate to atomic shells.** The σ-rate measures non-associativity in the binary CL on Z/NZ; atomic shells aren't in correspondence with N-element rings, so direct numerical translation isn't expected.
3. **Tunneling and σ-rate measure related but different things.** Both decay with their respective "size parameter," but the rates differ because the underlying mechanisms differ.

This is the cleanest negative result in the doc. Worth flagging.

---

## §5. Summary table — three shapes vs TIG signatures

| Shape | What it measures | Scaling with n (s-orbitals) | TIG match? |
|-------|------------------|------------------------------|------------|
| Edge size (1/I_r) | Outer boundary sharpness | n²/4 (Bohr scaling) | Substrate primes ↔ odd-l multiplicities (per companion doc); coefficient 1/4 echoes 4-core but standard QM |
| Bump arc | Intrinsic interior shape | linear in n + per-node contribution | Per-node arc contributions are non-trivial structure; no clean TIG numerical match yet |
| Tunneling | Escape probability beyond classical region | n^(-0.365) — much slower than 2/n | **NO MATCH** — tunneling decay is slower than TIG σ-rate by factor 2.7× in exponent |

**Honest synthesis**: the three-shape framework is structurally clean (edges, interior, tail), but only one shape (edge size, via the companion doc's substrate-prime correspondence) shows a candidate TIG-specific signature. The other two shapes give clean atomic physics that doesn't yet pin to TIG numbers.

This is a **negative result that scopes** the framework: TIG's signature appears in the EDGE structure (substrate primes ↔ odd-l multiplicity) but not (yet) in the INTERIOR shape (bump arc) or TAIL behavior (tunneling). If TIG describes electrons as boundary-gates, this is consistent — boundary-gate properties should show up at edges, not in interiors or tails.

---

## §6. Three computational tasks for ClaudeCode

### §6.1 Priority 1: Asymptote of nodeless bump arc

**Task**: compute bump_arc for nodeless (l = n−1) shells at n = 10, 15, 20, 30, 50. Determine the asymptotic limit.

**Test against**: 4/π² ≈ 0.405, 1+sqrt(3)/2 ≈ 1.866, (2/3)·1/ζ(2) = 4/π² (same), T* = 5/7, 1+T* = 12/7 ≈ 1.714, 2 (delta-function limit).

**Falsification**: if no TIG number matches the asymptote within 1%, bump arc has no TIG-specific structural match.

**Success**: if asymptote = some clean TIG combination (especially involving 4/π² or T*), the substrate's corridor structure is encoded in the orbital shape.

**Implementation**: extend `three_shapes_shell_measurement.py` to use mpmath at higher precision for n ≥ 10 where standard scipy.integrate.quad becomes unstable.

### §6.2 Priority 2: Better σ-rate analog candidates

**Task**: instead of tunneling fraction, test these as σ-rate analogs for atomic shells:

1. **Binding energy** E_n = -13.6/n² eV → scales as 1/n², not 1/n
2. **Adjacent-shell energy gap** ΔE = E_{n+1} - E_n ∝ 1/n³
3. **Quantum defect** δ_l (zero for hydrogen, but real for multi-electron atoms)
4. **Adjacent-shell radial overlap** with proper sign tracking
5. **Asymptotic deviation from semiclassical limit**: max |R_{n,l} - R_classical|

For each, fit log-log slope and compare to -1 (the σ-rate bound exponent).

**Falsification**: if no candidate has slope = -1 within 0.1, σ-rate doesn't translate to atomic shells.

**Success**: if some candidate has slope = -1 ± 0.1, it identifies the right "σ-rate analog" in atomic physics.

### §6.3 Priority 3: Multi-electron Fisher information from Sen-Antolín-Angulo data

**Task**: pull published shell-resolved S_r and I_r values for atoms across the periodic table from Sen 2005 (J. Chem. Phys. 123:074110) and Esquivel et al. 2010. Check whether the substrate-prime ↔ odd-l correspondence (per companion doc) shows up in real multi-electron Fisher information data.

**Specifically**: at Z values where p, f, h shells fill (substrate clicks), is the Fisher information distinctively scaled compared to s, d, g, i shell-filling Z values (between substrate clicks)?

**Implementation**: digitize tables from the published papers; compute correlation between (Z, dominant orbital l) and (S_r, I_r); check for systematic differences at substrate-click Z values.

**Falsification**: if Fisher information at d, g, i filling Z values is statistically indistinguishable from p, f, h filling Z values, the substrate-orbital correspondence is coincidence.

**Success**: if there's a systematic difference (substrate-click filling shows distinctive scaling), structural correspondence is empirically supported.

---

## §7. Cross-references

| Reference | Connection |
|-----------|-----------|
| `FORMULAS_AND_TABLES.md` §17 | TIG measurement constants — T*=5/7, 4/π², σ-rate, Wob(k) — used as comparison targets |
| `FORMULAS_AND_TABLES.md` D2 | sinc² continuum limit, where 4/π² lives |
| `FORMULAS_AND_TABLES.md` D71 | Sharpened σ-rate σ(N) ≤ 2(N-2)²/N³, used as the bound for shape 3 |
| `SPECULATION_ELECTRON_BLACK_HOLE_BRIDGE.md` | Electron-as-boundary-gate intuition; this doc tests one consequence (edge widening) |
| `SPECULATION_SHELL_FISHER_INFORMATION.md` | Companion doc on substrate primes ↔ odd-l multiplicities |
| `BRAIDING_FRACTAL_FORMAL.md` Axiom 7 | The 4-core {V, H, Br, R}, related to 1/4 prefactor in edge_size |
| `BRAIDING_FRACTAL_FORMAL.md` Axiom 8 | Substrate ladder — the source of {3, 7, 11} primes in companion doc |

---

## §8. Status

```
[COMPUTED]      All three shapes for n=1..7 at machine precision
[CLEAN]         Edge size = n²/4 (Bohr); bump arc gives non-trivial interior info
[NEGATIVE]      Tunneling decay slope -0.365 ≠ TIG σ-rate slope -1
[OPEN]          Asymptote of nodeless bump arc (need n ≥ 10)
[OPEN]          Better σ-rate analog (5 candidates flagged)
[REPRODUCIBLE]  three_shapes_shell_measurement.py runs in ~30 seconds
```

---

## §9. One-paragraph summary

Defined three independent shape measures for hydrogenic shells: edge size (1/I_r, outer boundary sharpness), bump arc (intrinsic interior shape, flat-region-corrected), and tunneling fraction (probability beyond classical turning point, σ-rate analog). Edge size grows as n²/4 for s-orbitals (standard Bohr scaling, with the 1/4 prefactor echoing the 4-core but not specifically TIG). Bump arc shows non-trivial structure: nodeless shells slowly approach a limit near 1.1, and adding nodes increases arc length with per-node contribution decreasing as more nodes are present (the first node added contributes ~0.5-0.95, subsequent nodes ~0.4). Tunneling fraction decays as n^(-0.365), which is monotone but **does NOT match** the TIG σ-rate slope of -1. Three follow-up computational tasks defined: pin the bump arc asymptote at high n, test alternative σ-rate analogs, and check the substrate-prime ↔ odd-l correspondence in published multi-electron Fisher information data.

---

© 2026 Brayden Sanders / 7Site LLC

Trinity Infinity Geometry · Three-Shape Speculation Bridge · Locked 2026-05-08
