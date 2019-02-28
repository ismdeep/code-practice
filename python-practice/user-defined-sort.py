# coding: utf-8
# author: ismdeep
# dateime: 2019-02-28 13:54:52
# filename: user-defined-sorted.py
# blog: https://ismdeep.com


def cmp_fun(a, b):
    return True if a[1] > b[1] else False


def udsort(_list_, cmp=None, reverse=False):
    for i in range(len(_list_) - 1, 0, -1):
        max_i = i
        for j in range(0, i):
            if cmp is None:
                if reverse:
                    if _list_[j] < _list_[max_i]:
                        max_i = j
                else:
                    if _list_[j] > _list_[max_i]:
                        max_i = j
            else:
                if reverse:
                    if cmp(_list_[j], _list_[i]):
                        max_i = j
                else:
                    if not cmp(_list_[j], _list_[i]):
                        max_i = j
        if max_i != i:
            tmp = _list_[max_i]
            _list_[max_i] = _list_[i]
            _list_[i] = tmp


def main():
    l = [1, 2, 3, 4]
    udsort(l)
    print(l)


if __name__ == '__main__':
    main()
