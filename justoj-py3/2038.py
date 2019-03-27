# coding: utf-8
# author: ismdeep
# dateime: 2019-03-27 13:52:19
# filename: 2038.py
# blog: https://ismdeep.com
while True:
    try:
        s = input().strip()
        s = list(s)
        cnt = 0
        for i in range(len(s) - 1):
            if s[i] == 'Y' and s[i+1] == 'S':
                s[i] = 'A'
                s[i+1] = 'A'
                cnt += 1
        s = ''.join(s)
        if s.find('YY') >= 0 or s.find('SS') >= 0:
            cnt += 1
        print(cnt)
    except Exception as e:
        break