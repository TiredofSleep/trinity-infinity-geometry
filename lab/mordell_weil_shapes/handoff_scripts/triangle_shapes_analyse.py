import json, numpy as np, math
from scipy import stats
d=json.load(open('shapes_full.json')); n=len(d)
g=lambda k: np.array([c[k] for c in d],float)
N,h1,h2,x,y,reg,ld=g('N'),g('h1'),g('h2'),g('x'),g('y'),g('reg'),g('logdisc')
ang=np.degrees(np.arctan2(y,x))
print("complete sample: %d rank-2 optimal curves, conductor 389 to %d"%(n,N.max()))
rng=np.random.default_rng(0); M=10**6
xs=np.sin(rng.uniform(0,math.pi/6,M)); ys=np.sqrt(1-xs**2)/rng.uniform(0,1,M)
print("                       measured   equal-shapes null")
for lab,e,m in (("median elongation",np.median(y),np.median(ys)),("share elongation>2",(y>2).mean(),(ys>2).mean()),("share elongation>5",(y>5).mean(),(ys>5).mean()),("median angle",np.median(ang),np.median(np.degrees(np.arctan2(ys,xs)))),("median |x|",np.median(x),np.median(xs))):
    print("%-22s %8.3f   %8.3f"%(lab,e,m))
print("\nby conductor band:  n   median elongation  share>2   median shortest side  median log-disc")
for lo,hi in ((0,1e3),(1e3,1e4),(1e4,3e4),(3e4,6e4),(6e4,1e5)):
    m=(N>=lo)&(N<hi); print("%6d-%6d %6d %10.3f %12.3f %14.3f %14.2f"%(lo,hi,m.sum(),np.median(y[m]),(y[m]>2).mean(),np.median(h1[m]),np.median(ld[m])))
# the boring explanation: a floor on the shortest side. Does elongation track h2/h1 only through sizes?
print("\nSpearman: elongation vs log N %.3f ; shortest side vs log-disc %.3f ; elongation vs regulator %.3f"%(stats.spearmanr(y,np.log(N)).statistic,stats.spearmanr(h1,ld).statistic,stats.spearmanr(y,reg).statistic))
# floor model: draw both squared lengths independently from the empirical law of the shortest-side pool, angle uniform -> reduce -> elongation
pool=np.concatenate([h1,h2]); K=200000
a=rng.choice(pool,K); c=rng.choice(pool,K); th=rng.uniform(0,math.pi,K); b=np.sqrt(a*c)*np.cos(th)
A,B,C=a.copy(),b.copy(),c.copy()
for _ in range(60):
    sw=A>C; A[sw],C[sw]=C[sw],A[sw]
    k=np.round(B/A); C=C-2*k*B+k*k*A; B=B-k*A
sw=A>C; A[sw],C[sw]=C[sw],A[sw]
ym=np.sqrt(np.maximum(A*C-B*B,0))/A; xm=np.abs(B)/A
print("\nsize-only model (two independent sizes from the data, random angle):")
print("  median elongation %.3f, share>2 %.3f, share>5 %.3f, median |x| %.3f"%(np.median(ym),(ym>2).mean(),(ym>5).mean(),np.median(xm)))
print("  KS against data: elongation p=%.2e, x p=%.2e"%(stats.ks_2samp(y,ym).pvalue,stats.ks_2samp(x,xm).pvalue))
print("x: share in fifths of [0,0.5]:",np.round(np.histogram(x,bins=5,range=(0,.5))[0]/n,3)," null:",np.round(np.histogram(xs,bins=5,range=(0,.5))[0]/M,3))
print("angle deciles:",np.round(np.percentile(ang,[10,25,50,75,90]),1))
