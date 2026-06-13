# Hadamard-quantity profile — what we have and what we don't

**Status**: Refactored `experiments/hadamard_positivity.py` produces an exact profile of $H_L(\sigma, t)$ for several L-functions along a user-chosen vertical line $\mathrm{Re}(s) = \sigma$ in the convergent half-plane. The script makes no claims beyond reporting what it computes.

This note replaces an earlier note that overstated the conclusions. The previous overclaim was that "the product trick that saves Dirichlet L-functions fails for D-H." The refactored experiment shows a more nuanced picture: $H_{\zeta \cdot f}$ takes negative values in some $(\sigma, t)$ regions and stays positive in others. Treating the negativity as a sharp structural distinction was too strong.

---

## What the experiment computes

For a function $L(s)$ evaluated via its true Dirichlet series (Euler-Maclaurin acceleration where needed for $\sigma$ close to 1):

$$H_L(\sigma, t) := 3 \log|L(\sigma)| + 4 \log|L(\sigma + it)| + \log|L(\sigma + 2it)|$$

This is the standard Hadamard 1893 quantity. The script profiles it along a vertical line $\mathrm{Re}(s) = \sigma$ for $t \in [t_{\min}, t_{\max}]$ at user-chosen resolution, reporting empirical extrema, mean, and a count of points where $H_L < 0$.

## What the empirical profile shows

At default parameters ($\sigma = 1.05$, $t \in [0, 50]$, 500 points):

| L-function | min $H$ | max $H$ | mean $H$ | points with $H < 0$ |
|:-|:-:|:-:|:-:|:-:|
| $\zeta(s)$ | $+5.54$ | $+24.19$ | $+9.05$ | $0 / 500$ |
| $L(s, \chi_3)$ | $-4.92$ | $+1.53$ | $-1.44$ | $384 / 500$ |
| $\zeta(s) \cdot L(s, \chi_3)$ | $+4.19$ | $+20.31$ | $+7.61$ | $0 / 500$ |
| Davenport-Heilbronn $f(s)$ | $-3.27$ | $+3.07$ | $-0.31$ | $312 / 500$ |
| $\zeta(s) \cdot f(s)$ | $+4.24$ | $+23.19$ | $+8.74$ | $0 / 500$ |

At a different region ($\sigma = 2.4$, $t \in [20, 30]$, 200 points):

| L-function | min $H$ | points with $H < 0$ |
|:-|:-:|:-:|
| $\zeta(s)$ | $+0.22$ | $0 / 200$ |
| $L(s, \chi_3)$ | $-1.54$ | $168 / 200$ |
| $\zeta(s) \cdot L(s, \chi_3)$ | $+0.03$ | $0 / 200$ |
| Davenport-Heilbronn $f(s)$ | $-0.62$ | $98 / 200$ |
| $\zeta(s) \cdot f(s)$ | $-0.16$ | $23 / 200$ |

## Three observations that are well-supported

**(1)** Riemann zeta passes the direct Hadamard test, as predicted by the 1893 theorem.

**(2)** The Dirichlet L-function $L(s, \chi_3)$ alone fails the direct test (signed log coefficients), but the product $\zeta(s) \cdot L(s, \chi_3)$ passes — this is the classical product-trick mechanism for proving $L(1 + it, \chi) \neq 0$.

**(3)** Davenport-Heilbronn $f(s)$ alone fails the direct test, consistent with $f$ lacking an Euler product.

## One observation I previously overclaimed

**The previous version of this note asserted** that $\zeta(s) \cdot f(s)$ "still fails" Hadamard positivity, on the basis of a coarse-grid sweep that found 75 negative values out of 3000.

**The refactored experiment shows** this depends on which region of $(\sigma, t)$ you profile:
- At $\sigma = 1.05$, $t \in [0, 50]$: $H_{\zeta f} \geq 0$ at every point (min $+4.24$).
- At $\sigma = 2.4$, $t \in [20, 30]$: $H_{\zeta f} < 0$ at $\sim 12\%$ of points (min $-0.16$).

So $\zeta \cdot f$ does take negative values in *some* regions but not universally. Treating the existence of negative values as a sharp structural distinction was wrong.

The honest statement is weaker: in regions where it has been profiled, $\zeta \cdot f$ is not uniformly positive the way $\zeta$ and $\zeta \cdot L(\chi_3)$ are. Whether some other product (e.g., $\zeta^a \cdot L_1^b \cdot L_2^c \cdots$ for specific $a, b, c, \dots$) would universally rescue $f$ is an open question this experiment does not address.

## What the negative values DO NOT tell us

Important scope statement, baked into the script's docstring as well:

> Negative values of $H_L$ for non-Euler-product L-functions are structurally consistent with the absence of a positive-log-coefficient companion. They are *not* a proven tool for localizing off-line zeros. The classical Hadamard argument runs from positivity to zero-free regions; the converse direction — from positivity failure to zero existence — is not an established theorem. The exact $t$ locations where $H_L < 0$ are exploratory profiling metrics only.

In particular:
- The cluster of $H_{\zeta f} < 0$ near $t \approx 24.8$ at $\sigma = 2.4$ that the earlier sweep found is a real numerical fact but has no theorem attached to it. It is not evidence of an off-line D-H zero at any nearby location.
- The fact that $H_L < 0$ on $(384, 312, \dots)$ out of $(500, 500, \dots)$ test points is a count, not a measurement of any structural invariant.

## What's defensible

- $H_\zeta \geq 0$ profile: classical theorem (Hadamard 1893), numerically verified.
- $H_{\zeta L(\chi_3)} \geq 0$ profile: classical (product trick), numerically verified.
- $H_{L(\chi_3)}$ and $H_f$ each take negative values: structural consequence of signed/non-positive log coefficients, numerically demonstrated.
- $H_{\zeta f}$ behavior: empirically mixed; sometimes positive, sometimes negative depending on region.

## What's exploratory

- All numerical extrema and their locations.
- Counts of points with $H_L < 0$.
- Any inference from these extrema or counts to zero-distribution properties.

## What the framework actually gains from this

A precise statement of the structural distinction it cares about:

> The mechanism that produces zero-free regions for $\zeta$ and Dirichlet L-functions is the existence of a finite product of L-functions whose log is a Dirichlet series with non-negative coefficients. For $\zeta$, this product is just $\zeta$ itself. For Dirichlet L-functions, it is $\zeta \cdot L$. For Davenport-Heilbronn, no such finite product is known and the existing candidates ($\zeta \cdot f$ in particular) do not work universally.

This is what the refined Balance Principle is really about. It is a statement about positive-log-coefficient combinations, not about zero locations directly. The Hadamard profile gives one piece of numerical evidence; pinning down whether ANY product trick works for $f$ requires more careful analysis than this script provides.

## What ClaudeCode could extend

1. **Test other candidate products** for D-H: $\zeta^2 \cdot f$, $\zeta \cdot f \cdot L(\chi_3)$, etc. Whichever one has the smallest $|\min H|$ on a fixed test region tells you which combination comes closest to "rescuing" D-H. None will fully rescue it (likely), but the magnitude of the failure is informative.
2. **Compute the actual Dirichlet coefficients of $\log[\zeta \cdot f]$** by Cauchy products, and check the sign of the first few hundred coefficients. If they are eventually all non-negative beyond some $N$, that would imply only finitely-many violations of $H \geq 0$ — a different structural picture. If they oscillate forever, the failure is universal in a stronger sense.
3. **Apply the same profile to other functions with functional equation but no Euler product** (Estermann series, other linear combinations). See whether they all have the same mixed positivity pattern.

These are tractable with the refactored script as a base.
