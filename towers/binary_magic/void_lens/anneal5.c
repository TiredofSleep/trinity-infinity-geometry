/* anneal5.c -- natural 5x5 magic squares by simulated annealing; prints one square per line (25 ints).
   Build: cc -O2 -o anneal5 anneal5.c     Run: ./anneal5 SECONDS SEED > squares5.txt              */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
static int M[25];
static unsigned long long s;
static double rnd(void){ s ^= s << 13; s ^= s >> 7; s ^= s << 17; return (s >> 11) * (1.0 / 9007199254740992.0); }
static int cost(void){
  int c = 0, i, j, t;
  for (i = 0; i < 5; i++){ t = 0; for (j = 0; j < 5; j++) t += M[5*i+j]; c += abs(t - 65); }
  for (j = 0; j < 5; j++){ t = 0; for (i = 0; i < 5; i++) t += M[5*i+j]; c += abs(t - 65); }
  t = 0; for (i = 0; i < 5; i++) t += M[6*i]; c += abs(t - 65);
  t = 0; for (i = 0; i < 5; i++) t += M[5*i+4-i]; c += abs(t - 65);
  return c;
}
int main(int argc, char **argv){
  double secs = argc > 1 ? atof(argv[1]) : 10; s = argc > 2 ? strtoull(argv[2], 0, 10) : 88172645463325252ULL;
  clock_t t0 = clock(); long found = 0;
  while ((double)(clock() - t0) / CLOCKS_PER_SEC < secs){
    int i, k; for (i = 0; i < 25; i++) M[i] = i + 1;
    for (i = 24; i > 0; i--){ k = (int)(rnd() * (i + 1)); int x = M[i]; M[i] = M[k]; M[k] = x; }
    int c = cost(); double T = 3.0;
    for (long step = 0; step < 40000 && c; step++){
      int a = (int)(rnd() * 25), b = (int)(rnd() * 25); int x = M[a]; M[a] = M[b]; M[b] = x;
      int c2 = cost();
      if (c2 <= c || rnd() < exp((c - c2) / T)) c = c2; else { x = M[a]; M[a] = M[b]; M[b] = x; }
      T *= 0.9997; if (T < 0.05) T = 0.05;
    }
    if (!c){ found++; for (i = 0; i < 25; i++) printf("%d%c", M[i], i == 24 ? '\n' : ' '); }
  }
  fprintf(stderr, "found %ld\n", found);
  return 0;
}
