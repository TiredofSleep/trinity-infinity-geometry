"""larger_arrays.py -- round 10 of PREREG.md: the arrays round 9 could not reach, committed with its predictions
before the run.

    "you are only spinning one wheel... imagine a 10x10 of wheels or larger?"  -- the author, 9 November 2026

Round 9 wrote out all D^2 phase-point operators, which stops near D = 81.  This script never forms them.  For a state
psi on n wheels of p levels (D = p^n), with <a|A_(q,k)|b> = [a + b = 2q] w^(k.(a - b)) as in round 3,
    W(q, k) = (1/D) sum_s conj(psi(q + s)) psi(q - s) w^(2k.s),
so for each q the Wigner function is one n-dimensional Fourier transform over s.  The sign matrix sum_u s_u A_u / D has
the entry G((a + b)/2, a - b) at (a, b), where G is the same transform of the signs over k.  A state even or odd under
the half turn has W(-u) = W(u), so on a side only half of the q's are computed.  The climbs are round 3's sign
ascent, unchanged; `calibrate` checks them against round 3's code from the same starts on arrays already run.

The norm-type states.  For the field with q = p^n elements and its norm N(x) = x^((q-1)/(p-1)), which lies in F_p,
    psi_c = sum_x w^(c N(x)) |x> / sqrt q,    c = 1, ..., p - 1,
with x written in a polynomial basis (another basis is a Clifford operation away).  psi_-c is the complex conjugate of
psi_c and has the same values, so c runs over 1 at 3 levels, 1 and 2 at 5, and 1, 2 and 3 at 7.

For each new array (three wheels of 5, five wheels of 3, three wheels of 7) `run` climbs from random states on the even
side, on the odd side and in the whole space; it climbs from each norm-type state itself and from random kicks of it;
and for every best state it logs the half-turn value, the largest |<A_u>|, the purity of each wheel, M2, the zero set
of the Weyl expectations, and whether its Wigner values are a norm-type state's.  `combine` scores V0 to V6.

numpy + scipy.  `run` uses six worker processes at below-normal priority, one thread each.  ASCII output.
Run:  python larger_arrays.py calibrate   (about two minutes; writes larger_arrays_calibrate.log)
      python larger_arrays.py run         (about three hours; writes larger_arrays_run.log)
      python larger_arrays.py combine     (writes larger_arrays_combined.log)
Set LARGER_ARRAYS_SMOKE=1 for a quick test of the code on arrays already run; its scores mean nothing.
"""
import itertools
import os
import sys

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import time

import numpy as np
import scipy.fft as sf
import scipy.linalg as sl

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20261110
SMOKE = os.environ.get("LARGER_ARRAYS_SMOKE") == "1"
TAG = "_smoke" if SMOKE else ""
WORKERS = 6
SIDE_CODE = {"even": 0, "odd": 1, "whole": 2}
MODULI = {(3, 3): [2, 2, 0, 1], (3, 4): [1, 0, 1, 1, 1], (5, 2): [2, 0, 1], (5, 3): [1, 1, 0, 1],
          (7, 3): [1, 1, 0, 1], (3, 5): [1, 2, 0, 0, 0, 1]}          # monic, constant term first
# (p, n): climbs on the even side, the odd side and the whole space; climbs per job; climbs per batch
PLAN = {(5, 3): ({"even": 40_000, "odd": 40_000, "whole": 10_000}, {"even": 5_000, "odd": 5_000, "whole": 2_500}, 100),
        (3, 5): ({"even": 4_000, "odd": 4_000, "whole": 800}, {"even": 500, "odd": 500, "whole": 100}, 40),
        (7, 3): ({"even": 2_000, "odd": 2_000, "whole": 400}, {"even": 250, "odd": 250, "whole": 50}, 20)}
KICKS = {(5, 3): 500, (3, 5): 100, (7, 3): 50}                         # per norm-type state and per kick size
KICK_SIZES = (0.05, 0.3)
if SMOKE:
    PLAN = {(3, 3): ({"even": 300, "odd": 300, "whole": 300}, {"even": 150, "odd": 150, "whole": 150}, 50),
            (5, 2): ({"even": 200, "odd": 200, "whole": 200}, {"even": 100, "odd": 100, "whole": 100}, 50),
            (3, 4): ({"even": 20, "odd": 20, "whole": 10}, {"even": 10, "odd": 10, "whole": 5}, 10)}
    KICKS = {(3, 3): 20, (5, 2): 20, (3, 4): 4}
LOG = None
T0 = time.time()


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def gentle():
    try:
        import ctypes
        ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x00004000)
    except Exception:
        pass


# ------------------------------------------------------------------ the structured machinery
class Array:
    """n wheels of p levels: index tables for the Wigner function and the sign matrix, and the two sides' bases"""

    def __init__(self, p, n):
        self.p, self.n, self.D = p, n, p ** n
        dg = np.array(list(itertools.product(range(p), repeat=n)), dtype=np.int64).reshape(-1, n)  # kron order
        wt = p ** np.arange(n - 1, -1, -1)
        idx = lambda v: ((v % p) @ wt).astype(np.int64)
        D = self.D
        self.digits = dg
        self.plus = idx(dg[:, None, :] + dg[None, :, :])                  # [q, s] -> q + s
        self.minus = idx(dg[:, None, :] - dg[None, :, :])                 # [q, s] -> q - s ; [a, b] -> a - b
        self.two = idx(2 * dg)                                            # k -> 2k
        self.half = idx(pow(2, -1, p) * (dg[:, None, :] + dg[None, :, :]))  # [a, b] -> (a + b)/2
        self.neg = idx(-dg)
        self.shape = (p,) * n
        self.axes = tuple(range(2, 2 + n))
        self.R = np.array([x for x in range(1, D) if x < self.neg[x]], dtype=np.int64)   # one of each pair {x, -x}
        self.qrep = np.concatenate(([0], self.R))                          # half of the q's
        self.qweight = np.where(self.qrep == 0, 1.0, 2.0)
        pos = np.full(D, -1)
        pos[self.qrep] = np.arange(len(self.qrep))
        self.whole_flat = (self.half * D + self.minus).ravel()
        self.sides = {}
        for name, sg in (("even", 1.0), ("odd", -1.0)):
            I0 = self.qrep.copy() if name == "even" else self.R.copy()   # basis |0>, (|x> + sg |-x>)/sqrt 2
            I1 = self.neg[I0]
            c0 = np.where(I0 == 0, 1.0, 2 ** -0.5)
            c1 = np.where(I0 == 0, 0.0, sg * 2 ** -0.5)
            flat, coef = {}, {}
            for a, Ia, ca in ((0, I0, c0), (1, I1, c1)):
                for b, Ib, cb in ((0, I0, c0), (1, I1, c1)):
                    q = self.half[Ia[:, None], Ib[None, :]]
                    t = self.minus[Ia[:, None], Ib[None, :]]
                    inrep = pos[q] >= 0
                    flat[a, b] = (np.where(inrep, pos[q], pos[self.neg[q]]) * D
                                  + np.where(inrep, t, self.neg[t])).ravel()  # G(-r, t) = G(r, -t)
                    coef[a, b] = np.outer(ca, cb).ravel()
            self.sides[name] = (I0, I1, c0, c1, flat, coef)

    def dim(self, side):
        return self.D if side == "whole" else len(self.sides[side][0])

    def full(self, Phi, side):
        """coordinates on a side's basis -> states in C^D"""
        if side == "whole":
            return Phi
        I0, I1, c0, c1, _, _ = self.sides[side]
        Psi = np.zeros((len(Phi), self.D), complex)
        Psi[:, I0] += Phi * c0
        Psi[:, I1] += Phi * c1
        return Psi

    def wigner(self, Psi, rows=None):
        """W[:, q, k] = <psi|A_(q,k)|psi> / D for q in `rows` (all q by default)"""
        rows = np.arange(self.D) if rows is None else rows
        B, D, h = len(Psi), self.D, len(rows)
        f = Psi.conj()[:, self.plus[rows]] * Psi[:, self.minus[rows]]
        F = sf.ifftn(f.reshape((B, h) + self.shape), axes=self.axes, workers=1, overwrite_x=True).reshape(B, h, D)
        return F[:, :, self.two].real

    def side_wigner(self, Psi, side):
        return self.wigner(Psi, None if side == "whole" else self.qrep)

    def negativity(self, W, side="whole"):
        if side == "whole":
            return (np.abs(W).sum(axis=(1, 2)) - 1) / 2
        return ((np.abs(W).sum(axis=2) * self.qweight).sum(axis=1) - 1) / 2

    def side_matrix(self, S, side):
        """signs at (q, k), all q (whole) or the half q's (a side) -> Q^dagger (sum_u s_u A_u / D) Q"""
        B, h, D = S.shape
        G = sf.ifftn(S.reshape((B, h) + self.shape), axes=self.axes, workers=1).reshape(B, h * D)
        if side == "whole":
            return G[:, self.whole_flat].reshape(B, D, D)
        _, _, _, _, flat, coef = self.sides[side]
        k = self.dim(side)
        M = np.zeros((B, k * k), complex)
        for key in flat:
            M += coef[key] * G[:, flat[key]]
        return M.reshape(B, k, k)


def top_vectors(M):
    k = M.shape[-1]
    if k < 100:
        return np.linalg.eigh(M)[1][:, :, -1]
    out = np.empty(M.shape[:2], complex)
    for i, h in enumerate(M):
        out[i] = sl.eigh(h, subset_by_index=[k - 1, k - 1], driver="evr", overwrite_a=True, check_finite=False)[1][:, 0]
    return out


def ascend(arr, Phi, side, max_steps=1000):
    """round 3's sign ascent: give each point the sign of the state's Wigner value there, replace the state by the top
    eigenvector of sum_u s_u A_u (on the side), repeat until the signs stop changing"""
    Phi = Phi / np.linalg.norm(Phi, axis=1, keepdims=True)
    B = len(Phi)
    h = arr.D if side == "whole" else len(arr.qrep)
    signs = np.zeros((B, h, arr.D), np.int8)
    live = np.arange(B)
    for _ in range(max_steps):
        s = np.where(arr.side_wigner(arr.full(Phi[live], side), side) >= 0, 1, -1).astype(np.int8)
        moving = (s != signs[live]).reshape(len(live), -1).any(axis=1)
        live, s = live[moving], s[moving]
        if len(live) == 0:
            break
        Phi[live] = top_vectors(arr.side_matrix(s.astype(float), side))
        signs[live] = s
    N = arr.negativity(arr.side_wigner(arr.full(Phi, side), side), side)
    return Phi, N, len(live)


# ------------------------------------------------------------------ the field and its norm-type states
def poly_mod(a, m, p):
    a = [x % p for x in a]
    while len(a) >= len(m):
        c = a[-1]
        if c:
            for i in range(len(m)):
                a[len(a) - len(m) + i] = (a[len(a) - len(m) + i] - c * m[i]) % p
        a.pop()
    return a


def irreducible(m, p):
    """no monic factor of degree 1 .. deg/2"""
    n = len(m) - 1
    for d in range(1, n // 2 + 1):
        for low in itertools.product(range(p), repeat=d):
            if not any(poly_mod(list(m), list(low) + [1], p)):
                return False
    return True


def norm_values(p, n):
    """N(x) = x^((q-1)/(p-1)) for x = c_0 + c_1 t + ... (index: c_0 the first wheel), in the field F_p[t]/(MODULI)"""
    m = MODULI[p, n]
    assert irreducible(m, p)

    def mul(x, y):
        prod = [0] * (2 * n - 1)
        for i in range(n):
            for k in range(n):
                prod[i + k] += x[i] * y[k]
        r = poly_mod(prod, m, p)
        return r + [0] * (n - len(r))

    e = (p ** n - 1) // (p - 1)
    out = []
    for x in itertools.product(range(p), repeat=n):
        r, b, k = [1] + [0] * (n - 1), list(x), e
        while k:
            if k & 1:
                r = mul(r, b)
            b, k = mul(b, b), k >> 1
        assert not any(r[1:]), "the norm lies in F_p"
        out.append(r[0])
    return np.array(out)


def norm_state(p, n, c):
    return np.exp(2j * np.pi * c * norm_values(p, n) / p) / np.sqrt(p ** n)


def norm_classes(p):
    return list(range(1, (p - 1) // 2 + 1))


# ------------------------------------------------------------------ what a state looks like
def weyl_sizes(arr, psi):
    """|<psi| Z^b X^a |psi>| for every (a, b), as a D x D array"""
    V = psi.conj()[arr.plus] * psi[None, :]                               # [a, x] = conj psi(x + a) psi(x)
    return np.abs(sf.fftn(V.reshape((arr.D,) + arr.shape), axes=tuple(range(1, 1 + arr.n)), workers=1)
                  ).reshape(arr.D, arr.D)


def zero_set(arr, psi, tol=1e-6):
    """the Weyl operators with zero expectation: their number, and whether with the identity they form a Lagrangian
    (a subgroup of D elements on which the symplectic form vanishes); and whether |chi| = 1/sqrt D everywhere else"""
    C = weyl_sizes(arr, psi)
    Z = np.argwhere(C < tol)
    flat = bool(np.allclose(C[C >= tol][1:], arr.D ** -0.5, atol=1e-6)) if (C >= tol).sum() > 1 else False
    if len(Z) != arr.D - 1:
        return len(Z), False, flat
    pts = np.vstack([[0, 0], Z])
    a, b = arr.digits[pts[:, 0]], arr.digits[pts[:, 1]]
    sym = ((a @ b.T) - (b @ a.T)) % arr.p
    keys = set(map(tuple, np.hstack([a, b])))
    closed = all(tuple(np.hstack([(a[i] + a[j]) % arr.p, (b[i] + b[j]) % arr.p])) in keys
                 for i in range(1, len(pts)) for j in range(i, len(pts)))
    return len(Z), bool(closed and not sym.any()), flat


def purities(psi, p, n):
    T = psi.reshape((p,) * n)
    out = []
    for i in range(n):
        M = np.moveaxis(T, i, 0).reshape(p, -1)
        rho = M @ M.conj().T
        out.append(round(float(np.real(np.trace(rho @ rho))), 6))
    return out


def sre2(arr, psi):
    """the stabilizer Renyi entropy M2 = -ln( sum over the D^2 Weyl operators of |<psi|W|psi>|^4 / D )"""
    return float(-np.log((weyl_sizes(arr, psi) ** 4).sum() / arr.D))


def describe(arr, psi, norm_sorted):
    W = arr.wigner(psi[None, :])[0]
    Ws = np.sort(W.ravel())
    match = [c for c, Wc in norm_sorted.items() if np.allclose(Ws, Wc, atol=1e-9)]
    nz, lag, flat = zero_set(arr, psi)
    return dict(half=float(np.real(np.vdot(psi, psi[arr.neg]))), maxA=float(arr.D * np.abs(W).max()),
                pur=purities(psi, arr.p, arr.n), m2=sre2(arr, psi), zeros=nz, lag=lag, flat=flat,
                match=",".join(map(str, match)) if match else "none")


# ------------------------------------------------------------------ the jobs
def search_job(job):
    gentle()
    kind, p, n, side, climbs, chunk, batch = job
    arr = Array(p, n)
    rng = np.random.default_rng([SEED, 10, p, n, SIDE_CODE[side], chunk])
    k = arr.dim(side)
    values, reps, stuck, t = [], {}, 0, time.time()
    for b in range(0, climbs, batch):
        m = min(batch, climbs - b)
        Phi, N, left = ascend(arr, rng.normal(size=(m, k)) + 1j * rng.normal(size=(m, k)), side)
        values.append(N)
        stuck += left
        for i in np.argsort(-N)[:30]:
            key = round(float(N[i]), 9)
            if len(reps.setdefault(key, [])) < 3:
                reps[key].append(arr.full(Phi[i:i + 1], side)[0])
        reps = {key: reps[key] for key in sorted(reps)[-12:]}
    return job, np.concatenate(values), reps, stuck, time.time() - t


def kick_job(job):
    gentle()
    kind, p, n, c, eps, count, batch = job
    arr = Array(p, n)
    rng = np.random.default_rng([SEED, 10, p, n, 3, c, int(eps * 100)])
    psi = norm_state(p, n, c)
    values, reps, stuck, t = [], {}, 0, time.time()
    for b in range(0, count, batch):
        m = min(batch, count - b)
        g = rng.normal(size=(m, arr.D)) + 1j * rng.normal(size=(m, arr.D))
        g /= np.linalg.norm(g, axis=1, keepdims=True)
        Phi, N, left = ascend(arr, psi[None, :] + eps * g, "whole")
        values.append(N)
        stuck += left
        for i in np.argsort(-N)[:10]:
            key = round(float(N[i]), 9)
            if len(reps.setdefault(key, [])) < 2:
                reps[key].append(Phi[i])
        reps = {key: reps[key] for key in sorted(reps)[-6:]}
    return job, np.concatenate(values), reps, stuck, time.time() - t


def run_job(job):
    return search_job(job) if job[0] == "search" else kick_job(job)


def jobs():
    """every search chunk, the first chunk of each search first, then the kicks"""
    out, kick = [], []
    for (p, n), (climbs, per, batch) in PLAN.items():
        for side in ("whole", "even", "odd"):
            for chunk in range(-(-climbs[side] // per[side])):
                out.append(("search", p, n, side, min(per[side], climbs[side] - chunk * per[side]), chunk, batch))
        for c in norm_classes(p):
            for eps in KICK_SIZES:
                kick.append(("kick", p, n, c, eps, KICKS[p, n], batch))
    return sorted(out, key=lambda j: j[5]) + kick


def run():
    global LOG
    import multiprocessing as mp
    LOG = open(os.path.join(HERE, f"larger_arrays_run{TAG}.log"), "w", encoding="utf-8")
    todo = jobs()
    arrays = {(p, n): Array(p, n) for (p, n) in PLAN}
    norm_sorted = {(p, n): {c: np.sort(arrays[p, n].wigner(norm_state(p, n, c)[None, :])[0].ravel())
                            for c in norm_classes(p)} for (p, n) in PLAN}
    say(f"round 10: {len(todo)} jobs on {WORKERS} workers; seed {SEED}" + ("; SMOKE TEST, scores mean nothing" if SMOKE
                                                                         else ""))
    for (p, n), (climbs, per, batch) in PLAN.items():
        D = p ** n
        say(f"  {n} wheels of {p}: D = {D}, ceiling (sqrt D - 1)/2 = {(np.sqrt(D) - 1) / 2:.9f}; climbs even "
            f"{climbs['even']}, odd {climbs['odd']}, whole {climbs['whole']}; kicks {KICKS[p, n]} per norm-type "
            f"state (c = {norm_classes(p)}) and per size {KICK_SIZES}")
    pending = {}
    for (p, n), (climbs, per, batch) in PLAN.items():
        for side in ("even", "odd", "whole"):
            pending[p, n, side] = -(-climbs[side] // per[side])
    merged = {}
    with mp.Pool(WORKERS, initializer=gentle) as pool:
        for job, values, reps, stuck, dt in pool.imap_unordered(run_job, todo):
            if job[0] == "kick":
                _, p, n, c, eps, count, _ = job
                best = values.max()
                say(f"KICK {p} {n} {c} {eps} {count} {best:.12f} {int((values > best - 1e-9).sum())} {stuck} "
                    f"[{dt:.0f} s; {time.time() - T0:.0f} s]")
                continue
            _, p, n, side, climbs, chunk, _ = job
            m = merged.setdefault((p, n, side), {"values": [], "reps": {}, "stuck": 0})
            m["values"].append(values)
            m["stuck"] += stuck
            for key, states in reps.items():
                m["reps"].setdefault(key, []).extend(states)
            say(f"  job {n} wheels of {p}, {side}, chunk {chunk}: {climbs} climbs done [{dt:.0f} s; "
                f"{time.time() - T0:.0f} s]")
            pending[p, n, side] -= 1
            if pending[p, n, side] == 0:
                V = np.concatenate(m["values"])
                best = V.max()
                tops = sorted(m["reps"], reverse=True)
                say(f"RESULT {p} {n} {side} {best:.12f} {int((V > best - 1e-9).sum())} {len(V)} {m['stuck']}")
                say(f"  the next tops: " + ", ".join(f"{v:.9f}" for v in tops[1:6]))
                for i, psi in enumerate(m["reps"][tops[0]][:3]):
                    d = describe(arrays[p, n], psi, norm_sorted[p, n])
                    say(f"STATE {p} {n} {side} {i + 1} {d['half']:+.9f} {d['maxA']:.9f} {d['m2']:.9f} {d['zeros']} "
                        f"{d['lag']} {d['flat']} {d['match']} {d['pur']}")
    for (p, n), arr in arrays.items():
        for c in norm_classes(p):
            psi = norm_state(p, n, c)
            Nc = arr.negativity(arr.wigner(psi[None, :]))[0]
            _, Nfix, _ = ascend(arr, psi[None, :].copy(), "whole")
            d = describe(arr, psi, norm_sorted[p, n])
            say(f"NORM {p} {n} {c} {Nc:.12f} {Nfix[0]:.12f} {d['half']:+.9f} {d['maxA']:.9f} {d['m2']:.9f} "
                f"{d['zeros']} {d['lag']} {d['flat']}")
    say(f"[{time.time() - T0:.0f} s]")
    LOG.close()


# ------------------------------------------------------------------ the check against round 3's code
def calibrate():
    global LOG
    import round3 as r3
    import many_wheels as mw
    LOG = open(os.path.join(HERE, "larger_arrays_calibrate.log"), "w", encoding="utf-8")
    rng = np.random.default_rng([SEED, 10, 0])
    say("the structured code against round 3's, from the same starts, on arrays round 9 ran")
    total = same = 0
    for p, n, side, B in ((3, 3, "even", 300), (3, 3, "odd", 300), (3, 3, "whole", 300), (5, 2, "even", 300),
                          (5, 2, "odd", 300), (7, 2, "even", 100), (3, 4, "even", 40), (3, 4, "odd", 40)):
        arr = Array(p, n)
        A = mw.array_points(p, n)
        E, O = mw.array_sides(p, n)
        k = arr.dim(side)
        Phi0 = rng.normal(size=(B, k)) + 1j * rng.normal(size=(B, k))
        if side == "whole":
            Phi_mw, Ak = Phi0.copy(), A
        else:
            Q = arr.full(np.eye(k, dtype=complex), side).T
            Qmw = E if side == "even" else O
            Phi_mw = (Qmw.conj().T @ (Q @ Phi0.T)).T                     # the same states in round 9's coordinates
            Ak = np.matmul(Qmw.conj().T, np.matmul(A, Qmw))
        _, N_old, _ = r3.ascend(Phi_mw, Ak, p ** n)
        Phi, N_new, _ = ascend(arr, Phi0.copy(), side)
        Wd = r3.wigner(arr.full(Phi, side), A, p ** n)
        err_w = np.abs(np.sort(Wd, axis=1) - np.sort(arr.wigner(arr.full(Phi, side)).reshape(B, -1), axis=1)).max()
        ok = int((np.abs(N_old - N_new) < 1e-9).sum())
        total, same = total + B, same + ok
        say(f"  {n} wheels of {p}, {side}: same end value from {ok} of {B} starts; Wigner values against the dense "
            f"operators within {err_w:.1e}")
    known = []
    for p, n, target in ((3, 3, 17 / 9), (3, 4, 2000 / 729), (5, 2, 0.0)):
        arr = Array(p, n)
        got = arr.negativity(arr.wigner(norm_state(p, n, 1)[None, :]))[0]
        known.append(abs(got - target) < 1e-9)
        say(f"  the norm state on {n} wheels of {p}: {got:.12f} (known {target:.12f})")
    say(f"CALIBRATE {same} {total} {all(known)}")
    LOG.close()


# ------------------------------------------------------------------ the scores
def combine():
    global LOG
    R9 = {}
    for part in ("three", "four", "five", "seven"):
        for line in open(os.path.join(HERE, f"many_wheels_{part}.log"), encoding="utf-8"):
            if line.startswith("RESULT "):
                p, n, e, o, w = line.split()[1:]
                R9[int(p), int(n)] = (float(e), float(o), float(w))
    R9[3, 3] = R9[3, 3][:2] + (max(R9[3, 3][2], 17 / 9),)                # the norm state found after round 9's run
    res, kicks, norms, states = {}, {}, {}, {}
    for line in open(os.path.join(HERE, f"larger_arrays_run{TAG}.log"), encoding="utf-8"):
        f = line.split()
        if line.startswith("RESULT "):
            res[int(f[1]), int(f[2]), f[3]] = (float(f[4]), int(f[5]), int(f[6]), int(f[7]))
        elif line.startswith("KICK "):
            kicks[int(f[1]), int(f[2]), int(f[3]), float(f[4])] = (float(f[6]), int(f[7]), int(f[8]))
        elif line.startswith("NORM "):
            norms[int(f[1]), int(f[2]), int(f[3])] = (float(f[4]), float(f[5]))
        elif line.startswith("STATE "):
            states.setdefault((int(f[1]), int(f[2]), f[3]), []).append(f[4:12])
    cal = [l.split() for l in open(os.path.join(HERE, "larger_arrays_calibrate.log"), encoding="utf-8")
           if l.startswith("CALIBRATE ")][0]
    LOG = open(os.path.join(HERE, f"larger_arrays_combined{TAG}.log"), "w", encoding="utf-8")
    S = lambda N: 1 + 2 * N
    Nof = lambda s: (s - 1) / 2
    tol = 1e-9
    best, normbest, products, side_of = {}, {}, {}, {}
    for (p, n) in PLAN:
        D = p ** n
        ceiling = (np.sqrt(D) - 1) / 2
        e, o, w = (res[p, n, s][0] for s in ("even", "odd", "whole"))
        nb = max(norms[p, n, c][0] for c in norm_classes(p))
        kb = max(v[0] for key, v in kicks.items() if key[:2] == (p, n))
        normbest[p, n] = nb
        best[p, n] = max(e, o, w, kb, nb, max(norms[p, n, c][1] for c in norm_classes(p)))
        side_of[p, n] = "even" if e > o + tol else "odd" if o > e + tol else "tie"
        cands = [S(max(R9[p, m])) * S(max(R9[p, n - m])) for m in range(1, n) if (p, m) in R9 and (p, n - m) in R9]
        products[p, n] = Nof(max(cands)) if cands else float("nan")
        say(f"  {n} wheels of {p} (D = {D}): even {e:.9f}, odd {o:.9f}, whole {w:.9f}; kicks {kb:.9f}; best norm-type "
            f"state {nb:.9f}; best of all {best[p, n]:.9f} = {best[p, n] / ceiling:.4f} of the ceiling {ceiling:.6f}; "
            f"best product of smaller arrays' bests {products[p, n]:.9f}")
        for c in norm_classes(p):
            say(f"    norm-type state c = {c}: {norms[p, n, c][0]:.12f}; the ascent from it ends at "
                f"{norms[p, n, c][1]:.12f}")
        for side in ("even", "odd", "whole"):
            for st in states.get((p, n, side), [])[:1]:
                say(f"    {side} best: half-turn value {st[1]}, largest |<A_u>| {st[2]}, M2 {st[3]}, Weyl zeros {st[4]} "
                    f"(Lagrangian {st[5]}, flat elsewhere {st[6]}), Wigner values of norm-type state c = {st[7]}")
    three = [k for k in ((5, 3), (7, 3)) if k in PLAN]
    v0 = int(cal[1]) == int(cal[2]) and cal[3] == "True"
    v1 = all(best[k] <= normbest[k] + tol for k in three)
    v2 = all(normbest[k] > max(res[k + ("even",)][0], res[k + ("odd",)][0]) + tol for k in three)
    v3 = (3, 5) in PLAN and best[3, 5] > normbest[3, 5] + tol
    v4 = all(best[k] > products[k] + tol for k in PLAN)
    v5 = all(side_of[k] == "odd" for k in PLAN)
    v6 = all(best[k] >= 0.88 * (np.sqrt(k[0] ** k[1]) - 1) / 2 for k in PLAN)
    for name, ok, what in (
            ("V0", v0, f"calibration: the structured code ends where round 3's does from {cal[1]} of {cal[2]} starts, "
                       "and reproduces the known norm states"),
            ("V1", v1, "three wheels of 5 and of 7: nothing found beats the best norm-type state"),
            ("V2", v2, "three wheels of 5 and of 7: the best norm-type state beats both sides' bests"),
            ("V3", v3, "five wheels of 3: the norm state does not win; something found beats it"),
            ("V4", v4, "every new array's best beats every product of smaller arrays' bests"),
            ("V5", v5, "the odd side wins on every new array, an odd number of wheels each (found: "
                       + ", ".join(f"{side_of[k]} at {k[1]} of {k[0]}" for k in PLAN) + ")"),
            ("V6", v6, "every new array's best reaches 88% of its ceiling")):
        say(f"{name} {'HELD' if ok else 'DIED'}: {what}")
    LOG.close()


if __name__ == "__main__":
    gentle()
    part = sys.argv[1] if len(sys.argv) > 1 else "run"
    {"run": run, "calibrate": calibrate, "combine": combine}[part]()
