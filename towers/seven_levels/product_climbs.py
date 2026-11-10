"""product_climbs.py -- read after round 10's run (not registered): climbing from products of smaller arrays' bests.

Round 10's searches ended below states that were already known.  On five wheels of 3 the best climb reached 6.082020,
but the four-wheel best (98/27) times a one-wheel best (1/3) has 517/81 = 6.382716, and on either side.  On three wheels
of 7 the sides' bests, 7.238233 and 7.241590, sit below the products 7.435601 (even) and 7.408152 (odd).  This script
  1. finds round 9's best states again on the small arrays, by seeded climbs, and checks them against round 9's values;
  2. on each new array forms every product of two smaller arrays' best states (and of the norm state on three wheels
     of 3), checks that its value is the product's, reads its side, and climbs from it on its side and in the whole
     space;
  3. kicks the best state each side reached by random vectors of relative size 0.05 and 0.3, and climbs again, on the
     side and in the whole space;
  4. reruns the round 10 kick job that found the best state on three wheels of 5, and describes that state.

numpy + scipy + larger_arrays.py.  Six worker processes at below-normal priority, one thread each.  ASCII output;
writes product_climbs.log.
Run:  python product_climbs.py    (about 15 minutes)
"""
import ctypes
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import time

import numpy as np

import larger_arrays as la

HERE = os.path.dirname(os.path.abspath(__file__))
WORKERS = 6
NEW = [(5, 3), (3, 5), (7, 3)]
SPLITS = {(5, 3): [((5, 1), (5, 2))], (3, 5): [((3, 1), (3, 4)), ((3, 2), (3, 3))], (7, 3): [((7, 1), (7, 2))]}
CAP = {(3, 4, "odd"): 20_000, (5, 2, "even"): 20_000, (5, 2, "odd"): 40_000, (7, 2, "even"): 40_000,
       (7, 2, "odd"): 80_000}                                       # climbs allowed to find round 9's best again
KICKS = 20
KICK_SIZES = (0.05, 0.3)
LOG = None
T0 = time.time()


def gentle():
    try:
        ctypes.windll.kernel32.SetPriorityClass(ctypes.c_void_p(-1), 0x00004000)
    except Exception:
        pass


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def round9():
    out = {}
    for part in ("three", "four", "five", "seven"):
        for line in open(os.path.join(HERE, f"many_wheels_{part}.log"), encoding="utf-8"):
            if line.startswith("RESULT "):
                p, n, e, o, w = line.split()[1:]
                out[int(p), int(n)] = {"even": float(e), "odd": float(o)}
    return out


def to_side(arr, psi, side):
    I0, I1, c0, c1, _, _ = arr.sides[side]
    return c0 * psi[I0] + c1 * psi[I1]


def side_of(arr, psi):
    half = float(np.real(np.vdot(psi, psi[arr.neg])))
    return "even" if half > 1 - 1e-9 else "odd" if half < -1 + 1e-9 else None


def look(arr, psi):
    """the half-turn value, the largest |<A_u>| with its sign, and the purity of each wheel"""
    W = arr.wigner(psi[None, :])[0]
    i = np.unravel_index(np.abs(W).argmax(), W.shape)
    return (float(np.real(np.vdot(psi, psi[arr.neg]))), float(arr.D * abs(W[i])), int(np.sign(W[i])),
            la.purities(psi, arr.p, arr.n))


# ------------------------------------------------------------------ the jobs
def regain(job):
    _, p, n, side, target, cap = job
    arr = la.Array(p, n)
    rng = np.random.default_rng([la.SEED, 11, p, n, la.SIDE_CODE[side]])
    k = arr.dim(side)
    best, psi, used = -1.0, None, 0
    while used < cap and best < target - 1e-9:
        m = min(200, cap - used)
        Phi, N, _ = la.ascend(arr, rng.normal(size=(m, k)) + 1j * rng.normal(size=(m, k)), side)
        used += m
        i = int(np.argmax(N))
        if N[i] > best:
            best, psi = float(N[i]), arr.full(Phi[i:i + 1], side)[0]
    return job, best, psi, used


def climb_product(job):
    _, p, n, label, psi, formula = job
    arr = la.Array(p, n)
    N0 = float(arr.negativity(arr.wigner(psi[None, :]))[0])
    side = side_of(arr, psi)
    out = dict(N0=N0, side=side, side_end=float("nan"), side_state=None)
    if side:
        Phi = to_side(arr, psi, side)
        assert np.allclose(arr.full(Phi[None, :], side)[0], psi)
        P, N, _ = la.ascend(arr, Phi[None, :], side)
        out.update(side_end=float(N[0]), side_state=arr.full(P, side)[0])
    P, N, _ = la.ascend(arr, psi[None, :].copy(), "whole")
    out.update(whole_end=float(N[0]), whole_look=look(arr, P[0]))
    return job[:4] + (formula,), out


def kick(job):
    _, p, n, side, mode, eps, psi, tag = job
    arr = la.Array(p, n)
    rng = np.random.default_rng([la.SEED, 11, p, n, 9, tag])
    base = psi if mode == "whole" else to_side(arr, psi, mode)
    g = rng.normal(size=(KICKS, len(base))) + 1j * rng.normal(size=(KICKS, len(base)))
    g /= np.linalg.norm(g, axis=1, keepdims=True)
    Phi, N, left = la.ascend(arr, base[None, :] + eps * g, mode)
    i = int(np.argmax(N))
    best = arr.full(Phi[i:i + 1], mode)[0]
    return job[:6], float(N[i]), int((N > N[i] - 1e-9).sum()), left, look(arr, best)


def rerun_kick(job):
    return job, la.kick_job(("kick", 5, 3, 2, 0.3, la.KICKS[5, 3], 100))


def run_any(job):
    return {"regain": regain, "product": climb_product, "kick": kick, "rerun": rerun_kick}[job[0]](job)


def main():
    global LOG
    import multiprocessing as mp
    gentle()
    LOG = open(os.path.join(HERE, "product_climbs.log"), "w", encoding="utf-8")
    R9 = round9()
    S = lambda N: 1 + 2 * N
    say("1. round 9's best states, found again by seeded climbs")
    small = sorted({a for k in NEW for pair in SPLITS[k] for a in pair})
    todo = [("regain", p, n, side, R9[p, n][side], CAP.get((p, n, side), 5_000)) for (p, n) in small
            for side in ("even", "odd")]
    states = {}
    with mp.Pool(WORKERS, initializer=gentle) as pool:
        for job, best, psi, used in pool.imap_unordered(regain, todo):
            _, p, n, side, target, cap = job
            states[p, n, side] = (best, psi)
            say(f"REGAIN {p} {n} {side} {best:.12f} {target:.12f} {used} {abs(best - target) < 1e-9}")
    states[3, 3, "norm"] = (17 / 9, la.norm_state(3, 3, 1))
    say()
    say("2. the products of two smaller arrays' best states on each new array, and the climbs from them")
    todo, labels = [], {}
    for (p, n) in NEW:
        for a, b in SPLITS[p, n]:
            for sa in ("even", "odd", "norm"):
                for sb in ("even", "odd", "norm"):
                    if (a + (sa,)) not in states or (b + (sb,)) not in states:
                        continue
                    (Na, pa), (Nb, pb) = states[a + (sa,)], states[b + (sb,)]
                    label = f"{a[1]}-of-{p}-{sa}*{b[1]}-of-{p}-{sb}"
                    todo.append(("product", p, n, label, np.kron(pa, pb), (S(Na) * S(Nb) - 1) / 2))
    todo.append(("rerun",))
    reached, rerun = {}, None
    with mp.Pool(WORKERS, initializer=gentle) as pool:
        for res in pool.imap_unordered(run_any, todo):
            if res[0][0] == "rerun":
                rerun = res[1]
                continue
            (_, p, n, label, formula), o = res
            h, mA, sg, pur = o["whole_look"]
            say(f"PRODUCT {p} {n} {label} {o['N0']:.12f} {formula:.12f} {o['side']} {o['side_end']:.12f} "
                f"{o['whole_end']:.12f} {h:+.6f} {mA:.6f} {sg:+d}")
            if o["side"] and o["side_end"] > reached.get((p, n, o["side"]), (-1, None))[0]:
                reached[p, n, o["side"]] = (o["side_end"], o["side_state"])
    say()
    say("3. kicks of the best state each side reached from the products")
    todo = []
    for tag, ((p, n, side), (val, psi)) in enumerate(sorted(reached.items(), key=lambda t: t[0])):
        say(f"  {n} wheels of {p}, {side}: kicking the state at {val:.12f}")
        for mode in (side, "whole"):
            for j, eps in enumerate(KICK_SIZES):
                todo.append(("kick", p, n, side, mode, eps, psi, 100 * tag + 10 * (mode == "whole") + j))
    with mp.Pool(WORKERS, initializer=gentle) as pool:
        for job, best, count, left, (h, mA, sg, pur) in pool.imap_unordered(kick, todo):
            _, p, n, side, mode, eps = job
            say(f"KICKP {p} {n} {side} {mode} {eps} {KICKS} {best:.12f} {count} {left} {h:+.6f} {mA:.6f} {sg:+d} "
                f"{pur}")
    say()
    say("4. the best state found on three wheels of 5 (round 10's kick of norm-type state c = 2 at size 0.3), again")
    job, values, reps, stuck, dt = rerun
    top = max(reps)
    psi = reps[top][0]
    arr = la.Array(5, 3)
    norm_sorted = {c: np.sort(arr.wigner(la.norm_state(5, 3, c)[None, :])[0].ravel()) for c in la.norm_classes(5)}
    d = la.describe(arr, psi, norm_sorted)
    h, mA, sg, pur = look(arr, psi)
    W = arr.wigner(psi[None, :])[0]
    ov = [abs(np.vdot(la.norm_state(5, 3, c), psi)) ** 2 for c in range(1, 5)]
    say(f"BEST53 {top:.12f} {int((values > top - 1e-9).sum())} {h:+.9f} {mA:.9f} {sg:+d} {d['m2']:.9f} {d['zeros']} "
        f"{d['lag']} {d['flat']} {d['match']} {pur}")
    say(f"  its overlaps with the norm-type states c = 1..4: {', '.join(f'{x:.6f}' for x in ov)}; its Wigner function "
        f"takes {len(np.unique(np.round(W, 10)))} distinct values; the next values this kick job reached: "
        + ", ".join(f"{v:.9f}" for v in sorted(reps, reverse=True)[1:6]))
    say(f"[{time.time() - T0:.0f} s]")
    LOG.close()


if __name__ == "__main__":
    main()
