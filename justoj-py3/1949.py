n = int(input())
cnt = 0
for i in range(1, n + 1):
    if i % 7 == 0 or str(i).find('7') >= 0:
        cnt += 1
print(cnt)
