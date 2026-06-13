"""
staircase_envelope.py — visualize the framework's central lens.

============================================================================
THE LENS
============================================================================

Two metaphors that the framework keeps pointing at, made concrete in one
figure:

1.  "Primes form an interleaved staircase against waves, and the
     interleaving cancels to a straight line."

    Mathematical content (the explicit formula):

        psi(x)  =  x  -  sum_{rho}  x^rho / rho  +  lower-order terms

    where psi(x) = sum_{p^k <= x} log(p) is the Chebyshev prime-power
    counting function (a staircase that jumps at every prime power), and
    the rho sum runs over non-trivial zeros of zeta.

    The line y = x is the smooth trend. The waves are x^rho/rho, one
    per zero, oscillating at frequency Im(rho). Their cancellation makes
    the staircase track the line, with fluctuations bounded by what the
    zeros allow.

2.  "Every line lives inside two parabolic arcs."

    Concretely, under RH:

        |psi(x) - x|  <=  c * sqrt(x) * (log x)^2

    So the staircase psi(x) is sandwiched between two parabolic envelopes

        y = x + k * sqrt(x)    and    y = x - k * sqrt(x)

    (for an appropriate k depending on the precision wanted and the
    range of x). The envelope's width grows as sqrt(x), not as x --
    that's the parabolic flattening of the relative gap.

----------------------------------------------------------------------------
WHAT THIS SCRIPT PRODUCES
----------------------------------------------------------------------------

Three panels:

  (A) The staircase itself, for small x where the discrete jumps are
      visible. Overlaid with the line y = x.

  (B) The same staircase at a larger x range, with the parabolic
      envelopes  y = x +/- k * sqrt(x)  shown.  The staircase is visibly
      "inside the tube."

  (C) The residual psi(x) - x.  This is what's left after subtracting
      the line.  It oscillates with amplitude bounded (under RH) by
      sqrt(x).  The k * sqrt(x) envelope is now centered on zero,
      and the residual visibly stays within it.

If RH fails (some zero has Re(rho) = sigma > 1/2), the parabolic envelope
in panel (C) would be too tight to contain the residual --- it would
escape as x^sigma instead of x^{1/2}.  Panel (C) is what makes RH
empirically falsifiable.

----------------------------------------------------------------------------
HONEST SCOPE
----------------------------------------------------------------------------

This script just plots real prime data against the right reference
curves.  It does not prove RH (the staircase staying within the
envelope is the conjecture, verified to enormous x).  It is a
visualization aid for the framework's lens.

The data is real:  primes from a sieve, psi(x) from a direct sum.
The envelopes are mathematical objects, not empirical fits.
"""

import math
from pathlib import Path
from typing import List, Tuple

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------------
# Prime sieve and psi(x)
# ----------------------------------------------------------------------------

def sieve(N: int) -> List[int]:
    """Return all primes <= N (simple Eratosthenes)."""
    if N < 2:
        return []
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.isqrt(N)) + 1):
        if is_prime[i]:
            for j in range(i * i, N + 1, i):
                is_prime[j] = False
    return [i for i, p in enumerate(is_prime) if p]


def psi_staircase(x_max: int) -> Tuple[List[float], List[float]]:
    """
    Return (x_values, psi_values) for plotting psi(x) as a staircase.

    psi(x) = sum_{p^k <= x} log(p).

    For plotting, we return the (x, y) pairs immediately before and
    after every jump, so matplotlib's default line-plot renders the
    staircase cleanly.
    """
    primes = sieve(x_max)
    # build a list of (jump_x, jump_value) -- the value of x at which a
    # jump occurs, and the log(p) added there.
    jumps: List[Tuple[int, float]] = []
    for p in primes:
        pk = p
        while pk <= x_max:
            jumps.append((pk, math.log(p)))
            pk *= p
    jumps.sort()

    xs = [0.0]
    ys = [0.0]
    running = 0.0
    for jx, jv in jumps:
        # horizontal up to the jump
        xs.append(jx)
        ys.append(running)
        # vertical jump
        running += jv
        xs.append(jx)
        ys.append(running)
    # finish off the plot
    xs.append(float(x_max))
    ys.append(running)
    return xs, ys


# ----------------------------------------------------------------------------
# Sampled psi(x) for the residual plot (don't need staircase detail at scale)
# ----------------------------------------------------------------------------

def psi_sampled(x_array: List[float], x_max_for_sieve: int) -> List[float]:
    """psi(x) evaluated at each x in x_array."""
    primes = sieve(x_max_for_sieve)
    out = [0.0] * len(x_array)
    for p in primes:
        log_p = math.log(p)
        pk = p
        while pk <= x_max_for_sieve:
            for i, x in enumerate(x_array):
                if x >= pk:
                    out[i] += log_p
            pk *= p
    return out


# ----------------------------------------------------------------------------
# Draw it
# ----------------------------------------------------------------------------

def make_figure(small_xmax: int, large_xmax: int, k_envelope: float,
                output_path: Path) -> Path:
    fig, axes = plt.subplots(1, 3, figsize=(20, 6))

    # ---- Panel A: the staircase, small x, with line y = x ----
    ax = axes[0]
    xs, ys = psi_staircase(small_xmax)
    ax.plot(xs, ys, color="#1f77b4", linewidth=1.0, label="psi(x)  (staircase)")
    ax.plot([0, small_xmax], [0, small_xmax], color="black", linewidth=1.5,
            linestyle="--", label="y = x  (the line)")
    ax.set_xlabel("x")
    ax.set_ylabel("psi(x)")
    ax.set_title(f"(A) Prime staircase vs the line, x in [0, {small_xmax}]\n"
                 f"every prime power contributes a step of log(p)",
                 fontsize=11)
    ax.legend(loc="upper left", fontsize=10)
    ax.grid(alpha=0.3)
    ax.set_xlim(0, small_xmax)
    ax.set_ylim(0, small_xmax * 1.1)

    # ---- Panel B: staircase inside the parabolic envelope, larger x ----
    ax = axes[1]
    # sample psi on a coarser grid so the plot is fast
    n_sample = 800
    xs_sample = [1.0 + (large_xmax - 1.0) * i / (n_sample - 1) for i in range(n_sample)]
    psi_sample = psi_sampled(xs_sample, large_xmax)
    ax.plot(xs_sample, psi_sample, color="#1f77b4", linewidth=1.2,
            label="psi(x)")
    ax.plot(xs_sample, xs_sample, color="black", linewidth=1.5, linestyle="--",
            label="y = x")
    upper = [x + k_envelope * math.sqrt(x) for x in xs_sample]
    lower = [x - k_envelope * math.sqrt(x) for x in xs_sample]
    ax.plot(xs_sample, upper, color="#d62728", linewidth=1.5,
            label=f"y = x +/- {k_envelope}*sqrt(x)  (parabolic envelope)")
    ax.plot(xs_sample, lower, color="#d62728", linewidth=1.5)
    ax.fill_between(xs_sample, lower, upper, color="#d62728", alpha=0.08)
    ax.set_xlabel("x")
    ax.set_ylabel("psi(x)")
    ax.set_title(f"(B) Same staircase, larger x in [1, {large_xmax}]\n"
                 f"with parabolic envelope y = x +/- {k_envelope}*sqrt(x)",
                 fontsize=11)
    ax.legend(loc="upper left", fontsize=10)
    ax.grid(alpha=0.3)
    ax.set_xlim(0, large_xmax)

    # ---- Panel C: residual psi(x) - x in its sqrt(x) tube ----
    ax = axes[2]
    residual = [p - x for p, x in zip(psi_sample, xs_sample)]
    ax.plot(xs_sample, residual, color="#1f77b4", linewidth=1.0,
            label="psi(x) - x  (residual)")
    ax.axhline(0, color="black", linewidth=1.0, linestyle="--", label="y = 0")
    env_upper = [k_envelope * math.sqrt(x) for x in xs_sample]
    env_lower = [-k_envelope * math.sqrt(x) for x in xs_sample]
    ax.plot(xs_sample, env_upper, color="#d62728", linewidth=1.5,
            label=f"y = +/- {k_envelope}*sqrt(x)")
    ax.plot(xs_sample, env_lower, color="#d62728", linewidth=1.5)
    ax.fill_between(xs_sample, env_lower, env_upper, color="#d62728", alpha=0.08)
    ax.set_xlabel("x")
    ax.set_ylabel("psi(x) - x")
    ax.set_title(f"(C) Residual: the staircase minus the line\n"
                 f"oscillates within the sqrt(x) tube",
                 fontsize=11)
    ax.legend(loc="upper left", fontsize=10)
    ax.grid(alpha=0.3)
    ax.set_xlim(0, large_xmax)

    fig.suptitle(
        "The framework's lens: prime staircase against the line, inside the "
        "parabolic envelope.\n"
        "Under RH the residual stays in a tube of width ~ sqrt(x) (and would "
        "escape it as x^sigma if any zero had Re=sigma > 1/2).",
        fontsize=13, fontweight="bold"
    )
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=120, bbox_inches="tight")
    plt.close(fig)
    return output_path


def main() -> None:
    out = Path(__file__).parent.parent / "plots" / "staircase_envelope.png"
    saved = make_figure(small_xmax=100, large_xmax=2000, k_envelope=3.0,
                        output_path=out)
    print(f"Saved figure to: {saved}")


if __name__ == "__main__":
    main()
