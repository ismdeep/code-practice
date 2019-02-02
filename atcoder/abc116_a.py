s = input().split(" ")
item = [int(i) for i in s]
item.sort()
print(int(item[0] * item[1] / 2))
