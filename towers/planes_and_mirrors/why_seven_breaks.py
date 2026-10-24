"""
why_seven_breaks.py — why the 7 (the octonions' Fano plane) breaks at 16.
On n bits, an algebra with e_a e_b = +-e_(a xor b) and anticommuting imaginary units is fixed by one sign
per line (which way round each XOR-triple multiplies). On 4 bits there are 35 lines and 15 Fano planes
inside, and each line sits in 3 of those planes. Question: can the 35 signs be chosen so that every one
of the 15 planes is a working copy of the octonions?
"""
import itertools
import numpy as np
rng = np.random.default_rng(2)

def algebra(nbits, sign):
    """structure constants T[a,b] = (sign, a^b). sign: dict line(sorted triple) -> +1/-1 meaning e_a e_b = s e_c."""
    N = 2 ** nbits
    T = np.zeros((N, N, N))
    for a in range(N):
        for b in range(N):
            c = a ^ b
            if a == 0 or b == 0: s = 1
            elif a == b: s = -1
            else:
                line = tuple(sorted((a, b, c))); s0 = sign[line]
                x, y, z = line                       # e_x e_y = s0 e_z, cyclic: e_y e_z = s0 e_x, e_z e_x = s0 e_y
                cyc = {(x, y), (y, z), (z, x)}
                s = s0 if (a, b) in cyc else -s0
            T[a, b, c] = s
    return T
def prod(T, x, y): return np.einsum("abc,a,b->c", T, x, y)
def alternative(T, idx, trials=6):
    n = T.shape[0]
    for _ in range(trials):
        x = np.zeros(n); y = np.zeros(n); x[idx] = rng.normal(size=len(idx)); y[idx] = rng.normal(size=len(idx))
        if not np.allclose(prod(T, prod(T, x, x), y), prod(T, x, prod(T, x, y))): return False
    return True
def lines_of(points):
    return [t for t in itertools.combinations(sorted(points), 3) if t[0] ^ t[1] ^ t[2] == 0]

# --- one Fano plane: which of the 128 sign choices give the octonions?
L3 = lines_of(range(1, 8))
good3 = [bits for bits in itertools.product((1, -1), repeat=7)
         if alternative(algebra(3, dict(zip(L3, bits))), list(range(8)))]
print(f"Fano plane: {len(good3)} of 128 sign choices give the octonions")
gb = {tuple(int(b < 0) for b in g) for g in good3}
affine = all(tuple(p ^ q ^ r for p, q, r in zip(u, v, w)) in gb for u in gb for v in gb for w in gb)
print("   the good choices form an affine subspace over F2 (closed under u+v+w):", affine)

# --- 4 bits: 35 lines, 15 Fano planes
L4 = lines_of(range(1, 16))
planes = sorted({frozenset({a, b, c, a ^ b, a ^ c, b ^ c, a ^ b ^ c})
                 for a, b, c in itertools.combinations(range(1, 16), 3)
                 if len({a, b, c, a ^ b, a ^ c, b ^ c, a ^ b ^ c}) == 7}, key=sorted)
print(f"\n4 bits: {len(L4)} lines, {len(planes)} Fano planes, planes through each line:",
      {sum(set(l) <= P for P in planes) for l in L4})

def good_set_for(P):
    """sign patterns (on P's lines, in L4 order) that make the sub-plane P octonionic"""
    lp = [l for l in L4 if set(l) <= P]
    pts = sorted(P)
    out = set()
    for bits in itertools.product((1, -1), repeat=7):
        sign = dict(zip(lp, bits)); sign.update({l: 1 for l in L4 if l not in sign})
        T = algebra(4, sign)
        if alternative(T, [0] + pts): out.add(bits)
    return lp, out

# the sedenions (Cayley-Dickson) as a sign choice: read their signs off the table
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def cd(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([cd(a, c) - cd(conj(d), b), cd(d, a) + cd(b, conj(c))])
E = np.eye(16)
sed_sign = {l: int(round(cd(E[l[0]], E[l[1]])[l[2]])) for l in L4}
T_sed = algebra(4, sed_sign)
assert all(np.allclose(prod(T_sed, E[a], E[b]), cd(E[a], E[b])) for a in range(16) for b in range(16))
n_oct = sum(alternative(T_sed, [0] + sorted(P)) for P in planes)
print(f"   the sedenions' own signs: {n_oct} of 15 sub-planes are octonions, {15 - n_oct} are not")

# --- search: can all 15 planes be octonions at once? (backtracking over the 35 signs)
info = [good_set_for(P) for P in planes]
order = L4
assign = {}
plane_lines = [lp for lp, _ in info]
def ok_partial():
    for lp, gs in info:
        if all(l in assign for l in lp) and tuple(assign[l] for l in lp) not in gs: return False
    return True
best = [0]
def search(i):
    if i == len(order): return True
    for s in (1, -1):
        assign[order[i]] = s
        if ok_partial():
            done = sum(all(l in assign for l in lp) for lp in plane_lines); best[0] = max(best[0], done)
            if search(i + 1): return True
        del assign[order[i]]
    return False
found = search(0)
print("   a sign choice making all 15 sub-planes octonions exists:", found)

# --- how many can be octonions at once? (exact, by maximizing over all choices via the affine structure)
# brute force over the 2^35 choices is too big; use local search with restarts for a lower bound,
# then the backtracking above already proved 15 is impossible.
def score(sign):
    return sum(tuple(sign[l] for l in lp) in gs for lp, gs in info)
bestscore = 0
for _ in range(60):
    sign = {l: int(rng.choice((1, -1))) for l in L4}
    improved = True
    while improved:
        improved = False
        for l in L4:
            s0 = score(sign); sign[l] *= -1
            if score(sign) > s0: improved = True
            else: sign[l] *= -1
    bestscore = max(bestscore, score(sign))
print(f"   most sub-planes that local search could make octonions at once: {bestscore} of 15")

# --- exact: each plane's 16 good choices are an affine subspace, i.e. 3 parity equations on its 7 line signs.
idx = {l: i for i, l in enumerate(L4)}
def equations(lp, gs):
    pts = [np.array([int(b < 0) for b in g]) for g in gs]
    g0 = pts[0]; V = np.array([(p - g0) % 2 for p in pts])
    eqs = []
    for w in itertools.product((0, 1), repeat=7):
        w = np.array(w)
        if w.any() and not ((V @ w) % 2).any():
            mask = 0
            for k in range(7):
                if w[k]: mask |= 1 << idx[lp[k]]
            eqs.append((mask, int(w @ g0 % 2)))
    # keep an independent set of 3
    basis = []
    for m, r in eqs:
        if rank([e for e, _ in basis] + [m]) > len(basis): basis.append((m, r))
    return basis
def rank(masks):
    rows = list(masks); r = 0
    for bit in range(36):
        piv = next((i for i in range(r, len(rows)) if rows[i] >> bit & 1), None)
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i] >> bit & 1: rows[i] ^= rows[r]
        r += 1
    return r
def consistent(eqs):                       # augmented rank == rank
    A = [m for m, _ in eqs]; Ab = [m | (r << 35) for m, r in eqs]
    return rank(A) == rank(Ab)
plane_eqs = [equations(lp, gs) for lp, gs in info]
print(f"\nEach plane = {set(len(e) for e in plane_eqs)} parity equations; all 15 planes: "
      f"{sum(len(e) for e in plane_eqs)} equations on 35 signs, rank {rank([m for e in plane_eqs for m, _ in e])}")
mx, count = 0, 0
for S in range(1 << 15):
    k = bin(S).count("1")
    if k < mx: continue
    eqs = [q for i in range(15) if S >> i & 1 for q in plane_eqs[i]]
    if consistent(eqs):
        if k > mx: mx, count = k, 1
        elif k == mx: count += 1
print(f"Exact maximum number of sub-planes that can be octonions at once: {mx} (achieved by {count} plane sets)")

# smallest set of planes whose demands already contradict each other
for k in range(2, 16):
    hit = next((S for S in itertools.combinations(range(15), k)
                if not consistent([q for i in S for q in plane_eqs[i]])), None)
    if hit:
        pts = [sorted(planes[i]) for i in hit]
        common = set.intersection(*[set(p) for p in pts])
        print(f"Smallest contradiction: {k} planes, e.g. {pts}; points shared by all of them: {sorted(common)}")
        break
oct_planes = [sorted(P) for P in planes if alternative(T_sed, [0] + sorted(P))]
print("Sedenions' octonion sub-planes:", oct_planes)
print("   do they all avoid the new unit e8?", all(8 not in P for P in oct_planes))

# --- what do the 135 best plane sets look like?
from collections import Counter
shapes = Counter()
for S in range(1 << 15):
    if bin(S).count("1") != 8: continue
    if not consistent([q for i in range(15) if S >> i & 1 for q in plane_eqs[i]]): continue
    chosen = [planes[i] for i in range(15) if S >> i & 1]
    through = Counter(p for P in chosen for p in P)
    shapes[tuple(sorted(Counter(through.values()).items()))] += 1
for sh, n in shapes.items():
    print(f"   {n:3d} best sets; how many chosen planes pass through each point (count: points): {sh}")
