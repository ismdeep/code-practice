# coding: utf-8
# author: ismdeep
# dateime: 2019-02-09 20:19:18
# filename: c.py
# blog: https://ismdeep.com

(k, a, b) = map(int, input().split())

if a + 1 < b:
    k = k - (a - 1)
    ans = a
    ans += int(k / 2) * (b - a)
    ans += (k % 2)
    print(ans)
else:
    print(k + 1)