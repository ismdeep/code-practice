#!/bin/bash
rm -rfv build
mkdir -p build
cd build
cmake ..
make
./gendata min=1 max=100 seed=1 count=10 ouput-count=1

