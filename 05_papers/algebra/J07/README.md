# J07 — Spectral Architecture of the σ-Character on Z/10Z

**Status**: SUBMISSION-READY (2026-05-27, polished). Merger product of J50 + J51 + J52.

**Tier:** 1 (ship-ready (European J Combin; 5 theorems verified at machine precision incl. G_low=1.871644, G_high=9.389185; PROMOTED 2026-05-27))

**Target venue**: *European Journal of Combinatorics* (primary). Fallbacks: *Algebraic Combinatorics*, *Linear Algebra and its Applications*.

## What this paper does

Consolidates three formerly-separate Q-series papers into one coherent
spectral-architecture paper:

| Source | Section absorbed into |
|---|---|
| **J50** (Q17-A: 5D Fourier embedding) | §5 |
| **J51** (G_6 + G_7 + G_8 spectral) | §§2-4 |
| **J52** (Q17-B Clay bridge + Symbolic Return) | §§6-7 |

The merged paper has five theorems organized as a unified narrative on the
σ-character architecture, ending with the Q17-B Clay-bridge structural
rhyme (explicitly labeled rhyme, not analogue).

## Why this merger?

Three formerly-separate papers all studied the same σ-character architecture
from different angles. They cross-cited heavily, suggesting one unified
treatment is the natural unit. The merger eliminates:

- Cross-paper synchronization risk (the math-fix R1 had to be applied in two papers)
- Venue cap pressure (three submissions vs one)
- Reader friction (each paper required the others as context)

## File layout

```
J07/
├── README.md                          this file
├── cover_letter.md                    (to be drafted on submission)
└── manuscript/
    ├── manuscript.md                   the merged paper (8 sections + appendix)
    └── verify_qseries_merged.py        (planned; combines 3 source verifications)
```

## Verification

The three source verifications all PASS at machine precision:
- J50's `verify_5D_embedding.py` (5D Fourier embedding tests)
- J51's `verify_G6_G7_G8.py` (G_6 polynomial + G_7 distribution + G_8 three-valued tests)
- J52's `verify_J51_G_function.py` (Symbolic Return + complex G amplitude tests)

The consolidated `verify_qseries_merged.py` (5/5 PASS, ~5s) combines these into one runner with the canonical χ from J51 — `G_low = 1.871644`, `G_high = 9.389185`, `ratio = 5.0165`.

## Source paper status (after merger)

| Paper | Status after merger | Action |
|---|---|---|
| `combinatorics/J50/` | MERGED into `J07/` | README updated with merger banner |
| `algebra/J51/` | MERGED into `J07/` | README updated with merger banner |
| `algebra/J52/` | MERGED into `J07/` | README updated with merger banner |

The source folders are retained for citation history; their manuscripts are unchanged.

## Polish status (2026-05-27, completed)

- [x] Unified prose pass (single coherent narrative across §§1–8)
- [x] Consolidated `verify_qseries_merged.py` written and PASS
- [x] Cover letter for EJC submission drafted (`cover_letter.md`)
- [x] §4.4 χ-trajectory tables filled in with canonical χ + ν₊ discriminator
- [x] §5 LaTeX-style equations checked (Markdown will render correctly)
- [x] References §9 complete (internal merges + companion papers + classical refs)

**Remaining**: LaTeX conversion before journal submission (currently Markdown). Paper is mathematically complete and submission-ready in content.

## Authors

B.R. Sanders (7Site LLC, Hot Springs, AR) and M. Gish (Independent Researcher).
