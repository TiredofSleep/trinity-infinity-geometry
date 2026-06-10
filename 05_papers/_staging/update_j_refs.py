r"""update_j_refs.py -- batch-update J-number cross-references inside .md files.

After renumber_all_v2.py moved folders to new J-numbers, this script updates
the TEXT inside README.md / manuscript.md / cover_letter.md / etc. to match.

Single-pass regex substitution so swaps (J17<->J20, J15<->J12) work correctly.

Topic-disambiguation: no old J-number appears in more than one topic area, so
a global mapping works.

Usage:
  python update_j_refs.py            # dry-run, prints proposed changes
  python update_j_refs.py --apply    # actually write files

RE-EXECUTION NOTE 2026-06-10: original run (commit 0d6d0f1) lost with the
local working copy; re-executed verbatim on the fresh clone.
"""
import os
import re
import sys

REPO = r"C:\Users\brayd\OneDrive\Desktop\trinity-infinity-geometry"

# OLD J-number -> NEW J-number
MAPPING = {
    # Tier 1 (J01-J31)
    "J35": "J01",
    "J62_RH_short_note": "J02",
    "J62": "J02",
    "J61": "J03",
    "J59": "J04",
    "J60": "J05",
    "J63_strata_fingerprint": "J06",
    "J63": "J06",
    "J_qseries_merged": "J07",
    "J_Fp_merged": "J08",
    "J30": "J09",
    "J32": "J10",
    "J31": "J11",
    "J15": "J12",
    # J13 -> J13 (no-op)
    "J01": "J14",   # combinatorics
    "J02": "J15",   # combinatorics
    "J25": "J16",
    "J54": "J17",   # combinatorics
    "J26": "J18",
    "J37": "J19",
    "J17": "J20",
    "J18": "J21",
    # J22 -> J22 (no-op)
    "J20": "J23",
    "J03": "J24",   # number_theory
    "J08": "J25",   # number_theory
    "J42": "J26",
    "J06": "J27",
    "J09": "J28",
    "J58": "J29",
    "J27": "J30",   # combinatorics
    "J34": "J31",   # interdisciplinary
    # Tier 2 (J32-J40)
    "J05": "J32",
    "J07": "J33",   # combinatorics
    "J10": "J34",   # combinatorics
    "J12": "J35",   # combinatorics
    "J19": "J36",   # combinatorics
    "J23": "J37",   # physics
    "J40": "J38",   # physics
    "J52": "J39",   # combinatorics
    "J53": "J40",   # interdisciplinary
    # Tier 3 (J41-J47)
    "J04": "J41",   # number_theory
    "J36": "J42",   # physics
    "J39": "J43",   # physics
    "J45": "J44",   # physics
    "J48": "J45",   # physics
    "J49": "J46",   # interdisciplinary
    "J56_DRAFT": "J47",
    # MERGED tombstones (J48-J52)
    "J14": "J48",
    "J16": "J49",
    "J21": "J50",   # combinatorics
    "J43": "J51",
    "J51": "J52",
}

# Sort by length DESC so longer keys (J_qseries_merged, J62_RH_short_note,
# J56_DRAFT, J63_strata_fingerprint) match before shorter ones (J62, J63, J_).
keys_sorted = sorted(MAPPING.keys(), key=len, reverse=True)

# Word-boundary regex. Captures the OLD J-string.
PAT = re.compile(
    r"(?<![A-Za-z0-9_])("
    + "|".join(re.escape(k) for k in keys_sorted)
    + r")(?![A-Za-z0-9_])"
)


def replace(m):
    return MAPPING[m.group(1)]


# Directories / files to skip:
SKIP_DIRS = {
    os.path.join(REPO, "05_papers", "_staging"),
    os.path.join(REPO, "tmp_renumber"),
    os.path.join(REPO, ".git"),
    os.path.join(REPO, ".github"),
}
SKIP_FILENAMES = {
    "MEMORY.md",
    "memory.md",
}


def should_skip(path):
    p = os.path.abspath(path)
    for d in SKIP_DIRS:
        if p.startswith(os.path.abspath(d) + os.sep) or p == os.path.abspath(d):
            return True
    if os.path.basename(p) in SKIP_FILENAMES:
        return True
    return False


def find_markdown_files(roots):
    out = []
    for root in roots:
        for dirpath, dirnames, filenames in os.walk(root):
            # prune
            dirnames[:] = [
                d for d in dirnames
                if not should_skip(os.path.join(dirpath, d))
            ]
            for fn in filenames:
                if fn.lower().endswith((".md", ".tex")):
                    p = os.path.join(dirpath, fn)
                    if not should_skip(p):
                        out.append(p)
    return out


def main():
    apply = "--apply" in sys.argv
    roots = [
        os.path.join(REPO, "05_papers"),
        os.path.join(REPO, "04_meta"),
        os.path.join(REPO, "03_canonical_reference"),
    ]
    # Top-level README + a few specific files
    extra_files = [
        os.path.join(REPO, "README.md"),
    ]

    files = find_markdown_files(roots)
    for ef in extra_files:
        if os.path.isfile(ef) and not should_skip(ef):
            files.append(ef)

    print(f"Scanning {len(files)} .md/.tex files...\n")

    total_files_changed = 0
    total_subs = 0

    for path in files:
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
        except (UnicodeDecodeError, OSError) as e:
            print(f"  SKIP {path}: {e}")
            continue
        n_subs = 0

        def counting_replace(m):
            nonlocal n_subs
            n_subs += 1
            return MAPPING[m.group(1)]

        new_content = PAT.sub(counting_replace, content)
        if new_content != content:
            rel = os.path.relpath(path, REPO)
            print(f"  {'WRITE' if apply else 'DRY  '} {rel}  ({n_subs} substitutions)")
            total_files_changed += 1
            total_subs += n_subs
            if apply:
                with open(path, "w", encoding="utf-8", newline="\n") as f:
                    f.write(new_content)

    print(f"\nFiles changed: {total_files_changed}")
    print(f"Total substitutions: {total_subs}")
    print(f"Mode: {'APPLIED' if apply else 'DRY-RUN (use --apply to write)'}")


if __name__ == "__main__":
    main()
