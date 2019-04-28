# coding: utf-8
# author: ismdeep
# dateime: 2019-04-28 10:16:12
# filename: cross-cnt-diff.py
# blog: https://ismdeep.com
ans = eval(input())
cross_cnt = dict()
for a, b, c in ans:
    if (a, b) not in cross_cnt:
        cross_cnt[(a, b)] = 0
    if (a, c) not in cross_cnt:
        cross_cnt[(a, c)] = 0
    if (b, c) not in cross_cnt:
        cross_cnt[(b, c)] = 0
    cross_cnt[(a, b)] += 1
    cross_cnt[(a, c)] += 1
    cross_cnt[(b, c)] += 1

min_val = 5000
max_val = 0

for item, cnt in cross_cnt:
    min_val = cnt if cnt < min_val else min_val
    max_val = cnt if cnt > max_val else max_val
print(max_val - min_val)
