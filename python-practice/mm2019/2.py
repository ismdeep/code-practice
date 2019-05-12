# coding: utf-8
# author: ismdeep
# dateime: 2019-05-12 21:00:49
# filename: 2.py
# blog: https://ismdeep.com

ww, hh = 3000, 1500

woods = [(373, 201), (406, 229)]


ans = [(0,[])] * 10


def ans_sort(ans):
    for i in range(0, len(ans)):
        x = i
        for j in range(i + 1, len(ans)):
            if ans[j][0] > ans[x][0]:
                x = j
        ans[i], ans[x] = ans[x], ans[i]



def is_single(history):
    _ = set()
    for item in history:
        _.add(item[0])
        _.add(item[1])
    return True if len(_) <= 2 else False


def search(left_size, history):
    if left_size < 201:
        if is_single(history):
            return
        _sum_ = 0
        for item in history:
            _sum_ += item[0] * (hh // item[1]) * item[1]
        p = _sum_ / (ww * hh)
        tmp = [item for item in history]
        ans[9] = (p, tmp)
        ans_sort(ans)


    for wood in woods:
        if left_size > wood[0]:
            tmp = [item for item in history]
            tmp.append((wood[0], wood[1]))
            search(left_size - wood[0], tmp)
        if left_size > wood[1]:
            tmp = [item for item in history]
            tmp.append((wood[1], wood[0]))
            search(left_size - wood[1], tmp)


search(ww, [])

for item in ans:
    print(item)