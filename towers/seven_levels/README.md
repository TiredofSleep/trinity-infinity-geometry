# Seven levels: the two faces of 7 on a quantum system

> *how can these viewpoints syncronize to our viewing space for quantum parts?* · *what extensions would this
> imply? test them?* — the author, 7 November 2026

### Tags: **[FORCED]** checked by [`verify_seven_levels.py`](verify_seven_levels.py) · **[NAMED]** a cited standard result · **[READING]** an interpretation · **[FENCE]** outside the mathematics.

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
    turning wheel.
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

## 13. Our space, and what it cannot hold [FORCED; FENCE]

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

## 14. Standing

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
    and Hadani's); the larger arrays' values (search results), with the norm state's win on three wheels of 7.

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
  taught that at 243 and 343 levels random climbs stop short of states already known.
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
    that reaches the top at 243 levels and more, which must start from the states already known.

## Run it

```
python verify_seven_levels.py          # about two minutes (numpy + scipy)
python verify_seven_levels.py --full   # adds the long counts (2^24, 2^28, the norm state's symmetries) and reruns: about 25 minutes
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
```

- The first reruns all eight predictions and the page's other checks, among them the states recorded by rounds 2
  and 3. It exits with 1 if the recorded score changes or a check fails. With `--full`, its output is kept in
  [`verify_seven_levels.log`](verify_seven_levels.log).
- The second reruns round 2's search, which is seeded, and rewrites [`most_negative.log`](most_negative.log).
- The third reruns round 3, which is seeded, and rewrites [`round3.log`](round3.log). The scored lines were the same
  on two runs.
- The lines for rounds 4 to 10, `edge_state.py`, `flat_states.py` and `product_climbs.py` rerun those runs, which
  are seeded, and rewrite their logs.

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
