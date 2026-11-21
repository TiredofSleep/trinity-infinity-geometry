"""saturation_sample.py -- are Cremona's tabulated generators a basis modulo torsion? A check on a random sample.

  python -I saturation_sample.py DATA_DIR [n]

Takes n (default 2000) optimal rank-2 curves at random (seed 20261121) from the allgens tables below DATA_DIR and asks
PARI's ellsaturation whether the group their tabulated generators span is saturated at every prime up to 100. If it
were not, the saturated basis would have a smaller regulator, by the square of the index.
(every_loop.py checks every curve of a class with more than one curve in another way, through the BSD quotient.)
"""
import glob
import os
import random
import re
import sys

LINE = re.compile(r'(\d+) (\w+) (\d+) \[([-\d,]+)\] (\d+) \[([\d,]*)\] ?(.*)')
PT = re.compile(r'\[(-?\d+):(-?\d+):(-?\d+)\]')


def main(data_dir, n=2000):
    try:
        from cypari import pari
    except ImportError:
        import cypari2
        pari = cypari2.Pari()
    pari.allocatemem(4 * 10 ** 8)
    lines = []
    for fn in sorted(f for f in glob.glob(os.path.join(data_dir, '**', 'allgens.*'), recursive=True)
                     if re.search(r'allgens\.\d+-\d+$', f)):
        for line in open(fn):
            m = LINE.match(line.strip())
            if m and m.group(3) == '1' and m.group(5) == '2':
                lines.append(m)
    random.seed(20261121)
    sample = random.sample(lines, n)
    changed = []
    for m in sample:
        E = pari.ellinit([int(t) for t in m.group(4).split(',')])
        P = [[pari(int(X)) / int(Z), pari(int(Y)) / int(Z)] for X, Y, Z in PT.findall(m.group(7))[:2]]
        reg_tab = float(pari.matdet(pari.ellheightmatrix(E, P)))
        S = pari.ellsaturation(E, P, 100)
        reg_sat = float(pari.matdet(pari.ellheightmatrix(E, S)))
        if abs(reg_tab / reg_sat - 1) > 1e-9:
            changed.append((m.group(1) + m.group(2) + '1', reg_tab / reg_sat))
    print(f"{n} of the {len(lines)} optimal rank-2 curves, chosen at random (seed 20261121)")
    print(f"curves whose tabulated generators are not saturated at some prime up to 100: {len(changed)}")
    for c in changed[:20]:
        print("  ", c)
    print("PASS" if not changed else "FAIL")


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 2000)
