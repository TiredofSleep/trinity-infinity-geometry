"""
Generate the Davenport-Heilbronn balance defect schematic.

IMPORTANT: This is a CONCEPTUAL DIAGRAM, not a computation of D-H zeros.

Computing D-H zeros in the critical strip requires:
    - Numerical evaluation of a Dirichlet series that doesn't converge in the strip
    - Approximate functional equation methods (Riemann-Siegel-style)
    - Multi-precision arithmetic for stability
None of which is in scope for this harness.

What this plot DOES show:
    - The structural distinction between an L-function with Euler product (left)
      and one without (right).
    - The conjectured 4-orbit position of an off-line zero of D-H.
    - The qualitative point that "off-line zeros exist for D-H" — a known
      fact from the literature (Davenport-Heilbronn 1936, Spira 1994).

What this plot does NOT show:
    - Numerically computed D-H zero coordinates (those would require SageMath
      or similar; the coordinates we showed earlier were cited from memory).
    - Quantitative balance defect measurements.

The schematic is labeled clearly so no one mistakes it for raw data.
"""

import os
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # non-interactive backend, for headless runs
import matplotlib.pyplot as plt


def make_balance_defect_schematic(output_path: Path) -> Path:
    """
    Draw the conceptual side-by-side schematic.

    Returns the path to the saved figure.
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    # --- Left panel: ζ(s) (Euler product, RH conjecturally holds) ---
    ax = axes[0]
    ax.axvspan(0, 1, alpha=0.08, color="gray")
    ax.axvline(0.5, color="black", linewidth=2.5, label="Critical line Re(s)=1/2")

    # First few ζ zeros (well-known imaginary parts)
    zeta_t = [14.13, 21.02, 25.01, 30.42, 32.94, 37.59, 40.92, 43.33]
    for t in zeta_t:
        ax.scatter([0.5], [t], color="red", s=60, zorder=5)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 50)
    ax.set_xlabel("Re(s)")
    ax.set_ylabel("Im(s)")
    ax.set_title("ζ(s) — Riemann zeta\nHAS Euler product\nAll known zeros on critical line",
                 fontsize=11)
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(alpha=0.3)
    ax.text(0.05, 45,
            "Empirical:\nAll computed zeros\non Re(s) = 1/2\n(to 10^13+)",
            fontsize=10, color="red", fontweight="bold",
            bbox=dict(boxstyle="round", facecolor="white", edgecolor="red", alpha=0.8))

    # --- Right panel: Davenport-Heilbronn (no Euler product) ---
    ax = axes[1]
    ax.axvspan(0, 1, alpha=0.08, color="gray")
    ax.axvline(0.5, color="black", linewidth=2.5, label="Critical line Re(s)=1/2")

    # Schematic: a typical off-line zero (4-orbit under conjugation + functional equation)
    # NOTE: coordinates here are illustrative, not computed.
    sigma_off = 0.78
    t_off = 35

    # 4-orbit of an off-line zero
    ax.scatter([sigma_off, sigma_off, 1 - sigma_off, 1 - sigma_off],
               [t_off, -t_off, t_off, -t_off],
               color="orange", s=200, marker="X", zorder=6,
               edgecolor="red", linewidth=2,
               label="Off-line zero (schematic, 4-orbit)")

    # Some on-line zeros for D-H (qualitatively)
    dh_online = [10, 18, 27, 42]
    for t in dh_online:
        ax.scatter([0.5], [t], color="purple", s=60, zorder=5)
    ax.scatter([], [], color="purple", s=60, label="On-line zeros (schematic)")

    # Annotation: balance defect
    ax.annotate("", xy=(0.5, t_off + 3), xytext=(sigma_off, t_off),
                arrowprops=dict(arrowstyle="->", color="red", linewidth=1.5))
    ax.text(0.62, t_off + 5, "balance defect\n(no exact on-line\ncompanion at same t)",
            fontsize=9, color="red",
            bbox=dict(boxstyle="round", facecolor="white", edgecolor="red", alpha=0.8))

    ax.set_xlim(0, 1)
    ax.set_ylim(-50, 50)
    ax.set_xlabel("Re(s)")
    ax.set_ylabel("Im(s)")
    ax.set_title("Davenport-Heilbronn function\nNO Euler product\nHas off-line zeros (known since 1936)",
                 fontsize=11)
    ax.legend(loc="lower right", fontsize=9)
    ax.grid(alpha=0.3)
    ax.text(0.05, -45,
            "Schematic only.\nActual zero coords\nrequire SageMath/PARI.",
            fontsize=10, color="darkorange", fontweight="bold",
            bbox=dict(boxstyle="round", facecolor="white", edgecolor="orange", alpha=0.8))

    fig.suptitle(
        "Conceptual schematic: Euler product structure correlates with on-line zero distribution\n"
        "(diagram is illustrative — quantitative zero data not computed here)",
        fontsize=12, fontweight="bold")
    plt.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=120, bbox_inches="tight")
    plt.close(fig)
    return output_path


if __name__ == "__main__":
    out = Path(__file__).parent.parent / "plots" / "dh_balance_defect_schematic.png"
    saved = make_balance_defect_schematic(out)
    print(f"Saved schematic to: {saved}")
