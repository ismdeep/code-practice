# coding: utf-8
# author: ismdeep
# dateime: 2019-02-16 13:05:55
# filename: 1928.py
# blog: https://ismdeep.com


def is_p(val):
    s1 = str(val)
    s2 = s1[::-1]
    return True if s1 == s2 else False


def cnt_step(val):
    if is_p(val):
        return 0
    return 1 + cnt_step(val + int(str(val)[::-1]))


n = int(input())
for i in range(n):
    val = int(input())
    cnt = cnt_step(val)
    if cnt > 8:
        print(0)
    else:
        print(cnt)
