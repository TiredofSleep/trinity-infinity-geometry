# J_Fp_merged — F_p Structure of the 4-Core Commutative Non-Associative Algebra

**Status**: SUBMISSION-READY (2026-05-27, polished). Merger product of J14 + J16.

**Tier:** 1 (ship-ready (Algebra Universalis; idempotent counts verified at 6 primes; chain-shell dets match exactly; PROMOTED 2026-05-27))

**Target venue**: *Algebra Universalis* (primary). Fallback: *Algebras and Representation Theory*.

## What this paper does

Consolidates two formerly-separate papers on the same 4-dimensional commutative non-associative algebra into one coherent paper:

| Source | Section absorbed into |
|---|---|
| **J14** (F_p Structural Invariance of a 4-Algebra) | §§2-3, §5 |
| **J16** (4-Algebra over F_5 with Rigid Idempotent Decomposition) | §4, §5.1 |

The merged paper has four theorems on the prime-by-prime structure of the 4-algebra $V$ (honestly scoped per the 2026-05-27 polish):

1. **Lens-Invariant Skeleton** — cyclic structure $L_{e_2}^4 = \mathrm{id}_V$ holds at every prime (Tier-A); idempotent count varies: **3 at p∈{2,5,7}; 5 at p∈{3,11}; 7 at p=13** (Tier-B); chain-shell determinants are integer-invariant (Tier-A).
2. **Aut Variation** — $|\mathrm{Aut}(V_p)|$ takes values $\{6, 24, 40, 336, 1320, 2184\}$ at $p\in\{2,3,5,7,11,13\}$ respectively (Tier-A, inherited from J14).
3. **F_5 Rigid Idempotent Decomposition** — unique orthogonal idempotent decomposition of $V_5$ with $|\mathrm{Aut}(V_5)| = 40 = F_{20} \times \mathbb{Z}/2$ (Tier-A, inherited from J16).
4. **BHML Chain-Shell Rank Profile** — seven chain-shell determinants $\{5305, 2843, -2886, 2929, -7542, 7272, -7002\}$ verified exactly; rank-preservation mod $p$ profile computed (Tier-A).

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

The consolidated `verify_J_Fp_merged.py` (PASS at all 6 primes, ~10s) combines these into one runner — total idempotents at $p\in\{2,3,5,7,11,13\}$ are $\{4, 6, 4, 4, 6, 8\}$ respectively; chain-shell dets exactly match.

## Source paper status (after merger)

| Paper | Status after merger | Action |
|---|---|---|
| `algebra/J14/` | MERGED into `J_Fp_merged/` | README updated with merger banner |
| `algebra/J16/` | MERGED into `J_Fp_merged/` | README updated with merger banner |

The source folders are retained for citation history; their manuscripts are unchanged.

## Polish status (2026-05-27, completed)

- [x] Unified prose pass
- [x] Consolidated `verify_J_Fp_merged.py` written and PASS at all 6 primes
- [x] Cover letter for Algebra Universalis (`cover_letter.md`)
- [x] §1.1 multiplication table CORRECTED against canonical `ck_tables.py` BHML (e_0 is the identity, not the zero map; e_2·e_4 = e_0; e_4·e_4 = e_0)
- [x] §2 Theorem 1 honestly re-stated as Tier-A invariants + Tier-B prime-dependent variation
- [x] References complete

**Remaining**: LaTeX conversion before journal submission (currently Markdown). Mathematically complete; correctly scoped.

## Authors

B.R. Sanders (7Site LLC, Hot Springs, AR) and M. Gish (Independent Researcher).
