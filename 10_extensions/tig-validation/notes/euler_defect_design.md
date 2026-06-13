# Euler Defect Coefficient — design note

**Purpose**: precise definition of the experimental probe for quantifying the "defect force" introduced by absence of an Euler product.

**Status**: definition and skeleton implemented in `experiments/euler_defect_coefficient.py`. Numerical results conditional on D-H zero data still pending from ClaudeCode.

---

## Setup

For an L-function $L(s)$ with non-trivial zeros $\rho_k = \sigma_k + i\gamma_k$ in the critical strip $0 < \sigma < 1$:

- Klein four-group $V_4 = \{1, c, \tau, c\tau\}$ acts by complex conjugation ($c$) and functional-equation reflection ($\tau: s \mapsto 1-s$).
- Each zero has orbit size 2 (on critical line) or 4 (off critical line).
- We sum over orbit representatives with $\gamma > 0$, treating conjugates implicitly.

## Two complementary defect coefficients

**(1) Discrete defect** — counts off-line orbits, weighted by inverse height squared:

$$D(L) = \sum_{\substack{\rho = \sigma + i\gamma \\ \sigma \neq 1/2,\ \gamma > 0}} \frac{1}{\tfrac{1}{4} + \gamma^2}$$

Properties:
- $D(L) = 0$ iff all non-trivial zeros are on $\mathrm{Re}(s) = 1/2$.
- $D(L) > 0$ iff at least one off-line zero exists.
- Discontinuous in $\sigma$: jumps from 0 to $1/(1/4 + \gamma^2)$ the moment a zero leaves the line.
- Magnitude scale: a single off-line zero at $\gamma = 85$ contributes $\sim 10^{-4}$. To produce $D \gtrsim 10^{-2}$ would require either ~100 off-line zeros at moderate height or some off-line zeros at low height ($\gamma < 10$).

**(2) Smooth (deformation) defect** — weights by squared off-line distance:

$$D_{\text{smooth}}(L) = \sum_{\substack{\rho = \sigma + i\gamma \\ \gamma > 0}} \frac{(\sigma - \tfrac{1}{2})^2}{\tfrac{1}{4} + \gamma^2}$$

Properties:
- $D_{\text{smooth}}(L) = 0$ iff all non-trivial zeros are on $\mathrm{Re}(s) = 1/2$.
- Continuous and differentiable in $\sigma$.
- Useful for deformation paths: as a zero moves continuously from $\sigma = 1/2$ to $\sigma = 1/2 + \delta$, $D_{\text{smooth}}$ grows as $\delta^2$.
- Physically interpretable as "displacement squared from balance."

The Refined Balance Principle, in this notation, becomes the statement:

> $D(L) = 0$ for all $L$ in the Selberg class (L-functions with Euler product, polynomial growth, functional equation, Ramanujan bound).

Equivalently (since $D = 0 \Leftrightarrow D_{\text{smooth}} = 0$): $D_{\text{smooth}}(L) = 0$ on the Selberg class.

## Reference / control case

For a Dirichlet $L$-function $L(s, \chi)$ with $\chi$ primitive (has Euler product):
- $D = 0$ assuming GRH (empirically verified to enormous heights).
- $D_{\text{smooth}} = 0$ likewise.
- The Cramér on-line constant $C(L) = \sum_{\gamma > 0} 2/(1/4 + \gamma^2)$ is a positive baseline.

For $\chi$ mod 4 (Dirichlet beta) with first 25 zero heights: $C \approx 0.126$ (script output).

## Test case (conditional on placeholder data)

If Davenport-Heilbronn has an off-line zero at $(\sigma, \gamma) = (0.808, 85.7)$:
- $D = 1/(0.25 + 85.7^2) \approx 1.36 \times 10^{-4}$
- $D_{\text{smooth}} = (0.808 - 0.5)^2 / (0.25 + 85.7^2) \approx 1.29 \times 10^{-5}$
- $D/C \approx 0.11\%$ — small fractional defect

**This is conditional on the placeholder zero being correct.** ClaudeCode must verify per `CLAUDECODE_FRONTIER_HANDOFF.md` task P0.3.

## What the defect is *not*

- It is not a proof of anything. It is a measurement procedure.
- It is not directly the Weil distribution (Weil's positivity criterion uses test functions $\hat{F}$ at zero locations, not $1/(1/4 + \gamma^2)$). Connecting $D$ to Weil's full criterion would require choosing specific test functions; we have not done so here.
- It is not a sufficient probe by itself: it is concentrated at low heights ($1/\gamma^2$ falloff), so off-line zeros at very high $\gamma$ would barely register. A complementary probe with different weight (e.g., $1/\gamma$) would catch high-height off-line zeros better but converges more slowly.

## Connections

- **Cramér L²**: the on-line baseline $C$ is exactly Cramér's constant, computed from on-line zeros only.
- **Weil's explicit formula**: the discrete defect $D$ can be re-expressed as a sum over zeros of a specific test-function evaluation; this is the natural link to Weil's quadratic form.
- **Refined Balance Principle**: equivalent to $D = 0$ on the Selberg class. The framework's claim, restated in measurement terms.

## What needs to be computed next

1. **Real D-H zeros** (P0.3 in handoff). Without these the numerical $D(\text{D-H})$ is conditional on a recollection.
2. **Reference D for Dirichlet L-functions**: should be exactly 0 to within numerical precision. This is a baseline check on the test infrastructure.
3. **Deformation curves with real continuous deformations** (not just synthetic interpolation). Construct a one-parameter family of zeta-like functions that interpolate between Euler-product and non-Euler-product; track $D$ along the family.
4. **Cross-check against Weil's explicit formula** in classical form: derive $D$ as the value of a known test-function evaluation, confirming our definition aligns with established theory.

These are tractable for ClaudeCode with mpmath / Sage.

## Honesty boundary

The whole experiment depends on knowing the zeros. Until ClaudeCode produces verified D-H zero coordinates:
- All numerical $D(\text{D-H})$ values are illustrative
- The structural claim ("$D$ measures off-line zero content") is exact and unconditional
- The deformation curves are synthetic and labeled as such

This note ships with the script. Nobody reading it should mistake illustration for measurement.
