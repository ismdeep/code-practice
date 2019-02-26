# coding: utf-8
# author: ismdeep
# dateime: 2019-02-26 14:16:55
# filename: 2159.py
# blog: https://ismdeep.com


def is_leap_year(_year_):
    return True if _year_ % 400 == 0 or (_year_ % 4 == 0 and _year_ % 100 != 0) else False


day_cnt = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
y, m, d = map(int, input().split())
cnt = d
for i in range(m):
    cnt += day_cnt[i]
if is_leap_year(y) and m > 2:
    cnt += 1
print(d)

