/* t7_rigorous.c -- the p = 7 theorem with rigorous interval arithmetic.

   "make it rigor"  -- the author, 18 November 2026

   Claim (see ../t_optimal_7.py and RIGOROUS.md): every diagonal state on 7 levels has S = sum |W| <= S_T, with equality
   only at the T states of class 1.  This program is the branch and bound of t_optimal_7.py redone so that every number
   it compares is a rigorous bound:
     - every double operation is enclosed: a result r of a round-to-nearest operation is within u|r|/(1-u) + 2^-1075
       of the exact value (u = 2^-53), so [dn(r), up(r)], widened by 4u|r| + 4 * 2^-1074, contains it;
     - cos and sin are never taken from the C library: the argument is reduced by an integer multiple of pi/2, with
       pi/2 enclosed by two adjacent doubles, and a Taylor polynomial with interval coefficients and an explicit
       remainder is evaluated in interval arithmetic (constants from constants.py, 60-digit arithmetic);
     - boxes are stored by their double endpoints, split at a double, so the children cover the parent exactly;
     - the domain covered is [-PI7_HI, PI7_HI]^2 x [0, TWO_PI_HI]^4, which contains D = [-pi/7, pi/7]^2 x [0, 2 pi]^4.
   A box is discarded when (a) its upper bound for S is below ST_LO <= S_T, or (b) S is smooth on it and an interval
   partial derivative excludes 0, or (c) it lies inside a cube of half-width rho0 around phi_3 or phi_4 (the lemmas K1-K4
   of constants.py, and the analysis in RIGOROUS.md, make S <= S_T there).

   Build:  build.bat   (MSVC: /O2 /fp:strict /openmp)
   Run:    t7_rigorous.exe prove [threads]      -> the verdict and the counts
           t7_rigorous.exe selftest in out     -> enclosures for constants.py's check of the trigonometry
*/
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <float.h>
#include <stdint.h>
#include <windows.h>
#include <omp.h>
#include "t7_constants.h"

static double B2D(uint64_t b) { double d; memcpy(&d, &b, 8); return d; }
static uint64_t D2B(double d) { uint64_t b; memcpy(&b, &d, 8); return b; }

typedef struct { double lo, hi; } I;

static double FOURU, ETA;
static I PI_I, TWO_PI_I, PIO2_I, SHIFT_I[7], COSC_I[NT + 1], SINC_I[NT + 1];
static double PI7_HI, TWO_PI_HI, REMC, REMS, RHO0, ST_LO;
static double CUBE_LO[2][6], CUBE_HI[2][6];

static double dn(double r) { return r - (fabs(r) * FOURU + ETA); }
static double up(double r) { return r + (fabs(r) * FOURU + ETA); }
static I mk(double lo, double hi) { I r; r.lo = lo; r.hi = hi; return r; }
static I pt(double x) { return mk(x, x); }
static I iadd(I a, I b) { return mk(dn(a.lo + b.lo), up(a.hi + b.hi)); }
static I isub(I a, I b) { return mk(dn(a.lo - b.hi), up(a.hi - b.lo)); }
static I ineg(I a) { return mk(-a.hi, -a.lo); }
static I imul(I a, I b) {
    double p1 = a.lo * b.lo, p2 = a.lo * b.hi, p3 = a.hi * b.lo, p4 = a.hi * b.hi;
    double mn = fmin(fmin(p1, p2), fmin(p3, p4)), mx = fmax(fmax(p1, p2), fmax(p3, p4));
    return mk(dn(mn), up(mx));
}
static I isqr(I a) {
    double l = fabs(a.lo), h = fabs(a.hi);
    if (a.lo <= 0.0 && a.hi >= 0.0) { double m = fmax(l, h); return mk(0.0, up(m * m)); }
    { double mn = fmin(l, h), mx = fmax(l, h); double lo = dn(mn * mn); return mk(lo < 0.0 ? 0.0 : lo, up(mx * mx)); }
}
static I iscale(I a, double k) {       /* k = +-2 or +-1: exact scaling by a power of two */
    double x = k * a.lo, y = k * a.hi;
    return mk(fmin(x, y), fmax(x, y));
}
static I enc_sub(double x, double y) { double r = x - y; return mk(dn(r), up(r)); }   /* encloses x - y exactly */

static I imul_pos(I a, I x) {         /* a * x for an interval x with x.lo >= 0 */
    if (a.lo >= 0.0) return mk(dn(a.lo * x.lo), up(a.hi * x.hi));
    if (a.hi <= 0.0) return mk(dn(a.lo * x.hi), up(a.hi * x.lo));
    return mk(dn(a.lo * x.hi), up(a.hi * x.hi));
}

static I horner(I x2, const I *c) {   /* x2.lo >= 0 (it is a square) */
    I acc = c[NT];
    int j;
    for (j = NT - 1; j >= 0; --j) acc = iadd(imul_pos(acc, x2), c[j]);
    return acc;
}

/* enclosures of cos and sin over the (narrow) interval X; returns 0 if the reduction failed (never expected) */
static int sincos_encl(I X, I *cs, I *sn) {
    double mid = 0.5 * X.lo + 0.5 * X.hi;
    double kd = nearbyint(mid / PIO2_I.lo);
    I K, R, R2, c, s;
    long long k = (long long)kd;
    int q;
    if (kd >= 0.0) K = mk(dn(kd * PIO2_I.lo), up(kd * PIO2_I.hi));
    else K = mk(dn(kd * PIO2_I.hi), up(kd * PIO2_I.lo));
    R = isub(X, K);
    if (fabs(R.lo) > RMAX || fabs(R.hi) > RMAX) return 0;
    R2 = isqr(R);
    c = iadd(horner(R2, COSC_I), mk(-REMC, REMC));
    s = iadd(imul(R, horner(R2, SINC_I)), mk(-REMS, REMS));
    q = (int)(((k % 4) + 4) % 4);
    if (q == 0) { *cs = c; *sn = s; }
    else if (q == 1) { *cs = ineg(s); *sn = c; }
    else if (q == 2) { *cs = ineg(c); *sn = ineg(s); }
    else { *cs = s; *sn = ineg(c); }
    if (cs->lo < -1.0) cs->lo = -1.0;
    if (cs->hi > 1.0) cs->hi = 1.0;
    if (sn->lo < -1.0) sn->lo = -1.0;
    if (sn->hi > 1.0) sn->hi = 1.0;
    return 1;
}

/* the ranges of cos and sin over [a, b] with a in A and b in B (a <= b).  The extremes are at the ends or at interior
   critical points j pi/2: j = 0 mod 4 is a maximum of cos (1), 2 mod 4 a minimum of cos (-1), 1 mod 4 a maximum of sin,
   3 mod 4 a minimum of sin.  Every j whose enclosure of j pi/2 may meet [A.lo, B.hi] is counted (conservative); the
   candidates j0..j1 cover every j with j pi/2 in [A.lo, B.hi], with a slack of one on each side. */
static int trig_ranges(I A, I B, double *cmin, double *cmax, double *smin, double *smax) {
    I cA, sA, cB, sB;
    double lo = A.lo, hi = B.hi;
    long long j, j0, j1;
    if (!sincos_encl(A, &cA, &sA) || !sincos_encl(B, &cB, &sB)) return 0;
    *cmin = fmin(cA.lo, cB.lo); *cmax = fmax(cA.hi, cB.hi);
    *smin = fmin(sA.lo, sB.lo); *smax = fmax(sA.hi, sB.hi);
    j0 = (long long)floor(lo / PIO2_I.lo) - 1;
    j1 = (long long)ceil(hi / PIO2_I.lo) + 1;
    for (j = j0; j <= j1; ++j) {
        double jd = (double)j;
        I P = (jd >= 0.0) ? mk(dn(jd * PIO2_I.lo), up(jd * PIO2_I.hi)) : mk(dn(jd * PIO2_I.hi), up(jd * PIO2_I.lo));
        if (P.hi >= lo && P.lo <= hi) {
            int r = (int)(((j % 4) + 4) % 4);
            if (r == 0) *cmax = 1.0;
            else if (r == 2) *cmin = -1.0;
            else if (r == 1) *smax = 1.0;
            else *smin = -1.0;
        }
    }
    return 1;
}

static const int AI[7][3] = {{1,2,3},{2,3,4},{3,4,5},{4,5,6},{5,6,0},{6,0,1},{0,1,2}};
static const int BI[7][3] = {{6,5,4},{0,6,5},{1,0,6},{2,1,0},{3,2,1},{4,3,2},{5,4,3}};

typedef struct { double U, Sc; int smooth, mono, fail; } Result;

static void eval_box(const double *lo6, const double *hi6, Result *res) {
    double L[7], H[7], M[7], RAD[7];
    double sum_kept = 0.0, sum_rem = 0.0, sum_other = 0.0, sum_exact = 0.0, lin = 0.0, Sc = 0.0;
    I G[7], GI[7];
    int i, q, s, u, all_kept = 1;
    L[0] = H[0] = M[0] = RAD[0] = 0.0;
    for (i = 0; i < 6; ++i) {
        L[i + 1] = lo6[i]; H[i + 1] = hi6[i];
        M[i + 1] = 0.5 * lo6[i] + 0.5 * hi6[i];
        if (M[i + 1] < lo6[i]) M[i + 1] = lo6[i];
        if (M[i + 1] > hi6[i]) M[i + 1] = hi6[i];
        RAD[i + 1] = up(fmax(M[i + 1] - lo6[i], hi6[i] - M[i + 1]));
    }
    for (i = 0; i < 7; ++i) { G[i] = pt(0.0); GI[i] = pt(0.0); }
    res->fail = 0;
    for (q = 0; q < 7; ++q) {
        I Abase[3], Bbase[3], Cbase[3];
        double w[3];
        for (u = 0; u < 3; ++u) {
            int a = AI[q][u], b = BI[q][u];
            Abase[u] = enc_sub(L[a], H[b]);
            Bbase[u] = enc_sub(H[a], L[b]);
            Cbase[u] = enc_sub(M[a], M[b]);
            w[u] = up(RAD[a] + RAD[b]);
        }
        for (s = 0; s < 7; ++s) {
            I cc[3], sc[3], Ec;
            double cmn[3], cmx[3], smn[3], smx[3], tmax, tmin, Emax, Emin, absmax;
            int keep, sigma;
            for (u = 0; u < 3; ++u) {
                int k = (2 * s * (u + 1)) % 7;
                I A = isub(Abase[u], SHIFT_I[k]), B = isub(Bbase[u], SHIFT_I[k]), C = isub(Cbase[u], SHIFT_I[k]);
                if (!sincos_encl(C, &cc[u], &sc[u]) || !trig_ranges(A, B, &cmn[u], &cmx[u], &smn[u], &smx[u])) {
                    res->fail = 1; return;
                }
            }
            Ec = iadd(pt(1.0), iscale(iadd(iadd(cc[0], cc[1]), cc[2]), 2.0));
            tmax = up(up(cmx[0] + cmx[1]) + cmx[2]);
            tmin = dn(dn(cmn[0] + cmn[1]) + cmn[2]);
            Emax = up(1.0 + 2.0 * tmax);
            Emin = dn(1.0 + 2.0 * tmin);
            absmax = fmax(fabs(Emax), fabs(Emin));
            sum_exact = up(sum_exact + absmax);
            Sc += fabs(0.5 * Ec.lo + 0.5 * Ec.hi);
            keep = (Emin > 0.0) || (Emax < 0.0);
            sigma = (Emin > 0.0) ? 1 : -1;
            if (keep) {
                double sigE = (sigma > 0) ? Ec.hi : -Ec.lo;
                sum_kept = up(sum_kept + sigE);
                for (u = 0; u < 3; ++u) {
                    int a = AI[q][u], b = BI[q][u];
                    sum_rem = up(sum_rem + up(w[u] * w[u]));
                    /* d E / d phi_a = -2 sin(angle), d E / d phi_b = +2 sin(angle); times sigma */
                    G[a] = iadd(G[a], iscale(sc[u], -2.0 * sigma));
                    G[b] = iadd(G[b], iscale(sc[u], 2.0 * sigma));
                    GI[a] = iadd(GI[a], iscale(mk(smn[u], smx[u]), -2.0 * sigma));
                    GI[b] = iadd(GI[b], iscale(mk(smn[u], smx[u]), 2.0 * sigma));
                }
            } else {
                all_kept = 0;
                sum_other = up(sum_other + absmax);
            }
        }
    }
    for (i = 1; i < 7; ++i) lin = up(lin + up(fmax(fabs(G[i].lo), fabs(G[i].hi)) * RAD[i]));
    {
        double Umix = up(up(up(up(sum_kept + lin) + sum_rem) + sum_other) / 49.0);
        double Uex = up(sum_exact / 49.0);
        res->U = fmin(Umix, Uex);
    }
    res->Sc = Sc / 49.0;
    res->smooth = all_kept;
    res->mono = 0;
    if (all_kept)
        for (i = 1; i < 7; ++i)
            if (GI[i].lo > 0.0 || GI[i].hi < 0.0) { res->mono = 1; break; }
}

typedef struct { double lo[6], hi[6]; } Box;
typedef struct { long long boxes, by_bound, by_mono, by_cube, fails, stuck, overflow; double maxc; int aborted; } Stats;

static int inside_cube_pts(const double *lo6, const double *hi6) {
    int c, i;
    for (c = 0; c < 2; ++c) {
        int in = 1;
        for (i = 0; i < 6; ++i)
            if (!(lo6[i] >= CUBE_LO[c][i] && hi6[i] <= CUBE_HI[c][i])) { in = 0; break; }
        if (in) return 1;
    }
    return 0;
}
static int inside_cube(const Box *b) { return inside_cube_pts(b->lo, b->hi); }

#define STACKMAX 100000
#define LIMIT 2000000000LL

static void process(const Box *b0, Stats *st, Box *stack) {
    int top = 0;
    stack[top++] = *b0;
    while (top > 0) {
        Box b = stack[--top];
        Result r;
        int j, i;
        double wmax = -1.0, m;
        eval_box(b.lo, b.hi, &r);
        st->boxes++;
        if (r.fail) { st->fails++; continue; }     /* counted; the verdict requires zero */
        if (r.Sc > st->maxc) st->maxc = r.Sc;
        if (r.U < ST_LO) { st->by_bound++; continue; }
        if (r.mono) { st->by_mono++; continue; }
        if (inside_cube(&b)) { st->by_cube++; continue; }
        j = 0;
        for (i = 0; i < 6; ++i) if (b.hi[i] - b.lo[i] > wmax) { wmax = b.hi[i] - b.lo[i]; j = i; }
        m = 0.5 * b.lo[j] + 0.5 * b.hi[j];
        if (!(m > b.lo[j] && m < b.hi[j])) { st->stuck++; continue; }
        if (top + 2 > STACKMAX) { st->overflow++; continue; }
        {
            Box c1 = b, c2 = b;
            c1.hi[j] = m; c2.lo[j] = m;
            stack[top++] = c2; stack[top++] = c1;
        }
        if (st->boxes > LIMIT) { st->aborted = 1; return; }
    }
}

static void init_constants(void) {
    int i, c;
    FOURU = 2.0 * DBL_EPSILON;                 /* 2^-51 = 4u */
    ETA = 4.0 * B2D(1ULL);                     /* 4 * 2^-1074 */
    PI_I = mk(B2D(PI_LO_B), B2D(PI_HI_B));
    TWO_PI_I = mk(B2D(TWO_PI_LO_B), B2D(TWO_PI_HI_B));
    PIO2_I = mk(B2D(PIO2_LO_B), B2D(PIO2_HI_B));
    PI7_HI = B2D(PI7_HI_B);
    TWO_PI_HI = B2D(TWO_PI_HI_B);
    for (i = 0; i < 7; ++i) SHIFT_I[i] = mk(B2D(SHIFT_LO_B[i]), B2D(SHIFT_HI_B[i]));
    for (i = 0; i <= NT; ++i) {
        COSC_I[i] = mk(B2D(COSC_LO_B[i]), B2D(COSC_HI_B[i]));
        SINC_I[i] = mk(B2D(SINC_LO_B[i]), B2D(SINC_HI_B[i]));
    }
    REMC = B2D(REMC_HI_B);
    REMS = B2D(REMS_HI_B);
    RHO0 = B2D(RHO0_B);
    ST_LO = B2D(ST_LO_B);
    for (c = 0; c < 2; ++c)
        for (i = 0; i < 6; ++i) {
            double plo = B2D(c == 0 ? PHI3_LO_B[i] : PHI4_LO_B[i]), phi = B2D(c == 0 ? PHI3_HI_B[i] : PHI4_HI_B[i]);
            CUBE_LO[c][i] = up(phi - RHO0);      /* >= phi* - rho0 */
            CUBE_HI[c][i] = dn(plo + RHO0);      /* <= phi* + rho0 */
        }
}

static int selftest(const char *in, const char *out) {
    FILE *fi = fopen(in, "r"), *fo = fopen(out, "w");
    char kind[8];
    unsigned long long xa, xb;
    if (!fi || !fo) return 2;
    while (fscanf(fi, "%7s %llx %llx", kind, &xa, &xb) == 3) {
        double a = B2D(xa), b = B2D(xb);
        if (kind[0] == 'P') {                        /* point enclosures of cos and sin at a */
            I c, s;
            int ok = sincos_encl(pt(a), &c, &s);
            fprintf(fo, "P %d %016llx %016llx %016llx %016llx\n", ok, D2B(c.lo), D2B(c.hi), D2B(s.lo), D2B(s.hi));
        } else {                                     /* ranges over [a, b] */
            double cmn, cmx, smn, smx;
            int ok = trig_ranges(pt(a), pt(b), &cmn, &cmx, &smn, &smx);
            fprintf(fo, "R %d %016llx %016llx %016llx %016llx\n", ok, D2B(cmn), D2B(cmx), D2B(smn), D2B(smx));
        }
    }
    fclose(fi); fclose(fo);
    return 0;
}

/* for selftest.py: the bounds of eval_box on given boxes, to compare with the float prover and with sampled points */
static int boxtest(const char *in, const char *out) {
    FILE *fi = fopen(in, "r"), *fo = fopen(out, "w");
    unsigned long long v[12];
    if (!fi || !fo) return 2;
    for (;;) {
        double lo6[6], hi6[6];
        Result r;
        int i, got = 0;
        for (i = 0; i < 12; ++i) got += fscanf(fi, "%llx", &v[i]);
        if (got != 12) break;
        for (i = 0; i < 6; ++i) { lo6[i] = B2D(v[i]); hi6[i] = B2D(v[6 + i]); }
        eval_box(lo6, hi6, &r);
        fprintf(fo, "%016llx %d %d %d %d\n", D2B(r.U), r.smooth, r.mono, r.fail, inside_cube_pts(lo6, hi6));
    }
    fclose(fi); fclose(fo);
    return 0;
}

int main(int argc, char **argv) {
    int threads = 4, n, k, done;
    double t0;
    Box init[1024];
    Stats total;
    init_constants();
    SetPriorityClass(GetCurrentProcess(), BELOW_NORMAL_PRIORITY_CLASS);
    if (argc >= 4 && strcmp(argv[1], "selftest") == 0) return selftest(argv[2], argv[3]);
    if (argc >= 4 && strcmp(argv[1], "boxtest") == 0) return boxtest(argv[2], argv[3]);
    if (argc < 2 || strcmp(argv[1], "prove") != 0) { fprintf(stderr, "usage: t7_rigorous prove [threads] | selftest in out\n"); return 2; }
    if (argc >= 3) threads = atoi(argv[2]);
    omp_set_num_threads(threads);
    /* the initial grid over [-PI7_HI, PI7_HI]^2 x [0, TWO_PI_HI]^4: 2 x 2 x 4^4 boxes with shared double endpoints */
    {
        double e1[3], e3[5];
        int a, b, c, d, e, f;
        e1[0] = -PI7_HI; e1[1] = 0.0; e1[2] = PI7_HI;
        e3[0] = 0.0; e3[4] = TWO_PI_HI; e3[2] = 0.5 * TWO_PI_HI; e3[1] = 0.25 * TWO_PI_HI; e3[3] = 0.75 * TWO_PI_HI;
        n = 0;
        for (a = 0; a < 2; ++a) for (b = 0; b < 2; ++b) for (c = 0; c < 4; ++c) for (d = 0; d < 4; ++d)
        for (e = 0; e < 4; ++e) for (f = 0; f < 4; ++f) {
            Box *x = &init[n++];
            x->lo[0] = e1[a]; x->hi[0] = e1[a + 1]; x->lo[1] = e1[b]; x->hi[1] = e1[b + 1];
            x->lo[2] = e3[c]; x->hi[2] = e3[c + 1]; x->lo[3] = e3[d]; x->hi[3] = e3[d + 1];
            x->lo[4] = e3[e]; x->hi[4] = e3[e + 1]; x->lo[5] = e3[f]; x->hi[5] = e3[f + 1];
        }
    }
    memset(&total, 0, sizeof(total));
    total.maxc = -1.0;
    done = 0;
    t0 = omp_get_wtime();
#pragma omp parallel
    {
        Stats st;
        Box *stack = (Box *)malloc(STACKMAX * sizeof(Box));
        memset(&st, 0, sizeof(st));
        st.maxc = -1.0;
#pragma omp for schedule(dynamic, 1)
        for (k = 0; k < n; ++k) {
            process(&init[k], &st, stack);
#pragma omp critical
            {
                ++done;
                if (done % 64 == 0) {
                    fprintf(stderr, "  progress: %d/%d first-grid boxes done, %lld boxes in this thread, %.0f s\n",
                            done, n, st.boxes, omp_get_wtime() - t0);
                    fflush(stderr);
                }
            }
        }
#pragma omp critical
        {
            total.boxes += st.boxes; total.by_bound += st.by_bound; total.by_mono += st.by_mono; total.by_cube += st.by_cube;
            total.fails += st.fails; total.stuck += st.stuck; total.overflow += st.overflow;
            if (st.maxc > total.maxc) total.maxc = st.maxc;
            if (st.aborted) total.aborted = 1;
        }
        free(stack);
    }
    printf("boxes %lld by_bound %lld by_monotone %lld by_cube %lld fails %lld stuck %lld overflow %lld aborted %d\n",
           total.boxes, total.by_bound, total.by_mono, total.by_cube, total.fails, total.stuck, total.overflow, total.aborted);
    printf("max_center_S %.16g ST_LO %.16g\n", total.maxc, ST_LO);
    printf("seconds %.1f threads %d\n", omp_get_wtime() - t0, threads);
    if (total.fails == 0 && total.stuck == 0 && total.overflow == 0 && !total.aborted)
        printf("VERDICT PASS: every box discarded with rigorous bounds\n");
    else
        printf("VERDICT FAIL\n");
    return 0;
}
