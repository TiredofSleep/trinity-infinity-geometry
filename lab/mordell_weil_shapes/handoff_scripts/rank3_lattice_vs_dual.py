import cypari2, math, json, glob, re, time, numpy as np, itertools
pari=cypari2.Pari(); pari.allocatemem(10**9)
box=np.array([c for c in itertools.product(range(-4,5),repeat=3) if any(c)])
def minimum(G):
    M=pari.matrix(3,3,[float(v) for v in np.array(G).flatten()]); U=pari.qflllgram(M); R=U.mattranspose()*M*U
    R=np.array([[float(R[i][j]) for j in range(3)] for i in range(3)])
    return float(np.einsum('ni,ij,nj->n',box,R,box).min())
big=np.array([c for c in itertools.product(range(-9,10),repeat=3) if any(c)])
brute=lambda G: float(np.einsum('ni,ij,nj->n',big,np.array(G),big).min())
vol3=math.pi/6; out=[]; mism=0; k=0
for fn in sorted(glob.glob('../ecdata/allgens.*')+glob.glob('../ec2/allgens.*')+glob.glob('allgens.*')):
    for line in open(fn):
        m=re.match(r'(\d+) (\w+) (\d+) \[([-\d,]+)\] (\d+) \[([\d,]*)\] ?(.*)',line.strip())
        if not m or m.group(5)!='3' or m.group(3)!='1': continue
        E=pari.ellinit([int(t) for t in m.group(4).split(',')])
        pts=re.findall(r'\[(-?\d+):(-?\d+):(-?\d+)\]',m.group(7))[:3]
        Pp=[[pari(int(X))/int(Z),pari(int(Y))/int(Z)] for X,Y,Z in pts]
        H=np.array([[float(v) for v in row] for row in pari.ellheightmatrix(E,Pp)]); det=np.linalg.det(H); Hi=np.linalg.inv(H)
        m1,m2=minimum(H),minimum(Hi); k+=1
        if k%10==0:
            if abs(brute(H)-m1)>1e-9*m1 or abs(brute(Hi)-m2)>1e-9*m2: mism+=1
        out.append(dict(N=int(m.group(1)),tors=m.group(6),reg=det,m1=m1,m2=m2,d=vol3*m1**1.5/math.sqrt(det),dd=vol3*m2**1.5*math.sqrt(det),sg=int(pari.sign(E.disc()))))
json.dump(out,open('rank3.json','w'))
a=np.array([c['d'] for c in out]); b=np.array([c['dd'] for c in out]); df=a-b; n=len(df)
print("rank-3 curves %d ; brute-force cross-check on every 10th: mismatches %d of %d"%(n,mism,k//10))
print("lattice %.4f ; opposite %.4f ; paired difference %+.4f, s.e. %.4f, %.1f s.e. ; lattice denser in %.3f of curves"%(a.mean(),b.mean(),df.mean(),df.std()/math.sqrt(n),df.mean()/(df.std()/math.sqrt(n)),(df>0).mean()))
tf=np.array([c['tors']=='' for c in out]); print("torsion-free only (n=%d): %+.4f ; with torsion (n=%d): %+.4f"%(tf.sum(),df[tf].mean(),(~tf).sum(),df[~tf].mean()))
N=np.array([c['N'] for c in out],float)
for lo,hi in ((0,1e5),(1e5,2.5e5),(2.5e5,5e5)): 
    mm=(N>=lo)&(N<hi); print("  conductor %6d-%6d n=%4d lattice %.4f opposite %.4f diff %+.4f"%(lo,hi,mm.sum(),a[mm].mean(),b[mm].mean(),df[mm].mean()))
# rank 2 sanity: density of Lambda and of its dual must agree
d2=json.load(open('../ecdata/shapes_full.json'))[:2000]; mx=0
for c in d2:
    A,B,C=c['h1'],c['B'],c['h2']; det=A*C-B*B; Ai,Bi,Ci=C/det,-B/det,A/det
    def red(A,B,C):
        for _ in range(100):
            if A>C: A,C=C,A
            t=round(B/A)
            if t==0: break
            C=C-2*t*B+t*t*A; B=B-t*A
        return min(A,C)
    mx=max(mx,abs(math.pi/4*red(A,B,C)/math.sqrt(det)-math.pi/4*red(Ai,Bi,Ci)*math.sqrt(det)))
print("rank-2 sanity, 2000 curves: largest |density - dual density| = %.2e"%mx)
