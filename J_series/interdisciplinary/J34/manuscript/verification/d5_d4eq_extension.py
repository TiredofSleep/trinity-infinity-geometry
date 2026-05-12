"""
d5_d4eq_extension.py - Implements WP114 §6 recommendations:

  Recommendation 2: D4 reformulated with D_4-equivariant Higgs embedding
                    (average alignment over the D_4 orbit of the canonical
                    9-vector Higgs direction).
  Recommendation 3: D5 = prime-7 discriminant indicator (HARMONY-side
                    structural signature; complement to D3's wobble-side
                    prime-11 signature).

Re-runs the WP114 9-family structured matrix battery + TSML/BHML controls
with the augmented detector set {D1, D2, D3, D4, D4_eq, D5} and reports
which detectors discriminate TSML from generic structured matrices.
"""
from __future__ import annotations

import numpy as np
import sympy as sp

# Reuse existing detectors and family generators
import sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from structured_matrix_sweep import (
    DETECTORS, FAMILIES, P56_matrix, sample_family, evaluate, compute_stats,
    cohens_d, TSML, BHML, _P56,
)


# ----- D4 reformulated: D_4-equivariant Higgs alignment -----

# sigma^3 permutation: (0)(3)(8)(9)(1 5)(7 4)(6 2)
def sigma3_matrix():
    P = np.eye(10)
    swaps = [(1, 5), (7, 4), (6, 2)]
    for i, j in swaps:
        P[i, i] = 0; P[j, j] = 0; P[i, j] = 1; P[j, i] = 1
    return P


_S3 = sigma3_matrix()


def d4_orbit_of(v):
    """Orbit of a 10-vector under D_4 = <P_56, sigma^3>.
    Each element is a 10-vector; orbit has up to 8 elements."""
    e = v.copy()
    p56 = _P56 @ e
    s3 = _S3 @ e
    # Build the 8-element D_4 orbit by left-multiplication by all 8 group elements
    elements = [e]
    elements.append(_P56 @ e)
    elements.append(_S3 @ e)
    elements.append(_P56 @ _S3 @ e)
    elements.append(_S3 @ _P56 @ e)
    elements.append(_P56 @ _S3 @ _P56 @ e)
    elements.append(_S3 @ _P56 @ _S3 @ e)
    elements.append(_P56 @ _S3 @ _P56 @ _S3 @ e)
    # Deduplicate
    seen = []
    for el in elements:
        is_dup = any(np.allclose(el, s, atol=1e-12) for s in seen)
        if not is_dup:
            seen.append(el)
    return seen


# Canonical 9-vector Higgs direction (WP104 §2.3)
HIGGS9 = np.array([-1/np.sqrt(2), -1/np.sqrt(2), -1/np.sqrt(2),
                    -1/np.sqrt(2), -1/np.sqrt(2), 0.0, 0.0,
                    -1/np.sqrt(2), 0.0])
# Embed as a 10-vector by zero-padding (the 9-vec is over operators 0..8)
HIGGS10 = np.concatenate([HIGGS9, [0.0]])


def D4_higgs_eq(M):
    """D_4-equivariant Higgs alignment: max cos(angle) over the D_4 orbit
    of the Higgs direction.

    For a 10x10 real M, take the 10-dim sum of its rows (or column projection)
    and compute the maximum cosine alignment with any element in the
    D_4-orbit of HIGGS10.
    """
    # Use M's column-sum as a 10-vector "direction"
    direction = M.sum(axis=0)
    if np.linalg.norm(direction) == 0:
        return 0.0
    direction = direction / np.linalg.norm(direction)
    orbit = d4_orbit_of(HIGGS10)
    cos_values = []
    for v in orbit:
        if np.linalg.norm(v) > 0:
            v_norm = v / np.linalg.norm(v)
            cos_values.append(abs(float(np.dot(direction, v_norm))))
    return max(cos_values) if cos_values else 0.0


# ----- D5: prime-7 discriminant indicator -----

def D5_prime7_disc(M, scale=1.0, threshold=5):
    """Returns 1 if 7^threshold divides the discriminant of the SQUAREFREE
    PART of the integer characteristic polynomial of M, else 0.

    WP107 found TSML's discriminant of the 8th-degree squarefree part
    (after factoring out lam^2 from the full 10×10 char poly) has 2^16 · 7^7
    · 659 · ... — so threshold=5 or higher should distinguish TSML.

    For TSML/BHML use scale=1 (already integer); for random Gaussian etc.
    use scale=10 to get integer matrix at comparable scale.
    """
    try:
        # Integer matrix
        if scale == 1.0:
            M_int = np.round(M).astype(int)
        else:
            M_int = np.round(M * scale).astype(int)
        sp_M = sp.Matrix(M_int.tolist())
        lam = sp.symbols("lam")
        chi = sp_M.charpoly(lam).as_expr()
        poly = sp.Poly(chi, lam)
        # Factor out lam^k
        coeffs = poly.all_coeffs()  # descending
        # Find trailing zeros
        k = 0
        while k < len(coeffs) and coeffs[-1 - k] == 0:
            k += 1
        # Divide by lam^k
        if k > 0:
            sf_coeffs = coeffs[:len(coeffs) - k]
        else:
            sf_coeffs = coeffs
        if len(sf_coeffs) < 2:
            return 0
        sf_poly = sp.Poly(sf_coeffs, lam)
        try:
            disc = sp.discriminant(sf_poly.as_expr(), lam)
        except Exception:
            return 0
        if disc == 0:
            return 0
        disc_int = int(disc)
        if disc_int < 0:
            disc_int = -disc_int
        for _ in range(threshold):
            if disc_int % 7 != 0:
                return 0
            disc_int //= 7
        return 1
    except Exception:
        return 0


def D5_prime7_disc_lower_threshold(M):
    """Variant with threshold=3 (less strict)."""
    return D5_prime7_disc(M, scale=10.0, threshold=3)


EXTENDED_DETECTORS = dict(DETECTORS)
EXTENDED_DETECTORS["D4_eq_higgs"] = D4_higgs_eq
# For TSML/BHML controls (already-integer matrices), use scale=1
# For random samples, use scale=10
EXTENDED_DETECTORS["D5_prime7_7_int"] = lambda M: D5_prime7_disc(M, scale=1.0, threshold=7)
EXTENDED_DETECTORS["D5_prime7_5_int"] = lambda M: D5_prime7_disc(M, scale=1.0, threshold=5)
EXTENDED_DETECTORS["D5_prime7_3_scl"] = D5_prime7_disc_lower_threshold


def evaluate_ext(M):
    return {name: f(M) for name, f in EXTENDED_DETECTORS.items()}


def compute_stats_ext(samples):
    if not samples:
        return {}
    detector_values = {name: [] for name in EXTENDED_DETECTORS}
    for M in samples:
        ev = evaluate_ext(M)
        for name in EXTENDED_DETECTORS:
            detector_values[name].append(ev[name])
    stats = {}
    for name, vals in detector_values.items():
        a = np.array(vals, dtype=float)
        stats[name] = {
            "mean": float(np.mean(a)),
            "std":  float(np.std(a, ddof=1)) if len(a) > 1 else 0.0,
            "min":  float(np.min(a)),
            "max":  float(np.max(a)),
            "n":    len(a),
        }
    return stats


def main():
    print("=" * 100)
    print("WP114 §6 EXTENSION: D5 (prime-7 disc) + D4_eq (D_4-equivariant Higgs)")
    print("=" * 100)
    print()

    # First: TSML / BHML evaluation
    print("Positive controls under extended detector set:")
    print("-" * 80)
    tsml_eval = evaluate_ext(TSML)
    bhml_eval = evaluate_ext(BHML)
    for name in EXTENDED_DETECTORS:
        print(f"  {name:<16} TSML = {tsml_eval[name]:+10.6f}    BHML = {bhml_eval[name]:+10.6f}")
    print()

    # Family sweep
    print("Family sweep (200 samples each, EXTENDED detector set):")
    print("-" * 110)
    print(f"{'family':<16}", end="")
    for name in EXTENDED_DETECTORS:
        print(f"{name:<14}", end="")
    print()
    print("-" * 110)

    family_stats = {}
    gauss_stats = None
    for fname in FAMILIES:
        samples = sample_family(fname, n_samples=200)
        stats = compute_stats_ext(samples)
        family_stats[fname] = stats
        if fname == "gaussian":
            gauss_stats = stats
        print(f"  {fname:<14}", end="")
        for name in EXTENDED_DETECTORS:
            mean = stats[name]["mean"]
            print(f"{mean:+10.6f}    ", end="")
        print()
    print()

    # Cohen's d vs Gaussian baseline
    print("Cohen's d vs Gaussian baseline:")
    print("-" * 110)
    print(f"{'family':<16}", end="")
    for name in EXTENDED_DETECTORS:
        print(f"{name:<14}", end="")
    print()
    print("-" * 110)

    big_effects = []
    for fname in FAMILIES:
        if fname == "gaussian":
            continue
        d = cohens_d(family_stats[fname], gauss_stats)
        print(f"  {fname:<14}", end="")
        for name in EXTENDED_DETECTORS:
            v = d[name]
            tag = "**" if abs(v) >= 0.8 else ("*" if abs(v) >= 0.5 else (
                "." if abs(v) >= 0.2 else ""))
            print(f"{v:+8.3f}{tag:<6}", end="")
            if abs(v) >= 0.5:
                big_effects.append((fname, name, v))
        print()
    print()
    print("Tag legend: ** large (|d|>=0.8), * medium (>=0.5), . small (>=0.2), blank no effect (<0.2)")
    print()

    # TSML / BHML vs Gaussian (single-sample d)
    print("TSML / BHML vs Gaussian baseline (single-sample Cohen's d):")
    print("-" * 110)
    for matrix_name, ev in [("TSML", tsml_eval), ("BHML", bhml_eval)]:
        print(f"  {matrix_name:<14}", end="")
        for name in EXTENDED_DETECTORS:
            mb = gauss_stats[name]["mean"]
            sb = gauss_stats[name]["std"]
            v = (ev[name] - mb) / sb if sb > 0 else float("inf")
            tag = "**" if abs(v) >= 0.8 else ("*" if abs(v) >= 0.5 else (
                "." if abs(v) >= 0.2 else ""))
            v_str = f"{v:+8.3f}" if abs(v) < 1e6 else "+inf "
            print(f"{v_str}{tag:<6}", end="")
        print()
    print()

    # Verdict
    print("=" * 100)
    print("VERDICT")
    print("=" * 100)
    print()

    # D3, D5 specifically
    print("Detector summary (TSML at integer scale; Gaussian at scale=10 baseline):")
    print(f"  TSML D3_prime11 = {tsml_eval['D3_prime11']:.0f}; baseline freq = {gauss_stats['D3_prime11']['mean']:.4f}")
    print(f"  TSML D5_prime7_7_int = {tsml_eval['D5_prime7_7_int']:.0f} (THRESHOLD 7^7 in disc of squarefree part)")
    print(f"  TSML D5_prime7_5_int = {tsml_eval['D5_prime7_5_int']:.0f} (THRESHOLD 7^5 in disc of squarefree part)")
    print(f"  TSML D5_prime7_3_scl = {tsml_eval['D5_prime7_3_scl']:.0f} (scaled, threshold 7^3)")
    print(f"  TSML D4_eq_higgs = {tsml_eval['D4_eq_higgs']:.4f} (D_4-equivariant max-orbit alignment)")
    print(f"  TSML D4_higgs_cos (original) = {tsml_eval['D4_higgs_cos']:.4f}")
    print()

    # Identify which families fire D5_prime7_3_scl
    print("Families with D5 (prime-7^3 in scaled disc) > 0 across the 200 samples:")
    for fname in FAMILIES:
        d5 = family_stats[fname]["D5_prime7_3_scl"]["mean"]
        if d5 > 0.005:
            print(f"  {fname:<14} D5_prime7_3_scl mean = {d5:.4f} (frac of samples)")
    print()

    if big_effects:
        print(f"All medium-or-larger family effects across extended detectors:")
        for fname, name, v in big_effects:
            print(f"  {fname:<14} {name:<14} d = {v:+.3f}")


if __name__ == "__main__":
    main()
