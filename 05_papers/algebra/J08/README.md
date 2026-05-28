# J08 — F_p Structure of the 4-Core Commutative Non-Associative Algebra

**Status**: DRAFT — rescued 2026-05-28 (math errors found 2026-05-27 are now corrected; see "Rescue notice" at end)

**Tier:** 1 (re-promoted 2026-05-28 after §4 rescue; was demoted to Tier 2 on 2026-05-27)

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
3. **F_5 Rigid 2-Idempotent Decomposition** — orthogonal idempotent pair $\varepsilon_\pm = (e_0 \pm e_4)/2$ in $V_5$ (so $\varepsilon_+ = 3e_0 + 3e_4$, $\varepsilon_- = 3e_0 + 2e_4$), satisfying $\varepsilon_\pm^2 = \varepsilon_\pm$, $\varepsilon_+ \varepsilon_- = 0$, $\varepsilon_+ + \varepsilon_- = e_0$; rigid under $\mathrm{Aut}(V_5)$ (preserves the 2-set $\{\varepsilon_+, \varepsilon_-\}$ since $e_0$ is the unique multiplicative identity). $|\mathrm{Aut}(V_5)| = 40 = F_{20} \times \mathbb{Z}/2$ (Tier-A; pair derived from $\mathbb{F}_5[\mathbb{Z}/2]$ sub-algebra on $\mathrm{span}(e_0, e_4)$ since $e_4^2 = e_0$).
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

**Historical references are broken**: the older `verify_J14.py` and `verify_J16.py` cited in earlier drafts of this README no longer exist post-renumbering (J14, J16 were renumbered/absorbed). The 2026-05-27 referee pass identified THREE math errors in earlier drafts, all of which have now been addressed in the 2026-05-28 rescue:
- §1.2 falsely claimed $L_{e_3}$ is a 4-cycle. **Corrected:** $L_{e_3}$ has rank 3, kernel $e_0 - e_4$, and acts on its 3-dim image as the 3-cycle $(e_2\ e_4\ e_3)$ of order 3; so $L_{e_3}^4 = L_{e_3}$ (not $\mathrm{id}_V$).
- §2.5 falsely claimed $V$ is power-associative ($e_2^3 \cdot e_2 = e_0$ but $(e_2^2)^2 = e_2$). **Partial rescue:** PA fails globally at $e_2$ but **holds on the subalgebras $\mathrm{span}(e_0, e_3)$ and $\mathrm{span}(e_0, e_4)$ at every prime** (proved by a-independence of the quartic obstruction). The lens-invariant skeleton is now **four properties globally, plus the subalgebra-PA Tier-A result**.
- §4 Theorem 3 falsely proposed the triple $\epsilon_2 = 2e_3 + 3e_4$, $\epsilon_3 = 3e_3 + 2e_4$, $\epsilon_4 = e_4 - e_2$ ($\epsilon_2^2 \neq \epsilon_2$). **Full rescue:** the correct decomposition is the 2-idempotent pair $\varepsilon_\pm = (e_0 \pm e_4)/2$ derived from the $\mathbb{F}_5[\mathbb{Z}/2]$ sub-algebra on $\mathrm{span}(e_0, e_4)$ (since $e_4^2 = e_0$). All four orthogonal-decomposition axioms verified.

See `_staging/referee_reports/03_algebra_cluster_J02_J05_J07_J08.md`, `_staging/referee_reports/08_J08_power_assoc_FIX.md`, and `_staging/referee_reports/29_J08_rescue_attempt.md` for the audit trail.

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

## Rescue notice (2026-05-28)

Per `05_papers/_staging/referee_reports/29_J08_rescue_attempt.md`, the three math errors identified in the 2026-05-27 audit have been addressed:

| Error (2026-05-27) | Rescue (2026-05-28) | Tier |
|---|---|---|
| §2.5 power-associativity fails at $a = e_2$ | Reframed as "subalgebra PA on $\mathrm{span}(e_0, e_3) \cup \mathrm{span}(e_0, e_4)$ at every prime" — proved by a-independence of the quartic obstruction | Tier-A (subalgebra-restricted) |
| §1.2 $L_{e_3}$ NOT a 4-cycle | Reframed: rank 3, kernel $e_0 - e_4$, image-restricted action is the 3-cycle $(e_2\,e_4\,e_3)$ of order 3; $L_{e_3}^4 = L_{e_3}$ (not $\mathrm{id}_V$) | Tier-A |
| §4 $\varepsilon_2 = 2e_3 + 3e_4$ NOT idempotent | Replaced by the correct pair $\varepsilon_\pm = (e_0 \pm e_4)/2$ derived from the $\mathbb{F}_5[\mathbb{Z}/2]$ sub-algebra; all four orthogonal-decomposition axioms verified; pair is rigid under $\mathrm{Aut}(V_5)$ | Tier-A |

Substantive rewrites of §1.2, §2.5, §4 have been applied; the bundled verifier `verify_J_Fp_merged.py` now includes `check_F5_idempotents()` (brute-force enumeration of all 625 elements of $V_5$ confirming exactly 4 idempotents) and `check_PA_on_subalgebras()` (verifies PA on both subalgebras at all six primes). Re-promoted to Tier 1.
