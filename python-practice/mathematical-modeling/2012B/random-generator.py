# coding: utf-8
# author: ismdeep
# dateime: 2019-04-27 09:04:10
# filename: random-generator.py
# blog: https://ismdeep.com

from random import Random
import os
import sys


def task_assignment_generator(seed=None):
    r = Random()
    if seed is not None:
        r.seed(seed)
    found = False
    ans = []
    while not found:
        task_cnt = [0] * 20
        ans = []
        for paper_index in range(500):
            b = []
            for val in range(20):
                if task_cnt[val] < 75:
                    b.append(val)
            r.shuffle(b)
            try:
                tmp = [b[0],b[1],b[2]]
                tmp.sort()
                ans.append((tmp[0], tmp[1], tmp[2]))
            except:
                found = False
                break
            task_cnt[b[0]] += 1
            task_cnt[b[1]] += 1
            task_cnt[b[2]] += 1
            found = True
    return ans


tasks = [0] * 20
seed = None
try:
    seed = int(sys.argv[1])
except:
    pass
ans = task_assignment_generator()
print(ans)
