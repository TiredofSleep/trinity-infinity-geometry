# Verdicts

Written-up findings from the "U-line" investigation (2026-05-27): can the
σ-magma and Family C be used for cryptography, do they correspond to
Steiner systems, do they embed in known lattices, etc.

Each verdict is a self-contained markdown explaining what we tested, what
we found, and (where applicable) why the negative answer is structurally
forced.

## Index

| File | Question | Answer |
|---|---|---|
| `sigma_magma_crypto_verdict.md` | Is the σ-magma a cryptographic primitive? | **NO** — catastrophic differential weakness; "sum-then-permute" structural flaw |
| `steiner_family_c_verdict.md` | Is Family C a Steiner-system variety? | **NO** — Family C sits strictly below the squag variety (profile 14 vs 342) |
| `sts_classification_corrected.md` | Is the profile-382-vs-342 split = geometric-vs-combinatorial STS? | **NO** (retraction) — PG(3,2) STS(15) is maximally geometric and profile 342; the split is purely a small-order coincidence (orders ≤ 9 vs ≥ 13) |
| `sigma_k12_verdict.md` | Does σ-magma embed in Aut(K₁₂)? | **NO** — three independent obstructions (non-assoc, \|Aut\|=1, L_a non-closed) |

## Associated data

| File | Contents |
|---|---|
| `squag_variety_diff.json` | The 40 ETP equation IDs (with texts) that hold in STS(3,7,9) but fail in STS(13) |
| `sts_15_classification.json` | PG(3,2) STS(15) profile data (the refuting case) |

## Why these are valuable

Negative results with mechanistic explanations close research branches
cleanly. The σ-magma is **algebraically isolated** — not a crypto
primitive, not a Steiner system, not a lattice subobject. Its
mathematical content lives entirely in its own quasigroup structure and
Family C minimality, which is itself a publishable position (see J60 / J61).

Outside readers can save time by reading these verdicts before pursuing
the same investigations.

## Reproducing

Each verdict references one or more Python scripts in `../extensions/`.
Run e.g.:

```bash
cd ..
ETP_PATH=/path/to/equational_theories/scripts \
python extensions/sigma_magma_crypto.py  # ~5 min for 10^6 trials
```
