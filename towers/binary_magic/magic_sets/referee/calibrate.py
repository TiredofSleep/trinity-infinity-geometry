import sys
import numpy as np
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from gram import analyse
from verify_sets import graph_star
from core import mat

square = [['XI', 'IX', 'XX'], ['IZ', 'ZI', 'ZZ'], ['XZ', 'ZX', 'YY'],
          ['XI', 'IZ', 'XZ'], ['IX', 'ZI', 'ZX'], ['XX', 'ZZ', 'YY']]
print('square    ', analyse('square', square, n_actual=2))
pent = graph_star(3, [(0, 1), (1, 2), (0, 2)])
print('pentagram ', analyse('pentagram', pent, n_actual=3))
# pentagram padded to 5 qubits by I's: must still need only 3
pad = [[s + 'II' for s in c] for c in pent]
print('pent+II   ', analyse('pent+II', pad, n_actual=5))
# 6-qubit graph star: refine C0 into its negative ID subset, keep the 4 matching local contexts
g6 = graph_star(6, [(0, 1), (1, 2), (0, 2), (0, 3), (3, 4), (4, 5), (0, 5)])
Ca = ['XXXXXX', 'YYXXXX', 'XYYXXX', 'YXYXXX']
loc = [c for c in g6[1:] if c[-1] in Ca]
sub = [Ca] + loc
obs = sorted({o for c in sub for o in c})
print('6q sub-proof: %d observables, %d contexts' % (len(obs), len(sub)), obs)
print('6q sub     ', analyse('6q-sub', sub, n_actual=6))
# signs of the sub-proof by explicit matrices
I = np.eye(64)
for c in sub:
    P = np.eye(64, dtype=complex)
    for o in c: P = P @ mat(o)
    print('   ', c, '+I' if np.allclose(P, I) else ('-I' if np.allclose(P, -I) else '??'))
