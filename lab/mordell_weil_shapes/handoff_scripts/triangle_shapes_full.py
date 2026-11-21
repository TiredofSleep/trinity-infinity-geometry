import cypari2, math, json, glob, re, time
pari=cypari2.Pari(); pari.allocatemem(10**9)
out=[]; t0=time.time(); bad=0
for fn in sorted(glob.glob('allgens.*')):
    for line in open(fn):
        m=re.match(r'(\d+) (\w+) (\d+) \[([-\d,]+)\] (\d+) \[([\d,]*)\] ?(.*)',line.strip())
        if not m or m.group(5)!='2' or m.group(3)!='1': continue
        N=int(m.group(1)); ai=[int(t) for t in m.group(4).split(',')]
        pts=re.findall(r'\[(-?\d+):(-?\d+):(-?\d+)\]',m.group(7))
        ntors=len([t for t in m.group(6).split(',') if t])
        gens=pts[:2]
        try:
            E=pari.ellinit(ai); P=[]
            for X,Y,Z in gens:
                X,Y,Z=int(X),int(Y),int(Z); P.append([pari(X)/Z,pari(Y)/Z])
            H=pari.ellheightmatrix(E,P); A,B,C=float(H[0][0]),float(H[0][1]),float(H[1][1])
            reg=A*C-B*B
            for _ in range(500):
                if A>C: A,C=C,A
                k=round(B/A)
                if k==0: break
                C=C-2*k*B+k*k*A; B=B-k*A
            if A>C: A,C=C,A
            out.append(dict(N=N,cls=m.group(2),h1=A,h2=C,B=B,reg=reg,x=abs(B)/A,y=math.sqrt(A*C-B*B)/A,tors=m.group(6),logdisc=float(pari.log(abs(E.disc())))))
        except Exception as e:
            bad+=1; err=repr(e)
json.dump(out,open('shapes_full.json','w'))
print("rank-2 optimal curves with shapes:",len(out)," failures:",bad," seconds:",round(time.time()-t0))
print(globals().get("err"))
