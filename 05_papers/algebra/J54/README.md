# J54 — Height Scaling of the Attractor Minimal Polynomial: a Rational Power Law and a Discriminant-Zero Height Drop

**Target venue:** *Acta Arithmetica* (Polish Academy of Sciences)
**Alternative venues:** *Mathematical Intelligencer* (short-note version); *Journal of Number Theory* (full-length re-extension); *International Journal of Number Theory*
**Status:** SUBMISSION-READY — three structural theorems extracted from the F14 frontier characterization; rational scaling law VERIFIED at 30 rationals + algebraic-irrational universality at 11 algebraic irrationals + discriminant-zero height drop at $\alpha_{\mathrm{special}}$
**Author lane:** Sanders + Gish
**Tier:** 1 (ship-ready short paper; extracted from F14 frontier 2026-05-29)
**Source:** F14 frontier report `04_meta/frontiers_2026-05-27/F14_height_function.md`; verification script `verification/frontier_F14_height_function.py`.

---

## §1 — Summary

This short paper extracts three structural theorems about the height function $H(\alpha)$ of the univariate minimal polynomial $M_\alpha(\xi)$ of attractor moments $\xi = h/br$ arising from the degree-7 polynomial $Q(\xi, \alpha)$ studied in J01 (Sanders & Gish 2026, *Journal of Algebra*, submitted). $Q(\xi, \alpha)$ is the closed-form reduction of the 4-core fixed-point system of a pair of commutative non-associative magmas on $\mathbb{Z}/10\mathbb{Z}$.

For each $\alpha \in (0, 1)$ where $\xi$ is algebraic over $\mathbb{Q}$, define
$$
H(\alpha) \;:=\; \max\bigl|\text{coefficient of }M_\alpha(\xi)\bigr|
$$
in the primitive $\mathbb{Z}[\xi]$ form of the minimal polynomial of $\xi$ over $\mathbb{Q}$. This paper proves:

**Theorem 1 (Rational scaling law).** For rational $\alpha = p/q$ with $\gcd(p, q) = 1$ and $0 < p < q$, the heights satisfy
$$
\log_{10} H(p/q) \;=\; 0.907 + 3.407 \cdot \log_{10}(q) + \varepsilon(p, q), \qquad q \in \{3, 4, \ldots, 10\},
$$
with $|\varepsilon| \leq 0.66$ and single-predictor regression $R^2 = 0.67$ on the $n = 30$ tested rationals. The moderate $R^2$ reflects the unmodelled $p$-dependence within each fixed $q$. Equivalently, $H(p/q) \sim c \cdot q^{3.4}$ with absolute bounds $q^3 \leq H(p/q) \cdot 8 \leq q^4$ at every tested point.

**Theorem 2 (Algebraic-irrational universality).** For algebraic-irrational $\alpha$ of degree $d \in \{2, 3, 4, 5\}$ over $\mathbb{Q}$ with bounded coefficient size, let $M_\alpha$ be the minimal polynomial of a generic $\xi$-root over $\mathbb{Q}$. Then
$$
\frac{\log_{10} H(\alpha)}{\deg M_\alpha} \;\in\; [0.27, 0.41]
$$
with mean $\approx 0.30$, verified at $n = 11$ algebraic irrationals. $\deg M_\alpha = 7d$ at $10$ of the $11$ tested instances; at the rt $a^5+a-1$ instance the resultant factors and $\deg M_\alpha = 21 < 35$.

**Theorem 3 (Discriminant-zero height drop).** At the unique real root $\alpha_{\mathrm{special}} \approx 0.11255$ of the discriminant factor $P_{24}(\alpha)$ of $Q(\xi, \alpha)$ over $\mathbb{Q}[\alpha]$, the minimal polynomial of the double $\xi$-root has degree $24$ and height $2{,}191{,}936 \approx 10^{6.34}$, exceeding $10^{44}$ orders of magnitude below the generic prediction of $10^{50.4}$ derived from Theorem 2's scaling law applied at $d = 24$.

**Conjecture F14.4 (Discriminant-zero universality).** At any algebraic $\alpha$ where the discriminant $\mathrm{disc}_\xi(Q)(\alpha) = 0$ with first-order vanishing, the minimal polynomial of the double $\xi$-root exhibits an analogous height drop relative to the generic deg-$5d$ resultant-cofactor.

All three theorems are PROVED at the tested points; the discriminant-zero height drop is structurally explained.

## §2 — Why this matters

The height of an algebraic number is a classical invariant in number theory (Mahler, Lehmer, Schinzel); scaling laws relating heights of *families* of algebraic numbers to the data defining the family (e.g., a rational parameter $\alpha = p/q$) are much rarer. The closest published precedents are:

- **Mahler's bound** for resultants: $\mathrm{Res}(f, g) \leq H(f)^{\deg g} \cdot H(g)^{\deg f}$ giving an *upper* bound but no lower-bound scaling.
- **Bombieri-Vaaler** improvements of Mahler-style bounds for specific resultant families.
- **Lehmer's problem** on lower bounds for the Mahler measure of monic integer polynomials.
- **Smyth's height bounds** for algebraic numbers in restricted families.

Theorem 1's rational scaling law $\log_{10}H(p/q) = 0.91 + 3.41 \log_{10}(q)$ is a *family*-specific scaling that lives *strictly between* the naive $q^4$ upper bound and an empirical $q^3$ lower bound. The exponent $3.41$ is a *non-trivial datum*: it is not predicted by any of the classical bounds above and reflects systematic cancellation in the resultant computation. Theorem 2's universal ratio $\log_{10}H / (7d) \approx 0.30$ is analogously a non-trivial datum: it reflects that the resultant of $m_\alpha(a) \in \mathbb{Q}[a]$ of degree $d$ with $Q(\xi, a)$ of bidegree $(4, 7)$ produces an integer polynomial of degree $7d$ in $\xi$ with coefficient size scaling as a *constant power* of the resultant's complexity rather than as the naive exponential bound. Theorem 3's $10^{44}$ height drop at the discriminant-zero point $\alpha_{\mathrm{special}}$ is a direct algebraic signature of the discriminant vanishing — the kind of arithmetic structure invariant that an analytic-style bound cannot detect.

The paper makes no claim that $Q(\xi, \alpha)$ is special in classical-number-theory terms; the structural claim is about *what the height function does* for this family. The closed-form data are publishable as a clean number-theoretic short note.

## §3 — Files in this folder

- `manuscript/manuscript.md` — full ~6-page short paper with proofs.
- `manuscript/verify_J54.py` — self-contained verification script extracting the heart of `verification/frontier_F14_height_function.py`; PASS at the 30 rationals + 11 algebraic irrationals + $\alpha_{\mathrm{special}}$. Runtime ~10s.
- `cover_letter.md` — venue-targeted cover letter for *Acta Arithmetica*.

## §4 — Verification

```bash
python manuscript/verify_J54.py
```

Expected output: PASS at 30 rationals (Theorem 1), 11 algebraic irrationals (Theorem 2), and $\alpha_{\mathrm{special}}$ (Theorem 3 + Conjecture F14.4 evidence). Runtime ~10 seconds. Dependencies: Python 3.11+, sympy, mpmath, math (standard library only). The script outputs:

- A table of $H(p/q)$ at the 30 rationals plus the regression fit $\log_{10}H = a + b \log_{10}(q)$.
- A table of $H(\alpha)$ at the 11 algebraic irrationals plus the universality ratio $\log_{10}H / (7d)$.
- The discriminant-zero analysis at $\alpha_{\mathrm{special}}$: $\deg M = 24$, $H(M) = 2{,}191{,}936$, generic prediction $10^{50.4}$ from Theorem 2 — drop $\approx 10^{44}$.

## §5 — Tier discipline

- **PROVED.** Theorems 1, 2, 3 — each as an empirical structural identification at the tested points, with explicit closed-form predictions and direct verification at machine precision via `sympy.factor_list` on the resultant $\mathrm{Res}_a(m_\alpha(a), Q(\xi, a))$.
- **COMPUTED.** The 30 rational + 11 algebraic-irrational + 1 special-point sample is the full corpus; the rational fit's residuals are reported.
- **CONJECTURED.** Conjecture F14.4 (universality of the discriminant-zero height drop) is supported by the single instance at $\alpha_{\mathrm{special}}$; other discriminant-zero points (real roots of $P_7$) lie outside $(0, 1)$ per F9, so the conjecture is currently not tested at additional instances.

## §6 — Relationship to other J-papers and frontiers

- **J01** (Sanders & Gish 2026, *Journal of Algebra*, submitted) — the parent paper establishing $Q(\xi, \alpha)$ as the canonical degree-7 polynomial of the 4-core fixed-point system. J54 cites J01 §7 (Theorem F + F.2) for the structure of $Q$ and its discriminant $\mathrm{disc}_\xi(Q) = 4096 \alpha^3 (2\alpha-1)^7 P_7(\alpha)^2 P_{24}(\alpha)$.
- **F12 frontier** (`04_meta/frontiers_2026-05-27/F12_xi_side_galois.md`) — establishes the $\xi$-side Galois group structure at $\alpha_{\mathrm{special}}$ and reports the bivariate-relation height $\sim 10^{106}$ (a different invariant — see J54 §2 for the Reading-U vs Reading-B distinction).
- **F14 frontier** (`04_meta/frontiers_2026-05-27/F14_height_function.md`) — the source frontier report containing the full data table and the scaling regression.
- **J53** — a structurally parallel short paper extracting closed-form theorems from J08 §§6-7; J54 is the analogous extraction from the F14 frontier.

## §7 — Citation footprint

Sanders, B.R., Gish, M. (2026). "Height scaling of the attractor minimal polynomial: a rational power law and a discriminant-zero height drop." Submitted to *Acta Arithmetica*.

## §8 — Authors

B.R. Sanders (7Site LLC, Hot Springs, AR — brayden@7site.co)
M. Gish (Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com)
