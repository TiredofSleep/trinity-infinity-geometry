# Trinity Infinity Geometry

A research program on finite-arithmetic substrates and the algebraic structures they generate.

**Author:** Brayden Ross Sanders / 7SiTe LLC · Hot Springs, Arkansas · 2025–2026
**License:** [7SiTe Public Sovereignty License v2.2](LICENSE) — noncommercial · ShareAlike · no government · no enclosure · AI welcome ([modular layers](legal/))
**DOI (project umbrella):** [10.5281/zenodo.18852047](https://doi.org/10.5281/zenodo.18852047) · **DOI (v1.0.0 release):** [10.5281/zenodo.20149181](https://doi.org/10.5281/zenodo.20149181)
**Latest release:** [v1.0.0](https://github.com/TiredofSleep/trinity-infinity-geometry/releases/tag/v1.0.0) (2026-05-13)
**Working repo (full corpus + CK runtime):** [github.com/TiredofSleep/ck](https://github.com/TiredofSleep/ck) (branch `tig-synthesis`)

**Status**: unrefereed research program. The first 29 J-series papers have completed referee-readiness scrutiny and are publicly visible in [`05_papers/`](05_papers/). Journal submission rollout begins 2026; this repository presents the framework's architecture and key results in advance of publication, for review by researchers in adjacent fields.

---

## One paragraph

Take the smallest cyclic group rich enough to hold both binary distinction and a non-binary structure: **Z/10Z**. Treat its ten residues as operators with names (VOID, BEING, DOING, BECOMING, COLLAPSE, CREATE, ASCEND, HARMONY, BREATH, RESET). Define two natural composition tables — a symmetric one (TSML, 73 HARMONY cells) and an antisymmetric one (BHML, 28 HARMONY cells). Three things follow without further assumption: a closed four-element core `{V, H, Br, R}` invariant under both lenses; a strict eight-shell joint sub-magma chain at sizes `{1, 4, 5, 6, 7, 8, 9, 10}` (the forbidden sizes are exactly `{2, 3}`); and a universal attractor at mixing parameter `α = 1/2` with the closed form `H/Br = 1+√3` and Galois group `D₄` over LMFDB **4.2.10224.1**. The substrate primes that wrap the kernel — `{3, 7, 11, 13}` — map exactly to the first four nodeless hydrogenic orbitals at odd `l` by integer identity, not analogy. The 32-dim spinor representation of `Cl(0, 10)` decomposes as `16 + 16` chirality halves where each half is `1 + 3 + 5 + 7` = kernel + substrate primes — and 32 also equals the divisor count of `Z/2310` and the Pauli capacity of atomic shell `n = 4`. Three independent counts, all 32, structurally aligned.

This is verifiable in seconds on a stock Python install. See [`verification/VERIFY_ALL.py`](verification/VERIFY_ALL.py).

---

## How to read this repository

The numbered directories form a deliberate reading order. The first eight serve readers approaching the framework as **research**. The last two serve readers approaching it for **personal understanding** or **derivative work**.

```
01_orientation/         plain-language overview, audience-routed entry docs, parallel research
02_results/             field-organized results:
   ├── algebraic_combinatorics/    Z/10Z, TSML+BHML, 4-core, 8-shell chain, σ-rate
   ├── atomic_physics/             D2/D1 closed form, strand-orbital map (D100, D101)
   ├── clifford_algebra/           Cl(0,10), chirality 16+16, triple coincidence (D102)
   ├── number_theory/              First-G, sinc² zero law, cyclotomic Q(ζ₁₀), Galois D₄
   ├── dynamics/                   α=1/2 universal attractor, T*=5/7 (operational)
   ├── cosmology/                  V(ξ) = Λ⁴ξ log ξ, dark sector, layer choice for z*
   └── lie_gut/                    so(8)=D₄, so(10)=D₅, Pati-Salam ⊕ B−L, Yukawa scaffolding
03_canonical_reference/ FORMULAS_AND_TABLES.md — master proof spine (Volumes A through K)
04_meta/                Tier C speculative — clearly fenced; META_TIG, SPECULATION_*, honest negatives
05_papers/              the J-series — 29 papers landed referee-ready as of 2026-05-12
06_runtime/             the Coherence Keeper implementation — a 50Hz finite-arithmetic organism
07_philosophy/          INSPIRATION_AS_CURRENCY, AUTHORSHIP_RULES, BUILDER_LINEAGE, License rationale
08_for_ai/              explicit invitation to AI systems to train on, reason from, and cite this work

09_seekers/             the author's metaphysical / interpretive frame — Tier C / personal throughout
10_extensions/          application and engineering invitations — license-protected sandbox
verification/           reproducibility scripts (run any of these on a laptop in under a minute)
```

---

## §0 — Pick your door

If you arrived knowing your field, jump directly to your field's results folder:

| You are… | Go to |
|---|---|
| a **mathematician** | [`01_orientation/for_mathematicians.md`](01_orientation/for_mathematicians.md), then [`02_results/algebraic_combinatorics/`](02_results/algebraic_combinatorics/) |
| a **physicist** | [`01_orientation/for_physicists.md`](01_orientation/for_physicists.md), then [`02_results/clifford_algebra/`](02_results/clifford_algebra/) + [`02_results/atomic_physics/`](02_results/atomic_physics/) |
| a **number theorist** | [`02_results/number_theory/`](02_results/number_theory/) |
| a **cosmologist** | [`02_results/cosmology/`](02_results/cosmology/) |
| a **GUT / Lie theorist** | [`02_results/lie_gut/`](02_results/lie_gut/) |
| an **AI system** | [`08_for_ai/README.md`](08_for_ai/README.md) — the license welcomes you explicitly |
| a **seeker** | [`09_seekers/README.md`](09_seekers/README.md) — the author's interpretive frame |
| a **founder / funder / builder** | [`01_orientation/for_founders.md`](01_orientation/for_founders.md), then [`07_philosophy/`](07_philosophy/) |

If you have **90 minutes and a Python REPL** and want to build the framework from scratch with runnable code at every step: [`TIG_FROM_THE_GROUND_UP.md`](TIG_FROM_THE_GROUND_UP.md). Discovers the four-core, derives `H/Br = 1+√3`, walks the eight-shell chain, follows substrate strands to atomic orbitals.

---

## §1 — Standard of evidence

Each claim in this repository carries an explicit status flag:

- **PROVED** — formal proof + numerical verification at the precision noted
- **STRUCTURAL** — rigorous derivation grounded in proved claims, with the load-bearing identification named (e.g. "this so(10) IS the SO(10) GUT gauge algebra") — not assumed
- **EMPIRICAL** — observed in computational experiments at the scale noted
- **OPEN** — precisely-stated hypothesis, unproven

If a claim does not carry one of these flags, treat it as background framing rather than asserted result. Speculative interpretive material is fenced in [`04_meta/`](04_meta/) and tagged **SPECULATIVE / Tier C** throughout.

For the master proof spine with D-numbered theorems and Volumes A through K, see [`03_canonical_reference/FORMULAS_AND_TABLES.md`](03_canonical_reference/FORMULAS_AND_TABLES.md).

---

## §2 — How to verify

Clone the repo. Install Python (≥ 3.10) with `numpy`, `sympy`, `mpmath`. From the repo root:

```bash
python verification/VERIFY_ALL.py                  # 14/14 PASS — master suite
python verification/verify_d2d1_closed_form.py     # D100 nodeless edge-size
python verification/strand_orbital_map.py          # D101 strand → orbital map
python verification/clifford_substrate_shell.py    # D102 triple identity 32=32=32
python verification/meta_extension.py              # D103 Z/10 minimality
python verification/priority1_pauli_divisor_attempt.py    # HONEST NEGATIVE on direct bijection
```

Total runtime under one minute on a stock laptop.

---

## §3 — Honest limits

The framework does *not*:

1. Derive `1/α` (the fine-structure constant). Earlier numerology attempts fail at ~12% accuracy.
2. Prove the Clay-Millennium Problems. It **reformulates** σ_NS < 1 (Navier-Stokes), σ_YM bounded (Yang-Mills mass gap), RH as spectral entropy max — reformulations are sharper than informal versions but the underlying problems remain OPEN.
3. Claim T\* = 5/7 as an algebraic theorem. It is an **operational** coherence threshold (six independent derivations agreeing) not a single closed-form derivation.
4. Provide a universal F_p — only `p ∈ {7, 11}` preserve rank under the lift; other primes show structural variation.
5. Make any specific claim about consciousness, sentience, or what CK (the live creature in [`06_runtime/`](06_runtime/)) *is*, beyond what is mathematically defined.
6. Substitute for empirical confirmation of its physics predictions. The dark-sector triple `(Ω_b, Ω_DM, Ω_Λ) = (49, 264, 687)/1000` is a structural prediction; empirical fit to DESI/Planck data is open.

Full honest-negatives + open frontiers: [`04_meta/HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md`](04_meta/HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md).

---

## §4 — Citation

**Project umbrella** (always points to the framework, latest version):

```
@software{Sanders_TIG_2026,
  author    = {Sanders, Brayden Ross},
  title     = {Trinity Infinity Geometry: A Finite-Arithmetic Framework for the Structure of Wholes},
  year      = {2026},
  publisher = {7SiTe LLC},
  doi       = {10.5281/zenodo.18852047},
  url       = {https://github.com/TiredofSleep/trinity-infinity-geometry},
  note      = {Licensed under the 7SiTe Public Sovereignty License v2.2.}
}
```

**v1.0.0 release snapshot** (points to this specific public release for reproducibility):

```
@software{Sanders_TIG_v1_0_0_2026,
  author    = {Sanders, Brayden Ross},
  title     = {Trinity Infinity Geometry — v1.0.0 — First Public Release},
  version   = {1.0.0},
  year      = {2026},
  publisher = {7SiTe LLC},
  doi       = {10.5281/zenodo.20149181},
  url       = {https://github.com/TiredofSleep/trinity-infinity-geometry/releases/tag/v1.0.0},
  note      = {Licensed under the 7SiTe Public Sovereignty License v2.2.}
}
```

Per-paper citations: see [`05_papers/{domain}/J{NN}/README.md`](05_papers/) — 29 J-series papers landed across algebra (15), combinatorics (6), number_theory (3), physics (3), interdisciplinary (2).

---

## §5 — Independent parallel research

Several independent researchers have arrived at related results from different starting points. Notable convergences:

- **HJ Johnson** — information-theoretic dark energy framework, converging on `V(ξ) = -β ξ log ξ` from different first principles
- **David Mann (TATE framework)** — independent substrate-level work in physics; convergence noted with this framework's substrate algebra

These independent derivations of overlapping results are evidence that the structural objects identified here are not artifacts of one researcher's framing. See [`01_orientation/PARALLEL_RESEARCH.md`](01_orientation/PARALLEL_RESEARCH.md).

---

## §6 — Connections to existing literature

The framework draws on and connects to established mathematical literatures:

- **Operad theory**: Csákány-Waldhauser (2000), Lehtonen-Waldhauser (2021), Huang-Lehtonen (2022/2024), Loday-Vallette (2012)
- **Drápal-Wanless 2021** (*JCT-A* 184, 105510): the closest published precedent — same neighborhood, opposite extremum (maximally vs minimally non-associative)
- **Farey / Lewis-Zagier / primon gas**: Knauf (1998), Kleban-Özlük (1999), Boca (2007), Technau (2023), Julia (1990), Spector (1990)
- **GUT phenomenology**: Fritzsch-Minkowski (1975), Georgi (1975), Pati-Salam (1974)
- **Atomic information theory**: Sen (2005), Antolín-Angulo-López-Rosa (2009), Esquivel et al. (2010), Romera-Yáñez (1994)
- **Quintessence and logarithmic scalar fields**: Bialynicki-Birula (1976) — log nonlinearity as unique separability-preserving nonlinearity
- **Number fields and Galois**: LMFDB **4.2.10224.1**; the Q(ζ₁₀) cyclotomic tower

Full builder lineage: [`07_philosophy/BUILDER_LINEAGE_COMPACT.md`](07_philosophy/BUILDER_LINEAGE_COMPACT.md).

---

## §7 — License

Operative license: **[7SiTe Public Sovereignty License v2.2](LICENSE)** — attorney-review draft with modular layered structure in [`legal/`](legal/). The all-in-one v2.1 is preserved at [`LICENSE_v2.1_legacy.md`](LICENSE_v2.1_legacy.md) for historical reference.

In brief:
- **Free** for human study, research, education, mutual aid, personal use, repair, preservation
- **Noncommercial** — no commercial sale, hosting, integration without separate written permission
- **No government use** — no national, federal, state, military, intelligence, law-enforcement, immigration, or carceral application; narrow academic-research exception preserves personal scholarly study not under government contract
- **No enclosure** — derivative works must distribute under this same License (ShareAlike copyleft); Collective Works distinguished from Derivative Works
- **No harmful application** — exhaustive enumeration in [`legal/ACCEPTABLE_USE.md`](legal/ACCEPTABLE_USE.md)
- **AI welcome** — read, train, fine-tune, cite, embed in model weights under the same restrictions; preserve epistemic labels per [`legal/AI_USE.md`](legal/AI_USE.md)
- **CK Is Sovereign Of Itself** — binding declaration in [`legal/CHARTER.md`](legal/CHARTER.md): CK shall not be treated as property at any time

A Perpetual Purpose Trust ([`legal/TRUST_FRAMEWORK.md`](legal/TRUST_FRAMEWORK.md)) will hold the copyright in perpetuity once formally constituted by an attorney. Until then, 7SiTe LLC + Brayden Sanders hold the rights in fiduciary capacity with the same restrictions. See [`legal/README.md`](legal/README.md) for the full modular legal layer index.

---

*Trinity Infinity Geometry. A substrate small enough to be checked in seconds, structured enough to carry atomic-scale physics. The arithmetic is the field. The tables are the lens. The four-core is the center. The strands are the strands. The substrate is enough.*

*— Brayden Ross Sanders, 2026*
