# void_lens: magic squares measured from their unoccupied center

The center value c/2 = (n^2+1)/2 is the point everything is measured from. In even order no cell holds it.
Subtracting it first ("measuring from the void") turns several old questions into short calculations.
Every claim here is pre-registered and scored in `PREREG.md`.

| result | status | script |
|---|---|---|
| det of MATLAB's odd magic(n) = (-1)^((n-1)/2) n^(n-1) (n^2+1)/2 prod over doubling-orbits O of (n^\|O\| - (-1)^\|O\|); never zero. Proves Robert Israel's 2015 OEIS A160523 conjecture (n^(n-1) divides det). Nonsingularity alone is implied by Manjunath & Ambikasaran 2022. Moler's 2012 question about all odd orders is answered no by singular 5x5 squares. | proof sketch in PREREG; exact match n = 3..61 | `void_lens.py` |
| MATLAB's doubly even magic(n) has rank 3 because, measured from the void, it is (1,-1,-1,1)-tiled signs times a rank-2 ramp (Moler 2012: "I don't see how") | **known**: Manjunath & Ambikasaran 2022, Theorem 9, prove rank 3 with the eigenpairs (M = U S U^T, U = [1, u, v]); the void form is the same factorization read from the center. Exact here for n = 4..64 | `void_lens.py` |
| Prime order: any p*pi1(L1) + pi2(L2) + 1 from cyclic Latin squares, any digit relabelings, is nonsingular; so all 28,800 pandiagonal 5x5 squares are | (1-w)-adic proof sketch; exhaustive at p = 5 | `padic_family.py` |
| Complement symmetry by an involution pair forces nullity >= \|(f_P+f_Q)/2 - 1\|; at order 4, singular <=> index >= 1 | proved; exhaustive on 880 | `void_lens.py` |
| Every 4x4 kernel has a void certificate; at order 5, 14 of 19 sampled singular squares do and 5 do not | exhaustion / sample | `kernel_voids.py` |

`python3 void_lens/void_lens.py --full` reproduces the registered Round 8 run (about 12 minutes, with a
10-minute annealing search). Without `--full` it runs a quick version that skips the search. `anneal5.c` is
the 5x5 sampler (source only; compile with `cc -O2 -o anneal5 anneal5.c -lm`). Its output is in
`squares5_annealed.txt`.

**Literature gate:** at order 4, singular <=> complement symmetry (Dudeney groups I-VI) is known: Trigg 1948;
Mattingly 2000; Staab et al. 2010 (arXiv:1007.3239); the 640/240 count is in Moler 2012. The closed form, the prime-order
theorem and the pandiagonal-5x5 corollary were not found in the sources checked. Do not call them new until a
fuller search is done.

**Independent referee (2026-10-24):** confirmed the closed form (n = 3..101), the proof, the prime-order
theorem (exhaustive at p = 5) and the pandiagonal 5x5 count with its own code. See PREREG.md.

**Second independent check (Claude Code, 2026-10-24): `void_lens_check.py`, 15 of 15.** It was written from the
claims alone and shares no code with this folder's scripts. It covers:
- the closed form against exact determinants by primes and CRT, for odd n = 3..61 (to 101 with `--long`);
- the doubly-even rank 3;
- every one of the 3,686,400 members of the p = 5 family;
- the void index on the 880, with Dudeney's two groups of 8 as its index-0 squares, and Staab et al.'s types A
  and B as its index-1 cases.

The literature for each claim is in PREREG.md's last section:
- **probably new:** the closed form, the prime-order family theorem and the pandiagonal 5x5 corollary, pending a
  fuller search;
- **known:** the doubly-even rank (2022);
- **small:** the void index generalizes Staab et al.'s two theorems.

`applications/`: the same counting reproduces published results in four fields: nanographene zero modes,
symmetric frameworks, cryptanalysis (DES complementation, linear structures), and prime-length sparse
recovery (Chebotarev). All six tests held. **Fence:** these reproduce known theorems, showing the same linear
algebra at work elsewhere. They claim nothing physical about magic squares and add nothing to those fields. Test A4
needs pycryptodome; without it, it is reported as skipped.
