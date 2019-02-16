# coding: utf-8
# author: ismdeep
# dateime: 2019-02-16 12:45:16
# filename: 1910.py
# blog: https://ismdeep.com
n = int(input())
for i in range(n):
    AH, AM, AS, BH, BM, BS = map(int, input().split(' '))
    AH += BH
    AM += BM
    AS += BS
    AM += int(AS / 60)
    AS %= 60
    AH += int(AM / 60)
    AM %= 60
    print(AH, AM, AS)
