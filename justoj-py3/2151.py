# coding: utf-8
# author: ismdeep
# dateime: 2019-02-21 08:29:17
# filename: 2151.py
# blog: https://ismdeep.com
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
print(a[k-1], a[len(a) - k])
