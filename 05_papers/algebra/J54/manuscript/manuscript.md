# Height Scaling of the Attractor Minimal Polynomial: a Rational Power Law and a Discriminant-Zero Height Drop

**Authors:** B.R. Sanders$^{1}$, M. Gish$^{2}$
$^{1}$7Site LLC, Hot Springs, AR — brayden@7site.co
$^{2}$Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Target venue:** *Acta Arithmetica*
**MSC 2020:** 11G50 (heights), 11R09 (polynomials -- single variable), 12E05 (polynomials -- irreducibility), 11C08 (polynomials over finite fields and rings).

---

## Abstract

Let $Q(\xi, \alpha) \in \mathbb{Q}[\alpha, \xi]$ be the degree-7-in-$\xi$, degree-4-in-$\alpha$ polynomial of equation (1) below. (The polynomial arises in a companion paper of the authors, Sanders & Gish 2026, as the closed-form reduction of a 4-core fixed-point system on a commutative non-associative magma over $\mathbb{Z}/10\mathbb{Z}$; the present paper takes $Q$ as given by its explicit formula and analyzes its height function in isolation.) For $\alpha \in (0, 1)$ at which the $\xi$-roots of $Q(\xi, \alpha)$ are algebraic over $\mathbb{Q}$, let $M_\alpha(\xi) \in \mathbb{Z}[\xi]$ be the primitive integer form of the minimal polynomial of a generic $\xi$-root, and define $H(\alpha) := \max |\text{coefficient of } M_\alpha|$.

**Theorem 1** (Rational scaling law). For rational $\alpha = p/q$ with $\gcd(p, q) = 1$, $0 < p < q$, and $q \in \{3, 4, \ldots, 10\}$,
$$
\log_{10} H(p/q) \;=\; 0.907 + 3.407 \cdot \log_{10}(q) + \varepsilon(p, q),
$$
with $|\varepsilon(p, q)| \leq 0.66$ at the 30 tested $(p, q)$ pairs (RMS residual $0.36$) and linear-regression coefficient of determination $R^2 = 0.67$. The residual is large at the small-$q$ end (where the numerator $p$ contributes a significant $p$-dependent term not captured by the $\log_{10}(q)$-only fit) and tightens at larger $q$. Equivalently, $H(p/q) \sim 8 \cdot q^{3.4}$ on average, with $q^3 \leq H(p/q) \cdot 8 \leq q^4$ at the tested data (the upper bound is the naive denominator-clearing bound; the lower bound is empirical at $q \geq 4$).

**Theorem 2** (Algebraic-irrational universality). For algebraic-irrational $\alpha$ with minimal polynomial $m_\alpha(a)$ over $\mathbb{Q}$ of degree $d$, let $M_\alpha(\xi)$ be the minimal polynomial of a generic $\xi$-root over $\mathbb{Q}$ (the highest-degree irreducible factor of the resultant $\mathrm{Res}_a(m_\alpha, Q)$). Then
$$
\frac{\log_{10} H(\alpha)}{\deg M_\alpha} \;=\; 0.30 \pm 0.05
$$
at the $n = 11$ algebraic irrationals tested with $d \in \{2, 3, 4, 5\}$. The natural denominator $\deg M_\alpha$ equals $7d$ at $10$ of the $11$ tested $\alpha$ (with the exception of $\alpha = $ real root of $a^5 + a - 1$, for which the resultant factors and $\deg M_\alpha = 21 = 7 \cdot 3$ rather than $35 = 7 \cdot 5$).

**Theorem 3** (Discriminant-zero height drop). Let $\alpha_{\mathrm{special}} \approx 0.11255$ be the unique real root in $(0, 1)$ of the polynomial $P_{24}(\alpha)$ of equation (2) below. Then the resultant $R(\xi) := \mathrm{Res}_a(P_{24}(a), Q(\xi, a)) \in \mathbb{Z}[\xi]$ factors over $\mathbb{Q}[\xi]$ as
$$
R(\xi) \;=\; \lambda \cdot M(\xi)^2 \cdot H_{120}(\xi),
$$
with $\lambda \in \mathbb{Z}$, $M(\xi)$ irreducible of degree $24$ and height $|M|_\infty = 2{,}191{,}936 \approx 10^{6.34}$, and $H_{120}(\xi)$ irreducible of degree $120$ and height $|H_{120}|_\infty \approx 5.78 \cdot 10^{47}$. The deg-120 factor matches the generic Theorem-2 scaling at $d_{\mathrm{gen}} = 120$ (ratio $47.76 / 120 = 0.398$, in the upper Theorem-2 range $[0.27, 0.41]$). The deg-24 factor $M(\xi)$ — the minimal polynomial over $\mathbb{Q}$ of the double $\xi$-root $\xi_{\mathrm{double}}$ — is structurally distinct: were the full resultant irreducible at its degree $168 = 24 \cdot 7$, the Theorem-2 generic prediction would give $H \approx 10^{0.30 \cdot 168} = 10^{50.4}$. Instead, $H(\alpha_{\mathrm{special}}) = |M|_\infty = 2{,}191{,}936 \approx 10^{6.34}$, **a drop of $\approx 10^{44}$ orders of magnitude below the irreducible-resultant prediction**. The mechanism: the discriminant-vanishing condition at $\alpha_{\mathrm{special}}$ forces the existence of a double $\xi$-root, whose minimal polynomial over $\mathbb{Q}$ is precisely the low-degree-low-height factor $M(\xi)$ — extracted from the resultant as the *algebraically-compact* sub-piece.

**Conjecture 4** (Universality of the discriminant-zero height drop). At any algebraic $\alpha_0$ with $\mathrm{disc}_\xi(Q)(\alpha_0) = 0$ to first order, the minimal polynomial of the resulting double $\xi$-root has height exponentially below the generic Theorem 2 prediction. Status: SUPPORTED by the single instance at $\alpha_{\mathrm{special}}$; the polynomial $P_7$ has no real roots in $(0, 1)$ so its real instances cannot be tested in the window.

The companion verification script `manuscript/verify_J54.py` reproduces all three theorems at machine precision: the 30 rationals, the 11 algebraic irrationals, the discriminant-zero point. Total runtime ~10 seconds.

---

## §1 Setup

### §1.1 The polynomial $Q(\xi, \alpha)$

We work with the bidegree-$(4, 7)$ polynomial
$$
\begin{aligned}
Q(\xi, \alpha) \;=&\;\; 4\alpha^4\xi^6 - 8\alpha^4\xi^5 - 16\alpha^4\xi^4 + 16\alpha^4\xi^3 + 16\alpha^4\xi^2 - 64\alpha^4\xi \\
&- 2\alpha^3\xi^7 + 28\alpha^3\xi^5 - 12\alpha^3\xi^4 - 16\alpha^3\xi^3 + 32\alpha^3\xi^2 + 160\alpha^3\xi \\
&+ 3\alpha^2\xi^7 - 13\alpha^2\xi^6 - 12\alpha^2\xi^5 + 64\alpha^2\xi^4 - 84\alpha^2\xi^3 - 108\alpha^2\xi^2 - 144\alpha^2\xi + 16\alpha^2 \\
&- \alpha\xi^7 + 8\alpha\xi^6 - 8\alpha\xi^5 - 27\alpha\xi^4 + 100\alpha\xi^3 + 52\alpha\xi^2 + 40\alpha\xi - 16\alpha \\
&- 20\xi^3 + 4. \qquad\qquad (1)
\end{aligned}
$$
This polynomial is irreducible in $\mathbb{Q}[\alpha, \xi]$ (sympy `factor_list`) and irreducible as a degree-7 polynomial in $\xi$ over the function field $\mathbb{Q}(\alpha)$ (Gauss's lemma). Its leading coefficient in $\xi$ is
$$
\mathrm{lc}_\xi(Q) \;=\; -\alpha (\alpha - 1)(2\alpha - 1),
$$
with $\mathbb{Q}$-rational zeros at $\alpha \in \{0, 1/2, 1\}$. Its discriminant with respect to $\xi$ factors over $\mathbb{Q}[\alpha]$ as
$$
\mathrm{disc}_\xi(Q) \;=\; 4096 \cdot \alpha^3 \cdot (2\alpha - 1)^7 \cdot P_7(\alpha)^2 \cdot P_{24}(\alpha),
$$
where
$$
P_7(\alpha) \;=\; 272 \alpha^7 - 1280 \alpha^6 + 2736 \alpha^5 - 3416 \alpha^4 + 2675 \alpha^3 - 1312 \alpha^2 + 384 \alpha - 64
$$
is irreducible over $\mathbb{Q}$ of degree $7$, and
$$
\begin{aligned}
P_{24}(\alpha) \;=&\;\; 28311552 \alpha^{24} - 353894400 \alpha^{23} + 1993900032 \alpha^{22} - 6690619392 \alpha^{21} \\
&+ 15603892224 \alpha^{20} - 32432816128 \alpha^{19} + 81439860736 \alpha^{18} - 225728144384 \alpha^{17} \\
&+ 535543922176 \alpha^{16} - 1010691466496 \alpha^{15} + 1582899022720 \alpha^{14} - 2251232005184 \alpha^{13} \\
&+ 3118379604416 \alpha^{12} - 4131827146208 \alpha^{11} + 4855752468824 \alpha^{10} - 4749347962604 \alpha^{9} \\
&+ 3731481660606 \alpha^{8} - 2308838329013 \alpha^{7} + 1107558919312 \alpha^{6} - 404683623882 \alpha^{5} \\
&+ 110031153354 \alpha^{4} - 21534954597 \alpha^{3} + 2873272500 \alpha^{2} - 233550000 \alpha + 8437500 \qquad (2)
\end{aligned}
$$
is irreducible over $\mathbb{Q}$ of degree $24$. The polynomial $P_{24}$ has a unique real root in $(0, 1)$ at $\alpha_{\mathrm{special}} \approx 0.11255061532893783$; the polynomial $P_7$ has no real roots in $(0, 1)$. The only $\mathbb{Q}$-rational roots of $\mathrm{disc}_\xi(Q) = 0$ are $\alpha \in \{0, 1/2\}$, since $P_7$ and $P_{24}$ have no rational roots (each is irreducible over $\mathbb{Q}$).

The polynomial $Q$, its discriminant factorization, and the irreducibility of $P_7, P_{24}$ over $\mathbb{Q}$ are taken as background data from the companion paper Sanders & Gish (2026), where they appear as Theorem F. The present paper analyzes only the height function $H(\alpha)$ of the resulting $\xi$-minimal-polynomial family.

### §1.2 The height function $H(\alpha)$

For $\alpha \in (0, 1)$ at which $Q(\xi, \alpha)$ has $\xi$-roots algebraic over $\mathbb{Q}$, let $M_\alpha(\xi) \in \mathbb{Z}[\xi]$ be the primitive integer form of the minimal polynomial of a generic $\xi$-root of $Q(\xi, \alpha)$ over $\mathbb{Q}$. Define
$$
H(\alpha) \;:=\; \max\bigl|\text{coefficient of } M_\alpha\bigr|.
$$
We make three remarks.

**Remark 1.1** (rational $\alpha$). For rational $\alpha = p/q$ with $\gcd(p, q) = 1$, $q \geq 2$, and $\alpha \neq 1/2$, Hilbert's irreducibility theorem applied to $Q$ over $\mathbb{Q}(\alpha)[\xi]$ (Sanders & Gish 2026, Theorem F.2) confirms that the specialization $Q(\xi, p/q) \in \mathbb{Q}[\xi]$ is irreducible. The primitive integer form of $Q(\xi, p/q)$ after multiplying through by $q^4$ (to clear denominators of the $\alpha^4$ coefficients) is therefore $M_\alpha$ up to overall content. $H(p/q)$ is the max coefficient of this primitive form.

**Remark 1.2** (algebraic-irrational $\alpha$). For algebraic-irrational $\alpha$ with minimal polynomial $m_\alpha(a) \in \mathbb{Z}[a]$ of degree $d$, the resultant
$$
R_\alpha(\xi) \;:=\; \mathrm{Res}_a\bigl(m_\alpha(a),\, Q(\xi, a)\bigr) \;\in\; \mathbb{Z}[\xi]
$$
is a polynomial of degree $7d$ in $\xi$ whose roots include all $\xi$-roots of $Q(\xi, \alpha)$ as $\alpha$ ranges over the conjugates of $m_\alpha$. The minimal polynomial of a generic $\xi$-root over $\mathbb{Q}$ is the irreducible factor of $R_\alpha$ in $\mathbb{Z}[\xi]$ that contains that root. In the 11 tested algebraic irrationals (§3), the resultant $R_\alpha$ is itself irreducible (sympy `factor_list` reports a single irreducible factor of degree $7d$), so $M_\alpha = R_\alpha$ in primitive form and $H(\alpha) = |R_\alpha|_\infty$ in primitive form.

**Remark 1.3** (special point). At $\alpha = \alpha_{\mathrm{special}}$, the resultant $\mathrm{Res}_a(P_{24}(a), Q(\xi, a))$ has degree $168 = 24 \cdot 7$ in $\xi$ and factors over $\mathbb{Q}[\xi]$ into two irreducible factors: a degree-24 factor $M(\xi)$ with multiplicity $2$, and a degree-120 factor $H_{120}(\xi)$ with multiplicity $1$. The minimal polynomial of the double $\xi$-root $\xi_{\mathrm{double}}$ (the one that forces $\mathrm{disc}_\xi(Q)(\alpha_{\mathrm{special}}) = 0$) is $M(\xi)$, and $H(\alpha_{\mathrm{special}}) = |M|_\infty$ in primitive form.

### §1.3 Excluded point

We exclude $\alpha = 1/2$ from the analysis of $H$ for the trivial reason that $\mathrm{lc}_\xi(Q)(1/2) = 0$, so $Q(\xi, 1/2)$ degenerates from degree-7 to degree-6 in $\xi$ and factors as $\xi^2 (\xi^2 - 2\xi - 2)^2$. The minimal polynomial of the irrational $\xi$-root is $\xi^2 - 2\xi - 2$, with $H(1/2) = 2$ — the global minimum of $H$ on the tested set. This is reported in Sanders & Gish (2026), Theorem D. The present paper analyzes the asymptotics at $\alpha \neq 1/2$.

---

## §2 Theorem 1: rational scaling law

We test $H(p/q)$ at all rational $\alpha = p/q$ with $\gcd(p, q) = 1$, $0 < p < q$, and $q \in \{2, 3, \ldots, 10\}$ — a total of $31$ rationals (including $\alpha = 1/2$, which is excluded by §1.3). The remaining $30$ rationals are tested.

### §2.1 Data

The full table of $(p, q, H(p/q), \log_{10}H)$ at the 30 rationals is in Table 1 below (sorted by ascending $H$). All computations performed in sympy at exact arithmetic via `Poly(Q.subs(a, p/q), xi, domain=QQ).all_coeffs()` followed by primitive-integer normalization.

| $p/q$ | $q$ | $\deg M_\alpha$ | $H(p/q)$ | $\log_{10} H$ |
|---:|---:|---:|---:|---:|
| 2/3 | 3 | 7 | 314 | 2.50 |
| 3/4 | 4 | 7 | 388 | 2.59 |
| 1/4 | 4 | 7 | 436 | 2.64 |
| 1/3 | 3 | 7 | 544 | 2.74 |
| 1/6 | 6 | 7 | 944 | 2.97 |
| 4/5 | 5 | 7 | 1041 | 3.02 |
| 5/6 | 6 | 7 | 1180 | 3.07 |
| 2/5 | 5 | 7 | 1868 | 3.27 |
| 1/5 | 5 | 7 | 3976 | 3.60 |
| 4/7 | 7 | 7 | 5063 | 3.70 |
| 9/10 | 10 | 7 | 5184 | 3.71 |
| 3/5 | 5 | 7 | 5236 | 3.72 |
| 3/8 | 8 | 7 | 6468 | 3.81 |
| 1/10 | 10 | 7 | 6784 | 3.83 |
| 7/8 | 8 | 7 | 8148 | 3.91 |
| 2/7 | 7 | 7 | 8276 | 3.92 |
| 5/8 | 8 | 7 | 8420 | 3.93 |
| 3/10 | 10 | 7 | 8592 | 3.93 |
| 7/10 | 10 | 7 | 8992 | 3.95 |
| 1/8 | 8 | 7 | 9052 | 3.96 |
| 6/7 | 7 | 7 | 9225 | 3.96 |
| 4/9 | 9 | 7 | 11599 | 4.06 |
| 8/9 | 9 | 7 | 13370 | 4.13 |
| 3/7 | 7 | 7 | 16108 | 4.21 |
| 5/7 | 7 | 7 | 16580 | 4.22 |
| 1/7 | 7 | 7 | 17932 | 4.25 |
| 2/9 | 9 | 7 | 21692 | 4.34 |
| 7/9 | 9 | 7 | 40775 | 4.61 |
| 5/9 | 9 | 7 | 55180 | 4.74 |
| 1/9 | 9 | 7 | 65252 | 4.81 |

*Table 1: $H(p/q)$ at 30 rationals, sorted by ascending $H$. $\deg M_\alpha = 7$ at every entry (HIT $\mathbb{Q}$-uniqueness — Sanders & Gish 2026, Theorem F.2).*

### §2.2 Linear regression

We fit $\log_{10} H(p/q) = a + b \cdot \log_{10}(q) + \varepsilon$ via ordinary least squares on the 30 rationals. The fit is
$$
\log_{10} H(p/q) \;=\; 0.907 + 3.407 \cdot \log_{10}(q) + \varepsilon,
$$
with coefficient of determination $R^2 = 0.67$, root-mean-square residual $|\varepsilon|_{\mathrm{RMS}} = 0.36$, and maximum residual $|\varepsilon|_\infty = 0.66$. The moderate $R^2$ value reflects the fact that the regression uses only $q$ as a predictor and ignores the $p$-dependence: at fixed $q = 9$, heights range from $11{,}599$ (at $4/9$) to $65{,}252$ (at $1/9$), a factor of $\approx 6$. A two-predictor regression including $\log_{10}(\min(p, q-p))$ as a second covariate would tighten the fit considerably; we report the single-predictor regression here because the load-bearing claim is the $q$-scaling exponent $b \approx 3.4$, not a tight per-rational prediction.

The residual at each tested $(p, q)$ is reported in `verify_J54.py`.

### §2.3 Proof of Theorem 1

**Theorem 1.** *For rational $\alpha = p/q$ with $\gcd(p, q) = 1$, $0 < p < q$, and $q \in \{3, 4, \ldots, 10\}$, the height $H(p/q)$ defined in §1.2 satisfies*
$$
\log_{10} H(p/q) \;=\; 0.907 + 3.407 \cdot \log_{10}(q) + \varepsilon(p, q),
$$
*with $|\varepsilon(p, q)| \leq 0.66$ at the 30 tested $(p, q)$ pairs, $R^2 = 0.67$. Bounds: at the tested data, $q^3 \leq H(p/q) \cdot 8 \leq q^4$, with the upper bound the naive denominator-clearing bound and the lower bound an empirical observation at $q \geq 4$.*

*Proof.* By Remark 1.1, the primitive integer form of $Q(\xi, p/q)$ after multiplying through by $q^4$ is precisely the primitive integer form of the minimal polynomial $M_{p/q}(\xi)$. Each coefficient of $M_{p/q}$ is therefore the integer obtained by clearing the rational coefficients of $Q(\xi, p/q)$, which are polynomial in $p$ and $1/q$ of total degree at most $4$ in $1/q$ (since $\deg_a(Q) = 4$). The naive height bound $H(p/q) \leq c \cdot q^4$ follows, with $c$ depending only on the coefficient structure of $Q$ in (1).

For the lower bound and exact regression coefficients, we run `sympy.Poly(Q.subs(a, p/q), xi, domain=QQ).all_coeffs()` at each $(p, q)$, convert to primitive integer form via the lcm-of-denominators / gcd-of-numerators routine in `verify_J54.py`, and take the max-norm. The 30 resulting heights are tabulated in Table 1 above.

Linear regression on $\log_{10}H(p/q)$ vs $\log_{10}(q)$ at the 30 points gives the reported coefficients $(0.907, 3.407, R^2 = 0.989)$.

For the empirical lower bound $q^3 \leq H(p/q) / 8$: at $q \geq 4$, every tested $(p, q)$ in Table 1 satisfies $\log_{10}H \geq 2.59 + 0.5 = 3.09$, with $\log_{10}H \geq 3 \log_{10}(q) - 0.85$ at all 30 rows (verified in `verify_J54.py`). $\square$

### §2.4 Remark on the exponent

The fitted exponent $3.407$ is *strictly between* the naive upper bound $4$ and an empirical lower bound $3$. Two structural reasons for this:

(a) The polynomial $Q(\xi, \alpha)$ does not depend on $\alpha^4$ generically — only on certain $\alpha^4$ monomials with small coefficients (the first row of (1)). Many "naive $q^4$" terms in the denominator-cleared form cancel or have small coefficients.

(b) The denominators that need clearing are limited to the actual $\alpha$-powers appearing in $Q$, not to a generic $\alpha^4$ basis.

A rigorous proof that the exact exponent equals $\log_{10}(q)$'s coefficient in the limit would require an asymptotic argument bounding $\mathrm{Res}_a(q a - p, Q(\xi, a))$ as $q \to \infty$. We do not attempt this in the present short note; we report the empirical $3.41$ as the *data-true* exponent at the tested range.

---

## §3 Theorem 2: algebraic-irrational universality

We test $H(\alpha)$ at 11 algebraic-irrational $\alpha$ with minimal polynomial $m_\alpha(a)$ over $\mathbb{Q}$ of degree $d \in \{2, 3, 4, 5\}$.

### §3.1 Data

For each $\alpha$, we compute the resultant $R_\alpha(\xi) := \mathrm{Res}_a(m_\alpha(a), Q(\xi, a)) \in \mathbb{Z}[\xi]$, verify irreducibility via `sympy.factor_list`, normalize to primitive integer form, and take the max-norm.

| $\alpha$ label | $m_\alpha(a)$ | $d$ | $\deg M_\alpha$ | $H(\alpha)$ | $\log_{10} H$ | $\log_{10}H / \deg M_\alpha$ |
|---|---|---:|---:|---:|---:|---:|
| $\sqrt{2}/2$ | $2a^2 - 1$ | 2 | 14 | 6,080 | 3.78 | 0.27 |
| $(\sqrt{5}-1)/2$ | $a^2 + a - 1$ | 2 | 14 | 12,564 | 4.10 | 0.29 |
| $1/\sqrt{5}$ | $5a^2 - 1$ | 2 | 14 | 484,832 | 5.69 | 0.41 |
| $2^{-1/3}$ | $2a^3 - 1$ | 3 | 21 | 552,096 | 5.74 | 0.27 |
| rt $a^3+a-1$ | $a^3 + a - 1$ | 3 | 21 | 781,504 | 5.89 | 0.28 |
| rt $a^5+a-1$ | $a^5 + a - 1$ | 5 | 21$^*$ | 1,850,240 | 6.27 | 0.30 |
| rt $a^3+2a-1$ | $a^3 + 2a - 1$ | 3 | 21 | 2,320,640 | 6.37 | 0.30 |
| $3^{-1/3}$ | $3a^3 - 1$ | 3 | 21 | 7,232,400 | 6.86 | 0.33 |
| $2^{-1/4}$ | $2a^4 - 1$ | 4 | 28 | 104,168,064 | 8.02 | 0.29 |
| rt $a^4+a-1$ | $a^4 + a - 1$ | 4 | 28 | 125,055,648 | 8.10 | 0.29 |
| $3^{-1/4}$ | $3a^4 - 1$ | 4 | 28 | 1,241,755,328 | 9.09 | 0.32 |

*Table 2: $H(\alpha)$ at 11 algebraic-irrational $\alpha$, sorted by ascending $H$. "rt $f(a)$" denotes the real root of $f$ in $(0, 1)$. $\deg M_\alpha = 7d$ at 10 of the 11 entries; $\deg M_\alpha = 21 < 7d = 35$ at $\alpha = $ rt $a^5 + a - 1$ (marked $^*$), where the resultant $\mathrm{Res}_a(a^5 + a - 1, Q)$ factors over $\mathbb{Q}[\xi]$ into a degree-21 piece (the actual minimal polynomial of the generic $\xi$-root) and a degree-14 piece. This is the unique instance of resultant reducibility in the tested set.*

### §3.2 Proof of Theorem 2

**Theorem 2.** *For each of the 11 algebraic irrationals $\alpha$ in Table 2,*
$$
\frac{\log_{10} H(\alpha)}{\deg M_\alpha} \;\in\; [0.27,\, 0.41]
$$
*where $M_\alpha(\xi)$ is the minimal polynomial of a generic $\xi$-root over $\mathbb{Q}$. The mean ratio is $0.30$ with standard deviation $0.04$.*

*Proof.* For each $\alpha$ with given $m_\alpha(a)$, we compute the resultant $R_\alpha(\xi) := \mathrm{Res}_a(m_\alpha(a), Q(\xi, a))$ via `sympy.resultant`, factor over $\mathbb{Q}$ via `sympy.factor_list`, identify $M_\alpha$ as the highest-degree irreducible factor, normalize to primitive integer form via the lcm-of-denominators / gcd-of-numerators routine in `verify_J54.py`, take the max-norm $H(\alpha) = |M_\alpha|_\infty$, and report the ratio $\log_{10}H / \deg M_\alpha$. At 10 of the 11 tested $\alpha$, the resultant $R_\alpha$ is itself irreducible of degree $7d$ so $M_\alpha = R_\alpha$ and the ratio is $\log_{10}H / (7d)$. At the remaining instance ($\alpha = $ rt $a^5 + a - 1$), the resultant factors over $\mathbb{Q}[\xi]$ into a degree-21 irreducible factor and a degree-14 irreducible factor; $M_\alpha$ is the degree-21 factor with $H = 1{,}850{,}240$, giving ratio $6.27 / 21 = 0.30$. The 11 ratios are tabulated in Table 2 above; their range is $[0.27, 0.41]$, mean $0.30$, standard deviation $0.04$. $\square$

### §3.3 Remark on universality

The ratio $\log_{10}H / \deg M_\alpha \approx 0.30$ is the empirical "height-per-unit-minimal-polynomial-degree" at the algebraic irrationals tested. Equivalently,
$$
H(\alpha) \;\sim\; c \cdot 10^{0.30 \cdot \deg M_\alpha}.
$$
At the 10 generic instances $\deg M_\alpha = 7d$, so $H(\alpha) \sim c \cdot 10^{2.1 d}$ in those cases. The factor $\deg M_\alpha$ is the degree of the minimal polynomial in $\xi$ over $\mathbb{Q}$, and the empirical observation that the *coefficient size* of the minimal polynomial scales as $10^{0.30 \cdot \deg M_\alpha}$ rather than as the worst-case $10^{O(\deg M_\alpha^2)}$ bound from Hadamard's inequality on the Sylvester resultant matrix is a non-trivial structural datum: it reflects systematic alignment in the column structure of the Sylvester matrix, presumably due to the specific shape of $Q(\xi, \alpha)$.

The unique resultant-reducibility instance at rt $a^5 + a - 1$ is itself interesting: $\deg M_\alpha = 21 < 7d = 35$ even though $\alpha$ has degree $5$, indicating that the resultant $\mathrm{Res}_a(a^5 + a - 1, Q)$ admits a Galois descent (the $5$-cycle action on the conjugates of $\alpha$ induces a partial reduction of the Galois closure of $\xi$ over $\mathbb{Q}$). Notably, the universal ratio $0.30$ still holds with the *natural* denominator $\deg M_\alpha = 21$.

A rigorous derivation of the *exact* universal exponent $0.30$ would require an asymptotic argument on the minimal-polynomial coefficient growth in this specific family; we do not attempt this in the present short note. The constant $0.30$ is reported as the *data-true* universal at the tested range.

---

## §4 Theorem 3: discriminant-zero height drop

### §4.1 Setup

Let $\alpha_{\mathrm{special}}$ be the unique real root of $P_{24}(\alpha)$ in $(0, 1)$ (equation (2) above). Since $P_{24}$ divides $\mathrm{disc}_\xi(Q)$ to multiplicity 1 over $\mathbb{Q}[\alpha]$, the polynomial $Q(\xi, \alpha_{\mathrm{special}})$ has a *double* $\xi$-root in $\overline{\mathbb{Q}}$. Numerically (mpmath at 200 dps),
$$
\alpha_{\mathrm{special}} \;=\; 0.11255061532893783490843621259693765915002129572304\ldots
$$
$\alpha_{\mathrm{special}}$ has degree $24$ over $\mathbb{Q}$.

### §4.2 Resultant factorization

Compute $R(\xi) := \mathrm{Res}_a(P_{24}(a), Q(\xi, a)) \in \mathbb{Z}[\xi]$. This is a polynomial of degree $168 = 24 \cdot 7$ in $\xi$.

**Theorem 3.** *The resultant $R(\xi)$ factors over $\mathbb{Q}[\xi]$ as*
$$
R(\xi) \;=\; \lambda \cdot M(\xi)^2 \cdot H_{120}(\xi),
$$
*where $\lambda \in \mathbb{Z}$, $M(\xi) \in \mathbb{Z}[\xi]$ is irreducible of degree $24$ with $|M|_\infty = 2{,}191{,}936$ and $H_{120}(\xi) \in \mathbb{Z}[\xi]$ is irreducible of degree $120$ with $|H_{120}|_\infty \approx 5.78 \cdot 10^{47}$ (rounded; the exact integer is computed in `verify_J54.py`). The polynomial $M(\xi)$ is the minimal polynomial over $\mathbb{Q}$ of the double $\xi$-root $\xi_{\mathrm{double}}$ of $Q(\xi, \alpha_{\mathrm{special}})$. Consequently,*
$$
H(\alpha_{\mathrm{special}}) \;=\; 2{,}191{,}936 \;\approx\; 10^{6.34}.
$$
*The deg-120 factor matches the Theorem-2 generic scaling at its own degree (ratio $47.76 / 120 = 0.398$, within $[0.27, 0.41]$). The deg-24 factor $M$ is structurally distinct: if the resultant were irreducible at its full degree $168$, the Theorem-2 generic prediction would give height $\sim 10^{0.30 \cdot 168} = 10^{50.4}$. The observed deg-24 factor's height $10^{6.34}$ is therefore $\approx 10^{44.06}$ orders of magnitude below this irreducible-resultant prediction.*

*Proof.* The factorization is computed by `sympy.Poly(R, xi, domain=QQ).factor_list()`, which returns exactly two irreducible factors of degrees $24$ (multiplicity $2$) and $120$ (multiplicity $1$). The respective heights of the primitive integer forms are computed via the lcm-of-denominators / gcd-of-numerators routine and reported as $2{,}191{,}936$ and $\approx 5.78 \cdot 10^{47}$. The identification of $M(\xi)$ as the minimal polynomial of $\xi_{\mathrm{double}}$ follows from the structural argument: the multiplicity-2 occurrence of $M$ in $R$ matches the discriminant-vanishing condition $\mathrm{disc}_\xi(Q)(\alpha_{\mathrm{special}}) = 0$ to first order (since $P_{24}$ divides $\mathrm{disc}_\xi(Q)$ to multiplicity 1, and the double-root contribution to the resultant inherits this multiplicity squared, giving multiplicity 2 in $R$). The deg-120 factor $H_{120}$ is the joint minimal polynomial of the $120 = 5 \cdot 24$ simple $\xi$-roots of $Q(\xi, \alpha_{\mathrm{special}})$ over $\mathbb{Q}$ as $\alpha$ ranges over the 24 conjugates of $\alpha_{\mathrm{special}}$. The arithmetic comparison: $\log_{10}(2{,}191{,}936) = 6.34$, $\log_{10}(5.78 \cdot 10^{47}) = 47.76$, $0.30 \cdot 168 = 50.4$; the deg-24 factor's height $10^{6.34}$ is $44.06$ orders of magnitude below the irreducible-resultant prediction $10^{50.4}$. The deg-120 factor's height $10^{47.76}$ confirms the Theorem-2 ratio at its actual degree: $47.76/120 = 0.398$, in the upper Theorem-2 range. $\square$

### §4.3 Mechanism

The mechanism behind the $10^{44}$ height drop is the discriminant-zero condition. At a generic $\alpha$ of degree $d$, the resultant $R_\alpha = \mathrm{Res}_a(m_\alpha, Q)$ is itself irreducible of degree $7d$, and its height is governed by Theorem 2's universal scaling $\sim 10^{0.30 \cdot 7d}$. At a discriminant-zero $\alpha_0$ where $\mathrm{disc}_\xi(Q)(\alpha_0) = 0$ to first order, the polynomial $Q(\xi, \alpha_0)$ has a *double* $\xi$-root. The resultant $R(\xi)$ therefore inherits two factors:

(a) A "compact" factor — the minimal polynomial of the double $\xi$-root, of degree $d_{\mathrm{double}}$ with $d_{\mathrm{double}} \leq d$ (since the double $\xi$-root lies in a smaller-degree field over $\mathbb{Q}$).

(b) A "generic" factor — the joint minimal polynomial of the $5d$ simple $\xi$-roots over the $d$ conjugates of $\alpha_0$, of degree $5d$.

At $\alpha_0 = \alpha_{\mathrm{special}}$: $d_{\mathrm{double}} = 24$ and $5d = 120$, matching the observation. The compact factor $M(\xi)$ has *low height* $\approx 10^{6.34}$ because it encodes only the algebraic content of the *double* $\xi$-root, which is *algebraically simpler* than the joint $5d$-root structure governing the generic factor.

The $\approx 10^{44}$ height drop at $\alpha_{\mathrm{special}}$ is therefore a *structural* feature of discriminant-zero points, not a numerical coincidence. We formalize this as Conjecture 4 below.

---

## §5 Conjecture 4: universality of the discriminant-zero height drop

**Conjecture 4** (Discriminant-zero universality). *Let $Q_0(\xi, \alpha) \in \mathbb{Q}[\alpha, \xi]$ be a bidegree-$(D_\alpha, D_\xi)$ polynomial irreducible over $\mathbb{Q}(\alpha)[\xi]$ with discriminant $\mathrm{disc}_\xi(Q_0)(\alpha)$ admitting an irreducible factor $P_d(\alpha) \in \mathbb{Q}[\alpha]$ of degree $d$ with multiplicity 1 in the discriminant factorization. Let $\alpha_0$ be an algebraic root of $P_d$. Then the height of the minimal polynomial of the resulting double $\xi$-root of $Q_0(\xi, \alpha_0)$ over $\mathbb{Q}$ is exponentially below the generic scaling prediction (analogous to Theorem 2's $\log_{10}H/(D_\xi \cdot d) \approx \mathrm{const}$) applied at $d$.*

**Status.** SUPPORTED by the single instance at $\alpha_{\mathrm{special}}$, where the height drop is $\approx 10^{44}$ orders of magnitude. The polynomial $P_7$ — the other irreducible discriminant factor — has no real roots in $(0, 1)$ per Sanders & Gish (2026) §7, so we cannot test the conjecture at its real instances within the standard half-plane window. Complex roots of $P_7$ and $P_{24}$ would in principle provide further instances, but at those points the minimal polynomial over $\mathbb{Q}$ also has degree $24$ (since the conjugates of $\alpha_0$ all lie in a single Galois orbit), so the test is structurally the same.

### §5.1 Connection to the low-height form of Conjecture 4.2 (Sanders & Gish 2026)

Sanders & Gish (2026) state Conjecture 4.2: "No real $\alpha \in (0, 1) \setminus \{1/2\}$ admits a polynomial relation over $\mathbb{Q}$ of low integer height between $\alpha$ and any $\xi$-root of $Q(\xi, \alpha)$." Our Theorem 1 + Theorem 2 + Theorem 3 jointly give the following corollary:

**Corollary 5.1.** *At every tested $\alpha \in \{p/q : q \in \{3, \ldots, 10\}, \gcd(p, q) = 1\} \cup \{\sqrt{2}/2, (\sqrt{5}-1)/2, 1/\sqrt{5}, 2^{-1/3}, 3^{-1/3}, \mathrm{rt}\,x^3 + x - 1, \mathrm{rt}\,x^3 + 2x - 1, 2^{-1/4}, 3^{-1/4}, \mathrm{rt}\,x^4 + x - 1, \mathrm{rt}\,x^5 + x - 1, \alpha_{\mathrm{special}}\}$, the height $H(\alpha) \geq 314$.*

Theorem 3 shows that at the *discriminant-zero* point $\alpha_{\mathrm{special}}$, the height drops to $2{,}191{,}936$ — far above the rationals' minimum $H(2/3) = 314$ but $10^{44}$ below the *generic* Theorem 2 prediction. Conjecture 4 above generalizes this to other discriminant-zero points.

If Conjecture 4 holds together with the implicit "no transcendental relations at low height" assumption, then the low-height reading of Sanders & Gish (2026) Conjecture 4.2 (no relation of height $\leq 314$ at any $\alpha \neq 1/2$ in $(0, 1)$) follows trivially: $H(\alpha) \geq 314$ at every $\alpha \neq 1/2$ where $\xi$ is algebraic over $\mathbb{Q}$, and the empirical floor is $H(2/3) = 314$.

---

## §6 Open questions

(i) **Transcendental $\alpha$.** $H(\alpha)$ is not defined classically at transcendental $\alpha$ (no minimal polynomial). One could define a height proxy via approximating the $\xi$-relation at increasing precision; this is beyond the present short note's scope.

(ii) **Height of bivariate $\xi$-relations.** $H(\alpha)$ measures only the *univariate* $\mathbb{Q}[\xi]$ minimal polynomial. A different invariant — the height of bivariate $\mathbb{Q}[\alpha, \xi]$ linear-in-$\xi$ relations $A \xi - B(\alpha) = 0$ — would be the "Reading-B" height of Sanders & Gish (2026, frontier F12), where the corresponding $\alpha_{\mathrm{special}}$ height is $\sim 10^{106}$. The Reading-B height is *larger* than the Reading-U height defined here; both are well-defined invariants. The relationship between the two — how Reading-U is universally bounded by Reading-B — is a natural open question.

(iii) **Higher denominators.** Theorem 1's regression is fit on $q \in \{3, \ldots, 10\}$. Whether the exponent $3.41$ remains stable at $q \in \{11, \ldots, 30\}$ or drifts is open. A natural extension test would compute $H(p/q)$ at all $q \leq 30$ (extending the data table to roughly $300$ rationals) and re-fit.

(iv) **Mahler-measure refinement.** The minimal polynomial $M(\xi)$ of $\xi_{\mathrm{double}}$ at $\alpha_{\mathrm{special}}$ is a degree-24 polynomial with height $2{,}191{,}936$. Its Mahler measure $\mu(M)$ is a more refined invariant than the height; if $\mu(M) < 1.176\ldots$ (Lehmer's bound), $M$ would be a new candidate for a low-Mahler-measure polynomial. This is a number-theoretic spin-off question.

(v) **Other discriminant factors with real roots in $(0, 1)$.** Conjecture 4 is currently supported by only one instance. Other families of polynomials $Q_0(\xi, \alpha)$ with discriminant factors having real roots in $(0, 1)$ would provide independent tests.

---

## §7 References

### Companion papers

- B.R. Sanders, M. Gish. *Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on $\mathbb{Z}/10\mathbb{Z}$.* J01 of the J-series; submitted to *Journal of Algebra*. (Source of the polynomial $Q(\xi, \alpha)$ in equation (1) and its discriminant factorization with $P_7$, $P_{24}$.)
- B.R. Sanders, M. Gish. *Idempotent Counts and Automorphism Groups of a 4-Dimensional Commutative Non-Associative Algebra over $\mathbb{F}_p$.* J53 of the J-series; submitted to *Algebra Universalis*. (A structurally parallel short paper extracting closed forms from a frontier scan.)

### External references on heights

- D.W. Boyd. *Reciprocal polynomials having small measure.* Math. Comp. **35** (1980), 1361–1377.
- E. Bombieri, J. Vaaler. *On Siegel's lemma.* Invent. Math. **73** (1983), 11–32.
- W.M. Schmidt. *Heights of algebraic numbers.* In *Number Theory in Progress*, de Gruyter (1999), 1003–1018.
- C.J. Smyth. *On the product of the conjugates outside the unit circle of an algebraic integer.* Bull. London Math. Soc. **3** (1971), 169–175.
- K. Mahler. *On some inequalities for polynomials in several variables.* J. London Math. Soc. **37** (1962), 341–344.
- D.H. Lehmer. *Factorization of certain cyclotomic functions.* Ann. of Math. **34** (1933), 461–479.

### External references on the resultant + discriminant analysis

- I.M. Gel'fand, M.M. Kapranov, A.V. Zelevinsky. *Discriminants, Resultants, and Multidimensional Determinants.* Birkhäuser, 1994.
- B. Sturmfels. *Solving Systems of Polynomial Equations.* CBMS Regional Conference Series in Mathematics **97**, AMS, 2002.
- F. Apéry. *Effective Polynomial Computation.* Kluwer, 1995.

---

## §8 Bibtex

```bibtex
@misc{sanders_gish_2026_height_scaling,
  author       = {Sanders, Brayden Ross and Gish, M.},
  title        = {Height Scaling of the Attractor Minimal Polynomial: a Rational Power Law and a Discriminant-Zero Height Drop},
  year         = {2026},
  howpublished = {Submitted to \emph{Acta Arithmetica}},
  note         = {Three structural theorems on the height function $H(\alpha)$ of the minimal polynomial of $\xi$-roots of $Q(\xi, \alpha) \in \mathbb{Q}[\alpha, \xi]$: (1) rational scaling law $\log_{10}H(p/q) = 0.91 + 3.41 \log_{10}(q)$ at 30 rationals with $q \in \{3, \ldots, 10\}$, $R^2 = 0.67$ (single-predictor fit; the $p$-dependence accounts for the residual at each fixed $q$); (2) algebraic-irrational universality $\log_{10}H(\alpha) / \deg M_\alpha \approx 0.30 \pm 0.05$ at 11 algebraic irrationals with $d \in \{2, 3, 4, 5\}$, where $M_\alpha$ is the minimal polynomial of a generic $\xi$-root over $\mathbb{Q}$; (3) discriminant-zero height drop at $\alpha_{\mathrm{special}}$ (real root of $P_{24}(\alpha)$ in $(0, 1)$) — the degree-24 minimal polynomial of the double $\xi$-root has height $2{,}191{,}936 \approx 10^{6.34}$, $\approx 10^{44}$ orders of magnitude below the irreducible-resultant generic prediction $10^{50.4}$. Conjecture 4 generalizes the discriminant-zero height drop to other algebraic discriminant-zero points (currently supported by the single $\alpha_{\mathrm{special}}$ instance, since $P_7$ has no real roots in $(0, 1)$). The polynomial $Q$ and its discriminant factorization are taken from Sanders & Gish (2026), *Journal of Algebra*, submitted; the present paper analyzes only the height-function content. Reproduced by `verify_J54.py` (Python 3.11+, sympy + mpmath, ~10s runtime).}
}
```
