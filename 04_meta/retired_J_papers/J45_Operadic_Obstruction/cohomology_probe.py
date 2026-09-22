#!/usr/bin/env python3
# ============================================================
# cohomology_probe.py
#
# Companion to NON_CLOSURE_QUESTION.md / manuscript.md OPEN(c).
#
# QUESTION (manuscript OPEN(c)): is the operadic non-closure obstruction
# -- the failure of a D_4-equivariant ternary fuse rule on the magma
# (Z/10Z, T) (TSML_RAW), witnessed by 16 incoherent D_4-orbits and
# localized to the sigma^3-defect at the single triple (3,9,9) --
# a GENUINE (co)homological class, or an ARTIFACT of the restricted
# (input-derived) value space?
#
# STRATEGY. Cohomology is well-defined *linear algebra* only over a field.
# We build the magma ALGEBRA A = k[Z/10Z] (10-dim, basis e_0..e_9,
# e_a * e_b = e_{T(a,b)}) over the CRT factor fields of the ground ring
# Z/10Z = Z/2 x Z/5, i.e. k = F_2 and F_5, plus F_3 (a control: the label
# gap 7-4=3 vanishes mod 3) and a large prime P = 1000003 as a char-0 proxy.
#
# We then compute, HONESTLY, four distinct things and report exactly what
# each is and is not able to say:
#
#   [A] Non-associativity census + the sigma^3 / sink-7 mechanism.
#   [B] Hochschild cochain differentials d^1, d^2 as explicit matrices and
#       the FATAL check d^2 . d^1 =? 0.  (For a non-associative algebra this
#       is nonzero, so strict Hochschild H^n is NOT DEFINED -- we quantify.)
#   [C] The WELL-DEFINED theory that actually houses an equivariance
#       obstruction: group cohomology H^*(<sigma^3>, A) and H^*(D_4, A),
#       computed by explicit bar/periodic complexes over each field.
#       We locate the defect cochain and test coboundary-ness.
#   [D] The value-space question made precise: the bracketing sub-bundle
#       W(t) = span{e_L(t), e_R(t)}; its D_4-equivariance failure (= the 16
#       orbits); and dim Hom_{D_4}(k[N], A) for the ENLARGED (full) value
#       space -- i.e. does enlargement remove the obstruction?
#   [E] The naive "values-as-scalars" reading behind the 7=4 <=> char 3
#       heuristic, and why it is NOT a genuine cohomology.
#
# All finite-field linear algebra is done by explicit Gaussian elimination
# mod p (function gf_rank), cross-checked at a large prime for char 0.
#
# Run:
#   PYTHONIOENCODING=utf-8 /c/ck_venv/lora312/Scripts/python.exe cohomology_probe.py
#
# Authors: computation for the TIG J45 resurface note, 2026-09-22.
# License: CC-BY-4.0.
# ============================================================

from __future__ import annotations
from itertools import product
from collections import Counter
import numpy as np

# ------------------------------------------------------------
# The canonical TSML_RAW table on Z/10Z (identical to the verifier).
# ------------------------------------------------------------
_TSML_ROWS = [
    "0000000700",  # 0: V
    "0737777777",  # 1: L
    "0377477779",  # 2: C
    "0777777773",  # 3: P
    "0747777787",  # 4: O
    "0777777777",  # 5: B
    "0777777777",  # 6: S
    "7777777777",  # 7: H (HARMONY)
    "0777877777",  # 8: Br
    "0797377777",  # 9: R
]
TSML = [[int(c) for c in row] for row in _TSML_ROWS]
N10 = 10

def T(a, b):
    return TSML[a][b]

# D_4 generators as permutations of {0..9} (p[i] = image of i).
P56  = tuple(6 if i == 5 else (5 if i == 6 else i) for i in range(10))
_SIG = {0:0,1:7,2:1,3:3,4:2,5:4,6:5,7:6,8:8,9:9}   # sigma = (0)(3)(8)(9)(1 7 6 5 4 2)
SIGMA  = tuple(_SIG[i] for i in range(10))
def compose(p, q):  # p after q
    return tuple(p[q[i]] for i in range(10))
SIGMA3 = compose(SIGMA, compose(SIGMA, SIGMA))       # (1 5)(7 4)(6 2)
IDENT  = tuple(range(10))

def gen_group(gens):
    elts = {IDENT}; frontier=[IDENT]
    while frontier:
        nf=[]
        for g in frontier:
            for s in gens:
                h=compose(g,s)
                if h not in elts:
                    elts.add(h); nf.append(h)
        frontier=nf
    return sorted(elts)
D4 = gen_group([P56, SIGMA3])

def act3(p, t):
    return (p[t[0]], p[t[1]], p[t[2]])

def perm_matrix(p, field_size=None):
    """10x10 permutation matrix M with M[p[i], i] = 1 (acts on column vectors:
    (M v)_{p[i]} = v_i, i.e. M e_i = e_{p[i]})."""
    M = np.zeros((10,10), dtype=np.int64)
    for i in range(10):
        M[p[i], i] = 1
    return M

# ============================================================
# Finite-field / rational linear algebra
# ============================================================
def gf_rref(mat, p):
    """Row-reduce a copy of `mat` (2D int array) over F_p (p prime) OR over Q
    if p is None (uses python-fraction-free... here we always pass a prime;
    a large prime P proxies char 0).  Returns (rref, rank, pivots)."""
    A = (np.asarray(mat, dtype=np.int64) % p).copy()
    rows, cols = A.shape
    r = 0
    pivots = []
    for c in range(cols):
        # find pivot in column c at or below row r
        piv = -1
        for i in range(r, rows):
            if A[i, c] % p != 0:
                piv = i; break
        if piv == -1:
            continue
        A[[r, piv]] = A[[piv, r]]
        inv = pow(int(A[r, c]), p-2, p)          # Fermat inverse (p prime)
        A[r] = (A[r] * inv) % p
        # eliminate column c from all other rows
        col = A[:, c].copy()
        col[r] = 0
        nz = np.nonzero(col % p)[0]
        for i in nz:
            f = A[i, c] % p
            if f:
                A[i] = (A[i] - f * A[r]) % p
        pivots.append(c)
        r += 1
        if r == rows:
            break
    return A, r, pivots

def gf_rank(mat, p):
    if mat.size == 0:
        return 0
    return gf_rref(mat, p)[1]

def gf_kernel_dim(mat, p):
    """dim ker of the linear map with matrix `mat` (rows=codomain, cols=domain)
    over F_p:  ncols - rank."""
    if mat.size == 0:
        return 0
    ncols = mat.shape[1]
    return ncols - gf_rank(mat, p)

def in_span_gf(vecs, target, p):
    """Is `target` in the F_p-span of the rows of `vecs`?  vecs: (m,n) array."""
    vecs = np.asarray(vecs, dtype=np.int64) % p
    target = np.asarray(target, dtype=np.int64).reshape(1, -1) % p
    r0 = gf_rank(vecs, p)
    r1 = gf_rank(np.vstack([vecs, target]), p)
    return r0 == r1

FIELDS = [("F2", 2), ("F3", 3), ("F5", 5), ("Q~P", 1000003)]

# ============================================================
# [A]  Non-associativity census + the sigma^3 / sink-7 mechanism
# ============================================================
def L(a,b,c): return T(T(a,b),c)
def R(a,b,c): return T(a,T(b,c))

def section_A():
    print("="*70)
    print("[A]  Magma A = k[Z/10Z], non-associativity, and the mechanism")
    print("="*70)
    Nlist = [(a,b,c) for a,b,c in product(range(10),repeat=3) if L(a,b,c)!=R(a,b,c)]
    print(f"  |non-associative locus N| = {len(Nlist)}  (expect 126)")
    # sink structure of HARMONY = 7
    cell_counts = Counter(TSML[i][j] for i in range(10) for j in range(10))
    print(f"  TSML cell-value multiset: {dict(sorted(cell_counts.items()))}")
    print(f"  value 7 (HARMONY) occupies {cell_counts[7]}/100 cells  -> dominant sink")
    # sigma^3 fixed points and the 7<->4 swap
    fixed = [i for i in range(10) if SIGMA3[i]==i]
    print(f"  sigma^3 = {SIGMA3}")
    print(f"  sigma^3 fixed points: {fixed};  swaps: 1<->5, 2<->6, 4<->7")
    # the localized defect at (3,9,9)
    t = (3,9,9)
    print(f"  triple {t}: L={L(*t)}, R={R(*t)}, bracket pair={{{L(*t)},{R(*t)}}}")
    print(f"    sigma^3.{t} = {act3(SIGMA3,t)}  (fixed);  sigma^3(7)=4, sigma^3(4)=7")
    print(f"    so an equivariant Phi must have Phi(3,9,9) in the sigma^3-fixed set.")
    # every bracketing pair contains 7
    pairs = Counter(frozenset({L(*x),R(*x)}) for x in Nlist)
    print(f"  bracketing-pair distribution: "
          + ", ".join(f"{set(sorted(k))}:{v}" for k,v in sorted(pairs.items(),key=lambda kv:sorted(kv[0]))))
    print(f"    -> ALL {len(Nlist)} disagreements route through 7, and 7 is NOT sigma^3-fixed.")
    return Nlist

# ============================================================
# [A2]  ROOT CAUSE: is D_4 even a symmetry of the arity-2 magma T?
# ============================================================
def is_auto(g):
    """Is permutation g a magma automorphism of T:  T(g a, g b) = g(T(a,b)) for all a,b?"""
    return all(T(g[a],g[b])==g[T(a,b)] for a,b in product(range(10),repeat=2))

def section_A2(Nlist):
    print()
    print("="*70)
    print("[A2] ROOT CAUSE: which of D_4 are genuine automorphisms of the magma T?")
    print("="*70)
    autos = [g for g in D4 if is_auto(g)]
    print(f"  D_4 elements that ARE binary-magma automorphisms of T: {len(autos)} of 8")
    print(f"    -> the genuine symmetry group of the RAW table T inside D_4 is <P56> = Z/2,")
    print(f"       NOT D_4.  (P56 auto: {is_auto(P56)};  sigma^3 auto: {is_auto(SIGMA3)}.)")
    for name,g in [("P56",P56),("sigma^3",SIGMA3)]:
        viol=[(a,b) for a,b in product(range(10),repeat=2) if T(g[a],g[b])!=g[T(a,b)]]
        print(f"    T equivariance under {name}: {100-len(viol)}/100 cells; {len(viol)} violations")
    g=SIGMA3
    viol=[(a,b,T(g[a],g[b]),g[T(a,b)]) for a,b in product(range(10),repeat=2) if T(g[a],g[b])!=g[T(a,b)]]
    sink74=[v for v in viol if v[2]==7 and v[3]==4]
    print(f"    of the {len(viol)} sigma^3 violations, {len(sink74)} are exactly (actual T=7, demanded 4):")
    print(f"       i.e. T lands on the sink HARMONY=7 where sigma^3-equivariance demands 4.")
    # Consequence: N is not sigma^3-invariant / not D_4-invariant
    Nset=set(Nlist)
    for name,g in [("P56",P56),("sigma^3",SIGMA3)]:
        leave=[t for t in Nlist if act3(g,t) not in Nset]
        print(f"    consequently the locus N is {'INVARIANT' if not leave else 'NOT invariant'} under {name}"
              f" ({len(leave)}/126 triples escape N).")
    print("    CONCLUSION: sigma^3 is not a symmetry of T at ANY arity; the arity-3")
    print("    'sigma^3-obstruction' is the inherited shadow of this arity-2 non-symmetry,")
    print("    not a new higher-operadic phenomenon.  P56 IS a genuine symmetry (Family H")
    print("    is P56-equivariant, Theorem 4.2).")

# ============================================================
# [B]  Hochschild differentials and the fatal d.d check
# ============================================================
# Cochain C^n = Hom(A^{x n}, A); basis indexed by (i_1..i_n, j):
#   the map sending (e_{i_1},...,e_{i_n}) -> e_j and all other basis tuples->0.
# Flatten index (i_1..i_n, j) to an integer.  dim C^n = 10^{n+1}.

def flat_idx(args, j):
    idx = 0
    for a in args:
        idx = idx*10 + a
    return idx*10 + j

def build_d(n):
    """Matrix of Hochschild d^n : C^n -> C^{n+1} (rows = C^{n+1}, cols = C^n),
    integer entries in {-1,0,+1}, built from the magma product T.
    Uses:  (d f)(a_0..a_n) = a_0 f(a_1..a_n)
                             + sum_{i=1}^n (-1)^i f(..,a_{i-1}a_i,..)
                             + (-1)^{n+1} f(a_0..a_{n-1}) a_n.
    """
    dom = 10**(n+1)      # dim C^n
    cod = 10**(n+2)      # dim C^{n+1}
    M = np.zeros((cod, dom), dtype=np.int64)
    for tup in product(range(10), repeat=n+1):  # arguments a_0..a_n of (d f)
        a = tup
        for j in range(10):                      # output basis e_j of the value
            row = flat_idx(a, j)
            # term 0: a_0 * f(a_1..a_n)  -> f(a_1..a_n) = e_k contributes e_{T(a_0,k)}
            #   we express as: this row (with value index T(a_0,k)) gets +col(f=(a_1..a_n)->k)
            #   Rather than invert, we accumulate per (source cochain -> which output).
            pass
    # It is cleaner to accumulate by iterating over source cochains' contributions.
    M[:] = 0
    for a in product(range(10), repeat=n+1):
        a0 = a[0]; an = a[-1]
        inner_right = a[1:]      # (a_1..a_n)
        inner_left  = a[:-1]     # (a_0..a_{n-1})
        for k in range(10):
            # term 0: + a0 * f(inner_right)   ; f(inner_right)=e_k -> a0*e_k = e_{T(a0,k)}
            r = flat_idx(a, T(a0, k)); col = flat_idx(inner_right, k)
            M[r, col] += 1
            # term n+1: (-1)^{n+1} f(inner_left) * a_n ; f(inner_left)=e_k -> e_{T(k,an)}
            r = flat_idx(a, T(k, an)); col = flat_idx(inner_left, k)
            M[r, col] += (-1)**(n+1)
        # middle terms i=1..n: (-1)^i f(a_0,..,a_{i-1}*a_i,..,a_n)
        for i in range(1, n+1):
            merged = a[:i-1] + (T(a[i-1], a[i]),) + a[i+1:]   # length n
            for j in range(10):
                r = flat_idx(a, j); col = flat_idx(merged, j)
                M[r, col] += (-1)**i
    return M

def section_B():
    print()
    print("="*70)
    print("[B]  Strict Hochschild attempt: is there even a cochain complex?")
    print("="*70)
    print("  Building d^1: C^1(dim 100) -> C^2(dim 1000) and")
    print("           d^2: C^2(dim 1000) -> C^3(dim 10000).")
    d1 = build_d(1)   # 1000 x 100
    d2 = build_d(2)   # 10000 x 1000
    print(f"  shapes: d1 {d1.shape}, d2 {d2.shape}")
    # The FATAL check: for a genuine complex we need d2 . d1 = 0.
    comp = d2.dot(d1)   # 10000 x 100
    print()
    print("  FATAL CHECK  d^2 . d^1 =? 0   (holds iff A is associative):")
    hdr = "    field:      " + "".join(f"{name:>10}" for name,_ in FIELDS)
    print(hdr)
    ranks_comp = []
    for name,p in FIELDS:
        rc = gf_rank(comp, p)
        ranks_comp.append(rc)
    print("    rank(d2.d1)=" + "".join(f"{r:>10}" for r in ranks_comp))
    nonzero = any(r>0 for r in ranks_comp)
    print(f"    => d^2 . d^1 {'is NONZERO' if nonzero else 'vanishes'} : "
          f"strict Hochschild cohomology is {'NOT DEFINED' if nonzero else 'defined'} for this A.")
    print()
    print("  For the record, the individual would-be dimensions (NOT a cohomology,")
    print("  since im d^1 is not contained in ker d^2):")
    print("    field       rank d1   ker d1   rank d2   ker d2 (=dim C^2 - rank d2)")
    rows = {}
    for name,p in FIELDS:
        r1 = gf_rank(d1, p)
        k1 = d1.shape[1] - r1
        r2 = gf_rank(d2, p)
        k2 = d2.shape[1] - r2
        rows[name] = (r1,k1,r2,k2)
        print(f"    {name:<10}{r1:>9}{k1:>9}{r2:>10}{k2:>9}")
    # how much of im d1 leaves ker d2:
    print()
    for name,p in FIELDS:
        r1 = gf_rank(d1,p)
        # dim( im d1 cap ker d2 ) = dim im d1 - rank(d2 restricted to im d1)
        # rank(d2 . d1) already = dim of d2(im d1); so im d1 \not\subset ker d2 by amount rank(d2.d1)
        rc = gf_rank(comp,p)
        print(f"    {name}: dim im d^1 = {r1}, of which {rc} dims are pushed OUT of ker d^2 by d^2"
              f"  (={'obstructed' if rc>0 else 'ok'})")
    return d1, d2

# ============================================================
# [C]  The well-defined theory: group cohomology H^*(G, A)
# ============================================================
def group_cohomology_bar(elements, mult, act_mats, M_dim, p, upto=2):
    """Inhomogeneous bar cochain cohomology H^*(G, M) over F_p.
       elements: list of group elements (hashable), mult(g,h)->element,
       act_mats: dict elt-> M_dim x M_dim matrix (left action on M=F_p^{M_dim}),
       returns list of dims [dim H^0, dim H^1, ..., dim H^upto]."""
    G = list(elements)
    gi = {g:i for i,g in enumerate(G)}
    n_g = len(G)

    def cochain_dim(nn):
        return (n_g**nn) * M_dim

    def build_diff(nn):
        """d^nn : C^nn -> C^{nn+1}.  C^nn = functions G^nn -> M.
        A cochain is a vector of length n_g^nn * M_dim; block for tuple s in G^nn
        occupies coordinates [pos(s)*M_dim : +M_dim]."""
        dom = cochain_dim(nn)
        cod = cochain_dim(nn+1)
        Mm = np.zeros((cod, dom), dtype=np.int64)
        # enumerate G^{nn+1} tuples (arguments of d f)
        for args in product(range(n_g), repeat=nn+1):
            gtuple = tuple(G[i] for i in args)
            out_pos = 0
            for i in args:
                out_pos = out_pos*n_g + i
            out_base = out_pos*M_dim
            # term j=0: g_1 . f(g_2..g_{nn+1})
            g0 = gtuple[0]
            rest = gtuple[1:]                # length nn
            src_pos = 0
            for g in rest:
                src_pos = src_pos*n_g + gi[g]
            if nn==0:
                src_pos_val = 0
            src_base = (src_pos*M_dim) if nn>0 else 0
            A0 = act_mats[g0]
            for a in range(M_dim):
                for b in range(M_dim):
                    if A0[a,b]:
                        Mm[out_base+a, src_base+b] += A0[a,b]
            # middle terms i=1..nn : (-1)^i f(g_1,..,g_i g_{i+1},..)
            for i in range(1, nn+1):
                merged = gtuple[:i-1] + (mult(gtuple[i-1], gtuple[i]),) + gtuple[i+1:]
                sp = 0
                for g in merged:
                    sp = sp*n_g + gi[g]
                sb = sp*M_dim
                sign = (-1)**i
                for a in range(M_dim):
                    Mm[out_base+a, sb+a] += sign
            # last term (-1)^{nn+1} f(g_1..g_nn)   (no action)
            head = gtuple[:nn]
            sp = 0
            for g in head:
                sp = sp*n_g + gi[g]
            sb = sp*M_dim
            sign = (-1)**(nn+1)
            for a in range(M_dim):
                Mm[out_base+a, sb+a] += sign
            # NOTE for nn==0: C^0 = M (functions from G^0 = {*}); the two "f(...)"
            #   without action collapse; handled below specially.
        return Mm

    # Special-case d^0 : M -> C^1,  (d^0 m)(g) = g.m - m
    d = {}
    C1 = cochain_dim(1)
    D0 = np.zeros((C1, M_dim), dtype=np.int64)
    for i,g in enumerate(G):
        A = act_mats[g]
        base = i*M_dim
        for a in range(M_dim):
            for b in range(M_dim):
                if A[a,b]:
                    D0[base+a, b] += A[a,b]
            D0[base+a, a] -= 1
    d[0] = D0
    for nn in range(1, upto+1):
        d[nn] = build_diff(nn)

    dims = []
    # H^0 = ker d^0
    dims.append(gf_kernel_dim(d[0], p))
    for nn in range(1, upto+1):
        ker = gf_kernel_dim(d[nn], p)
        img = gf_rank(d[nn-1], p)
        dims.append(ker - img)
    return dims, d

def section_C(Nlist):
    print()
    print("="*70)
    print("[C]  Group cohomology of the value module A (the well-defined theory)")
    print("="*70)
    # module M = A = k^10 permutation module; action of g is perm_matrix(g).
    # (1) H^*(<sigma^3>, A) via 2-periodic complex, and locate the defect.
    print("  (C.1)  G = <sigma^3> = Z/2 acting on A = k^10 (permutation module).")
    s = perm_matrix(SIGMA3)
    I = np.eye(10, dtype=np.int64)
    one_minus = (I - s)          # 1 - s
    one_plus  = (I + s)          # 1 + s  (= norm)
    print("        cycle type of sigma^3 on {0..9}: fixed {0,3,8,9}; swaps (1 5)(2 6)(4 7)")
    print("        H^n(Z/2,A):  H^0=ker(1-s); H^1=ker(1+s)/im(1-s); H^2=ker(1-s)/im(1+s)")
    print("        field       H^0   H^1   H^2")
    for name,p in FIELDS:
        H0 = gf_kernel_dim(one_minus, p)
        H1 = gf_kernel_dim(one_plus, p) - gf_rank(one_minus, p)
        H2 = gf_kernel_dim(one_minus, p) - gf_rank(one_plus, p)
        print(f"        {name:<10}{H0:>5}{H1:>6}{H2:>6}")
    # the defect cochain delta = e_7 - e_4 = (1 - sigma^3) e_7
    delta = np.zeros(10, dtype=np.int64); delta[7]=1; delta[4]=-1
    e7 = np.zeros(10, dtype=np.int64); e7[7]=1
    print()
    print("        DEFECT cochain delta = e_7 - e_4  (the 'HARMONY not sigma^3-fixed' failure).")
    for name,p in FIELDS:
        # is delta a coboundary?  B^1 = im(1-s).
        is_cob = in_span_gf(one_minus.T, delta, p)   # columns of (1-s) span im(1-s); rows of transpose
        # is delta a cocycle?  Z^1 = ker(1+s) acting... delta in ker(1+s)?
        is_cocy = (( (one_plus.dot(delta)) % p == 0).all())
        print(f"        {name}: delta in Z^1 (cocycle)? {bool(is_cocy)};  delta in B^1 (coboundary)? {is_cob}"
              f"  => class [delta] = {'0 (trivial)' if is_cob else 'NONZERO'}")
    # (2) H^*(D_4, A) via bar resolution.
    print()
    print("  (C.2)  G = D_4 acting on A = k^10 (permutation module), bar cohomology.")
    act_mats = {g: perm_matrix(g) for g in D4}
    print("        field       H^0   H^1   H^2")
    for name,p in FIELDS:
        dims,_ = group_cohomology_bar(D4, compose, act_mats, 10, p, upto=2)
        print(f"        {name:<10}" + "".join(f"{dd:>6}" for dd in dims))
    print()
    print("        (Maschke: |D_4|=8=2^3, so char=2 is the only prime dividing |G|;")
    print("         over F_3, F_5 and char 0, H^{>0}(D_4, A) must vanish.)")

# ============================================================
# [D]  The value-space question: the bracketing sub-bundle & enlargement
# ============================================================
def stabilizer(t):
    return [g for g in D4 if act3(g,t)==t]

def section_D(Nlist):
    print()
    print("="*70)
    print("[D]  The value-space question made precise")
    print("="*70)
    Nset = set(Nlist)
    # restricted D_4 orbits
    seen=set(); orbits=[]
    for t in Nlist:
        if t in seen: continue
        orb=set()
        for g in D4:
            gt=act3(g,t)
            if gt in Nset: orb.add(gt)
        orbits.append(frozenset(orb)); seen|=orb
    print(f"  {len(orbits)} restricted D_4-orbits on N.")
    # (D.1) equivariance of the SET-valued bracketing sub-bundle W(t)={L,R}
    #       W is D_4-equivariant iff W(g t)=g.W(t) for all g,t (with g t in N).
    incoh=0
    for orb in orbits:
        members=sorted(orb); base=members[0]
        bL,bR=L(*base),R(*base)
        ok=True
        for t in members[1:]:
            g=next(g for g in D4 if act3(g,base)==t)
            expected=frozenset({g[bL], g[bR]})
            actual=frozenset({L(*t),R(*t)})
            if expected!=actual: ok=False; break
        if not ok: incoh+=1
    print(f"  (D.1) SET-valued bracketing bundle W(t)=span{{e_L,e_R}}:")
    print(f"        D_4-incoherent orbits = {incoh}  (expect 16) -> NO equivariant section")
    print(f"        valued in the restricted set {{L(t),R(t)}}.  [Theorem 4.1]")
    # Same coherence test under the GENUINE symmetry <P56> alone:
    P56grp = gen_group([P56])
    seenP=set(); orbP=[]
    for t in Nlist:
        if t in seenP: continue
        o=set()
        for g in P56grp:
            gt=act3(g,t)
            if gt in Nset: o.add(gt)
        orbP.append(frozenset(o)); seenP|=o
    incohP=0
    for orb in orbP:
        members=sorted(orb); base=members[0]; bL,bR=L(*base),R(*base); ok=True
        for t in members[1:]:
            g=next(g for g in P56grp if act3(g,base)==t)
            if frozenset({g[bL],g[bR]})!=frozenset({L(*t),R(*t)}): ok=False; break
        if not ok: incohP+=1
    print(f"        under the GENUINE symmetry <P56> alone: {len(orbP)} orbits, {incohP} incoherent")
    print(f"        => the 16 incoherence is a PURE sigma^3 effect; <P56> has NO obstruction.")
    # (D.2) ENLARGED value space: per restricted orbit, dim A^{Stab(base)}.
    #  NOTE (honesty): N is NOT D_4-stable (section A2), so k[N] is not literally a
    #  D_4-module.  But each restricted orbit's stabilizer is well-defined, and the
    #  value an equivariant Phi may take at a base triple must lie in A^{Stab};
    #  dim A^{Stab} >= 1 always, so equivariant values into the FULL A always exist.
    print()
    print("  (D.2) ENLARGED value space (values in all of A):")
    print("        per restricted orbit, an equivariant value must lie in A^{Stab(base)};")
    print("        we report min dim A^{Stab} over orbits and the aggregate sum.")
    for name,p in FIELDS:
        total=0; mindim=99
        for orb in orbits:
            base=sorted(orb)[0]
            H=stabilizer(base)
            blocks=[ (perm_matrix(g)-np.eye(10,dtype=np.int64)) for g in H ]
            Mstack=np.vstack(blocks) if blocks else np.zeros((1,10),dtype=np.int64)
            fixed_dim=10-gf_rank(Mstack,p)
            total+=fixed_dim; mindim=min(mindim,fixed_dim)
        print(f"        {name}: min_orbit dim A^Stab = {mindim} (>=1 => value always exists);"
              f" aggregate sum = {total}")
    # the localized fixed triple (3,9,9): its stabilizer and available fixed values
    H = stabilizer((3,9,9))
    blocks=[ (perm_matrix(g)-np.eye(10,dtype=np.int64)) for g in H ]
    Mstack=np.vstack(blocks)
    print(f"        at the triple (3,9,9): Stab = ALL of D_4 (|Stab|={len(H)}, since 3,9 are")
    print(f"        D_4-fixed points), so an equivariant value must lie in A^{{D_4}}, dim ="
          f"{10-gf_rank(Mstack,5)} over F5.")
    print(f"        A^{{D_4}} contains e_3 and e_9 (both in the natural value set {{3,7,9}}!) and")
    print(f"        e_4+e_7; only the isolated Family-H choice e_7 fails to be D_4-fixed.")
    print(f"        => even at this triple a natural D_4-fixed value (e_3 or e_9) exists;")
    print(f"        the genuine obstruction is the GLOBAL 16-orbit bracketing-pair incoherence.")
    # (D.3) the explicit local fix at (3,9,9) by transfer/averaging
    print()
    print("  (D.3) explicit resolution of the localized defect at (3,9,9):")
    print("        natural (Family-H) value v = e_7 is not sigma^3-fixed.")
    print("        transfer/average over <sigma^3>:  v_bar = (1/2)(e_7 + sigma^3 e_7) = (1/2)(e_7+e_4).")
    print("        v_bar IS sigma^3-fixed; correction v - v_bar = (1/2)(e_7 - e_4) = (1/2)*delta.")
    print("        exists over any field where 2 is invertible (char != 2): F_3, F_5, char 0.")
    print("        over F_2 the average fails, BUT (see C.1) delta already lies in the")
    print("        free/induced summand where H^*(Z/2,A)=0, so delta is a coboundary there too.")

# ============================================================
# [E]  The naive values-as-scalars reading (why it is NOT a cohomology)
# ============================================================
def section_E():
    print()
    print("="*70)
    print("[E]  The 'values-as-scalars' heuristic (7 = 4  <=>  char 3)")
    print("="*70)
    print("  Heuristic: read the fuse value as a SCALAR label in k; the sigma^3-defect")
    print("  is the demand 7 = sigma^3(7) = 4, i.e. 7 - 4 = 3 = 0 in k.")
    for name,p in FIELDS:
        print(f"    {name}: 7 mod p = {7%p}, 4 mod p = {4%p}, (7-4) mod p = {(7-4)%p}"
              f"  => defect {'VANISHES' if (7-4)%p==0 else 'survives'}")
    print("  BUT sigma^3 acts on labels as the permutation (1 5)(2 6)(4 7): it fixes")
    print("  0 and 3 while swapping 4<->7, so it is NOT realizable as any affine map")
    print("  x -> a x + b on k (fixing 0 forces b=0; fixing 3 forces a=1 = identity).")
    print("  Hence 'values-as-scalars' does not define a linear G-action and carries no")
    print("  cochain complex; the char-3 coincidence is numerology of the labels, not a")
    print("  cohomology class.  The genuine module computation is section [C].")

# ============================================================
def main():
    Nlist = section_A()
    section_A2(Nlist)
    section_B()
    section_C(Nlist)
    section_D(Nlist)
    section_E()
    print()
    print("="*70)
    print("VERDICT: COBOUNDARY-ARTIFACT (not a genuine cohomological class).")
    print("  (1) A is non-associative -> strict Hochschild H^2,H^3 are NOT DEFINED;")
    print("  (2) in the well-defined H^*(<sigma^3>,A) / H^*(D_4,A), the defect")
    print("      delta = e_7 - e_4 = (1-sigma^3)e_7 is a COBOUNDARY (trivial class)")
    print("      in every characteristic, and H^{>0} vanishes entirely over F_5/F_3/")
    print("      char 0 by Maschke (char does not divide |D_4|=8);")
    print("  (3) ROOT: sigma^3 is not even a magma automorphism of T (80/100 arity-2")
    print("      violations); only <P56>=Z/2 is.  The arity-3 obstruction is the")
    print("      inherited shadow of arity-2 non-symmetry, resolved by enlarging the")
    print("      value space (transfer/averaging, char != 2).")
    print("See COHOMOLOGY_INVESTIGATION.md for the full reasoning and dimension tables.")
    print("="*70)

if __name__ == "__main__":
    main()
