"""Where is sinc^2 concave on (0,1)?  (J24 Remark 7.4 says: concave near t = 1/2.)"""
import math
import sympy as sp
s = lambda t: (math.sin(math.pi*t)/(math.pi*t))**2
h = 1e-4
for t in [0.3, 0.4, 0.45, 0.5, 0.55, 0.6]:
    d2 = (s(t+h) - 2*s(t) + s(t-h))/h**2
    print(f"t={t:.2f}  finite-difference (sinc^2)'' = {d2:+.5f}  ({'convex' if d2 > 0 else 'concave'})")
t = sp.symbols('t')
g2 = sp.diff((sp.sin(sp.pi*t)/(sp.pi*t))**2, t, 2)
root = sp.nsolve(g2, t, 0.415)
print("inflection point of sinc^2 in (0,1): t =", sp.N(root, 10))
