# coding: utf-8
# author: ismdeep
# dateime: 2019-03-08 17:07:47
# filename: a.py
# blog: https://ismdeep.com
n = int(input())
a = list(map(int, input().split()))
v = []
prev = 0
cnt = 0
for item in a:
    if item == prev:
        cnt += 1
    else:
        if cnt > 0:
            v.append(cnt)
        cnt = 1
    prev = item
v.append(cnt)
ans = v[0]
try:
    max_ans = min(v[0], v[1]) * 2
    for i in range(len(v) - 1):
        if max_ans < min(v[i], v[i + 1]) * 2:
            max_ans = min(v[i], v[i + 1]) * 2
    print(max_ans)
except:
    print(0)

