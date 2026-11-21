import cypari2, math, json, glob, re, time
pari=cypari2.Pari(); pari.allocatemem(10**9)
out={}; t0=time.time(); bad=0
for fn in sorted(glob.glob('../ecdata/allgens.*')+glob.glob('../ec2/allgens.*')+glob.glob('allgens.*')):
    for line in open(fn):
        m=re.match(r'(\d+) (\w+) (\d+) \[([-\d,]+)\] (\d+) ',line)
        if not m or m.group(5)!='2' or m.group(3)!='1': continue
        try:
            E=pari.ellinit([int(t) for t in m.group(4).split(',')]); sg=int(pari.sign(E.disc()))
            w=E.omega(); tau=complex(w[0])/complex(w[1])
            if tau.imag<0: tau=-tau
            for _ in range(200):
                tau=complex(tau.real-round(tau.real),tau.imag)
                if abs(tau)<1-1e-12: tau=-1/tau
                else: break
            out[m.group(1)+m.group(2)]=(sg,abs(tau.real),tau.imag,float(abs(complex(w[0]))),float(pari.ellheight(E)) if False else 0.0)
        except Exception as e:
            bad+=1; err=repr(e)
json.dump(out,open('periods.json','w'))
print("curves",len(out),"failures",bad,"seconds",round(time.time()-t0),globals().get('err'))
