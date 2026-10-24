# The electron clock test, and the paradox treasure map

> **Filed 2026-10-24** from the October chats, with the fenced readings ([`../FENCED_READINGS.md`](../FENCED_READINGS.md), R6).
> - **Credit:** the paradox types in §2 (veridical, falsidical, antinomy) are Quine's, from "The Ways of
>   Paradox" (1962; reprinted 1966), as `paradox_map.py` says. *Anomaly* and *resemblance* are added here.
> - **The tally is a reading:** the classifications are judgment calls, as the script says.
> - **The four-question test** at the end is a method, not a result. It goes to Book IV's toolkit.


## 1. The channeling dip: status and a replication spec (`channeling_numbers.py`)

**The claim.** Gouanère et al. (AFLB 30, 2005) and Catillon et al. (Found. Phys. 38:659, 2008):
~80 MeV electrons along the ⟨110⟩ axis of a 1 µm silicon crystal. The 0° transmission dips 8% within
0.5% of 80.874 MeV/c, the momentum at which an electron passes one atom per tick of de Broglie's clock.
The data came from the Saclay electron linac (ALS) as a by-product of an earlier planar-channeling
study. The scan covered ±1.5% in 0.083% steps, with a beam momentum spread of 0.809 MeV/c (~1%).

**Weak points.**
- One experiment, one crystal, one axis.
- The 2005 paper says "8% dip" in the abstract and "1% effect" in the text.
- No error bars or significance are given in the parts I could read.
- The beam spread is wider than the effect window.
- Simulations need twice de Broglie's frequency at half the distance (zitterbewegung), which gives the
  same momentum, so the dip cannot tell the two clocks apart.
- Bauer (arXiv:1409.0888) reproduces it with plain Dirac dynamics plus an effective mass m* ≈ 1.0013 m₀.

**Replication:** none found as of October 2026. The 2008 paper has ~56 citations, mostly theory.

**Correction to my earlier figure:** 1.55 × 10²¹ is the angular rate 2mc²/ħ in rad/s. In cycles per second,
de Broglie's clock is 1.24 × 10²⁰ Hz and zitterbewegung is 2.47 × 10²⁰ Hz.

**The decisive version.** The resonance momentum must scale exactly with the atomic spacing d:
p = d·(mc²)²/(hc).

| crystal / axis | d (Å) | predicted p (MeV/c) | critical angle (mrad) |
|---|---|---|---|
| Si ⟨110⟩ | 3.840 | 80.88 | 1.14 |
| Ge ⟨110⟩ | 4.001 | 84.26 | 1.65 |
| Si ⟨100⟩ | 5.431 | 114.38 | 0.81 |
| W ⟨111⟩ | 2.741 | 57.73 | 3.67 |
| diamond ⟨110⟩ | 2.522 | 53.12 | 1.14 |

**Kill and confirm criteria.**
- **Confirm:** with ≤0.1% momentum steps and divergence well below 1 mrad, the dip reappears in Si ⟨110⟩
  and moves to the predicted momentum in a second crystal or axis (Ge ⟨110⟩ or Si ⟨100⟩).
- **Kill:** no dip, or a dip that stays put when d changes (an ordinary channeling effect).

**Where it could run** (ask them; nothing here is arranged):
- **CERN CLEAR:** electron beams of up to a few hundred MeV, tunable per user; the closest energy match.
- **INFN Frascati BTF:** electrons from 25 to 700 MeV, but ~0.5–1% resolution, too coarse without an added spectrometer.
- **MAMI, Mainz:** the leading electron-channeling group (EU TECHNO-CLS), but its beams start at ~180 MeV.

## 2. Does paradox point to treasure? (`paradox_map.py`)

Here 61 historical paradoxes and anomalies, plus this session's 10 pushes, are each classified by type and outcome. These are judgment
calls, and famous paradoxes are biased toward winners, so known failures are included on purpose.

| type | resolved | became new structure |
|---|---|---|
| **antinomy:** two accepted, independently checked rules can't both hold | 22 | **19 (86%)** |
| **veridical:** true but surprising | 13 | 5 (38%) |
| **anomaly:** data vs accepted theory | 14 | 5 (36%); 8 were mistakes |
| **falsidical:** a hidden fallacy | 3 | 1 |
| **resemblance** (this session only): "this looks like that" | 6 | 0 |

**The map works for one kind of paradox.** The treasure sits where two rules that each
check out independently can't both close: √2 against the fractions, Russell's set, the ultraviolet
catastrophe, the Mermin grid, the forced-empty carry. Surprise alone usually just recalibrates intuition.
Anomalies are coin flips weighted toward error until they replicate. Resemblance never paid
once this session.

**The test before digging.**
1. Can I name the two rules that collide?
2. Has each one been checked on its own?
3. Does the clash survive a re-measurement or a second proof?
4. Is it a clash, or only a likeness? A likeness is not a paradox.

Pass all four and it's worth digging. The channeling dip currently fails step 3, which is why the
replication matters.
