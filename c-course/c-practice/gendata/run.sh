#!/bin/bash
rm -rfv build
mkdir -p build
cd build
cmake ..
make
./gendata

