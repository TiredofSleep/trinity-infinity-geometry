// anneal8_fullbinary.js: sample "fully binary" 8x8 magic squares on 0..63. Every one of the six bit
// planes has exactly four 1s in every row, every column and both diagonals; that makes the square
// magic (each line sums to 4 * 63 = 252). This is the order-8 analog of the 528 fully binary 4x4 squares.
// Simulated annealing over swaps, with random restarts. Not a uniform sample.
// Usage: node anneal8_fullbinary.js COUNT SEED > out.txt
const want = parseInt(process.argv[2] || "10"), seed0 = BigInt(process.argv[3] || "12345");
let s = (Number(seed0 % 4294967291n) >>> 0) || 2463534242;
function rng() { s ^= s << 13; s >>>= 0; s ^= s >>> 17; s ^= s << 5; s >>>= 0; return s; }
function urand() { return rng() / 4294967296; }
const g = new Int32Array(64), rb = new Int32Array(48), cb = new Int32Array(48), d1 = new Int32Array(6), d2 = new Int32Array(6);
function add(p, v, sg) {
  const i = p >> 3, j = p & 7;
  for (let k = 0; k < 6; k++) {
    const b = ((v >> k) & 1) * sg;
    rb[i * 6 + k] += b; cb[j * 6 + k] += b;
    if (i === j) d1[k] += b;
    if (i + j === 7) d2[k] += b;
  }
}
function rowc(i) { let c = 0; for (let k = 0; k < 6; k++) { const d = rb[i * 6 + k] - 4; c += d * d; } return c; }
function colc(j) { let c = 0; for (let k = 0; k < 6; k++) { const d = cb[j * 6 + k] - 4; c += d * d; } return c; }
function diagc() { let c = 0; for (let k = 0; k < 6; k++) { const a = d1[k] - 4, b = d2[k] - 4; c += a * a + b * b; } return c; }
function local(ia, ja, ib, jb) {
  let c = rowc(ia) + colc(ja) + diagc();
  if (ib !== ia) c += rowc(ib);
  if (jb !== ja) c += colc(jb);
  return c;
}
let found = 0;
const out = [];
while (found < want) {
  for (let p = 0; p < 64; p++) g[p] = p;
  for (let p = 63; p > 0; p--) { const q = rng() % (p + 1); const t = g[p]; g[p] = g[q]; g[q] = t; }
  rb.fill(0); cb.fill(0); d1.fill(0); d2.fill(0);
  for (let p = 0; p < 64; p++) add(p, g[p], 1);
  let c = 0; for (let i = 0; i < 8; i++) c += rowc(i) + colc(i); c += diagc();
  let temp = 4.0;
  for (let it = 0; it < 30000000 && c > 0; it++) {
    const a = rng() & 63, b = rng() & 63; if (a === b) continue;
    const ia = a >> 3, ja = a & 7, ib = b >> 3, jb = b & 7, va = g[a], vb = g[b];
    const before = local(ia, ja, ib, jb);
    add(a, va, -1); add(b, vb, -1); add(a, vb, 1); add(b, va, 1);
    const delta = local(ia, ja, ib, jb) - before;
    if (delta <= 0 || urand() < Math.exp(-delta / temp)) { g[a] = vb; g[b] = va; c += delta; }
    else { add(a, vb, -1); add(b, va, -1); add(a, va, 1); add(b, vb, 1); }
    temp *= 0.9999997; if (temp < 0.15) temp = 0.15;
  }
  if (c === 0) { process.stdout.write(Array.from(g).join(" ") + "\n"); found++; }
}
