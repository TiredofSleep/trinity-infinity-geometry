#!/usr/bin/env python3
"""test_ledger.py -- pins every number ledger_math.py prints, and ties them to PREDICTIONS.md.

    python test_ledger.py      # about ten seconds; needs numpy and scipy. Exits 1 on any failure.

1. It runs ledger_math.py and compares the output, line for line, with ledger_math.expected. Changing any
   input changes a printed number, so the test fails until ledger_math.expected and PREDICTIONS.md are
   updated together.
2. For each bet, the headline numbers printed must also appear in that bet's section of PREDICTIONS.md.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FAILS = []


def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (f"   ({detail})" if detail and not ok else ""))
    if not ok:
        FAILS.append(name)


run = subprocess.run([sys.executable, "ledger_math.py"], cwd=HERE, capture_output=True, text=True,
                     env=dict(os.environ, PYTHONIOENCODING="utf-8"))
check("ledger_math.py runs", run.returncode == 0, run.stderr[-300:])
got = run.stdout.splitlines()
want = open(os.path.join(HERE, "ledger_math.expected"), encoding="utf-8").read().splitlines()
diff = [(i + 1, w, g) for i, (w, g) in enumerate(zip(want, got)) if w != g]
check("output matches ledger_math.expected line for line", not diff and len(got) == len(want),
      f"first difference at line {diff[0][0]}" if diff else f"{len(got)} lines vs {len(want)}")

# Headline numbers: each must appear in the calculator's line for that bet and in that bet's ledger section.
HEADLINES = {
    "P1": ["0.6666645", "0.0000051", "1776.969", "1776.93"],
    "P2": ["0.363", "8.67", "50.29", "59.3", "8.9", "1.2", "4.0"],
    "P5": ["1.17%"],
    "P6": ["0.339", "157.8", "167.6", "172.5", "80.327"],
    "P7": ["0.03084", "0.02966", "0.00053", "+2.21", "0.02944", "-0.41", "0.380", "8.84", "59.5"],
    "P8": ["0.66666652", "1776.96651"],
}
ledger = open(os.path.join(HERE, "PREDICTIONS.md"), encoding="utf-8").read()
sections = {m.group(1): m.start() for m in re.finditer(r"^## (P\d+)\.", ledger, re.M)}
order = sorted(sections.values()) + [len(ledger)]
text_of = {p: ledger[s:order[order.index(s) + 1]] for p, s in sections.items()}
blocks, cur = {}, None
for line in got:
    m = re.match(r"(P\d+)\s", line)
    cur = m.group(1) if m else cur
    if cur:
        blocks[cur] = blocks.get(cur, "") + line + "\n"
for p, nums in HEADLINES.items():
    in_out = [n for n in nums if n not in blocks.get(p, "")]
    in_ledger = [n for n in nums if n not in text_of.get(p, "").replace("**", "")]
    check(f"{p}: {', '.join(nums)} printed and in its ledger section", not in_out and not in_ledger,
          f"missing from output {in_out}; missing from ledger {in_ledger}")

print()
print("FAILED: " + "; ".join(FAILS) if FAILS else "All checks passed.")
sys.exit(1 if FAILS else 0)
