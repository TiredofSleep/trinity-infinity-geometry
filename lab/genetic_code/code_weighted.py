"""code_weighted.py -- part 2 of the fenced genetic-code study (PREREG.md, this folder), committed with its
predictions before the run.  The same question as part 1, with Freeland and Hurst's (1998) misreading weights by
letter position, and with a second amino-acid scale that has no ties.

  H1  calibration: with Freeland and Hurst's weights and polar requirement, at most 20 of a million random codes
      beat the standard code (they found about one in a million).
  H2  with those weights, the standard code is more optimized than the vertebrate mitochondrial code.
  H3  the best code found pairs its third letters: for one of the three ways to pair the four bases, every box's
      two pairs each share a meaning (with the scale's tied amino acids merged).
  H4  (forced) the weights cannot tell the three pairings apart: relabeling the third letter never changes the cost.
  H5  with a scale that has no ties (polar requirement and Kyte-Doolittle hydropathy, standardized), the best code
      found pairs its third letters too.

numpy only.  One process at below-normal priority.  ASCII output; also written to code_weighted.log.
Run:  python code_weighted.py      (about fifteen minutes; seeded, so a rerun repeats it)
"""
import ctypes
import itertools
import os

import numpy as np

try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.c_void_p(-1), 0x00004000)
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = open(os.path.join(HERE, "code_weighted.log"), "w", encoding="utf-8")
rng = np.random.default_rng(20261110)
SC = {}


def say(s=""):
    print(s, flush=True)
    LOG.write(s + "\n")
    LOG.flush()


STANDARD = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"   # NCBI table 1
MITO = "FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSS**VVVVAAAADDEEGGGG"       # NCBI table 2
PR = {"A": 7.0, "R": 9.1, "N": 10.0, "D": 13.0, "C": 4.8, "Q": 8.6, "E": 12.5, "G": 7.9, "H": 8.4, "I": 4.9,
      "L": 4.9, "K": 10.1, "M": 5.3, "F": 5.0, "P": 6.6, "S": 7.5, "T": 6.6, "W": 5.2, "Y": 5.4, "V": 5.6}
KD = {"I": 4.5, "V": 4.2, "L": 3.8, "F": 2.8, "C": 2.5, "M": 1.9, "A": 1.8, "G": -0.4, "T": -0.7, "S": -0.8,
      "W": -0.9, "Y": -1.3, "P": -1.6, "H": -3.2, "E": -3.5, "Q": -3.5, "D": -3.5, "N": -3.5, "K": -3.9, "R": -4.5}
AMINO = sorted(PR)
# Freeland and Hurst (1998): misreading weights by letter position, for transitions and transversions
FH = {0: (1.0, 0.5), 1: (0.5, 0.1), 2: (1.0, 1.0)}
TIES = {"P": "T", "I": "L"}                                            # polar requirement cannot tell these apart

PAIRS, WEIGHT = [], []
for c in range(64):
    b = [c // 16, (c // 4) % 4, c % 4]
    for pos in range(3):
        for nb in range(4):
            if nb != b[pos]:
                b2 = list(b)
                b2[pos] = nb
                c2 = 16 * b2[0] + 4 * b2[1] + b2[2]
                if c < c2:
                    ts = {b[pos], nb} in ({0, 1}, {2, 3})
                    PAIRS.append((c, c2))
                    WEIGHT.append(FH[pos][0] if ts else FH[pos][1])
PAIRS, WEIGHT = np.array(PAIRS), np.array(WEIGHT)


def z(scale):
    v = np.array([scale[a] for a in AMINO])
    return (v - v.mean()) / v.std()


PROPS = {"polar requirement": np.array([PR[a] for a in AMINO])[:, None],
         "polar requirement and hydropathy": np.stack([z(PR), z(KD)], axis=1)}


def cost(codes, props):
    """Freeland and Hurst's weighted mean squared change over single-letter changes between sense codons"""
    codes = np.atleast_2d(codes)
    sense = codes >= 0
    x = props[np.maximum(codes, 0)]                                    # (n, 64, m)
    a, b = x[:, PAIRS[:, 0]], x[:, PAIRS[:, 1]]
    ok = sense[:, PAIRS[:, 0]] & sense[:, PAIRS[:, 1]]
    d2 = ((a - b) ** 2).sum(axis=2)
    return (np.where(ok, d2, 0.0) * WEIGHT).sum(axis=1) / (ok * WEIGHT).sum(axis=1)


def as_codes(table):
    return np.array([AMINO.index(x) if x != "*" else -1 for x in table])


def letters(code):
    return "".join("*" if x < 0 else AMINO[x] for x in code)


def random_share(table, props, n=1_000_000, chunk=20_000):
    codes = as_codes(table)
    mine = cost(codes, props)[0]
    better = 0
    for start in range(0, n, chunk):
        m = min(chunk, n - start)
        perms = np.argsort(rng.random((m, 20)), axis=1)
        better += int((cost(np.where(codes >= 0, perms[:, np.maximum(codes, 0)], -1), props) < mine - 1e-12).sum())
    return mine, better / n


PAIRINGS = {"pyrimidine/purine (UC | AG)": ((0, 1), (2, 3)), "UA | CG": ((0, 2), (1, 3)),
            "UG | CA": ((0, 3), (1, 2))}


def pairing_of(code, merge_ties):
    """the third-letter pairings under which every box's two pairs each share a meaning"""
    s = letters(code)
    if merge_ties:
        s = "".join(TIES.get(ch, ch) for ch in s)
    box = np.array(list(s)).reshape(16, 4)
    return [name for name, ((a, b), (c, d)) in PAIRINGS.items()
            if ((box[:, a] == box[:, b]) & (box[:, c] == box[:, d])).all()]


def climb(start, props, units, chains=96, steps=200_000, t0=1.0, t1=1e-4):
    k = len(units)
    unit_of = np.empty(64, dtype=int)
    for j, u in enumerate(units):
        unit_of[u] = j
    meaning = np.array([start[u[0]] for u in units])
    S = np.tile(meaning, (chains, 1))
    for r in range(chains):
        S[r] = S[r][rng.permutation(k)]
    cur = cost(S[:, unit_of], props)
    rows = np.arange(chains)
    for t in t0 * (t1 / t0) ** (np.arange(steps) / (steps - 1)):
        i, j = rng.integers(0, k, chains), rng.integers(0, k, chains)
        new = S.copy()
        new[rows, i], new[rows, j] = S[rows, j], S[rows, i]
        c_new = cost(new[:, unit_of], props)
        accept = (c_new < cur) | (rng.random(chains) < np.exp(-(c_new - cur) / t))
        S[accept], cur[accept] = new[accept], c_new[accept]
    ii, jj = np.array([(i, j) for i in range(k) for j in range(i + 1, k)]).T
    improved = True
    while improved:
        improved = False
        for r in range(chains):
            trial = np.repeat(S[[r]], len(ii), axis=0)
            trial[np.arange(len(ii)), ii], trial[np.arange(len(ii)), jj] = S[r, jj], S[r, ii]
            c_t = cost(trial[:, unit_of], props)
            b = int(np.argmin(c_t))
            if c_t[b] < cur[r] - 1e-12:
                S[r], cur[r] = trial[b], c_t[b]
                improved = True
    order = np.argsort(cur)
    return S[order][:, unit_of], cur[order]


# ------------------------------------------------------------------ H1, H2
P1 = PROPS["polar requirement"]
c_std, f_std = random_share(STANDARD, P1)
c_mt, f_mt = random_share(MITO, P1)
say(f"Freeland and Hurst's weights, polar requirement: the standard code costs {c_std:.4f}, and {f_std * 1e6:.0f} of a "
    f"million random codes with its blocks beat it; the mitochondrial code costs {c_mt:.4f}, and {f_mt * 1e6:.0f} of a "
    f"million beat it")
SC["H1"] = f_std <= 20e-6
say(f"H1 {'HELD' if SC['H1'] else 'DIED'}: at most 20 of a million random codes beat the standard code "
    f"({f_std * 1e6:.0f})")
SC["H2"] = f_std < f_mt
say(f"H2 {'HELD' if SC['H2'] else 'DIED'}: the standard code is more optimized than the mitochondrial code "
    f"({f_std:.2e} against {f_mt:.2e})")

# ------------------------------------------------------------------ H4: the third letter's relabelings
codes_r = np.array([as_codes(MITO)[rng.permutation(64)] for _ in range(200)])
worst = 0.0
for perm in itertools.permutations(range(4)):
    relabel = np.array([16 * (c // 16) + 4 * ((c // 4) % 4) + perm[c % 4] for c in range(64)])
    for props in PROPS.values():
        moved = np.empty_like(codes_r)
        moved[:, relabel] = codes_r
        worst = max(worst, np.abs(cost(moved, props) - cost(codes_r, props)).max())
SC["H4"] = worst < 1e-12
say(f"H4 {'HELD' if SC['H4'] else 'DIED'}: all 24 relabelings of the third letter leave the cost unchanged, on 200 "
    f"random codes and both scales (largest change {worst:.1e}), so the weights cannot prefer one pairing")

# ------------------------------------------------------------------ H3, H5: climbing with the mitochondrial composition
mito = as_codes(MITO)
singles = [[c] for c in range(64)]
halves = [[4 * x + 0, 4 * x + 1] for x in range(16)] + [[4 * x + 2, 4 * x + 3] for x in range(16)]
found = {}
for label, props in PROPS.items():
    merge = label == "polar requirement"
    all_codes, all_cost = climb(mito, props, singles)
    sym_codes, sym_cost = climb(mito, props, halves)
    at_best = all_codes[all_cost < all_cost[0] + 1e-9]
    kinds = [pairing_of(c, merge) for c in at_best]
    found[label] = (all_cost[0], sym_cost[0], kinds)
    say(f"\n{label}{' (ties merged)' if merge else ''}:")
    say(f"  climbing over every code: best cost {all_cost[0]:.6f}, reached by {len(at_best)} of 96 chains; their "
        f"third-letter pairings: {kinds}")
    say(f"    the best code: {letters(all_codes[0])}")
    say(f"  climbing over pyrimidine/purine-paired codes only: best cost {sym_cost[0]:.6f}")
    say(f"    the best such code: {letters(sym_codes[0])}")
    say(f"  the natural codes: standard {cost(as_codes(STANDARD), props)[0]:.6f}, mitochondrial "
        f"{cost(mito, props)[0]:.6f}")
k3 = found["polar requirement"][2]
SC["H3"] = len(k3) > 0 and all(len(k) > 0 for k in k3)
say(f"\nH3 {'HELD' if SC['H3'] else 'DIED'}: every climb that reaches the best cost (polar requirement, ties merged) "
    f"pairs its third letters: {k3}")
k5 = found["polar requirement and hydropathy"][2]
SC["H5"] = len(k5) > 0 and all(len(k) > 0 for k in k5)
say(f"H5 {'HELD' if SC['H5'] else 'DIED'}: with the scale that has no ties, every climb that reaches the best cost "
    f"pairs its third letters: {k5}")
say(f"\nSCORE: {sum(SC.values())} of {len(SC)} held: " + ", ".join(f"{k} {'held' if v else 'died'}"
                                                              for k, v in SC.items()))
LOG.close()
