"""Independent audit check for J14 (the operation CL_N on Z/N and its
non-associativity rate).  Fresh, vectorised code; exact integer counts.

CL_N(a,b) = N-1 if a or b is N-1; else 0 if a or b is 0;
            else a+b if a+b = ab (mod N); else N-1.

Run:  python -I check_j14.py
"""
from math import gcd
import sys
import time

import numpy as np

T0 = time.time()
FAIL = []


def check(label, ok):
    print(("  [ok]   " if ok else "  [FAIL] ") + label)
    if not ok:
        FAIL.append(label)


def factor(n):
    f, p, m = {}, 2, n
    while p * p <= m:
        while m % p == 0:
            f[p] = f.get(p, 0) + 1
            m //= p
        p += 1
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f


def sqf(n):
    return all(e == 1 for e in factor(n).values())


def phi(n):
    r = n
    for p in factor(n):
        r -= r // p
    return r


def table(N):
    a = np.arange(N)[:, None]
    b = np.arange(N)[None, :]
    s = (a + b) % N
    echo = s == (a * b) % N
    T = np.where(echo, s, N - 1)
    T = np.where((a == 0) | (b == 0), 0, T)
    T = np.where((a == N - 1) | (b == N - 1), N - 1, T)
    return T.astype(np.int64)


def nonassoc(N, split=False):
    """Exact count of (a,b,c) with T[T[a,b],c] != T[a,T[b,c]]; optionally by case."""
    T = table(N)
    TBC = T                      # T[b, c]
    tot = 0
    case1 = case2 = case3 = 0
    cidx = np.arange(N)
    for a in range(N):
        left = T[T[a, :][:, None], cidx[None, :]]      # T[T[a,b], c]
        right = T[a, TBC]                               # T[a, T[b,c]]
        bad = left != right
        cnt = int(bad.sum())
        tot += cnt
        if split:
            if a == 0:
                case1 += cnt
            else:
                c0 = int(bad[:, 0].sum())
                case2 += c0
                case3 += cnt - c0
    return (tot, case1, case2, case3) if split else tot


print("=" * 72)
print("J14 claims on CL_N")
print("=" * 72)
# 1. The 'Echo lemma': a+b = ab has phi(N) solutions -- for EVERY N, not only squarefree
ok = all(sum(1 for a in range(N) for b in range(N) if (a + b - a * b) % N == 0) == phi(N)
         for N in range(2, 201))
check("#{(a,b): a+b = ab mod N} = phi(N) for EVERY N in [2,200] (squarefree not needed)", ok)

# 2. The paper's table at N = 10, 30, 210 (Case 1 / Case 2 / Case 3)
want = {10: (128, 61, 61, 6), 30: (1560, 777, 777, 6), 210: (86464, 43217, 43217, 30)}
for N, w in want.items():
    got = nonassoc(N, split=True)
    check(f"N={N}: (total, case1, case2, case3) = {got} (paper: {w})", got == w)

# 3. sigma(N) < 2/N and the two-sided bound for squarefree N in [3, 400]
worst = 0.0
ok_up = ok_two = True
vals = {}
for N in range(3, 401):
    if not sqf(N):
        continue
    t = nonassoc(N)
    vals[N] = t
    ok_up &= t < 2 * N * N
    lo, hi = 2 * (N - 2) ** 2 - 2 * phi(N), 2 * (N - 2) ** 2 + 2 * phi(N)
    ok_two &= lo <= t <= hi
    worst = max(worst, t / N ** 2)
check(f"squarefree 3 <= N <= 400: count < 2N^2 (i.e. N*sigma < 2); max N*sigma = {worst:.4f}", ok_up)
check("squarefree 3 <= N <= 400: 2(N-2)^2 - 2phi <= count <= 2(N-2)^2 + 2phi", ok_two)

# 4. The 'broader test set' in Sec. 5: N*sigma <= 1.993
big = [10, 30, 42, 66, 105, 110, 154, 210, 330, 462, 770, 1155]
ns = {}
for N in big:
    t = vals.get(N) if N in vals else nonassoc(N)
    ns[N] = t / N ** 2
mx = max(ns.values())
print("  N*sigma on the paper's broader set:", {k: round(v, 4) for k, v in ns.items()})
check(f"paper: N*sigma <= 1.993 on that set; actual max = {mx:.4f}", mx <= 1.993)

# 5. Non-squarefree N = 2^k: the paper's table and the failure at 64
pw = {2 ** k: nonassoc(2 ** k) / 4 ** k for k in range(1, 8)}
print("  N*sigma at N = 2^k:", {k: round(v, 3) for k, v in pw.items()})
check("N=64 and N=128 exceed N*sigma = 2 (bound genuinely needs squarefree N)",
      pw[64] > 2 and pw[128] > 2)
# where the excess comes from: case 3 (a, c != 0) at N=64 vs 2 phi(N)
t64 = nonassoc(64, split=True)
check(f"N=64: case-3 count {t64[3]} > 2*phi(64) = {2 * phi(64)} -- the step 'a^2 = 0 forces a = 0' "
      "is what fails off squarefree N", t64[3] > 2 * phi(64))

# 6. E(N): echo pairs inside {1..N-2}^2 -- closed form phi(N) - #({-1,-2,-1/2} & units)
ok_E = True
for N in range(3, 301):
    if not sqf(N):
        continue
    E = sum(1 for b in range(1, N - 1) for c in range(1, N - 1) if ((b - 1) * (c - 1)) % N == 1 % N)
    excl = {(-1) % N}
    if N % 2 == 1:
        excl |= {(-2) % N, (-pow(2, -1, N)) % N}
    excl = {u for u in excl if gcd(u, N) == 1}
    ok_E &= E == phi(N) - len(excl)
check("E(N) = phi(N) - #({-1, -2, -1/2} among the units), squarefree N <= 300 (exact, sharper "
      "than the paper's E <= phi)", ok_E)

# 7. Lemma E_h: #roots of b^2+b-1 mod N equals the Legendre product (independent recount)
ok_h = True
for N in range(3, 301):
    if not sqf(N):
        continue
    direct = sum(1 for b in range(1, N - 1) for c in range(1, N - 1)
                 if ((b - 1) * (c - 1)) % N == 1 and (b + c) % N == N - 1)
    prod = 1
    for p in factor(N):
        prod *= sum(1 for x in range(p) if (x * x + x - 1) % p == 0)
    ok_h &= direct == prod
check("E_h(N) = prod over p | N of #roots of x^2+x-1 mod p (squarefree N <= 300)", ok_h)

# 8. The companion F6 note says the DIS=0 count at primorials N = 2, 6, 30, 210 is N; it is phi(N)
cnt = {N: sum(1 for a in range(N) for b in range(N) if (a + b - a * b) % N == 0) for N in (2, 6, 30, 210)}
check(f"F6 note's 'DIS=0 count = N at primorials' is wrong: actual {cnt} = phi(N)",
      all(cnt[N] == phi(N) for N in cnt) and any(cnt[N] != N for N in cnt))

print("=" * 72)
print(f"elapsed {time.time() - T0:.1f} s ; failures: {len(FAIL)}")
for f_ in FAIL:
    print("  FAILED:", f_)
sys.exit(1 if FAIL else 0)
