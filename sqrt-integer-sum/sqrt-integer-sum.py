# coding: utf-8
# author: ismdeep
# dateime: 2019-02-09 11:13:31
# filename: naive.py.py
# blog: https://ismdeep.com
import math
import time


def fast_algo(__n__):
    sqrt_n_1 = int(math.sqrt(__n__))
    sum_val = int((sqrt_n_1 - 1) * sqrt_n_1 * (2 * sqrt_n_1 - 1) / 3) + int(sqrt_n_1 * (sqrt_n_1 - 1) / 2)
    sum_val += (__n__ + 1) * sqrt_n_1
    sum_val -= sqrt_n_1 * sqrt_n_1 * sqrt_n_1
    return sum_val


def naive_algo(__n__):
    sum_val = 0
    for i in range(1, __n__ + 1):
        sum_val += int(math.sqrt(i))
    return sum_val


if __name__ == '__main__':
    n = 29374923749234802384
    start_1 = int(time.time() * 1000)
    print(fast_algo(n))
    print("cost: {%d}ms", int(time.time() * 1000) - start_1)
    start_2 = int(time.time() * 1000)
    print(naive_algo(n))
    print("cost: {%d}ms", int(time.time() * 1000) - start_2)
