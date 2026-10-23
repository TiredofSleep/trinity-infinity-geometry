/* anneal8_binary.c — sample 8x8 magic squares on 0..63 whose rows and columns are ALSO bit-balanced
   (every bit plane has exactly 4 ones in every row and column: the order-8 analog of the property
   every 4x4 square has). Diagonals only need to sum to 252. Usage: ./anneal8_binary N seed
   Incremental cost: only the touched rows, columns and diagonals are re-scored. */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define N 8
#define T 252
static unsigned long long s;
static unsigned long long rng(void){ s ^= s << 13; s ^= s >> 7; s ^= s << 17; return s; }
static double urand(void){ return (rng() >> 11) * (1.0/9007199254740992.0); }
int g[64], rb[N][6], cb[N][6], d1, d2;
static long rowc(int i){ long c=0; for(int k=0;k<6;k++) c+=(long)(rb[i][k]-4)*(rb[i][k]-4)*(1L<<k); return c; }
static long colc(int j){ long c=0; for(int k=0;k<6;k++) c+=(long)(cb[j][k]-4)*(cb[j][k]-4)*(1L<<k); return c; }
static long diagc(void){ return (long)(d1-T)*(d1-T)+(long)(d2-T)*(d2-T); }
static long local(int ia,int ja,int ib,int jb){ long c=rowc(ia)+colc(ja)+diagc(); if(ib!=ia) c+=rowc(ib); if(jb!=ja) c+=colc(jb); return c; }
static void add(int p,int v,int sgn){ int i=p/N,j=p%N; for(int k=0;k<6;k++){ int b=(v>>k)&1; rb[i][k]+=sgn*b; cb[j][k]+=sgn*b; }
  if(i==j) d1+=sgn*v; if(i+j==N-1) d2+=sgn*v; }
int main(int argc,char**argv){
  int want = argc>1? atoi(argv[1]) : 10; s = argc>2? strtoull(argv[2],0,10) : 88172645463325252ULL;
  int found=0;
  while(found<want){
    for(int p=0;p<64;p++) g[p]=p;
    for(int p=63;p>0;p--){ int q=rng()%(p+1); int t=g[p]; g[p]=g[q]; g[q]=t; }
    for(int i=0;i<N;i++) for(int k=0;k<6;k++) rb[i][k]=cb[i][k]=0; d1=d2=0;
    for(int p=0;p<64;p++) add(p,g[p],1);
    long c=0; for(int i=0;i<N;i++) c+=rowc(i)+colc(i); c+=diagc();
    double temp=50.0;
    for(long it=0; it<8000000 && c>0; it++){
      int a=rng()%64, b=rng()%64; if(a==b) continue;
      int ia=a/N, ja=a%N, ib=b/N, jb=b%N;
      int va=g[a], vb=g[b];
      long before=local(ia,ja,ib,jb);
      add(a,va,-1); add(b,vb,-1); add(a,vb,1); add(b,va,1);
      long delta=local(ia,ja,ib,jb)-before;
      if(delta<=0 || urand()<exp(-delta/temp)){ g[a]=vb; g[b]=va; c+=delta; }
      else { add(a,vb,-1); add(b,va,-1); add(a,va,1); add(b,vb,1); }
      temp*=0.999997; if(temp<0.2) temp=0.2;
    }
    if(c==0){ for(int p=0;p<64;p++) printf("%d%c",g[p],p==63?'\n':' '); found++; fflush(stdout);}
  }
  return 0;
}
