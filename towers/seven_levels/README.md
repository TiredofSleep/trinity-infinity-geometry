# Seven levels: the two faces of 7 on a quantum system

> *how can these viewpoints syncronize to our viewing space for quantum parts?* · *what extensions would this
> imply? test them?* — the author, 7 November 2026

### Tags: **[FORCED]** checked by [`verify_seven_levels.py`](verify_seven_levels.py) · **[NAMED]** a cited standard result · **[READING]** an interpretation · **[FENCE]** outside the mathematics.

**Keywords:** magic states · Wigner negativity · discrete Wigner function · qudits · Clifford hierarchy · Kloosterman sums · Sato–Tate law · Weil representation · quantum chaos · quantum cat map · Walsh spectra · bent functions · elliptic curves · finite fields · pre-registered predictions

**Pages here:** [`NORM_STATE.md`](NORM_STATE.md), the norm state's Kloosterman values, proved · [`TORUS_MOMENTS.md`](TORUS_MOMENTS.md), the fourth-moment theorem and the semicircle · [`DETERMINANTS.md`](DETERMINANTS.md), the determinants of the Airy pieces, proved (Theorem 8) · [`LITERATURE_MAP.md`](LITERATURE_MAP.md), who else works on this ground · [`PREREG.md`](PREREG.md), every registration and score, rounds 1 to 28 · [`COIN_AT_FIVE.md`](COIN_AT_FIVE.md), the coin at 5 in the fifth moment, the cubics from 7 to 81, the prime 3, and the coin's edge · [`modular_symbols.py`](modular_symbols.py), the engine that names the modular forms · [`verify_seven_levels.py`](verify_seven_levels.py), every check. Rounds: 1 §2–3, 2 §4, 3 §5, 4 §6, 5 §7, 6 §8, 8 §9, 7 §10, 9 §11, 10 §12, 11 and 12 §13, 13 §14, 14 §15, 15 §16, 16 §17, 17 §18, 18 §19, 19 and 20 §20, 21 to 28 §21.

**A side floor of the number tower**, built on the sevenths of [`../../base/SEVENTHS.md`](../../base/SEVENTHS.md).
- A quantum system with seven levels, |0⟩ to |6⟩, is indexed by the seven remainders mod 7, so both faces of 7
  act on it.
- This page says how, and says what our three-dimensional space can and cannot hold.
- Eight predictions were registered before the run ([`PREREG.md`](PREREG.md)). Seven held and one died.
- A second round of five, on the most negative state, was registered after that one died. All five held (§4).
- A third round of ten took up the three questions round 2 left open, registered with its script. Nine held, and
  the one that died showed the strange state's group returning at eleven levels (§5).
- A fourth round of thirteen took up round 3's next questions: twelve held (§6). The genetic-code test the
  author asked for is fenced in [`../../lab/genetic_code/`](../../lab/genetic_code/README.md).
- A fifth round went to 17 and 19: seven of twelve held, and at 19 the odd side won (§7).
- A sixth round tested the author's prediction for what follows, against a rival reading, at 23 and 29. Both died:
  the even side won at 23 and the odd side at 29 (§8).
- Then the data were read from other angles, the author's 7-wheel rule was registered as round 7, and a two-wheels
  test ran as round 8: two of three held (§9).
- Round 7 ran at 31: the even side won, and the author's 7-wheel died there (§10).
- Then the author asked about many wheels at once. Round 9 ran arrays of two to four wheels, and all eight of its
  predictions held. The best states of big arrays are collective, and on three wheels of 3 levels the best state found
  sits on neither face: it is the norm state of the field with 27 elements (§11).
- Round 10 ran three larger arrays with new code, and two of its seven predictions held. On three wheels of any odd
  prime the norm state is flat, and its Wigner values are Kloosterman sums. It wins on three wheels of 7 and loses on
  three of 5, where the winner found still sits on neither face. On five wheels of 3 the searches fell short of a known
  product state (§12).
- Zooming out showed the two wheels of §9 to be the two tori of SL(2, p), whose states are studied in radar and quantum
  chaos. Round 11 measured the magic of every one of them up to 401, exactly: all five predictions held, and it follows
  the Sato–Tate law, like the norm state's. Round 12 found the whole distribution of their Wigner values to be the
  semicircle, six of six held, and the fourth moment is proved exactly (§13).
- Round 13 took every cubic-phase state, the magic states of the third level's diagonal gates: their Wigner functions
  are Walsh spectra, none reaches the ceiling, and on three wheels of 3, 5 and 7 the norm state is the most magic of
  them (§14).
- Round 14 laid the author's Smith chart over the phase plane: it turns the whole turning wheel only at 7. The
  triangle's unfolding happened only at 5, the norm state's reign ends at 11, and the Fano plane's cubic is poor magic
  (§15).

---

## 1. The dictionary [FORCED; NAMED: Weyl, Schwinger, Gottesman]

| in the sevenths | on seven quantum levels |
|---|---|
| adding 1: the heptagon, base 7 | the **shift** X, which sends \|k⟩ to \|k + 1⟩ |
| the shift's Fourier partner | the **clock** Z, which gives \|k⟩ the phase ωᵏ, with ω = e^(2πi/7) |
| multiplying by 10: the octahedron turning round 0 | the **multiplier**, which sends \|k⟩ to \|3k⟩ and fixes \|0⟩ |
| the half turn, k → −k | the **parity**, which is the Fourier transform done twice |
| a seventh of a turn of our space | for spin 3, the seven f-orbitals, it is exactly the clock: its eigenvalues are the seven 7th roots of unity |

The **Clifford group**, which quantum computing is built on, is the set of operations that carry shifts and
clocks to shifts and clocks, up to phase.

## 2. What held

- **Q1. The classical part is the two faces.** Of the 5040 ways to permute the seven levels, exactly 42 are
  Clifford operations: the maps k → ak + b. The Fourier transform, which joins the two faces, is not a
  permutation of the levels at all.
- **Q2. The 168 again.** The Clifford group's geometric part, SL(2, 7), has 336 elements. Modulo ±1 its 168
  have the same orders as the Fano plane's 168 symmetries [NAMED: PSL(2, 7) ≅ GL(3, 2)].
- **Q3. The eight bases sit like the cube's corners.**
  - A seven-level system has eight mutually unbiased bases, the most it can have [NAMED: Wootters and Fields
    1989].
  - The multipliers fix two of them, the levels and the Fourier basis, and split the other six into {1, 2, 4}
    and {3, 5, 6}. The Fourier transform swaps the pair and swaps the triples.
  - The 168 contains 14 copies of the cube's rotation group, and each moves the eight bases exactly as the cube's
    rotations move its eight corners.
  - [READING] So the levels sit on the octahedron with its centre, and the bases on the cube: the polar pair of
    [`../../coin/THE_POLAR_COIN.md`](../../coin/THE_POLAR_COIN.md).
- **Q4. The magic subspace is Klein's space.**
  - Some states change sign under the half turn. Those are the states with negative quasi-probability at the
    centre of phase space, the resource that quantum computing needs.
  - They span three dimensions, one for each axis of the octahedron: (|j⟩ − |−j⟩)/√2 for j = 1, 2, 4.
  - The Clifford group acts there through exactly 168 matrices up to scalars. Its generators are Klein's own:
    diag(ω⁴, ω², ω) and a cycle of the three coordinates.
  - Klein's quartic x³y + y³z + z³x is invariant [NAMED: Klein 1878; this is the odd part of the Weil
    representation].
- **Q5. The octahedron acts on the magic subspace as on our space.** Each of the 14 copies of S₄ acts there
  with the character of the octahedron's rotations of ordinary space: 3, −1, 0 and 1 on elements of orders 1,
  2, 3 and 4. The elements of order 7 do not act like rotations: their traces are (−1 ± √−7)/2, the sum
  ω + ω² + ω⁴ over the squares and its conjugate.
- **Q6. The octahedron's height is a magic state.**
  - The Legendre state is +1 on the squares, −1 on the others and 0 at the centre. That is the height of each
    corner along the wheel's axis.
  - It is an eigenvector of every multiplier, and of the Fourier transform with eigenvalue i, which is Gauss's
    sum.
  - It changes sign under the half turn, and its quasi-probability at the centre is −1/7.
- **Q8. The same coin at 5.**
  - Five levels have 20 Clifford permutations, the maps k → ak + b.
  - The geometric part, modulo ±1, has the element orders of the icosahedron's rotation group.
  - The magic subspace, in two dimensions, carries the binary icosahedral group, 120 matrices: the icosahedron's
    rotations lifted to spinors.

## 3. What died

- **Q7. The Legendre state is not the most negative state.** A search from 125 starts found total negativity
  0.7325, against the Legendre state's 0.7283. The state it found is not even odd under the half turn: its
  parity expectation is +0.23. The guess is kept in [`../../GRAVEYARD.md`](../../GRAVEYARD.md), with the
  counterexample in the log to 8 decimals. Round 2 (§4) found what that state is.
- **T8 (round 3).** The Legendre state is not the deepest odd state at eleven levels. A tetrahedral state is
  (§5).
- **U9 (round 4).** At thirteen the even side wins by 0.017, not by less than 0.01 (§6).
- **V2, V4a, V4b, V5b, V6 (round 5).** At nineteen the odd side wins, the margins grew instead of shrinking,
  and the odd winner at 19 has 4 symmetries, not 12 or more (§7).
- **W1 and W2 (round 6).** The author's prediction, that the odd side wins from 19 on, died at 23. The rival, that
  the Legendre state's side wins, died at 23 and at 29 (§8).
- **Y1 (round 8).** The turning wheel's best symmetric state does not beat the multiplying wheel's at every prime:
  at 13 it loses (§9).
- **X1 (round 7).** The author's 7-wheel: at 31 it never reaches the half turn, and the even side wins anyway (§10).
- **V1, V2, V4, V5 and V6 (round 10).** On three wheels of 5 the norm-type state loses. On five wheels of 3 the
  searches fell short of a product state. The even side won on two arrays with an odd number of wheels, and two arrays
  fell below 88% of the ceiling (§12).

## 4. Round 2: the most negative state [FORCED; READING; NAMED: Veitch et al., Wang et al., Jain and Prakash]

Q7 died, so a second round asked which seven-level state is the most negative. Five predictions were
registered before the run, and all five held ([`PREREG.md`](PREREG.md)).

- **The search.** [`most_negative.py`](most_negative.py) maximizes the total negativity from 400 random starts.
  Its output is in [`most_negative.log`](most_negative.log).
  - The best value found is **0.732522**. Three starts reached it, and their states are the same up to symmetry.
  - At least 17 other starts stopped at a second peak, 0.729722.
  - This is a search, not a proof. A larger value is not ruled out. Round 3 (§5) proved that no state with a
    symmetry beats it.
- **The state** [FORCED, on the state as recorded to 8 decimals].
  - Its Wigner function reaches the ceiling, +1/7, at exactly one point: its own centre. Four Clifford
    operations fix it: the identity, and a quarter turn about that centre with its square and its cube.
  - Each quarter turn is the Fourier transform seen in another frame.
    - In the frames of one, the state is real and even, and the Fourier transform sends it to minus itself.
    - In the frames of the other, it is an eigenstate with eigenvalue +1, but never real. Among real states,
      that eigenspace reaches only 0.615232.
  - It is negative at 16 of the 49 points, none deeper than −0.068.
  - Each eigenspace of the Fourier transform has its own best state: 0.732522 for the eigenvalues −1 and +1,
    0.728262 for i (the Legendre state), and 0.601107 for −i, which holds a single state.
- **A coin: deep or wide** [READING, on FORCED facts].
  - The edge is the centre, where the Wigner operator is the half turn itself. So an odd state sits on the
    floor there, at −1/7, and an even state sits on the ceiling, at +1/7.
  - One side is the Legendre state. It is odd: −1/7 at the centre, negative at 13 points, total 0.728262. Twelve
    Clifford operations fix it: the six multipliers, and the Fourier transform after each.
  - The other side is the maximizer. It is even about its own centre: +1/7 there, negative at 16 points, none
    deeper than −0.068, total 0.732522. Four operations fix it. The more symmetric state loses.
- **The same coin at three.**
  - The strange state (|1⟩ − |2⟩)/√2 is the Legendre state of 3. It is odd: −1/3 at the centre and +1/6 at the
    other eight points. Its −1/3 is unique, so every operation that fixes it fixes the centre, and all 24
    Clifford operations that fix the centre fix it.
  - The Norrell state (|1⟩ + |2⟩)/√2 is even: +1/3 at the centre, and −1/6 at two points. Six operations fix it.
  - Both total 1/3, the largest value the search found. Of the 100 starts, 99 reached it: 30 at the strange
    state and 69 at the Norrell state, up to symmetry. None reached it anywhere else.
  - The tie is known. Mana, the logarithm of 1 + 2 × the total negativity, ranks states exactly as the total
    negativity does. Jain and Prakash credit Veitch, Mousavian, Gottesman and Emerson (2014) with seeing that
    the two states share the largest mana, and Wang, Wilde and Su (2020) with showing that a finer measure,
    the thauma, ranks the strange state first.
  - So at three the two sides tie. At seven the best even state found beats the Legendre state, by 0.0043.
    Round 3 (§5) made both sides exact at seven, and took the coin to eleven.
  - Jain and Prakash (2020) found the same split at five: the most magic state there is not the most symmetric
    one. They also proved that above 3 no state is fixed by every Clifford operation that fixes the centre, as
    the strange state is at 3.

## 5. Round 3: the three open questions [FORCED; READING; NAMED: Jain and Prakash, Erew and Goldstein]

The author asked for all three of round 2's open questions. Ten predictions were registered before the run,
with the script that tests them, and nine held ([`PREREG.md`](PREREG.md)). The script is
[`round3.py`](round3.py); its output is in [`round3.log`](round3.log).

- **Two tools.** Both rest on one identity: the sum of a state's |W| is the largest value of Σ s_u W_u over
  sign choices s_u = ±1, one for each phase-space point.
  - *The sign ascent.* Give each point the sign of the state's Wigner value there. Then replace the state with
    the top eigenvector of Σ s_u A_u, where A_u is the point's Wigner operator. No step lowers the sum of |W|,
    so every start climbs to a local maximum. A million climbs at seven levels take about twenty seconds.
  - *The exhaustive count.* If a symmetry fixes a state, the state's signs are constant along the symmetry's
    orbits in phase space. So the best state a symmetry fixes is found by trying every sign choice that is
    constant on those orbits. For the half turn at seven levels that is 2^24 = 16 777 216 choices on each side,
    and every one was tried.
- **A. Is 0.732522 the maximum?** Among states with a symmetry, yes, by exhaustion [FORCED]. Among the rest,
  a million climbs found nothing higher.
  - *The even side.* Every even sign choice was tried. The best is the round-2 record. The 84 choices that
    reach it are its 84 images under the 336 symmetries that fix the centre. The next even state is round 2's
    second peak, 0.729722.
  - *Every kind of symmetry.* A state with any symmetry has one of prime order: 2, 3 or 7. Up to conjugacy
    that leaves only a few kinds, and each was counted:
    - the half turn, the only kind of order 2: the even side above, and the odd side (B, below);
    - the multiplier ×2, since all subgroups of order 3 are conjugate. Its best state is the Legendre state;
    - the shift: only stabilizer states, at 0;
    - the shear: at most 0.320997;
    - 42 groups of shears with a shift that fix no point: at most 0.725152, at a state with 21 symmetries,
      the Frobenius group of order 21.

    None beats the record. So if 0.732522 is ever beaten, the winner has no ordinary symmetry. Round 4 (§6)
    adds the mirror symmetries.
  - *The search.* A million climbs from random states: 1460 reached the record, and none went higher. The
    third-highest top, 0.729616, has no ordinary symmetry. Round 4 found it has a mirror symmetry.
  - *Its exact value.* x = 7(1 + 2N), seven times the sum of |W|, is a root of
    x¹² − 36x¹¹ + 258x¹⁰ + 3468x⁹ − 39873x⁸ − 108680x⁷ + 1734236x⁶
    + 1510968x⁵ − 26665265x⁴ − 10245204x³ + 127009090x² + 35031356x − 154719151,
    which is irreducible. So N = 0.732522000010631… is an algebraic number of degree 12.
  - *What fixes it.* Its four symmetries do not pin it down. They fix a two-dimensional family of states, and
    the record is the best point of that family. Round 2's state, moved to its centre, is a real, even vector:
    (−0.0864, −0.3634, −0.0776, 0.5985, 0.5985, −0.0776, −0.3634).
- **B. Is the Legendre state the best odd state?** At seven, yes, by exhaustion [FORCED]. At eleven, no.
  - *Seven.* Every odd sign choice was tried. The best is the Legendre state, reached by 28 choices, its 28
    images. The next odd state has 0.721570. The Legendre state's value is
    N = (4 cos(2π/7) − 4 cos(6π/7) − 1)/7, and x = 7(1 + 2N) is a root of x³ − 15x² − 37x − 13. Its 12
    symmetries fix no other state.
  - *Eleven.* **T8 died**: the registered guess that the Legendre state is still the deepest odd state. A million
    climbs among the odd states found 1.029707, against the Legendre state's 0.787711. The Legendre state of 11
    is a local maximum, but far down: 2 of the million odd climbs ended there. The new state:
    - has 24 symmetries, with the element orders of the binary tetrahedral group SL(2, 3). That is the strange
      state's own group at three;
    - is the only state those symmetries fix, and in a frame centred on its floor point it is real;
    - has x = 11(1 + 2N) a root of an irreducible polynomial of degree 10.
  - So the deepest odd state is the Legendre state at 3 and at 7, but not at 11. There the deepest odd state
    found carries the strange state's group. The guess is kept in [`../../GRAVEYARD.md`](../../GRAVEYARD.md).
- **C. Which side wins at eleven?** The even side, by 0.0029 [measured].
  - A million climbs among the even states found 1.032586. A million among the odd ones found 1.029707.
  - The winner touches the ceiling, +1/11, at one point, its centre. Its only symmetry is the half turn about
    that point. It is negative at 44 of the 121 points, none deeper than −0.0396.
  - It is not fixed by its symmetry. It is just the best of the even states, which fill six dimensions, and its
    x has degree 30.
  - A million climbs in the whole space found nothing higher; 181 of them reached it.
- **The coin across the primes** [READING, on exhaustive and measured facts].

  | p | odd side: best state | its symmetries | even side: best state | its symmetries | the even side wins by |
  |---|---|---|---|---|---|
  | 3 | 1/3, the strange state | 24 | 1/3, the Norrell state | 6 | 0, a tie |
  | 5 | 0.433070 | 6 | 0.556677, Jain and Prakash's | 6 | 0.124 |
  | 7 | 0.728262, the Legendre state | 12 | 0.732522, the record | 4 | 0.0043 |
  | 11 | 1.029707, found | 24 | 1.032586, found | 2 | 0.0029 |

  - The rows for 3, 5 and 7 are exhaustive. The row for 11 rests on searches.
  - The even side wins at every prime above 3 tried. At 3, 7 and 11, which are 3 more than a multiple of 4,
    the two sides end within 0.005 of each other. At 5 they are 0.124 apart.
  - At 3 and 5 every best state is the only state its symmetries fix. At 7 and 11 the odd side's best still is,
    but the winner, on the even side, is not: it has to be found by climbing, and the more symmetric side loses.
  - At 11 the odd side's best state has the strange state's group.
  - At 5, where the Legendre state is even, it has exactly 2/5, short of Jain and Prakash's state.

## 6. Round 4: closing in [FORCED; READING; NAMED: Samuelson, Good and Turing]

The author asked for all three of round 3's next questions, and for the genetic-code test. Thirteen predictions
were registered with the script that tests them, and twelve held ([`PREREG.md`](PREREG.md)). The script is
[`round4.py`](round4.py), run in three parts; the logs are [`round4_seven.log`](round4_seven.log),
[`round4_eleven.log`](round4_eleven.log) and [`round4_thirteen.log`](round4_thirteen.log). The genetic-code study is
fenced in [`../../lab/genetic_code/`](../../lab/genetic_code/README.md).

- **Seven: toward a proof** [FORCED, except the search].
  - *Every symmetry, mirrors too.* A mirror symmetry is a Clifford operation composed with complex conjugation.
    Its square is an ordinary symmetry, which round 3 counted, unless it squares to the identity. The run checked
    that all 392 mirror symmetries that square to the identity are conjugate to complex conjugation, which fixes
    exactly the real states. All 2^28 sign choices symmetric under its mirror, (q, p) → (q, −p), were tried. The
    best is the record, reached by 42 choices, all its images. So no state with any symmetry, ordinary or
    mirror, beats the record.
  - *A bound on the negative points.* The Wigner operators of k points sum to an operator with trace k and squared
    norm 7k, so its lowest eigenvalue cannot be very low (Samuelson's inequality). A state that beats the record
    therefore has between 8 and 24 negative points.
  - *The search.* Ten million climbs: 14 754 reached the record, and none went higher. They found 52 348
    different tops, and 3248 were reached only once, so by Good and Turing's rule the tops never reached hold
    about 3 × 10⁻⁴ of the starting states.
  - *A correction to round 3.* Round 3 said the third-highest top, 0.729616, has no symmetry. It has no ordinary
    one, but it has a mirror symmetry, so the real count covers it. The best state found with no symmetry of any
    kind is the fifth top, 0.725917, 0.0066 below the record.
  - *What is left.* A state that beats the record would have no symmetry of any kind, between 8 and 24 negative
    points, and a basin smaller than about 3 × 10⁻⁴ of the space. A proof would have to rule out about 2^48 sign
    choices, roughly 10^10 up to the symmetries. That is beyond this pass, but finite.
- **Eleven: the true maximum** [measured, except the counts].
  - Ten million climbs among even states and four million in the whole space found nothing above 1.032586, and
    neither did 2000 kicks from each of the 20 highest tops. The even climbs reached it 158 331 times.
  - Exhaustive counts cover every state with a symmetry of order 4, 5, 6 or 11 [FORCED]. The best of them is the
    tetrahedral state, 1.029707, which has symmetries of orders 4 and 6. States whose only symmetries have order
    2 or 3 are beyond counting: 2^60 and 2^40 sign choices.
  - Ten million odd climbs found nothing above the tetrahedral state.
  - Some samples of one top had looked like different states. All 35 such pairs are mirror images.
  - So the winner, whose only symmetry is its half turn, stays ahead of every state with more symmetry. A rival's
    symmetries, if it had any, would all have order 2 or 3.
- **Thirteen: which side wins** [measured, except the tetrahedral rule].
  - The Legendre state of 13 is even, as (−1 | 13) = +1 forces, with 24 symmetries. It has 0.933851.
  - Three million climbs on each side: the even side found 1.168522 and the odd side 1.151336. The even side wins
    by 0.017.
  - The winner touches the ceiling, +1/13, at one point, its centre, and its only symmetry is the half turn there.
    Its symmetry does not fix it. Two million climbs in the whole space found the same state, but only 8 times.
  - The odd side's best has 6 symmetries, and they do not fix it either.
- **Where the tetrahedral states sit** [FORCED].
  - A state that a binary tetrahedral group fixes lies on the Legendre state's side. The group contains the half
    turn, and each of its characters is trivial there. For p ≥ 5 every operator of SL(2, p) has determinant 1, so
    the half turn's operator is (−1 | p) times the parity.
  - The run found the states such a group fixes. At 3 there is one, the strange state, odd. At 11 there are two,
    1.029707 and 0.899019, both odd. At 13 there is one, 0.982303, even. At 7 there are none: every copy of the
    group acts on the three-dimensional odd subspace with the octahedral character, which fixes no line (Q5).
  - So the Legendre symbol of −1 decides two things at once: which side the Legendre state is on, and which side
    the tetrahedral states are on.
- **The coin across five primes** [READING, on exhaustive and measured facts].

  | p | odd side: best state | its symmetries | even side: best state | its symmetries | the even side wins by |
  |---|---|---|---|---|---|
  | 3 | 1/3, the strange state | 24 | 1/3, the Norrell state | 6 | 0, a tie |
  | 5 | 0.433070 | 6 | 0.556677, Jain and Prakash's | 6 | 0.124 |
  | 7 | 0.728262, the Legendre state | 12 | 0.732522, the record | 4 | 0.0043 |
  | 11 | 1.029707, found | 24 | 1.032586, found | 2 | 0.0029 |
  | 13 | 1.151336, found | 6 | 1.168522, found | 2 | 0.017 |

  - The even side wins at every prime above 3, up to 13. Round 5 found the odd side winning at 19 (§7).
  - When p is 3 more than a multiple of 4, the Legendre state's side is the odd one. There the best odd state is
    a highly symmetric one, with 12 symmetries at 7 and 24 at 11, and it comes within 0.005.
  - When p is 1 more, the symmetric states move to the even side, and they do not win it: at 13 the tetrahedral
    state has 0.982 and the Legendre state 0.934, against 1.169. The sides end farther apart.
  - From 7 on, no winner is fixed by its symmetries alone.
  - Round 4 tested two readings at 13. The size reading said the sides would end close; that died (U9). The
    Legendre-side reading said the winner would be fixed by its symmetries; that is false too. Each reading had
    half of it.

## 7. Round 5: seventeen and nineteen [FORCED; READING]

The author asked for 17 and 19. Twelve predictions were registered with the script that tests them, and seven held
([`PREREG.md`](PREREG.md)). The script is [`round5.py`](round5.py), run once for each prime; the logs are
[`round5_seventeen.log`](round5_seventeen.log), [`round5_nineteen.log`](round5_nineteen.log) and
[`round5_combined.log`](round5_combined.log).

- **Seventeen: the even side wins, by 0.031** [measured].
  - Three million climbs on each side found 1.402567 on the even side and 1.371867 on the odd side. The margin is
    wider than 13's 0.017, so the guess that it would shrink died (V4a).
  - The winner touches the ceiling, +1/17, at one point, its centre. It has 6 symmetries, a sixth of a turn about
    that point, and they do not fix it.
  - The Legendre state of 17 is even, with 32 symmetries. It has 1.250924.
- **Nineteen: the odd side wins** [measured].
  - Two million climbs on each side found 1.507862 on the odd side and 1.484879 on the even side. The even side's
    streak ends here (V2, V5b died).
  - The winner sits on the floor, −1/19, at its centre. It has 4 symmetries, a quarter turn about that point, and
    they do not fix it.
  - An unregistered check ran two million more climbs on the even side with a fresh seed, plus 20 000 kicks from
    its highest tops. It found the same even best, 224 times, and nothing higher.
  - The Legendre state of 19 is odd, with 36 symmetries. It has 1.356950.
- **The exceptional groups' states sit on the Legendre state's side** [FORCED, and checked].
  - At 17 there are two kinds of binary tetrahedral group and two of binary octahedral. The tetrahedral ones fix
    three states each and the octahedral ones one each, all even, from 1.167172 to 1.388656.
  - At 19 the binary tetrahedral group fixes three odd states, up to 1.495712, and the two kinds of binary
    icosahedral group fix none.
  - From 17 on, the best of these states sits between the two sides: above the losing side's best, below the
    winner. The guess that a highly symmetric state would win the odd side at 19 died (V6).
- **The coin across seven primes** [READING, on exhaustive and measured facts].

  | p | odd side: best state | its symmetries | even side: best state | its symmetries | the even side ahead by |
  |---|---|---|---|---|---|
  | 3 | 1/3, the strange state | 24 | 1/3, the Norrell state | 6 | 0, a tie |
  | 5 | 0.433070 | 6 | 0.556677 | 6 | 0.124 |
  | 7 | 0.728262, the Legendre state | 12 | 0.732522, the record | 4 | 0.0043 |
  | 11 | 1.029707 | 24 | 1.032586 | 2 | 0.0029 |
  | 13 | 1.151336 | 6 | 1.168522 | 2 | 0.017 |
  | 17 | 1.371867 | 2 | 1.402567 | 6 | 0.031 |
  | 19 | 1.507862 | 4 | 1.484879 | 2 | −0.023 |

  - From 11 on, the rows rest on searches.
  - From 7 on, no winner is fixed by its symmetries.
  - Three readings fit some of this, and none fits all of it.
    - *The even side wins.* That held from 5 to 17 and broke at 19.
    - *The Legendre side wins.* The side that holds the Legendre state and the tetrahedral states won at 5, 13, 17
      and 19. It lost at 7 and 11, by less than 0.005.
    - *The author's prediction, made on seeing 19:* "even only wins the lows, the odd wins the rest".
  - The author's prediction and the Legendre-side reading are now registered against each other as round 6
    ([`PREREG.md`](PREREG.md)). They agree at 23 (the odd side) and part at 29: the author says odd, the rival
    says even.
- **The genetic-code study's second part** used Freeland and Hurst's weights by letter position. The best codes
  pair their third letters, but the weights cannot choose the pairing: all three pairings of the four bases appear
  among the best codes. See [`../../lab/genetic_code/`](../../lab/genetic_code/README.md).

## 8. Round 6: the author's prediction [READING; measured]

> *i'd predict that even only wins the lows, the odd wins the rest?* — the author, 8 November 2026, on seeing
> nineteen

Round 5 broke the even side's streak at 19, and the author predicted what would follow. The prediction was
registered in the author's words (W1), against the rival reading that the Legendre state's side wins (W2), before
any run at 23 or 29 ([`PREREG.md`](PREREG.md)). The script was committed before its run, as the registration
promised: [`round6.py`](round6.py), with the logs [`round6_twentythree.log`](round6_twentythree.log),
[`round6_twentynine.log`](round6_twentynine.log) and [`round6_combined.log`](round6_combined.log).

- **Twenty-three: the even side wins, by 0.0036, and both readings die there.**
  - Two million climbs on each side found 1.700022 on the even side and 1.696423 on the odd side.
  - Both readings had said the odd side would win at 23.
  - An unregistered check ran two million more odd climbs with a fresh seed, and kicks from the highest odd tops.
    It found the same odd best, 353 times, and nothing higher.
  - Each side's winner has only its half turn, and is not fixed by it.
- **Twenty-nine: the odd side wins, by 0.0063.**
  - Two million climbs on each side found 1.963715 on the odd side and 1.957461 on the even side. The author called
    this one.
  - The odd winner sits on the floor at its centre. It has 10 symmetries, turns of orders 5 and 10 about that
    point, and they do not fix it.
  - The even best was reached only 6 times in two million climbs, so 29 is the least certain row. An unregistered
    recheck ran two million more even climbs with a fresh seed, and kicks from the highest even tops. It found the
    same even best, 11 times, and nothing higher.
- **The exceptional states** [FORCED, not scored]. They sit on the Legendre state's side, as round 4's rule says.
  - At 23 the two kinds of binary tetrahedral group fix two odd states each, all at 1.490815, and the two kinds of
    binary octahedral group fix none.
  - At 29 the binary tetrahedral group fixes three even states, at 1.656907 and twice at 1.79327, and the two
    kinds of binary icosahedral group fix none.
- **The coin across nine primes.**

  | p | odd side: best state | even side: best state | the even side ahead by |
  |---|---|---|---|
  | 3 | 1/3 | 1/3 | 0, a tie |
  | 5 | 0.433070 | 0.556677 | 0.124 |
  | 7 | 0.728262 | 0.732522 | 0.0043 |
  | 11 | 1.029707 | 1.032586 | 0.0029 |
  | 13 | 1.151336 | 1.168522 | 0.017 |
  | 17 | 1.371867 | 1.402567 | 0.031 |
  | 19 | 1.507862 | 1.484879 | −0.023 |
  | 23 | 1.696423 | 1.700022 | 0.0036 |
  | 29 | 1.963715 | 1.957461 | −0.0063 |

  - The even side wins at 5, 7, 11, 13, 17 and 23, the odd side at 19 and 29, and 3 is a tie.
  - Neither registered reading survives. The author's had the odd side winning from 19 on, and 23 broke it. The
    Legendre-side reading had the odd side at 23 and the even side at 29, and both calls were wrong.
  - The odd side's two wins come at 19 and 29, the two primes tested that are 4 more than a multiple of 5. That is
    two data points: an observation, not a reading. The next such prime, 59, is beyond this machinery for now.
  - The margins have shrunk overall: under 0.007 at 23 and 29, against 0.124 at 5. From 19 on, each side's best is
    reached only rarely. Fresh-seed rechecks at 19, 23 and 29 found the same bests, but a better state with a tiny
    basin cannot be ruled out.
  - From 7 on, no winner is fixed by its symmetries.

## 9. Other angles, and the two-wheels test [READING; measured]

After round 6 the author asked to pause and look at the data from other angles. The author then pointed to the wheel
of numbers around 7 and to Shor's algorithm. Made exact, that is a rule, registered as round 7
([`PREREG.md`](PREREG.md)): the even side wins exactly when the powers of 7 modulo p pass through the half turn, the
case Shor's period finding checks for. It fitted all eight primes
run before it other than 7 itself, and of the bases 2 to 29 only 7 did. At 31 it died (§10).

- **Flatness: what every winner shares.** The total negativity has a ceiling, (√p − 1)/2, reached only if every point
  of the Wigner function had the same size. From 7 on, both sides' best states reach 88 to 90% of it at every prime.
  The contest is about making the quasi-probabilities as even as possible, and both sides do that almost equally well.
- **The edge: why the gap is small.** Two effects of size about 1/p pull opposite ways. An odd state gets −1/p at the
  centre for free; an even state has one more dimension to work in. From 7 on, every gap between the sides is at most
  about half of 1/p.
- **The two wheels.** The symmetries that fix the centre include two cyclic wheels that share only the half turn: the
  multiplying wheel, k → ak, with p − 1 steps, and the turning wheel, the rotations of phase space, with p + 1 steps.
  Every winner found has a symmetry from the turning wheel, or only the half turn. The Legendre state, which the whole
  multiplying wheel fixes, has not won since 3.
  - [NAMED] The two wheels are the two kinds of maximal torus in SL(2, p): the multiplying wheel is the split torus and
    the turning wheel the non-split one. Their eigenvectors are the "oscillator system" of Gurevich, Hadani and
    Sochen, used for radar sequences, and the Hecke eigenfunctions of the quantized cat map in quantum chaos (Kurlberg
    and Rudnick). So round 8's one-line families measured the Wigner negativity of those states at every prime from 5
    to 29. At 5 the most negative state of all, Jain and Prakash's, is one of them: an eigenvector of the whole
    turning wheel. Round 11 measured all of them up to 401 (§13).
- **The two-wheels test** (round 8, registered with its script, 2 of 3 held). The script is
  [`two_wheels.py`](two_wheels.py); its output is in [`two_wheels_combined.log`](two_wheels_combined.log).
  - For each prime and each order m > 2 on each wheel, the sign ascent searched every eigenspace of the order-m
    symmetry, with equal effort on both wheels. A one-line eigenspace is exact.
  - The turning wheel's best beat the multiplying wheel's at 5, 7, 11, 17, 19, 23 and 29, and reached the winner
    wherever the winner has a turning symmetry. Nothing beat a known winner.
  - At 13 the multiplying wheel won, 1.167364 against 1.105229 (Y1 died). The turning side is exact: the verifier
    counts every sign choice in its order-7 family.
  - The test had a confound: a small order fixes a large family, and at 13 the turning wheel offers only orders 7
    and 14.
  - Read after the run, the logs hold 14 pairs of families of equal size, one on each wheel. The turning wheel wins 12
    and loses at 13 (dimension 2) and 19 (dimension 4). At equal size a turning symmetry is usually the better one,
    not always.

## 10. Round 7: the 7-wheel at thirty-one [READING; measured]

> *it must be related to the wheel of numbers revolving around 7? i am thinking shor's with a 7 wheel
> conversion?* — the author, 8 November 2026

The author's rule (X1) was made exact in §9 and registered before any run at 31: the even side wins exactly when the
powers of 7 modulo p pass through the half turn. At 31 they never do, since the 7-wheel's period there is 15, so the
rule called the odd side. The rival observation (X2), that the odd side's wins fall at primes 4 more than a multiple
of 5, called the even side. The script was committed before its run: [`round7.py`](round7.py), with the logs
[`round7_thirtyone.log`](round7_thirtyone.log) and [`round7_combined.log`](round7_combined.log).

- **Thirty-one: the even side wins, by 0.0138, and the 7-wheel dies.**
  - Two million climbs on each side found 2.045297 on the even side and 2.031473 on the odd side.
  - A timing test of 2 000 climbs per side had printed the same order before the run. It is disclosed in
    [`PREREG.md`](PREREG.md), and it could not change the registered calls.
  - An unregistered recheck ran two million more odd climbs with a fresh seed, and kicks from the ten highest
    odd tops. It found the same odd best, once again, and nothing higher. Both searches reached it only
    once, so its basin is tiny.
  - The even winner has only its half turn. The best odd state has six symmetries, turns of order 3 and 6 from the
    multiplying wheel (6 divides 30), and they do not fix it.
- **The exceptional states** [FORCED, not scored]. 31 is 3 more than a multiple of 4, so round 4's rule puts them on
  the odd side, and there they sit. The two kinds of binary tetrahedral group fix three odd states each (1.906903
  once and 1.779773 twice), the two kinds of binary octahedral group one each (1.906903), and the binary icosahedral
  groups none.
- **The coin across ten primes.** To the table in §8, 31 adds the odd side at 2.031473 and the even side at
  2.045297, the even side ahead by 0.0138.
  - The even side wins at 5, 7, 11, 13, 17, 23 and 31, the odd side at 19 and 29, and 3 is a tie.
  - No number wheel of any base from 2 to 30 now fits every decided prime. Before 31, only 7 did.
  - The rival observation fits all nine, but it rests on two odd wins. Its next odd call is 59, beyond this
    machinery; 37 would test its even call again.
  - Flatness and the edge still hold. Both bests reach 89 to 90% of the ceiling, (√31 − 1)/2 = 2.283882, and the gap,
    0.0138, is 43% of 1/31.

## 11. Round 9: many wheels [FORCED; READING; measured; NAMED: Liu and Winter, Knipfer et al.]

> *you are only spinning one wheel... imagine a 10x10 of wheels or larger?* — the author, 9 November 2026

**Made exact.**
- An array of n wheels is n p-level systems side by side: D = p^n levels and D² phase-space points.
- Each point's operator is the product of the wheels' operators. The array's half turn is every wheel's half turn
  at once.
- A product state's sum of sizes multiplies. So the best product state, the best single wheel repeated, reaches the
  fraction fⁿ of the ceiling √D.
- Clifford operations keep the negativity and can entangle the wheels. So the test that entanglement pays is to beat
  every product.

Eight predictions were registered with the script, [`many_wheels.py`](many_wheels.py), before its full run
([`PREREG.md`](PREREG.md)). Its pilots had been seen by mistake, and six of the eight only checked them. All eight
held. The output is in `many_wheels_three.log`, `_four`, `_five`, `_seven` and `_combined`.

- **The 10 × 10 array** [FORCED]. No search reaches 3^100 levels, but this arithmetic is exact.
  - Each point's operator has (D + 1)/2 eigenvalues +1 and (D − 1)/2 eigenvalues −1. So the average random state's
    sum of sizes follows from a Beta distribution, and it tends to √(2/π) = 0.798 of the ceiling.

  | levels | best single wheel, f | random beats every product from | 10 wheels: product, random | 100 wheels: product, random |
  |---|---|---|---|---|
  | 3 | 0.962 | 6 wheels | 0.681, 0.798 | 0.021, 0.798 |
  | 5 | 0.945 | 4 wheels | 0.569, 0.798 | 0.0035, 0.798 |
  | 7 | 0.932 | 4 wheels | 0.493, 0.798 | 0.00085, 0.798 |

  - So in a 10 × 10 array the wheels cannot spin separately. Every product state, and every Clifford image of one,
    falls below the average random state: 37 times below it at 3 levels and 940 times at 7. The best states are
    collective.
  - This is the many-wheel case of Liu and Winter's theorem that typical many-body states are nearly maximally
    magic [NAMED].
  - The measure counts the wheels and ignores their layout: a 10 × 10 grid and a line of 100 wheels are the same to
    it. The layout would matter for what neighbouring wheels can do together, not for this ceiling.
- **The searches** [measured]. The sign ascent ran on the even side, the odd side and the whole space of each array.

  | array | D | even side | odd side | whole space | best product of smaller bests | best, share of the ceiling |
  |---|---|---|---|---|---|---|
  | one wheel of 3 | 3 | 1/3 | 1/3 | 1/3 | — | 0.911 |
  | two wheels of 3 | 9 | 8/9 | 8/9 | 8/9 | 8/9 | 0.889 |
  | three wheels of 3 | 27 | 1.875593 | 1.886964 | **17/9** | 49/27 | 0.900 |
  | four wheels of 3 | 81 | **98/27** | 3.476833† | 3.289771* | 3.478273 | 0.907 |
  | two wheels of 5 | 25 | **1.766937** | 1.727386 | 1.766078* | 1.733134 | 0.883 |
  | two wheels of 7 | 49 | **2.719253** | 2.633836 | 2.510505* | 2.538221 | 0.906 |

  \* The whole-space search had a tenth or less of the side searches' climbs.

  † Round 10's climbs from the products later found an odd state at 3.533331 (§12). The even side still wins.

  - **Two wheels of 3:** nothing beats a product of two single-wheel bests. The best states found are entangled, yet
    their Wigner values are a product's, as a Clifford image of a product's would be.
  - **From three wheels of 3, two of 5 and two of 7 on, entanglement pays:** the best state beats every product.
  - **The coin persists in arrays.** The even side wins at four wheels of 3, two of 5 and two of 7. At three wheels of
    3 the odd side beats the even side, but the best state found is on neither face (below).
  - **Two measures, two winners.** The most negative states are not the most magic by the stabilizer Rényi entropy
    M₂, the measure Knipfer et al. maximize [NAMED]. At two wheels of 3 the best states' M₂ is ln 4, against their
    maximum ln(81/17) = 1.561. At two wheels of 5 and of 7 it falls below their values too.
- **Three wheels of 3: the winner sits on the edge** [FORCED for the state; measured for the search]. The whole-space
  search beat both sides with 17/9, at a state on neither face. A second search with a fresh seed found 17/9 again,
  11 times in 200 000 climbs, and nothing higher.
  - The state is the **norm state** of the field with 27 elements, up to a Clifford operation:
    ψ = Σ ω^N(x) |x⟩ / √27, where x runs over the field, ω = e^(2πi/3), and N(x) = x·x³·x⁹ is the field's norm,
    which lies in the three-element field. [`edge_state.py`](edge_state.py) reruns the search and finds an explicit
    Clifford operation for each best state; its output is in [`edge_state.log`](edge_state.log).
  - Its Wigner function takes only three values: 2/243, −1/243 and −4/243, at 351, 351 and 27 points. So its
    negativity is exactly 17/9. No point's operator has it as an eigenstate: |⟨A_u⟩| ≤ 4/9 everywhere, so it is
    neither even nor odd about any centre.
  - **Its flatness.** Its Weyl expectations vanish on 26 operators, which form a Lagrangian with the identity, and
    have the same size, 1/√27, on all 702 others. That comes from N being cubic: each difference N(x + a) − N(x) is
    quadratic, and for a ≠ 0 it has no flat direction, so it spreads evenly over every frequency.
  - It has exactly 1 053 Clifford symmetries: the 27 shifts x → x + a, each with a quadratic phase, and 39 linear
    maps, multiplication by the 13 nonzero squares and the field's own map x → x³ (the Frobenius map). Every
    symmetry keeps that Lagrangian, so a count over all the maps that do finds them all.
  - **Its coin.** The half turn sends it to its complex conjugate, a different state with the same value. Here the
    edge is a flip between two states, not a fixed point. The state's odd part, with weight 13/18, is the field's
    Legendre state: the quadratic character of the 27-element field as amplitudes, the field's version of the state
    that is the best odd state at seven levels. Its even part, with weight 5/18, is |0⟩ minus half of every other
    basis state.
  - **Checked after the run, and negative:**
    - at two wheels the norm is quadratic, so the norm state is a stabilizer state, with no negativity;
    - at four wheels of 3 the norm state gives only 2000/729 ≈ 2.743. The four-wheel best, 98/27, is something
      else, an even state whose structure is open;
    - the states of the field's multiplicative characters, Σ χ(x) |x⟩ for each character χ of its wheel of nonzero
      elements, stay below every array's best.
  - The verifier checks the norm state's value, levels, coin, zero set, symmetries and M₂, which matches the logged
    M₂ of the state the run found. It also checks the other arrays' norm states, and with `--full` the character
    states and the exact count of symmetries.

## 12. Round 10: the larger arrays [FORCED; READING; measured; NAMED: Kloosterman, Weil, Davenport and Hasse, Katz, Damski et al.]

> *you are only spinning one wheel... imagine a 10x10 of wheels or larger?* — the author, 9 November 2026

Round 9 stopped near 81 levels, because it wrote out every phase-point operator. Round 10 ran three larger arrays with
code that never does: three wheels of 5 (125 levels), five wheels of 3 (243) and three wheels of 7 (343). Seven
predictions were registered with the script, [`larger_arrays.py`](larger_arrays.py), before any run
([`PREREG.md`](PREREG.md)), and two held. The output is in `larger_arrays_run.log` and `larger_arrays_combined.log`.
What was read after the run is in [`flat_states.log`](flat_states.log) and [`product_climbs.log`](product_climbs.log).

- **The new code** [FORCED]. For each point q the Wigner function is one Fourier transform:
  W(q, k) = (1/D) Σ_s ψ̄(q + s) ψ(q − s) ω^(2k·s). A state on one side needs only half of the q's. The verifier checks
  it against round 9's operators at every point. In the calibration, from all 1 680 starts, the climbs end where round
  3's code ends.
- **Flat on three wheels of every odd prime** [FORCED; proved before the run]. Take the field with p³ elements and its
  norm N to F_p. Every norm-type state ψ_c = Σ_x ω^(c·N(x)) |x⟩ / √(p³) has Weyl expectations zero on the Z-type
  operators, which form a Lagrangian, and of size exactly 1/√(p³) on every other operator.
  - So the flatness of round 9's three-qutrit winner is no accident of 3.
  - The reason: each difference N(x + a) − N(x) has the quadratic part Tr(a^(p²) x^(p+1)), and that form is never
    degenerate. A degenerate one would need z^(p−1) = −1 in the field, which is impossible because p² + p + 1 is odd.
  - The half turn sends ψ_c to its complex conjugate, and no point's operator has it as an eigenstate. So at every p it
    sits on neither face, and the edge is a flip between two states, as at 3.
  - On five wheels of 3 the norm has degree 5, its differences are not quadratic, and the argument fails. That norm
    state is zero on a Lagrangian too, but not flat elsewhere, and its negativity is 4232/729.
- **Its Wigner values are Kloosterman sums** [FORCED; derived during the run, after the registration; NAMED:
  Kloosterman, Davenport and Hasse, Weil, Katz].
  - Each norm-type state takes the value K(m)/p⁵ at (p² + p + 1)p³ points for each nonzero m in F_p, and −(p + 1)/p⁵
    at the other p³ points. Here K(m) = Σ_a ω^(a + m/a), over the nonzero a in F_p, is the Kloosterman sum. Every c
    gives the same values.
  - So its negativity is exact at every prime: the sum of sizes is [(p + 1) + (p² + p + 1) Σ_m |K(m)|]/p². That is
    17/9 at 3, 4.252724 at 5 and 7.902228 at 7.
  - The route: Davenport and Hasse's theorem turns the Gauss sum of a character composed with the norm into the cube of
    the character's Gauss sum over F_p, and summing squared Gauss sums over the characters gives a Kloosterman sum.
    Both proofs are written out in [`NORM_STATE.md`](NORM_STATE.md). [`verify_norm_state.py`](verify_norm_state.py)
    checks the whole statement from the state itself at p = 3, 5, 7, 11 and 13, and each step of the proof at every
    odd prime up to 101.
  - Its share of the ceiling is 90.0% at 3, 83.5% at 5, 90.2% at 7, 84.0% at 11, 82.4% at 13 and 88.8% at 17. Below
    2 000 only 3 and 7 reach 90%, and 7 reaches the most. As p grows the share tends to 8/(3π) = 84.9%, because the
    Kloosterman angles follow the Sato–Tate law (Katz). The average random state tends to √(2/π) = 79.8%.
  - [READING] So how strong the norm state is at a prime is decided by that prime's Kloosterman sums. At 5 they are
    small: 0.38, −3.24, 1.24 and 2.62, against Weil's bound 2√5 = 4.47.
- **The searches** [measured].

  | array | D | even side | odd side | whole space | kicks of the norm-type states | norm-type state | best product of smaller bests | best, share of the ceiling |
  |---|---|---|---|---|---|---|---|---|
  | three wheels of 5 | 125 | 4.293476 | 4.291598 | 4.162584 | **4.301387** | 4.252724 | 4.290842 (even) | 4.301387, 0.845 |
  | five wheels of 3 | 243 | 6.082020 | 6.069252 | 5.925177 | 6.052266 | 4232/729 = 5.805213 | **517/81 = 6.382716** (either side) | 6.382716, 0.875 (search: 6.082020, 0.834) |
  | three wheels of 7 | 343 | 7.238233 | 7.241590 | 7.097608 | 7.902228 | **7.902228** | 7.435601 (even) | 7.902228, 0.902 |

  - **Three wheels of 7: the norm state wins, on neither face.** Nothing found beats it. All 300 kicks of it climbed
    back to it, and it stands 0.47 above the best product.
  - **Three wheels of 5: the norm state loses, but the winner is still on neither face.** Both sides' bests beat the
    norm state, and a climb from a kicked norm-type state found the best state of all, 4.301387. That state is the
    norm-type state reshaped: its overlap with it is 0.956. No point's operator has it as an eigenstate, and it is not
    flat.
  - **Five wheels of 3: the searches fell short.** The best climb reached 6.082020. But the four-wheel best times a
    one-wheel best is a state of the array, with 517/81 = 6.382716 on either side, and the climb leaves it where it is.
    So V4's death is the search's: 4 000 climbs on each side ended 0.30 below a state already known.
  - **Climbing from the products** [read after the run]. Every product of two smaller arrays' best states is a fixed
    point of the climb, on its side and in the whole space. Every kick of the best one on each side climbed back to it
    or lower. At three wheels of 7 the products, 7.435601 (even) and 7.408174 (odd), stay far below the norm state.
  - **The coin.** As scored, the even side won at three wheels of 5 (by 0.0019) and five of 3, and the odd side at
    three of 7. But the searches on the two largest arrays fell short of known states. Read with those states, the
    sides tie at five of 3 (517/81 each), and at three of 7 the even side leads, 7.435601 against 7.408174. On all
    three arrays of three wheels tried, at 3, 5 and 7, the best state found sits on neither face.
- **Other flat states** [measured; read after the run]. Damski, Bistroń, Ponterio, Czartowski and Życzkowski build
  flat states like these for every p^n, as fiducials of product Weyl–Heisenberg mutually unbiased bases: from Alltop's
  cubic phases ω^Tr(a x³) for p ≥ 5, and from a Galois ring at 3 [NAMED]. The norm form is not among their
  constructions. [`flat_states.py`](flat_states.py) tries them against the norm-type states:
  - three wheels of 5: of the 624 states ω^(Tr(a x³) + b N(x)), 128 are flat. The best flat value is the norm-type
    states' 4.252724, and Alltop's states reach 4.057183;
  - three wheels of 7: 804 of 2 400 are flat. The best flat value, 7.902228, belongs to the norm-type states and 228
    mixed ones. Alltop's states reach 7.458638;
  - three wheels of 3: the 702 Galois-ring states, as we reconstructed the construction, are all flat, at 1.738433,
    below 17/9.

  [READING] Flatness alone does not make a winner. The norm-type states are the best flat states in every family
  tried, and they still lose at 5; the Galois-ring states are flat and fall well short at 3.
- **A correction to round 9** [measured]. Finding round 9's best states again, the seeded odd climbs on four wheels of
  3 reached 3.533331, above the 3.476833 that round 9 logged for the odd side. The operators' contraction confirms it.
  The even side's 98/27 stays ahead, so the coin there stands.

## 13. Round 11: the oscillator states [FORCED; measured; NAMED: Gurevich, Hadani and Sochen, Kurlberg and Rudnick, Katz]

> *zoom out, and look for work that shares ground, let's see if what we have is useful* — the author, 12 November 2026

Zooming out found that the two wheels of §9 are the two kinds of maximal torus in SL(2, p), and that their
eigenvectors, the oscillator states, are studied in radar and in quantum chaos, where their Wigner functions are
Kloosterman-type sums. Nobody we found had measured their magic. Round 11 measured every one of them, the p − 2
one-line states of the split torus and the p of the non-split torus, at every prime from 5 to 401: exactly, with no
search. Five predictions were registered with the script, [`oscillator_states.py`](oscillator_states.py), before the
run ([`PREREG.md`](PREREG.md)), and all five held.

- **The share of the ceiling is a statistic** [FORCED]. For a pure state on p levels, Σ W² = 1/p, so the root mean
  square of the Wigner function is exactly p^(−3/2), and S/√p, the sum of sizes over √p, is mean |W| over rms W. It
  depends only on the shape of the distribution of values: 8/(3π) = 0.849 for Sato–Tate, √(2/π) = 0.798 for a
  Gaussian (the average random state), 2√2/π = 0.900 for a uniform angle. The ratio μ4/μ2² separates them too: 2, 3
  and 1.5.
- **The oscillator states follow Sato–Tate** [measured, exact values]. At the primes from 211 to 401, over 20 056
  states:

  | | mean S/√p | mean μ4/μ2² |
  |---|---|---|
  | the oscillator states | **0.8468** | **2.0032** |
  | Sato–Tate | 0.8488 | 2 |
  | Gaussian, the average random state | 0.7979 | 3 |
  | uniform angle | 0.9003 | 1.5 |

  - So their magic obeys the same law as round 10's norm state, whose values are Kloosterman sums.
  - The non-split states sit on Sato–Tate's value once finite size is allowed for (0.8483). The split states come up
    from below (0.8452), held back by the tiny Wigner values on their two axes.
- **Two exact identities** [FORCED; proved in [`TORUS_MOMENTS.md`](TORUS_MOMENTS.md)]. Averaged over the non-split
  torus's p eigenvectors, μ4/μ2² is exactly 2p/(p + 1), which tends to Sato–Tate's 2. Averaging a phase-point operator
  over the torus gives an operator diagonal in that basis, so the average is a trace: a count of parallelograms on the
  torus's circles, weighted by their areas, which a Legendre-symbol sum closes.
  - The third moment is a count of triangles, and only degenerate triangles have area zero, so it is exactly
    2/(p²(p + 1)). The skew tapers as −(p + 2)/((p + 1)√(p − 1)), and its split by parity depends on whether the
    turning wheel holds a hexagon (p ≡ 2 mod 3). The exact law reproduces all 77 of round 12's logged skews.
- **The whole distribution** [measured; round 12, registered first, six of six held]. Standardized, the values follow
  the semicircle through the eighth moment: at the primes from 211 to 401 the third, fourth, sixth and eighth moments
  average −0.057, 2.010, 5.066 and 14.35, against the semicircle's 0, 2, 5 and 14 (Gaussian: 0, 3, 15, 105). All 2.06
  billion values lie at Kolmogorov distance 0.0072 from the semicircle law, against 0.0426 from the Gaussian. The skew
  shrinks like −1/√p, exactly (TORUS_MOMENTS.md §6). See [`TORUS_MOMENTS.md`](TORUS_MOMENTS.md) §5 and [`torus_moments.py`](torus_moments.py).
- **Good, not best** [measured]. The states lie close together: S/√p spreads by about 0.14/√p at each prime. So the
  best of them settles near 86% of the ceiling, between the average random state (80%) and the best states found by
  search from 7 to 31 (89 to 90%). None beats a known winner. At 5 one of them is the winner: Jain and Prakash's state.
- **The two wheels again.** The non-split torus's best beats the split torus's at 65 of the 77 primes, as round 8's
  turning-wheel advantage suggested.
- [READING] The author's one wheel and many wheels meet here. The states of one wheel's two tori and the norm state on
  three wheels both have Kloosterman-type values, and their magic follows the same Sato–Tate law: number theory
  decides how far a structured state's quasi-probabilities can spread.

## 14. Round 13: cubic magic [FORCED; measured; NAMED: Cui, Gottesman and Krishna, Howard and Vala, Mesnager, Özbudak and Sınak]

> *it's okay to drift, i am the visionary, you are the drafter... let's pick a useful direction* — the author,
> 14 November 2026

Round 10's proof used one fact about the norm: it is a cubic. A cubic-phase state, ψ_f = Σ ω^f(x) |x⟩ / √q with f of
degree at most 3, is the magic state of one of the third level's diagonal gates, the non-Clifford gates of
fault-tolerant computing with qudits [NAMED: Cui, Gottesman and Krishna]. Round 13 asked which of them carries the most
magic. Six predictions were registered with the script, [`cubic_magic.py`](cubic_magic.py), before the run
([`PREREG.md`](PREREG.md)); four held.

- **Every cubic state's Wigner function is a Walsh spectrum** [FORCED]. If C is f's cubic part, the Wigner values are
  S(w)/q², each q times, where S(w) = Σ_s ω^(w·s − 2C(s)). So the negativity is the L1 norm of a cubic's Walsh spectrum,
  and only the cubic part matters. For one qudit this was known as a cubic character sum [NAMED: Howard and Vala].
- **None reaches the ceiling** [FORCED, with NAMED]. By Parseval the ceiling needs a flat Walsh spectrum, a bent
  function, and Mesnager, Özbudak and Sınak proved that no homogeneous cubic is bent in odd characteristic.
- **On three wheels the norm state is the best cubic** [measured; exhaustive at 3 and 5]. Over all 2 187 cubic forms at
  3 and all 9 765 625 at 5, and 2 000 004 at 7, nothing beats the norm form: 17/9, 4.252724 and 7.902228. The CCZ-type
  state ω^(xyz) comes second at 3 (16/9). Per wheel the norm state beats both CCZ and three single-wheel cubes.
  - [READING] So among the diagonal non-Clifford gates on three qudits, the norm's phase gives the most negativity per
    magic state.
  - At 5 elliptic curves tie it: forms whose curve is smooth with 8 points have different Wigner values but the same
    negativity, to 10⁻⁹. Why is open.
  - From 11 on it is no longer the best: smooth curves beat it (§15).
- **On two wheels the cubics are not the record holders** [measured, exhaustive]. The best two-wheel cubic falls short of
  round 9's searches: (9 + 3√5)/10 = 1.570820 against 1.766937 at 5. From 7 to 23 it sits at 0.845 to 0.856 of the
  ceiling: the semicircle's 0.849 again.
  - [READING] A coin by p mod 3: the best two-wheel cubic splits into three rational lines when p is 2 more than a
    multiple of 3, and has one rational root when p is 1 more, at all seven primes from 5 to 23.

## 15. Round 14: the triangle, the planes and the Smith chart [FORCED; measured; READING]

> *if the triangle unfolds to 8 pointed curves under p=5, that makes sense to be a coin... do the fano, consider the
> double smith* · *the smith chart from electrical engineering... laid over other planes* — the author, 14 November 2026

Six predictions were registered with [`planes.py`](planes.py) ([`PREREG.md`](PREREG.md)); the forced one held and the
five fresh ones died.

- **The Smith chart laid over the phase plane** [FORCED]. The chart is the map z → (z − 1)/(z + 1). Its square is the
  impedance–admittance flip z → −1/z, which is the Fourier transform's action, and its fourth power is the identity: a
  quarter turn of the Riemann sphere. Over F_p it lies in the turning wheel exactly when p is 7 more than a multiple of 8,
  with order 8, and only at 7 is that the whole wheel. The double chart's flip fixes the most negative seven-level state.
- **The triangle unfolds only at 5** [measured]. At 7, 11 and 13 no curve but the norm class ties the norm value.
- **The norm state's reign ends at 11** [measured]. At 11 and 13, smooth curves beat it: 15.013610 against 14.900798 at
  11, on a curve with 12 points, and 19.498692 against 18.887726 at 13. The winners sit at Sato–Tate's share.
  - [READING] A coin by size: the triangle (no points) wins at 3, 5 and 7, and elliptic curves win from 11 on.
- **Design cubics are poor magic** [measured]. The Fano cubic on 7 wheels reaches 0.56 to 0.64 of √q and the
  affine-plane cubic on 9 wheels 0.78, below random cubics, whose share is the Gaussian 0.798. Their Walsh spectra take
  few values, and a concentrated spectrum has a small L1 norm.

## 16. Round 15: the free picture [FORCED; measured; NAMED: Voiculescu, Bożejko and Speicher]

> *2 and 3* — the author, 14 November 2026

[`TORUS_MOMENTS.md`](TORUS_MOMENTS.md) §7 reduces every moment of the oscillator states' Wigner values to polygons on
the torus's circles, weighted by their areas, and proves both ends. Pairings that do not cross have area 0 and give the
Catalan numbers, the semicircle's moments; crossing pairings fall away like 1/p. What is left is whether the other,
generic polygons' phases cancel. Round 15 registered eight predictions with [`free_moments.py`](free_moments.py)
([`PREREG.md`](PREREG.md)), and all eight held.

- At the sixth moment, at every prime up to 101, the generic polygons' part falls like 1/p: about 0.9/p when p is 1
  more than a multiple of 3, and 2.8/p when it is 2 more, the hexagons again.
- At 1009 the 10th and 12th moments are 42.20 and 133.1, against the semicircle's 42 and 132 (Gaussian: 945 and
  10 395).
- The corrections are free. At 1009 the fifth, seventh, ninth and eleventh moments over the third are 5.01, 21.01,
  83.8 and 328.7, against free probability's non-crossing counts 5, 21, 84 and 330; the classical counts are 10, 105,
  1 260 and 17 325.
- [READING] The Wigner values at a point are the eigenvalues of a sum of symmetries, one for each point of a circle.
  They add like free variables, because their commutation phase, a symplectic area, cancels on crossing pairings.

## 17. Round 16: the exact sixth moment, and modular forms [measured exactly; FORCED in part; NAMED: Hulek, Spandaw, van Geemen and van Straten]

> *go after an exact formula for the 6th moment first.. The free fourth cumulant equals 3/p² to every digit the log
> keeps. Worth a short exact proof as a small theorem* — the author, 14 November 2026

Every moment of the oscillator states' Wigner values is an exact integer count. Read from the states at every prime
up to 199, the counts fitted exact formulas, and round 16 then predicted them at every prime from 211 to 401 without
refitting ([`TORUS_MOMENTS.md`](TORUS_MOMENTS.md) §8; [`exact_moments.py`](exact_moments.py)).

- **The sixth moment is exact, and a modular form is in it.** Summed over the circles,
  Tr S_C⁶ adds up to p[5p⁴ − p³ − 5p² − 1 + (p + 1)(b(p) − (−3|p)p²)], where b(p) are the coefficients of
  (η(τ)η(2τ)η(3τ)η(6τ))², the newform of weight 4 and level 6. It is the form of the sixth moment of Kloosterman sums,
  and it enters only through the count of closed hexagons; the hexagons with phase 0 are a polynomial count.
- **The fourth free cumulant is exact,** and it is 3/p² only to leading order. Its next term depends on p mod 3, on
  p mod 4 and, when p ≡ 1 (mod 4), on the angle of the Gaussian prime a + bi with p = a² + b². Behind it is η(4τ)⁶,
  the form with complex multiplication by the Gaussian integers.
- **Proved:** the sixth moment, in full. The phase-0 hexagons are counted by an elementary argument, triangle by
  triangle, and the modular form comes only from the closed hexagons, through the classical evaluation of
  Kloosterman's sixth moment ([`verify_sixth_moment.py`](verify_sixth_moment.py)).
- **Open then:** the count behind the fourth cumulant, the fifth moments and J6, which fit no formula tried. The fifth
  moments are now exact (§18).
- Who else works on this ground, and what their theorems give this floor: [`LITERATURE_MAP.md`](LITERATURE_MAP.md).

## 18. Round 17: the fifth moments [FORCED; measured exactly; NAMED: Peters, Top and van der Vlugt; Clebsch]

> *1, apply the hexagon method to the fifth moments* — the author, 14 November 2026

Both fifth moments are exact ([`TORUS_MOMENTS.md`](TORUS_MOMENTS.md) §8, Theorems 6 and 7;
[`verify_fifth_moment.py`](verify_fifth_moment.py)).

- **J5 carries an elliptic curve and Kloosterman's fifth moment.** Summed over the circles, Tr(P S_C⁵) is
  p(p + 1)[f(p) − p·a_E(p) + (4(−3|p) − 3)p − 1]. Here f is the weight-3, level-15 form of Kloosterman's fifth moment,
  and E is the curve y² = x(x − 4)(4x² − 52x + 9), of conductor 150. The hexagon method proves it: the phase-0
  polygons number (p + 1)·#E(F_p).
- **I5 carries the weight-4 form of level 10,** through a double octic. Summed over the circles, Tr S_C⁵ is
  p(p + 1)[p³ + 4p² − (1 + (5|p))p − 4 + a(p)] − p⁵ − 1.
  - A second method gets there: expanding the conditions in Gauss sums of Hermitian forms leaves one count.
  - That count lives on the double cover of 3-space branched along Clebsch's diagonal cubic surface (1871) and its
    five Sylvester planes.
  - Its count matches the newform exactly at every prime tried; that match is the one step that is measured, not
    proved.
- **One count for every odd moment and every even parity-weighted moment.** The same method writes I_n (n odd) and J_n
  (n even) through the points of the turning wheel that multiply to ±1 and whose Cayley coordinates sum to 0.
  - It gives the third moment again.
  - It reduces the fourth cumulant's open count to one character sum on an elliptic surface.
  - It makes J6 a count on a fourfold.
- **The free picture holds at the fifth moment:** √p times the fifth moment tends to 5, as the free cumulants say.
- **The forms were named here.** [`modular_symbols.py`](modular_symbols.py) computes the Hecke eigenvalues of
  Γ0(N), and it reproduces the four weight-4 eta products of levels 5, 6, 8 and 9. It was written because LMFDB
  answered a burst of queries with a captcha, which this work does not try to get past.
- **Round 17** tested both formulas, the double octic and the curve at primes where they were not found
  ([`PREREG.md`](PREREG.md); [`fifth_moments.py`](fifth_moments.py) `test`). Six of seven held.
  - The double octic and the curve held blind to 601, in exact arithmetic.
  - The operators matched both formulas at every prime from 409 to 509, but missed the registered precision bar, so
    that half is inconclusive.

## 19. Round 18: J4 proved, and the fourth free cumulant with it [FORCED; NAMED: Landen, Jacobi]

> *1 and 2, J4's surface sum first* — the author, 14 November 2026

Theorem 5 is proved ([`TORUS_MOMENTS.md`](TORUS_MOMENTS.md) §8, "The proof of Theorem 5";
[`fourth_cumulant.py`](fourth_cumulant.py)).
- **The last open count of round 16 is closed.** It was one character sum on an elliptic surface. Pairing the four
  points leaves the Legendre family. A 2-isogeny over F_p, Landen's transformation, moves it to the Legendre family at
  the squares, and quartic Jacobi sums evaluate that.
- **The result.** T(p) = p + 2(a² − b²) when p ≡ 1 (mod 4) and p = a² + b² with a odd; T(p) = p when p ≡ 3 (mod 4).
  So J4 = (3p + 1)(p² − 1) − 4p(p + 1)b² at every odd prime, and the fourth free cumulant is exact.
- **The Gaussian integers' form η(4τ)⁶ comes from the Jacobi sum** of a character of order 4.
- **Round 18 held three of three.** The surface sum held at every prime from 409 to 3001, and every step of the proof at
  every prime to 1009.

## 20. Rounds 19 and 20: the coin at 5, and at 7 and 9 [FORCED; measured; NAMED: Clebsch, Laza and Zheng]

> *1 and 2, J4's surface sum first* — the author, 14 November 2026: the "1" says yes to testing the reading that the
> fifth moment's split by (5|p) is the coin at 5.

The details are in [`COIN_AT_FIVE.md`](COIN_AT_FIVE.md) ([`coin_at_five.py`](coin_at_five.py)).
- **The dictionary** [FORCED]. The double octic behind I5 is the coin at 5.
  - The five planes where one point sits at the centre are the solid face.
  - Clebsch's cubic, which holds the regular pentagon, is the flat face.
  - Their 15 rational lines are the edge.
  - The sign of a permutation swaps the two sixes of the cubic's other lines, as √5 ↦ −√5 does.
  - At the prime 5 the cubic pinches at the centre.
- **The edge, in the moments** (round 19). I5's formula holds at p = 5, where (5|5) = 0 averages its two sides, and at
  3. The parity-weighted moments J3 and J5 do not hold at their edges: that registered claim died, and is kept in the
  graveyard.
- **The coin at 7.** The flat face at 7 is the cubic fourfold {Σx = Σx³ = 0} in seven variables.
  - Its count was read after round 19 and held blind at every prime from 401 to 601 (round 20):
    #X7(F_p) = 1 + p + ⋯ + p⁴ + p²(14 + 6(5|p)) + p·c(p).
  - c is the weight-3 CM form of Q(√−35), as Laza and Zheng's lattice implies.
  - So 7 enters only through √−35 = √5·√−7, the pentagon's number times the heptagon's.
- **At 9**, where the coin breaks, the nine-variable cubic adds one character, (105|p) = (−3|p)(−35|p), and eight
  copies of the same CM form. That count also held blind.
- **The scores.** Round 19 held two of three scored predictions (C1 failed on its J side). Round 20 held two of two.

## 21. Rounds 21 to 28: the coin on its edge; eleven to eighty-one; the prime 3; and Theorem 8 [FORCED; measured; NAMED: Sabbah and Yu, LMFDB, Schütt, Klein, Yun, SGA 7]

> *1 and 2, the mirror rule first* — the author, 14 November 2026: a coin on its edge shows the mirror; and go past
> the base, to eleven.

> *1 and 3, seventeen first* — the author, 15 November 2026: register seventeen, and take up the reading that 13's
> piece is both faces at once.

> *2 and 3, 27 first* — the author, 15 November 2026: test the sharpened rule at 27, three coins of 3, first; and
> test seventeen's square classes blind.

> *1 and 3, 81 first* — the author, 15 November 2026: 81, four coins of 3, first; and twenty-five's own
> determinant.

> *2 and 3, the proof first* — the author, 16 November 2026: turn the rule into a theorem, and settle round 27's one
> assumption.

The details are in [`COIN_AT_FIVE.md`](COIN_AT_FIVE.md) §5 to §12 ([`edge_rule.py`](edge_rule.py)).
- **Why J3 mirrors at 3** [FORCED].
  - J3 counts corners of hexagons inscribed in the circles, and their ratio is a cube root of unity.
  - At p = 3 the two cube roots merge into 1. The hexagon's phase vanishes, and its sum over the circles is p − 1 = 2
    in place of −1 for each root.
  - At every prime edge q the q − 1 primitive roots merge into one point of weight p − 1 = q − 1, so the mirror is
    exact. At 9 it fails.
- **The rule.** On its edge a coin shows the fixed set of its flip. A count without a phase sees that set once, which
  averages the sides; a count with a phase mirrors.
- **The cubics' edges** (round 21: four of four held, blind).
  - Clebsch's cubic has 21 lines over F_5: the 15 of the edge, and 6 through the centre, where the double six's
    conjugate pairs merge.
  - Every symbol of the cubics in 5, 7 and 9 variables reads 0 at its edge prime.
  - The CM form enters with |c(p)| = p at 5 and 7, where its field ramifies.
- **Where the counts come from** [FORCED].
  - The cubics' counts are the moments of the cubic exponential sums. So they split into the symmetric powers of the
    Airy sheaf, whose Hodge numbers Sabbah and Yu computed.
  - Each n brings one new piece: (5|p) at 5, X7's form at 7 (LMFDB's 35.3.c.b, signs and all), and (105|p) at 9.
  - The cubics' nodes mod p number exactly the pieces' dimensions ramified at p.
- **Eleven** (round 22: five of five held, blind).
  - The cubic in eleven variables has the predicted shape at every prime from 13 to 401.
  - Its new piece is a weight-3 form with complex multiplication by Q(√−1155), and −1155 = (−3)(5)(−7)(−11).
  - √−11 entered at 11, where the centre pinches, as √−7 entered at 7.
- **Thirteen** (round 23: one of two scored held; round 24 held its read blind).
  - The new piece does not split into a twisted Tate class and a CM form; that registered prediction died.
  - It is a twisted symmetric square. At every prime, T13/p⁵ + (−15015|p)p² is a square times a product of −1, 2, 3,
    5, 11 and 13 that six characters decide. It held blind at every prime from 409 to 601.
  - −15015 = (−3)·5·(−7)·(−11)·13, the product of the signed roots up to 13, is its determinant's character.
- **Fifteen and "3 at its square"** (round 24: five of five held, blind).
  - The author: 9 is two coins of 3 tossed together, so 3 enters only at its square. In the pieces, 3 is absent from
    5 and 7 and present from 9 on.
  - At 15 the nodes, that reading and Schütt's condition leave one field, Q(√−3003). The piece has complex
    multiplication by exactly that field.
- **The prime 3** (round 25: three of three held, blind).
  - On Σx = 0 the cubic is 3e3, so it has a good model e1 = e3 = 0 at 3. Its nodes mod 3 are the sign vectors whose
    sum is a multiple of 9. The cubic in nine variables pinches at its centre mod 3, as the cubic in q variables does
    mod q.
  - Counted at 3 for the first time, the pieces below 9 keep their values: −27, and 27 from LMFDB's a₃ = 1. V9's line
    ramifies, and from 9 on each piece loses exactly one dimension. That is the author's "3 at its square", seen at 3
    itself.
- **Seventeen and twenty-one** (round 25).
  - Both new pieces have three dimensions, and both are twisted symmetric squares, like 13's.
  - Their determinants are those the nodes' parity gives. 17's, (−51051|p), held blind. 21's, (−138567|p), passes
    every test, but its registered sign test saw too few signs and is counted as not held.
  - The reading at 13 was made exact as a dictionary: a piece keeps a line exactly when the base's n points keep an
    axis. It died at 17. The 17-gon keeps its axis, but 17's piece keeps no line. "Both faces at once" belongs to
    the three-dimensional pieces, not to 13 alone.
- **Twenty-seven: the coins at the cube and the square** (round 26: seven of nine held; two lacked signs).
  - By the critical values, a node ramifies only at an odd valuation. For 3 the valuation starts one coin late, so 3
    enters at 9 but not at 27, and 5 enters at 5 and 15 but not at 25.
  - A faster counter (exponential sums mod primes, joined by the Chinese remainder theorem) reached 27 variables at
    every prime to 1999, and the field of p² elements to 151. That read each piece's determinant at each prime.
  - V27's determinant is (3187041|p) at all 27 primes, the same as V23's, which has no such node. The rivals fit at
    chance level. The infinite place had already ruled out 3 at 27; the count decided 5 at 25.
  - Twenty-one's determinant held prime by prime. Seventeen's and twenty-one's square classes held blind at 224 and
    273 new primes.
- **Eighty-one, and twenty-five** (round 27: five of five held).
  - The Hodge types come from the cubics alone: peeling the smooth cubics' Hodge numbers by the ballot triangle gives
    Sabbah and Yu's types to k = 201.
  - At 81 the only new node is the centre, which pinches only mod 3. V79's determinant is odd and V81's even, so 3
    enters at 81, four coins of 3, as the rule says. Complex conjugation decided it before any count.
  - The same argument decides every power of a prime ≡ 3 (mod 4), always as the rule does: 3 at its even powers, 7,
    11, 19, … at their odd powers. It is blind at 5, 13, 17 and the other primes ≡ 1 (mod 4).
  - So 25 had to be counted. A counter over the field of p³ elements read V25's determinant at all 27 primes from 29
    to 151: (3187041|p), so 5 does not enter at 25. The rival fits 14 of 27, about what chance gives.
  - The rule is one symbol, (p/A_k), with A_k the product of the odd numbers up to k, each multiple of 3 divided by 3
    once. Yun proved (p/d!!) for the Kloosterman moments; the cube's 3 is the difference.
  - The cubic in 81 variables, counted at 281 primes: every piece from V29 to V81 has its forced shape, and V79 and
    V81 behave like pieces with the full orthogonal group.
- **Theorem 8: the determinants, proved** ([`DETERMINANTS.md`](DETERMINANTS.md); round 28: five of five held).
  - Every piece V_k has determinant (p/A_k). The cubic's nodes are ordinary double points at every prime from 5 up
    and in the good model at 3. Each orbit of nodes gives the antisymmetric part, which is V_k, one vanishing cycle.
    Picard–Lefschetz turns it over exactly when the critical value has odd valuation, and the determinant is
    unramified at 2.
  - So the author's coins hold at every k, and complex conjugation fixes every middle class: round 27's one
    assumption is now a corollary.
  - Its first new predictions, the determinants of V29, V31, V33, V35 and V39, held blind at every prime from 41 to
    151. Yun's symbol without the cube's 3 fits at chance level where the two differ.
  - Credited: Picard–Lefschetz (SGA 7); Chuang's thesis, which already holds the local picture at primes from 5 up
    in another model; Yun's (p/d!!) for the Kloosterman moments.
- **Theorem 9: the pieces at 7, 11 and 15 are CM newforms** [FORCED, given Theorem 8 and Corollary 2; NAMED: Livné
  1995, Serre, Hecke] ([`CM_PIECES.md`](CM_PIECES.md)).
  - Each is two-dimensional and orthogonal, with a nontrivial determinant. So it is induced from a Hecke character
    of Q(√−35), Q(√−1155) or Q(√−3003), and the conductor makes that character unramified (at 15 after twisting
    by (5|·)).
  - The class groups have exponent 2, so there are 2, 8 and 8 candidates. Exactly one has the measured traces at
    every good prime to 401.
  - At 7 it is 35.3.c.b, Chênevert's theorem by another route. At 11 and 15 the signs on the ramified primes are
    (3, 5, −7, 11) and (3, 7, −11, 13).
  - The one-dimensional pieces at 5 and 9 equal their determinants. Only 13, 17 and 21 are left measured.

## 22. Round 29: one wheel, the qudit T state and the ladder [FORCED; measured; NAMED: Howard and Vala, Cui, Gottesman and Krishna, Katz, Deligne, Wilson and White, Zhu, Mao and Yi, Feng and Luo]

> *where can we try and extend this to be useful on the frontier of applications?* and *1 yes, then the qudit round*
> — the author, 17 November 2026

Round 29 put one qudit's magic states against random states. Six predictions were registered with the script,
[`one_wheel.py`](one_wheel.py), before the test ([`PREREG.md`](PREREG.md)), and five held. For readers outside this
project, the statements and evidence are in a short note in standard terms:
[`QUDIT_NEGATIVITY_NOTE.md`](QUDIT_NEGATIVITY_NOTE.md).

- **The T state's law** [FORCED from NAMED; measured].
  - The T state's Wigner values are Birch sums (round 13, with one wheel). So its sum of sizes is
    S = (1/p)Σ_a|S_t(a)|, and by the semicircle law S/√p tends to 8/(3π) = 0.8488.
  - Measured: a mean of 0.84890 over every class at every prime from 1000 to 3000.
- **It beats random states at every prime from 31 to 5000** [measured].
  - The exact Haar mean is p·E|2X − 1| with X ~ Beta((p + 1)/2, (p − 1)/2). It tends to √(2/π)·√p = 0.7979√p, which is
    Wilson and White's mana.
  - Every class of T state is above it at all 659 primes.
- **The ladder is not monotone** [FORCED from NAMED; measured].
  - A degree-d phase state's rows are sums of odd polynomials of degree 2m + 1 (d = 2m + 1 or 2m + 2). By Katz's
    monodromy and Deligne's equidistribution, they behave like traces of random USp(2m) matrices.
  - E|tr| is 0.8488, 0.7905, 0.7985, 0.7978, …, tending to 0.7979.
  - Measured at the 114 primes from 700 to 1500:
    - x⁵, x⁶ and random quintics and sextics sit at 0.7899 to 0.7907, below random states at every one of the primes;
    - x⁷, x⁸ and random septics and octics sit at 0.7979 to 0.7986.
  - [READING] So among the polynomial phase gates ω^f on one qudit, only the cubic level, the T gate, beats random
    states for Wigner negativity, and degrees 5 and 6 fall below them. The hierarchy's higher levels also hold
    p^m-th-root phases (Cui, Gottesman and Krishna), which were not tested.
- **At 5 and 7 the T state is the best phase state** [measured, exhaustive].
  - Over all 25 phase classes at 5, and all 2401 at 7, the maximum is a T state: S = 1 + 2/√5 at 5, and 2.450304 at 7
    (t = 1). The registered guess Q5 said otherwise, and died.
  - At 11 a degree-10 phase beats T in a sample of 10⁶ (2.877 against 2.827). At 13 no sampled phase does (T has
    3.2047).
  - Feng and Luo found 500 diagonal gates with other phases that beat T at 5 [NAMED]. Among phases that are p-th
    roots of unity, T is the maximum at 5 and 7.
- **The moments are the cubics' counts** [FORCED].
  - The T state's n-th Wigner moment is p^(1−2n)Σ_a S_t(a)^n, which is given by Livné's counts.
  - Chênevert's form 35.3.c.b enters the seventh: (14 + 6(5|p))/p⁹ + a_p/p¹⁰ when p ≡ 2 (mod 3).
- **When p ≡ 1 (mod 3), the cubic Gauss sum splits the three T states** [FORCED; derived; checked to 1000].
  - Σ_a S_t(a)³ = 2p² + 2p·Re(χ(3t)G(χ)²), while the fourth moment, 2p³ − p², is the same for all three.
  - This is Zhu, Mao and Yi's Lemma 24 (2024), read through the Wigner function [NAMED]. They treat third moments of
    Clifford orbits, and their κ(f, T) = g(3, ac)²/d² gives Σ_a S_t(a)³ = p·g(3, 3t)². The three Clifford classes of T
    gates are Feng and Luo's (2025) [NAMED].
  - [measured] The class split is what keeps the T state from settling fast. A single class (p ≡ 2 mod 3), and the
    three classes' mean, deviate by about 0.0005 from 1000 to 5000. The spread between the classes shrinks like
    p^(−1/2) (0.0039 rms from 3000 to 5000).
  - [measured] The class with the largest third moment is the most negative at 24 of 77 primes, which is chance.

## 23. Our space, and what it cannot hold [FORCED; FENCE]

- In our three-dimensional space the two faces cannot be one rigid object, because no symmetry of the octahedron
  has order 7.
- Each face lives in space by itself. The heptagon's turns and flips act on a spin-3 system as rotations: a
  seventh of a turn is the clock, and half a turn about a perpendicular axis is the flip. The octahedron's
  rotoreflection turns its six corners.
- The faces meet only in the seven-dimensional space of states. There the Fourier transform joins them, and it
  is a quantum operation, not a motion of space.
- The magic subspace is a complex copy of three-space. The octahedron's rotations act there as on ordinary
  space, but the whole 168 cannot be a group of rotations: the finite rotation groups are the cyclic, the
  dihedral and the three polyhedral groups, and it is none of them [NAMED: Klein].
- [FENCE] All of this is standard finite-dimensional quantum mechanics and classical group theory. It says how
  the sevenths' two faces act on a seven-level system, and it claims nothing new about particles. A physical
  reading would go to [`../../lab/FENCED_READINGS.md`](../../lab/FENCED_READINGS.md), with the test that would
  decide it.

## 24. Standing

- **Known, and credited:**
  - the Weyl operators and the Clifford group;
  - the p + 1 mutually unbiased bases;
  - the discrete Wigner function, and its positivity on the states built from shifts and clocks (Wootters 1987;
    Gross 2006);
  - PSL(2, 7) ≅ GL(3, 2), and Klein's quartic with its three-dimensional representation, the odd part of the
    Weil representation;
  - SL(2, 5) as the binary icosahedral group;
  - Galois's subgroups of index 7, which are the 14 copies of S₄;
  - the strange and Norrell states, their shared largest mana, and the thauma's ranking (Veitch et al. 2014;
    Wang, Wilde and Su 2020; Jain and Prakash 2020);
  - Jain and Prakash's five-level maximum, found by their search. Round 3's count makes its symmetric part exact;
  - that a state fixed by a group of Clifford operations is stationary for mana, with the list of such states for
    two, three and five levels (Erew and Goldstein 2025);
  - the tools round 4 borrows: Samuelson's inequality, Good and Turing's estimate of the unseen, and the sign of
    the half turn's operator in the Weil representation;
  - Liu and Winter's theorem that typical many-body states are nearly maximally magic, and Knipfer, Roman, Matcheva
    and Matchev's values of M₂ for two qudits;
  - the norm and the quadratic character of a finite field;
  - Kloosterman sums, Weil's bound on them, Davenport and Hasse's theorem on Gauss sums of lifted characters, and
    Katz's theorem that the Kloosterman angles follow the Sato–Tate law;
  - flat states for every p^n as fiducials of product Weyl–Heisenberg mutually unbiased bases, from Alltop's cubic
    phases (Alltop 1980; Klappenecker and Rötteler 2004) and a Galois ring at 3 (Damski, Bistroń, Ponterio,
    Czartowski and Życzkowski 2026);
  - the two wheels as the split and non-split tori, whose eigenvectors are the oscillator system (Gurevich, Hadani and
    Sochen 2008) and the Hecke eigenfunctions of the cat map; their Wigner functions as Kloosterman-type sums, bounded
    by 2/√p (Gurevich and Hadani), with Sato–Tate statistics (Kurlberg and Rudnick 2005). Round 10's Kloosterman
    values come from the same mechanism; the reading of them as magic was not found.
- **This repository's own:**
  - the dictionary, and the reading that puts the sevenths' two faces, the octahedron with its centre, the cube
    and Klein's space into one picture;
  - the most negative seven-level state found, its four symmetries, its two Fourier frames, and the coin it
    makes with the Legendre state;
  - round 3 at seven levels, by exhaustion: the record is the best even state and the best state with any
    symmetry, and the Legendre state is the best odd state; the record's exact value, of degree 12;
  - round 3 at eleven levels, by search: the tetrahedral odd state, the even winner, and the coin across 3, 5,
    7 and 11;
  - round 4: the record beats every state with any symmetry, ordinary or mirror; a rival needs 8 to 24
    negative points; at eleven, exhaustive counts for symmetries of order 4, 5, 6 and 11; at thirteen, the two
    sides; and the rule that the tetrahedral states sit on the Legendre state's side;
  - round 5: the coin at 17 and 19, the odd side's win at 19, and the exceptional groups' states there, all on
    the Legendre state's side;
  - round 6: the coin at 23 and 29, and the test of the author's prediction;
  - the angles (flatness, the edge's two effects, the two wheels) and round 8's two-wheels test;
  - round 7: the coin at 31, and the test of the author's 7-wheel;
  - round 9: the coin in arrays, the small arrays' best values (search results), and the norm state on three wheels
    of 3, exact: the best found there, and on neither face;
  - round 10: on three wheels of every odd prime the norm-type states are flat, and their Wigner values are
    Kloosterman sums, so their negativity is exact at every p, read as magic (the mechanism is close kin to Gurevich
    and Hadani's); the larger arrays' values (search results), with the norm state's win on three wheels of 7;
  - round 11: the magic of every oscillator state up to 401, exact: it follows the Sato–Tate law; and the theorem that,
    averaged over the non-split torus's states, the fourth-moment ratio is exactly 2p/(p + 1) and the third moment
    exactly 2/(p²(p + 1)), so the skew tapers as −1/√p ([`TORUS_MOMENTS.md`](TORUS_MOMENTS.md)).
  - round 29: one qudit's T state beats random states at every prime from 31 to 5000, with S/√p → 8/(3π); the
    ladder above it is not monotone (the fifth level falls below random, as USp(4)'s trace predicts); and at 5 and
    7, exhaustively, the T state is the most negative phase state (§22).

  Web searches (2026-11-07 to 09), Erew and Goldstein's list and the OpenAI math release cover three and five
  levels, and nothing on seven, eleven or thirteen. Web searches on 2026-11-10 found no maximum of the total Wigner
  negativity for three or more qutrits, and no use of the norm state as a magic state. They found Damski et al.'s
  flat states, but not the norm construction or Kloosterman sums as a state's Wigner values.
- **The yield.** Round 1 was mostly known: seven classical facts confirmed, and one guess dead. Round 2 is new
  as far as we checked, but it is a measurement, not a proof. Round 3 is new as far as we checked. At seven it
  is exhaustive for every state with a symmetry, exact up to rounding: the nearest rival values sit 0.0028 and
  0.0067 below. At eleven it is a search. Round 4 is new as far as we checked: exhaustive at seven for every
  state with a symmetry of any kind, exhaustive at eleven for symmetries of order 4, 5, 6 and 11, and a search
  at thirteen. Round 5 is a search, except its forced rule, and its guesses read off 3 to 13 mostly died.
  Round 6 is a search, and both of its readings died. Round 7 is a search, and the author's rule died at the first
  prime it predicted. Round 9 held all eight, but six only checked pilots; what it adds is exact arithmetic about large
  arrays, small arrays' values by search, and one exact state, read after the run. Round 10 held two of seven. What
  it adds is exact: the norm-type states' flatness and Kloosterman values on three wheels of every prime. Its searches
  taught that at 243 and 343 levels random climbs stop short of states already known. Round 11 held five of five, on
  exact values: the oscillator states' magic follows the Sato–Tate law. Its mechanism is Gurevich and Hadani's; the
  measurement and the exact identity are new as far as we checked. Round 12 held six of six: the full distribution is
  the semicircle through the eighth moment, measured; the third and fourth moments are proved. Round 13 held four of six: every
  cubic state's Wigner function is a Walsh spectrum (exact), and the norm state is the most magic cubic on three
  wheels of 3, 5 and 7 (exhaustive at 3 and 5), though not from 11 on. Round 14 held one of six, the forced Smith
  chart: its other five guesses died, and the deaths are kept. Round 16 held six of six: the sixth moment and the
  fourth free cumulant are exact, with modular forms in them. Round 15 held eight of eight: every moment reduces
  to polygon counts, only the non-crossing pairings survive, and the corrections are free. Round 17 held six of seven:
  the fifth moments are exact, the double octic and the curve held blind in exact arithmetic, and the operator checks
  at 409 to 509 matched but missed their precision bar. Round 18 held three of three: J4, and with it the fourth free
  cumulant, is proved, by Landen's transformation and quartic Jacobi sums. Round 19 held two of three. Its dictionary
  finds the author's coin at 5 in the fifth moment's double octic, and the coin at 7 in the arithmetic of its flat face.
  The parity-weighted moments' formulas did not hold at the edge primes, and that death is kept. Round 20 held two of
  two: exact counts for the cubics in 7 and 9 variables, held blind. Round 21 held four of four. On their edges the
  cubics see the fixed set of the flip, and J3's mirror is the merge of the cube roots. Round 22 held five of five: in
  eleven variables √−11 enters, by complex multiplication by Q(√−1155). Round 23 held one of two scored: the piece at
  13 does not split, and the read after, a twisted symmetric square with determinant (−15015|p), held blind in round 24,
  which also held fifteen's field, Q(√−3003), five of five. Round 25 held nine of eleven scored. The author's "3 at its
  square" held at the prime 3 itself, in the cubic's good model there, and the nodes' parity gave seventeen's
  determinant blind. The reading at 13, made exact as a dictionary with the base's axes, died at 17, and twenty-one's
  sign test saw too few signs to count. Round 26 held seven of nine. At 27, 3 does not enter at its cube and 5 does
  not enter at its square, read in V27's determinant at every prime against three rivals. Twenty-one's determinant and
  the square classes of 17 and 21 held blind. Two sign tests saw too few signs to count, and none of their signs
  disagreed. Round 27 held five of five. At 81, 3 enters again, four coins of 3: complex conjugation decides it,
  as it decides every power of a prime ≡ 3 (mod 4). Twenty-five's own determinant, counted at every prime over the
  field of p³ elements, keeps 5 out at its square. The rule is Yun's double factorial with the cube's 3 taken out.
  Theorem 8 then proves the rule, with its corollary on complex conjugation, and round 28 held five of five: the
  first determinants past 27 are the theorem's, at every prime.
  Round 29 held five of six. The T state's law and its lead over random states held, and so did the ladder, with the
  fifth level below random. The guess that the T state is not the best phase state at 7 died: at 5 and 7 it is the
  best.
- **Open:**
  - a proof at seven for states with no symmetry of any kind: about 10^10 classes of sign choices remain;
  - at eleven, states whose only symmetries have order 2 or 3;
  - which side wins at large p. The odd side won at 19 and 29, the even side at 23 and 31. The author's 7-wheel died at
    31, and no number wheel of base 2 to 30 fits every decided prime. The rival observation, that the odd side wins at
    primes 4 more than a multiple of 5, fits all nine on two odd wins; 37 would test it again (about six hours), and
    59 is beyond this machinery;
  - why a turning symmetry usually beats a multiplying one at equal family size (12 of 14 pairs, read after round 8),
    and why not at 13 and 19;
  - many wheels: whether the norm state is the maximum on three wheels of 3 and of 7; what the four-wheel best, 98/27,
    is; what the best state on five wheels of 3 is, where the searches stopped below the product 517/81; and a search
    that reaches the top at 243 levels and more, which must start from the states already known;
  - the oscillator states: a proof that the generic polygons' area phases cancel at every even order, the one step
    left for the whole semicircle (round 15 measured the sixth, and Theorem 4 now proves it); the double octic's
    count behind I5, which matches the level-10 form at every prime tried; and J6, now a count on a fourfold;
  - the coin:
    - proofs of the cubics' Airy pieces;
    - a blind test of the mirror half, which needs a new parity-weighted formula;
    - the roots of the pieces at 13, 17 and 21: the weight-3 newforms they are the symmetric squares of;
    - the coins that complex conjugation cannot see, past 25: 125 (three coins of 5) and 169 (two coins of 13), whose
      pieces have 21 and 29 dimensions;
    - the four-dimensional pieces' Hilbert-type roots over Q(√969969) and Q(√3187041);
    - whether the seventh moment carries Q(√−35), as the fifth carries √5;
  - cubic magic: why elliptic curves with 8 points tie the norm form at 5; whether the two-wheel coin by p mod 3
    continues; and the best cubic on four or more wheels.

## Run it

```
python verify_seven_levels.py          # about two minutes (numpy + scipy)
python verify_seven_levels.py --full   # adds the long counts (2^24, 2^28, the norm state's symmetries) and reruns: about 50 minutes
python verify_norm_state.py            # NORM_STATE.md's proof, checked: about a minute (numpy)
python most_negative.py                # round 2's search, about a minute and a half
python round3.py                       # round 3, about seven minutes (numpy + sympy)
python round4.py seven                 # round 4's three parts, run at once: about 17, 43 and 19 minutes
python round4.py eleven
python round4.py thirteen
python round5.py seventeen             # round 5, run at once: about 33 and 34 minutes
python round5.py nineteen
python round5.py combine
python round6.py twentythree           # round 6, run at once: about 29 and 70 minutes
python round6.py twentynine
python round6.py combine
python two_wheels.py A                 # round 8, run at once: about 8 and 18 minutes
python two_wheels.py B
python two_wheels.py combine
python round7.py thirtyone             # round 7, about two hours
python round7.py combine
python many_wheels.py three            # round 9, run two at a time: about 30, 60, 20 and 120 minutes
python many_wheels.py four
python many_wheels.py five
python many_wheels.py seven
python many_wheels.py combine
python edge_state.py                   # the three-wheel winner as the norm state, about 20 minutes
python larger_arrays.py calibrate      # round 10: the check against round 3's code, about two minutes
python larger_arrays.py run            # about three hours on six workers
python larger_arrays.py combine
python flat_states.py                  # read after round 10: the flat states, under a minute
python product_climbs.py               # read after round 10: the climbs from products, about 15 minutes on six workers
python oscillator_states.py calibrate  # round 11: seconds
python oscillator_states.py run        # about seven minutes, one process
python oscillator_states.py combine
python verify_torus_moments.py         # TORUS_MOMENTS.md's proof, step by step: seconds
python torus_moments.py calibrate      # round 12: seconds
python torus_moments.py run            # about eleven minutes, one process
python torus_moments.py combine
python cubic_magic.py calibrate        # round 13: seconds
python cubic_magic.py run              # about seven minutes, one process
python cubic_magic.py combine
python planes.py run                   # round 14: about twenty minutes, one process
python planes.py combine
python free_moments.py calibrate       # round 15: seconds
python free_moments.py run             # about nine minutes, one process
python exact_moments.py collect        # round 16: seconds
python exact_moments_fit.py            # the exact fits, about a minute (sympy)
python exact_moments.py test           # the blind test, minutes
python verify_sixth_moment.py          # the sixth moment's proof, step by step: seconds
python modular_symbols.py              # the engine that names the forms, checked on four eta products: seconds
python fifth_moments.py collect        # round 17: the double octic's sums to 401, a minute
python verify_fifth_moment.py          # the fifth moments' proofs, step by step: under a minute
python fifth_moments.py test           # round 17's blind test at 409..601, minutes on four processes
python fourth_cumulant.py              # Theorem 5's proof, step by step at every odd prime to 401: seconds
python fourth_cumulant.py test         # round 18: the surface sum to 3001, a minute on four processes
python coin_at_five.py                 # the coin at 5: the dictionary, checked, seconds
python coin_at_five.py test            # round 19: the edge, and the cubics to 397, a minute on four processes
python coin_at_five.py test20          # round 20: the cubics at 401..601, blind, a minute on four processes
python edge_rule.py                    # the coin's edge: the forced checks F1 to F5, seconds
python edge_rule.py test               # round 21: the cubics at their edge primes 5 and 7, blind, seconds
python edge_rule.py test22             # round 22: the cubic in eleven variables to 401, a minute on four processes
python edge_rule.py test23             # round 23: the cubic in thirteen variables to 401, a minute on four processes
python edge_rule.py test24             # round 24: thirteen at 409..601, blind, and fifteen to 401, a minute on four processes
python edge_rule.py verify25           # round 25's forced checks: the base's rule at 13, 17, 21 and the good model at 3, seconds
python edge_rule.py test25             # round 25: seventeen to 401, twenty-one to 113, and the prime 3, a minute on four processes
python edge_rule.py verify26           # round 26's forced checks: the infinite place, reading a determinant, the new counter, seconds
python edge_rule.py test26             # round 26: 27 variables to 1999 and the field of p^2 elements to 151, two minutes on four processes
python edge_rule.py verify27           # round 27's forced checks: the Hodge types, the infinite place at every k, the symbol, the p^3 counter, seconds
python edge_rule.py test27             # round 27: 81 variables at 83..1999 and the field of p^3 elements to 151, four minutes on four processes
python verify_determinants.py          # Theorem 8 (DETERMINANTS.md), step by step, about a minute
python verify_conductors.py            # its conductor corollary, against the L-function's functional equation, under a minute
python verify_cm_pieces.py             # Theorem 9: the pieces at 7, 11 and 15 are CM newforms, under a minute
python one_wheel.py calibrate          # round 29's forced identities, at the primes up to 29, under a minute
python one_wheel.py test               # round 29: the T state to 5000, the ladder from 700 to 1500, three minutes on four processes
python one_wheel.py reads              # after round 29's test: where the T state's slow approach comes from, a minute
python edge_rule.py test28             # round 28: the determinants of V29 to V39, blind, four minutes on four processes
```

- The first reruns all eight predictions and the page's other checks, among them the states recorded by rounds 2
  and 3. It exits with 1 if the recorded score changes or a check fails. With `--full`, its output is kept in
  [`verify_seven_levels.log`](verify_seven_levels.log).
- The second reruns round 2's search, which is seeded, and rewrites [`most_negative.log`](most_negative.log).
- The third reruns round 3, which is seeded, and rewrites [`round3.log`](round3.log). The scored lines were the same
  on two runs.
- The lines for rounds 4 to 15, `edge_state.py`, `flat_states.py` and `product_climbs.py` rerun those runs, which
  are seeded or exact, and rewrite their logs.

## Sources

- H. Weyl, *The Theory of Groups and Quantum Mechanics* (1931); J. Schwinger, "Unitary operator bases",
  *Proc. Natl. Acad. Sci.* **46** (1960).
- D. Gottesman, "Fault-tolerant quantum computation with higher-dimensional systems" (1999).
- W. K. Wootters, "A Wigner-function formulation of finite-state quantum mechanics", *Ann. Phys.* **176** (1987);
  W. K. Wootters and B. D. Fields, "Optimal state-determination by mutually unbiased measurements", *Ann. Phys.*
  **191** (1989).
- D. Gross, "Hudson's theorem for finite-dimensional quantum systems", *J. Math. Phys.* **47** (2006).
- M. Howard, J. Wallman, V. Veitch and J. Emerson, "Contextuality supplies the 'magic' for quantum computation",
  *Nature* **510** (2014).
- F. Klein, "Ueber die Transformation siebenter Ordnung der elliptischen Functionen", *Math. Ann.* **14** (1878);
  N. D. Elkies, "The Klein quartic in number theory", in *The Eightfold Way* (1999).
- É. Galois, letter to Auguste Chevalier (1832): PSL(2, p) has a subgroup of index p only for p ≤ 11.
- V. Veitch, S. A. H. Mousavian, D. Gottesman and J. Emerson, "The resource theory of stabilizer quantum
  computation", *New J. Phys.* **16** (2014) 013009.
- X. Wang, M. M. Wilde and Y. Su, "Efficiently computable bounds for magic state distillation", *Phys. Rev.
  Lett.* **124** (2020) 090505.
- A. Jain and S. Prakash, "Qutrit and ququint magic states", *Phys. Rev. A* **102** (2020) 042409,
  [arXiv:2003.07164](https://arxiv.org/abs/2003.07164).
- M. Erew and M. Goldstein, "Extremizing measures of magic on pure states by Clifford-stabilizer states" (2025),
  [arXiv:2512.19657](https://arxiv.org/abs/2512.19657).
- P. A. Samuelson, "How deviant can you be?", *J. Amer. Statist. Assoc.* **63** (1968).
- I. J. Good, "The population frequencies of species and the estimation of population parameters",
  *Biometrika* **40** (1953).
- A. Weil, "Sur certains groupes d'opérateurs unitaires", *Acta Math.* **111** (1964).
- Z.-W. Liu and A. Winter, "Many-body quantum magic", *PRX Quantum* **3** (2022) 020333,
  [doi:10.1103/PRXQuantum.3.020333](https://link.aps.org/doi/10.1103/PRXQuantum.3.020333).
- M. Knipfer, A. Roman, K. Matcheva and K. Matchev, "Analytical landscape of maximal magic for two-qutrit states and
  beyond" (2026), [arXiv:2607.07197](https://arxiv.org/abs/2607.07197).
- R. Lidl and H. Niederreiter, *Finite Fields* (1983): the norm and the quadratic character.
- H. D. Kloosterman, "On the representation of numbers in the form ax² + by² + cz² + dt²", *Acta Math.* **49**
  (1926).
- H. Davenport and H. Hasse, "Die Nullstellen der Kongruenzzetafunktionen in gewissen zyklischen Fällen", *J. reine
  angew. Math.* **172** (1935).
- A. Weil, "On some exponential sums", *Proc. Natl. Acad. Sci.* **34** (1948).
- N. M. Katz, *Gauss Sums, Kloosterman Sums, and Monodromy Groups*, Annals of Mathematics Studies **116** (1988).
- W. O. Alltop, "Complex sequences with low periodic correlations", *IEEE Trans. Inf. Theory* **26** (1980).
- A. Klappenecker and M. Rötteler, "Constructions of mutually unbiased bases", in *Finite Fields and Applications*,
  Lecture Notes in Computer Science **2948** (2004).
- B. S. Damski, R. Bistroń, D. Ponterio, J. Czartowski and K. Życzkowski, "Product Weyl–Heisenberg covariant mutually
  unbiased bases and extremal non-stabilizerness" (2026), [arXiv:2603.15550](https://arxiv.org/abs/2603.15550).
- S. Gurevich, R. Hadani and N. Sochen, "The finite harmonic oscillator and its associated sequences", *Proc. Natl.
  Acad. Sci.* **105** (2008), [PMC2481336](https://pmc.ncbi.nlm.nih.gov/articles/PMC2481336); and "... and its
  applications to sequences, communication and radar", [arXiv:0808.1495](https://arxiv.org/abs/0808.1495).
- S. Gurevich and R. Hadani, "Proof of the Kurlberg–Rudnick rate conjecture",
  [arXiv:math-ph/0404074](https://arxiv.org/abs/math-ph/0404074); and "Bounds on certain higher-dimensional
  exponential sums via the self-reducibility of the Weil representation",
  [arXiv:math/0612765](https://arxiv.org/abs/math/0612765).
- P. Kurlberg and Z. Rudnick, "On the distribution of matrix elements for the quantum cat map", *Ann. of Math.*
  **161** (2005).
- J. Cui, D. Gottesman and A. Krishna, "Diagonal gates in the Clifford hierarchy", *Phys. Rev. A* **95** (2017),
  [arXiv:1608.06596](https://arxiv.org/abs/1608.06596).
- M. Howard and J. Vala, "Qudit versions of the qubit π/8 gate", *Phys. Rev. A* **86** (2012),
  [arXiv:1206.1598](https://arxiv.org/abs/1206.1598).
- S. Mesnager, F. Özbudak and A. Sınak, "On the p-ary (cubic) bent and plateaued (vectorial) functions", *Des.
  Codes Cryptogr.* **86** (2018).
