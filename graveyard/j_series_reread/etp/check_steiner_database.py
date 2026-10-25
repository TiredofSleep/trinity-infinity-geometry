"""Steiner quasigroups (squags) and the ETP catalog.

Archive claim (etp_database/verdicts): STS(3), STS(7), STS(9) have profile 382, cyclic
STS(13) and PG(3,2) STS(15) have profile 342 ("40 small-order coincidences").
Test: (1) a sound rewriting prover for squag laws (x*x = x, x*y = y*x, x*(x*y) = y);
(2) direct profiles of many Steiner triple systems."""
import os, sys, time, itertools, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etpcore as E

if len(sys.argv) < 2:
    sys.exit("usage: python check_steiner_database.py <archive>/etp_database   (<archive>: a checkout of the tag archive-2026-09-24; see ../README.md)")
ARCH = sys.argv[1]
t0 = time.time()


# ---- sound normal form for squag terms: every step is an instance of a squag axiom
def sq_nf(t, idem=True):
    if isinstance(t, int):
        return ("v", t)
    a, b = sq_nf(t[0], idem), sq_nf(t[1], idem)
    while True:
        if idem and a == b:                      # u*u = u
            return a
        # u*(u*w) = w, using commutativity inside the product
        if b[0] == "m" and a in (b[1], b[2]):
            return b[2] if a == b[1] else b[1]
        if a[0] == "m" and b in (a[1], a[2]):
            return a[2] if b == a[1] else a[1]
        x, y = sorted((a, b), key=repr)          # u*w = w*u
        return ("m", x, y)


def proved(i, idem=True):
    s, t = E.LAWS[i - 1]
    return sq_nf(s, idem) == sq_nf(t, idem)


def squag_from_blocks(v, blocks):
    T = -np.ones((v, v), dtype=np.int64)
    for x in range(v):
        T[x, x] = x
    for b in blocks:
        b = list(b)
        for i in range(3):
            for j in range(3):
                if i != j:
                    a, c = b[i], b[j]
                    assert T[a, c] < 0
                    T[a, c] = b[3 - i - j]
    assert (T >= 0).all()
    return T


def affine3(m):        # AG(m,3): x*y = -(x+y) componentwise over GF(3)
    pts = list(itertools.product(range(3), repeat=m))
    idx = {p: i for i, p in enumerate(pts)}
    v = len(pts)
    return np.array([[idx[tuple((-a - b) % 3 for a, b in zip(p, q))] for q in pts] for p in pts])


def projective2(m):    # PG(m-1,2): nonzero vectors of GF(2)^m, x*y = x+y (x != y), x*x = x
    v = 2 ** m - 1
    T = np.array([[(x + 1) ^ (y + 1) for y in range(v)] for x in range(v)]) - 1
    for x in range(v):
        T[x, x] = x
    return T


def cyclic_family(v):
    """search for base blocks {0,a,b} of a cyclic STS(v) (plus the short orbit if v = 3 mod 6)"""
    need = set(range(1, v))
    blocks = []
    if v % 6 == 3:
        third = v // 3
        need -= {third, 2 * third}
        blocks.append((0, third, 2 * third))
    def rec(need):
        if not need:
            return []
        d = min(need)
        for b in range(d + 1, v):
            a = d
            diffs = {a, v - a, b, v - b, (b - a) % v, (a - b) % v}
            if len(diffs) == 6 and diffs <= need:
                r = rec(need - diffs)
                if r is not None:
                    return [(0, a, b)] + r
        return None
    base = rec(need)
    out = set()
    for bb in base:
        for s in range(v):
            out.add(frozenset((x + s) % v for x in bb))
    if v % 6 == 3:
        for s in range(v // 3):
            out.add(frozenset((x + s) % v for x in blocks[0]))
    return squag_from_blocks(v, [tuple(sorted(b)) for b in out])


S3 = affine3(1)
P3 = E.profile(S3)
print("STS(3) profile size:", len(P3))
pr = [i for i in sorted(P3) if proved(i)]
print("laws of STS(3) proved for ALL squags by the rewriting normal form:", len(pr), "of", len(P3))
print("laws proved by rewriting that are NOT in STS(3) profile (soundness check, must be 0):",
      sum(1 for i in range(1, E.NLAWS + 1) if proved(i) and i not in P3))
arch = json.load(open(os.path.join(ARCH, "verdicts", "squag_variety_diff.json"), encoding="utf-8"))
forty = arch["small_sts_extras"]["eq_ids"]
print("the archive's 40 'small-order coincidences': proved for all squags:", sum(proved(i) for i in forty), "of", len(forty))
print("   archived profile_3 equals ours:", set(arch["profile_3"]["eq_ids"]) == P3)

systems = [("STS(7) Fano = PG(2,2)", projective2(3)), ("STS(9) = AG(2,3)", affine3(2)),
           ("STS(13) cyclic", cyclic_family(13)), ("STS(15) = PG(3,2)", projective2(4)),
           ("STS(15) cyclic", cyclic_family(15)), ("STS(19) cyclic", cyclic_family(19)),
           ("STS(21) cyclic", cyclic_family(21)), ("STS(25) cyclic", cyclic_family(25)),
           ("STS(27) = AG(3,3)", affine3(3)), ("STS(31) = PG(4,2)", projective2(5))]
for name, T in systems:
    v = len(T)
    is_squag = (all(T[x, x] == x for x in range(v)) and np.array_equal(T, T.T)
                and all(T[x, T[x, y]] == y for x in range(v) for y in range(v)))
    t1 = time.time()
    p = E.profile_big(T, samples=3000, prover=lambda i: proved(i))
    # independent of the prover: the archive's 40 laws checked exhaustively on this table
    direct = all(E.holds(i, T) for i in forty) if v <= 15 else None
    print(f"{name}: squag={is_squag}; profile size {len(p)}; equal to STS(3)'s: {p == P3};"
          f" the 40 laws hold (exhaustive): {direct}   ({time.time() - t1:.1f}s)")

# totally symmetric quasigroups (no idempotence): -(x+y) mod n
for n in (4, 5, 7):
    T = (-np.add.outer(np.arange(n), np.arange(n))) % n
    p = E.profile(T)
    pr2 = sum(1 for i in p if proved(i, idem=False))
    print(f"-(x+y) mod {n}: profile {len(p)}; proved for every totally symmetric quasigroup: {pr2}")
print("time %.1fs" % (time.time() - t0))
