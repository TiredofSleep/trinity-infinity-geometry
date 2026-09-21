#!/usr/bin/env python3
"""
cu_depletion_KILLED_STRAND.py  --  A GRAVEYARD ARTIFACT. READ THIS DOCSTRING.

This is the Navier-Stokes "cancelled fraction" harness from the session. It is
included as an EXAMPLE OF THE CHECK WORKING, and a KILLED claim to NOT resurrect.

THE STORY (for Claude Code):
  The session hypothesized that the Leray projection removes a FIXED fraction 1/3
  of the nonlinear inertial term pointwise -- i.e. c(u) = |grad p|^2 / |N|^2 = 1/3
  on average, tying it to the tetrahedral 1/3.

  WHEN COMPUTED HONESTLY (below), THIS WAS FALSE:
    - the pointwise cancelled fraction is FIELD-DEPENDENT and can exceed 1
      (impossible for a real projection fraction);
    - it does NOT average 1/3; the spectral energy fraction drifted toward ~0.1
      and DEPENDED on resolution.
  REASON: the pressure is NONLOCAL (inverse Laplacian). "Project N(x) onto k
  pointwise" is a LOCAL operation; the real Leray projector is not. The local 1/3
  (a random-vector-onto-one-axis average) does NOT survive contact with the
  nonlocal operator. This is the SAME nonlocality wall that makes NS hard.

  THE REAL 1/3 (in the papers) is cos^2(1,1,1) = 1/(N-1) at N=4 -- a GEOMETRIC
  quantity from the simplex/cube, NOT this fluid quantity. They are DIFFERENT 1/3s
  that happen to share a value. Do not weld them (that was tested and killed too).

DO NOT: resurrect "c = 1/3 universal", or claim this fluid 1/3 equals the geometric
1/3. Both are in the graveyard (what_is_tig_deep.md section 8, items 1 and 2).

WHAT SURVIVES: the harness itself computes the (field-dependent) cancelled fraction
correctly and could, on real turbulence data (e.g. Johns Hopkins Turbulence
Database), be used to study how c(u) actually varies with |grad u|. That is a real
but modest measurement, NOT the original claim. If extended, frame it as "how does
the cancelled fraction vary" -- an open measurement -- never as "it is 1/3".
"""
import numpy as np

def wavenumbers(n):
    k = np.fft.fftfreq(n, d=1.0/n)
    kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')
    k2 = kx**2 + ky**2 + kz**2
    k2[0,0,0] = 1.0
    return kx, ky, kz, k2

def make_solenoidal(n, seed=1):
    """random divergence-free field with a rough Kolmogorov-ish spectrum"""
    rng = np.random.default_rng(seed)
    kx, ky, kz, k2 = wavenumbers(n)
    kmag = np.sqrt(k2)
    amp = np.where((kmag > 0) & (kmag <= n//3), kmag**(-5/6 - 1), 0.0)
    uh = np.array([amp*np.exp(2j*np.pi*rng.random(k2.shape)) for _ in range(3)])
    kv = np.stack([kx, ky, kz])
    kdu = sum(kv[i]*uh[i] for i in range(3))
    for i in range(3):
        uh[i] -= kv[i]*kdu/k2                        # Leray project (make div-free)
    u = np.array([np.fft.ifftn(uh[i]).real for i in range(3)])
    return u

def cancelled_energy_fraction(u):
    """spectral energy fraction of the nonlinear term removed by the Leray projection.
    (This is the honest, global version. It is NOT 1/3 and depends on the field.)"""
    n = u.shape[1]
    kx, ky, kz, k2 = wavenumbers(n)
    uh = [np.fft.fftn(u[i]) for i in range(3)]
    A = np.empty(u.shape[1:] + (3,3))
    for i in range(3):
        for j, kk in enumerate([kx, ky, kz]):
            A[..., i, j] = np.fft.ifftn(1j*kk*uh[i]).real
    N = np.array([u[0]*A[...,i,0] + u[1]*A[...,i,1] + u[2]*A[...,i,2] for i in range(3)])
    Nh = np.stack([np.fft.fftn(N[i]) for i in range(3)])
    kv = np.stack([kx, ky, kz])
    kdN = kv[0]*Nh[0] + kv[1]*Nh[1] + kv[2]*Nh[2]
    gph = kv*(kdN/k2)[None]                          # k-parallel (cancelled) part
    E_tot = np.sum(np.abs(Nh)**2)
    E_can = np.sum(np.abs(gph)**2)
    return E_can/E_tot

if __name__ == "__main__":
    print("Demonstrating the KILLED claim: cancelled fraction is NOT a fixed 1/3.")
    print(f"{'grid':>6} {'cancelled energy fraction':>28}")
    for n in [24, 32, 48]:
        u = make_solenoidal(n)
        f = cancelled_energy_fraction(u)
        print(f"{n:>4}^3 {f:>28.4f}")
    print("\n-> field-dependent, resolution-dependent, NOT 1/3. Claim falsified.")
    print("   The geometric 1/3 (papers) is cos^2(1,1,1); a DIFFERENT quantity.")
