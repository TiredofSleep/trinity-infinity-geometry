import json, numpy as np, math, glob
from collections import Counter
size=Counter()
for fn in glob.glob('../ecdata/allgens.*')+glob.glob('../ec2/allgens.*')+glob.glob('allgens.*'):
    for line in open(fn):
        t=line.split(' ',3)
        if len(t)>=3: size[(int(t[0]),t[1])]+=1
d=json.load(open('../ecdata/shapes_full.json'))+json.load(open('../ec2/shapes_100k_300k.json'))+json.load(open('shapes_300k_500k.json'))
N=np.array([c['N'] for c in d],float); y=np.array([c['y'] for c in d]); tors=np.array([c['tors'] for c in d]); cs=np.array([size[(int(c['N']),c['cls'])] for c in d])
dens=math.pi/(4*y); L=np.log(N)
def slope(m):
    x=L[m]-L[m].mean(); b=(x*dens[m]).sum()/(x*x).sum(); r=dens[m]-dens[m].mean()-b*x; se=math.sqrt((r*r).sum()/(m.sum()-2)/(x*x).sum()); return b,se
groups=[("no loop at all",(tors=='')&(cs==1)),("isogeny only",(tors=='')&(cs>=2)),("Z/2",tors=='2'),("above 0.607: Z/3,Z/4,Z/6,Z/2xZ/2,Z/5,Z/8",np.isin(tors,['3','4','6','2,2','5','8','2,4'])),("  Z/3 alone",tors=='3'),("  Z/4 alone",tors=='4'),("  Z/2xZ/2 alone",tors=='2,2')]
print("%-44s n       mean     slope per e-fold   s.e.     slope/s.e."%"")
for lab,m in groups:
    b,se=slope(m); print("%-44s %6d  %.4f   %+.5f          %.5f   %+.1f"%(lab,m.sum(),dens[m].mean(),b,se,b/se))
# is there anything special at 0.607 in the distribution itself?
tf=(tors=='')&(cs==1); h,e=np.histogram(dens[tf],bins=np.arange(0.50,0.72,0.01))
print("\nloop-free curves, counts per 0.01 of density from 0.50 to 0.71:",h.tolist())
