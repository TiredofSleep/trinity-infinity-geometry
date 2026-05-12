# Submission Target: Integers / Journal of Number Theory

## Venue Options (ranked by fit)

### Option A: Integers — Electronic Journal of Combinatorial Number Theory
- **URL:** https://integers-ejcnt.org/
- **Format:** LaTeX (preferred), PDF accepted
- **Review:** Peer-reviewed, open access
- **Turnaround:** ~2-4 months
- **Why this venue:** Pure combinatorial number theory. The sinc² zero law and First-G law are exactly the kind of finite, verifiable results they publish. No framework knowledge required.
- **How to submit:** Email submission to the editor. See website for current editor contact.

### Option B: Journal of Number Theory (Elsevier)
- **URL:** https://www.sciencedirect.com/journal/journal-of-number-theory
- **Format:** LaTeX via Editorial Manager
- **Review:** Peer-reviewed
- **Turnaround:** ~3-6 months
- **Why this venue:** Higher impact. The First-G Law connects to RSA security and Montgomery pair correlation — broader appeal.
- **How to submit:** https://www.editorialmanager.com/jnt/

## Papers in This Folder

1. **WP_SINC2_ZERO_LAW.md** — The lead paper. Self-contained, 3-line proof, 3 corollaries. Verified for all primes 3..199.
2. **WP34_FIRST_G_LAW.md** — Companion. First non-unit at k = spf(b). 36,662 cases, 0 exceptions. Connects to RSA hardness.
3. **proof_d25_loop_closure.py** — Runnable verification script. Include as supplementary material.

## Submission Strategy

- Submit WP_SINC2_ZERO_LAW first (cleaner, shorter, most self-contained)
- Reference WP34 as "companion paper, available at [DOI]"
- Include proof script as electronic supplementary material
- The sinc² result needs NO TIG/CK context — it's pure prime arithmetic
- Mention the Zenodo DOI (10.5281/zenodo.18852047) for provenance

## What Needs Doing Before Submission

1. Convert markdown to LaTeX (standard article class)
2. Add proper bibliography (BibTeX entries for Montgomery, Shannon, Riemann)
3. Add MSC classification codes: 11A41 (primes), 11N05 (distribution of primes), 42A16 (Fourier coefficients)
4. Add keywords: sinc function, prime arithmetic, corridor, loop closure
5. Verify proof script runs cleanly on fresh Python install

## arXiv Strategy

- Submit to arXiv math.NT (Number Theory) simultaneously
- Need 2 endorsements for math.NT — currently have 1
- The sinc² paper is the strongest arXiv candidate (shortest, most self-contained)
- If endorsements are blocked: submit to math.CO (Combinatorics) which may have lower endorsement barriers
