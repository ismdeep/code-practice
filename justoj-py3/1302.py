trans = [
    ('S', '!', 'A')
    , ('S', '=', 'A')
    , ('S', '*', 'A')
    , ('S', '/', 'A')
    , ('S', '%', 'A')
    , ('S', '^', 'A')
    , ('A', '=', 'J')
    , ('S', '+', 'B')
    , ('B', '+', 'J')
    , ('B', '=', 'J')
    , ('S', '-', 'C')
    , ('C', '=', 'J')
    , ('C', '-', 'H')
    , ('S', '>', 'D')
    , ('D', '>', 'G')
    , ('G', '=', 'J')
    , ('S', '<', 'E')
    , ('E', '<', 'F')
    , ('E', '=', 'J')
    , ('D', '=', 'J')
    , ('F', '<', 'J')
    , ('S', '&', 'K')
    , ('K', '&', 'L')
    , ('K', '=', 'J')
    , ('S', '|', 'M')
    , ('M', '|', 'N')
    , ('M', '=', 'J')
]
start_state = 'S'
terminals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']


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
