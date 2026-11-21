"""Does a floor on the shortest vector explain the packing?  Model: given each curve's actual regulator and a
floor f on the squared shortest length, the shape is uniform on the modular surface cut off at
elongation <= sqrt(Reg)/f.  Floor = a low percentile of the shortest side within the curve's conductor band and
torsion class.  Unregistered diagnostic, 2026-11-20."""
import json, numpy as np, math
d=json.load(open('../ecdata/shapes_full.json'))+json.load(open('../ec2/shapes_100k_300k.json'))+json.load(open('shapes_300k_500k.json'))
N=np.array([c['N'] for c in d],float); y=np.array([c['y'] for c in d]); h1=np.array([c['h1'] for c in d]); reg=np.array([c['reg'] for c in d]); tors=np.array([c['tors'] for c in d])
dens=math.pi/(4*y); cls=np.where(tors=='',0,np.where(tors=='2',1,2))
bands=[(0,1e4),(1e4,3e4),(3e4,6e4),(6e4,1e5),(1e5,2e5),(2e5,3e5),(3e5,4e5),(4e5,5e5)]
rng=np.random.default_rng(0)
def model(pct):
    pred=np.full(len(y),np.nan); pthin=np.full(len(y),np.nan)
    for lo,hi in bands:
        for c in (0,1,2):
            m=(N>=lo)&(N<hi)&(cls==c)
            if m.sum()<50: continue
            f=np.percentile(h1[m],pct); Ymax=np.sqrt(reg[m])/f
            K=400; xs=np.sin(rng.uniform(0,math.pi/6,(m.sum(),K))); y0=np.sqrt(1-xs**2)
            ok=Ymax[:,None]>y0; w=np.where(ok,1-y0/np.maximum(Ymax[:,None],1e-9),0)       # acceptance weight for each x
            u=rng.uniform(0,1,(m.sum(),K)); umin=np.where(ok,y0/Ymax[:,None],1); uu=umin+(1-umin)*u; ys=y0/uu
            W=w.sum(1); W[W==0]=np.nan
            pred[m]=(w*(math.pi/(4*ys))).sum(1)/W; pthin[m]=(w*(ys>2)).sum(1)/W
    return pred,pthin
for pct in (0.5,5.0):
    pred,pthin=model(pct); ok=~np.isnan(pred)
    print("\nfloor = %.1fth percentile of the shortest side in each band and torsion class"%pct)
    print("%-22s actual mean density   floor model   actual thin share   floor model"%"")
    for lab,c in (("no closing wheels",0),("order 2",1),("other torsion",2)):
        m=ok&(cls==c); print("%-22s %.4f               %.4f        %.4f              %.4f"%(lab,dens[m].mean(),pred[m].mean(),(y[m]>2).mean(),pthin[m].mean()))
    print("torsion-free by band: actual",[round(float(dens[ok&(cls==0)&(N>=lo)&(N<hi)].mean()),3) for lo,hi in bands])
    print("                      model ",[round(float(pred[ok&(cls==0)&(N>=lo)&(N<hi)].mean()),3) for lo,hi in bands])
for c,lab in ((0,"no closing wheels"),(1,"order 2"),(2,"other")):
    m=cls==c; print("%-18s median regulator %.3f ; median shortest side %.3f ; median sqrt(Reg)/shortest %.3f"%(lab,np.median(reg[m]),np.median(h1[m]),np.median(np.sqrt(reg[m])/h1[m])))
