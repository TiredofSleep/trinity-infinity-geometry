"""
TIG validation harness — main entry point.

Runs three things:
  1. Catalan constant baseline (convergent Dirichlet series sanity check)
  2. BSD balance equation for documented low-rank curves (11a1, 37a1, 389a1)
  3. Conceptual D-H balance defect schematic (saved to plots/)

Exit codes:
  0 = all tests passed
  1 = at least one test failed (review output)
  2 = unexpected error during execution

Run with:
  python run_validation.py            # full output
  python run_validation.py --quiet    # concise output
"""

import sys
import traceback
from pathlib import Path

# Make src/ importable
sys.path.insert(0, str(Path(__file__).parent))

from src.catalan import verify_catalan
from src.bsd import load_curves, verify_curve, report as report_bsd
from src.plots import make_balance_defect_schematic


def run_catalan_test(quiet: bool = False) -> bool:
    """Test 1: Catalan's constant via convergent series."""
    if not quiet:
        print()
        print("=" * 70)
        print("TEST 1: Catalan's constant via Dirichlet beta")
        print("=" * 70)
    passed, computed, known, error = verify_catalan(tolerance=1e-5)
    if not quiet:
        print(f"  Computed G = beta(2): {computed:.10f}")
        print(f"  Known value:          {known:.10f}")
        print(f"  Absolute error:       {error:.2e}")
        print(f"  Status: {'PASS' if passed else 'FAIL'}")
    elif passed:
        print(f"  Catalan G: PASS (err={error:.2e})")
    else:
        print(f"  Catalan G: FAIL (err={error:.2e})")
    return passed


def run_bsd_tests(quiet: bool = False) -> bool:
    """Test 2: BSD balance for documented low-rank curves."""
    if not quiet:
        print()
        print("=" * 70)
        print("TEST 2: BSD balance equation (rank 0, 1, 2 curves)")
        print("=" * 70)

    data_path = Path(__file__).parent / "data" / "elliptic_curves.json"
    curves = load_curves(data_path)

    all_passed = True
    for label, curve in curves.items():
        try:
            result = verify_curve(curve, tolerance=1e-3)
            if not quiet:
                report_bsd(result, verbose=True)
                print()
            else:
                marker = "PASS" if result["passed"] else "FAIL"
                print(f"  BSD {label} (rank {result['rank']}): {marker} "
                      f"(ratio={result['ratio']:.6f})")
            if not result["passed"]:
                all_passed = False
        except NotImplementedError as e:
            print(f"  BSD {label}: SKIPPED — {e}")
        except Exception as e:
            print(f"  BSD {label}: ERROR — {e}")
            all_passed = False

    # Demonstrate the scope guard for rank >= 3
    if not quiet:
        print("  -- Rank >= 3 scope guard demonstration --")
    try:
        from src.bsd import BSDInputs
        fake_rank3 = BSDInputs(
            label="5077a1", rank=3, L_leading=1.0, Omega=1.0, R=1.0,
            sha=1, tamagawa=1, torsion=1, lmfdb_url="N/A",
        )
        verify_curve(fake_rank3)
        print("  ERROR: rank-3 verification did not raise NotImplementedError")
        all_passed = False
    except NotImplementedError:
        if not quiet:
            print("  Correctly refused rank-3 verification (NotImplementedError raised).")
        else:
            print("  BSD rank-3 guard: PASS")

    return all_passed


def run_plot_generation(quiet: bool = False) -> bool:
    """Test 3: Generate the D-H balance defect schematic."""
    if not quiet:
        print()
        print("=" * 70)
        print("TEST 3: Generate D-H balance defect schematic (conceptual)")
        print("=" * 70)
    output_path = Path(__file__).parent / "plots" / "dh_balance_defect_schematic.png"
    try:
        saved = make_balance_defect_schematic(output_path)
        if saved.exists():
            size = saved.stat().st_size
            if not quiet:
                print(f"  Saved schematic: {saved}")
                print(f"  File size: {size} bytes")
                print("  Status: PASS")
            else:
                print(f"  D-H schematic: PASS (saved to {saved.name})")
            return True
        else:
            print(f"  D-H schematic: FAIL (file not created)")
            return False
    except Exception as e:
        print(f"  D-H schematic: ERROR — {e}")
        traceback.print_exc()
        return False


def main():
    quiet = "--quiet" in sys.argv

    print("TIG validation harness")
    print("Purpose: clean, reproducible numerical checks. No fabrication.")

    try:
        passed = {
            "catalan":    run_catalan_test(quiet),
            "bsd":        run_bsd_tests(quiet),
            "plot":       run_plot_generation(quiet),
        }
    except Exception:
        traceback.print_exc()
        return 2

    print()
    print("=" * 70)
    print("Summary")
    print("=" * 70)
    for name, ok in passed.items():
        print(f"  {name:10s}: {'PASS' if ok else 'FAIL'}")

    return 0 if all(passed.values()) else 1


if __name__ == "__main__":
    sys.exit(main())
