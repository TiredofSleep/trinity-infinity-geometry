"""
paradox_map.py — does paradox point to treasure? A tally with the misses left in.

Types (after Quine, "The Ways of Paradox", 1966, plus empirical anomalies):
  ANTINOMY    two accepted, independently checked rules cannot both hold
  VERIDICAL   true but surprising (the conclusion is right; intuition was wrong)
  FALSIDICAL  a fallacy (the argument has a hidden error)
  ANOMALY     a measurement disagrees with accepted theory
Outcomes:
  NEW      led to new structure (a theory, concept or object that did not exist before)
  CLARIFY  resolved inside existing theory; no new structure
  ERROR    the paradox itself was a mistake (bad data, bad reasoning, noise)
  OPEN     unresolved

The classifications are judgment calls. Famous paradoxes are biased toward ones that paid off, so
well-known anomalies that evaporated are included on purpose.
"""
from collections import Counter, defaultdict

P = [
    # name, type, outcome, one-line resolution
    ("Incommensurability of the diagonal (sqrt 2)", "ANTINOMY", "NEW", "Eudoxus' proportions, later the real numbers"),
    ("Russell's paradox", "ANTINOMY", "NEW", "axiomatic set theory, type theory"),
    ("Liar paradox", "ANTINOMY", "NEW", "Tarski's undefinability of truth; object/metalanguage"),
    ("Berry paradox", "ANTINOMY", "NEW", "Chaitin's incompleteness via description length"),
    ("Burali-Forti / Cantor's largest cardinal", "ANTINOMY", "NEW", "proper classes"),
    ("Richard's paradox", "ANTINOMY", "NEW", "the diagonal method Goedel turned into a theorem"),
    ("Sorites (the heap)", "ANTINOMY", "OPEN", "several logics of vagueness, no consensus"),
    ("Newcomb's problem", "ANTINOMY", "OPEN", "split between evidential and causal decision theory"),
    ("Condorcet voting cycles", "ANTINOMY", "NEW", "Arrow's impossibility theorem, social choice"),
    ("St Petersburg paradox", "ANTINOMY", "NEW", "expected utility (Bernoulli 1738)"),
    ("Allais paradox", "ANTINOMY", "NEW", "non-expected-utility and prospect theory"),
    ("Ellsberg paradox", "ANTINOMY", "NEW", "models of ambiguity aversion"),
    ("Ultraviolet catastrophe", "ANTINOMY", "NEW", "Planck's quanta"),
    ("Gibbs mixing paradox", "ANTINOMY", "NEW", "indistinguishable particles, quantum statistics"),
    ("Maxwell's demon", "ANTINOMY", "NEW", "Landauer's principle, thermodynamics of information"),
    ("D'Alembert's paradox (zero drag)", "ANTINOMY", "NEW", "Prandtl's boundary layer"),
    ("Stokes' paradox (2D creeping flow)", "ANTINOMY", "NEW", "Oseen's equations, matched asymptotics"),
    ("Klein paradox", "ANTINOMY", "NEW", "pair creation; quantum field theory"),
    ("EPR paradox", "ANTINOMY", "NEW", "Bell's theorem, entanglement"),
    ("Olbers' paradox (dark night sky)", "ANTINOMY", "NEW", "a universe of finite age"),
    ("Ehrenfest paradox (spinning disk)", "ANTINOMY", "NEW", "non-Euclidean geometry in rotating frames, a step toward GR"),
    ("Black hole information paradox", "ANTINOMY", "OPEN", "productive (holography, Page curve) but unresolved"),
    ("Twin paradox", "ANTINOMY", "CLARIFY", "resolved inside special relativity (proper time)"),
    ("Ladder-in-barn paradox", "ANTINOMY", "CLARIFY", "relativity of simultaneity"),
    ("Abraham-Minkowski momentum of light", "ANTINOMY", "CLARIFY", "both correct for different momenta (Barnett 2010)"),
    ("Galileo's squares paradox", "VERIDICAL", "NEW", "Cantor's cardinality, centuries later"),
    ("Banach-Tarski", "VERIDICAL", "NEW", "von Neumann's amenable groups"),
    ("Braess's paradox", "VERIDICAL", "NEW", "selfish routing, price of anarchy"),
    ("Simpson's paradox", "VERIDICAL", "NEW", "causal inference (do-calculus)"),
    ("Parrondo's paradox", "VERIDICAL", "NEW", "a modest theory of combined losing games / ratchets"),
    ("Skolem's paradox", "VERIDICAL", "CLARIFY", "set-theoretic notions are model-relative"),
    ("Hilbert's hotel", "VERIDICAL", "CLARIFY", "an illustration of existing cardinality"),
    ("Birthday paradox", "VERIDICAL", "CLARIFY", "plain counting"),
    ("Monty Hall", "VERIDICAL", "CLARIFY", "conditional probability"),
    ("Bertrand's chord paradox", "VERIDICAL", "CLARIFY", "the sampling measure must be specified"),
    ("Jevons paradox", "VERIDICAL", "CLARIFY", "rebound effect, ordinary economics"),
    ("Feynman's reverse sprinkler", "VERIDICAL", "CLARIFY", "ordinary fluid mechanics (experiment 2024)"),
    ("Hydrostatic paradox", "VERIDICAL", "CLARIFY", "pressure depends on depth only"),
    ("Zeno's paradoxes", "FALSIDICAL", "NEW", "limits and convergent series, built mostly for other reasons"),
    ("Two-envelope paradox", "FALSIDICAL", "ERROR", "an illegitimate expectation"),
    ("Missing-dollar riddle", "FALSIDICAL", "ERROR", "misleading bookkeeping"),
    ("Mercury's perihelion", "ANOMALY", "NEW", "general relativity"),
    ("Uranus' orbit", "ANOMALY", "NEW", "a new object (Neptune), same laws"),
    ("Michelson-Morley null result", "ANOMALY", "NEW", "special relativity"),
    ("Solar neutrino deficit", "ANOMALY", "NEW", "neutrino oscillation and mass"),
    ("Fermi-Pasta-Ulam-Tsingou recurrence", "ANOMALY", "NEW", "solitons, integrability"),
    ("Galaxy rotation curves", "ANOMALY", "OPEN", "dark matter or modified gravity"),
    ("Hubble tension", "ANOMALY", "OPEN", "unresolved"),
    ("Neutron lifetime (beam vs bottle)", "ANOMALY", "OPEN", "unresolved"),
    ("Faint young Sun", "ANOMALY", "OPEN", "unresolved"),
    ("Fermi paradox", "ANOMALY", "OPEN", "no new structure yet"),
    ("Electron-channeling clock dip", "ANOMALY", "OPEN", "one experiment, unreplicated"),
    ("Muon g-2", "ANOMALY", "CLARIFY", "closed mostly by a better Standard Model calculation (lattice)"),
    ("Proton radius puzzle", "ANOMALY", "ERROR", "older hydrogen measurements were off"),
    ("Pioneer anomaly", "ANOMALY", "ERROR", "thermal recoil"),
    ("OPERA faster-than-light neutrinos", "ANOMALY", "ERROR", "a loose fibre connector"),
    ("BICEP2 primordial B-modes", "ANOMALY", "ERROR", "galactic dust"),
    ("750 GeV diphoton bump", "ANOMALY", "ERROR", "statistical fluctuation"),
    ("Cold fusion", "ANOMALY", "ERROR", "not reproducible"),
    ("N-rays", "ANOMALY", "ERROR", "observer bias"),
    ("Polywater", "ANOMALY", "ERROR", "contamination"),
]

# This session's own paradox-like pushes, scored the same way.
SESSION = [
    ("Pattern '1s->2s with 4s->8s' never occurs among the 880", "ANTINOMY", "NEW", "forced-empty proof; the carry formalism"),
    ("Trefoil regions match Takemura's unrelated classes", "ANOMALY", "NEW", "degree 3 = invertible; parity theorem"),
    ("The fold is universal at 4x4 but absent at 8x8", "ANTINOMY", "NEW", "proof; law vs family"),
    ("Mermin grid closes for qubits, not qutrits", "ANTINOMY", "NEW", "the 1 = -1 proof"),
    ("'0 48 64 192 0' as a sequence law", "RESEMBLANCE", "ERROR", "the user meant trefoil regions"),
    ("SYK phase diagram looks like a coin with a vortex", "RESEMBLANCE", "ERROR", "pareidolia"),
    ("Verlinde's 400,000 matches the Still Point miss", "RESEMBLANCE", "ERROR", "coincidence of a number"),
    ("3-6-9 meme", "RESEMBLANCE", "ERROR", "digital roots mod 9"),
    ("'Structure lens charged, flow lens balanced'", "RESEMBLANCE", "ERROR", "ran backwards against the toy"),
    ("Dual-lens push", "RESEMBLANCE", "ERROR", "smuggled retired readings; the forced part already existed"),
]

def table(rows, title):
    by = defaultdict(Counter)
    for _, t, o, _ in rows:
        by[t][o] += 1
    print(f"\n{title}")
    print(f"  {'type':12s} {'n':>3s} {'NEW':>4s} {'CLARIFY':>8s} {'ERROR':>6s} {'OPEN':>5s}   hit rate (NEW / resolved)")
    for t in ("ANTINOMY", "VERIDICAL", "FALSIDICAL", "ANOMALY", "RESEMBLANCE"):
        c = by.get(t)
        if not c:
            continue
        n = sum(c.values()); resolved = n - c["OPEN"]
        rate = f"{c['NEW']}/{resolved} = {c['NEW'] / resolved:.0%}" if resolved else "-"
        print(f"  {t:12s} {n:3d} {c['NEW']:4d} {c['CLARIFY']:8d} {c['ERROR']:6d} {c['OPEN']:5d}   {rate}")

table(P, f"History ({len(P)} paradoxes and anomalies)")
table(SESSION, f"This session ({len(SESSION)} items)")
anom = [r for r in P if r[1] == "ANOMALY" and r[2] != "OPEN"]
print(f"\nAnomalies alone: {sum(r[2] == 'NEW' for r in anom)} of {len(anom)} resolved ones became new structure;"
      f" {sum(r[2] == 'ERROR' for r in anom)} were mistakes.")
