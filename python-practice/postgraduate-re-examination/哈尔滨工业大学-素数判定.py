# coding: utf-8
import math


def is_prime(val):
    if val <= 1:
        return False
    for item in range(2, math.floor(math.sqrt(val)) + 1):
        if val % item == 0:
            return False
    return True

n = int(input())

print('yes' if is_prime(n) else 'no')