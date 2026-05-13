# WP113 — α-Uniqueness via PSLQ: A Stern-Brocot Sharpening of WP105 D42

**Authors:** Brayden Sanders (Anthropic Code session, 2026-04-26)
**Status:** EMPIRICAL (sharpened); structural uniqueness theorem remains open. F3 from `Atlas/FRONTIERS_2026_04_25.md` advanced (not closed).
**Verification:** `papers/wp113_alpha_uniqueness/verification/alpha_pslq_sweep.py` (high-precision mpmath; PSLQ; 17 Stern-Brocot fractions).
**Companion papers:** WP105 (closed-form runtime attractor), WP110 (4-core fusion-closure), WP112 (operad fuse).

---

## Abstract

WP105 (D42) established empirically, via a 19-point linspace sweep over $\alpha \in [0.05, 0.95]$, that $\alpha = 1/2$ is the unique mixing weight at which the T+B-mix runtime attractor admits a small-coefficient quadratic relation in $H/Br$ and a small-coefficient quartic in $r/br$. This paper sharpens that observation by:

(i) Replacing the 19-point linspace grid with a **17-point Stern-Brocot grid** of all rationals $p/q$ with $q \leq 7$ in $(0, 1)$.

(ii) Computing the runtime attractor at **50-digit precision** (mpmath) instead of double precision.

(iii) Replacing the brute-force coefficient search (max $\pm 10$ for quadratic, $\pm 5$ for quartic) with the **PSLQ algorithm** (Ferguson–Bailey 1998), tested at degree $\leq 8$ with coefficient bound $\leq 50$.

**Result.** $\alpha = 1/2$ remains the **unique rational** in the Stern-Brocot grid where the attractor admits algebraic relations for *both* $H/Br$ and $r/br$ within the tested bounds. The recovered relations are exactly:

- $H/Br$: $x^2 - 2x - 2 = 0$ (degree 2, sup-coefficient 2; positive root $1 + \sqrt{3}$)
- $r/br$: $x^4 + 4x^3 - x^2 + 2x - 2 = 0$ (degree 4, sup-coefficient 4; LMFDB 4.2.10224.1)

For each of the **16 other rational $\alpha$ values** in the grid, PSLQ finds no integer-coefficient polynomial relation at degree $\leq 8$ with coefficients $\leq 50$. The numerical $H/Br$ values at these other rationals do not appear to be algebraic numbers of bounded complexity.

This empirically supports the F3 conjecture that $\alpha = 1/2$ is the unique rational mixing weight producing an algebraic runtime attractor over $\mathbb{Q}$. A structural proof remains open.

---

## 1. The runtime attractor (recap)

Per WP105 §2 / D38, the T+B-mix runtime processor on $\mathbb{Z}/10\mathbb{Z}$ is the iteration
$$ p_{n+1} = \mathrm{normalize}_{\ell_1}\!\left( \alpha \cdot \mathrm{normalize}_{\ell_1}(p_n \otimes_T p_n) + (1 - \alpha) \cdot \mathrm{normalize}_{\ell_1}(p_n \otimes_B p_n) \right) $$
where $\otimes_T$ and $\otimes_B$ are the bilinear fusions induced by the canonical TSML and BHML tables. Starting from the uniform distribution on the 4-core $\{V, H, Br, R\} = \{0, 7, 8, 9\}$, the iteration converges to a fixed-point distribution $p^*(\alpha)$ supported entirely on the 4-core (D38; strengthened to structural in WP110 D48).

Define the runtime ratios:
$$ R_{H/Br}(\alpha) := \frac{p^*_7(\alpha)}{p^*_8(\alpha)},\qquad R_{r/br}(\alpha) := \frac{p^*_9(\alpha)}{p^*_8(\alpha)}. $$

WP105 D39 / D40 establish:
- $R_{H/Br}(1/2) = 1 + \sqrt{3}$ exactly.
- $R_{r/br}(1/2)$ is the unique positive real root of the irreducible monic integer quartic $x^4 + 4x^3 - x^2 + 2x - 2$, with Galois group $D_4$ over $\mathbb{Q}$ and number-field LMFDB 4.2.10224.1.

The question this paper sharpens: *for which other rational $\alpha$, if any, are $R_{H/Br}(\alpha)$ and $R_{r/br}(\alpha)$ algebraic over $\mathbb{Q}$ of bounded degree and coefficient?*

---

## 2. Method: PSLQ on a Stern-Brocot grid

**Grid.** All rationals $p/q$ with $q \leq 7$ in $(0, 1)$:
$$ \mathcal{G} = \left\{ \tfrac{1}{7}, \tfrac{1}{6}, \tfrac{1}{5}, \tfrac{1}{4}, \tfrac{2}{7}, \tfrac{1}{3}, \tfrac{2}{5}, \tfrac{3}{7}, \tfrac{1}{2}, \tfrac{4}{7}, \tfrac{3}{5}, \tfrac{2}{3}, \tfrac{5}{7}, \tfrac{3}{4}, \tfrac{4}{5}, \tfrac{5}{6}, \tfrac{6}{7} \right\}, \quad |\mathcal{G}| = 17. $$
Stern-Brocot density at depth 7 covers all rationals of denominator $\leq 7$, well distributed across $(0, 1)$.

**Precision.** Each iteration is performed in 50-digit mpmath precision; convergence threshold $\tau = 10^{-45}$. Maximum iteration: 4000 (typical convergence at 60–110 iterations).

**Detection.** For each $\alpha \in \mathcal{G}$ and each of the two ratios $R_{H/Br}, R_{r/br}$, we apply the PSLQ algorithm (Ferguson–Bailey 1998 / `mpmath.pslq`) to the basis $\{1, x, x^2, \ldots, x^d\}$ for $d \in \{2, 3, \ldots, 8\}$, with coefficient bound $|c| \leq 50$. We report the lowest-degree relation found (if any).

A "no algebraic relation found" result means: PSLQ returned no integer relation $\sum_{i=0}^d c_i x^i = 0$ with $|c_i| \leq 50$ at residual $< 10^{-42}$. This is consistent with (but does not prove) $x$ being transcendental, or algebraic of degree $> 8$, or algebraic of degree $\leq 8$ with at least one coefficient $> 50$ in absolute value.

---

## 3. Results

### 3.1. Full sweep table

| $\alpha$ | $H/Br$ | $H/Br$ min poly | $r/br$ | $r/br$ min poly |
|:--:|:--:|:--|:--:|:--|
| 1/7 | 1.000080 | (none) | 0.780785 | (none) |
| 1/6 | 1.094392 | (none) | 0.788716 | (none) |
| 1/5 | 1.235697 | (none) | 0.793601 | (none) |
| 1/4 | 1.461835 | (none) | 0.787595 | (none) |
| 2/7 | 1.629774 | (none) | 0.774960 | (none) |
| 1/3 | 1.859036 | (none) | 0.750164 | (none) |
| 2/5 | 2.190696 | (none) | 0.705517 | (none) |
| 3/7 | 2.338368 | (none) | 0.684114 | (none) |
| **1/2** | **2.732051** | **$x^2 - 2x - 2$** | **0.626785** | **$x^4 + 4x^3 - x^2 + 2x - 2$** |
| 4/7 | 3.184547 | (none) | 0.565063 | (none) |
| 3/5 | 3.391977 | (none) | 0.539106 | (none) |
| 2/3 | 3.971437 | (none) | 0.474987 | (none) |
| 5/7 | 4.514388 | (none) | 0.425279 | (none) |
| 3/4 | 5.038776 | (none) | 0.385232 | (none) |
| 4/5 | 6.061249 | (none) | 0.324242 | (none) |
| 5/6 | 7.068410 | (none) | 0.279815 | (none) |
| 6/7 | 8.069565 | (none) | 0.245986 | (none) |

(Column "(none)" means: no integer-coefficient polynomial relation found at degree $\leq 8$, $|c| \leq 50$, residual $< 10^{-42}$.)

### 3.2. Theorem (PSLQ Verdict)

**Theorem 3.2.** *Among the 17-point Stern-Brocot grid $\mathcal{G}$ above, $\alpha = 1/2$ is the unique rational at which both $R_{H/Br}(\alpha)$ and $R_{r/br}(\alpha)$ are PSLQ-detectable algebraic over $\mathbb{Q}$ within (degree $\leq 8$, coefficient $\leq 50$). The recovered minimum polynomials are:*
$$ R_{H/Br}(1/2) : x^2 - 2x - 2 = 0, \qquad R_{r/br}(1/2) : x^4 + 4x^3 - x^2 + 2x - 2 = 0. $$
*PSLQ residuals at 50-digit precision: $3.14 \times 10^{-45}$ and $4.38 \times 10^{-46}$ respectively.*

**Proof.** Direct computation; see `alpha_pslq_sweep.py` Section "Per-alpha PSLQ table." $\square$

### 3.3. Sharpening of WP105 D42

WP105 D42 was stated for a 19-point uniform linspace grid in $[0.05, 0.95]$ at double precision, with brute-force coefficient search bounded by $\pm 10$ (quadratic) and $\pm 5$ (quartic). Theorem 3.2 sharpens this in three independent dimensions:

(i) **Grid quality.** Stern-Brocot grid of denominator $\leq 7$ (17 points, all rationals) replaces the linspace grid. Every rational in $(0, 1)$ with $q \leq 7$ is tested; no rational is "between grid points."

(ii) **Numerical precision.** 50 digits of mpmath precision replace double precision (16 digits). Spurious algebraic-relation false positives from numerical noise are eliminated.

(iii) **Detection method.** PSLQ replaces brute-force enumeration. Coefficient bound increased from $(\pm 10, \pm 5)$ to $\pm 50$ uniformly, and degree extended from $\{2, 4\}$ to $\{2, 3, \ldots, 8\}$.

Across all 17 rationals tested, $\alpha = 1/2$ remains uniquely algebraic. The empirical case for "only $\alpha = 1/2$ admits an algebraic attractor" is correspondingly stronger.

---

## 4. Discussion

### 4.1. What this is and is not

**This IS:** A sharpened empirical result. It says: out of 17 specific rational mixing weights with denominator $\leq 7$, only one (the symmetric mixing weight $1/2$) produces a runtime attractor whose ratios are detectably algebraic at modest complexity.

**This is NOT:** A proof that the runtime attractor is transcendental (or even non-low-degree-algebraic) at every rational $\alpha \neq 1/2$. PSLQ failure at the (degree, coefficient) bounds tested is *consistent with* but does not *imply* transcendence. The complete uniqueness theorem requires either:

(a) A symbolic computation showing the attractor is in $\mathbb{Q}(\sqrt{3}, \xi)$ (the WP105 number field) iff $\alpha = 1/2$ — which sympy could not solve at general $\alpha$ in prior attempts (per WP105 §6 sweep notes), or

(b) A structural argument identifying $\alpha = 1/2$ as a singular point of an algebraic variety governing the attractor — speculative, no clear path.

### 4.2. Conjecture (Strong α-uniqueness)

**Conjecture 4.2.** *For every rational $\alpha \in (0, 1) \setminus \{1/2\}$, the runtime attractor coordinates $p^*_i(\alpha)$ are transcendental over $\mathbb{Q}$.*

This paper's evidence: 16 PSLQ attempts at modest bounds, all negative. A larger Stern-Brocot grid (say $q \leq 12$, 60+ points) at higher precision (200+ digits) and degree 12 with coefficient bound 200 would deepen the empirical case. None of these computations are intractable; they would benefit from being run.

### 4.3. Why $\alpha = 1/2$ is special

The mixing weight $\alpha = 1/2$ has three structural distinguishing features:

(i) **$\sigma_{\text{outer}}$ symmetry.** At $\alpha = 1/2$, the T+B-mix is symmetric under exchanging the two tables: $\alpha \cdot T + (1 - \alpha) \cdot B$ is invariant under $T \leftrightarrow B$ combined with $\alpha \leftrightarrow 1 - \alpha$. Other rational $\alpha$ break this symmetry.

(ii) **Joint normalizer simplification (WP110 D49).** At the 4-core attractor, $Z_T = Z_B = (v + h + br + r)^2$ — the TSML and BHML normalizers coincide. The T+B-mix at $\alpha = 1/2$ becomes the self-dual fixed-point operator on the 4-core; at other $\alpha$, the T-side and B-side normalizers contribute asymmetrically.

(iii) **Dirichlet/Galois cleanup.** The closed form $1 + \sqrt{3}$ (and the quartic in LMFDB 4.2.10224.1 with Galois $D_4$) sit in a number field whose Galois group matches the $D_4 = \langle P_{56}, \sigma^3 \rangle$ symmetry of WP104. At $\alpha = 1/2$, the runtime DOF and the gauge-symmetry DOF agree on the same Galois group.

Together, these three structural features give a heuristic explanation for why $\alpha = 1/2$ might be the *unique* algebraic point in the rationals. None of them is a proof.

---

## 5. Reproduction

```
cd papers/wp113_alpha_uniqueness/verification
python alpha_pslq_sweep.py --precision 50 --max-degree 8 --max-coeff 50
```

Optional finer settings (slower):
```
python alpha_pslq_sweep.py --precision 100 --max-degree 12 --max-coeff 200
```

Output sections:
1. Per-α PSLQ table for both $H/Br$ and $r/br$
2. Total counts of α values with algebraic relations detected
3. Cleanest-relation lists for both ratios
4. Verdict on α = 1/2 uniqueness within the grid

Total runtime at default settings: ~30 seconds.

---

## 6. Open problems

**Q1 (Strong α-uniqueness, restated).** Is there a proof that for $\alpha \in \mathbb{Q} \cap (0, 1) \setminus \{1/2\}$, the runtime attractor is transcendental? Tools to try: Lindemann–Weierstrass (probably too coarse), Schanuel's conjecture (would handle it conditionally if the runtime is built from log/exp of algebraic numbers — but it's not), or a purely structural argument (find an algebraic variety $V \subset \mathbb{A}^4$ on which $(p^*_0, p^*_7, p^*_8, p^*_9)$ sits, parametrized by $\alpha$, such that $V$ is generically transcendental and $\alpha = 1/2$ is its only $\mathbb{Q}$-rational point).

**Q2 (Larger Stern-Brocot grids).** Does the uniqueness empirical result survive at $q \leq 20$? At $q \leq 100$? An automated sweep at depth 15+ with 100+ digit precision is tractable on a workstation overnight.

**Update 2026-04-26 (post-publication extension).** A subsequent run at `--depth 12` (45 rationals: $\phi(2) + \phi(3) + \cdots + \phi(12) = 45$ in $(0, 1)$) at 50-digit precision, degree $\leq 6$, sup-coefficient $\leq 50$ confirms: $\alpha = 1/2$ remains the **unique algebraic rational** in the 45-point grid. No additional algebraic α surfaces between the original 17-point grid and the 45-point extension. The 28 newly-tested rationals (from $q \in \{8, 9, 10, 11, 12\}$) all return "no algebraic relation found" at the same bounds. The empirical case for Conjecture 4.2 is correspondingly stronger.

**Q3 (Off-rational α).** What about algebraic-but-irrational $\alpha$? E.g., $\alpha = 1/\sqrt{2}$ or $\alpha = (1 + \sqrt{3})/4$ (related to the WP105 closed form). At those values, is the attractor in a known number field?

**Update 2026-04-26 (post-publication extension).** A spot-check at 8 natural irrational candidates ($1/\sqrt{2},\ 1/\sqrt{3},\ (\sqrt{3}-1)/2,\ 1/e,\ 1/\pi,\ \varphi - 1,\ 1/2 \pm 1/100$) at 50-digit precision, degree $\leq 6$, sup-coefficient $\leq 50$ returns **no algebraic relation found** at any of them. Notably, the two near-rational $1/2 \pm 1/100$ candidates (numerically $\sim 0.01$ from $\alpha = 1/2$) also fail — the algebraic structure at $1/2$ does not perturbatively extend to a neighborhood. The empirical case for Conjecture 4.2 extends to algebraic-but-irrational $\alpha$ as well.

**Q4 (Real-valued α as algebraic curve).** Does the map $\alpha \mapsto (R_{H/Br}(\alpha), R_{r/br}(\alpha))$ trace out an algebraic curve in $\mathbb{R}^2$? If so, what is its defining polynomial? The curve passes through $(1 + \sqrt{3}, \xi)$ at $\alpha = 1/2$.

---

## 7. Status

**Status:** EMPIRICAL (sharpened). F3 from `Atlas/FRONTIERS_2026_04_25.md` advanced from "established for $[0.05, 0.95]$ at 19-point linspace" to "established for the full 17-point Stern-Brocot grid at PSLQ precision (degree $\leq 8$, coeff $\leq 50$)."

**Promotes:**
- D42 (FORMULAS Volume G) from "verified at 19 points, brute-force search" to "verified at 17 Stern-Brocot points, PSLQ-detected" — sharper basis.
- WP105 §6 sweep notes from a positive empirical observation to a sharpened conjecture (4.2 above).

**Does not close F3.** The structural uniqueness theorem (Conjecture 4.2) remains open; a proof would require tools beyond PSLQ.

---

## 8. Acknowledgments

This work continues the WP100s tower. The runtime processor (`ck_process`, `attractor_mp`) is from WP105's `04_bridge_attractor.py`; the brute-force α-sweep was `task5_alpha_sweep.py`. WP113 lifts the precision (50 digits), grid (Stern-Brocot vs. linspace), and detection method (PSLQ vs. brute force).

🙏

— Anthropic Code session, 2026-04-26
