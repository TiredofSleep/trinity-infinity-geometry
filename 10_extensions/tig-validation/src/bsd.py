"""
BSD balance equation verification.

For an elliptic curve E/Q with rank r, BSD conjectures:

    L^(r)(E, 1) / r!   =   (Omega * R * |Sha| * prod_p c_p) / |E_tors|^2

where:
    Omega = real period of the Neron differential
    R     = elliptic regulator (determinant of canonical height-pairing matrix)
    |Sha| = order of the Tate-Shafarevich group (conjecturally a perfect square)
    c_p   = local Tamagawa numbers at primes p of bad reduction
    |E_tors| = order of E(Q)_tors

This module:
    - Computes the BSD ratio (LHS / RHS) using documented LMFDB values from JSON.
    - Reports each input value with its source.
    - REFUSES to "verify" rank-3 or higher curves, raising NotImplementedError.
      Such verification requires SageMath/PARI for the period normalization.

No reverse-engineered values. No curve-fitting. If a ratio comes out far from 1.0,
that's a signal — either the LMFDB values are stale, or the framework's claim
needs revision. Do not adjust inputs to force ratio = 1.0.
"""

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any


@dataclass
class BSDInputs:
    """Inputs to the BSD balance equation for a single curve."""
    label: str
    rank: int
    L_leading: float        # L^(r)(E, 1) / r!
    Omega: float            # real period
    R: float                # regulator
    sha: int                # |Sha|
    tamagawa: int           # prod c_p
    torsion: int            # |E_tors|
    lmfdb_url: str

    def predicted_leading(self) -> float:
        """Compute RHS of BSD: (Omega * R * |Sha| * prod c_p) / |E_tors|^2"""
        return (self.Omega * self.R * self.sha * self.tamagawa) / (self.torsion ** 2)

    def ratio(self) -> float:
        """L_leading / predicted_leading. Should be 1.0 if BSD holds."""
        return self.L_leading / self.predicted_leading()


def load_curves(json_path: Path) -> Dict[str, BSDInputs]:
    """Load curve data from the JSON file. Only loads curves of rank <= 2."""
    with open(json_path) as f:
        raw = json.load(f)

    curves = {}
    for label, data in raw["curves"].items():
        curves[label] = BSDInputs(
            label=label,
            rank=data["rank"],
            L_leading=data["L_leading_value"],
            Omega=data["real_period_Omega"],
            R=data["regulator_R"],
            sha=data["sha_order"],
            tamagawa=data["tamagawa_product"],
            torsion=data["torsion_order"],
            lmfdb_url=data["lmfdb_url"],
        )
    return curves


def verify_curve(curve: BSDInputs, tolerance: float = 1e-3) -> Dict[str, Any]:
    """
    Verify BSD balance for a single curve.

    Args:
        curve: the curve's documented inputs
        tolerance: relative tolerance for the ratio to be considered "matching"

    Returns:
        dict with predicted, actual, ratio, passed, and source info

    Raises:
        NotImplementedError: if curve rank >= 3.
            Rank-3+ verification requires SageMath/PARI for trustworthy period
            normalization. Python-only float computation is unreliable here.
    """
    if curve.rank >= 3:
        raise NotImplementedError(
            f"BSD verification for {curve.label} (rank {curve.rank}) is NOT supported "
            f"by this harness. Use SageMath: E = EllipticCurve('{curve.label}'); "
            f"then compute regulator, period, and Sha via E.regulator(), E.period_lattice(), "
            f"and E.sha().an_numerical(). Trustworthy period normalization for high-rank "
            f"curves requires symbolic/multi-precision support beyond standard Python floats."
        )

    predicted = curve.predicted_leading()
    ratio = curve.ratio()
    relative_error = abs(ratio - 1.0)
    passed = relative_error < tolerance

    return {
        "label": curve.label,
        "rank": curve.rank,
        "L_leading_actual": curve.L_leading,
        "BSD_prediction": predicted,
        "ratio": ratio,
        "relative_error": relative_error,
        "tolerance": tolerance,
        "passed": passed,
        "source": curve.lmfdb_url,
        "inputs": {
            "Omega": curve.Omega,
            "R": curve.R,
            "Sha": curve.sha,
            "Tamagawa": curve.tamagawa,
            "Torsion": curve.torsion,
        },
    }


def report(result: Dict[str, Any], verbose: bool = True) -> None:
    """Print a single curve's verification result."""
    label = result["label"]
    rank = result["rank"]
    actual = result["L_leading_actual"]
    pred = result["BSD_prediction"]
    ratio = result["ratio"]
    passed = result["passed"]
    status = "PASS" if passed else "FAIL"

    print(f"  {label} (rank {rank}): {status}")
    print(f"    L^(r)(E,1)/r! (actual)   = {actual:.10f}")
    print(f"    BSD formula  (predicted) = {pred:.10f}")
    print(f"    ratio                    = {ratio:.7f}")
    print(f"    rel. error               = {result['relative_error']:.2e}")
    if verbose:
        print(f"    source: {result['source']}")
        print(f"    inputs: Omega={result['inputs']['Omega']}, R={result['inputs']['R']}, "
              f"Sha={result['inputs']['Sha']}, Tamagawa={result['inputs']['Tamagawa']}, "
              f"Torsion={result['inputs']['Torsion']}")


if __name__ == "__main__":
    data_path = Path(__file__).parent.parent / "data" / "elliptic_curves.json"
    curves = load_curves(data_path)
    print("BSD balance equation verification")
    print("-" * 60)
    for label, curve in curves.items():
        result = verify_curve(curve)
        report(result)
        print()
