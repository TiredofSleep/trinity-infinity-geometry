# The genetic code: symmetry or optimum? [FENCE]

> *how does this parallel our look at mitochondria?* · *do all 3 and the mitochondrial research in this next
> pass* — the author, 8 and 9 November 2026

Round 3 of the seven levels ([`../../towers/seven_levels/`](../../towers/seven_levels/README.md) §5) found the
best states on the symmetric side, even under the half turn, without their symmetry picking them out: they had to
be found by climbing. This study asks the same question of genetic codes, in biology's own terms. Four
predictions were registered before the run ([`PREREG.md`](PREREG.md), commit d2485b4), and two held. The script
is [`code_symmetry.py`](code_symmetry.py); its output is in [`code_symmetry.log`](code_symmetry.log), and
[`verify_code_symmetry.py`](verify_code_symmetry.py) rechecks the recorded results in seconds.

**The two codes.**
- The vertebrate mitochondrial code keeps a third-letter symmetry everywhere: xyU and xyC mean the same, and so
  do xyA and xyG (pyrimidine with pyrimidine, purine with purine). That is what lets mitochondria read their code
  with 22 tRNAs.
- The standard code breaks it at AUA and UGA. The usual history runs from the standard code to the mitochondrial
  ones, by codon reassignment (Osawa and Jukes), so the symmetric code came later.

**The setting** is Haig and Hurst's (1991): the mean squared change in polar requirement over all single-letter
changes between sense codons. A transition bias b weighs transitions (U and C, A and G) 1 and transversions 1/b.

## What held, and what died

- **G0, the calibration, held.**
  - The standard code's MS0 is 5.1936, Haig and Hurst's 5.194.
  - Of a million random codes with its blocks, 98 beat it. Haig and Hurst found 2 in 10 000; a later run, 114 in a
    million.
- **G1 died.** The vertebrate mitochondrial code is a little *more* optimized than the standard code, not less:
  51 of a million random codes with its own blocks beat it (MS0 5.1735). The literature is split on this, and
  this is one measure.
- **G2 died as registered, and the way it died is the result.**
  - With transitions weighed twice transversions, the best code found over every code costs 2.856163. That is
    exactly the cost of the best symmetric code. Yet it breaks the third-letter symmetry.
  - Two features of the model allow that, and neither is about biology:
    - the model weighs the three letters alike, so the optimum can carry its pairing at any letter;
    - the polar-requirement scale has ties: threonine and proline both have 6.6, leucine and isoleucine 4.9.
  - Merge the tied amino acids, and the best code is exactly pyrimidine/purine-symmetric at its second letter. Its
    only broken pairs there are four T/P and L/I swaps.
  - So the optimum's value lies on the symmetric side, but the symmetry does not pick out the code: equally good
    codes break it.
- **G3 held.** With every change weighed equally, the best code found costs 3.560945. It breaks the symmetry at
  every letter, even with the ties merged, and the best symmetric code costs 0.014 more (3.574844).
- **Beyond the scored round.** Both natural codes are far from the summit, as Novozhilov, Wolf and Koonin (2007)
  found for the standard code:
  - with transition bias, the standard code costs 4.66 and the mitochondrial 4.70, against 2.86 for the best found;
  - with equal weights they cost 5.19 and 5.17, against 3.56.

## The reading, and its fence [READING; FENCE]

- **The shape it shares with the seven levels.** The optimum sits on the side that the weights favour. When
  transitions dominate, that is the pyrimidine/purine-symmetric side, and the symmetry still does not pick out the
  winner. With the weights made neutral, the optimum leaves the symmetric side. The symmetry of the optimum
  follows the symmetry of the weights, as the coin's sides follow the half turn.
- **What it does not say.** Nothing here is about how codes evolved. The model leaves out:
  - position-specific misreading: the third letter is the one the ribosome misreads most (wobble);
  - amino-acid frequencies;
  - the tRNA machinery, which is what the mitochondrial symmetry actually serves.
- **Not the same group.** The codon table's third-letter pairing and the seven-level half turn are different
  groups. The parallel is in the shape of the question, not in shared mathematics.
- **The test that would decide more.** Run the same climb with Freeland and Hurst's (1998) position-specific
  misreading weights and a property scale without ties, registered first.
- **The first look.** The first look at mitochondria (May 2026) used the TIG tables. The September audit retired
  those tables, so its numbers do not stand. Only the method, a registered direction and then a null, carries over.

## Sources

- D. Haig and L. D. Hurst, "A quantitative measure of error minimization in the genetic code", *J. Mol. Evol.*
  **33** (1991) 412–417.
- S. J. Freeland and L. D. Hurst, "The genetic code is one in a million", *J. Mol. Evol.* **47** (1998) 238–248.
- S. J. Freeland, R. D. Knight, L. F. Landweber and L. D. Hurst, "Early fixation of an optimal genetic code",
  *Mol. Biol. Evol.* **17** (2000) 511–518.
- A. S. Novozhilov, Y. I. Wolf and E. V. Koonin, "Evolution of the genetic code: partial optimization of a random
  code for robustness to translation error in a rugged fitness landscape", *Biology Direct* **2** (2007) 24.
- C. R. Woese et al., polar requirement (1966); F. H. C. Crick, "Codon–anticodon pairing: the wobble hypothesis",
  *J. Mol. Biol.* **19** (1966); S. Osawa and T. H. Jukes on codon reassignment (1989).
- NCBI genetic codes, translation tables 1 and 2.
