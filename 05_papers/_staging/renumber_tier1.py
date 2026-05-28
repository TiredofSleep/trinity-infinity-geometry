r"""renumber_tier1.py -- rename Tier 1 papers from old J-numbers to new J01-J20.

Old -> New mapping (per user approval 2026-05-27):

  Centerpiece + most accessible + most novel first:
    J35  -> J01  (Joint Closure + Universal Attractor + 4-core)
    J62  -> J02  (TSML 8x8 Null + RH Structural Rhyme)
    J61  -> J03  (Type Specimens + C5 Fossil-Variety)

  sigma-magma trilogy + Strata + 2 mergers:
    J59  -> J04  (sigma-Magma Algebraic Rigidity)
    J60  -> J05  (ETP Profile of Linear Magmas)
    J63  -> J06  (Strata-Prime Fingerprint)
    J_qseries_merged -> J07  (Q-series Spectral Architecture)
    J_Fp_merged      -> J08  (F_p 4-Core Algebra)

  Older proven Tier 1 (in topic order):
    J15  -> J09  (Galois D_4 over LMFDB 4.2.10224.1)
    J13  -> J10  (Forced 5/7)
    J01  -> J11  (sigma(N) decay)
    J02  -> J12  (Joint Closure + Per-Coord Fuse)
    J17  -> J13  (V^otimes n vs Cl(2n))
    J18  -> J14  (-21 Invariant + sigma^2-Triadic)
    J22  -> J15  (HARMONY Ladder 70/71/72/73)
    J25  -> J16  (CL Forcing Axioms A1-A9)
    J26  -> J17  (F_p Extensions of CL_BHML)
    J31  -> J18  (Wedderburn D_4 of [TSML, BHML])

  Honest negatives:
    J27  -> J19  ((Z/10Z)* sub-magma)
    J34  -> J20  (Algebraic Detectors)

Two-pass safe rename via tmp/ to avoid collisions.
"""
import os
import sys
import subprocess

# Old folder -> New folder
RENAME = [
    ("05_papers/algebra/J35",                          "05_papers/algebra/J01"),
    ("05_papers/number_theory/J62_RH_short_note",      "05_papers/number_theory/J02"),
    ("05_papers/algebra/J61",                          "05_papers/algebra/J03"),
    ("05_papers/algebra/J59",                          "05_papers/algebra/J04"),
    ("05_papers/algebra/J60",                          "05_papers/algebra/J05"),
    ("05_papers/number_theory/J63_strata_fingerprint", "05_papers/number_theory/J06"),
    ("05_papers/algebra/J_qseries_merged",             "05_papers/algebra/J07"),
    ("05_papers/algebra/J_Fp_merged",                  "05_papers/algebra/J08"),
    ("05_papers/algebra/J15",                          "05_papers/algebra/J09"),
    ("05_papers/algebra/J13",                          "05_papers/algebra/J10"),
    ("05_papers/combinatorics/J01",                    "05_papers/combinatorics/J11"),
    ("05_papers/combinatorics/J02",                    "05_papers/combinatorics/J12"),
    ("05_papers/algebra/J17",                          "05_papers/algebra/J13"),
    ("05_papers/algebra/J18",                          "05_papers/algebra/J14"),
    ("05_papers/algebra/J22",                          "05_papers/algebra/J15"),
    ("05_papers/algebra/J25",                          "05_papers/algebra/J16"),
    ("05_papers/algebra/J26",                          "05_papers/algebra/J17"),
    ("05_papers/algebra/J31",                          "05_papers/algebra/J18"),
    ("05_papers/combinatorics/J27",                    "05_papers/combinatorics/J19"),
    ("05_papers/interdisciplinary/J34",                "05_papers/interdisciplinary/J20"),
]

REPO = r"C:\Users\brayd\OneDrive\Desktop\trinity-infinity-geometry"


def run(cmd, cwd=REPO, check=True):
    """Run a shell command via git/os, returning stdout."""
    if isinstance(cmd, str):
        cmd = cmd.split()
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0:
        print(f"FAIL: {' '.join(cmd)}\n  stderr: {r.stderr}")
        sys.exit(r.returncode)
    return r.stdout


def main():
    # Phase 1: rename old -> tmp/ to avoid collisions
    print("=== Phase 1: rename old -> tmp/ ===")
    os.makedirs(os.path.join(REPO, "tmp_renumber"), exist_ok=True)
    for old, new in RENAME:
        old_path = os.path.join(REPO, old.replace("/", os.sep))
        if not os.path.isdir(old_path):
            print(f"  SKIP (missing): {old}")
            continue
        tmp_target = os.path.join(REPO, "tmp_renumber", new.replace("/", "_"))
        print(f"  git mv {old} tmp_renumber/{new.replace('/', '_')}")
        run(["git", "mv", old, f"tmp_renumber/{new.replace('/', '_')}"])

    # Phase 2: rename tmp/ -> new
    print("\n=== Phase 2: rename tmp/ -> new ===")
    for old, new in RENAME:
        tmp_name = new.replace("/", "_")
        tmp_path = os.path.join(REPO, "tmp_renumber", tmp_name)
        if not os.path.isdir(tmp_path):
            print(f"  SKIP (missing tmp): tmp_renumber/{tmp_name}")
            continue
        # Make sure target parent exists
        new_parent = os.path.dirname(os.path.join(REPO, new.replace("/", os.sep)))
        os.makedirs(new_parent, exist_ok=True)
        print(f"  git mv tmp_renumber/{tmp_name} {new}")
        run(["git", "mv", f"tmp_renumber/{tmp_name}", new])

    # Phase 3: cleanup tmp_renumber/
    print("\n=== Phase 3: cleanup tmp_renumber/ ===")
    tmp_dir = os.path.join(REPO, "tmp_renumber")
    if os.path.isdir(tmp_dir) and not os.listdir(tmp_dir):
        os.rmdir(tmp_dir)
        print("  removed empty tmp_renumber/")

    print("\n=== Phase 4: status ===")
    print(run(["git", "status", "--short"], check=False))


if __name__ == "__main__":
    main()
