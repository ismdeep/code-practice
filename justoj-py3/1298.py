# coding: utf-8
# author: ismdeep
# dateime: 2019-03-04 13:57:01
# filename: 1298.py
# blog: https://ismdeep.com

trans = [
    ('S', 'a', 'U'),
    ('S', 'b', 'V'),
    ('U', 'a', 'Q'),
    ('U', 'b', 'V'),
    ('V', 'a', 'U'),
    ('V', 'b', 'Q'),
    ('Q', 'a', 'Q'),
    ('Q', 'b', 'Q')
]
start_state = 'S'
terminals = ['Q']


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
