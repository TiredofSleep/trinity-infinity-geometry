# J09 — A Small Commutative Non-Associative Magma on Z/10Z with Role-Deterministic Boundary Behavior

**Status:** REVISED (2026-05-08; Path-B rewrite per fresh-eyes referee + SFM family-structure context)
**Phase:** Phase 1
**Target venue:** Algebra Universalis
**Author lane:** Sanders + Gish
**Tier:** B (small finite commutative non-associative magma; role-mode reduction)

---

## §1 — Manuscript

**Local path:** `manuscript/manuscript.tex` (amsart, ~10 pages)

**Abstract (1-sentence):** A small commutative non-associative magma $M_R$ on $\{V, F, S, T\}$, obtained as the role-mode reduction of a specific commutative binary operation $\BH$ on $\Z/10\Z$ along the four-block partition $V = \{0\}, F = \{1,3,5,7,9\}, S = \{2,4,8\}, T = \{6\}$, with the property that $\BH$ is *role-deterministic on the boundary* (output role determined by input roles whenever at least one input is in $V \cup T$) and *role-branching on the interior* $\{F, S\}^2$.

Files in this J-folder's `manuscript/`:

- `manuscript.tex` (main submission file; amsart)
- `ck_tables.py` (CC-BY-4.0; the two tables $\TS$ and $\BH$ explicit, plus the role partition and $\sigma$ permutation)
- `verify_role_magma.py` (verification script — runs in <0.1 s and ends with `ALL CHECKS PASSED.`)

## §2 — Verification script

**Local path:** `manuscript/verify_role_magma.py`

Verifies (in <0.1 s on a standard laptop):
1. The 4×4 role-mode table $M_R$ from $\BH$ via the role partition.
2. $M_R$ is commutative, has $V$ as two-sided identity, and is non-associative (with explicit witness $M_R(M_R(F,F),S) = F \neq T = M_R(F, M_R(F,S))$).
3. $\BH$ is role-deterministic on every input pair containing $V$ or $T$, and role-branching on $\{F,S\}^2$, with the exact role-output multisets listed in Theorem 4.1.
4. The first-passage time $\tau(n) = 7-n$ on $\{1, \ldots, 6\}$ for the $\BH$-self-orbit; $\tau(8) = 1$; $\tau(0) = \tau(9) = \infty$.
5. The row-asymmetry function $\Psi$ and its $\sigma$-orbit decomposition: $\Psi(\Z/10\Z) = 21 = T_6$; $\Psi(\sigma\text{-fixed}) = -1$; $\Psi(\sigma\text{-cycle}) = 22$.

Output ends with `ALL CHECKS PASSED.`

## §3 — Dependencies

- **Companion four-core paper (Sanders + Gish, manuscript in preparation):** establishes the joint $\{0,7,8,9\}$-preservation and the broader algebraic family in which $\BH$ and $\TS$ are canonical members. Cited in §1 (closest published precedent paragraph) and §6 (open questions) of the J09 manuscript.
- **Drápal & Wanless (2021), JCTA 184 (2021), 105510:** closest published precedent for the small commutative non-associative magma neighborhood. Cited in §1 (closest published precedent paragraph).

## §4 — Cover letter

See `cover_letter.md` in this folder. Updated to reflect referee-driven revisions.

## §5 — Notes (post-revision 2026-05-08)

**Status: REVISED to address J09 fresh-eyes referee report (`Atlas/META_PLAN_2026-05-06/REFEREE_REPORTS/J09_AlgUni_FreshEyes.md`).**

The major referee critiques were:
1. **TS and BH operations not defined in the paper.** Reader had to consult an unavailable companion paper.
2. **"Paradoxical information algebra" undefined.** Title and abstract named a class without defining it.
3. **§1.1 called the 6-cycle σ an "involution" — it has order 6, not 2.**
4. **Trefoil characterization predicated on undefined "runtime processor."**
5. **Save plan recommended Path B rewrite focusing on the role-magma $M_R$.**

The revised manuscript adopts **Path B**:

1. **Tables $\TS$ and $\BH$ are now defined explicitly inline** (§2, Tables 1 and 2). The reader can verify every claim without consulting any companion paper. The bundled `ck_tables.py` is an electronic copy of the same tables.
2. **"Paradoxical information algebra" removed from title and abstract.** New title: *"A Small Commutative Non-Associative Magma on $\Z/10\Z$ with Role-Deterministic Boundary Behavior."* The class language is dropped; the role-mode reduction $M_R$ is presented as a specific small finite commutative non-associative magma on $\{V, F, S, T\}$.
3. **§1.1 corrected: $\sigma$ is described as a permutation of order 6, not an involution.** The actual involution $\sigma^3 = (1\,5)(2\,6)(4\,7)(0)(3)(8)(9)$ is named explicitly when referenced.
4. **Trefoil characterization removed entirely.** The "What this paper does not claim" section explicitly states the paper does not introduce a trefoil characterization; the predicate is not formal.
5. **Path B applied: focus is on $M_R$ as a small algebra.** Theorem 3.2 (commutativity / non-associativity), Theorem 3.3 (V is two-sided identity), Theorem 4.1 (role-deterministic boundary, role-branching interior with explicit multisets), and Lemma 5.1 (linear first-passage time on $\{1, \ldots, 6\}$) are the load-bearing results. The row-asymmetry $\Psi$ is recorded as a side observation; the $\Psi(\Z/10\Z) = 21 = T_6$ row sum and the $\sigma$-orbit decomposition are facts; the Fibonacci row-decomposition does *not* hold for $\Psi$ on the full $\Z/10\Z$ and is honestly retracted in Remark 6.2.
6. **Suggestive terminology stripped.** "Trefoil-equivalent," "paradoxical information algebra," "the runtime processor," "Crossing Lemma," "Rademacher invariant" all removed from the body; only mentioned in the "What this paper does not claim" section as language we are explicitly *not* using.

### Family-Structure framing (per `Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md`)

The two operations $\BH$ and $\TS$ are members of the TIG family of commutative non-associative magmas on $\Z/10\Z$ identified in companion work; the family is defined by 5 conjoint membership criteria (C1–C5) with the joint $\{0, 7, 8, 9\}$-preservation as the load-bearing fact. The closest published precedent for this neighborhood is **Drápal & Wanless (2021), J. Combin. Theory Ser. A 184, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN.** $M_R$ is commutative, has $V$ as two-sided identity, and is non-associative (Theorems 3.1, 3.2). $\BH$ is role-deterministic on every input pair containing $V$ or $T$, role-branching on $\{F, S\}^2$ with the explicit multisets (Theorem 4.1). $\tau(n) = 7 - n$ on $\{1, \ldots, 7\}$ (Lemma 5.1).
- **COMPUTED.** `verify_role_magma.py` verifies the role-mode table, the role-output distributions, the period function, and the row-asymmetry function in <0.1 s.
- **STRUCTURAL RHYME.** The row-asymmetry sum $\Psi(\Z/10\Z) = 21 = T_6$ (sixth triangular number) is recorded as a numerical observation; the $\sigma$-orbit decomposition $\{-1, 22\}$ is recorded as a numerical observation. Neither is asserted as a structural theorem.
- **OPEN.** A characterization of the role partition $\{V, F, S, T\}$ as a congruence of some derived structure (it is not a congruence of $\BH$ itself). Whether analogous role-deterministic-boundary algebras exist on $\Z/14\Z$, $\Z/18\Z$, $\Z/12\Z$.

### Lens-ownership (§0)

The substrate is $\Z/10\Z$ with two specific commutative tables $\BH$ and $\TS$ defined explicitly in §2 by elementary rules; the four-block role partition $\{V, F, S, T\}$ is a labeling-by-fiat motivated by an interpretive reading not used in the proofs.

### Hardening status

- License: `ck_tables.py` and `verify_role_magma.py` are CC-BY-4.0 (verified)
- AI-attribution: removed
- Author lane: Sanders + Gish
- Drápal–Wanless 2021 cited (verified)
- $\sigma$ correctly described as order-6 permutation (not "involution")
- Tables $\TS$ and $\BH$ inline in §2 (referee Issue 1 addressed)
- "Paradoxical information algebra" / "trefoil" / "runtime processor" excised (referee Issues 2, 3 addressed)

## §6 — Submission checklist

- [x] Manuscript .tex finalized with Path-B rewrite (2026-05-08)
- [x] Verification script `verify_role_magma.py` green (`ALL CHECKS PASSED.`)
- [x] Tables $\TS$ and $\BH$ defined inline (referee Issue 1)
- [x] $\sigma$ correctly described as order-6 permutation (m2)
- [x] "Paradoxical information algebra" / "trefoil" / "runtime processor" removed (Issues 2, 3)
- [x] Tier-classified PROVEN/COMPUTED/RHYME/OPEN paragraph in §0
- [x] Lens-ownership paragraph
- [x] Cover letter updated
- [x] Drápal–Wanless 2021 cited (closest published precedent)
- [ ] Brayden's referee-rigor pass complete
- [ ] Submitted

---

## §7 — Citation footprint

Sanders, B.R., Gish. (2026). "A Small Commutative Non-Associative Magma on $\Z/10\Z$ with Role-Deterministic Boundary Behavior." Submitted to *Algebra Universalis*.
