"""t_optimal_7.py -- a computer-assisted proof that at p = 7 the T state is the most Wigner-negative diagonal state.

    "attempt the proof"  -- the author, 18 November 2026 (after round 30 found it numerically)

Claim.  For every phase vector phi in R^7, the diagonal state psi = sum_x exp(i phi(x)) |x> / sqrt 7 has
    S(phi) = sum_(q,s) |W(q,s)| <= S_T = 2.4503041185...,
with equality exactly at the T states f = c x^3 + (lower), c in {3, 4} (the class t = c/4 = 1).

Reduction.
  - W(q, s) = E(q, s)/49 with E(q, s) = 1 + 2 sum_(u=1..3) cos(phi(q+u) - phi(q-u) - 4 pi s u / 7).
  - S is unchanged by the global phase (so phi(0) = 0) and by the Clifford phases w^(b x + g x^2), which translate the
    torus T^6 of phi(1..6) by the 49 vectors 2 pi (b x + g x^2)/7.  Since (b, g) -> (b + g, 2b + 4g) is a bijection of
    F_7^2, every phi has a translate in  D = [-pi/7, pi/7]^2 x [0, 2 pi]^4  (phi(1), phi(2), then phi(3..6)).
  - In D the T states of class t = 1 are exactly two points, phi_c = (2 pi/7) c (x^3 + 4x^2 + 2x), c = 3, 4.

Branch and bound over closed boxes B in D (center c, half-widths r).  A box is discarded when one of these holds:
  (a) an upper bound for S on B is below S_T - 1e-9.  The bound: each E(q, s) depends on three angles through disjoint
      pairs of coordinates, so its exact range over B is computed term by term; the terms that keep their sign over B
      are linearized together (with the remainder sum_u w_u^2, w_u the angle's half-range), and the others take their
      exact maximum of |E|;
  (b) S is smooth on B (every E keeps its sign) and some partial derivative of S is nonzero on all of B (an interval
      bound): then B holds no critical point, so no maximum of S (a maximum of S = sum |E|/49 at a point where all E
      are nonzero is a critical point; where some E vanishes with nonzero gradient S increases in some direction);
  (c) B lies inside the cube of half-width rho0 = 0.004 around phi_3 or phi_4, where S is smooth and concave (the
      Hessian moves by at most 24 rho0 < 0.1098 = the smallest |eigenvalue| at phi_c), so phi_c is the only maximum.
When every box is discarded, max S = S_T, attained only at phi_3 and phi_4 in D, and so only at T states of class 1.

Floating point.  Double precision throughout; the margins (1e-9 in (a), 1e-12 in (b)) are far above the rounding error
of these sums (about 1e-14).  This is a computer-assisted proof in floating point, not a formally verified one.

  python t_optimal_7.py check     # the lemmas: the bound on samples, the two maximizers, the Hessian, rho0 (seconds)
  python t_optimal_7.py prove     # the branch and bound over D (minutes; four processes, below-normal priority)
  python t_optimal_7.py control   # the same prover at p = 5, where the T state is NOT optimal: it must fail (seconds)

numpy only.  ASCII output; writes t_optimal_7.log.
"""
import math
import os
import sys
import time

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
P = 7
QQ = np.arange(P)
UU = np.arange(1, 4)
AI = (QQ[:, None] + UU[None, :]) % P              # (q, u): the index q + u
BI = (QQ[:, None] - UU[None, :]) % P              # (q, u): the index q - u
SHIFT = 4 * np.pi * np.outer(np.arange(P), UU) / P   # (s, u)
TWO_PI = 2 * np.pi
RHO0 = 0.004
LOG = None


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def low_priority():
    try:
        import ctypes
        ctypes.windll.kernel32.SetPriorityClass(ctypes.c_void_p(-1), 0x00004000)
    except Exception:
        pass


def full(v):
    """phi(0..6) from phi(1..6), for a batch (N, 6) -> (N, 7)"""
    return np.concatenate([np.zeros((v.shape[0], 1)), v], axis=1)


def E_of(phi7):
    th = phi7[:, AI] - phi7[:, BI]                                   # (N, q, u)
    ang = th[:, :, None, :] - SHIFT[None, None, :, :]                # (N, q, s, u)
    return 1 + 2 * np.cos(ang).sum(axis=3), ang


def S_of(phi7):
    return np.abs(E_of(phi7)[0]).sum(axis=(1, 2)) / 49


def cos_range(ang, w):
    """exact range of cos over [ang - w, ang + w]"""
    lo, hi = ang - w, ang + w
    cl, ch = np.cos(lo), np.cos(hi)
    cmax, cmin = np.maximum(cl, ch), np.minimum(cl, ch)
    wide = (hi - lo) >= TWO_PI
    has_top = (np.ceil(lo / TWO_PI) * TWO_PI <= hi) | wide
    has_bot = (np.ceil((lo - np.pi) / TWO_PI) * TWO_PI + np.pi <= hi) | wide
    return np.where(has_bot, -1.0, cmin), np.where(has_top, 1.0, cmax)


def sin_range(ang, w):
    """exact range of sin over [ang - w, ang + w] (sin x = cos(x - pi/2))"""
    return cos_range(ang - np.pi / 2, w)


def bounds(c6, r6):
    """for a batch of boxes: the upper bound U for S, whether S is smooth on the box, and whether the interval gradient
    excludes 0 in some coordinate (only meaningful where smooth), plus S at the center"""
    N = c6.shape[0]
    c7, r7 = full(c6), full(r6)
    E, ang = E_of(c7)                                                # (N, q, s), (N, q, s, u)
    w = (r7[:, AI] + r7[:, BI])[:, :, None, :] * np.ones((1, 1, P, 1))   # (N, q, s, u)
    cmin, cmax = cos_range(ang, w)
    Emax = 1 + 2 * cmax.sum(axis=3)
    Emin = 1 + 2 * cmin.sum(axis=3)
    absmax = np.maximum(np.abs(Emax), np.abs(Emin))
    exact = absmax.sum(axis=(1, 2))
    keep = (Emin > 0) | (Emax < 0)
    sig = np.sign(E)
    ks = keep * sig                                                  # (N, q, s)
    sn = np.sin(ang)                                                 # (N, q, s, u)
    grad = np.zeros((N, P))
    for q in range(P):
        for u in range(3):
            t = (ks[:, q, :] * sn[:, q, :, u]).sum(axis=1)           # d/dphi of sum_s ks E, through angle u
            grad[:, AI[q, u]] += -2 * t
            grad[:, BI[q, u]] += 2 * t
    R = (w ** 2).sum(axis=3)                                         # linearization remainder per term
    lin = (ks * E).sum(axis=(1, 2)) + (np.abs(grad[:, 1:]) * r6).sum(axis=1) + (keep * R).sum(axis=(1, 2))
    other = (absmax * (~keep)).sum(axis=(1, 2))
    U = np.minimum(lin + other, exact) / 49
    smooth = keep.all(axis=(1, 2))
    # interval gradient of S on smooth boxes: d/dphi_x of sum sig E = sum over (q, s, u) of -+2 sig sin(angle)
    smin, smax = sin_range(ang, w)
    glo = np.zeros((N, P))
    ghi = np.zeros((N, P))
    for q in range(P):
        for u in range(3):
            # coefficient -2 sig on index a, +2 sig on index b; interval of k * [smin, smax]
            for idx, k0 in ((AI[q, u], -2.0), (BI[q, u], 2.0)):
                k = k0 * sig[:, q, :]                                # (N, s)
                lo = np.minimum(k * smin[:, q, :, u], k * smax[:, q, :, u]).sum(axis=1)
                hi = np.maximum(k * smin[:, q, :, u], k * smax[:, q, :, u]).sum(axis=1)
                glo[:, idx] += lo
                ghi[:, idx] += hi
    monotone = smooth & ((glo[:, 1:] > 1e-12) | (ghi[:, 1:] < -1e-12)).any(axis=1)
    S_center = np.abs(E).sum(axis=(1, 2)) / 49
    return U, smooth, monotone, S_center


def maximizers():
    x = np.arange(P)
    out = []
    for c in (3, 4):
        f = (c * (x ** 3 + 4 * x * x + 2 * x)) % P
        phi = TWO_PI * f / P
        v = phi[1:].copy()
        v[:2] = np.where(v[:2] > np.pi / 7, v[:2] - TWO_PI, v[:2])   # into [-pi/7, pi/7] (they are 0)
        out.append(v)
    return out


S_T = None


def hessian(phi7):
    """the analytic Hessian of sum sig E / 49 at phi (sig = the signs there), in phi(1..6)"""
    E, ang = E_of(phi7[None, :])
    E, ang = E[0], ang[0]
    sig = np.sign(E)
    H = np.zeros((P, P))
    for q in range(P):
        for s in range(P):
            for u in range(3):
                cval = -2 * sig[q, s] * np.cos(ang[q, s, u])
                a, b = AI[q, u], BI[q, u]
                H[a, a] += cval
                H[b, b] += cval
                H[a, b] -= cval
                H[b, a] -= cval
    return H[1:, 1:] / 49, E


def check():
    global LOG, S_T
    LOG = open(os.path.join(HERE, "t_optimal_7_check.log"), "w", encoding="utf-8")
    say("t_optimal_7.py check -- the lemmas of the proof at p = 7")
    ok_all = True
    rng = np.random.default_rng(20261118)
    # the bound is an upper bound (sampled, many sizes)
    ok = True
    for r0 in (0.002, 0.02, 0.1, 0.3, 1.0):
        c = np.column_stack([rng.uniform(-np.pi / 7, np.pi / 7, (400, 2)), rng.uniform(0, TWO_PI, (400, 4))])
        r = np.full((400, 6), r0)
        U, smooth, mono, S0 = bounds(c, r)
        for _ in range(30):
            x = c + rng.uniform(-1, 1, (400, 6)) * r
            ok &= bool(np.all(S_of(full(x)) <= U + 1e-12))
    say(f"[{'PASS' if ok else 'FAIL'}] L1 the bound U is above S at 60 000 sampled points of 2000 random boxes (half-widths 0.002 to 1)")
    ok_all &= ok
    mx = maximizers()
    vals = [float(S_of(full(v[None, :]))[0]) for v in mx]
    S_T = vals[0]
    x = np.arange(P)
    T_direct = float(S_of(full((TWO_PI * ((4 * x ** 3) % P) / P)[1:][None, :]))[0])
    ok = abs(vals[0] - vals[1]) < 1e-13 and abs(vals[0] - T_direct) < 1e-13
    say(f"[{'PASS' if ok else 'FAIL'}] L2 the two maximizers in D (c = 3, 4) have S = {vals[0]:.13f} = S of the T state 4x^3")
    ok_all &= ok
    ok = True
    for v in mx:
        H, E = hessian(full(v[None, :])[0])
        lam = np.linalg.eigvalsh(H)
        g = bounds(v[None, :], np.zeros((1, 6)))
        minE = float(np.abs(E).min())
        # gradient at the maximizer
        c7 = full(v[None, :])
        E7, ang = E_of(c7)
        sig = np.sign(E7)[0]
        grad = np.zeros(P)
        for q in range(P):
            for u in range(3):
                t = (sig[q, :] * np.sin(ang[0, q, :, u])).sum()
                grad[AI[q, u]] += -2 * t
                grad[BI[q, u]] += 2 * t
        ok &= lam.max() < -24 * RHO0 and minE > 12 * RHO0 * 1.01 and np.abs(grad[1:]).max() < 1e-12
        say(f"     maximizer: Hessian eigenvalues {np.round(lam, 6)}; min |E| = {minE:.4f}; max |grad| = {np.abs(grad[1:]).max():.1e}")
    say(f"[{'PASS' if ok else 'FAIL'}] L3 at both maximizers: gradient 0, Hessian below -24 rho0 = {-24 * RHO0:.4f}, and every |E| above "
        f"12 rho0 (so on the cube of half-width rho0 = {RHO0} the signs hold, S is smooth and concave)")
    ok_all &= ok
    say(f"{'ALL PASS' if ok_all else 'FAILED'}")
    LOG.close()
    return ok_all


def _worker(args):
    c0, r0, ST, mx = args
    low_priority()
    stack_c, stack_r = [c0], [r0]
    stats = {"boxes": 0, "by_bound": 0, "by_monotone": 0, "by_concave": 0, "max_center": -1.0, "min_halfwidth": 9.0}
    mx = np.array(mx)
    while stack_c:
        C = np.array(stack_c[-20000:]) if len(stack_c) > 20000 else np.array(stack_c)
        Rr = np.array(stack_r[-20000:]) if len(stack_r) > 20000 else np.array(stack_r)
        del stack_c[-len(C):]
        del stack_r[-len(Rr):]
        U, smooth, mono, S0 = bounds(C, Rr)
        stats["boxes"] += len(C)
        stats["max_center"] = max(stats["max_center"], float(S0.max()))
        by_bound = U < ST - 1e-9
        inside = np.zeros(len(C), dtype=bool)
        for v in mx:
            inside |= np.all(np.abs(C - v) + Rr <= RHO0, axis=1)
        drop = by_bound | mono | inside
        stats["by_bound"] += int(by_bound.sum())
        stats["by_monotone"] += int((mono & ~by_bound).sum())
        stats["by_concave"] += int((inside & ~by_bound & ~mono).sum())
        keepC, keepR = C[~drop], Rr[~drop]
        if len(keepC):
            stats["min_halfwidth"] = min(stats["min_halfwidth"], float(keepR.max(axis=1).min()))
            j = np.argmax(keepR, axis=1)
            idx = np.arange(len(keepC))
            half = keepR[idx, j] / 2
            child_r = keepR.copy()
            child_r[idx, j] = half
            for sgn in (-1, 1):
                cc = keepC.copy()
                cc[idx, j] += sgn * half
                stack_c.extend(list(cc))
                stack_r.extend(list(child_r))
        if stats["boxes"] > 4e8:
            stats["aborted"] = True
            break
    return stats


def prove():
    global LOG, S_T
    if not check():
        print("the lemmas failed; no proof")
        return
    LOG = open(os.path.join(HERE, "t_optimal_7.log"), "w", encoding="utf-8")
    t0 = time.time()
    say("t_optimal_7.py prove -- branch and bound over D = [-pi/7, pi/7]^2 x [0, 2 pi]^4")
    say(f"S_T = {S_T:.13f}; discard margin 1e-9; concave cubes of half-width {RHO0} around the two maximizers")
    # initial grid: 2 x 2 in phi(1), phi(2) and 4 in each of phi(3..6): 1024 boxes, dealt to 4 workers in 64 chunks
    e12 = np.pi / 7
    c1 = [-e12 / 2, e12 / 2]
    c3 = [TWO_PI * (k + 0.5) / 4 for k in range(4)]
    boxes = [np.array([a, b, c, d, e, f]) for a in c1 for b in c1 for c in c3 for d in c3 for e in c3 for f in c3]
    r0 = np.array([e12 / 2, e12 / 2, TWO_PI / 8, TWO_PI / 8, TWO_PI / 8, TWO_PI / 8])
    mx = maximizers()
    from multiprocessing import Pool
    with Pool(4) as pool:
        results = pool.map(_worker, [(b, r0, S_T, mx) for b in boxes], chunksize=4)
    tot = {k: sum(r.get(k, 0) for r in results) for k in ("boxes", "by_bound", "by_monotone", "by_concave")}
    maxc = max(r["max_center"] for r in results)
    aborted = any(r.get("aborted") for r in results)
    minw = min(r["min_halfwidth"] for r in results)
    say(f"boxes examined {tot['boxes']}; discarded by the bound {tot['by_bound']}, by monotonicity {tot['by_monotone']}, "
        f"inside the concave cubes {tot['by_concave']}; the smallest box split had half-width {minw:.2e}")
    say(f"the largest S at any box center: {maxc:.13f} (S_T = {S_T:.13f})")
    ok = (not aborted) and maxc <= S_T + 1e-12
    say(f"[{'PASS' if ok else 'FAIL'}] THEOREM (p = 7): every diagonal state has S <= S_T, with equality only at the T states of class 1"
        + ("" if not aborted else "  (ABORTED: box limit reached)"))
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    LOG.close()


def control():
    """the same branch and bound at p = 5 with the T state's value 1 + 2/sqrt 5 as the target.  Feng and Luo proved the T
    state is not optimal there, so a sound prover must fail: it must reach a box center above the target."""
    global LOG, P, QQ, UU, AI, BI, SHIFT
    LOG = open(os.path.join(HERE, "t_optimal_7_control.log"), "w", encoding="utf-8")
    t0 = time.time()
    P = 5
    QQ, UU = np.arange(P), np.arange(1, (P - 1) // 2 + 1)
    AI = (QQ[:, None] + UU[None, :]) % P
    BI = (QQ[:, None] - UU[None, :]) % P
    SHIFT = 4 * np.pi * np.outer(np.arange(P), UU) / P
    target = 1 + 2 / math.sqrt(5)
    say("t_optimal_7.py control -- the same prover at p = 5, target S_T(5) = 1 + 2/sqrt 5 (Feng and Luo: T is not optimal)")
    e = np.pi / 5
    stack_c = [np.array([a, b, c, d]) for a in (-e / 2, e / 2) for b in (-e / 2, e / 2)
               for c in (np.pi / 2, 3 * np.pi / 2) for d in (np.pi / 2, 3 * np.pi / 2)]
    r0 = np.array([e / 2, e / 2, np.pi / 2, np.pi / 2])
    stack_r = [r0.copy() for _ in stack_c]
    boxes, found = 0, None
    while stack_c and found is None and boxes < 2e7:
        C = np.array(stack_c[-5000:]); Rr = np.array(stack_r[-5000:])
        del stack_c[-len(C):]; del stack_r[-len(Rr):]
        U, smooth, mono, S0 = bounds_general(C, Rr)
        boxes += len(C)
        if S0.max() > target + 1e-9:
            found = (float(S0.max()), C[int(np.argmax(S0))])
            break
        drop = (U < target - 1e-9) | mono
        kc, kr = C[~drop], Rr[~drop]
        if len(kc):
            j = np.argmax(kr, axis=1); idx = np.arange(len(kc)); half = kr[idx, j] / 2
            cr = kr.copy(); cr[idx, j] = half
            for sg in (-1, 1):
                cc = kc.copy(); cc[idx, j] += sg * half
                stack_c.extend(list(cc)); stack_r.extend(list(cr))
    ok = found is not None
    if ok:
        say(f"after {boxes} boxes the prover reached a center with S = {found[0]:.6f} > {target:.6f}, at phases "
            f"{[0.0] + [round(float(v), 4) for v in found[1]]}")
    say(f"[{'PASS' if ok else 'FAIL'}] CONTROL the prover does not prove a false optimality: at p = 5 it finds a state above the T state")
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    LOG.close()


def bounds_general(c, r):
    """bounds() for any p: the same formulas, with (p - 1)/2 angles per row and E = 1 + 2 sum cos"""
    N = c.shape[0]
    c7, r7 = full(c), full(r)
    nu = UU.size
    th = c7[:, AI] - c7[:, BI]
    ang = th[:, :, None, :] - SHIFT[None, None, :, :]
    E = 1 + 2 * np.cos(ang).sum(axis=3)
    w = (r7[:, AI] + r7[:, BI])[:, :, None, :] * np.ones((1, 1, P, 1))
    cmin, cmax = cos_range(ang, w)
    Emax = 1 + 2 * cmax.sum(axis=3); Emin = 1 + 2 * cmin.sum(axis=3)
    absmax = np.maximum(np.abs(Emax), np.abs(Emin)); exact = absmax.sum(axis=(1, 2))
    keep = (Emin > 0) | (Emax < 0); sig = np.sign(E); ks = keep * sig; sn = np.sin(ang)
    grad = np.zeros((N, P))
    for q in range(P):
        for u in range(nu):
            t = (ks[:, q, :] * sn[:, q, :, u]).sum(axis=1)
            grad[:, AI[q, u]] += -2 * t; grad[:, BI[q, u]] += 2 * t
    R = (w ** 2).sum(axis=3)
    lin = (ks * E).sum(axis=(1, 2)) + (np.abs(grad[:, 1:]) * r).sum(axis=1) + (keep * R).sum(axis=(1, 2))
    other = (absmax * (~keep)).sum(axis=(1, 2))
    U = np.minimum(lin + other, exact) / P ** 2
    smooth = keep.all(axis=(1, 2))
    smin, smax = sin_range(ang, w)
    glo = np.zeros((N, P)); ghi = np.zeros((N, P))
    for q in range(P):
        for u in range(nu):
            for idx, k0 in ((AI[q, u], -2.0), (BI[q, u], 2.0)):
                k = k0 * sig[:, q, :]
                glo[:, idx] += np.minimum(k * smin[:, q, :, u], k * smax[:, q, :, u]).sum(axis=1)
                ghi[:, idx] += np.maximum(k * smin[:, q, :, u], k * smax[:, q, :, u]).sum(axis=1)
    mono = smooth & ((glo[:, 1:] > 1e-12) | (ghi[:, 1:] < -1e-12)).any(axis=1)
    return U, smooth, mono, np.abs(E).sum(axis=(1, 2)) / P ** 2


if __name__ == "__main__":
    {"check": check, "prove": prove, "control": control}[sys.argv[1] if len(sys.argv) > 1 else "check"]()
