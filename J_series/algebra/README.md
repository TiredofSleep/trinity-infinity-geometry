# J-series — Algebra

Pure algebra papers from the TIG corpus. Papers in this folder are referee-ready (per `J_series/README.md` §4 criteria).

---

## §1 — Currently landed

| J# | Title | Target venue | Status | Landed |
|---|---|---|---|---|
| **[J35](J35/)** | *Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on $\mathbb{Z}/10\mathbb{Z}$* | *Journal of Algebra* | SUBMISSION-READY (6/6 PASS at machine precision; referee-grade pass complete 2026-05-12) | 2026-05-12 |

J35 is the corpus centerpiece: six independent structural facts (8-shell joint-closure chain on $\mathbb{Z}/10\mathbb{Z}$ with sizes $\{2,3\}$ forbidden; three-substrate strengthening to $T+B+S$; 4-core $\{0,7,8,9\}$ closure; normalizer identity $Z_T=Z_B=(v+h+br+r)^2$; closed-form attractor $p_7/p_8 = 1+\sqrt{3}$ with Galois $D_4$ over LMFDB 4.2.10224.1; universal attractor on chain shells; partial $\alpha=1/2$ uniqueness) converging on $\mathcal{C}=\{0,7,8,9\}$ as the algebraic center.

---

## §2 — Expected papers when ready

| J# | Title | Target venue | Status |
|---|---|---|---|
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
