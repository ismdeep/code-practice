# coding: utf-8
# author: ismdeep
# dateime: 2019-06-26 14:14:45
# filename: 哈尔滨工业大学-最大公约数.py
# blog: https://ismdeep.com

from math import gcd

a, b = map(int, input().strip().split())
print(gcd(a, b))
