# coding: utf-8

perfect_numbers = [6, 28, 496, 8128]
n = int(input())
ans = []
for perfect_number in perfect_numbers:
    if perfect_number <= n:
        ans.append(perfect_number)
print(*ans)
