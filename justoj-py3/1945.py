n = int(input())
while n > 0:
    n -= 1
    a = list(map(int, input().split()))
    ans = []
    flag = a[0]
    for item in a[::-1]:
        if item < flag:
            ans.append(item)
    ans.append(flag)
    for item in a:
        if item > flag:
            ans.append(item)
    print(*ans)
