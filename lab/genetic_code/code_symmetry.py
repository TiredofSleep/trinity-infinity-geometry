"""code_symmetry.py -- the fenced genetic-code study of PREREG.md (this folder), committed with its predictions
before the run.  It asks round 3's question of genetic codes: does the most error-resistant code keep the
third-letter symmetry, or break it?

  G0  calibration (Haig and Hurst 1991): the standard code's mean squared change in polar requirement over all
      single-letter changes between sense codons, MS0 = 5.194, and the share of random codes that beat it.
  G1  the vertebrate mitochondrial code, scored the same way against random codes with its own blocks.
  G2  with transitions weighted twice transversions, the best code found by climbing, over every code with the
      mitochondrial composition, keeps the third-letter pyrimidine/purine symmetry.
  G3  with every change weighted equally, it does not.

numpy only.  One process at below-normal priority.  ASCII output; also written to code_symmetry.log.
Run:  python code_symmetry.py      (a few minutes; seeded, so a rerun repeats it)
"""
import ctypes
import os
from itertools import product

import numpy as np

try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.c_void_p(-1), 0x00004000)
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = open(os.path.join(HERE, "code_symmetry.log"), "w", encoding="utf-8")
rng = np.random.default_rng(20261109)
SC = {}


def say(s=""):
    print(s, flush=True)
    LOG.write(s + "\n")
    LOG.flush()


BASES = "UCAG"                                                         # U, C pyrimidines; A, G purines
# NCBI translation tables 1 (standard) and 2 (vertebrate mitochondrial), codons in the order UUU, UUC, UUA, ...
STANDARD = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
MITO = "FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSS**VVVVAAAADDEEGGGG"
# polar requirement (Woese et al. 1966), as used by Haig and Hurst (1991)
PR = {"A": 7.0, "R": 9.1, "N": 10.0, "D": 13.0, "C": 4.8, "Q": 8.6, "E": 12.5, "G": 7.9, "H": 8.4, "I": 4.9,
      "L": 4.9, "K": 10.1, "M": 5.3, "F": 5.0, "P": 6.6, "S": 7.5, "T": 6.6, "W": 5.2, "Y": 5.4, "V": 5.6}
AMINO = sorted(PR)
PRV = np.array([PR[a] for a in AMINO])

# every unordered pair of codons that differ in one letter, with whether the change is a transition
PAIRS, TRANSITION = [], []
for c in range(64):
    b = [c // 16, (c // 4) % 4, c % 4]
    for pos in range(3):
        for nb in range(4):
            if nb != b[pos]:
                b2 = list(b)
                b2[pos] = nb
                c2 = 16 * b2[0] + 4 * b2[1] + b2[2]
                if c < c2:
                    PAIRS.append((c, c2))
                    TRANSITION.append({b[pos], nb} in ({0, 1}, {2, 3}))
PAIRS = np.array(PAIRS)
TRANSITION = np.array(TRANSITION)


def cost(codes, bias=1.0):
    """mean squared change in polar requirement over single-letter changes between sense codons; transversions
    weigh 1/bias against transitions.  codes: (n, 64) array of letters as indices into AMINO, stop = -1"""
    codes = np.atleast_2d(codes)
    pr = np.where(codes >= 0, PRV[np.maximum(codes, 0)], np.nan)
    w = np.where(TRANSITION, 1.0, 1.0 / bias)
    a, b = pr[:, PAIRS[:, 0]], pr[:, PAIRS[:, 1]]
    sense = ~(np.isnan(a) | np.isnan(b))
    d2 = np.where(sense, (a - b) ** 2, 0.0)
    return (d2 * w).sum(axis=1) / (sense * w).sum(axis=1)


def as_codes(table):
    return np.array([AMINO.index(x) if x != "*" else -1 for x in table])


def random_share(table, n=1_000_000, chunk=20_000):
    """the share of random codes, the same blocks with the 20 amino acids shuffled among them, that beat the code"""
    codes = as_codes(table)
    mine = cost(codes)[0]
    better = 0
    for start in range(0, n, chunk):
        m = min(chunk, n - start)
        perms = np.argsort(rng.random((m, 20)), axis=1)                 # amino acid i -> perms[:, i]
        shuffled = np.where(codes >= 0, perms[:, np.maximum(codes, 0)], -1)
        better += int((cost(shuffled) < mine - 1e-12).sum())
    return mine, better / n


def symmetric(code):
    """the third-letter pyrimidine/purine symmetry: xyU and xyC mean the same, and so do xyA and xyG"""
    c = np.asarray(code).reshape(16, 4)
    return bool(((c[:, 0] == c[:, 1]) & (c[:, 2] == c[:, 3])).all())


def climb(start, bias, units, chains=96, steps=200_000, t0=1.0, t1=1e-4):
    """simulated annealing over codes: swap the meanings of two units (single codons, or the two codons of a
    third-letter half-box), then polish by trying every swap until none helps.  start: one code (64,)"""
    k = len(units)
    unit_of = np.empty(64, dtype=int)                                  # the unit each codon belongs to
    for j, u in enumerate(units):
        unit_of[u] = j
    meaning = np.array([start[u[0]] for u in units])                   # each unit carries one meaning
    S = np.tile(meaning, (chains, 1))
    for r in range(chains):
        S[r] = S[r][rng.permutation(k)]

    def expand(S):
        return S[:, unit_of]

    cur = cost(expand(S), bias)
    temps = t0 * (t1 / t0) ** (np.arange(steps) / (steps - 1))
    rows = np.arange(chains)
    for t in temps:
        i, j = rng.integers(0, k, chains), rng.integers(0, k, chains)
        new = S.copy()
        new[rows, i], new[rows, j] = S[rows, j], S[rows, i]
        c_new = cost(expand(new), bias)
        accept = (c_new < cur) | (rng.random(chains) < np.exp(-(c_new - cur) / t))
        S[accept], cur[accept] = new[accept], c_new[accept]
    pairs = [(i, j) for i in range(k) for j in range(i + 1, k)]
    improved = True
    while improved:                                                    # polish: the best single swap, until none helps
        improved = False
        for r in range(chains):
            trial = np.repeat(S[[r]], len(pairs), axis=0)
            ii, jj = np.array(pairs).T
            trial[np.arange(len(pairs)), ii], trial[np.arange(len(pairs)), jj] = S[r, jj], S[r, ii]
            c_t = cost(expand(trial), bias)
            b = int(np.argmin(c_t))
            if c_t[b] < cur[r] - 1e-12:
                S[r], cur[r] = trial[b], c_t[b]
                improved = True
    codes = expand(S)
    order = np.argsort(cur)
    return codes[order], cur[order]


def letters(code):
    return "".join("*" if x < 0 else AMINO[x] for x in code)


# ------------------------------------------------------------------ G0, G1
s_std, f_std = random_share(STANDARD)
say(f"G0 data: the standard code's MS0 = {s_std:.4f}; {f_std * 1e6:.0f} of 1000000 random codes with its blocks "
    "beat it")
SC["G0"] = abs(s_std - 5.194) < 0.0005 and 5e-5 <= f_std <= 3e-4
say(f"G0 {'HELD' if SC['G0'] else 'DIED'}: MS0 is Haig and Hurst's 5.194, and the share is between 5e-5 and 3e-4")
s_mt, f_mt = random_share(MITO)
say(f"G1 data: the vertebrate mitochondrial code's MS0 = {s_mt:.4f}; {f_mt * 1e6:.0f} of 1000000 random codes with "
    f"its blocks beat it")
SC["G1"] = f_mt > f_std
say(f"G1 {'HELD' if SC['G1'] else 'DIED'}: the mitochondrial code is less optimized than the standard code "
    f"({f_mt:.2e} against {f_std:.2e} of random codes beat it)")

# ------------------------------------------------------------------ G2, G3: climbing with the mitochondrial composition
mito = as_codes(MITO)
singles = [[c] for c in range(64)]
halves = [[4 * x + 0, 4 * x + 1] for x in range(16)] + [[4 * x + 2, 4 * x + 3] for x in range(16)]
assert symmetric(mito)
results = {}
for bias in (2.0, 1.0):
    all_codes, all_cost = climb(mito, bias, singles)
    sym_codes, sym_cost = climb(mito, bias, halves)
    results[bias] = (all_codes, all_cost, sym_codes, sym_cost)
    n_best = int((all_cost < all_cost[0] + 1e-9).sum())
    n_sym = sum(symmetric(c) for c in all_codes[all_cost < all_cost[0] + 1e-9])
    say(f"\nbias {bias:g} (transitions weigh {bias:g} times transversions):")
    say(f"  climbing over every code: best cost {all_cost[0]:.6f}, reached by {n_best} of 96 chains, {n_sym} of them "
        f"with the third-letter symmetry")
    say(f"    the best code: {letters(all_codes[0])}")
    say(f"  climbing over symmetric codes only: best cost {sym_cost[0]:.6f}")
    say(f"    the best symmetric code: {letters(sym_codes[0])}")
    say(f"  the natural codes at this bias: standard {cost(as_codes(STANDARD), bias)[0]:.6f}, mitochondrial "
        f"{cost(mito, bias)[0]:.6f}")
c2, s2 = results[2.0][0], results[2.0][2]
SC["G2"] = symmetric(c2[0]) and abs(results[2.0][1][0] - results[2.0][3][0]) < 1e-9
say(f"\nG2 {'HELD' if SC['G2'] else 'DIED'}: with transition bias the best code found keeps the third-letter symmetry "
    f"({symmetric(c2[0])}), at the same cost as the best symmetric code "
    f"({results[2.0][1][0]:.6f} against {results[2.0][3][0]:.6f})")
SC["G3"] = not symmetric(results[1.0][0][0])
say(f"G3 {'HELD' if SC['G3'] else 'DIED'}: with equal weights the best code found breaks the third-letter symmetry "
    f"({not symmetric(results[1.0][0][0])}); best over every code {results[1.0][1][0]:.6f}, best symmetric "
    f"{results[1.0][3][0]:.6f}")
say(f"\nSCORE: {sum(SC.values())} of {len(SC)} held: " + ", ".join(f"{k} {'held' if v else 'died'}"
                                                              for k, v in SC.items()))
LOG.close()
