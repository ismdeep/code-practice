#!/bin/bash
mkdir -p bin
mkdir -p data
gcc 06-gendata.c -o ./bin/06-gendata
./bin/06-gendata > ./data/06-in.txt
cat ./data/06-in.txt
echo -------------------------------
gcc 06.c -o ./bin/06
./bin/06 < ./data/06-in.txt

