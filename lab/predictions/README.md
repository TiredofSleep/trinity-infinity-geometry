# The prediction ledger

*Fenced physics, in the lab: the author's dated bets on experiments, each written down before the deciding data
arrives. None of them is a premise of the base, the towers or the coin.*

Each bet in [`PREDICTIONS.md`](PREDICTIONS.md) records the author's words with their time, the prediction, its
status at registration, the result that would kill it, and the experiment that will decide it. Its status changes
only when that experiment reports.

| | bet | status at registration | decided by |
|---|---|---|---|
| P1 | Koide's relation gives the tau mass, 1776.969 MeV | consistent (PDG 1776.93 ± 0.09) | Belle II, BESIII |
| P2 | the same rule for neutrinos: normal ordering, sum 59.3 meV | open | JUNO; DESI, Euclid, CMB-S4 |
| P3 | the unitarity-triangle angle α is at least 90° | open | Belle II, LHCb |
| P4 | the matter dipole stays at least twice the kinematic value | open | Euclid, SPHEREx, Rubin, SKA |
| P5 | the neutron lifetime gap: the beam value (about 888 s) is right | open | J-PARC, BL3 |
| P6 | up-type quarks "turn" exactly 1/3 more than down-type | disfavored: it needs a top mass 4.6–7.8σ from the measured one | FCC-ee |
| P7 | neutrinos sit half a window (15°) past the charged leptons | +2.21σ with JUNO's first result | JUNO |
| P8 | the angle is exactly 2/9, so Koide's 2/3 gives way slightly | consistent; a standing fork with P1, 2.5 keV apart | beyond planned experiments |

**Sources.** P1 is Koide's relation (1981), with the cone reading of Foot (1994). P2's sign choice and P7 are
Brannen's (2006), and the near-coincidence δ ≈ 2/9 behind P8 is his too. The author's own are P3 to P6 and P8's
reading of 2/9 as a charge count. Rounds testing these ideas against the cube are in
[`../generation_loop/`](../generation_loop/README.md).

**Run.** `python ledger_math.py` recomputes every number in the ledger from the inputs at its top (numpy, scipy;
P8 needs mpmath). `python test_ledger.py` pins that output against `ledger_math.expected` and checks that each bet's
headline numbers also appear in its section of the ledger. Change an input, and the test fails until the ledger is
updated to match.

**What was not checked here.** The calculator reproduces every number in the ledger. The experimental inputs are
as the chat quoted them, and they were not each re-read at the source. The NuFIT 6.1 value in P2 and P7 is
second-hand by the ledger's own account.

**Not set up.** A scheduled job that watches new PDG, FLAG and experiment releases and flags any bet whose status
should change was proposed. Whether to run one is the author's call, and none is running.
