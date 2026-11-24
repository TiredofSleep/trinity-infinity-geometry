"""watkins_bsd_check.py -- read after round 10: are the generators a basis? (not registered)

  python -I watkins_bsd_check.py RESULTS.json

For 200 curves drawn at random (seed 7) from stratum U, the analytic order of Sha from the BSD formula,
L''(1)/2! = Omega * Reg * prod(c_p) * Sha / |tors|^2, with Reg from the generators found by watkins_round.py (PARI's
ellanalyticrank on the minimal model, ellbsd). A basis gives a perfect square; generators spanning a sublattice of
index k would give the true order divided by k^2.
"""
import json, math, random, sys
from cypari import pari
pari.allocatemem(2 * 10 ** 9)
import ctypes
k32 = ctypes.windll.kernel32; k32.GetCurrentProcess.restype = ctypes.c_void_p
k32.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_uint]; k32.SetPriorityClass(k32.GetCurrentProcess(), 0x4000)
res = [r for r in json.load(open(sys.argv[1])) if r.get('ok') and r['stratum'] == 'U']
random.seed(7); pick = random.sample(res, 200)
worst, bad = 0.0, []
for r in pick:
    Em = pari(f"ellminimalmodel(ellinit({r['ai']}))")
    reg = r['G'][0][0] * r['G'][1][1] - r['G'][0][1] ** 2
    ar = pari.ellanalyticrank(Em)
    sha = float(ar[1]) / math.factorial(int(ar[0])) / (float(pari.ellbsd(Em)) * reg)
    sq = round(math.sqrt(max(sha, 0))) ** 2
    worst = max(worst, abs(sha - sq))
    if abs(sha - sq) > 1e-6 or sq == 0: bad.append((r['N'], sha))
print(f"200 random curves of stratum U (conductors {min(r['N'] for r in pick)} to {max(r['N'] for r in pick)}): "
      f"analytic Sha a perfect square in {200 - len(bad)}; largest distance {worst:.2e}; exceptions {bad[:5]}")
