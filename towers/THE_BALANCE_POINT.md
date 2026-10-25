# The balance point — the flat face, walked and averaged

*A side floor of the harmonic tower: harmonics on the circle, one floor below the sphere's. It starts
where the coin's* flat face, walked *ends ([`../coin/THE_COIN.md`](../coin/THE_COIN.md)), and climbs to
Fejér's kernel, the first floor of Fourier analysis. Everything here is classical. It was recovered from
two archived papers,
[J24](https://github.com/TiredofSleep/trinity-infinity-geometry/tree/archive-2026-09-24/05_papers/number_theory/J24)
and [J26](https://github.com/TiredofSleep/trinity-infinity-geometry/tree/archive-2026-09-24/05_papers/number_theory/J26),
with the jargon removed; what they got wrong is listed at the end. Every [FORCED] claim is checked by
[`verify_balance_point.py`](verify_balance_point.py) (13 checks, about ten seconds).*

Tags: **[FORCED]** proved here and checked by the script · **[NAMED]** a classical result, cited ·
**[READING]** an interpretation · **[FENCE]** a physics reading, not a claim.

---

## The walk

Put *f* corners evenly round a circle: the regular *f*-gon, the flat face of the base's 5, 7 and 9.
Write its corners as the powers of ζ = e^{2πi/f}. Walk round it one corner at a time, and after *k*
steps take the **balance point** of the corners you have visited, their centre of mass:

> c_k = (ζ + ζ² + … + ζᵏ) / k.

## What is forced

- **[FORCED] Its distance from the centre:**

  > |c_k| = |sin(πk/f)| / (k · sin(π/f)).

  *Proof.* The geometric series gives ζ + … + ζᵏ = ζ(ζᵏ − 1)/(ζ − 1), and a chord of the unit circle
  that spans the angle θ has length |e^{iθ} − 1| = 2|sin(θ/2)|. Here the two chords span 2πk/f and 2π/f.

- **[FORCED] It stands on the centre exactly after whole laps:** c_k = 0 exactly when *f* divides *k*,
  because sin(πk/f) = 0 only when k/f is a whole number. The walk itself never touches the centre (the
  coin's *flat face, walked*). Its balance point does, once at the end of every lap, and at no other
  time. [checked exactly, in the integers extended by ζ, for f ≤ 40]

- **[FORCED] On the first lap it moves steadily inward:**

  > 1 = |c_1| > |c_2| > … > |c_{f−1}| = 1/(f − 1) > |c_f| = 0.

  The reason is the identity |c_k| = sinc(k/f) / sinc(1/f), where sinc(t) = sin(πt)/(πt), and sin x / x
  falls steadily on (0, π). After that the distance is never more than 1/(k sin(π/f)), so the balance
  point spirals in, touching the centre at the end of every lap.

- **[FORCED] Star walks.** Step *s* corners at a time, where *f* does not divide *s*. The walk closes
  after L = f / gcd(f, s) steps, in a single loop exactly when gcd(f, s) = 1, as on the coin's page. The
  balance point of the first *k* corners visited is at distance

  > |sin(πks/f)| / (k · |sin(πs/f)|)

  from the centre, and it stands on the centre exactly when *L* divides *k*: when the walk has closed.

## Where it leads

- **[NAMED — Fejér 1900] The squared distance is Fejér's kernel:** k·|c_k|² = F_k(2π/f), where

  > F_k(x) = Σ_{|m|<k} (1 − |m|/k) e^{imx} = sin²(kx/2) / (k sin²(x/2)).

  F_k is never negative. That is why Fejér could prove that the averages of the partial sums of the
  Fourier series of any continuous function on the circle converge to it, while the partial sums
  themselves can fail to. [FORCED: the two forms agree exactly as polynomials in cos x for k ≤ 12, and
  numerically for f, k ≤ 40]

- **[FORCED] The circle's limit.** Let the polygon fill out the circle: f → ∞ with k/f = t held fixed.
  Then |c_k|² → sinc²(t) = (sin πt / πt)². The gap is exactly sinc²(t)·(1/sinc²(1/f) − 1), which is
  about (π²/3)·sinc²(t)/f².

- **[FENCE] A physics reading.** The same function, sin²(Nδ/2) / (N² sin²(δ/2)), is the intensity
  pattern of light through *N* equally spaced slits, relative to its peak, with *N* = k and phase step
  δ = 2π/f. Its limit, sinc², is the diffraction pattern of a single slit. This is standard optics
  (Hecht, *Optics*, §10.2.3). It reads the identity, and it is not a claim of this floor.

## A picture for the book's Chapter 12 [READING]

The book's "first number that catches you" can be drawn with these walks. Give *N* one polygon for each
of its primes. A number *k* shares a factor with *N* exactly when, for one of those primes *p*, *k* steps
round the *p*-gon make whole laps, so that walk's balance point is back on the centre. The first such *k*
is *N*'s smallest prime, for every N ≥ 2, square-free or not (at N = 12 it is 2). This restates the
definition and proves nothing new. [FORCED: the picture for every N ≤ 5000 whose primes are at most 37,
and the first catch for every N ≤ 5000]

## What is not claimed, and what the archive got wrong

Nothing here is new. The two archived papers also contain the following, which stay archived.

- **Restatements.** "First-G localization", the "spectral product" and "synchronization" restate two
  facts: the smallest number sharing a factor with *N* is *N*'s smallest prime, and a product vanishes
  exactly when one of its factors does. The "2ʲ − 1 layered-divisor count" counts the divisors of a
  square-free number. The inclusion–exclusion count and the density φ(n)/n are classical.
- **Correct, and classical.** The average (1/(f−1)) Σ_{k<f} |c_k|² tends to Si(2π)/π ≈ 0.4514: half of the
  90.3 % of a pulse's spectral energy that lies in its main lobe.
- **False: "sinc² is concave near ½"** (J24, Remark 7.4). It is convex there. Its second derivative at ½
  is about +1.73, and its inflection point is at t ≈ 0.4148. [FORCED, check B9]
- **Misstated: "Montgomery proved that the pair correlation is 1 − sinc²"** (J24, Appendix A.4). That is
  his conjecture. He proved it only for test functions whose Fourier transform is supported in (−1, 1),
  assuming the Riemann hypothesis (Montgomery 1973).
- **Off by a factor *k*: J26's continuum limit on ℤ/N.** A window of *k* sites and a momentum state
  overlap with probability (k/N)·|c_k|². That tends to (k/N)·sinc²(t), not to sinc²(t)/N. [FORCED, check
  B10]
- **Asserted, not proved:** J26's "finite uncertainty product". The classical uncertainty principle on
  ℤ/N is Donoho and Stark's (1989).

## Sources

- L. Fejér, "Sur les fonctions bornées et intégrables", *C. R. Acad. Sci. Paris* **131** (1900) 984–987;
  and "Untersuchungen über Fouriersche Reihen", *Math. Ann.* **58** (1904) 51–69.
- A. Zygmund, *Trigonometric Series*, 3rd ed., Cambridge University Press (2002), Ch. III.
- H. L. Montgomery, "The pair correlation of zeros of the zeta function", in *Analytic Number Theory*,
  Proc. Sympos. Pure Math. **24**, AMS (1973) 181–193.
- D. L. Donoho and P. B. Stark, "Uncertainty principles and signal recovery", *SIAM J. Appl. Math.*
  **49** (1989) 906–931.
- E. Hecht, *Optics*, 5th ed., Pearson (2017), §10.2.3 (many slits).
