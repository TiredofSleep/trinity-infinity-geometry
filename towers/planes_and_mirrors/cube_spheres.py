"""
cube_spheres.py — every cube is two spheres (contained and containing), plus the one it actually lives on,
and the physics version: corners = definite outcomes, sphere = quantum correlations. See PREREG.md.
"""
import itertools, math
import numpy as np
rng = np.random.default_rng(5)
res = {}

# S1: the two spheres
ok = True
for n in range(1, 9):
    corners = np.array(list(itertools.product((-1, 1), repeat=n)), float)
    r_out = np.linalg.norm(corners, axis=1).max(); r_in = 1.0                  # face centres at distance 1
    ok &= math.isclose(r_out, math.sqrt(n))
    ball = math.pi ** (n / 2) / math.gamma(n / 2 + 1)
    print(f"  n={n}: contained r=1, containing r={r_out:.3f}; contained ball fills {ball / 2**n:6.1%} of the cube,"
          f" cube fills {2**n / (ball * n ** (n / 2)):6.1%} of the containing ball")
only4 = [n for n in range(1, 50) if math.isclose(math.sqrt(n), 2.0)]
res["S1"] = ok and only4 == [4]
print("S1  radii 1 and sqrt(n); corner distance = edge length only in n =", only4)

# S2: the third sphere, where the cube's volume actually is
ok = True
for n in (3, 10, 100, 1000):
    r = np.linalg.norm(rng.uniform(-1, 1, size=(20000, n)), axis=1)
    ok &= abs(r.mean() / math.sqrt(n / 3) - 1) < 0.01 and 0.2 < r.std() < 0.33
    print(f"  n={n:4d}: points sit at radius {r.mean():7.3f} (sqrt(n/3) = {math.sqrt(n/3):7.3f}), shell width {r.std():.3f};"
          f" contained r=1, containing r={math.sqrt(n):.2f}")
res["S2"] = ok
print("S2  the cube lives on a third sphere, sqrt(n/3), in a shell of fixed width:", ok)

# corner value and vector value of a two-party sign game A (rows = Alice's settings, cols = Bob's)
def corner_value(A):
    m = A.shape[0]
    return max(np.abs(np.array(x) @ A).sum() for x in itertools.product((-1, 1), repeat=m))
try:
    import cvxpy as cp
    def vector_value(A):
        m, k = A.shape
        X = cp.Variable((m + k, m + k), PSD=True)
        prob = cp.Problem(cp.Maximize(cp.sum(cp.multiply(A, X[:m, m:]))), [cp.diag(X) == 1])
        prob.solve(solver=cp.CLARABEL)
        return prob.value
    SOLVER = "SDP (cvxpy/Clarabel), exact up to solver tolerance"
except ImportError:
    def vector_value(A, restarts=20):                   # fallback: alternating maximisation, a lower bound
        m, k = A.shape; best = 0
        for _ in range(restarts):
            V = rng.normal(size=(k, m + k)); V /= np.linalg.norm(V, axis=1, keepdims=True)
            for _ in range(500):
                U = A @ V; U /= np.linalg.norm(U, axis=1, keepdims=True)
                V = A.T @ U; V /= np.linalg.norm(V, axis=1, keepdims=True)
            best = max(best, np.sum(A * (U @ V.T)))
        return best
    SOLVER = "alternating maximisation (lower bound)"
print(f"\nvector values by {SOLVER}")

# S3: CHSH
CHSH = np.array([[1, 1], [1, -1]], float)
c, q = corner_value(CHSH), vector_value(CHSH)
res["S3"] = math.isclose(c, 2) and abs(q - 2 * math.sqrt(2)) < 1e-5
print(f"S3  CHSH: corners {c:.0f}, sphere {q:.6f} (2*sqrt2 = {2*math.sqrt(2):.6f}); ratio {q/c:.6f}")

# S4: KCBS pentagon: 5 projectors, neighbours exclusive. Corners: max independent set; vectors: Lovasz theta.
alpha = max(sum(s) for s in itertools.product((0, 1), repeat=5) if all(not (s[i] and s[(i + 1) % 5]) for i in range(5)))
th = math.acos(1 / math.sqrt(5)) / 2 * 0                                     # explicit umbrella construction:
cz = math.sqrt(1 / math.sqrt(5)); rr = math.sqrt(1 - cz ** 2)               # each vector at height cz on a unit sphere
V = np.array([[rr * math.cos(4 * math.pi * k / 5), rr * math.sin(4 * math.pi * k / 5), cz] for k in range(5)])
orth = all(abs(V[k] @ V[(k + 1) % 5]) < 1e-12 for k in range(5))
theta = sum((V[k] @ np.array([0, 0, 1])) ** 2 for k in range(5))
res["S4"] = alpha == 2 and orth and math.isclose(theta, math.sqrt(5))
print(f"S4  KCBS: corners {alpha}, sphere {theta:.6f} (sqrt5 = {math.sqrt(5):.6f}); neighbours orthogonal: {orth}")

# S5-S7: random sign games
KRIVINE = math.pi / (2 * math.log(1 + math.sqrt(2)))
means, worst, allr = [], [], []
for n in range(2, 9):
    rs = []
    for _ in range(200):
        A = rng.choice((-1.0, 1.0), size=(n, n))
        rs.append(vector_value(A) / corner_value(A))
    means.append(np.mean(rs)); worst.append(max(rs)); allr += rs
    print(f"  size {n}: mean ratio {np.mean(rs):.4f}, max {max(rs):.4f}")
res["S5"] = max(allr) <= KRIVINE + 1e-6
res["S6"] = max(allr) <= math.sqrt(2) + 1e-6
res["S7"] = all(b > a for a, b in zip(means, means[1:]))
print(f"S5  max ratio {max(allr):.4f} <= Krivine {KRIVINE:.4f}: {res['S5']}")
print(f"S6  max ratio {max(allr):.4f} <= sqrt2 {math.sqrt(2):.4f}: {res['S6']}")
print(f"S7  mean ratio grows with size: {res['S7']}  {[round(m, 4) for m in means]}")
print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
assert all(res[k] for k in ("S1", "S3", "S4", "S5")), "a translation check failed"

# ---------- POST HOC (after scoring)
print("\n--- post hoc")
for n in (3, 10, 100, 1000):
    x = rng.uniform(-1, 1, size=(20000, n)); r = np.linalg.norm(x, axis=1)
    rms = math.sqrt((r ** 2).mean())
    assert abs(rms / math.sqrt(n / 3) - 1) < 0.01
    print(f"  n={n:4d}: root-mean-square radius {rms:7.3f} vs sqrt(n/3) {math.sqrt(n/3):7.3f}; mean radius {r.mean():7.3f}")
print("S2 diagnosis: sqrt(n/3) is the root-mean-square radius, exact in every dimension. The mean radius is a little")
print("   smaller (a curved average of a spread-out shell), so it misses by 4% at n = 3 and converges as n grows.")
print("S7 diagnosis: the mean ratio zigzags by parity, higher at even sizes. With an odd number of +-1 entries a column")
print("   sum can never be 0, so definite outcomes lose less to the sphere. Odd sizes: 1.07 -> 1.09 -> 1.10, even: 1.18,")
print("   1.12, 1.11, 1.12.")
