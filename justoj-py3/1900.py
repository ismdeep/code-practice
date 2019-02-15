# coding: utf-8
# author: ismdeep
# dateime: 2019-02-15 23:46:16
# filename: 1900.py
# blog: https://ismdeep.com
while True:
    try:
        r = float(input())
        print('{0:.3f}'.format((3.1415926 * 4.0 / 3.0 * r ** 3 )))
    except:
        break
