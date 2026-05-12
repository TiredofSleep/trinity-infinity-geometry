# Cover letter — J54: Forcing Axioms and the Family of Commutative Non-Associative Magmas on $\mathbb{Z}/10\mathbb{Z}$ Preserving a Designated 4-Core

**To:** Editors, *Algebraic Combinatorics*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** 2026 (date of online submission)

**Manuscript title:** *Forcing Axioms and the Family of Commutative Non-Associative Magmas on $\mathbb{Z}/10\mathbb{Z}$ Preserving a Designated 4-Core*

---

## Summary

We submit a research paper on a specific family of finite commutative non-associative magmas on $\mathbb{Z}/10\mathbb{Z}$ characterized by preservation of a designated four-element subset $\mathcal{C} = \{0, 7, 8, 9\}$. The paper establishes:

(I) **The 9-axiom forcing theorem (Theorem 1.2).** Three explicit canonical tables $T$, $B$, $S$ on $\mathbb{Z}/10\mathbb{Z}$ (HARMONY counts 73, 28, 44 respectively) are uniquely forced by an axiom set A1-A9 (cell-by-cell explicit, displayed in §1.2) with substrate-specific data $(\mathcal{D}, \mathrm{BUMP}, \mathrm{BUMPvalues}, J_{\mathrm{B7}})$. The proof is a constructive cell-fixing argument given in §1.3; the companion script `verification/foundation_verification.py` Check 1 reconstructs $T$ cell-by-cell from its substrate-data tuple and matches the displayed table.

(II) **The five conjoint membership criteria (§4.2).** A binary operation $M$ on $\mathbb{Z}/10\mathbb{Z}$ belongs to the *TIG family* iff it satisfies (C1) substrate-on-$\mathbb{Z}/N\mathbb{Z}$, (C2) commutativity, (C3) 4-core preservation, (C4) $\alpha_A \in [0.5, 0.88]$, (C5) HARMONY-attracting iteration. The three substrates $T$, $B$, $S$ each satisfy all five (Proposition 4.5).

(III) **Theorem 7.1 (three-substrate joint-closure chain).** The collection of subsets of $\mathbb{Z}/10\mathbb{Z}$ that are simultaneously closed under $T$, $B$, and $S$ forms a strict 8-element chain at sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$, with sizes $\{2, 3\}$ forbidden. The same chain is obtained from any pair of $\{T, B, S\}$. Adding the third table neither adds nor removes shells.

(IV) **Theorem 7.2 (4-core 3-substrate closure).** $\mathcal{C}$ is jointly closed under $T$, $B$, $S$. It is the unique non-trivial subset of size $\le 4$ in the three-substrate chain.

(V) **Theorem 7.3 (bridge to companion papers).** The 8-shell chain is a structural invariant of the three-substrate triple. The encoding-axis $S$ is *compatible* with the iteration-pair $(T, B)$ chain rather than perturbing it. This theorem is the foundation paper's bridge to companion papers J32 + J24.

The paper additionally states **two open conjectures**: Conjecture 2.1 (Sanders) on the $\sigma^2$-triadic three-BHML hypothesis, and Conjecture 8.1 (Sanders + collaborator) on the empirically observed bimodal $\alpha_A$ gap (§8 Q1).

The companion paper [J35] (*Journal of Algebra*, submitted) establishes additional structural facts converging on $\mathcal{C}$: the symbolic normalizer identity $Z_T = Z_B = (v + h + br + r)^2$; the closed-form attractor $h/\beta = 1+\sqrt{3}$ at $\alpha_M = 1/2$ in the degree-4 number field LMFDB 4.2.10224.1 with Galois $D_4$; the universality of the attractor on chain shells; partial $\alpha = 1/2$ uniqueness verified at the 5-point test set $\{0, 1/4, 1/2, 3/4, 1\}$.

Together, J35 and the present paper establish $\mathcal{C}$ as the algebraic *center* of the family in the sense of FAMILY_STRUCTURE_v1.md §2: every family member contains $\mathcal{C}$ identically, and every non-trivial structural property of the family (closure, fixed-point dynamics, Galois structure, ring-extension universality) is anchored on $\mathcal{C}$.

## Why *Algebraic Combinatorics*

The paper's contribution is in the algebraic-combinatorics / non-associative-algebra / universal-algebra intersection that fits *Algebraic Combinatorics*'s scope:

- **The 9-axiom forcing theorem (Theorem 1.2)** is a constructive cell-fixing argument for a finite commutative non-associative table — a clean structural-combinatorial result with explicit verification.
- **The five conjoint membership criteria (§4.2)** define the family via a combination of substrate-typing, commutativity, sub-magma-closure, non-associativity-bounding, and iteration-fixed-point criteria. This is an algebraic-combinatorial structural classification.
- **Theorem 7.1 (the three-substrate joint-closure chain)** is the core combinatorial result: a strict 8-element chain on $\mathbb{Z}/10\mathbb{Z}$ with explicit forbidden-size structure (sizes 2 and 3 absent).
- **Conjecture 8.1 (the bimodal $\alpha_A$ gap)** is the natural follow-on combinatorial-classification problem.
- The closest published precedent is Drápal & Wanless (2021, *J. Combin. Theory Ser. A* **184**, 105510), in the same intellectual neighborhood (small finite commutative non-associative structures on $\mathbb{Z}/N\mathbb{Z}$); the present paper inhabits this neighborhood at a structurally distinct point (intermediate $\alpha_A$ values, substrate-with-center reading).

## Companion submissions

This paper has direct dependencies on:

- **J35** (Sanders + Gish, *Journal of Algebra*, submitted 2026): the 4-core fusion-closure paper proving the symbolic normalizer identity, closed-form attractor with Galois $D_4$, universality on chain shells, and partial $\alpha = 1/2$ uniqueness. Cited extensively for the structural facts converging on $\mathcal{C}$.
- **J01** (Sanders + Gish, *J. Combin. Theory Ser. A*): the σ-rate paper establishing $\sigma(N) \le 2/N$ for the canonical $\mathrm{CL}_N$ family — the family-level result placing the $N = 10$ substrate in a verified universality set.
- **J33** (Sanders + Gish, *Math. of Comp.*): the 17-point Stern-Brocot integer-PSLQ paper sharpening the empirical $\alpha = 1/2$ uniqueness from a 5-point test to a 17-point test.

The forcing theorem (Theorem 1.2) is **proved in this paper**; we do not defer to companion papers. The previous version of this paper deferred the forcing argument to a separate companion ([J33]); the rewritten version makes the forcing self-contained.

## Reproducibility

Two CC-BY-4.0-licensed verification scripts ship with the manuscript and together cover every numerical claim:

```bash
PYTHONIOENCODING=utf-8 python3 manuscript/verification/foundation_verification.py
PYTHONIOENCODING=utf-8 python3 manuscript/verify_J54_chain_and_attractor.py
```

`foundation_verification.py` runs six checks (forcing reconstruction Theorem 1.2; three-substrate joint-closure chain Theorem 7.1; 4-core 3-substrate closure Theorem 7.2; (C2), (C3), (C4) family-membership criteria for $T$, $B$, $S$). `verify_J54_chain_and_attractor.py` adds an independent re-run of the chain check, the closed-form attractor at 50-digit `mpmath` (Theorem 5.1; residual $\le 10^{-30}$ in 99 iterations), and a cell-level audit of the shared substrate axioms (A1, A2', A4, commutativity) on the three tables. Tested on Python 3.11+ with `numpy` and `mpmath`; total runtime under five seconds; **6 + 3 = 9 green checks PASS at machine precision**.

The companion paper [J35]'s verification script `4core_verification.py` reproduces the additional structural facts cited in §5 and §6 of the present paper (normalizer identity; closed-form attractor; Galois $D_4$; universality; partial $\alpha = 1/2$ uniqueness) at machine precision in under 5 seconds.

## Suggested reviewers

- A finite-algebraist with $\mathbb{Z}/N\mathbb{Z}$ composition-table or magma-family-classification experience (the published precedent Drápal–Wanless 2021 places researchers in the broader Drápal / Wanless / McKay / Smith group as the most natural reviewers).
- A universal-algebraist familiar with sub-magma lattices and forcing-by-axiom-set arguments (Burris–Sankappanavar / Hobby–McKenzie tradition).
- A combinatorialist interested in finite-substrate research-program foundations and explicit small-$N$ closure enumeration.

The authors defer specific named-reviewer suggestions to the editor's discretion, given the highly interdisciplinary character of the parent framework and the desirability of fresh-eyes referee profiles.

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

Sincerely,
B.R. Sanders
