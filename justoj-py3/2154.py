a = []
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))
print(a[0][0] + a[1][1] + a[2][2] + a[3][3], a[3][0] + a[2][1] + a[1][2] + a[0][3])
