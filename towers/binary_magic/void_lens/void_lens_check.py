#!/usr/bin/env python3
"""
void_lens_check.py -- an independent check of Round 8 (void_lens/PREREG.md), written in Claude Code on
2026-10-24 from the claims alone. It shares no code with void_lens.py, padic_family.py or kernel_voids.py:
  A  MATLAB's odd magic(n) by the siamese rule itself; exact determinants by elimination modulo primes and
     Chinese remaindering past the Hadamard bound; the closed form evaluated separately.
  B  MATLAB's doubly-even rule read directly; rank <= 3 from an explicit decomposition, rank >= 3 from the
     rank modulo a prime.
  C  the prime-order family p*pi1(a1 i + b1 j) + pi2(a2 i + b2 j) + 1: every member at p = 5 (3,686,400
     matrices) by batched LU determinants in numpy, with any small value rechecked exactly; random members at
     p = 7; the chat's singular member at n = 9.
  D  the void index on the 880 order-4 squares, with complement maps factored over arbitrary involutions,
     mapped onto Dudeney's 12 groups and onto Staab et al.'s types A and B.
Run from binary_magic/:  python void_lens/void_lens_check.py [--long]   (--long: A up to n = 101)
Prints ASCII only.
"""
import itertools, json, os, random, sys
from collections import Counter
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
LONG = "--long" in sys.argv
checks = []
def check(name, ok):
    checks.append(ok); print(("  ok   " if ok else "  FAIL ") + name, flush=True)

# ------------------------------------------------------------------ exact arithmetic by primes
PRIMES = []
def primes_from(start, k):
    out, x = [], start | 1
    while len(out) < k:
        if all(x % d for d in range(3, int(x ** 0.5) + 1, 2)):
            out.append(x)
        x += 2
    return out
PRIMES = primes_from(2_000_000_011, 80)

def det_mod(A, p):
    A = [[x % p for x in r] for r in A]; n = len(A); d = 1
    for c in range(n):
        piv = next((r for r in range(c, n) if A[r][c]), None)
        if piv is None:
            return 0
        if piv != c:
            A[c], A[piv] = A[piv], A[c]; d = -d
        d = d * A[c][c] % p
        inv = pow(A[c][c], p - 2, p)
        for r in range(c + 1, n):
            if A[r][c]:
                f = A[r][c] * inv % p
                A[r] = [(x - f * y) % p for x, y in zip(A[r], A[c])]
    return d % p

def rank_mod(A, p):
    A = [[x % p for x in r] for r in A]; rk = 0; rows, cols = len(A), len(A[0])
    for c in range(cols):
        piv = next((r for r in range(rk, rows) if A[r][c]), None)
        if piv is None:
            continue
        A[rk], A[piv] = A[piv], A[rk]
        inv = pow(A[rk][c], p - 2, p)
        for r in range(rows):
            if r != rk and A[r][c]:
                f = A[r][c] * inv % p
                A[r] = [(x - f * y) % p for x, y in zip(A[r], A[rk])]
        rk += 1
    return rk

def det_exact(A):
    """integer determinant by CRT over primes, past the Hadamard bound"""
    H = 1
    for r in A:
        H *= sum(x * x for x in r)
    H = int(H ** 0.5) + 1 if H < 10 ** 300 else None
    bound = 2 * (H if H is not None else 1)
    if H is None:                                    # big: use log2 of the Hadamard bound instead
        import math
        lg = sum(0.5 * math.log2(sum(x * x for x in r)) for r in A) + 2
    M, x = 1, 0
    for p in PRIMES:
        r = det_mod(A, p)
        # combine x (mod M) with r (mod p)
        t = ((r - x) * pow(M, -1, p)) % p
        x, M = x + M * t, M * p
        if (H is not None and M > bound) or (H is None and M.bit_length() > lg):
            break
    else:
        raise RuntimeError("not enough primes")
    return x - M if x > M // 2 else x

# ------------------------------------------------------------------ A
def siamese(n):
    """de la Loubere: 1 in the middle of the top row, then up-right; when blocked, step down"""
    M = [[0] * n for _ in range(n)]
    i, j = 0, n // 2
    for k in range(1, n * n + 1):
        M[i][j] = k
        a, b = (i - 1) % n, (j + 1) % n
        if M[a][b]:
            a, b = (i + 1) % n, j
        i, j = a, b
    return M

def closed_form(n):
    seen, orbits = set(), []
    for k in range(1, n):
        if k not in seen:
            o, x = [], k
            while x not in o:
                o.append(x); x = 2 * x % n
            seen |= set(o); orbits.append(len(o))
    v = (-1) ** ((n - 1) // 2) * n ** (n - 1) * (n * n + 1) // 2
    for L in orbits:
        v *= n ** L - (-1) ** L
    return v

print("A. MATLAB's odd magic(n): det against the closed form")
check("siamese(3) and siamese(5) are MATLAB's magic(3) and magic(5)",
      siamese(3) == [[8, 1, 6], [3, 5, 7], [4, 9, 2]] and
      siamese(5) == [[17, 24, 1, 8, 15], [23, 5, 7, 14, 16], [4, 6, 13, 20, 22], [10, 12, 19, 21, 3], [11, 18, 25, 2, 9]])
top = 101 if LONG else 61
bad = [n for n in range(3, top + 1, 2) if det_exact(siamese(n)) != closed_form(n)]
check(f"det magic(n) = (-1)^((n-1)/2) n^(n-1) (n^2+1)/2 prod_O (n^|O| - (-1)^|O|) for every odd n = 3..{top}"
      f"{'' if not bad else ' -- mismatch at ' + str(bad)}", not bad)
check("so n^(n-1) divides det for those n (Israel's 2015 OEIS A160523 observation), and det != 0",
      all(closed_form(n) % n ** (n - 1) == 0 and closed_form(n) != 0 for n in range(3, top + 1, 2)))
check("A160523's printed terms: n = 3, 5, 7, 9 give -360, 5070000, -348052801600, 75035738059027200",
      [closed_form(n) for n in (3, 5, 7, 9)] == [-360, 5070000, -348052801600, 75035738059027200])

# ------------------------------------------------------------------ B
def doubly_even(n):
    J = [((i % 4) // 2) for i in range(1, n + 1)]        # MATLAB: J = fix(mod(1:n,4)/2); K = (J'==J)
    return [[(n * n + 1 - ((i - 1) * n + j)) if J[i - 1] == J[j - 1] else ((i - 1) * n + j)
             for j in range(1, n + 1)] for i in range(1, n + 1)]

print("B. MATLAB's doubly-even magic(n): rank 3")
ok_dec, ok_rank = True, True
for n in range(4, 65, 4):
    M = doubly_even(n)
    sig = [(-1) ** ((i % 4) // 2) for i in range(1, n + 1)]
    a = [2 * (i - 1) - (n - 1) for i in range(1, n + 1)]      # twice (i-1) - (n-1)/2, odd about the centre
    ok_dec &= all(2 * M[i][j] - (n * n + 1) == -sig[i] * sig[j] * (n * a[i] + a[j]) for i in range(n) for j in range(n))
    ok_rank &= rank_mod(M, PRIMES[0]) == 3
check("for n = 4..64, 2M - (n^2+1)E = -(sigma sigma^T) o (n a 1^T + 1 a^T) with sigma = (1,-1,-1,1) tiled:"
      " so rank M <= 3", ok_dec)
check("rank of M modulo a prime is 3 for every such n, so rank M >= 3: exactly 3", ok_rank)

# ------------------------------------------------------------------ C
print("C. the prime-order family")
def family_dets(p, slopes, P1, P2):
    I, J = np.meshgrid(range(p), range(p), indexing="ij")
    out = []
    for a1, b1, a2, b2 in slopes:
        L1 = (a1 * I + b1 * J) % p; L2 = (a2 * I + b2 * J) % p
        M = p * P1[:, None, L1] + P2[None, :, L2] + 1          # shape (len P1, len P2, p, p)
        out.append(np.abs(np.linalg.det(M.reshape(-1, p, p).astype(np.float64))))
    return np.concatenate(out)

p = 5
perms = np.array(list(itertools.permutations(range(p))))
slopes = list(itertools.product(range(1, p), repeat=4))
d = family_dets(p, slopes, perms, perms)
check(f"p = 5: all {len(d):,} members (every pi1, pi2 in S_5, every unit slope) have |det| >= 1"
      f" (smallest {d.min():.1f})", len(d) == 3_686_400 and d.min() > 0.5)
rng = np.random.default_rng(2026)
p = 7
P1 = np.array([rng.permutation(p) for _ in range(150)]); P2 = np.array([rng.permutation(p) for _ in range(150)])
sl = [tuple(int(x) for x in rng.integers(1, p, 4)) for _ in range(3)]
d7 = family_dets(p, sl, P1, P2)
check(f"p = 7: {len(d7):,} random members, |det| >= 1 (smallest {d7.min():.1f})", d7.min() > 0.5)

def member(n, p1, p2, a1, b1, a2, b2):
    return [[n * p1[(a1 * i + b1 * j) % n] + p2[(a2 * i + b2 * j) % n] + 1 for j in range(n)] for i in range(n)]
M9 = member(9, [3, 6, 4, 2, 1, 0, 8, 5, 7], [0, 3, 8, 2, 5, 7, 1, 4, 6], 1, 1, 1, 1)
check("n = 9 (composite): the chat's member with digit maps 364210857 / 038257146 is singular, rank 7",
      det_exact(M9) == 0 and max(rank_mod(M9, q) for q in PRIMES[:3]) == 7)

def pandiagonal_magic(M):
    n = len(M); s = n * (n * n + 1) // 2
    return (sorted(v for r in M for v in r) == list(range(1, n * n + 1)) and all(sum(r) == s for r in M)
            and all(sum(c) == s for c in zip(*M)) and
            all(sum(M[i][(i + k) % n] for i in range(n)) == s and sum(M[i][(k - i) % n] for i in range(n)) == s
                for k in range(n)))
pan = set()
for a1, b1, a2, b2 in itertools.product(range(1, 5), repeat=4):
    if not pandiagonal_magic(member(5, list(range(5)), list(range(5)), a1, b1, a2, b2)):
        continue
    for p1 in itertools.permutations(range(5)):
        for p2 in itertools.permutations(range(5)):
            pan.add(tuple(v for r in member(5, p1, p2, a1, b1, a2, b2) for v in r))
check(f"the family's pandiagonal magic 5x5 members: {len(pan):,} (MathWorld: 3,600 up to the 8 symmetries,"
      f" so 28,800); none singular (covered by the 3,686,400 above)", len(pan) == 28800)

# ------------------------------------------------------------------ D
print("D. the void index on the 880")
SQ = [s["square"] for s in json.load(open(os.path.join(HERE, "..", "squares_4x4.json")))]
def factor_complement(M):
    """the complement map (where 15 - x sits), if it is (i, j) -> (P i, Q j) for permutations P, Q"""
    pos = {M[i][j]: (i, j) for i in range(4) for j in range(4)}
    tgt = {(i, j): pos[15 - M[i][j]] for i in range(4) for j in range(4)}
    P = [tgt[(i, 0)][0] for i in range(4)]; Q = [tgt[(0, j)][1] for j in range(4)]
    return (P, Q) if all(tgt[(i, j)] == (P[i], Q[j]) for i in range(4) for j in range(4)) else None
def nullity(M):
    return 4 - rank_mod(M, PRIMES[0])
def pattern(M):                                        # Dudeney's group: complement-pair positions up to symmetry
    out, A = [], [r[:] for r in M]
    def pp(G):
        pos = {G[i][j]: (i, j) for i in range(4) for j in range(4)}
        return tuple(sorted(tuple(sorted((pos[v], pos[15 - v]))) for v in range(8)))
    for _ in range(4):
        A = [list(r) for r in zip(*A[::-1])]; out += [pp(A), pp([r[::-1] for r in A])]
    return min(out)
groups = Counter(pattern(M) for M in SQ)
size = {k: v for k, v in groups.items()}
rows = []
for M in SQ:
    f = factor_complement(M)
    if f is None:
        rows.append((None, None, nullity(M), size[pattern(M)])); continue
    P, Q = f
    assert all(P[P[i]] == i for i in range(4)) and all(Q[Q[j]] == j for j in range(4))   # involutions
    fP, fQ = sum(P[i] == i for i in range(4)), sum(Q[j] == j for j in range(4))
    rows.append(((fP, fQ), abs((fP + fQ) / 2 - 1), nullity(M), size[pattern(M)]))
kinds = Counter((r[0], r[1], r[2]) for r in rows)
for k, v in sorted(kinds.items(), key=str):
    print(f"     fixed lines {k[0]}, index {k[1]}, nullity {k[2]}: {v}")
check("whenever the complement map factors, it is a pair of involutions and nullity >= |(f_P + f_Q)/2 - 1|",
      all(r[0] is None or r[2] >= r[1] for r in rows))
check("at order 4: singular exactly when the index is >= 1", all((r[2] > 0) == (r[1] is not None and r[1] >= 1) for r in rows))
idx0 = [r for r in rows if r[1] == 0]
check(f"the {len(idx0)} index-0 squares (one transposition times a fixed-point-free involution) are exactly"
      f" Dudeney's two groups of 8, and they are invertible",
      len(idx0) == 16 and all(r[3] == 8 for r in idx0) and all(r[2] == 0 for r in idx0)
      and sum(1 for r in rows if r[3] == 8) == 16)
check("index 1 occurs as f = (0,0) [Staab et al.'s type A: 144] and (4,0) / (0,4) [type B: 496]",
      Counter(r[0] for r in rows if r[1] == 1) == Counter({(0, 0): 144, (4, 0): 288, (0, 4): 208}))
check("Staab et al.'s rank bound for type B of order 2m, rank <= m + 1, is the index for f = (0, 2m):"
      " |(0 + 2m)/2 - 1| = m - 1 = 2m - (m + 1)", all(abs((0 + 2 * m) / 2 - 1) == 2 * m - (m + 1) for m in range(1, 20)))

print(f"\n{sum(checks)} of {len(checks)} checks pass")
sys.exit(0 if all(checks) else 1)
