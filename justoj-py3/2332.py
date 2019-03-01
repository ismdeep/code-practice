# coding: utf-8
# author: ismdeep
# dateime: 2019-03-01 14:33:39
# filename: 2332.py
# blog: https://ismdeep.com

n = int(input())
ans = [0] * n
for i in range(n):
    lang, val = input().split()
    ans[int(val) - 1] = lang
for item in ans:
    print(item)
