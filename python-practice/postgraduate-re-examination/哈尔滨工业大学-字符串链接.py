# coding: utf-8

while True:
    try:
        a = input().split()
        print('%s%s' % (a[0], a[1]))
    except:
        exit(0)
