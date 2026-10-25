"""etpcore.py -- an independent rebuild of the ETP law catalog and a profile engine.

Written fresh for this audit (does not import or copy the archived scripts).

Catalog definition (Equational Theories Project, Tao et al. 2024-25): all magma laws
s = t with at most four operations in total, taken up to renaming of variables and
up to swapping the two sides, the trivial laws t = t removed except x = x.  Numbering:
by total number of operations; then by the number of operations on the smaller side
(the left side is the smaller); then by the shape of the left tree, then of the right
tree (shapes listed recursively by size of the left subtree); then by the variable
pattern, as a restricted-growth string over the leaves read left to right.  The first
member of each equivalence class met in this order keeps the number.
"""
import itertools
import numpy as np

LEAF = 0  # a shape is LEAF or a pair (left_shape, right_shape)


def all_shapes(ops):
    """binary tree shapes with `ops` internal nodes, in catalog order"""
    if ops == 0:
        return [LEAF]
    out = []
    for left_ops in range(ops):
        for a in all_shapes(left_ops):
            for b in all_shapes(ops - 1 - left_ops):
                out.append((a, b))
    return out


def count_leaves(shape):
    return 1 if shape == LEAF else count_leaves(shape[0]) + count_leaves(shape[1])


def growth_strings(length):
    """restricted-growth strings of the given length, lexicographic (0 first)"""
    if length == 0:
        return [()]
    res = [(0,)]
    for _ in range(length - 1):
        nxt = []
        for s in res:
            top = max(s)
            for v in range(top + 2):
                nxt.append(s + (v,))
        res = nxt
    return res


def plant(shape, labels, pos=0):
    """fill the leaves of `shape` with labels[pos:], return (term, next_pos).
    A term is an int (a variable) or a pair of terms."""
    if shape == LEAF:
        return labels[pos], pos + 1
    a, pos = plant(shape[0], labels, pos)
    b, pos = plant(shape[1], labels, pos)
    return (a, b), pos


def term_vars(t, acc=None):
    if acc is None:
        acc = []
    if isinstance(t, int):
        acc.append(t)
    else:
        term_vars(t[0], acc)
        term_vars(t[1], acc)
    return acc


def nops(t):
    return 0 if isinstance(t, int) else 1 + nops(t[0]) + nops(t[1])


def rename(t, m):
    return m[t] if isinstance(t, int) else (rename(t[0], m), rename(t[1], m))


def normal_pair(s, t):
    """rename variables in order of first appearance, reading s then t"""
    m = {}
    for v in term_vars(s) + term_vars(t):
        if v not in m:
            m[v] = len(m)
    return rename(s, m), rename(t, m)


def law_key(s, t):
    """equivalence-class key: renaming, and side swap"""
    a = repr(normal_pair(s, t))
    b = repr(normal_pair(t, s))
    return min(a, b)


def build_catalog():
    laws = []
    seen = set()
    for total in range(5):
        for small in range(total // 2 + 1):
            for sl in all_shapes(small):
                for sr in all_shapes(total - small):
                    nl = count_leaves(sl) + count_leaves(sr)
                    for g in growth_strings(nl):
                        s, p = plant(sl, g)
                        t, _ = plant(sr, g, p)
                        if total > 0 and s == t:
                            continue
                        k = law_key(s, t)
                        if k in seen:
                            continue
                        seen.add(k)
                        laws.append((s, t))
    return laws


LAWS = build_catalog()
NLAWS = len(LAWS)
NV = [max(term_vars(s) + term_vars(t)) + 1 for s, t in LAWS]


def show_term(t, top=True):
    if isinstance(t, int):
        return "xyzwuv"[t]
    a = show_term(t[0], False)
    b = show_term(t[1], False)
    s = a + " * " + b
    return s if top else "(" + s + ")"


def show(i):
    s, t = LAWS[i - 1]
    return show_term(s) + " = " + show_term(t)


# ---------------------------------------------------------------- mirror (opposite magma)

def mirror_term(t):
    return t if isinstance(t, int) else (mirror_term(t[1]), mirror_term(t[0]))


KEY2ID = {law_key(s, t): i for i, (s, t) in enumerate(LAWS, start=1)}


def law_id(s, t):
    return KEY2ID[law_key(s, t)]


MIRROR = [0] + [law_id(mirror_term(s), mirror_term(t)) for s, t in LAWS]


# ---------------------------------------------------------------- evaluation

_GRID = {}


def grid(n, k):
    if (n, k) not in _GRID:
        _GRID[n, k] = np.indices((n,) * k).reshape(k, -1)
    return _GRID[n, k]


def ev1(t, T, env):
    """value of term t in table T (n x n array) at the assignments env (k x N)"""
    if isinstance(t, int):
        return env[t]
    return T[ev1(t[0], T, env), ev1(t[1], T, env)]


def holds(i, T):
    T = np.asarray(T)
    s, t = LAWS[i - 1]
    env = grid(len(T), NV[i - 1])
    return bool(np.array_equal(ev1(s, T, env), ev1(t, T, env)))


def profile(T):
    """set of catalog numbers of the laws that hold in T (exhaustive check)"""
    T = np.asarray(T)
    return {i for i in range(1, NLAWS + 1) if holds(i, T)}


def profile_big(T, samples=4000, rng=None, prover=None, exhaustive_limit=6 * 10 ** 7):
    """profile for larger tables: refute by random assignments first; a law that
    survives is either proved by `prover(i)` (a sound proof that it holds in every
    member of a class T belongs to) or checked exhaustively (chunked)."""
    T = np.asarray(T)
    n = len(T)
    rng = np.random.default_rng(12345) if rng is None else rng
    out = set()
    undecided = []
    for i in range(1, NLAWS + 1):
        s, t = LAWS[i - 1]
        k = NV[i - 1]
        if n ** k <= 20000:
            if holds(i, T):
                out.add(i)
            continue
        env = rng.integers(0, n, size=(k, samples))
        if not np.array_equal(ev1(s, T, env), ev1(t, T, env)):
            continue
        if prover is not None and prover(i):
            out.add(i)
            continue
        undecided.append(i)
    for i in undecided:
        s, t = LAWS[i - 1]
        k = NV[i - 1]
        total = n ** k
        if total > exhaustive_limit:
            raise RuntimeError(f"law {i} undecided and too large to check exhaustively (n^k={total})")
        ok = True
        step = 2_000_000
        for start in range(0, total, step):
            idx = np.arange(start, min(total, start + step))
            env = np.array(np.unravel_index(idx, (n,) * k))
            if not np.array_equal(ev1(s, T, env), ev1(t, T, env)):
                ok = False
                break
        if ok:
            out.add(i)
    return out


# ---------------------------------------------------------------- batch evaluation (many tables)

def ev_batch(t, TF, n, env):
    """TF: (B, n*n) flattened tables; env: (k, N) assignments -> (B, N) or (N,) for a variable"""
    if isinstance(t, int):
        return env[t]
    a = ev_batch(t[0], TF, n, env)
    b = ev_batch(t[1], TF, n, env)
    idx = a * n + b
    if idx.ndim == 1:
        return TF[:, idx]
    return np.take_along_axis(TF, idx, axis=1)


def holds_batch(i, TF, n, env=None):
    s, t = LAWS[i - 1]
    if env is None:
        env = grid(n, NV[i - 1])
    a = ev_batch(s, TF, n, env)
    b = ev_batch(t, TF, n, env)
    B = TF.shape[0]
    if a.ndim == 1:
        a = np.broadcast_to(a, (B, a.shape[0]))
    if b.ndim == 1:
        b = np.broadcast_to(b, (B, b.shape[0]))
    return np.all(a == b, axis=1)


def profiles_batch(tables, laws=None, prefilter=8, seed=7):
    """boolean matrix (B, len(laws)) of which laws hold in each table (exhaustive, with a
    random-assignment prefilter that only removes laws already refuted)."""
    tables = np.asarray(tables)
    B, n, _ = tables.shape
    TF = tables.reshape(B, n * n).astype(np.int64)
    laws = list(range(1, NLAWS + 1)) if laws is None else laws
    res = np.zeros((B, len(laws)), dtype=bool)
    rng = np.random.default_rng(seed)
    for col, i in enumerate(laws):
        k = NV[i - 1]
        alive = np.arange(B)
        if prefilter and n ** k > 4 * prefilter:
            env = rng.integers(0, n, size=(k, prefilter))
            ok = holds_batch(i, TF, n, env)
            alive = np.flatnonzero(ok)
            if len(alive) == 0:
                continue
        ok = holds_batch(i, TF[alive], n)
        res[alive[ok], col] = True
    return res


# ---------------------------------------------------------------- isomorphism classes

def canon_codes(tables):
    """for each n x n table, the minimal base-n code over all relabelings"""
    tables = np.asarray(tables)
    B, n, _ = tables.shape
    best = None
    weights = (n ** np.arange(n * n - 1, -1, -1)).astype(np.int64)
    for p in itertools.permutations(range(n)):
        p = np.array(p)
        inv = np.argsort(p)
        # relabeled table U[a, b] = p[T[inv a, inv b]]
        U = p[tables[:, inv[:, None], inv[None, :]]]
        code = U.reshape(B, n * n).astype(np.int64) @ weights
        best = code if best is None else np.minimum(best, code)
    return best


def decode(code, n):
    digits = []
    for _ in range(n * n):
        digits.append(code % n)
        code //= n
    return np.array(digits[::-1]).reshape(n, n)


def product(A, B):
    A = np.asarray(A)
    B = np.asarray(B)
    na, nb = len(A), len(B)
    i = np.arange(na * nb)
    return (A[(i // nb)[:, None], (i // nb)[None, :]] * nb + B[(i % nb)[:, None], (i % nb)[None, :]])
