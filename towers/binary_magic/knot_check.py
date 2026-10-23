"""
knot_check.py — does the carry cube actually knot?

Setup (from trefoil_view.py): looking down the cube's diagonal gives a trefoil layout.
A knot needs over/under at each crossing. The only signed thing in the data is the
carry sign: on a carrying diagonal each carry is +1 or -1 (the other diagonal is the
exact opposite). Rule tested: a present crossing gets oriented crossing sign = carry sign,
applied the same way at every crossing.

Two independent ways to decide which crossings are "present" in a square:
  M1 (pair / Tait rule): the crossing between two petals is present when BOTH of those
      carries are used. (Crossing = edge between two petals.)
  M2 (direct rule): each carry is one crossing.
Absent crossings are smoothed; both smoothings are tried.

Knot type is identified with the Kauffman bracket (up to a unit +-A^k):
  unknot 1, 2-component unlink -A^2 - A^-2, Hopf link -A^4 - A^-4, trefoil A^-7 - A^-3 - A^5 (or mirror).
Needs squares_4x4.json.
"""
import json, math, itertools
import numpy as np
import sympy as sp
from collections import Counter

A = sp.symbols("A")
d = -A**2 - A**-2

# ---------- 1. the trefoil projection as a PD diagram ----------
def w(t):
    return np.exp(1j * t) - 2 * np.exp(-2j * t)
def dw(t):
    return 1j * np.exp(1j * t) + 4j * np.exp(-2j * t)

N = 6000
ts = np.linspace(0, 2 * np.pi, N, endpoint=False)
P = w(ts)
pairs = []
for i in range(N):
    dist = np.abs(P - P[i])
    gap = np.minimum(np.abs(np.arange(N) - i), N - np.abs(np.arange(N) - i))
    dist[gap < N // 10] = np.inf
    j = int(np.argmin(dist))
    if dist[j] < 5e-3 and i < j:
        pairs.append((ts[i], ts[j]))
crossings = []
for s, t in pairs:                                   # cluster near-duplicates, refine
    if all(abs(s - c[0]) > 0.05 for c in crossings):
        from scipy.optimize import fsolve
        f = lambda v: [(w(v[0]) - w(v[1])).real, (w(v[0]) - w(v[1])).imag]
        s2, t2 = fsolve(f, [s, t])
        crossings.append((s2 % (2 * np.pi), t2 % (2 * np.pi)))
crossings = sorted(crossings, key=lambda c: c[0])
assert len(crossings) == 3
angle = [round(math.degrees(np.angle(w(c[0]) * 1j * -1j)) % 360) for c in crossings]
# report positions in the same frame as trefoil_view.py (x = Im w, y = Re w)
pos_deg = [round(math.degrees(math.atan2(w(c[0]).real, w(c[0]).imag)) % 360) for c in crossings]
print("1. crossings at", pos_deg, "deg")

# passages in order along the curve; edges are labeled by the passage they START at
passages = sorted([(c[0], k) for k, c in enumerate(crossings)] + [(c[1], k) for k, c in enumerate(crossings)])
n_pass = len(passages)                               # 6
edge_in = {}                                          # (crossing, which strand) -> edge entering
edge_out = {}
for idx, (tp, k) in enumerate(passages):
    strand = 0 if abs(tp - crossings[k][0]) < 1e-9 else 1
    edge_in[(k, strand)] = (idx - 1) % n_pass + 1
    edge_out[(k, strand)] = idx % n_pass + 1

def crossing_X(k, over_strand):
    """PD X[a,b,c,d]: a = incoming under edge, then counterclockwise."""
    u = 1 - over_strand
    tu = crossings[k][u]
    to = crossings[k][over_strand]
    Tu, To = dw(tu), dw(to)
    Tu = np.array([Tu.imag, Tu.real]); To = np.array([To.imag, To.real])
    cross = Tu[0] * To[1] - Tu[1] * To[0]           # >0: over strand goes left-to-right ccw from under
    a, c = edge_in[(k, u)], edge_out[(k, u)]
    if cross > 0:   # counterclockwise from incoming-under we meet outgoing-over first
        b, dd = edge_out[(k, over_strand)], edge_in[(k, over_strand)]
    else:
        b, dd = edge_in[(k, over_strand)], edge_out[(k, over_strand)]
    sign = 1 if cross < 0 else -1                    # oriented crossing sign (right-hand rule)
    return (a, b, c, dd), sign

def over_for_sign(k, s):
    for o in (0, 1):
        if crossing_X(k, o)[1] == s:
            return o

def bracket(Xs, Ps):
    """Kauffman bracket. Xs: list of X tuples; Ps: list of 2-edge joins (smoothed crossings)."""
    total = 0
    for state in itertools.product((0, 1), repeat=len(Xs)):
        parent = {}
        def find(x):
            parent.setdefault(x, x)
            while parent[x] != x:
                parent[x] = parent[parent[x]]; x = parent[x]
            return x
        def join(x, y):
            parent[find(x)] = find(y)
        for e in range(1, n_pass + 1):
            find(e)
        for (a, b, c, dd), s in zip(Xs, state):
            if s == 0: join(a, b); join(c, dd)      # A-smoothing
            else:      join(a, dd); join(b, c)      # B-smoothing
        for x, y in Ps:
            join(x, y)
        loops = len({find(e) for e in range(1, n_pass + 1)})
        total += A**(state.count(0) - state.count(1)) * d**(loops - 1)
    return sp.expand(total)

def normalize(expr):
    expr = sp.expand(expr)
    poly = sp.Poly(sp.expand(expr * A**40), A)
    coeffs = poly.all_coeffs()
    while coeffs and coeffs[-1] == 0:
        coeffs.pop()
    lead = coeffs[0]
    return tuple(c / lead for c in coeffs)

TYPES = {
    normalize(sp.Integer(1)): "unknot",
    normalize(d): "2-unlink",
    normalize(-A**4 - A**-4): "Hopf link",
    normalize(A**-7 - A**-3 - A**5): "trefoil",
    normalize(A**7 - A**3 - A**-5): "trefoil (mirror)",
}
def knot_type(Xs, Ps):
    return TYPES.get(normalize(bracket(Xs, Ps)), "other")

# ---------- 2. all 8 full sign patterns ----------
print("2. all 8 over/under choices on the 3 crossings:")
full = {}
for signs in itertools.product((1, -1), repeat=3):
    Xs = [crossing_X(k, over_for_sign(k, s))[0] for k, s in enumerate(signs)]
    full[signs] = knot_type(Xs, [])
    print(f"   crossing signs {signs}: {full[signs]}")
knotted = [s for s, kt in full.items() if kt.startswith("trefoil")]
assert sorted(knotted) == [(-1, -1, -1), (1, 1, 1)]
print("   -> knotted exactly when all three signs agree; the other 6 are unknots")

# ---------- 3. what the squares supply ----------
LINES = [[(i, j) for j in range(4)] for i in range(4)] + \
        [[(i, j) for i in range(4)] for j in range(4)] + \
        [[(i, i) for i in range(4)], [(i, 3 - i) for i in range(4)]]
def carries(M):
    """carry vector (a,b,c) on the main diagonal; rows/cols never carry and anti = -main."""
    L = LINES[8]
    dd = [sum((M[i][j] >> k) & 1 for i, j in L) - 2 for k in range(4)]
    return (-dd[0] // 2, dd[2] + 2 * dd[3], dd[3])

# geometric slots: crossing angle -> which petals it sits between (from trefoil_view.py)
# petals: carry0 (1->2) at 270, carry1 (2->4) at 150, carry2 (4->8) at 30
slot_pair = {90: (1, 2), 210: (0, 1), 330: (0, 2)}
slot_direct = {90: 0, 330: 1, 210: 2}               # each carry -> the crossing opposite its petal
k_at = {ang: k for k, ang in enumerate(pos_deg)}

def diagram(M, mode, smoothing):
    a = carries(M)
    Xs, Ps = [], []
    for ang, k in k_at.items():
        if mode == "M1":
            i, j = slot_pair[ang]
            present = a[i] != 0 and a[j] != 0
            s = a[i] if present else 0
            assert not present or a[i] == a[j]       # forced: the two carries share a sign
        else:
            i = slot_direct[ang]
            present = a[i] != 0
            s = a[i]
        if present:
            Xs.append(crossing_X(k, over_for_sign(k, s))[0])
        else:
            (x1, x2, x3, x4), _ = crossing_X(k, 0)
            Ps += [(x1, x2), (x3, x4)] if smoothing == "A" else [(x1, x4), (x2, x3)]
    return Xs, Ps

squares = [tuple(map(tuple, s["square"])) for s in json.load(open("squares_4x4.json"))]
cache = {}
for mode in ("M1", "M2"):
    for smoothing in ("A", "B"):
        tally = Counter()
        for M in squares:
            a = carries(M)
            key = (mode, smoothing, a)
            if key not in cache:
                cache[key] = knot_type(*diagram(M, mode, smoothing))
            tally[cache[key]] += 1
        print(f"3. {mode}, absent crossings smoothed {smoothing}: {dict(tally)}")

# who knots, and with which hand
hand = Counter()
for M in squares:
    a = carries(M)
    if all(a):
        hand["right" if a[0] > 0 else "left"] += 1
assert sum(hand.values()) == 48
print(f"4. squares with all three crossings: {sum(hand.values())}, split {dict(hand)} (880 reps)")
def rot(M):
    return tuple(zip(*M[::-1]))
flip = all(carries(rot(M)) == tuple(-x for x in carries(M)) for M in squares)
print(f"   turning a square 90 deg flips every carry sign (mirror knot): {flip}")
assert flip
