# J-series — Algebra

Pure algebra papers from the TIG corpus. Papers in this folder are referee-ready (per `J_series/README.md` §4 criteria).

---

## §1 — Currently landed

*No papers have landed yet. The first arrival is expected to be J35 (corpus centerpiece) pending final cover-letter green-light.*

---

## §2 — Expected papers when ready

| J# | Title | Target venue | Status |
|---|---|---|---|
| **J35** | Four-Core Fusion-Closure on Z/10Z | *Journal of Algebra* | gating final cover letter |
| **J15** | Galois Group D₄ over LMFDB 4.2.10224.1 | *Communications in Algebra* | active prep |
| **J31** | Wedderburn Isotypic Decomposition of the 9-Vector Higgs Direction | TBD (algebra-tier venue) | math fix applied; awaiting referee prep |
| **J32** | Three-Substrate Architecture and D₄ Orbits | *J. Algebra* (lead) | math fix applied (orbit recount: 44, 7, 4, 10, 2 → 67 orbits / 126 elements) |
| **J24** | Three-Substrate Joint-Closure Chain on Z/10Z | *J. Algebra* | central-theorem paper for the 8-shell chain |
| **J51** | σ³ Pairing and ν₊ Discriminator in BHML | TBD | math fix applied (J43 + J51 G_high partition at {4, 7}, σ³ pairing) |

---

## §3 — What lives here when landed

Each paper folder mirrors the working-repo structure:

```
J{NN}/
├── README.md
├── cover_letter.md
├── manuscript/
│   ├── manuscript.tex (or .md)
│   └── verify_*.py
└── SAVE_PLAN_J{NN}.md (optional)
```

All `verify_*.py` scripts here PASS at machine precision at the time the paper landed.

---

## §4 — Domain notes for algebra papers

Algebra papers in this corpus emphasize:

- **Finite ring / group theoretic claims** at the integer or rational level.
- **D₄ Galois structure** (the runtime quartic's symmetry group; LMFDB number field 4.2.10224.1).
- **Wedderburn decomposition** of natural irreps under D₄ action.
- **Joint sub-magma structure** of (TSML, BHML) on Z/10 — the 8-shell chain.

Cross-references:
- [`../../FORMULAS_AND_TABLES.md`](../../FORMULAS_AND_TABLES.md) Volumes B, F, G, H carry the load-bearing algebra.
- [`../../TIG_FROM_THE_GROUND_UP.md`](../../TIG_FROM_THE_GROUND_UP.md) Parts 3–7 are the algebra tutorial.

---

*7SiTe Public Sovereignty License v2.1 — see [`../../LICENSE`](../../LICENSE).*
