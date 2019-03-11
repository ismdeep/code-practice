while True:
    a,b=map(int,input().split())
    if a is 0 and b is 0:
        exit(0)
    ans = []
    for i in range(100):
        if (a * 100 + i) % b == 0:
            ans.append('%02d' % i )
    print(*ans)
