trans = [
    ('S', '"', 'T')
    , ('S', '\'', 'T')
    , ('S', ';', 'T')
    , ('S', ',', 'T')
    , ('S', ':', 'T')
    , ('S', '(', 'T')
    , ('S', ')', 'T')
    , ('S', '[', 'T')
    , ('S', ']', 'T')
    , ('S', '{', 'T')
    , ('S', '}', 'T')
    , ('S', '#', 'T')
]
start_state = 'S'
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
            if '' is s:
                continue
            print('accept' if dfa(s) else 'not accept')
        except:
            exit(0)


if __name__ == '__main__':
    main()
