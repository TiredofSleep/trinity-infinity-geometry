# J_Fp_merged — F_p Structure of the 4-Core Commutative Non-Associative Algebra

**Status**: CONSOLIDATED DRAFT (2026-05-27). Merger product of J14 + J16.

**Tier:** 2 (CONSOLIDATED DRAFT 2026-05-27 (merger of J14+J16); awaiting prose polish)

**Target venue**: *Algebra Universalis* (primary). Fallback: *Algebras and Representation Theory*.

## What this paper does

Consolidates two formerly-separate papers on the same 4-dimensional commutative non-associative algebra into one coherent paper:

| Source | Section absorbed into |
|---|---|
| **J14** (F_p Structural Invariance of a 4-Algebra) | §§2-3, §5 |
| **J16** (4-Algebra over F_5 with Rigid Idempotent Decomposition) | §4, §5.1 |

The merged paper has four theorems on the prime-by-prime structure of the 4-algebra $V$:

1. **Lens-Invariant Skeleton** — five structural properties that hold across all $p \in \{2, 3, 5, 7, 11, 13\}$
2. **Aut Variation** — $|\mathrm{Aut}(V_p)|$ takes values $\{6, 24, 40, 336, 1320, 2184\}$ across the primes
3. **F_5 Rigid Idempotent Decomposition** — unique orthogonal idempotent decomposition of $V_5$ with $|\mathrm{Aut}(V_5)| = 40 = F_{20} \times \mathbb{Z}/2$
4. **BHML Chain-Shell Rank Profile** — full prime-by-prime rank pattern of the seven BHML chain shells

## Why this merger?

J14 and J16 studied the *same algebra* from two complementary angles:
- J14: the cross-prime perspective (what's invariant, what varies)
- J16: the $\mathbb{F}_5$-specific perspective (rigid idempotents)

These are not naturally separate papers. Co-locating them:
- Removes sync risk (claims about $V_5$ must match across both)
- Lets a referee evaluate the algebra in one read
- Combines venue capacity (Algebra Universalis or Algebras and Rep. Theory)

## File layout

```
J_Fp_merged/
├── README.md                          this file
├── cover_letter.md                    (to be drafted on submission)
└── manuscript/
    ├── manuscript.md                   the merged paper (7 sections + appendix)
    └── verify_J_Fp_merged.py           (planned; combines source verifications)
```

## Verification

Both source verifications PASS at machine precision:
- J14's `verify_J14.py` (12/12 PASS, ~2s)
- J16's `verify_J16.py`, `verify_discrete_dirac_4core.py`, `test_tig_dirac.py` (all PASS)

The consolidated `verify_J_Fp_merged.py` will combine these into one runner.

## Source paper status (after merger)

| Paper | Status after merger | Action |
|---|---|---|
| `algebra/J14/` | MERGED into `J_Fp_merged/` | README updated with merger banner |
| `algebra/J16/` | MERGED into `J_Fp_merged/` | README updated with merger banner |

The source folders are retained for citation history; their manuscripts are unchanged.

## What remains

- [ ] Unified prose pass (currently stitched from source content)
- [ ] Write consolidated `verify_J_Fp_merged.py`
- [ ] Generate cover letter for Algebra Universalis submission
- [ ] §1.1 multiplication table needs verification against the source BHML restriction
- [ ] §4 idempotent decomposition needs the precise basis-form check
- [ ] References §7 needs full Sanders-Gish citations completed

**Estimated remaining effort**: 1 week of focused prose work.

## Authors

B.R. Sanders (7Site LLC, Hot Springs, AR) and M. Gish (Independent Researcher).
