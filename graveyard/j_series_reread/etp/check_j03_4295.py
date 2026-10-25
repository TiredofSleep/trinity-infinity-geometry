"""All finite models of ETP law 4295, x*(x*y) = y*(z*x), of orders 2..5, by an explicit
structure theorem (derived for this audit), then: isomorphism classes and smallest profiles.

Structure theorem.  T is a model of 4295 on M iff there are
  * a partition pi of M (elements with equal columns),
  * a nonempty set I of classes, a class Z in I,
  * a map K : pi -> I with K(r) = Z for every r in I,
  * a symmetric map E : I x I -> Z,
  * for each class p not in I, a column c_p : M -> K(p) (free),
such that T[x, s] = c_p(x) for s in a class p not in I, and T[x, s] = E[K(cls x), cls s]
for s in a class of I.  (Proof sketch: 4295 makes y*(z*x) independent of z, so all
entries of a column have equal columns; this gives K; comparing the classes of both
sides of 4295 forces K o K to be constant = Z; both sides then equal E[K(cls x), K(cls y)].)
Right-nested products u*(v*w) equal E[K(cls u), K(cls w)].
"""
import os, sys, time, itertools
from collections import Counter
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etpcore as E

C5 = {1, 4269, 4284, 4287, 4290, 4293, 4295, 4316, 4340, 4343, 4345, 4360, 4369, 4371}


def set_partitions(elems):
    if not elems:
        yield []
        return
    first, rest = elems[0], elems[1:]
    for part in set_partitions(rest):
        for i in range(len(part)):
            yield part[:i] + [[first] + part[i]] + part[i + 1:]
        yield [[first]] + part


def models_4295(n, only_nonconstant=False):
    M = list(range(n))
    codes = set()
    w = (n ** np.arange(n * n - 1, -1, -1)).astype(np.int64)
    for part in set_partitions(M):
        k = len(part)
        cls = [0] * n
        for ci, block in enumerate(part):
            for x in block:
                cls[x] = ci
        for r in range(1, k + 1):
            for I in itertools.combinations(range(k), r):
                rest = [p for p in range(k) if p not in I]
                for Z in I:
                    zvals = part[Z]
                    if only_nonconstant and (len(I) < 2 or len(zvals) < 2):
                        continue
                    pairs = [(a, b) for ai, a in enumerate(I) for b in I[ai:]]
                    for Kr in itertools.product(I, repeat=len(rest)):
                        K = {p: Z for p in I}
                        K.update(dict(zip(rest, Kr)))
                        for Ev in itertools.product(zvals, repeat=len(pairs)):
                            if only_nonconstant and len(set(Ev)) < 2:
                                continue
                            Em = {}
                            for (a, b), v in zip(pairs, Ev):
                                Em[a, b] = Em[b, a] = v
                            base = np.zeros((n, n), dtype=np.int64)
                            for s in M:
                                if cls[s] in I:
                                    for x in M:
                                        base[x, s] = Em[K[cls[x]], cls[s]]
                            free_cols = [s for s in M if cls[s] not in I]
                            # columns of the same class are equal: choose one function per class
                            choices = [list(itertools.product(part[K[p]], repeat=n)) for p in rest]
                            for pick in itertools.product(*choices):
                                T = base.copy()
                                for p, f in zip(rest, pick):
                                    for s in part[p]:
                                        T[:, s] = f
                                codes.add(int(T.ravel() @ w))
    return codes


def decode_many(codes, n):
    arr = np.array(sorted(codes), dtype=np.int64)
    digits = np.zeros((len(arr), n * n), dtype=np.int64)
    a = arr.copy()
    for j in range(n * n - 1, -1, -1):
        digits[:, j] = a % n
        a //= n
    return digits.reshape(-1, n, n)


def brute_models(n):
    tabs = np.array(list(itertools.product(range(n), repeat=n * n)), dtype=np.int64).reshape(-1, n, n)
    ok = E.holds_batch(4295, tabs.reshape(len(tabs), n * n), n)
    return tabs[ok]


t0 = time.time()
for n in (2, 3):
    mine = decode_many(models_4295(n), n)
    brute = brute_models(n)
    same = {tuple(T.ravel()) for T in mine} == {tuple(T.ravel()) for T in brute}
    print(f"order {n}: structure theorem gives {len(mine)} labeled models; brute force {len(brute)}; identical: {same}")
    both = sum(1 for T in brute if not (np.all(T == T[:, :1]) or np.all(T == T[:1, :])))
    print(f"   models depending on both arguments: {both} of {len(brute)}")

for n in (2, 3, 4, 5):
    t1 = time.time()
    tabs = decode_many(models_4295(n), n)
    canon = np.concatenate([E.canon_codes(tabs[i:i + 20000]) for i in range(0, len(tabs), 20000)])
    reps_codes, first = np.unique(canon, return_index=True)
    reps = tabs[first]
    # right-nested products constant -> all 112 laws u*(v*w) = u'*(v'*w') hold -> profile >= 113
    rn = np.array([len({int(T[u, T[v, w]]) for u in range(n) for v in range(n) for w in range(n)}) for T in reps])
    small = reps[rn > 1]
    M = E.profiles_batch(small) if len(small) else np.zeros((0, E.NLAWS), bool)
    sizes = M.sum(axis=1) if len(small) else np.array([], int)
    spec = int(sum(1 for row in M if set(np.flatnonzero(row) + 1) == C5))
    low = int(sizes.min()) if len(sizes) else None
    if n <= 3:
        allM = E.profiles_batch(reps)
        low_all = int(allM.sum(axis=1).min())
    else:
        low_all = low if (low is not None and low < 113) else None
    print(f"order {n}: {len(tabs)} labeled models, {len(reps)} up to isomorphism; "
          f"{len(small)} classes with non-constant right-nested products; smallest profile among them: {low}; "
          f"smallest overall: {low_all}; type specimens: {spec}   ({time.time() - t1:.1f}s)")
    if n == 5:
        print("   order-5 profile sizes among the non-constant classes:", dict(sorted(Counter(sizes.tolist()).items())))
print("time %.1fs" % (time.time() - t0))
