#!/usr/bin/env python3
"""
void_fold.py -- Round 7 (code_lens/PREREG.md): the fold through the void at 7.5.

Run from binary_magic/:  python3 code_lens/void_fold.py

The value 7.5 is held by no cell, yet every fold is a reflection measured from it:
  b = 1111: n -> 15 - n, the point reflection through 7.5 itself;
  b weight 3, kept bit k: n -> (15 - 2^k + 2^(k+1) n_k) - n, a reflection through 7.5 -+ 2^(k-1).
Walsh columns: chi_00 = (1,1,1,1), chi_01 = (1,-1,1,-1), chi_10 = (1,1,-1,-1), chi_11 = (1,-1,-1,1).
The mirror j -> 3-j fixes chi_00 and chi_11 and negates chi_01, chi_10.
Prints ASCII only.
"""
import itertools, json, os, sys
from collections import Counter, defaultdict
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
squares = [tuple(map(tuple, s["square"])) for s in json.load(open(os.path.join(HERE, "..", "squares_4x4.json")))]
assert len(squares) == 880

CHI = {"00": (1, 1, 1, 1), "01": (1, -1, 1, -1), "10": (1, 1, -1, -1), "11": (1, -1, -1, 1)}
NZ = ["01", "10", "11"]

def det(A):                                   # exact Laplace expansion, fine for 4x4 / 3x3 / 2x2
    n = len(A)
    if n == 1: return A[0][0]
    return sum((-1) ** j * A[0][j] * det([r[:j] + r[j + 1:] for r in A[1:]]) for j in range(n))

def v2(x):
    x = abs(x); k = 0
    while x % 2 == 0: x //= 2; k += 1
    return k

def matvec(M, v): return tuple(sum(M[i][j] * v[j] for j in range(4)) for i in range(4))
def vecmat(v, M): return tuple(sum(v[i] * M[i][j] for i in range(4)) for j in range(4))
def T(M): return tuple(zip(*M))

def folds(M):
    """(direction, mask) for every cell-address translation a in {0011 (LR), 1100 (TB)} that is an XOR symmetry."""
    S = [M[x >> 2][x & 3] for x in range(16)]
    out = []
    for a, d in ((0b0011, "LR"), (0b1100, "TB")):
        b = S[0] ^ S[a]
        if all(S[x ^ a] ^ S[x] == b for x in range(16)):
            out.append((d, b))
    return out

def corner(M):                                # identical to code_lens.py
    d = [sum((M[i][i] >> k) & 1 for i in range(4)) - 2 for k in range(4)]
    a, c = -d[0] // 2, d[3]; b = d[2] + 2 * d[3]
    return "".join("1" if x else "0" for x in (c, b, a))

def affine(M):
    S = [M[x >> 2][x & 3] for x in range(16)]
    return all(all(S[x ^ a] ^ S[x] == S[0] ^ S[a] for x in range(16)) for a in range(1, 16))

def walsh_block(M):
    """W[r][c] = sum_ij M_ij chi_r(i) chi_c(j) for r, c in NZ (the 3x3 block; row/col 00 is fixed by the sums)."""
    return [[sum(M[i][j] * CHI[r][i] * CHI[c][j] for i in range(4) for j in range(4)) for c in NZ] for r in NZ]

res = {}
weights = Counter(); both = 0; v1_ok = v2_ok = True
val_by_k = defaultdict(Counter); v6_bad = []; det_by_kind = defaultdict(Counter)
corners = Counter(); n_aff = 0; sing_iff_comp = True; det_identity = True

for M in squares:
    D = det([list(r) for r in M])
    W = walsh_block(M)
    # det M = 120 * det(W) / 256  (H^T M H = diag(120, W) for the full Walsh matrix H, det H = 16)
    if Fraction(120 * det(W), 256) != D: det_identity = False
    fs = folds(M)
    assert fs, "every square folds (atlas row: Proved, given Nimm0)"
    kinds = set()
    for d, b in fs:
        w = bin(b).count("1"); weights[w] += 1
        X = M if d == "LR" else T(M)          # reduce TB to LR by transposing
        img = matvec(X, CHI["11"])
        if w == 4:
            kinds.add("comp")
            if any(img): v1_ok = False
        elif w == 3:
            kinds.add("3bit")
            k = [m for m in range(4) if not (b >> m) & 1][0]
            sig = [x // 2 ** (k + 1) for x in img]
            if [x % 2 ** (k + 1) for x in img] != [0] * 4 or sorted(sig) != [-1, -1, 1, 1]:
                v2_ok = False
            r_star = [r for r in NZ if abs(sum(s * c for s, c in zip(sig, CHI[r]))) == 4]
            if len(r_star) != 1: v2_ok = False
            if D:
                val_by_k[k][v2(D)] += 1
                # V6: lowest flipped plane's 2x2 minor (rows != r*, columns 01, 10), halved
                m0 = min(m for m in range(4) if m != k)
                B = [[(X[i][j] >> m0) & 1 for j in range(4)] for i in range(4)]
                Wm = walsh_block(tuple(tuple(1 - 2 * B[i][j] for j in range(4)) for i in range(4)))
                rows_left = [NZ.index(r) for r in NZ if r != r_star[0]]
                minor = [[Wm[i][0], Wm[i][1]] for i in rows_left]
                ent = [x for row in minor for x in row]
                # W(F_m) = 4 * (Walsh of the row-sign vectors), and those are 0, +-2, +-4; "halved" in the
                # registration means det(minor / 8) odd.
                assert all(x % 8 == 0 for x in ent)
                dq = det([[x // 8 for x in row] for row in minor])
                if dq % 2 == 0: v6_bad.append((M, k, m0, minor))
    if "comp" in kinds and "3bit" in kinds: both += 1
    det_by_kind["comp" if "comp" in kinds else "3bit"][D != 0] += 1
    corners[corner(M)] += 1
    n_aff += affine(M)
    if (D == 0) != ("comp" in kinds): sing_iff_comp = False

print("ROUND 7: the fold through the void at 7.5")
print("  identity det M = 120 det(W')/256 on all 880:", det_identity)
print("  fold masks by weight (over all folds found):", dict(sorted(weights.items())))
print("  squares with both a complement and a 3-bit fold:", both)
print("  complement-fold squares (invertible?):", dict(det_by_kind["comp"]),
      "  3-bit-only squares (invertible?):", dict(det_by_kind["3bit"]))
print("  v2(det) by kept bit k (3-bit folds of invertible squares):",
      {k: dict(c) for k, c in sorted(val_by_k.items())})
print("  V6 failures (lowest flipped plane's minor even):", len(v6_bad))
print("  carry corners:", dict(sorted(corners.items())), " affine:", n_aff)

res["V1"] = v1_ok
res["V2"] = v2_ok
res["V3"] = set(weights) <= {3, 4}
res["V4"] = both == 0
res["V5"] = all(len(c) == 1 for c in val_by_k.values())
res["V6"] = not v6_bad
want = {"000": 528, "001": 64, "010": 64, "100": 64, "011": 56, "110": 56, "111": 48}
res["V7"] = (dict(corners) == want and n_aff == 432 and sing_iff_comp and det_identity)
print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
if v6_bad:
    M, k, m0, minor = v6_bad[0]
    print("  first V6 failure: k =", k, "m0 =", m0, "minor =", minor)
    print("  square:", [list(r) for r in M])

# ---------------- Round 7b: complement symmetry over every XOR translation of the cell address ----------------
RB = {"01": 1, "10": 2, "11": 3}
def chi(r, a): return -1 if bin(RB[r] & a).count("1") % 2 else 1

def symmetries(M):
    S = [M[x >> 2][x & 3] for x in range(16)]
    return [(a, S[0] ^ S[a]) for a in range(1, 16) if all(S[x ^ a] ^ S[x] == S[0] ^ S[a] for x in range(16))]

r7b = {"V7b": True, "V8": True, "V9": True, "V10": True}
w2_on = Counter(); inv_masks = Counter(); certs = Counter(); cert_planes = Counter()
for M in squares:
    D = det([list(r) for r in M]); W = walsh_block(M); sy = symmetries(M)
    comp = [(a, b) for a, b in sy if b == 15]
    if (D == 0) != bool(comp): r7b["V7b"] = False
    for a, _ in comp:
        ar, ac = a >> 2, a & 3
        Z = [(i, j) for i, r in enumerate(NZ) for j, c in enumerate(NZ) if chi(r, ar) * chi(c, ac) == 1]
        if any(W[i][j] for i, j in Z): r7b["V8"] = False
        if ar == 0:
            c0 = [c for c in NZ if chi(c, ac) == 1][0]
            if any(matvec(M, CHI[c0])): r7b["V8"] = False
        elif ac == 0:
            r0 = [r for r in NZ if chi(r, ar) == 1][0]
            if any(vecmat(CHI[r0], M)): r7b["V8"] = False
        else:
            r0 = [r for r in NZ if chi(r, ar) == 1][0]
            c1, c2 = [c for c in NZ if chi(c, ac) == -1]
            x, y = W[NZ.index(r0)][NZ.index(c1)], W[NZ.index(r0)][NZ.index(c2)]
            v = CHI[c1] if (x, y) == (0, 0) else tuple(y * p - x * q for p, q in zip(CHI[c1], CHI[c2]))
            if any(matvec(M, v)): r7b["V8"] = False
    for d, b in folds(M):
        if bin(b).count("1") == 2:
            w2_on["singular" if D == 0 else "invertible"] += 1
    if D:
        for a, b in sy:
            inv_masks[bin(b).count("1")] += 1
        if any(bin(b).count("1") != 3 for a, b in sy): r7b["V10"] = False
        # V11 (exploratory): which flipped planes certify det != 0 by the mod-2 minor test
        d, b = next((d, b) for d, b in folds(M) if bin(b).count("1") == 3)
        X = M if d == "LR" else T(M)
        k = [m for m in range(4) if not (b >> m) & 1][0]
        sig = [x // 2 ** (k + 1) for x in matvec(X, CHI["11"])]
        rs = [r for r in NZ if abs(sum(s * c for s, c in zip(sig, CHI[r]))) == 4][0]
        rows_left = [NZ.index(r) for r in NZ if r != rs]
        good = []
        for m in range(4):
            if m == k: continue
            B = [[(X[i][j] >> m) & 1 for j in range(4)] for i in range(4)]
            Wm = walsh_block(tuple(tuple(1 - 2 * B[i][j] for j in range(4)) for i in range(4)))
            if det([[Wm[i][0] // 8, Wm[i][1] // 8] for i in rows_left]) % 2: good.append(m)
        certs[len(good)] += 1
        for m in good: cert_planes[(k, m)] += 1
if w2_on["invertible"]: r7b["V9"] = False

print("\nROUND 7b: complement symmetry over all 15 translations")
print("  weight-2 mirror folds by square type:", dict(w2_on))
print("  masks of all XOR symmetries on invertible squares, by weight:", dict(inv_masks))
print("  V11 (exploratory): invertible squares by number of single planes that certify mod 2:", dict(certs))
print("                     (kept bit k, certifying plane m):", dict(sorted(cert_planes.items())))
print("SCORE:", {k: ("HELD" if v else "LOST") for k, v in r7b.items()})
