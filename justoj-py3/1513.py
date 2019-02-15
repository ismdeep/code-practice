# coding: utf-8
# author: ismdeep
# dateime: 2019-02-15 23:31:02
# filename: 32 2.py
# blog: https://ismdeep.com
n, k = map(int, input().split(' '))
mod_val = 10 ** k
tmp = n % mod_val
_ = set()
_.add(tmp)
found = False
cnt = 1
while not found:
    tmp = tmp * n
    tmp = tmp % mod_val
    if tmp in _:
        found = True
    else:
        _.add(tmp)
    cnt += 1
print(cnt - 1)