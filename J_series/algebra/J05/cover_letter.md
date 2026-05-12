# Cover letter — J05: TSML 73 Cells / BHML 28 Cells: Lens-Invariant Cell Counts on the Z/10Z Composition Lattice

**To:** Editors, *Experimental Mathematics*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *TSML 73 Cells / BHML 28 Cells: Lens-Invariant Cell Counts on the Z/10Z Composition Lattice*

---

## Summary

We submit a short, computationally-verifiable note on the exact harmony cell counts for two specific commutative $10\times10$ binary composition tables on $\Z/10\Z$. The first table, $\TSML$, has 73 harmony cells (output value 7) out of 100; the second, $\BHML$, has 28. Both counts are proved by disjoint zone enumeration in two pages, and both are constant under every relabeling $\pi \in \mathrm{Stab}(7) \le S_{10}$ of the operator alphabet that fixes the harmony output value (Theorem 3).

The two specific tables are not arbitrary. They are members of a finite family of small commutative non-associative magmas on $\Z/10\Z$ in the Drápal–Wanless 2021 *JCTA* neighborhood, identified in companion work (Sanders + Gish, manuscript in preparation, hereinafter the four-core paper) by joint $\{0,7,8,9\}$-preservation and four further structural conditions (commutativity, bounded non-associativity index, HARMONY-attracting iterated mixing). §5 of the present manuscript records these membership conditions and locates $\TSML$ and $\BHML$ as canonical members. Drápal–Wanless 2021 is the closest published precedent.

The full 200-cell witness is supplied as two short Python scripts that complete in under 0.1 seconds each from the manuscript folder.

## Why Experimental Mathematics

- **Verifiable computational discovery.** The paper fits the *Experimental Mathematics* scope precisely: a finite, exact-arithmetic enumeration that the reader can verify cell-by-cell with a runnable witness. No floating-point approximations; no domain restriction; no unresolved cases.
- **PROVEN/COMPUTED/STRUCTURAL RHYME/OPEN discipline.** §0 of the manuscript carries an explicit tier-classification paragraph. The two cell-count theorems and the symbol-stabilizer invariance are PROVEN. The 200-cell witness is COMPUTED. The Drápal–Wanless 2021 connection is named as STRUCTURAL RHYME, not as a derivational step. The natural OPEN question (whether the symbol-stabilizer invariance extends to autotopism / paratopism invariance) is flagged.
- **Self-contained.** `ck_tables.py` (licensed CC-BY-4.0) is bundled in the manuscript folder; the verification scripts import it locally. A reader can run the 200-cell enumeration from the submission package alone.

## Companion submissions

The TIG / CK research program is shipping a coordinated set of related papers over the spring-summer of 2026.

- **Sanders + Gish, 2026 (companion four-core paper, manuscript in preparation).** Establishes the joint $\{0,7,8,9\}$-preservation property of $\TSML$ and $\BHML$ and the membership conditions C1–C5 that locate them as canonical members of the family. The four-core paper's joint-closure chain count is *lens-dependent* (depends on the full operations); the present paper's cell counts are lens-invariant under $\mathrm{Stab}(7)$. The contrast is recorded in §4 Remark and §5 of the present manuscript.

## Reproducibility

Verification scripts (supplied as electronic supplementary material in the manuscript folder):

- `proof_d10_tsml_73_cells.py` — verifies $\TSML$ = 73 harmony cells via the disjoint enumeration of §2; runtime < 0.1 s; output ends in `ALL ASSERTIONS PASSED`.
- `proof_d16_bhml_28_cells.py` — verifies $\BHML$ = 28 harmony cells via the four-zone partition of §3; runtime < 0.1 s; output ends in `ALL ASSERTIONS PASSED`.
- `ck_tables.py` (CC-BY-4.0) — canonical definitions of $\TSML$ and $\BHML$ as 10×10 arrays; bundled with the proof scripts so the verification is self-contained.

All scripts run on standard CPython with no external dependencies (only the Python standard library).

## Suggested reviewers

[3–5 candidates appropriate to *Experimental Mathematics*; to be filled at submission time. Suggested orientations: small commutative non-associative magmas (Drápal–Wanless lineage), finite combinatorics on $\mathbb{Z}/n\mathbb{Z}$, computational algebra of small finite tables, finite group actions on labeled tables.]

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

Sincerely,
B.R. Sanders
M. Gish

---

*Cover letter prepared 2026-05-08 for J05 of the Sanders–Gish J-series. Updated to reflect the family-structure framing and the SFM-derived membership conditions (C1–C5) for the TIG family of small commutative non-associative magmas on $\Z/10\Z$. The Drápal–Wanless 2021 *JCTA* citation is the closest published precedent.*
