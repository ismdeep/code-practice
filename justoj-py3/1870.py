import math


def is_prime(val):
    for i in range(2, int(math.sqrt(val)) + 1):
        if val % i == 0:
            return False
    return True


n = int(input())
print(1 if is_prime(n) else 0)
