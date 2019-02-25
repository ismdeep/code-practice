# coding: utf-8
# author: ismdeep
# dateime: 2019-02-25 13:05:14
# filename: 2152.py
# blog: https://ismdeep.com
a = []
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))
max_value = a[0][0]
max_i, max_j = 0, 0

for i in range(len(a)):
    line = a[i]
    for j in range(len(line)):
        if max_value < a[i][j]:
            max_value = a[i][j]
            max_i, max_j = i, j

print("%d row=%d col=%d" % (max_value, max_i + 1, max_j + 1))
