"""mw_shapes.py -- an independent recomputation of the rank-2 (and rank-3) Mordell-Weil lattice data of the
lens handoff (Part F), from Cremona's allgens tables, with PARI (cypari). Written 2026-11-21 from the definitions in
the handoff's files. The handoff's scripts were read but not run (they need cypari2, which has no Windows build).
run_all.py drives this file, and analyse.py compares the result with every number of 20 November.

For every optimal curve (curve number 1 of its isogeny class) of rank 2 or 3 it records: conductor, label, a-invariants,
torsion structure, isogeny-class size, the height Gram matrix of the tabulated generators, the sign and size of the
minimal discriminant, the reduced period-lattice shape tau, and (positive discriminant) which generators lie on the
bounded real component.

Usage: python -I mw_shapes.py OUT.json FILE [FILE ...]   (one process per call; run_all.py runs several)
"""
import json
import math
import os
import re
import sys
import time


def low_priority():
    try:
        import ctypes
        ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x4000)
    except Exception:
        pass


LINE = re.compile(r'(\d+) (\w+) (\d+) \[([-\d,]+)\] (\d+) \[([\d,]*)\] ?(.*)')
PT = re.compile(r'\[(-?\d+):(-?\d+):(-?\d+)\]')


def reduce_tau(t):
    """reduce a point of the upper half plane to the standard fundamental domain, then |Re| in [0, 1/2]"""
    for _ in range(1000):
        t = complex(t.real - round(t.real), t.imag)
        if abs(t) < 1 - 1e-15:
            t = -1 / t
        else:
            break
    return abs(t.real), t.imag


def main():
    low_priority()
    from cypari import pari
    pari.allocatemem(2 * 10 ** 8)
    out_path, files = sys.argv[1], sys.argv[2:]
    rows, bad, t0 = [], [], time.time()
    for fn in files:
        lines = open(fn).read().splitlines()
        size = {}
        parsed = []
        for line in lines:
            m = LINE.match(line.strip())
            if not m:
                continue
            key = (m.group(1), m.group(2))
            size[key] = size.get(key, 0) + 1
            parsed.append(m)
        for m in parsed:
            r = int(m.group(5))
            if m.group(3) != '1' or r not in (2, 3):
                continue
            N = int(m.group(1))
            ai = [int(t) for t in m.group(4).split(',')]
            tors = [int(t) for t in m.group(6).split(',') if t]
            pts = PT.findall(m.group(7))
            gens = pts[:r]
            try:
                E = pari.ellinit(ai)
                P = [[pari(int(X)) / int(Z), pari(int(Y)) / int(Z)] for X, Y, Z in gens]
                for q in P:
                    assert pari.ellisoncurve(E, q)
                H = pari.ellheightmatrix(E, P)
                G = [[float(H[i][j]) for j in range(r)] for i in range(r)]
                disc = E.disc() if hasattr(E, 'disc') else pari.member_disc(E)
                disc = int(disc)
                om = E.omega() if hasattr(E, 'omega') else pari.member_omega(E)
                w1, w2 = complex(om[0]), complex(om[1])
                tau = w2 / w1 if (w2 / w1).imag > 0 else w1 / w2
                tx, ty = reduce_tau(tau)
                egg = None
                if disc > 0:
                    b2, b4, b6 = int(E[5]), int(E[6]), int(E[7])
                    roots = sorted(float(z.real()) for z in pari.polroots(pari(f"4*x^3+({b2})*x^2+2*({b4})*x+({b6})")))
                    mid = (roots[1] + roots[2]) / 2
                    egg = [1 if float(q[0]) < mid else 0 for q in P]
                rows.append(dict(N=N, cls=m.group(2), r=r, ai=ai, tors=tors, iso=size[(m.group(1), m.group(2))],
                                 G=G, disc_sign=1 if disc > 0 else -1, logdisc=math.log(abs(disc)),
                                 tau=[tx, ty], egg=egg))
            except Exception as e:
                bad.append((N, m.group(2), repr(e)[:120]))
    json.dump(dict(rows=rows, bad=bad), open(out_path, "w"))
    print(f"{os.path.basename(out_path)}: {len(rows)} curves, {len(bad)} failures, {time.time() - t0:.0f} s", flush=True)


if __name__ == "__main__":
    main()
