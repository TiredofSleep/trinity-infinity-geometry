"""digits5.py -- the p = 5 maximum to 60 digits, its symmetry, and a search for an integer polynomial (not part of
the proof: the rigorous enclosure is bb5.exe's; this refines the certified critical point by Newton's method).

Usage: python digits5.py   -> digits5.log
"""
import os
import struct

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
mp.mp.dps = 130
P = 5
LOG = open(os.path.join(HERE, "digits5.log"), "w", encoding="utf-8")


def say(s=""):
    print(s, flush=True)
    LOG.write(s + "\n")


def d(h):
    return struct.unpack("<d", struct.pack("<Q", int(h, 16)))[0]


x = [mp.mpf(d(h)) for h in open(os.path.join(HERE, "candidates_5.txt")).read().split("\n")[4].split()[:4]]
AI = [[(q + u) % P for u in (1, 2)] for q in range(P)]
BI = [[(q - u) % P for u in (1, 2)] for q in range(P)]


def ev(x):
    phi = [mp.mpf(0)] + list(x)
    E, ang = {}, {}
    for q in range(P):
        for s in range(P):
            t = mp.mpf(1)
            for ui, u in enumerate((1, 2)):
                a = phi[AI[q][ui]] - phi[BI[q][ui]] - 4 * mp.pi * s * u / P
                ang[q, s, ui] = a
                t += 2 * mp.cos(a)
            E[q, s] = t
    return E, ang


E, _ = ev(x)
sg = {k: mp.sign(v) for k, v in E.items()}


def grad_hess(x):
    E, ang = ev(x)
    g = [mp.mpf(0)] * P
    H = mp.zeros(P, P)
    for q in range(P):
        for s in range(P):
            for ui in range(2):
                a, b = AI[q][ui], BI[q][ui]
                t = sg[q, s] * mp.sin(ang[q, s, ui])
                c = -2 * sg[q, s] * mp.cos(ang[q, s, ui])
                g[a] -= 2 * t
                g[b] += 2 * t
                H[a, a] += c
                H[b, b] += c
                H[a, b] -= c
                H[b, a] -= c
    return mp.matrix(g[1:]), mp.matrix([[H[i, j] for j in range(1, P)] for i in range(1, P)]), E


for it in range(20):
    g, H, E = grad_hess(x)
    step = mp.lu_solve(H, g)
    x = [x[i] - step[i] for i in range(4)]
    if max(abs(s) for s in step) < mp.mpf(10) ** -125:
        break
g, H, E = grad_hess(x)
S = sum(abs(v) for v in E.values()) / 25
say("digits5.py -- the maximum of S over diagonal states at p = 5, to 60 digits (Newton at 130 digits)")
say(f"  the signs of E are those of the certified critical point; |grad| after Newton {mp.nstr(max(abs(v) for v in g), 3)}")
say(f"  S*_5 = {mp.nstr(S, 60)}")
say(f"  phases in turns: {[mp.nstr(v / (2 * mp.pi), 25) for v in x]}")
say(f"  phi(2) - 2 phi(1) = {mp.nstr(x[1] - 2 * x[0], 3)}")
phi = [mp.mpf(0)] + x
for eps in (1, -1):
    for alpha in range(1, 5):
        for t in range(5):
            for beta in range(5):
                for gamma in range(5):
                    if (eps, alpha, t, beta, gamma) == (1, 1, 0, 0, 0):
                        continue
                    ok = True
                    for xx in range(5):
                        v = eps * (phi[(alpha * xx + t) % 5] - phi[t]) + 2 * mp.pi * (beta * xx + gamma * xx * xx) / 5 - phi[xx]
                        r = v / (2 * mp.pi)
                        if abs(r - mp.nint(r)) > mp.mpf(10) ** -100:
                            ok = False
                            break
                    if ok:
                        say(f"  symmetry: {'conjugation, ' if eps < 0 else ''}x -> {alpha} x + {t}, Clifford phase (beta, gamma) = ({beta}, {gamma})")
a, b = x[0], x[2] - x[0]
for name, v in (("S*_5", S), ("cos a", mp.cos(a)), ("cos b", mp.cos(b)), ("cos(a + b)", mp.cos(a + b))):
    hit = None
    for deg in range(2, 25):
        r = mp.findpoly(v, deg, maxcoeff=10 ** 9)
        if r:
            hit = (deg, r)
            break
    say(f"  integer polynomial for {name}: {hit if hit else 'none of degree <= 24 with coefficients <= 1e9'}")
LOG.close()
