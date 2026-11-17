"""verify_conductors.py -- checks the conductor corollary of Theorem 8 (AIRY_DETERMINANTS_NOTE.md, Section 4).

    "2 first, draft the note to Chenevert... no gates"  -- the author, 17 November 2026

The proof sketch of Theorem 8 finds, at each prime l, the inertia action on rho_n: one reflection for each S_n-orbit of
nodes mod l whose critical value has odd valuation, and nothing else (the action is tame).  So the same count N_l(n)
that gives the determinant chi^(N_l(n)) also gives the conductor:

    cond(rho_n) = prod over l of l^(N_l(n)),
    N_l(n) = #{odd j <= n : v_l(j) odd}                     (l >= 5),
    N_3(n) = #{odd j <= n : v_3(j) even and >= 2}           (in the model e1 = e3 = 0).

Chenevert's thesis (McGill 2008, p. 146) names the Artin conductor of a representation from geometry, read from
geometric data, as of great interest.  This script tests the formula against the functional equation of the L-function.
A weight-3 newform of level N with real coefficients a_n satisfies, with F(t) = sum_n a_n exp(-2 pi n t / sqrt N),

    F(1/t) = eps t^3 F(t)  for every t > 0,  eps = +1 or -1,

and fails it at any other level.  The traces a_p come from exact point counts (edge_rule.t_values and airy), at the good
primes and at the bad primes l >= 5 where the naive model has only nodes.  The traces at 2 and 3 have no count here, so
they are scanned over every integer allowed by the Weil bound, not assumed.

  C0. N_l(n) reproduces the determinant of Theorem 8 (D_n) for every odd n <= 41: the parity of the conductor exponent.
  C1. n = 5, 9: rho_n is the character (5|p), (105|p) (rounds 19-20); the formula gives 5 and 105, their conductors.
  C2. n = 7: rho_7 is the newform 35.3.c.b (Chenevert's theorem).  Control: the scan must return level 35 and LMFDB's
      a_2 = 0, a_3 = 1.
  C3. n = 11: the formula gives 1155 = 3*5*7*11.  The functional equation must hold there and fail at the rival levels.
  C4. n = 15: the formula gives 75075 = 3*5^2*7*11*13.  Equivalently, rho_15 twisted by (5|p) has level 3003 and is
      unramified at 5 (its trace at 5 is scanned too).
  A fit at one level to machine precision already fixes the conductor; the rival levels show that the test can tell.
  A rival is scored only where its sums have converged by n = 503 (the same residual, to 10%, when cut at n = 400).
  Rivals with l^2 in the level at a prime l whose trace the counts give as nonzero are excluded without the functional
  equation too: for a newform, l^2 | N with the character ramified only once at l forces a_l = 0 (Li, Atkin-Lehner).

numpy + sympy + edge_rule.py.  ASCII output; writes runs/verify_conductors.log and exits with 1 if a check fails.
Run:  python verify_conductors.py      (about two minutes; four workers at below-normal priority)
"""
import itertools
import math
import os
import sys
import time

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import numpy as np
import sympy

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import edge_rule as er  # noqa: E402  (sets below-normal priority on import, through coin_at_five)

os.makedirs(os.path.join(HERE, "runs"), exist_ok=True)   # run logs go to runs/ (ignored); the committed copy is the reference
LOG = open(os.path.join(HERE, "runs", "verify_conductors.log"), "w", encoding="utf-8")
FAILS = []
PMAX = 503          # traces at every prime up to here
TS = [1.03, 1.07, 1.11, 1.15, 1.19, 1.23, 1.27]


def say(s=""):
    print(s, flush=True)
    LOG.write(s + "\n")
    LOG.flush()


def check(name, ok, detail=""):
    say(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAILS.append(name)


def vl(j, l):
    v = 0
    while j % l == 0:
        j //= l
        v += 1
    return v


def N_l(n, l):
    """the number of S_n-orbits of nodes mod l whose critical value has odd valuation (Steps 3-4 of the sketch)"""
    if l == 3:
        return sum(1 for j in range(1, n + 1, 2) if vl(j, 3) >= 2 and vl(j, 3) % 2 == 0)
    return sum(1 for j in range(1, n + 1, 2) if vl(j, l) % 2 == 1)


def conductor(n):
    return math.prod(l ** N_l(n, l) for l in sympy.primerange(3, n + 1))


def disc(n):
    """D_n = prod of l* over the l with N_l(n) odd"""
    return math.prod(er.signed(l) for l in sympy.primerange(3, n + 1) if N_l(n, l) % 2)


def A(n):
    return math.prod(j // (3 if j % 3 == 0 else 1) for j in range(1, n + 1, 2))


def _traces(p):
    er.low_priority()
    return p, er.airy(p, er.t_values(p, (3, 5, 7, 9, 11, 13, 15)))


def kron(D, p):
    return int(sympy.jacobi_symbol(D % p, p)) if p % 2 else (0 if D % 2 == 0 else (1 if D % 8 in (1, 7) else -1))


FACT = {}


def coefficients(ap, N, D, nmax, k=3):
    """a_n for n <= nmax from the a_p: Hecke's recursion with character (D|.) at p not dividing N, a_(p^r) = a_p^r at p | N"""
    if not FACT:
        FACT.update({n: sympy.factorint(n) for n in range(2, PMAX + 1)})
    pp = {}
    for p in sympy.primerange(2, nmax + 1):
        pw = [1, ap[p]]
        while p ** len(pw) <= nmax:
            if N % p == 0:
                pw.append(ap[p] * pw[-1])
            else:
                pw.append(ap[p] * pw[-1] - kron(D, p) * p ** (k - 1) * pw[-2])
        pp[p] = pw
    a = np.zeros(nmax + 1)
    a[1] = 1.0
    for n in range(2, nmax + 1):
        a[n] = math.prod(pp[p][e] for p, e in FACT[n].items())
    return a


EXP = {}


def fe_residual(a, N, ts=TS):
    """max over t of |F(1/t) - eps t^3 F(t)|, relative to the size of the terms, for the better sign eps"""
    key = (N, len(a))
    if key not in EXP:
        n = np.arange(len(a))
        sq = math.sqrt(N)
        EXP[key] = (np.array([np.exp(-2 * math.pi * n / (t * sq)) for t in ts]),
                    np.array([t ** 3 * np.exp(-2 * math.pi * n * t / sq) for t in ts]))
    E1, E2 = EXP[key]
    u, v = E1 @ a, E2 @ a
    scale = max(np.max(np.abs(u)), np.max(np.abs(v)))
    r = {eps: float(np.max(np.abs(u - eps * v)) / scale) for eps in (1, -1)}
    eps = min(r, key=r.get)
    return r[eps], eps


def converged(known, vals, M, D):
    """a rival is scored only if its best residual is the same (to 10%) with the sums cut at n = 400 as at n = PMAX"""
    ap = dict(known)
    ap.update(vals)
    hi = fe_residual(coefficients(ap, M, D, PMAX), M)[0]
    lo = fe_residual(coefficients(ap, M, D, 400), M)[0]
    return abs(hi - lo) <= 0.1 * hi, lo


def scan(known, unknown, N, D, nmax):
    """try every value of the unknown traces; return the residuals sorted, with the values that gave them"""
    names = sorted(unknown)
    out = []
    for vals in itertools.product(*(unknown[p] for p in names)):
        ap = dict(known)
        ap.update(zip(names, vals))
        res, eps = fe_residual(coefficients(ap, N, D, nmax), N)
        out.append((res, dict(zip(names, vals)), eps))
    out.sort(key=lambda r: r[0])
    return out


def weil(p):
    """the integers allowed at p for a weight-3 form: |a_p| <= 2p"""
    return list(range(-2 * p, 2 * p + 1))


def main():
    t0 = time.time()
    say("verify_conductors.py -- the conductor of rho_n from the nodes, against the functional equation")
    say()
    # C0: the parity of the conductor exponent is the determinant
    ok0 = all(int(sympy.jacobi_symbol(p, A(n))) == kron(disc(n), p)
              for n in range(5, 42, 2) for p in sympy.primerange(3, 400) if A(n) % p)
    table = {5: 5, 7: -35, 9: 105, 11: -1155, 13: -15015, 15: -3003, 17: -51051, 19: 969969, 21: -138567,
             23: 3187041, 25: 3187041, 27: 3187041, 29: 92424189, 31: -2865149859, 33: 260468169,
             35: -9116385915, 39: -25946636835}
    ok0 &= all(disc(n) == d for n, d in table.items())
    check("C0 the nodes' count N_l(n) gives Theorem 8's D_n (the table, n = 5..39) and (p/A_n) = (D_n|p), n <= 41", ok0)
    for n in (5, 7, 9, 11, 13, 15, 17, 19, 21):
        say(f"     n = {n:2d}: conductor {conductor(n)} = {sympy.factorint(conductor(n))}, D_n = {disc(n)}")
    check("C1 n = 5, 9: the formula gives 5 and 105, the conductors of (5|p) and (105|p)",
          conductor(5) == 5 and conductor(9) == 105)
    check("    and 35, 1155, 75075 at n = 7, 11, 15",
          conductor(7) == 35 and conductor(11) == 1155 and conductor(15) == 75075)
    say()

    from multiprocessing import Pool
    P = [p for p in sympy.primerange(5, PMAX + 1)]
    with Pool(4) as pool:
        T = dict(pool.map(_traces, P))
    say(f"traces from exact counts at the {len(P)} primes 5..{PMAX} ({(time.time() - t0) / 60:.1f} minutes)")
    a7 = {p: T[p][7] / p ** 3 for p in P}
    a11 = {p: T[p][11] / p ** 5 for p in P}
    a15 = {p: T[p][15] / p ** 7 for p in P}
    integral = all(x.denominator == 1 and abs(x) <= 2 * p for d in (a7, a11, a15) for p, x in d.items()
                   if not (d is a15 and p == 5))
    check("    every trace is an integer within the Weil bound 2p (5 | T15 excepted: T15(5) = 0)",
          integral and T[5][15] == 0)
    a7 = {p: int(x) for p, x in a7.items()}
    a11 = {p: int(x) for p, x in a11.items()}
    a15t = {p: er.leg(5, p) * int(x) for p, x in a15.items() if p != 5}   # rho_15 twisted by (5|p)
    lm = er.LMFDB_35_3_c_b
    check("    rho_7's traces equal LMFDB 35.3.c.b's a_p wherever both are listed (5..97)",
          all(a7[p] == lm[p] for p in lm if p in a7))
    say(f"     bad primes from the counts: rho_7 a_5, a_7 = {a7[5]}, {a7[7]};  rho_11 a_5, a_7, a_11 = "
        f"{a11[5]}, {a11[7]}, {a11[11]};  rho_15 (twisted) a_7, a_11, a_13 = {a15t[7]}, {a15t[11]}, {a15t[13]}")
    say()

    cases = [
        ("C2", "rho_7", a7, -35, 35, [105, 175, 245, 315], {2: weil(2), 3: weil(3)}),
        ("C3", "rho_11", a11, -1155, 1155, [3465, 5775, 8085, 12705], {2: weil(2), 3: weil(3)}),
        ("C4", "rho_15 x (5|.)", a15t, -3003, 3003, [9009, 15015, 21021], {2: weil(2), 3: weil(3), 5: weil(5)}),
    ]
    for tag, name, known, D, N, rivals, unknown in cases:
        nmax = PMAX
        say(f"{tag} {name}: character ({D}|.), predicted level {N}; unknown traces {sorted(unknown)} scanned "
            f"({math.prod(len(v) for v in unknown.values())} combinations), a_n to n = {nmax}")
        best = scan(known, unknown, N, D, nmax)
        r0, vals0, eps0 = best[0]
        r1 = best[1][0]
        say(f"     level {N}: best residual {r0:.2e} at {vals0} (sign {eps0:+d}); next best {r1:.2e}")
        rival_best = {}
        for M in rivals:
            rb = scan(known, unknown, M, D, nmax)[0]
            conv, lo = converged(known, rb[1], M, D)
            heavy = [l for l in (5, 7, 11, 13) if M % (l * l) == 0 and l in known and known[l] != 0]
            note = (f"; also excluded without the functional equation: {heavy[0]}^2 | N would force a_{heavy[0]} = 0, "
                    f"but the count gives {known[heavy[0]]}") if heavy else ""
            if conv:
                rival_best[M] = rb[0]
                say(f"     rival level {M} = {sympy.factorint(M)}: best residual {rb[0]:.2e} at {rb[1]}{note}")
            else:
                say(f"     rival level {M} = {sympy.factorint(M)}: not scored, its sums have not converged by n = {nmax} "
                    f"(residual {rb[0]:.1e} there, {lo:.1e} at n = 400){note}")
        three = [M for M in rivals if M % 9 == 0]
        ok = (r0 < 1e-12 and r1 > 1e-4 and all(rival_best[M] > 1e-4 for M in rival_best)
              and all(M in rival_best for M in three))
        detail = (f"residual {r0:.1e}; every other choice of the unknowns, and every scored rival (3^2 among them), "
                  f">= {min([r1] + list(rival_best.values())):.1e}")
        if tag == "C2":
            ok &= vals0 == {2: lm[2], 3: lm[3]}
            detail += f"; it picks LMFDB's a_2 = {lm[2]}, a_3 = {lm[3]}"
        if tag == "C3":
            ok &= vals0[2] == 0 and abs(vals0[3]) == 3
            detail += f"; it picks a_2 = 0 (2 is inert in Q(sqrt -1155)) and |a_3| = 3"
        if tag == "C4":
            ok &= vals0[2] == 0 and vals0[5] == 0 and abs(vals0[3]) == 3
            detail += f"; it picks a_2 = a_5 = 0 (inert in Q(sqrt -3003)) and |a_3| = 3"
        check(f"{tag} the functional equation holds at level {N} alone", ok, detail)
        say()

    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    say(f"{'ALL PASS' if not FAILS else 'FAILED: ' + ', '.join(FAILS)}")
    LOG.close()
    sys.exit(1 if FAILS else 0)


if __name__ == "__main__":
    main()
