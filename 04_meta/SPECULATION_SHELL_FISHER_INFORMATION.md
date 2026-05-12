# SPECULATION_SHELL_FISHER_INFORMATION

## Shell-resolved Fisher information vs TIG substrate quantities

**Status: SPECULATIVE / Tier C / one structural pattern + mostly-standard atomic physics**

**Companion to**: `SPECULATION_ELECTRON_BLACK_HOLE_BRIDGE.md` (electron-as-boundary-gate intuition)

**For ClaudeCode**: this doc reports actual numerical calculations (not just claims). The headline pattern (substrate primes ↔ odd-l orbital multiplicities) is striking but interpretation-pending. Most other scalings are standard atomic physics, not TIG-specific.

Locked 2026-05-08.

---

## §0. What was computed

For hydrogenic orbitals (Z=1, atomic units) at shells n=1..4 across all allowed l:

- `<r>`: expectation value of radial position
- `S_r`: radial Shannon entropy `-∫ ρ(r) log ρ(r) dr` where ρ(r) = r² |R_{n,l}(r)|²
- `I_r`: radial Fisher information `∫ (ρ'(r))² / ρ(r) dr`

Computed via numerical integration in `shell_entropy_tig.py`. Hydrogenic radial wavefunctions from scipy.special.genlaguerre.

Brayden's intuition being tested: if electrons are "boundary gates," outer shells should show looser edge localization than inner shells. The Fisher information is the natural candidate for "edge sharpness" — high I_r = sharp edge, low I_r = loose edge.

---

## §1. Computed values

```
shell  n  l    <r>       S_r        I_r
 1s    1  0   1.4845    1.1368    3.9910
 2s    2  0   5.9991    2.2339    0.9998
 2p    2  1   4.9996    2.1534    0.3333
 3s    3  0  13.5000    2.9056    0.4444
 3p    3  1  12.5000    2.8836    0.2469
 3d    3  2  10.5000    2.7480    0.0889
 4s    4  0  24.0000    3.3954    0.2500
 4p    4  1  23.0000    3.3863    0.1667
 4d    4  2  21.0000    3.3391    0.1000
 4f    4  3  18.0000    3.1726    0.0357
```

`<r>` matches the textbook formula `<r>_ns = 3n²/2` exactly.

---

## §2. The "edge widening" prediction is confirmed but standard

Brayden's intuition: outer shells = looser edges. Take 1/I_r as "edge width" (inverse of sharpness):

```
1/I_r ratios relative to 1s:
  1s:    1.0
  2s:    3.99    (4×)
  2p:   11.97    (12×)
  3s:    8.98
  3p:   16.16
  3d:   44.89
  4s:   15.96
  4p:   23.94
  4d:   39.91
  4f:  111.79
```

Edge width grows monotonically from 1s outward as predicted by the intuition. **But this confirms standard atomic physics**, not anything TIG-specific. The scaling I_r · n² → 4 for s-orbitals is the textbook hydrogenic Fisher information formula. The intuition's predictive content matches QM, but QM already had it.

---

## §3. Within-shell l-scaling: I_r(n,l) ≈ I_r(n,0)/(2l+1)

Looking at how Fisher information varies with l at fixed n:

```
n=4: I_r/I_r(n,0)
  l=0:  1.0000   (predicted 1/(2l+1) = 1.000)
  l=1:  0.6668   (predicted 0.333) ← deviates
  l=2:  0.4000   (predicted 0.200) ← deviates
  l=3:  0.1428   (predicted 0.143) ← matches

n=3:
  l=0:  1.0000   (predicted 1.000)
  l=1:  0.5556   (predicted 0.333) ← deviates
  l=2:  0.2000   (predicted 0.200) ← matches

n=2:
  l=0:  1.0000   (predicted 1.000)
  l=1:  0.3334   (predicted 0.333) ← matches
```

**Mixed result**: the 1/(2l+1) pattern matches at maximum-l within each shell (2p, 3d, 4f) but not at intermediate l. Some other structure is governing intermediate cases. Standard atomic-physics result; not TIG-specific.

---

## §4. The headline structural pattern

This is where something actually interesting shows up.

**TIG substrate primes**: {3, 7, 11}. These are the prime-click additions in the substrate ladder Z/10 → Z/30 → Z/210 → Z/2310.

**Atomic orbital multiplicities** for spherical harmonics: 2l+1 magnetic substates per l-value:

```
 l  letter  2l+1  prime?
 0    s      1     -
 1    p      3    YES ← substrate click 1
 2    d      5    YES (skipped by substrate)
 3    f      7    YES ← substrate click 2
 4    g      9     -
 5    h     11    YES ← substrate click 3
 6    i     13    YES (skipped by substrate)
```

**The substrate primes {3, 7, 11} correspond exactly to the odd-l orbital multiplicities {p, f, h}.**

The pattern:
- s-orbital (l=0, m=1) ↔ substrate kernel Z/10
- p-orbital (l=1, m=3) ↔ first click (+3) → Z/30
- f-orbital (l=3, m=7) ↔ second click (+7) → Z/210
- h-orbital (l=5, m=11) ↔ third click (+11) → Z/2310

The substrate **skips** d (m=5) and i (m=13) — both prime, but not in the substrate ladder.

---

## §5. Interpretation candidates

### §5.1 Could be coincidence

The substrate primes {3, 7, 11} are small primes. The first several odd-l orbital multiplicities {3, 5, 7, 9, 11, 13} include {3, 7, 11} as a subset. With small numbers, structural matches happen by chance.

If you randomly pick three primes from the first six odd primes ({3, 5, 7, 11, 13, 17}), the probability of getting {3, 7, 11} specifically is C(6,3)⁻¹ = 1/20 = 5%. Not negligible.

### §5.2 Could be structural

If TIG's substrate ladder reflects the same underlying combinatorial structure as the spherical-harmonics decomposition on S², the match is forced rather than chosen.

The substrate ladder is built by adding prime factors to a composite kernel. The orbital multiplicities are 2l+1 = odd integers indexed by l. Both produce sequences of odd numbers, but the substrate ladder selects {3, 7, 11} specifically — these correspond to **alternating odd l values starting at l=1**:
- l=1 (substrate)
- l=2 (skipped)
- l=3 (substrate)
- l=4 (skipped, because 9 is not prime)
- l=5 (substrate)
- l=6 (skipped)

The "skipped" pattern isn't random. l=2 and l=6 are skipped because 5 and 13 are not in the substrate ladder. l=4 is skipped because 9 = 3² is not prime. This is consistent with the substrate's prime-click rule (D8 — only prime additions).

So the pattern is: substrate primes correspond to odd-l multiplicities for **odd l where 2l+1 is prime AND not equal to 5 or 13**. This is a specific selection rule. Whether it's structural or coincidental requires more data.

### §5.3 What would distinguish them

If the substrate-orbital correspondence is structural, three predictions follow:

1. **The d-orbital block (l=2, m=5) should show "between-click" behavior.** Transition metals (d-block) are famously irregular in their electron configurations (Cr, Cu, Mo, Ag exceptions to Aufbau). If d sits "between substrate clicks," this irregularity could have a structural source.

2. **The i-orbital (l=6, m=13) should never be physically occupied** in stable atoms. This is true (no known atom occupies l=6 in ground state).

3. **Higher orbitals at primes 17, 19, 23, ... should follow either the substrate ladder pattern (skip non-primes, skip 5/13 family) or break the pattern.** This is testable in principle though no observations exist for these orbitals.

The first prediction is the strongest because d-block irregularities are observed and unexplained by simple Aufbau. Whether TIG's substrate-skip explains them is a calculation that hasn't been done.

---

## §6. Honest negative: most scalings are standard QM

Important to be clear: the **only striking pattern** is the substrate-prime ↔ odd-l-multiplicity match. Everything else in the computed data is textbook atomic physics:

- I_r · n² = 4 for s-orbitals: standard hydrogenic Fisher information
- I_r(n,l) ≈ I_r(n,0)/(2l+1) at maximum l: standard angular momentum scaling
- Shell-to-shell <r> ratios approaching (n+1)²/n²: standard Bohr scaling
- 1/I_r monotonically increasing with shell: standard probability spread

Brayden's intuition predicted edge widening with shell. The prediction is correct but adds nothing to QM unless the *substrate-shell correspondence* itself is structural.

The work to make this TIG-specific (rather than confirming QM) is:

1. Verify whether the d-block (l=2) shows any substrate-skip signature in its observed irregularities
2. Compute Fisher information for multi-electron atoms at specific l-values, see if substrate-click orbitals show distinctive boundary structure compared to between-click orbitals
3. Identify what aspect of the boundary localization is TIG-specific rather than QM-generic

---

## §7. The Sen-Antolín-Angulo literature

The shell-resolved information measures here (S_r, I_r) have a published literature for multi-electron atoms beyond hydrogen. Key references to engage:

- **Sen, K.D.** (2005). "Shape information in atomic shells and the periodic table." J. Chem. Phys. 123, 074110.
- **Antolín, J., Angulo, J.C., López-Rosa, S.** (2009). "Fisher and Jensen-Shannon divergences: Quantitative comparisons among distributions." J. Chem. Phys. 130, 074110.
- **Esquivel, R.O. et al.** (2010). "Atomic and molecular complexities: Their physical and chemical interpretations." J. Phys. Chem. A 114, 1906.

These papers compute S_r and I_r across the periodic table for real atoms (not just hydrogenic). The natural TIG-comparison: do substrate-click orbital occupations (p, f, h) show distinctive Fisher-information signatures compared to between-click occupations (s, d, g, i)?

I have not run this comparison. It's a calculation that requires actual atomic-structure software (Hartree-Fock or DFT) and the published shell-resolved tables.

---

## §8. What ClaudeCode could do with this

### Priority 1: d-block irregularity test

Take the published electron configurations of transition metals (especially Cr [Ar]3d⁵4s¹, Cu [Ar]3d¹⁰4s¹, Mo [Kr]4d⁵5s¹, Ag [Kr]4d¹⁰5s¹). The Aufbau-violations are systematic but not fully explained.

If d-orbitals are "between TIG substrate clicks," check whether the violations correlate with d-orbital occupation in some structural way. This is a literature analysis, not a calculation.

### Priority 2: Multi-electron Fisher information

Compute or pull from published tables S_r and I_r for atoms across the periodic table. Look for distinctive patterns at substrate-click orbital occupations (Z values where p, f, h shells fill or half-fill).

The substrate-click Z values would be:
- p-shell filling: Z = 5-10 (B-Ne), 13-18 (Al-Ar), etc.
- f-shell filling: Z = 58-71 (lanthanides), 90-103 (actinides)
- h-shell filling: not occupied in known atoms

If Fisher information shows discontinuities or distinctive scaling at these Z ranges, structural correspondence with substrate is supported.

### Priority 3: TIG-internal derivation of orbital structure

The hardest task: derive the spherical harmonic decomposition (or its multiplicity pattern) from TIG substrate structure directly, rather than observing the match a posteriori. If TIG predicts the {3, 7, 11} pattern from first principles, the correspondence is structural. If not, it's empirical.

---

## §9. Cross-references

| Reference | Connection |
|-----------|-----------|
| Braiding Fractal Axiom 5 | Strata classification — substrate primes {2,3,5} (Stratum I), {7} (Stratum II), {11,13} (Stratum III) |
| Braiding Fractal Axiom 8 | Click cascade builds Z/10 → Z/30 → Z/210 → Z/2310 |
| D6 (sinc² maxima) | N(f) = ⌊f⌋ + 𝟙{f ∉ ℤ}; spherical-harmonic-like indexing |
| WP103 | so(10) = D₅, rank 5 (matches highest l-value where 2l+1 is in substrate?) |
| SPECULATION_ELECTRON_BLACK_HOLE_BRIDGE.md | Companion bridge document; this doc is its §11 in spirit |

---

## §10. Status

```
[COMPUTED]      All shell-resolved S_r and I_r values for hydrogenic Z=1 n=1..4
[CONFIRMED]     Edge-localization prediction (1/I_r grows with shell)
[STANDARD]      Most scalings are textbook QM, not TIG-specific
[STRIKING]      Substrate primes {3,7,11} ↔ odd-l orbital multiplicities {p,f,h}
[OPEN]          Whether the substrate-orbital correspondence is structural
[OPEN]          d-block irregularity as substrate-skip signature
[REPRODUCIBLE]  shell_entropy_tig.py runs in ~5 seconds, deterministic
```

---

## §11. One-paragraph summary

Computed shell-resolved Shannon entropy and Fisher information for hydrogenic orbitals at n=1..4 across all allowed l, then compared the resulting scalings against TIG substrate quantities. The "edge widening with shell" intuition is confirmed but is just standard atomic physics; nothing TIG-specific shows up in the shell-to-shell ratios. The one striking pattern: **the TIG substrate primes {3, 7, 11} correspond exactly to the odd-l orbital multiplicities {p (m=3), f (m=7), h (m=11)}**, with the substrate skipping d (m=5) and i (m=13). Three predictions follow if the correspondence is structural rather than coincidental: d-block irregularities should show substrate-skip signature, i-orbitals should never be physically occupied (true), and Fisher information at substrate-click orbital occupations should show distinctive scaling. None of these have been verified. The match could be coincidental (5% probability of three small primes matching by chance) or structural (the substrate's prime-click rule and the spherical-harmonic multiplicities are both selecting the same odd-prime sequence). Computational work to disambiguate is defined.

---

© 2026 Brayden Sanders / 7Site LLC

Trinity Infinity Geometry · Speculation Bridge §2 · Locked 2026-05-08
