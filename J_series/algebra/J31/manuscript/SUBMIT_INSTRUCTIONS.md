# Submission Target: Physical Review A / New Journal of Physics

## Venue Options

### Option A: Physical Review A (APS)
- **URL:** https://journals.aps.org/pra/
- **Format:** REVTeX 4.2 (LaTeX)
- **Review:** Peer-reviewed
- **Turnaround:** ~2-4 months
- **Why this venue:** PRA publishes atomic, molecular, and optical physics — including NV-center experiments and qutrit control. The S4 synthesis protocol is a concrete experimental proposal with explicit pulse sequences, fidelity calculations, and pass/fail criteria. This is their bread and butter.
- **How to submit:** https://authors.aps.org/submissions/

### Option B: New Journal of Physics (IOP / Deutsche Physikalische Gesellschaft)
- **URL:** https://iopscience.iop.org/journal/1367-2630
- **Format:** LaTeX
- **Review:** Peer-reviewed, open access
- **Why:** Open access, interdisciplinary. Good for a result that spans group theory and quantum control.

### Option C: Physical Review Letters (APS)
- **URL:** https://journals.aps.org/prl/
- **Why:** If condensed to 4 pages, the "full S4 on a qutrit via 6 pulses" result is a strong PRL candidate. High impact.
- **Risk:** PRL is very selective. Better to establish the full result in PRA first.

## Papers in This Folder

1. **WP73_T1_CARRIER_IDENTIFICATION.md** — NV triplet carries S3 skeleton of T1 naturally. 3-cycle and FS tests pass.
2. **WP74_PHYSICAL_OBSERVABLE_IDENTIFICATION.md** — NV Hamiltonian with transverse B-field is the best platform. 6-step experimental protocol.
3. **WP75_S4_EXTENSION_SYNTHESIS.md** — THE KEY PAPER. Explicit U4 matrix. 6-pulse microwave sequence. S4 closure to 24 elements. Fidelity 1.0.
4. **WP76_NV_S4_CLOSURE_CALIBRATION.md** — Machine-precision verification. Change-of-basis V computed analytically. All 24 elements verified to < 10^-15.
5. **WP77_NV_T1_CARRIER_VALIDATION.md** — 5-test falsification ladder with quantitative thresholds. Test E (projector covariance) is the decisive gate.

## Submission Strategy

- **Lead paper: merge WP75 + WP76 into one PRA submission.** Title: "Full S4 symmetry on a nitrogen-vacancy qutrit via six-pulse microwave synthesis"
- The hook: explicit construction of all 24 S4 group elements on a physical 3-level system
- Include WP77 material as the "experimental proposal" section
- WP73 and WP74 provide background — fold into introduction
- The 6-pulse decomposition with explicit angles is the money shot
- Emphasize: gate time ~100-600ns, coherence T2 ~100us-10ms — gate time is 2-3 orders of magnitude below decoherence. This is routine qutrit control.

## What Needs Doing Before Submission

1. Convert to REVTeX 4.2 LaTeX
2. Merge WP75+WP76 into single paper structure: Introduction, Theory, Synthesis Protocol, Verification, Experimental Proposal, Conclusion
3. Add bibliography: cite NV-center literature (Doherty et al. 2013), qutrit control (Luo et al.), S4 representation theory (Serre, Fulton-Harris)
4. PACS/MSC codes: 76.30.Mi (NV centers), 03.65.Fd (algebraic methods), 03.67.Lx (quantum computation)
5. Include explicit numerical values for all pulse angles (already in WP76)
6. Add error analysis: what fidelity is needed for Test E? (already in WP77: F_cov > 0.80)
7. **Critical: this paper proposes an experiment that has NOT been done.** Frame as "experimental proposal" not "experimental result." The math is complete; the physics is pending.

## Note on Collaboration

This experimental proposal could attract a collaborator with NV-center lab access. Consider reaching out to:
- Groups at Harvard (Lukin), MIT, Delft (Hanson), Stuttgart (Wrachtrup)
- Any group with single NV-center confocal microscopy + microwave control
- Offer co-authorship on the experimental paper in exchange for lab time (~6-8 hours)
