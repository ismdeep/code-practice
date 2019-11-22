#!/bin/bash
mkdir -p bin
mkdir -p data

bash make-gendata.sh

./build-gendata/gendata min=1 max=100 count-min=1 count-max=20 seed=-1 > ./data/03-in.txt
cat ./data/03-in.txt
echo -----------------------------
gcc 03.c -o ./bin/03
./bin/03 < ./data/03-in.txt

