import json, numpy as np, math, glob, re
from collections import Counter
size=Counter()
for fn in glob.glob('../ecdata/allgens.*')+glob.glob('../ec2/allgens.*')+glob.glob('allgens.*'):
    for line in open(fn):
        t=line.split(' ',3)
        if len(t)>=3: size[(int(t[0]),t[1])]+=1
d=json.load(open('../ecdata/shapes_full.json'))+json.load(open('../ec2/shapes_100k_300k.json'))+json.load(open('shapes_300k_500k.json'))
N=np.array([c['N'] for c in d],float); y=np.array([c['y'] for c in d]); tors=np.array([c['tors'] for c in d])
cs=np.array([size[(int(c['N']),c['cls'])] for c in d]); dens=math.pi/(4*y); tf=tors==''
a=tf&(cs==1); b=tf&(cs>=2)
se=math.sqrt(dens[a].var()/a.sum()+dens[b].var()/b.sum())
print("torsion-free rank-2 optimal curves: class size 1: n=%d mean density %.4f ; class size >=2: n=%d mean density %.4f"%(a.sum(),dens[a].mean(),b.sum(),dens[b].mean()))
print("difference %.4f, s.e. %.4f, = %.1f standard errors"%(dens[b].mean()-dens[a].mean(),se,(dens[b].mean()-dens[a].mean())/se))
for k in (1,2,3,4):
    m=tf&((cs==k) if k<4 else (cs>=4))
    if m.sum(): print("  class size %s: n=%6d  mean density %.4f  thin share %.4f"%(k if k<4 else '4+',m.sum(),dens[m].mean(),(y[m]>2).mean()))
print("with torsion, by class size:",[(k,int(((~tf)&(cs==k)).sum()),round(float(dens[(~tf)&(cs==k)].mean()),4)) for k in (2,3,4,6,8) if ((~tf)&(cs==k)).sum()>30])
bands=[(1e3,1e4),(1e4,3e4),(3e4,6e4),(6e4,1e5),(1e5,2e5),(2e5,3e5),(3e5,4e5),(4e5,5e5)]
print("trend, class size 1 :",[round(float(dens[a&(N>=lo)&(N<hi)].mean()),4) for lo,hi in bands])
print("trend, class size>=2:",[round(float(dens[b&(N>=lo)&(N<hi)].mean()),4) for lo,hi in bands])
