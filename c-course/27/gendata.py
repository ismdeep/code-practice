# coding: utf-8

import random

n = random.randint(2, 100)
print(n)
a = []
for i in range(n):
    a.append(random.randint(1, 100))
print(*a)
