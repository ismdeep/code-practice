# coding: utf-8
# author: ismdeep
# dateime: 2019-06-26 13:04:58
# filename: 哈尔滨工业大学-百鸡问题.py
# blog: https://ismdeep.com

n = int(input())
for x in range(0, 101):
    for y in range(0, 101 - x):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 <= n:
            print('x=%d,y=%d,z=%d' % (x, y, z))
