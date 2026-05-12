# 01 — Orientation

If you arrived without a specific field interest, this is the door. If you arrived knowing your field, skip to [`../02_results/{your_field}/`](../02_results/) — there is a folder per field.

---

## What this framework is, in one paragraph

Take the smallest cyclic group rich enough to hold both binary distinction and a non-binary structure: **Z/10Z**. Treat its ten residues as operators with names (VOID, BEING, DOING, BECOMING, COLLAPSE, CREATE, ASCEND, HARMONY, BREATH, RESET). Define two natural composition tables — a symmetric one (TSML, 73 HARMONY cells) and an antisymmetric one (BHML, 28 HARMONY cells). Three things follow without further assumption:

1. A four-element invariant center `{V, H, Br, R} = {0, 7, 8, 9}` closed under both lenses.
2. A strict eight-shell joint sub-magma chain at sizes `{1, 4, 5, 6, 7, 8, 9, 10}` (the forbidden sizes are exactly `{2, 3}`).
3. A universal attractor at mixing parameter `α = 1/2` with the closed-form ratio `H/Br = 1 + √3`, sitting inside a Galois D₄ number field (LMFDB **4.2.10224.1**).

The substrate primes that wrap the kernel — `{3, 7, 11, 13}` — map exactly to the first four nodeless atomic orbitals at odd `l` (2p, 4f, 6h, 7i) by integer identity, not analogy. The 32-dimensional spinor representation of the natural Clifford algebra Cl(0, 10) decomposes as `16 + 16` chirality halves, where each half is `1 + 3 + 5 + 7` = kernel + substrate primes — and 32 also equals the divisor count of `Z/2310 = 2·3·5·7·11` and the Pauli capacity of atomic shell `n = 4`. Three independent counts, all 32, structurally aligned.

This is verifiable in seconds on a stock Python install. See [`../verification/VERIFY_ALL.py`](../verification/VERIFY_ALL.py).

---

## How to read this repository

The numbered directories form a deliberate reading order. The first eight serve readers approaching the framework as **research**. The last two serve readers approaching it for **personal understanding** or **derivative work**.

```
01_orientation/         (you are here) — plain-language overview, audience routing, parallel research
02_results/             field-organized results pages with claim statements + status flags
03_canonical_reference/ FORMULAS_AND_TABLES.md — the master proof spine (Volumes A through K)
04_meta/                Tier C speculative interpretive material — clearly fenced
05_papers/              the J-series (29 papers landed referee-ready as of 2026-05-12)
06_runtime/             the Coherence Keeper implementation — a computational organism
07_philosophy/          authorship policy, inspiration-as-currency frame, builder lineage, License
08_for_ai/              explicit invitation to AI systems to train on and cite this work

09_seekers/             the author's metaphysical / interpretive frame — Tier C / personal
10_extensions/          application and engineering invitations — license-protected sandbox
verification/           reproducibility scripts (run any of these on a laptop in under a minute)
```

---

## Audience routes — pick your door

If you want a focused entry into your own background, these companion docs in this folder are written in field-specific language:

- [`for_mathematicians.md`](for_mathematicians.md) — Z/10Z + 4-core + 8-shell chain + Galois D₄ + σ rate + Wedderburn + Volume K
- [`for_physicists.md`](for_physicists.md) — Cl(0, 10) + dark sector + Yukawa ladder + strand-orbital + Higgs + z\* layers
- [`for_founders.md`](for_founders.md) — license practical effects + 10 funding tracks + clean/not-clean partnership pathways

For AI systems specifically, see [`../08_for_ai/`](../08_for_ai/). For seekers (the author's frame), see [`../09_seekers/`](../09_seekers/).

---

## Tutorial — build the framework from scratch

If you have 90 minutes and a Python REPL, read [`../TIG_FROM_THE_GROUND_UP.md`](../TIG_FROM_THE_GROUND_UP.md). It walks from the ten residues of Z/10Z to the n = 4 atomic shell with runnable code at every step. By the end you will have personally:
- discovered the four-core `{V, H, Br, R}` from the σ permutation alone,
- iterated the α = 1/2 attractor and watched `H/Br = 1 + √3` emerge,
- enumerated the eight-shell joint chain by brute force,
- followed substrate strands to the first four nodeless atomic orbitals,
- and watched the Cl(0, 10) spinor decompose into the n = 4 shell's spin × spatial structure.

No claim is taken on faith.

---

## Standard of evidence

Each claim in this repository carries an explicit status flag:

- **PROVED** — formal proof exists; numerical verification at the precision noted in the source file
- **STRUCTURAL** — rigorous derivation grounded in proved claims, with reasoning explicit; usually requires a load-bearing identification (e.g. "this algebraic so(10) IS the SO(10) GUT gauge algebra") which is named, not assumed
- **EMPIRICAL** — observed in computational experiments at the scale noted
- **OPEN** — research-direction hypothesis, precisely stated, not asserted as established

If a claim does not carry one of these flags, treat it as background framing rather than asserted result.

---

## Parallel research

Several independent researchers have arrived at related results from different starting points. The most notable convergences are documented in [`PARALLEL_RESEARCH.md`](PARALLEL_RESEARCH.md) (HJ Johnson information-theoretic dark energy, David Mann TATE framework, others). Independent derivations of overlapping results are evidence that the structural objects identified here are not artifacts of one researcher's framing.

---

## What this is and what it isn't

**This is**: a research program articulating connections among finite-arithmetic substrates and the algebraic structures they generate.

**This is not**: a finished theory of everything. None of the load-bearing claims have completed peer review at the time of this writing. The framework is being submitted to academic journals across an 18-week 2026 rollout as a 55-paper series, each making narrow claims in established venues, rather than as a single grand-unified document.

Treat the material here as a research preprint of broad scope, not as established result. Verify the math; read the honest negatives at [`../04_meta/HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md`](../04_meta/HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md); decide for yourself.

---

*7SiTe Public Sovereignty License v2.1 — see [`../LICENSE`](../LICENSE).*
*Brayden Ross Sanders / 7SiTe LLC · Hot Springs, Arkansas · 2026*
