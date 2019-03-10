import math


def is_prime(val):
    for i in range(2, int(math.sqrt(val)) + 1):
        if val % i == 0:
            return False
    return True


n = int(input())
primes = []
for item in range(2, n + 1):
    if is_prime(item):
        primes.append(item)
print(*primes)
