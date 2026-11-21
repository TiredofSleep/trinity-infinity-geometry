import json, numpy as np, math
d=json.load(open('../ecdata/shapes_full.json'))+json.load(open('../ec2/shapes_100k_300k.json'))+json.load(open('shapes_300k_500k.json'))
N=np.array([c['N'] for c in d],float); y=np.array([c['y'] for c in d]); x=np.array([c['x'] for c in d]); tors=np.array([c['tors'] for c in d])
dens=math.pi/(4*y)          # discs of radius half the shortest side, one per lattice point
rng=np.random.default_rng(0); M=10**6; xs=np.sin(rng.uniform(0,math.pi/6,M)); ys=np.sqrt(1-xs**2)/rng.uniform(0,1,M); dn=math.pi/(4*ys)
print("packing density = pi/(4 x elongation). best possible (hexagonal) %.4f ; square %.4f ; elongation 2 -> %.4f"%(math.pi/(2*math.sqrt(3)),math.pi/4,math.pi/8))
print("%-26s mean density  median   share above 0.85 (near-hexagonal)"%"")
print("%-26s %.4f       %.4f   %.4f"%("random shapes (null)",dn.mean(),np.median(dn),(dn>0.85).mean()))
for lab,m in (("all rank-2 curves",np.ones(len(y),bool)),("no closing wheels",tors==''),("order 2",tors=='2'),("order 3",tors=='3'),("order 4",tors=='4'),("two of order 2",tors=='2,2')):
    print("%-26s %.4f       %.4f   %.4f   n=%d"%(lab,dens[m].mean(),np.median(dens[m]),(dens[m]>0.85).mean(),m.sum()))
print("\nmean density by conductor band, torsion-free:",[round(float(dens[(N>=lo)&(N<hi)&(tors=='')].mean()),4) for lo,hi in [(1e3,1e4),(1e4,3e4),(3e4,6e4),(6e4,1e5),(1e5,2e5),(2e5,3e5),(3e5,4e5),(4e5,5e5)]])
i=int(np.argmax(dens)); print("densest lattice in the sample: conductor %d, density %.5f (x=%.4f, y=%.4f)"%(N[i],dens[i],x[i],y[i]))
