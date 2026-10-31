#!/usr/bin/env python3
"""test_scores.py -- runs every round script and checks its SCORE line against the scores recorded in PREREG.md.

    python test_scores.py      # about 35 seconds; needs numpy, scipy and mpmath. Exits 1 on any failure.

PREREG.md records each round's scores in tables under headings that contain "score". Every row whose first cell
starts with a round id (G1a, G10b, ...) gives that id's recorded outcome, held or lost. Each script prints one
final line, SCORE: {id: 'HELD' | 'LOST', ...}. The two must agree for every id, and every recorded id must be scored
by some script.
"""
import ast
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROUNDS = ["search.py", "rounds3.py", "round6.py", "round7.py", "round8.py", "round9.py", "round10.py"]
FAILS = []


def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (f"   ({detail})" if detail and not ok else ""))
    if not ok:
        FAILS.append(name)


recorded, in_scores = {}, False
for line in open(os.path.join(HERE, "PREREG.md"), encoding="utf-8"):
    if line.startswith("#"):
        in_scores = "score" in line.lower()
        continue
    m = re.match(r"\|\s*(G\d+[a-z])\b[^|]*\|", line)
    if in_scores and m:
        last = [c for c in line.strip().strip("|").split("|")][-1].lower()
        outcome = "HELD" if "held" in last else "LOST" if "lost" in last else None
        recorded[m.group(1)] = outcome
check(f"PREREG.md records an outcome for every scored id ({len(recorded)} ids)",
      len(recorded) > 0 and None not in recorded.values(), str(recorded))

scored = {}
for script in ROUNDS:
    run = subprocess.run([sys.executable, script], cwd=HERE, capture_output=True, text=True,
                         env=dict(os.environ, PYTHONIOENCODING="utf-8"))
    lines = [l for l in run.stdout.splitlines() if l.startswith("SCORE:")]
    ok = run.returncode == 0 and len(lines) == 1
    got = ast.literal_eval(lines[0][len("SCORE:"):].strip()) if ok else {}
    scored.update(got)
    bad = {k: (v, recorded.get(k)) for k, v in got.items() if recorded.get(k) != v}
    check(f"{script}: {got}", ok and not bad, f"exit {run.returncode}; mismatches {bad}" if ok else run.stderr[-300:])
check("every id recorded in PREREG.md is scored by a script", set(recorded) <= set(scored),
      str(sorted(set(recorded) - set(scored))))

print()
print("FAILED: " + "; ".join(FAILS) if FAILS else "All checks passed.")
sys.exit(1 if FAILS else 0)
