"""run_all.py — runs every check script in binary_magic/ and order8/; exits nonzero if any fails.
Run from inside binary_magic/. About 12 minutes in all (split_check.py and the code_lens rounds are the slow ones)."""
import subprocess, sys, time, os
SCRIPTS = ["binary_magic.py", "split_check.py", "trefoil_view.py", "knot_check.py", "takemura_cross.py",
           "degree_explained.py", "fourier_check.py", "triad_atlas.py", "fold_proof_check.py",
           "dirac_tower.py", "residue_test.py", "semimagic_test.py", "metasurface_check.py",
           "context_check.py", "quantum_check.py", "mermin_magic.py", "qutrit_grids.py",
           "order8/order8_test.py", "order8/order8_bitbalanced_test.py", "order8/affine_count.py",
           "independent_check.py squares_4x4.json", "fitting_crosscheck.py squares_4x4.json",
           "order8/order8_families.py ../squares_4x4.json fullbinary8_samples.txt",
           "code_lens/code_lens.py", "code_lens/order8_lens.py", "code_lens/antinomy.py",
           "code_lens/fold_mechanism.py", "code_lens/fold_pull.py", "code_lens/fold_needs.py",
           "code_lens/nimm0_coupling.py", "code_lens/void_fold.py", "code_lens/void_fold_check.py",
           "mermin_28.py", "void_lens/void_lens.py", "void_lens/padic_family.py", "void_lens/kernel_voids.py",
           "void_lens/padic_lemma.py", "void_lens/void_lens_check.py",
           "void_lens/applications/void_applications.py"]
ENV = dict(os.environ, PYTHONIOENCODING="utf-8")          # some scripts print symbols a Windows console can't
bad = 0
for s in SCRIPTS:
    s, *args = s.split()
    d, f = os.path.split(s)
    t = time.time()
    r = subprocess.run([sys.executable, f, *args], cwd=d or ".", capture_output=True, text=True, env=ENV)
    ok = r.returncode == 0
    bad += not ok
    print(f"{'PASS' if ok else 'FAIL'}  {s}  ({time.time() - t:.1f}s)")
    if not ok:
        print(r.stdout[-800:], r.stderr[-800:])
print("ALL GREEN" if not bad else f"{bad} FAILED")
sys.exit(bad)
