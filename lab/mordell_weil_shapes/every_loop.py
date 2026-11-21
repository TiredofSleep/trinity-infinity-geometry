"""every_loop.py -- the registered round "every loop fails a little"
(registered/REGISTERED_2026-11-21_every_loop_fails_a_little.md).

The author's sentence (20 November 2026): "every loop fails a little, none fails badly". Read as: no curve whose
isogeny class has more than one curve (a loop) has a rank-2 Mordell-Weil lattice of elongation above 5.

  python -I every_loop.py selftest                         synthetic lattices only: reduction, neighbours, bootstrap
  python -I every_loop.py compute DATA_DIR PARTS_DIR [W]   heights of every curve of every rank-2 class (W workers)
  python -I every_loop.py score PARTS_DIR                  the registered criteria L1-L3, then the description

DATA_DIR holds Cremona's allgens tables: every file named allgens.* below it is read. The compute step runs at
below-normal priority with at most W worker processes (default 4). Needs numpy and PARI through cypari (or cypari2).
"""
import glob
import json
import math
import os
import re
import subprocess
import sys
import time

LINE = re.compile(r'(\d+) (\w+) (\d+) \[([-\d,]+)\] (\d+) \[([\d,]*)\] ?(.*)')
PT = re.compile(r'\[(-?\d+):(-?\d+):(-?\d+)\]')
FAIL, BAD = 2.0, 5.0                 # thin: elongation above 2; fails badly: above 5 (density below pi/20)
SEED, NBOOT = 20261121, 2000
NMAX = 16                            # largest index n tried when relating a fresh lattice to its optimal partner
BELOW_NORMAL = 0x00004000


def low_priority():
    try:
        import ctypes
        k32 = ctypes.windll.kernel32
        k32.GetCurrentProcess.restype = ctypes.c_void_p
        k32.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_uint]
        k32.SetPriorityClass(k32.GetCurrentProcess(), BELOW_NORMAL)
    except Exception:
        pass


def get_pari():
    try:
        from cypari import pari
    except ImportError:
        import cypari2
        pari = cypari2.Pari()
    pari.allocatemem(2 * 10 ** 8)
    return pari


# ----------------------------------------------------------------------------------------------------------------
# geometry of binary forms
# ----------------------------------------------------------------------------------------------------------------
def reduce_forms(A, B, C):
    """Lagrange-Gauss reduction of positive definite forms (arrays), to |B| <= A <= C"""
    import numpy as np
    A, B, C = np.array(A, float), np.array(B, float), np.array(C, float)
    for _ in range(300):
        sw = A > C
        A[sw], C[sw] = C[sw], A[sw]
        k = np.round(B / A)
        if not k.any():
            break
        C = C - 2 * k * B + k * k * A
        B = B - k * A
    sw = A > C
    A[sw], C[sw] = C[sw], A[sw]
    assert np.all(np.abs(B) <= A / 2 * (1 + 1e-9)) and np.all(A <= C * (1 + 1e-9)), "reduction did not converge"
    return A, B, C


def reduce_tau(t):
    """a point of the upper half plane, reduced to the standard fundamental domain; returns (|Re|, Im)"""
    for _ in range(1000):
        t = complex(t.real - round(t.real), t.imag)
        if abs(t) < 1 - 1e-13:
            t = -1 / t
        else:
            break
    return abs(t.real), t.imag


def tau_of(A, B, C):
    return complex(B / A, math.sqrt(max(A * C - B * B, 0.0)) / A)


def neighbours(n):
    """(a, b, d) with ad = n, 0 <= b < d: tau -> (a tau + b)/d runs over the index-n sublattices of <1, tau>"""
    return [(a, b, n // a) for a in range(1, n + 1) if n % a == 0 for b in range(n // a)]


NEIGH = {n: neighbours(n) for n in range(1, NMAX + 1)}


def relation_index(tau_p, x_f, y_f, tol=1e-7):
    """smallest n <= NMAX with (a tau_p + b)/d equivalent to the fresh shape (x_f, y_f); 0 if none"""
    for n in range(1, NMAX + 1):
        for a, b, d in NEIGH[n]:
            x, y = reduce_tau((a * tau_p + b) / d)
            if abs(y - y_f) <= tol * y_f and abs(x - x_f) <= tol:
                return n
    return 0


# ----------------------------------------------------------------------------------------------------------------
# compute
# ----------------------------------------------------------------------------------------------------------------
def compute_file(fn, out):
    low_priority()
    pari = get_pari()
    classes = {}
    for line in open(fn).read().splitlines():
        m = LINE.match(line.strip())
        if m:
            classes.setdefault((m.group(1), m.group(2)), []).append(m)
    rows, bad, t0 = [], [], time.time()
    for (N, cls), ms in classes.items():
        if not any(m.group(5) == '2' for m in ms):
            continue
        size = len(ms)
        for m in ms:
            label = N + cls + m.group(3)
            if m.group(5) != '2':
                bad.append((label, 'rank differs within its class'))
                continue
            try:
                ai = [int(t) for t in m.group(4).split(',')]
                tors = [int(t) for t in m.group(6).split(',') if t]
                gens = [[int(X), int(Y), int(Z)] for X, Y, Z in PT.findall(m.group(7))[:2]]
                E = pari.ellinit(ai)
                P = [[pari(X) / Z, pari(Y) / Z] for X, Y, Z in gens]
                if len(P) != 2 or not all(pari.ellisoncurve(E, q) for q in P):
                    raise ValueError('generator missing or not on the curve')
                H = pari.ellheightmatrix(E, P)
                G = [[float(H[i][j]) for j in range(2)] for i in range(2)]
                if not G[0][0] * G[1][1] - G[0][1] ** 2 > 0:
                    raise ValueError('regulator not positive')
                bsd = float(pari.ellbsd(E)) if size >= 2 else None
                rows.append(dict(N=int(N), cls=cls, num=int(m.group(3)), size=size, ai=ai, tors=tors, gens=gens,
                                 G=G, bsd=bsd))
            except Exception as e:
                bad.append((label, repr(e)[:100]))
    json.dump(dict(rows=rows, bad=bad), open(out, 'w'))
    print(f"{os.path.basename(fn)}: {len(rows)} curves, {len(bad)} failures, {time.time() - t0:.0f} s", flush=True)


def compute(data_dir, parts_dir, workers=4):
    low_priority()
    files = sorted(glob.glob(os.path.join(data_dir, '**', 'allgens.*'), recursive=True))
    files = [f for f in files if re.search(r'allgens\.\d+-\d+$', f)]
    os.makedirs(parts_dir, exist_ok=True)
    jobs = [(f, os.path.join(parts_dir, os.path.basename(f) + '.json')) for f in files]
    running, t0 = [], time.time()
    print(f"{len(files)} tables, {workers} workers at below-normal priority", flush=True)
    while jobs or running:
        while jobs and len(running) < workers:
            f, o = jobs.pop(0)
            running.append(subprocess.Popen([sys.executable, '-I', os.path.abspath(__file__), 'compute-file', f, o],
                                            creationflags=BELOW_NORMAL if os.name == 'nt' else 0))
        time.sleep(1)
        running = [p for p in running if p.poll() is None]
    print(f"all {len(files)} tables done in {time.time() - t0:.0f} s", flush=True)


# ----------------------------------------------------------------------------------------------------------------
# score
# ----------------------------------------------------------------------------------------------------------------
def boot_q(n2, n5, rng, nboot=NBOOT):
    """bootstrap of q = sum n5 / sum n2 over clusters (one entry per isogeny class)"""
    import numpy as np
    n2, n5, k = np.asarray(n2, float), np.asarray(n5, float), len(n2)
    out = np.empty(nboot)
    for i in range(nboot):
        idx = rng.integers(0, k, k)
        out[i] = n5[idx].sum() / n2[idx].sum()
    return out


def clusters(keys, y):
    """per isogeny class: number above FAIL and above BAD"""
    import numpy as np
    order = {}
    for i, key in enumerate(keys):
        order.setdefault(key, []).append(i)
    n2 = np.array([int(np.sum(y[ix] > FAIL)) for ix in order.values()])
    n5 = np.array([int(np.sum(y[ix] > BAD)) for ix in order.values()])
    return n2, n5


def criterion(name, y_test, keys_test, y_ref, keys_ref, rng):
    import numpy as np
    k5 = int(np.sum(y_test > BAD))
    s2t, s5t = np.mean(y_test > FAIL), np.mean(y_test > BAD)
    s2r, s5r = np.mean(y_ref > FAIL), np.mean(y_ref > BAD)
    qt, qr = s5t / s2t, s5r / s2r
    bt = boot_q(*clusters(keys_test, y_test), rng)
    br = boot_q(*clusters(keys_ref, y_ref), rng)
    se = float(np.std(br - bt, ddof=1))
    diff = qr - qt
    strict = 'PASS' if k5 == 0 else 'MISS'
    graded = 'PASS' if diff > 2 * se else ('MISS' if qt >= qr else 'UNDECIDED')
    print(f"{name}: n = {len(y_test)}; above 5: {k5}  -> strict {strict}")
    print(f"{name}: q = {qt:.5f} (share above 2 {s2t:.4f}, above 5 {s5t:.5f}; bootstrap s.e. {np.std(bt, ddof=1):.5f})")
    print(f"{' ' * len(name)}  against no loop q = {qr:.5f} (share above 2 {s2r:.4f}, above 5 {s5r:.5f}; "
          f"s.e. {np.std(br, ddof=1):.5f})")
    print(f"{' ' * len(name)}  difference {diff:+.5f}, s.e. {se:.5f} ({diff / se:+.1f} s.e.)  -> graded {graded}")
    return strict, graded


def describe(name, y):
    import numpy as np
    d = math.pi / (4 * y)
    print(f"  {name:34s} n={len(y):>7}  above 2 {np.mean(y > 2):.4f}  above 3/5/8/10: "
          f"{int(np.sum(y > 3)):>6} {int(np.sum(y > 5)):>5} {int(np.sum(y > 8)):>4} {int(np.sum(y > 10)):>3}  "
          f"mean density {d.mean():.4f}")


def score(parts_dir):
    import numpy as np
    rows, bad = [], []
    for fn in sorted(glob.glob(os.path.join(parts_dir, '*.json'))):
        d = json.load(open(fn))
        rows += d['rows']
        bad += d['bad']
    print(f"read {len(rows)} curves of rank-2 classes from {len(glob.glob(os.path.join(parts_dir, '*.json')))} "
          f"tables; {len(bad)} failures")
    for b in bad[:20]:
        print("  failure:", b)

    # ---- pipeline check: Omega * Reg * prod c_p / |tors|^2 must agree across an isogeny class ----
    by_class = {}
    for r in rows:
        by_class.setdefault((r['N'], r['cls']), []).append(r)
    opt = {k: next((r for r in v if r['num'] == 1), None) for k, v in by_class.items()}
    reg = lambda r: r['G'][0][0] * r['G'][1][1] - r['G'][0][1] ** 2
    flagged = []
    for r in rows:
        if r['num'] >= 2:
            o = opt[(r['N'], r['cls'])]
            if o is None:
                flagged.append((r, None))
                continue
            ratio = (r['bsd'] * reg(r)) / (o['bsd'] * reg(o))
            if abs(ratio - 1) > 1e-6:
                flagged.append((r, ratio))
    fresh_n = sum(1 for r in rows if r['num'] >= 2)
    print(f"\nPIPELINE: {fresh_n} fresh curves; {len(flagged)} whose BSD quotient Omega*Reg*prod(c_p)/|tors|^2 "
          f"differs from the optimal partner's by more than 1e-6")
    if flagged:
        pari = get_pari()

        def saturate(r):
            E = pari.ellinit(r['ai'])
            P = [[pari(X) / Z, pari(Y) / Z] for X, Y, Z in r['gens']]
            S = pari.ellsaturation(E, P, 100)
            H = pari.ellheightmatrix(E, S)
            G = [[float(H[i][j]) for j in range(2)] for i in range(2)]
            return G, reg(dict(G=G)) / reg(r)

        changed = 0
        for r, ratio in flagged:
            o = opt[(r['N'], r['cls'])]
            G, fr = saturate(r)
            go, fo = saturate(o) if o is not None else (None, 1.0)
            if abs(fr - 1) > 1e-6:
                r['G'] = G
                changed += 1
            if o is not None and abs(fo - 1) > 1e-6:
                o['G'] = go
                changed += 1
            new_ratio = (r['bsd'] * reg(r)) / (o['bsd'] * reg(o)) if o is not None else None
            print(f"  {r['N']}{r['cls']}{r['num']}: quotient {ratio}; regulator after saturation x{fr:.6f} "
                  f"(partner x{fo:.6f}); quotient now {new_ratio}")
        print(f"  generators changed by saturation: {changed}")
    fresh_failed = sum(1 for lab, _ in bad if (mm := re.match(r'\d+[a-z]+(\d+)$', lab)) and int(mm.group(1)) >= 2)
    void = len(flagged) + fresh_failed > 0.01 * fresh_n
    print(f"  fresh curves that failed to compute: {fresh_failed}; flagged or failed above 1% (round void): {void}")

    # ---- shapes ----
    G = np.array([r['G'] for r in rows], float)
    A, B, C = reduce_forms(G[:, 0, 0], G[:, 0, 1], G[:, 1, 1])
    x, y = np.abs(B) / A, np.sqrt(A * C - B * B) / A
    num = np.array([r['num'] for r in rows])
    size = np.array([r['size'] for r in rows])
    torsion = np.array([int(np.prod(r['tors'])) if r['tors'] else 1 for r in rows])
    tstr = np.array([str(r['tors']) for r in rows])
    keys = np.array([f"{r['N']}{r['cls']}" for r in rows])
    Ncond = np.array([r['N'] for r in rows])
    fresh = num >= 2
    loopless = (num == 1) & (size == 1)
    hidden = (num == 1) & (size >= 2) & (torsion == 1)
    seen = (num == 1) & (torsion > 1)
    print(f"\ngroups: fresh {fresh.sum()}, optimal with no loop {loopless.sum()}, optimal hidden-loop {hidden.sum()}, "
          f"optimal with torsion {seen.sum()}, optimal in all {int((num == 1).sum())}")

    rng = np.random.default_rng(SEED)
    print("\n==== REGISTERED CRITERIA ====")
    l1, l2 = criterion("L1/L2 fresh curves", y[fresh], keys[fresh], y[loopless], keys[loopless], rng)
    l3s, l3g = criterion("L3 hidden-loop optimal curves", y[hidden], keys[hidden], y[loopless], keys[loopless], rng)
    print(f"\nSCORE: L1 {l1}; L2 {l2}; L3 strict {l3s}; L3 graded {l3g}"
          f"{'  (ROUND VOID: pipeline)' if void else ''}")
    rival = (int(np.sum(y[fresh] > BAD)) >= 20) and (l2 == 'MISS')
    print(f"RIVAL (L1 misses by 20 or more, and L2 misses): {'HELD' if rival else 'DIED'}")

    print("\n==== SEEN, NOT SCORED: optimal curves with torsion ====")
    k5 = int(np.sum(y[seen] > BAD))
    print(f"  n = {seen.sum()}; above 5: {k5}; q = {np.mean(y[seen] > BAD) / np.mean(y[seen] > FAIL):.5f}")

    print("\n==== DESCRIPTION (no prediction) ====")
    describe("fresh (non-optimal) curves", y[fresh])
    describe("optimal, no loop", y[loopless])
    describe("optimal, hidden loop (isogeny only)", y[hidden])
    describe("optimal, torsion", y[seen])
    describe("optimal, any loop", y[(num == 1) & (size >= 2)])
    print("\nfresh curves by torsion:")
    for t in sorted(set(tstr[fresh]), key=lambda s: (len(s), s)):
        m = fresh & (tstr == t)
        describe(f"torsion {t}", y[m])
    print("\nfresh curves by conductor band (q against no loop in the same band):")
    for lo, hi in ((0, 1e5), (1e5, 2e5), (2e5, 3e5), (3e5, 4e5), (4e5, 5e5)):
        mf, ml = fresh & (Ncond >= lo) & (Ncond < hi), loopless & (Ncond >= lo) & (Ncond < hi)
        qf = np.mean(y[mf] > BAD) / np.mean(y[mf] > FAIL)
        ql = np.mean(y[ml] > BAD) / np.mean(y[ml] > FAIL)
        print(f"  {int(lo):>6}-{int(hi) - 1:<6}  fresh n={mf.sum():>6} q={qf:.4f}   no loop n={ml.sum():>6} q={ql:.4f}")

    # ---- relation of each fresh lattice to its optimal partner's ----
    idx_opt = {k: i for i, k in enumerate(keys) if num[i] == 1}
    rel = np.zeros(len(rows), int)
    for i in np.nonzero(fresh)[0]:
        j = idx_opt.get(keys[i])
        if j is not None:
            rel[i] = relation_index(tau_of(A[j], B[j], C[j]), x[i], y[i])
    print("\nfresh lattice against its optimal partner's: smallest index n with (a tau + b)/d equivalent "
          f"(n = 1: same shape; 0: none up to {NMAX})")
    partner_y = np.array([y[idx_opt[k]] if k in idx_opt else np.nan for k in keys])
    for n in sorted(set(rel[fresh])):
        m = fresh & (rel == n)
        print(f"  n = {n:>2}: {m.sum():>6} curves; above 2 {np.mean(y[m] > 2):.4f}; above 5 {int(np.sum(y[m] > 5)):>4}; "
              f"median elongation {np.median(y[m]):.3f} (partners {np.nanmedian(partner_y[m]):.3f}); "
              f"thinner than partner {np.mean(y[m] > partner_y[m] * (1 + 1e-9)):.3f}")
    tail = np.nonzero(fresh & (y > BAD))[0]
    tail = tail[np.argsort(-y[tail])]
    print(f"\nevery fresh curve above 5 ({len(tail)}), thinnest first: label, elongation, torsion, class size, "
          f"partner's elongation, n")
    for i in tail:
        r = rows[i]
        print(f"  {r['N']}{r['cls']}{r['num']:<3} {y[i]:7.3f}  {str(r['tors']):8s} {r['size']}  "
              f"{partner_y[i]:7.3f}  {rel[i]}")


# ----------------------------------------------------------------------------------------------------------------
# self-test on synthetic lattices (no curve data)
# ----------------------------------------------------------------------------------------------------------------
def selftest():
    import numpy as np
    rng = np.random.default_rng(7)
    ok = True

    def random_tau():
        while True:
            t = complex(rng.uniform(-0.5, 0.5), math.exp(rng.uniform(math.log(0.87), math.log(12))))
            if abs(t) >= 1:
                return t

    def gram(vectors):
        v1, v2 = vectors
        return np.array([[abs(v1) ** 2, (v1 * v2.conjugate()).real], [(v1 * v2.conjugate()).real, abs(v2) ** 2]])

    def unimodular():
        U = np.eye(2, dtype=int)      # small entries, so that the test's own rounding stays far below 1e-9
        for _ in range(3):
            E = np.array([[1, int(rng.integers(-2, 3))], [0, 1]]) if rng.random() < 0.5 else \
                np.array([[1, 0], [int(rng.integers(-2, 3)), 1]])
            U = U @ E
        if rng.random() < 0.5:
            U = U @ np.array([[0, 1], [1, 0]])
        return U

    # 1. reduction is invariant under change of basis and scaling, and finds the shortest vector
    taus = [random_tau() for _ in range(2000)]
    errs = 0
    for t in taus:
        s = math.exp(rng.uniform(-3, 3))
        G0 = s * gram((1 + 0j, t))
        U = unimodular()
        G1 = U.T @ G0 @ U
        A0, B0, C0 = reduce_forms([G0[0, 0]], [G0[0, 1]], [G0[1, 1]])
        A1, B1, C1 = reduce_forms([G1[0, 0]], [G1[0, 1]], [G1[1, 1]])
        y0, y1 = math.sqrt(A0[0] * C0[0] - B0[0] ** 2) / A0[0], math.sqrt(A1[0] * C1[0] - B1[0] ** 2) / A1[0]
        # tau is reduced, so the shortest vector of s<1, tau> has norm s, and the elongation is Im tau
        if abs(y0 - y1) > 1e-9 * y0 or abs(A1[0] - s) > 1e-9 * s or abs(y0 - t.imag) > 1e-9 * y0:
            errs += 1
    print(f"selftest 1 (reduction invariant under change of basis, shortest vector, elongation = Im tau): "
          f"{errs} errors in 2000")
    ok &= errs == 0

    # 2. the neighbour classifier recovers a prime index from a scaled, re-based sublattice
    errs, tried = 0, 0
    for t in taus[:1000]:
        for p in (2, 3, 5, 7, 11, 13):
            a, b, d = NEIGH[p][int(rng.integers(0, len(NEIGH[p])))]
            G1 = math.exp(rng.uniform(-2, 2)) * gram((d + 0j, a * t + b))
            U = unimodular()
            G1 = U.T @ G1 @ U
            A1, B1, C1 = reduce_forms([G1[0, 0]], [G1[0, 1]], [G1[1, 1]])
            xf, yf = abs(B1[0]) / A1[0], math.sqrt(A1[0] * C1[0] - B1[0] ** 2) / A1[0]
            n = relation_index(t, xf, yf)
            tried += 1
            if n != p:
                errs += 1
    print(f"selftest 2 (index-p neighbour recovered, p = 2..13): {errs} errors in {tried}")
    ok &= errs == 0
    n = relation_index(taus[0], *reduce_tau(taus[0]))
    print(f"selftest 3 (a lattice against itself gives n = 1): n = {n}")
    ok &= n == 1

    # 4. the bootstrap: synthetic clusters with a known q
    k = 20000
    n2 = rng.integers(1, 4, k)
    n5 = rng.binomial(n2, 0.03)
    b = boot_q(n2, n5, np.random.default_rng(SEED), 500)
    q = n5.sum() / n2.sum()
    se_binom = math.sqrt(q * (1 - q) / n2.sum())
    print(f"selftest 4 (bootstrap): q = {q:.4f}, bootstrap s.e. {b.std(ddof=1):.5f}, binomial s.e. {se_binom:.5f}")
    ok &= abs(b.std(ddof=1) / se_binom - 1) < 0.15

    # 5. the PARI pipeline on a two-curve class OUTSIDE Cremona's tables (conductor 619 904 > 500 000):
    #    y^2 = x^3 - 30x^2 + 58x (minimal model [0,0,0,-242,-1420]) and its 2-isogenous curve
    import tempfile
    pari = get_pari()
    E = pari.ellinit([0, 0, 0, -242, -1420])
    P = pari.ellsaturation(E, [[-8, 2], [40, 230]], 100)
    T = pari.elltors(E)[2][0]
    iso = pari.ellisogeny(E, T)
    Ep, v = pari(f"my(v, e = ellminimalmodel(ellinit({iso[0]}), &v)); [e, v]")
    Pp = [pari.ellchangepoint(pari.ellisogenyapply(iso[1], q), v) for q in P]
    Pp = pari.ellsaturation(Ep, Pp, 100)

    def projective(q):
        X, Y = pari(q[0]), pari(q[1])
        Z = pari.lcm(pari.denominator(X), pari.denominator(Y))
        return f"[{X * Z}:{Y * Z}:{Z}]"

    def tors_str(e):
        return '[' + ','.join(str(int(t)) for t in pari.elltors(e)[1]) + ']'

    lines = [f"619904 zz {k} [{','.join(str(int(t)) for t in e[:5])}] 2 {tors_str(e)} {projective(g[0])} {projective(g[1])}"
             for k, e, g in ((1, E, P), (2, Ep, Pp))]
    with tempfile.TemporaryDirectory() as tmp:
        fn, out = os.path.join(tmp, 'allgens.test'), os.path.join(tmp, 'out.json')
        open(fn, 'w').write('\n'.join(lines) + '\n')
        import contextlib, io
        with contextlib.redirect_stdout(io.StringIO()):
            compute_file(fn, out)
        d = json.load(open(out))
    rows = d['rows']
    regs = [r['G'][0][0] * r['G'][1][1] - r['G'][0][1] ** 2 for r in rows]
    quotient = rows[1]['bsd'] * regs[1] / (rows[0]['bsd'] * regs[0])
    A5, B5, C5 = reduce_forms([r['G'][0][0] for r in rows], [r['G'][0][1] for r in rows], [r['G'][1][1] for r in rows])
    n = relation_index(tau_of(A5[0], B5[0], C5[0]), abs(B5[1]) / A5[1], math.sqrt(A5[1] * C5[1] - B5[1] ** 2) / A5[1])
    good5 = len(rows) == 2 and not d['bad'] and [r['size'] for r in rows] == [2, 2] and abs(quotient - 1) < 1e-6 \
        and n in (1, 2)
    print(f"selftest 5 (PARI pipeline, a 2-isogenous pair of conductor 619904): {len(rows)} curves, "
          f"{len(d['bad'])} failures, BSD quotient {quotient:.12f}, index n = {n}")
    ok &= good5

    # 6. the scoring code end to end, on random lattices with a made-up class structure (no curve data)
    with tempfile.TemporaryDirectory() as tmp:
        fake = []
        for c in range(3000):
            size = 1 if c % 3 else int(rng.integers(2, 5))
            for k in range(1, size + 1):
                t = random_tau()
                s = math.exp(rng.uniform(-2, 2))
                Gm = s * gram((1 + 0j, t))
                fake.append(dict(N=1000 + c, cls='a', num=k, size=size, ai=[0, 0, 0, 0, 1], tors=[2] if c % 5 == 0 else [],
                                 gens=[], G=Gm.tolist(), bsd=(1.0 / (s * s * t.imag ** 2)) if size >= 2 else None))
        json.dump(dict(rows=fake, bad=[]), open(os.path.join(tmp, 'fake.json'), 'w'))
        buf = io.StringIO()
        import warnings
        with contextlib.redirect_stdout(buf), warnings.catch_warnings():
            warnings.simplefilter('ignore')          # the made-up data leave some conductor bands empty
            score(tmp)
    text = buf.getvalue()
    good6 = 'SCORE: L1' in text and 'whose BSD quotient' in text and ' 0 whose BSD quotient' in text
    print(f"selftest 6 (scoring end to end on random lattices): {'ran' if 'SCORE: L1' in text else 'FAILED'}, "
          f"BSD check clean: {' 0 whose BSD quotient' in text}")
    ok &= good6
    print("SELFTEST", "PASS" if ok else "FAIL")
    return ok


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'selftest':
        sys.exit(0 if selftest() else 1)
    elif cmd == 'compute':
        compute(sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 4)
    elif cmd == 'compute-file':
        compute_file(sys.argv[2], sys.argv[3])
    elif cmd == 'score':
        low_priority()
        score(sys.argv[2])
    else:
        print(__doc__)
