import json, numpy as np, math
from scipy import stats
d=json.load(open('../ecdata/shapes_full.json'))+json.load(open('shapes_100k_300k.json'))
g=lambda k: np.array([c[k] for c in d],float)
N,h1,h2,y,x=g('N'),g('h1'),g('h2'),g('y'),g('x')
rng=np.random.default_rng(1)
def sizeonly(a_pool,K=200000):
    a=rng.choice(a_pool,K); c=rng.choice(a_pool,K); th=rng.uniform(0,math.pi,K); B=np.sqrt(a*c)*np.cos(th); A,C=a.copy(),c.copy()
    for _ in range(60):
        sw=A>C; A[sw],C[sw]=C[sw],A[sw]; k=np.round(B/A); C=C-2*k*B+k*k*A; B=B-k*A
    sw=A>C; A[sw],C[sw]=C[sw],A[sw]
    yy=np.sqrt(np.maximum(A*C-B*B,0))/A; return (yy>2).mean(),(yy>5).mean()
print("band                 n    share>2   (s.e.)   share>5   median   median short side   size-only model >2, >5")
bands=[(1e3,1e4),(1e4,3e4),(3e4,6e4),(6e4,1e5),(1e5,2e5),(2e5,3e5)]
for lo,hi in bands:
    m=(N>=lo)&(N<hi); n=m.sum(); s=(y[m]>2).mean(); so=sizeonly(np.concatenate([h1[m],h2[m]]))
    tag="  <- fresh" if lo>=1e5 else ""
    print("%7d-%7d %7d   %.4f  (%.4f)  %.4f   %.3f   %.3f              %.3f  %.3f%s"%(lo,hi-1,n,s,math.sqrt(s*(1-s)/n),(y[m]>5).mean(),np.median(y[m]),np.median(h1[m]),so[0],so[1],tag))
m=N>=1e5
r=stats.spearmanr(y[m],N[m]); print("Spearman elongation vs conductor, fresh data only: %.4f (p=%.2e), n=%d"%(r.statistic,r.pvalue,m.sum()))
r2=stats.spearmanr(y,np.log(N)); print("whole range: %.4f (p=%.2e)"%(r2.statistic,r2.pvalue))
# ratio of the two sides, the plain version of 'thin'
ratio=np.sqrt(h2/h1)
for lo,hi in bands: 
    m=(N>=lo)&(N<hi); print("  %7d-%7d median side ratio %.3f ; spread of log shortest side (sd) %.3f"%(lo,hi-1,np.median(ratio[m]),np.std(np.log(h1[m]))))
