"""
trefoil_view.py — the carry cube seen down its body diagonal, laid on a trefoil.

Claim tested: looking down the cube's (1,1,1) axis,
  - 000 and 111 land on the same point (the center),
  - the three one-carry corners (001, 010, 100) form one triangle,
  - the three two-carry corners (011, 101, 110) form a second triangle, turned 60 degrees,
and a standard trefoil diagram has the same layout: 3 lobes (petals), 3 crossings
sitting 60 degrees between them, one central region.
So petals <-> one-carry corners, crossings <-> two-carry corners, center <-> 000/111.

Then: are the counts trefoil-symmetric (unchanged by a 120-degree turn)?
Needs squares_4x4.json from binary_magic.py.
"""
import json, math
import numpy as np
from collections import Counter, defaultdict

# ---------- 1. the cube down its diagonal ----------
n = np.array([1, 1, 1]) / math.sqrt(3)
u = np.array([1, -1, 0]) / math.sqrt(2)
w = np.cross(n, u)
def proj(bits):
    p = np.array(bits, float) - 0.5
    return np.array([p @ u, p @ w])
corners = {format(k, "03b"): proj([int(b) for b in format(k, "03b")]) for k in range(8)}
ang = {c: math.degrees(math.atan2(p[1], p[0])) % 360 for c, p in corners.items() if np.linalg.norm(p) > 1e-9}
center = [c for c, p in corners.items() if np.linalg.norm(p) < 1e-9]
assert center == ["000", "111"]
one = sorted(ang[c] for c in ("001", "010", "100"))
two = sorted(ang[c] for c in ("011", "101", "110"))
gaps1 = [round((one[(i + 1) % 3] - one[i]) % 360, 6) for i in range(3)]
offset = min(abs((a - b + 180) % 360 - 180) for a in one for b in two)
assert gaps1 == [120, 120, 120] and round(offset, 6) == 60
print("1. Down the diagonal: 000 and 111 coincide at the center;")
print("   one-carry corners at", [round(a) for a in one], "deg; two-carry corners at",
      [round(a) for a in two], "deg (offset 60)")

# ---------- 2. the trefoil diagram has the same layout ----------
t = np.linspace(0, 2 * math.pi, 20000, endpoint=False)
x = np.sin(t) + 2 * np.sin(2 * t)
y = np.cos(t) - 2 * np.cos(2 * t)
r = np.hypot(x, y)
# lobe tips: local maxima of radius
tips = [math.degrees(math.atan2(y[i], x[i])) % 360 for i in range(len(t))
        if r[i] > r[i - 1] and r[i] >= r[(i + 1) % len(t)]]
# crossings: pairs of far-apart parameters that land on the same point
pts = np.stack([x, y], 1)
cross = []
step = 40
for i in range(0, len(t), step):
    d = np.linalg.norm(pts - pts[i], axis=1)
    gap = np.minimum(np.abs(np.arange(len(t)) - i), len(t) - np.abs(np.arange(len(t)) - i))
    d[gap < 2000] = np.inf
    j = int(np.argmin(d))
    if d[j] < 0.02:
        a = math.degrees(math.atan2(pts[i][1], pts[i][0])) % 360
        if all(abs((a - b + 180) % 360 - 180) > 10 for b in cross):
            cross.append(a)
tips, cross = sorted(tips), sorted(cross)
assert len(tips) == 3 and len(cross) == 3
off = min(abs((a - b + 180) % 360 - 180) for a in tips for b in cross)
print(f"2. Trefoil: lobe tips at {[round(a) for a in tips]} deg, crossings at "
      f"{[round(a) for a in cross]} deg -> offset {off:.0f} deg. Same layout.")
assert abs(off - 60) < 1.5

# ---------- 3. carry counts on that picture ----------
S = 30
LINES = [[(i, j) for j in range(4)] for i in range(4)] + \
        [[(i, j) for i in range(4)] for j in range(4)] + \
        [[(i, i) for i in range(4)], [(i, 3 - i) for i in range(4)]]
squares = [tuple(map(tuple, s["square"])) for s in json.load(open("squares_4x4.json"))]
def corner_of(M):
    U = set()
    for L in LINES:
        d = [sum((M[i][j] >> k) & 1 for i, j in L) - 2 for k in range(4)]
        a, c = -d[0] // 2, d[3]
        b = d[2] + 2 * d[3]
        U |= {k for k, v in enumerate((a, b, c)) if v}
    return "".join("1" if k in U else "0" for k in (2, 1, 0))
def geo(M):
    out, A = [], M
    for _ in range(4):
        A = tuple(zip(*A[::-1])); out += [A, tuple(r[::-1] for r in A)]
    return out
def pattern_canon(M):
    def pp(G):
        pos = {G[i][j]: (i, j) for i in range(4) for j in range(4)}
        return tuple(sorted(tuple(sorted((pos[v], pos[15 - v]))) for v in range(8)))
    return min(pp(G) for G in geo(M))

cnt = Counter(corner_of(M) for M in squares)
def region_line(c):
    return (f"petals  001/010/100 = {c['001']}/{c['010']}/{c['100']}   "
            f"crossings 011/101/110 = {c['011']}/{c['101']}/{c['110']}   "
            f"center 000 + 111 = {c['000']} + {c['111']}")
print("3. All 880:", region_line(cnt))
groups = defaultdict(list)
for M in squares:
    groups[pattern_canon(M)].append(M)
for key, sq in sorted(groups.items(), key=lambda kv: -len(kv[1])):
    print(f"   group {len(sq):3d}:", region_line(Counter(corner_of(M) for M in sq)))

# ---------- 4. is the picture trefoil-symmetric? ----------
# A 120-degree turn about the diagonal cycles the three carries: 001 -> 010 -> 100 -> 001.
def turn(c):
    return c[1:] + c[0]
petals_sym = cnt["001"] == cnt["010"] == cnt["100"]
cross_sym = cnt["011"] == cnt["101"] == cnt["110"]
print(f"4. 120-degree turn: petals symmetric = {petals_sym}; crossings symmetric = {cross_sym}")
assert petals_sym and not cross_sym and cnt["101"] == 0
print("   The empty crossing is 101: carries 1->2 and 4->8, which never touch on the chain 1-2-4-8.")
print("   Closing it would need a carry 8 -> 1 (two 8s = 16, not 1). It closes only mod 15.")
