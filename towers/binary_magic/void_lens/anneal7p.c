/* anneal7p.c -- natural pandiagonal 7x7 magic squares by simulated annealing (rows, columns and all 14
   broken diagonals sum to 175). One square per line (49 ints).
   Build: cc -O2 -o anneal7p anneal7p.c -lm     Run: ./anneal7p SECONDS SEED > out.txt               */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#define N 7
static int M[N*N];
static unsigned long long s;
static double rnd(void){ s ^= s << 13; s ^= s >> 7; s ^= s << 17; return (s >> 11) * (1.0 / 9007199254740992.0); }
static int cost(void){
  int c = 0, i, j, d, t, S = N * (N * N + 1) / 2;
  for (i = 0; i < N; i++){ t = 0; for (j = 0; j < N; j++) t += M[N*i+j]; c += abs(t - S); }
  for (j = 0; j < N; j++){ t = 0; for (i = 0; i < N; i++) t += M[N*i+j]; c += abs(t - S); }
  for (d = 0; d < N; d++){
    t = 0; for (i = 0; i < N; i++) t += M[N*i + (i + d) % N]; c += abs(t - S);
    t = 0; for (i = 0; i < N; i++) t += M[N*i + ((d - i) % N + N) % N]; c += abs(t - S);
  }
  return c;
}
int main(int argc, char **argv){
  double secs = argc > 1 ? atof(argv[1]) : 10; s = argc > 2 ? strtoull(argv[2], 0, 10) : 88172645463325252ULL;
  clock_t t0 = clock(); long found = 0, tries = 0;
  while ((double)(clock() - t0) / CLOCKS_PER_SEC < secs){
    int i, k; tries++;
    for (i = 0; i < N*N; i++) M[i] = i + 1;
    for (i = N*N - 1; i > 0; i--){ k = (int)(rnd() * (i + 1)); int x = M[i]; M[i] = M[k]; M[k] = x; }
    int c = cost(); double T = 12.0;
    for (long step = 0; step < 3000000 && c; step++){
      int a = (int)(rnd() * N*N), b = (int)(rnd() * N*N); int x = M[a]; M[a] = M[b]; M[b] = x;
      int c2 = cost();
      if (c2 <= c || rnd() < exp((c - c2) / T)) c = c2; else { x = M[a]; M[a] = M[b]; M[b] = x; }
      T *= 0.999997; if (T < 0.05) T = 0.05;
    }
    if (!c){ found++; for (i = 0; i < N*N; i++) printf("%d%c", M[i], i == N*N - 1 ? '\n' : ' '); }
  }
  fprintf(stderr, "found %ld of %ld\n", found, tries);
  return 0;
}
