# The kernel ledger: forced and accidental zeros across domains

Written 2026-10-24 before any test in this folder ran.

**Status.** The lemma below is standard (Schur's lemma bookkeeping), and Levels 0-2 are known theorems in
each field. What this file adds is one ledger applied the same way everywhere, plus a sharp question: what
is left over once every forcing mechanism has been counted?

## Setting
- A linear map T : V -> W. Its kernel is what T sends to nothing. Its cokernel is what T cannot reach: the
  obstruction. index(T) = dim V - dim W = dim ker - dim coker.
- Every domain below is a choice of T. The question is always the same: how much of ker T (or coker T) is
  *forced*, and by what?

## Level 0: global count
- nullity >= max(0, dim V - dim W), and conullity >= max(0, dim W - dim V).
- Instances:
  - Maxwell's rule for frameworks (mechanisms - self-stresses = 2j - 3 - b in 2D);
  - Sutherland and Lieb for bipartite hoppings (nullity >= |N_A - N_B|).

## Level 1: symmetry sectors, with a twist
Let a finite group G act on V and W, and let T g = chi(g) g T for a one-dimensional character chi:
- chi trivial: T is equivariant;
- chi = sign: T is anti-equivariant, as with a complement symmetry or a chiral operator.

**Lemma.** T maps the rho-isotypic part of V into the (rho x chi)-isotypic part of W. Hence
  nullity(T) >= sum over irreps rho of dim(rho) * max(0, m_rho(V) - m_(rho x chi)(W)),
and the same holds for the cokernel with V and W swapped.

*Proof.* T g v = chi(g) g T v, so T intertwines rho with rho x chi. Apply Schur's lemma block by block.

Instances:
- **The void index (Round 8).** G = <P> x <Q> (row and column involutions), chi = sign, coming from
  P M Q = cE - M once the constant direction is set aside. It gives nullity >= |(f_P + f_Q)/2 - 1|.
- **Fowler-Guest:** G is the point group and T is the rigidity matrix.
- **Chiral index:** G = <Gamma>, chi = sign.
- **Linear structures:** f(x ^ a) = f(x) ^ 1 gives G = <x -> x ^ a> with a sign twist. Half the Walsh spectrum
  vanishes.

## Level 2: local imbalance (support)
- If T has a fixed zero pattern, every set S of domain coordinates with fewer neighbours N(S) than |S| forces
  nullity >= |S| - |N(S)|. The maximum over S is the Hall/Konig deficiency, dim V - nu (nu = maximum matching).
- For generic values on the support, nullity equals that deficiency exactly: generic rank = term rank
  (Edmonds 1967).
- Instances:
  - non-Kekulean molecules: Clar's goblet has balanced sublattices but deficiency 2;
  - Laman counts for frameworks.
- With a G-invariant support and G-respecting generic values, the count is made per sector. In rigidity these
  are the orbit-matrix counts of Schulze and Whiteley.

## Level 3: arithmetic residue
What is left once Levels 0-2 are counted is *value-forced*. It vanishes under generic perturbation within the
same support and symmetry class. Two kinds:
- **(3a) structured:** roots of unity cancel over the cosets of a subgroup. Examples are DFT minors at
  composite n, and the 4k-cycle eigenvalue 2cos(pi/2) = 0.
- **(3b) accidental:** integer coincidences with no visible structure. Example: the 5 order-5 magic squares
  with dense support and no symmetry (Round 8c).

**Theorems that close Level 3** for a whole class show arithmetic cancellation is impossible:
- Chebotarev: every minor of the prime-length DFT is nonzero;
- Round 8b: prime-order cyclic-Latin squares are nonsingular;
- the siamese closed form.

All of them work at the prime (1 - w), or by dominance of magnitudes.

## Dictionary
| domain | T : V -> W | Level 1 (symmetry, twist) | Level 2 (local) | Level 3 residue | known theorems |
|---|---|---|---|---|---|
| pi-electron molecules | adjacency block C^B -> C^A | chirality; point group | Hall deficiency (non-Kekulean) | 4k-cycles; accidents | Sutherland, Lieb, Ovchinnikov, Longuet-Higgins; Fajtlowicz-John-Sachs (benzenoids: nullity = n - 2nu) |
| frameworks | joint velocities -> bar strains | point group (Fowler-Guest) | Laman (sub)counts | special geometry (parallel, collinear) | Maxwell-Calladine, Laman, Schulze |
| magic squares | R^n -> R^n | complement symmetry (void index) | constant-sum line subsets | integer coincidences | Trigg, Mattingly, Staab; Rounds 7-8 |
| Fourier / sparse recovery | signals on C -> samples on R | subgroup translations | none (dense) | coset cancellations; none at prime n | Chebotarev, Tao, Donoho-Stark |
| Boolean functions | f -> Walsh spectrum | x -> x ^ a, sign twist | none | coincidental zeros | linear structures |
| contextuality | assignments -> context parities over F2 | context symmetries | none | coker = the obstruction (the parity proof) | Mermin; TLC; edge theorem |

## The cross-domain question
In each domain, does the observed kernel equal the Level 0-2 forced count plus a residue that is
(3a) structured or (3b) accidental? Is the split predictable? The tests are in `PREREG.md`.

## What the tests found (2026-10-24; details and scores in PREREG.md)
| domain | forced part (Levels 0-2) | residue (Level 3) |
|---|---|---|
| benzenoids | exact: nullity = n - 2nu in 300/300 | none |
| diluted square lattice, equal hoppings | exact once weights are generic (300/300) | in 44% of clusters; all of it disappears under random weights |
| mirror frameworks | sector bound in 300/300; exact in 98% of generically rigid graphs | 2% (extra local flexes) |
| DFT minors | -- (dense support) | at composite n: one level of subgroup pigeonhole explains 87-100%; the rest needs deeper levels of the subgroup chain (Cooley-Tukey). At prime n: none (Chebotarev). |
| magic squares | order 4: all 640 kernels forced (496 local + 144 global) | order 5: 5 of 19 singular are accidental; order 6: no singular square in 2,851 |

**Cross-domain law (pieces proved, the rest measured here).** A residue needs arithmetic that the support and
the symmetry do not see: equal weights, roots of unity of composite order, small integers. Where the values
are arithmetically generic, the forced ledger is exact and the residue is empty. Three of those cases are
proved:
- random weights (Edmonds: generic rank = term rank);
- prime-order roots of unity (Chebotarev);
- prime-order cyclic-Latin squares (Round 8b, by (1-w)-adic valuation).

**Open cross-domain problem.** Predict the size of the residue from the arithmetic of the values.
- Fourier: the subgroup lattice predicts most of it (the single-level certificate covers 87-89% at n = 12, 16).
- Equal-weight lattices: 4k-cycles are a known source (2cos(pi/2) = 0). How much of the 44% they explain was not
  measured here.
- Magic squares: nothing yet predicts the accidental order-5 kernels. That is the least understood corner of the
  ledger.

## Order 5, read through the user's "concentric / eccentric" picture (Rounds K6-K7)
Every kernel vector has zero sum, so every kernel says two weighted clouds of lines share a barycenter.
Classified by weights and center, over 85 singular 5x5 squares:
- **concentric:** equal weights, center = the void, i.e. complementary pairs. 71%. Forced (Level 2).
- **eccentric:** equal weights, center off the void, i.e. l_a + l_b = l_c + l_d or 2 l_c = l_a + l_b. 5%. It
  forces a kernel by itself, but only special values put a square there.
- **weighted:** unequal weights, e.g. 3 r0 + 2 r1 = 4 r2 + r3. 25%. The true residue.

The first formalization of "4 seen as 5" (kernels merge or drop a line) lost: it was small-number pigeonhole.
The eccentric class is the part of the idea that survived a fresh test. At order 4, every kernel is
concentric: the three cube axes.

## The weighted quarter has structure (Rounds K8-K8b)
- **Not noise.** On 39,831 fresh squares, det = 0 occurs 3.06x as often as an equally divisible nonzero
  determinant (25 weighted zeros vs an 8.2 lattice estimate). Weighted-singular squares have a singular base-5
  digit layer about 2x as often as nonsingular ones.
- **The void blocks the obvious proof.** Write M = 5A + B + 1. Singularity forces B v = 0 mod 5, but every row of
  B sums to 0 mod 5, so B always kills the constant vector mod 5. In 126 of 161 singular squares, the kernel
  reduced mod 5 *is* that constant direction.
- **Measured hint (post hoc):** when B's rank mod 5 drops to 2, the singular rate rises about 19x.
- **Next:** test that hint on fresh squares (T3-T5 in PREREG).
- **K9 (64,680 fresh squares):**
  - Low digit rank mod 5 raises the singular rate (about 9x at rank 2; registered 10x, lost narrowly).
  - It strongly raises the 5-adic divisibility of det.
  - It does *not* separate weighted kernels from concentric ones.
  - A first 5-adic lattice estimate was badly scaled and failed. Whether the weighted excess is 5-adic is open.
