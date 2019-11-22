#!/bin/bash
rm -rfv build-gendata
mkdir build-gendata
cd build-gendata
cmake ../../gendata
make

