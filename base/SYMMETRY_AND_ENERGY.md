# Symmetry and energy — when the most symmetric arrangement wins every contest

*The base picks each shape by symmetry ([`SEVEN_AND_NINE.md`](SEVEN_AND_NINE.md)). Another rule picks by
energy: let the points push each other apart and see where they settle. But "push apart" can follow many
laws, such as Coulomb's 1/r, steeper powers, or Gaussian and logarithmic laws, and the laws can disagree.
This page asks when one arrangement wins every contest at once.*
- *On the circle, always.*
- *On the sphere, at 2, 3, 4 and 6 (and 12), and never at 8.*
- *In the plane, the triangular lattice wins among lattices. Whether it beats every arrangement is a 2026
  claim.*
- *In space no lattice wins, and a coin decides why.*

*Everything is classical apart from the claim. Every [FORCED] line is checked by
[`verify_symmetry_and_energy.py`](verify_symmetry_and_energy.py) (23 checks, about fifteen seconds).*

Tags: **[FORCED]** proved here or computed by the script · **[NAMED]** a cited standard result · **[OPEN]**
not settled · **[COIN]** a classified pair: both faces kept, the edge named · **[READING]** an
interpretation · **[FENCE]** two things that share a word but are not one object.

---

## 1. The contest

Put *n* points on a circle or a sphere, and let every pair pay *f*(*r*²) for its distance *r*. A **contest**
is a choice of *f*. "Every contest" means every completely monotone *f*: Coulomb's 1/*r*, the steeper powers
1/*r*ˢ, the Gaussians e^(−*a r*²), and every mixture of them. The logarithm is their limit. An arrangement
that wins all of them is **universally optimal** [NAMED: Cohn and Kumar 2007].

Here "completely monotone" means on all of (0, ∞), so by Bernstein's theorem every contest is a mixture of
Gaussians. Cohn and Kumar allow a slightly larger class: potentials completely monotone on (0, 4], the
squared distances that occur on the unit sphere. That class adds polynomials such as 4 − *r*², and §3 says
what they change.

The script plays seven contests: powers *s* = 1, 3, 12 and 40, Gaussians *a* = 1 and 4, and the logarithm.
- [FORCED] The search reproduces the published Coulomb (Thomson) energies for 2 to 9 and 12 points.
- Seven contests can show that **no** arrangement wins them all, when two winners differ. Only a theorem can
  show that one arrangement wins them all.

## 2. On the circle, symmetry always wins

- [NAMED; FORCED] The regular *n*-gon is **sharp**. It averages every wave up to *n* − 1 turns correctly
  (a design of strength *n* − 1), while using only ⌊*n*/2⌋ different distances. Cohn and Kumar proved that
  every sharp arrangement wins every contest.
- [FORCED, measured] The search agrees: for *n* = 3 to 9, the regular polygon wins all seven contests.

So the base's flat faces, the pentagon, the heptagon and the nonagon, win every contest on their circles.

## 3. On the sphere, symmetry wins at 2, 3, 4, 6 and 12, and loses at 8 and 20

**The test** [NAMED: Cohn and Kumar 2007; FORCED: the numbers]. An arrangement is sharp when its design
strength *t*, the degree up to which it averages every polynomial correctly, is at least 2*m* − 1. Here *m*
is its number of different distances.

| shape | *t* | *m* | sharp? |
|---|---|---|---|
| segment through the centre (2) | 1 | 1 | yes |
| triangle on a great circle (3) | 1 | 1 | yes |
| tetrahedron (4) | 2 | 1 | yes |
| octahedron (6) | 3 | 2 | yes |
| icosahedron (12, past the base) | 5 | 3 | yes |
| cube (8) | 3 | 3 | no |
| dodecahedron (20) | 5 | 5 | no |
| triangular bipyramid (5) | 1 | 3 | no |

- [NAMED; FORCED, measured] So the segment, the triangle, the tetrahedron and the octahedron, and the
  icosahedron past the base, win every contest. The search confirms each one in all seven.
- **The cube loses every contest.** [FORCED; the proof is written out here.]
  - Turn the cube's top face about the vertical axis by an angle ψ, keeping its height. The points stay on the
    sphere, and the distances inside each face do not change.
  - Take a completely monotone *f*. Between a top corner and a bottom corner, *f* is a power series in the
    cosine of the angle between them, with no negative coefficients (Bernstein's theorem).
  - Each power of a cosine is a sum of cosines of multiples of the angle, again with no negative
    coefficients. Summing over the four turns of the square leaves only multiples of 4. So the energy is
    *F*(ψ) = *c*₀ + *c*₁ cos 4ψ + *c*₂ cos 8ψ + …, with every *c* ≥ 0 and *c*₁ > 0.
  - So ψ = 0, the cube, is the highest point. The 45° turn, a square antiprism, is lower by
    2(*c*₁ + *c*₃ + …) > 0. ∎
  - The script checks every twist on a grid, in all seven contests.
  - In Cohn and Kumar's larger class, a polynomial of degree at most 3 in *r*² gives *c*₁ = 0, and there the
    cube ties: it is a 3-design, and every 3-design wins such a contest [NAMED: Delsarte, Goethals and
    Seidel]. Any potential with more in it makes the twist win [FORCED: the second derivative along the
    twist, computed exactly by [`verify_dodecahedron.py`](verify_dodecahedron.py)].
- [FORCED; NAMED] **The cube loses even though it is balanced to degree 3**, which is the most that 8 points
  allow. Every twisted cube is still a 3-design, and no 8 points make a 4-design: that takes at least 9
  [Delsarte, Goethals and Seidel 1977].
- [FORCED, measured] The Coulomb winner at 8 is the square antiprism at its best height, which is Thomson's
  answer.
- **The dodecahedron loses all seven contests too** [FORCED, measured; registered as a prediction in
  [`../THE_LENS.md`](../THE_LENS.md) §7 before it was run]. In each it is a saddle: one family of three
  moves lowers its energy. Under Coulomb's law the best 20 points are Thomson's, at 150.881568334, against
  the dodecahedron's 151.798620562. [NAMED: Nerattini, Brauchart and Kiessling (2014) state that the
  dodecahedron minimizes no power law with *s* > −2.]
- **The dodecahedron loses every contest** [FORCED: exact arithmetic in ℚ(√5),
  [`verify_dodecahedron.py`](verify_dodecahedron.py); NEW: not found in the literature we checked]. In Cohn
  and Kumar's larger class it loses every contest except one kind: the polynomials of degree at most 5 in
  *r*². There it ties, because it is a 5-design [NAMED: Delsarte, Goethals and Seidel].
  - *Why.* Every potential of that class is f = Σ *c*ₙ (4 − *r*²)ⁿ with every *c*ₙ ≥ 0 (Bernstein). Along one
    of the dodecahedron's flexes, the second derivative of the energy is Σ *c*ₙ 2ⁿ Λₙ.
  - Λₙ = 0 for *n* ≤ 5, and Λₙ < 0 for every *n* ≥ 6: exactly up to *n* = 60, and by an explicit bound
    beyond. The first of them is Λ₆ = −320/81.
  - So unless the potential stops at degree 5, a small move along the flex lowers the energy.
  - That the dodecahedron is not universally optimal was known [NAMED: Cohn and Kumar 2007, who note it is
    not even an optimal spherical code; Ballinger et al. 2009].
- **Rigid wins, floppy loses** [FORCED, measured]. Put bars along each solid's edges and keep its corners on
  the sphere.
  - The tetrahedron, the octahedron and the icosahedron, whose faces are triangles, cannot flex. Each is a
    local minimum in all seven contests.
  - The cube can flex in 2 ways and the dodecahedron in 8. Each is a saddle in all seven contests.
  - The cube's twist is one of its flexes, and the dodecahedron's three losing moves are flexes too.
  - The run behind the dodecahedron's line, with its log: [`run_dodecahedron.py`](run_dodecahedron.py).
- **At 5, 7 and 9 no arrangement wins every contest** [FORCED, measured]. The winners of the seven contests
  differ: their inner products differ by up to 0.49 at 5, 0.43 at 7 and 0.10 at 9 (and 0.11 at 8).
- **The edge inside five** [NAMED; FORCED]. Over the powers *s*, the triangular bipyramid wins until
  *s* = 15.0480773927797…, and from there a square pyramid wins. Melnyk, Knop and Smith found this switch by
  computation in 1977, and Schwartz proved it with a computer-assisted proof. The script finds the tie at
  *s* = 15.0480773928.
- [FORCED] The base's flat faces, put on a great circle of the sphere, lose every contest there. Its solid
  faces at 5, 7 and 9 need a centre, which a sphere does not have.

**[COIN] The polar pair gets opposite verdicts.** By [`../coin/THE_POLAR_COIN.md`](../coin/THE_POLAR_COIN.md),
the cube and the octahedron are the two sides of one coin. On the sphere the octahedron wins every contest,
and the cube loses every one. The tetrahedron, on that coin's edge, wins every one. The next pair agrees in
every contest: the icosahedron wins and the dodecahedron loses. In both pairs the winner is the side with
triangle faces, which is rigid, and the loser is the side that flexes. Each loser's verdict has its own
edge, at its design strength. The cube ties the contests that see only degree 3 or less, and the
dodecahedron those that see only degree 5 or less.

## 4. The plane: the triangular lattice

For infinitely many points at a fixed density, a contest is the energy per point. For a Gaussian of
steepness *a* that is the lattice's theta function θ(*a*), the sum of e^(−*a*|*v*|²) over its points.

- [NAMED; FORCED, measured] **Among lattices, the triangular lattice wins every contest** (Montgomery
  1988). The script checks it against the square lattice at six steepnesses, and against 200 random
  lattices at three.
- [OPEN] **Among all arrangements**, lattice or not, this is Cohn and Kumar's 2007 conjecture. OpenAI's 2026
  release claims a proof (family 090; Lean-checked by its own account, not refereed).

## 5. Space: no lattice wins, and a coin decides why

- [NAMED; FORCED] **Poisson's coin.** Poisson summation turns a lattice's contest at steepness *a* into
  its dual lattice's contest at π²/*a*:

  > θ_Λ(*a*) = (π/*a*)^(*d*/2) · θ_Λ*(π²/*a*),  at density one.

  Done twice, *a* → π²/*a* → *a* changes nothing, and the edge is *a* = π.
- [FORCED] So **a lattice that wins every contest has a dual that wins every contest too**. A lone winner
  must be its own dual. The triangular lattice is (turned), and so are the square lattice and simple cubic.
- [FORCED] In space, face-centred cubic and body-centred cubic are each other's duals: a pair of sides.
  - They tie exactly on the edge, *a* = π; the script finds a difference of 7 × 10⁻¹⁶.
  - Face-centred cubic wins the steeper contests and body-centred cubic the gentler ones, so **no lattice in
    space wins them all**.
  - The self-dual simple cubic lattice loses to both on the edge. Being one's own dual is necessary for a lone
    winner, but not enough.
- [OPEN] Sarnak and Strömbergsson (2006) conjectured that these two are the best lattices on their two
  sides. A 2026 preprint claims a proof; it is not checked here.
- [FORCED] **The base is in this contest.** The nearest shells of the three cubic lattices hold 12, 8 and 6
  points: with the centre, 13, 9 and 7. The base's 9, the cube with its centre, is the body-centred cell, and
  its 7, the octahedron with its centre, is simple cubic's ([`SEVEN_AND_NINE.md`](SEVEN_AND_NINE.md)).
- [NAMED] In 8 and 24 dimensions, the E₈ and Leech lattices, each its own dual, win every contest among all
  arrangements (Cohn, Kumar, Miller, Radchenko and Viazovska 2022).

## What this settles

- **[COIN] The base's two rules, symmetry and energy, are both kept.**
  - They agree at 0 to 4 and at 6, in every contest.
  - They part at 8, in every contest.
  - At 5, 7 and 9 energy has no single answer, and at 5 the switch between its answers is an exact edge,
    *s* = 15.048….
  - The flat faces win every contest on their circles.
- **In the plane and in space:**
  - the plane: proved among lattices; among all arrangements, a claim;
  - space: the verdict splits at the edge of Poisson's coin;
  - 8 and 24 dimensions: proved.
- **[READING]** Two reasons make one arrangement win every contest here: being sharp on the circle and the
  sphere, and being one's own dual among lattices. Where the best shapes come as a pair of sides, the
  verdicts split or one side loses: the cube and the octahedron on the sphere, the two cubic lattices in
  space.

## What this is, and is not

- **Is:** classical results arranged around the base's shapes, with every number computed: Cohn and Kumar,
  Thomson, Schwartz, Montgomery, Poisson summation, and Cohn, Kumar, Miller, Radchenko and Viazovska. The
  cube's twist is written out here. It is elementary, and no novelty is claimed for it.
- **Is not:** new. The plane's all-arrangements case is OpenAI's claim, and the space lattices are open.
- **[FENCE]** "Energy" here is a mathematical contest. Thomson posed the sphere problem in 1904 for a model
  of the atom that turned out wrong. Real molecular shapes and crystal structures are set by quantum
  mechanics, not by this contest.

## Sources

- H. Cohn and A. Kumar, "Universally optimal distribution of points on spheres", *J. Amer. Math. Soc.*
  **20** (2007) 99–148.
- P. Delsarte, J. M. Goethals and J. J. Seidel, "Spherical codes and designs", *Geom. Dedicata* **6**
  (1977) 363–388.
- J. J. Thomson, *Philos. Mag.* **7** (1904) 237–265. Energies: D. J. Wales and S. Ulker, *Phys. Rev. B*
  **74** (2006) 212101.
- T. W. Melnyk, O. Knop and W. R. Smith, *Can. J. Chem.* **55** (1977) 1745–1761.
- B. Ballinger, G. Blekherman, H. Cohn, N. Giansiracusa, E. Kelly and A. Schürmann, "Experimental study of
  energy-minimizing point configurations on spheres", *Experiment. Math.* **18** (2009); arXiv:math/0611451.
- R. Nerattini, J. S. Brauchart and M. K.-H. Kiessling, "'Magic' numbers in Smale's 7th problem",
  arXiv:1307.2834 (v3, 2014): the dodecahedron minimizes no power law with *s* > −2 (stated there in a footnote).
- R. E. Schwartz, "The phase transition in five point energy minimization", arXiv:1610.03303.
- H. L. Montgomery, "Minimal theta functions", *Glasgow Math. J.* **30** (1988) 75–85.
- P. Sarnak and A. Strömbergsson, "Minima of Epstein's zeta function and heights of flat tori", *Invent.
  Math.* **165** (2006) 115–151. The claimed proof: arXiv:2609.17356 (2026), not checked.
- H. Cohn, A. Kumar, S. D. Miller, D. Radchenko and M. Viazovska, "Universal optimality of the E₈ and Leech
  lattices and interpolation formulas", *Ann. of Math.* **196** (2022) 983–1082.
- J. H. Conway and N. J. A. Sloane, *Sphere Packings, Lattices and Groups*, 3rd ed., Springer (1999).
- OpenAI, *Mathematics manuscript collection*, https://github.com/openai/math (October 2026), family 090.
