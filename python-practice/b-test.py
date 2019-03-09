# coding: utf-8
# author: ismdeep
# dateime: 2019-03-08 18:43:03
# filename: b-test.py
# blog: https://ismdeep.com
import random

cnt0 = random.randint(0, 10)
cnt1 = random.randint(0, 10)
cnt2 = random.randint(0, 10)
cnt3 = random.randint(0, 10)
a = ''
b = ''
cnt3 += (cnt0 + cnt1 + cnt2 + cnt3) % 2
print(cnt0 + cnt1 + cnt2 + cnt3)
for i in range(cnt0):
    a += '0'
    b += '0'
for i in range(cnt1):
    a += '1'
    b += '0'
for i in range(cnt2):
    a += '0'
    b += '1'
for i in range(cnt3):
    a += '1'
    b += '1'
print(a)
print(b)