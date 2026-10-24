# Planes and mirrors: why the number tower stops at 8

**A side floor of the number tower** (ℝ → ℂ → ℍ → 𝕆, [`../THE_TOWERS.md`](../THE_TOWERS.md) §2). These scripts
check what the octonions' 7 dimensions contain, what a mirror does at each floor of the Cayley–Dickson
doubling, and why the doubling breaks at 16. They also check the "cube between two spheres" picture of the
Bell gap. They came from the author's directions in the October 2026 chat:
- dimensions as "stacked, nested, and mirrored in imaginary";
- "why would 7 break at 16";
- "every cube is two spheres".

Each prediction was written in [`PREREG.md`](PREREG.md) before its script ran (only `cube_spheres.py` has one).

> **Run it:** `python run_all.py` (numpy; `cube_spheres.py` uses cvxpy if installed, and falls back if not).

| script | what it checks | status |
|---|---|---|
| `seven_check.py` | Octonions by doubling, basis labelled by 3-bit strings: e_a e_b = ±e_(a⊕b). The 7 Fano lines are copies of the quaternions; there is a 7-D cross product; associativity fails; G₂ (the octonions' symmetry) has dimension 14; one more doubling breaks division | **known**, checked |
| `mirror_room.py` | Two mirrors make a turn of twice their angle. Plane quantities in 3-D travel as arrows and flip the wrong way in a mirror; in 4-D the Hodge star splits the 6 planes 3 + 3 | **known**, checked |
| `mirror_tower.py` | At every floor of the doubling, conjugation is a true mirror (determinant −1, because 2ⁿ − 1 imaginary axes is odd). The new unit l satisfies l·a = a*·l. Remove the mirror from the doubling rule and the algebra collapses; keep it, and it still breaks at 16 | **known**, checked |
| `mirror_brake.py` | The Radon–Hurwitz count: anticommuting imaginary units available on ℝⁿ against those a product needs (8 against 15 at n = 16); the Freudenthal–Tits square | **known**, checked |
| `why_seven_breaks.py` | On 4 bits, an algebra with e_a e_b = ±e_(a⊕b) is fixed by one sign per line (35 lines, 15 Fano sub-planes). No sign choice makes all 15 sub-planes octonions. The script finds the exact maximum, 8, achieved by 135 plane sets, and the smallest contradiction, 5 planes | the sedenions' own split, 8 octonion sub-planes and 7 not, is **known** (Cawagas 2004; Cawagas et al., arXiv:0907.2047). The maximum over **all** sign choices and the 5-plane clash are **not checked against the literature** |
| `cube_spheres.py` | The cube [−1, 1]ⁿ between its inscribed sphere (radius 1) and circumscribed sphere (√n). CHSH (2 against 2√2) and KCBS (2 against √5), and the Grothendieck–Krivine cap on random two-party games | **known** (Tsirelson 1980; Krivine 1979); predictions and scores in `PREREG.md` |

**Fences.**
- The "cube is two spheres" picture is a way of seeing the Bell gap, not a derivation.
- The "magic" in the Freudenthal–Tits *magic square* is a name, not the magic squares of `../binary_magic/`.
- The √(n/3) radius of uniform points in a cube is a coincidence of the number 3, not "the three" of the base.
