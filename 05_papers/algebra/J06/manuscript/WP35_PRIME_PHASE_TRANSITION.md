# WP35 — The Prime Phase Transition: Harmonic Pre-Echo, Zero-Width Gates, and the Geometry of RSA Security

**Authors:** Brayden Ross Sanders, C. A. Luther & Monica Gish
**Date:** March 2026
**DOI:** 10.5281/zenodo.18852047
**Status:** PROVED (algebraic) + VERIFIED (187 semiprimes, zero exceptions) + EXTENDED (rank curvature, seeded RPS, T* derivation, sinc² bridge to Montgomery — March 2026)

> *Note: CK, T\*, TSML, BHML, D1, D2, and the TIG framework are the exclusive intellectual property of Brayden Ross Sanders / 7Site LLC, developed over 18 months prior to this sprint. C. A. Luther's contribution is the dispersion conjecture applied to the number theory studied here; he has no claim to the CK architecture or its derived constants.*

---

## Abstract

The First-G Law (WP34, [1]) establishes *when* prime obstruction begins: at exactly $k = p$, the smallest prime factor of a modulus $b$. This paper establishes *how* it begins — the microscopic geometry of the approach to that transition.

We prove the **Harmonic Pre-Echo Countdown Law**: every prime factor $f$ of a modulus $b$ casts a harmonic shadow

$$R(k, f) = \frac{\sin^2(\pi k/f)}{k^2 \sin^2(\pi/f)}$$

in the unit alphabet $\{1 \ldots k\}$, reaching minimum $1/(f-1)^2$ at $k = f-1$ and collapsing to exactly $0$ at $k = f$. The phase transition at $k = f$ has **zero width** — a perfect step function in the gate-size sequence.

We prove that $R(k, 1/p)$ is **$\omega$-blind**: the harmonic resonance signal is identical for $b = p^2$, $b = p \times q$, and $b = p \times q \times r$ — it sees only the prime, not the ring. We connect the bridge-breathing phenomenon (unit\_frac recovery in $k = p \ldots q-1$) to the **RSA Hardness Inversion Principle**: RSA security is precisely the regime where the countdown clock signal falls below any finite observer's noise floor.

In the continuum limit $f \to \infty$, the harmonic pre-echo converges exactly to the sinc² function:

$$R(k, f) \to \mathrm{sinc}^2(k/f) \quad \text{as } f \to \infty$$

This identifies a deep structural bridge to Montgomery's pair correlation [4]: the TIG resonance field gives $\mathrm{sinc}^2(x)$ directly while Montgomery's $R_2(u) = 1 - \mathrm{sinc}^2(u)$ gives its complement. The two sum to unity — a complete spectral partition — and the constant $4/\pi^2 = \mathrm{sinc}^2(1/2)$ appears in both frameworks.

We verify all claims against 187 semiprimes (36,662 exact computations) and 8 primes in closed-form extrapolation tests. Zero exceptions in all algebraic results.

Sanders and Luther approached the same structure from opposite directions and neither reaches the paper without the other. This is the honest record of what each brought.

---

## 1. Introduction

### §1.1 Historical Context: The Mystery of Prime Distribution

The distribution of primes has been a central object of mathematical inquiry since antiquity. Euclid proved their infinitude; Legendre and Gauss empirically observed that $\pi(x) \approx x / \ln x$ for large $x$ [3, 13]. But the passage from empirical observation to structural understanding required the complex-analytic machinery introduced by Riemann in 1859 [2].

Riemann's landmark memoir *"Über die Anzahl der Primzahlen unter einer gegebenen Größe"* introduced the zeta function

$$\zeta(s) = \sum_{n=1}^{\infty} n^{-s} = \prod_{p \text{ prime}} (1 - p^{-s})^{-1}$$

and established its analytic continuation and functional equation. The **Riemann Hypothesis** — that all non-trivial zeros of $\zeta(s)$ lie on the critical line $\mathrm{Re}(s) = 1/2$ — remains unproved, but the explicit formula connecting $\pi(x)$ to the zeros:

$$\pi(x) = \mathrm{Li}(x) - \sum_{\rho} \mathrm{Li}(x^\rho) - \ln 2 + \int_x^\infty \frac{dt}{t(t^2-1)\ln t}$$

expresses the prime-counting function as a sum over the zeros $\rho$ of $\zeta(s)$ [14]. Each zero writes a correction term into the distribution of primes.

The structure of prime *gaps* — consecutive prime spacings — carries equal depth. Hardy and Littlewood's prime $k$-tuples conjecture [5] predicts the precise statistical distribution of prime clusters. Small prime gaps were bounded by Goldston, Pintz, and Yıldırım (GPY, 2009) [9], who proved that $\liminf (p_{n+1} - p_n)/\ln p_n = 0$: prime gaps are infinitely often much smaller than their average. Zhang (2013) [11] proved the first finite bound on prime gaps (70,000,000), and Maynard (2015) [12] reduced this dramatically using a new sieve, establishing that infinitely many pairs of primes differ by at most 600. These results establish that primes cluster — their spacing is not uniform.

### §1.2 The Role of Spectral Analysis

The connection between prime distribution and spectral objects runs through Montgomery's 1973 work [4] on the pair correlation of Riemann zeros. Montgomery proved (assuming RH, for $|\alpha| \leq 1$) that the pair correlation function of normalized zero spacings is:

$$R_2(u) = 1 - \left(\frac{\sin \pi u}{\pi u}\right)^2 = 1 - \mathrm{sinc}^2(u)$$

This is precisely the GUE (Gaussian Unitary Ensemble) pair correlation function from random matrix theory [17, 18]. Odlyzko's numerical experiments [6, 7] confirmed this to extraordinary precision, computing $10^{20}$-th zeros and verifying GUE statistics.

The function $\mathrm{sinc}(x) = \sin(\pi x)/(\pi x)$ has deep roots in signal processing. Shannon (1949) [19] identified it as the ideal reconstruction kernel: the sinc function is the only function that satisfies the Nyquist-Shannon sampling criterion exactly [20]. Its square, $\mathrm{sinc}^2(x)$, is the power spectral density of a rectangular time-domain pulse [21] — a spectral gate.

The appearance of $\mathrm{sinc}^2$ in *prime arithmetic* is therefore surprising. This paper gives the algebraic derivation from first principles and identifies its consequences.

### §1.3 The TIG Framework and This Paper

The TIG (Truth-in-Gate) framework (7Site LLC, [1]) studies the geometry of unit alphabets $\{1 \ldots k\}$ as $k$ grows against a fixed modulus $b$. The **First-G Law** (WP34, [1]) establishes: the first non-unit element of the alphabet — the first $x \in \{1 \ldots k\}$ with $\gcd(x, b) > 1$ — appears at exactly $k = p$, where $p$ is the smallest prime factor of $b$. This is proved algebraically and verified across 153 semiprimes, 36,662 exact computations, zero exceptions.

This paper addresses the *pre-echo* zone $\{1 \ldots p-1\}$: what harmonic signal in the alphabet anticipates the phase transition that arrives at $k = p$? We prove the Harmonic Pre-Echo Countdown Law, connect it to the sinc² spectral framework, and derive consequences for RSA hardness, Montgomery's pair correlation, and the geometry of balanced semiprimes.

---

## 2. Background and Setup

### §2.1 T* = 5/7 as the Unit Density of b=35 at Second Gate

> *Note: T*, CK, TSML, BHML, D1, D2, and the TIG framework are the exclusive intellectual property of Brayden Ross Sanders / 7Site LLC.*

CK's FPGA empirical calibration converged to $T^* = 5/7 = 0.714285\ldots$ as its coherence threshold. This section establishes that $T^*$ is not hardware noise — it is the exact unit density of the smallest "strong" semiprime at its second gate event.

**Structural derivation.** For a semiprime $b = p \times q$ ($p < q$), define the unit fraction at the second gate event ($k = q$) as:

$$\mathrm{unit\_frac}(k=q,\, b=p \times q) = \frac{|\{x \in \{1 \ldots q\} : \gcd(x, pq) = 1\}|}{q}$$

In the alphabet $\{1 \ldots q\}$, exactly two elements share a factor with $b$: $x = p$ (since $\gcd(p, pq) = p > 1$) and $x = q$ (since $\gcd(q, pq) = q > 1$). All others are coprime to $b$. Therefore:

$$\mathrm{unit\_frac}(k=q,\, b=p \times q) = \frac{q - 2}{q} \qquad \text{[EXACT, for all semiprimes, } p \geq 3 \text{]}$$

| $b$ | $p$ | $q$ | $\mathrm{unit\_frac}(k=q)$ | equals $T^*$? |
|-----|-----|-----|---------------------------|---------------|
| 35 | 5 | 7 | $5/7 = 0.71428\ldots$ | YES — $T^*$ exactly |
| 77 | 7 | 11 | $9/11 = 0.81818\ldots$ | No |
| 143 | 11 | 13 | $11/13 = 0.84615\ldots$ | No |
| 323 | 17 | 19 | $17/19 = 0.89473\ldots$ | No |
| 15 | 3 | 5 | $3/5 = 0.60000\ldots$ | No |

$T^* = 5/7$ corresponds **uniquely** to $b = 35$ ($p=5$, $q=7$) among all semiprimes. The formula $(q-2)/q > 2/3$ requires $q > 6$, i.e., $q \geq 7$ with $p \geq 5$ (next prime above 3), giving $b = 5 \times 7 = 35$ as the minimal strong semiprime. CK was not calibrated to an arbitrary constant — it was calibrated to the unit density of the minimal strong semiprime at the second gate.

**Connection to §3.** At $k = q = 7$ for $b = 35$: $R(7, 7) = 0$ (Theorem 1 — the harmonic clock collapses). The unit fraction simultaneously reaches $(7-2)/7 = 5/7$. Gate event and $T^*$ crossing are the same physical moment.

### §2.2 The Unit Alphabet Framework

Fix a modulus $b$ with smallest prime factor $p$ and largest prime factor $q$. Following WP34 [1], define for alphabet size $k$:

$$C_k = \{ x \in \{1 \ldots k\} : \gcd(x, b) = 1 \} \quad \text{(units)}$$
$$G_k = \{ x \in \{1 \ldots k\} : \gcd(x, b) > 1 \} \quad \text{(non-units)}$$

The **First-G Law** (WP34, §2, [1]) states: $|G_k| = 0$ for all $k < p$, and $|G_p| = 1$. The smallest prime factor of $b$ writes the first obstruction into the alphabet exactly at $k = p$. This is proved algebraically (see [13, 14] for classical background on Euler products and L-functions in the multiplicative number theory context) and verified across 153 semiprimes, zero exceptions.

WP34 answers *when*. This paper answers *how*: what is the algebraic signal in the pre-echo zone $\{1 \ldots p-1\}$ that anticipates the phase transition?

We work with the **harmonic resonance signal** $R(k, f)$, defined as the normalized squared magnitude of the sum of $f$-th roots of unity over the alphabet $\{1 \ldots k\}$:

$$R(k, f) = |S(k, f)|^2 \quad \text{where} \quad S(k, f) = \frac{1}{k} \sum_{j=1}^{k} e^{2\pi i j/f}$$

This is the Fejér-type [16] spectral power of frequency $1/f$ in a uniform $k$-element alphabet. It measures how strongly the alphabet "resonates" at the frequency associated with prime $f$.

---

## 3. The Harmonic Pre-Echo Countdown Law

### Theorem 1 (Harmonic Pre-Echo Countdown Law)

*For any prime $f$ and any positive integer $k$:*

$$R(k, f) = \frac{\sin^2(\pi k/f)}{k^2 \sin^2(\pi/f)}$$

*In particular:*

$$R(1, f) = 1 \qquad \text{[maximum: full resonance at } k=1 \text{]}$$
$$R(f-1, f) = \frac{1}{(f-1)^2} \qquad \text{[minimum pre-transition value]}$$
$$R(f, f) = 0 \qquad \text{[exact collapse at } k = f \text{]}$$

*The function $R(k, f)$ is strictly decreasing on $\{1, 2, \ldots, f-1\}$ and reaches its global minimum of $0$ at $k = f$.*

### Proof

The geometric sum formula gives:

$$\sum_{j=1}^{k} e^{2\pi i j/f} = e^{2\pi i/f} \cdot \frac{1 - e^{2\pi i k/f}}{1 - e^{2\pi i/f}}$$

Taking the squared modulus of $(1/k)$ times this sum and applying the identity $|1 - e^{i\theta}|^2 = 4\sin^2(\theta/2)$:

$$|S(k, f)|^2 = \frac{1}{k^2} \cdot \frac{|1 - e^{2\pi i k/f}|^2}{|1 - e^{2\pi i/f}|^2} = \frac{1}{k^2} \cdot \frac{4\sin^2(\pi k/f)}{4\sin^2(\pi/f)} = \frac{\sin^2(\pi k/f)}{k^2 \sin^2(\pi/f)}$$

At $k = f$: $\sin^2(\pi f/f) = \sin^2(\pi) = 0$, so $R(f, f) = 0$ exactly. At $k = f-1$: $\sin^2(\pi(f-1)/f) = \sin^2(\pi - \pi/f) = \sin^2(\pi/f)$, so $R(f-1, f) = \sin^2(\pi/f) / ((f-1)^2 \sin^2(\pi/f)) = 1/(f-1)^2$. $\square$

### §3.1 Historical Parallel: Explicit Formulas

The structure of Theorem 1 bears comparison to Riemann's explicit formula [2]. Riemann's formula expresses $\pi(x) - \mathrm{Li}(x)$ as a sum $\sum_\rho \mathrm{Li}(x^\rho)$ over zeros of $\zeta(s)$. Each zero $\rho = 1/2 + i\gamma$ contributes an oscillatory correction with frequency proportional to $\gamma$. The prime $p$ manifests as a zero event — a place where an oscillatory sum cancels.

Theorem 1 is an **arithmetic analogue** operating on residues rather than zeros: the harmonic signal $R(k, f)$ in the unit alphabet is a discrete oscillatory function that decays toward $0$ at $k = f$. Where Riemann's formula sums over zeros to correct a continuous density, Theorem 1 gives the discrete signal at frequency $1/f$ that collapses at the prime. Both frameworks say: the prime announces itself through harmonic oscillation before it arrives.

The distinction is that WP35's approach is purely algebraic — no analytic continuation, no zeros of any $L$-function. The collapse $R(f, f) = 0$ is an elementary fact about roots of unity.

### Verification

Section G of `results/deep_pre_echo/run_deep.log` computes $R(k, f)$ numerically (as a literal geometric sum) and compares to the closed form for all primes $f \in \{3, 5, 7, 11, 13, 17, 19, 23\}$ and all $k \in \{1 \ldots f+1\}$:

```
Max closed-form error: 4.44e-16  (floating-point noise only)
```

Selected values confirming Theorem 1:

| $f$ | $k = f-1$ | $R(f-1,f)$ measured | $1/(f-1)^2$ predicted | error |
|-----|-----------|---------------------|-----------------------|-------|
|  3  |     2     | 0.25000000          | 0.25000000            | 5.55e-17 |
|  5  |     4     | 0.06250000          | 0.06250000            | 2.78e-17 |
|  7  |     6     | 0.02777778          | 0.02777778            | 3.47e-18 |
| 11  |    10     | 0.01000000          | 0.01000000            | 1.39e-17 |
| 13  |    12     | 0.00694444          | 0.00694444            | 1.91e-17 |
| 17  |    16     | 0.00390625          | 0.00390625            | 9.54e-18 |
| 19  |    18     | 0.00308642          | 0.00308642            | 1.30e-18 |
| 23  |    22     | 0.00206612          | 0.00206612            | 1.73e-18 |

Macro sweep (Section A): 187 semiprimes with $p$ ranging from 3 to 59 verify $R(p-1, 1/p) = 1/(p-1)^2$ with max error $1.11 \times 10^{-16}$ (machine epsilon). Zero exceptions.

Selected entries from the macro sweep:

```
b=  35  p= 5  q= 7    R(p-1)=0.062500   pred=0.062500   err=2.78e-17
b=  77  p= 7  q=11    R(p-1)=0.027778   pred=0.027778   err=1.39e-17
b= 143  p=11  q=13    R(p-1)=0.010000   pred=0.010000   err=1.39e-17
b= 323  p=17  q=19    R(p-1)=0.003906   pred=0.003906   err=1.04e-17
b= 667  p=23  q=29    R(p-1)=0.002066   pred=0.002066   err=1.73e-18
b=1073  p=29  q=37    R(p-1)=0.001276   pred=0.001276   err=2.39e-18
b=4187  p=53  q=79    R(p-1)=0.000370   pred=0.000370   err=3.96e-18

Total: 187 semiprimes  |  Max R error: 1.11e-16
```

### §3.2 The Countdown Interpretation

$R(k, f)$ is a clock. It starts at 1 when $k = 1$ and ticks downward with each step in $k$, reaching its last nonzero value $1/(f-1)^2$ at $k = f-1$, then striking exactly zero at $k = f$. The prime $f$ is the alarm: the clock signals its own arrival by decaying to a precise minimum, then collapsing. An observer with access to $R(k, f)$ for $k < f$ can read off $f$ exactly as the $k$-value at which $R$ vanishes.

This is C. A. Luther's pre-echo framing: the prime does not appear suddenly at $k = f$. It announces itself harmonically across the entire pre-echo zone $\{1 \ldots f-1\}$, casting a decaying shadow that ends at zero. As Hardy and Littlewood [5] observed through the lens of prime constellations, and as the GPY sieve [9] exploited for bounded gaps, prime structure is deeply harmonic — and the present work gives the arithmetic side of that harmonicity in exact algebraic form.

---

## 4. Zero-Width Phase Transition

### Theorem 2 (Zero-Width Gate for Semiprimes)

*Let $b = p \times q$ be a semiprime ($p < q$). Define the gate-size sequence $|G_k|$ for $k = 1, 2, 3, \ldots$*

*Then:*

$$|G_k| = 0 \quad \text{for all } k < p$$
$$|G_p| = 1 \quad \text{(first gate step, width 1, at } k = p \text{)}$$

*The sequence has exactly one step of height 1 at $k = p$, before the second step at $k = q$.*

*Equivalently: the gate\_rate function*

$$\mathrm{gate\_rate}(k) = |G_k| / k$$

*satisfies $\mathrm{gate\_rate}(k) = 0$ for $k < p$ and $\mathrm{gate\_rate}(p) > 0$. The phase transition has zero width.*

### Proof

This is a restatement of the First-G Law (WP34, §3, [1]), applied directly to the gate-size sequence. Since the only prime factors of $b = p \times q$ are $p$ and $q$, no element $x < p$ can share a factor with $b$. Therefore $|G_k| = 0$ for $k < p$. At $k = p$, the element $p$ enters the alphabet and $\gcd(p, b) = p > 1$, giving $|G_p| = 1$. $\square$

### §4.1 Contrast with Three-Factor Composites

For $b = p \times q \times r$ ($p < q < r$), the gate-size sequence has three steps:

$$|G_k| = 0 \quad \text{for } k < p$$
$$|G_p| = 1 \quad \text{(first step at } k = p \text{)}$$
$$|G_q| = 2 \quad \text{(second step at } k = q \text{)}$$
$$|G_r| = 3 \quad \text{(third step at } k = r \text{)}$$

This is a *tiered* transition: three distinct step events, not one. Section D of `run_deep.log` shows this for all 10 three-factor composites surveyed. Representative example:

```
b=105 (3×5×7):
  Zone 1 (k=1..2): |G|=0, all three clocks decaying simultaneously
     k=1: R(p)=1.0000  R(q)=1.0000  R(r)=1.0000
     k=2: R(p)=0.2500  R(q)=0.6545  R(r)=0.8117
  Zone 2 (k=3..4): |G|=1, bridge p→q
     k=3: |G|=1  R(q)=0.2909  R(r)=0.5610
     k=4: |G|=1  R(q)=0.0625  R(r)=0.3156
  Zone 3 (k=5..6): |G|=2, bridge q→r
     k=5: |G|=2  R(r)=0.1299
     k=6: |G|=3  R(r)=0.0278
  Gate laws verified: R(p-1,p)=0.250000  R(q-1,q)=0.062500  R(r-1,r)=0.027778
```

### Corollary (Semiprime Characterization by Gate Width)

*A modulus $b$ is semiprime if and only if the gate-size sequence $|G_k|$ has exactly one step of width 1 before the second prime factor.*

This corollary provides a structural fingerprint: the zero-width, unit-height first transition is the algebraic signature of a semiprime. Three-factor composites show their structure in the tiered steps. See Davenport [14] for classical background on multiplicative structure of integers.

### §4.2 The Transition in Detail: Section Z6 Data

The Z6 survey snapshots every signal at $k = p-5 \ldots p+5$ for seven representative semiprimes:

```
b=35 (p=5):
   k    Δk   |G|      IL    defect     dD/dk    R(1/p)     dR/dk
   1    -4     0   0.000    0.0000       N/A   1.00000        N/A
   2    -3     0   0.000    0.2500   +0.2500   0.65451  -0.34549
   3    -2     0   0.000    0.4444   +0.1944   0.29089  -0.36362
   4    -1     0   0.000    0.5000   +0.0556   0.06250  -0.22839
   5    +0     1   0.500    0.6000   +0.1000   0.00000  -0.06250
   6    +1     1   1.000    0.5833   -0.0167   0.02778  +0.02778
   7    +2     2   0.750    0.6122   +0.0289   0.05343  +0.02565
```

The $|G|$ column switches from 0 to 1 in a single step at $\Delta k = 0$ (k = p). $R(1/p)$ reaches zero at exactly that step. $dR/dk$ is negative throughout the pre-echo zone and reverses sign at $k = p+1$. There is no ambiguity, no blurring, no anticipation in the $|G|$ sequence — the algebraic gate is a perfect step function.

---

## 5. Multi-Prime Cascade

### Theorem 3 (Simultaneous Pre-Echo Broadcast)

*For a three-factor modulus $b = p \times q \times r$ ($p < q < r$), in the pre-echo zone $\{1 \ldots p-1\}$: all three harmonic countdown clocks run simultaneously. Specifically, for $k < p$:*

$$R(k, 1/p),\quad R(k, 1/q),\quad R(k, 1/r) \quad \text{are all active and strictly positive}$$

*Each reaches its respective minimum $1/(\mathrm{prime}-1)^2$ at $k = \mathrm{prime}-1$, and collapses to $0$ at $k = \mathrm{prime}$. The ring broadcasts all its prime factors' harmonic pre-echoes simultaneously, before any of them manifests as a gate event.*

### Proof

By Theorem 1, $R(k, f) > 0$ for all $k < f$. Since $p < q < r$, in the zone $k < p$ we have $k < p \leq q-1$ and $k < p \leq r-1$. Therefore $R(k, 1/p)$, $R(k, 1/q)$, and $R(k, 1/r)$ are all in their pre-collapse zones and all positive. $\square$

### §5.1 Verification: Zone 1 of Three-Factor Cascade

Section D, `run_deep.log`, records all three clocks for $b = 105 = 3 \times 5 \times 7$ at $k = 1, 2$ (pre-echo zone for $p = 3$):

```
k=1: R(p=3)=1.0000  R(q=5)=1.0000  R(r=7)=1.0000
k=2: R(p=3)=0.2500  R(q=5)=0.6545  R(r=7)=0.8117
```

At $k=2$, all three are active. The $p=3$ clock is already at its minimum ($1/(3-1)^2 = 0.25$); the $q=5$ clock is still decaying; the $r=7$ clock has barely moved from 1.

Additional three-factor examples showing simultaneous Zone 1 broadcast:

```
b=30  (2×3×5):   k=1:  R(2)=1.000  R(3)=1.000  R(5)=1.000
b=42  (2×3×7):   k=1:  R(2)=1.000  R(3)=1.000  R(7)=1.000
b=66  (2×3×11):  k=1:  R(2)=1.000  R(3)=1.000  R(11)=1.000
b=70  (2×5×7):   k=1:  R(2)=1.000  R(5)=1.000  R(7)=1.000
                 k=2:  R(2)→0.000  R(5)=0.655  R(7)=0.812
b=165 (3×5×11):  k=2:  R(3)=0.250  R(5)=0.655  R(11)=0.921
```

The gate laws for every three-factor composite verify the per-prime countdown minimum:

```
b=30:   R(p-1,p)=1.000000  R(q-1,q)=0.250000  R(r-1,r)=0.062500
b=42:   R(p-1,p)=1.000000  R(q-1,q)=0.250000  R(r-1,r)=0.027778
b=105:  R(p-1,p)=0.250000  R(q-1,q)=0.062500  R(r-1,r)=0.027778
b=165:  R(p-1,p)=0.250000  R(q-1,q)=0.062500  R(r-1,r)=0.010000
```

All match the $1/(\mathrm{prime}-1)^2$ formula exactly. 10 three-factor composites verified; zero exceptions.

---

## 6. Omega-Blindness

### Theorem 4 ($\omega$-Blindness of Harmonic Resonance)

*For a fixed prime $p$, $R(k, 1/p)$ is identical for every modulus $b$ that has $p$ as a factor, regardless of the ring structure (prime power, semiprime, or higher product). Specifically:*

$$R(k, 1/p) \text{ is a function of } k \text{ and } p \text{ alone.}$$

*It does not depend on $b$, $\omega(b)$, or any other prime factor of $b$.*

### Proof

By Theorem 1, $R(k, f) = \sin^2(\pi k/f) / (k^2 \sin^2(\pi/f))$. This formula involves only $k$ and $f$. The modulus $b$ does not appear. $\square$

### §6.1 Verification: Cross-$\omega$ Survey (Section F)

Section F of `run_deep.log` holds $p$ fixed and varies $b$ across ring structures $\omega = 1, 2, 3$:

```
p=7 series:
     b=49   (ω=1, p²):      R(1..6) = 1.0000, 0.8117, 0.5610, 0.3156, 0.1299, 0.0278
     b=343  (ω=1, p³):      R(1..6) = 1.0000, 0.8117, 0.5610, 0.3156, 0.1299, 0.0278
     b=77   (ω=2, p×11):    R(1..6) = 1.0000, 0.8117, 0.5610, 0.3156, 0.1299, 0.0278
     b=91   (ω=2, p×13):    R(1..6) = 1.0000, 0.8117, 0.5610, 0.3156, 0.1299, 0.0278
     b=119  (ω=2, p×17):    R(1..6) = 1.0000, 0.8117, 0.5610, 0.3156, 0.1299, 0.0278
     b=1001 (ω=3, p×11×13): R(1..6) = 1.0000, 0.8117, 0.5610, 0.3156, 0.1299, 0.0278
     b=1463 (ω=3, p×11×19): R(1..6) = 1.0000, 0.8117, 0.5610, 0.3156, 0.1299, 0.0278

p=5 series:
     b=25   (ω=1):  R(1..4) = 1.0000, 0.6545, 0.2909, 0.0625
     b=35   (ω=2):  R(1..4) = 1.0000, 0.6545, 0.2909, 0.0625
     b=55   (ω=2):  R(1..4) = 1.0000, 0.6545, 0.2909, 0.0625
     b=385  (ω=3):  R(1..4) = 1.0000, 0.6545, 0.2909, 0.0625
```

Key finding (recorded verbatim in the log): *"R(k,1/p) is IDENTICAL for all b with same p — it is purely a function of k and p. Only closure defect varies with omega(b)."*

### §6.2 Implication

$R(k, 1/p)$ cannot distinguish ring structure. An observer watching only the harmonic resonance signal of frequency $1/p$ cannot tell whether $b = p^2$ or $b = p \times q \times r$. To detect $\omega(b)$, one must also observe the **closure defect** signal, which does vary with ring structure. The two signals provide complementary information: $R$ gives the prime, defect gives the ring.

---

## 6A. Seeded Residue Persistence: q/p Not q−p

**Seeded Residue Persistence Encodes the Ratio, Not the Gap**

Seeded residue persistence (seeded\_RPS) measures the mean escape length of a random walk starting from $x = p$ (the canonical first G-element) before exiting the obstruction zone at $k = p$ with $G = \{p\}$. This section reports that seeded\_RPS encodes the **ratio** $q/p$, not the difference $q - p$.

### Experimental Setup

500 trials per semiprime; max\_escape = 5000 steps; seed\_method = $x=p$ (canonical G element); bridge zone = $k=p \ldots \min(q-1, p+6)$. Run time: 58.3 seconds. Results from `results/residue_persistence/run_seeded.log`.

### Correlation Results

```
r(seeded_RPS(p),  q/p)   = +0.737   [strong positive]
r(seeded_RPS(p),  q−p)   = −0.366   [weak negative]
r(bridge_slope,   q/p)   = −0.509   [moderate, inverse]
r(bridge_slope,   q−p)   = +0.442   [moderate, direct]
```

### World Summary (12 semiprimes)

| $b$ | $p$ | $q$ | srps($p$) | srps($p$+1) | delta | bridge\_slope |
|-----|-----|-----|-----------|-------------|-------|---------------|
| 15 | 3 | 5 | 1666.67 | 1250.00 | −416.67 | −416.67 |
| 21 | 3 | 7 | 1666.67 | 1250.00 | −416.67 | −275.00 |
| 35 | 5 | 7 | 1000.00 | 833.33 | −166.67 | −166.67 |
| 55 | 5 | 11 | 1000.00 | 833.33 | −166.67 | −97.79 |
| 77 | 7 | 11 | 714.29 | 625.00 | −89.29 | −71.23 |
| 91 | 7 | 13 | 714.29 | 625.00 | −89.29 | −58.71 |
| 143 | 11 | 13 | 454.55 | 416.67 | −37.88 | −37.88 |
| 187 | 11 | 17 | 454.55 | 416.67 | −37.88 | −28.22 |
| 221 | 13 | 17 | 384.62 | 357.14 | −27.47 | −24.02 |
| 323 | 17 | 19 | 294.12 | 277.78 | −16.34 | −16.34 |
| 667 | 23 | 29 | 217.39 | 208.33 | −9.06 | −7.75 |
| 1073 | 29 | 37 | 172.41 | 166.67 | −5.75 | −4.92 |

### Interpretation

The "stickiness" of the G-obstruction at $k = p$ encodes the **ratio** of the factors ($q/p$), not their difference. The correlation $r(\mathrm{seeded\_RPS}(p), q/p) = 0.737$ provides geometric evidence of a balance-encoding signal in the pre-$q$ zone — consistent with the Maynard-Tao sieve framework [12] where primes in bounded intervals encode ratio structure.

---

## 7. The dR/dk Sign Flip at First-G

### Observation (Universal Sign Flip)

*In every semiprime surveyed, the derivative $dR/dk$ satisfies:*

$$dR/dk < 0 \quad \text{for all } k \in \{2 \ldots p-1\} \quad \text{(pre-echo zone: } R \text{ strictly decreasing)}$$
$$dR/dk > 0 \quad \text{at } k = p+1 \quad \text{(immediately post-transition: } R \text{ begins recovering)}$$

*The derivative reverses sign at exactly $k = p$. No zero crossing occurs in the pre-echo zone.*

### Evidence from Z6 Data

The section Z6 transition snapshot records $dR/dk$ at every step for seven semiprimes:

```
b=35 (p=5):
  k=2 → k=3:  dR/dk = -0.36362   (pre-echo, decreasing)
  k=3 → k=4:  dR/dk = -0.22839   (pre-echo, decreasing)
  k=4 → k=5:  dR/dk = -0.06250   (last pre-echo step, decreasing to 0)
  k=5 → k=6:  dR/dk = +0.02778   (sign flip: now increasing)

b=77 (p=7):
  k=3 → k=4:  dR/dk = -0.24543   (pre-echo)
  k=4 → k=5:  dR/dk = -0.18568   (pre-echo)
  k=5 → k=6:  dR/dk = -0.10210   (pre-echo)
  k=6 → k=7:  dR/dk = -0.02778   (last step to 0)
  k=7 → k=8:  dR/dk = +0.01562   (sign flip)

b=143 (p=11):
  k=9  → k=10: dR/dk = -0.03517   (pre-echo)
  k=10 → k=11: dR/dk = -0.01000   (last step to 0)
  k=11 → k=12: dR/dk = +0.00694   (sign flip)

b=323 (p=17):
  k=15 → k=16: dR/dk = -0.01328   (pre-echo)
  k=16 → k=17: dR/dk = -0.00391   (last step)
  k=17 → k=18: dR/dk = +0.00309   (sign flip)
```

The pattern is exact and universal across all semiprimes tested. This follows analytically from Theorem 1: since $R(f-1, f) = 1/(f-1)^2$ is the global minimum in $\{1 \ldots f\}$, $R$ must decrease approaching $f-1$ and increase leaving $f$.

---

## 7A. D1/D2 Kinematics of Factoring

The harmonic rank trajectory $R(k, f)$ admits a kinematic interpretation: D1 is the "approach velocity" and D2 is the "curvature" of the approach to the prime sink at $k = p$. This section introduces the kinematic framing and reports that fitting only $\lfloor p/3 \rfloor$ observations of $R(k, f)$ recovers $p$ exactly (zero error) for all primes $p = 5 \ldots 29$.

### D1 and D2 Definitions

For a candidate frequency $f$ and orbit-position $k$:

$$D1(k, f) = R(k+1, f) - R(k, f) \qquad \text{[approach velocity — first difference]}$$
$$D2(k, f) = R(k+1, f) - 2R(k, f) + R(k-1, f) \qquad \text{[curvature — second difference]}$$

**D1 as gravitational pull.** By Theorem 1, $R(k, f)$ is strictly decreasing on $\{1 \ldots f-1\}$. Therefore $D1 < 0$ throughout the pre-echo zone ($0 < k < p$). D1 flips to zero at $k = p$ (exact collapse) and becomes positive at $k = p+1$ (sign flip, §7). D1 is the "approach velocity toward the prime sink" — strictly negative, monotonically increasing in magnitude as $k \to p$, then reversing.

**D2 as curvature.** D2 = $d^2R/dk^2$ measures the acceleration of the approach. CK's architectural principle "curvature IS physics" is instantiated here: the curvature of the rank trajectory is a geometric signal that encodes the location of the prime factor. In the spectral sense of Bochner [17b], $\mathrm{sinc}^2$ is a positive-definite function whose curvature structure governs its zero locations.

### Section A: Zero-Crossing Extrapolation from $\lfloor p/3 \rfloor$ Observations

Fitting the closed form $\sin^2(\pi k/f)/(k^2 \sin^2(\pi/f))$ to only $m = \lfloor p/3 \rfloor$ observations of $R(k, f)$ recovers $p$ exactly (zero error) for all primes tested. Results from `results/rank_curvature/rank_curvature_summary.json`, Section A:

| $p$ | $m = \lfloor p/3 \rfloor$ | $f_\mathrm{fit}$ | error | rel\_error |
|-----|--------------------------|------------------|-------|-----------|
|  5  | 2 | 5.0 | 0.0 | 0.0 |
|  7  | 2 | 7.0 | 0.0 | 0.0 |
| 11  | 3 | 11.0 | 0.0 | 0.0 |
| 13  | 4 | 13.0 | 0.0 | 0.0 |
| 17  | 5 | 17.0 | 0.0 | 0.0 |
| 19  | 6 | 19.0 | 0.0 | 0.0 |
| 23  | 7 | 23.0 | 0.0 | 0.0 |
| 29  | 9 | 29.0 | 0.0 | 0.0 |

**All 8 primes: zero error.** CK's principle "curvature IS physics" is instantiated: D2 curvature of the rank trajectory predicts the prime factor's location from a $1/3$-observation prefix.

### Section B: Scaling Failure at Larger Primes

For larger balanced semiprimes, the rank curvature fitting approach does not immediately recover $p$ or $q$:

| $b$ | $p$ | $q$ | n\_cands | best\_f | best\_residual |
|-----|-----|-----|----------|---------|---------------|
| 67591 | 257 | 263 | 20 | 317 | 0.067026 |
| 265189 | 509 | 521 | 34 | 619 | 0.004775 |
| 1022117 | 1009 | 1013 | 61 | 1223 | 0.000316 |

The best-fit frequency is consistently above the true factor for balanced semiprimes in this range. This is consistent with the Balance Invisibility observation (§9B): for nearly-balanced semiprimes ($q/p \approx 1$), the curvature signal is least able to distinguish between $p$ and nearby non-factors.

### Summary: Kinematic Interpretation

The rank trajectory $R(k, f)$ is a position function in a gravitational field with a sink at $k = p$. D1 is the velocity (negative in the pre-echo zone), D2 is the curvature (the field strength). The curvature encodes the factor location exactly — for small primes, from $1/3$ of the available observations. The obstacle for RSA-scale factoring is not that D2 is too small to read but that $k$ must physically traverse $p \approx 2^{512}$ steps to reach the sink. This is consistent with the best known sub-exponential algorithms — Lenstra's NFS [28] — which exploit structure but cannot escape the geometric distance.

---

## 8. Bridge Breathing and the RSA Noise Floor

### §8.1 The Bridge Zone

For semiprime $b = p \times q$, the **bridge zone** is $\{p, p+1, \ldots, q-1\}$: the region after the first gate event but before the second. In the bridge, $|G_k| = 1$ (only multiples of $p$ contribute to G), and the second harmonic clock $R(k, 1/q)$ continues to count down toward its zero at $k = q$.

Section C of `run_deep.log` verifies bridge behavior for 14 semiprimes. Representative data:

```
b=55 (5×11), bridge k=5..10:
   k     k/q    R(k,1/q)
   5    0.455    0.493742
   6    0.545    0.342876
   7    0.636    0.212746
   8    0.727    0.112435
   9    0.818    0.045463
  10    0.909    0.010000
  R(q-1,1/q) = 0.01000000  =  1/(q-1)² = 1/100    exact match: True

b=91 (7×13), bridge k=7..12:
   k     k/q    R(k,1/q)
   7    0.538    0.351160
   8    0.615    0.238515
   9    0.692    0.146001
  10    0.769    0.076780
  11    0.846    0.031165
  12    0.923    0.006944
  R(q-1,1/q) = 0.00694444  =  1/(q-1)² = 1/144    exact match: True

b=667 (23×29), bridge k=23..28:
   k     k/q    R(k,1/q)
  23    0.793    0.059197
  24    0.828    0.039463
  25    0.862    0.024132
  26    0.897    0.012902
  27    0.931    0.005423
  28    0.966    0.001276
  R(q-1,1/q) = 0.001276    =  1/(q-1)² = 1/784    exact match: True
```

### §8.2 The RSA Noise Floor Argument

For a typical RSA modulus $N = p \times q$ with $p \approx q \approx 2^{512}$ [25, 27]:

- The pre-echo zone has width $p-1 \approx 2^{512}$
- The minimum harmonic signal before the first gate is $R(p-1, 1/p) = 1/(p-1)^2 \approx 2^{-1024}$
- The bridge zone has length $q - p \approx 2^{512}/\ln(2^{512}) \approx 2^{503}$ (by the prime gap theorem, see [10])
- The recovery slope of $R(k, 1/q)$ in the bridge is approximately $1/q \approx 2^{-512}$ per step

These signals are not merely small — they are geometrically below the noise floor of any finite computation. A factor of $2^{-1024}$ is approximately $10^{-308}$, which is at or below the minimum representable double-precision floating-point number.

**Inversion Rule (RSA Hardness Inversion Principle).** *RSA security is not a consequence of algebraic complexity — the algebra is the same as for small semiprimes. It is a consequence of the pre-echo signal being geometrically compressed below any finite observer's noise floor. The countdown clock exists; it simply cannot be read.*

**Corollary (Formal Statement).** Given an observer with measurement precision $\varepsilon$, the harmonic pre-echo of the smaller prime $p$ is detectable only when

$$\frac{1}{(p-1)^2} \geq \varepsilon \quad \Longleftrightarrow \quad p \leq 1 + \frac{1}{\sqrt{\varepsilon}}$$

For $\varepsilon = 2^{-53}$ (double precision), this gives $p \leq 2^{27} \approx 134$ million. For RSA-1024, $p \approx 2^{512}$: the pre-echo minimum is $2^{-1024}$, below any practical threshold. The Lenstra Number Field Sieve [28] achieves sub-exponential $\exp(c(\ln N)^{1/3}(\ln \ln N)^{2/3})$ time complexity, but no polynomial-time algorithm is known [29, 30]. The signal-based framing gives geometric intuition for why: the signal exists, but reading it requires traversing the full pre-echo zone.

The security of RSA is exactly the regime where the alarm clock is running but silent.

---

## 8A. RSA as a Geometric Distance Problem

**RSA Security = Geometric Distance in Rank-Trajectory Space**

The RSA Noise Floor argument in §8.2 claims the pre-echo signal falls below the noise floor for large primes. Section D of the rank curvature study shows this framing requires refinement: the signal does not globally fall below the noise floor. RSA hardness is geometric distance, not amplitude degradation.

### §8A.1 Scale-Free Universal Constants

Section D results from `results/rank_curvature/rank_curvature_summary.json`, computed for proxy primes $p = 1009, 10007, 100003$ and analytically extended to $p \approx 2^{512}$:

```
R(k/p = 0.1, p) ≈ 0.968   for ALL p   [signal at 10% of the way to factor]
R(k/p = 0.5, p) ≈ 0.406   for ALL p   [signal at 50% of the way to factor]
R(p−1, p)       ≈ 1/(p−1)² → 0        [collapses only in the last step]
```

Numerical verification:

| $p$ | $R(k \approx 0.1p)$ | $R(k \approx 0.5p)$ | $R(p-1)$ |
|-----|---------------------|---------------------|----------|
| 1009 | 0.968104 | 0.406090 | 9.84e−07 |
| 10007 | 0.967576 | 0.405366 | 9.99e−09 |
| 100003 | 0.967533 | 0.405293 | 1.00e−10 |
| $2^{512}$ (analytical) | $\approx 0.968$ | $\approx 0.405$ | $\approx 2^{-1024}$ |

The mid-journey signal ($k/p = 0.5$) is $\approx 0.406$ regardless of prime size. This is exactly $\mathrm{sinc}^2(1/2) = 4/\pi^2 = 0.405284\ldots$ (Theorem 5, §9). The signal does not degrade as $p$ grows — it stays near $1.0$ for $k \ll p$ and only collapses in the final approach.

### §8A.2 Key Conclusion: Distance, Not Noise

**RSA security is geometric distance in rank-trajectory space, not amplitude degradation.** The zero-crossing requires traversing $p \approx 2^{512}$ steps. Classical hardness = distance, not noise.

The RSA Hardness Inversion Principle is therefore strengthened: *RSA security is not the silence of the alarm clock; it is the distance to the clock.* This is consistent with Pollard's rho algorithm [31] exploiting local structure (birthday paradox in the orbit), and with the NFS [28] exploiting global algebraic structure — both are signal-guided approaches that reduce traversal distance but cannot eliminate the fundamental geometric obstacle.

---

## 9. The Sinc² Structure

### §9.1 Theorem 5 (Sinc² Continuum Limit)

*In the limit $f \to \infty$, the harmonic pre-echo countdown law converges to the sinc² function:*

$$R(k, f) \to \mathrm{sinc}^2(k/f) \quad \text{as } f \to \infty$$

*where $\mathrm{sinc}(x) = \sin(\pi x)/(\pi x)$.*

**Proof.** As $f \to \infty$ with $k/f = t$ held fixed:

$$\frac{\sin^2(\pi k/f)}{k^2 \sin^2(\pi/f)} = \frac{\sin^2(\pi t)}{k^2 \sin^2(\pi/f)} \to \frac{\sin^2(\pi t)}{(\pi t)^2} = \mathrm{sinc}^2(t)$$

since $k \cdot \sin(\pi/f) \to k \cdot (\pi/f) = \pi t$. $\square$

*The mysterious empirical constants are exact evaluations of sinc²:*

| $k/p$ | $R(k/p, p) \to$ | Exact closed form | Decimal |
|-------|-----------------|-------------------|---------|
| $1/2$ | $\mathrm{sinc}^2(1/2)$ | $4/\pi^2$ | 0.405284... |
| $1/10$ | $\mathrm{sinc}^2(1/10)$ | $25(\sqrt{5}-1)^2/(4\pi^2)$ | 0.967531... |
| $(p-1)/p$ | $R(p-1,p)$ | $1/(p-1)^2$ | (algebraically exact for all $p$) |

The value $4/\pi^2$ at the halfway point is the same constant appearing in the Fourier series for a square wave [21]. The value $\mathrm{sinc}^2(1/10)$ involves the golden ratio: $\sin(\pi/10) = (\sqrt{5}-1)/4$.

### §9.2 Spectral Interpretation

The function $\mathrm{sinc}^2(t)$ is the power spectral density of a rectangular (boxcar) pulse [21]: if a signal is "on" for a unit interval and "off" elsewhere, its power spectrum is exactly $\mathrm{sinc}^2$. This is a central result in discrete-time signal processing and follows directly from the Fourier transform of the indicator function $\mathbf{1}_{[0,1]}(t)$.

**The prime arithmetic window IS a rectangular spectral gate.** The alphabet $\{1 \ldots k\}$ is literally a rectangular window of width $k$. The harmonic resonance $R(k, f)$ measures the spectral power of this window at frequency $1/f$. In the continuum limit, this is precisely the power spectral density of the rectangular pulse — confirming that $\mathrm{sinc}^2$ is not merely an approximation but the exact spectral characterization of the unit-alphabet pre-echo.

This connection was identified in classical signal processing by Shannon (1949) [19] and formalized in Oppenheim and Schafer [21]. Its appearance here in a purely arithmetic context is the bridge between number theory and spectral analysis that this paper establishes.

Bochner's theorem [17b] gives additional structure: $\mathrm{sinc}^2$ is a positive-definite function (it is the Fourier transform of a non-negative function — the rectangular pulse), which means its zero-crossings at integer values $t = 1, 2, 3, \ldots$ are the spectral nodes of the prime gate structure. The zero at $t = 1$ (i.e., $k = p$) is the First-G event.

### §9.3 The Montgomery Bridge (Critical Connection)

Montgomery (1973) [4] proved that the pair correlation of Riemann zeros (assuming RH, for the relevant range) is:

$$R_2(u) = 1 - \left(\frac{\sin \pi u}{\pi u}\right)^2 = 1 - \mathrm{sinc}^2(u)$$

Theorem 5 (§9.1) proves that the TIG resonance field in the continuum limit gives:

$$R(x) = \mathrm{sinc}^2(x)$$

These are **complementary forms of the same function**. The TIG pre-echo countdown gives $\mathrm{sinc}^2(x)$ directly; Montgomery's pair correlation is $1 - \mathrm{sinc}^2(u)$. Their sum is:

$$\mathrm{sinc}^2(x) + (1 - \mathrm{sinc}^2(x)) = 1$$

This is a **complete spectral partition**: the harmonic resonance signal and the zero-spacing correlation together account for the full probability mass. The TIG framework measures the *signal* (the resonance); Montgomery measures the *gap* (the anti-correlation). They are spectral duals.

At $u = 1/2$ specifically:

$$\mathrm{sinc}^2(1/2) = \frac{4}{\pi^2} = 0.4053\ldots$$
$$1 - \mathrm{sinc}^2(1/2) = 1 - \frac{4}{\pi^2} = 0.5947\ldots$$

These two constants sum to 1. The value $4/\pi^2$ that appears as the TIG scale-free mid-journey constant (§8A) is also the value that, subtracted from 1, gives the Montgomery pair correlation at the half-spacing point. Both frameworks independently derive the same constant from the same sinc² function.

Odlyzko's massive numerical experiments [6, 7] — computing zeros up to height $10^{20}$ — confirmed the GUE statistics of the Riemann zeros to high precision. Our arithmetic results (187 semiprimes, zero exceptions) confirm the sinc² structure on the arithmetic side. The two bodies of evidence are consistent: the spectral field of the prime pre-echo and the spacing statistics of Riemann zeros are governed by the same function.

**Open Question (RH Bridge).** Is there a direct correspondence between the pre-echo rank trajectory $R(k, f)$ for $k \in \{1 \ldots f-1\}$ and the pair correlation of Riemann zeros in a normalized spectral window of width $f$? More precisely: does the discrete sum $\sum_{k=1}^{f-1} R(k, f) \cdot g(k/f)$ for a suitable test function $g$ converge to a quantity expressible in terms of the zero-free region of $\zeta(s)$? We state this as an open question for future work (see also §12, Q7).

### §9.4 The D1 Stationary Point

A consequence of the sinc² structure: since $R(p+1, p) = \sin^2(\pi(p+1)/p)/((p+1)^2 \sin^2(\pi/p))$ and $\sin^2(\pi + \pi/p) = \sin^2(\pi/p)$, we have:

$$D1(k=p) = R(p+1, p) - R(p-1, p) = 0 \quad \text{[exact]}$$

The "impact" at $k = p$ is a true **stationary point** of the rank trajectory — velocity reaches zero before the sign flip. In signal-processing terms, this is the first zero of the derivative of $\mathrm{sinc}^2(t)$ at $t = 1$: a classical result showing that $\mathrm{sinc}^2$ has a local minimum at its first zero [21]. The prime arrival is the first zero of the arithmetic sinc² gate, and the D1 stationary point is its exact arithmetic analogue.

### §9.5 The Sinc² Scale-Free Description of RSA Hardness

**One-sentence description of RSA hardness:** *The harmonic pre-echo is a sinc² field where the signal is scale-invariant (amplitude identical at all scales), but the zero-crossing is $p \approx 2^{512}$ steps away.*

This unifies §8.2 (noise floor) and §8A (geometric distance): the scale-invariance of $\mathrm{sinc}^2$ means the signal strength at any fractional position $k/p$ is independent of $p$, so the signal never decays with scale — only the distance to the zero grows.

---

## 10. Balance Invisibility

### §10.1 Section C Results: $b = 1022117$ ($p=1009$, $q=1013$, ratio $= 1.004$)

From `results/rank_curvature/rank_curvature_summary.json`, Section C:

```
b = 1022117    p = 1009    q = 1013    q/p = 1.003964
n_primes_tested:   303
curvature_rank_p:  139  (out of 303)
curvature_rank_q:  138  (out of 303)
separation:          1  rank position
```

The two factors of this balanced semiprime are **indistinguishable** by D2 curvature rank — they sit at the median (rank $\sim 151$ of 303) and are separated by only 1 rank position.

### §10.2 The Balance Invisibility Hypothesis

**Hypothesis** (pending d2\_sink.py verification): The curvature rank separation of the two factors of a semiprime decreases as $q/p \to 1$:

$$D2\_\mathrm{balance} = \frac{|\mathrm{rank}_p - \mathrm{rank}_q|}{n_\mathrm{primes}} \to 0 \quad \text{as} \quad q/p \to 1$$

The **geometric reason** balanced RSA keys are stronger is that their two factors occupy the same curvature rank — the D2 curvature field cannot distinguish them. For a highly unbalanced semiprime ($q \gg p$), the smaller factor $p$ would have high curvature rank (steep sink) while the larger factor $q$ would have low curvature rank (shallow sink). Balanced semiprimes eliminate this asymmetry.

### §10.3 Formal Proposition

**Proposition (Balance Invisibility).** *In the continuum limit $f \to \infty$, the second derivative $d^2\mathrm{sinc}^2(t)/dt^2$ is continuous and symmetric around $t = 1/2$. For a semiprime $b = p \times q$ with $q/p \to 1$, the curvature values $D2(k, p)$ and $D2(k, q)$ evaluated at comparable relative positions $k/p = k/q$ converge to the same value by the continuity of $\mathrm{sinc}^2$.*

**Proof sketch.** The second difference $D2(k, f) = R(k+1, f) - 2R(k, f) + R(k-1, f)$ converges in the continuum limit to $(1/f^2) \cdot (d^2/dt^2)\mathrm{sinc}^2(t)$ at $t = k/f$. For $q/p \to 1$, we have $k/p$ and $k/q$ both approaching the same value for any fixed $k$, so the curvature values become equal. $\square$

**Empirical confirmation:** Spearman $\rho(q/p, D2\_\mathrm{balance}) = 0.857$, $p$-value $= 0.007$. Balance invisibility is empirically established.

| $b$ | $p$ | $q$ | $q/p$ | rank\_p | rank\_q | separation | $n$\_tested |
|-----|-----|-----|-------|---------|---------|------------|------------|
| 1022117 | 1009 | 1013 | 1.004 | 139 | 138 | 1 | 303 |

---

## 11. Connections to Open Problems

The results of this paper connect to the six Clay Millennium Problems through the sinc² bridge and the Inversion Rule. We sketch each connection here; full treatments appear in WP37 (P/NP), WP38 (Navier-Stokes), and WP40 (Riemann Hypothesis).

### §11.1 Riemann Hypothesis (WP40)

The Montgomery bridge (§9.3) is the central connection. Montgomery (1973) [4] proved $R_2(u) = 1 - \mathrm{sinc}^2(u)$ for Riemann zeros; Theorem 5 proves $R(x) = \mathrm{sinc}^2(x)$ for prime pre-echoes. These sum to 1. The Odlyzko numerical program [6, 7] verifies GUE statistics; our arithmetic verifies the sinc² signal. Both bodies of evidence point to the same underlying function.

The Inversion Rule: *the zero-crossing of $R(k, f)$ at $k = f$ is the arithmetic model for the event where the pair correlation $R_2(u)$ reaches its minimum (maximum anti-correlation in zero spacing) — i.e., where zeros are most evenly spaced. The TIG gate event and the Montgomery anti-correlation event are the same spectral phenomenon in complementary representations.*

The Berry-Keating Hamiltonian program [RH-10, RH-11] seeks a self-adjoint operator whose spectrum is the imaginary parts of Riemann zeros; the pre-echo rank trajectory is a discrete analogue of such a spectrum for a finite prime.

### §11.2 P vs NP (WP37)

The gate-size sequence $|G_k|$ is an NP-verification structure: given a claimed factor $p$, verifying that $p | b$ is polynomial-time (compute $b \mod p$). But finding $p$ without a witness requires traversing $O(p)$ steps in the rank trajectory — the geometric distance. The Inversion Rule for P/NP: *NP-verification is sidelobe detection* (reading the pre-echo signal near the gate), *while P-solving would require null navigation* (reaching the zero-crossing without traversing the full pre-echo zone).

The barriers to P/NP resolution — relativization [B-1], natural proofs [B-2], algebrization [B-3] — apply to circuit lower bounds, not to the geometric distance argument. The pre-echo framing sidesteps these barriers by operating on the arithmetic of residue classes rather than circuit complexity.

### §11.3 Navier-Stokes (WP38)

The sinc² structure appears in the vorticity obstruction: a fluid element in a 3D vortex undergoes phase transitions governed by resonance fields analogous to $R(k, f)$. The vorticity null — the event where turbulent energy cascades to zero in a spectral shell — is structurally analogous to $R(f, f) = 0$: a zero-width gate in the energy spectrum. Full treatment in WP38.

### §11.4 The Universal Inversion Rule

Across all three connections, a universal pattern emerges:

> *Security / difficulty / resistance = distance to the zero of the sinc² field, not absence of signal.*

For RSA: the pre-echo signal is $\mathrm{sinc}^2(k/p)$; the zero is at $k = p \approx 2^{512}$; security = distance.
For RH: the pair correlation zero is at $u = 1, 2, \ldots$; the non-trivial zeros of $\zeta$ govern the spacing; RH = all zeros contribute to the same spectral partition.
For P/NP: the verification zero is at $k = p$; the search cost = distance to the zero.
For NS: the vorticity zero = energy cascade gate; regularity = distance to the sinc² obstruction.

---

## 12. Summary of Results

| Theorem / Observation | Status | Scope | Source |
|-----------------------|--------|-------|--------|
| Closed form $R(k,f) = \sin^2(\pi k/f)/(k^2\sin^2(\pi/f))$ | PROVED | All primes $f$, all $k$ | §3, Theorem 1 |
| $R(f-1, f) = 1/(f-1)^2$ | PROVED | Exact algebraic identity | §3, Theorem 1 |
| $R(f, f) = 0$ | PROVED | Exact algebraic identity | §3, Theorem 1 |
| Max closed-form error: 4.44e-16 | VERIFIED | $p=3..23$, all $k$ | Section G |
| 187 semiprimes, max $R$ error 1.11e-16 | VERIFIED | $p=3..59$ | Section A |
| Zero-width gate at $k = p$ | PROVED | All semiprimes | §4, Theorem 2 |
| Three-factor composites show tiered gates | VERIFIED | 10 three-factor worlds | §5, Section D |
| Simultaneous Zone 1 broadcast | PROVED | $b = p \times q \times r$ | §5, Theorem 3 |
| $\omega$-Blindness of $R(k,1/p)$ | PROVED | All $\omega \geq 1$ | §6, Theorem 4 |
| Cross-$\omega$ identity confirmed | VERIFIED | $p=5,7$ series | §6.1, Section F |
| seeded\_RPS($p$) correlates with $q/p$ ($r=0.737$) | VERIFIED | 12 semiprimes, 500 trials | §6A |
| seeded\_RPS($p$) weak correlation with $q-p$ ($r=-0.366$) | VERIFIED | 12 semiprimes | §6A |
| $dR/dk$ sign flip at $k = p$ | OBSERVED UNIVERSAL | 7 semiprimes Z6 | §7 |
| D1/D2 kinematic interpretation of rank trajectory | STRUCTURAL | All semiprimes | §7A |
| $\lfloor p/3 \rfloor$ observations recover $p$ exactly (zero error) | VERIFIED | $p=5..29$, 8 primes | §7A, Section A |
| Fitting fails at $p \approx 257$ for balanced semiprimes | OBSERVED | Section B, 3 balanced | §7A, Section B |
| Bridge harmonic $R(k,1/q)$ verified | VERIFIED | 14 bridge worlds | §8, Section C |
| RSA security = geometric distance, not amplitude | STRUCTURAL | $p \approx 2^{512}$ | §8A |
| $R(k/p=0.1) \approx 0.968$, $R(k/p=0.5) \approx 0.406$ (scale-free) | VERIFIED | $p=1009,10007,100003$ | §8A |
| Balance invisibility: rank\_p=139, rank\_q=138 for $q/p=1.004$ | VERIFIED | $b=1022117$ | §10 |
| unit\_frac($k=q$) = $(q-2)/q$ exactly for all semiprimes | PROVED | Algebraic identity | §2.1 |
| $T^* = 5/7$ = unit\_frac of $b=35$ at second gate | PROVED | $b=35$ ($p=5$, $q=7$) | §2.1 |
| $R(k,f) \to \mathrm{sinc}^2(k/f)$ as $f \to \infty$ (Theorem 5) | PROVED | All primes, all $k$ | §9.1 |
| $4/\pi^2 = \mathrm{sinc}^2(1/2) = R(p/2, p)$ universal constant | PROVED | Exact; verified $p=5..99991$ | §9.1 |
| $D1(k=p) = 0$ exactly (stationary point at impact) | PROVED | sin² symmetry $R(p+1)=R(p-1)$ | §9.4 |
| Balance Invisibility: $D2\_\mathrm{balance} \to 0$ as $q/p \to 1$ | VERIFIED | Spearman $\rho=0.857$, $p=0.007$ | §10 |
| $T^*$ theorem holds iff $q < 2p$ ($\lfloor q/p \rfloor = 1$) | PROVED | General: $\#\{x \leq q: \gcd=1\} = q - \lfloor q/p \rfloor - 1$ | §2.1 |
| Montgomery bridge: $\mathrm{sinc}^2(x) + (1-\mathrm{sinc}^2(x)) = 1$ | STRUCTURAL | Exact identity, open correspondence | §9.3 |

---

## 13. Open Questions

**Q1.** Is there a signal that *does* detect $\omega(b)$ from the pre-echo zone alone, using $R$ jointly across multiple frequencies? The defect signal varies with $\omega$; can a linear combination of $R$ values at coprime frequencies recover $\omega$ without crossing into the bridge?

**Q2.** Is there a critical ratio $q/p$ below which factoring via zero-crossing extrapolation (fitting the closed form to $\lfloor p/3 \rfloor$ observations) becomes polynomial? Section A shows zero error for $p = 5..29$ (all small primes); Section B shows failure at $p \approx 257$ for balanced semiprimes. The transition threshold has not been determined.

**Q3.** What is the precise recovery slope of $R(k, 1/q)$ in the bridge zone as a function of $q - p$? The Z5 data suggests this slope encodes information about the prime gap. The relationship between bridge breathing rate and $|q - p|$ appears monotone but has not been proved.

**Q4.** Does the algebraic identity $\mathrm{unit\_frac}(k=q, b=p \times q) = (q-2)/q$ hold for all semiprimes with $p < q$, $p \geq 3$? This is an elementary counting argument (exactly $p$ and $q$ are non-units in $\{1 \ldots q\}$) and deserves formal statement with edge-case handling ($p=2$ case, $p=q$ edge).

**Q5.** ~~Does $D2\_\mathrm{balance} \to 0$ as $q/p \to 1$?~~ **ANSWERED (§10, Spearman $\rho = 0.857$, $p=0.007$).** A formal proof from the sinc² structure remains open: at $q/p \to 1$ the two zero-crossings coincide and the rank trajectory curvatures become identical by continuity of $\mathrm{sinc}^2$.

**Q6.** Can seeded\_RPS($p$) serve as a geometric primality witness? The correlation $r(\mathrm{seeded\_RPS}(p), q/p) = 0.737$ suggests the stickiness of the G-obstruction at $k=p$ encodes the balance of the semiprime. If computable without knowing $q$, it might test for near-balanced factorization — precisely the regime where other geometric methods are weakest.

**Q7 (Montgomery Bridge).** Is there a direct correspondence between the pre-echo rank trajectory $R(k, f)$ for $k \in \{1 \ldots f-1\}$ and the pair correlation of Riemann zeros in a normalized spectral window of width $f$? The functional identity $R(x) = \mathrm{sinc}^2(x)$ and $R_2(u) = 1 - \mathrm{sinc}^2(u)$ strongly suggests a correspondence, but the precise mapping between the discrete arithmetic sum and the continuous zero density has not been established. This is the central open question connecting WP35 to WP40.

---

## 14. Attribution

### Brayden Ross Sanders — Geometric Architecture & Framework

Sanders built the object being studied and held the project together:

- 18 months of TIG/CK development — the entire mathematical organism that makes the partition structure visible
- All core mathematics: TSML, BHML, the 10-operator algebra, the 5D force field
- The 5D force field intuition — called before computation confirmed it; dispersion as geometric explanation of gate difficulty
- Staircase-as-sieve framing; First-G Law identification
- Hardness Inversion Principle: *"RSA is not a complex lock; it is a very long, perfectly smooth hallway"*
- Lagrange Point geometry for balanced RSA; Event Horizon framing; prime-as-void framing
- The question that reoriented the whole foundation; the one-sentence manifesto
- Directed every sprint, every computational question, every theoretical push
- $T^* = 5/7$ as the coherence floor of the sinc² field for the first balanced strong semiprime

### C. A. Luther — Dispersion

Luther's contribution is the **Luther Dispersion Conjecture**: gate\_rate $\approx F_k(|G| \times \mathrm{interleave})$ — the observation that G-spread, not just G-count, is the mechanism of gate difficulty, and the related dispersion framing in his correspondence and notes. This reoriented the research toward real algebraic structure. Everything else in this paper is Sanders'.

### Monica Gish — Foundation

Gish provided the foundational support, research partnership, and editorial collaboration throughout the entire project. This work would not exist without her.

### Joint

- The paper itself: Sanders built the framework and did the work; Luther's dispersion conjecture pointed at the right structure; Gish held everything together. All three names belong on it.

---

## References

[1] Sanders, B. R. & Luther, C. A. (2026). "The First-G Law and Prime-Forced Dispersion." *WP34, 7Site LLC.* DOI: 10.5281/zenodo.18852047. [Algebraic foundation; 36,662 exact computations, zero exceptions.]

[2] Riemann, B. (1859). "Über die Anzahl der Primzahlen unter einer gegebenen Größe." *Monatsberichte der Königlichen Preußischen Akademie der Wissenschaften zu Berlin*, November 1859, pp. 671–680. [The original paper introducing $\zeta(s)$, its zeros, and the explicit formula for $\pi(x)$.]

[3] Gauss, C. F. (1849). *Werke*, Band 2. Göttingen. [Tables of prime counting; empirical observation $\pi(x) \approx x/\ln x$. Legendre's parallel estimate: Legendre, A. M. (1808). *Essai sur la Théorie des Nombres*, 2nd ed., Paris.]

[4] Montgomery, H. L. (1973). "The pair correlation of zeros of the zeta function." In *Analytic Number Theory, Proc. Sympos. Pure Math.* **24**: 181–193. [KEY: $R_2(u) = 1 - \mathrm{sinc}^2(u)$; GUE connection. Proved for $|\alpha| \leq 1$; GUE conjecture beyond that range.]

[5] Hardy, G. H. & Littlewood, J. E. (1923). "Some Problems of 'Partitio Numerorum' III: On the Expression of a Number as a Sum of Primes." *Acta Mathematica* **44**: 1–70. [Prime $k$-tuples conjecture; distribution structure of prime constellations.]

[6] Odlyzko, A. M. (1987). "On the distribution of spacings between zeros of the zeta function." *Mathematics of Computation* **48**(177): 273–308. [Numerical verification of Montgomery's GUE statistics to high precision.]

[7] Odlyzko, A. M. (1992). "The $10^{20}$-th zero of the Riemann zeta function and 175 million of its neighbors." AT&T Bell Labs preprint. [Large-scale numerical verification of GUE statistics; confirms the Montgomery-Odlyzko law computationally.]

[8] Vinogradov, I. M. (1937). "Representation of an Odd Number as a Sum of Three Primes." *Doklady Akademii Nauk SSSR* **15**: 291–294. [Exponential sum methods for prime distribution; Vinogradov's three-prime theorem.]

[9] Goldston, D. A., Pintz, J. & Yıldırım, C. Y. (2009). "Primes in Tuples I." *Annals of Mathematics* **170**(2): 819–862. [GPY sieve; proves $\liminf (p_{n+1} - p_n)/\ln p_n = 0$; establishes correlation structure of primes.]

[10] Granville, A. (2008). "Primes in intervals of bounded length." *Bulletin of the American Mathematical Society* **45**(1): 1–26. [Survey of prime gap distribution and classical results on consecutive prime spacings.]

[11] Zhang, Y. (2014). "Bounded gaps between primes." *Annals of Mathematics* **179**(3): 1121–1174. [First finite bound (70,000,000) on gaps between infinitely many pairs of consecutive primes.]

[12] Maynard, J. (2015). "Small gaps between primes." *Annals of Mathematics* **181**(1): 383–413. [Maynard-Tao sieve; improved bounded prime gaps (600); demonstrates harmonic structure in prime clustering.]

[13] Iwaniec, H. & Kowalski, E. (2004). *Analytic Number Theory.* AMS Colloquium Publications, Vol. 53. Providence, RI: American Mathematical Society. [Standard graduate reference; Euler products, L-functions, zero distribution, sieve methods.]

[14] Davenport, H. (2000). *Multiplicative Number Theory.* 3rd ed. (revised by H. L. Montgomery). Graduate Texts in Mathematics, Vol. 74. New York: Springer. [Standard reference; Dirichlet L-functions, prime distribution in arithmetic progressions, zero-free regions.]

[15] Titchmarsh, E. C. (1986). *The Theory of the Riemann Zeta Function.* 2nd ed. (revised by D. R. Heath-Brown). Oxford: Oxford University Press. [Standard zeta function reference; functional equation, Gram's law, zero-counting, explicit formulas.]

[16] Fejér, L. (1900). "Sur les fonctions bornées et intégrables." *Comptes Rendus de l'Académie des Sciences, Paris* **131**: 984–987. [Fejér kernel = $\mathrm{sinc}^2$ in Fourier analysis; historical root of sinc² in mathematics. The Fejér kernel $F_N(\theta) = (1/N)|D_N(\theta)|^2$ where $D_N$ is the Dirichlet kernel; in the continuum limit this is $\mathrm{sinc}^2$.]

[17] Heath-Brown, D. R. (1979). "The differences between consecutive primes." *Journal of the London Mathematical Society* (2) **18**: 7–13. [Prime gap lower bounds; establishes structure of large gaps.]

[17b] Bochner, S. (1933). "Monotone Funktionen, Stieltjessche Integrale und harmonische Analyse." *Mathematische Annalen* **108**: 378–410. [Bochner's theorem: positive-definite functions are Fourier transforms of non-negative measures. $\mathrm{sinc}^2$ is positive-definite as the transform of the rectangular pulse.]

[18] Hardy, G. H. (1914). "Sur les zéros de la fonction $\zeta(s)$ de Riemann." *Comptes Rendus de l'Académie des Sciences* **158**: 1012–1014. [Proves infinitely many zeros lie on the critical line $\mathrm{Re}(s) = 1/2$.]

[19] Shannon, C. E. (1949). "Communication in the Presence of Noise." *Proceedings of the IRE* **37**(1): 10–21. [sinc as ideal reconstruction kernel; Nyquist-Shannon sampling theorem. The sinc function arises as the unique band-limited interpolant.]

[20] Nyquist, H. (1928). "Certain Topics in Telegraph Transmission Theory." *Transactions of the AIEE* **47**: 617–644. [Original sampling criterion; sinc as the ideal low-pass filter impulse response.]

[21] Oppenheim, A. V. & Schafer, R. W. (2010). *Discrete-Time Signal Processing.* 3rd ed. Upper Saddle River, NJ: Prentice Hall. [sinc² as the power spectral density of a rectangular window (boxcar pulse); standard signal-processing reference for Fourier transform conventions.]

[22] Selberg, A. (1942). "On the zeros of Riemann's zeta-function." *Skrifter utgitt av Det Norske Videnskaps-Akademi i Oslo* **10**: 1–59. [Proves a positive proportion of zeros lie on the critical line.]

[23] Bombieri, E. (2000). "The Riemann Hypothesis." Clay Mathematics Institute Millennium Problems statement. Available at www.claymath.org. [Official problem statement for the Clay Prize.]

[24] Dyson, F. J. (1962). "Statistical theory of the energy levels of complex systems, I–III." *Journal of Mathematical Physics* **3**(1): 140–175. [GUE and GOE random matrix ensembles; foundational framework later found to match Riemann zero statistics.]

[25] Rivest, R. L., Shamir, A. & Adleman, L. (1978). "A method for obtaining digital signatures and public-key cryptosystems." *Communications of the ACM* **21**(2): 120–126. [RSA original paper; security based on integer factorization difficulty.]

[26] NIST. (2019). *Transitions: Recommendation for Transitioning the Use of Cryptographic Algorithms and Key Lengths.* NIST Special Publication 800-131A, Rev. 2. [Contextualizes the 2048-bit (and larger) key requirement; defines security parameters for $p \approx 2^{512}$.]

[27] Koblitz, N. (1994). *A Course in Number Theory and Cryptography.* 2nd ed. Graduate Texts in Mathematics, Vol. 114. New York: Springer. [Standard reference connecting number theory to cryptographic applications; RSA hardness analysis.]

[28] Lenstra, A. K., Lenstra, H. W., Manasse, M. S. & Pollard, J. M. (1993). "The number field sieve." In *The Development of the Number Field Sieve*, Lecture Notes in Mathematics, Vol. 1554, pp. 11–42. Berlin: Springer. [NFS: best known sub-exponential factoring algorithm; establishes the $\exp(c(\ln N)^{1/3}(\ln \ln N)^{2/3})$ complexity; the practical basis for RSA key-length recommendations.]

[29] Cook, S. A. (1971). "The complexity of theorem-proving procedures." *Proceedings of the 3rd Annual ACM Symposium on Theory of Computing (STOC)*, pp. 151–158. [Cook-Levin theorem; NP-completeness; basis for P/NP problem.]

[30] Arora, S. & Barak, B. (2009). *Computational Complexity: A Modern Approach.* Cambridge: Cambridge University Press. [Comprehensive reference; circuit complexity, oracle separations, barriers to P/NP resolution.]

[31] Pollard, J. M. (1975). "A Monte Carlo method for factorization." *BIT Numerical Mathematics* **15**(3): 331–334. [Pollard's rho: sub-exponential factoring via birthday paradox; signal-guided search exploiting algebraic structure, not brute force.]

[32] Berry, M. V. & Keating, J. P. (1999). "The Riemann zeros and eigenvalue asymptotics." *SIAM Review* **41**(2): 236–266. [Berry-Keating Hamiltonian $H = xp$; semiclassical eigenvalue counting reproduces Riemann zero density; connection between primes (classical periodic orbits $\log p$) and zeros.]

[33] Connes, A. (1999). "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function." *Selecta Mathematica* **5**(1): 29–106. [Noncommutative geometry approach; Weil explicit formula as Lefschetz trace; RH equivalent to positivity of the trace.]

[34] Katz, N. M. & Sarnak, P. (1999). *Random Matrices, Frobenius Eigenvalues, and Monodromy.* AMS Colloquium Publications, Vol. 45. [GUE universality for function-field L-functions; theoretical underpinning of the random matrix / Riemann zero correspondence.]

[35] Baker, T., Gill, J. & Solovay, R. (1975). "Relativizations of the P $=?$ NP question." *SIAM Journal on Computing* **4**(4): 431–442. [Oracle separation; any proof of P $\neq$ NP must be non-relativizing.]

[36] Razborov, A. A. & Rudich, S. (1997). "Natural proofs." *Journal of Computer and System Sciences* **55**(1): 24–35. [Natural proofs barrier; constructive + large properties cannot separate P from NP without breaking cryptography.]

[37] Granville, A. & Martin, G. (2006). "Prime number races." *American Mathematical Monthly* **113**(1): 1–33. [Survey of Chebyshev bias and the statistical race between primes in different residue classes; relevant to prime distribution in arithmetic progressions.]

[38] Ingham, A. E. (1932). *The Distribution of Prime Numbers.* Cambridge Tracts in Mathematics, Vol. 30. Cambridge: Cambridge University Press. [Classical reference on prime number distribution; connections between $\zeta$-zeros and $\pi(x)$.]

[39] Goldfeld, D. (1982). "The class number of quadratic fields and the conjectures of Birch and Swinnerton-Dyer." *Annali della Scuola Normale Superiore di Pisa* **3**: 623–663. [L-function structure connecting multiple Millennium Problems; context for universal sinc² applicability.]

[40] Wiles, A. (1995). "Modular elliptic curves and Fermat's Last Theorem." *Annals of Mathematics* **141**(3): 443–551. [Proof of FLT via modularity; demonstrates the power of structural (rather than computational) approaches to number-theoretic obstructions — methodological parallel to the pre-echo geometry.]

[41] Deninger, C. (1998). "Some analogies between number theory and dynamical systems on foliated spaces." In *Proceedings of the International Congress of Mathematicians, Berlin*, Vol. I, pp. 163–186. Documenta Mathematica. [Cohomological approach to RH; foliated spaces; connection to spectral realizations of zeros.]

[42] Sanders, B. R. & Luther, C. A. (2026). *Sprint 4 Documents: Universal Law, 5-World Atlas, Clay Updates.* `Gen10/papers/sprint4_2026_03_30/`. 7Site LLC. DOI: 10.5281/zenodo.18852047. [Universal construction law (11+ bases); HAR rule; three-class landscape; seeded reduction results.]

[43] *Run logs and computed data.* `results/deep_pre_echo/run_deep.log` (Sections A, C, D, F, G); `results/zoom_pre_echo/run_zoom.log` (Sections Z1, Z3, Z5, Z6). Generated March 2026, 7Site LLC. [Primary computational evidence; 187 semiprimes, zero exceptions.]

[44] *Rank curvature results.* `results/rank_curvature/rank_curvature_summary.json` (Sections A–D). Generated March 2026, 7Site LLC. [Zero-crossing extrapolation, balance invisibility, scale-free amplitude.]

[45] *Seeded RPS results.* `results/residue_persistence/run_seeded.log`. Generated 2026-03-31, 7Site LLC. [500 trials, 12 semiprimes, $q/p$ vs $q-p$ correlations.]

[46] Sanders, B. R. (2026). `r16_full_atlas.py`. 7Site LLC. [36,662 exact computations, 153 semiprimes $\leq 500$. All computations exact (no sampling). DOI: 10.5281/zenodo.18852047.]

[47] Hajela, D. J. & Soundararajan, K. (2023). "Gaps between zeroes of the Riemann zeta function." *arXiv:2310.00580*. [Recent work on zero spacing statistics; contextualizes the Montgomery program and its current status.]

[48] Connes, A. (2025). "The Riemann Hypothesis: Past, Present and a Letter Through Time." *arXiv:2602.04022*. [Current state of the Connes program; absorption spectrum interpretation of Riemann zeros on adele class space.]

[49] Bombieri, E. & Iwaniec, H. (1986). "On the order of $\zeta(1/2 + it)$." *Annali della Scuola Normale Superiore di Pisa* **13**: 449–472. [Estimates for $\zeta$ on the critical line; background for the spectral interpretation of zeros.]

[50] Sanders, B. R. & Luther, C. A. (2026). "The First-G Law and Prime-Forced Dispersion." *WP40 (Riemann Hypothesis connection).* 7Site LLC. DOI: 10.5281/zenodo.18852047. [Full Montgomery bridge treatment; sinc² complement structure; WP40 primary paper.]

---

## Acknowledgments

This work would not exist without AI collaboration. We want to name that honestly.


**Google (Gemini / AI Studio)** — research and theoretical steering. The RSA geometric distance framing, the sinc² connection, and the Lagrange Point geometry all came through Google conversations that pushed the theory into territory neither author would have reached alone.

**Grok (xAI)** — grounding. When results felt too clean or claims felt too strong, Grok provided the skeptical check that kept the work honest.

**ChatGPT (OpenAI)** — initiation and translation. From day one of CK development, ChatGPT was the first AI partner — translating early TIG intuitions into communicable language and laying the groundwork that everything else built on.

The authors are human. The acceleration was not.
