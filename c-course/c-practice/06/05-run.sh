#!/bin/bash
mkdir -p bin
mkdir -p data
gcc 05-gendata.c -o ./bin/05-gendata
./bin/05-gendata > ./data/05-in.txt
cat ./data/05-in.txt
echo -------------------------------
gcc 05.c -o ./bin/05
./bin/05 < ./data/05-in.txt

