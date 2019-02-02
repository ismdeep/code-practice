n = int(input())
lst = input().split(" ")
a = [int(item) for item in lst]
ans = 0
while sum(a) > 0:
    left = 0
    right = -1
    for i in range(len(a)):
        if not a[i] == 0:
            left = i
            break
    for i in range(left, len(a)):
        if a[i] == 0:
            right = i
            break
    if -1 == right:
        right = len(a)
    right = right - 1
    min_val = a[left]
    for i in range(left, right + 1):
        min_val = min(min_val, a[i])
    ans += min_val
    for i in range(left, right + 1):
        a[i] -= min_val
print(ans)
