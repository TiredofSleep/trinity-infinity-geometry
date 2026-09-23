#!/usr/bin/env python3
"""three_renderings.py -- which structure belongs to the DESCRIPTIONS, and which to one AI RENDERING?

The composition tables were built by AI from verbal descriptions of the ten operators (VOID,
LATTICE, COUNTER, PROGRESS, COLLAPSE, BALANCE, CHAOS, HARMONY, BREATH, RESET). Three renderings
exist in the source history, all in CK's first commit (2026-03-03, ck.h):

  CL_STD   "the Standard table, 44 harmony" -- from the author's first repo
  CL_TSML  73 harmony -- the runtime's table
  CL_BHML  28 harmony

A property that holds in all three renderings is plausibly the descriptions' content. A property
that holds in one rendering (or one pairing) only is a property of that AI rendering.

    python verification/three_renderings.py      (~30 s)

See 04_meta/FOUNDATION_NULL_MODEL_AUDIT.md.
"""
import numpy as np

from foundation_null_model import BHML, N, SUBSETS, TSML, antisym, closure_dim

STD = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 7, 8, 1], [2, 3, 4, 5, 6, 7, 7, 8, 7, 2],
       [3, 4, 5, 6, 7, 7, 7, 7, 7, 3], [4, 5, 6, 7, 7, 7, 7, 8, 7, 4], [5, 6, 7, 7, 7, 8, 7, 7, 7, 5],
       [6, 7, 7, 7, 7, 7, 8, 7, 7, 6], [7, 7, 8, 7, 8, 7, 7, 8, 7, 7], [8, 8, 7, 7, 7, 7, 7, 7, 7, 8],
       [9, 1, 2, 3, 4, 5, 6, 7, 8, 0]]
TABS = {"STD": np.array(STD), "TSML": np.array(TSML), "BHML": np.array(BHML)}
CORE = (0, 7, 8, 9)
NAMES = ["VOID", "LATTICE", "COUNTER", "PROGRESS", "COLLAPSE", "BALANCE", "CHAOS", "HARMONY", "BREATH", "RESET"]


def closed_sets(*Ts):
    return [s for s in SUBSETS if all(all(T[a, b] in s for a in s for b in s) for T in Ts)]


def void_role(T):
    if all(T[0, j] == j for j in range(N)):
        return "identity"
    if all(T[0, j] == 0 for j in range(N) if j != 7):
        return "absorber"
    return "other"


def attractor(A, B, iters=4000):
    p = np.full(N, 0.1)
    for _ in range(iters):
        o = np.zeros(N)
        for i in range(N):
            for j in range(N):
                o[A[i, j]] += 0.5 * p[i] * p[j]
                o[B[i, j]] += 0.5 * p[i] * p[j]
        p = o / o.sum()
    return p


if __name__ == "__main__":
    print("=" * 78)
    print("THREE RENDERINGS OF ONE SET OF DESCRIPTIONS -- what is shared, what is rendering-specific")
    print("=" * 78)
    print(f"{'':6}{'HARM':>6}{'VOID role':>11}{'7 absorbs':>11}{'8*8':>5}{'9*9':>5}{'4-core closed':>15}{'Lie dim':>9}  closed-set sizes")
    for nm, T in TABS.items():
        print(f"{nm:6}{int((T == 7).sum()):>6}{void_role(T):>11}{str(all(T[7, j] == 7 for j in range(N))):>11}"
              f"{T[8, 8]:>5}{T[9, 9]:>5}{str(all(T[a, b] in CORE for a in CORE for b in CORE)):>15}"
              f"{closure_dim([antisym(T.tolist(), i) for i in range(N)]):>9}  {sorted({len(s) for s in closed_sets(T)})}")
    agree = [(i, j, int(TABS['STD'][i, j])) for i in range(N) for j in range(i, N)
             if TABS['STD'][i, j] == TABS['TSML'][i, j] == TABS['BHML'][i, j]]
    assert len(agree) == 12
    print(f"\ncells (unordered) where ALL THREE renderings agree: {len(agree)} of 55")
    for i, j, v in agree:
        print(f"    {NAMES[i]} * {NAMES[j]} = {NAMES[v]}")
    print("\npairings:")
    for a, b in [("TSML", "BHML"), ("STD", "BHML"), ("STD", "TSML")]:
        cs = closed_sets(TABS[a], TABS[b])
        p = attractor(TABS[a], TABS[b])
        supp = [i for i in range(N) if p[i] > 1e-9]
        print(f"  {a}+{b}: agree on {int((TABS[a] == TABS[b]).sum())}/100 cells | 4-core jointly closed: {CORE in cs} | "
              f"closed-set sizes {sorted({len(s) for s in cs})}")
        print(f"      alpha=1/2 attractor support {supp}, H/Br = {p[7] / p[8]:.6f}  (1+sqrt3 = {1 + 3 ** 0.5:.6f})")
    print("\nREADING")
    print("  DESCRIPTION-LEVEL (all three renderings): {VOID, HARMONY, BREATH, RESET} closes on itself;")
    print("    BREATH*BREATH = HARMONY; CHAOS with LATTICE..BALANCE, HARMONY or BREATH gives HARMONY;")
    print("    LATTICE*COUNTER = PROGRESS; BALANCE*BREATH = HARMONY.")
    print("  RENDERING-LEVEL (one rendering or one pairing): VOID as identity vs absorber; the chain with")
    print("    forbidden sizes {2,3} (TSML+BHML only); so(9) vs so(10); RESET*RESET; H/Br = 1+sqrt3 (the two")
    print("    pairings where exactly one table has HARMONY*HARMONY = BREATH); every count built on one table.")
    print("=" * 78)
