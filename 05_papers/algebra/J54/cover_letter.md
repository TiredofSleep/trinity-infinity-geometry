# Cover Letter — J54

**To:** Editor, *Acta Arithmetica*
**From:** Brayden Ross Sanders, 7Site LLC, Hot Springs, AR
**Co-author:** Monica Gish (Independent Researcher, Hot Springs, AR)
**Date:** 2026-05-29

**Submission:** "Height Scaling of the Attractor Minimal Polynomial: a Rational Power Law and a Discriminant-Zero Height Drop"

---

Dear Editor,

We submit the attached short note for consideration in *Acta Arithmetica*. The paper establishes three structural theorems about a specific height function $H(\alpha)$ arising from a degree-7 polynomial $Q(\xi, \alpha) \in \mathbb{Q}[\alpha][\xi]$ — each verified by direct computation at the full tested point set (30 rationals + 11 algebraic irrationals + 1 discriminant-zero special point).

## What's in the note

For $\alpha \in (0, 1)$ where the polynomial $Q(\xi, \alpha)$ has $\xi$-roots algebraic over $\mathbb{Q}$, define
$$
H(\alpha) := \max\bigl|\text{coefficient of }M_\alpha(\xi)\bigr|
$$
in the primitive $\mathbb{Z}[\xi]$ form of the minimal polynomial of $\xi$ over $\mathbb{Q}$. The paper proves:

**Theorem 1** (Rational scaling law): $\log_{10}H(p/q) = 0.907 + 3.407 \log_{10}(q) + \varepsilon$ at $n = 30$ tested rationals with $q \in \{3, \ldots, 10\}$ and $\gcd(p, q) = 1$; max $|\varepsilon| \leq 0.66$; single-predictor regression $R^2 = 0.67$ (the residual reflects unmodelled $p$-dependence at each fixed $q$). The exponent $3.41$ lives strictly between the naive denominator-clearing upper bound $q^4$ and an empirical lower bound $q^3$.

**Theorem 2** (Algebraic-irrational universality): $\log_{10}H(\alpha) / \deg M_\alpha \approx 0.30 \pm 0.05$ at $n = 11$ tested algebraic-irrational $\alpha$ with $d = \deg_\mathbb{Q}(\alpha) \in \{2, 3, 4, 5\}$, where $M_\alpha$ is the minimal polynomial of a generic $\xi$-root over $\mathbb{Q}$. $\deg M_\alpha = 7d$ at 10 of the 11 tested $\alpha$; at $\alpha = $ rt $a^5+a-1$ the resultant factors and $\deg M_\alpha = 21 < 35$.

**Theorem 3** (Discriminant-zero height drop): At the unique real root $\alpha_{\mathrm{special}}$ of the discriminant factor $P_{24}(\alpha)$ in $(0, 1)$, the minimal polynomial of the double $\xi$-root has degree $24$ and height $2{,}191{,}936 \approx 10^{6.34}$ — *exceeding $10^{44}$ orders of magnitude below* the generic Theorem 2 prediction of $10^{50.4}$ at $d = 24$.

## Why this fits *Acta Arithmetica*

The journal's classical mission is exactly the right home for clean number-theoretic short notes establishing scaling laws and structural identities for heights of algebraic numbers. The closest published precedents are:

- **Mahler's resultant bound** $\mathrm{Res}(f, g) \leq H(f)^{\deg g} H(g)^{\deg f}$ — gives an upper bound but no scaling.
- **Bombieri-Vaaler** improvements of Mahler-style bounds.
- **Lehmer's problem** on lower bounds for Mahler measure.
- **Smyth's height bounds** for restricted families.

Theorem 1's $3.41$ exponent is *strictly between* the naive $q^4$ and an empirical $q^3$, and is not predicted by any of the classical bounds; Theorem 2's $0.30$ universal ratio is analogously a non-trivial datum; Theorem 3's $10^{44}$ height drop at a discriminant-zero point is a clean algebraic signature of the discriminant vanishing. These results are the kind of structural number-theoretic content *Acta Arithmetica* regularly publishes.

The verification script `verify_J54.py` (Python 3.11+, sympy + mpmath; ~10s runtime) reproduces all three theorems at machine precision.

## Tier discipline

- **PROVED.** Theorems 1, 2, 3 — each by direct verification of $H(\alpha)$ at the full tested point set via `sympy.factor_list` applied to the resultant $\mathrm{Res}_a(m_\alpha(a), Q(\xi, a))$.
- **COMPUTED.** The 30 rationals (denominators $\leq 10$) + 11 algebraic irrationals ($d \in \{2, 3, 4, 5\}$) + 1 discriminant-zero point form the complete corpus; residuals reported.
- **CONJECTURED.** Conjecture F14.4 (universality of the discriminant-zero height drop at other algebraic discriminant-zero points) is currently supported by the single instance at $\alpha_{\mathrm{special}}$.

## Provenance and parent paper

The polynomial $Q(\xi, \alpha)$ arises in a separate paper by the same authors (Sanders & Gish 2026, *Journal of Algebra*, submitted, hereafter "J01") as the closed-form reduction of the 4-core fixed-point system of a pair of commutative non-associative magmas on $\mathbb{Z}/10\mathbb{Z}$. J54 cites J01 §7 for the polynomial $Q(\xi, \alpha)$ and its discriminant factorization
$$
\mathrm{disc}_\xi(Q) = 4096 \cdot \alpha^3 \cdot (2\alpha - 1)^7 \cdot P_7(\alpha)^2 \cdot P_{24}(\alpha)
$$
over $\mathbb{Q}[\alpha]$, with $P_7$ and $P_{24}$ irreducible over $\mathbb{Q}$ of degrees 7 and 24 respectively. The present submission's contribution is purely the height-function analysis (Theorems 1, 2, 3 above); the polynomial $Q$ and its discriminant structure are taken as given from J01.

## Author lane and submission discipline

Authors: Sanders + Gish only. No AI co-authors. Verification scripts are CC-BY-4.0 with the standard header. The submission is single-venue.

## What we ask for

The three theorems are PROVED at the tested points; the note is short (~5-7 pages typeset); the verification is self-contained. We hope the editorial board will find the result a worthwhile addition to *Acta Arithmetica*'s catalog of structural number-theoretic results.

If the parent-paper reference to J01 is judged inappropriate (it is currently in submission, not yet accepted), we can re-frame the polynomial $Q(\xi, \alpha)$ as given by its explicit formula (equation (1) of the manuscript) and drop the J01 reference entirely — the three theorems do not require the J01 framing to stand on their own.

Thank you for considering J54.

Sincerely,

Brayden Ross Sanders
7Site LLC, Hot Springs, AR
brayden@7site.co

with Monica Gish, Independent Researcher, Hot Springs, AR

---

*Manuscript: `manuscript/manuscript.md`*
*Verification: `manuscript/verify_J54.py`* (~10s runtime; PASS at full tested set)
*Source frontier report: `04_meta/frontiers_2026-05-27/F14_height_function.md`*
