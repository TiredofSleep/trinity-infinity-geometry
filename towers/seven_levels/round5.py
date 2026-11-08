"""round5.py -- round 5 of PREREG.md, committed with its predictions before the run.

  seventeen (1 more than a multiple of 4) and nineteen (3 more): which side of the coin wins, by how much, what the
  winner looks like, and on which side the states of the binary tetrahedral, octahedral and icosahedral groups sit.

It uses round3.py's tools (the sign ascent) and round4.py's mirror test.  The exceptional groups are found as 2 x 2
matrices over F_p, and their operators are rebuilt from words in the Fourier transform, the shear and a primitive
multiplier.  numpy only.  One process per prime at below-normal priority and three threads; the two can run at once.
ASCII output; each part writes round5_<part>.log.
Run:  python round5.py seventeen
      python round5.py nineteen
      python round5.py combine      (after both: scores V3 from the two logs)
Set ROUND5_SMOKE=1 for a quick test of the code at a tiny size; its scores mean nothing.
"""
import os
import sys

PART = sys.argv[1] if len(sys.argv) > 1 else "seventeen"
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "3")
import time
from collections import Counter, deque

import numpy as np

import round3 as r3
import round4 as r4

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20261110
SMOKE = os.environ.get("ROUND5_SMOKE") == "1"
LOG = None
T0 = time.time()
SC = {}
mp = np.linalg.matrix_power


def n(x):
    return max(x // 5000, 2) if SMOKE else x


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def clock():
    return f"[{time.time() - T0:.0f} s]"


def score(name, held, text):
    SC[name] = bool(held)
    say(f"{name} {'HELD' if held else 'DIED'}: {text}")


# ------------------------------------------------------------------ SL(2, p) as 2 x 2 matrices, and its operators
def mul(X, Y, p):
    a, b, c, d = X
    e, f, g, h = Y
    return ((a * e + b * g) % p, (a * f + b * h) % p, (c * e + d * g) % p, (c * f + d * h) % p)


def order(X, p):
    Y, k = X, 1
    while Y != (1, 0, 0, 1):
        Y, k = mul(Y, X, p), k + 1
    return k


def closure(gens, p, cap):
    G, frontier = {(1, 0, 0, 1)}, [(1, 0, 0, 1)]
    while frontier and len(G) <= cap:
        new = []
        for x in frontier:
            for g in gens:
                y = mul(g, x, p)
                if y not in G:
                    G.add(y)
                    new.append(y)
        frontier = new
    return G


def matrix_of(perm, d):
    """the linear map of phase space behind a Clifford operation that fixes the centre: images of (1,0) and (0,1)"""
    q1, p1 = divmod(int(perm[d]), d)
    q2, p2 = divmod(int(perm[1]), d)
    return (q1, q2, p1, p2)


class Weil:
    """the operators of SL(2, p), rebuilt from words in three generators"""

    def __init__(self, d, A):
        w, X, Z, F, P, T = r3.basics(d)
        g = next(a for a in range(2, d) if len({pow(a, e, d) for e in range(1, d)}) == d - 1)
        M = np.eye(d)[[(pow(g, -1, d) * k) % d for k in range(d)]]
        self.d, self.A, self.P = d, A, P
        self.U = [F, T, M.astype(complex)]
        self.M = [matrix_of(r3.perm_of(U, A), d) for U in self.U]
        self.parent = {(1, 0, 0, 1): None}
        queue = deque([(1, 0, 0, 1)])
        while queue:                                                   # breadth-first: a word for every element
            x = queue.popleft()
            for i, gm in enumerate(self.M):
                y = mul(gm, x, d)
                if y not in self.parent:
                    self.parent[y] = (x, i)
                    queue.append(y)


def operator(W, X):
    """the Clifford operator (up to phase) whose phase-space map is the matrix X"""
    word = []
    while W.parent[X] is not None:
        x, i = W.parent[X]
        word.append(i)
        X = x
    U = np.eye(W.d, dtype=complex)
    for i in word:                                                     # word lists M_i outermost first
        U = U @ W.U[i]
    return U


def exceptional(W, p):
    """one binary tetrahedral, octahedral or icosahedral subgroup from each conjugacy class, found from a fixed
    element of order 4 and every element of order 3"""
    els = list(W.parent)
    a = next(x for x in els if order(x, p) == 4)
    threes = [x for x in els if order(x, p) == 3]
    profiles = {24: {1: 1, 2: 1, 3: 8, 4: 6, 6: 8},
                48: {1: 1, 2: 1, 3: 8, 4: 18, 6: 8, 8: 12},
                120: {1: 1, 2: 1, 3: 20, 4: 30, 5: 24, 6: 20, 10: 24}}
    names = {24: "tetrahedral", 48: "octahedral", 120: "icosahedral"}
    found = {}
    for b in threes:
        G = frozenset(closure([a, b], p, 121))
        if len(G) in profiles and dict(sorted(Counter(order(x, p) for x in G).items())) == profiles[len(G)]:
            reps = found.setdefault(len(G), [])
            if not any(conjugate(G, R, els, p) for R, _ in reps):
                reps.append((G, b))
    out = []
    for size in sorted(found):
        for k, (G, b) in enumerate(found[size]):
            out.append((f"binary {names[size]} (order {size}), class {k + 1}", a, b))
    return out


def conjugate(G, R, els, p):
    g0 = min(G)
    for h in els:
        hi = inverse(h, p)
        if mul(mul(h, g0, p), hi, p) in R and all(mul(mul(h, x, p), hi, p) in R for x in G):
            return True
    return False


def inverse(X, p):
    a, b, c, d = X
    return (d % p, (-b) % p, (-c) % p, a % p)


def fixed_states(Ua, Ub):
    """common eigenvectors of two operators: the states their group fixes up to phase"""
    out = []
    for Ea in r3.eigenspaces(Ua):
        for Eb in r3.eigenspaces(Ub):
            u, s, _ = np.linalg.svd(Ea.conj().T @ Eb)
            for j in np.where(s > 1 - 1e-8)[0]:
                out.append(Ea @ u[:, j])
    return out


# ------------------------------------------------------------------ one prime
def run(p, rng):
    A = r3.phase_points(p)
    E, O = r3.sides(p)
    w, X, Z, F, P, T = r3.basics(p)
    lins, mirs = r3.linear_parts(p), r4.mirror_parts(p)
    leg = 1 if pow(p - 1, (p - 1) // 2, p) == 1 else -1                # (-1 | p): the Legendre state's side
    side = "even" if leg == 1 else "odd"
    L = r3.legendre(p)
    WL = r3.wigner(L[None, :], A, p)[0]
    NL = r3.negativity(WL)
    say(f"{p} levels: the Legendre state is {side} (parity {np.real(np.vdot(L, P @ L)):+.0f}), total negativity "
        f"{NL:.12f}; " + "symmetries %d, orders %s, ceiling points %d, floor points %d, negative points %d, "
        "deepest %+.6f" % r3.describe(WL, p, lins))
    climbs = {"seventeen": (3_000_000, 3_000_000, 1_500_000), "nineteen": (2_000_000, 2_000_000, 1_000_000)}[PART]
    Ne, reps_e, _ = r3.search(r3.compress(A, E), p, n(climbs[0]), rng, batch=10000)
    say(f"  {climbs[0]} climbs among even states: best {Ne.max():.12f} (reached {int((Ne > Ne.max() - 1e-9).sum())} "
        f"times) {clock()}")
    No, reps_o, _ = r3.search(r3.compress(A, O), p, n(climbs[1]), rng, batch=10000)
    say(f"  {climbs[1]} climbs among odd states: best {No.max():.12f} (reached {int((No > No.max() - 1e-9).sum())} "
        f"times) {clock()}")
    Nf, reps_f, _ = r3.search(A, p, n(climbs[2]), rng, batch=5000)
    say(f"  {climbs[2]} climbs in the whole space: best {Nf.max():.12f} (reached {int((Nf > Nf.max() - 1e-9).sum())} "
        f"times) {clock()}")
    even_side = max(Ne.max(), NL if leg == 1 else -1)
    odd_side = max(No.max(), NL if leg == -1 else -1)
    margin = even_side - odd_side
    say(f"  the even side {even_side:.12f}, the odd side {odd_side:.12f}: the even side ahead by {margin:.6f}")
    best_state = max(((Nf.max(), reps_f[max(reps_f)][0]), (Ne.max(), E @ reps_e[max(reps_e)][0]),
                      (No.max(), O @ reps_o[max(reps_o)][0])), key=lambda t: t[0])[1]
    Wb = r3.wigner(best_state[None, :], A, p)[0]
    Db = r3.describe(Wb, p, lins)
    alone = r3.fixed_by_symmetry_alone(best_state, A, p, lins)
    say("  the best state found: symmetries %d, orders %s, ceiling points %d, floor points %d, negative points %d, "
        "deepest %+.6f" % Db + f"; fixed by its symmetries alone: {alone[0]} (residual {alone[1]:.1e})")
    Wo = r3.wigner((O @ reps_o[max(reps_o)][0])[None, :], A, p)[0]
    Do = r3.describe(Wo, p, lins)
    say("  the best odd state found: symmetries %d, orders %s, ceiling points %d, floor points %d, negative points %d, "
        "deepest %+.6f" % Do)
    We = r3.wigner((E @ reps_e[max(reps_e)][0])[None, :], A, p)[0]
    say("  the best even state found: symmetries %d, orders %s, ceiling points %d, floor points %d, negative points "
        "%d, deepest %+.6f" % r3.describe(We, p, lins))
    say(clock())

    # the exceptional groups' states
    Wl = Weil(p, A)
    groups = exceptional(Wl, p)
    ex_lines, on_side = [], True
    for name, a, b in groups:
        states = fixed_states(operator(Wl, a), operator(Wl, b))
        pars = [round(float(np.real(np.vdot(s, P @ s))), 6) for s in states]
        vals = [round(float(r3.negativity(r3.wigner(s[None, :], A, p)[0])), 6) for s in states]
        on_side &= all(abs(x - leg) < 1e-6 for x in pars)
        ex_lines.append(f"    {name}: fixes {len(states)} state(s); parities {pars}; total negativities {vals}")
    say(f"  the exceptional groups in SL(2, {p}) ({len(Wl.parent)} elements), one from each conjugacy class:")
    for ln in ex_lines:
        say(ln)
    say(clock())
    return dict(NL=NL, leg=leg, even=even_side, odd=odd_side, margin=margin, Db=Db, alone=alone[0], Do=Do,
                on_side=on_side, Ne=Ne, No=No, Nf=Nf, reps=(reps_e, reps_o, reps_f), A=A, E=E, O=O, lins=lins,
                mirs=mirs)


def combine():
    """V3: the margin at 19 is smaller than at 17, read from the two parts' logs"""
    global LOG
    m = {}
    for part, tag in (("seventeen", "17"), ("nineteen", "19")):
        for line in open(os.path.join(HERE, f"round5_{part}.log"), encoding="utf-8"):
            if line.startswith(f"margin at {tag}:"):
                m[tag] = float(line.split(":")[1])
    LOG = open(os.path.join(HERE, "round5_combined.log"), "w", encoding="utf-8")
    score("V3", m["19"] < m["17"], f"the margin at 19 ({m['19']:.6f}) is smaller than at 17 ({m['17']:.6f})")
    LOG.close()


def main():
    global LOG
    try:
        import ctypes
        ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x00004000)
    except Exception:
        pass
    if PART == "combine":
        combine()
        return
    p = {"seventeen": 17, "nineteen": 19}[PART]
    LOG = open(os.path.join(HERE, f"round5_{PART}.log"), "w", encoding="utf-8")
    rng = np.random.default_rng([SEED, p])
    R = run(p, rng)
    tag = "17" if p == 17 else "19"
    score(f"V{1 if p == 17 else 2}", R["margin"] > 1e-6, f"the even side wins at {tag}, by {R['margin']:.6f}")
    if p == 17:
        score("V4a", R["margin"] < 0.017, f"the margin at 17 is below 13's 0.017: {R['margin']:.6f}")
    else:
        score("V4b", R["margin"] < 0.0029, f"the margin at 19 is below 11's 0.0029: {R['margin']:.6f}")
    score(f"V5{'a' if p == 17 else 'b'}", R["Db"][2] == 1 and R["Db"][3] == 0 and not R["alone"],
          f"the best state found at {tag} touches the ceiling at {R['Db'][2]} point(s) and the floor at {R['Db'][3]}, "
          f"and its symmetries alone do not fix it: {not R['alone']}")
    if p == 19:
        score("V6", R["Do"][0] >= 12, f"the best odd state found at 19 has {R['Do'][0]} symmetries (at least 12)")
    beat = R["even"] if p == 17 else R["odd"]
    score(f"V7{'a' if p == 17 else 'b'}", beat > R["NL"] + 1e-6,
          f"the Legendre state of {tag} ({R['NL']:.6f}) is beaten on its own side: {beat:.6f}")
    score(f"V8{'a' if p == 17 else 'b'}", R["on_side"],
          "every state fixed by an exceptional group lies on the Legendre state's side "
          f"({'even' if R['leg'] == 1 else 'odd'})")
    reps_e, reps_o, reps_f = R["reps"]
    for name, reps, Ns, Q in (("even", reps_e, R["Ne"], R["E"]), ("odd", reps_o, R["No"], R["O"]),
                              ("whole-space", reps_f, R["Nf"], np.eye(p))):
        say(f"  the {name} climbs' five highest tops: "
            + ", ".join(f"{v:.9f} x{c}" for v, c in sorted(Counter(np.round(Ns, 9)).items(), reverse=True)[:5]))
        for v in sorted(reps, reverse=True)[:2]:
            Ws = [r3.wigner((Q @ s)[None, :], R["A"], p)[0] for s in reps[v]]
            same = all(r4.carries_ext(Ws[0], W2, p, R["lins"], R["mirs"]) for W2 in Ws[1:])
            say(f"    top {v:.9f}: symmetries %d, orders %s, ceiling points %d, floor points %d, negative points %d, "
                "deepest %+.6f" % r3.describe(Ws[0], p, R["lins"]) + f"; {len(Ws)} samples, one state up to symmetry "
                f"or mirror: {same}")
    say(f"\nmargin at {tag}: {R['margin']:.9f}")
    say(f"ROUND 5 ({PART}): {sum(SC.values())} of {len(SC)} held here: "
        + ", ".join(f"{k} {'held' if v else 'died'}" for k, v in SC.items()))
    LOG.close()


if __name__ == "__main__":
    main()
