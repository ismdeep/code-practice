@echo off
cls
gcc 01-gendata.c -o 01-gendata && 01-gendata > 03-in.txt && type 03-in.txt && echo ------------------------------- && gcc -fexec-charset=GBK 03.c -o 03 && 03 < 03-in.txt
pause
