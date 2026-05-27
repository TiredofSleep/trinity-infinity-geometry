"""sigma_magma_crypto.py -- cryptographic-quality tests for the sigma-magma.

Tests:
  (1) Differential uniformity (exact, over all 10^4 input pairs)
  (2) Linear approximation table bias (exact, over all 10^4 input pairs)
  (3) Avalanche (Monte Carlo, 10^6 trials)
  (4) Collision resistance for iterated Merkle-Damgaard hash (10^6 random messages)

Baselines for comparison:
  - pure addition: x*y = (x+y) mod 10
  - affine: x*y = (3x+7y+5) mod 10
  - sigma-magma: x*y = sigma((x+y) mod 10) with sigma = [0,7,1,3,2,4,5,6,8,9]
  - perfect random: a fresh uniformly-random 10x10 table

These compare a non-trivial yet structured magma (sigma-magma) against
the linear/affine baseline (worst possible) and a random function (best).
A crypto-relevant primitive should sit between these two.
"""
import random
import sys
import time
from collections import Counter


SIGMA = [0, 7, 1, 3, 2, 4, 5, 6, 8, 9]
N = 10


def magma_sigma(x, y):
    """sigma-magma: x*y = sigma((x+y) mod 10)."""
    return SIGMA[(x + y) % N]


def magma_add(x, y):
    """Pure addition: x*y = (x+y) mod 10."""
    return (x + y) % N


def magma_affine(x, y, a=3, b=7, c=5):
    """Affine: x*y = (ax + by + c) mod 10."""
    return (a * x + b * y + c) % N


def random_table(seed=42):
    """Return a uniformly random 10x10 table."""
    rng = random.Random(seed)
    t = [[rng.randrange(N) for _ in range(N)] for _ in range(N)]
    return lambda x, y: t[x][y]


# --------------- Test 1: differential uniformity ----------------

def differential_uniformity(op):
    """For each non-trivial (dx, dy), and each dz, count:
       |{(x,y) : op(x+dx, y+dy) - op(x,y) == dz mod N}|
       Return max over all (dx, dy, dz) with (dx, dy) != (0,0).
       Lower = better resistance to differential cryptanalysis.
    """
    max_count = 0
    worst = None
    for dx in range(N):
        for dy in range(N):
            if dx == 0 and dy == 0:
                continue
            counts = [0] * N
            for x in range(N):
                for y in range(N):
                    dz = (op((x + dx) % N, (y + dy) % N) - op(x, y)) % N
                    counts[dz] += 1
            mx = max(counts)
            if mx > max_count:
                max_count = mx
                worst = (dx, dy, counts.index(mx))
    return max_count, worst


# --------------- Test 2: linear approximation bias ----------------

def linear_bias(op):
    """Compute max bias of linear approximations:
       For each non-trivial (a, b, c) in Z_10^3, count:
           |{(x,y) : a*x + b*y + c*op(x,y) == 0 mod N}| - N^2 / N
       Return the maximum bias normalized to [0, 1].
       Bias = 0 means perfectly balanced (no linear leakage).
       Bias = 1 means deterministically linear.
    """
    max_bias = 0
    worst = None
    expected = N * N / N  # = 10 for N=10
    for a in range(N):
        for b in range(N):
            for c in range(N):
                if a == 0 and b == 0 and c == 0:
                    continue
                cnt = 0
                for x in range(N):
                    for y in range(N):
                        if (a * x + b * y + c * op(x, y)) % N == 0:
                            cnt += 1
                # bias from expected
                bias = abs(cnt - expected) / (N * N)
                if bias > max_bias:
                    max_bias = bias
                    worst = (a, b, c, cnt)
    return max_bias, worst


# --------------- Test 3: avalanche ----------------

def avalanche_monte_carlo(op, n_trials=10**6, seed=42):
    """Probability that changing one input changes the output."""
    rng = random.Random(seed)
    n_change_x = 0  # output changes when x changes
    n_change_y = 0  # output changes when y changes
    for _ in range(n_trials):
        x = rng.randrange(N)
        y = rng.randrange(N)
        # flip x to a different value
        xp = (x + 1 + rng.randrange(N - 1)) % N
        yp = (y + 1 + rng.randrange(N - 1)) % N
        if op(x, y) != op(xp, y):
            n_change_x += 1
        if op(x, y) != op(x, yp):
            n_change_y += 1
    p_change_x = n_change_x / n_trials
    p_change_y = n_change_y / n_trials
    # Ideal for random function: 9/10 = 0.9
    ideal = (N - 1) / N
    return p_change_x, p_change_y, ideal


# --------------- Test 4: Merkle-Damgaard collision resistance ----------------

def md_hash(message, op, state0=0):
    """Iterate state = state ⋄ msg[i]. Output: final state (single digit, 0..9)."""
    state = state0
    for d in message:
        state = op(state, d)
    return state


def md_hash_extended(message, op, state_len=4, state0=None):
    """Extended state: each digit of state updated independently by msg digits.
       This gives a 10^state_len output space.
    """
    if state0 is None:
        state0 = [0] * state_len
    state = list(state0)
    for i, d in enumerate(message):
        idx = i % state_len
        state[idx] = op(state[idx], d)
    return tuple(state)


def collision_test(op, n_trials=10**6, msg_len=8, state_len=4, seed=42):
    """Generate n_trials random messages, hash each, count collisions."""
    rng = random.Random(seed)
    seen = {}
    n_collisions = 0
    for _ in range(n_trials):
        msg = [rng.randrange(N) for _ in range(msg_len)]
        h = md_hash_extended(msg, op, state_len=state_len)
        if h in seen:
            n_collisions += 1
        else:
            seen[h] = msg
    # Expected for random function over 10^state_len space:
    # E[collisions] ~ (n_trials choose 2) / 10^state_len
    space_size = N ** state_len
    expected = n_trials * (n_trials - 1) / (2 * space_size)
    return n_collisions, expected, space_size


# --------------- Master harness ----------------

def run_all(op, name, n_avalanche=10**6, n_collision=10**6):
    print(f"\n{'='*60}")
    print(f"  {name}")
    print(f"{'='*60}")

    t0 = time.time()
    du, du_worst = differential_uniformity(op)
    print(f"[1] Differential uniformity:")
    print(f"      max counts:     {du} / 100   (lower is better; min = 10 = uniform)")
    print(f"      worst (dx,dy,dz): {du_worst}")
    print(f"      ratio:          {du/100:.2%}")
    print(f"      time: {time.time()-t0:.2f}s")

    t0 = time.time()
    lb, lb_worst = linear_bias(op)
    print(f"[2] Linear approximation bias:")
    print(f"      max bias:       {lb:.4f}   (lower is better; 0 = perfectly balanced)")
    print(f"      worst (a,b,c,cnt): {lb_worst}")
    print(f"      time: {time.time()-t0:.2f}s")

    t0 = time.time()
    px, py, ideal = avalanche_monte_carlo(op, n_trials=n_avalanche)
    print(f"[3] Avalanche (n={n_avalanche}):")
    print(f"      P(output changes | x flipped): {px:.4f}")
    print(f"      P(output changes | y flipped): {py:.4f}")
    print(f"      ideal (random function):       {ideal:.4f}")
    print(f"      time: {time.time()-t0:.2f}s")

    t0 = time.time()
    n_coll, exp_coll, space = collision_test(op, n_trials=n_collision)
    print(f"[4] Merkle-Damgaard collisions (n={n_collision}, msg_len=8, state_len=4, space=10^4=10000):")
    print(f"      observed:       {n_coll}")
    print(f"      expected (random): {exp_coll:.0f}")
    print(f"      ratio observed/expected: {n_coll / exp_coll:.3f}")
    print(f"      time: {time.time()-t0:.2f}s")

    return {
        "name": name,
        "differential_uniformity": du,
        "du_worst": du_worst,
        "linear_bias": lb,
        "lb_worst": lb_worst,
        "avalanche_x": px,
        "avalanche_y": py,
        "avalanche_ideal": ideal,
        "n_collisions": n_coll,
        "expected_collisions": exp_coll,
    }


def main():
    if hasattr(sys.stdout, "reconfigure"):
        try: sys.stdout.reconfigure(encoding="utf-8")
        except: pass

    n_avalanche = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
    n_collision = int(sys.argv[2]) if len(sys.argv) > 2 else 10**6

    print(f"sigma-magma cryptographic tests")
    print(f"  n_avalanche  = {n_avalanche}")
    print(f"  n_collision  = {n_collision}")

    results = []
    results.append(run_all(magma_add, "Pure addition  x*y = (x+y) mod 10",
                            n_avalanche, n_collision))
    results.append(run_all(lambda x, y: magma_affine(x, y, 3, 7, 5),
                            "Affine  x*y = (3x+7y+5) mod 10",
                            n_avalanche, n_collision))
    results.append(run_all(magma_sigma,
                            "sigma-magma  x*y = sigma((x+y) mod 10)",
                            n_avalanche, n_collision))
    rand_op = random_table(seed=42)
    results.append(run_all(rand_op, "Random 10x10 table (seed=42)",
                            n_avalanche, n_collision))

    print("\n\n" + "="*60)
    print("  COMPARISON SUMMARY")
    print("="*60)
    print(f"{'name':<45s}  {'DU':>5s}  {'LB':>6s}  {'av-x':>6s}  {'av-y':>6s}  {'coll/exp':>9s}")
    for r in results:
        coll_ratio = r["n_collisions"] / r["expected_collisions"] if r["expected_collisions"] > 0 else float('inf')
        print(f"{r['name']:<45s}  {r['differential_uniformity']:>5d}  "
              f"{r['linear_bias']:>6.3f}  {r['avalanche_x']:>6.3f}  "
              f"{r['avalanche_y']:>6.3f}  {coll_ratio:>9.3f}")


if __name__ == "__main__":
    main()
