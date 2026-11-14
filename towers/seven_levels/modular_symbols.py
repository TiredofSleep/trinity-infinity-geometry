"""Modular symbols of weight k for Gamma0(N): the plus quotient, Hecke operators by Merel's Heilbronn matrices, and
the Hecke eigensystems with integer eigenvalues in the cuspidal range (the rational newforms and their old copies).

Written for the fifth moments (TORUS_MOMENTS.md, section 8), to name the modular forms that appear there, after
LMFDB's web interface answered a burst of queries with a captcha.  Linear algebra is done modulo a prime P ~ 2^26,
and every eigenvalue is read back as the integer of least absolute value; an eigenvector is kept only if all its
a(p) satisfy Deligne's bound |a(p)| <= 2 p^((k-1)/2).

Conventions (as in W. Stein, "Modular Forms: A Computational Approach", AMS 2007, chapter 8, and Sage):
Manin symbols [X^i Y^(w-i), (c:d)] with w = k - 2, (c:d) in P^1(Z/NZ); the right action
[P, x] g = [P(aX + bY, cX + dY), (c, d) g]; the relations x + x S = 0 and x + x T + x T^2 = 0, and the plus quotient
x = x J, with S = [[0,-1],[1,0]], T = [[0,-1],[1,-1]], J = [[-1,0],[0,1]].
Merel's theorem: T_n [P, x] = sum of [P|h, x h] over the h = [[a,b],[c,d]] with ad - bc = n, a > b >= 0, d > c >= 0.

Self-test (python modular_symbols.py): the weight-4 newforms of levels 5, 6, 8 and 9 come out equal to the eta
products eta(t)^4 eta(5t)^4, (eta(t)eta(2t)eta(3t)eta(6t))^2, eta(2t)^4 eta(4t)^4 and eta(3t)^8."""
from math import gcd, comb
import numpy as np
import sympy

P = int(sympy.prevprime(2 ** 26))


def inv(x):
    return pow(int(x) % P, P - 2, P)


def p1(N):
    units = [u for u in range(1, N) if gcd(u, N) == 1] if N > 1 else [0]
    idx = -np.ones((N, N), dtype=np.int64)
    reps = []
    for c in range(N):
        for d in range(N):
            if idx[c, d] >= 0 or gcd(gcd(c, d), N) != 1:
                continue
            k = len(reps)
            reps.append((c, d))
            for u in units:
                idx[u * c % N, u * d % N] = k
    return reps, idx


def act_poly(w, a, b, c, d):
    """matrix A[i][j]: X^i Y^(w-i) |g  =  sum_j A[i][j] X^j Y^(w-j)  with (aX + bY)^i (cX + dY)^(w-i)"""
    A = [[0] * (w + 1) for _ in range(w + 1)]
    for i in range(w + 1):
        # (aX + bY)^i = sum_r C(i,r) a^r b^(i-r) X^r Y^(i-r);  (cX + dY)^(w-i) = sum_s C(w-i,s) c^s d^(w-i-s) X^s Y^(..)
        for r in range(i + 1):
            for s in range(w - i + 1):
                A[i][r + s] += comb(i, r) * a ** r * b ** (i - r) * comb(w - i, s) * c ** s * d ** (w - i - s)
    return A


_HCACHE = {}


def heilbronn(n):
    """Merel's set: ad - bc = n, a > b >= 0, d > c >= 0  (enumerated over (a, b), then d in a short range)"""
    if n in _HCACHE:
        return _HCACHE[n]
    out = []
    for a in range(1, n + 1):
        if n % a == 0:
            d = n // a
            for c in range(d):
                out.append((a, 0, c, d))
        for b in range(1, a):
            lo = -(-n // a)                      # ad >= n
            hi = -(-n // (a - b)) - 1            # d (a - b) < n
            for d in range(lo, hi + 1):
                r = a * d - n
                if r % b == 0:
                    c = r // b
                    if 0 <= c < d:
                        out.append((a, b, c, d))
    _HCACHE[n] = out
    return out


class Space:
    def __init__(self, N, k=4):
        self.N, self.k, self.w = N, k, k - 2
        w = self.w
        self.reps, self.idx = p1(N)
        M = self.M = len(self.reps)
        n = self.n = (w + 1) * M
        sym = lambda i, x: i * M + x
        # union-find with signs for the two-term relations
        parent = list(range(n)); sign = [1] * n; zero = [False] * n

        def find(s):
            sg = 1
            while parent[s] != s:
                sg *= sign[s]; s = parent[s]
            return s, sg

        def union(s1, s2, sg):            # s1 = sg * s2
            r1, g1 = find(s1); r2, g2 = find(s2)
            rel = g1 * sg * g2            # r1 = rel * r2
            if r1 == r2:
                if rel != 1:
                    zero[r1] = True
                return
            parent[r1] = r2; sign[r1] = rel
            if zero[r1]:
                zero[r2] = True

        N_ = N
        for x, (c, d) in enumerate(self.reps):
            xS = self.idx[d % N_, (-c) % N_]
            xJ = self.idx[(-c) % N_, d % N_]
            for i in range(w + 1):
                union(sym(i, x), sym(w - i, xS), -((-1) ** i))
                union(sym(i, x), sym(i, xJ), (-1) ** i)
        roots = {}
        self.gen = [None] * n            # (generator index, sign) or None
        for s in range(n):
            r, g = find(s)
            if zero[r]:
                continue
            if r not in roots:
                roots[r] = len(roots)
            self.gen[s] = (roots[r], g)
        G = self.G = len(roots)
        # three-term relations
        AT = act_poly(w, 0, -1, 1, -1)
        AT2 = act_poly(w, -1, 1, -1, 0)
        rows = []
        seen = set()
        for x, (c, d) in enumerate(self.reps):
            xT = self.idx[d % N_, (-c - d) % N_]
            xT2 = self.idx[(-c - d) % N_, c % N_]
            for i in range(w + 1):
                row = {}
                for s, cf in [(sym(i, x), 1)] + [(sym(j, xT), AT[i][j]) for j in range(w + 1)] + \
                             [(sym(j, xT2), AT2[i][j]) for j in range(w + 1)]:
                    if cf == 0 or self.gen[s] is None:
                        continue
                    gi, sg = self.gen[s]
                    row[gi] = (row.get(gi, 0) + sg * cf) % P
                row = {a: b for a, b in row.items() if b}
                key = tuple(sorted(row.items()))
                if row and key not in seen:
                    seen.add(key); rows.append(row)
        R = np.zeros((len(rows), G), dtype=np.int64)
        for r, row in enumerate(rows):
            for a, b in row.items():
                R[r, a] = b
        # RREF mod P
        piv_cols = []
        r = 0
        for col in range(G):
            if r >= R.shape[0]:
                break
            nz = np.nonzero(R[r:, col])[0]
            if len(nz) == 0:
                continue
            pr = r + nz[0]
            if pr != r:
                R[[r, pr]] = R[[pr, r]]
            R[r] = R[r] * inv(R[r, col]) % P
            others = np.nonzero(R[:, col])[0]
            others = others[others != r]
            if len(others):
                R[others] = (R[others] - R[others, col][:, None] * R[r][None, :]) % P
            piv_cols.append(col)
            r += 1
        self.rank = r
        pivset = set(piv_cols)
        free = [c for c in range(G) if c not in pivset]
        self.d = len(free)
        pos = {c: j for j, c in enumerate(free)}
        proj_gen = np.zeros((G, self.d), dtype=np.int64)
        for j, c in enumerate(free):
            proj_gen[c, j] = 1
        for rr, c in enumerate(piv_cols):
            proj_gen[c] = (-R[rr, free]) % P
        self.proj_gen = proj_gen
        self.free = free

    def proj(self, s):
        g = self.gen[s]
        if g is None:
            return None
        return (g[1] * self.proj_gen[g[0]]) % P

    def proj_full(self):
        """n x d matrix of every symbol's coordinates"""
        out = np.zeros((self.n, self.d), dtype=np.int64)
        for s in range(self.n):
            g = self.gen[s]
            if g is not None:
                out[s] = (g[1] * self.proj_gen[g[0]]) % P
        return out

    def basis_symbol(self, j):
        """a Manin symbol whose generator is the j-th free generator"""
        c = self.free[j]
        for s in range(self.n):
            g = self.gen[s]
            if g is not None and g[0] == c:
                return s, g[1]
        raise ValueError

    def apply_heilbronn_symbol(self, s, H):
        """list of (symbol, coefficient) for T_n applied to symbol s"""
        M, w, N = self.M, self.w, self.N
        i, x = divmod(s, M)
        c0, d0 = self.reps[x]
        out = {}
        for (a, b, c, d) in H:
            y = self.idx[(c0 * a + d0 * c) % N, (c0 * b + d0 * d) % N]
            A = act_poly(w, a, b, c, d)[i]
            for j in range(w + 1):
                if A[j]:
                    t = j * M + y
                    out[t] = (out.get(t, 0) + A[j]) % P
        return out

    def hecke(self, n, PF=None):
        PF = self.proj_full() if PF is None else PF
        H = heilbronn(n)
        Tm = np.zeros((self.d, self.d), dtype=np.int64)
        for j in range(self.d):
            s, sg = self.basis_symbol(j)
            for t, cf in self.apply_heilbronn_symbol(s, H).items():
                Tm[:, j] = (Tm[:, j] + sg * cf % P * PF[t]) % P
        return Tm


def nullspace(A):
    """basis (rows) of {v : A v = 0} mod P"""
    A = A.copy() % P
    m, n = A.shape
    piv = []
    r = 0
    for col in range(n):
        if r >= m:
            break
        nz = np.nonzero(A[r:, col])[0]
        if len(nz) == 0:
            continue
        pr = r + nz[0]
        if pr != r:
            A[[r, pr]] = A[[pr, r]]
        A[r] = A[r] * inv(A[r, col]) % P
        others = np.nonzero(A[:, col])[0]
        others = others[others != r]
        if len(others):
            A[others] = (A[others] - A[others, col][:, None] * A[r][None, :]) % P
        piv.append(col)
        r += 1
    free = [c for c in range(n) if c not in set(piv)]
    basis = []
    for f in free:
        v = np.zeros(n, dtype=np.int64)
        v[f] = 1
        for rr, c in enumerate(piv):
            v[c] = (-A[rr, f]) % P
        basis.append(v)
    return np.array(basis, dtype=np.int64).reshape(len(basis), n)


def lift(x):
    x = int(x) % P
    return x - P if x > P // 2 else x


def minpoly_roots(T, bound):
    """integer roots in [-bound, bound] of the minimal polynomial of T acting on a random vector (Krylov + BM)"""
    d = T.shape[0]
    rng = np.random.default_rng(12345)
    v = rng.integers(0, P, d, dtype=np.int64)
    u = rng.integers(0, P, d, dtype=np.int64)
    seq = []
    x = v.copy()
    for _ in range(2 * d + 2):
        seq.append(int((u * x % P).sum() % P))
        x = (T * x[None, :] % P).sum(axis=1) % P
    # Berlekamp-Massey mod P
    C, B = [1], [1]
    L, m, b = 0, 1, 1
    for nn in range(len(seq)):
        dlt = seq[nn]
        for i in range(1, L + 1):
            dlt = (dlt + C[i] * seq[nn - i]) % P
        if dlt == 0:
            m += 1
            continue
        coef = dlt * inv(b) % P
        Cn = C + [0] * (len(B) + m - len(C))
        for i in range(len(B)):
            Cn[i + m] = (Cn[i + m] - coef * B[i]) % P
        if 2 * L <= nn:
            B, L, b, m = C, nn + 1 - L, dlt, 1
        else:
            m += 1
        C = Cn
    # C(x) = 1 + c1 x + ... is the connection polynomial; minimal polynomial = x^L C(1/x)
    C = C + [0] * (L + 1 - len(C))
    poly = [C[L - i] for i in range(L + 1)]       # coefficients of x^0..x^L
    roots = []
    for lam in range(-bound, bound + 1):
        val = 0
        for cf in reversed(poly):
            val = (val * lam + cf) % P
        if val == 0:
            roots.append(lam)
    return roots, L


def rational_eigensystems(N, primes, k=4, ells=(7, 11, 13), verbose=False):
    S = Space(N, k)
    PF = S.proj_full()
    Ts = {l: S.hecke(l, PF) for l in ells if N % l}
    ells = [l for l in ells if N % l]
    l0 = ells[0]
    bound = lambda l: int(2 * l ** ((k - 1) / 2))
    roots, L = minpoly_roots(Ts[l0], bound(l0))
    systems = []
    for lam in roots:
        W = nullspace(((Ts[l0] - lam * np.eye(S.d, dtype=np.int64)) % P).T)     # left eigenvectors as rows
        cands = [(W, {l0: lam})]
        for l in ells[1:]:
            new = []
            for Wc, ev in cands:
                # restrict T_l^T to the row space of Wc: Wc T_l = Mx Wc
                WT = np.array([(Ts[l].T * w_[None, :] % P).sum(axis=1) % P for w_ in Wc])   # (T^T w) for each row w
                for mu in range(-bound(l), bound(l) + 1):
                    # vectors c with c (WT - mu Wc) = 0
                    Mx = (WT - mu * Wc) % P
                    ns = nullspace(Mx.T)
                    if ns.shape[0]:
                        new.append(((ns @ Wc) % P, {**ev, l: mu}))
            cands = new
        for Wc, ev in cands:
            phi = Wc[0]
            phif = (PF * phi[None, :] % P).sum(axis=1) % P           # phi on every symbol
            nzs = np.nonzero(phif)[0]
            if len(nzs) == 0:
                continue
            m = int(nzs[0])
            den = inv(phif[m])
            ap = {}
            ok = True
            for p in primes:
                if N % p == 0:
                    continue
                val = 0
                for t, cf in S.apply_heilbronn_symbol(m, heilbronn(p)).items():
                    val = (val + cf * phif[t]) % P
                a = lift(val * den % P)
                if abs(a) > 2 * p ** ((k - 1) / 2) + 1e-9:
                    ok = False
                    break
                ap[p] = a
            if ok:
                systems.append(dict(level=N, ev=ev, ap=ap, mult=int(Wc.shape[0])))
    if verbose:
        print(f"N={N}: symbols {S.n}, generators {S.G}, plus-space dim {S.d}, minpoly degree {L}, "
              f"rational cusp systems {len(systems)}", flush=True)
    return systems


if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import exact_moments as emo
    primes = [q for q in range(7, 200) if sympy.isprime(q)]
    known = {5: [(1, 4), (5, 4)], 6: [(1, 2), (2, 2), (3, 2), (6, 2)], 8: [(2, 4), (4, 4)], 9: [(3, 8)]}
    allok = True
    for N, spec in known.items():
        cf = emo.eta_coeffs(spec, 200)
        sy = rational_eigensystems(N, primes, verbose=True)
        ok = len(sy) == 1 and all(sy[0]["ap"][p] == cf[p] for p in sy[0]["ap"])
        allok &= ok
        print(f"   level {N}: the one rational system equals the eta product at every prime 7..199: {ok}")
    print("SELF-TEST", "PASS" if allok else "FAIL")
