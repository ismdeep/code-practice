# coding: utf-8
# author: ismdeep
# dateime: 2019-02-18 10:29:10
# filename: 2147.py
# blog: https://ismdeep.com
a = list(map(int, input().split()))
a.sort()
ans = sum(a)
ans -= a[0]
ans -= a[len(a) - 1]
ans = int(ans / (len(a) - 2))
print(ans)
