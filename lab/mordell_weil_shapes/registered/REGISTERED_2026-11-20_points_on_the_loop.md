# Registered before looking: do the points reach the loop?

Written 2026-11-20, about 23:24 US Central. Not yet computed on any data.

**Statement (Brayden, 23:20):** "Maybe points and angles are the birth of a loop.. they are like the opposite
of a loop, if that's possibly imaginable."

**What is exact in it (Claude; classical, no test needed).**
- *Opposite of a loop.* Pontryagin duality: the dual of the circle is the integers and the dual of the
  integers is the circle. A point of infinite order generates a copy of ℤ. Its dual object is a loop.
- *Birth of a loop.* The multiples of a real point of infinite order never close up, but they fill the
  component they live on densely and evenly (Kronecker, Weyl). The closure of the angle is the loop.

**The test.** A curve with positive discriminant has two real pieces: the unbounded one, which contains the
identity, and the closed loop (the "egg"). Rational points either all lie on the unbounded piece, or half
of them (a coset of an index-2 subgroup) lie on the egg. With trivial torsion, the egg carries rational
points exactly when at least one of the two generators lies on it.

- **P1.** Among loop-free rank-2 curves with positive discriminant, curves whose rational points reach the
  egg have higher mean packing density than curves whose points all stay on the unbounded piece.
  (Direction from Brayden's "only curves that can loop" pack.) Pass: positive, above three standard errors.
  Miss: zero or negative.
- **P2 (two-sided, recorded):** whether the strong dependence on the curve's own shape (Spearman −0.128
  with Im τ) is carried by one of the two classes.

**Stated beforehand:** the egg is bounded, so a point on it has bounded x-coordinate and can more easily
have small height. That could make one side of the triangle short and the packing *worse*. So the mundane
expectation, if anything, runs against P1.

---

# Outcome (`scripts/egg.py`, `scripts/egg_test.py`; registered 23:20 CST, computed after)

Loop-free rank-2 optimal curves with positive discriminant, conductor below 500 000 (75 476 with both
generators located; 5 curves dropped by a floating-point tolerance on the real roots).

| | n | mean density | thin share | median shortest side | median Im τ |
|---|---|---|---|---|---|
| rational points reach the egg | 73 331 | 0.5481 | 21.1% | | 1.504 |
| all points on the unbounded piece | 2 145 | 0.5254 | 25.7% | 0.813 | 1.894 |
| — one generator on the egg | 47 807 | 0.5517 | | 0.701 | |
| — both generators on the egg | 25 524 | 0.5414 | | 0.762 | |

**P1: pass.** Difference +0.0227, standard error 0.0037, 6.1 standard errors. The mundane expectation
stated beforehand ran the other way and was wrong in direction: the shortest side *is* smaller when a
generator sits on the egg (0.70 against 0.81), and the packing is still better.
("One on the egg" and "both on the egg" are the same situation in different bases, since P and P + Q
generate the same lattice; the split between them reflects how the tables chose generators.)

**P2.** The dependence on the curve's own shape is present in both classes: Spearman −0.126 where the
points reach the egg, −0.161 where they do not (7.4 standard errors on 2 145 curves).

**Confound to remove.** Curves whose points miss the egg have more elongated period lattices (median Im τ
1.89 against 1.50), and elongation lowers packing. Compare within matched bands of Im τ before quoting the
+0.023. In the density-by-fifths tables the miss-the-egg class is lower in every fifth, but the fifths are
cut at different places in the two classes.

**Unpredicted, and possibly the better question.** Only 2.8% of these curves have all their rational points
on the unbounded piece. If each generator landed on either piece independently and evenly, it would be 25%.
Find out whether this strong preference for reaching the egg is known (it may follow from how small points
arise, or from the tables' ordering by conductor) before treating it as new.

**Illustration of "the birth of a loop" (classical).** On 389a1 the first 5 000 multiples of one generator,
placed by their elliptic logarithm around the real curve, are spread evenly: largest gap 0.00043 of the way
round against 0.00020 for perfectly even spacing.
