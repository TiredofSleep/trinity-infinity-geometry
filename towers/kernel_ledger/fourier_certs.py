"""fourier_certs.py -- certificates for vanishing minors of the n-point DFT (kernel_ledger, Round K3').
F[R, C] = (w^(t f)), rows = times R, columns = frequencies C.
class_pigeonhole(n, R, C): some subgroup K (times) and some class b of its annihilator K-perp (frequencies) with
  |C cap (b + K-perp)| > number of cosets of K that meet R. Then a vector supported on that class can be made to
  vanish on every coset meeting R, and w^(kf) is constant on the class, so it is in the kernel. Sound by construction.
Tried in both orientations (det F[R, C] = det F[C, R]^T, F symmetric). Prints nothing on import."""
def divisors(n): return [d for d in range(1, n + 1) if n % d == 0]
def class_pigeonhole(n, R, C):
    for d in divisors(n):
        K = range(0, n, d)                                   # dZ_n
        Kp = [f for f in range(n) if all((k * f) % n == 0 for k in K)]
        cos = {t % d for t in R}                              # cosets of dZ_n are residues mod d
        m = len(Kp) and n // len(Kp)                          # K-perp = mZ_n with m = n / |K-perp|
        classes = {}
        for f in C: classes[f % m] = classes.get(f % m, 0) + 1
        if max(classes.values()) > len(cos): return True
    return False
def certified(n, R, C): return class_pigeonhole(n, R, C) or class_pigeonhole(n, C, R)
