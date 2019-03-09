# coding: utf-8
# author: ismdeep
# dateime: 2019-03-08 17:37:51
# filename: b.py
# blog: https://ismdeep.com
n = int(input())
stra = input()
strb = input()
a = [0] * n
l0 = set()
l1 = set()
l2 = set()
l3 = set()
for i in range(n):
    if '0' == stra[i] and '0' == strb[i]:
        a[i] = 0
        l0.add(i + 1)
    if '1' == stra[i] and '0' == strb[i]:
        a[i] = 1
        l1.add(i + 1)
    if '0' == stra[i] and '1' == strb[i]:
        a[i] = 2
        l2.add(i + 1)
    if '1' == stra[i] and '1' == strb[i]:
        a[i] = 3
        l3.add(i + 1)
first = []
second = []
if len(l3) > 0:
    kill_cnt = min(len(l3), abs(len(l2) - len(l1)))
    if kill_cnt > 0:
        if len(l1) > len(l2):
            for i in range(kill_cnt):
                first.append(l1.pop())
                second.append(l3.pop())
        else:
            for i in range(kill_cnt):
                first.append(l3.pop())
                second.append(l2.pop())
    while len(l3) > 0:
        if len(l1) == 0 and len(l2) == 0:
            while len(l3) >= 2:
                first.append(l3.pop())
                second.append(l3.pop())
            # print('-1')
            # exit(0)
        if len(l1) > len(l2):
            first.append(l1.pop())
            second.append(l3.pop())
        elif len(l3) > 0 and len(l2) > 0:
            first.append(l3.pop())
            second.append(l2.pop())
        else:
            if len(l1) == 0 and len(l2) == 0 and len(l0) > 0:
                print('-1')
                exit(0)

if len(l1) != len(l2) and len(l0) == 0:
    print('-1')
    exit(0)

while len(l1) > 0 or len(l2) > 0:
    if len(l1) > 0 and len(l2) == 0 and len(l0) == 0:
        print('-1')
        exit(0)
    if len(l2) > 0 and len(l1) == 0 and len(l0) == 0:
        print('-1')
        exit(0)
    if len(l1) > 0 and len(l2) > 0:
        first.append(l1.pop())
        second.append(l2.pop())
    else:
        if len(l1) > len(l2) and len(l0) > 0:
            first.append(l0.pop())
            second.append(l1.pop())
        elif len(l1) < len(l2) and len(l0) > 0:
            first.append(l2.pop())
            second.append(l0.pop())

while len(l0) > 1:
    first.append(l0.pop())
    second.append(l0.pop())

print(*first)

# print('first  : ', *first)
# print('second : ', *second)
# print('l0', l0)
# print('l1', l1)
# print('l2', l2)
# print('l3', l3)
