"""
verify_fenced_readings.py: the exact pieces inside the fenced readings of FENCED_READINGS.md.

None of these is evidence for anything. They are the parts of the October 2026 readings that are
plain mathematics or plain arithmetic on measured constants, checked so that the readings stand on
correct numbers. Run: python verify_fenced_readings.py   (numpy only)
"""
import itertools
import numpy as np

FAILS = []
def check(name, cond):
    print(f"  {'ok  ' if cond else 'FAIL'} {name}")
    if not cond:
        FAILS.append(name)

# 1. the cube's corners 0..7 and the body-diagonal shadow (R1 in FENCED_READINGS)
corners = {n: np.array([(n >> 2) & 1, (n >> 1) & 1, n & 1], float) for n in range(8)}
d = np.ones(3) / np.sqrt(3)
u, t = np.array([1, -1, 0]) / np.sqrt(2), np.array([1, 1, -2]) / np.sqrt(6)    # the shadow plane
shadow = {n: (round(float(v @ u), 9), round(float(v @ t), 9)) for n, v in corners.items()}
centre = [n for n, s in shadow.items() if s == shadow[0]]
check("down the long diagonal, exactly 0 (000) and 7 (111) land on the centre", centre == [0, 7])
rim = sorted(round(float(np.degrees(np.arctan2(s[1], s[0])))) % 360 for n, s in shadow.items() if n not in (0, 7))
check("the other six form a regular hexagon (six directions 60 degrees apart)",
      all((b - a) % 360 == 60 for a, b in zip(rim, rim[1:] + rim[:1])))
check("7 + 1 = 0 mod 8, so 7 is -1, not 0", (7 + 1) % 8 == 0 and 7 % 8 != 0)
check("7 is 0 with every bit flipped (7 = 0 XOR 111)", 0 ^ 0b111 == 7)

# 2. clock and shift: the cube-root version of Dirac's square root (R3)
w = np.exp(2j * np.pi / 3)
C = np.diag([1, w, w * w]); S = np.roll(np.eye(3), 1, axis=0)
check("C S = w S C (the order matters: S C = w^2 C S)", np.allclose(C @ S, w * S @ C))
rng = np.random.default_rng(0)
a, b = rng.normal(size=2) + 1j * rng.normal(size=2)
M = a * C + b * S
check("(aC + bS)^3 = (a^3 + b^3) I, because 1 + w + w^2 = 0", np.allclose(M @ M @ M, (a ** 3 + b ** 3) * np.eye(3)))
I3 = np.eye(3)
E = [np.kron(C, I3), np.kron(S, I3), np.kron(C @ S, C)]          # three 9x9 matrices
c = rng.normal() + 1j * rng.normal()
N = a * E[0] + b * E[1] + c * E[2]
check("in 9 x 9, three matrices linearize the cube: (ae1 + be2 + ce3)^3 = a^3 + b^3 + c^3",
      all(np.allclose(np.linalg.matrix_power(e, 3), np.eye(9)) for e in E)
      and np.allclose(N @ N @ N, (a ** 3 + b ** 3 + c ** 3) * np.eye(9)))
lam = w
check("a cube root of unity turns at sin 120 = 0.866 and grows or decays at cos 120 = -1/2",
      np.isclose(lam.imag, np.sin(np.radians(120))) and np.isclose(lam.real, -0.5))

# 3. the electron's numbers (R5, R6): CODATA 2018 values
hbar, h, c0 = 1.054571817e-34, 6.62607015e-34, 299792458.0
me, mmu, mp = 9.1093837015e-31, 1.883531627e-28, 1.67262192369e-27
re_class = 2.8179403262e-15                                          # classical electron radius, m
r = hbar / (2 * me * c0)
check(f"the circulation radius hbar/(2mc) is {r:.3g} m (about 1.9e-13 m)", abs(r - 1.93e-13) < 0.01e-13)
check("and m c r = hbar/2 holds by construction, so the 'match' is not evidence", np.isclose(me * c0 * r, hbar / 2))
check(f"the muon's is {me / mmu * r:.3g} m: smaller by the mass ratio, {mmu / me:.1f}", abs(mmu / me - 206.8) < 0.1)
rp = hbar / (2 * mp * c0)
check(f"for the proton the formula gives {rp:.3g} m, but its measured charge radius is 0.84e-15 m: "
      f"{0.8409e-15 / rp:.1f} times larger", 7 < 0.8409e-15 / rp < 9)
omega = 2 * me * c0 ** 2 / hbar
check(f"zitterbewegung: 2mc^2/hbar = {omega:.3g} per second is an ANGULAR frequency; in cycles per "
      f"second it is 2mc^2/h = {2 * me * c0 ** 2 / h:.3g}. The chat's 'about 1.5e21 cycles per second' "
      "is off by 2 pi", abs(omega - 1.55e21) < 0.01e21 and abs(2 * me * c0 ** 2 / h - 2.47e20) < 0.01e20)
v = 5 * hbar / (4 * me * re_class)            # a solid ball of radius r_e spinning with L = hbar/2
check(f"a solid ball the size of the classical electron radius, spinning with hbar/2, has a surface "
      f"speed of {v / c0:.0f} c", 165 < v / c0 < 175)
d_si = 3.84e-10                                # silicon atoms along the <110> row, m
mc2_eV, hc_eVm = 0.51099895e6, 1.23984198e-6
p = mc2_eV ** 2 * d_si / hc_eVm / 1e6
check(f"de Broglie's clock (frequency mc^2/h) matches the row spacing at p = {p:.2f} MeV/c "
      "(the 80.87 MeV/c prediction; the 2005 dip was at 81.1)", abs(p - 80.87) < 0.05)

print()
print("ALL CHECKS PASSED" if not FAILS else f"{len(FAILS)} FAILED: {FAILS}")
raise SystemExit(1 if FAILS else 0)
