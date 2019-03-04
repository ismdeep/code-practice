# coding: utf-8
# author: ismdeep
# dateime: 2019-03-04 15:17:20
# filename: 1301.py
# blog: https://ismdeep.com
# coding: utf-8
# author: ismdeep
# dateime: 2019-03-04 14:17:43
# filename: 1299.py
# blog: https://ismdeep.com
trans = []
pre_trans = [
    ('S', 'd', 'A')
    , ('S', '.', 'D')
    , ('D', 'd', 'B')
    , ('A', 'd', 'A')
    , ('A', 'e', 'E')
    , ('A', '.', 'B')
    , ('B', 'd', 'B')
    , ('B', 'e', 'E')
    , ('E', '+', 'F')
    , ('E', '-', 'F')
    , ('E', 'd', 'C')
    , ('F', 'd', 'C')
    , ('C', 'd', 'C')
]
start_state = 'S'
terminals = ['A', 'B', 'C']


def dfa(_str_):
    state = start_state
    for item in _str_:
        found = False
        new_state = ''
        for (_from_, _link_, _to_) in trans:
            if _from_ == state and _link_ == item:
                found = True
                new_state = _to_
        if not found:
            return False
        state = new_state
    return True if state in terminals else False


def main():
    for _from_, _link_, _to_ in pre_trans:
        if _link_ is 'd':
            for item in '0123456789':
                trans.append((_from_, item, _to_))
        else:
            trans.append((_from_, _link_, _to_))
    while True:
        try:
            s = input()
            s = s.strip()
            if '' is s:
                continue
            print('accept' if dfa(s) else 'not accept')
        except:
            exit(0)


if __name__ == '__main__':
    main()
