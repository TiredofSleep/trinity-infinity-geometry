"""Why Z/n and -(x+y) mod n have the profiles they have: the 'gap' of a law.

In Z/n (x*y = x+y) a term is the sum of its leaves, so s = t holds iff for every
variable v, (#v in s) - (#v in t) = 0 mod n.  In x*y = -(x+y) a leaf at depth d
contributes (-1)^d, so s = t holds iff the signed counts agree mod n.  Let g(law) be
the gcd of the differences (0 if all vanish).  Then the law holds in the magma mod n
iff n divides g.  This script computes g for all 4694 laws, compares the predicted
profiles with the engine's direct computation, and lists the gaps that occur."""
import os, sys, math, time
from collections import Counter
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etpcore as E


def counts(t, sign, depth=0, acc=None):
    if acc is None:
        acc = Counter()
    if isinstance(t, int):
        acc[t] += (-1) ** depth if sign else 1
    else:
        counts(t[0], sign, depth + 1, acc)
        counts(t[1], sign, depth + 1, acc)
    return acc


def gap(i, sign):
    s, t = E.LAWS[i - 1]
    a, b = counts(s, sign), counts(t, sign)
    g = 0
    for v in set(a) | set(b):
        g = math.gcd(g, a[v] - b[v])
    return g


for sign, name, mk in ((False, "Z/n", lambda n: (np.add.outer(np.arange(n), np.arange(n))) % n),
                       (True, "-(x+y) mod n", lambda n: (-np.add.outer(np.arange(n), np.arange(n))) % n)):
    G = {i: gap(i, sign) for i in range(1, E.NLAWS + 1)}
    dist = Counter(G.values())
    print(name, ": gap distribution", dict(sorted(dist.items())))
    ok = True
    for n in range(1, 13):
        pred = {i for i, g in G.items() if g % n == 0}
        got = E.profile(mk(n)) if n <= 10 else E.profile_big(mk(n))
        print(f"   n={n}: predicted {len(pred)}  computed {len(got)}  equal={pred == got}")
        ok &= pred == got
    print("   all equal:", ok)
    if sign:
        six = sorted(i for i, g in G.items() if g == 6)
        print("   laws with gap 6 (hold mod 6 only among n>=4):", [(i, E.show(i)) for i in six])
