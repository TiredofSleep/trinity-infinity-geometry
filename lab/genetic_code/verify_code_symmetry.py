"""verify_code_symmetry.py -- rechecks the results recorded in code_symmetry.log in a few seconds, without the
million random codes or the climbing.  numpy only.  Exits with 1 if a check fails.
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
print("all checks pass" if OK else "A CHECK FAILED")
sys.exit(0 if OK else 1)
