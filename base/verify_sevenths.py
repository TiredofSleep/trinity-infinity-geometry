"""verify_sevenths.py -- checks every [FORCED] line of SEVENTHS.md ("The sevenths").

numpy only.  ASCII output.  Exit code 1 on any failure.
Run:  python verify_sevenths.py           (about half a minute)
      python verify_sevenths.py --long    (also re-derives the decimal edge primes up to 40000: a minute more)
"""
import cmath
import math
import sys
from fractions import Fraction as Fr
from itertools import permutations, product

import numpy as np

FAILED = []
LONG = "--long" in sys.argv


def check(label, ok):
    print(("PASS  " if ok else "FAIL  ") + label)
    if not ok:
        FAILED.append(label)


# ------------------------------------------------------------------ tools
def primes(n):
    s = bytearray([1]) * (n + 1)
    s[:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


def order(b, p):
    x, k = b % p, 1
    while x != 1:
        x, k = x * b % p, k + 1
    return k


def full(b, p):
    """1/p has the full period p - 1 in base b"""
    return b % p != 0 and order(b, p) == p - 1


def digits(k, p, b=10):
    out, r = [], k % p
    for _ in range(order(b, p)):
        r *= b
        out.append(r // p)
        r %= p
    return out


def square(p, b=10):
    return np.array([digits(k, p, b) for k in range(1, p)])


def diagonal(p, b=10):
    """sum of the main diagonal (digit k of k/p) without building the square"""
    x, d = 1, 0
    for k in range(1, p):
        d += (b * (k * x % p)) // p
        x = x * b % p
    return d


def edge_primes(b, limit):
    """full-period primes whose square is fully magic (the diagonal equals the rows)"""
    return [p for p in primes(limit) if p > 2 and full(b, p) and 2 * diagonal(p, b) == (b - 1) * (p - 1)]


def class_number(D):
    """number of reduced forms of discriminant D < 0"""
    h, a = 0, 1
    while 3 * a * a <= -D:
        for bb in range(-a + 1, a + 1):
            if (bb * bb - D) % (4 * a) == 0:
                c = (bb * bb - D) // (4 * a)
                if c >= a and not (bb < 0 and a == c):
                    h += 1
        a += 1
    return h


def modes(p, b):
    """the wheel's Fourier modes, directly and by the character formula (b - w^-m) B_1,chi"""
    a = digits(1, p, b)
    n = p - 1
    w = cmath.exp(2j * math.pi / n)
    direct = [sum(a[j] * w ** (j * m) for j in range(n)) for m in range(n)]
    log = {}
    x = 1
    for j in range(n):
        log[x] = j
        x = x * b % p
    formula = [(b - w ** (-m)) * sum(x * w ** (log[x] * m) for x in range(1, p)) / p for m in range(n)]
    return direct, formula


# ------------------------------------------------------------------ 1. the wheel
W = digits(1, 7)
check("1/7 = 0.142857...: a repeating block of 6 digits, the most a seventh can have (10 is a primitive root mod 7)",
      W == [1, 4, 2, 8, 5, 7] and order(10, 7) == 6)
turn = {k: next(r for r in range(6) if pow(10, r, 7) == k) for k in range(1, 7)}
check("every seventh is the wheel turned: k/7 is 142857 started r places on, where 10^r leaves remainder k "
      "(the wheel runs 1 -> 3 -> 2 -> 6 -> 4 -> 5)",
      all(digits(k, 7) == W[turn[k]:] + W[:turn[k]] for k in range(1, 7))
      and [pow(10, r, 7) for r in range(6)] == [1, 3, 2, 6, 4, 5])
check("half a turn (3 places) sends k/7 to (7 - k)/7 and every digit d to 9 - d; 142 + 857 = 999",
      all((turn[k] + 3) % 6 == turn[7 - k] for k in range(1, 7))
      and all(digits(7 - k, 7)[j] == 9 - digits(k, 7)[j] for k in range(1, 7) for j in range(6)) and 142 + 857 == 999)
check("measured from 4.5, half a turn is negation: the wheel's second half is minus its first",
      all(W[j + 3] - 4.5 == -(W[j] - 4.5) for j in range(3)))

# ------------------------------------------------------------------ 2. the square
M = square(7)
check("the sevenths square: every row and every column adds to 27; the diagonals add to 31 and 23",
      (M.sum(0) == 27).all() and (M.sum(1) == 27).all() and np.trace(M) == 31 and np.trace(M[:, ::-1]) == 23)
ok_all = True
for p in primes(400):
    if p > 2 and full(10, p):
        A = square(p)
        s = 9 * (p - 1) // 2
        ok_all &= bool((A.sum(0) == s).all() and (A.sum(1) == s).all()
                       and np.trace(A) + np.trace(A[:, ::-1]) == 2 * s
                       and all(A[p - 1 - k - 1, k] == 9 - A[k, k] for k in range(p - 1)))
check("for every prime below 400 with a full decimal period: rows and columns all agree, and each diagonal is the "
      "other's flip, entry by entry (so the diagonals always average the row sum)", ok_all)
edge = edge_primes(10, 5000)
check(f"the primes whose square stands on the edge (fully magic), below 5000: {edge}", edge == [19, 383])
A19 = square(19)
check("the 19 square: every row, column and both diagonals add to 81",
      (A19.sum(0) == 81).all() and (A19.sum(1) == 81).all() and np.trace(A19) == 81 and np.trace(A19[:, ::-1]) == 81)
if LONG:
    e40 = edge_primes(10, 40000)
    check(f"[--long] below 40000: {e40} (OEIS A072359 begins 19, 383, 32327, 34061)", e40 == [19, 383, 32327, 34061])

# ------------------------------------------------------------------ 3. what the half turn pays for
check("rank 4: the columns weighted 0, 1, -1, 0, 1, -1, or 2, -1, -1, 2, -1, -1, add to nothing",
      np.linalg.matrix_rank(M) == 4 and not (M @ np.array([0, 1, -1, 0, 1, -1])).any()
      and not (M @ np.array([2, -1, -1, 2, -1, -1])).any())
check("measured from the centre (every digit minus 4.5), rank 3: exactly half", np.linalg.matrix_rank(M - 4.5) == 3)
d7, f7 = modes(7, 10)
target = [27, complex(-5, -3 * 3 ** 0.5), 0, -11, 0, complex(-5, 3 * 3 ** 0.5)]     # mode m = sum a_j w^(jm)
check("the wheel's six modes are 27, -5 - 3 sqrt3 i, 0, -11, 0, -5 + 3 sqrt3 i",
      all(abs(x - y) < 1e-9 for x, y in zip(d7, target)))
ok_g = True
for p in primes(400):
    if p % 4 == 3 and p > 3 and full(10, p):
        alt = sum((-1) ** j * d for j, d in enumerate(digits(1, p)))
        ok_g &= alt == -11 * class_number(-p)
check("the half-turn mode is the alternating digit sum: -11 = -11 x h(-7); and -11 h(-p) for every p = 3 mod 4 "
      "below 400 with a full decimal period (Girstmair)", ok_g and sum((-1) ** j * d for j, d in enumerate(W)) == -11)
ok_f = True
for p, b in ((7, 10), (17, 10), (19, 10), (23, 10), (29, 10), (5, 7), (11, 7), (13, 7), (11, 2), (17, 3)):
    d, f = modes(p, b)
    sc = max(abs(x) for x in d)
    ok_f &= all(abs(x - y) < 1e-9 * sc for x, y in zip(d, f))
    ok_f &= all(abs(d[m]) < 1e-9 * sc for m in range(2, p - 1, 2))          # even characters: zero
    ok_f &= all(abs(d[m]) > 1e-6 * sc for m in range(1, p - 1, 2))          # odd characters: never zero
check("mode m equals (b - w^-m) B_1,chi exactly as computed, the even modes vanish and the odd ones do not "
      "(ten primes in bases 2, 3, 7 and 10)", ok_f)
ok_r = True
cases = 0
for b, limit in ((10, 200), (7, 150), (3, 150), (2, 150)):
    for p in primes(limit):
        if p > 2 and full(b, p):
            A = square(p, b)
            ok_r &= bool(np.linalg.matrix_rank(A) == (p + 1) // 2
                         and np.linalg.matrix_rank(A - (b - 1) / 2) == (p - 1) // 2)
            cases += 1
check(f"rank (p + 1)/2, and (p - 1)/2 measured from the centre, for every full-period square checked ({cases} squares "
      "in bases 10, 7, 3 and 2)", ok_r)

# ------------------------------------------------------------------ 4. the wheel on the octahedron
n = np.ones(3) / math.sqrt(3)
K = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
R60 = np.eye(3) + math.sin(math.pi / 3) * K + (1 - math.cos(math.pi / 3)) * K @ K
S6 = (np.eye(3) - 2 * np.outer(n, n)) @ R60
O = np.vstack([np.eye(3), -np.eye(3)])
step = [int(np.argmin(np.linalg.norm(O - S6 @ x, axis=1))) for x in O]
cyc = [0]
while step[cyc[-1]] != 0:
    cyc.append(step[cyc[-1]])
label = {c: pow(10, r, 7) for r, c in enumerate(cyc)}
opp = sorted({tuple(sorted((label[i], label[j]))) for i in range(6) for j in range(6) if np.allclose(O[i], -O[j])})
faces = sorted({tuple(sorted(label[x] for x in (s, step[step[s]], step[step[step[step[s]]]]))) for s in range(6)})
check("a sixth of a turn and a mirror (S6) visits the octahedron's six corners in one cycle, and three of them are the "
      "inversion through the centre", len(cyc) == 6 and np.allclose(np.linalg.matrix_power(S6, 3), -np.eye(3)))
check("labelled round the wheel, opposite corners carry 1 and 6, 2 and 5, 3 and 4 (pairs adding to 7)",
      opp == [(1, 6), (2, 5), (3, 4)])
check("two steps go round a face: the corners split into the squares mod 7, {1, 2, 4}, and {3, 5, 6}",
      faces == [(1, 2, 4), (3, 5, 6)] and sorted({x * x % 7 for x in range(1, 7)}) == [1, 2, 4])

# ------------------------------------------------------------------ 5. how unique is counting in sevenths?
check("7 has a full wheel in base b exactly when b leaves remainder 3 or 5 mod 7 (b = 2..60); in base 7, 1/7 = 0.1",
      all(full(b, 7) == (b % 7 in (3, 5)) for b in range(2, 61)) and Fr(1, 7) * 7 == 1)
check("in base 10, 7 is the smallest prime with a full wheel", [p for p in primes(7) if full(10, p)] == [7])
ok_ds = True
for p in primes(200):
    if p % 4 == 3:
        Q = {x * x % p for x in range(1, p)}
        count = {d: 0 for d in range(1, p)}
        for x in Q:
            for y in Q:
                if x != y:
                    count[(x - y) % p] += 1
        ok_ds &= set(count.values()) == {(p - 3) // 4}
check("for every prime p = 3 mod 4 below 200, the squares mod p repeat every nonzero difference (p - 3)/4 times: "
      "once only at p = 7", ok_ds)
LINES = [frozenset({(1 + k) % 7, (2 + k) % 7, (4 + k) % 7}) for k in range(7)]
check("the Fano plane: the 7 translates of {1, 2, 4} mod 7 are lines with every pair of points on exactly one",
      all(sum(1 for L in LINES if {a, c} <= L) == 1 for a in range(7) for c in range(a + 1, 7)))

T = np.zeros((8, 8, 8))                              # index 0 is 1; index i + 1 is e_i
for a in range(8):
    T[0, a, a] = T[a, 0, a] = 1
for i in range(7):
    T[i + 1, i + 1, 0] = -1
for i in range(7):
    a, c, e = i, (i + 1) % 7, (i + 3) % 7
    for x, y, z in ((a, c, e), (c, e, a), (e, a, c)):
        T[x + 1, y + 1, z + 1] = 1
        T[y + 1, x + 1, z + 1] = -1


def mul(x, y):
    return np.einsum("a,b,abc->c", x, y, T)


rng = np.random.default_rng(7)
X, Y, Z = rng.normal(size=(3, 1000, 8))
norms = all(abs(np.linalg.norm(mul(x, y)) - np.linalg.norm(x) * np.linalg.norm(y)) < 1e-9 for x, y in zip(X, Y))
alt = all(np.allclose(mul(x, mul(x, y)), mul(mul(x, x), y)) for x, y in zip(X[:200], Y[:200]))
nonassoc = any(not np.allclose(mul(mul(x, y), z), mul(x, mul(y, z))) for x, y, z in zip(X[:20], Y[:20], Z[:20]))
cross = True
for a_, b_ in zip(X[:300], Y[:300]):
    a_[0] = b_[0] = 0
    c_ = mul(a_, b_)
    c_[0] = 0
    cross &= abs(c_ @ c_ - ((a_ @ a_) * (b_ @ b_) - (a_ @ b_) ** 2)) < 1e-9 and abs(c_ @ a_) < 1e-9
check("the rule e_i e_(i+1) = e_(i+3) (indices mod 7, the Fano lines) multiplies the octonions: norms multiply, it "
      "is alternative and not associative, and Im(ab) is a cross product in 7 dimensions",
      norms and alt and nonassoc and cross)


def times_alpha(x):                                  # multiply by alpha in F8 = F2[alpha]/(alpha^3 + alpha + 1)
    x <<= 1
    return x ^ 0b1011 if x & 0b1000 else x


pw = [1]
for _ in range(6):
    pw.append(times_alpha(pw[-1]))
check("the same plane on the cube's corners: the powers of alpha in F8 run through the seven nonzero 3-bit strings, "
      "and alpha^i XOR alpha^(i+1) = alpha^(i+3) for every i",
      sorted(pw) == list(range(1, 8)) and all(pw[i] ^ pw[(i + 1) % 7] == pw[(i + 3) % 7] for i in range(7)))
sym = sum(1 for s in permutations(range(7)) if all(frozenset(s[x] for x in L) in LINES for L in LINES))
inv = sum(1 for m in product((0, 1), repeat=9)
          if round(np.linalg.det(np.array(m).reshape(3, 3))) % 2 == 1)
check(f"the Fano plane has {sym} symmetries among the 5040 orders of its points, the number of invertible 3 x 3 "
      "matrices over F2", sym == inv == 168)
best = max((Fr(1, p) + Fr(1, q) + Fr(1, r), (p, q, r)) for p in range(2, 61) for q in range(p, 61)
           for r in range(q, 61) if Fr(1, p) + Fr(1, q) + Fr(1, r) < 1)
check("among 1/p + 1/q + 1/r below 1 (p, q, r from 2 to 60) the largest is 1/2 + 1/3 + 1/7 = 41/42; so Hurwitz's "
      "bound is 84(g - 1), which is 168 at genus 3", best == (Fr(41, 42), (2, 3, 7)) and 2 * 42 * (3 - 1) == 168)


def constructible(n):                                # Gauss-Wantzel
    while n % 2 == 0:
        n //= 2
    for f in (3, 5, 17, 257, 65537):
        if n % f == 0:
            n //= f
    return n == 1


cub = [abs(x ** 3 + x ** 2 - 2 * x - 1) for x in (2 * math.cos(2 * math.pi * k / 7) for k in (1, 2, 3))]
check("the heptagon is the first regular polygon straightedge and compass cannot draw; 2cos(2 pi/7) solves "
      "x^3 + x^2 - 2x - 1 = 0, which has no rational root and three real ones (discriminant 49)",
      [n for n in range(3, 8) if not constructible(n)] == [7] and max(cub) < 1e-12
      and all(x ** 3 + x ** 2 - 2 * x - 1 != 0 for x in (1, -1)) and 4 + 32 + 4 - 27 + 36 == 49)
sqfree = [d for d in range(1, 201) if all(d % (q * q) for q in range(2, 15))]
one = [d for d in sqfree if class_number(-d if d % 4 == 3 else -4 * d) == 1]
check(f"class number 1 below 200: Q(sqrt -d) for d = {one}", one == [1, 2, 3, 7, 11, 19, 43, 67, 163])

# base 10, viewed in sevenths: every number by its numerator
def tail(n, places=12):
    r, out = n % 7, []
    for _ in range(places):
        r *= 10
        out.append(r // 7)
        r %= 7
    return out


check("the view: n/7 is (n div 7) followed by the wheel turned by the turns of n's remainder, or by nothing when 7 "
      "divides n (every n up to 20000); 10/7 = 1.428571..., 100/7 = 14.285714..., 2026/7 = 289.428571...",
      all(tail(n) == ([0] * 12 if n % 7 == 0 else (W[turn[n % 7]:] + W[:turn[n % 7]]) * 2) for n in range(1, 20001))
      and (10 // 7, tail(10, 6)) == (1, [4, 2, 8, 5, 7, 1]) and (2026 // 7, tail(2026, 6)) == (289, [4, 2, 8, 5, 7, 1]))
check("multiplication becomes rotation: the turns of a product are the sum of the turns, mod 6",
      all(turn[a * c % 7] == (turn[a] + turn[c]) % 6 for a in range(1, 7) for c in range(1, 7)))
check("Fermat: six turns are the whole wheel, so k^6 leaves 1; Euler: k^3 leaves 1 for an even number of turns "
      "(the squares 1, 2, 4) and -1 for an odd number",
      all(pow(k, 6, 7) == 1 and pow(k, 3, 7) == (1 if turn[k] % 2 == 0 else 6) for k in range(1, 7)))
check("Wilson: 6! leaves -1, because its turns add to 0 + 1 + 2 + 3 + 4 + 5 = 15, which is half a turn",
      math.factorial(6) % 7 == 6 and sum(turn.values()) % 6 == 3)
check("orders: 3 and 5 turn the whole wheel, 2 and 4 a third of it, 6 half of it",
      {k: 6 // math.gcd(turn[k], 6) for k in range(1, 7)} == {1: 1, 2: 3, 3: 6, 4: 3, 5: 6, 6: 2})


def alt_blocks(m):
    s, sign = 0, 1
    while m:
        s, m, sign = s + sign * (m % 1000), m // 1000, -sign
    return s


check("the base is a turn: x10 is one turn, x100 two, and 1000 leaves -1, half the wheel; so 7 divides n exactly when "
      "it divides the alternating sum of n's three-digit blocks (every n below 200000), and 1001 = 7 x 11 x 13",
      [pow(10, r, 7) for r in (1, 2, 3)] == [3, 2, 6] and 7 * 11 * 13 == 1001
      and all((m % 7 == 0) == (alt_blocks(m) % 7 == 0) for m in range(1, 200001)))
fw = [p for p in primes(200) if p > 5 and full(10, p)]
check(f"among base 10's full wheels below 200 ({len(fw)} primes), only 7's half turn is a thousand",
      [p for p in fw if pow(10, 3, p) == p - 1 and (p - 1) // 2 == 3] == [7] and fw[0] == 7)
sieve = np.ones(10 ** 7 + 1, bool)
sieve[:2] = False
for i in range(2, int(10 ** 3.5) + 1):
    if sieve[i]:
        sieve[i * i::i] = False
PR = np.nonzero(sieve)[0]
RES = PR % 7
shares = [int((RES == k).sum()) for k in range(1, 7)]
lead = np.cumsum(np.isin(RES, [3, 5, 6]).astype(int)) - np.cumsum(np.isin(RES, [1, 2, 4]).astype(int))
at = lead[np.searchsorted(PR, np.arange(1000, 10 ** 7 + 1, 1000), side="right") - 1]
check(f"primes on the wheel: below ten million the six turns hold {min(shares)} to {max(shares)} primes each, and "
      "the odd turns (3, 5, 6) lead the even ones (1, 2, 4) at every checkpoint, every thousand",
      max(shares) - min(shares) < 0.002 * max(shares) and (at > 0).all())
PI = Fr("3.14159265358979323846264338327950288419716939937510582097494459")
xx, cf = PI, []
for _ in range(5):
    a0 = xx.numerator // xx.denominator
    cf.append(a0)
    xx = 1 / (xx - a0)
check("pi's continued fraction begins 3; 7, 15, 1, 292, so its first approximation is 3 + 1/7 = 22/7 = 3.142857...: "
      "the wheel, unturned, and above pi (Archimedes)",
      cf == [3, 7, 15, 1, 292] and tail(22, 6) == W and Fr(22, 7) > PI)

# an aside: counting in base 7 (a different system from the author's)
check("in base 7 the first full wheel is 1/5 = 0.1254 1254 ..., whose halves add to 66 (Midy, with 6 for 9)",
      digits(1, 5, 7) == [1, 2, 5, 4] and (1 * 7 + 2) + (5 * 7 + 4) == 6 * 7 + 6
      and [p for p in primes(13) if full(7, p)] == [2, 5, 11, 13])
ok7 = True
for p in primes(400):
    if p % 4 == 3 and p > 3 and full(7, p):
        ok7 &= sum((-1) ** j * d for j, d in enumerate(digits(1, p, 7))) == -8 * class_number(-p)
check("Girstmair's formula in base 7: the alternating digit sum of 1/p is -8 h(-p) (every such p below 400; "
      "for 1/23 it is -24 = -8 x 3)", ok7 and sum((-1) ** j * d for j, d in enumerate(digits(1, 23, 7))) == -24)
first = {b: next(p for p in primes(30000) if p > 2 and full(b, p) and 2 * diagonal(p, b) == (b - 1) * (p - 1))
         for b in (2, 3, 10)}
check(f"the first fully magic prime squares in bases 2, 3 and 10: {first[2]}, {first[3]}, {first[10]} "
      "(OEIS A096339, A096660, A072359)", first == {2: 59, 3: 223, 10: 19})
e7 = edge_primes(7, 20000)
check(f"in base 7, the fully magic prime squares below 20000 (besides the trivial 2): {e7}", e7 == [10831])

print()
print("ALL CHECKS PASS" if not FAILED else f"{len(FAILED)} FAILED")
sys.exit(1 if FAILED else 0)
