while True:
    try:
        a = list(map(int, input().split()))
        print(max(a))
    except:
        exit(0)
