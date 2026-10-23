/* anneal8.c — sample 8x8 magic squares on 0..63 (all rows, columns, both diagonals = 252)
   by simulated annealing with random restarts. Usage: ./anneal8 N seed > squares8.txt
   Not a uniform sample of all magic squares, but carries no built-in binary structure. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define N 8
#define T 252
static unsigned long long s;
static unsigned long long rng(void){ s ^= s << 13; s ^= s >> 7; s ^= s << 17; return s; }
static double urand(void){ return (rng() >> 11) * (1.0/9007199254740992.0); }
int g[64], rs[N], cs[N], d1, d2;
static long cost(void){ long c=0; for(int i=0;i<N;i++){ c+=(long)(rs[i]-T)*(rs[i]-T); c+=(long)(cs[i]-T)*(cs[i]-T);} c+=(long)(d1-T)*(d1-T)+(long)(d2-T)*(d2-T); return c; }
static void recompute(void){ for(int i=0;i<N;i++){rs[i]=cs[i]=0;} d1=d2=0;
  for(int p=0;p<64;p++){ int i=p/N,j=p%N; rs[i]+=g[p]; cs[j]+=g[p]; if(i==j) d1+=g[p]; if(i+j==N-1) d2+=g[p]; } }
static void add(int p,int v){ int i=p/N,j=p%N; rs[i]+=v; cs[j]+=v; if(i==j) d1+=v; if(i+j==N-1) d2+=v; }
int main(int argc,char**argv){
  int want = argc>1? atoi(argv[1]) : 100; s = argc>2? strtoull(argv[2],0,10) : 88172645463325252ULL;
  int found=0;
  while(found<want){
    for(int p=0;p<64;p++) g[p]=p;
    for(int p=63;p>0;p--){ int q=rng()%(p+1); int t=g[p]; g[p]=g[q]; g[q]=t; }
    recompute(); long c=cost(); double temp=200.0;
    for(long it=0; it<4000000 && c>0; it++){
      int a=rng()%64, b=rng()%64; if(a==b) continue;
      int va=g[a], vb=g[b];
      add(a,vb-va); add(b,va-vb);
      long c2=cost();
      if(c2<=c || urand()<exp((c-c2)/temp)){ g[a]=vb; g[b]=va; c=c2; }
      else { add(a,va-vb); add(b,vb-va); }
      temp*=0.999995; if(temp<0.3) temp=0.3;
    }
    if(c==0){ for(int p=0;p<64;p++) printf("%d%c",g[p],p==63?'\n':' '); found++; fflush(stdout);}
  }
  return 0;
}
