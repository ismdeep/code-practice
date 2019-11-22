#!/bin/bash
mkdir -p bin
mkdir -p data

gcc 04-gendata.c -o ./bin/04-gendata
./bin/04-gendata > ./data/04-in.txt
gcc 04.c -o ./bin/04
cat ./data/04-in.txt
echo -------------------------------
./bin/04 < ./data/04-in.txt
