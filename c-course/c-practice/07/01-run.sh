#!/bin/bash
mkdir -p bin
mkdir -p data
gcc 01-gendata.c -o ./bin/01-gendata
./bin/01-gendata > ./data/01-in.txt
cat ./data/01-in.txt
echo -------------------------------------
gcc 01.c -o ./bin/01 -lm
./bin/01 < ./data/01-in.txt

