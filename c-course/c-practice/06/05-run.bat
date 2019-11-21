@echo off
cls
gcc 05-gendata.c -o 05-gendata
05-gendata > 05-in.txt
type 05-in.txt
echo -------------------------------
gcc -fexec-charset=GBK 05.c -o 05
05 < 05-in.txt
pause
