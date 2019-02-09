# coding: utf-8
# author: ismdeep
# dateime: 2019-02-09 15:14:27
# filename: 2337.py
# blog: https://ismdeep.com
l = []
l.append(input())
l.append(input())
l.append(input())
s = input()
index = 0
for item in l:
    index += 1
    if item.find(s) >= 0:
        print(index, item.find(s) + 1)
