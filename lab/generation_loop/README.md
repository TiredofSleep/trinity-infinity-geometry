# The generation loop: Koide's cone and Brannen's angle, tested against the cube

*Fenced physics, in the lab. None of this is a premise of the base, the towers or the coin.*

The charged-lepton masses obey Koide's relation, (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² = 2/3, to 0.4σ. Two
numbers sit behind it: the ratio 2/3 itself, which says that the vector of square roots makes 45° with the cube's
diagonal (Foot 1994), and an angle, δ = 0.2222220471, that fixes the hierarchy (Brannen 2006). In ten
pre-registered rounds on 2026-10-30, the claude.ai chat asked whether the cube's geometry supplies either one. Each
round was written down before its code ran, and the author's directions are quoted in [`PREREG.md`](PREREG.md) with
their times.

**What came out.**
- **No.** Small sums of cube rotations never give 2/3 (G1). δ is not a simple angle: no hit among 7.3 million
  rational and cube-angle candidates (G2, G4, G6). The quark families carry neither the angle nor the cone, in any
  convention tried (G7–G9, 0 of 7). And a search for a correction term cannot identify the small gap between exact
  Koide and an exact δ = 2/9: hits come at the chance rate (G10).
- **Yes, small.** The *flag circle*. Mix the projectors onto one corner's edge, face diagonal and body diagonal: the
  mixtures that reach Koide's purity 2/3 form a circle. It is a circle because the face-to-body squared cosine is
  2/3 itself, while the edge-to-body pair sits at the base's magic angle, with squared cosine 1/3
  ([`../../towers/THE_ONE_THIRD_AND_THE_FOLD.md`](../../towers/THE_ONE_THIRD_AND_THE_FOLD.md)). It is elementary,
  and it was not found in the sources checked.
- **Known.** The 45° cone (Foot 1994); the amplitude √2 and the angle near 2/9, and the neutrino step of π/12
  (Brannen 2006). The bets that remain open are in [`../predictions/`](../predictions/README.md).

**Status.** The last four rounds lost all ten of their predictions. A new round should start from a question of the
author's.

| file | what |
|---|---|
| `PREREG.md` | every round's registration, scores, errata, literature check, and the review of 2026-10-31 |
| `search.py` | G1–G2: cube rotations; the angle against a fixed grammar |
| `rounds3.py`, `round6.py` | G3–G6: mixtures on the cube's axes, the flag circle, the lepton point on it |
| `round7.py`, `round8.py`, `round9.py` | G7–G9: the quark families, in every convention (`round9.py` runs the masses at four loops) |
| `round10.py` | G10: the correction search, with its chance calibration |
| `test_scores.py` | reruns every round and checks each SCORE line against `PREREG.md` (about 35 s) |
| `qcd_running_check.py` | review: an independent four-loop running that reproduces every number `round9.py` prints |
| `g10_calibration_check.py` | review: G10 rebuilt, with two more calibrations; no verdict changes |
| `flag_circle_check.py` | review: the flag circle, and why it is a circle, checked symbolically |

Each script has its `.log`. Run from this folder (numpy, scipy, mpmath, sympy). Output is ASCII.
