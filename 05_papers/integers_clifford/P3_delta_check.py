#!/usr/bin/env python3
"""
P3_delta_check.py
Give P3's "gap = 2*Delta" law an INDEPENDENT Delta column and test it honestly.

Run:
    PYTHONIOENCODING=utf-8 /c/ck_venv/lora312/Scripts/python.exe P3_delta_check.py

WHY THIS FILE EXISTS
--------------------
The prior pass (P3_gap_data_table.md / P3_gap_check.py) showed P3's "gap = 2*Delta"
was UNTESTABLE as stated: Delta (the on-site A/B sublattice energy asymmetry) was only
ever back-computed as gap/2, so "gap = 2*Delta" was true by definition. The fix is to
pin Delta INDEPENDENTLY of the measured gap and see whether gap = 2*Delta then holds.

The cleanest independent knob is a FIELD-TUNED BUCKLED HONEYCOMB (silicene, germanene,
stanene). Their two sublattices sit in two planes separated vertically by the buckling
distance d (a measured STRUCTURAL quantity). A perpendicular field E_z raises one plane's
on-site energy relative to the other by e*E_z*d, so the sublattice asymmetry is
    Delta_geo = e * E_z * (d/2)          [INDEPENDENT of the gap: geometry x field knob]
and the naive prediction is
    gap_naive = 2*Delta_geo = e * E_z * d.
This is exactly the formula the silicene literature writes down (E_g = e*E*Delta_0).
So gap = 2*Delta becomes a REAL, non-circular prediction here. We test it.

KEY SUBTLETY (state plainly): in the 2-band gapped-Dirac tight-binding MODEL,
gap = 2*|Delta| is EXACT BY CONSTRUCTION (diagonalize [[Delta, vk],[vk*, -Delta]] ->
E = +-Delta at k=0). So even a perfect match tests the standard MODEL, not TIG; TIG
contributes only the framing "Delta = sublattice asymmetry" (itself the textbook reading
of the honeycomb Hamiltonian, Castro Neto 2009). The one place Delta is a genuine
independent INPUT is the field-tuned case -- and there the naive law is what gets tested.

NO NUMBER HERE IS FABRICATED. Sources + [verify]/[estimate] tags are in
P3_independent_delta_test.md. Output is ASCII-only (spelled 'Delta','Angstrom').
"""

# --------------------------------------------------------------------------
# Physical constants / unit convention
#   Work in "eV per (V/Angstrom)" for field slopes, i.e. e = 1 in units of
#   [eV / (V/Angstrom * Angstrom)]. Then a slope dGap/dE_z has units eV/(V/Angstrom),
#   which numerically equals e*(length in Angstrom). 1 V/Angstrom = 10 V/nm.
# --------------------------------------------------------------------------

def line(): print("-" * 76)

# ==========================================================================
# CASE 1 -- SILICENE, field-tuned  (THE clean independent test)
#   Buckling d and screened gap slope are INDEPENDENT experimental/DFT inputs.
#   Delta is NOT taken as gap/2 here -> the test is non-circular.
# ==========================================================================
# Structural + response numbers (all cited in the .md):
d_Si          = 0.44     # Angstrom, buckling (A-B vertical separation) [Drummond 2012; Ni 2012]
so_gap_Si     = 0.0015   # eV, spin-orbit (Kane-Mele) gap ~1.5 meV [Drummond 2012]
Ez_crit_Si    = 0.020    # V/Angstrom, topological->band-insulator transition (=20 mV/A) [Drummond 2012]

# Slopes dDelta/dE_z (units eV/(V/Angstrom) = e*Angstrom):
dDelta_geo_Si     = d_Si / 2.0   # 0.220  point-geometry: Delta = e*E_z*(d/2)   [INDEPENDENT input]
dDelta_unscr_Si   = 0.56         # 0.554-0.573, Drummond first-order PT, no screening [Drummond 2012]
dDelta_screened_Si= 0.0742       # DFT self-consistent (screened) [Drummond 2012, verbatim]
# Independent cross-check of the SCREENED gap slope from a second DFT study:
dGap_Ni_Si        = 0.157        # ~0.157 e*Angstrom gap slope [Ni 2012, DFT] (~2x dDelta_screened -> consistent)

def report_case1():
    print("[CASE 1] SILICENE, field-tuned -- the clean INDEPENDENT test")
    print("  Buckling d = %.2f Angstrom (measured structure, independent of gap)." % d_Si)
    print("  Field knob E_z is an experimental input.  So:")
    print("    Delta_geo(E_z) = e*E_z*(d/2)        <- INDEPENDENT of the gap")
    print("    gap_naive      = 2*Delta_geo = e*E_z*d   (the literature's E_g = e*E*Delta_0)")
    print()
    # express everything as slopes vs E_z (eV per V/Angstrom):
    gap_naive_slope   = 2 * dDelta_geo_Si          # = d_Si = 0.44
    gap_unscr_slope   = 2 * dDelta_unscr_Si        # = 1.12  (Drummond first-order PT)
    gap_screened_slope= 2 * dDelta_screened_Si     # = 0.148 (Drummond DFT)
    print("  gap-vs-field SLOPES  dGap/dE_z   [eV per (V/Angstrom); 1 V/A = 10 V/nm]:")
    print("    naive geometric   2*e*(d/2) = e*d        = %.3f   <- P3's gap=2*Delta_geo" % gap_naive_slope)
    print("    Drummond 1st-order PT, UNSCREENED        = %.3f   (2 x %.2f)" % (gap_unscr_slope, dDelta_unscr_Si))
    print("    Drummond DFT, SCREENED (real)            = %.3f   (2 x %.4f)" % (gap_screened_slope, dDelta_screened_Si))
    print("    Ni 2012 DFT gap slope (independent check)= %.3f" % dGap_Ni_Si)
    print()
    r_geo   = gap_naive_slope   / gap_screened_slope
    r_unscr = gap_unscr_slope   / gap_screened_slope
    print("  DOES gap = 2*Delta_geo HOLD?")
    print("    real_gap / (2*Delta_geo)      = %.3f / %.3f = %.2f    -> OFF by ~%.0fx (TOO SMALL)"
          % (gap_screened_slope, gap_naive_slope, gap_screened_slope/gap_naive_slope, r_geo))
    print("    Drummond's own factor (unscr/screened)   = %.1fx  ('suppressed by about eight')" % r_unscr)
    print("    => FAIL: the naive gap=2*Delta_geo OVERSHOOTS the real gap by ~3x (point-geometry)")
    print("             to ~8x (full first-order PT). Cause = sublattice polarizability/screening.")
    # worked point at a realistic field:
    Ez = 0.10  # V/Angstrom = 1 V/nm
    print()
    print("  Worked point at E_z = %.2f V/Angstrom (= 1 V/nm):" % Ez)
    print("    Delta_geo        = %.4f eV   -> 2*Delta_geo (predicted gap) = %.1f meV"
          % (dDelta_geo_Si*Ez, 2*dDelta_geo_Si*Ez*1000))
    print("    real DFT gap     = %.1f meV  (screened)"
          % (gap_screened_slope*Ez*1000))
    print("    ratio predicted/real = %.1f  -> gap = 2*Delta_geo is WRONG by that factor."
          % ((2*dDelta_geo_Si*Ez)/(gap_screened_slope*Ez)))
    print("  NOTE: SO gap ~%.1f meV sets a floor; a topological transition at E_z ~ %.0f mV/A"
          % (so_gap_Si*1000, Ez_crit_Si*1000))
    print("        means near zero field the gap does NOT even go through the origin in Delta_geo.")

# ==========================================================================
# CASE 2 -- GERMANENE & STANENE (same buckled series; extends Case 1)
# ==========================================================================
BUCKLED = [
    # name,      d(Angstrom), SO_gap(eV),   note
    ("silicene",  0.44, 0.0015, "d,SO: Drummond/Liu 2011; screened ~3-8x (Case 1)"),
    ("germanene", 0.64, 0.0239, "SO 23.9 meV [Liu 2011]; screening even stronger, gap saturates"),
    ("stanene",   0.85, 0.100,  "SO ~0.1 eV [verify]; d=0.85 A [Molle 2017]"),
]
def report_case2():
    print("[CASE 2] BUCKLED SERIES -- naive geometric gap slope vs reality")
    print("  %-11s %-9s %-11s %-10s" % ("material","d(Ang)","SO gap(eV)","e*d (naive gap slope, eV/(V/A))"))
    for name, d, so, note in BUCKLED:
        print("  %-11s %-9.2f %-11.4f %-10.3f   %s" % (name, d, so, d, note))
    print("  Naive slope grows with buckling (0.44->0.85), but in ALL cases the real DFT")
    print("  gap is suppressed several-fold by the same polarizability screening as silicene")
    print("  [estimate for Ge/Sn factor; hard number pinned only for Si]. Same verdict as Case 1.")

# ==========================================================================
# CASE 3 -- hBN  (large-Delta anchor; on-site Delta from an INDEPENDENT TB fit)
# ==========================================================================
def report_case3():
    print("[CASE 3] hBN -- on-site Delta from tight-binding fits (independent of optical gap)")
    Delta_lo, Delta_hi = 2.3, 2.9   # eV, staggered on-site asymmetry from TB fits [verify]
    eps_B, eps_N = 3.34, -1.40      # eV, a representative fit -> Delta=(eps_B-eps_N)/2 [verify]
    Delta_rep = (eps_B - eps_N)/2.0
    gap_meas = 6.0                  # eV, measured (Cassabois 2016)
    gap_dft  = 4.5                  # eV, typical DFT single-particle gap [approx]
    print("    representative TB on-site: eps_B=+%.2f, eps_N=%.2f eV -> Delta=(eps_B-eps_N)/2=%.2f eV [verify]"
          % (eps_B, eps_N, Delta_rep))
    print("    TB Delta range across fits: %.1f - %.1f eV  -> predicted 2*Delta = %.1f - %.1f eV"
          % (Delta_lo, Delta_hi, 2*Delta_lo, 2*Delta_hi))
    print("    measured optical/QP gap ~%.1f eV ; DFT single-particle gap ~%.1f eV" % (gap_meas, gap_dft))
    print("    2*Delta (~%.1f eV) matches the DFT gap well but UNDER-shoots the ~6 eV measured gap by ~%.0f%%."
          % (2*Delta_rep, 100*(gap_meas-2*Delta_rep)/gap_meas))
    print("    HONEST READING: right scale & sign, but (a) gap=2*Delta is EXACT in the NN 2-band")
    print("    model by construction, and (b) the TB Delta is FIT to the DFT band structure, so")
    print("    the agreement is largely circular; the ~6 eV needs further-neighbor hopping + GW.")

# ==========================================================================
# CASE 4 -- graphene on hBN (substrate-induced Delta reported separately)
# ==========================================================================
def report_case4():
    print("[CASE 4] graphene/hBN -- substrate-induced local mass vs actual gap")
    print("    Local sublattice mass from the aligned substrate is LARGE, but the absolute")
    print("    moire gap is much smaller (mass sign varies across the moire, averaging down):")
    print("      commensurate/lattice-matched DFT gap ~50 meV [Giovannetti 2007]")
    print("      observed (incommensurate, aligned)  ~30 meV [Hunt 2013; many-body enhanced]")
    print("      local max mass term  >>  absolute gap  [Jung 2015, origin-of-gaps]")
    print("    => 'gap = 2*Delta_local' FAILS here: the gap is set by moire averaging, not 2*Delta.")

# ==========================================================================
# CASE 5 -- MoS2 / TMDs  (honest breakdown of the 2-band picture)
# ==========================================================================
def report_case5():
    print("[CASE 5] MoS2 / TMDs -- the simple gap=2*Delta picture does NOT apply")
    print("    monolayer MoS2 direct gap ~1.8 eV [Mak 2010]; but the band edges are Mo 4d")
    print("    orbitals (not a single pz per site) and SOC splits the valence band by ~0.15 eV")
    print("    [Zhu 2011; Xiao 2012]. The 2x2 [[Delta,vk],[vk*,-Delta]] model is not the right")
    print("    Hamiltonian, so no clean independent-Delta test exists. Flagged, not scored.")

def main():
    print("=" * 76)
    print("P3 -- 'gap = 2*Delta' with an INDEPENDENT Delta column, tested honestly")
    print("=" * 76)
    print()
    print("The model identity (all the prior verify script actually asserted):")
    print("  diagonalize [[Delta, vk],[vk*, -Delta]] -> E=+-Delta at k=0 -> gap=2|Delta|, EXACT.")
    print("  True for ANY Delta, so it tests the MODEL, never TIG. TIG only adds the label")
    print("  'Delta = sublattice asymmetry' (already the textbook reading, Castro Neto 2009).")
    print("  The ONLY non-circular test is where Delta is an independent INPUT -> below.")
    print()
    line(); report_case1()
    print(); line(); report_case2()
    print(); line(); report_case3()
    print(); line(); report_case4()
    print(); line(); report_case5()

    print()
    print("=" * 76)
    print("HONEST VERDICT")
    print("=" * 76)
    print("  * Field-tuned silicene is the one CLEAN independent test (Delta = e*E_z*d/2 set by")
    print("    measured buckling d and the field knob, NOT by the gap). Result: the naive")
    print("    gap = 2*Delta_geo OVERSHOOTS the real gap by ~3x (point-geometry) to ~8x")
    print("    (Drummond's first-order PT). gap=2*Delta is rescued ONLY by using the SCREENED")
    print("    effective Delta_eff = gap/2 -- i.e. back to the circular identity. The real")
    print("    physics (sublattice polarizability, factor ~3-8) is exactly what TIG does NOT")
    print("    supply. So P3's law FAILS as an independent prediction here.")
    print("  * hBN: 2*Delta from independent TB fits (~4.6-5.8 eV) is the right scale but the")
    print("    match is model-imposed (gap=2*Delta exact) and partly circular (Delta fit to DFT).")
    print("  * graphene/hBN: gap << 2*(local mass) -- moire averaging, law fails.")
    print("  * MoS2/TMDs: multi-orbital + SOC; 2-band gap=2*Delta not applicable (flagged).")
    print("  ------------------------------------------------------------------------------")
    print("  WHAT IT ESTABLISHES FOR P3:")
    print("    P3 is a RESTATEMENT of the standard gapped-Dirac tight-binding model. Its 'gap")
    print("    = 2*Delta' is an exact model identity, not a TIG prediction. Where Delta is an")
    print("    independent input (field-tuned silicene) the *naive* law is quantitatively")
    print("    WRONG (screening, 3-8x); where it 'works' (hBN) the success belongs to the")
    print("    textbook model and is partly circular. TIG contributes only framing.")
    print("    STATUS: HONEST NEGATIVE -- P3 as a falsifiable TIG law is not supported;")
    print("    it survives only as a re-labeling of the standard model.")
    print("=" * 76)

if __name__ == "__main__":
    main()
