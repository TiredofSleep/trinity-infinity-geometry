"""run_all.py — runs every script in clock_and_paradox/; exits nonzero if any fails."""
import subprocess, sys, os
ENV = dict(os.environ, PYTHONIOENCODING="utf-8")
bad = 0
for s in ["channeling_numbers.py", "paradox_map.py", "halving_check.py"]:
    r = subprocess.run([sys.executable, s], capture_output=True, text=True, env=ENV); ok = r.returncode == 0; bad += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {s}")
    if not ok: print(r.stdout[-600:], r.stderr[-600:])
print("ALL GREEN" if not bad else f"{bad} FAILED"); sys.exit(bad)
