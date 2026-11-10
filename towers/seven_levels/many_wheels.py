"""many_wheels.py -- round 9 of PREREG.md: many wheels, committed with its predictions before the run.

    "you are only spinning one wheel... imagine a 10x10 of wheels or larger?"  -- the author, 9 November 2026

One wheel is one p-level system.  An array of n wheels has dimension D = p^n and a phase space of D^2 points; each
point's operator is the product of the wheels' operators.  So a product state's Wigner function is the product of the
wheels' Wigner functions, and the sum of its sizes multiplies.  The array's half turn is every wheel's half turn at
once, the operator at the origin, and the coin is even or odd under it.  The ceiling is (sqrt D - 1)/2.

For each array the script climbs from random states (round 3's sign ascent) on the even side, on the odd side and in
the whole space.  It reports each best state's purity on every wheel (1 for a wheel not entangled with the rest) and
its stabilizer Renyi entropy M2, to compare with Knipfer, Roman, Matcheva and Matchev (2026); neither is scored.  The
combine step scores Z0 to Z7 and prints the large-array numbers: products of the best single wheels against the
average random state, up to a hundred wheels.

numpy + scipy.  Below-normal priority, three threads.  ASCII output; each part writes many_wheels_<part>.log.
Run:  python many_wheels.py three      (one, two and three wheels of 3 levels; about 25 minutes)
      python many_wheels.py four       (four wheels of 3 levels; about an hour and a half)
      python many_wheels.py five       (one and two wheels of 5 levels; about 15 minutes)
      python many_wheels.py seven      (one and two wheels of 7 levels; about an hour)
      python many_wheels.py combine    (after all four)
Set MANY_WHEELS_SMOKE=1 for a quick test of the code at a tiny size; its scores mean nothing.
"""
import itertools
import os
import sys

PART = sys.argv[1] if len(sys.argv) > 1 else "three"
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "3")
import time

import numpy as np

import round3 as r3

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20261109
SMOKE = os.environ.get("MANY_WHEELS_SMOKE") == "1"
# (p, n, climbs on the even side, on the odd side, in the whole space)
PLAN = {"three": [(3, 1, 100_000, 100_000, 100_000), (3, 2, 1_000_000, 1_000_000, 1_000_000),
                  (3, 3, 500_000, 500_000, 100_000)],
        "four": [(3, 4, 10_000, 10_000, 1_000)],
        "five": [(5, 1, 100_000, 100_000, 100_000), (5, 2, 500_000, 500_000, 100_000)],
        "seven": [(7, 1, 200_000, 200_000, 50_000), (7, 2, 200_000, 200_000, 20_000)]}
KNOWN_ONE = {3: (1 / 3, 1 / 3), 5: (0.556677223351, 0.433070425601), 7: (0.732522000011, 0.728262097)}
KNIPFER = {(3, 2): ("ln(81/17), their maximum", np.log(81 / 17)), (5, 2): ("ln(625/49), their numerical peak",
           np.log(625 / 49)), (7, 2): ("ln(2401/97), their conjecture", np.log(2401 / 97))}
SINGLE = {}                                                            # one wheel's best states, for the check at two
LOG = None
T0 = time.time()


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def clock():
    return f"[{time.time() - T0:.0f} s]"


def array_points(p, n):
    """the phase-point operators of n wheels: products of one wheel's, indexed (u1, ..., un), the origin first"""
    A1 = r3.phase_points(p)
    A = A1
    for _ in range(n - 1):
        A = np.einsum("aij,bkl->abikjl", A, A1).reshape(len(A) * len(A1), A.shape[1] * p, A.shape[2] * p)
    return A


def array_sides(p, n):
    """orthonormal bases of the even and the odd states under the array's half turn"""
    E1, O1 = r3.sides(p)
    even, odd = [], []
    for pattern in itertools.product((0, 1), repeat=n):                 # 1 marks an odd wheel
        M = np.ones((1, 1), complex)
        for b in pattern:
            M = np.kron(M, O1 if b else E1)
        (odd if sum(pattern) % 2 else even).append(M)
    return np.hstack(even), np.hstack(odd)


def purities(psi, p, n):
    """the purity of each wheel's reduced state: 1 when that wheel is not entangled with the rest"""
    T = psi.reshape((p,) * n)
    out = []
    for i in range(n):
        M = np.moveaxis(T, i, 0).reshape(p, -1)
        rho = M @ M.conj().T
        out.append(round(float(np.real(np.trace(rho @ rho))), 6))
    return out


def sre2(psi, p, n):
    """the stabilizer Renyi entropy M2 = -ln( sum over the D^2 Weyl operators of |<psi|W|psi>|^4 / D )"""
    T = psi.reshape((p,) * n)
    axes = tuple(range(n))
    total = 0.0
    for x in itertools.product(range(p), repeat=n):
        R = np.roll(T, shift=[-xi for xi in x], axis=axes)              # R[k] = T[k + x]
        total += (np.abs(np.fft.fftn(np.conj(R) * T)) ** 4).sum()
    return float(-np.log(total / p ** n))


def climbs(x):
    return max(x // 1000, 20) if SMOKE else x


def run(p, n, ce, co, cw, rng):
    D = p ** n
    A = array_points(p, n)
    E, O = array_sides(p, n)
    assert np.allclose(A[0] @ E, E) and np.allclose(A[0] @ O, -O) and np.allclose(A.sum(axis=0), D * np.eye(D))
    ceiling = (np.sqrt(D) - 1) / 2
    say(f"{n} wheel(s) of {p} levels: D = {D}, {len(A)} points, the even side {E.shape[1]} dimensions, the odd side "
        f"{O.shape[1]}; the ceiling (sqrt D - 1)/2 = {ceiling:.9f}")
    best = {}
    for name, Q, c in (("even", E, ce), ("odd", O, co), ("whole", None, cw)):
        Ak = A if Q is None else np.matmul(Q.conj().T, np.matmul(A, Q))     # round 3's compress, by matmul
        Ns, reps, stuck = r3.search(Ak, D, climbs(c), rng, batch=5000 if D < 40 else 1000 if D < 60 else 500)
        top = reps[max(reps)][0]
        psi = top if Q is None else Q @ top
        best[name] = Ns.max()
        par = float(np.real(np.vdot(psi, A[0] @ psi)))
        m2 = sre2(psi, p, n) if n > 1 else float("nan")
        extra = f"; M2 {m2:.6f}" if n > 1 else ""
        if (p, n) in KNIPFER and n > 1:
            extra += f" (Knipfer et al.: {KNIPFER[p, n][0]} = {KNIPFER[p, n][1]:.6f})"
        if n == 1 and name != "whole":
            SINGLE.setdefault(p, {})[name] = r3.wigner(psi[None, :], A, D)[0]
        if n == 2 and p in SINGLE:
            Wb = np.sort(r3.wigner(psi[None, :], A, D)[0])
            same = [a + "-" + b for a, b in (("even", "even"), ("odd", "odd"), ("even", "odd"))
                    if np.allclose(Wb, np.sort(np.outer(SINGLE[p][a], SINGLE[p][b]).ravel()), atol=1e-9)]
            extra += ("; its Wigner values are those of the product " + " and ".join(same)) if same else                 "; its Wigner values are no product's"
        else:
            same = None
        say(f"  {c} climbs, {name}: best {Ns.max():.12f}, {Ns.max() / ceiling:.4f} of the ceiling (reached "
            f"{int((Ns > Ns.max() - 1e-9).sum())} times; {stuck} still moving); its half-turn value {par:+.6f}; "
            f"purity on each wheel {purities(psi, p, n)}{extra} {clock()}")
        say(f"CHECK {p} {n} {name} {m2:.9f} {'na' if same is None else 'yes' if same else 'no'}")
    say(f"RESULT {p} {n} {best['even']:.12f} {best['odd']:.12f} {best['whole']:.12f}")
    return best


def mean_random_fraction(D):
    """the average of sum |W| over random pure states, as a fraction of sqrt D.  Each point's value <A_u> is 2B - 1
    with B ~ Beta((D+1)/2, (D-1)/2), since A_u has (D+1)/2 eigenvalues +1 and (D-1)/2 eigenvalues -1; E|B - 1/2| is
    exact through the incomplete beta function.  Above D = 10^12 the normal limit sqrt(2/pi) is used."""
    if D > 10 ** 12:
        return float(np.sqrt(2 / np.pi))
    from scipy.special import betainc
    a, b = (D + 1) / 2, (D - 1) / 2
    m = a / (a + b)
    e_abs = (m - 0.5) + 2 * (0.5 * betainc(a, b, 0.5) - m * betainc(a + 1, b, 0.5))
    return float(np.sqrt(D) * 2 * e_abs)


def combine():
    global LOG
    R, C = {}, {}
    for part in PLAN:
        for line in open(os.path.join(HERE, f"many_wheels_{part}.log"), encoding="utf-8"):
            if line.startswith("RESULT "):
                p, n, e, o, w = line.split()[1:]
                R[int(p), int(n)] = (float(e), float(o), float(w))
            if line.startswith("CHECK "):
                p, n, name, m2, prodvals = line.split()[1:]
                C[int(p), int(n), name] = (float(m2), prodvals)
    LOG = open(os.path.join(HERE, "many_wheels_combined.log"), "w", encoding="utf-8")
    S = lambda N: 1 + 2 * N                                              # sum of sizes, which multiplies
    Nof = lambda s: (s - 1) / 2
    best = {k: max(v) for k, v in R.items()}
    for (p, n), (e, o, w) in sorted(R.items()):
        ceiling = (np.sqrt(p ** n) - 1) / 2
        say(f"  {n} wheel(s) of {p}: even {e:.9f}, odd {o:.9f}, whole {w:.9f}; even ahead by {e - o:+.9f}; best "
            f"{best[p, n] / ceiling:.4f} of the ceiling")
    # products of smaller bests, side by side: a product's half-turn value is the product of its parts'
    prod = {}
    for (p, n) in R:
        if n == 1:
            continue
        cands_e, cands_o = [], []
        for m in range(1, n):
            if (p, m) in R and (p, n - m) in R:
                (e1, o1, _), (e2, o2, _) = R[p, m], R[p, n - m]
                cands_e += [S(e1) * S(e2), S(o1) * S(o2)]
                cands_o += [S(e1) * S(o2), S(o1) * S(e2)]
        if cands_e:
            prod[p, n] = (Nof(max(cands_e)), Nof(max(cands_o)))
            say(f"  {n} wheels of {p}: the best product of smaller arrays' bests: even {prod[p, n][0]:.9f}, odd "
                f"{prod[p, n][1]:.9f}")
    tol = 1e-6
    z0 = all(abs(R[p, 1][0] - KNOWN_ONE[p][0]) < tol and abs(R[p, 1][1] - KNOWN_ONE[p][1]) < tol for p in (3, 5, 7))
    z1 = max(R[3, 2]) < 8 / 9 + tol
    big = ((3, 3), (3, 4), (5, 2), (7, 2))
    z2 = all(best[k] > max(prod[k]) + tol for k in big)
    side = lambda k: "even" if R[k][0] > R[k][1] + tol else "odd" if R[k][1] > R[k][0] + tol else "tie"
    z3 = [side(k) for k in big] == ["odd", "even", "even", "even"]
    z4 = all(best[k] >= 0.88 * (np.sqrt(k[0] ** k[1]) - 1) / 2 for k in ((3, 2),) + big)
    z5 = abs(best[3, 4] - 98 / 27) < 1e-9
    z6 = all(C[3, 2, nm][1] == "yes" for nm in ("even", "odd", "whole"))
    z7 = all(C[k + (nm,)][0] < KNIPFER[k][1] - 1e-6 for k in ((5, 2), (7, 2)) for nm in ("even", "odd", "whole"))
    for name, ok, what in (
            ("Z0", z0, "one wheel reproduces the known bests at 3, 5 and 7"),
            ("Z1", z1, "two wheels of 3: nothing beats 8/9, the value of a product of two single-wheel bests"),
            ("Z2", z2, "three and four wheels of 3, two of 5 and two of 7: the best state beats every product of "
                       "smaller arrays' bests"),
            ("Z3", z3, "the pilot's coin holds: odd at three wheels of 3, even at four of 3, two of 5 and two of 7 "
                       f"(found: {', '.join(side(k) for k in big)})"),
            ("Z4", z4, "every best state, from two wheels on, reaches 88% of its ceiling"),
            ("Z5", z5, f"four wheels of 3: the best is 98/27, nothing higher (found {best[3, 4]:.12f})"),
            ("Z6", z6, "two wheels of 3: every best state found has the Wigner values of a product of single-wheel "
                       "bests"),
            ("Z7", z7, "two wheels of 5 and of 7: every best state found has M2 below Knipfer et al.'s values "
                       "(ln(625/49) and ln(2401/97))")):
        say(f"{name} {'HELD' if ok else 'DIED'}: {what}")
    say()
    say("the large-array numbers (forced, not searched): the best single-wheel state, repeated on every wheel, against "
        "the average random state, as fractions of the ceiling sqrt D of the sum of sizes")
    for p in (3, 5, 7):
        f1 = S(max(KNOWN_ONE[p])) / np.sqrt(p)
        cross = next(k for k in range(1, 200) if f1 ** k < mean_random_fraction(p ** k))
        row = ", ".join(f"{k} wheels: {f1 ** k:.3g} against {mean_random_fraction(p ** k):.3f}"
                        for k in (1, 2, 3, 4, 10, 100))
        say(f"  {p} levels: {row}; the average random state is ahead from {cross} wheels on")
    LOG.close()


def main():
    global LOG
    try:
        import ctypes
        ctypes.windll.kernel32.SetPriorityClass(ctypes.c_void_p(-1), 0x00004000)
    except Exception:
        pass
    if PART == "combine":
        combine()
        return
    LOG = open(os.path.join(HERE, f"many_wheels_{PART}.log"), "w", encoding="utf-8")
    for p, n, ce, co, cw in PLAN[PART]:
        run(p, n, ce, co, cw, np.random.default_rng([SEED, p, n]))
    LOG.close()


if __name__ == "__main__":
    main()
