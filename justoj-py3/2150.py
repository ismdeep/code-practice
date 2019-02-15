# coding: utf-8
# author: ismdeep
# dateime: 2019-02-15 18:29:44
# filename: 2150.py
# blog: https://ismdeep.com
n, k = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
a.sort(reverse=True)
print(a[k-1])
