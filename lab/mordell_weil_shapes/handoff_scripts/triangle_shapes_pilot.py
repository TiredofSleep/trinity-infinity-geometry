import cypari2, math, time, json, sys
pari=cypari2.Pari(); pari.allocatemem(10**9)
t0=time.time(); out=[]; seen=set(); tried=0
R=int(sys.argv[1]); LIM=float(sys.argv[2])
for a in range(-R,R+1):
    for b in range(-R,R+1):
        if time.time()-t0>LIM: break
        if 4*a**3+27*b*b==0: continue
        try:
            E=pari.ellinit(pari.ellminimalmodel(pari.ellinit([0,0,0,a,b])))
            key=str(pari.ellglobalred(E)[0])+str(E[0:5])
            if key in seen: continue
            seen.add(key); tried+=1
            if int(pari.ellrootno(E))!=1: continue
            r=pari.ellrank(E)
            if int(r[0])!=2 or int(r[1])!=2: continue
            pts=pari.ellsaturation(E,r[3],200)
            H=pari.ellheightmatrix(E,pts)
            A,B,C=float(H[0][0]),float(H[0][1]),float(H[1][1])
            # Gauss reduction of the form A x^2 + 2B xy + C y^2
            for _ in range(200):
                if A>C: A,C=C,A
                k=round(B/A)
                if k==0: break
                C=C-2*k*B+k*k*A; B=B-k*A
            if A>C: A,C=C,A
            x=abs(B)/A; y=math.sqrt(A*C-B*B)/A
            out.append(dict(a=a,b=b,N=int(pari.ellglobalred(E)[0]),reg=A*C-B*B,x=x,y=y,angle=math.degrees(math.atan2(y,x))))
        except Exception as e:
            pass
json.dump(out,open('shapes_pilot.json','w'))
print("curves tried",tried,"rank-2 with shapes",len(out),"seconds",round(time.time()-t0))
