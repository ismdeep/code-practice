s = int(input())
_ = set()

while not s in _:
    _.add(s)
    if 0 == s % 2:
        s = int(s / 2)
    else:
        s = 3 * s + 1
print(len(_) + 1)
