# coding: utf-8
# author: ismdeep
# dateime: 2019-06-26 14:02:23
# filename: 哈尔滨工业大学-判断三角形类型.py
# blog: https://ismdeep.com
import math
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

a = list(map(float, input().strip().split()))
a.sort()
x = math.sqrt(a[0] * a[0] + a[1] * a[1])
if a[2] > x + 0.00001:
    print("钝角三角形")
elif a[2] < x - 0.00001:
    print("锐角三角形")
else:
    print("直角三角形")
