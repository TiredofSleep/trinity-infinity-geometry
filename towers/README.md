# The towers — where the base points

Each shape of the [base](../base/README.md) is the ground floor of a tower of higher mathematics,
climbing from something a child can build to what a graduate student studies. Every tower also carries
a **coin** — a flip with two sides and an edge, where its paradox sits. The coins are the second lens:
see [`../coin/`](../coin/README.md).

> **Run the checks** (Python 3.10+, numpy):
>
> ```
> python verify_towers.py         # every checked floor of every tower
> python verify_two_builds.py     # equal distance lifts; perpendicularity doubles
> python verify_one_third_fold.py # the 1/3 as lift, fold and gap
> python bott_verify.py           # the Clifford tower's eight-step clock
> python verify_spinor_floor.py   # Cl(2n) acts on 2^n spinors
> python verify_two_faces_of_s4.py # the tetrahedron's group and the cube's rotations
> python verify_balance_point.py  # the flat face walked and averaged: Fejer's kernel (needs sympy)
> ```

| file | what it is |
|---|---|
| [`THE_TOWERS.md`](THE_TOWERS.md) | **Start here — the map**, in eight parts, each tower from its ground floor to its top: the three towers that never end — simplex, cross-polytope and cube, the only regular shapes in every dimension; ℝ → ℂ → ℍ → 𝕆; the Clifford tower; the symmetry tower (A₅ and the quintic; the quaternions double-covering rotation); the lattice tower (to E₈); the harmonic, real-number and growth towers. |
| [`THE_TWO_BUILDS.md`](THE_TWO_BUILDS.md) | Where two towers fork: equal distance (the simplex tower — each point lifts a dimension) and perpendicularity (the cube and Clifford towers — each direction doubles), both counted by Pascal's triangle. |
| [`P2_clifford_cube_skeleton.md`](P2_clifford_cube_skeleton.md) | The Clifford tower's ground floor: the cube's three perpendicular axes generate Cl(3); its bivectors square to −1; its two shadows, square and hexagon, are joined by cos² = 1/3. |
| [`THE_ONE_THIRD_AND_THE_FOLD.md`](THE_ONE_THIRD_AND_THE_FOLD.md) | The tetrahedron's one number as lift, fold and tiling gap, and its return up ℝ → ℂ → ℍ — the bottom of the harmonic and number towers. |
| [`THE_SPINOR_FLOOR.md`](THE_SPINOR_FLOOR.md) | A floor of the Clifford tower, below Bott: Cl(2n) is every operator on 2ⁿ spinors. Pascal's row 2n grades the algebra and row n the spinors, and at n = 3 the half-spinors are the cube's two tetrahedra. Classical; recovered from the archived J20. |
| [`bott_periodicity.md`](bott_periodicity.md) | The top of the Clifford tower: the algebras repeat with period 8 = 4 + 4, because ℍ ⊗ ℍ ≅ ℝ(4). |
| [`THE_TWO_FACES_OF_S4.md`](THE_TWO_FACES_OF_S4.md) | A floor of the symmetry tower: S₄ acts on space as the tetrahedron's group, mirrors included, and as the cube's rotations, and the central inversion turns one into the other. Its coin's edge is A₄. Classical; corrects a label in the archived J43. |
| [`THE_BALANCE_POINT.md`](THE_BALANCE_POINT.md) | A side floor of the harmonic tower, on the circle: walk a polygon and average where you have been. The average stands on the centre exactly at whole laps, and its squared distance is Fejér's kernel. Classical; recovered from the archived J24 and J26, with their errors listed. |
| [`binary_magic/`](binary_magic/README.md) | A floor of the cube tower: the cube's corners counted in binary, and all 880 4×4 magic squares read one binary digit at a time. Fitting (1931) had the layers; the fold theorem is new. Also inside: `code_lens/` (the tesseract code), `magic_sets/` (graph-star magic sets: 16 observables at 5 qubits against 26 published, and 16 proved minimal among context-minimal sets) and `void_lens/` (squares measured from their center: a closed-form determinant, and the pandiagonal 5×5 squares are never singular). **Closed for now (2026-10-25):** [`binary_magic/STATUS.md`](binary_magic/STATUS.md). Run `python run_all.py` inside it (39 scripts, about 15 minutes). |
| [`kernel_ledger/`](kernel_ledger/README.md) | The same thread's last round: one ledger for "forced or accidental zeros" across molecules, frames, Fourier minors and magic squares. Levels 0–2 are known theorems; the measured residues are the new part. With the author's essay *A Ledger of Nothing*. Run `python run_all.py` inside it (8 scripts, about 2 minutes). |
| [`laws_of_a_table/`](laws_of_a_table/README.md) | A side floor of the number tower, which climbs by giving up laws: this floor counts them, with the 4,694 short laws of the Equational Theories Project as a ruler. ℤ/n obeys 32 for every n ≥ 5; every Steiner triple system obeys the same 382 (new, small); and eight closures of 14 laws all have finite specimens (new, small). From the archived ETP papers, corrected. Four scripts, about a minute in all. |
| [`planes_and_mirrors/`](planes_and_mirrors/README.md) | A side floor of the number tower: what 7 dimensions contain, mirrors at every floor of the doubling, and why the octonions' Fano plane breaks at 16. Mostly known mathematics, checked. |
