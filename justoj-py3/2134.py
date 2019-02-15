# coding: utf-8
# author: ismdeep
# dateime: 2019-02-15 19:24:25
# filename: 2134.py
# blog: https://ismdeep.com
s = input()
s = s + input()
s = s + input()
s = s + input()
s = s + input()
cnt = [0, 0, 0, 0, 0]
for item in s:
    if 'A' <= item <= 'Z':
        cnt[0] += 1
    elif 'a' <= item <= 'z':
        cnt[1] += 1
    elif ' ' == item:
        cnt[2] += 1
    elif '0' <= item <= '9':
        cnt[3] += 1
    else:
        cnt[4] += 1
print(cnt[0])
print(cnt[1])
print(cnt[3])
print(cnt[2])
print(cnt[4])
