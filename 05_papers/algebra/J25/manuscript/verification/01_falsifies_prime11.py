"""
DECISIVE TEST: Is BHML's anti-collapse role SPECIFIC to BHML, or generic?

Hypothesis to test (from Gemini's pitch):
  "The 11-prime asymmetry is the physical reason the system stays alive."
  
Test design:
  Replace BHML with various alternative tables and measure information 
  preservation (reconstruction error) at α=0.5 mix:
  
  Conditions:
    1. T-only           — baseline (no mix)
    2. T+BHML-mix       — actual TIG pipeline
    3. T+random_table   — random integer table {0..9} (10 trials)
    4. T+11-free table  — random table with prime-11 explicitly absent from char poly
    5. T+identity       — mix with identity (preserve input directly)
    6. T+T_transpose    — mix with TSML's transpose (test asymmetry)
    7. T+T_negated      — mix with -TSML (test sign)
    
If condition 2 (real BHML) significantly outperforms 3-7, then BHML is 
SPECIFICALLY doing anti-collapse work.

If conditions 2-7 are all comparable, then "any mix is anti-collapse" — 
Gemini's strong claim about prime-11 doesn't survive.
"""
import numpy as np
from sympy import factorint
from numpy.linalg import lstsq

np.random.seed(42)

# Reference tables
TSML_ROWS = ["0000000700","0737777777","0377477779","0777777773","0747777787",
             "0777777777","0777777777","7777777777","0777877777","0797377777"]
T = np.array([[int(c) for c in row] for row in TSML_ROWS], dtype=float)

BHML_ROWS = ["0123456789","1234567266","2334567366","3444567466","4555567577",
             "5666667677","6777777777","7234567890","8666777978","9666777080"]
B_REAL = np.array([[int(c) for c in row] for row in BHML_ROWS], dtype=float)


# Operations
def fuse(p, q, table):
    r = np.zeros(10)
    for a in range(10):
        for b in range(10):
            r[int(table[a, b])] += p[a] * q[b]
    return r

def normalize_l1(v):
    s = v.sum()
    return v / s if s > 1e-12 else v

def get_trail(p_init, T_table, B_table=None, depth=4, alpha=0.5):
    """Generate fuse trail. If B_table is None, T-only."""
    trail = [p_init.copy()]
    p = p_init.copy()
    for _ in range(depth):
        p_t = normalize_l1(fuse(p, p, table=T_table))
        if B_table is not None:
            p_b = normalize_l1(fuse(p, p, table=B_table))
            p = normalize_l1(alpha * p_t + (1 - alpha) * p_b)
        else:
            p = p_t
        trail.append(p.copy())
    return trail


def has_prime_11_signature(table):
    """Check if a table has prime-11 in c_2 and c_8 of char poly (TSML's signature)."""
    char_poly = np.poly(table)
    int_coeffs = [int(round(c)) for c in char_poly]
    has_c2 = abs(int_coeffs[2]) > 0 and abs(int_coeffs[2]) % 11 == 0
    has_c8 = len(int_coeffs) > 8 and abs(int_coeffs[8]) > 0 and abs(int_coeffs[8]) % 11 == 0
    return has_c2 and has_c8


def reconstruction_error(T_table, B_table, n_train=200, n_test=100, depth=4, alpha=0.5):
    """
    Measure how well we can reconstruct input from trail.
    Lower = more information preserved.
    """
    np.random.seed(7)
    train_inputs = [normalize_l1(np.random.dirichlet(np.ones(10))) for _ in range(n_train)]
    np.random.seed(8)
    test_inputs = [normalize_l1(np.random.dirichlet(np.ones(10))) for _ in range(n_test)]
    
    train_trails = [get_trail(p, T_table, B_table, depth=depth, alpha=alpha) for p in train_inputs]
    test_trails = [get_trail(p, T_table, B_table, depth=depth, alpha=alpha) for p in test_inputs]
    
    # Trail [p_1..p_depth] → p_0 (linear regression)
    X_train = np.array([np.concatenate(t[1:]) for t in train_trails])
    y_train = np.array(train_inputs)
    W, _, _, _ = lstsq(X_train, y_train, rcond=None)
    
    X_test = np.array([np.concatenate(t[1:]) for t in test_trails])
    y_test = np.array(test_inputs)
    y_pred = X_test @ W
    err = np.linalg.norm(y_pred - y_test, axis=1).mean()
    
    # Baseline (predict mean of training set)
    baseline = np.linalg.norm(np.tile(y_train.mean(axis=0), (n_test, 1)) - y_test, axis=1).mean()
    
    return err, baseline


def make_random_table(seed, ensure_no_11=False, max_attempts=100):
    """Random 10x10 integer table {0..9}."""
    rng = np.random.RandomState(seed)
    if not ensure_no_11:
        return rng.randint(0, 10, size=(10, 10)).astype(float)
    
    # Try until we find one without prime 11
    for _ in range(max_attempts):
        candidate = rng.randint(0, 10, size=(10, 10)).astype(float)
        if not has_prime_11_signature(candidate):
            return candidate
    return None  # couldn't find one


# ============================================================
# Run the test
# ============================================================

print("="*70)
print("BHML SPECIFICITY TEST")
print("="*70)
print()

results = []

# Condition 1: T-only baseline
err, base = reconstruction_error(T, None)
results.append(('T-only (no mix)', err, base, 'baseline'))
print(f"  T-only:                    err={err:.4f}  baseline={base:.4f}  improvement={(base-err)/base*100:.1f}%")

# Condition 2: T+real BHML
err, base = reconstruction_error(T, B_REAL)
real_err = err
print(f"  T+BHML (real):             err={err:.4f}  baseline={base:.4f}  improvement={(base-err)/base*100:.1f}%")
real_has_11 = has_prime_11_signature(B_REAL)
print(f"    BHML has prime-11 sig: {real_has_11}")
print()

# Condition 3: T+random tables (10 trials)
print("Condition 3: T + random integer tables (10 trials)")
print("-" * 70)
random_errs = []
random_with_11 = []
random_no_11 = []
for trial in range(10):
    rand_table = make_random_table(seed=100 + trial)
    err, base = reconstruction_error(T, rand_table)
    has_11 = has_prime_11_signature(rand_table)
    random_errs.append(err)
    if has_11:
        random_with_11.append(err)
    else:
        random_no_11.append(err)
    print(f"  Trial {trial}: err={err:.4f}  has_11={has_11}")

print()
print(f"  Mean random-table err: {np.mean(random_errs):.4f}")
if random_with_11:
    print(f"  Random tables WITH 11:  mean err={np.mean(random_with_11):.4f} (n={len(random_with_11)})")
if random_no_11:
    print(f"  Random tables WITHOUT 11: mean err={np.mean(random_no_11):.4f} (n={len(random_no_11)})")
print()

# Condition 4: T+identity
identity = np.tile(np.arange(10), (10, 1)).astype(float)  # row i has value i in every column
err, base = reconstruction_error(T, identity)
print(f"  T+identity-table:          err={err:.4f}  improvement={(base-err)/base*100:.1f}%")

# Identity table: T[a,b] = b regardless of a. This makes fuse(p, q) = q (sums of pq)
# Actually: r[c] = sum_{a,b: T[a,b]=c} p[a]*q[b] = sum_{a,b: b=c} p[a]*q[b] = sum_a p[a] * q[c] = q[c]
# So fuse(p, p) = p. That's identity-like.

# Condition 5: T+T_transpose
T_transpose = T.T
err, base = reconstruction_error(T, T_transpose)
print(f"  T+TSML_transpose:          err={err:.4f}  improvement={(base-err)/base*100:.1f}%")

# Condition 6: T+constant (every cell = HARMONY = 7)
T_harmony = np.ones((10, 10)) * 7
err, base = reconstruction_error(T, T_harmony)
print(f"  T+all-HARMONY (7s):        err={err:.4f}  improvement={(base-err)/base*100:.1f}%")

# Condition 7: T+VOID-shifted (every cell = 0 except a few)
T_void_shift = np.zeros((10, 10))
T_void_shift[1, 1] = 7  # one nonzero
err, base = reconstruction_error(T, T_void_shift)
print(f"  T+sparse-table:            err={err:.4f}  improvement={(base-err)/base*100:.1f}%")

print()
print("="*70)
print("SUMMARY: is BHML specifically anti-collapse?")
print("="*70)
print()
print(f"  T-only baseline error:        {results[0][1]:.4f}")
print(f"  T+BHML error:                 {real_err:.4f}  (ratio to baseline: {real_err/results[0][1]:.3f})")
print(f"  T+random mean error:          {np.mean(random_errs):.4f}  (ratio to baseline: {np.mean(random_errs)/results[0][1]:.3f})")
if random_with_11:
    print(f"  T+random WITH 11:             {np.mean(random_with_11):.4f}")
if random_no_11:
    print(f"  T+random WITHOUT 11:          {np.mean(random_no_11):.4f}")
print()

# Decision
random_ratio = np.mean(random_errs) / results[0][1]
bhml_ratio = real_err / results[0][1]
relative_improvement = (np.mean(random_errs) - real_err) / np.mean(random_errs)

print(f"BHML's improvement over random-table-mix: {relative_improvement*100:+.1f}%")
print()

if relative_improvement > 0.10:
    print("✓ BHML SIGNIFICANTLY outperforms random tables.")
    print("  → 'Anti-collapse via BHML' has structural specificity.")
elif relative_improvement > 0.02:
    print("~ BHML modestly outperforms random tables.")
    print("  → Some specificity, but mostly generic-mix effect.")
else:
    print("⚠ BHML is comparable to random tables.")
    print("  → 'Any mix is anti-collapse' — Gemini's strong claim DOES NOT SURVIVE.")
    print("  → For IHÉS: do not claim BHML's prime-11 signature is the cause.")
print()

# Test prime-11 specifically
print("="*70)
print("PRIME-11 SUBHYPOTHESIS")
print("="*70)
if random_with_11 and random_no_11:
    diff = np.mean(random_no_11) - np.mean(random_with_11)
    if diff > 0.005:
        print(f"  Random tables WITH 11 do better by {diff:.4f}.")
        print(f"  → Modest support for 11 specifically being helpful.")
    elif diff < -0.005:
        print(f"  Random tables WITHOUT 11 do better by {-diff:.4f}.")
        print(f"  → 11 is NOT the specific helpful feature.")
    else:
        print(f"  Random tables with vs without 11 perform comparably (diff={diff:.4f}).")
        print(f"  → Prime-11 has no observable effect on anti-collapse.")
else:
    print("  Insufficient samples for prime-11 subhypothesis.")
