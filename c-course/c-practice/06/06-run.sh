#!/bin/bash

gcc 06-gendata.c -o 06-gendata
./06-gendata > 06-in.txt
cat 06-in.txt
echo -------------------------------
gcc -fexec-charset=UTF-8 06.c -o 06
./06 < 06-in.txt

read -p ""