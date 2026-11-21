/* bb.c -- the maximum of S = sum |W| over the diagonal states on p levels (p = 3, 5, 7), with rigorous bounds.

   "1 yes, then p = 5 alongside everything else"  -- the author, 21 November 2026

   This generalizes ../t7_rigorous/t7_rigorous.c to any small odd prime p (fixed at compile time, /DP=5).  The interval
   arithmetic is the same: every rounding is enclosed (dn/up), cos and sin come from the program's own enclosures
   (reduction by k pi/2 and a Taylor polynomial with a Lagrange remainder), and the constants come from bb_constants.h
   (exact rational arithmetic).  What is new: the maximizers need not be known in closed form.  The program reads
   candidate points (prepare.py) and certifies, for each, a box B_c around it:
     (i)   every E(q, s) keeps its sign on B_c, so S is smooth there;
     (ii)  the interval Hessian of S over B_c is negative definite (an interval LDL^T of -H with positive pivots), so S
           is strictly concave on B_c and has at most one critical point there;
     (iii) the Krawczyk operator of grad S on a small box X_c inside B_c maps X_c into its interior, so grad S has
           exactly one zero phi_c* in X_c; it is the maximum of S over B_c;
     (iv)  for c > 0, the symmetry g_c of S (an affine map of F_p, conjugation, a Clifford phase, multiples of 2 pi)
           maps X_0 into B_c, so phi_c* = g_c(phi_0*) and S(phi_c*) = S(phi_0*).
   Then the branch and bound of t7_rigorous.c runs over D = [-pi/p, pi/p]^2 x [0, 2 pi]^(p-3), discarding a box when
   (a) its upper bound is below S_LO = max_c (lower bound of S on X_c), (b) S is smooth on it and a partial derivative
   cannot vanish, or (c) it lies inside some B_c.  Here S_LO = max_c (lower bound of S at the point m_c): phi_c* is the
   maximum of S over B_c, which contains m_c.  If every box is discarded, every global maximizer in D is one of the
   phi_c*, and the maximum is S(phi_0*), enclosed between S_LO and the upper bound of S on X_c.

   Build: build.bat     Run: bb5.exe prove candidates_5.txt [threads]     bb5.exe boxtest in out  (for bb_selftest.py)
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
#include "bb_constants.h"

#ifndef P
#define P 5
#endif
#define NU ((P - 1) / 2)
#define DIM (P - 1)
#define MAXC 128

static double B2D(uint64_t b) { double d; memcpy(&d, &b, 8); return d; }
static uint64_t D2B(double d) { uint64_t b; memcpy(&b, &d, 8); return b; }

typedef struct { double lo, hi; } I;

static double FOURU, ETA, RMAX, REMC, REMS, PIP_HI, TWO_PI_HI, P2;
static I PI_I, TWO_PI_I, PIO2_I, SHIFT_I[P], COSC_I[NT + 1], SINC_I[NT + 1];
static int AI[P][NU], BI[P][NU];

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
static I idiv_pos(I a, I b) { return imul(a, mk(dn(1.0 / b.hi), up(1.0 / b.lo))); }   /* b.lo > 0 */
static I isqr(I a) {
    double l = fabs(a.lo), h = fabs(a.hi);
    if (a.lo <= 0.0 && a.hi >= 0.0) { double m = fmax(l, h); return mk(0.0, up(m * m)); }
    { double mn = fmin(l, h), mx = fmax(l, h); double lo = dn(mn * mn); return mk(lo < 0.0 ? 0.0 : lo, up(mx * mx)); }
}
static I iscale(I a, double k) {       /* k = +-2 or +-1: exact scaling by a power of two */
    double x = k * a.lo, y = k * a.hi;
    return mk(fmin(x, y), fmax(x, y));
}
static I enc_sub(double x, double y) { double r = x - y; return mk(dn(r), up(r)); }
static I imul_pos(I a, I x) {         /* a * x for an interval x with x.lo >= 0 */
    if (a.lo >= 0.0) return mk(dn(a.lo * x.lo), up(a.hi * x.hi));
    if (a.hi <= 0.0) return mk(dn(a.lo * x.hi), up(a.hi * x.lo));
    return mk(dn(a.lo * x.hi), up(a.hi * x.hi));
}
static I horner(I x2, const I *c) {
    I acc = c[NT];
    int j;
    for (j = NT - 1; j >= 0; --j) acc = iadd(imul_pos(acc, x2), c[j]);
    return acc;
}

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

/* the ranges of cos and sin over [a, b] with a in A and b in B (a <= b): ends, plus interior multiples of pi/2 */
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
        I Pj = (jd >= 0.0) ? mk(dn(jd * PIO2_I.lo), up(jd * PIO2_I.hi)) : mk(dn(jd * PIO2_I.hi), up(jd * PIO2_I.lo));
        if (Pj.hi >= lo && Pj.lo <= hi) {
            int r = (int)(((j % 4) + 4) % 4);
            if (r == 0) *cmax = 1.0;
            else if (r == 2) *cmin = -1.0;
            else if (r == 1) *smax = 1.0;
            else *smin = -1.0;
        }
    }
    return 1;
}

typedef struct { double U, L, Sc; int smooth, mono, fail; } Result;

/* the box [lo, hi] in the coordinates phi(1), ..., phi(p - 1); phi(0) = 0 */
static void eval_box(const double *lo, const double *hi, Result *res) {
    double Lc[P], Hc[P], M[P], RAD[P];
    double sum_kept = 0.0, sum_rem = 0.0, sum_other = 0.0, sum_exact = 0.0, sum_low = 0.0, lin = 0.0, Sc = 0.0;
    I G[P], GI[P];
    int i, q, s, u, all_kept = 1;
    Lc[0] = Hc[0] = M[0] = RAD[0] = 0.0;
    for (i = 0; i < DIM; ++i) {
        Lc[i + 1] = lo[i]; Hc[i + 1] = hi[i];
        M[i + 1] = 0.5 * lo[i] + 0.5 * hi[i];
        if (M[i + 1] < lo[i]) M[i + 1] = lo[i];
        if (M[i + 1] > hi[i]) M[i + 1] = hi[i];
        RAD[i + 1] = up(fmax(M[i + 1] - lo[i], hi[i] - M[i + 1]));
    }
    for (i = 0; i < P; ++i) { G[i] = pt(0.0); GI[i] = pt(0.0); }
    res->fail = 0;
    for (q = 0; q < P; ++q) {
        I Abase[NU], Bbase[NU], Cbase[NU];
        double w[NU];
        for (u = 0; u < NU; ++u) {
            int a = AI[q][u], b = BI[q][u];
            Abase[u] = enc_sub(Lc[a], Hc[b]);
            Bbase[u] = enc_sub(Hc[a], Lc[b]);
            Cbase[u] = enc_sub(M[a], M[b]);
            w[u] = up(RAD[a] + RAD[b]);
        }
        for (s = 0; s < P; ++s) {
            I cc[NU], sc[NU], Ec, sumc = pt(0.0);
            double cmn[NU], cmx[NU], smn[NU], smx[NU], tmax = 0.0, tmin = 0.0, Emax, Emin, absmax;
            int keep, sigma;
            for (u = 0; u < NU; ++u) {
                int k = (2 * s * (u + 1)) % P;
                I A = isub(Abase[u], SHIFT_I[k]), B = isub(Bbase[u], SHIFT_I[k]), C = isub(Cbase[u], SHIFT_I[k]);
                if (!sincos_encl(C, &cc[u], &sc[u]) || !trig_ranges(A, B, &cmn[u], &cmx[u], &smn[u], &smx[u])) {
                    res->fail = 1; return;
                }
                sumc = iadd(sumc, cc[u]);
                tmax = up(tmax + cmx[u]);
                tmin = dn(tmin + cmn[u]);
            }
            Ec = iadd(pt(1.0), iscale(sumc, 2.0));
            Emax = up(1.0 + 2.0 * tmax);
            Emin = dn(1.0 + 2.0 * tmin);
            absmax = fmax(fabs(Emax), fabs(Emin));
            sum_exact = up(sum_exact + absmax);
            Sc += fabs(0.5 * Ec.lo + 0.5 * Ec.hi);
            keep = (Emin > 0.0) || (Emax < 0.0);
            sigma = (Emin > 0.0) ? 1 : -1;
            if (keep) {
                double sigE = (sigma > 0) ? Ec.hi : -Ec.lo;
                sum_low = dn(sum_low + ((sigma > 0) ? Emin : -Emax));
                sum_kept = up(sum_kept + sigE);
                for (u = 0; u < NU; ++u) {
                    int a = AI[q][u], b = BI[q][u];
                    sum_rem = up(sum_rem + up(w[u] * w[u]));
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
    for (i = 1; i < P; ++i) lin = up(lin + up(fmax(fabs(G[i].lo), fabs(G[i].hi)) * RAD[i]));
    {
        double Umix = up(up(up(up(sum_kept + lin) + sum_rem) + sum_other) / P2);
        double Uex = up(sum_exact / P2);
        res->U = fmin(Umix, Uex);
    }
    res->L = dn(sum_low / P2);
    res->Sc = Sc / P2;
    res->smooth = all_kept;
    res->mono = 0;
    if (all_kept)
        for (i = 1; i < P; ++i)
            if (GI[i].lo > 0.0 || GI[i].hi < 0.0) { res->mono = 1; break; }
}

/* the interval Hessian of P^2 S over a box on which every E keeps its sign (returns 0 otherwise) */
static int hess_box(const double *lo, const double *hi, I Hm[DIM][DIM]) {
    double Lc[P], Hc[P];
    int i, j, q, s, u;
    Lc[0] = Hc[0] = 0.0;
    for (i = 0; i < DIM; ++i) { Lc[i + 1] = lo[i]; Hc[i + 1] = hi[i]; }
    for (i = 0; i < DIM; ++i) for (j = 0; j < DIM; ++j) Hm[i][j] = pt(0.0);
    for (q = 0; q < P; ++q) {
        for (s = 0; s < P; ++s) {
            double cmn[NU], cmx[NU], smn[NU], smx[NU], tmax = 0.0, tmin = 0.0, Emax, Emin;
            int sigma;
            for (u = 0; u < NU; ++u) {
                int a = AI[q][u], b = BI[q][u], k = (2 * s * (u + 1)) % P;
                I A = isub(enc_sub(Lc[a], Hc[b]), SHIFT_I[k]), B = isub(enc_sub(Hc[a], Lc[b]), SHIFT_I[k]);
                if (!trig_ranges(A, B, &cmn[u], &cmx[u], &smn[u], &smx[u])) return 0;
                tmax = up(tmax + cmx[u]);
                tmin = dn(tmin + cmn[u]);
            }
            Emax = up(1.0 + 2.0 * tmax);
            Emin = dn(1.0 + 2.0 * tmin);
            if (!(Emin > 0.0 || Emax < 0.0)) return 0;
            sigma = (Emin > 0.0) ? 1 : -1;
            for (u = 0; u < NU; ++u) {
                int a = AI[q][u], b = BI[q][u];
                I T = iscale(mk(cmn[u], cmx[u]), -2.0 * sigma);      /* second derivative of 2 sigma cos(angle) */
                if (a >= 1) Hm[a - 1][a - 1] = iadd(Hm[a - 1][a - 1], T);
                if (b >= 1) Hm[b - 1][b - 1] = iadd(Hm[b - 1][b - 1], T);
                if (a >= 1 && b >= 1) {
                    Hm[a - 1][b - 1] = isub(Hm[a - 1][b - 1], T);
                    Hm[b - 1][a - 1] = isub(Hm[b - 1][a - 1], T);
                }
            }
        }
    }
    return 1;
}

/* the gradient of P^2 S at the point m, as intervals (returns 0 if some E has no certified sign there) */
static int grad_pt(const double *m, I g[DIM]) {
    double M[P];
    int i, q, s, u;
    M[0] = 0.0;
    for (i = 0; i < DIM; ++i) { M[i + 1] = m[i]; g[i] = pt(0.0); }
    for (q = 0; q < P; ++q) {
        for (s = 0; s < P; ++s) {
            I cc[NU], sc[NU], sumc = pt(0.0), Ec;
            int sigma;
            for (u = 0; u < NU; ++u) {
                int a = AI[q][u], b = BI[q][u], k = (2 * s * (u + 1)) % P;
                if (!sincos_encl(isub(enc_sub(M[a], M[b]), SHIFT_I[k]), &cc[u], &sc[u])) return 0;
                sumc = iadd(sumc, cc[u]);
            }
            Ec = iadd(pt(1.0), iscale(sumc, 2.0));
            if (!(Ec.lo > 0.0 || Ec.hi < 0.0)) return 0;
            sigma = (Ec.lo > 0.0) ? 1 : -1;
            for (u = 0; u < NU; ++u) {
                int a = AI[q][u], b = BI[q][u];
                if (a >= 1) g[a - 1] = iadd(g[a - 1], iscale(sc[u], -2.0 * sigma));
                if (b >= 1) g[b - 1] = iadd(g[b - 1], iscale(sc[u], 2.0 * sigma));
            }
        }
    }
    return 1;
}

/* is -Hm positive definite for every symmetric matrix in the interval matrix Hm?  (interval LDL^T, pivots > 0) */
static int negdef(I Hm[DIM][DIM], double *minpivot) {
    I A[DIM][DIM], L[DIM][DIM], D[DIM];
    int i, j, k;
    for (i = 0; i < DIM; ++i) for (j = 0; j < DIM; ++j) A[i][j] = ineg(Hm[i][j]);
    *minpivot = 1e300;
    for (i = 0; i < DIM; ++i) {
        for (j = 0; j <= i; ++j) {
            I s = A[i][j];
            for (k = 0; k < j; ++k) s = isub(s, imul(imul(L[i][k], L[j][k]), D[k]));
            if (i == j) {
                D[i] = s;
                if (s.lo < *minpivot) *minpivot = s.lo;
                if (!(s.lo > 0.0)) return 0;
            } else {
                L[i][j] = idiv_pos(s, D[j]);
            }
        }
    }
    return 1;
}

/* an approximate inverse (floating point, Gauss-Jordan); any matrix is valid in the Krawczyk operator */
static int approx_inverse(double Mx[DIM][DIM], double Y[DIM][DIM]) {
    double A[DIM][2 * DIM];
    int i, j, k;
    for (i = 0; i < DIM; ++i) for (j = 0; j < DIM; ++j) { A[i][j] = Mx[i][j]; A[i][DIM + j] = (i == j) ? 1.0 : 0.0; }
    for (k = 0; k < DIM; ++k) {
        int piv = k;
        for (i = k + 1; i < DIM; ++i) if (fabs(A[i][k]) > fabs(A[piv][k])) piv = i;
        if (A[piv][k] == 0.0) return 0;
        for (j = 0; j < 2 * DIM; ++j) { double t = A[k][j]; A[k][j] = A[piv][j]; A[piv][j] = t; }
        for (j = 0; j < 2 * DIM; ++j) if (j != k) A[k][j] /= A[k][k];
        A[k][k] = 1.0;
        for (i = 0; i < DIM; ++i) {
            if (i == k) continue;
            { double f = A[i][k]; for (j = 0; j < 2 * DIM; ++j) A[i][j] -= f * A[k][j]; }
        }
    }
    for (i = 0; i < DIM; ++i) for (j = 0; j < DIM; ++j) Y[i][j] = A[i][DIM + j];
    return 1;
}

typedef struct {
    double m[DIM], Blo[DIM], Bhi[DIM], Xlo[DIM], Xhi[DIM];
    int eps, alpha, t, k[DIM], n[DIM];
    double Lval, Uval, minpivot_B, kraw_margin;
    int smooth_ok, negdef_ok, kraw_ok, image_ok;
} Cand;

static Cand CAND[MAXC];
static int NCAND;
static double RHO, EPSK, S_LO;

static void certify(Cand *c) {
    Result r;
    I HB[DIM][DIM], HX[DIM][DIM], g[DIM];
    double Mx[DIM][DIM], Y[DIM][DIM];
    int i, j, k;
    for (i = 0; i < DIM; ++i) {
        c->Blo[i] = dn(c->m[i] - RHO); c->Bhi[i] = up(c->m[i] + RHO);
        c->Xlo[i] = dn(c->m[i] - EPSK); c->Xhi[i] = up(c->m[i] + EPSK);
    }
    eval_box(c->Blo, c->Bhi, &r);
    c->smooth_ok = (!r.fail && r.smooth);
    c->negdef_ok = c->smooth_ok && hess_box(c->Blo, c->Bhi, HB) && negdef(HB, &c->minpivot_B);
    c->kraw_ok = 0;
    c->kraw_margin = -1.0;
    if (c->negdef_ok && grad_pt(c->m, g) && hess_box(c->Xlo, c->Xhi, HX)) {
        I K[DIM];
        int inside = 1;
        double margin = 1e300;
        for (i = 0; i < DIM; ++i) for (j = 0; j < DIM; ++j) Mx[i][j] = 0.5 * HX[i][j].lo + 0.5 * HX[i][j].hi;
        if (approx_inverse(Mx, Y)) {
            for (i = 0; i < DIM; ++i) {
                I Yg = pt(0.0), acc;
                for (j = 0; j < DIM; ++j) Yg = iadd(Yg, imul(pt(Y[i][j]), g[j]));
                acc = isub(pt(c->m[i]), Yg);
                for (j = 0; j < DIM; ++j) {
                    I YH = pt(0.0), Dj = mk(dn(c->Xlo[j] - c->m[j]), up(c->Xhi[j] - c->m[j]));
                    for (k = 0; k < DIM; ++k) YH = iadd(YH, imul(pt(Y[i][k]), HX[k][j]));
                    acc = iadd(acc, imul(isub(pt(i == j ? 1.0 : 0.0), YH), Dj));
                }
                K[i] = acc;
                if (!(K[i].lo > c->Xlo[i] && K[i].hi < c->Xhi[i])) inside = 0;
                margin = fmin(margin, fmin(K[i].lo - c->Xlo[i], c->Xhi[i] - K[i].hi));
            }
            c->kraw_ok = inside;
            c->kraw_margin = margin;
        }
    }
    /* S(phi_c*) is the maximum of S over B_c, so it is at least S(m) (m is in B_c) and at most the bound on X_c */
    eval_box(c->m, c->m, &r);
    c->Lval = r.L;
    eval_box(c->Xlo, c->Xhi, &r);
    c->Uval = r.U;
}

/* does the symmetry g_c map X_0 into B_c?  psi_x = eps (X0[(alpha x + t) mod p] - X0[t]) + 2 pi k_x / p + 2 pi n_x */
static int image_inside(const Cand *c0, const Cand *c) {
    I X0[P];
    int x;
    X0[0] = pt(0.0);
    for (x = 1; x < P; ++x) X0[x] = mk(c0->Xlo[x - 1], c0->Xhi[x - 1]);
    for (x = 1; x < P; ++x) {
        int a = (c->alpha * x + c->t) % P;
        I d = isub(X0[a], X0[c->t]);
        if (c->eps < 0) d = ineg(d);
        d = iadd(d, SHIFT_I[c->k[x - 1]]);
        d = iadd(d, imul(pt((double)c->n[x - 1]), TWO_PI_I));
        if (!(d.lo >= c->Blo[x - 1] && d.hi <= c->Bhi[x - 1])) return 0;
    }
    return 1;
}

typedef struct { double lo[DIM], hi[DIM]; } Box;
typedef struct { long long boxes, by_bound, by_mono, by_cube, fails, stuck, overflow; double maxc; int aborted; } Stats;

static int inside_some_B(const Box *b) {
    int c, i;
    for (c = 0; c < NCAND; ++c) {
        int in = 1;
        for (i = 0; i < DIM; ++i)
            if (!(b->lo[i] >= CAND[c].Blo[i] && b->hi[i] <= CAND[c].Bhi[i])) { in = 0; break; }
        if (in) return 1;
    }
    return 0;
}

#define STACKMAX 100000
#define LIMIT 4000000000LL

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
        if (r.fail) { st->fails++; continue; }
        if (r.Sc > st->maxc) st->maxc = r.Sc;
        if (r.U < S_LO) { st->by_bound++; continue; }
        if (r.mono) { st->by_mono++; continue; }
        if (inside_some_B(&b)) { st->by_cube++; continue; }
        j = 0;
        for (i = 0; i < DIM; ++i) if (b.hi[i] - b.lo[i] > wmax) { wmax = b.hi[i] - b.lo[i]; j = i; }
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
    int i, q, u;
    FOURU = 2.0 * DBL_EPSILON;
    ETA = 4.0 * B2D(1ULL);
    P2 = (double)(P * P);
    PI_I = mk(B2D(PI_LO_B), B2D(PI_HI_B));
    TWO_PI_I = mk(B2D(TWO_PI_LO_B), B2D(TWO_PI_HI_B));
    PIO2_I = mk(B2D(PIO2_LO_B), B2D(PIO2_HI_B));
    TWO_PI_HI = TWO_PI_I.hi;
    PIP_HI = up(PI_I.hi / (double)P);
    for (i = 0; i < P; ++i) SHIFT_I[i] = idiv_pos(imul(TWO_PI_I, pt((double)i)), pt((double)P));
    for (i = 0; i <= NT; ++i) {
        COSC_I[i] = mk(B2D(COSC_LO_B[i]), B2D(COSC_HI_B[i]));
        SINC_I[i] = mk(B2D(SINC_LO_B[i]), B2D(SINC_HI_B[i]));
    }
    REMC = B2D(REMC_HI_B);
    REMS = B2D(REMS_HI_B);
    RMAX = B2D(RMAX_B);
    for (q = 0; q < P; ++q)
        for (u = 0; u < NU; ++u) { AI[q][u] = (q + u + 1) % P; BI[q][u] = ((q - u - 1) % P + P) % P; }
}

static int read_candidates(const char *path) {
    FILE *f = fopen(path, "r");
    char key[32];
    int p, c, i;
    unsigned long long b;
    if (!f) return 0;
    if (fscanf(f, "%31s %d", key, &p) != 2 || p != P) return 0;
    if (fscanf(f, "%31s %llx", key, &b) != 2) return 0;
    RHO = B2D(b);
    if (fscanf(f, "%31s %llx", key, &b) != 2) return 0;
    EPSK = B2D(b);
    if (fscanf(f, "%31s %d", key, &NCAND) != 2 || NCAND < 1 || NCAND > MAXC) return 0;
    for (c = 0; c < NCAND; ++c) {
        Cand *cd = &CAND[c];
        for (i = 0; i < DIM; ++i) { if (fscanf(f, "%llx", &b) != 1) return 0; cd->m[i] = B2D(b); }
        if (fscanf(f, "%d %d %d", &cd->eps, &cd->alpha, &cd->t) != 3) return 0;
        for (i = 0; i < DIM; ++i) if (fscanf(f, "%d", &cd->k[i]) != 1) return 0;
        for (i = 0; i < DIM; ++i) if (fscanf(f, "%d", &cd->n[i]) != 1) return 0;
    }
    fclose(f);
    return 1;
}

static int boxtest(const char *in, const char *out) {
    FILE *fi = fopen(in, "r"), *fo = fopen(out, "w");
    unsigned long long v[2 * DIM];
    if (!fi || !fo) return 2;
    for (;;) {
        double lo[DIM], hi[DIM];
        Result r;
        int i, got = 0;
        for (i = 0; i < 2 * DIM; ++i) got += fscanf(fi, "%llx", &v[i]);
        if (got != 2 * DIM) break;
        for (i = 0; i < DIM; ++i) { lo[i] = B2D(v[i]); hi[i] = B2D(v[DIM + i]); }
        eval_box(lo, hi, &r);
        fprintf(fo, "%016llx %016llx %d %d %d\n", D2B(r.U), D2B(r.L), r.smooth, r.mono, r.fail);
    }
    fclose(fi); fclose(fo);
    return 0;
}

int main(int argc, char **argv) {
    int threads = 4, n = 0, k, done = 0, c, all_cert = 1, all_img = 1;
    double t0, s_hi = 1e300;
    static Box init[4096];
    Stats total;
    init_constants();
    SetPriorityClass(GetCurrentProcess(), BELOW_NORMAL_PRIORITY_CLASS);
    if (argc >= 4 && strcmp(argv[1], "boxtest") == 0) return boxtest(argv[2], argv[3]);
    if (argc < 3 || strcmp(argv[1], "prove") != 0) { fprintf(stderr, "usage: bb prove candidates [threads] | boxtest in out\n"); return 2; }
    if (argc >= 4) threads = atoi(argv[3]);
    if (!read_candidates(argv[2])) { printf("could not read %s\n", argv[2]); return 2; }
    printf("p = %d: %d candidate maximizers, certified boxes of half-width %.4g, Krawczyk boxes of half-width %.3g\n",
           P, NCAND, RHO, EPSK);
    S_LO = -1.0;
    for (c = 0; c < NCAND; ++c) {
        certify(&CAND[c]);
        CAND[c].image_ok = (c == 0) ? 1 : image_inside(&CAND[0], &CAND[c]);
        if (!(CAND[c].smooth_ok && CAND[c].negdef_ok && CAND[c].kraw_ok)) all_cert = 0;
        if (!CAND[c].image_ok) all_img = 0;
        if (CAND[c].Lval > S_LO) S_LO = CAND[c].Lval;
        if (CAND[c].Uval < s_hi) s_hi = CAND[c].Uval;
    }
    {   /* the certified boxes must be pairwise disjoint, so the NCAND critical points are distinct */
        int c2, i;
        for (c = 0; c < NCAND; ++c)
            for (c2 = c + 1; c2 < NCAND; ++c2) {
                int overlap = 1;
                for (i = 0; i < DIM; ++i)
                    if (CAND[c].Bhi[i] < CAND[c2].Blo[i] || CAND[c2].Bhi[i] < CAND[c].Blo[i]) { overlap = 0; break; }
                if (overlap) { all_cert = 0; printf("certified boxes %d and %d overlap\n", c, c2); }
            }
    }
    {
        double minpiv = 1e300, minmarg = 1e300;
        for (c = 0; c < NCAND; ++c) { minpiv = fmin(minpiv, CAND[c].minpivot_B); minmarg = fmin(minmarg, CAND[c].kraw_margin); }
        printf("certified: %s (signs fixed, -Hessian positive definite on every B_c [smallest pivot %.4g], Krawczyk "
               "contraction on every X_c [smallest margin %.3g]); symmetry images of X_0 inside every B_c: %s\n",
               all_cert ? "all" : "NOT ALL", minpiv, minmarg, all_img ? "yes" : "NO");
    }
    printf("S at the maximizer lies in [%.17g, %.17g]\n", S_LO, s_hi);
    /* the first grid: phi(1), phi(2) in [-pi/p, pi/p] (2 pieces each), the others in [0, 2 pi] (4 pieces each) */
    {
        double e1[3], e3[5];
        int idx[DIM], i, total_boxes = 1;
        e1[0] = -PIP_HI; e1[1] = 0.0; e1[2] = PIP_HI;
        e3[0] = 0.0; e3[4] = TWO_PI_HI; e3[2] = 0.5 * TWO_PI_HI; e3[1] = 0.25 * TWO_PI_HI; e3[3] = 0.75 * TWO_PI_HI;
        for (i = 0; i < DIM; ++i) total_boxes *= (i < 2) ? 2 : 4;
        for (k = 0; k < total_boxes; ++k) {
            int rem = k;
            for (i = 0; i < DIM; ++i) { int base = (i < 2) ? 2 : 4; idx[i] = rem % base; rem /= base; }
            for (i = 0; i < DIM; ++i) {
                if (i < 2) { init[n].lo[i] = e1[idx[i]]; init[n].hi[i] = e1[idx[i] + 1]; }
                else { init[n].lo[i] = e3[idx[i]]; init[n].hi[i] = e3[idx[i] + 1]; }
            }
            ++n;
        }
    }
    memset(&total, 0, sizeof(total));
    total.maxc = -1.0;
    omp_set_num_threads(threads);
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
                if (n >= 64 && done % (n / 16) == 0) {
                    fprintf(stderr, "  progress: %d/%d first-grid boxes done, %.0f s\n", done, n, omp_get_wtime() - t0);
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
    printf("boxes %lld by_bound %lld by_monotone %lld by_certified_box %lld fails %lld stuck %lld overflow %lld aborted %d\n",
           total.boxes, total.by_bound, total.by_mono, total.by_cube, total.fails, total.stuck, total.overflow, total.aborted);
    printf("max_center_S %.16g S_LO %.16g seconds %.1f threads %d\n", total.maxc, S_LO, omp_get_wtime() - t0, threads);
    if (all_cert && all_img && total.fails == 0 && total.stuck == 0 && total.overflow == 0 && !total.aborted)
        printf("VERDICT PASS: the maximum of S over diagonal states on %d levels lies in [%.17g, %.17g], attained exactly "
               "at the %d certified critical points in D, all images of one under the symmetries\n", P, S_LO, s_hi, NCAND);
    else
        printf("VERDICT FAIL\n");
    return 0;
}
