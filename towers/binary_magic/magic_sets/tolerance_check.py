"""
tolerance_check.py: Lemma 5 of LOWER_BOUND.md, and what it says about the published sets.

Lemma 5. TLC's Theorem 2 gives the noncontextual bound b = C - 2 w_min, where w_min is the least weight in
s + (column space of the incidence matrix). In a context-minimal clash the contexts have one dependency
(Lemma 2), so the column space is every even-weight vector, s + it is every odd-weight vector, and w_min = 1:
b = C - 2 and the noise tolerance is exactly 2/C.
Corollary. If w_min > 1, or if C - 1 > V - 2n for a genuine n-qubit set (Lemma 1 gives r <= V - 2n), the
contexts have a second dependency, and the set contains a proper sub-collection of its own contexts that is
itself a parity clash.
Checks: b = C - 2 by brute force on the context-minimal sets at hand, then TLC's Tables I-II as printed
(arXiv:2202.13141v2). Prints ASCII only.
"""
from ms_core import parse, check_magic, noncontextual_bound
from lower_bound2 import is_minimal
from waegell_stars import graph_star_cycle, odd_kernel, even_kernel, star

checks = []
def check(name, ok):
    checks.append(ok); print(("  ok   " if ok else "  FAIL ") + name)


def square():
    obs = "XI IX XX IZ ZI ZZ XZ ZX YY".split()
    return obs, [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8]]


print("1. b = C - 2 on context-minimal clashes (brute force over every +-1 assignment):")
for name, (obs, ctxs) in [("Mermin square", square()), ("pentagram (C_3 graph star)", graph_star_cycle(3)),
                          ("C_5 graph star", graph_star_cycle(5)), ("Waegell-Aravind 4-qubit Star", star(even_kernel(4), False)),
                          ("Waegell-Aravind 5-qubit Star", star(odd_kernel(5)))]:
    ops = [parse(l) for l in obs]
    clash, neg, _ = check_magic(ops, ctxs)
    V, C = len(obs), len(ctxs)
    b = noncontextual_bound(V, ctxs, neg)
    check(f"{name}: clash {clash}, context-minimal {is_minimal(V, ctxs)}, b = {b} of {C}, eps = 2/{C}",
          clash and is_minimal(V, ctxs) and b == C - 2)

# TLC Tables I and II as printed: (n, name, observables V, contexts C, b, Q); Table II also gives the
# degree / context-size profiles, used here only to confirm the transcription (incidences must agree).
TABLE = [(2, "Square", 9, 6, 4, 6, None, None), (3, "Pentagram", 10, 5, 3, 5, None, None),
         (3, "MS3-27", 27, 27, 21, 27, None, None), (4, "MS4-21", 21, 21, 15, 21, None, None),
         (4, "MS4-27", 27, 27, 17, 27, None, None), (5, "MS5-27", 27, 27, 17, 27, None, None),
         (3, "MS3-15", 15, 20, 14, 20, {4: 10, 6: 5}, {3: 10, 4: 10}),
         (3, "MS3-18", 18, 18, 12, 18, {2: 3, 4: 15}, {3: 6, 4: 12}),
         (3, "MS3-27b", 27, 27, 17, 27, {4: 27}, {4: 27}),
         (3, "MS3-29", 29, 33, 19, 33, {4: 27, 12: 2}, None),
         (4, "MS4-20", 20, 19, 17, 19, {2: 5, 4: 15}, {3: 6, 4: 13}),
         (4, "MS4-21b", 21, 16, 14, 16, {2: 11, 4: 10}, {3: 2, 4: 14}),
         (4, "MS4-21c", 21, 21, 19, 21, {2: 1, 4: 19, 6: 1}, {4: 21}),
         (4, "MS4-24", 24, 26, 20, 26, {2: 3, 4: 11, 6: 9, 10: 1}, {3: 2, 4: 12, 5: 12}),
         (5, "MS5-26", 26, 30, 24, 30, {4: 25, 10: 1}, {3: 10, 4: 20}),
         (5, "MS5-29", 29, 34, 28, 34, {4: 23, 6: 5, 8: 1}, {3: 6, 4: 28}),
         (5, "MS5-31", 31, 30, 24, 30, {2: 3, 4: 23, 6: 2, 8: 3}, {3: 2, 4: 12, 5: 16}),
         (6, "MS6-35", 35, 36, 30, 36, {4: 30, 8: 5}, {3: 3, 4: 14, 5: 19})]

print("\n2. The published table (Trandafir-Lisonek-Cabello, Tables I-II):")
ok = True
for n, name, V, C, b, Q, dg, sz in TABLE:
    ok &= Q == C and (dg is None or sum(dg.values()) == V)
    if dg and sz:
        ok &= sum(k * m for k, m in dg.items()) == sum(k * m for k, m in sz.items()) and sum(sz.values()) == C
check("transcription consistent: Q = C, and incidence totals agree wherever profiles are printed", ok)
hi_w = [name for n, name, V, C, b, Q, *_ in TABLE if (Q - b) // 2 > 1]
forced = [name for n, name, V, C, b, Q, *_ in TABLE if C - 1 > V - 2 * n]
print(f"  w_min = (C - b)/2 > 1 for {len(hi_w)} of {len(TABLE)}: {', '.join(hi_w)}")
print(f"  C - 1 > V - 2n for {len(forced)} of {len(TABLE)}: all but "
      f"{', '.join(name for _, name, *_ in TABLE if name not in forced)}")
check("13 of the 18 have w_min > 1 (the chat's count)", len(hi_w) == 13)
check("16 of the 18 must hide a smaller parity clash among their own contexts (by Lemmas 1-2 and their"
      " own qubit counts); only the square and the pentagram are context-minimal", len(forced) == 16
      and set(name for _, name, *_ in TABLE if name not in forced) == {"Square", "Pentagram"})

print(f"\n{sum(checks)} of {len(checks)} checks pass")
raise SystemExit(0 if all(checks) else 1)
