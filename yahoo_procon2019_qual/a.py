# coding: utf-8
# author: ismdeep
# dateime: 2019-02-09 20:04:13
# filename: a.py.py
# blog: https://ismdeep.com
s = input()
n = int(s.split()[0])
k = int(s.split()[1])
if 2 * k - 1 <= n:
    print('YES')
else:
    print('NO')
