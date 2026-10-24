"""run_all.py — runs every check in magic_sets/; exits nonzero if any fails."""
import subprocess, sys, time, os
ENV = dict(os.environ, PYTHONIOENCODING="utf-8")
SCRIPTS = ["validate.py", "stars.py", "verify_ms5_16.py", "verify_star.py", "graph_star.py", "export_sets.py",
           "split_test.py", "critical_check.py", "game_use.py", "independent_star_check.py",
           "waegell_stars.py 3 4 5 6", "waegell_realize.py 4 5 6", "tolerance_check.py",
           "lower_bound4.py 5 14 4", "lower_bound5.py 5 14 4", "l4_calibrate.py"]
bad = 0
for s in SCRIPTS:
    s, *args = s.split()
    t = time.time(); r = subprocess.run([sys.executable, s, *args], capture_output=True, text=True, env=ENV)
    ok = r.returncode == 0; bad += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {s} {' '.join(args)}  ({time.time() - t:.1f}s)")
    if not ok: print(r.stdout[-800:], r.stderr[-800:])
print("ALL GREEN" if not bad else f"{bad} FAILED"); sys.exit(bad)
