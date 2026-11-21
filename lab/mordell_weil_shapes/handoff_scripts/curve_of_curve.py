import json, numpy as np, math, glob
from collections import Counter
from scipy import stats
size=Counter()
for fn in glob.glob('../ecdata/allgens.*')+glob.glob('../ec2/allgens.*')+glob.glob('allgens.*'):
    for line in open(fn):
        t=line.split(' ',3)
        if len(t)>=3: size[(int(t[0]),t[1])]+=1
P=json.load(open('periods.json'))
d=json.load(open('../ecdata/shapes_full.json'))+json.load(open('../ec2/shapes_100k_300k.json'))+json.load(open('shapes_300k_500k.json'))
N=np.array([c['N'] for c in d],float); y=np.array([c['y'] for c in d]); tors=np.array([c['tors'] for c in d]); cs=np.array([size[(int(c['N']),c['cls'])] for c in d])
pp=np.array([P[str(c['N'])+c['cls']][:3] for c in d]); sg=pp[:,0]; tre=pp[:,1]; tim=pp[:,2]
dens=math.pi/(4*y); L=np.log(N); lf=(tors=='')&(cs==1)
print("check: Re tau by sign:",{int(s):np.round(np.unique(np.round(tre[sg==s],3))[:4],3).tolist() for s in (-1,1)})
a=lf&(sg>0); b=lf&(sg<0); se=math.sqrt(dens[a].var()/a.sum()+dens[b].var()/b.sum())
print("\nA1  loop-free curves: with a real loop (disc>0) n=%d density %.4f ; without (disc<0) n=%d density %.4f"%(a.sum(),dens[a].mean(),b.sum(),dens[b].mean()))
print("    difference %+.4f, s.e. %.4f, %.1f standard errors ; thin share %.4f vs %.4f"%(dens[a].mean()-dens[b].mean(),se,(dens[a].mean()-dens[b].mean())/se,(y[a]>2).mean(),(y[b]>2).mean()))
for lab,m in (("isogeny only",(tors=='')&(cs>=2)),("Z/2",tors=='2'),("Z/3",tors=='3'),("Z/4",tors=='4'),("Z/2xZ/2",tors=='2,2')):
    u=m&(sg>0); v=m&(sg<0)
    if u.sum()>20 and v.sum()>20: print("    %-13s disc>0: n=%6d %.4f   disc<0: n=%6d %.4f"%(lab,u.sum(),dens[u].mean(),v.sum(),dens[v].mean()))
    else: print("    %-13s disc>0: n=%d  disc<0: n=%d"%(lab,u.sum(),v.sum()))
print("\nB1  correlation of packing with the curve's own elongation Im tau (loop-free):")
for s,lab in ((1,"disc>0"),(-1,"disc<0")):
    m=lf&(sg==s); r=stats.spearmanr(dens[m],tim[m]).statistic; print("    %s: n=%d Spearman %+.4f (%.1f s.e.) ; median Im tau %.3f"%(lab,m.sum(),r,r*math.sqrt(m.sum()),np.median(tim[m])))
    q=np.quantile(tim[m],[0,.2,.4,.6,.8,1]); print("       density by fifths of Im tau:",[round(float(dens[m&(tim>=q[i])&(tim<=q[i+1])].mean()),4) for i in range(5)],"  Im tau cuts",np.round(q[1:5],2))
def slope(m):
    x=L[m]-L[m].mean(); bb=(x*dens[m]).sum()/(x*x).sum(); r=dens[m]-dens[m].mean()-bb*x; return bb,math.sqrt((r*r).sum()/(m.sum()-2)/(x*x).sum())
print("\nB2  conductor trend, loop-free: disc>0 slope %+.5f (se %.5f) ; disc<0 slope %+.5f (se %.5f)"%(*slope(a),*slope(b)))
print("    share of disc>0 by band:",[round(float((sg[lf&(N>=lo)&(N<hi)]>0).mean()),3) for lo,hi in [(1e3,1e4),(1e4,3e4),(3e4,6e4),(6e4,1e5),(1e5,2e5),(2e5,3e5),(3e5,4e5),(4e5,5e5)]])
# uniform measure cut off at elongation Y: mean density
rng=np.random.default_rng(0); M=2*10**6; xs=np.sin(rng.uniform(0,math.pi/6,M)); ys=np.sqrt(1-xs**2)/rng.uniform(0,1,M)
print("    uniform shapes cut off at elongation Y -> mean density:",{Y:round(float((math.pi/(4*ys[ys<=Y])).mean()),4) for Y in (1.5,2,2.5,3,4,6)})
