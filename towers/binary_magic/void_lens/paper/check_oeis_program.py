"""check_oeis_program.py -- the OEIS A160523 draft's program against OEIS's own data, exact determinants of MATLAB's
odd magic(n) for n = 3..31, and the table in magic_det.tex. Exits 1 on any mismatch. Run: python check_oeis_program.py"""
from fractions import Fraction


def a(n):                      # the program in oeis_A160523_submission.txt, verbatim logic
    if n % 2 == 0:
        return -10 if n == 2 else 0
    s = (-1)**((n-1)//2) * n**(n-1) * (n*n+1) // 2
    seen = [False]*n
    for k in range(1, n):
        if not seen[k]:
            L, j = 0, k
            while not seen[j]:
                seen[j], L, j = True, L+1, 2*j % n
            s *= n**L - (-1)**L
    return s


def magic_odd(n):              # MATLAB magic.m, odd branch: M = n*mod(I+J-(n+3)/2, n) + mod(I+2J-2, n) + 1
    return [[n * ((I + J - (n + 3) // 2) % n) + ((I + 2 * J - 2) % n) + 1 for J in range(1, n + 1)]
            for I in range(1, n + 1)]


def det_bareiss(M):
    M = [row[:] for row in M]; n = len(M); sign, prev = 1, 1
    for k in range(n - 1):
        if M[k][k] == 0:
            r = next((i for i in range(k + 1, n) if M[i][k]), None)
            if r is None:
                return 0
            M[k], M[r] = M[r], M[k]; sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // prev
        prev = M[k][k]
    return sign * M[n - 1][n - 1]


OEIS = [1, -10, -360, 0, 5070000, 0, -348052801600, 0, 75035738059027200, 0, -41037749689303977660600, 0,
        46138065481819513248350194800, 0, -95867954490405704140800000000000000, 0,
        343347181141827635973213833586893432832000, 0,
        -1962493419491568854064862681564905921231239717640, 0]
ok_oeis = all(a(n) == OEIS[n - 1] for n in range(1, 21))
print("program matches OEIS A160523 data for n = 1..20:", ok_oeis)
ok_exact = all(a(n) == det_bareiss(magic_odd(n)) for n in range(3, 32, 2))
print("program matches exact det of MATLAB's odd magic(n) for n = 3..31:", ok_exact)
table = {3: -40, 5: 8112, 7: -2958400, 9: 1743123200, 11: -1582182900600, 13: 1980337235410800,
         15: -3283944692869234688}
ok_table = all(a(n) == v * n ** (n - 1) for n, v in table.items())
print("paper's table det/n^(n-1) for n = 3..15 matches:", ok_table)
print("example a(7) =", a(7))
raise SystemExit(0 if (ok_oeis and ok_exact and ok_table) else 1)
