"""
F6 Test Step A: compute sigma(N=2^k) for k=1..6 and check vs 2/2^k bound.

WP101 proves sigma(N) <= 2^omega(N)/N for SQUAREFREE N.
For N = 2^k (k>=2), N is NOT squarefree.  CK's crystal conjectures
sigma_NS(k) <= sigma(N=2^k) <= 2/2^k.  This script tests whether
sigma(2^k) actually satisfies this bound, which is the prerequisite
for the cyclotomic-NS analogy to be empirically defensible.
"""
import math
import sys
import time

def compute_sigma(N):
    """Non-associativity rate of the binary CL on Z/NZ."""
    harmony = N - 1
    dis = [[abs((a+b) % N - (a*b) % N) for b in range(N)] for a in range(N)]
    table = [[0]*N for _ in range(N)]
    for a in range(N):
        for b in range(N):
            if a == harmony or b == harmony:
                table[a][b] = harmony
            elif a == 0 or b == 0:
                table[a][b] = 0
            elif dis[a][b] == 0:
                table[a][b] = (a + b) % N
            else:
                table[a][b] = harmony
    violations = 0
    total = N ** 3
    for a in range(N):
        for b in range(N):
            ab = table[a][b]
            for c in range(N):
                lhs = table[ab][c]
                rhs = table[a][table[b][c]]
                if lhs != rhs:
                    violations += 1
    return violations / total

def count_dis_zero(N):
    c = 0
    for a in range(N):
        for b in range(N):
            if (a+b) % N == (a*b) % N:
                c += 1
    return c

print("=" * 80)
print("F6 Test Step A: sigma(N = 2^k) -- does CK's 2^(1-k) bound hold for prime powers?")
print("=" * 80)
print(f"\n{'k':>3} {'N=2^k':>6} {'sigma(N)':>12} {'2/N':>10} {'1/N':>10} "
      f"{'DIS=0':>6} {'pass 2/N':>10} {'time':>8}")
print("-" * 80)

results = []
for k in range(1, 8):
    N = 2 ** k
    if k >= 7:
        # 2^7 = 128, triple loop = 2.1M ops; 2^8 = 256, 16.8M; 2^9 prohibitive
        # Stop at k=8 (N=256) at most.
        if k > 8:
            print(f"  (k={k}: N=256, skipping triple loop - >16M ops)")
            continue
    t0 = time.time()
    sigma = compute_sigma(N)
    elapsed = time.time() - t0
    dis0 = count_dis_zero(N)
    bound_2N = 2.0 / N
    pass_str = "PASS" if sigma <= bound_2N else "FAIL"
    print(f"{k:>3} {N:>6} {sigma:>12.6f} {bound_2N:>10.6f} {1/N:>10.6f} "
          f"{dis0:>6} {pass_str:>10} {elapsed:>7.2f}s")
    results.append((k, N, sigma, bound_2N, dis0))

print()
print("INTERPRETATION:")
print("  - For squarefree N, WP101 proves sigma(N) <= 2^omega(N)/N (omega = # distinct primes)")
print("  - For N = 2^k (k>=2), N is NOT squarefree.  WP101 doesn't directly cover this case.")
print("  - If sigma(2^k) <= 2/2^k holds empirically, the cyclotomic-NS analogy is")
print("    EMPIRICALLY supported as far as the arithmetic side goes.")
print("  - If the bound FAILS, the analogy needs refinement: maybe sigma_NS(k)")
print("    corresponds to sigma at a different N (e.g. squarefree primorial near 2^k),")
print("    or the bound is something other than 2/N.")
print()

# Fit a power law sigma(2^k) ~ C * 2^(-alpha k)
import math as _m
if len(results) >= 3:
    log_sigmas = [_m.log(r[2]) for r in results if r[2] > 0]
    ks = [r[0] for r in results if r[2] > 0]
    if len(log_sigmas) >= 2:
        n = len(ks)
        sum_k = sum(ks); sum_y = sum(log_sigmas)
        sum_kk = sum(k*k for k in ks); sum_ky = sum(k*y for k, y in zip(ks, log_sigmas))
        slope = (n*sum_ky - sum_k*sum_y) / (n*sum_kk - sum_k*sum_k)
        intercept = (sum_y - slope*sum_k) / n
        print(f"Power-law fit: log(sigma) = {slope:.4f}*k + {intercept:.4f}")
        print(f"  => sigma(2^k) ~ {_m.exp(intercept):.4f} * 2^({slope/_m.log(2):.4f}*k)")
        print(f"  Predicted exponent: -1 (i.e. sigma ~ 2/2^k)")
        print(f"  Empirical exponent (per log2):  {slope/_m.log(2):.4f}")

