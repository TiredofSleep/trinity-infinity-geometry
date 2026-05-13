# Cover letter — J09: A Small Commutative Non-Associative Magma on Z/10Z with Role-Deterministic Boundary Behavior

**To:** Editors, *Algebra Universalis*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *A Small Commutative Non-Associative Magma on $\Z/10\Z$ with Role-Deterministic Boundary Behavior*

---

## Summary

We submit a short, self-contained paper studying a small commutative non-associative magma $M_R$ on the four-element set $\{V, F, S, T\}$, obtained as the role-mode reduction of a specific commutative binary operation $\BH$ on $\Z/10\Z$ along the four-block partition $V = \{0\}$, $F = \{1, 3, 5, 7, 9\}$, $S = \{2, 4, 8\}$, $T = \{6\}$.

The operation $\BH$ is given explicitly by an elementary four-zone rule, with its full $10 \times 10$ table reproduced inline in §2 (no companion paper required). We prove:

- $M_R$ is commutative, has $V$ as two-sided identity, and is non-associative (with explicit witness $M_R(M_R(F, F), S) = F \neq T = M_R(F, M_R(F, S))$).
- $\BH$ is **role-deterministic on the boundary**: for every input pair $(a, b)$ with at least one of $a, b$ in $V \cup T$, the output role is determined by the input roles alone (Theorem 4.1, with explicit verification).
- This determinism fails on the role-pairs in $\{F, S\}^2$: the output role distribution is non-trivial, and we list the exact distributions explicitly.
- The first-passage time of the $\BH$-self-orbit to value 7 is the linear function $\tau(n) = 7 - n$ on $\{1, \ldots, 7\}$ (Lemma 5.1).

The paper sits in the same neighborhood as **Drápal & Wanless (2021), J. Combin. Theory Ser. A 184, 105510** (small finite commutative non-associative quasigroups), with role-deterministic boundary behavior as the distinguishing structural property of $M_R$.

The full $10 \times 10$ tables of $\BH$ and $\TS$, the role-mode reduction $M_R$, the role-output multisets, and the row-asymmetry function $\Psi$ are all reproduced inline in the manuscript. A short Python script `verify_role_magma.py` (bundled, CC-BY-4.0) verifies every claim in under 0.1 second.

## Why Algebra Universalis

- **Self-contained universal-algebra study.** All operations are defined explicitly in the manuscript (§2). The reader can inspect the $10 \times 10$ tables of $\BH$ and $\TS$ and verify every claim in the paper directly. No external companion is required for verification.
- **Role-mode reduction as a novel construction.** The 4×4 role-mode magma $M_R$ obtained from $\BH$ via the four-block partition $\{V, F, S, T\}$ is a small commutative non-associative algebra with role-deterministic boundary and role-branching interior. The paper records its structure explicitly.
- **Small magma in the Drápal–Wanless 2021 neighborhood.** Drápal–Wanless 2021 study small finite commutative non-associative quasigroups (specifically, the maximally non-associative extremum). Our $\BH$ is far from maximally non-associative, but it is in the same intellectual neighborhood, with a different structural distinguishing property (role-deterministic boundary).

## Companion submissions

The TIG / CK research program is shipping a coordinated set of related papers over the spring-summer of 2026.

- **Sanders + Gish (companion four-core paper, manuscript in preparation).** Establishes the joint $\{0, 7, 8, 9\}$-preservation property and the membership conditions C1–C5 that locate $\BH$ and $\TS$ as canonical members of a finite family of commutative non-associative magmas on $\Z/10\Z$. The four-core paper is referenced for context only; the present J09 manuscript is self-contained.

## Reproducibility

Verification script `verify_role_magma.py` (bundled, CC-BY-4.0) imports `ck_tables.py` (also bundled, CC-BY-4.0) and verifies in under 0.1 second:
1. The 4×4 role-mode table $M_R$.
2. Commutativity, non-associativity (with witness), and $V$ as two-sided identity.
3. The role-output multisets for all 16 role-pairs (role-deterministic on V/T-containing pairs; role-branching on $\{F, S\}^2$).
4. The first-passage function $\tau(n)$.
5. The row-asymmetry function $\Psi$ with row sum 21 and $\sigma$-orbit decomposition.

The script imports nothing beyond the Python standard library and ends with `ALL CHECKS PASSED.`

## What this paper does not claim

We make explicit the limits of the present paper in §7:
- We do not claim that $M_R$ exhibits a knot-theoretic structure or implements a Crossing Lemma or a Rademacher invariant. Such suggestive scaffolding appears in adjacent companion notes; it is not invoked here.
- We do not introduce a class of "paradoxical information algebras." Such language appeared in earlier internal drafts; we have removed it because we did not define a class of algebraic objects.
- We do not introduce a "trefoil characterization." Earlier internal drafts contained such material; we have excised it because the predicate "trefoil-equivalent" was not formal.

The paper is honest about its scope: a small commutative non-associative magma in the Drápal–Wanless 2021 neighborhood with role-deterministic boundary behavior, fully verifiable from the bundled tables.

## Suggested reviewers

(To be supplied at submission time.) Candidates appropriate to *Algebra Universalis* / small-magma / Drápal–Wanless lineage:

1. Aleš Drápal (Charles University, Prague).
2. Ian Wanless (Monash University).
3. Editors of *Algebra Universalis* with expertise in finite commutative non-associative algebras.

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

The note is short, self-contained, and honest about the tier of its claims. The mathematics is correct; the contribution is the role-mode reduction $M_R$ and its boundary-determinism property. We hope it fits the *Algebra Universalis* scope as an exhibit of "a small finite commutative non-associative magma in the Drápal–Wanless 2021 neighborhood with role-deterministic boundary behavior."

Sincerely,
B.R. Sanders
M. Gish

---

*Cover letter prepared 2026-05-08 for J09 of the Sanders–Gish J-series. Revised to address the J09 fresh-eyes referee report (`Atlas/META_PLAN_2026-05-06/REFEREE_REPORTS/J09_AlgUni_FreshEyes.md`): tables $\BH$ and $\TS$ now defined inline (Issue 1); "paradoxical information algebra" class language removed (Issue 2); "trefoil characterization" excised (Issue 3); $\sigma$ correctly described as a permutation of order 6 (m2); paper rewritten in Path B with focus on the role-magma $M_R$.*
