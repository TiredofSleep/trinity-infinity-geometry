# The towers — where the base points

Each shape of the [base](../base/README.md) is the ground floor of a tower of higher mathematics,
climbing from something a child can build to what a graduate student studies. Every tower also carries
a **coin** — a flip with two sides and an edge, where its paradox sits. The coins are the second lens:
see [`../coin/`](../coin/README.md).

> **Run the checks** (Python 3.10+, numpy):
>
> ```
> python verify_towers.py         # every checked floor of the eight towers
> python verify_two_builds.py     # equal distance lifts; perpendicularity doubles
> python verify_one_third_fold.py # the 1/3 as lift, fold and gap
> python bott_verify.py           # the Clifford tower's eight-step clock
> ```

| file | what it is |
|---|---|
| [`THE_TOWERS.md`](THE_TOWERS.md) | **Start here — the map.** Eight towers, each from its ground floor to its top: the simplex, cross-polytope and cube towers (the only regular shapes in every dimension); ℝ → ℂ → ℍ → 𝕆; the Clifford tower; the symmetry tower (A₅ and the quintic; the quaternions double-covering rotation); the lattice tower (to E₈); the harmonic, real-number and growth towers. |
| [`THE_TWO_BUILDS.md`](THE_TWO_BUILDS.md) | Where two towers fork: equal distance (the simplex tower — each point lifts a dimension) and perpendicularity (the cube and Clifford towers — each direction doubles), both counted by Pascal's triangle. |
| [`P2_clifford_cube_skeleton.md`](P2_clifford_cube_skeleton.md) | The Clifford tower's ground floor: the cube's three perpendicular axes generate Cl(3); its bivectors square to −1; its two shadows, square and hexagon, are joined by cos² = 1/3. |
| [`THE_ONE_THIRD_AND_THE_FOLD.md`](THE_ONE_THIRD_AND_THE_FOLD.md) | The tetrahedron's one number as lift, fold and tiling gap, and its return up ℝ → ℂ → ℍ — the bottom of the harmonic and number towers. |
| [`bott_periodicity.md`](bott_periodicity.md) | The top of the Clifford tower: the algebras repeat with period 8 = 4 + 4, because ℍ ⊗ ℍ ≅ ℝ(4). |
