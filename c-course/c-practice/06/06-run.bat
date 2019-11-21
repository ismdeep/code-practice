@echo off
cls
gcc 06-gendata.c -o 06-gendata
06-gendata > 06-in.txt
type 06-in.txt
echo -------------------------------
gcc -fexec-charset=GBK 06.c -o 06
06 < 06-in.txt
pause
