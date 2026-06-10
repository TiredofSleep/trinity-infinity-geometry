#!/bin/bash
# Re-run every verification script and check exit code + key outputs.
# Triggered by Brayden 2026-04-29: "double check all the work on the repo".
set +e

PY=/c/ck_venv/lora312/Scripts/python.exe
DIR="$(dirname "$0")"
PASS=0
FAIL=0
ERRORS=()

run_one() {
    local script="$1"
    local check_string="$2"
    local out
    echo "==== $script ===="
    out=$("$PY" "$DIR/$script" 2>&1)
    local rc=$?
    if [ $rc -ne 0 ]; then
        echo "  FAIL: exit code $rc"
        FAIL=$((FAIL+1))
        ERRORS+=("$script: exit $rc")
        return
    fi
    if [ -n "$check_string" ]; then
        if echo "$out" | grep -q "$check_string"; then
            echo "  PASS: contains '$check_string'"
            PASS=$((PASS+1))
        else
            echo "  FAIL: missing '$check_string'"
            FAIL=$((FAIL+1))
            ERRORS+=("$script: missing '$check_string'")
        fi
    else
        echo "  PASS (no string check)"
        PASS=$((PASS+1))
    fi
}

# Per-script expected output strings
run_one "f1_so7_singlet_bilinear.py" "All 7 verified"
run_one "f1_f10_field_check.py" "TIG visits THREE different quadratic fields"
run_one "f2_bb_coupling_sharpening.py" "F2 STATUS: SHARPENED"
run_one "f3_galois_alpha_uniqueness.py" "x^2 - 2x - 2 = 0"
run_one "f5a_universality_scan.py" "STRATEGY A: H/Br = 1+sqrt(3) UNIVERSAL"
run_one "f8_jacobian_alpha_half.py" "LINEARLY STABLE"
run_one "f8_pslq_deeper.py" "VERIFIED at 100 digits"
run_one "f9_lmfdb_depth_analysis.py" "Stern-Brocot depth DECREASES as rank INCREASES"
run_one "f10_i_action_descent.py" "is JUSTIFIED"
run_one "f_cross_depth2_primitives.py" "Five frontiers, ONE algebraic primitive"
run_one "f_depth3_primitives.py" "WOBBLE prime 11"
run_one "f_field_match_71.py" "SQUAREFREE PARTS MATCH"
run_one "harmony_complementarity.py" "TSML's HARMONY = sink"
run_one "m_invariance_check.py" "M-only"
run_one "alpha_by_size.py" "FULLY ASSOCIATIVE"

echo ""
echo "================================="
echo "VERIFICATION SUMMARY"
echo "================================="
echo "PASSED: $PASS"
echo "FAILED: $FAIL"
if [ $FAIL -gt 0 ]; then
    echo ""
    echo "Errors:"
    for e in "${ERRORS[@]}"; do
        echo "  - $e"
    done
    exit 1
fi
echo "ALL VERIFICATION SCRIPTS PASS."
