@echo off
cls
gcc 04-gendata.c -o 04-gendata && 04-gendata > 04-in.txt && type 04-in.txt && echo ------------------------------- && gcc -fexec-charset=GBK 04.c -o 04 && 04 < 04-in.txt
pause
