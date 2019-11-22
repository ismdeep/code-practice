#!/bin/bash
mkdir -p bin
mkdir -p data

gcc 03-gendata.c -o ./bin/03-gendata
./bin/03-gendata > ./data/03-in.txt
gcc 03.c -o ./bin/03
cat ./data/03-in.txt
echo -------------------------------
./bin/03 < ./data/03-in.txt
