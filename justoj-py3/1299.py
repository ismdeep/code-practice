# coding: utf-8
# author: ismdeep
# dateime: 2019-03-04 14:17:43
# filename: 1299.py
# blog: https://ismdeep.com
trans = [
    ('T', '0', 'T'),
    ('T', '1', 'T'),
    ('T', '2', 'T'),
    ('T', '3', 'T'),
    ('T', '4', 'T'),
    ('T', '5', 'T'),
    ('T', '6', 'T'),
    ('T', '7', 'T'),
    ('T', '8', 'T'),
    ('T', '9', 'T')
]
start_state = 'T'
terminals = ['T']


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
    while True:
        try:
            s = input()
            s = s.strip()
            print('accept' if dfa(s) else 'not accept')
        except:
            exit(0)


if __name__ == '__main__':
    main()
