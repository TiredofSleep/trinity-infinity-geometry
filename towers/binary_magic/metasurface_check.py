"""
metasurface_check.py — bit planes of magic squares as 1-bit coding-metasurface tiles.

Coding metasurface (Cui et al. 2014): cells are '0' (reflection phase 0) or '1' (phase pi).
A periodic array of a 4x4 tile reflects only into diffraction orders (p, q), p, q in {0,1,2,3};
amplitude F(p,q) = sum_ij (-1)^B_ij * i^-(p*i + q*j)  (discrete Fourier transform of the tile).
(0,0) = straight back (specular). p = 0 or q = 0 = the two principal planes.
"""
import json, random
import numpy as np
from collections import Counter

squares = [np.array(s["square"]) for s in json.load(open("squares_4x4.json"))]
def far_field(B):
    D = 1 - 2 * B
    return np.abs(np.fft.fft2(D)) ** 2
def stats(F):
    tot = F.sum()
    spec = F[0, 0] / tot
    axes = (F[0, :].sum() + F[:, 0].sum() - F[0, 0]) / tot
    beams = int((F > 1e-9 * tot).sum())
    return spec, axes, beams

out = Counter(); worst_axis = 0.0
for A in squares:
    for k in range(4):
        spec, axes, beams = stats(far_field((A >> k) & 1))
        worst_axis = max(worst_axis, axes)
        out[beams] += 1
print(f"magic-square bit planes (3520 tiles): energy on specular + both axes, worst case = {worst_axis:.2e}")
print("  number of reflected beams per tile:", dict(sorted(out.items())))

random.seed(3)
rand_axes, rand_beams = [], Counter()
for _ in range(20000):
    B = np.array([1] * 8 + [0] * 8); np.random.shuffle(B); B = B.reshape(4, 4)
    spec, axes, beams = stats(far_field(B))
    rand_axes.append(axes); rand_beams[beams] += 1
print(f"random half-on tiles (20000): mean energy on specular + axes = {np.mean(rand_axes):.2f}, "
      f"tiles with none = {sum(a < 1e-9 for a in rand_axes)}")
print("  number of reflected beams per tile:", dict(sorted(rand_beams.items())))
