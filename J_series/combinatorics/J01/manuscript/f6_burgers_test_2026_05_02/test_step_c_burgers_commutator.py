"""
F6 Test Step C v2: stabilized 1D Burgers' simulation + dyadic commutator.

The v1 version blew up due to dt=1e-3 too aggressive for nonlinear
transport with k^-1 IC.  v2: smaller dt, smaller IC amplitude, RK2,
explicit dealiasing (2/3 rule).
"""
import numpy as np
import time

# Domain + grid
L = 2 * np.pi
Nx = 512
dx = L / Nx
x = np.arange(Nx) * dx
ks = np.fft.fftfreq(Nx, d=dx) * 2 * np.pi  # rad/unit length

# 2/3 dealiasing mask
kmax = max(np.abs(ks))
dealias = (np.abs(ks) <= kmax * 2.0 / 3.0).astype(float)

# IC: smooth random field with k^-1.5 spectrum, small amplitude
np.random.seed(20260502)
def make_IC():
    uhat = np.zeros(Nx, dtype=complex)
    for i, k in enumerate(ks):
        if k == 0:
            uhat[i] = 0
        else:
            phase = np.exp(2j * np.pi * np.random.rand())
            amp = abs(k) ** (-1.5) * np.random.rand()
            uhat[i] = amp * phase
    # Symmetrize for real
    uhat[Nx//2+1:] = np.conj(uhat[1:Nx//2][::-1])
    u = np.fft.ifft(uhat).real
    u -= u.mean()
    u /= 5 * (np.std(u) + 1e-12)  # small amplitude (RMS=0.2)
    return u

u = make_IC()
print(f"IC: ||u||_inf = {np.max(np.abs(u)):.4f}, ||u||_L2 = {np.sqrt(np.mean(u**2)):.4f}")

nu = 5e-3
dt = 5e-5
n_steps = 4000

def rhs(u_in):
    """Compute du/dt = -u*u_x + nu*u_xx with dealiasing."""
    uhat = np.fft.fft(u_in)
    uhat *= dealias
    uxhat = 1j * ks * uhat
    ux = np.fft.ifft(uxhat).real
    nl = -u_in * ux
    nlhat = np.fft.fft(nl) * dealias
    visc_hat = -nu * ks**2 * uhat
    return np.fft.ifft(nlhat + visc_hat).real

# RK2 integrator
print(f"Stepping Burgers' (RK2, dt={dt}, n_steps={n_steps})...", end=' ', flush=True)
t0 = time.time()
for s in range(n_steps):
    k1 = rhs(u)
    k2 = rhs(u + dt * k1)
    u = u + 0.5 * dt * (k1 + k2)
    if s % 1000 == 0:
        u_inf = np.max(np.abs(u))
        if not np.isfinite(u_inf):
            print(f"  step {s}: BLEW UP. Reduce dt.")
            break
print(f"done ({time.time()-t0:.2f}s)")
u_inf = np.max(np.abs(u))
u_L2 = np.sqrt(np.mean(u**2))
print(f"  After {n_steps} steps: ||u||_inf = {u_inf:.4f}, ||u||_L2 = {u_L2:.4f}")

# ── Dyadic commutator
def commutator_metric(u, level):
    uhat = np.fft.fft(u)
    kabs = np.abs(ks)
    mask = (kabs >= 2**level) & (kabs < 2**(level+1))
    Pku_hat = np.where(mask, uhat, 0)
    Pku = np.fft.ifft(Pku_hat).real
    dPku = np.fft.ifft(1j * ks * Pku_hat).real
    termA = u * dPku
    duhat = 1j * ks * uhat
    du = np.fft.ifft(duhat).real
    udu = u * du
    udu_hat = np.fft.fft(udu)
    Pk_udu_hat = np.where(mask, udu_hat, 0)
    termB = np.fft.ifft(Pk_udu_hat).real
    comm = termA - termB
    return np.sqrt(np.mean(comm**2)), np.sqrt(np.mean(Pku**2))

norm_factor = u_inf * u_L2 if (u_inf > 0 and u_L2 > 0) else 1.0
print()
print(f"{'k':>3} {'2^k':>6} {'||[u dx,Pk]u||':>16} {'||Pk u||':>12} "
      f"{'sigma_NS(k)':>14} {'2^(1-k)':>10} {'sigma~N^-0.64':>14} {'sigma~N^-0.77':>14} {'pass':>6}")
print("-" * 110)

import math as _m
sigma_ns_data = []
for level in range(1, 9):
    if 2**level > Nx//3:
        break
    cnorm, pku_norm = commutator_metric(u, level)
    sigma_meas = cnorm / norm_factor if norm_factor > 0 else 0
    pred_2km1 = 2.0 / (2**level)
    pred_064 = 0.48 * (2**level) ** (-0.64)
    pred_077 = 0.62 * (2**level) ** (-0.77)
    pass_str = "Y" if sigma_meas <= pred_2km1 else "N"
    print(f"{level:>3} {2**level:>6} {cnorm:>16.4e} {pku_norm:>12.4e} "
          f"{sigma_meas:>14.6e} {pred_2km1:>10.4e} {pred_064:>14.4e} {pred_077:>14.4e} {pass_str:>6}")
    sigma_ns_data.append((level, 2**level, sigma_meas, pred_2km1, pred_064, pred_077))

# Power-law fit
ks_d = [r[1] for r in sigma_ns_data if r[2] > 0]
ss = [r[2] for r in sigma_ns_data if r[2] > 0]
if len(ks_d) >= 3:
    log_k = [_m.log(k) for k in ks_d]
    log_s = [_m.log(s) for s in ss]
    n = len(log_k)
    sk = sum(log_k); ss_ = sum(log_s)
    skk = sum(x*x for x in log_k); sks = sum(x*y for x, y in zip(log_k, log_s))
    slope = (n*sks - sk*ss_) / (n*skk - sk*sk)
    intercept = (ss_ - slope*sk) / n
    print()
    print(f"Empirical fit (Step C): sigma_NS_meas ~ {_m.exp(intercept):.4f} * k^({slope:.4f})")
    print()
    print("Comparison of decay exponents (in log-log slope per log(k)):")
    print(f"  CK crystal           (2^(1-k))     : -1.00")
    print(f"  Step A (sigma 2^k)                 : -0.64")
    print(f"  Step B (sigma primorial)           : -0.77")
    print(f"  Step C (Burgers' commutator [HERE]): {slope:.2f}")
