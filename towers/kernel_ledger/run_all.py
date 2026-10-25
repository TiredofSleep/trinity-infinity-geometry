"""run_all.py -- runs every check in kernel_ledger/; exits nonzero if any fails. Run from inside kernel_ledger/.
Needs ../binary_magic/ beside it (four_in_five.py and friends read its squares). Under a minute or two in all.
fourier_fresh.py is re-scored from its saved halves ("merge"); the full run takes tens of minutes."""
import os, subprocess, sys, time
ENV = dict(os.environ, PYTHONIOENCODING="utf-8")
SCRIPTS = ["ledger_tests.py", "four_in_five.py", "eccentric.py", "weighted.py", "digit_filter.py", "digit_rank.py",
           "fourier_fresh.py merge", "robustness/zero_audit.py"]
bad = 0
for s in SCRIPTS:
    s, *args = s.split()
    d, f = os.path.split(s)
    t = time.time()
    r = subprocess.run([sys.executable, f, *args], cwd=d or ".", capture_output=True, text=True, env=ENV)
    ok = r.returncode == 0
    bad += not ok
    last = [l for l in r.stdout.strip().splitlines() if l.strip()][-1:] or ["(no output)"]
    print(f"{'PASS' if ok else 'FAIL'}  {s} {' '.join(args)}  ({time.time() - t:.1f}s)  {last[0][:100]}")
    if not ok:
        print(r.stdout[-800:], r.stderr[-800:])
print("ALL GREEN" if not bad else f"{bad} FAILED")
sys.exit(bad)
