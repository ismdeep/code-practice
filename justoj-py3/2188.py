# coding: utf-8
# author: ismdeep
# dateime: 2019-02-23 15:16:11
# filename: 2188.py
# blog: https://ismdeep.com
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

s = ['三', '四', '五', '六', '日', '一', '二']
n = int(input())
print('%d天后星期%s' % (n, s[n % 7]))
