"""
semimagic_test.py — kill test for "balance is what quantizes the residue."

Semi-magic squares: rows and columns sum to 30, diagonals free (partial lock).
Sample them, and compare residues with the fully locked magic squares and with random grids.
Residue (a): XOR of each line (which Dirac element it multiplies to).
Residue (b): Takemura degree (degree 3 <=> invertible, since row sums are constant).
"""
import itertools, random, math, json
from functools import reduce
from collections import Counter, defaultdict

random.seed(7)
quads = [q for q in itertools.combinations(range(16), 4) if sum(q) == 30]
def sample_semimagic():
    while True:
        rows, used = [], set()
        pool = quads[:]
        random.shuffle(pool)
        for q in pool:
            if not used & set(q):
                rows.append(q); used |= set(q)
                if len(rows) == 4:
                    break
        if len(rows) < 4:
            continue
        r0 = list(rows[0]); random.shuffle(r0)
        p1s = list(itertools.permutations(rows[1])); random.shuffle(p1s)
        for p1 in p1s:
            for p2 in itertools.permutations(rows[2]):
                need = [30 - r0[j] - p1[j] - p2[j] for j in range(4)]
                if sorted(need) == sorted(rows[3]):
                    M = [r0, list(p1), list(p2), need]
                    random.shuffle(M)
                    return M
LINES = [[(i, j) for j in range(4)] for i in range(4)] + [[(i, j) for i in range(4)] for j in range(4)] + \
        [[(i, i) for i in range(4)], [(i, 3 - i) for i in range(4)]]
perms = list(itertools.permutations(range(4)))
SG = [(-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) for p in perms]
def degree(M):
    c = defaultdict(int)
    for p, s in zip(perms, SG):
        c[sum(M[i][p[i]] for i in range(4))] += s
    if all(v == 0 for v in c.values()):
        return "inf"
    m = 0
    while sum(x * v ** m for v, x in c.items()) == 0:
        m += 1
    return str(m)
def entropy(cnt):
    n = sum(cnt.values())
    return -sum(v / n * math.log2(v / n) for v in cnt.values() if v)
def profile(sq):
    rc, dg, deg = Counter(), Counter(), Counter()
    for M in sq:
        for k, L in enumerate(LINES):
            x = reduce(lambda a, b: a ^ b, (M[i][j] for i, j in L))
            (rc if k < 8 else dg)[x] += 1
        deg[degree(M)] += 1
    n = len(sq)
    return (f"rows/cols {len(rc):2d} values {entropy(rc):.2f} bits | diagonals {len(dg):2d} values "
            f"{entropy(dg):.2f} bits | degree " + ", ".join(f"{k}: {100*v/n:.1f}%" for k, v in sorted(deg.items())))

semi = [sample_semimagic() for _ in range(20000)]
assert all(sum(r) == 30 for M in semi for r in M) and all(sum(c) == 30 for M in semi for c in zip(*M))
magic = [s["square"] for s in json.load(open("squares_4x4.json"))]
rand = []
for _ in range(20000):
    v = list(range(16)); random.shuffle(v); rand.append([v[4 * i:4 * i + 4] for i in range(4)])
print("random     ", profile(rand))
print("semi-magic ", profile(semi))
print("magic      ", profile(magic))
