# For Physicists

The framework is finite-arithmetic at root, but it has carriers that contact physics: a Clifford algebra `Cl(0, 10)` (32-dim spinor), a dark-sector triple, a Yukawa mass-hierarchy ladder, a strand-to-orbital map for atomic structure, and an inflation coupling. Each is exact at the algebraic / rational level; whether each empirically matches observed nature is **open**.

This document organizes the physical content of the framework. Every claim is tier-labeled.

---

## §1 — The Clifford carrier `Cl(0, 10)`

**PROVED (algebraic).** The framework's 10 operators on Z/10Z embed naturally into the Clifford algebra Cl(0, 10) over ℝ. Standard construction: 10 γ-matrices built from Pauli tensor products on ℂ³², satisfying `{γ_a, γ_b} = 2δ_{ab} I` (all 100 anticommutation relations verified at machine precision). The 45 generators `Σ_{ab} = (1/4)[γ_a, γ_b]` form a faithful 32-dimensional representation of so(10).

The volume element `ω = γ₁ γ₂ … γ₁₀` satisfies `ω² = −I` (because n=10 ≡ 2 mod 4). The chirality projectors `P_± = (I ± iω)/2` split the 32-dim spinor space into **16 + 16** (the two chiral 16-irreps of Spin(10)).

This is the standard SO(10) GUT spinor construction, but here it emerges as the carrier for the substrate's 10-operator algebra, not as an external choice.

**PROVED (Volume K, 2026-05-12).** Each 16-dim chirality half admits a finer substrate-coherent decomposition:

```
16 = 1 + 3 + 5 + 7
   = (2·0+1) + (2·1+1) + (2·2+1) + (2·3+1)    [spatial states (l, m) for l = 0..3]
   = (kernel-base) + (strand 1 = prime 3) + (kernel-Z/5 partner) + (strand 2 = prime 7)
```

Reading: the Z/10 kernel's Z/2 factor = electron spin; the strand primes provide the orbital multiplicity ladder. The Cl(0, 10) spinor is exactly the algebraic shape of the n = 4 atomic shell.

### Verification

```bash
python _verification_scripts/clifford_substrate_shell.py
```

Output exhibits the triple identity `32 = 32 = 32` and the chirality split.

---

## §2 — The strand–orbital map (D101, Volume K)

**PROVED (exact algebraic identity).** The four substrate primes that wrap the Z/10Z kernel — `{3, 7, 11, 13}` — map exactly to the first four nodeless hydrogenic orbitals at odd `l`, by the rule:

```
strand p_n  →  orbital (l = (p_n − 1)/2,  n = l + 1)
```

The full mapping:

| substrate strand | modulus | mult `2l+1` | l | n | orbital | D₂/D₁ · 8π |
|---|---|---|---|---|---|---|
| 3 | Z/30 | 3 | 1 | 2 | **2p** | 3/(8π) |
| 7 | Z/210 | 7 | 3 | 4 | **4f** | 7/(8π) |
| 11 | Z/2310 | 11 | 5 | 6 | **6h** | 11/(8π) |
| 13 | Z/30030 | 13 | 6 | 7 | **7i** | 13/(8π) |

Substrate strands hit **odd-l** orbitals (p, f, h, i). Even-l orbitals (s, d, g) are not strand-derived because: 1s is kernel-base (no wrapping); 3d's multiplicity 5 = kernel-Z/5 partner; 5g's multiplicity 9 = 3² is composite (only first prime powers wrap).

**Important read.** The hydrogen atom's nodeless-orbital ladder is *exactly* the substrate-strand ladder, by integer identity. This is not an analogy — the multiplicities match by algebraic equality.

### Verification

```bash
python _verification_scripts/strand_orbital_map.py
python _verification_scripts/verify_d2d1_closed_form.py
```

The latter verifies `edge_size = n²(2l+1)/4` for nodeless orbitals to machine precision at n ≥ 5.

---

## §3 — Dark-sector predictions (STRUCTURAL)

**STRUCTURAL.** The runtime function `predict_dark_sector()` outputs an exact rational dark-sector triple:

```
Ω_b   = 49 / 1000
Ω_DM  = 264 / 1000
Ω_Λ   = 687 / 1000
```

These three rationals sum to 1.000 exactly. The derivation goes through the Cl(0, 10) substrate decomposition and the 4-core mass-distribution structure; it is internally consistent but identifies the algebraic Ω-triple with the *physical* cosmological density parameters — that identification is the STRUCTURAL claim.

**Empirical comparison.** DESI 2024 / Planck 2018 give roughly Ω_b ≈ 0.0493, Ω_DM ≈ 0.265, Ω_Λ ≈ 0.685. The framework's rational triple sits within ~0.2% of the observed values. Whether this represents a deep correspondence or a fortuitous numerical match within current observational uncertainty is **open**.

---

## §4 — Yukawa mass-hierarchy ladder (STRUCTURAL)

**STRUCTURAL.** The runtime function `predict_yukawa()` outputs a Froggatt–Nielsen-style mass-ratio ladder with slope:

```
λ = 10 / 49 ≈ 0.204
```

and a top-quark Yukawa anchor `y_t ≈ 0.93`. The ladder produces a hierarchy

```
y_n ∼ y_t · λⁿ
```

across the three generations of quarks and leptons.

**Setup paper.** The Yukawa scaffolding (which Higgs irreps couple to which fermion bilinears under SO(10) → SO(9) → SO(7) breaking with BHML's `‖VEV‖² = 13/4` in the **54** irrep) is in the J-series at J45 §2. The framework does *not* complete the Yukawa derivation from first principles — it sets up the structure and identifies where the framework's input engages the Yukawa computation. Going from this scaffolding to a falsifiable mass prediction requires committing to a specific Higgs sector (combinations of 10, 54, 126), running RG flows from GUT to electroweak scale, and comparing to observed masses. That work is open.

---

## §5 — The 9-vector Higgs direction (PROVED algebraically)

**PROVED.** BHML's `σ_outer`-breaking content lies **100% in the 54 irrep** of so(10) (J23). The explicit direction is a 9-vector in the so(9)-vector subspace with:

- six components at `−1/√2` on `{V, L, C, P, X, H}`
- two zeros at BREATH and RESET
- one component at `−1/2` on the symmetric pair `(B + S)/√2`

Squared norm:

```
‖v‖² = 13 / 4   (exact)
```

The integer 13 is exactly half the count of σ_outer-asymmetric BHML cells.

**Inflation coupling.** Under the (load-bearing) identification `m²_ξ = ‖VEV‖² = 13/4`, the inflation coupling becomes `κ_ξ = 13/(4e)`. STRUCTURAL — algebraic value exact; physical identification is the inference.

### Verification

```bash
python _verification_scripts/VERIFY_ALL.py    # item 19 (inflation κ_ξ = 13/(4e))
```

---

## §6 — Symmetry structure and the D₄ Galois group

**PROVED.** The runtime quartic in the closed-form attractor at α = 1/2 has Galois group `D₄` (dihedral, order 8) over ℚ. LMFDB number field 4.2.10224.1. Independently verified via cubic resolvent + Gröbner basis in PARI/GP.

The D₄ generated by `⟨P_{56}, σ³⟩` acts in the spinor representation. The doubly-invariant subalgebra under this D₄ is `su(4) ⊕ u(1)` — Pati–Salam plus B−L (D72 / WP104). This is the natural decomposition for SO(10) GUT model-building, but here it emerges from the substrate's symmetry structure, not from external GUT model-building.

---

## §7 — Cosmological z\* layers (OPEN, three layers)

For the cosmology paper J46, the redshift z\* of the freezing-quintessence transition is layered:

- **Layer 1 (script-honest):** z\* ≈ 2.13, derived from BBM minimality applied to the script as written. Most defensible to referees; least bold.
- **Layer 2 (postulate-as-axiom):** z\* = √3, stated as a consequence of BBM minimality + scale-free derivative axioms. Cleaner structure; requires referees to accept the axioms.
- **Layer 3a (hybrid):** keep z\* = √3 but state the minimality axioms explicitly so a reader can choose which to accept.

This is **a publication-strategy choice, not a math question.** All three are internally consistent. Each corresponds to a different target journal.

---

## §8 — What is NOT in the framework

Honest scoping:

- **The fine-structure constant 1/α.** Earlier numerology (4·40 − 2√7 − π/7) fails at ~12.6%. If 1/α has algebraic origin here, the path has not been found.
- **The Millennium Problems.** σ_NS < 1 (Navier–Stokes), σ_YM bounded (Yang–Mills mass gap), RH as spectral entropy max — these are **reformulations**, not proofs.
- **A standalone derivation of T\* = 5/7.** T\* is operational: six independent derivations converge on it, but no single closed-form theorem produces it.
- **F_p universality.** Only p ∈ {7, 11} preserve rank under the lift; other primes vary. This is structural data, not noise — but the naive "universal F_p" framing is wrong.

---

## §9 — How to verify

```bash
python _verification_scripts/VERIFY_ALL.py                  # 14/14 PASS
python _verification_scripts/verify_d2d1_closed_form.py     # D100 nodeless edge-size
python _verification_scripts/strand_orbital_map.py          # D101 strand→orbital map
python _verification_scripts/clifford_substrate_shell.py    # D102 triple identity 32=32=32
python _verification_scripts/meta_extension.py              # D103 Z/10 minimality
python _verification_scripts/priority1_pauli_divisor_attempt.py    # HONEST NEGATIVE on direct bijection
```

Total runtime under one minute.

---

## §10 — Further reading

- **[`../03_canonical_reference/FORMULAS_AND_TABLES.md`](../03_canonical_reference/FORMULAS_AND_TABLES.md)** — every D-number cross-referenced, with derivation pointer
- **[`../02_results/algebraic_combinatorics/BRAIDING_FRACTAL_AXIOMS.md`](../02_results/algebraic_combinatorics/BRAIDING_FRACTAL_AXIOMS.md)** — the 10 architectural axioms
- **[`../04_meta/`](../04_meta/)** — honest limits, the Clay rotation, the cosmology layers
- **Full J-series** (55 papers) at [github.com/TiredofSleep/ck](https://github.com/TiredofSleep/ck) `tig-synthesis` branch. Cleanest physics entries: J23 (Discrete Dirac), J35 (4-core + Galois D₄), J45 (mass hierarchy + freezing quintessence), J46 (cosmology — pending layer decision).

---

*7SiTe Public Sovereignty License v2.1 — see [`../LICENSE`](../LICENSE).*
*Brayden Ross Sanders / 7SiTe LLC · 2026*
