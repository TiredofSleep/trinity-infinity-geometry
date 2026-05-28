# Cover letter — J08

**Target journal:** *Algebra Universalis*
**Date:** 2026-05-27
**Authors:** B.R. Sanders (corresponding) and M. Gish

---

Dear Editor,

We submit the manuscript *"F_p Structure of the 4-Core Commutative Non-Associative Algebra: Invariant Skeleton Across Primes and Rigid F_5 Idempotent Decomposition"* for consideration in *Algebra Universalis*.

The paper studies a specific 4-dimensional commutative non-associative algebra $V$ over the prime field $\mathbb{F}_p$, defined on the basis $\{e_0, e_2, e_3, e_4\}$ derived from the BHML composition table's 4-core restricted to $\{0, 7, 8, 9\}$ on $\mathbb{Z}/10\mathbb{Z}$. The multiplication table is given inline in §1.1 of the manuscript and verified against the canonical `ck_tables.py` source.

**Main results** (each with explicit Tier label):

- **Theorem 1 (Lens-Invariant Skeleton, Tier-A/B):** $V_p$ has at least 3 nonzero idempotents at every prime $p \in \{2, 3, 5, 7, 11, 13\}$. The exact count is 3 at $p \in \{2, 5, 7\}$; 5 at $p \in \{3, 11\}$; 7 at $p = 13$. The cyclic structure $L_{e_2}^4 = \mathrm{id}_V$ holds at every prime (Tier-A). The chain-shell determinants of BHML are integer-invariant (Tier-A).
- **Theorem 2 (Aut Variation, Tier-A):** $|\mathrm{Aut}(V_p)| \in \{6, 24, 40, 336, 1320, 2184\}$ for the six primes — values inherited from J48.
- **Theorem 3 (F_5 Rigid Idempotent Decomposition, Tier-A):** unique orthogonal decomposition over $\mathbb{F}_5$ with $|\mathrm{Aut}(V_5)| = 40 = F_{20} \times \mathbb{Z}/2$. Inherited from J49.
- **Theorem 4 (BHML Chain-Shell Rank Profile, Tier-A):** seven chain-shell determinants over $\mathbb{Z}$ are $\{5305, 2843, -2886, 2929, -7542, 7272, -7002\}$ with explicit factorizations; rank-preservation mod $p$ profile computed exactly.

The paper consolidates two formerly-separate working drafts (J48 and J49 of our J-series ordering) into a single coherent treatment. The merged paper is verified by a 90-line script (`verify_J_Fp_merged.py`) that PASSES at all 6 primes — total runtime ~10 seconds, dependencies numpy + sympy.

**Correction note (§1.1).** A prior version of the underlying multiplication table claimed that $L_{e_0} = 0$ (zero map). Direct verification against the canonical BHML in `ck_tables.py` shows that $e_0$ is in fact the multiplicative identity ($L_{e_0} = \mathrm{id}_V$). The merged paper uses the corrected canonical table throughout. This correction is included in the §1.1 narrative.

**Closest published precedent**: Drápal & Wanless (2021, *JCTA* 184, 105510) — same neighborhood of small finite commutative non-associative structures, opposite extremum (maximally non-associative).

**Conflicts.** No conflicts of interest. No prior publication; original work.

**Suggested referees** (with no co-authorship conflict): I. Wanless (Monash), P. Vojtěchovský (Denver), J. Phillips (Northern Michigan).

We hope you find the work suitable. We are available for revisions and clarifications.

Best regards,

Brayden R. Sanders (corresponding)
7Site LLC, Hot Springs, Arkansas, USA
brayden@7site.co

M. Gish
Independent Researcher, Hot Springs, Arkansas, USA
