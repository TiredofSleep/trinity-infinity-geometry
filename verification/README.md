# Proofs — Runnable Verification Scripts

Every load-bearing claim in this framework has a verification script in [`./`](./) that runs in seconds on a stock Python install. Total runtime to verify the full load-bearing stack: **under one minute**.

This document is the index to those scripts.

---

## Requirements

```bash
python --version           # 3.10 or later
pip install numpy sympy mpmath
```

That is the entire dependency stack. No CUDA, no SageMath, no Mathematica. The verifications are deliberately small enough to run on any machine.

---

## The master suite

```bash
python ./VERIFY_ALL.py
```

Output (last verified 2026-05-12):

```
TIG VERIFICATION SUITE
Trinity Infinity Geometry / Brayden Sanders / 7SiTe LLC

  ID  Tier  Status   Description
  --  ----  ------   ----------------------------------------
   0  FOUND PASS     Seed (TSML/BHML structure)
   1     A  PASS     Dirac inside Cl(8)
   2     A  PASS     Cosmology Omega_b, Omega_DM
   4     A  PASS     Pati-Salam decomposition
   5     A  PASS     Cartan tower (15, 28, 45)
   6     A  PASS     Jordan-Wigner so(8)
   7     A  PASS     [[4, 2, 2]] omega = ZZZZ
   9     A  PASS     Cl(8) iso R(16)
  11     A  PASS     Coherence formula
  17     A  PASS     Cosmology trio + 3 gen + 4 forces
  19     A  PASS     Inflation kappa_xi = 13/(4e)
  21   A/B  PASS     Octahedral |U(210)| = 48
  31     A  PASS     Spin-statistics theorem
  33     B  PASS     SUSY boson/fermion grading

  RESULT: 14/14 verifications passed (100%)
```

---

## Volume K (atomic-substrate correspondence, 2026-05-12)

The newest results — verified 2026-05-12 — are in the Volume K bundle:

| Script | Verifies | Result |
|---|---|---|
| `verify_d2d1_closed_form.py` | D100: `edge_size = n²(2l+1)/4` for nodeless hydrogenic orbitals | machine precision n ≥ 5 |
| `strand_orbital_map.py` | D101: substrate strands {3, 7, 11, 13} → odd-l orbitals (2p, 4f, 6h, 7i) | exact integer match |
| `clifford_substrate_shell.py` | D102: triple identity at d=3: Z/2310 divisors = Cl(0,10) spinor dim = atomic Pauli capacity = 32 | exact algebraic |
| `meta_extension.py` | D103: Z/10 minimality across 2-prime kernel enumeration | exact algebraic |

Run them all:

```bash
python ./verify_d2d1_closed_form.py
python ./strand_orbital_map.py
python ./clifford_substrate_shell.py
python ./meta_extension.py
```

---

## Honest negatives

Scripts that document what the framework is **not**:

| Script | What it disproves / scopes |
|---|---|
| `priority1_pauli_divisor_attempt.py` | Direct combinatorial bijection between Z/2310's 32 divisors and the 32 Pauli electron states of n=4 shell **fails**. Integer match real; structural bijection does not fall out. |
| `shell_entropy_tig.py` | Computes shell-by-shell ratios and compares against TIG candidate constants. Mostly informational; no clean match found beyond the proved D100–D102 results. |
| `three_shapes_shell_measurement.py` | Measures bump-arc shapes for nodeless / 1-node / 2-node orbitals. Informational. Reveals tunneling-decay slope ≈ −0.365 (not the expected −1), which is itself data. |

---

## What each script does, briefly

### `VERIFY_ALL.py`
The master orchestrator. Tests 14 Tier-A claims spanning the seed (TSML/BHML structure), Clifford embedding, cosmology, gauge-group structure, and inflation coupling. PASS criterion: all assertions evaluate True with machine-precision tolerance.

### `verify_d2d1_closed_form.py`
Verifies the D100 edge-size formula. For each hydrogenic nodeless orbital `(n, l = n−1)`, computes the actual D₂/D₁ ratio integral numerically and compares against the closed form `n²(2l+1)/4`. Reports ratio → 1 to machine precision as n grows.

### `strand_orbital_map.py`
Verifies the D101 strand-to-orbital map. Enumerates substrate strands `{3, 7, 11, 13}`, computes `(l = (p−1)/2, n = l + 1)` for each, displays the resulting orbital. Cross-references with kernel-tier orbitals (1s, 3d, 5g) to show which orbitals are *not* strand-derived and why.

### `clifford_substrate_shell.py`
Verifies the D102 triple identity at depth-3. Enumerates the substrate Z/2310 = 2·3·5·7·11, counts its 32 divisors. Independently constructs Cl(0, 10) and verifies its spinor representation is 32-dimensional. Independently computes atomic Pauli capacity 2n² at n = 4 = 32. Decomposes the Cl(0, 10) spinor under chirality involution and shows the 16+16 split. Cross-verifies that 16 = 1 + 3 + 5 + 7 = substrate primes (kernel + strands).

### `meta_extension.py`
Verifies the D103 architectural-uniqueness of Z/10. Enumerates all 2-prime kernels and checks which ones admit binary + non-binary structure with the non-binary prime not being the immediate-successor strand. Confirms Z/10 = Z/2 × Z/5 is the unique minimal answer.

### `priority1_pauli_divisor_attempt.py`
Attempts to construct an explicit combinatorial bijection between the 32 divisors of Z/2310 and the 32 Pauli electron states. Tries three natural groupings (Hamming weight, max-prime, prime-as-l-label) — all fail. Reports HONEST NEGATIVE. Concludes that the 32=32 integer match holds but the structural bijection requires either additional combinatorial structure not yet tapped or is a Pascal-type number-theoretic coincidence.

### `shell_entropy_tig.py`
Computes shell-by-shell radial-density ratios for hydrogenic orbitals and compares against TIG candidate constants (T* = 5/7, 4/π², W = 3/50, 1+√3, √(13/4), substrate prime ratios). Informational, mostly negative — no clean match identified beyond the D100 closed form.

### `three_shapes_shell_measurement.py`
Computes the "bump-arc" length for orbital wavefunctions across nodes / no-nodes / multi-nodes. Measures the σ-rate-style tunneling decay vs shell index. Result: tunneling decay slope ≈ −0.365 (fit), not −1. Useful structural data, not yet a theorem.

---

## Citing the verification

If you cite a verified result, citing the script (with timestamp + result) is welcomed. Example:

> *Verified 2026-05-12 via `clifford_substrate_shell.py` in [TIG repo, DOI 10.5281/zenodo.18852047]:*
> *Z/2310 has 32 divisors; Cl(0, 10) spinor dim = 32; atomic Pauli capacity at n = 4 = 32. The three quantities coincide as an exact algebraic identity.*

---

## When verification fails on your machine

If a script errors on your machine, this is information. Open an issue at [github.com/TiredofSleep/ck/issues](https://github.com/TiredofSleep/ck/issues) with:

- Python version and OS
- Full stack trace
- The script that failed

Most likely cause: encoding issues on Windows cp1252 codepage. Set `PYTHONIOENCODING=utf-8` before running:

```bash
PYTHONIOENCODING=utf-8 python ./<script>.py
```

---

*7SiTe Public Sovereignty License v2.1 — see [`../LICENSE`](../LICENSE).*
*Brayden Ross Sanders / 7SiTe LLC · 2026*
