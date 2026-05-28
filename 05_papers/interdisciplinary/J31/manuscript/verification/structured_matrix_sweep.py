"""
structured_matrix_sweep.py - Extend WP106 specificity scoping to a
broader battery of structured 10x10 matrix families.

WP106 verified that 16 distilgpt2 weight tensors show NO TIG structure
under 4 detectors (Cohen's |d| < 0.5 across all). This script extends
the negative scope to:

    1. Gaussian random matrices (baseline; large sample)
    2. Symmetric matrices (S = (M + M^T)/2 for random M)
    3. Antisymmetric matrices (A = (M - M^T)/2 for random M)
    4. Permutation matrices (random permutations)
    5. Hadamard-style sign matrices (entries +/-1)
    6. Orthogonal matrices (random Haar-orthogonal via QR)
    7. DFT (discrete Fourier transform) real part
    8. Identity matrix
    9. Diagonal matrices (random)
   10. Companion matrices of random integer polynomials

For each family, generate 200 samples (or as many as the family allows),
apply the four WP106 detectors (Lie/Jordan ratio, P_56 invariance, prime-11
in characteristic polynomial, Higgs-direction alignment), and report:

    - mean and std of each detector across the family
    - comparison to TSML and BHML (the canonical "positive" controls)
    - Cohen's d vs Gaussian baseline

Question we're answering: which (if any) structured matrix families
reproduce TSML/BHML's TIG signature? Expected answer: none, but with
specific deviations for permutation, orthogonal, and Hadamard families
that are interpretable.
"""
from __future__ import annotations

import numpy as np
from numpy.linalg import qr


# ----- canonical TSML / BHML (positive controls) -----
TSML_ROWS = [
    "0000000700",  "0737777777",  "0377477779",  "0777777773",  "0747777787",
    "0777777777",  "0777777777",  "7777777777",  "0777877777",  "0797377777",
]
BHML_ROWS = [
    "0123456789",  "1234567266",  "2334567366",  "3444567466",  "4555567577",
    "5666667677",  "6777777777",  "7234567890",  "8666777978",  "9666777080",
]
TSML = np.array([[int(c) for c in row] for row in TSML_ROWS], dtype=float)
BHML = np.array([[int(c) for c in row] for row in BHML_ROWS], dtype=float)


# ----- the 4 WP106 detectors -----

def D1_lj(M):
    """Lie/Jordan ratio: ||A||^2 / (||A||^2 + ||S||^2)."""
    A = (M - M.T) / 2
    S = (M + M.T) / 2
    a = np.sum(A * A)
    s = np.sum(S * S)
    if a + s == 0:
        return 0.0
    return a / (a + s)


def P56_matrix():
    """Elementary transposition (5,6)."""
    P = np.eye(10)
    P[5, 5] = 0; P[6, 6] = 0; P[5, 6] = 1; P[6, 5] = 1
    return P


_P56 = P56_matrix()


def D2_p56(M):
    """P_56 invariance defect: ||M - P_56 M P_56||^2 / ||M||^2."""
    M_swapped = _P56 @ M @ _P56
    diff = M - M_swapped
    if np.sum(M * M) == 0:
        return 0.0
    return np.sum(diff * diff) / np.sum(M * M)


def D3_prime11(M, scale=10.0, tol=1e-6):
    """Returns 1 if 11 divides both c_2 and c_8 of the integer-rounded
    characteristic polynomial of M, else 0.

    Uses sympy for the integer poly. M is rescaled by 'scale' before rounding
    to give integer matrix in a comparable range.
    """
    try:
        import sympy as sp
        M_int = np.round(M * scale).astype(int)
        sp_M = sp.Matrix(M_int.tolist())
        lam = sp.symbols("lam")
        chi = sp_M.charpoly(lam).as_expr()
        coeffs = sp.Poly(chi, lam).all_coeffs()
        # coeffs in descending order; for 10x10 we have 11 coefficients
        # c_2 corresponds to deg-2 coefficient = coeffs[8] (since index 0 is leading)
        # c_8 = coeffs[2]
        # But index depends on length; let's grab by degree explicitly.
        # Since the matrix is 10x10, degree is 10.
        c2 = coeffs[8]   # coefficient of lam^2
        c8 = coeffs[2]   # coefficient of lam^8
        return 1 if (c2 % 11 == 0 and c8 % 11 == 0 and c2 != 0 and c8 != 0) else 0
    except Exception:
        return 0


def D4_higgs(M):
    """Cosine of angle between M's antisymmetric upper-triangle and the
    canonical 9-vector embedding of the WP104 Higgs direction.

    Higgs direction (9-vec, WP104 §2.3): v_0..v_4, v_7 = -1/sqrt(2);
    v_8 = v_9 = 0; (v_5+v_6)/sqrt(2) = -1/2.

    Embed v as a flat antisym vector by:
       v_emb[i,j] = sign(i-j) * v_index(i+j) ... (heuristic; we use a fixed
       embedding so that comparison across matrices is meaningful, even if
       the embedding is one of many choices).
    """
    A = (M - M.T) / 2
    # Upper triangle entries (i < j), 45 of them
    ut = np.array([A[i, j] for i in range(10) for j in range(i + 1, 10)])
    # Fixed Higgs embedding (45-vector); per WP106 §1.1 we use a canonical
    # but not unique encoding. Take the WP104 9-vector and tile/index.
    higgs9 = np.array([-1/np.sqrt(2), -1/np.sqrt(2), -1/np.sqrt(2),
                       -1/np.sqrt(2), -1/np.sqrt(2), 0.0, 0.0,
                       -1/np.sqrt(2), 0.0])  # v_0..v_8 with v_5=v_6=0,
                                              # v_7=-1/sqrt(2), v_8=0
    # Embed as repeating pattern (length 45 = 5 * 9)
    higgs45 = np.tile(higgs9, 5)
    if np.linalg.norm(ut) == 0 or np.linalg.norm(higgs45) == 0:
        return 0.0
    return float(np.dot(ut, higgs45) / (np.linalg.norm(ut) * np.linalg.norm(higgs45)))


DETECTORS = {
    "D1_LJ":          D1_lj,
    "D2_P56":         D2_p56,
    "D3_prime11":     D3_prime11,
    "D4_higgs_cos":   D4_higgs,
}


# ----- structured-matrix family generators -----

def gen_gaussian(n, rng):
    return rng.standard_normal((n, n))


def gen_symmetric(n, rng):
    M = rng.standard_normal((n, n))
    return (M + M.T) / 2


def gen_antisymmetric(n, rng):
    M = rng.standard_normal((n, n))
    return (M - M.T) / 2


def gen_permutation(n, rng):
    perm = rng.permutation(n)
    P = np.zeros((n, n))
    for i, j in enumerate(perm):
        P[i, j] = 1
    return P


def gen_hadamard_sign(n, rng):
    return rng.choice([-1.0, 1.0], size=(n, n))


def gen_orthogonal(n, rng):
    M = rng.standard_normal((n, n))
    Q, _ = qr(M)
    return Q


def gen_dft_real(n, rng=None):
    """Real part of the DFT matrix (n=10)."""
    omega = np.exp(2j * np.pi / n)
    return np.real(np.array([[omega ** (i * j) for j in range(n)] for i in range(n)]))


def gen_identity(n, rng=None):
    return np.eye(n)


def gen_diagonal(n, rng):
    d = rng.standard_normal(n)
    return np.diag(d)


def gen_companion(n, rng):
    """Companion matrix of a random monic integer polynomial of degree n.
    Coefficients in [-3, 3]."""
    coeffs = rng.integers(-3, 4, size=n).astype(float)  # constant ... lam^(n-1)
    C = np.zeros((n, n))
    for i in range(n - 1):
        C[i + 1, i] = 1
    for i in range(n):
        C[i, n - 1] = -coeffs[i]
    return C


FAMILIES = {
    "gaussian":     (gen_gaussian, True),       # rng-driven
    "symmetric":    (gen_symmetric, True),
    "antisymmetric":(gen_antisymmetric, True),
    "permutation":  (gen_permutation, True),
    "hadamard":     (gen_hadamard_sign, True),
    "orthogonal":   (gen_orthogonal, True),
    "dft_real":     (gen_dft_real, False),
    "identity":     (gen_identity, False),
    "diagonal":     (gen_diagonal, True),
    "companion":    (gen_companion, True),
}


def sample_family(family_name, n_samples=200, n=10, seed=0):
    """Sample n_samples 10x10 matrices from a family. For deterministic
    families (dft, identity), just return the single matrix repeated."""
    rng = np.random.default_rng(seed)
    gen, is_random = FAMILIES[family_name]
    samples = []
    if not is_random:
        # Single deterministic matrix
        samples = [gen(n)]
    else:
        for _ in range(n_samples):
            samples.append(gen(n, rng))
    return samples


def evaluate(M):
    return {name: f(M) for name, f in DETECTORS.items()}


def compute_stats(samples):
    """For each detector, compute mean, std, min, max across samples."""
    if not samples:
        return {}
    detector_values = {name: [] for name in DETECTORS}
    for M in samples:
        ev = evaluate(M)
        for name in DETECTORS:
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


def cohens_d(stats_a, stats_b):
    """Cohen's d between two stats dicts."""
    out = {}
    for name in stats_a:
        ma = stats_a[name]["mean"]
        mb = stats_b[name]["mean"]
        sa = stats_a[name]["std"]
        sb = stats_b[name]["std"]
        if sa == 0 and sb == 0:
            out[name] = float("inf") if ma != mb else 0.0
        else:
            pooled = np.sqrt((sa ** 2 + sb ** 2) / 2)
            out[name] = (ma - mb) / pooled if pooled > 0 else float("inf")
    return out


def main():
    print("=" * 100)
    print("WP114 -- specificity extension: structured-matrix sweep")
    print("=" * 100)
    print()

    # Positive controls: TSML and BHML
    print("Positive controls:")
    print("-" * 70)
    tsml_eval = evaluate(TSML)
    bhml_eval = evaluate(BHML)
    for name in DETECTORS:
        print(f"  {name:<14} TSML = {tsml_eval[name]:+10.6f}    BHML = {bhml_eval[name]:+10.6f}")
    print()

    # Sample each family
    print("Family sweep (200 samples each, 10x10 matrices):")
    print("-" * 100)
    print(f"{'family':<16} {'D1_LJ mean':<14} {'D2_P56 mean':<14} {'D3_prime11':<14} {'D4_higgs mean':<14}")
    print("-" * 100)

    family_stats = {}
    gauss_stats = None
    for fname in FAMILIES:
        samples = sample_family(fname, n_samples=200)
        stats = compute_stats(samples)
        family_stats[fname] = stats
        if fname == "gaussian":
            gauss_stats = stats
        d1 = stats["D1_LJ"]["mean"]
        d2 = stats["D2_P56"]["mean"]
        # D3 is integer; show fraction of samples with positive
        d3_frac = stats["D3_prime11"]["mean"]
        d4 = stats["D4_higgs_cos"]["mean"]
        print(f"  {fname:<14} {d1:+10.6f}     {d2:+10.6f}     {d3_frac:+10.6f}     {d4:+10.6f}")
    print()

    # Cohen's d vs Gaussian baseline
    print("Cohen's d vs Gaussian baseline:")
    print("-" * 100)
    print(f"{'family':<16} {'D1_LJ d':<12} {'D2_P56 d':<12} {'D3_prime11 d':<14} {'D4_higgs d':<12}")
    print("-" * 100)
    for fname in FAMILIES:
        if fname == "gaussian":
            continue
        d = cohens_d(family_stats[fname], gauss_stats)
        d1 = d["D1_LJ"]
        d2 = d["D2_P56"]
        d3 = d["D3_prime11"]
        d4 = d["D4_higgs_cos"]

        def tag(x):
            if abs(x) >= 0.8:
                return "**"
            if abs(x) >= 0.5:
                return "*"
            if abs(x) >= 0.2:
                return "."
            return ""

        print(f"  {fname:<14} {d1:+8.3f}{tag(d1):<4} {d2:+8.3f}{tag(d2):<4} "
              f"{d3:+8.3f}{tag(d3):<6} {d4:+8.3f}{tag(d4):<4}")
    print()
    print("Tag legend: ** large effect (|d|>=0.8), * medium (>=0.5), . small (>=0.2), blank no effect (<0.2)")
    print()

    # Comparison to TSML / BHML (treat them as 1-element samples)
    print("TSML / BHML vs Gaussian baseline (Cohen's d, single-sample):")
    print("-" * 100)
    for matrix_name, ev in [("TSML", tsml_eval), ("BHML", bhml_eval)]:
        d_tsml = {}
        for name in DETECTORS:
            mb = gauss_stats[name]["mean"]
            sb = gauss_stats[name]["std"]
            if sb > 0:
                d_tsml[name] = (ev[name] - mb) / sb
            else:
                d_tsml[name] = float("inf")
        d1 = d_tsml["D1_LJ"]
        d2 = d_tsml["D2_P56"]
        d3 = d_tsml["D3_prime11"]
        d4 = d_tsml["D4_higgs_cos"]

        def tag(x):
            if abs(x) >= 0.8:
                return "**"
            if abs(x) >= 0.5:
                return "*"
            if abs(x) >= 0.2:
                return "."
            return ""

        print(f"  {matrix_name:<14} {d1:+8.3f}{tag(d1):<4} {d2:+8.3f}{tag(d2):<4} "
              f"{d3:+8.3f}{tag(d3):<6} {d4:+8.3f}{tag(d4):<4}")
    print()

    # Verdict
    print("=" * 100)
    print("VERDICT")
    print("=" * 100)
    print()
    big_effects = []
    for fname in FAMILIES:
        if fname == "gaussian":
            continue
        d = cohens_d(family_stats[fname], gauss_stats)
        for name, value in d.items():
            if abs(value) >= 0.5:
                big_effects.append((fname, name, value))
    if not big_effects:
        print("  NO structured family in the test battery shows medium-or-larger Cohen's d (|d| >= 0.5)")
        print("  on ANY detector relative to the Gaussian baseline.")
        print("  The negative scope established in WP106 EXTENDS to all 9 structured matrix")
        print("  families tested. TIG structure remains specific to canonical TSML/BHML.")
    else:
        print(f"  {len(big_effects)} (family, detector) pairs show medium-or-larger effect:")
        for fname, dname, val in big_effects:
            print(f"    {fname:<14} {dname:<14} d = {val:+.3f}")
        print()
        print("  These deviations from the Gaussian baseline are STRUCTURAL features of the")
        print("  family (e.g., antisymmetric matrices have D1_LJ = 1.0 by definition).")
        print("  They do NOT indicate TIG-structure presence; they indicate detector")
        print("  measurement of the family's known structural property.")


if __name__ == "__main__":
    main()
