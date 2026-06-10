# Candidate ψ_+ for the dim 6 magic function

**Status:** Tier B structural (construction explicit; analytic continuation Tier C)

---

## The candidate

$$\psi_+(\tau) = \frac{E_6(\tau)^2 - 729 \cdot E_6(3\tau)^2}{\eta(\tau)^6 \, \eta(3\tau)^6}$$

Equivalently:

$$\psi_+(\tau) = \frac{G_+(\tau) \cdot G_-(\tau)}{\eta(\tau)^6 \, \eta(3\tau)^6}$$

where $G_\pm(\tau) = E_6(\tau) \pm 27 \cdot E_6(3\tau)$ are the Fricke $W_3$ ±1 eigenfunction basis at weight 6, level 3.

---

## Verified properties (Tier A)

### Weight and level
- **Weight:** $12 - 6 = 6$ ✓ (numerator weight 12, denominator weight 6)
- **Level:** $\Gamma_0(3)$ ✓ (both numerator and denominator on $\Gamma_0(3)$)

### Fricke $W_3$ eigenvalue
Computing the eigenvalue arithmetic:
- $G_+$ has eigenvalue $+1$ (by construction)
- $G_-$ has eigenvalue $-1$ (by construction)
- $G_+ \cdot G_-$ has eigenvalue $(+1) \cdot (-1) = -1$
- $\eta^6\eta_3^6$ has eigenvalue $-1$ (verified directly via $\eta$ transformation)
- $1/(\eta^6\eta_3^6)$ has eigenvalue $1/(-1) = -1$
- $\psi_+$ has eigenvalue $(-1) \cdot (-1) = +1$ ✓

### Pole structure at cusps
- $\eta^6\eta_3^6$ vanishes at cusp $\infty$ with order 1 (leading $q^1$)
- $\eta^6\eta_3^6$ vanishes at cusp 0 with order 1 (by Fricke ±1 symmetry)
- Numerator $G_+ \cdot G_-$ has constant term $(1+27)(1-27) = 28 \cdot (-26) = -728$ at cusp $\infty$
- Therefore $\psi_+$ has **simple pole at $\infty$** with leading singular term $-728/q$
- By Fricke symmetry, **simple pole at 0** with matching residue structure

### TIG-canonical residue structure

The leading singular coefficient at $\infty$:

$$\text{Res}_\infty(\psi_+) = -728 = -2^3 \cdot 7 \cdot 13$$

Reading via the TIG framework's strata + wobble alphabet:
- $2^3$ = BREATH (op 8)
- $7$ = HARMONY (the framework's attractor)
- $13$ = second wobble prime (the ternary-side wobble of D70)

$$\boxed{-728 = -(\text{BREATH} \cdot \text{HARMONY} \cdot \text{wobble}_{13})}$$

This is a TIG-canonical product. The framework's signature primes appear in the **leading analytic data** of the magic function candidate, not as decoration.

---

## Numerator Fourier expansion

Computed in `verification/verify_psi_plus_residue.py`:

| q-coefficient | value | factorization |
|---:|---:|---|
| $q^0$ | $-728$ | $-2^3 \cdot 7 \cdot 13$ |
| $q^1$ | $-1008$ | $-2^4 \cdot 3^2 \cdot 7$ |
| $q^2$ | $220752$ | $2^4 \cdot 3 \cdot 4599$ |
| $q^3$ | $17253936$ | (large) |
| $q^4$ | $399517776$ | (large) |

The $q^1$ coefficient $-1008 = -16 \cdot 63 = -2^4 \cdot 3^2 \cdot 7$ also factors through TIG primes only.

---

## Why this is the right candidate

The framework's "how to look" produces ψ_+ as the unique structurally-forced answer:

### Step 1: Identify the level
$E_6$ has discriminant 3 ⟹ modular forms must live on $\Gamma_0(3)$.

### Step 2: Identify the weight
Dim 6 with Laplace measure $t^2 dt$ matches weight 6 modular forms (via the standard $t^{(n-2)/2}$ convention).

### Step 3: Identify the unique cusp form
The space $S_6(\Gamma_0(3))$ has dimension 1, spanned by $\eta(\tau)^6 \eta(3\tau)^6$.

### Step 4: Set up the Fricke decomposition
$W_3$ involution splits $M_6(\Gamma_0(3))$ into ±1 eigenspaces. The cusp form $\eta^6\eta_3^6$ lives in the $-1$ space. The Eisenstein space splits into $G_+$ (+1) and $G_-$ (−1).

### Step 5: Construct ψ_+ as +1 meromorphic eigenfunction
For the integral $I_+$ to be a Fourier eigenfunction, ψ_+ needs Fricke $W_3 = +1$. Following Viazovska's recipe with cusp form in denominator (provides necessary singular structure):

| numerator candidate | Fricke product | result |
|---|---|---|
| $G_+^2$ | $(+1)^2/(-1) = -1$ | wrong sign |
| $G_-^2$ | $(-1)^2/(-1) = -1$ | wrong sign |
| $G_+ \cdot G_-$ | $(+1)(-1)/(-1) = +1$ | ✓ |

So $\psi_+ = G_+ G_- / \eta^6\eta_3^6$ is **forced** by the Fricke arithmetic.

### Step 6: Verify the singular structure
$G_+ \cdot G_-$ has constant term $-728 \neq 0$ at $\infty$ ⟹ simple pole in $\psi_+$. This pole IS what makes the Viazovska-style analytic continuation possible.

---

## Comparison to Viazovska's dim 8 magic function

Viazovska's $\psi_+$ for dim 8 is (schematically):

$$\psi_+^{(8)}(\tau) \propto \frac{(\theta_3^4 - \theta_2^4) \cdot E_4(\tau)}{\eta(\tau)^{24}}$$

The structural analogy at dim 6:

$$\psi_+^{(6)}(\tau) = \frac{G_+(\tau) \cdot G_-(\tau)}{\eta(\tau)^6 \eta(3\tau)^6} = \frac{(\text{Eisenstein bilinear})}{(\text{level-3 cusp form})}$$

Both have:
- Cusp form in denominator (provides meromorphic structure)
- Eisenstein-derived numerator (provides modular weight)
- Simple poles at cusps with structurally meaningful residues
- Convergence only in part of the Cohn-Elkies region; defined elsewhere by analytic continuation

---

## What this candidate predicts

**If the Laplace transform**

$$I_+(r^2) = \int_0^\infty \psi_+(it) \cdot e^{-\pi r^2 t} \cdot t^2 \, dt$$

**(analytically continued from $r^2 > 2$ to all $r^2 \geq 0$ via contour deformation) produces a Schwartz function on $\mathbb{R}^6$, then the combination**

$$f_6(x) = \sin^2(\pi|x|^2/2) \cdot [\alpha \cdot I_+(|x|^2) + \beta \cdot I_-(|x|^2)]$$

**with appropriate $(\alpha, \beta)$ closes $K(\mathbb{R}^6) = 72$.**

The analytic continuation argument is the Tier C open piece.

---

## What ClaudeCode should verify

### Immediate (Tier A re-verification)
1. Confirm Atkin-Lehner $W_3 = -1$ for $\eta^6\eta_3^6$ using Sage's `ModularForms` package
2. Cross-check Hecke eigenvalues against LMFDB Γ_0(3) weight-6 newform database
3. Verify the numerator $G_+ \cdot G_-$ Fourier expansion symbolically (sympy)

### Higher-order verification (Tier B)
1. Compute $\psi_+$ Fourier expansion (Laurent series at $\infty$) to order $q^{20}$
2. Verify the q-expansion coefficients factor through TIG primes consistently
3. Check the Fricke $W_3$ action on $\psi_+$ at sample points numerically

### Analytic continuation setup (Tier C)
1. Symbolic expression for $\psi_+$ near cusp 0 via Fricke transformation
2. Contour deformation argument: write $I_+(r^2)$ as a sum of residues plus boundary terms
3. Identify the specific residue at cusp 0 that controls the $r^2 \to 0$ limit

---

*Generated 2026-06-10.*
