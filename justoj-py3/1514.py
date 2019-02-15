# coding: utf-8
# author: ismdeep
# dateime: 2019-02-15 23:25:46
# filename: 1514.py
# blog: https://ismdeep.com
n = input()
a = list(map(int, input().split(' ')))
b = []
for item in a:
    if item not in b:
        b.append(item)
b.sort()
print(len(b))
print(*b)
