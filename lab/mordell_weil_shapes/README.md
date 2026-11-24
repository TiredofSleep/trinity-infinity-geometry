# Shapes of Mordell–Weil lattices [MEASURED; NAMED: Watkins 2006; lab]

> *rounded triangles sounds like a method of wheel packing* — the author, 20 November 2026
>
> *1 lab* — the author, 21 November 2026, on where this work lives

This folder holds Part F of the lens handoff of 20 November 2026, made exact, checked, and extended by one registered
round. It is a statistic of the objects the Birch and Swinnerton-Dyer conjecture is about, and it is not progress on
that conjecture.

## The object

- **The lattice.** For an elliptic curve E over ℚ of rank 2, take its rational points modulo torsion, with the
  canonical height as the inner product. That gives a lattice in the plane.
- **Its shape.** Take the height Gram matrix of a basis and reduce it to (A, B, C) with |B| ≤ A ≤ C. The point
  x = |B|/A, y = √(AC − B²)/A is the lattice's shape. It lies in the fundamental domain of SL₂(ℤ), with x in [0, ½].
  The **elongation** y is at least √3/2, the hexagonal value.
- **The triangle.** The regulator AC − B² is the squared area of the parallelogram on two generators. In the author's
  words, the link at rank 2 is "the pairs, and all three": a triangle, with a shape and a size.
- **The packing.** Put a disc of radius half the shortest vector at every lattice point. The density is π/(4y): 0.9069
  for the hexagonal lattice, 0.7854 for the square one. Elongation above 2 (density below 0.393) is called *thin*.
- **The null.** For "a random lattice", the natural law is the uniform measure dx dy/y² on SL₂(ℤ)\H. Under it, 47.7%
  of lattices are thin.

## Known: Watkins asked first [NAMED]

Watkins, "Some heuristics about elliptic curves" (arXiv math/0608766, 2006), §6.4, did this before us.
- He computed the Mordell–Weil groups of 2 143 079 rank-2 curves of prime conductor below 10¹⁰, from the Stein–Watkins
  database.
- He placed their lattices in the same coordinates and compared them with the same uniform law.
- He found them rounder than the uniform law: 35.4% thin, against 47.7%. He also found x skewed toward ½. He left open
  whether this is an artefact of small discriminants or a sign that the uniform law is simply wrong.
- **His figures do not reproduce (round 10, below).** On his own population, with generators checked by the BSD
  formula, 9.2% are thin, not 35.4%.

The handoff's "nobody we could find has asked" was wrong, and it is in the graveyard.

What the work here adds, as far as we know, uses Cremona's complete tables rather than a sample ordered by
discriminant: every optimal rank-2 curve of conductor below 500 000, 279 056 in all. On them it registers and scores
trends and splits by conductor, torsion, isogeny and real components; rank 3 against its dual; and the round of
21 November.

**A first literature pass (24 November 2026; web searches, not a full reading).**
- **On the distribution of shapes:** nothing was found beyond Watkins. Prakash ("Effective height bounds from
  Mordell–Weil lattice symmetries", arXiv 2509.22672, 2025) uses the height Gram matrix of a rank-2 Mordell–Weil
  lattice and its Bravais type, but to bound heights on curves of higher genus, not to study shapes.
- **On torsion and the shape:** nothing was found that states round 9's effect.
- **The nearest known mechanism concerns sizes, not shapes.**
  - Lang's conjecture puts a floor under the height of a point of infinite order, ĥ(P) ≥ c log|Δ|. Silverman proved
    it for integral j-invariant, and Hindry and Silverman under the abc conjecture.
  - In function fields, Jain ("Points of low height on elliptic surfaces with torsion", *LMS J. Comput. Math.* 13,
    2010) found the smallest heights when there is a 2- or 3-torsion point. Elkies (arXiv math/0608593, 2006) found
    them without torsion.
  - Comparing those two minima is the natural first test of "torsion raises the floor". It has not been done here.
- **The contrast:** Bhargava and Harron (*Compositio* 2016) proved that the lattice shapes of rings of integers in
  Sₙ number fields of degree 3, 4 and 5 *are* equidistributed. Mordell–Weil lattices, by Watkins's data and
  Cremona's, are not.
- **Not yet read:** Park, Poonen, Voight and Wood's model, and Delaunay's heuristics. Both concern ranks and Sha
  rather than shapes.

## The tension with Watkins, resolved by round 10 ([`registered/REGISTERED_2026-11-24_the_watkins_tension.md`](registered/REGISTERED_2026-11-24_the_watkins_tension.md))

| share with elongation at least | 1 | 2 | 4 | 8 | 16 |
|---|---|---|---|---|---|
| uniform law, (3/π)/Y | 0.955 | 0.477 | 0.239 | 0.119 | 0.060 |
| Watkins (2006): prime conductor below 10¹⁰, as published | 0.935 | 0.354 | 0.094 | 0.017 | 0.002 |
| **the same population, recomputed here (4 000 at random)** | **0.891** | **0.092** | **0.001** | **0** | **0** |
| Cremona: prime conductor below 5 × 10⁵ (1 052 curves) | 0.885 | 0.101 | 0.003 | 0 | 0 |
| Cremona: every conductor below 5 × 10⁵ (279 056 curves) | 0.928 | 0.199 | 0.019 | 0.0002 | 0 |

- **What looked like a tension.** Cremona's prime-conductor curves seemed far rounder than Watkins's: 10.1% thin
  against 35.4% ([`watkins_compare.py`](watkins_compare.py), [`watkins_compare.log`](watkins_compare.log)). Both
  populations have |Δ| = N.
- **Round 10 took Watkins's own curves.** It used the Stein–Watkins prime tables, which hold 2 143 079 classes of
  analytic rank 2, his count. The generators were found with PARI ([`watkins_round.py`](watkins_round.py)).
  - Below 5 × 10⁵ the tables hold exactly Cremona's 1 052 curves, and their shapes match Cremona's to 4 × 10⁻¹⁶.
  - For 220 of 220 curves checked, out to 10¹⁰, the BSD formula with these regulators gives a perfect square for Sha.
- **The result:** 9.2% ± 0.5% of Watkins's population is thin, not 35.4%. No curve reaches elongation 8, where he
  reports 1.7%.
  - From 5 × 10⁴ to 10¹⁰ the thin share is flat at 8–10%.
  - The curves' period lattices do not change shape with conductor either.
- **Unknown:** the cause of the published figures. Doubling or halving the pairing's off-diagonal does not produce
  them.
- **What died with it:** the reconciliation this page offered on 21 November. It said Watkins's curves might have
  more elongated period lattices; there was nothing to reconcile.
- **One part of Watkins's report does reproduce: the horizontal skew.** For all of Cremona's curves with y ≥ 1, the
  share in each tenth of x rises from 0.087 to 0.101–0.104, against his 0.090 to 0.105. The prime-conductor sample of
  round 10 is too small to show it.

## Reproduced here ([`analyse.log`](analyse.log))

Every number of 20 November was recomputed by this repository's own pipeline.
- [`mw_shapes.py`](mw_shapes.py) parses the tables and computes heights with PARI 2.15 through `cypari`.
  [`run_all.py`](run_all.py) drives it at below-normal priority, and [`analyse.py`](analyse.py) compares.
- The handoff's scripts, in [`handoff_scripts/`](handoff_scripts/README.md), were read for their definitions but not
  run.
- The run ([`run_all.log`](run_all.log)): 287 955 optimal curves, of which 279 056 have rank 2 and 8 899 rank 3. There
  were no failures, in 110 seconds.

| the handoff's number | recomputed |
|---|---|
| thin share by band, 10³ to 5 × 10⁵: 0.2430, 0.2324, 0.2175, 0.2124, 0.2040, 0.1980, 0.1922, 0.1870 | the same, to four places |
| by torsion, trivial / ℤ/2 / ℤ/3 / ℤ/4 / ℤ/2 × ℤ/2: thin 0.2222 / 0.0982 / 0.0583 / 0.0175 / 0.0032 | the same |
| hidden loops: 0.5835 against 0.5434, 18.7 s.e. | the same |
| real loop (sign of the discriminant): 7.8 s.e.; Spearman against Im τ −0.128 and −0.032 | the same |
| points on the loop: 0.5481 against 0.5254, 6.1 s.e., 2.8% missing | the same; 73 337 curves reach the loop, against the handoff's 73 331 |
| largest elongation 13.17 (conductor 383 786); counts above 3, 5, 8, 10, 15: 15 885, 1 705, 63, 8, 0 | the same |
| rank 3: lattice 0.3055, dual 0.3179, 15.6 s.e. | the same |

The one difference: the handoff's two counts for points on the loop sum to 6 fewer than its total of curves with
positive discriminant. So 6 curves were probably dropped there.

**Checks of the data.**
- [`saturation_sample.py`](saturation_sample.py): the tabulated generators of 2 000 random rank-2 curves are saturated
  at every prime up to 100 ([`saturation_sample.log`](saturation_sample.log)).
- The round of 21 November checked every curve of every class with more than one curve, 125 622 in all. The BSD
  quotient Ω·Reg·∏c_p/|tors|² agrees across each class, except for 42 curves, where Sha changes from 1 to 4.
- Not done: the regulators against Cremona's `allbsd` table, which needs another download.

## The ledger of registered rounds ([`registered/`](registered/))

| # | date | claim (whose) | outcome |
|---|---|---|---|
| 1 | Nov 20 | thin lattices get rarer as the conductor grows (the author) | pass |
| 2 | Nov 20 | the decline continues at the fitted rate (the author) | pass: 0.1922 and 0.1870 against 0.193 and 0.190 |
| 3 | Nov 20 | the mean density tends to the honeycomb's (the author) | not testable in range; the diagnostic points against it |
| 4 | Nov 20 | torsion-free curves with an isogeny pack better (the author's sentence, Claude's reading) | pass, 18.7 s.e. |
| 5 | Nov 20 | groups above density 0.607 rise toward the honeycomb (the author) | **miss**: slope −0.0050 ± 0.0023 |
| 6 | Nov 20 | a closed real component packs better; packing follows the period lattice (the author's sentence) | pass, 7.8 s.e. and 35 s.e. |
| 7 | Nov 20 | rational points on the closed component pack better (the author's sentence) | pass, 6.1 s.e. |
| 8 | Nov 20 | at rank 3 a lattice and its dual pack differently (Claude, two-sided) | pass, 15.6 s.e.; Claude's direction was wrong |
| 9 | Nov 21 | "every loop fails a little, none fails badly" (the author) | strict **miss**; graded pass, 19.7 s.e.; Claude's rival died |
| 10 | Nov 24 | on the Stein–Watkins tables: Watkins's 35.4% reproduced (Claude); thin lattices keep getting rarer out to 10¹⁰ (the author's sentence of rounds 1 and 2) | Watkins's figure **does not reproduce** (9.2%); the author's sentence is not decided (flat at 8–10%); Claude's rival and W3 died |

**Round 9** ([`REGISTERED_2026-11-21_every_loop_fails_a_little.md`](registered/REGISTERED_2026-11-21_every_loop_fails_a_little.md))
was registered and pushed before any shape was computed. It ran on the 69 616 non-optimal curves of the rank-2
classes, which no script had read for shape.
- 72 of them fail badly (elongation above 5). But a lattice with a loop that fails is a quarter as likely to fail
  badly as one with no loop.
- Read after the run, the exceptions have a mechanism. 63 of the 72 are their round optimal partner's lattice,
  stretched by the isogeny's degree, 2, 3 or 5.
- The protection belongs to rational torsion. No optimal curve with a loop lies above elongation 8; all 63 optimal
  curves there have no loop.

## Open, for the author

- **Fresh data beyond Cremona's tables.** The Stein–Watkins tables are now in hand: prime conductors to 10¹⁰ and all
  conductors to 10⁸, though not complete. Round 10 used the prime tables. The torsion and isogeny rounds could be run
  again on the all-conductor tables.
- **Rounds that round 9 names:**
  - in classes of three or more curves, is the stretch factor the isogeny's degree?
  - does optimality pick the rounder member of a pair?
- **The handoff's unregistered patterns.** These are a common density near 0.614 at which group trends change sign,
  the 2.8% of curves with no rational point on the closed component, and the missing lattices beyond elongation
  13.2. Each needs fresh data and a registration.
- **Rank 3:** its shapes live in a five-dimensional space.

## Reproduce

```
# Cremona's allgens tables, conductors 0-499 999 (github.com/JohnCremona/ecdata; handoff_scripts/fetch_data.sh)
python -I run_all.py DATA_DIR OUT_DIR 4          # 287 955 curves, about 2 minutes on 4 workers
python -I analyse.py OUT_DIR/all_rows.json       # every number of 20 November, beside the handoff's
python -I watkins_compare.py OUT_DIR/all_rows.json
python -I saturation_sample.py DATA_DIR
python -I every_loop.py selftest                 # round 9: synthetic lattices and a pair outside the tables
python -I every_loop.py compute DATA_DIR PARTS_DIR 4
python -I every_loop.py score PARTS_DIR
python -I every_loop_after.py PARTS_DIR
```

## Sources

- J. E. Cremona, *Algorithms for Modular Elliptic Curves* (2nd ed., 1997), and the `ecdata` tables
  (github.com/JohnCremona/ecdata): the `allgens` files, conductor below 500 000.
- M. Watkins, "Some heuristics about elliptic curves", *Experiment. Math.* 17 (2008); arXiv math/0608766 (2006), §6.4.
- C. L. Siegel, on the invariant measure on spaces of lattices (cited by Watkins for the uniform law).
- The PARI Group, PARI/GP 2.15.4, through the `cypari` binding (2.5.7).
