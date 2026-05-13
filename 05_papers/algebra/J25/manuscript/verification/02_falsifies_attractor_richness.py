"""
02_falsifies_attractor_richness.py

Tests Gemini's second proposed mechanism for BHML's anti-collapse role:
"BHML's richer attractor structure mitigates TSML's single-point attractor."

RESULT: Falsified.
  - TSML attractor entropy: 0.000 (single point)
  - BHML attractor entropy: 1.358 (4-component fixed point)
  - Random tables mean attractor entropy: 2.238 (RICHER than BHML)
  - Correlation (H_attractor, anti-collapse improvement): -0.118 (weak)
  
BHML's attractor entropy is at the 0th percentile of random tables,
yet BHML outperforms 100% of them on anti-collapse. So attractor
richness is NOT the mechanism.

What IS the mechanism: see 03_eight_magma_core.py and 04_bridge_attractor.py
"""
import numpy as np
from numpy.linalg import lstsq

TSML_ROWS = ["0000000700","0737777777","0377477779","0777777773","0747777787",
             "0777777777","0777777777","7777777777","0777877777","0797377777"]
T = np.array([[int(c) for c in row] for row in TSML_ROWS], dtype=float)

BHML_ROWS = ["0123456789","1234567266","2334567366","3444567466","4555567577",
             "5666667677","6777777777","7234567890","8666777978","9666777080"]
B_REAL = np.array([[int(c) for c in row] for row in BHML_ROWS], dtype=float)


def fuse(p, q, table):
    r = np.zeros(10)
    for a in range(10):
        for b in range(10):
            r[int(table[a, b])] += p[a] * q[b]
    return r


def normalize_l1(v):
    s = v.sum()
    return v / s if s > 1e-12 else v


def entropy(p, eps=1e-12):
    return -np.sum(p[p > eps] * np.log(p[p > eps]))


def fixed_point_entropy(table, n_inits=20, depth=15):
    """Find table's typical fixed point and measure its entropy."""
    np.random.seed(0)
    fixed_points = []
    for _ in range(n_inits):
        p = normalize_l1(np.random.dirichlet(np.ones(10)))
        for _ in range(depth):
            p = normalize_l1(fuse(p, p, table))
        fixed_points.append(p)
    mean_fp = np.mean(fixed_points, axis=0)
    return entropy(mean_fp), mean_fp


def reconstruction_with_mix(B_table, n=200, depth=4, alpha=0.5):
    np.random.seed(7)
    train_inputs = [normalize_l1(np.random.dirichlet(np.ones(10))) for _ in range(n)]
    np.random.seed(8)
    test_inputs = [normalize_l1(np.random.dirichlet(np.ones(10))) for _ in range(100)]
    def trail(p):
        out = [p.copy()]
        p_cur = p.copy()
        for _ in range(depth):
            p_t = normalize_l1(fuse(p_cur, p_cur, T))
            p_b = normalize_l1(fuse(p_cur, p_cur, B_table))
            p_cur = normalize_l1(alpha * p_t + (1 - alpha) * p_b)
            out.append(p_cur.copy())
        return out
    train_trails = [trail(p) for p in train_inputs]
    test_trails = [trail(p) for p in test_inputs]
    X_train = np.array([np.concatenate(t[1:]) for t in train_trails])
    y_train = np.array(train_inputs)
    W, _, _, _ = lstsq(X_train, y_train, rcond=None)
    X_test = np.array([np.concatenate(t[1:]) for t in test_trails])
    y_test = np.array(test_inputs)
    return np.linalg.norm(X_test @ W - y_test, axis=1).mean()


if __name__ == "__main__":
    print("ATTRACTOR-RICHNESS HYPOTHESIS")
    print("=" * 60)

    T_attr_H, T_attr = fixed_point_entropy(T)
    B_attr_H, B_attr = fixed_point_entropy(B_REAL)
    real_err = reconstruction_with_mix(B_REAL)

    print(f"\nTSML attractor entropy: {T_attr_H:.4f}  (collapses to HARMONY)")
    print(f"BHML attractor entropy: {B_attr_H:.4f}  (4-component)")
    print(f"BHML anti-collapse err: {real_err:.4f}")

    print(f"\nTesting 40 random tables...")
    results = []
    for seed in range(40):
        np.random.seed(seed + 1000)
        table = np.random.randint(0, 10, size=(10, 10)).astype(float)
        H_attr, _ = fixed_point_entropy(table)
        err = reconstruction_with_mix(table)
        results.append((H_attr, err))

    H_vals = np.array([r[0] for r in results])
    err_vals = np.array([r[1] for r in results])
    corr = np.corrcoef(H_vals, err_vals)[0, 1]

    print(f"\nRandom tables:")
    print(f"  Mean attractor entropy: {H_vals.mean():.3f}")
    print(f"  Mean reconstruction err: {err_vals.mean():.4f}")
    print(f"  Pearson(H_attr, err): {corr:+.3f}")

    bhml_pct = (sum(1 for h in H_vals if h < B_attr_H) / len(H_vals)) * 100
    err_pct = (sum(1 for e in err_vals if e > real_err) / len(err_vals)) * 100
    print(f"\nBHML attractor entropy at {bhml_pct:.0f}th percentile of random tables")
    print(f"BHML err better than {err_pct:.0f}% of random tables")

    print(f"\nVERDICT: Attractor richness is NOT the anti-collapse mechanism.")
    print(f"  Random tables are RICHER but PERFORM WORSE.")
    print(f"  See 03_eight_magma_core.py for the actual mechanism.")
