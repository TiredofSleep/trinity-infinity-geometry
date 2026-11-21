import json, numpy as np, math
from scipy import stats
d=json.load(open('../ecdata/shapes_full.json'))+json.load(open('../ec2/shapes_100k_300k.json'))+json.load(open('shapes_300k_500k.json'))
g=lambda k: np.array([c[k] for c in d],float)
N,h1,h2,y=g('N'),g('h1'),g('h2'),g('y'); tors=np.array([c['tors'] for c in d])
bands=[(1e3,1e4),(1e4,3e4),(3e4,6e4),(6e4,1e5),(1e5,2e5),(2e5,3e5),(3e5,4e5),(4e5,5e5)]
print("band               n   share>2  (s.e.)   2<e<=5   share>5   median")
for lo,hi in bands:
    m=(N>=lo)&(N<hi); n=m.sum(); s=(y[m]>2).mean()
    print("%7d-%7d %6d  %.4f (%.4f)  %.4f   %.4f   %.3f%s"%(lo,hi-1,n,s,math.sqrt(s*(1-s)/n),((y[m]>2)&(y[m]<=5)).mean(),(y[m]>5).mean(),np.median(y[m]),"  <- fresh" if lo>=3e5 else ""))
# the tail: which side is unusual?
print("\ncurves with elongation > 5, relative to their band's medians:")
for lo,hi in [(1e4,1e5),(1e5,3e5),(3e5,5e5)]:
    m=(N>=lo)&(N<hi); t=m&(y>5); mid=m&(y>2)&(y<=5)
    print("  %7d-%7d  n=%4d  short side = %.2f x typical, long side = %.2f x typical   | merely thin (2-5): short %.2f x, long %.2f x"%(lo,hi-1,t.sum(),np.median(h1[t])/np.median(h1[m]),np.median(h2[t])/np.median(h2[m]),np.median(h1[mid])/np.median(h1[m]),np.median(h2[mid])/np.median(h2[m])))
nt=tors!=''
print("\nshare>5 with torsion %.4f (n=%d) vs without %.4f ; share>2 with torsion %.4f vs without %.4f"%((y[nt]>5).mean(),nt.sum(),(y[~nt]>5).mean(),(y[nt]>2).mean(),(y[~nt]>2).mean()))
# shortest side against log conductor: floor?
for lo,hi in bands: 
    m=(N>=lo)&(N<hi); print("  band %7d: 1st percentile of shortest side %.4f ; median %.3f ; median/ln N %.4f"%(lo,np.percentile(h1[m],1),np.median(h1[m]),np.median(h1[m])/math.log(np.median(N[m]))))
