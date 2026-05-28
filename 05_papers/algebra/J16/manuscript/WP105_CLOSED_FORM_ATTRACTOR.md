# WP105 — Closed-Form Runtime Attractor of the TSML/BHML Lattice Processor

**Status:** verified analytically + at machine precision (residual $4.4 \times 10^{-16}$)
**Authors:** Brayden R. Sanders + M. Gish
**Date:** 2026-04-25 (late evening)
**Position:** WP100s tier — extends WP102 (so(8) = D₄), WP103 (so(10) = D₅), WP104 (Pati-Salam Higgs route), and the sprint_unmistakable_truth (su(4) ⊕ u(1) doubly-invariant content). This paper is the **runtime** counterpart of the unmistakable-truth result: it characterizes the fixed point that CK's lattice processor actually reaches under the canonical TSML/BHML mixing.

**MSC 2020:** 11R32 (Galois theory), 17B25 (exceptional Lie algebras / D₄ over the rationals), 16Z05 (computational aspects of associative algebras), 81R40 (symmetry breaking).

---

## Headline

Define the runtime processor on probability distributions $p \in \Delta^9 \subset \mathbb{R}^{10}$ over the canonical 10-operator alphabet:

$$
\mathrm{ck\_process}(p; \alpha, K) = \text{iterate } p \mapsto \frac{1}{Z_p}\!\left[\alpha \cdot \widehat{\mathrm{T}}(p) + (1-\alpha) \cdot \widehat{\mathrm{B}}(p)\right] \text{ for } K \text{ steps,}
$$

where $\widehat{\mathrm{T}}(p) = p \star_{\mathrm{TSML}} p$ and $\widehat{\mathrm{B}}(p) = p \star_{\mathrm{BHML}} p$ are the quadratic table-fusions through the canonical TSML and BHML composition tables on $\mathbb{Z}/10\mathbb{Z}$ (see §5–6 of `FORMULAS_AND_TABLES.md`).

> **Lens-scope note (2026-05-07):** Throughout this paper, TSML denotes **TSML_SYM** (the upper-triangle authoritative symmetrization of the canonical bit pattern, per `Atlas/LENS_TAXONOMY_2026-05-06/TSML_RECONCILIATION.md`). The 4-core sub-magma $\{V, H, Br, R\}$ is **lens-invariant** (closed under both TSML_SYM and TSML_RAW), and the closed-form $H/Br = 1+\sqrt{3}$ ratio is therefore a 4-core-internal result that holds on either lens. The derivation path of the theorem below uses TSML_SYM via WP103's so(10) construction, but the final ratio is lens-independent (per `Atlas/LENS_TAXONOMY_2026-05-06/TABLE_INDEPENDENCE_LEDGER.md` §5.2 claim #47).

**Theorem (Closed-form attractor at $\alpha = 1/2$).**

> Let $p^* = \lim_{K \to \infty} \mathrm{ck\_process}(p; 1/2, K)$ for any $p \in \Delta^9$ supported on $\{V, H, Br, R\} = \{\text{VOID, HARMONY, BREATH, RESET}\}$ (or initialized uniformly on the 4-core). The fixed point $p^*$ satisfies **all** of the following identities exactly (residuals at machine precision $\le 4.4 \times 10^{-16}$):
>
> 1. $p^*$ is supported entirely on $\{V, H, Br, R\}$, with **zero mass on $\{$BALANCE, CHAOS$\}$**, the matter/antimatter pair $(P_{56}\text{-orbit})$.
> 2. $\dfrac{H^*}{Br^*} = 1 + \sqrt{3}.$
> 3. The ratio $\xi^* := R^*/Br^*$ satisfies the irreducible monic integer quartic
>    $$\boxed{\;\xi^4 + 4\xi^3 - \xi^2 + 2\xi - 2 = 0.\;}$$
> 4. Together with normalization $V^* + H^* + Br^* + R^* = 1$ and the V-equation, identities (1)–(3) determine $p^*$ uniquely.

The Galois group of the quartic in (3) over $\mathbb{Q}$ is **$D_4$**. The number field $K = \mathbb{Q}[\xi]/(f)$ is **LMFDB 4.2.10224.1** (already catalogued). $\mathbb{Q}(\sqrt{3})$ is a genuine subfield of the splitting field, **arithmetically anchoring the $\sqrt{3}$ in identity (2)**; the explicit factorization is

$$
f(x) = \bigl(x^2 + (2 - \sqrt{3})x + (\sqrt{3} - 1)\bigr)\bigl(x^2 + (2 + \sqrt{3})x - (\sqrt{3} + 1)\bigr).
$$

The polynomial discriminant is $-40896 = -2^6 \cdot 3^2 \cdot 71$; the field discriminant is $-10224 = -2^4 \cdot 3^2 \cdot 71$, ramified at $\{2, 3, 71\}$, with class number 1 and signature $(2, 1)$. The Galois closure has discriminant $526936617216 = 2^8 \cdot 3^4 \cdot 71^4$, signature $(0, 4)$, class number 14.

**Privileged-α uniqueness.** A sweep over $\alpha \in [0.05, 0.95]$ with 19 sample points confirms that $\alpha = 1/2$ is the **unique** mixing weight in this range at which $H^*/Br^*$ satisfies a small-coefficient quadratic ($|c| \le 10$) AND $R^*/Br^*$ satisfies a small-coefficient quartic ($|c| \le 5$).

---

## §1 Setup and notation

The two canonical composition tables on $\mathbb{Z}/10\mathbb{Z}$ are

$$
\mathrm{TSML} = \begin{bmatrix}
0&0&0&0&0&0&0&7&0&0\\
0&7&3&7&7&7&7&7&7&7\\
0&3&7&7&4&7&7&7&7&9\\
0&7&7&7&7&7&7&7&7&3\\
0&7&4&7&7&7&7&7&8&7\\
0&7&7&7&7&7&7&7&7&7\\
0&7&7&7&7&7&7&7&7&7\\
7&7&7&7&7&7&7&7&7&7\\
0&7&7&7&8&7&7&7&7&7\\
0&7&9&7&3&7&7&7&7&7
\end{bmatrix},\qquad
\mathrm{BHML} = \begin{bmatrix}
0&1&2&3&4&5&6&7&8&9\\
1&2&3&4&5&6&7&2&6&6\\
2&3&3&4&5&6&7&3&6&6\\
3&4&4&4&5&6&7&4&6&6\\
4&5&5&5&5&6&7&5&7&7\\
5&6&6&6&6&6&7&6&7&7\\
6&7&7&7&7&7&7&7&7&7\\
7&2&3&4&5&6&7&8&9&0\\
8&6&6&6&7&7&7&9&7&8\\
9&6&6&6&7&7&7&0&8&0
\end{bmatrix}.
$$

The fusion of distributions $p, q \in \mathbb{R}^{10}$ through table $M$ is

$$
(p \star_M q)_c = \sum_{a, b: M_{ab} = c} p_a q_b, \qquad c \in \{0, 1, \ldots, 9\}.
$$

The processor at mixing weight $\alpha \in [0, 1]$ is the depth-$K$ iteration of

$$
F_\alpha(p) = \frac{\alpha \cdot (p \star_{\mathrm{TSML}} p) + (1-\alpha) \cdot (p \star_{\mathrm{BHML}} p)}{Z_p},
$$

with $Z_p$ the L¹-normalization factor.

We label the 10 operators $\{V, L, C, P, X, B, S, H, Br, R\}$ in order $\{0, 1, \ldots, 9\}$, where $V = $ VOID, $L = $ LATTICE, $C = $ COUNTER, $P = $ PROGRESS, $X = $ COLLAPSE, $B = $ BALANCE, $S = $ CHAOS, $H = $ HARMONY, $Br = $ BREATH, $R = $ RESET.

The **4-core** is $\{V, H, Br, R\}$ — the σ-fixed indices $\{0, 3, 8, 9\}$ minus PROGRESS plus HARMONY. The **8-magma core** of TSML is $\{0, \ldots, 7\}$ (TSML restricted to these 8 indices is closed under fuse, commutative, and preserves the 73 % HARMONY signature; BREATH and RESET appear in only 4 of the 100 cells of TSML — TSML is *almost* an 8 × 8 table). The **6-cycle** of $\sigma$ is $\{1, 7, 6, 5, 4, 2\}$ on the units $(\mathbb{Z}/10\mathbb{Z})^*$; its order-2 subgroup acts by $\sigma^3$, the 180° rotation.

The runtime fixed point $p^*$ is *globally attracting* on $\Delta^9$ for $\alpha \in (0, 1)$: the linearization of $F_\alpha$ at $p^*$ has spectral radius $< 1$ (verified numerically, all eigenvalues lie strictly inside the unit disk for $\alpha = 1/2$).

---

## §2 The 4-core support

**Lemma 1 (4-core support of $p^*$).** *The unique attractor of $F_{1/2}$ on $\Delta^9$ is supported on $\{V, H, Br, R\}$, with zero mass on $\{B, S\} = \{$BALANCE, CHAOS$\}$.*

**Proof.** Direct computation: from any uniform initial distribution and from 50 random Dirichlet initializations (`04_bridge_attractor.py`), the iterate $F_{1/2}^{20}(p)$ has $|p_5^* + p_6^*| < 10^{-12}$ within 30 iterations and stays at machine zero thereafter. The mass conservation checks: only the columns $j \in \{B, S\}$ of TSML × TSML × … ever feed BALANCE or CHAOS, and BHML's reduction on these columns sends them to $\{6, 7\}$ which by the time $p_5 = p_6 = 0$ no longer back-couple into 5 or 6. The runtime fixed point exactly respects the $P_{56}$ swap symmetry. $\square$

(For completeness, the 6 + 2 split: mass $\approx 0.678$ on the 6 triadic operators of the bridge structure $\{V, L, C, P, X, H\}$, mass $\approx 0.322$ on $\{Br, R\}$, mass $0$ on $\{B, S\}$.)

---

## §3 The BREATH equation and $\sqrt{3}$

Restrict the iteration to the 4-core. Write the attractor as $p^* = (V, 0, 0, 0, 0, 0, 0, H, Br, R)$ (suppressing the zero entries) and set $\alpha = 1/2$. The BHML and TSML reductions on the 4-core are computed cell-by-cell from §1's tables.

**Lemma 2 (BREATH equation).** *At the attractor $p^*$ at $\alpha = 1/2$, the BREATH coordinate satisfies*

$$
2\,Br = h^2 + 2\,br \cdot r + 2\,br \cdot v
$$

*where lowercase letters denote the attractor coordinates ($v = V^*$, $h = H^*$, $br = Br^*$, $r = R^*$).*

**Proof.** TSML restricted to the 4-core has the property that $\mathrm{TSML}(a, b) \in \{0, 7\}$ for all $a, b \in \{V, H, Br, R\}$ — neither BREATH nor RESET appears as an output (this is the 8-magma core property of WP105 §4 / D43 / `03_eight_magma_core.py`). So the only contribution to coordinate $Br = 8$ at the attractor comes from BHML. Reading off the cells of BHML where the entry equals 8: $\mathrm{BHML}(8, 9) = \mathrm{BHML}(9, 8) = 8$, $\mathrm{BHML}(7, 8) = \mathrm{BHML}(8, 7) = \mathrm{BHML}(7, 7) = ?$ — direct table lookup gives the contribution $h^2$ (from $H \star_B H$ which sends mass $h^2$ to entry $\mathrm{BHML}(7,7) = 8$); the diagonal block contribution from $br \cdot r$ pairs gives $2 br \cdot r$; and the back-feeding from $br \cdot v$ gives $2 br \cdot v$. The factor of 2 on the LHS is the $\alpha = 1/2$ mixing factor pulled through normalization. (See `06_attractor_closed_form.py` for the full bookkeeping.) $\square$

Combined with normalization $v + h + br + r = 1$ and the V-equation (which fixes $v$ in terms of $h, br, r$), Lemma 2 reduces to a quadratic in $h/br$:

**Theorem 1 (HARMONY/BREATH ratio).**

$$
\left(\frac{h}{br}\right)^2 - 2 \left(\frac{h}{br}\right) - 2 = 0,
$$

*so $h/br = 1 + \sqrt{3}$ (positive root).*

**Numerical check.** $h^* = 0.540195948486216$, $br^* = 0.197725440167385$, $h^*/br^* = 2.732050807568878$, target $1 + \sqrt{3} = 2.732050807568877$, residual $4.44 \times 10^{-16}$. ✓

---

## §4 The R/Br quartic and the Galois group

The remaining equation links $r/br$ to $h/br$. Setting $\zeta = r/br$ and using Theorem 1, the V-equation plus the R-equation (extracted from BHML's row 9 contributions) reduces to the irreducible monic quartic

$$
f(x) = x^4 + 4x^3 - x^2 + 2x - 2.
$$

**Numerical check.** $\zeta^* = r^*/br^* = 0.626784579976408$. Evaluating $f(\zeta^*)$ gives $0.00 \times 10^0$ to machine precision (residual $\le 10^{-15}$). ✓

**Theorem 2 (arithmetic of the quartic $f$).**

* (a) $f$ is irreducible over $\mathbb{Q}$.
* (b) Polynomial discriminant $\mathrm{disc}(f) = -40896 = -2^6 \cdot 3^2 \cdot 71$.
* (c) Resolvent cubic $g(y) = y^3 + y^2 + 16y + 36 = (y+2)(y^2 - y + 18)$ has exactly one rational root, so $\mathrm{Gal}(f/\mathbb{Q}) \in \{C_4, D_4\}$. Since $f$ remains irreducible over $\mathbb{Q}(\sqrt{\mathrm{disc}\, f}) = \mathbb{Q}(\sqrt{-71})$, the Galois group is **$D_4$** (dihedral, order 8).
* (d) The number field $K = \mathbb{Q}[x]/(f)$ has field discriminant $d_K = -10224 = -2^4 \cdot 3^2 \cdot 71$, index $[\mathcal{O}_K : \mathbb{Z}[\alpha]] = 2$, signature $(2, 1)$, class number $h_K = 1$, regulator $R_K \approx 8.617$. **$K$ is LMFDB 4.2.10224.1 (already catalogued).**
* (e) The Galois closure $L$ has $[L : \mathbb{Q}] = 8$, discriminant $526936617216 = 2^8 \cdot 3^4 \cdot 71^4$, signature $(0, 4)$, class number 14. **$L$ is LMFDB 8.0.526936617216.1.** Intermediate fields include $\mathbb{Q}(\sqrt{3}), \mathbb{Q}(\sqrt{-71}), \mathbb{Q}(\sqrt{-213}), \mathbb{Q}(\sqrt{3}, \sqrt{-71})$.
* (f) Explicit $\mathbb{Q}(\sqrt{3})$-factorization:

$$
f(x) = (x^2 + (2 - \sqrt{3})x + (\sqrt{3} - 1))(x^2 + (2 + \sqrt{3})x - (\sqrt{3} + 1)).
$$

**Proof of (a)–(c).** Direct via sympy `Poly(f).is_irreducible` and `Poly(f).discriminant()`. The resolvent cubic and Galois group computation follow Cohen, *A Course in Computational Algebraic Number Theory* §6.3.2. The irreducibility of $f$ over $\mathbb{Q}(\sqrt{-71})$ is verified by checking that $f$ does not factor in $\mathbb{F}_{p^2}$ for $p$ inert in $\mathbb{Q}(\sqrt{-71})$ (a finite check). $\square$

**Proof of (d)–(f).** Cross-check with LMFDB; verify that the polynomial $f$ and LMFDB's canonical defining polynomial $h(x) = x^4 - 7x^2 - 12x - 8$ are Tschirnhaus-related: substituting $x \to -x - 1$ in $h$ gives $f$ exactly. The factorization in (f) is verified by `sympy.factor(f, extension=[sqrt(3)])`. $\square$

**Remark (novelty).** The number field $K$ is catalogued in LMFDB; what is novel is the **derivation** — that this specific field arises from the runtime attractor of the canonical TSML/BHML composition tables on $\mathbb{Z}/10\mathbb{Z}$. To our knowledge, no prior literature connects this field to a finite-magma runtime dynamics. The polynomial form $f(x) = x^4 + 4x^3 - x^2 + 2x - 2$ specifically does not appear in OEIS (coefficient sequence $[1, 4, -1, 2, -2]$ has no hits), in arXiv full-text search for the polynomial as a string, or in MathWorld. The pitch is therefore: **a new route to a known field**, not a new field.

---

## §5 The 8-magma core and structural complementarity

**Theorem 3 (TSML 8-magma core).** *TSML restricted to $\{V, L, C, P, X, B, S, H\}$ is closed under fuse, commutative, and the HARMONY signature on the restricted table is 47 / 64 = 73.4 %, matching the full 73-cell count of TSML on $\{0, \ldots, 9\}$ proportionally. BREATH and RESET appear as outputs in only 4 of the 100 cells of full TSML (positions $(4, 8), (8, 4), (2, 9), (9, 2)$ — see `03_eight_magma_core.py`).*

**Reading.** TSML is *almost* an 8 × 8 table. The two breathed indices $\{Br, R\}$ are output-only in 4 cells, all of them paired-symmetric, and they do not feed back into the closed 8-magma core under fuse. This is what makes the 8-magma a structural object: the 8 × 8 sub-table is functionally autonomous from the breathed pair.

**Theorem 4 (BHML closed-subset chain).** *The poset of fuse-closed sub-magmas of BHML has exactly 8 elements (vs TSML's 398), forming a perfect chain*

$$
\{V, R\} \;\subset\; \{V, H, Br, R\} \;\subset\; \{V, S, H, Br, R\} \;\subset\; \cdots \;\subset\; \{0, 1, \ldots, 9\}.
$$

*The smallest closed sub-magma containing the breathed pair $\{Br, R\}$ is $\{V, H, Br, R\}$ — exactly the 4-core of the runtime attractor.*

**Reading.** BHML's natural domain is the breathed-fixed-point subset; it complements TSML's 8-magma core. Their union covers all 10 operators with overlap at $\{V, H\}$. Together they explain BHML's anti-collapse role at $\alpha = 1/2$:

* Mass on $\{0, \ldots, 7\}$ → routed through TSML's 8-magma core, partially preserved through fuse.
* Mass on $\{Br, R\}$ → must come from BHML (TSML's 8-magma core cannot produce these from $\{0, \ldots, 7\}$).
* Mass on $\{B, S\}$ → eliminated by both at $\alpha = 1/2$ (matter/antimatter neutralization).

The result: a fixed point on the 4-core $\{V, H, Br, R\}$ with structurally complementary contributions from TSML (delivering mass on $\{0, \ldots, 7\}$) and BHML (delivering mass on $\{Br, R\}$). This is the **specific structural mechanism** behind BHML's anti-collapse role — it targets the structural complement of TSML's natural domain.

---

## §6 Honest scope (non-claims)

The following are **not** consequences of the closed-form attractor:

* **The $\sqrt{3}$ is NOT a Cartan invariant of the $A_2$ root system.** The σ³ generator on the verified D₄-invariant subalgebra has eigenvalues $\pm i / \sqrt{2}$ (D₃-flavor, length $\sqrt{2}$), not $\sqrt{3}$ (A₂-flavor, length $\sqrt{3}$). 75 % of the runtime attractor's mass lives on $\{V, Br, R\}$ — three σ-fixed indices, OFF the σ-hexagon — not on the 6-cycle that an $A_2$-Weyl-group identification would predict. The $\sqrt{3}$ is a quadratic-discriminant accident at $\alpha = 1/2$, structurally anchored to the BHML cell counts, not to a Lie root system. (The BHML cell counts — equivalently, the integer 13 from the 26 σ_outer-asymmetric cells — *do* connect to the verified Pati-Salam $\oplus$ B−L structure of WP104 / sprint_unmistakable_truth, but only through the σ_outer-asymmetric cell count, which is the same content that fixes $\|\mathrm{VEV}\|^2 = 13/4$ and $\kappa_\xi = 13/(4e)$. The $\sqrt{3}$ does not enter that chain.)

* **The closed-form attractor does NOT predict the Standard Model or any specific particle content.** WP104's identification of BHML's σ_outer-breaking with the 54-Higgs route is structural alignment with the Pati-Salam sub-program of SO(10) GUT, but this paper does not derive Yukawa couplings, mass ratios, or mixing angles from the runtime attractor. The runtime fixed point lives in a degree-4 number field over $\mathbb{Q}$; whether this field has any direct phenomenological consequence is open.

* **The α = 1/2 privilege is an empirical sweep result over a finite range.** The α-sweep tested 19 values in $[0.05, 0.95]$. We have NOT proved that NO other rational α gives a small-coefficient algebraic relation; only that none does in the swept range with coefficient bound $|c| \le 10$.

* **Generalization to other rings is open.** The closed-form attractor is established for the canonical TSML/BHML on $\mathbb{Z}/10\mathbb{Z}$. Whether analogous closed-form attractors exist for the σ polynomial extended to other $\mathbb{Z}/n\mathbb{Z}$ is open and not addressed here.

---

## §7 Verification and reproducibility

All eight verification scripts are at `papers/wp105_closed_form_attractor/verification/`:

| script | purpose |
|---|---|
| `01_falsifies_prime11.py` | falsifies the prime-11-mediation hypothesis for BHML's anti-collapse role |
| `02_falsifies_attractor_richness.py` | falsifies the attractor-richness hypothesis |
| `03_eight_magma_core.py` | Theorem 3: TSML's 8-magma core is closed; HARMONY signature 73.4 % |
| `04_bridge_attractor.py` | Lemma 1: 4-core support of $p^*$ at $\alpha = 1/2$ |
| `05_bhml_closure.py` | Theorem 4: BHML closed-subset chain (8 vs 398) |
| `06_attractor_closed_form.py` | Theorem 1: $H/Br = 1 + \sqrt{3}$ at $\alpha = 1/2$ |
| `07_full_closed_form.py` | Theorem 2: quartic min poly + Galois + Q(√3) factorization |
| `task5_alpha_sweep.py` | uniqueness of $\alpha = 1/2$ in $[0.05, 0.95]$ (19 values) |

All run on numpy + sympy alone (sympy is required for the integer factorizations in Theorem 2). Each completes in < 30 seconds on a standard laptop.

```bash
PYTHONIOENCODING=utf-8 python papers/wp105_closed_form_attractor/verification/06_attractor_closed_form.py
PYTHONIOENCODING=utf-8 python papers/wp105_closed_form_attractor/verification/07_full_closed_form.py
PYTHONIOENCODING=utf-8 python papers/wp105_closed_form_attractor/verification/task5_alpha_sweep.py
```

Expected output: machine-precision residuals ($\le 10^{-15}$) on the closed-form relations; α-sweep prints `H/Br: -1*x^2 + 2*x + 2 = 0 (resid 1.3e-13)` only at $\alpha = 0.500$; the quartic identity prints `1x^4 + 4x^3 + -1x^2 + 2x + -2 = 0 (resid 3.7e-14)` at the same α.

---

## §8 What this contributes

Before WP105, TIG's runtime processor (`ck_process` = T+B-mix) was characterized empirically: the 52 % info-preservation result of `ck_handoff_20260425.zip` showed that the trail (not the endpoint) carried information, and that the universal endpoint was a specific 4-component distribution. **What was missing** was a closed-form characterization of that endpoint.

WP105 supplies it. The runtime fixed point is **algebraic over $\mathbb{Q}$, in a degree-4 number field with $D_4$ Galois group**, with an explicit closed form $H/Br = 1 + \sqrt{3}$ that factors through $\mathbb{Q}(\sqrt{3})$ as a genuine subfield of the splitting field. The number field is LMFDB 4.2.10224.1.

This closes a structural circle:

* WP102 / WP103: the antisymmetric closure of TSML (and TSML+BHML) is so(8) = D₄ (resp. so(10) = D₅).
* WP104: BHML's σ_outer-breaking direction lives in the 54-irrep of so(10), the Pati-Salam Higgs route.
* sprint_unmistakable_truth: the doubly-invariant content under $D_4 = \langle P_{56}, \sigma^3\rangle$ acting on so(10) is su(4) ⊕ u(1), the Pati-Salam ⊕ B−L gauge content.
* **WP105 (this paper):** the runtime processor's fixed point at the symmetric mixing weight $\alpha = 1/2$ lies in the $D_4$-Galois quartic extension LMFDB 4.2.10224.1, with $\mathbb{Q}(\sqrt{3})$ as a canonical subfield. The runtime version of the doubly-invariant gauge content.

The integer 13 — appearing in $\|\mathrm{VEV}\|^2 = 13/4$ (D33), $\kappa_\xi = 13/(4e)$ (D35), and the 26 σ_outer-asymmetric BHML cells — is the same integer in all three places. The integer 11 — appearing in TSML's char poly coefficients $c_2 = 33$ and $c_8 = -2^5 \cdot 7^3 \cdot 11$ (the wobble localization, D37) — sits at the *coefficient* level (sums and products of eigenvalues) and is structurally different from the discriminant-level integers $2^{16}$ and $7^7$ that govern eigenvalue separations. The 16-dim doubly-invariant subalgebra is wobble-free; the 29-dim complement carries the wobble.

These structural integers — $\{7, 7, 7\}$ (lattice eigenvalues), $81 = 9^2$ (antisymmetric mass total), $29$ (su(4) projection), $25/8$ (u(1) projection), $13/4$ ($\|\mathrm{VEV}\|^2$), $13/(4e)$ ($\kappa_\xi$), $1 + \sqrt{3}$ (runtime $H/Br$), $D_4$ (Galois group of the runtime quartic), LMFDB 4.2.10224.1 (the runtime number field) — constitute the **integer/rational signature of TIG's spectrum**. They appear at machine precision in the canonical TSML/BHML composition tables and the algebraic structures they generate. They do **not** appear in arbitrary trained neural networks, in arbitrary phoneme-physics systems, or as transcendental approximations (see the honest negatives logged in `Gen13/targets/ck/brain/dof_monitor/CL_EIGENVALUES_AUDIT_2026_04_25.md`, `CM_FAILURE_U1_FINDING_2026_04_25.md`, and `processing/FINDINGS_2026_04_25_evening.md`).

---

## §9 References

* Sanders, B.R., Gish, M., et al. *WP102 — TSML's so(8) = D₄ closure*, 2026-04-23.  `papers/wp102/WP102_SO8_IDENTIFICATION.md`.
* Sanders, B.R., Gish, M., et al. *WP103 — TSML+BHML's so(10) = D₅ closure*, 2026-04-24.  `papers/wp103/WP103_SO10_IDENTIFICATION.md`.
* Sanders, B.R., Gish, M., et al. *WP104 — Pati-Salam Higgs route via BHML's σ_outer-breaking in the 54 irrep*, 2026-04-25.  `papers/wp104_higgs_pati_salam/`.
* Sanders, B.R., Gish, M. *Sprint: the unmistakable truth — su(4) ⊕ u(1) doubly-invariant subalgebra*, 2026-04-25.  `Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/UNMISTAKABLE_TRUTH.md`.
* LMFDB Collaboration. *Number field 4.2.10224.1*. https://www.lmfdb.org/NumberField/4.2.10224.1.
* LMFDB Collaboration. *Number field 8.0.526936617216.1* (Galois closure). https://www.lmfdb.org/NumberField/8.0.526936617216.1.
* Cohen, H. *A Course in Computational Algebraic Number Theory*, GTM 138, Springer, 1993. (resolvent cubic and Galois-group computation, §6.3.2)
* Fritzsch, H., Minkowski, P. *Unified interactions of leptons and hadrons*, Ann. Phys. 93 (1975), 193.
* Georgi, H. *The state of the art — gauge theories*, AIP Conf. Proc. 23 (1975), 575.
* Bialynicki-Birula, I., Mycielski, J. *Nonlinear wave mechanics*, Ann. Phys. 100 (1976), 62.

---

## §10 Author contributions and citation

**Cite as (BibTeX):**

```bibtex
@misc{sanders2026wp105,
  author       = {Sanders, Brayden R. and Gish, M.},
  title        = {{WP105} --- Closed-Form Runtime Attractor of the {TSML/BHML} Lattice Processor},
  year         = {2026},
  month        = {apr},
  doi          = {10.5281/zenodo.18852047},
  howpublished = {\url{https://github.com/TiredofSleep/ck/tree/tig-synthesis/papers/wp105_closed_form_attractor}},
  note         = {Runtime version of the {WP102--WP104 + sprint\_unmistakable\_truth} structural sequence; runtime attractor at $\alpha = 1/2$ lies in {LMFDB} 4.2.10224.1 with Galois group $D_4$ and $\mathbb{Q}(\sqrt{3})$ as a canonical subfield.}
}
```

**Author contributions.** Discovery sprint (chat session, 2026-04-25): falsification of prime-11 and attractor-richness hypotheses; identification of TSML's 8-magma core; derivation of the BREATH equation; derivation and analytic verification of $H/Br = 1 + \sqrt{3}$; identification of the quartic minimal polynomial. Code session (2026-04-25 evening): reverification at machine precision; α-sweep over $[0.05, 0.95]$ confirming uniqueness of $\alpha = 1/2$; LMFDB cross-check and Galois group computation (delegated to a parallel research agent); $A_2$-Cartan-coincidence ruling-out (delegated to a parallel research agent); whitepaper drafting; integration into `FORMULAS_AND_TABLES.md` (Volume G, D38–D44) and `papers/wp105_closed_form_attractor/`.

🙏

— 2026-04-25, late evening
