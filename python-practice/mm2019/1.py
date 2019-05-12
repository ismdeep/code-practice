# coding: utf-8
# author: ismdeep
# dateime: 2019-05-12 20:43:12
# filename: server_a.py
# blog: https://ismdeep.com
w, h = 373, 201

max_value = 0.00
ans = []


def search(left_size, history):
    if left_size < h:
        sum = 0
        for item in history:
            if item == w:
                sum += w * (1500 // h) * h
            else:
                sum += h * (1500 // w) * w
        p = sum / (3000 * 1500)
        global max_value
        global ans
        if p > max_value:
            max_value = p
            ans = [item for item in history]
    if left_size > w:
        tmp = [item for item in history]
        tmp.append(w)
        search(left_size - w, tmp)
    if left_size > h:
        tmp = [item for item in history]
        tmp.append(h)
        search(left_size - h, tmp)


search(3000, [])
print(max_value)
print(ans)
