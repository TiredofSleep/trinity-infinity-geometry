"""
harmony_complementarity.py — TSML and BHML treat HARMONY (op 7)
                              oppositely.

Triggered by Brayden 2026-04-29: "the difference between tsml8 and
tsml10 is whether or not bhml10 has 'become' something... like bhml
feeds back into the 8-10 space of tsml"

Claim verified by this script:
  * TSML row 7 (HARMONY-on-left)  is constant 7   — absorbing structure
  * TSML col 7 (HARMONY-on-right) is constant 7   — absorbing structure
  * BHML row 7 = [7, 2, 3, 4, 5, 6, 7, 8, 9, 0]   — +1 cyclic shift on b≠0
  * BHML col 7 = [7, 2, 3, 4, 5, 6, 7, 8, 9, 0]   — same shape

So TSML treats HARMONY as a SINK; BHML treats HARMONY as a +1 SUCCESSOR.

Distribution of TSML_10's 126 non-associative triples:
  ~half (60) involve operators 8 or 9 (the "8-10 extension")
  ~half (66) are entirely in operators 0..7 (TSML_8)

The transition point: TSML's restricted-to-{0..n-1} alpha drops at n=8
(adding operator 7 = HARMONY).  Adding op 7 closes the subset under
TSML's multiplication; the previously-hidden non-associativity (from
intermediate values escaping to op 7 in {0..6}-restricted operands)
becomes structurally locked-in.

The 7 in T*=5/7 = the largest operand-set size before HARMONY is
included.  The 8 in "TSML_8" = the closure point.

Reference: Atlas/FRONTIER_FINDINGS_2026_04_29.md §16
"""
from __future__ import annotations

import itertools

TSML_ROWS = [
    "0000000700",  "0737777777",  "0377477779",  "0777777773",  "0747777787",
    "0777777777",  "0777777777",  "7777777777",  "0777877777",  "0797377777",
]
BHML_ROWS = [
    "0123456789",  "1234567266",  "2334567366",  "3444567466",  "4555567577",
    "5666667677",  "6777777777",  "7234567890",  "8666777978",  "9666777080",
]


def find_non_assoc(M, n):
    """All non-associative triples (a,b,c) with operands in {0..n-1}.
    Intermediate values are allowed to escape outside the subset; we
    just check whether (ab)c == a(bc) holds in the FULL magma."""
    out = []
    for a, b, c in itertools.product(range(n), repeat=3):
        if M[M[a][b]][c] != M[a][M[b][c]]:
            out.append((a, b, c))
    return out


def main():
    TSML = [[int(c) for c in row] for row in TSML_ROWS]
    BHML = [[int(c) for c in row] for row in BHML_ROWS]

    print("=" * 72)
    print("TSML and BHML — opposite handling of HARMONY (op 7)")
    print("=" * 72)
    print()
    print("TSML row 7 (HARMONY-on-left):  ", [TSML[7][b] for b in range(10)])
    print("TSML col 7 (HARMONY-on-right): ", [TSML[a][7] for a in range(10)])
    print("  -> TSML treats HARMONY as ABSORBING:")
    print("     HARMONY * anything = HARMONY ; anything * HARMONY = HARMONY")
    print()
    print("BHML row 7:                    ", [BHML[7][b] for b in range(10)])
    print("BHML col 7:                    ", [BHML[a][7] for a in range(10)])
    print("  -> BHML treats HARMONY as +1 SUCCESSOR (on b != 0):")
    print("     HARMONY * b = (b+1) mod 10 for b in {1..9}")
    print("     HARMONY * 0 = HARMONY (the b=0 case maps to HARMONY itself)")
    print()
    print("=" * 72)
    print("Where TSML_10's 126 non-associative triples live")
    print("=" * 72)
    failed = find_non_assoc(TSML, 10)
    in_extension = sum(1 for t in failed if any(x in {8, 9} for x in t))
    purely_low   = sum(1 for t in failed if all(x < 8 for x in t))
    print(f"\nTotal non-assoc:              {len(failed)} / 1000")
    print(f"Failures involving op 8 or 9: {in_extension}")
    print(f"Failures purely in ops 0..7:  {purely_low}")
    print(f"\n~{round(in_extension/len(failed)*100)}% of TSML_10's failures "
          f"involve the BHML-style 8-10 extension operators.")
    print()
    print("=" * 72)
    print("Walking TSML's restricted alpha by subset size n")
    print("=" * 72)
    for n in range(2, 11):
        f = len(find_non_assoc(TSML, n))
        a = (n**3 - f) / n**3
        marker = "  <- closure point (op 7 = HARMONY now in subset)" if n == 8 else ""
        print(f"  n={n:2d}: {f:3d} fail / {n**3:4d} = alpha {a:.4f}{marker}")

    print()
    print("=" * 72)
    print("Net")
    print("=" * 72)
    print("""
TSML's HARMONY = sink (constant 7).
BHML's HARMONY = +1 cyclic successor (mod 10, with b=0 -> 7).
The two magmas are COMPLEMENTARY in their HARMONY-handling.

This complementarity is the structural mechanism for "M+M proved
sufficient" on Z/10Z: TSML's absorption-to-HARMONY would lock the
algebra; BHML's cyclic +1 successor in the same row OPENS it back.
The pair jointly spans the dynamics by carrying opposite algebraic
styles in the {7, 8, 9} HARMONY-region.

Brayden 2026-04-29: "BHML feeds back into the 8-10 space of TSML"
operationalizes here — BHML's structure on operators 7-9 IS the
generating-cycle that TSML's absorbing-row would have foreclosed.
The pair is dual; either alone would over- or under-constrain.

Reference: Atlas/FRONTIER_FINDINGS_2026_04_29.md §16
""")


if __name__ == "__main__":
    main()
