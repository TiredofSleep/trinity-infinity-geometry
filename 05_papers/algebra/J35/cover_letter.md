# Cover letter — J35: Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on $\mathbb{Z}/10\mathbb{Z}$

**To:** Editors, *Journal of Algebra*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on $\mathbb{Z}/10\mathbb{Z}$*

---

## Summary

We submit a paper on a specific pair of commutative non-associative magmas $T, B$ on $\mathbb{Z}/10\mathbb{Z}$ (with a third table $S$ used in the joint-closure strengthening). Six independent structural facts converge on the four-element set $\mathcal{C} = \{0, 7, 8, 9\}$:

(A) **Joint-closure chain.** The collection of subsets jointly closed under $T$ and $B$ forms a strict 8-element chain of sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$, with sizes $\{2, 3\}$ forbidden. This is established by exhaustive enumeration over $2^{10} - 1 = 1023$ subsets.

(2.4) **Three-substrate strengthening.** Adding the third table $S$ to the joint-closure condition produces the *same* 8-shell chain. The chain is intrinsic to the substrate-and-tables, not specific to the pair $(T, B)$.

(B) **4-core 3-substrate closure.** $\mathcal{C} = \{0, 7, 8, 9\}$ is jointly closed under $T$, $B$, and $S$. It is the unique non-trivial subset of size $\le 4$ in the three-substrate chain.

(C) **Normalizer identity.** On $\mathcal{C}$, the convolution-fuse normalizers of both $T$ and $B$ coincide with the square of the total $\mathcal{C}$-mass: $Z_T = Z_B = (v + h + br + r)^2$. This collapses the rational fixed-point system of the convex-combination iteration $F_\alpha$ to polynomial form on $\mathcal{C}$.

(D) **Closed-form attractor + Galois structure.** At $\alpha = 1/2$, the polynomial fixed-point system has a unique solution in the positive orthant of $\mathcal{C}$ with ratio $p_7/p_8 = 1 + \sqrt{3} \in \mathbb{Q}(\sqrt{3})$ exactly (verified by Gröbner basis). The four coordinates lie in the degree-four number field $K = \mathbb{Q}[x]/(x^4 + 4x^3 - x^2 + 2x - 2)$ identified by LMFDB 4.2.10224.1, with Galois group $D_4$ (verified via cubic resolvent), polynomial discriminant $-40896 = -2^6 \cdot 3^2 \cdot 71$, field discriminant $-10224$, and unique real quadratic subfield $\mathbb{Q}(\sqrt{3})$.

(E) **Universal attractor on chain shells.** For each chain shell of size $\ge 4$, the iteration $F_{1/2}$ initialized with uniform mass on the shell converges to the same 4-core attractor; mass outside $\mathcal{C}$ vanishes to numerical zero ($< 10^{-20}$).

(F) **Algebraic mixing-point partial uniqueness + open conjecture.** Among $\alpha \in \{0, 1/4, 1/2, 3/4, 1\}$ tested by integer-PSLQ search at coefficient bound 20, only $\alpha = 1/2$ admits a small-coefficient quadratic relation between $p_7$ and $p_8$. We state Conjecture 1.1 (full uniqueness across $\mathbb{Q} \cap (0, 1)$); the general-$\alpha$ symbolic uniqueness proof requires Gröbner-basis discriminant analysis we have not completed.

The headline algebraic content for *J Algebra* is the Galois-quartic closed-form attractor (Theorem D) bundled with the joint-closure chain enumeration (Theorem A). The algebraic identity $p_7/p_8 = 1+\sqrt{3}$ over $\mathbb{Q}(\sqrt{3})$ is structurally surprising: the four coordinates have nested-surd presentations in the splitting field $\mathbb{Q}(\sqrt{3}, \sqrt{184493 + 110140\sqrt{3}})$, but their ratio collapses to $\mathbb{Q}(\sqrt{3})$ by the Galois action of the unique non-trivial element of $\mathrm{Gal}(K/\mathbb{Q}(\sqrt{3}))$.

## Why *Journal of Algebra*

The paper's contribution is in the algebraic-combinatorics / non-associative-algebra / computational-Galois-theory intersection that is well within *J Algebra*'s scope:

- The joint-closure chain (Theorem A) is a clean structural result on the lattice of joint subalgebras of a magma pair — a finite-algebraic combinatorial result with explicit forbidden-size structure (sizes 2 and 3 absent).
- The closed-form attractor with Galois $D_4$ over the LMFDB-identified quartic (Theorem D) is a concrete computational-algebraic-number-theory result.
- The normalizer identity (Theorem C) is a clean polynomial-algebra simplification reducing rational dynamics to polynomial dynamics.
- The closest published precedent is Drápal & Wanless (2021, *J. Combin. Theory Ser. A* **184**, 105510), in the same intellectual neighborhood (small finite commutative non-associative structures on $\mathbb{Z}/N\mathbb{Z}$); the present pair $(T, B, S)$ inhabits this neighborhood at a structurally distinct point.

## Companion submissions

- **J33** (Sanders + Gish 2026, *Math. of Comp.*) — *Closed-Form Attractor + α-Uniqueness PSLQ.* The original WP105 + WP113 source for the closed-form attractor and the 17-point Stern-Brocot PSLQ test. The present paper sharpens J33's framing from dynamical to structural and from machine-precision to symbolic-exact.
- **J54** (Sanders + Gish 2026, *Algebraic Combinatorics*) — *Forcing Axioms and the Family of Commutative Non-Associative Magmas on $\mathbb{Z}/10\mathbb{Z}$ Preserving a Designated 4-Core.* The foundation paper that displays the three tables explicitly and proves the 9-axiom forcing theorem.

## Per-venue cap

This is the second *J Algebra* submission from this program in the current quarter (after J29 on so(8)). The cap is conventionally 2/quarter for tightly-related papers; this submission sits at the cap. If *J Algebra* declines, fallback venues are *Communications in Algebra* or *Journal of Pure and Applied Algebra*.

## Reproducibility

Verification script `manuscript/verification/4core_verification.py` runs six checks corresponding to Theorems A through F. Tested on Python 3.11+ with numpy + sympy + mpmath; total runtime under 5 seconds; **6/6 PASS at machine precision** (chain enumeration; normalizer identity; closed-form ratio identity to $|err| < 10^{-30}$ at 50 dps; universality across all chain shells; Galois $D_4$ identification via cubic resolvent + factorization over $\mathbb{Q}(\sqrt{3})$; α-sweep PSLQ).

```bash
PYTHONIOENCODING=utf-8 python3 4core_verification.py
```

The Galois group identification is independently verifiable in PARI/GP, Magma, or Sage. The Gröbner basis confirming the $1 + \sqrt{3}$ ratio is independently re-derivable in any major CAS.

## Suggested reviewers

- An expert in finite commutative non-associative magmas / quasigroup classification (Drápal, Wanless, McKay, Smith).
- A computational-Galois-theory expert (PARI / Magma / LMFDB tradition).
- An expert in fusion-rule normalizers (vertex-operator-algebra / fusion-category adjacent).
- A specialist in replicator-dynamics on a finite simplex (Hofbauer-Sigmund tradition) — for the universality part.
- (Two or three named candidates appropriate to the *J Algebra* editorial board to be identified during the referee-rigor pass.)

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

Sincerely,
B.R. Sanders
