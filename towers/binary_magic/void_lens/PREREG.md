# void_lens: measuring from the unoccupied center (pre-registration log)

Same rules as the other folders. Predictions are written before the code runs and never edited; scores are
appended. *translation* = forced by a derivation (a failure means a bug or a wrong derivation); *real* = a guess
that can lose.

## Round 8 (written 2026-10-24, before any script in this folder ran)

**Literature found before writing (Task 16):**
- Moler, "Magic Squares, Part 3, Linear Algebra" (MathWorks blog, 2012):
  - 640 of the 880 order-4 squares have rank 3 and 240 have rank 4, so the 640/240 split is **known**;
  - MATLAB's doubly-even magic(n) always has rank 3: "I don't see how today";
  - singly-even magic(n) has rank n/2 + 2;
  - for odd n, magic(n) appears to have full rank: "Frankly, I have no idea", and "it is likely that their sum
    has full rank as well".
- Loly (Wolfram 2006 talk): the six singular Dudeney groups vs the six non-singular ones; Franklin and
  most-perfect 8x8 squares have 3 nonzero eigenvalues.
- Even-order associative squares are singular (Mattingly 2000; Lee et al. 2012).

**Disclosure.** Before the derivation in Part A, I computed det(magic(n)) for odd n = 3..21 and factored it
(exploration, scratch). The closed form below was then derived by hand. Only n >= 23 is fresh data for D1.

### Part A: odd-order MATLAB magic(n) (de la Loubere / siamese), Moler's open question
MATLAB: A = mod(I+J-(n+3)/2, n), B = mod(I+2J-2, n), M = n*A + B + 1 (1-based I = row, J = column).

**Derivation (measure from the void).**
- Subtract the center value c/2 = (n^2+1)/2. Then N = M - (c/2)E = n*alpha(i+j) + beta(i+2j), where alpha and
  beta are zero-mean shifted sawtooths on Z_n. The void step is what makes both pieces zero-mean.
- In the Fourier basis e_k(j) = w^(kj), w = exp(2 pi i/n):
  - e_k maps to n*alpha^(k) e_(-k) + beta^(k/2) e_(-k/2);
  - e_0 is killed by N, and M e_0 = s e_0 with s = n(n^2+1)/2.
- So, apart from the line e_0, M is "diagonal + permutation times diagonal". Its determinant factors over the
  orbits O of k -> 2k on Z_n \ {0}.
- Each orbit contributes (n^|O| / prod_O (w^k - 1)) * (n^|O| - (-1)^|O|). The phase sum over an orbit is
  k(2^|O| - 1) = 0 mod n, and |alpha^| = |beta^|.

**Claimed closed form:** det magic(n) = (-1)^((n-1)/2) * n^(n-1) * (n^2+1)/2 * prod over orbits O of
(n^|O| - (-1)^|O|).
- Every factor is nonzero, so **magic(n) is nonsingular for every odd n**.
- Example: n = 5 has one orbit of length 4, so det = 5^4 * 13 * (5^4 - 1) = 5,070,000.

**General version.** Let M = n*rho(a1 i + b1 j + c1) + rho(a2 i + b2 j + c2) + 1, where rho = mod n and a1, b1,
a2, b2 are units mod n (two "linear" Latin squares).
- Column k of N lands on two Fourier rows, with magnitudes n*n/|w^x - 1| and n/|w^y - 1|.
- Over any cycle, the diagonal product beats the off-diagonal product by a factor of at least
  (n sin(pi/n))^L >= 2^L > 1, so the cycle determinant never vanishes.
- **Every odd-order square of this linear type is nonsingular, magic or not.**

| id | kind | prediction | kill condition |
|---|---|---|---|
| D1 | translation | The closed form equals the exact determinant of MATLAB's magic(n) for every odd n from 23 to 61 (fresh). n = 3..21 is rechecked and labelled as already seen. | Any mismatch. |
| D2 | translation | Exhaustively for n = 5 and 7, every parameter choice (a1, b1, a2, b2 units; c1, c2 any) gives det != 0. Also 2,000 random choices each for n = 9, 15, 21, 25 (composite n included). | Any zero determinant. |
| D3 | real | The linear family covers *every* pandiagonal 5x5 magic square: its magic members give 28,800 distinct pandiagonal squares, the known total counting rotations and reflections. If so, D2 proves every pandiagonal 5x5 square nonsingular. | A different count. |
| D4 | real | Singular natural 5x5 magic squares exist and are easy to find: a simple annealing search finds one within 10 CPU-minutes. This shows the theorem is about the construction, not the order. | None found. |

### Part B: Moler's "I don't see how" (doubly even) and his n/2 + 2 (singly even)
**Derivation.**
- MATLAB's doubly-even rule complements the cells where floor((I mod 4)/2) = floor((J mod 4)/2).
- In +-1 form that complement pattern is -sigma sigma^T, where sigma is (1,-1,-1,1) tiled. That is the order-4
  void vector chi_11, the kernel of the mirror-complement 4x4 squares.
- Measured from the void, the natural fill is a ramp n*u_i + w_j, with u and w odd about the center.
- So N = -n (sigma*u) sigma^T - sigma (sigma*w)^T has rank <= 2, and M = N + (c/2)E has rank <= 3.

| id | kind | prediction | kill condition |
|---|---|---|---|
| E1 | translation | For n = 4, 8, ..., 64: N equals the rank-2 formula entry by entry, and rank magic(n) = 3. | Any mismatch. |
| E2 | check of a published claim | Singly even magic(n) (LUX), n = 6, 10, ..., 62: rank = n/2 + 2. | Any other rank. |

### Part C: the void index bound for complement symmetries
**Derivation.**
- Suppose P M Q = cE - M for involutions P (rows) and Q (columns), with f_P and f_Q fixed points.
- Then M maps (A_Q + <1>) into S_P, and (S_Q orthogonal to 1) into A_P, where S and A are the +1 and -1
  eigenspaces.
- Counting dimensions: **nullity(M) >= |(f_P + f_Q)/2 - 1|**. The "-1" is the constant, measured-from
  direction. Examples:
  - even associative: f = 0, 0, so nullity >= 1;
  - odd associative: 1, 1, so the bound is 0 (the center is occupied);
  - a 4x4 mirror: 4, 0, so >= 1;
  - an 8x8 mirror: 8, 0, so >= 3.
- No cell may hold c/2 more than once, so f_P f_Q <= 1.
- For any square, the complement map is fixed (where c - x sits). A row-times-column complement symmetry
  exists iff that map factorises as (P(i), Q(j)), and then it is unique.

| id | kind | prediction | kill condition |
|---|---|---|---|
| I1 | translation | All 880: whenever the complement map factorises, nullity >= the bound. | Any exception. |
| I2 | real | Some 4x4 square has a factorised complement map of index 0 (one transposition times a fixed-point-free involution). | None. |
| I3 | real | Refined converse at order 4: a square is singular iff its complement map factorises with index >= 1. Index-0 symmetries, if they exist, sit on invertible squares. | A counterexample either way. |
| I4 | translation | Random affine fully binary 8x8 squares with a mirror complement (all value forms have odd column parity): nullity >= 3, on 500 samples. | Any exception. |
| I5 | real | None of the 2,000 annealed 8x8 squares (all non-singular per the atlas) has a factorised complement map. | One that does. |

## Round 8b (written after a quick debug run of Round 8 showed D3 failing, before the scripts below ran)
**What the debug run showed.** The affine-digit family gives only 800 of the pandiagonal 5x5 squares. The
missing ones relabel the digits by arbitrary permutations pi, and my magnitude argument needs sawtooth digits.

**Derivation (by hand): a p-adic version for prime order p.**
- Let M = p*pi1(a1 i + b1 j) + pi2(a2 i + b2 j) + 1, with pi1 and pi2 any permutations of Z_p and the a's and
  b's units.
- Centered at the void, column k of N lands on two Fourier rows, with coefficients p*f1^(k/b1) and
  f2^(k/b2), where f = pi - (p-1)/2 has zero mean.
- Work in Z[w] at the prime (1 - w), which has norm p:
  - p has valuation p - 1;
  - Galois conjugation permutes k, so f^(k) has the same valuation v for every k != 0;
  - f^ divisible by p would force all of pi's values to be congruent mod p, which is impossible for a
    permutation, so v <= p - 2.
- Over a cycle of length L, the two terms have valuations L(p - 1 + v1) and L v2 <= L(p - 2). They differ, so the
  cycle determinant is nonzero.
- **Every such square of prime order is nonsingular, for any digit relabelings, magic or not.**

| id | kind | prediction | kill condition |
|---|---|---|---|
| P1 | real (memory) | The extended family at p = 5 gives exactly 28,800 distinct pandiagonal magic squares. I recall that total, counting the 8 rotations and reflections, from the literature. If it holds, every pandiagonal 5x5 square is in the family, hence nonsingular. | Any other count. |
| P2 | translation | No zero determinant: (a) exhaustively over all pandiagonal members at p = 5; (b) 20,000 random members (any pi, any unit parameters) at each of p = 5, 7, 11, 13. | Any zero. |
| P3 | real | The p-adic argument does not extend to composite n: random members at n = 9, 15 and 25 with arbitrary pi include singular ones. | No zero in 20,000 each. |

### Round 8 scores (full run, `round8_full.log`; predictions above unchanged)
| id | result | outcome |
|---|---|---|
| D1 | the closed form equals the exact det for n = 23..61 (fresh), and 3..21 (seen) | **held** |
| D2 | 77,904 linear squares (exhaustive n = 5, 7; 2,000 each at n = 9, 15, 21, 25): no zero determinant | **held** |
| D3 | the affine-digit family gives 1,472 magic and 800 pandiagonal 5x5 squares, not 28,800 | **lost** (the family is too narrow; see 8b) |
| D4 | a singular natural 5x5 square, found after 179 annealed squares (348 s): [[7,16,12,11,19],[9,15,22,2,17],[20,23,13,3,6],[8,10,4,25,18],[21,1,14,24,5]], rank 4 | **held** |
| E1 | doubly even n = 4..64: N = -sigma sigma^T o (ramp), exactly, and rank 3 | **held** |
| E2 | singly even n = 6..62: rank n/2 + 2 | **held** (Moler's claim confirmed) |
| I1 | 880: every factorised complement map respects the bound | **held** |
| I2 | 16 squares have index-0 complement symmetries (11 of type f = 0,2 and 5 of type 2,0) | **held** |
| I3 | singular <=> factorised complement map of index >= 1, on all 880; the 16 index-0 squares are all invertible | **held** |
| I4 | 500 affine 8x8 mirror-complement squares: nullity 3 (186), 4 (305), 5 (9), never below 3 | **held** |
| I5 | 2,000 annealed 8x8 squares: none has a factorised complement map | **held** |

### Round 8b scores (`round8b.log`)
| id | result | outcome |
|---|---|---|
| P1 | the extended family at p = 5 gives exactly 28,800 pandiagonal magic squares. MathWorld gives 3,600 up to rotation and reflection, and x 8 = 28,800 (no magic square is fixed by a symmetry). | **held** |
| P2 | no zero determinant: all 28,800 pandiagonal members; 20,000 random members at p = 5, 7; 5,000 at p = 11, 13 | **held** |
| P3 | n = 9 has singular members (3 in 20,000; e.g. equal slopes (1,1,1,1) with digit maps [3,6,4,2,1,0,8,5,7] / [0,3,8,2,5,7,1,4,6], rank 7 by sympy). None found at n = 15 or 25 in 3,000 each. | **held** |

**Consequence of P1 + P2 + the 8b derivation:** every pandiagonal 5x5 magic square is nonsingular.
Not found in the literature checked so far; see the literature gate below.

**Tally, Round 8/8b real predictions:** D3 lost; D4, I2, I3, I5, P1 and P3 held, so **6 of 7**. Running record:
27 of 46.

### Post hoc observation (labelled; needs a fresh test)
D4's singular 5x5 square has columns 0 and 4 summing to 26 = c in every row. A pair of complementary lines is a
*local* void. It forces the kernel s(e_0 + e_4) - c 1, proportional to (3,-2,-2,-2,3), the null vector sympy
reports. More generally, any proper set S of columns (or rows) whose sum is a constant vector t 1 forces the
kernel s 1_S - t 1.

## Round 8c: does every kernel have a void? (written before `kernel_voids.py` ran)
**Two kinds of void certificate:**
- (a) *local*: a proper set S of rows or columns whose sum is a constant vector t 1;
- (b) *global*: a factorised complement map with void index >= 1.

Either one forces a kernel. The question is whether every singular natural magic square has one.
**Sample:** natural 5x5 squares from a C annealer (source `anneal5.c`, compiled in scratch, binary not shipped).
Deduplicated up to the 8 symmetries; 5 CPU-minutes of annealing.

| id | kind | prediction | kill condition |
|---|---|---|---|
| H1 | translation + real | 880: every square of type (4,0) or (0,4) has a local certificate (forced: a complementary pair). **Real part:** none of the 144 type-(0,0) squares has one; they are explained only globally. | Any type-(0,0) square with a local certificate. |
| H2 | real | Every singular 5x5 square in the sample has a void certificate, (a) or (b). | One singular square with neither. |
| H3 | real | Every local certificate in the 5x5 sample is a true complementary pair, with t = 26 = c. | A constant pair sum t != 26. |
| H4 | exploratory | The fraction of singular squares in the sample. Not a prediction. | -- |

### Round 8c scores (`round8c.log`)
| id | result | outcome |
|---|---|---|
| H1 | 880: every type-(4,0) and type-(0,4) square has a complementary line pair; none of the 144 type-(0,0) squares has any local certificate. At order 4, **every kernel has a void**: local for 496, global for 144. | **held** |
| H2 | 10,034 distinct annealed 5x5 squares, 19 singular (0.19%), all of rank 4. 14 have a complementary pair; **5 have no void certificate**. Their kernels are "accidental" small-integer relations, e.g. left kernel (-3,-2,4,1,0): 3 r0 + 2 r1 = 4 r2 + r3. | **lost** |
| H3 | all 14 local certificates are true complementary pairs (t = 26) | **held** |

**Tally:** Round 8c real predictions 2 of 3 (H1's real part, H3). Running record: **29 of 49.**

## Where Round 8 leaves the void lens
- **Proved, and verified on fresh data:**
  - **Moler's odd question (2012).** det magic(n) = (-1)^((n-1)/2) n^(n-1) (n^2+1)/2 prod_O (n^|O| - (-1)^|O|),
    where O runs over the orbits of doubling mod n. So MATLAB's odd magic(n) is never singular.
  - **Moler's "I don't see how".** Doubly even magic(n) = (c/2)E - sigma sigma^T o (n u 1^T + 1 u^T). That is
    rank <= 3, and the sign pattern is the order-4 void vector (1,-1,-1,1) tiled.
  - **Prime order.** Every square p*pi1(L1) + pi2(L2) + 1 built from two cyclic Latin squares with any digit
    relabelings is nonsingular ((1 - w)-adic valuations). Hence **all 28,800 pandiagonal 5x5 squares are
    nonsingular**.
  - **Void index bound.** A complement symmetry by an involution pair forces nullity >= |(f_P + f_Q)/2 - 1|.
    At order 4 this is exact: singular <=> index >= 1. The 16 index-0 squares are the invertible ones that still
    have a complement symmetry.
- **Where it stops:** at order 5, 5 of 19 singular squares have no void certificate. Kernels are not always
  voids.
- **Literature gate (open):** the odd closed form, the prime-order family theorem and pandiagonal-5x5
  nonsingularity were not found in what was checked (Moler 2012; Loly 2006; Wikipedia; MathWorld). An
  independent referee is checking claims and literature.

## Round 8d: pandiagonal 7x7 (written before `pandiag7.py` ran)
**Sample:** natural pandiagonal 7x7 squares (all 7 rows, 7 columns and 14 broken diagonals sum to 175) from a C
annealer (`anneal7p.c`), 4 CPU-minutes. A square is "in the family" if its two base-7 digit squares are each
a cyclic Latin square up to relabeling (level sets are lines a i + b j = const).

| id | kind | prediction | kill condition |
|---|---|---|---|
| Q1 | real | Some sampled pandiagonal 7x7 squares are *not* in the cyclic family, so the 8b theorem does not cover all of them. | Every sampled square is in the family. |
| Q2 | real | Every sampled pandiagonal 7x7 square is nonsingular, in the family or not. | A singular one. |

### Round 8d status: not run (method failure, recorded so the predictions stay visible)
The annealer found **no** pandiagonal 7x7 square: 0 of 143 runs over about 40 s, across two tunings. That is
far short of the 4-minute budget, and swap-move annealing is clearly the wrong sampler for 28 rigid lines.
Q1 and Q2 stay **unscored**.

**Next attempt:** build pandiagonal 7x7 squares directly from pairs of orthogonal pandiagonal Latin squares,
including non-cyclic ones if any exist at order 7. Check the literature on non-cyclic pandiagonal Latin
squares first. `anneal7p.c` is kept as the record of what was tried.

## Round 8e: the lemma behind 8b (written before running)
| id | kind | prediction | kill condition |
|---|---|---|---|
| P4 | translation | For every permutation pi of Z_p (exhaustive p = 5, 7; 20,000 random at p = 11, 13), the centered transform f^(1) = sum_x (pi(x) - (p-1)/2) w^x has p-adic norm valuation v = v_p(N(f^)) with 1 <= v <= p - 2. | Any v = 0 or v >= p - 1. |

### Round 8e score (`round8e.log`)
| id | result | outcome |
|---|---|---|
| P4 | valuations seen: p = 5: {1, 3}; p = 7: {1, 2, 5}; p = 11: {1, 2, 3, 4, 7}; p = 13: {1, 2, 3, 4}. Always 1 <= v <= p - 2, and the bound is reached at p = 7. The first run used 2,000 samples at p = 11, 13 because of a code typo; it was rerun at the registered 20,000. | **held** |

## Corrections and a post hoc observation (2026-10-24, after Claude Code's literature check)
- **Literature, corrected.**
  - At order 4, "singular exactly when a complement symmetry exists" is **known**: these are Dudeney's (1917)
    groups I-VI.
  - The singularity goes back to Trigg (1948), with general proofs by Mattingly (2000) for even associative
    squares and by Staab et al. (arXiv:1007.3239, 2010) for symmetric permutation classes.
  - My Round 7 note credited Lee et al. for that general proof; that was wrong. Lee et al. (2012) concern
    odd-order nonsingular regular squares.
  - What still looks new from Round 7: one uniform proof with explicit kernels, and the impossibility of
    single-plane certificates.
- **Post hoc (labelled; computed after the fact).** The void index sorts Dudeney's 12 groups exactly:
  - groups of size 304, 96, 96, 48, 48 and 48: complement symmetry of index 1, all singular;
  - the four groups of 56: no complement symmetry, all invertible;
  - the two groups of 8: a complement symmetry of **index 0** (it fixes exactly two lines), all invertible.
  - So the index explains why Dudeney's two 8-square groups escape singularity although their complement pairs
    sit symmetrically. Whether this is in Staab et al. has not been checked.

## Independent referee (separate agent, own code, did not read this folder), 2026-10-24
- **Claim 1 (closed form) CONFIRMED** for every odd n from 3 to 101, against MATLAB's magic.m source text.
- **Claim 2 (proof) CONFIRMED**, prime or composite n. The referee added the omitted steps:
  - the sign of k -> -k;
  - the explicit phases;
  - S_O = 0 mod n;
  - prod (w^k - 1) = n.
- **Claim 3 (prime order) CONFIRMED:**
  - exhaustive at p = 5 (3,686,400 matrices, none singular);
  - the valuation lemma, exhaustive at p = 5 and 7;
  - a sharper prediction, v_p(det M) = 1 + v(pi2), held in 180k random cases;
  - an independent enumeration of pandiagonal 5x5 squares gives the same 28,800 (min |det| 73,125).
- **Claim 4 CONFIRMED, and stronger:** some singular 9x9 members are genuine magic squares, including a digit
  relabeling of MATLAB's own magic(9) (rank 7). The mechanism: equal residue-class sums mod 3 kill the
  coefficients alphahat(3) and betahat(3).
- **Literature (corrects my framing):**
  - Moler's 2012 question was about *all* odd-order magic squares. That is answered "no" by singular 5x5 squares
    (D4 found one; probably known earlier).
  - For MATLAB's squares, nonsingularity is *implied but never stated* by Manjunath & Ambikasaran
    (arXiv:2205.15563, 2022), through an eigenvalue bound.
  - OEIS A160523 lists det(magic(n)). Robert Israel (2015) conjectured divisibility by n^(n-1) there; **the closed
    form proves that conjecture**.
  - No closed form was found anywhere. The pandiagonal 5x5 corollary and the prime-order family theorem were not
    found either.

## Independent check and literature gate (Claude Code, 2026-10-24; the predictions and scores above are unchanged)
**Independent check:** `void_lens_check.py` was written from the claims alone and shares no code with this
folder's scripts. 15 of 15 checks pass, about 10 s.
- **A.** The siamese rule itself, checked against MATLAB's documented magic(3) and magic(5).
  - Exact determinants by elimination modulo primes and CRT past the Hadamard bound: the closed form holds for
    every odd n = 3..61, and 3..101 with `--long` (`void_lens_check_long.log`).
  - It reproduces OEIS A160523's printed terms.
- **B.** MATLAB's doubly-even rule, read directly. For n = 4..64, 2M - (n^2+1)E = -(sigma sigma^T) o (n a 1^T + 1 a^T),
  so rank <= 3, and the rank modulo a prime is 3, so rank = 3.
- **C.** Every member of the p = 5 family (all pi1, pi2 in S_5 and all unit slopes, 3,686,400 matrices) is
  nonsingular by batched LU determinants; the smallest |det| is 8,125.
  - 67,500 random members at p = 7 are nonsingular too.
  - The n = 9 member given above is singular, of rank 7.
  - The family's pandiagonal magic 5x5 members number 28,800.
- **D.** On the 880, the complement map factors over involutions exactly as stated:
  - (0,0): 144, (0,4): 208, (4,0): 288, all of index 1 and singular;
  - (0,2): 11 and (2,0): 5, of index 0 and invertible;
  - none: 224.
  The 16 index-0 squares are exactly Dudeney's two groups of 8.

**Literature (each claim):**
- **A, closed form for MATLAB's odd magic(n).**
  - OEIS A160523 (Bjerkeng 2009) lists the determinants. Robert Israel (2015) noted there that for n >= 3, a(n) = 0
    iff n is even, proved that n^(n-2) divides a(n), and observed that n^(n-1) appears to.
  - Manjunath & Ambikasaran (arXiv:2205.15563, Theorem 1) approximate the odd eigenvalues by n^2/(2 sin(j pi/n))
    with relative error <= 1/n. That keeps every eigenvalue at least n(n-1)/2 from 0, so nonsingularity follows,
    though they never say so. They give no determinant.
  - The closed form was not found anywhere checked. It proves Israel's observation and nonsingularity for every
    odd n. **Probably new.**
- **B, the doubly-even rank 3: KNOWN.** Manjunath & Ambikasaran (2022), Theorem 9, prove rank 3 with explicit
  eigenpairs, through a factorization M = U S U^T with U = [1, u, v].
  - That answers Moler's 2012 "I don't see how today".
  - The void form here is the same factorization, read from the center: an elementary restatement, not new.
- **C, the prime-order family and pandiagonal 5x5.**
  - Related prior work: Lee, Love, Narayan, Wascher & Webster (LAA 437, 2012) construct nonsingular regular magic
    squares of odd prime and prime-power orders, with centroskew S-circulant matrices. Jitjankarn & Rungratgasame
    (Mat. Vesnik 74, 2022) do so for every odd order by bordering.
  - The technique, valuations at (1 - w) in Z[w], is the classical one behind Chebotarev's theorem that every
    minor of the prime-order DFT is nonzero (see Tao 2005); `applications/` test A6 is that theorem.
  - The family theorem (any digit relabelings, prime p) and "every pandiagonal 5x5 magic square is nonsingular"
    were not found. **Probably new, pending a fuller search:** Rosser & Walker (1938-39) on diabolic squares, and
    Loly, Cameron, Trump & Schindel (LAA 2009), which are not read.
  - That every pandiagonal 5x5 square comes from two Latin squares (P1) is probably classical.
- **D, the void index.**
  - Staab et al. (arXiv:1007.3239) Theorems 12-13 are its two special cases: type A (f = (0,0), nullity >= 1) and
    type B of order 2m (f = (0, 2m), rank <= m + 1, which is the index bound exactly).
  - The bound for partial fixed points was not found there. Nor was the order-4 picture: singular iff index >= 1,
    with Dudeney's two groups of 8 as the index-0 squares, since Staab et al.'s permutation classes require trace 0.
  - **Small, probably new.**
- **E, order 5.** 5 of 19 annealed singular squares have no void certificate. This is a proven limit of the lens,
  with its evidence in `round8c.log`.
- **F, applications.** These are translation tests of known theorems: Lieb 1989 on zero modes, Fowler & Guest 2000
  on symmetric frames, the DES complementation property (1977), linear structures, and Chebotarev.
  - They show the same linear algebra at work elsewhere. They claim nothing about magic squares and add nothing to
    those fields.
  - Test A4 needs pycryptodome. Without it the flagship run reports A4 as skipped, not passed.
