"""watkins_round.py -- round 10, the tension with Watkins (registered/REGISTERED_2026-11-24_the_watkins_tension.md).

  python -I watkins_round.py sample SW_DIR OUT.json            draw the strata from the Stein-Watkins prime tables
  python -I watkins_round.py compute OUT.json RESULTS.json [W]  generators, heights and shapes (W workers, default 2)
  python -I watkins_round.py score RESULTS.json ALL_ROWS.json   the registered criteria (ALL_ROWS = run_all.py output)
  python -I watkins_round.py timing SW_DIR [n]                  time ellrank on n curves of p.99; prints no shape

SW_DIR holds the prime tables p.00.bz2 ... p.99.bz2 of the Stein-Watkins database (one isogeny class per header line
"N [factors] rank L-coefficient isogeny-number modular-degree", its curves on the lines after it, starting with '[').
"""
import bz2
import json
import math
import os
import random
import re
import subprocess
import sys
import time

SEED = 20261124
BELOW_NORMAL = 0x00004000
STRATA = {'A': (0, 5 * 10 ** 5, None), 'B': (10 ** 7, 10 ** 8, 2000), 'C': (9 * 10 ** 8, 10 ** 9, 2000),
          'D': (99 * 10 ** 8, 10 ** 10, 2000)}
N_UNIFORM = 4000
TAU_BINS = [0.866, 1.5, 2.0, 2.5, 3.5, math.inf]
WATKINS = {2: 0.354, 4: 0.094, 8: 0.017, 16: 0.002}
WATKINS_X = [0.090, 0.096, 0.098, 0.099, 0.100, 0.100, 0.102, 0.105, 0.106, 0.105]


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
    pari.allocatemem(8 * 10 ** 8)
    return pari


def rank2_classes(path):
    """(N, first curve's a-invariants) for every isogeny class of analytic rank 2 in one prime table"""
    out, cur = [], None
    with bz2.open(path, 'rt', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            if line[0] != '[':
                x = line.split()
                cur = (int(x[0]), int(x[2]))
                cur_first = True
            else:
                if cur is not None and cur_first:
                    cur_first = False
                    if cur[1] == 2:
                        ai = [int(t) for t in line.split()[0].strip('[]').split(',')]
                        out.append((cur[0], ai))
    return out


def sample(sw_dir, out_path):
    rng = random.Random(SEED)
    tables = {k: os.path.join(sw_dir, 'p.%02d.bz2' % k) for k in range(100)}
    allc = []
    counts = {}
    for k in range(100):
        cl = rank2_classes(tables[k])
        counts[k] = len(cl)
        allc += cl
        print(f"p.{k:02d}: {len(cl)} classes of analytic rank 2", flush=True)
    picked = {}
    for name, (lo, hi, n) in STRATA.items():
        pool = [c for c in allc if lo <= c[0] < hi]
        picked[name] = pool if n is None else rng.sample(pool, min(n, len(pool)))
        print(f"stratum {name}: {len(picked[name])} of {len(pool)} classes with {lo} <= N < {hi}")
    picked['U'] = rng.sample(allc, N_UNIFORM)
    print(f"stratum U: {N_UNIFORM} of {len(allc)} classes, uniform below 10^10")
    json.dump(dict(picked=picked, total=len(allc), per_table=counts), open(out_path, 'w'))


def reduce_tau(t):
    for _ in range(1000):
        t = complex(t.real - round(t.real), t.imag)
        if abs(t) < 1 - 1e-15:
            t = -1 / t
        else:
            break
    return abs(t.real), t.imag


def shape(G):
    A, B, C = G[0][0], G[0][1], G[1][1]
    for _ in range(300):
        if A > C:
            A, C = C, A
        k = round(B / A)
        if k == 0:
            break
        C, B = C - 2 * k * B + k * k * A, B - k * A
    if A > C:
        A, C = C, A
    return abs(B) / A, math.sqrt(A * C - B * B) / A


def one_curve(pari, N, ai):
    t0 = time.time()
    E = pari.ellinit(ai)
    res = dict(N=N, ai=ai)
    pts, r_lo, r_hi = [], None, None
    for effort in (0, 2, 5):
        try:
            rk = pari.ellrank(E, effort, pts) if pts else pari.ellrank(E, effort)
        except Exception as e:
            res['error'] = repr(e)[:80]
            continue
        r_lo, r_hi = int(rk[0]), int(rk[1])
        pts = [p for p in rk[3]]
        if r_lo >= 2:
            break
    res['r_lo'], res['r_hi'] = r_lo, r_hi
    om = E.omega() if hasattr(E, 'omega') else pari.member_omega(E)
    w1, w2 = complex(om[0]), complex(om[1])
    tau = w2 / w1 if (w2 / w1).imag > 0 else w1 / w2
    res['tau'] = list(reduce_tau(tau))
    if r_lo is None or r_lo < 2:
        res['ok'] = False
    else:
        S = pari.ellsaturation(E, pts, 100)
        H = pari.ellheightmatrix(E, S)
        G = [[float(H[i][j]) for j in range(len(S))] for i in range(len(S))]
        res['rank_found'] = len(S)
        if len(S) == 2:
            res['G'] = G
            res['x'], res['y'] = shape(G)
            res['ok'] = True
        else:
            res['ok'] = False
    res['seconds'] = time.time() - t0
    return res


def compute_chunk(in_path, out_path):
    low_priority()
    pari = get_pari()
    todo = json.load(open(in_path))
    out = []
    for stratum, N, ai in todo:
        r = one_curve(pari, N, ai)
        r['stratum'] = stratum
        out.append(r)
    json.dump(out, open(out_path, 'w'))


def compute(sample_path, results_path, workers=2):
    low_priority()
    d = json.load(open(sample_path))
    jobs = []
    for name in ('A', 'B', 'C', 'D', 'U'):
        for N, ai in d['picked'][name]:
            jobs.append((name, N, ai))
    tmp = results_path + '.parts'
    os.makedirs(tmp, exist_ok=True)
    chunks = [jobs[i::workers * 8] for i in range(workers * 8)]
    procs, files, t0 = [], [], time.time()
    pending = list(enumerate(chunks))
    while pending or procs:
        while pending and len(procs) < workers:
            i, ch = pending.pop(0)
            fi, fo = os.path.join(tmp, f"in{i}.json"), os.path.join(tmp, f"out{i}.json")
            json.dump(ch, open(fi, 'w'))
            procs.append(subprocess.Popen([sys.executable, '-I', os.path.abspath(__file__), 'compute-chunk', fi, fo],
                                          creationflags=BELOW_NORMAL if os.name == 'nt' else 0))
            files.append(fo)
        time.sleep(2)
        procs = [p for p in procs if p.poll() is None]
    res = []
    for fo in files:
        res += json.load(open(fo))
    json.dump(res, open(results_path, 'w'))
    fails = sum(1 for r in res if not r['ok'])
    print(f"{len(res)} curves in {time.time() - t0:.0f} s; {fails} without two independent points", flush=True)


def binom_se(k, n):
    p = k / n
    return math.sqrt(max(p * (1 - p), 0.25 / n) / n)


def score(results_path, all_rows_path):
    res = json.load(open(results_path))
    by = {}
    for r in res:
        by.setdefault(r['stratum'], []).append(r)
    print("==== CHECK OF THE PIPELINE AND FAILURES ====")
    for name in ('A', 'B', 'C', 'D', 'U'):
        rs = by.get(name, [])
        f = sum(1 for r in rs if not r['ok'])
        t = sorted(r['seconds'] for r in rs)
        print(f"  {name}: {len(rs)} curves, {f} failures ({f / max(len(rs), 1):.3%}), median {t[len(t) // 2]:.2f} s, "
              f"slowest {t[-1]:.1f} s")
    # W0: stratum A against Cremona's prime-conductor curves
    try:
        from cypari import pari
    except ImportError:
        import cypari2
        pari = cypari2.Pari()
    rows = [r for r in json.load(open(all_rows_path)) if r['r'] == 2]
    sieve = bytearray([1]) * (5 * 10 ** 5 + 1)
    sieve[0] = sieve[1] = 0
    for q in range(2, 708):
        if sieve[q]:
            sieve[q * q::q] = bytearray(len(sieve[q * q::q]))
    crem = {}
    for r in rows:
        if r['N'] <= 5 * 10 ** 5 and sieve[r['N']]:
            crem[(r['N'], str(pari.ellinit(r['ai'])[12]))] = shape(r['G'])
    matched, worst, absent, unfound = 0, 0.0, 0, 0
    for r in by.get('A', []):
        key = (r['N'], str(pari.ellinit(r['ai'])[12]))
        if key not in crem:
            absent += 1
        elif not r['ok']:
            unfound += 1
        else:
            cx, cy = crem[key]
            worst = max(worst, abs(cx - r['x']), abs(cy - r['y']))
            matched += 1
    w0 = absent == 0 and unfound == 0 and worst < 1e-6
    print(f"W0: stratum A has {len(by.get('A', []))} curves; {matched} matched to Cremona's prime-conductor rank-2 curves "
          f"(by conductor and j), {absent} absent from Cremona's tables, {unfound} without two points; largest shape "
          f"difference {worst:.2e}. Cremona has {len(crem)} such curves, so Stein-Watkins holds {matched + unfound} of "
          f"them  -> {'PASS' if w0 else 'FAIL (the round stops here)'}")

    def thin(rs, Y=2, fails_as=None):
        ok = [r for r in rs if r['ok']]
        k = sum(1 for r in ok if r['y'] >= Y)
        n = len(ok)
        if fails_as == 'thin':
            k += len(rs) - n
            n = len(rs)
        elif fails_as == 'round':
            n = len(rs)
        return k, n

    def decided(strata, crit):
        """a criterion evaluated with failures dropped; scored both ways if failures exceed 5% of any stratum used"""
        if all(sum(1 for r in rs if not r['ok']) <= 0.05 * len(rs) for rs in strata):
            return crit(None)
        a, b = crit('round'), crit('thin')
        return a if a == b else 'NOT DECIDED'

    print("\n==== REGISTERED CRITERIA ====")
    U = by['U']

    def w1(fa):
        k, n = thin(U, 2, fa)
        return 'PASS' if 0.32 <= k / n <= 0.39 else 'MISS'
    k, n = thin(U)
    print(f"W1 (Watkins reproduced): U thin share {k}/{n} = {k / n:.4f} (s.e. {binom_se(k, n):.4f}); window 0.32-0.39 "
          f"-> {decided([U], w1)}")
    shares = {}
    for name in ('A', 'B', 'C', 'D'):
        k, n = thin(by[name])
        shares[name] = (k / n, binom_se(k, n))
        print(f"   stratum {name}: thin share {k}/{n} = {k / n:.4f} (s.e. {binom_se(k, n):.4f})")

    def w2(fa):
        sh = {}
        for name in ('A', 'B', 'C', 'D'):
            k, n = thin(by[name], 2, fa)
            sh[name] = (k / n, binom_se(k, n))
        if sh['D'][0] > sh['A'][0] + 3 * math.hypot(sh['A'][1], sh['D'][1]):
            return 'MISS'
        steps = all(sh[b][0] <= sh[a][0] + math.hypot(sh[a][1], sh[b][1]) for a, b in (('A', 'B'), ('B', 'C'), ('C', 'D')))
        return 'PASS' if steps else 'NOT DECIDED (neither monotone nor a reversal)'
    print(f"W2 (the author's sentence carried to 10^10: A >= B >= C >= D) -> "
          f"{decided([by['A'], by['B'], by['C'], by['D']], w2)}")

    def rival(fa):
        k, n = thin(by['D'], 2, fa)
        return 'HELD' if k / n > 0.25 else 'DIED'
    print(f"RIVAL (D's thin share above 0.25) -> {decided([by['D']], rival)}")

    def bins(rs):
        out = []
        for lo, hi in zip(TAU_BINS[:-1], TAU_BINS[1:]):
            b = [r for r in rs if r['ok'] and lo <= r['tau'][1] < hi]
            out.append((lo, hi, sum(1 for r in b if r['y'] >= 2), len(b)))
        return out
    bA, bD = bins(by['A']), bins(by['D'])
    w3, rowsout = 'PASS', []
    for (lo, hi, kA, nA), (_, _, kD, nD) in zip(bA, bD):
        line = f"   Im tau [{lo}, {hi}): A {kA}/{nA}, D {kD}/{nD}"
        if nA >= 30 and nD >= 30:
            pa, pd = (kA + 0.5) / (nA + 1), (kD + 0.5) / (nD + 1)
            se = math.sqrt(pa * (1 - pa) / nA + pd * (1 - pd) / nD)
            z = (kD / nD - kA / nA) / se
            line += f"; difference {kD / nD - kA / nA:+.4f}, {z:+.1f} s.e."
            if abs(z) > 3:
                w3 = 'MISS'
        else:
            line += "; fewer than 30 in one of them, not compared"
        rowsout.append(line)
    print(f"W3 (the shape law given Im tau does not depend on the conductor) -> {w3}")
    for line in rowsout:
        print(line)

    print("\n==== RECORDED, NO PREDICTION ====")
    for name in ('A', 'B', 'C', 'D', 'U'):
        ok = [r for r in by[name] if r['ok']]
        ys = [r['y'] for r in ok]
        taus = sorted(r['tau'][1] for r in by[name])
        print(f"  {name}: n = {len(ok)}; shares y >= 2, 4, 8, 16: "
              + ', '.join(f"{sum(1 for y in ys if y >= Y) / len(ys):.4f}" for Y in (2, 4, 8, 16))
              + f"; Im tau median {taus[len(taus) // 2]:.3f}, upper quartile {taus[3 * len(taus) // 4]:.3f}")
    print("  Watkins: " + ', '.join(f"{v}" for v in WATKINS.values()))
    for name in ('A', 'D', 'U'):
        ok = [r for r in by[name] if r['ok'] and r['y'] >= 1]
        h = [0] * 10
        for r in ok:
            h[min(int(r['x'] / 0.05), 9)] += 1
        print(f"  x by tenths (y >= 1), {name}: " + ' '.join(f"{c / len(ok):.3f}" for c in h))
    print("  x by tenths, Watkins:   " + ' '.join(f"{v:.3f}" for v in WATKINS_X))
    for name in ('A', 'B', 'C', 'D', 'U'):
        print(f"  thin share by Im tau, {name}: "
              + '; '.join(f"[{lo},{hi}) {k}/{n}" for lo, hi, k, n in bins(by[name])))


def timing(sw_dir, n=8):
    low_priority()
    pari = get_pari()
    cl = rank2_classes(os.path.join(sw_dir, 'p.99.bz2'))
    rng = random.Random(1)
    for N, ai in rng.sample(cl, n):
        t0 = time.time()
        r = one_curve(pari, N, ai)
        print(f"  N = {N}: two independent points found: {r['ok']}; {time.time() - t0:.2f} s", flush=True)


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'sample':
        sample(sys.argv[2], sys.argv[3])
    elif cmd == 'compute':
        compute(sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 2)
    elif cmd == 'compute-chunk':
        compute_chunk(sys.argv[2], sys.argv[3])
    elif cmd == 'score':
        score(sys.argv[2], sys.argv[3])
    elif cmd == 'timing':
        timing(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 8)
