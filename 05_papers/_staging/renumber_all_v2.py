r"""renumber_all_v2.py -- comprehensive J-numbering reset for the entire portfolio.

After Tier 2 audit + 11 promotions approved 2026-05-27, renumber all 52 papers
into a contiguous J01-J52 scheme:

  J01-J31  Tier 1 (ship-ready spine, 31 papers)
  J32-J40  Tier 2 (drafts needing rigor pass, 9 papers)
  J41-J47  Tier 3 (hold / retire candidates, 7 papers)
  J48-J52  MERGED tombstones (5 papers, retained for citation)

Two-phase rename via tmp/ to avoid collisions.

Source: old TIER_INDEX numbering pre-2026-05-27.

RE-EXECUTION NOTE 2026-06-10: the original run of this script (commit
0d6d0f1) was lost when the local working copy was deleted before the
renumbering commits were pushed. Re-executed verbatim on a fresh clone
of origin/main (a24f44f). Mapping unchanged.
"""
import os
import sys
import subprocess

REPO = r"C:\Users\brayd\OneDrive\Desktop\trinity-infinity-geometry"

# Old folder -> New folder. Subdirectories preserved (papers stay in their topic area).
RENAME = [
    # === TIER 1 (J01-J31) ===
    # Flagship triad
    ("05_papers/algebra/J35",                          "05_papers/algebra/J01"),
    ("05_papers/number_theory/J62_RH_short_note",      "05_papers/number_theory/J02"),
    ("05_papers/algebra/J61",                          "05_papers/algebra/J03"),
    # σ-magma trilogy
    ("05_papers/algebra/J59",                          "05_papers/algebra/J04"),
    ("05_papers/algebra/J60",                          "05_papers/algebra/J05"),
    # Strata + mergers
    ("05_papers/number_theory/J63_strata_fingerprint", "05_papers/number_theory/J06"),
    ("05_papers/algebra/J_qseries_merged",             "05_papers/algebra/J07"),
    ("05_papers/algebra/J_Fp_merged",                  "05_papers/algebra/J08"),
    # Lie lifts
    ("05_papers/algebra/J30",                          "05_papers/algebra/J09"),
    ("05_papers/algebra/J32",                          "05_papers/algebra/J10"),
    ("05_papers/algebra/J31",                          "05_papers/algebra/J11"),
    # Galois / cyclotomic
    ("05_papers/algebra/J15",                          "05_papers/algebra/J12"),
    # J13 stays at J13 (no-op for Forced 5/7)
    # Substrate / foundations
    ("05_papers/combinatorics/J01",                    "05_papers/combinatorics/J14"),
    ("05_papers/combinatorics/J02",                    "05_papers/combinatorics/J15"),
    ("05_papers/algebra/J25",                          "05_papers/algebra/J16"),
    ("05_papers/combinatorics/J54",                    "05_papers/combinatorics/J17"),
    ("05_papers/algebra/J26",                          "05_papers/algebra/J18"),
    ("05_papers/algebra/J37",                          "05_papers/algebra/J19"),
    ("05_papers/algebra/J17",                          "05_papers/algebra/J20"),
    ("05_papers/algebra/J18",                          "05_papers/algebra/J21"),
    # J22 stays at J22 (HARMONY ladder)
    ("05_papers/algebra/J20",                          "05_papers/algebra/J23"),
    ("05_papers/number_theory/J03",                    "05_papers/number_theory/J24"),
    ("05_papers/number_theory/J08",                    "05_papers/number_theory/J25"),
    ("05_papers/number_theory/J42",                    "05_papers/number_theory/J26"),
    ("05_papers/algebra/J06",                          "05_papers/algebra/J27"),
    ("05_papers/algebra/J09",                          "05_papers/algebra/J28"),
    ("05_papers/algebra/J58",                          "05_papers/algebra/J29"),
    ("05_papers/combinatorics/J27",                    "05_papers/combinatorics/J30"),
    ("05_papers/interdisciplinary/J34",                "05_papers/interdisciplinary/J31"),

    # === TIER 2 (J32-J40) ===
    ("05_papers/algebra/J05",                          "05_papers/algebra/J32"),
    ("05_papers/combinatorics/J07",                    "05_papers/combinatorics/J33"),
    ("05_papers/combinatorics/J10",                    "05_papers/combinatorics/J34"),
    ("05_papers/combinatorics/J12",                    "05_papers/combinatorics/J35"),
    ("05_papers/combinatorics/J19",                    "05_papers/combinatorics/J36"),
    ("05_papers/physics/J23",                          "05_papers/physics/J37"),
    ("05_papers/physics/J40",                          "05_papers/physics/J38"),
    ("05_papers/combinatorics/J52",                    "05_papers/combinatorics/J39"),
    ("05_papers/interdisciplinary/J53",                "05_papers/interdisciplinary/J40"),

    # === TIER 3 (J41-J47) ===
    ("05_papers/number_theory/J04",                    "05_papers/number_theory/J41"),
    ("05_papers/physics/J36",                          "05_papers/physics/J42"),
    ("05_papers/physics/J39",                          "05_papers/physics/J43"),
    ("05_papers/physics/J45",                          "05_papers/physics/J44"),
    ("05_papers/physics/J48",                          "05_papers/physics/J45"),
    ("05_papers/interdisciplinary/J49",                "05_papers/interdisciplinary/J46"),
    ("05_papers/interdisciplinary/J56_DRAFT",          "05_papers/interdisciplinary/J47"),

    # === MERGED tombstones (J48-J52) ===
    ("05_papers/algebra/J14",                          "05_papers/algebra/J48"),
    ("05_papers/algebra/J16",                          "05_papers/algebra/J49"),
    ("05_papers/combinatorics/J21",                    "05_papers/combinatorics/J50"),
    ("05_papers/algebra/J43",                          "05_papers/algebra/J51"),
    ("05_papers/algebra/J51",                          "05_papers/algebra/J52"),
]


def run(cmd, check=True):
    if isinstance(cmd, str):
        cmd = cmd.split()
    r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
    if check and r.returncode != 0:
        print(f"FAIL: {' '.join(cmd)}\n  stderr: {r.stderr}")
        sys.exit(r.returncode)
    return r.stdout


def main():
    # PHASE 1: rename old -> tmp/
    print("=== Phase 1: rename old -> tmp_renumber/ ===")
    tmp_dir = os.path.join(REPO, "tmp_renumber")
    os.makedirs(tmp_dir, exist_ok=True)
    for old, new in RENAME:
        old_path = os.path.join(REPO, old.replace("/", os.sep))
        if not os.path.isdir(old_path):
            print(f"  SKIP (missing source): {old}")
            continue
        # Use a unique tmp name derived from the NEW path so Phase 2 can match
        tmp_name = new.replace("/", "_").replace("\\", "_")
        print(f"  git mv {old} -> tmp_renumber/{tmp_name}")
        run(["git", "mv", old, f"tmp_renumber/{tmp_name}"])

    # PHASE 2: rename tmp/ -> new
    print("\n=== Phase 2: rename tmp_renumber/ -> new ===")
    for old, new in RENAME:
        tmp_name = new.replace("/", "_").replace("\\", "_")
        tmp_path = os.path.join(REPO, "tmp_renumber", tmp_name)
        if not os.path.isdir(tmp_path):
            print(f"  SKIP (missing tmp): tmp_renumber/{tmp_name}")
            continue
        # Ensure target parent exists
        new_parent = os.path.dirname(os.path.join(REPO, new.replace("/", os.sep)))
        os.makedirs(new_parent, exist_ok=True)
        # Target should NOT exist at this point (Phase 1 cleared collisions)
        new_path = os.path.join(REPO, new.replace("/", os.sep))
        if os.path.isdir(new_path):
            print(f"  CONFLICT: {new} already exists, skipping")
            continue
        print(f"  git mv tmp_renumber/{tmp_name} -> {new}")
        run(["git", "mv", f"tmp_renumber/{tmp_name}", new])

    # PHASE 3: cleanup
    print("\n=== Phase 3: cleanup tmp_renumber/ ===")
    if os.path.isdir(tmp_dir) and not os.listdir(tmp_dir):
        os.rmdir(tmp_dir)
        print("  removed empty tmp_renumber/")
    else:
        remaining = os.listdir(tmp_dir) if os.path.isdir(tmp_dir) else []
        print(f"  WARNING: tmp_renumber/ not empty: {remaining}")


if __name__ == "__main__":
    main()
