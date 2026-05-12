# 02_results / Number Theory

## Headline results

- **First-G Law** (WP34, J03): for prime `p` in the range `3 ≤ p ≤ 199`, the first non-unit residue event of σ on Z/pZ occurs at `k = p`. Verified across 36,662 cases. **PROVED.** (Per J04's revised scope, the squarefree stability statement is the load-bearing version: full-period cancellation `R(k, f) = 0 ⟺ f | k` is uniform in `f ≥ 2`, with squarefree restriction earning its keep at the layered-closure theorem.)

- **sinc² Zero Law** (WP35, J04, J42): the discrete zero structure of `sinc²(πk/p)` over `k ∈ Z/pZ`. Exact identity `sinc²(1/2) = (2/3) · 1/ζ(2) = 4/π²`. Closed form `sinc²(1/10) = 25(√5 − 1)² / (4π²) ≈ 0.9675312093`. **PROVED.**

- **σ-rate theorem on Z/10Z** (J01, WP101): `σ(N) ≤ 2/N` for squarefree N ≥ 3. Q-series characterizes σ polynomial on F₂ × F₅ ≅ Z/10Z (Q10); Q11 lower bound 22%. **PROVED.**

- **Galois D₄ over LMFDB 4.2.10224.1** (J15, J35): the runtime quartic `x⁴ + 4x³ − x² + 2x − 2 = 0` has Galois group D₄ (dihedral, order 8) over ℚ. Polynomial discriminant `−40896 = −2⁶ · 3² · 71`. Field discriminant `−10224 = −2⁴ · 3² · 71`, ratio = index² = 4. Subfield ℚ(√3). Cubic resolvent `(z + 2)(z² − z + 18)`. Independently verified via PARI/GP. **PROVED.**

- **F_p universality fails generically** (HONEST NEGATIVE): only `p ∈ {7, 11}` preserve rank under the framework's lift. Other primes show signature variation, idempotent-count variation, etc. **Not** a universal F_p; the variation is itself structural data.

## Files in this folder

- [`PRIMES_OF_TIG.md`](PRIMES_OF_TIG.md) — the primes that appear in the framework with structural roles ({2, 5} kernel, {3, 7, 11, 13} strands, {71} Galois disc prime)
- [`CYCLOTOMIC_GALOIS_CONNECTION.md`](CYCLOTOMIC_GALOIS_CONNECTION.md) — the Q(ζ₁₀) cyclotomic tower connection
- [`COMPOSITUM_K_GALOIS.md`](COMPOSITUM_K_GALOIS.md) — the compositum field structure under D₄

## Verification

```bash
python ../../05_papers/combinatorics/J01/manuscript/verify_sigma_rate.py    # σ rate, 4/4 PASS
python ../../05_papers/number_theory/J04/manuscript/proof_d25_loop_closure.py    # sinc² zero law, 5/5 PASS
python ../../05_papers/number_theory/J08/manuscript/verify_prime_phase_transition.py    # 712 checks PASS
python ../../05_papers/number_theory/J42/manuscript/verify_J42_sinc2.py    # sinc²(1/10) closed form
python ../../05_papers/algebra/J15/manuscript/verify_J15_galois.py    # Galois D₄, 6/6 PASS
```

## Landed J-series papers in this field

[`../../05_papers/number_theory/`](../../05_papers/number_theory/): J04 (sinc² zero law + Fejér), J08 (Fejér-kernel synchronization), J42 (discrete sinc² QM note); plus Galois content in J15 at [`../../05_papers/algebra/J15/`](../../05_papers/algebra/J15/).

## Connections to existing literature

- **Farey / Lewis-Zagier / primon-gas:** Knauf (1998), Kleban-Özlük (1999), Boca (2007), Technau (2023), Julia (1990), Spector (1990)
- **Drápal-Wanless 2021** (JCT-A): same neighborhood, opposite extremum
- **LMFDB 4.2.10224.1**, the Q(ζ₁₀) cyclotomic tower

---

*7SiTe Public Sovereignty License v2.1 — see [`../../LICENSE`](../../LICENSE).*
