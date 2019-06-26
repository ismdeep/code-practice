# coding: utf-8
# author: ismdeep
# dateime: 2019-06-26 14:11:31
# filename: 哈尔滨工业大学-众数.py
# blog: https://ismdeep.com
a = list(map(int, input().strip().split()))
cnt = [0] * 11
for item in a:
    cnt[item] += 1
max_index = 10
for i in range(10, 0, -1):
    if cnt[i] >= cnt[max_index]:
        max_index = i
print(max_index)
