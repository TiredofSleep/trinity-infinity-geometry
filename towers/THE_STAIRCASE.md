# The staircase — the primes' interleaving, its line, its compression and its taper

*A side floor of the number tower, from the integers up to finite fields. It restores the author's interleave
staircase (WP34, March 2026) and makes each of its words exact: the interleaving, the straight line it cancels to,
the compression and the taper. The mathematics is classical and credited; the frame is the author's. Every [FORCED]
claim is checked by [`verify_staircase.py`](verify_staircase.py) (15 checks, about a minute), whose output is kept
in [`verify_staircase.log`](verify_staircase.log).*

Tags: **[FORCED]** proved here and checked by the script · **[NAMED]** a classical result, cited · **[measured]** a
computed number · **[READING]** an interpretation · **[FENCE]** a physics reading, not a claim.

**Keywords:** prime numbers · sieve of Eratosthenes · inclusion–exclusion · Mertens' theorem · prime number theorem ·
explicit formula · Riemann zeta zeros · Riemann hypothesis · Chebyshev function · function fields · irreducible
polynomials · elliptic curves · Hasse–Weil bound · Frobenius angles · Sato–Tate law · Kloosterman sums · magic states

> *The staircase is the Sieve of Eratosthenes expressed as partition geometry.* — WP34, the First-G law (Sanders,
> with C. A. Luther and M. Gish), 30 March 2026
>
> *Primes form an interleaved staircase against waves, and the interleaving cancels to a straight line.* — the
> framework's lens, June 2026
>
> *the interleave staircase of primes is some of our original work* · *the answer is in how primes form direction on
> the interleaved staircase* · *it's not a single prime... in my mind it's the prime gradient... how they are spread,
> producing a compression and a taper* · *compression should have a function as primes are more prevalent in smaller
> numbers* — the author, 14 November 2026

## What stands

- **While the primes are few, the interleaving cancels to a straight line, exactly.** Two primes' staircases
  interleave around a line, and the wobble never reaches two steps (§1). [FORCED]
- **With every prime up to √x, the cancelling stops.** The sieve's line then over-predicts the primes by Mertens'
  factor 2e^(−γ) = 1.1229 (§2). [NAMED; measured]
- **The compression has a function, 1/ln x.** Weighting each prime by ln p undoes it, and the staircase becomes the
  line y = x (§3). [NAMED; FORCED identity]
- **The waves are the zeros of ζ, and their taper, √x, is the Riemann hypothesis** (§4). [NAMED]
- **Over finite fields the line is exact.** For polynomials there are no waves at all. On curves the waves come back
  with the taper proved: each prime gets a direction, its Frobenius angle, and the directions spread by the Sato–Tate
  law (§5). [NAMED; FORCED checks]
- **On the qudit floor that spread is magic,** and its taper, −1/√p, is proved (§6;
  [`TORUS_MOMENTS.md`](seven_levels/TORUS_MOMENTS.md) §6). [FORCED]
- **Luther's dispersion has a formula from the primes.** On the Chinese-remainder grid the non-units are a cross, and
  they clump only at its two corners. WP34's interleave score is 1 − 2/(p + q − 2) over a period, and the staircase's
  wobble spreads with variance tending to (2^ω − 1)/12 for ω primes (§9). [FORCED]

## 1. The interleave staircase [FORCED]

Fix a number b. Grow the alphabet 1, 2, …, k and sort it, as WP34 did, into units C_k (coprime to b) and non-units
G_k (sharing a factor with b).

- **Two staircases, interleaved.** For b = pq the non-units are the multiples of p and the multiples of q: one
  staircase steps every p, the other every q. So |G_k| = ⌊k/p⌋ + ⌊k/q⌋ − ⌊k/pq⌋, and for any b,
  |G_k| = k − Σ_(d | b) μ(d)⌊k/d⌋ (inclusion–exclusion, Legendre's form).
- **The first step is at the smaller prime**, k = p: WP34's First-G law. It is also the first closing polygon of
  [THE_BALANCE_POINT.md](THE_BALANCE_POINT.md) (check B8). The script recomputes WP34's census: 153 semiprimes up to
  500, 36 662 pairs (b, k), and no exceptions.
- **The interleaving cancels to a straight line.** |G_k| = (1 − φ(b)/b)k + e(k). The wobble
  e(k) = Σ_(d | b) μ(d){k/d}, where {·} is the fractional part, repeats every b steps and stays between −2^(w − 1) and
  2^(w − 1) − 1, w being the number of primes in b. For two primes it stays inside (−2, 1): the staircase never strays
  two steps from the line of slope 1/p + 1/q − 1/pq. (Checked for every b up to 1000; for two primes the wobble runs
  from −1.838 to 0.906.)
- [READING] Two sides and an edge. The sides are the two staircases, of p and of q. Their sum averages to the line,
  and the edge is the wobble, where the two step patterns interleave.

## 2. Many primes: where the cancelling stops [NAMED; measured]

WP34 read the staircase as the sieve. Sieve 1, …, x by every prime up to √x, and what survives above √x is the
primes themselves: the staircase of the primes.

- With a fixed handful of primes the wobble stays bounded (§1). With all the primes up to √x there are 2^(π(√x))
  wobble terms, and they no longer cancel.
- The sieve's own line predicts the density Π_(p ≤ √x) (1 − 1/p). By Mertens' theorem that product is about
  2e^(−γ)/ln x, γ being Euler's constant [NAMED: Mertens 1874]. The primes' true density near x is 1/ln x [NAMED: the
  prime number theorem]. So the sieve's line over-predicts by 2e^(−γ) = 1.1229…, and the reason is that
  inclusion–exclusion fails to give an asymptotic formula in this range [NAMED: Lagarias 2013].
- [measured] Near 10⁵, 10⁶ and 10⁷ the over-prediction is 1.098, 1.121 and 1.121. [FORCED] Mertens' product itself,
  e^γ ln y Π_(p ≤ y) (1 − 1/p), lies within 1/(2 ln² y) of 1 at y = 10³ to 10⁷, as Rosser and Schoenfeld's bounds
  require; it is 0.99613, 0.99877, 0.99970, 0.99996 and 0.99999.
- [READING] A coin. One side is the sieve's line, which treats the primes as independent; the other is the primes'
  true line. The edge is the factor 2e^(−γ): the interleaving of many staircases, where it fails to cancel.

## 3. The compression function [NAMED; FORCED]

- **The function is 1/ln x.** Near x, about one number in ln x is prime [NAMED: Gauss's density, from his tables of
  1792–93; the prime number theorem, Hadamard and de la Vallée Poussin 1896]. It is 0.43 at 10, 0.22 at 100, 0.072 at
  a million and 0.036 at 10¹². The primes are packed tightest at the start and thin out ever more slowly, and the
  compression's own gradient is −1/(x ln² x).
- **Counting is the line seen through the compression.** By summation by parts, exactly,
  π(x) = θ(x)/ln x + ∫_2^x θ(t)/(t ln² t) dt, where θ(x) = Σ_(p ≤ x) ln p. [FORCED; checked at x = 10³ to 10⁷.]
  The count follows Li(x): π(x)/(Li(x) − Li(2)) is 0.951, 0.987, 0.996, 0.998 and 0.9995 there.
- **Weight each prime by ln p, and the staircase straightens.** ψ(x) = Σ_(p^k ≤ x) ln p tends to x. The step height
  ln p is exactly the reciprocal of the compression, so density times step is (1/ln x) · ln x = 1, the slope of the
  line y = x. [measured] ψ(x)/x = 1.0013, 1.0005, 0.9996 and 0.99985 at 10⁴ to 10⁷.
- [READING] Another coin. One side is the counting staircase π, with steps of height 1, which bends like Li(x). The
  other is the weighted staircase ψ, with steps of height ln p, which is straight. The edge is the compression itself,
  the change of weight between them.

## 4. The waves and the taper [NAMED; checked]

- **The explicit formula** [NAMED: Riemann 1859; von Mangoldt 1895]. For x > 1 not a prime power,

  ψ(x) = x − Σ_ρ x^ρ/ρ − ln 2π − ½ ln(1 − x^(−2)),

  the sum running over the zeros ρ of ζ in order of height. This is the lens line exactly: the staircase is the
  straight line minus a sum of waves, one for each zero. A zero ρ = β + iγ gives a wave of size x^β/|ρ| that turns
  γ radians per unit of ln x.
- [checked] With the first 10, 30 and 100 zeros (computed with mpmath), the formula misses ψ at x = 2.5, 3.5, …, 100.5
  by 0.94, 0.67 and 0.28 (root mean square): the waves rebuild the steps.
- **The taper.** If every β = ½, which is the Riemann hypothesis (open), every wave has size √x/|ρ|. Against the line
  the waves then taper as 1/√x, and each higher wave as 1/|ρ|. The archived lens's second line, *every line lives
  inside two parabolic arcs*, is this envelope: the Riemann hypothesis is equivalent to ψ(x) = x + O(√x ln² x)
  [NAMED: von Koch 1901].
- [checked, not proved] |ψ(x) − x| stays below √x ln² x/(8π), Schoenfeld's explicit form of the envelope [NAMED:
  Schoenfeld 1976], at every x from 74 to 10⁷. The largest ratio is 0.93.
- **The author's sentences of 20 November** about the primes are matched, in [`THE_LENS.md`](../THE_LENS.md) §8, to
  the classical results they restate, each with a check. Among them are the balance, the crossings, Lehmer's near
  miss, the spectrum of the zeros and the rate in log time.

## 5. The finite-field twin: how primes form direction [NAMED; FORCED checks; measured]

- **Polynomials: the line with no waves.** In F_q[T] the primes are the monic irreducible polynomials, and N_q(n) of
  them have degree n. The weighted staircase is exactly straight: Σ_(d | n) d·N_q(d) = q^n [FORCED]. There are no
  waves at all, because the zeta function of F_q[T], 1/(1 − qu), has no zeros. The compression is the same function:
  N_q(n) = (1/n) Σ_(d | n) μ(d) q^(n/d) ≈ q^n/n [NAMED: Gauss], a density of 1/n = 1/log_q(q^n). (The script counts
  the irreducible polynomials by brute force for q = 2, 3, 5 and 7.)
- **Curves: the waves come back, with the taper proved.** On an elliptic curve E over F_p, the points over F_(p^n)
  number p^n + 1 − α^n − ᾱ^n, where αᾱ = p, so |α| = √p [NAMED: Hasse 1933; Weil 1948]. There are two waves, each of
  size exactly p^(n/2): here the Riemann hypothesis is a theorem, and the taper is exactly the square root. [FORCED,
  by counting points on 10 curves over F_5, F_7, F_11 and F_13, for n = 1, 2 and 3.]
- **Direction.** Write α = √p e^(iθ). One curve over the integers gives every prime p its own angle θ_p, a direction
  on the circle, with a_p = 2√p cos θ_p. The directions are spread by the Sato–Tate law, (2/π) sin² θ dθ: crowded at
  right angles, rare near 0 and π [NAMED: Clozel, Harris, Shepherd-Barron and Taylor 2008; Barnet-Lamb, Geraghty,
  Harris and Taylor 2011, for curves without complex multiplication].
  - [measured] For y² = x³ + x + 1, at the 9 590 primes from 3 to 10⁵, a_p/√p has moments 0.998, 1.981 and 4.913
    against Sato–Tate's 1, 2 and 5. The angles lie at Kolmogorov distance 0.009 from the law, and 0.161 from a uniform
    angle.
- **Kloosterman sums give each prime a whole fan of directions**: K(a, p) = 2√p cos θ_(p,a) for a = 1, …, p − 1,
  with |K| ≤ 2√p [NAMED: Weil 1948]. At a fixed p the angles follow Sato–Tate as p grows [NAMED: Katz 1988].
  [FORCED] The script checks the bound at every a for every prime up to 199, and the exact moments
  Σ_a K² = p² − p − 1 and Σ_a K⁴ = 2p³ − 3p² − 3p − 1.

## 6. On the qudit floor, the spread is magic and the taper is proved [FORCED, elsewhere]

- On three qudits, the norm state's Wigner values are the Kloosterman sums K(m)/p⁵
  ([`NORM_STATE.md`](seven_levels/NORM_STATE.md)). So its magic is a statistic of the primes' directions: S/√q tends
  to E|2 cos θ| = 8/(3π), Sato–Tate's value.
- The oscillator states' Wigner values follow the same law, and their taper is proved
  ([`TORUS_MOMENTS.md`](seven_levels/TORUS_MOMENTS.md)). Averaged over the eigenbasis, the skew is exactly
  −(p + 2)/((p + 1)√(p − 1)), and the fourth-moment ratio is 2 − 2/(p + 1).
- [READING] The same square root three times. The integers' waves taper as 1/√x if the Riemann hypothesis holds. A
  curve's waves taper as 1/√p because Weil proved it. The qudit floor's shape tapers as 1/√p, proved on that floor.

## 7. The prime gradient on this floor [READING; measured]

The author's prime gradient, read off the qudit floor's results ([`seven_levels/README.md`](seven_levels/README.md)
§12 to §15): the small primes are where exact coincidences live, and the large ones are where the laws take over.

| prime | what happens there |
|---|---|
| 3 | the norm state is the most magic cubic on three qudits, at 0.900 of the ceiling |
| 5 | the triangle unfolds: smooth cubic curves with 8 points tie the norm state |
| 7 | the Smith chart turns the whole turning wheel, and the norm state wins again, at 0.902 |
| 11 on | smooth curves beat the norm state, and the best shares settle near Sato–Tate's 0.849, with 1/√p tapers |

- [READING] Compression at the small primes and taper at the large ones: the gradient runs from coincidence to law.
  Below 2000, only 3 and 7 bring the norm state to 0.9 of the ceiling.

## 8. Fenced

The author also asked why the coin's edge should be 137 (14 November 2026). That reading was tested with the other
physics readings, fenced, registered before it ran and judged against a look-elsewhere null:
[`../lab/alpha_137/`](../lab/alpha_137/README.md). Of 630 pre-named expressions built from this page's functions at
137, the nearest, 137 + ln 137/137, misses the inverse fine-structure constant by 8.7 × 10⁻⁵, 4 100 times the
measurement's uncertainty, and a grammar that size comes that close by chance 2.2% of the time. The reading died at
its registered bar, and its death is kept.

## 9. Prime-forced dispersion: Luther's question, made exact [FORCED; NAMED]

> *the prime p determines not only the onset of obstruction but the entire spread of G across the alphabet* —
> C. A. Luther, in WP34 §9, March 2026

WP34 called this prime-forced dispersion and left one step open: to write the dispersion as an explicit formula from
the primes. Here it is.

- **The picture** [NAMED: the Chinese remainder theorem]. The map n → (n mod p, n mod q) lays 1, 2, …, pq on a
  p × q grid, wrapped into a torus, along a line of slope 1. The non-units are exactly the grid's two axes, a cross.
  So the staircase of non-units is that line meeting the cross, one axis every p steps and the other every q steps.
- **Clumps happen only at the corners** [FORCED]. In each period exactly two non-units are followed by another, where
  the line steps from one axis to the other: at the two corners next to the origin. For b = 2q the two merge into one
  run of three, q − 1, q, q + 1, and a prime square has none. (Checked for every semiprime up to 1000.)
- **Luther's dispersion, as a formula from the primes** [FORCED]. WP34 measured dispersion by its interleave score: the
  number of changes between units and non-units in 1, …, k, over 2·min(|C_k|, |G_k|). At every k the number of
  changes is 2(|G_k| − A_k), less 1 when k itself is a non-unit. Here |G_k| = ⌊k/p⌋ + ⌊k/q⌋ − ⌊k/pq⌋, and A_k counts
  the corners passed, each with one floor. Over a whole period the score is 1 − 2/(p + q − 2) for odd primes,
  (q − 2)/(q − 1) for b = 2q, and 1 for a prime square. (Checked at every k for all 153 semiprimes up to 500; WP34's
  0.625 at b = 15 and 21 with k = 9 comes back.)
- **The wobble's spread counts the primes** [FORCED]. Over a period, the wobble e(k) of §1 has variance
  (1/12) Σ (−1)^(|S| + |S′|) (d_(S∩S′)² − 1)/(d_S d_S′), summed over pairs of nonempty sets S, S′ of b's primes, with
  d_S their product. It rests on one covariance: over a common period, {k/d} and {k/d′} have covariance
  (g² − 1)/(12 d d′), with g = gcd(d, d′), the discrete form of Franel's integral [NAMED: Franel 1924]. As the primes
  grow, the variance tends to (2^ω − 1)/12 for ω primes, one twelfth for each nonempty set of them: 1/12, 1/4, 7/12,
  5/4. That is WP34's ω hierarchy, found here in the spread itself. (Checked exactly for every b up to 400.)
- [READING] **The coin with the gate.** WP34 tied dispersion to a "gate rate", the success rate of a hill-climb over
  tables. The audit of 2026-09-24 found that the hill-climb sees a symbol only as a unit, a non-unit or HAR, so its rate
  depends on the count of non-units alone, and the stored runs show exactly that (`papers/Q_SERIES_AUDIT_2026-09-24.md`
  in the retired ck repository). So the conjecture that dispersion moves the gate rate died, and the death is kept. The
  dispersion itself stands, locked by the primes, and now exact. Two sides: the numbers, which see where the non-units
  sit, and the algorithm, which sees only how many. The edge is the algorithm's symmetry, the relabelings that keep each
  symbol's unit status.

## Standing

- **Known, and credited** [NAMED]: inclusion–exclusion and Legendre's sieve; Mertens' theorems (1874), with Rosser
  and Schoenfeld's bounds (1962); Gauss's density and the prime number theorem (1896); the explicit formula (Riemann
  1859; von Mangoldt 1895), with von Koch's envelope (1901) and Schoenfeld's (1976); Gauss's count of irreducible
  polynomials; Hasse (1933) and Weil (1948); the Sato–Tate theorem (2008, 2011); Weil's bound and Katz's
  equidistribution for Kloosterman sums (1948, 1988); the failure of inclusion–exclusion as the reason for Mertens'
  factor (Lagarias 2013).
- **The author's**, with WP34's co-authors: the interleave staircase and its reading as the sieve's partition geometry
  (March 2026); the lens line (June 2026); and the prime gradient, with its compression and its taper (14 November
  2026).
- **C. A. Luther's**, in WP34: prime-forced dispersion, the observation that the primes lock the whole spread of the
  non-units (March 2026). Its link to the gate rate died in the audit of 2026-09-24.
- **This page's own:** the gathering, the readings marked [READING], and the elementary formulas of §9 for WP34's
  interleave score and the wobble's variance. Nothing here is new mathematics except the qudit floor's taper, which is
  proved in [`TORUS_MOMENTS.md`](seven_levels/TORUS_MOMENTS.md) §6.
- **Checked** by [`verify_staircase.py`](verify_staircase.py): 15 checks, all passing
  ([`verify_staircase.log`](verify_staircase.log)).

## Run it

```
python verify_staircase.py     # 15 checks, about a minute (numpy, mpmath)
```

## Sources

- B. R. Sanders, C. A. Luther and M. Gish, WP34, "The First-G Law and Prime-Forced Dispersion" (March 2026), in the
  retired ck repository:
  [papers/WP34_FIRST_G_LAW.md](https://github.com/TiredofSleep/ck/blob/tig-synthesis/papers/WP34_FIRST_G_LAW.md).
- The lens note, "The staircase-and-envelope lens" (June 2026), archived at
  [archive-2026-09-24](https://github.com/TiredofSleep/trinity-infinity-geometry/blob/archive-2026-09-24/10_extensions/tig-validation/notes/staircase_envelope_lens.md).
- F. Mertens, "Ein Beitrag zur analytischen Zahlentheorie", *J. reine angew. Math.* **78** (1874).
- J. B. Rosser and L. Schoenfeld, "Approximate formulas for some functions of prime numbers", *Illinois J. Math.*
  **6** (1962).
- J. C. Lagarias, "Euler's constant: Euler's work and modern developments", *Bull. Amer. Math. Soc.* **50** (2013),
  [arXiv:1303.1856](https://arxiv.org/abs/1303.1856).
- B. Riemann, "Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse" (1859); H. von Mangoldt, "Zu Riemanns
  Abhandlung …", *J. reine angew. Math.* **114** (1895).
- J. Hadamard; C. J. de la Vallée Poussin: the prime number theorem (1896).
- H. von Koch, "Sur la distribution des nombres premiers", *Acta Math.* **24** (1901); L. Schoenfeld, "Sharper bounds
  for the Chebyshev functions θ(x) and ψ(x). II", *Math. Comp.* **30** (1976).
- H. Hasse (1933, 1936); A. Weil, "On some exponential sums", *Proc. Natl. Acad. Sci.* **34** (1948), and *Sur les
  courbes algébriques et les variétés qui s'en déduisent* (1948).
- L. Clozel, M. Harris, N. Shepherd-Barron and R. Taylor (2008); T. Barnet-Lamb, D. Geraghty, M. Harris and R. Taylor,
  *Publ. RIMS* **47** (2011): the Sato–Tate theorem.
- N. M. Katz, *Gauss Sums, Kloosterman Sums, and Monodromy Groups* (1988).
- R. Lidl and H. Niederreiter, *Finite Fields* (1983): Gauss's count of irreducible polynomials.
- J. Franel, "Les suites de Farey et le problème des nombres premiers", *Göttinger Nachrichten* (1924): the integral of
  a product of two sawtooth functions.
- The Q-series audit (2026-09-24), in the retired ck repository:
  [papers/Q_SERIES_AUDIT_2026-09-24.md](https://github.com/TiredofSleep/ck/blob/tig-synthesis/papers/Q_SERIES_AUDIT_2026-09-24.md).
