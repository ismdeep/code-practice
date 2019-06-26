# coding: utf-8
# author: ismdeep
# dateime: 2019-06-26 14:00:01
# filename: 哈尔滨工业大学-找x.py
# blog: https://ismdeep.com
n = int(input())
a = list(map(int, input().strip().split()))
x = int(input())
_index_ = -1
for i in range(n):
    if x == a[i]:
        _index_ = i
print(_index_)
