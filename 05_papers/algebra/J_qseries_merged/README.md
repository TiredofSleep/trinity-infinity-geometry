# J_qseries_merged — Spectral Architecture of the σ-Character on Z/10Z

**Status**: CONSOLIDATED DRAFT (2026-05-27). Merger product of J21 + J43 + J51.

**Tier:** 2 (CONSOLIDATED DRAFT 2026-05-27 (merger of J21+J43+J51); awaiting prose polish)

**Target venue**: *European Journal of Combinatorics* (primary). Fallbacks: *Algebraic Combinatorics*, *Linear Algebra and its Applications*.

## What this paper does

Consolidates three formerly-separate Q-series papers into one coherent
spectral-architecture paper:

| Source | Section absorbed into |
|---|---|
| **J21** (Q17-A: 5D Fourier embedding) | §5 |
| **J43** (G_6 + G_7 + G_8 spectral) | §§2-4 |
| **J51** (Q17-B Clay bridge + Symbolic Return) | §§6-7 |

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
J_qseries_merged/
├── README.md                          this file
├── cover_letter.md                    (to be drafted on submission)
└── manuscript/
    ├── manuscript.md                   the merged paper (8 sections + appendix)
    └── verify_qseries_merged.py        (planned; combines 3 source verifications)
```

## Verification

The three source verifications all PASS at machine precision:
- J21's `verify_5D_embedding.py` (5D Fourier embedding tests)
- J43's `verify_G6_G7_G8.py` (G_6 polynomial + G_7 distribution + G_8 three-valued tests)
- J51's `verify_J51_G_function.py` (Symbolic Return + complex G amplitude tests)

The consolidated `verify_qseries_merged.py` (to be written) will combine these into a single ~10-second run.

## Source paper status (after merger)

| Paper | Status after merger | Action |
|---|---|---|
| `combinatorics/J21/` | MERGED into `J_qseries_merged/` | README updated with merger banner |
| `algebra/J43/` | MERGED into `J_qseries_merged/` | README updated with merger banner |
| `algebra/J51/` | MERGED into `J_qseries_merged/` | README updated with merger banner |

The source folders are retained for citation history; their manuscripts are unchanged.

## What remains

- [ ] Unified prose polish pass (currently §§ are stitched from source content)
- [ ] Write the consolidated `verify_qseries_merged.py`
- [ ] Generate the cover letter for EJC submission
- [ ] §4.4 needs the precise numerical χ-trajectory tables filled in (currently has a TODO)
- [ ] §5 LaTeX equations need rendering check
- [ ] References §9 needs full bibliographic completion (Sanders-Gish citations to other J-series)

**Estimated remaining effort**: 1 week of focused prose work.

## Authors

B.R. Sanders (7Site LLC, Hot Springs, AR) and M. Gish (Independent Researcher).
