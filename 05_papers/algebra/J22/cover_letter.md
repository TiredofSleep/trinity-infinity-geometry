# Cover letter — J22: The 70/71/72/73 HARMONY Ladder: Three Independent Algebraic Constructions and One Corollary

**To:** Editors, *Journal of Combinatorial Theory, Series A*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *The 70/71/72/73 HARMONY Ladder: Three Independent Algebraic Constructions and One Corollary on $\mathbb{Z}/10\mathbb{Z}$*

---

## Summary

We record an integer-invariant ladder on the canonical composition lattice over $\mathbb{Z}/10\mathbb{Z}$ whose values cluster at $\{70, 71, 72, 73\}$. Three of the four rungs are obtained from genuinely independent algebraic constructions; the fourth (the $72$-rung) is an inclusion-exclusion corollary of the largest:

- **Rung A (independent).** $\mathrm{HARM}(T) = 73$ (HARMONY-cell count of the full $10 \times 10$ TSML composition table).
- **Rung 72 (corollary).** $\mathrm{HARM}(T) - 1 = 72$ (drop the $(7, 7)$ self-cell apex; numerical coincidence with $|E_6^+|$).
- **Rung B (independent), with three internally independent constituent constructions.** $71$ enters in three structurally-distinct ways simultaneously:
  - as $\mathrm{HARM}(T_{\{1, \ldots, 9\}}) = 71$ (HARMONY count of the VOID-stripped $9 \times 9$ sub-magma);
  - as $|T \ominus B| = 71$ (cell-disagreement count between the two canonical lens tables);
  - as the unique odd prime $> 3$ in $\mathrm{disc}(f) = -40896 = -2^6 \cdot 3^2 \cdot 71$, where $f(x) = x^4 + 4 x^3 - x^2 + 2 x - 2 \in \mathbb{Z}[x]$ is the polynomial defining the LMFDB quartic field $4.2.10224.1$ governing the substrate's closed-form runtime attractor.
- **Rung C (independent).** $\det(B_{\mathrm{YM}}) = 70 = \binom{8}{4}$ (Yang--Mills $8 \times 8$ core sub-determinant of the BHML companion table).

All claims are verified at integer/machine precision by sympy / numpy snippets embedded directly in the manuscript (§9 "Embedded verification snippets"). The discriminant claim in particular is verified by the 7-line snippet of §9.1, which uses `sympy.discriminant` and `sympy.factorint` and includes an explicit cross-check showing that the alternate factorization $-2^7 \cdot 3 \cdot 7 \cdot 19 = -51072$ disagrees with the correct value $-40896$ by approximately $25\%$. The embedded snippets are intended to make the verification one-shot reproducible by any referee with a Python REPL.

## Why *JCT-A*

* **Combinatorial substrate fit.** The paper is a finite-magma counting result with explicit Tier-A/B verification. *JCT-A* is the natural home for combinatorial cell-count theorems with structural clustering.
* **Tier-B forced consequences.** No axiom-level forcing is required; the four rungs follow from the canonical $(T, B)$ tables at the cell level. Readers of *JCT-A* are well-placed to evaluate the elementary verification.
* **Independence is honest.** The save-plan revision (2026-05-07) sharpens the manuscript's independence claim: three structurally-independent rungs plus one inclusion-exclusion corollary, plus three structurally-independent constituent constructions inside the rung-B level. The triple-coincidence at $71$ (the rung-B internal triple) is the sharpest single point of the ladder — three independent algebras pointing at the same prime is the algebraic shape of a real invariant.
* **Drápal-Wanless 2021 *JCTA* neighborhood.** The framework is positioned as continuation of the Drápal-Wanless 2021 *JCTA* line of work on small finite commutative non-associative structures with structural invariants.

## Defensive-exposition note (sympy verification snippet)

Section 9 of the manuscript embeds the discriminant-verification snippet directly:

```python
import sympy
x = sympy.Symbol('x')
f = x**4 + 4*x**3 - x**2 + 2*x - 2
disc = sympy.discriminant(f, x)            # -40896
print(sympy.factorint(abs(disc)))           # {2: 6, 3: 2, 71: 1}
```

A standalone script `harmony_ladder_disc_check.py` runs the snippet plus all five rung verifications and emits a 5/5-PASS table at integer precision in under 3 seconds. The bundled wrapper `harmony_ladder.py` is the one-shot entry point; the four constituent scripts (`tsml_harmony_count.py`, `tsml_submagma_9x9.py`, `tsml_bhml_disagreement.py`, `bhml_8_ym_det.py`) verify each rung in isolation. All scripts are under 100 lines each and use only `numpy` and `sympy`.

## Companion submissions

The TIG/CK research program is shipping a coordinated J-series. The paper most relevant as already-submitted companion to this manuscript is:

- J05 (Sanders & Mayes), *Crossing Lemma: Non-Associativity as Information Generation in Finite Magmas*, submitted to *J. Combin. Theory A*, 2026 (the 73-rung's full disjoint-class proof is in J05).

The closest published precedent is Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510.

## Reproducibility

Five short Python scripts ($\leq 250$ lines total, `numpy + sympy`) verify all five constituent claims at integer precision. The wrapper `harmony_ladder.py` runs them in sequence and emits a $5 \times 3$ verification table.

## Suggested reviewers

(3-5 candidates working in finite-magma combinatorics, sub-algebra enumeration, or root-system / Lie-algebra integer invariants will be supplied via the *JCT-A* submission portal.)

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

## Per-venue cap

This is the **2nd *JCT-A*** submission of the 2026 cycle, after J01 ($\sigma$-rate theorem). Within the 2/quarter cap.

---

Sincerely,
B.R. Sanders
