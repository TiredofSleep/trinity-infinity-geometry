import cypari2, json, glob, re, time, numpy as np
pari=cypari2.Pari(); pari.allocatemem(10**9)
out={}; t0=time.time(); bad=0
for fn in sorted(glob.glob('../ecdata/allgens.*')+glob.glob('../ec2/allgens.*')+glob.glob('allgens.*')):
    for line in open(fn):
        m=re.match(r'(\d+) (\w+) (\d+) \[([-\d,]+)\] (\d+) \[([\d,]*)\] ?(.*)',line.strip())
        if not m or m.group(5)!='2' or m.group(3)!='1': continue
        a1,a2,a3,a4,a6=[int(t) for t in m.group(4).split(',')]
        b2=a1*a1+4*a2; b4=2*a4+a1*a3; b6=a3*a3+4*a6
        r=np.roots([4,b2,2*b4,b6])
        if np.abs(r.imag).max()>1e-9*max(1,np.abs(r).max()): continue      # one real root: no egg
        e=np.sort(r.real); pts=re.findall(r'\[(-?\d+):(-?\d+):(-?\d+)\]',m.group(7))[:2]
        on=[1 if int(X)/int(Z) < (e[1]+e[2])/2 else 0 for X,Y,Z in pts]
        out[m.group(1)+m.group(2)]=on
json.dump(out,open('egg.json','w')); print("curves with an egg:",len(out),"seconds",round(time.time()-t0))
