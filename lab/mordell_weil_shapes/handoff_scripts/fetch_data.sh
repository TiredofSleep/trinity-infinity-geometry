#!/bin/sh
# Rebuild the data layout the Part F scripts expect. Run from an empty working directory.
# Source: J. Cremona's ecdata (github.com/JohnCremona/ecdata), allgens tables, conductors 1 to 499 999.
# Layout:  ecdata/ (0-99 999)   ec2/ (100 000-299 999)   ec3/ (300 000-499 999; run the analysis scripts from here)
set -e
base=https://raw.githubusercontent.com/JohnCremona/ecdata/master/allgens
mkdir -p ecdata ec2 ec3
curl -sS -o ecdata/allgens.00000-09999 $base/allgens.00000-09999
for k in 1 2 3 4 5 6 7 8 9; do curl -sS -o ecdata/allgens.${k}0000-${k}9999 $base/allgens.${k}0000-${k}9999; done
for k in $(seq 10 29); do curl -sS -o ec2/allgens.${k}0000-${k}9999 $base/allgens.${k}0000-${k}9999; done
for k in $(seq 30 49); do curl -sS -o ec3/allgens.${k}0000-${k}9999 $base/allgens.${k}0000-${k}9999; done
echo "Then: (cd ecdata && python3 triangle_shapes_full.py)  -> shapes_full.json"
echo "      in ec2 and ec3 run the same script with the output name changed to shapes_100k_300k.json / shapes_300k_500k.json"
echo "      in ec3: periods.py, egg.py, then the analysis scripts."
