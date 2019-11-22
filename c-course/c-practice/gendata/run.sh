#!/bin/bash
rm -rfv build
mkdir -p build
cd build
cmake ..
make
./gendata min=1 max=100 seed=-1 count-min=10 count-max=20 ouput-count=1
