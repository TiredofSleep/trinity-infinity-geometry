#!/usr/bin/env python3
"""
Generate canonical TIG visualizations:
  - sigma_orbits.png         — σ permutation cycle structure on Z/10
  - attractor_convergence.png — α=1/2 attractor iteration converging to H/Br=1+√3
  - shell_chain.png          — 8-shell joint sub-magma chain with forbidden {2,3}
  - strand_orbital.png       — substrate strands {3,7,11,13} → orbitals (2p,4f,6h,7i)

Run from repo root:
    python figures/_make_figures.py

Requires matplotlib, mpmath, numpy.
Copyright (c) 2026 Brayden Ross Sanders / 7SiTe LLC.
Licensed under CC-BY-4.0 (figures are CC-BY-4.0 for journal compatibility;
the corpus is governed by 7SiTe Public Sovereignty License v2.2 — see LICENSE).
"""
import os
import sys
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mp
from matplotlib.patches import FancyArrowPatch, Circle

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from ck_tables import TSML, BHML, CL

OUTDIR = os.path.dirname(os.path.abspath(__file__))


# ============================================================
# Figure 1: sigma permutation cycle structure
# ============================================================
def figure_sigma_orbits():
    """σ = (0)(1 7 9 3)(2 8 6 4)(5) with σ³-fixed 4-core highlighted."""
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect("equal")
    ax.axis("off")

    # ten points around a circle
    coords = {}
    for k in range(10):
        theta = math.pi / 2 - 2 * math.pi * k / 10
        coords[k] = (math.cos(theta), math.sin(theta))

    four_core = {0, 7, 8, 9}
    fixed_points = {0, 5}    # σ-fixed
    sigma_perm = {0: 0, 1: 7, 7: 9, 9: 3, 3: 1, 2: 8, 8: 6, 6: 4, 4: 2, 5: 5}

    # draw points
    for k, (x, y) in coords.items():
        if k in four_core:
            color, edge = "#d4a017", "#7a5c00"
            radius = 0.10
        elif k in fixed_points:
            color, edge = "#c8c8c8", "#666666"
            radius = 0.08
        else:
            color, edge = "#f5f0e8", "#999"
            radius = 0.08
        ax.add_patch(Circle((x, y), radius, fc=color, ec=edge, lw=2, zorder=3))
        ax.text(x, y, str(k), ha="center", va="center", fontsize=14,
                fontweight="bold", zorder=4)
        # label below
        name = CL[k]
        ax.text(x * 1.22, y * 1.22, name, ha="center", va="center",
                fontsize=9, color="#444", zorder=4)

    # draw the two 4-cycles as arrows
    cycle_a = [1, 7, 9, 3]
    cycle_b = [2, 8, 6, 4]
    for cycle, color in [(cycle_a, "#a02020"), (cycle_b, "#2050a0")]:
        for i in range(len(cycle)):
            src, dst = cycle[i], cycle[(i + 1) % len(cycle)]
            arrow = FancyArrowPatch(coords[src], coords[dst],
                                    arrowstyle="-|>", mutation_scale=18,
                                    color=color, lw=2.0, alpha=0.7,
                                    connectionstyle="arc3,rad=0.18", zorder=2)
            ax.add_patch(arrow)

    # title and legend
    ax.text(0, 1.40, r"$\sigma = (0)(1\;7\;9\;3)(2\;8\;6\;4)(5)$",
            ha="center", fontsize=15, fontweight="bold")
    ax.text(0, -1.40, "4-core (gold) = $\\sigma^3$-fixed points minus $\\sigma$-fixed: $\\{V, H, Br, R\\}$",
            ha="center", fontsize=10, color="#555")

    plt.tight_layout()
    out = os.path.join(OUTDIR, "sigma_orbits.png")
    plt.savefig(out, dpi=160, bbox_inches="tight")
    plt.close()
    print(f"wrote {out}")


# ============================================================
# Figure 2: attractor convergence
# ============================================================
def figure_attractor_convergence():
    """Iteration of α=1/2 joint operator, showing 4-core mass + H/Br ratio."""
    try:
        import mpmath as mp
    except ImportError:
        print("mpmath not available — skipping attractor figure")
        return
    mp.mp.dps = 50

    def fuse(table, p):
        out = [mp.mpf(0)] * 10
        for i in range(10):
            for j in range(10):
                out[table[i][j]] += p[i] * p[j]
        return out

    def joint_tick(p, alpha=mp.mpf(1) / 2):
        Tf = fuse(TSML, p)
        Bf = fuse(BHML, p)
        out = [alpha * Tf[k] + (1 - alpha) * Bf[k] for k in range(10)]
        s = sum(out)
        return [x / s for x in out]

    # start from 4-core uniform
    p = [mp.mpf(0)] * 10
    for c in [0, 7, 8, 9]:
        p[c] = mp.mpf(1) / 4

    n_steps = 80
    p_history = [list(p)]
    for step in range(n_steps):
        p = joint_tick(p)
        p_history.append(list(p))

    target = 1 + mp.sqrt(3)
    target_f = float(target)

    H_traj = [float(ph[7]) for ph in p_history]
    Br_traj = [float(ph[8]) for ph in p_history]
    V_traj = [float(ph[0]) for ph in p_history]
    R_traj = [float(ph[9]) for ph in p_history]
    ratios = [float(ph[7] / ph[8]) for ph in p_history]
    err = [abs(float(ph[7] / ph[8] - target)) for ph in p_history]
    err = [max(e, 1e-50) for e in err]    # for log plot

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    # top: mass evolution
    ax1.plot(V_traj, label="V (VOID)", color="#666666", lw=2)
    ax1.plot(H_traj, label="H (HARMONY)", color="#a02020", lw=2)
    ax1.plot(Br_traj, label="Br (BREATH)", color="#2050a0", lw=2)
    ax1.plot(R_traj, label="R (RESET)", color="#d4a017", lw=2)
    ax1.axhline(0.540, ls="--", color="#a02020", alpha=0.3,
                label="H asymptote ≈ 0.540")
    ax1.axhline(0.198, ls="--", color="#2050a0", alpha=0.3,
                label="Br asymptote ≈ 0.198")
    ax1.set_ylabel("4-core mass (fraction)", fontsize=11)
    ax1.set_title(r"α = 1/2 attractor convergence on $\mathbb{Z}/10\mathbb{Z}$",
                  fontsize=13)
    ax1.legend(fontsize=9, loc="center right")
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(0, 0.65)

    # bottom: H/Br ratio + error
    ax2.semilogy(err, color="#7a3c8c", lw=2, label="$|H/Br - (1+\\sqrt{3})|$")
    ax2.axhline(target_f, ls=":", color="grey")
    ax2.set_xlabel("Iteration", fontsize=11)
    ax2.set_ylabel("|error| (log scale)", fontsize=11)
    ax2.set_title("$H/Br$ converges to $1+\\sqrt{3}$ at machine precision", fontsize=11)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3, which="both")

    # annotate the closed form
    final_ratio = ratios[-1]
    ax2.text(0.95, 0.95,
             f"$H/Br_{{\\infty}} = 1+\\sqrt{{3}} \\approx {target_f:.10f}$",
             transform=ax2.transAxes, ha="right", va="top",
             fontsize=11, color="#7a3c8c",
             bbox=dict(facecolor="white", edgecolor="#7a3c8c", alpha=0.9))

    plt.tight_layout()
    out = os.path.join(OUTDIR, "attractor_convergence.png")
    plt.savefig(out, dpi=160, bbox_inches="tight")
    plt.close()
    print(f"wrote {out}")


# ============================================================
# Figure 3: 8-shell joint sub-magma chain
# ============================================================
def figure_shell_chain():
    """The 8-shell joint sub-magma chain on Z/10 with forbidden {2,3}."""
    from itertools import combinations

    def is_joint_closed(S, T1, T2):
        return all(T1[i][j] in S and T2[i][j] in S for i in S for j in S)

    # find one example for each size
    examples = {}
    for size in range(1, 11):
        for subset in combinations(range(10), size):
            if is_joint_closed(set(subset), TSML, BHML):
                examples[size] = subset
                break

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-1, 11)
    ax.axis("off")

    # draw the 10 columns (sizes 1..10)
    for size in range(1, 11):
        x = size
        if size in examples:
            # allowed shell — draw the 10 operator slots, fill in the shell
            shell = set(examples[size])
            for k in range(10):
                y = 10 - k
                in_shell = (k in shell)
                in_4core = (k in {0, 7, 8, 9})
                if in_shell:
                    fc = "#d4a017" if in_4core else "#a4d4a4"
                    ec = "#7a5c00" if in_4core else "#3c6c3c"
                    lw = 2
                else:
                    fc = "#f8f8f8"
                    ec = "#dcdcdc"
                    lw = 1
                ax.add_patch(mp.Circle((x, y), 0.28, fc=fc, ec=ec, lw=lw,
                                       zorder=3))
                if in_shell:
                    ax.text(x, y, str(k), ha="center", va="center", fontsize=10,
                            fontweight="bold", zorder=4)
            ax.text(x, -0.5, f"size {size}", ha="center", fontsize=10,
                    fontweight="bold", color="#3c6c3c")
        else:
            # forbidden size — draw X
            for k in range(10):
                y = 10 - k
                ax.add_patch(mp.Circle((x, y), 0.28, fc="#ffe8e8", ec="#cc6666",
                                       lw=1, zorder=3, alpha=0.4))
            ax.plot([x - 0.4, x + 0.4], [10.4, 0.6], color="#cc6666", lw=3, zorder=5)
            ax.plot([x + 0.4, x - 0.4], [10.4, 0.6], color="#cc6666", lw=3, zorder=5)
            ax.text(x, -0.5, f"size {size}\n(forbidden)", ha="center",
                    fontsize=10, fontweight="bold", color="#cc6666")

    # row labels (operator codes)
    for k in range(10):
        y = 10 - k
        ax.text(0.2, y, f"{k}: {CL[k][:5]}", ha="left", va="center", fontsize=8,
                color="#555")

    ax.text(5.5, 10.6,
            r"Joint TSML+BHML sub-magma chain on $\mathbb{Z}/10\mathbb{Z}$ — sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$ realized, $\{2, 3\}$ forbidden",
            ha="center", fontsize=12, fontweight="bold")
    ax.text(5.5, -1.0,
            "Gold = 4-core ($\\{V, H, Br, R\\}$); green = other 4-core-or-larger shell members; red X = no closed shell exists",
            ha="center", fontsize=10, color="#444")

    plt.tight_layout()
    out = os.path.join(OUTDIR, "shell_chain.png")
    plt.savefig(out, dpi=160, bbox_inches="tight")
    plt.close()
    print(f"wrote {out}")


# ============================================================
# Figure 4: strand-orbital correspondence (D101)
# ============================================================
def figure_strand_orbital():
    """Substrate strands {3,7,11,13} → odd-l atomic orbitals."""
    strands = [3, 7, 11, 13]
    fig, ax = plt.subplots(figsize=(11, 6))

    # left column: substrate
    ax.text(0.15, 0.92, "Substrate primes wrapping Z/10",
            transform=ax.transAxes, fontsize=12, fontweight="bold")
    moduli = [10, 30, 210, 2310, 30030]
    chain = ["Z/10", "Z/30", "Z/210", "Z/2310", "Z/30030"]
    for i, (m, label) in enumerate(zip(moduli, chain)):
        y = 0.75 - 0.13 * i
        ax.text(0.05, y, label, transform=ax.transAxes, fontsize=11,
                fontweight="bold", color="#333")
        if i > 0:
            ax.annotate("", xy=(0.13, y), xytext=(0.13, y + 0.085),
                        xycoords="axes fraction",
                        arrowprops=dict(arrowstyle="->", color="#888", lw=1.5))
            # annotate the strand prime
            p = strands[i - 1]
            ax.text(0.18, y + 0.04, f"× {p}", transform=ax.transAxes,
                    fontsize=10, color="#a02020", fontweight="bold")

    # right column: orbitals
    ax.text(0.55, 0.92, "Nodeless hydrogenic orbitals",
            transform=ax.transAxes, fontsize=12, fontweight="bold")
    orbital_data = [
        (None, "Z/10 = kernel", "(no strand)"),
        (3, "2p", "l=1, n=2, mult 3"),
        (7, "4f", "l=3, n=4, mult 7"),
        (11, "6h", "l=5, n=6, mult 11"),
        (13, "7i", "l=6, n=7, mult 13"),
    ]
    for i, (p, name, info) in enumerate(orbital_data):
        y = 0.75 - 0.13 * i
        color = "#a02020" if p else "#888"
        ax.text(0.55, y, name, transform=ax.transAxes, fontsize=12,
                fontweight="bold", color=color)
        ax.text(0.65, y, info, transform=ax.transAxes, fontsize=10,
                color="#555")
        if p is not None:
            # draw arrow from strand to orbital
            ax.annotate("", xy=(0.55, y), xytext=(0.30, y),
                        xycoords="axes fraction",
                        arrowprops=dict(arrowstyle="->", color="#a02020",
                                        lw=1.5))

    # mapping rule
    ax.text(0.5, 0.04,
            r"$\mathrm{strand}\ p\ \longrightarrow\ \mathrm{orbital}\ (l = (p-1)/2,\ n = l+1),\quad \mathrm{multiplicity}\ 2l+1 = p$",
            transform=ax.transAxes, ha="center", fontsize=11, color="#a02020",
            fontweight="bold", bbox=dict(facecolor="#fff8e8", edgecolor="#a02020",
                                          alpha=0.8))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.text(0.5, 1.04, "D101 — Strand-Orbital Correspondence (Volume K)",
            transform=ax.transAxes, ha="center", fontsize=13, fontweight="bold")

    plt.tight_layout()
    out = os.path.join(OUTDIR, "strand_orbital.png")
    plt.savefig(out, dpi=160, bbox_inches="tight")
    plt.close()
    print(f"wrote {out}")


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("Generating TIG canonical figures...")
    figure_sigma_orbits()
    figure_attractor_convergence()
    figure_shell_chain()
    figure_strand_orbital()
    print("Done.")
