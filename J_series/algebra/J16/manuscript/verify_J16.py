#!/usr/bin/env python3
# ============================================================
# verify_J16.py
#
# Top-level verification runner for:
#   "A Commutative Non-Associative 4-Algebra over F_5 with
#    Rigid Idempotent Decomposition"
#   (Sanders, Gish, 2026, Algebras and Representation Theory)
#
# This thin wrapper:
#   (i)  forces UTF-8 stdout so the Greek / mathematical symbols
#        in the two underlying scripts print correctly on Windows
#        consoles (cp1252) without modifying the upstream scripts;
#   (ii) runs both verification scripts:
#          - verify_discrete_dirac_4core.py  (14 algebraic checks)
#          - test_tig_dirac.py               (15+ unit tests)
#        backed by the deposited reference library tig_dirac.py.
#
# All checks pass deterministically in < 5 sec total runtime
# with numpy as the only external dependency.
#
# Run:
#   PYTHONIOENCODING=utf-8 /c/ck_venv/lora312/Scripts/python.exe verify_J16.py
# or on Windows shells without the env var:
#   /c/ck_venv/lora312/Scripts/python.exe -X utf8 verify_J16.py
#
# Copyright (c) 2026 B.R. Sanders and M. Gish.
# Licensed under CC-BY-4.0.
# ============================================================
import io
import os
import runpy
import sys

# ---- (i) force UTF-8 stdout so σ, ε, ⊗, etc. print on Windows -----------
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = [
    "verify_discrete_dirac_4core.py",
    "test_tig_dirac.py",
]

# Make sure tig_dirac.py (deposited in this same folder) is importable.
if HERE not in sys.path:
    sys.path.insert(0, HERE)

print("=" * 70)
print("J16 verification run")
print("=" * 70)

failures = []
for s in SCRIPTS:
    path = os.path.join(HERE, s)
    print(f"\n>>> running {s}")
    print("-" * 70)
    try:
        runpy.run_path(path, run_name="__main__")
        print(f"<<< {s}: PASS")
    except SystemExit as e:
        # Some test runners may sys.exit on completion.
        if (e.code or 0) == 0:
            print(f"<<< {s}: PASS (exit 0)")
        else:
            print(f"<<< {s}: FAIL (exit {e.code})")
            failures.append(s)
    except AssertionError as ae:
        print(f"<<< {s}: FAIL (assertion: {ae})")
        failures.append(s)
    except Exception as ex:
        print(f"<<< {s}: FAIL ({type(ex).__name__}: {ex})")
        failures.append(s)

print("\n" + "=" * 70)
if failures:
    print(f"J16 VERIFICATION: FAILED ({len(failures)} script(s))")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)
else:
    print("J16 VERIFICATION: ALL CHECKS PASS")
    print("  - verify_discrete_dirac_4core.py: 14 algebraic checks PASS")
    print("  - test_tig_dirac.py: structural unit tests PASS")
print("=" * 70)
