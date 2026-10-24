"""run_all.py — runs every check in planes_and_mirrors/; exits nonzero if any script errors."""
import subprocess, sys, time, os
ENV = dict(os.environ, PYTHONIOENCODING="utf-8")
SCRIPTS = ["mirror_room.py", "seven_check.py", "mirror_tower.py", "mirror_brake.py", "why_seven_breaks.py", "cube_spheres.py"]
bad = 0
for s in SCRIPTS:
    t = time.time(); r = subprocess.run([sys.executable, s], capture_output=True, text=True, env=ENV)
    ok = r.returncode == 0; bad += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {s}  ({time.time() - t:.1f}s)")
    if not ok: print(r.stdout[-800:], r.stderr[-800:])
print("ALL GREEN" if not bad else f"{bad} FAILED"); sys.exit(bad)
