# Pre-registration: every cube is two spheres (written 2026-10-23, before `cube_spheres.py` ran)

**The picture.** The cube [−1, 1]ⁿ sits between two spheres: a contained one (radius 1, touching the face
centres) and a containing one (radius √n, through the corners). The physics version: definite ±1 outcomes
are the cube's corners, and quantum correlations are unit vectors on a sphere (Tsirelson, 1980). The gap
between the two is the Bell gap.

| id | kind | prediction | kill condition |
|---|---|---|---|
| S1 | translation | The contained radius is 1 and the containing radius is √n. Only in 4D is the corner distance equal to the edge length (2). | Any mismatch. |
| S2 | translation | Uniform points in the cube sit on a third sphere, of radius √(n/3), in a shell about 0.26 wide that doesn't grow with n (n = 3 to 1,000). | Shell width grows with n, or the radius is off by more than 1%. |
| S3 | translation | CHSH: corners give 2, unit vectors give 2√2. The ratio √2 is exactly the square's containing-to-contained ratio. | Either value off. |
| S4 | translation | KCBS pentagon: corners give 2, unit vectors give √5. | Either value off. |
| S5 | translation | For random two-party sign games (sizes 2–8), the vector value never exceeds 1.7823 × the corner value (Krivine's bound on Grothendieck's constant). | Any ratio above 1.7823, which would mean a bug, since this is a theorem. |
| S6 | real | No random ±1 game of size 2–8 beats CHSH's ratio of √2 (200 games per size). | Any ratio above √2. |
| S7 | real | The average ratio grows steadily with size from 2 to 8. | Not monotone. |

## Scores (after running; predictions above unchanged)
| id | result | outcome |
|---|---|---|
| S1 | radii 1 and √n; only 4D puts the corners one edge length from the centre | **held** |
| S2 | the shell width is fixed (0.26–0.28), but the mean radius at n = 3 is 0.960, not 1.000 | **lost** (my registration used the mean; the exact statement is the root-mean-square radius) |
| S3 | CHSH: 2 vs 2.828427, ratio √2 | **held** |
| S4 | KCBS: 2 vs √5 | **held** |
| S5 | max ratio 1.4142, under Krivine's 1.7822 | **held** |
| S6 | max ratio exactly √2 (reached at sizes 2 and 4, never beaten) | **held** (at equality) |
| S7 | the mean ratio zigzags with parity, not monotone | **lost** |
