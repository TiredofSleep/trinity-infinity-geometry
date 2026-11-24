"""arb_check.py -- the maximum of S over diagonal states on p levels (p = 3, 5, 7), proved again in Arb.

A second proof of the theorems of OPTIMUM.md, independent of bb.c in its arithmetic. Every operation here is a ball
operation of Arb (python-flint), with Arb's own pi, cos and sin: there is no rounding model and no hand-made
enclosure. The logic is bb.c's, coded again from the statement in OPTIMUM.md, over the same domain
D = [-pi/p, pi/p]^2 x [0, 2 pi]^(p-3) (phi(0) = 0):
  (a) a box whose upper bound for S is below S_LO is discarded;
  (b) a box on which S is smooth and some partial derivative cannot vanish is discarded;
  (c) a box inside a certified box B_c is discarded.
B_c, S_LO and the certificates are recomputed here in Arb, from the candidate points of candidates_P.txt (prepare.py;
the points are untrusted): every E keeps its sign on B_c; -Hessian is positive definite on B_c (interval Cholesky);
the Krawczyk operator maps X_c into its interior; the symmetry that produced candidate c maps X_0 into B_c; the B_c
are pairwise disjoint. Then every global maximizer in D is one of the certified critical points, and they all share
the value S(phi_0*), enclosed between S_LO and the upper bound of S on X_0.

The bounds (S = (1/p^2) sum over (q, s) of |E(q, s)|, E = 1 + 2 sum_u cos(theta), theta = phi(q+u) - phi(q-u) - 4 pi s u/p):
  - on a box with centre m and half-widths r_i, each angle stays within w = r(q+u) + r(q-u) of its centre value;
  - |cos theta - cos theta_c| <= w (|sin theta_c| + w), and likewise for sin, give each E's range and each partial
    derivative's range;
  - U_exact = (1/p^2) sum of max |E| over the box;
  - U_mixed = (1/p^2) [sum over E of fixed sign of sigma E(m) + sum_i |grad_i(m)| r_i + sum of w^2 + the rest's max |E|],
    the second-order Taylor bound (|d^2/dtheta^2 2 cos| <= 2, so each term's remainder is at most w^2).

  python -I arb_check.py P [workers]      (P = 3, 5 or 7; 4 workers by default, at below-normal priority)
"""
import math
import multiprocessing as mp
import os
import sys
import time

from flint import arb, ctx

ctx.prec = 64
HERE = os.path.dirname(os.path.abspath(__file__))

P = NU = DIM = None
PI = TWO_PI = ONE = TWO = ZERO = None
CK = SK = None                 # cos and sin of 2 pi k / p
KIDX = None                    # KIDX[s][u] = 2 s (u + 1) mod p
PAIRS = None                   # PAIRS[q] = [(a, b)] for u = 1..NU: a = q + u, b = q - u (mod p)
CAND = None
S_LO = None


def low_priority():
    try:
        import ctypes
        k32 = ctypes.windll.kernel32
        k32.GetCurrentProcess.restype = ctypes.c_void_p
        k32.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_uint]
        k32.SetPriorityClass(k32.GetCurrentProcess(), 0x4000)
    except Exception:
        pass


def init(p):
    global P, NU, DIM, PI, TWO_PI, ONE, TWO, ZERO, CK, SK, KIDX, PAIRS
    P, NU, DIM = p, (p - 1) // 2, p - 1
    ctx.prec = 64
    PI = arb.pi()
    TWO_PI = 2 * PI
    ONE, TWO, ZERO = arb(1), arb(2), arb(0)
    CK = [(TWO_PI * k / P).cos() for k in range(P)]
    SK = [(TWO_PI * k / P).sin() for k in range(P)]
    KIDX = [[(2 * s * (u + 1)) % P for u in range(NU)] for s in range(P)]
    PAIRS = [[((q + u + 1) % P, (q - u - 1) % P) for u in range(NU)] for q in range(P)]


def float_above(x):
    """a double certainly >= the arb x"""
    f = float(x)
    while not (arb(f) >= x):
        f = math.nextafter(f, math.inf)
    return f


def float_below(x):
    """a double certainly <= the arb x"""
    f = float(x)
    while not (arb(f) <= x):
        f = math.nextafter(f, -math.inf)
    return f


def widen(ball, half):
    """a ball containing ball +- half (half an arb >= 0)"""
    r = float(half.abs_upper()) * (1 + 1e-12) + 1e-300
    return ball + arb(0, r)


def bounds(lo, hi):
    """bounds for S on the box [lo, hi] (lists of DIM doubles; lo == hi gives a point).
    Returns (U_mixed, U_exact, smooth, mono, L, Sc, grad_at_centre) with U_* arbs bounding P^2 S from above,
    L an arb bounding P^2 S from below at the centre's ball, and grad the gradient of P^2 S at the centre."""
    M = [0.0] + [0.5 * lo[i] + 0.5 * hi[i] for i in range(DIM)]
    Ma = [arb(x) for x in M]
    R = [ZERO]
    for i in range(DIM):
        r1, r2 = Ma[i + 1] - arb(lo[i]), arb(hi[i]) - Ma[i + 1]
        R.append(r1.max(r2))
    g = [ZERO] * P
    gi = [ZERO] * P
    sum_exact = ZERO
    sum_kept = ZERO
    sum_rem = ZERO
    sum_other = ZERO
    low = ZERO
    sc = ZERO
    all_kept = True
    for q in range(P):
        pre = []
        for (a, b) in PAIRS[q]:
            sD, cD = (Ma[a] - Ma[b]).sin_cos()
            w = R[a] + R[b]
            pre.append((a, b, sD, cD, w, w * w))
        for s in range(P):
            Ec = ONE
            Emax = ONE
            Emin = ONE
            terms = []
            for u in range(NU):
                a, b, sD, cD, w, w2 = pre[u]
                k = KIDX[s][u]
                ct = cD * CK[k] + sD * SK[k]
                st = sD * CK[k] - cD * SK[k]
                dc = w * (abs(st) + w)
                ds = w * (abs(ct) + w)
                Ec = Ec + 2 * ct
                hi_u = ct + dc
                lo_u = ct - dc
                if hi_u > ONE:
                    hi_u = ONE
                if lo_u < -ONE:
                    lo_u = -ONE
                Emax = Emax + 2 * hi_u
                Emin = Emin + 2 * lo_u
                terms.append((a, b, st, ds, w2))
            absmax = arb.max(abs(Emax), abs(Emin))
            sum_exact = sum_exact + absmax
            sc = sc + abs(Ec)
            if Emin > 0 or Emax < 0:
                sig = 1 if Emin > 0 else -1
                sum_kept = sum_kept + (Ec if sig > 0 else -Ec)
                low = low + (Emin if sig > 0 else -Emax)
                for (a, b, st, ds, w2) in terms:
                    t = 2 * st if sig > 0 else -2 * st
                    g[a] = g[a] - t
                    g[b] = g[b] + t
                    tb = widen(t, 2 * ds)
                    gi[a] = gi[a] - tb
                    gi[b] = gi[b] + tb
                    sum_rem = sum_rem + w2
            else:
                all_kept = False
                sum_other = sum_other + absmax
    lin = ZERO
    for i in range(1, P):
        lin = lin + abs(g[i]) * R[i]
    U_mixed = sum_kept + lin + sum_rem + sum_other
    mono = all_kept and any((gi[i] > 0) or (gi[i] < 0) for i in range(1, P))
    return U_mixed, sum_exact, all_kept, mono, low, sc, g[1:]


def hessian(lo, hi):
    """the interval Hessian of P^2 S over the box (None if some E has no certified sign on it)"""
    M = [0.0] + [0.5 * lo[i] + 0.5 * hi[i] for i in range(DIM)]
    Ma = [arb(x) for x in M]
    R = [ZERO]
    for i in range(DIM):
        r1, r2 = Ma[i + 1] - arb(lo[i]), arb(hi[i]) - Ma[i + 1]
        R.append(r1.max(r2))
    H = [[ZERO] * DIM for _ in range(DIM)]
    for q in range(P):
        pre = []
        for (a, b) in PAIRS[q]:
            sD, cD = (Ma[a] - Ma[b]).sin_cos()
            pre.append((a, b, sD, cD, R[a] + R[b]))
        for s in range(P):
            Emax = ONE
            Emin = ONE
            cosb = []
            for u in range(NU):
                a, b, sD, cD, w = pre[u]
                k = KIDX[s][u]
                ct = cD * CK[k] + sD * SK[k]
                st = sD * CK[k] - cD * SK[k]
                dc = w * (abs(st) + w)
                Emax = Emax + 2 * (ct + dc)
                Emin = Emin + 2 * (ct - dc)
                cosb.append((a, b, widen(ct, dc)))
            if not (Emin > 0 or Emax < 0):
                return None
            sig = 1 if Emin > 0 else -1
            for (a, b, cb) in cosb:
                T = -2 * cb if sig > 0 else 2 * cb          # second derivative of 2 sigma cos(theta) in theta
                if a >= 1:
                    H[a - 1][a - 1] = H[a - 1][a - 1] + T
                if b >= 1:
                    H[b - 1][b - 1] = H[b - 1][b - 1] + T
                if a >= 1 and b >= 1:
                    H[a - 1][b - 1] = H[a - 1][b - 1] - T
                    H[b - 1][a - 1] = H[b - 1][a - 1] - T
    return H


def cholesky_pivots(A):
    """interval Cholesky of the symmetric interval matrix A; returns the pivots (None if one is not certainly > 0).
    If every pivot is certainly positive, every symmetric matrix in A is positive definite (Alefeld and Mayer)."""
    n = len(A)
    L = [[ZERO] * n for _ in range(n)]
    piv = []
    for j in range(n):
        d = A[j][j]
        for k in range(j):
            d = d - L[j][k] * L[j][k]
        if not (d > 0):
            return None
        piv.append(d)
        L[j][j] = d.sqrt()
        for i in range(j + 1, n):
            v = A[i][j]
            for k in range(j):
                v = v - L[i][k] * L[j][k]
            L[i][j] = v / L[j][j]
    return piv


def read_candidates(path):
    tok = open(path).read().split()
    assert tok[0] == 'P' and int(tok[1]) == P
    import struct
    h2d = lambda h: struct.unpack('>d', bytes.fromhex(h.rjust(16, '0')))[0]
    rho, eps, n = h2d(tok[3]), h2d(tok[5]), int(tok[7])
    pos, cands = 8, []
    for _ in range(n):
        m = [h2d(tok[pos + i]) for i in range(DIM)]
        pos += DIM
        e, al, t = int(tok[pos]), int(tok[pos + 1]), int(tok[pos + 2])
        pos += 3
        k = [int(x) for x in tok[pos:pos + DIM]]
        pos += DIM
        nn = [int(x) for x in tok[pos:pos + DIM]]
        pos += DIM
        cands.append(dict(m=m, eps=e, alpha=al, t=t, k=k, n=nn))
    return rho, eps, cands


def certify(cands, rho, epsk, log):
    import numpy as np
    ok_all = True
    s_lo, s_hi, minpiv, minmarg = None, None, math.inf, math.inf
    for c in cands:
        m = c['m']
        c['Blo'] = [x - rho for x in m]
        c['Bhi'] = [x + rho for x in m]
        c['Xlo'] = [x - epsk for x in m]
        c['Xhi'] = [x + epsk for x in m]
        assert all(c['Xlo'][i] < m[i] < c['Xhi'][i] and c['Blo'][i] < c['Xlo'][i] and c['Xhi'][i] < c['Bhi'][i]
                   for i in range(DIM))
        _, _, smooth, _, _, _, _ = bounds(c['Blo'], c['Bhi'])
        HB = hessian(c['Blo'], c['Bhi']) if smooth else None
        piv = cholesky_pivots([[-x for x in row] for row in HB]) if HB is not None else None
        _, _, psmooth, _, low, _, gm = bounds(m, m)
        HX = hessian(c['Xlo'], c['Xhi'])
        kraw = False
        if piv is not None and psmooth and HX is not None:
            Mid = np.array([[float(x) for x in row] for row in HX])
            Y = np.linalg.inv(Mid)
            Ya = [[arb(float(Y[i][j])) for j in range(DIM)] for i in range(DIM)]
            kraw, marg = True, math.inf
            for i in range(DIM):
                acc = arb(m[i])
                for j in range(DIM):
                    acc = acc - Ya[i][j] * gm[j]
                for j in range(DIM):
                    yh = ZERO
                    for k in range(DIM):
                        yh = yh + Ya[i][k] * HX[k][j]
                    dj = (arb(c['Xlo'][j]) - arb(m[j])).union(arb(c['Xhi'][j]) - arb(m[j]))
                    acc = acc + ((ONE if i == j else ZERO) - yh) * dj
                if not (acc > arb(c['Xlo'][i]) and acc < arb(c['Xhi'][i])):
                    kraw = False
                marg = min(marg, float(acc.lower()) - c['Xlo'][i], c['Xhi'][i] - float(acc.upper()))
            minmarg = min(minmarg, marg)
        Ux, Ex, _, _, _, _, _ = bounds(c['Xlo'], c['Xhi'])
        c['L'] = low / (P * P)
        c['U'] = arb.min(Ux, Ex) / (P * P)
        c['ok'] = smooth and piv is not None and psmooth and kraw
        if piv is not None:
            minpiv = min(minpiv, min(float(d.lower()) for d in piv))
        ok_all &= c['ok']
        s_lo = c['L'] if s_lo is None else arb.max(s_lo, c['L'])
        s_hi = c['U'] if s_hi is None else arb.min(s_hi, c['U'])
    # symmetry images of X_0 inside every B_c
    c0 = cands[0]
    X0 = [ZERO] + [arb(c0['Xlo'][i]).union(arb(c0['Xhi'][i])) for i in range(DIM)]
    img_ok = True
    for c in cands[1:]:
        for x in range(1, P):
            a = (c['alpha'] * x + c['t']) % P
            d = X0[a] - X0[c['t']]
            if c['eps'] < 0:
                d = -d
            d = d + TWO_PI * c['k'][x - 1] / P + TWO_PI * c['n'][x - 1]
            if not (d >= arb(c['Blo'][x - 1]) and d <= arb(c['Bhi'][x - 1])):
                img_ok = False
    disjoint = True
    for i in range(len(cands)):
        for j in range(i + 1, len(cands)):
            if all(not (cands[i]['Bhi'][d] < cands[j]['Blo'][d] or cands[j]['Bhi'][d] < cands[i]['Blo'][d])
                   for d in range(DIM)):
                disjoint = False
    log(f"certified: {'all' if ok_all else 'NOT ALL'} (signs fixed, -Hessian positive definite on every B_c by interval "
        f"Cholesky [smallest pivot {minpiv:.4g}], Krawczyk contraction on every X_c [smallest margin {minmarg:.3g}]); "
        f"symmetry images of X_0 inside every B_c: {'yes' if img_ok else 'NO'}; B_c pairwise disjoint: "
        f"{'yes' if disjoint else 'NO'}")
    log(f"S at the maximizer lies in [{s_lo.lower()}, {s_hi.upper()}]")
    return ok_all and img_ok and disjoint, s_lo, s_hi


def worker_init(p, boxes_B, s_lo_float):
    global CAND, S_LO
    low_priority()
    init(p)
    CAND = [dict(Blo=lo, Bhi=hi) for lo, hi in boxes_B]
    S_LO = arb(s_lo_float) * (P * P)        # a double certainly below S_LO; the bounds are of P^2 S


def inside_some_B(lo, hi):
    for c in CAND:
        if all(lo[i] >= c['Blo'][i] and hi[i] <= c['Bhi'][i] for i in range(DIM)):
            return True
    return False


def process(box):
    st = dict(boxes=0, bound=0, mono=0, cube=0, stuck=0)
    stack = [box]
    while stack:
        lo, hi = stack.pop()
        st['boxes'] += 1
        Um, Ue, smooth, mono, _, _, _ = bounds(lo, hi)
        if Um < S_LO or Ue < S_LO:
            st['bound'] += 1
            continue
        if mono:
            st['mono'] += 1
            continue
        if inside_some_B(lo, hi):
            st['cube'] += 1
            continue
        j = max(range(DIM), key=lambda i: hi[i] - lo[i])
        mid = 0.5 * lo[j] + 0.5 * hi[j]
        if not (lo[j] < mid < hi[j]):
            st['stuck'] += 1
            continue
        lo2, hi1 = list(lo), list(hi)
        hi1[j] = mid
        lo2[j] = mid
        stack.append((lo2, list(hi)))
        stack.append((list(lo), hi1))
    return st


def main():
    p = int(sys.argv[1])
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    low_priority()
    init(p)
    out = open(os.path.join(HERE, f"arb{p}.log"), 'w')

    def log(s):
        print(s, flush=True)
        out.write(s + '\n')
        out.flush()
    import flint
    log(f"arb_check.py, p = {p}: Arb ball arithmetic (python-flint {flint.__version__}, {ctx.prec}-bit balls), "
        f"{workers} worker processes")
    rho, epsk, cands = read_candidates(os.path.join(HERE, f"candidates_{p}.txt"))
    log(f"{len(cands)} candidate maximizers, certified boxes of half-width {rho:.4g}, Krawczyk boxes of half-width {epsk:.3g}")
    t0 = time.time()
    cert_ok, s_lo, s_hi = certify(cands, rho, epsk, log)
    pip = float_above(PI / P)
    tpi = float_above(TWO_PI)
    e1 = [-pip, 0.0, pip]
    e3 = [0.0, 0.25 * tpi, 0.5 * tpi, 0.75 * tpi, tpi]
    boxes = []
    total = 1
    for i in range(DIM):
        total *= 2 if i < 2 else 4
    for kk in range(total):
        rem, lo, hi = kk, [], []
        for i in range(DIM):
            base = 2 if i < 2 else 4
            idx = rem % base
            rem //= base
            e = e1 if i < 2 else e3
            lo.append(e[idx])
            hi.append(e[idx + 1])
        boxes.append((lo, hi))
    s_lo_float = float_below(s_lo)
    boxes_B = [(c['Blo'], c['Bhi']) for c in cands]
    tot = dict(boxes=0, bound=0, mono=0, cube=0, stuck=0)
    with mp.Pool(workers, initializer=worker_init, initargs=(p, boxes_B, s_lo_float)) as pool:
        done = 0
        for st in pool.imap_unordered(process, boxes, chunksize=1):
            for key in tot:
                tot[key] += st[key]
            done += 1
            if len(boxes) >= 16 and done % (len(boxes) // 8) == 0:
                print(f"  progress: {done}/{len(boxes)} first-grid boxes, {tot['boxes']} boxes, "
                      f"{time.time() - t0:.0f} s", flush=True)
    log(f"boxes {tot['boxes']} by_bound {tot['bound']} by_monotone {tot['mono']} by_certified_box {tot['cube']} "
        f"stuck {tot['stuck']}; {time.time() - t0:.1f} s")
    if cert_ok and tot['stuck'] == 0:
        log(f"VERDICT PASS (Arb): the maximum of S over diagonal states on {p} levels lies in "
            f"[{s_lo.lower()}, {s_hi.upper()}], attained exactly at the {len(cands)} certified critical points in D")
    else:
        log("VERDICT FAIL")


if __name__ == '__main__':
    main()
