#!/bin/bash
mkdir -p bin
mkdir -p data
rm  -rfv build-gendata
mkdir -p build-gendata
cd build-gendata
cmake ../../gendata
make
cd ..
./build-gendata/gendata count-min=2 count-max=2 output-count=0 > ./data/01-in.txt
cat ./data/01-in.txt
echo ---------------------------
gcc 01.c -o ./bin/01
./bin/01 < ./data/01-in.txt

