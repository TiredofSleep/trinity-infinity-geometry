# The staircase-and-envelope lens

**Purpose**: A single image that holds together the framework's two main metaphors.

Reproducible from `experiments/staircase_envelope.py`. Output at `plots/staircase_envelope.png`.

---

## The two metaphors, fused

### "Primes form an interleaved staircase against waves, and the interleaving cancels to a straight line."

The Chebyshev function

$$\psi(x) = \sum_{p^k \le x} \log p$$

jumps by $\log p$ at every prime power $p^k$. It is a staircase. The explicit formula says

$$\psi(x) = x - \sum_\rho \frac{x^\rho}{\rho} + \text{lower order}$$

so the staircase decomposes into a smooth line ($y = x$) and a sum of waves, one wave per non-trivial zero $\rho$ of $\zeta$. Each wave $x^\rho / \rho$ has amplitude $x^{\mathrm{Re}(\rho)} / |\rho|$ and oscillates at frequency $\mathrm{Im}(\rho)$ in the variable $\log x$.

If we *subtract* the waves, the staircase becomes the line. Equivalently: the waves are exactly what's needed to interpolate between the discrete prime steps and produce the smooth $x$ growth. The cancellation isn't approximate — it's exact in the limit, and tightly bounded at any finite $x$.

### "Every line lives inside two parabolic arcs."

The line $y = x$ has parabolic envelopes $y = x \pm k \sqrt{x}$. Under RH, $\psi(x)$ lives inside this envelope (with an additional $(\log x)^2$ factor in the precise effective version, but the parabolic core of the envelope is the $\sqrt{x}$). The envelope width grows as $\sqrt{x}$, not as $x$, so in *relative* terms the staircase converges to the line: $\psi(x)/x \to 1$.

### Fusing them

The first metaphor says the staircase equals the line (modulo waves). The second says the line is surrounded by a parabolic envelope. Together: the staircase oscillates inside the envelope, and the waves *precisely* trace its specific path within. Each zero's wave contributes amplitude $x^{\mathrm{Re}(\rho)} / |\rho|$ to the residual. If all zeros have $\mathrm{Re}(\rho) = 1/2$ (RH), all waves have amplitude $\sqrt{x} / |\rho|$, and the envelope's $\sqrt{x}$ width is *just barely enough* to contain them.

If even one zero had $\mathrm{Re}(\rho) = \sigma > 1/2$, its wave would have amplitude $x^\sigma$, which grows faster than $\sqrt{x}$. The envelope would no longer contain the residual at large $x$. RH is equivalent to "the parabolic envelope is the right shape."

This is what the visualization shows.

---

## What the image actually shows

Three panels in `plots/staircase_envelope.png`:

**(A)** The staircase $\psi(x)$ for $x \in [0, 100]$, with the line $y = x$ overlaid. At this scale the discrete jumps are visible. The staircase tracks the line approximately, with small over/undershoots at each prime.

**(B)** The same staircase at larger scale, $x \in [1, 2000]$, with the parabolic envelopes $y = x \pm 3\sqrt{x}$ drawn. The discrete jumps are now invisible at this resolution; the staircase looks smooth. It stays well inside the envelope.

**(C)** The residual $\psi(x) - x$ alone, with the centered envelope $y = \pm 3\sqrt{x}$. This is the cleanest view: the residual oscillates, but its amplitude stays bounded by $\sqrt{x}$ growth. This is what RH conjectures, and what we see empirically.

---

## What this is

A visualization aid. Useful for:
- Talks and presentations where the lens needs to be transmitted quickly
- Pedagogical introduction to the framework's central image
- Showing what the empirical $|\psi(x) - x| \sim \sqrt{x}$ work in this repo is actually testing

## What this isn't

- A proof of anything. The staircase staying in the envelope is the conjecture (RH, effective version), verified empirically to very large $x$. The figure shows this for small $x$; ClaudeCode could extend to $x = 10^9$ or $10^{12}$.
- A localization of zeros. The waves' specific positions and amplitudes are *not* extracted from the figure; the figure shows only the resultant staircase. To see individual waves, one would need to subtract them off one at a time (as `experiments/euler_defect_coefficient.py` notes, this requires zero data).

The fused image is real and worth carrying around in your head. The math behind it is the explicit formula and the Riemann–von Mangoldt asymptotic. The framework's contribution is the metaphor's compactness: every linear summary lives in a parabolic envelope, and L-function theory is one particularly precise instance of this.
