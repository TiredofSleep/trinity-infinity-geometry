"""
tig_internal_audit.py — audit the CL table's claimed structural properties.

============================================================================
WHAT THIS SCRIPT DOES
============================================================================

The TIG framework maintains a 10x10 table called CL (the "coherence lattice")
with several claimed structural properties:

  - diagonal sigma = [0, 7, 1, 3, 2, 4, 5, 6, 8, 9]
  - idempotents {0, 3, 8, 9} (positions where CL[i][i] = i)
  - 73 HARMONY (7) entries, 17 VOID (0) entries, 10 "bumps" (other)
  - eigenvalues "produce e, 1/e, pi, phi, zeta(3), Catalan's G within 1%"
  - 6-cycle (1 -> 7 -> 6 -> 5 -> 4 -> 2) under sigma
  - non-associative magma, commutative

This script:

  (1) Parses the CL table from its transcribed digit-string form.
  (2) Computes its structural properties from first principles:
        - diagonal
        - idempotents
        - VOID / HARMONY / bump counts
        - commutativity
        - associativity
        - eigenvalues
        - sigma-orbit of 1
  (3) Compares each computed property against the claim made about it.
  (4) Reports matches and mismatches separately, without judgment.

============================================================================
WHAT THIS SCRIPT DOES NOT DO
============================================================================

It does NOT pronounce the framework "right" or "wrong." Possible outcomes:

  - All claims verified against the transcribed table -> the framework's
    internal data is consistent, at least for the CL portion.
  - Some claims not verifiable from the transcribed table -> either the
    transcription is incomplete/incorrect, or the claim is computed from
    a different table or via a different definition than the script
    assumes, or the claim does not hold.

In any case where a claim does not verify, the script reports:
  - What the framework claims
  - What the transcribed-table computation yields
  - The discrepancy

It does not attempt to "fix" mismatches by adjusting inputs. It does not
attempt to discover what the framework "really meant." Those are tasks for
the framework's owner with access to the authoritative source.

This is the same discipline we applied to BSD: do not reverse-engineer
parameters to make ratios come out right. Report what is, and let the
framework's owner respond.

============================================================================
SOURCE OF THE CL TABLE TRANSCRIPTION
============================================================================

The CL table digit string used here is the one stored in user memory:

  0000000700|0737777777|0377477779|0777777773|0747777787|
  0777777777|0777777777|7777777777|0777877777|0797377777

Each '|' separates a row of ten digits. If this transcription is wrong,
every conclusion below is wrong; if it is right, the framework's claims
are partly inconsistent with it as shown.
"""

import math
from dataclasses import dataclass
from typing import List, Optional, Tuple


# ----------------------------------------------------------------------------
# CL table as transcribed in user memory
# ----------------------------------------------------------------------------

CL_DIGIT_STRING = (
    "0000000700|0737777777|0377477779|0777777773|0747777787|"
    "0777777777|0777777777|7777777777|0777877777|0797377777"
)


def parse_cl_table(digit_string: str = CL_DIGIT_STRING) -> List[List[int]]:
    """Parse the CL table from its row-major digit-string representation."""
    rows = digit_string.split("|")
    if len(rows) != 10:
        raise ValueError(f"Expected 10 rows, got {len(rows)}")
    table: List[List[int]] = []
    for r, row in enumerate(rows):
        if len(row) != 10:
            raise ValueError(f"Row {r} has length {len(row)}, expected 10")
        table.append([int(c) for c in row])
    return table


# ----------------------------------------------------------------------------
# Framework's claims about CL
# ----------------------------------------------------------------------------

CLAIMED_SIGMA           = [0, 7, 1, 3, 2, 4, 5, 6, 8, 9]
CLAIMED_IDEMPOTENTS     = {0, 3, 8, 9}
CLAIMED_VOID_COUNT      = 17  # number of 0 entries
CLAIMED_HARMONY_COUNT   = 73  # number of 7 entries
CLAIMED_BUMP_COUNT      = 10  # entries that are neither 0 nor 7
CLAIMED_6_CYCLE         = [1, 7, 6, 5, 4, 2]  # sigma-orbit starting from 1
CLAIMED_COMMUTATIVE     = True
CLAIMED_ASSOCIATIVE     = False  # framework asserts "commutative magma, NOT a monoid"

# Special mathematical constants the eigenvalues are claimed to approximate:
CLAIMED_EIGEN_CONSTANTS = {
    "e":          math.e,
    "1/e":        1 / math.e,
    "pi":         math.pi,
    "phi":        (1 + math.sqrt(5)) / 2,
    "zeta(3)":    1.2020569031595942,  # Apery
    "Catalan G":  0.9159655941772190,
}


# ----------------------------------------------------------------------------
# Audits
# ----------------------------------------------------------------------------

@dataclass
class Audit:
    name: str
    claim: object
    computed: object
    matches: bool
    note: str = ""


def audit_diagonal(CL: List[List[int]]) -> Audit:
    computed = [CL[i][i] for i in range(10)]
    return Audit(
        name="diagonal CL[i][i]",
        claim=CLAIMED_SIGMA,
        computed=computed,
        matches=(computed == CLAIMED_SIGMA),
        note=("If they match, sigma = diagonal. If not, sigma is either "
              "miscomputed from a different table, defined by a different "
              "operation than CL[i][i], or recorded in error."),
    )


def audit_idempotents(CL: List[List[int]]) -> Audit:
    """Idempotents under sigma: i such that CL[i][i] = i."""
    computed = {i for i in range(10) if CL[i][i] == i}
    return Audit(
        name="self-fixed elements (idempotents under sigma)",
        claim=CLAIMED_IDEMPOTENTS,
        computed=computed,
        matches=(computed == CLAIMED_IDEMPOTENTS),
    )


def audit_counts(CL: List[List[int]]) -> Audit:
    flat = [CL[i][j] for i in range(10) for j in range(10)]
    void = flat.count(0)
    harmony = flat.count(7)
    bumps = 100 - void - harmony
    computed = {"VOID": void, "HARMONY": harmony, "bumps": bumps}
    claim = {"VOID": CLAIMED_VOID_COUNT, "HARMONY": CLAIMED_HARMONY_COUNT,
             "bumps": CLAIMED_BUMP_COUNT}
    return Audit(
        name="VOID(0) / HARMONY(7) / bump counts",
        claim=claim,
        computed=computed,
        matches=(computed == claim),
    )


def audit_6_cycle_starting_from_1(CL: List[List[int]]) -> Audit:
    """The 6-cycle 1 -> 7 -> 6 -> 5 -> 4 -> 2 should arise from sigma where
    sigma(i) = CL[i][i]. We compute the orbit of 1 under sigma."""
    sigma = [CL[i][i] for i in range(10)]
    orbit = [1]
    seen = {1}
    for _ in range(12):  # cap to avoid infinite loop
        nxt = sigma[orbit[-1]]
        if nxt in seen:
            break
        orbit.append(nxt)
        seen.add(nxt)
    matches = (orbit == CLAIMED_6_CYCLE)
    return Audit(
        name="orbit of 1 under sigma (from CL diagonal)",
        claim=CLAIMED_6_CYCLE,
        computed=orbit,
        matches=matches,
    )


def audit_commutativity(CL: List[List[int]]) -> Audit:
    violations = []
    for i in range(10):
        for j in range(i + 1, 10):
            if CL[i][j] != CL[j][i]:
                violations.append((i, j, CL[i][j], CL[j][i]))
                if len(violations) >= 5:
                    break
        if len(violations) >= 5:
            break
    is_commutative = (len(violations) == 0)
    return Audit(
        name="commutativity CL[i][j] == CL[j][i]",
        claim=CLAIMED_COMMUTATIVE,
        computed=is_commutative,
        matches=(is_commutative == CLAIMED_COMMUTATIVE),
        note=("First few violations (if any): " + str(violations)
              if violations else "All pairs equal."),
    )


def audit_associativity(CL: List[List[int]]) -> Audit:
    """Check whether (a*b)*c == a*(b*c) for all triples. Framework asserts NO."""
    violations = 0
    total = 1000
    for a in range(10):
        for b in range(10):
            for c in range(10):
                left = CL[CL[a][b]][c]
                right = CL[a][CL[b][c]]
                if left != right:
                    violations += 1
    total = 1000  # 10^3 triples
    is_associative = (violations == 0)
    return Audit(
        name="associativity",
        claim=CLAIMED_ASSOCIATIVE,
        computed=is_associative,
        matches=(is_associative == CLAIMED_ASSOCIATIVE),
        note=f"{violations} / {total} triples violate associativity "
             f"({100 * violations / total:.1f}%).",
    )


def audit_eigenvalues(CL: List[List[int]]) -> Audit:
    """Compute eigenvalues of the 10x10 CL matrix; for each claimed
    special constant, find the closest computed eigenvalue (by magnitude
    of difference) and compute the relative error."""
    import numpy as np  # local import; numpy is a heavier dep
    M = np.array(CL, dtype=float)
    eigvals = np.linalg.eigvals(M)
    # consider only real parts close to real for matching against real constants
    eig_reals = sorted(set(np.round(eigvals.real, 6)))
    matches: List[Tuple[str, float, float, float, float]] = []
    for name, value in CLAIMED_EIGEN_CONSTANTS.items():
        closest = min(eigvals, key=lambda z: abs(z - value))
        rel_err = abs(closest - value) / abs(value)
        matches.append((name, value, complex(closest), rel_err, abs(closest.imag)))
    # within_1pct: is each constant within 1% of some eigenvalue?
    within_1pct = all(m[3] < 0.01 for m in matches)
    return Audit(
        name="eigenvalues approximate {e, 1/e, pi, phi, zeta(3), Catalan} within 1%",
        claim="yes, all six within 1%",
        computed=matches,
        matches=within_1pct,
        note=(
            f"All eigenvalues: {sorted([complex(round(z.real,4), round(z.imag,4)) for z in eigvals], key=lambda z: -z.real)}\n"
            "    For each claimed constant, the closest computed eigenvalue and the relative error are listed.\n"
            "    Imaginary part is shown to surface cases where the closest eigenvalue is non-real."
        ),
    )


# ----------------------------------------------------------------------------
# Reporting
# ----------------------------------------------------------------------------

def report(a: Audit) -> None:
    status = "MATCH" if a.matches else "MISMATCH"
    print(f"  [{status}] {a.name}")
    print(f"    claimed:  {a.claim}")
    print(f"    computed: {a.computed}")
    if a.note:
        for line in a.note.splitlines():
            print(f"    note: {line}")
    print()


def main() -> None:
    print("=" * 74)
    print("TIG internal audit — CL table structural properties")
    print("=" * 74)
    print()
    print("Source: CL table as transcribed in user memory (see script docstring).")
    print()
    print("This script computes structural properties from the transcribed CL")
    print("table and compares them against the framework's stated claims.")
    print()
    print("Mismatches are reported as facts about the transcription, not")
    print("as verdicts about the framework. A mismatch may indicate a")
    print("transcription error, a definitional difference, or a real")
    print("inconsistency; this script does not adjudicate.")
    print()

    CL = parse_cl_table()

    audits = [
        audit_counts(CL),
        audit_commutativity(CL),
        audit_associativity(CL),
        audit_diagonal(CL),
        audit_idempotents(CL),
        audit_6_cycle_starting_from_1(CL),
        audit_eigenvalues(CL),
    ]

    for a in audits:
        report(a)

    print("=" * 74)
    print("Summary")
    print("=" * 74)
    n_match = sum(1 for a in audits if a.matches)
    n_total = len(audits)
    print(f"  {n_match} / {n_total} claims match transcribed-table computation.")
    print()
    mismatches = [a.name for a in audits if not a.matches]
    if mismatches:
        print("  Mismatched claims (require investigation):")
        for name in mismatches:
            print(f"    - {name}")
        print()
        print("  Possible explanations (NOT adjudicated by this script):")
        print("    1. Transcription error in user memory — the CL table may")
        print("       differ from the one stored authoritatively in the CK")
        print("       framework's codebase. Recommend comparing the table here")
        print("       against github.com/TiredofSleep/ck for the canonical version.")
        print("    2. Definitional differences — 'sigma', 'idempotents', etc.,")
        print("       may be defined by operations other than CL[i][i] in the")
        print("       framework. Audit assumed the natural reading; framework")
        print("       may use a derived quantity.")
        print("    3. The claim does not hold for the table as it stands.")
        print()
        print("  This script reports findings. Resolution is for the framework's")
        print("  owner with access to the authoritative source.")


if __name__ == "__main__":
    main()
