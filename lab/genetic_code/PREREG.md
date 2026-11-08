# The genetic code: symmetry or optimum? (registered 2026-11-09, before its run)

> *how does this parallel our look at mitochondria?* · *do all 3 and the mitochondrial research in this next
> pass* — the author, 8 and 9 November 2026

**The fence.** This tests a reading in biology's own terms. It does not claim that the seven-level coin governs
genetic codes. Round 3 found a pattern: the best state sits on the symmetric side (even under the half turn), but
its symmetry does not pick it out; it is found by climbing. The question carried over:
- the vertebrate mitochondrial code keeps a third-letter symmetry everywhere: xyU and xyC mean the same, and so do
  xyA and xyG (pyrimidine with pyrimidine, purine with purine);
- the standard code breaks it at AUA and UGA.

Does error minimization itself pick the symmetric side?

**The setting** (standard, from the literature):
- *The cost.* Haig and Hurst's (1991) mean squared change in polar requirement (Woese's scale) over all
  single-letter changes between sense codons. Changes to or from a stop are left out. With a transition bias b,
  transitions (U and C, A and G) weigh 1 and transversions 1/b.
- *Random codes.* The code's own blocks of synonymous codons, with the 20 amino acids shuffled among them and the
  stops kept (Haig and Hurst 1991; Freeland and Hurst 1998).
- *Climbing.* Simulated annealing over every code with the vertebrate mitochondrial composition: each amino acid,
  and stop, keeps its number of codons. There are 96 chains of 200 000 swaps each, then a full polish. One run
  swaps single codons (every code); the other swaps third-letter half-boxes (only symmetric codes). Seeded
  (20261109).

[`code_symmetry.py`](code_symmetry.py) is committed with these predictions, before its run.

**G0. (Calibration.)** The standard code's MS0 is 5.194, Haig and Hurst's value. Between 5 × 10⁻⁵ and 3 × 10⁻⁴ of a
million random codes beat it; Haig and Hurst found 2 in 10 000, and a later run 114 in a million.
*Kill:* MS0 off by more than 0.0005, or a share outside the window.

**G1. (A guess.)** The vertebrate mitochondrial code is less optimized than the standard code: a larger share of
random codes with its own blocks beat it.
*Kill:* the share is the same or smaller.

**G2.** With transition bias (b = 2), the best code found over every code keeps the third-letter symmetry, at the
same cost as the best symmetric code found.
*Kill:* the best code found breaks the symmetry, or the two costs differ by more than 10⁻⁹.

**G3.** With equal weights (b = 1), the best code found breaks the third-letter symmetry. The symmetry of the
optimum follows the symmetry of the mutation weights, as the coin's sides follow the half turn.
*Kill:* the best code found keeps it.

**Expected standing, stated before the run.**
- G0 is a calibration against known results.
- G1 is contested in the literature. Freeland, Knight, Landweber and Hurst (2000) found the nonstandard codes less
  adaptive; a 2018 study under another measure found most alternative codes better.
- G2 and G3 test a known intuition quantitatively, inside one model: when transitions dominate, the
  purine/pyrimidine equivalence at the third letter adds fault tolerance.
- Novozhilov, Wolf and Koonin (2007) climbed in code space before, keeping the standard block structure. This
  study frees it.
