"""
code_lens.py — Test A of PREREG.md: the 880 magic squares read on the [[16,6,4]] tesseract code.

Qubits = the 16 values 0..15 (corners of the tesseract). Checks = RM(1,4) (affine hyperplanes).
An X- or Z-type operator on a corner set S commutes with every check  <=>  |S| even and XOR(S) = 0.
Logical coordinates: c_ab(S) = |S ∩ {v : v_a = v_b = 1}| mod 2 for the 6 pairs a < b.
"""
import json, itertools, os
from collections import Counter, defaultdict
from functools import reduce

HERE = os.path.dirname(os.path.abspath(__file__))
squares = [tuple(map(tuple, s["square"])) for s in json.load(open(os.path.join(HERE, "..", "squares_4x4.json")))]
assert len(squares) == 880

# ---------- the code
V = range(16)
dot = lambda w, v: bin(w & v).count("1") & 1
CHECKS = {frozenset()} | {frozenset(V)} | {frozenset(v for v in V if dot(w, v) == c) for w in range(1, 16) for c in (0, 1)}
assert len(CHECKS) == 32                                     # RM(1,4): 2^5 words
xor = lambda S: reduce(lambda a, b: a ^ b, S, 0)
commutes_with_checks = lambda S: len(S) % 2 == 0 and xor(S) == 0
PAIRS = list(itertools.combinations(range(4), 2))
Q = {p: frozenset(v for v in V if (v >> p[0]) & 1 and (v >> p[1]) & 1) for p in PAIRS}
coords = lambda S: tuple(len(set(S) & Q[p]) & 1 for p in PAIRS)
COMP = {p: tuple(sorted(set(range(4)) - set(p))) for p in PAIRS}
def pairing(S, T):                                           # predicted commutation from coordinates alone
    cs, ct = dict(zip(PAIRS, coords(S))), dict(zip(PAIRS, coords(T)))
    return sum(cs[p] * ct[COMP[p]] for p in PAIRS) & 1

# sanity: the 140 affine planes are exactly the weight-4 operators that commute with every check,
# and the coordinate pairing reproduces |S ∩ T| mod 2 on all of them
flats = [frozenset(S) for S in itertools.combinations(V, 4) if commutes_with_checks(S)]
assert len(flats) == 140
assert all(pairing(S, T) == len(S & T) % 2 for S in flats for T in flats)
assert len({coords(S) for S in flats}) == 35                 # 35 classes (the Klein quadric), 4 parallel planes each
print("code: 32 checks, 140 minimum-weight logicals in 35 classes; coordinate pairing = overlap parity (all 140^2)")

# ---------- existing classes (same definitions as triad_atlas.py)
perms = list(itertools.permutations(range(4)))
SG = [(-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) for p in perms]
def corner(M):
    d = [sum((M[i][i] >> k) & 1 for i in range(4)) - 2 for k in range(4)]
    a, c = -d[0] // 2, d[3]; b = d[2] + 2 * d[3]
    return "".join("1" if x else "0" for x in (c, b, a))
REGION = {"000": "center", "111": "center", "001": "petal", "010": "petal", "100": "petal",
          "011": "crossing", "110": "crossing", "101": "crossing"}
def degree(M):
    c = defaultdict(int)
    for p, s in zip(perms, SG): c[sum(M[i][p[i]] for i in range(4))] += s
    if all(v == 0 for v in c.values()): return "inf"
    m = 0
    while sum(x * v ** m for v, x in c.items()) == 0: m += 1
    return m
def geo(M):
    out, A = [], M
    for _ in range(4):
        A = tuple(zip(*A[::-1])); out += [A, tuple(r[::-1] for r in A)]
    return out
def pattern(M):
    def pp(G):
        pos = {G[i][j]: (i, j) for i in range(4) for j in range(4)}
        return tuple(sorted(tuple(sorted((pos[v], pos[15 - v]))) for v in range(8)))
    return min(pp(G) for G in geo(M))
def affine(M):
    S = [M[x >> 2][x & 3] for x in range(16)]
    return all(all(S[x ^ a] ^ S[x] == S[0] ^ S[a] for x in range(16)) for a in range(1, 16))
groups = defaultdict(list)
for M in squares: groups[pattern(M)].append(M)
gid = {}
for k, (pat, Ms) in enumerate(sorted(groups.items(), key=lambda kv: -len(kv[1]))):
    for M in Ms: gid[M] = f"D{k+1}({len(Ms)})"

# ---------- per-square readings
rows_of = lambda M: [frozenset(r) for r in M]
cols_of = lambda M: [frozenset(c) for c in zip(*M)]
diags_of = lambda M: [frozenset(M[i][i] for i in range(4)), frozenset(M[i][3 - i] for i in range(4))]
data = []
for M in squares:
    R, C, D = rows_of(M), cols_of(M), diags_of(M)
    rec = dict(M=M, region=REGION[corner(M)], group=gid[M], degree=str(degree(M)), affine=affine(M))
    # A1
    rec["A1"] = all(len(S) == 4 and commutes_with_checks(S) and S not in CHECKS for S in R + C)
    # A2: physical overlap 1 and the coordinate pairing both say anticommute
    rec["A2"] = all(len(r & c) == 1 and pairing(r, c) == 1 for r in R for c in C)
    # A3: c_ab(line) = 1  <=>  the line holds all four on/off combinations of bits a, b
    def full22(S, p): return len({((v >> p[0]) & 1, (v >> p[1]) & 1) for v in S}) == 4
    rec["A3"] = all(dict(zip(PAIRS, coords(S)))[p] == int(full22(S, p)) for S in R + C for p in PAIRS)
    # A4: even number of rows (and of columns) with a full 2x2, for every pair
    rec["A4"] = all(sum(coords(S)[k] for S in L) % 2 == 0 for L in (R, C) for k in range(6))
    # A5: diagonals on their own
    rec["diag_logical"] = sum(commutes_with_checks(S) for S in D)
    # A6: both diagonals together (corners + centre): always commuting; check or logical?
    both = D[0] | D[1]
    assert len(both) == 8 and commutes_with_checks(both)
    rec["diagpair"] = "check" if both in CHECKS else "logical"
    # A7: how many distinct logical classes among rows / columns
    rec["rowcls"] = len({coords(S) for S in R}); rec["colcls"] = len({coords(S) for S in C})
    # A8: pairs whose interaction is balanced in all 8 lines
    rec["bal_pairs"] = sum(all(coords(S)[k] for S in R + C) for k in range(6))
    data.append(rec)

def report(name, ok):
    print(f"{name}: {'HELD' if ok else 'LOST'}")
    return ok
results = {}
print("\n--- translation checks")
for t in ("A1", "A2", "A3", "A4"):
    results[t] = report(t, all(r[t] for r in data))

def lines_up(key):
    """is the property a function of some existing class? returns the classes it is a function of"""
    out = []
    for part in ("region", "group", "degree", "affine"):
        f = defaultdict(set)
        for r in data: f[r[part]].add(r[key])
        if all(len(s) == 1 for s in f.values()): out.append(part)
    return out
def crosstab(key, part):
    t = defaultdict(Counter)
    for r in data: t[r[part]][r[key]] += 1
    return {k: dict(v) for k, v in sorted(t.items(), key=lambda kv: str(kv[0]))}

print("\n--- real tests")
print("A5  diagonals that are logicals on their own (0, 1 or 2 per square):", dict(Counter(r["diag_logical"] for r in data)))
for part in ("region", "group", "degree", "affine"):
    print(f"     by {part:7s}", crosstab("diag_logical", part))
lu = lines_up("diag_logical"); print("     lines up with:", lu or "nothing")
results["A5"] = bool(lu) and len(set(r["diag_logical"] for r in data)) > 1

print("\nA6  both diagonals together:", dict(Counter(r["diagpair"] for r in data)))
for part in ("region", "group", "degree", "affine"):
    print(f"     by {part:7s}", crosstab("diagpair", part))
lu = lines_up("diagpair"); print("     lines up with:", lu or "nothing")
results["A6"] = bool(lu) and len(set(r["diagpair"] for r in data)) > 1

print("\nA7  (distinct row classes, distinct column classes):",
      dict(Counter((min(r["rowcls"], r["colcls"]), max(r["rowcls"], r["colcls"])) for r in data)))
par = [r for r in data if r["rowcls"] == 1 and r["colcls"] == 1]
print(f"     parallel rows and parallel columns: {len(par)} squares, of which affine: {sum(r['affine'] for r in par)};"
      f" affine squares overall: {sum(r['affine'] for r in data)}")
assert all(r["rowcls"] == 1 and r["colcls"] == 1 for r in data if r["affine"])      # forced direction
results["A7"] = any(not r["affine"] for r in par)
print("     non-affine squares with parallel rows and columns exist:", results["A7"])

mx = max(r["bal_pairs"] for r in data)
top = [r for r in data if r["bal_pairs"] == mx]
print(f"\nA8  most interactions balanced in all 8 lines: {mx} of 6, reached by {len(top)} squares,"
      f" of which affine: {sum(r['affine'] for r in top)}")
print("     distribution:", dict(sorted(Counter(r["bal_pairs"] for r in data).items())))
print("     by affine:", crosstab("bal_pairs", "affine"))
results["A8"] = mx == 4 and all(r["affine"] for r in top)

print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in results.items()})

# ---------- POST HOC (found after scoring; not predictions; asserted so they stay true)
print("\n--- post hoc (found after scoring, so not evidence for anything; fresh tests in order8_lens.py)")
dl = Counter((corner(r["M"]), r["diag_logical"]) for r in data)
assert all((c == "000") == (n == 2) for (c, n) in dl)
print("P1  each diagonal is a logical on its own  <=>  carry corner 000 (Fitting's 528)")
assert all(coords(diags_of(r["M"])[0]) == coords(diags_of(r["M"])[1]) for r in data if r["diag_logical"] == 2)
print("P2  in those 528 the two diagonals are parallel planes, so together they form a check")
cls2corner = defaultdict(set)
for r in data:
    D = diags_of(r["M"]); cls2corner[coords(D[0] | D[1])].add(corner(r["M"]))
assert all(len(s) == 1 for s in cls2corner.values())
print(f"P3  the diagonal pair's logical class ({len(cls2corner)} classes occur) determines the carry corner;"
      " the 48 trefoils (corner 111) all sit in class", [k for k, s in cls2corner.items() if s == {"111"}][0])
assert all((r["rowcls"] == 1 and r["colcls"] == 1) == r["affine"] for r in data)
print("P4  parallel rows and parallel columns <=> affine (A7's guess lost). Proof: rows = cosets of W_r and")
print("    columns = cosets of W_c with W_r ∩ W_c = 0, so value(i,j) = alpha(i) XOR beta(j) with alpha, beta")
print("    bijections of 4 things; every bijection of 4 things is affine (AGL(2,2) = S4, both of order 24).")
assert all(results[t] for t in ("A1", "A2", "A3", "A4")), "a translation check failed: the code or the derivation is wrong"
json.dump([{k: (v if k != "M" else [list(x) for x in v]) for k, v in r.items()} for r in data],
          open(os.path.join(HERE, "code_lens_data.json"), "w"))
