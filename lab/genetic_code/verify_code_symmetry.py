"""verify_code_symmetry.py -- rechecks the results recorded in code_symmetry.log and code_weighted.log in a few
seconds, without the million random codes or the climbing.  numpy only.  Exits with 1 if a check fails.
Run:  python verify_code_symmetry.py
"""
import sys

import numpy as np

STANDARD = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
MITO = "FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSS**VVVVAAAADDEEGGGG"
PR = {"A": 7.0, "R": 9.1, "N": 10.0, "D": 13.0, "C": 4.8, "Q": 8.6, "E": 12.5, "G": 7.9, "H": 8.4, "I": 4.9,
      "L": 4.9, "K": 10.1, "M": 5.3, "F": 5.0, "P": 6.6, "S": 7.5, "T": 6.6, "W": 5.2, "Y": 5.4, "V": 5.6}
BEST_B2 = "HRTTHRTPNESSNESSQRAAQRAAKDGGKDGGVYCLVYCIT*LFP*LFPVLIPVLLS*WMS*WM"     # from code_symmetry.log
BEST_SYM_B2 = "**VV**YYEERRDDRRSSTTPPVVNNHHKKQQMMIIFFLLSSTTGGAAWWLLLLCCSSPPGGAA"
BEST_B1 = "Y*VYW*MMCLLCLTFLGEHGSEGGI*WITNATRDRRHDQQV*VVSKSSAKSSPNAALPFLPRTP"
BEST_SYM_B1 = "AAGGGGRRSSQQKKDDLLLLVVTTFFYYTT**CCLLMMVVIIWWPP**PPSSSSRRAAHHNNEE"
OK = True


def check(label, ok):
    global OK
    print(("PASS  " if ok else "FAIL  ") + label)
    OK &= bool(ok)


def cost(code, bias=1.0):
    """Haig and Hurst's mean squared change in polar requirement; transversions weigh 1/bias"""
    num = den = 0.0
    for c in range(64):
        b = [c // 16, (c // 4) % 4, c % 4]
        for pos in range(3):
            for nb in range(4):
                if nb == b[pos]:
                    continue
                b2 = list(b)
                b2[pos] = nb
                c2 = 16 * b2[0] + 4 * b2[1] + b2[2]
                if c < c2 and code[c] != "*" and code[c2] != "*":
                    w = 1.0 if {b[pos], nb} in ({0, 1}, {2, 3}) else 1.0 / bias
                    num += w * (PR[code[c]] - PR[code[c2]]) ** 2
                    den += w
    return num / den


def paired_at(code, pos):
    """is the code pyrimidine/purine-symmetric at this letter: U with C, and A with G, meaning the same?"""
    c = np.array(list(code)).reshape(4, 4, 4)
    take = [slice(None)] * 3

    def at(base):
        t = list(take)
        t[pos] = base
        return c[tuple(t)]
    return bool((at(0) == at(1)).all() and (at(2) == at(3)).all())


def merged(code):
    return code.replace("P", "T").replace("I", "L")


check(f"the standard code's MS0 is {cost(STANDARD):.4f}, Haig and Hurst's 5.194", abs(cost(STANDARD) - 5.194) < 5e-4)
check(f"the vertebrate mitochondrial code's MS0 is {cost(MITO):.4f}", abs(cost(MITO) - 5.1735) < 5e-5)
check("the mitochondrial code is symmetric at its third letter, and the standard code is not",
      paired_at(MITO, 2) and not paired_at(STANDARD, 2))
check(f"with transition bias 2, the best code found and the best symmetric code cost the same: "
      f"{cost(BEST_B2, 2):.6f} and {cost(BEST_SYM_B2, 2):.6f}",
      abs(cost(BEST_B2, 2) - 2.856163) < 1e-6 and abs(cost(BEST_SYM_B2, 2) - cost(BEST_B2, 2)) < 1e-9)
check("the best code found is symmetric at no letter, but with the tied amino acids merged (T = P = 6.6, "
      "L = I = 4.9) it is symmetric at its second letter; the best symmetric code is symmetric at its third",
      not any(paired_at(BEST_B2, k) for k in range(3)) and paired_at(merged(BEST_B2), 1)
      and paired_at(BEST_SYM_B2, 2))
check(f"with equal weights the best code found ({cost(BEST_B1):.6f}) beats the best symmetric code "
      f"({cost(BEST_SYM_B1):.6f}) by 0.014, and it is symmetric at no letter even with the ties merged",
      abs(cost(BEST_B1) - 3.560945) < 1e-6 and abs(cost(BEST_SYM_B1) - 3.574844) < 1e-6
      and not any(paired_at(merged(BEST_B1), k) for k in range(3)))
check("all four codes keep the mitochondrial composition",
      all(sorted(x) == sorted(MITO) for x in (BEST_B2, BEST_SYM_B2, BEST_B1, BEST_SYM_B1)))

# ---------------------------------------------------------------- part 2: Freeland and Hurst's weights
FH = {0: (1.0, 0.5), 1: (0.5, 0.1), 2: (1.0, 1.0)}           # by letter: (transition, transversion)
KD = {"I": 4.5, "V": 4.2, "L": 3.8, "F": 2.8, "C": 2.5, "M": 1.9, "A": 1.8, "G": -0.4, "T": -0.7, "S": -0.8,
      "W": -0.9, "Y": -1.3, "P": -1.6, "H": -3.2, "E": -3.5, "Q": -3.5, "D": -3.5, "N": -3.5, "K": -3.9, "R": -4.5}


def zscores(scale):
    v = np.array([scale[a] for a in sorted(PR)])
    return dict(zip(sorted(PR), (v - v.mean()) / v.std()))


ZP, ZK = zscores(PR), zscores(KD)


def fh_cost(code, both=False):
    num = den = 0.0
    for c in range(64):
        b = [c // 16, (c // 4) % 4, c % 4]
        for pos in range(3):
            for nb in range(4):
                if nb == b[pos]:
                    continue
                b2 = list(b)
                b2[pos] = nb
                c2 = 16 * b2[0] + 4 * b2[1] + b2[2]
                if c < c2 and code[c] != "*" and code[c2] != "*":
                    w = FH[pos][0] if {b[pos], nb} in ({0, 1}, {2, 3}) else FH[pos][1]
                    x, y = code[c], code[c2]
                    d2 = (ZP[x] - ZP[y]) ** 2 + (ZK[x] - ZK[y]) ** 2 if both else (PR[x] - PR[y]) ** 2
                    num += w * d2
                    den += w
    return num / den


def pairings(code):
    box = np.array(list(code)).reshape(16, 4)
    return [name for name, ((a, b), (c, d)) in (("U-C", ((0, 1), (2, 3))), ("U-A", ((0, 2), (1, 3))),
                                                ("U-G", ((0, 3), (1, 2))))
            if ((box[:, a] == box[:, b]) & (box[:, c] == box[:, d])).all()]


W_BEST = "GQGQ*D*DPATALMLMSHSH*E*ETTPTIWLWASASRNRNYVYVCICLSGSGRKRKVPVPLFLF"
W_BEST_YR = "GGQQ**DDIIMMTTAASSHH**EELLWWTTPPAASSRRNNCCLLYYVVSSGGRRKKLLFFVVPP"
W2_BEST = "PPPPRRRRYWYWFCFCSSSSQHQHTTTTLLLLSGSGKNKNAAAAVVVV*G*GDEDE*M*MILIL"
W2_BEST_YR = "DDEE**GGIILL**MMKKNNSSGGVVVVAAAARRRRPPPPFFCCYYWWQQHHSSSSLLLLTTTT"
check(f"part 2: with Freeland and Hurst's weights the standard code costs {fh_cost(STANDARD):.6f} and the "
      f"mitochondrial code {fh_cost(MITO):.6f}",
      abs(fh_cost(STANDARD) - 2.628345) < 1e-6 and abs(fh_cost(MITO) - 2.666200) < 1e-6)
rng = np.random.default_rng(7)
worst = 0.0
for _ in range(5):
    code = "".join(rng.permutation(list(MITO)))
    for perm in ((1, 0, 2, 3), (2, 3, 0, 1), (0, 2, 1, 3), (3, 1, 2, 0)):
        moved = [""] * 64
        for c in range(64):
            moved[16 * (c // 16) + 4 * ((c // 4) % 4) + perm[c % 4]] = code[c]
        moved = "".join(moved)
        worst = max(worst, abs(fh_cost(moved) - fh_cost(code)), abs(fh_cost(moved, True) - fh_cost(code, True)))
check(f"part 2: relabeling the third letter never changes the weighted cost (largest change {worst:.1e})",
      worst < 1e-12)
check(f"part 2: the best code found costs {fh_cost(W_BEST):.6f} and pairs its third letters "
      f"({pairings(merged(W_BEST))}, ties merged); the best pyrimidine/purine-paired code costs the same",
      abs(fh_cost(W_BEST) - 1.327775) < 1e-6 and abs(fh_cost(W_BEST_YR) - fh_cost(W_BEST)) < 1e-9
      and len(pairings(merged(W_BEST))) > 0 and pairings(W_BEST_YR) == ["U-C"])
check(f"part 2, the scale without ties: the best code found costs {fh_cost(W2_BEST, True):.6f} and pairs its third "
      f"letters ({pairings(W2_BEST)}); the best pyrimidine/purine-paired code costs the same",
      abs(fh_cost(W2_BEST, True) - 0.546390) < 1e-6 and abs(fh_cost(W2_BEST_YR, True) - fh_cost(W2_BEST, True)) < 1e-9
      and len(pairings(W2_BEST)) > 0 and pairings(W2_BEST_YR) == ["U-C"])
check("part 2: the four codes keep the mitochondrial composition",
      all(sorted(x) == sorted(MITO) for x in (W_BEST, W_BEST_YR, W2_BEST, W2_BEST_YR)))
print("all checks pass" if OK else "A CHECK FAILED")
sys.exit(0 if OK else 1)
