# coding: utf-8
# author: ismdeep
# dateime: 2019-02-16 12:54:13
# filename: 1911.py
# blog: https://ismdeep.com

n = int(input())
cnt = dict()
for i in range(n):
    val = int(input())
    if val not in cnt:
        cnt[val] = 0
    cnt[val] = cnt[val] + 1
max_cnt = 0
val = 0
keys = cnt.keys()
for key in keys:
    if cnt[key] > max_cnt:
        val = key
        max_cnt = cnt[key]
print(val)
print(max_cnt)

