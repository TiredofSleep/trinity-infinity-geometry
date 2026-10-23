#!/usr/bin/env python3
"""
binary_magic.py -- every magic arrangement built from binary corners.
  Level 3: the cube's 8 corners (0..7 = 3 bits).
  Level 4: the tesseract's 16 corners (0..15 = 4 bits) = all 4x4 magic squares.
Run: python3 binary_magic.py   (writes squares_4x4.json; asserts the known counts)
"""
import itertools, json, os
from collections import Counter

# ---------------- level 3: the cube ----------------
def cube_level():
    print("=" * 66); print("LEVEL 3: the cube's corners 0..7 (3 bits)"); print("=" * 66)
    # (a) a 2x2x2 magic cube: every axis line of 2 corners sums to 7 -> impossible
    ok = []
    for perm in itertools.permutations(range(8)):
        g = {(x, y, z): perm[4*x + 2*y + z] for x in (0, 1) for y in (0, 1) for z in (0, 1)}
        if all(g[(0,y,z)] + g[(1,y,z)] == 7 for y in (0,1) for z in (0,1)) and \
           all(g[(x,0,z)] + g[(x,1,z)] == 7 for x in (0,1) for z in (0,1)) and \
           all(g[(x,y,0)] + g[(x,y,1)] == 7 for x in (0,1) for y in (0,1)):
            ok.append(perm)
    print(f"2x2x2 magic cubes on 0..7: {len(ok)}  (a corner's 3 neighbours would all have to be 7-n)")
    assert not ok
    # (b) 2x4 magic rectangles: rows sum 14, columns sum 7
    rects = set()
    for perm in itertools.permutations(range(8)):
        top, bot = perm[:4], perm[4:]
        if sum(top) == 14 and all(a + b == 7 for a, b in zip(top, bot)):
            rects.add((frozenset(top), frozenset(bot)))
    rows = {frozenset(r) for pair in rects for r in pair}
    print(f"2x4 magic rectangles: row-sets that work = {sorted(sorted(r) for r in rows)}")
    parity = lambda n: bin(n).count("1") % 2
    for r in rows:
        assert len({parity(n) for n in r}) == 1
    print("  -> the only possible rows are the two tetrahedra (even vs odd number of 1-bits);")
    print("     the columns are forced to be the 4 long diagonals (n, 7-n). Unique up to order.")
    assert rows == {frozenset({0, 3, 5, 6}), frozenset({1, 2, 4, 7})}

# ---------------- level 4: the tesseract ----------------
N, S = 16, 30
def all_squares():
    quads = [frozenset(c) for c in itertools.combinations(range(N), 4) if sum(c) == S]
    partitions = set()
    def part(rem, chosen):
        if not rem:
            partitions.add(frozenset(chosen)); return
        m = min(rem)
        for q in quads:
            if m in q and q <= rem:
                part(rem - q, chosen + [q])
    part(frozenset(range(N)), [])
    squares = set()
    for P in partitions:
        rows = list(P)
        trans = [frozenset(t) for t in itertools.product(*rows) if sum(t) == S]
        colparts = set()
        def cpart(rem, chosen):
            if not rem:
                colparts.add(frozenset(chosen)); return
            m = min(rem)
            for t in trans:
                if m in t and t <= rem:
                    cpart(rem - t, chosen + [t])
        cpart(frozenset(range(N)), [])
        for C in colparts:
            cols = list(C)
            for ro in itertools.permutations(rows):
                for co in itertools.permutations(cols):
                    M = tuple(tuple(next(iter(r & c)) for c in co) for r in ro)
                    if sum(M[i][i] for i in range(4)) == S and sum(M[i][3-i] for i in range(4)) == S:
                        squares.add(M)
    return squares

def canon(M):
    forms, A = [], M
    for _ in range(4):
        A = tuple(zip(*A[::-1])); forms += [A, tuple(r[::-1] for r in A)]
    return min(forms)

def features(M):
    lines = [list(r) for r in M] + [list(c) for c in zip(*M)] + \
            [[M[i][i] for i in range(4)], [M[i][3-i] for i in range(4)]]
    broken = [[M[i][(i+k) % 4] for i in range(4)] for k in range(4)] + \
             [[M[i][(k-i) % 4] for i in range(4)] for k in range(4)]
    bits_balanced = [all(sum((v >> b) & 1 for v in L) == 2 for L in lines) for b in range(4)]
    return {
        "pandiagonal": all(sum(L) == S for L in broken),
        "associative": all(M[i][j] + M[3-i][3-j] == 15 for i in range(4) for j in range(4)),
        "planes_balanced": sum(bits_balanced),
    }

if __name__ == "__main__":
    cube_level()
    print("\n" + "=" * 66); print("LEVEL 4: the tesseract's corners 0..15 (4 bits) = every 4x4 magic square"); print("=" * 66)
    sq = all_squares()
    essentially = {canon(M) for M in sq}
    print(f"all 4x4 magic squares on 0..15: {len(sq)}; essentially different (up to rotation/reflection): {len(essentially)}")
    assert len(sq) == 7040 and len(essentially) == 880          # Frenicle (1693)
    data = [{"square": [list(r) for r in M], **features(M)} for M in sorted(essentially)]
    pan = sum(d["pandiagonal"] for d in data); asc = sum(d["associative"] for d in data)
    print(f"  pandiagonal (every wrapped diagonal also sums to 30): {pan}")
    assert pan == 48
    print(f"  associative (opposite cells are long diagonals n, 15-n): {asc}")
    hist = Counter(d["planes_balanced"] for d in data)
    print("  bit planes that are themselves balanced (2 ones per line), out of 4:")
    for k in sorted(hist):
        print(f"     {k} of 4 planes balanced: {hist[k]} squares")
    full = [d for d in data if d["planes_balanced"] == 4]
    print(f"  -> {len(full)} squares are built purely from binary: each bit plane is a balanced 0/1 pattern,")
    print("     so the square is magic because every binary layer is. Durer-style decomposition.")
    assert 3 not in hist   # 3 balanced planes force the 4th: 30 = 2*(1+2+4+8)
    print("  no square has exactly 3: if three bit layers balance, the line sum 30 = 2*(1+2+4+8) forces the 4th")
    pan_full = sum(d["pandiagonal"] and d["planes_balanced"] == 4 for d in data)
    asc_full = sum(d["associative"] and d["planes_balanced"] == 4 for d in data)
    overlap = sum(d["pandiagonal"] and d["associative"] for d in data)
    print(f"  all {pan_full} pandiagonal and all {asc_full} associative squares are fully binary; the two families never overlap ({overlap})")
    assert pan_full == 48 and asc_full == 48 and overlap == 0
    durer = [[v - 1 for v in r] for r in [[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]]
    dc = [list(r) for r in canon(tuple(map(tuple, durer)))]
    dd = next(d for d in data if d["square"] == dc)
    print(f"  Durer's 1514 square (minus 1): associative={dd['associative']}, binary layers balanced={dd['planes_balanced']}/4")
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "squares_4x4.json")
    json.dump(data, open(out, "w", newline=""), indent=0)
    print(f"\nwrote all {len(data)} squares with features to {out}")
