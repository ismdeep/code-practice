# coding: utf-8
# author: ismdeep
# dateime: 2019-02-09 20:08:40
# filename: b.py
# blog: https://ismdeep.com
a = [0, 0, 0, 0, 0]
s = input().split()
a[int(s[0])] += 1
a[int(s[1])] += 1
s = input().split()
a[int(s[0])] += 1
a[int(s[1])] += 1
s = input().split()
a[int(s[0])] += 1
a[int(s[1])] += 1

a.sort()

if 1 == a[1] and 1 == a[2] and 2 == a[3] and 2 == a[4]:
    print('YES')
else:
    print('NO')
