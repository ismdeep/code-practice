# coding: utf-8
# author: ismdeep
# dateime: 2019-02-24 10:37:50
# filename: 1840.py
# blog: https://ismdeep.com
s = input()
ans = ''
for item in s:
    if 'a' <= item <= 'z' or 'A' <= item <= 'Z':
        ans += item
print(ans)
