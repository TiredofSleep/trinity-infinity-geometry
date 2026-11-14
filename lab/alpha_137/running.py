#!/usr/bin/env python3
"""running.py -- the exact physics inside the author's answer of 14 November 2026 (README.md, "The author's answer").
[FENCE: physics readings; nothing here is a registered test.]

    "the edge was close... and it has a range at high energies, likely due to the edge being on the edge... it
     expresses the same 137 over itself fractally"  -- the author, 14 November 2026

  R1  the range: QED's one-loop leptonic running from zero momentum to the Z mass,
      delta_alpha = (alpha/3 pi) sum over e, mu, tau of (ln(M_Z^2/m^2) - 5/3), against Steinhauser's three-loop
      total 0.0314977 (1998)
  R2  the staircase of thresholds: the one-loop slope of 1/alpha per unit of ln Q is -(2/3 pi) b(Q), where
      b(Q) = sum of N_c Q_f^2 over the charged particles lighter than Q: each one steps the slope up at its mass
  R3  two literal "137 over itself" forms, computed on first reading the author's message, so post hoc and NOT a test:
      the fixed points of x = 137 + ln(x)/x and of x = 137 + ln(137)/x, against alpha^-1

Standard library only.  ASCII output; writes running.log.
"""
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ALPHA_INV = 137.035999177                                              # CODATA 2022
M = {"e": 0.51099895069, "mu": 105.6583755, "tau": 1776.86}           # MeV (CODATA 2022; PDG for tau)
MZ = 91187.6                                                           # MeV (PDG)
STEINHAUSER = 0.0314977                                                # three-loop leptonic, Phys. Lett. B 429 (1998)
OUT = []


def say(s=""):
    print(s)
    OUT.append(s)


def main():
    a = 1 / ALPHA_INV
    one_loop = sum(a / (3 * math.pi) * (math.log(MZ ** 2 / m ** 2) - 5 / 3) for m in M.values())
    say("running.py: the exact physics inside the author's answer [FENCE]")
    say()
    say(f"R1  one-loop leptonic running to the Z mass: {one_loop:.7f}; Steinhauser's three-loop total {STEINHAUSER}; "
        f"ratio {one_loop / STEINHAUSER:.5f}")
    ok1 = abs(one_loop / STEINHAUSER - 1) < 0.005
    say(f"    {'PASS' if ok1 else 'FAIL'}: within 0.5%. With the hadrons (about 0.0276, from e+e- data) 1/alpha falls "
        f"from {ALPHA_INV:.3f} to about {ALPHA_INV * (1 - STEINHAUSER - 0.0276):.2f} at the Z mass (on shell; 127.95 "
        f"in the MS-bar scheme)")
    say()
    steps = [("e", 0.511, 1.0), ("mu", 105.7, 1.0), ("u, d, s (as quarks)", 1000.0, 3 * (4 / 9 + 1 / 9 + 1 / 9)),
             ("c", 1270.0, 3 * 4 / 9), ("tau", 1776.9, 1.0), ("b", 4180.0, 3 * 1 / 9)]
    b = 0.0
    say("R2  the staircase of thresholds: b(Q) = sum of N_c Q_f^2 over charged particles lighter than Q")
    for name, mass, inc in steps:
        b += inc
        say(f"    above {mass:8.1f} MeV ({name}): b = {b:.4f}, slope of 1/alpha per unit of ln Q = "
            f"{-2 * b / (3 * math.pi):+.4f}")
    ok2 = abs(b - 20 / 3) < 1e-12
    say(f"    {'PASS' if ok2 else 'FAIL'}: with the three leptons and five quarks, b = 20/3")
    say()
    x = 137.0
    for _ in range(60):
        x = 137 + math.log(x) / x
    y = (137 + math.sqrt(137 ** 2 + 4 * math.log(137))) / 2
    z = 137 + math.log(137) / 137
    say("R3  post hoc, NOT a test (computed on first reading the author's message):")
    for name, v in (("137 + ln 137/137 (round c's nearest)", z), ("fixed point of x = 137 + ln(x)/x", x),
                    ("fixed point of x = 137 + ln(137)/x", y)):
        say(f"    {name:38s} {v:.9f}   {v - ALPHA_INV:+.3e} from alpha^-1")
    ok3 = abs(x - ALPHA_INV) > abs(z - ALPHA_INV) and abs(y - ALPHA_INV) > abs(z - ALPHA_INV)
    say(f"    {'PASS' if ok3 else 'FAIL'}: both self-referential forms land farther from alpha^-1 than the plain form")
    open(os.path.join(HERE, "running.log"), "w", encoding="utf-8").write("\n".join(OUT) + "\n")
    raise SystemExit(0 if ok1 and ok2 and ok3 else 1)


if __name__ == "__main__":
    main()
