"""symmetry_check.py -- is every candidate's symmetry g_c really a symmetry of S?

Both proofs (bb.c and arb_check.py) read, for each candidate c, integers (eps, alpha, t, k_1..k_{p-1}, n_1..n_{p-1})
from candidates_P.txt and use the map

    g_c(phi)_x = eps (phi(alpha x + t) - phi(t)) + 2 pi k_x / p + 2 pi n_x        (x = 1 .. p-1; phi(0) = 0)

in step 4 of the proof: g_c maps X_0 into B_c, so phi_c* = g_c(phi_0*) and S(phi_c*) = S(phi_0*). Neither program
checks that g_c preserves S; prepare.py, which wrote the integers, is not trusted. This script checks it.

g_c preserves S when
  - eps is 1 or -1 (complex conjugation sends W(q, s) to W(q, -s));
  - alpha is in 1 .. p-1 and t in 0 .. p-1 (x -> alpha x + t is an affine bijection of F_p, a Clifford operation;
    subtracting phi(t) is a global phase);
  - k_x = beta x + gamma x^2 (mod p) for some beta, gamma in F_p, with each k_x in 0 .. p-1 (the diagonal Clifford
    phase omega^(beta x + gamma x^2); bb.c indexes a table by k_x, so the range matters there too);
  - the n_x are integers (2 pi n_x changes nothing).
These are exact integer checks; they are the part of the proof. As a sanity check only, S(g_c(phi)) is also compared
with S(phi) in floating point at random phi.

  python -I symmetry_check.py        (writes symmetry_check.log)
"""
import cmath
import math
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))


def read_candidates(path, p):
    tok = open(path).read().split()
    assert tok[0] == 'P' and int(tok[1]) == p
    dim = p - 1
    n = int(tok[7])
    pos, out = 8, []
    for _ in range(n):
        pos += dim                                   # the point itself (hex doubles) is not needed here
        e, al, t = int(tok[pos]), int(tok[pos + 1]), int(tok[pos + 2])
        pos += 3
        k = [int(x) for x in tok[pos:pos + dim]]
        pos += dim
        nn = [int(x) for x in tok[pos:pos + dim]]
        pos += dim
        out.append(dict(eps=e, alpha=al, t=t, k=k, n=nn))
    assert pos == len(tok), "trailing data in " + path
    return out


def quadratic(k, p):
    """(beta, gamma) with k_x = beta x + gamma x^2 mod p for x = 1..p-1, or None"""
    for beta in range(p):
        for gamma in range(p):
            if all((beta * x + gamma * x * x - k[x - 1]) % p == 0 for x in range(1, p)):
                return beta, gamma
    return None


def S(phi, p):
    """total absolute Wigner value of the diagonal state with phases phi (phi[0] = 0), floating point"""
    tot = 0.0
    for q in range(p):
        for s in range(p):
            E = 1.0
            for u in range(1, (p - 1) // 2 + 1):
                E += 2 * math.cos(phi[(q + u) % p] - phi[(q - u) % p] - 4 * math.pi * s * u / p)
            tot += abs(E)
    return tot / p ** 2


def apply(c, phi, p):
    out = [0.0] * p
    for x in range(1, p):
        d = phi[(c['alpha'] * x + c['t']) % p] - phi[c['t']]
        if c['eps'] < 0:
            d = -d
        out[x] = d + 2 * math.pi * c['k'][x - 1] / p + 2 * math.pi * c['n'][x - 1]
    return out


def main():
    lines = []
    allok = True
    rng = random.Random(20261124)
    for p in (3, 5, 7):
        cands = read_candidates(os.path.join(HERE, f"candidates_{p}.txt"), p)
        bad, worst = [], 0.0
        for i, c in enumerate(cands):
            ok = (c['eps'] in (1, -1) and 1 <= c['alpha'] <= p - 1 and 0 <= c['t'] <= p - 1
                  and len(c['k']) == p - 1 and all(0 <= v <= p - 1 for v in c['k'])
                  and quadratic(c['k'], p) is not None and len(c['n']) == p - 1)
            if not ok:
                bad.append(i)
            for _ in range(200):
                phi = [0.0] + [rng.uniform(0, 2 * math.pi) for _ in range(p - 1)]
                worst = max(worst, abs(S(apply(c, phi, p), p) - S(phi, p)))
        allok &= not bad
        maps = sorted({(c['eps'], c['alpha'], c['t']) + tuple(quadratic(c['k'], p) or ()) for c in cands})
        lines.append(f"p = {p}: {len(cands)} candidates; symmetry data valid for "
                     f"{len(cands) - len(bad)} of {len(cands)}{'' if not bad else ' (invalid: ' + str(bad) + ')'}; "
                     f"distinct (eps, alpha, t, beta, gamma): {len(maps)}; "
                     f"sanity: |S(g phi) - S(phi)| <= {worst:.1e} at 200 random phi per candidate")
    lines.append("VERDICT " + ("PASS: every g_c is an affine map of F_p, conjugation or not, a diagonal Clifford phase "
                               "and multiples of 2 pi, so it preserves S" if allok else "FAIL"))
    with open(os.path.join(HERE, "symmetry_check.log"), 'w') as f:
        for s in lines:
            print(s)
            f.write(s + '\n')


if __name__ == '__main__':
    main()
