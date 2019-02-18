# coding: utf-8
# author: ismdeep
# dateime: 2019-02-18 10:38:40
# filename: 2148.py
# blog: https://ismdeep.com
a = list(map(int, input().split()))
max_val = max(a)
avg_val = sum(a) / len(a)
cnt = 0
for item in a:
    if item < avg_val:
        cnt += 1
print('%d %s %d' % (max_val, '{0:.2f}'.format(avg_val), cnt))