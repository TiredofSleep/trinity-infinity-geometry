/* annealN.c -- natural NxN (compile with -DN=6 etc.) magic squares by simulated annealing; prints one square per line (N*N ints).
   Build: cc -O2 -DN=6 -o anneal6 annealN.c -lm     Run: ./anneal6 SECONDS SEED > squares6.txt              */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#ifndef N
#define N 6
#endif
#define NN (N*N)
#define S (N*(N*N+1)/2)
static int M[NN];
static unsigned long long s;
static double rnd(void){ s ^= s << 13; s ^= s >> 7; s ^= s << 17; return (s >> 11) * (1.0 / 9007199254740992.0); }
static int cost(void){
  int c = 0, i, j, t;
  for (i = 0; i < N; i++){ t = 0; for (j = 0; j < N; j++) t += M[N*i+j]; c += abs(t - S); }
  for (j = 0; j < N; j++){ t = 0; for (i = 0; i < N; i++) t += M[N*i+j]; c += abs(t - S); }
  t = 0; for (i = 0; i < N; i++) t += M[(N+1)*i]; c += abs(t - S);
  t = 0; for (i = 0; i < N; i++) t += M[N*i+N-1-i]; c += abs(t - S);
  return c;
}
int main(int argc, char **argv){
  double secs = argc > 1 ? atof(argv[1]) : 10; s = argc > 2 ? strtoull(argv[2], 0, 10) : 88172645463325252ULL;
  clock_t t0 = clock(); long found = 0;
  while ((double)(clock() - t0) / CLOCKS_PER_SEC < secs){
    int i, k; for (i = 0; i < NN; i++) M[i] = i + 1;
    for (i = NN - 1; i > 0; i--){ k = (int)(rnd() * (i + 1)); int x = M[i]; M[i] = M[k]; M[k] = x; }
    int c = cost(); double T = 3.0;
    for (long step = 0; step < 200000 && c; step++){
      int a = (int)(rnd() * NN), b = (int)(rnd() * NN); int x = M[a]; M[a] = M[b]; M[b] = x;
      int c2 = cost();
      if (c2 <= c || rnd() < exp((c - c2) / T)) c = c2; else { x = M[a]; M[a] = M[b]; M[b] = x; }
      T *= 0.99995; if (T < 0.05) T = 0.05;
    }
    if (!c){ found++; for (i = 0; i < NN; i++) printf("%d%c", M[i], i == NN - 1 ? '\n' : ' '); }
  }
  fprintf(stderr, "found %ld\n", found);
  return 0;
}
