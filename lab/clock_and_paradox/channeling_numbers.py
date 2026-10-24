"""
channeling_numbers.py — numbers for a replication of the electron-channeling 'internal clock' dip.

Published claim (Gouanère et al. 2005, AFLB 30:109; Catillon et al. 2008, Found. Phys. 38:659):
~80 MeV electrons along Si <110> (1 um thick); 0-degree transmission dips ~8% within 0.5% of 80.874 MeV/c.
Resonance: the electron passes one atom per clock tick. With de Broglie's clock (frequency m c^2 / h),
time-dilated in the lab, the condition d / v = gamma h / (m c^2) gives  p c = d (m c^2)^2 / (h c).
(Simulations need twice that frequency with half the distance, i.e. zitterbewegung; same momentum.)
"""
import math

mc2 = 0.51099895          # MeV
hc = 1239.84198           # MeV fm
hbar = 6.582119569e-22    # MeV s
h = 4.135667696e-21       # MeV s
e2 = 1.43996              # MeV fm (e^2 / 4 pi eps0)

print("Clock frequencies (correcting an earlier figure of mine):")
print(f"  de Broglie clock  m c^2 / h      = {mc2 / h:.3e} Hz")
print(f"  zitterbewegung    2 m c^2 / h    = {2 * mc2 / h:.3e} Hz")
print(f"  as angular freq.  2 m c^2 / hbar = {2 * mc2 / hbar:.3e} rad/s   <- the '1.5e21' figure is rad/s, not Hz")

def p_res(d_angstrom, n=1):
    return n * d_angstrom * 1e5 * mc2 ** 2 / hc          # MeV/c, n = atoms per clock tick

def lindhard_mrad(Z, d_angstrom, pc_mev):
    return 1e3 * math.sqrt(2 * Z * e2 / (pc_mev * d_angstrom * 1e5))

AXES = [  # (crystal, axis, Z, spacing along the atomic row in angstrom)
    ("Si", "<110>", 14, 5.431 / math.sqrt(2)),
    ("Si", "<100>", 14, 5.431),
    ("Ge", "<110>", 32, 5.658 / math.sqrt(2)),
    ("C (diamond)", "<110>", 6, 3.567 / math.sqrt(2)),
    ("W", "<111>", 74, 3.165 * math.sqrt(3) / 2),
]
print("\nPredicted resonance momenta (n = 1; the dip should move in exact proportion to d):")
print(f"  {'crystal':12s} {'axis':6s} {'d (A)':>7s} {'p_res (MeV/c)':>14s} {'n=2':>8s} {'crit. angle (mrad)':>19s}")
for name, axis, Z, d in AXES:
    p = p_res(d)
    print(f"  {name:12s} {axis:6s} {d:7.3f} {p:14.3f} {p_res(d, 2):8.2f} {lindhard_mrad(Z, d, p):19.2f}")
si = p_res(5.431 / math.sqrt(2))
assert abs(si - 80.874) < 0.05, si
print(f"\nCheck: Si <110> gives {si:.3f} MeV/c, matching the published 80.874.")
print("A muon would need p ~", round(p_res(5.431 / math.sqrt(2)) * (105.6584 / mc2) ** 2 / 1e6, 2),
      "TeV/c for the same resonance, so this test is electrons-only.")
print("\nWhat a replication needs: momentum steps <= 0.1% (the dip sits within 0.5%), beam divergence well"
      " under the ~1 mrad critical angle, 1 um crystals, and at least two different crystals or axes,"
      " so the dip is seen to move with d. A dip that stays put when d changes is a channeling artifact.")
