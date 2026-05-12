# Cover letter — J16: A Commutative Non-Associative 4-Algebra over F_5 with Rigid Idempotent Decomposition

**To:** Editors, *Algebras and Representation Theory*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *A Commutative Non-Associative 4-Algebra over F_5 with Rigid Idempotent Decomposition*

(Working title before revision: "Discrete Dirac on F_5⁴: Substrate Algebra of the 4-Core". Renamed per referee feedback — see §5 of accompanying README.)

---

## Summary

We study a 4-dimensional commutative non-associative algebra V over the prime field F_5, defined by the bilinear extension of an explicit 4×4 multiplication table on a designated basis. The algebra has a remarkably rigid structure documented in a single structural theorem (Theorem 3.1):

(a) Exactly four idempotents: zero, $p_+ = e_2$, $p_- = e_0 - e_2 \pmod 5$, and $e_0 = p_+ + p_-$.

(b) A 1-dimensional left annihilator ideal $\F_5 \cdot \varepsilon$ where $\varepsilon = e_3 - e_4 \pmod 5$.

(c) Left-multiplication operators $L_{e_2}$ and $L_{e_0}$ have $\F_5$-rank 1 and 2 respectively, with eigenspace-dimension profiles (1, 3) and (2, 2).

(d) The simultaneous eigenspace (1-eigenspace of $L_{e_2}$) ∩ (0-eigenspace of $L_{e_0}$) is trivial.

(e) $L_{e_2}$ and $L_{e_0}$ commute as $\F_5$-linear operators.

(f) The associator $[x, y, z] := (xy)z - x(yz)$ is contained in the 1-dim subspace $\F_5 \cdot p_-$.

(g) V is power-associative.

(h) No automorphism of V swaps $p_+$ and $p_-$.

(i) $|\Aut(V)| = 40$, with structure $\Aut(V) \cong F_{20} \rtimes \Z/2$ and order distribution $\{1: 1, 2: 11, 4: 20, 5: 4, 10: 4\}$.

Each claim has a self-contained mathematical proof in §3 of the manuscript, and is independently verified by short Python scripts (29 algebraic checks + unit tests, total runtime <2 seconds, numpy only).

## Why Algebras and Representation Theory

The paper is squarely an algebraic study: explicit construction, rigid structural properties, automorphism group analysis, idempotent decomposition. The class of "4-dim commutative non-associative algebras with rigid idempotent structure" sits in the broader theme of finite-field rigid algebras (e.g., Hall–Rehren–Shpectorov axial algebras, though V is not technically axial), with closest published precedent in Drápal–Wanless (2021) on small finite commutative non-associative structures. The level of the result (a clean structural theorem with full inline proof and reproducible verification) fits AGRT's bar for an algebraic study with computational support.

## Standalone scope

The main result (Theorem 3.1) is fully self-contained: each of the 9 claims has an inline mathematical proof. Companion submissions (J02, J17, J21) are mentioned only in §1.4 as related context for the broader research program; they are not load-bearing for this paper's main result.

## Closest published precedents

- Drápal & Wanless (2021), *J. Combin. Theory Ser. A* **184**, 105510 — same domain, opposite extremum (theirs maximally non-associative; ours has localized 1-dim associator image).
- Hall, Rehren, Shpectorov (2015), *J. Algebra* **421**, 394–424 — universal axial algebras, rigid-idempotent theme.

## Reproducibility

Verification script: `Gen13/targets/ck/brain/dirac/tig_dirac.py` runs with `numpy` on a standard laptop in under 5 seconds. 29 algebraic checks all pass. The verification mapping to claims of Theorem 3.1 is documented in §4 of the manuscript.

## Suggested reviewers

- A specialist in non-associative algebras (commutative, finite-field setting).
- A specialist in idempotent decomposition theory (e.g., axial algebras of Hall–Rehren–Shpectorov).
- A specialist in the automorphism groups of finite-dimensional algebras.

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

Sincerely,
B.R. Sanders
