@echo off
cls
gcc 01-gendata.c -o 01-gendata && 01-gendata > 01-in.txt && type 01-in.txt && echo ------------------------------- && gcc -fexec-charset=GBK 01.c -o 01 && 01 < 01-in.txt
pause
