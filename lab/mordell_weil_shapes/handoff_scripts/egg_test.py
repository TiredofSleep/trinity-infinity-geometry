import json, numpy as np, math, glob, cypari2
from collections import Counter
from scipy import stats
size=Counter()
for fn in glob.glob('../ecdata/allgens.*')+glob.glob('../ec2/allgens.*')+glob.glob('allgens.*'):
    for line in open(fn):
        t=line.split(' ',3)
        if len(t)>=3: size[(int(t[0]),t[1])]+=1
P=json.load(open('periods.json')); G=json.load(open('egg.json'))
d=json.load(open('../ecdata/shapes_full.json'))+json.load(open('../ec2/shapes_100k_300k.json'))+json.load(open('shapes_300k_500k.json'))
key=[str(c['N'])+c['cls'] for c in d]
N=np.array([c['N'] for c in d],float); y=np.array([c['y'] for c in d]); h1=np.array([c['h1'] for c in d]); tors=np.array([c['tors'] for c in d]); cs=np.array([size[(int(c['N']),c['cls'])] for c in d])
sg=np.array([P[k][0] for k in key]); tim=np.array([P[k][2] for k in key]); dens=math.pi/(4*y)
egg=np.array([sum(G[k]) if k in G else -1 for k in key])
print("consistency: curves with positive discriminant %d, with three real roots %d"%((sg>0).sum(),(egg>=0).sum()))
lf=(tors=='')&(cs==1)&(sg>0)
a=lf&(egg>0); b=lf&(egg==0); se=math.sqrt(dens[a].var()/a.sum()+dens[b].var()/b.sum())
print("P1  points reach the egg: n=%d density %.4f thin %.4f | all on the open branch: n=%d density %.4f thin %.4f"%(a.sum(),dens[a].mean(),(y[a]>2).mean(),b.sum(),dens[b].mean(),(y[b]>2).mean()))
print("    difference %+.4f, s.e. %.4f, %.1f standard errors"%(dens[a].mean()-dens[b].mean(),se,(dens[a].mean()-dens[b].mean())/se))
for k,lab in ((0,"no generator on the egg"),(1,"one generator on the egg"),(2,"both on the egg")):
    m=lf&(egg==k); print("    %-26s n=%6d density %.4f  median shortest side %.3f"%(lab,m.sum(),dens[m].mean(),np.median(h1[m])))
m0=(tors=='')&(cs==1)&(sg<0); print("    for comparison, one-piece curves: n=%d density %.4f median shortest side %.3f"%(m0.sum(),dens[m0].mean(),np.median(h1[m0])))
print("P2  dependence on the curve's own shape (Spearman with Im tau):")
for lab,m in (("points reach the egg",a),("all on the open branch",b)):
    r=stats.spearmanr(dens[m],tim[m]).statistic; q=np.quantile(tim[m],[0,.2,.4,.6,.8,1])
    print("    %-24s %+.4f (%.1f s.e.)  density by fifths of Im tau: %s"%(lab,r,r*math.sqrt(m.sum()),[round(float(dens[m&(tim>=q[i])&(tim<=q[i+1])].mean()),4) for i in range(5)]))
print("    median Im tau: reach %.3f, do not reach %.3f"%(np.median(tim[a]),np.median(tim[b])))
# birth of a loop: multiples of a generator of 389a1 fill its real component evenly
pari=cypari2.Pari(); E=pari.ellinit([0,1,1,-2,0]); w1=float(E.omega()[0].real()); z=complex(pari.ellpointtoz(E,[0,0])).real
u=np.mod(np.arange(1,5001)*z/w1,1.0); print("\n389a1: 5000 multiples of one generator, position round the real curve: KS against even spacing p=%.2f ; largest gap %.5f (even would be %.5f)"%(stats.kstest(u,'uniform').pvalue,np.diff(np.sort(u)).max(),1/5000))
