#!/usr/bin/env python3
"""
void_lens.py -- Round 8 (void_lens/PREREG.md): measuring magic squares from their unoccupied center.

Run from binary_magic/:  python3 void_lens/void_lens.py --full   (the registered run, about 12 min, log in round8_full.log)
                         python3 void_lens/void_lens.py          (quick: smaller samples, D4 search skipped)
Part A: closed-form determinant of MATLAB's odd magic(n); nonsingularity of all odd "linear" squares.
Part B: why MATLAB's doubly-even magic(n) has rank 3; singly-even rank n/2 + 2.
Part C: the void index bound nullity >= |(f_P + f_Q)/2 - 1| for complement symmetries.
Prints ASCII only. Exact integer arithmetic throughout (no floating-point determinants or ranks).
"""
import itertools, json, math, os, random, sys, time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
QUICK = "--full" not in sys.argv
res = {}

# ---------------------------------------------------------------- exact linear algebra
def det_bareiss(A):
    A = [list(r) for r in A]; n = len(A); sign = 1; prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            p = next((r for r in range(k + 1, n) if A[r][k]), None)
            if p is None: return 0
            A[k], A[p] = A[p], A[k]; sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
        prev = A[k][k]
    return sign * A[n - 1][n - 1]

def rank_exact(A):
    A = [list(r) for r in A]; m, n = len(A), len(A[0]); r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c]), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]
        for i in range(m):
            if i != r and A[i][c]:
                f, g = A[r][c], A[i][c]
                A[i] = [f * x - g * y for x, y in zip(A[i], A[r])]
                gg = 0
                for x in A[i]: gg = math.gcd(gg, x)
                if gg > 1: A[i] = [x // gg for x in A[i]]
        r += 1
        if r == m: break
    return r

def is_magic(M):
    n = len(M); s = n * (n * n + 1) // 2 if min(min(r) for r in M) == 1 else n * (n * n - 1) // 2
    L = [sum(r) for r in M] + [sum(c) for c in zip(*M)]
    L += [sum(M[i][i] for i in range(n)), sum(M[i][n - 1 - i] for i in range(n))]
    return set(L) == {s} and sorted(v for r in M for v in r) == list(range(min(min(r) for r in M), min(min(r) for r in M) + n * n))

# ---------------------------------------------------------------- MATLAB magic(n), transcribed from magic.m
def magic(n):
    if n % 2 == 1:
        return [[n * ((I + J - (n + 3) // 2) % n) + ((I + 2 * J - 2) % n) + 1 for J in range(1, n + 1)]
                for I in range(1, n + 1)]
    if n % 4 == 0:
        t = [((i % 4) // 2) for i in range(1, n + 1)]
        return [[(n * n + 1 - ((I - 1) * n + J)) if t[I - 1] == t[J - 1] else ((I - 1) * n + J)
                 for J in range(1, n + 1)] for I in range(1, n + 1)]
    p = n // 2; A = magic(p)                          # singly even (LUX-type), as in magic.m
    M = [[0] * n for _ in range(n)]
    for i in range(p):
        for j in range(p):
            M[i][j] = A[i][j]; M[i][j + p] = A[i][j] + 2 * p * p
            M[i + p][j] = A[i][j] + 3 * p * p; M[i + p][j + p] = A[i][j] + p * p
    k = (n - 2) // 4
    cols = list(range(1, k + 1)) + list(range(n - k + 2, n + 1))
    for J in cols:
        for i in range(p):
            M[i][J - 1], M[i + p][J - 1] = M[i + p][J - 1], M[i][J - 1]
    i = k + 1
    for J in (1, i):
        M[i - 1][J - 1], M[i + p - 1][J - 1] = M[i + p - 1][J - 1], M[i - 1][J - 1]
    return M

# ---------------------------------------------------------------- Part A
def orbits_double(n):
    seen, out = set(), []
    for k in range(1, n):
        if k in seen: continue
        o = []; x = k
        while x not in o:
            o.append(x); x = (2 * x) % n
        seen |= set(o); out.append(o)
    return out

def closed_form(n):
    v = (-1) ** ((n - 1) // 2) * n ** (n - 1) * (n * n + 1) // 2
    for o in orbits_double(n):
        v *= n ** len(o) - (-1) ** len(o)
    return v

print("PART A: odd magic(n)")
seen_ok = all(det_bareiss(magic(n)) == closed_form(n) for n in range(3, 22, 2))
fresh = list(range(23, 62, 2)) if not QUICK else [23, 25, 27]
fresh_ok = True
for n in fresh:
    M = magic(n); assert is_magic(M)
    if det_bareiss(M) != closed_form(n): fresh_ok = False; print("  MISMATCH at n =", n)
print(f"  closed form matches exact det: n = 3..21 (already seen) {seen_ok}; n = {fresh[0]}..{fresh[-1]} (fresh) {fresh_ok}")
print("  examples:", {n: closed_form(n) for n in (3, 5, 7)})
res["D1"] = seen_ok and fresh_ok

def linear(n, a1, b1, c1, a2, b2, c2):
    return [[n * ((a1 * i + b1 * j + c1) % n) + ((a2 * i + b2 * j + c2) % n) + 1 for j in range(n)] for i in range(n)]

units = lambda n: [u for u in range(1, n) if math.gcd(u, n) == 1]
zero = 0; tested = 0
for n in (5, 7):
    U = units(n)
    for a1, b1, a2, b2 in itertools.product(U, repeat=4):
        for c1, c2 in itertools.product(range(n), repeat=2):
            tested += 1
            if det_bareiss(linear(n, a1, b1, c1, a2, b2, c2)) == 0: zero += 1
rng = random.Random(8)
for n in (9, 15, 21, 25):
    U = units(n)
    for _ in range(2000 if not QUICK else 100):
        tested += 1
        if det_bareiss(linear(n, *[rng.choice(U), rng.choice(U), rng.randrange(n), rng.choice(U), rng.choice(U), rng.randrange(n)])) == 0:
            zero += 1
print(f"  linear squares tested: {tested}; zero determinants: {zero}")
res["D2"] = zero == 0

# D3: does the linear family cover all pandiagonal 5x5 squares?
def pandiagonal(M):
    n = len(M); s = sum(M[0])
    return all(sum(M[i][(i + d) % n] for i in range(n)) == s and sum(M[i][(d - i) % n] for i in range(n)) == s
               for d in range(n))
fam = set(); magic5 = set()
for a1, b1, a2, b2 in itertools.product(units(5), repeat=4):
    for c1, c2 in itertools.product(range(5), repeat=2):
        M = linear(5, a1, b1, c1, a2, b2, c2)
        if not is_magic(M): continue
        key = tuple(v for r in M for v in r); magic5.add(key)
        if pandiagonal(M): fam.add(key)
print(f"  linear 5x5 family: {len(magic5)} distinct magic squares, {len(fam)} pandiagonal (prediction: 28,800)")
res["D3"] = len(fam) == 28800

# D4: a singular natural 5x5 magic square by simple annealing (budget 10 CPU-minutes)
def anneal5(rng, steps=200000):
    n = 5; s = 65; v = list(range(1, 26)); rng.shuffle(v); M = [v[5 * i:5 * i + 5] for i in range(5)]
    def cost(M):
        L = [sum(r) for r in M] + [sum(c) for c in zip(*M)] + [sum(M[i][i] for i in range(5)), sum(M[i][4 - i] for i in range(5))]
        return sum(abs(x - s) for x in L)
    c = cost(M); T = 3.0
    for t in range(steps):
        i1, j1, i2, j2 = rng.randrange(5), rng.randrange(5), rng.randrange(5), rng.randrange(5)
        M[i1][j1], M[i2][j2] = M[i2][j2], M[i1][j1]
        c2 = cost(M)
        if c2 <= c or rng.random() < math.exp((c - c2) / T): c = c2
        else: M[i1][j1], M[i2][j2] = M[i2][j2], M[i1][j1]
        T = max(0.05, T * 0.9995)
        if c == 0: return M
    return None
t0 = time.time(); found = None; made = 0; budget = 600 if not QUICK else 0
while time.time() - t0 < budget:
    M = anneal5(rng, 20000)
    if M is None: continue
    made += 1
    if det_bareiss(M) == 0: found = M; break
if QUICK:
    print("  D4 annealing search skipped in quick mode (registered result: round8_full.log)")
else:
    print(f"  annealing: {made} natural 5x5 magic squares in {time.time() - t0:.0f}s; singular one found: {found}")
    res["D4"] = found is not None

# ---------------------------------------------------------------- Part B
print("\nPART B: even magic(n)")
e1 = True
for n in range(4, 65, 4):
    M = magic(n); assert is_magic(M)
    sig = [1 if ((i % 4) // 2) == 0 else -1 for i in range(1, n + 1)]          # (1,-1,-1,1) tiled
    u = [2 * (i - 1) - (n - 1) for i in range(1, n + 1)]                        # 2*(i - (n+1)/2), odd about center
    # 2N = 2M - (n^2+1)E  =  -sigma_i sigma_j (n u_i + u_j)
    ok = all(2 * M[i][j] - (n * n + 1) == -sig[i] * sig[j] * (n * u[i] + u[j]) for i in range(n) for j in range(n))
    rk = rank_exact(M)
    if not ok or rk != 3: e1 = False; print("  E1 fails at n =", n, ok, rk)
print("  doubly even n = 4..64: rank-2 formula for M - (c/2)E exact and rank 3:", e1)
res["E1"] = e1
e2 = {}
for n in range(6, 63, 4):
    M = magic(n); assert is_magic(M), n
    e2[n] = rank_exact(M)
print("  singly even ranks:", e2)
res["E2"] = all(r == n // 2 + 2 for n, r in e2.items())

# ---------------------------------------------------------------- Part C
print("\nPART C: void index bound")
def comp_map(M, c):
    n = len(M); pos = {M[i][j]: (i, j) for i in range(n) for j in range(n)}
    m = {(i, j): pos.get(c - M[i][j]) for i in range(n) for j in range(n)}
    if any(v is None for v in m.values()): return None
    P = [m[(i, 0)][0] for i in range(n)]; Q = [m[(0, j)][1] for j in range(n)]
    if all(m[(i, j)] == (P[i], Q[j]) for i in range(n) for j in range(n)): return ("rowcol", P, Q)
    P2 = [m[(i, 0)][1] for i in range(n)]; Q2 = [m[(0, j)][0] for j in range(n)]
    if all(m[(i, j)] == (Q2[j], P2[i]) for i in range(n) for j in range(n)): return ("transpose", P2, Q2)
    return None

def fixed(p): return sum(1 for i, x in enumerate(p) if i == x)

sq4 = [s["square"] for s in json.load(open(os.path.join(HERE, "..", "squares_4x4.json")))]
i1 = True; kinds = Counter(); idx0 = []
for M in sq4:
    cm = comp_map(M, 15); D = det_bareiss(M); nul = 4 - rank_exact(M)
    if cm is None:
        kinds[("none", "singular" if D == 0 else "invertible")] += 1; continue
    t, P, Q = cm
    if t == "rowcol":
        b = abs((fixed(P) + fixed(Q)) / 2 - 1)
        if nul < b: i1 = False
        kinds[("rowcol f=%d,%d idx=%g" % (fixed(P), fixed(Q), b), "singular" if D == 0 else "invertible")] += 1
        if b == 0: idx0.append(M)
    else:
        kinds[("transpose-type", "singular" if D == 0 else "invertible")] += 1
for k, v in sorted(kinds.items()): print("  ", k, v)
res["I1"] = i1
res["I2"] = len(idx0) > 0
refined = all(((det_bareiss(M) == 0) ==
               (lambda cm: cm is not None and cm[0] == "rowcol" and abs((fixed(cm[1]) + fixed(cm[2])) / 2 - 1) >= 1)(comp_map(M, 15)))
              for M in sq4)
res["I3"] = refined

# I4: affine fully binary 8x8 squares with a mirror complement
def rand_affine8(rng, need_mirror):
    allowed = [(wr << 3) | wc for wr in range(1, 8) for wc in range(1, 8) if wr != wc
               and (not need_mirror or bin(wc).count("1") % 2 == 1)]
    while True:
        forms = rng.sample(allowed, 6)
        basis = []
        for f in forms:
            v = f
            for b in basis: v = min(v, v ^ b)
            if v == 0: break
            basis.append(v)
        if len(basis) == 6: break
    const = rng.randrange(64)
    M = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            x = (i << 3) | j
            M[i][j] = sum(((bin(f & x).count("1") + (const >> k)) % 2) << k for k, f in enumerate(forms))
    return M
i4 = True; nul_counts = Counter()
for _ in range(500 if not QUICK else 50):
    M = rand_affine8(rng, True)
    assert all(M[i][7 - j] == 63 - M[i][j] for i in range(8) for j in range(8))
    assert is_magic(M)
    nul = 8 - rank_exact(M); nul_counts[nul] += 1
    if nul < 3: i4 = False
print("  affine 8x8 with a left-right complement mirror: nullity counts", dict(sorted(nul_counts.items())))
res["I4"] = i4

ann = [list(map(int, l.split())) for l in open(os.path.join(HERE, "..", "order8", "squares8_annealed.txt"))]
ann = [[r[8 * i:8 * i + 8] for i in range(8)] for r in ann]
hits = sum(1 for M in ann if comp_map(M, 63) is not None)
print(f"  annealed 8x8: {len(ann)} squares, {hits} with a factorised complement map")
res["I5"] = hits == 0

print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
