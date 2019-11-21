#!/bin/bash

gcc 01-gendata.c -o 01-gendata
./01-gendata > 01-in.txt
cat 01-in.txt
echo -------------------------------
gcc -fexec-charset=UTF-8 01.c -o 01
./01 < 01-in.txt

read -p ""
