import json, numpy as np, math
d=json.load(open('../ecdata/shapes_full.json'))+json.load(open('../ec2/shapes_100k_300k.json'))+json.load(open('shapes_300k_500k.json'))
N=np.array([c['N'] for c in d],float); y=np.array([c['y'] for c in d]); x=np.array([c['x'] for c in d]); tors=np.array([c['tors'] for c in d])
dens=math.pi/(4*y); tf=tors==''
bands=[(1e3,1e4),(1e4,3e4),(3e4,6e4),(6e4,1e5),(1e5,2e5),(2e5,3e5),(3e5,4e5),(4e5,5e5)]
print("torsion-free curves. density percentiles by band, and share near the honeycomb")
print("band      lnN   mean    10th    25th    50th    75th    90th   share>0.85  share>0.89  mean x")
L=[];Mn=[]
for lo,hi in bands:
    m=(N>=lo)&(N<hi)&tf; q=np.percentile(dens[m],[10,25,50,75,90]); L.append(np.log(np.median(N[m]))); Mn.append(dens[m].mean())
    print("%7d  %.2f  %.4f  %.4f  %.4f  %.4f  %.4f  %.4f   %.4f      %.4f     %.4f"%(lo,L[-1],Mn[-1],*q,(dens[m]>0.85).mean(),(dens[m]>0.89).mean(),x[m].mean()))
L=np.array(L);Mn=np.array(Mn)
a,b=np.polyfit(L[1:],Mn[1:],1); print("\nstraight line in ln N (bands 2-8): slope %.4f per e-fold; reaches 0.9069 at ln N = %.0f (N ~ 10^%.0f)"%(a,(0.9069-b)/a,(0.9069-b)/a/math.log(10)))
# what limit does a saturating curve prefer?  dens = D - c*N^-beta, scan D
best=None
for D in np.arange(0.56,0.92,0.005):
    z=np.log(D-Mn[1:]); s,i=np.polyfit(L[1:],z,1); r=np.sum((z-(s*L[1:]+i))**2)
    if s<0 and (best is None or r<best[0]): best=(r,D,s)
print("saturating fits  D - c N^-beta: residual by limit D:")
for D in (0.57,0.60,0.65,0.70,0.80,0.9069):
    z=np.log(D-Mn[1:]); s,i=np.polyfit(L[1:],z,1); print("   limit %.4f: beta %.4f, rms residual %.5f"%(D,-s,math.sqrt(np.mean((np.exp(s*L[1:]+i)-(D-Mn[1:]))**2))))
