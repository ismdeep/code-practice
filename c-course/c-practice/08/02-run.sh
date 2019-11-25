#!/bin/bash
mkdir -p bin
mkdir -p data
rm  -rfv build-gendata
mkdir -p build-gendata
cd build-gendata
cmake ../../gendata
make
cd ..
./build-gendata/gendata count-min=2 count-max=20 output-count=1 > ./data/02-in.txt
sleep 1
./build-gendata/gendata count-min=1 count-max=1 output-count=0 >> ./data/02-in.txt
cat ./data/02-in.txt
echo ---------------------------
gcc 02.c -o ./bin/02
./bin/02 < ./data/02-in.txt

