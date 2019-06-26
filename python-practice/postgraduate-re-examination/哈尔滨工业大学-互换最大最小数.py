# coding: utf-8
# author: ismdeep
# dateime: 2019-06-26 13:12:12
# filename: 哈尔滨工业大学-互换最大最小数.py
# blog: https://ismdeep.com
n = int(input())
a = list(map(int, input().strip().split()))
min_index = 0
max_index = 0
for i in range(n):
    if a[i] < a[min_index]:
        min_index = i
    if a[i] > a[max_index]:
        max_index = i
a[min_index], a[max_index] = a[max_index], a[min_index]
print(*a)
