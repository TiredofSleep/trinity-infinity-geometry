#!/usr/bin/env python3
"""
P3_gap_check.py
Holds the published gap numbers for the P3 "gap = 2*Delta" experiment and prints an
HONEST comparison. Companion to P3_gap_data_table.md and P3_mass_sublattice_skeleton.md.

Run:
    PYTHONIOENCODING=utf-8 /c/ck_venv/lora312/Scripts/python.exe P3_gap_check.py

KEY POINT (do not skip): P3's "gap = 2*Delta" is a HONEYCOMB BAND-STRUCTURE law
(Delta = on-site sublattice energy asymmetry, in eV). It is NOT a superconducting-gap
claim. The BCS ratio 2*Delta/(k_B*T_c) = 3.53 is a DIFFERENT Delta and a DIFFERENT law
(it lives, in this paper set, in P4 -- an explicit FRAME with no ratio law). This script
reports BOTH tables and states plainly what each does and does not test.

Nothing here is fabricated. Superconducting ratios are technique/sample dependent; central
values + ranges + sources are in P3_gap_data_table.md. Cuprate/LSCO points are flagged
[verify] (anisotropic d-wave; a single number is not meaningful).
"""
import statistics as st

BCS_SWAVE = 3.528   # 2*Delta/(k_B*T_c), weak-coupling s-wave  [BCS 1957]
BCS_DWAVE = 4.28    # weak-coupling d-wave reference (cuprates) [Won-Maki 1994]

def line(): print("-" * 74)

# ---------------------------------------------------------------------------
# TABLE A -- superconducting gap ratios 2*Delta/(k_B*T_c)   (REQUESTED; NOT a P3 test)
#   (material, Tc_K, central ratio, (lo, hi) range, note)
# ---------------------------------------------------------------------------
SC = [
    ("Al",        1.2, 3.35, (3.3, 3.4),  "weak coupling ~ BCS"),
    ("Sn",        3.7, 3.55, (3.5, 3.6),  "near BCS"),
    ("In",        3.4, 3.6,  (3.6, 4.1),  "moderate; real spread"),
    ("Nb",        9.3, 3.7,  (2.8, 4.1),  "moderate-strong; wide lit spread"),
    ("Pb",        7.2, 4.3,  (4.1, 4.5),  "STRONG coupling"),
    ("Nb3Sn",    18.0, 4.5,  (4.2, 4.8),  "STRONG coupling A15"),
    ("MgB2 sigma",39.0,4.5,  (4.0, 5.0),  "two-gap: sigma band (strong)"),
    ("MgB2 pi",  39.0, 1.5,  (1.1, 2.0),  "two-gap: pi band (BELOW BCS)"),
    ("YBCO",     92.0, 4.0,  (2.5, 6.0),  "d-wave, anisotropic [verify]"),
    ("Bi2212",   90.0, 7.0,  (5.0, 9.0),  "d-wave; nodal ratio ~8.5"),
    ("LSCO",     38.0, 5.0,  (4.0, 6.0),  "d-wave, doping-dep [verify]"),
]

# Single-gap, s-wave-ish set for statistics (exclude cuprates=d-wave and MgB2-pi=2nd band)
SWAVE_SET = ["Al", "Sn", "In", "Nb", "Pb", "Nb3Sn", "MgB2 sigma"]

# ---------------------------------------------------------------------------
# TABLE B -- P3's ACTUAL domain: honeycomb band gap vs sublattice asymmetry
#   (material, band_gap_eV, note)   Delta_eff column is intentionally absent (see below).
# ---------------------------------------------------------------------------
HONEYCOMB = [
    ("graphene",  0.0,     "A=B, Dirac semimetal -- anchor (0,0)"),
    ("silicene",  0.0015,  "~1.5 meV, SOC (NOT sublattice asymmetry)"),
    ("germanene", 0.024,   "~24 meV, SOC"),
    ("MoS2",      1.8,     "d-orbitals+SOC break simple 2-band picture"),
    ("hBN",       6.0,     "B != N, far anchor"),
]

def main():
    print("=" * 74)
    print("P3 CHECK -- 'gap = 2*Delta', tested honestly against published data")
    print("=" * 74)

    print("\nP3's EXACT claim (P3_mass_sublattice_skeleton.md, verbatim):")
    print('  "the band gap at the Dirac point is exactly 2*Delta, where Delta is the')
    print('   on-site A/B energy difference ... linear in the asymmetry, with slope 2,')
    print('   passing through the origin."')
    print("  -> Delta = SUBLATTICE ASYMMETRY (eV). 'gap' = BAND gap. NOT superconducting.")

    # -- The forced identity (all P3's verify script actually asserts) --------
    line()
    print("[1] The FORM 'gap = 2*Delta' is an exact identity (diagonalize [[D,vk],[vk*,-D]]):")
    gap = lambda D: 2 * abs(D)
    for D in [0.0, 0.5, 1.0, 3.0]:
        assert abs(gap(D) - 2 * D) < 1e-12
        print(f"      gap(Delta={D:>3}) = {gap(D):>4}  (= 2*Delta, exact)")
    print("      -> true by construction for ANY Delta. Not falsifiable as a 'law'.")

    # -- TABLE A: superconducting ratios --------------------------------------
    line()
    print("[2] TABLE A -- superconducting 2*Delta/(k_B*T_c)  [REQUESTED, but NOT a P3 test]")
    print(f"    {'material':<11}{'Tc(K)':>7}{'ratio':>8}   range        note")
    for name, tc, r, (lo, hi), note in SC:
        print(f"    {name:<11}{tc:>7}{r:>8.2f}   {lo:>3.1f}-{hi:<3.1f}    {note}")

    vals = [r for (name, tc, r, rng, note) in SC if name in SWAVE_SET]
    mean = st.mean(vals)
    sd = st.stdev(vals)
    all_ratios = [r for (_n, _t, r, _g, _x) in SC]
    print(f"\n    Stats on s-wave/single-gap set {SWAVE_SET}:")
    print(f"      mean  = {mean:.2f}   (BCS weak-coupling s-wave = {BCS_SWAVE})")
    print(f"      stdev = {sd:.2f}     spread(min..max, this set) = {min(vals):.2f}..{max(vals):.2f}")
    print(f"      mean - BCS = {mean - BCS_SWAVE:+.2f}  (strong-coupling materials pull it UP)")
    print(f"    Full table incl. cuprates & MgB2-pi: ratios span {min(all_ratios):.2f}..{max(all_ratios):.2f}"
          f" (factor ~{max(all_ratios)/min(all_ratios):.0f}).")
    print(f"    Deviation from BCS {BCS_SWAVE} (each material):")
    for name, tc, r, rng, note in SC:
        print(f"      {name:<11} {r:>5.2f}   {r - BCS_SWAVE:+5.2f} vs 3.53   "
              f"{'(d-wave ref 4.28: '+format(r-BCS_DWAVE,'+.2f')+')' if 'd-wave' in note else ''}")
    print("    READING: no universal ratio; 3.53 only for weak-coupling s-wave; NEVER 2.")
    print("             If forced as a 'universal slope-2' law -> data STRAINS/refutes it,")
    print("             but that is a strawman P3 never asserted.")

    # -- TABLE B: honeycomb, P3's real domain ---------------------------------
    line()
    print("[3] TABLE B -- P3's ACTUAL domain: honeycomb band gap (eV) [what WOULD test P3]")
    print(f"    {'material':<11}{'gap(eV)':>9}    note")
    for name, g, note in HONEYCOMB:
        print(f"    {name:<11}{g:>9.4f}    {note}")
    print("    NOTE: the independent Delta_eff column is ABSENT ON PURPOSE.")
    print("          P3 concedes TIG does not supply Delta_eff (skeleton s.4 step 2, s.5).")
    print("          Without an INDEPENDENT Delta_eff, slope-2 is CIRCULAR:")
    print("          setting Delta_eff := gap/2 makes 'slope 2' trivially true.")
    print("          Data confirms only the SIGN (graphene gapless <-> hBN gapped),")
    print("          which P3 already tags [MEASURED]. The quantitative law is untested.")

    # -- VERDICT --------------------------------------------------------------
    print("\n" + "=" * 74)
    print("HONEST VERDICT")
    print("=" * 74)
    print("  * Requested SC ratio table (A): WRONG INSTRUMENT for P3 -- different Delta,")
    print("    different law (superconductivity is P4, an explicit FRAME with no ratio).")
    print("    -> Not support / not neutral / not strain: NOT APPLICABLE to P3.")
    print("  * SC data on its own terms: STRAINS any 'universal single ratio' reading")
    print("    (spans ~1.1 to ~9; =3.53 only for weak-coupling s-wave; never 2).")
    print("  * P3's real claim: the FORM gap=2*Delta is an exact identity (trivially true);")
    print("    the EMPIRICAL slope-2-across-materials law is UNDER-SPECIFIED (no independent")
    print("    Delta_eff) and risks circularity.")
    print("  => DATA DOES NOT YET SUPPORT P3. Status = NOT-YET-TESTABLE / UNDER-SPECIFIED")
    print("     (= P3's own [OPEN] tag), tending STRAINED if forced into the SC framing.")
    print("=" * 74)

if __name__ == "__main__":
    main()
