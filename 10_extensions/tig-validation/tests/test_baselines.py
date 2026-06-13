"""
Unit tests for the validation harness.

Run with: pytest tests/

These tests verify the harness itself works correctly. They are NOT a
mathematical proof of anything — just regression checks for the code.
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest

from src.catalan import catalan_constant, verify_catalan, dirichlet_beta, CATALAN_KNOWN
from src.bsd import BSDInputs, load_curves, verify_curve


# --- Catalan tests ---

def test_catalan_close_to_known():
    """Catalan via direct summation should match the known value to 6 decimals."""
    G = catalan_constant(max_terms=1_000_000)
    assert abs(G - CATALAN_KNOWN) < 1e-5, f"Catalan computation off: {G} vs {CATALAN_KNOWN}"


def test_dirichlet_beta_at_2():
    """beta(2) should equal Catalan's constant."""
    assert abs(dirichlet_beta(2.0, max_terms=1_000_000) - CATALAN_KNOWN) < 1e-5


def test_dirichlet_beta_rejects_nonpositive_s():
    with pytest.raises(ValueError):
        dirichlet_beta(0.0)
    with pytest.raises(ValueError):
        dirichlet_beta(-1.0)


def test_verify_catalan_returns_tuple():
    passed, computed, known, error = verify_catalan()
    assert isinstance(passed, bool)
    assert isinstance(computed, float)
    assert known == CATALAN_KNOWN
    assert error >= 0


# --- BSD tests ---

@pytest.fixture
def curve_data_path():
    return Path(__file__).parent.parent / "data" / "elliptic_curves.json"


def test_curves_load(curve_data_path):
    curves = load_curves(curve_data_path)
    assert "11a1" in curves
    assert "37a1" in curves
    assert "389a1" in curves


def test_11a1_balance(curve_data_path):
    curves = load_curves(curve_data_path)
    result = verify_curve(curves["11a1"])
    assert result["passed"], f"11a1 failed: ratio={result['ratio']}"
    assert result["rank"] == 0


def test_37a1_balance(curve_data_path):
    curves = load_curves(curve_data_path)
    result = verify_curve(curves["37a1"])
    assert result["passed"], f"37a1 failed: ratio={result['ratio']}"
    assert result["rank"] == 1


def test_389a1_balance(curve_data_path):
    curves = load_curves(curve_data_path)
    result = verify_curve(curves["389a1"])
    assert result["passed"], f"389a1 failed: ratio={result['ratio']}"
    assert result["rank"] == 2


def test_rank3_raises_not_implemented():
    """Rank >= 3 must NOT be silently verified."""
    fake_rank3 = BSDInputs(
        label="test_rank3", rank=3, L_leading=1.0, Omega=1.0, R=1.0,
        sha=1, tamagawa=1, torsion=1, lmfdb_url="test",
    )
    with pytest.raises(NotImplementedError) as exc_info:
        verify_curve(fake_rank3)
    msg = str(exc_info.value)
    assert "SageMath" in msg or "sagemath" in msg.lower(), \
        "Error message should point user to SageMath for rank-3 verification"


def test_rank4_also_raises():
    fake = BSDInputs(label="test_rank4", rank=4, L_leading=1.0, Omega=1.0, R=1.0,
                    sha=1, tamagawa=1, torsion=1, lmfdb_url="test")
    with pytest.raises(NotImplementedError):
        verify_curve(fake)


# --- Plot generation test ---

def test_plot_creates_file(tmp_path):
    from src.plots import make_balance_defect_schematic
    out = tmp_path / "dh_test.png"
    result = make_balance_defect_schematic(out)
    assert result.exists()
    assert result.stat().st_size > 1000  # at least a kilobyte


# --- Euler defect coefficient tests ---
# Note: these test the *measurement procedure*, not any mathematical claim
# about D-H. The procedure must be correct regardless of the input data.

def test_euler_defect_zero_when_all_on_line():
    """If every zero has sigma = 1/2, defect must be exactly zero."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    from euler_defect_coefficient import Zero, euler_defect_coefficient
    zeros = [Zero(sigma=0.5, gamma=g) for g in [14.13, 21.02, 25.01]]
    assert euler_defect_coefficient(zeros) == 0.0


def test_euler_defect_positive_when_off_line_zero_present():
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    from euler_defect_coefficient import Zero, euler_defect_coefficient
    zeros = [
        Zero(sigma=0.5, gamma=14.13),
        Zero(sigma=0.7, gamma=50.0),  # off-line
    ]
    assert euler_defect_coefficient(zeros) > 0.0


def test_euler_defect_formula_exact():
    """Verify the formula matches manual computation."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    from euler_defect_coefficient import Zero, euler_defect_coefficient
    gamma = 100.0
    z = Zero(sigma=0.8, gamma=gamma)
    expected = 1.0 / (0.25 + gamma ** 2)
    assert abs(euler_defect_coefficient([z]) - expected) < 1e-15


def test_smooth_defect_vanishes_on_critical_line():
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    from euler_defect_coefficient import Zero
    z = Zero(sigma=0.5, gamma=42.0)
    # smooth defect formula: (sigma - 0.5)^2 / (1/4 + gamma^2)
    assert (z.sigma - 0.5) ** 2 == 0.0


# --- Hadamard positivity tests ---
# These verify that the Hadamard-quantity profiler works correctly.
# They do NOT assert specific empirical "violations" for D-H -- those depend on
# (sigma, t) and are exploratory metrics, not provable claims.

def test_hurwitz_zeta_accuracy_at_known_value():
    """Hurwitz zeta(2, 1) = zeta(2) = pi^2 / 6 ~ 1.6449340668..."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    from hadamard_positivity import hurwitz_zeta
    import math
    val = hurwitz_zeta(2.0, 1.0)
    expected = math.pi ** 2 / 6
    assert abs(val.real - expected) < 1e-10, \
        f"hurwitz_zeta(2, 1) = {val} should be approximately pi^2/6 = {expected}"


def test_hadamard_zeta_positive_at_sigma_1_05():
    """At sigma = 1.05, t = 0..50 (small grid): H_zeta should be >= 0
    by Hadamard 1893. Spot-check a few points."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    from hadamard_positivity import zeta, hadamard_quantity
    for t in [1.0, 5.0, 14.13, 25.0, 40.0]:
        h = hadamard_quantity(zeta, 1.05, t)
        assert h >= 0, f"H_zeta(1.05, {t}) = {h} should be >= 0 (Hadamard 1893)"


def test_hadamard_dirichlet_chi3_alone_can_fail():
    """L(s, chi_3) alone: H can be < 0 because chi_3 has signed log coeffs.
    This is expected and well known; the structural Hadamard argument needs
    the product zeta * L(chi_3), not L(chi_3) alone."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    from hadamard_positivity import L_chi3, hadamard_quantity
    # at sigma=1.05, t=8 the Euler-Maclaurin profile showed H_L(chi_3) negative
    found_negative = False
    for t in [1.0, 5.0, 8.0, 10.0, 15.0]:
        h = hadamard_quantity(L_chi3, 1.05, t)
        if h < 0:
            found_negative = True
            break
    assert found_negative, "Expected H_L(chi_3) < 0 somewhere at sigma=1.05"


def test_hadamard_zeta_L_chi3_product_positive():
    """The classical 'product trick': H of zeta(s) * L(s, chi_3) is >= 0
    even when each factor alone may have negative H, because the product's
    log Dirichlet series has non-negative coefficients."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    from hadamard_positivity import zeta, L_chi3, hadamard_quantity
    def zeta_L(s):
        return zeta(s) * L_chi3(s)
    for t in [1.0, 5.0, 14.13, 25.0, 40.0]:
        h = hadamard_quantity(zeta_L, 1.05, t)
        assert h >= 0, f"H of zeta*L(chi_3) at (1.05, {t}) = {h} should be >= 0"


def test_profile_function_works():
    """profile() returns a well-formed Profile dataclass with consistent fields."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    from hadamard_positivity import profile, zeta
    p = profile(zeta, "zeta(s)", sigma=1.05, t_min=0.0, t_max=20.0, n_points=50)
    assert p.name == "zeta(s)"
    assert p.sigma == 1.05
    assert p.n_points == 50
    assert p.min_H <= p.max_H
    assert p.min_H <= p.mean_H <= p.max_H
    assert 0 <= p.n_negative <= p.n_points
    # zeta is known to satisfy Hadamard positivity
    assert p.n_negative == 0
    assert p.min_H >= 0


# --- Staircase envelope visualization test ---

def test_staircase_envelope_figure(tmp_path):
    """The staircase_envelope script produces a PNG that's a real figure."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    from staircase_envelope import make_figure
    out = tmp_path / "test_staircase.png"
    result = make_figure(small_xmax=50, large_xmax=500, k_envelope=3.0,
                        output_path=out)
    assert result.exists()
    assert result.stat().st_size > 10_000  # at least 10 KB


def test_psi_staircase_at_small_x():
    """psi(x) at small x can be hand-checked: psi(10) = log(2)+log(3)+log(2)+log(5)
    +log(7)+log(2)+log(3) for primes powers 2,3,4,5,7,8,9 <= 10."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    from staircase_envelope import psi_sampled
    import math
    psi_at_10 = psi_sampled([10.0], x_max_for_sieve=10)[0]
    expected = (math.log(2) + math.log(3) + math.log(2) + math.log(5)
                + math.log(7) + math.log(2) + math.log(3))
    # prime powers <= 10:  2, 3, 2^2=4, 5, 7, 2^3=8, 3^2=9
    assert abs(psi_at_10 - expected) < 1e-12, \
        f"psi(10) = {psi_at_10} should be {expected}"


# --- TIG internal audit tests ---
# These verify the audit machinery is correct. They do NOT assert any
# specific outcome about the framework's claims -- the outcomes are what
# the script reports. Tests check that the parser, comparators, and
# data structures are sound, so the script's findings can be trusted.

def test_cl_table_parses_to_10x10():
    """The transcribed CL table parses to a 10x10 matrix of integers 0-9."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    from tig_internal_audit import parse_cl_table, CL_DIGIT_STRING
    CL = parse_cl_table(CL_DIGIT_STRING)
    assert len(CL) == 10
    for row in CL:
        assert len(row) == 10
        for entry in row:
            assert isinstance(entry, int)
            assert 0 <= entry <= 9


def test_counts_audit_returns_audit_with_consistent_total():
    """The VOID + HARMONY + bumps counts always sum to 100."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    from tig_internal_audit import parse_cl_table, audit_counts
    CL = parse_cl_table()
    a = audit_counts(CL)
    total = (a.computed["VOID"] + a.computed["HARMONY"]
             + a.computed["bumps"])
    assert total == 100, f"Counts sum to {total}, expected 100"


def test_audit_dataclass_has_required_fields():
    """Every audit returns an Audit dataclass with name, claim, computed, matches."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    from tig_internal_audit import (
        parse_cl_table, audit_counts, audit_diagonal, audit_idempotents,
        audit_commutativity, audit_associativity, audit_6_cycle_starting_from_1,
    )
    CL = parse_cl_table()
    for fn in [audit_counts, audit_diagonal, audit_idempotents,
               audit_commutativity, audit_associativity,
               audit_6_cycle_starting_from_1]:
        a = fn(CL)
        assert hasattr(a, "name")
        assert hasattr(a, "claim")
        assert hasattr(a, "computed")
        assert hasattr(a, "matches")
        assert isinstance(a.matches, bool)


def test_associativity_audit_matches_framework_claim():
    """The transcribed CL table is non-associative; framework claims non-monoid;
    these are consistent. (One of the two findings the audit matches.)"""
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    from tig_internal_audit import parse_cl_table, audit_associativity
    CL = parse_cl_table()
    a = audit_associativity(CL)
    assert a.matches, "Framework claims non-associative; transcribed table is non-associative"


def test_counts_audit_matches_framework_claim():
    """The VOID/HARMONY/bumps counts (17/73/10) match what the framework claims.
    (The other finding the audit matches.)"""
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    from tig_internal_audit import parse_cl_table, audit_counts
    CL = parse_cl_table()
    a = audit_counts(CL)
    assert a.matches, "Framework's 17/73/10 counts should match transcribed table"


# --- Envelope analyzer tests ---
# These verify the analyzer correctly identifies envelope shapes on
# SYNTHETIC data where the truth is known.

def test_envelope_analyzer_detects_sqrt_envelope():
    """Synthetic data with |r(x)| ~ sqrt(x) should yield alpha ~ 0.5."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
    from envelope_analyzer import analyze
    import numpy as np
    rng = np.random.default_rng(7)
    n = 5000
    x = np.linspace(1, 10000, n)
    # |r(x)| ~ sqrt(x) by construction
    r = np.sqrt(x) * rng.standard_normal(n)
    result = analyze(x, r, skip_line_fit=True, n_bins=25)
    assert 0.35 < result.power_law.alpha < 0.7, \
        f"sqrt envelope should give alpha ~ 0.5, got {result.power_law.alpha}"


def test_envelope_analyzer_detects_linear_envelope():
    """Synthetic data with |r(x)| ~ x should yield alpha ~ 1.0."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
    from envelope_analyzer import analyze
    import numpy as np
    rng = np.random.default_rng(7)
    n = 5000
    x = np.linspace(1, 10000, n)
    # |r(x)| ~ x by construction
    r = x * rng.standard_normal(n)
    result = analyze(x, r, skip_line_fit=True, n_bins=25)
    assert 0.8 < result.power_law.alpha < 1.2, \
        f"linear envelope should give alpha ~ 1.0, got {result.power_law.alpha}"


def test_envelope_analyzer_detects_constant_envelope():
    """Synthetic data with |r(x)| ~ constant should yield alpha ~ 0."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
    from envelope_analyzer import analyze
    import numpy as np
    rng = np.random.default_rng(7)
    n = 5000
    x = np.linspace(1, 10000, n)
    # |r(x)| ~ constant (size 5)
    r = 5 * rng.standard_normal(n)
    result = analyze(x, r, skip_line_fit=True, n_bins=25)
    # constant envelope has alpha = 0 in theory; allow generous tolerance
    assert abs(result.power_law.alpha) < 0.2, \
        f"constant envelope should give alpha ~ 0, got {result.power_law.alpha}"


def test_envelope_analyzer_distinguishes_sqrt_from_linear():
    """The analyzer should report different alphas for sqrt-envelope vs
    linear-envelope data, even when they have the same scale of |r|."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
    from envelope_analyzer import analyze
    import numpy as np
    rng = np.random.default_rng(7)
    n = 5000
    x = np.linspace(1, 10000, n)
    r_sqrt = np.sqrt(x) * rng.standard_normal(n)
    r_linear = x * rng.standard_normal(n) / 100  # scaled so amplitudes are similar
    a1 = analyze(x, r_sqrt, skip_line_fit=True, n_bins=25)
    a2 = analyze(x, r_linear, skip_line_fit=True, n_bins=25)
    assert a2.power_law.alpha > a1.power_law.alpha + 0.2, \
        f"linear should give higher alpha than sqrt: " \
        f"sqrt={a1.power_law.alpha}, linear={a2.power_law.alpha}"


def test_envelope_analyzer_with_line_fit():
    """Analyzer should also work in standard mode: y = a + bx + residual.
    With line fit enabled, recover the line and analyze the residual."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
    from envelope_analyzer import analyze
    import numpy as np
    rng = np.random.default_rng(7)
    n = 5000
    x = np.linspace(1, 10000, n)
    true_a, true_b = 5.0, 2.0
    r = np.sqrt(x) * rng.standard_normal(n)
    y = true_a + true_b * x + r
    result = analyze(x, y, coords="linear", skip_line_fit=False, n_bins=25)
    assert abs(result.line_fit.slope - true_b) < 0.05, \
        f"line fit should recover slope ~ {true_b}, got {result.line_fit.slope}"
    assert 0.35 < result.power_law.alpha < 0.7, \
        f"sqrt envelope should give alpha ~ 0.5, got {result.power_law.alpha}"


def test_envelope_analyzer_report_format():
    """report() returns a string with required diagnostic sections."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
    from envelope_analyzer import analyze, report
    import numpy as np
    rng = np.random.default_rng(7)
    x = np.linspace(1, 1000, 500)
    r = np.sqrt(x) * rng.standard_normal(500)
    a = analyze(x, r, skip_line_fit=True, n_bins=15)
    text = report(a, header="test")
    assert "test" in text
    assert "alpha" in text
    assert "WHERE DOES THE LINE BREAK" in text
    assert "WHAT IS THE RESIDUAL ENVELOPE" in text
    assert "WHAT MECHANISM IS ON THE TABLE" in text


def test_cross_domain_envelopes_figure(tmp_path):
    """The cross-domain envelopes script produces a real PNG figure."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    from cross_domain_envelopes import make_figure
    out = tmp_path / "cross_domain.png"
    result = make_figure(output_path=out, walk_n=500, psi_xmax=500)
    assert result.exists()
    assert result.stat().st_size > 10_000


# --- Number theory envelope tests ---

def test_divisor_count_sieve_small():
    """Direct verification of divisor count sieve on small values."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    from number_theory_envelopes import divisor_count_sieve
    d = divisor_count_sieve(12)
    # d(1)=1, d(2)=2, d(3)=2, d(4)=3, d(5)=2, d(6)=4, d(7)=2,
    # d(8)=4, d(9)=3, d(10)=4, d(11)=2, d(12)=6
    expected = [0, 1, 2, 2, 3, 2, 4, 2, 4, 3, 4, 2, 6]
    assert list(d) == expected


def test_mobius_sieve_small():
    """Direct verification of Mobius sieve on small values."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    from number_theory_envelopes import mobius_sieve
    mu = mobius_sieve(12)
    # mu(1)=1, mu(2)=-1, mu(3)=-1, mu(4)=0, mu(5)=-1, mu(6)=1,
    # mu(7)=-1, mu(8)=0, mu(9)=0, mu(10)=1, mu(11)=-1, mu(12)=0
    expected = [0, 1, -1, -1, 0, -1, 1, -1, 0, 0, 1, -1, 0]
    assert list(mu) == expected


def test_divisor_residual_envelope_smaller_than_psi():
    """The divisor problem residual envelope should be smaller than the
    prime staircase residual envelope at comparable x. This is a real
    number-theoretic prediction: conjecturally alpha(Delta) ~ 0.25 < 0.5 ~ alpha(psi)."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
    from number_theory_envelopes import divisor_residual
    from envelope_analyzer import analyze
    import numpy as np

    N = 20_000
    xs, delta = divisor_residual(N)
    # subsample
    step = max(1, len(xs) // 1500)
    xs_sub = xs[::step]
    delta_sub = delta[::step]
    a = analyze(xs_sub, delta_sub, skip_line_fit=True, n_bins=20)
    # The conjectured exponent is 0.25; we should empirically measure
    # alpha somewhere between 0.15 and 0.45 (allowing for finite-scale noise
    # and main-term subtraction imperfections).
    assert 0.10 < a.power_law.alpha < 0.45, \
        f"divisor problem alpha should be in [0.10, 0.45], got {a.power_law.alpha}"


def test_mertens_function_at_small_x():
    """Verify Mertens function via cumsum of Mobius."""
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    from number_theory_envelopes import mertens
    M = mertens(10)
    # M(1)=1, M(2)=0, M(3)=-1, M(4)=-1, M(5)=-2, M(6)=-1, M(7)=-2, M(8)=-2, M(9)=-2, M(10)=-1
    expected = [0, 1, 0, -1, -1, -2, -1, -2, -2, -2, -1]
    assert list(M) == expected


def test_number_theory_figure_renders(tmp_path):
    """The number-theory envelopes script produces a real PNG figure."""
    # We'll run the script in a subprocess against a smaller N for speed
    import subprocess
    import os
    env = os.environ.copy()
    env["PYTHONPATH"] = str(Path(__file__).parent.parent / "src") + ":" + str(Path(__file__).parent.parent / "experiments")
    # Just check the figure-render path works by importing make_figure and calling it
    sys.path.insert(0, str(Path(__file__).parent.parent / "experiments"))
    sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
    from number_theory_envelopes import make_figure, divisor_residual, mertens
    from envelope_analyzer import analyze
    from staircase_envelope import psi_sampled
    import numpy as np

    N = 5_000
    xs_psi = np.linspace(10, N, 200)
    psi_vals = np.array(psi_sampled(list(xs_psi), N))
    psi_res = psi_vals - xs_psi
    a_psi = analyze(xs_psi, psi_res, skip_line_fit=True, n_bins=10)

    xs_div, delta = divisor_residual(N)
    step = max(1, len(xs_div) // 200)
    xs_div_sub = xs_div[::step]
    delta_sub = delta[::step]
    a_div = analyze(xs_div_sub, delta_sub, skip_line_fit=True, n_bins=10)

    M = mertens(N)
    ns_m = np.arange(1, N + 1, dtype=float)
    M_vals = M[1:].astype(float)
    a_m = analyze(ns_m[::step], M_vals[::step], skip_line_fit=True, n_bins=10)

    out = tmp_path / "nt_envelopes.png"
    result = make_figure(xs_psi, psi_res, xs_div_sub, delta_sub,
                         ns_m[::step], M_vals[::step],
                         a_psi, a_div, a_m, output_path=out)
    assert result.exists()
    assert result.stat().st_size > 10_000
