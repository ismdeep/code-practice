#!/bin/bash

gcc 05-gendata.c -o 05-gendata
./05-gendata > 05-in.txt
cat 05-in.txt
echo -------------------------------
gcc -fexec-charset=UTF-8 05.c -o 05
./05 < 05-in.txt

read -p ""