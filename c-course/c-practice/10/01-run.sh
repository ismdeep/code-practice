#!/bin/bash
mkdir -p bin
gcc 01.c -o ./bin/01
md5 data1.txt
./bin/01 data1.txt data2.txt
md5 data2.txt
