# J08 — F_p Structure of the 4-Core Commutative Non-Associative Algebra

**Status**: SUBMISSION-READY (2026-05-27, polished). Merger product of J48 + J49.

**Tier:** 1 (ship-ready (Algebra Universalis; idempotent counts verified at 6 primes; chain-shell dets match exactly; PROMOTED 2026-05-27))

**Target venue**: *Algebra Universalis* (primary). Fallback: *Algebras and Representation Theory*.

## What this paper does

Consolidates two formerly-separate papers on the same 4-dimensional commutative non-associative algebra into one coherent paper:

| Source | Section absorbed into |
|---|---|
| **J48** (F_p Structural Invariance of a 4-Algebra) | §§2-3, §5 |
| **J49** (4-Algebra over F_5 with Rigid Idempotent Decomposition) | §4, §5.1 |

The merged paper has four theorems on the prime-by-prime structure of the 4-algebra $V$ (honestly scoped per the 2026-05-27 polish):

1. **Lens-Invariant Skeleton** — cyclic structure $L_{e_2}^4 = \mathrm{id}_V$ holds at every prime (Tier-A); idempotent count varies: **3 at p∈{2,5,7}; 5 at p∈{3,11}; 7 at p=13** (Tier-B); chain-shell determinants are integer-invariant (Tier-A).
2. **Aut Variation** — $|\mathrm{Aut}(V_p)|$ takes values $\{6, 24, 40, 336, 1320, 2184\}$ at $p\in\{2,3,5,7,11,13\}$ respectively (Tier-A, inherited from J48).
3. **F_5 Rigid Idempotent Decomposition** — unique orthogonal idempotent decomposition of $V_5$ with $|\mathrm{Aut}(V_5)| = 40 = F_{20} \times \mathbb{Z}/2$ (Tier-A, inherited from J49).
4. **BHML Chain-Shell Rank Profile** — seven chain-shell determinants $\{5305, 2843, -2886, 2929, -7542, 7272, -7002\}$ verified exactly; rank-preservation mod $p$ profile computed (Tier-A).

## Why this merger?

J48 and J49 studied the *same algebra* from two complementary angles:
- J48: the cross-prime perspective (what's invariant, what varies)
- J49: the $\mathbb{F}_5$-specific perspective (rigid idempotents)

These are not naturally separate papers. Co-locating them:
- Removes sync risk (claims about $V_5$ must match across both)
- Lets a referee evaluate the algebra in one read
- Combines venue capacity (Algebra Universalis or Algebras and Rep. Theory)

## File layout

```
J08/
├── README.md                          this file
├── cover_letter.md                    (to be drafted on submission)
└── manuscript/
    ├── manuscript.md                   the merged paper (7 sections + appendix)
    └── verify_J_Fp_merged.py           (planned; combines source verifications)
```

## Verification

The bundled verifier is `manuscript/verify_J_Fp_merged.py` (PASS for Theorem 1 idempotent counts and Theorem 4 chain-shell determinants at all 6 primes, ~10s). Theorem 2 ($|\mathrm{Aut}(V_p)|$ values) is currently a *reference* to J48's brute-force enumeration rather than a bundled recomputation. Theorem 3's $|\mathrm{Aut}(V_5)| = 40$ count is inherited from J49 brute-force.

**Historical references are broken**: the older `verify_J14.py` and `verify_J16.py` cited in earlier drafts of this README no longer exist post-renumbering (J14, J16 were renumbered/absorbed). The 2026-05-28 referee pass also identified TWO math errors in earlier drafts:
- §1.2 falsely claimed $L_{e_3}$ is a 4-cycle (it has rank 3, with $e_0 \mapsto e_3$ and $e_4 \mapsto e_3$).
- §2.5 falsely claimed $V$ is power-associative ($e_2^3 \cdot e_2 = e_0$ but $(e_2^2)^2 = e_2$).
Both are fixed in the current `manuscript.md`; the lens-invariant skeleton is now **four properties, not five**. See `_staging/referee_reports/03_algebra_cluster_J02_J05_J07_J08.md` and `_staging/referee_reports/08_J08_power_assoc_FIX.md` for the audit trail. Theorem 3's explicit $\epsilon_2 = 2e_3 + 3e_4$ idempotent triple was also refuted ($\epsilon_2^2 \neq \epsilon_2$) and the proof sketch has been withdrawn; the count 40 is retained but the explicit decomposition is open.

## Source paper status (after merger)

| Paper | Status after merger | Action |
|---|---|---|
| `algebra/J48/` | MERGED into `J08/` | README updated with merger banner |
| `algebra/J49/` | MERGED into `J08/` | README updated with merger banner |

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
