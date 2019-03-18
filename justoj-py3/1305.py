# coding: utf-8
# author: ismdeep
# dateime: 2019-03-18 16:45:03
# filename: 1305.py
# blog: https://ismdeep.com
from queue import Queue


def convert_nfa_to_dfa(_trans_, _start_state_, _terminals_):
    link_set = []
    for _from_, _link_, _to_ in _trans_:
        if _link_ not in link_set:
            link_set.append(_link_)
    done = set()
    done.add(str([_start_state_]))
    q = Queue()
    q.put(str([_start_state_]))
    dfa_trans = []
    while q.qsize() > 0:
        states = eval(q.get())
        for _todo_link_ in link_set:
            next_states = []
            for state in states:
                for _from_, _link_, _to_ in _trans_:
                    if _from_ == state and _link_ == _todo_link_:
                        next_states.append(_to_)
            next_states2 = []
            for item in next_states:
                if item not in next_states2:
                    next_states2.append(item)
            next_states2.sort()
            dfa_trans.append((str(states), _todo_link_, str(next_states2)))
            if str(next_states2) not in done:
                q.put(str(next_states2))
                done.add(str(next_states2))
    return dfa_trans


def extract_trans(_trans_):
    trans = []
    for tran in _trans_:
        trans.append((tran[0], tran[1], tran[2]))
    return trans


def state_to_str(arr):
    ans = '{'
    for item in arr:
        if not ans == '{':
            ans += ','
        ans += str(item)
    ans += '}'
    ans = ans.replace('{A,S}', '{A}')
    ans = ans.replace('{B,S}', '{B}')
    ans = ans.replace('{A,B,S}', '{Q}')
    return ans


def dfa(_str_, _start_state_, _trans_, _terminals_):
    cur_state = str([_start_state_])
    routines = [cur_state]
    for _item_ in _str_:
        found = False
        new_state = ''
        for (_from_, _link_, _to_) in _trans_:
            if _from_ == cur_state and _link_ == _item_:
                found = True
                new_state = _to_
        if not found:
            return False, routines
        cur_state = new_state
        routines.append(cur_state)
    cur_state = eval(cur_state)
    terminals_in_state = False

    for terminal in _terminals_:
        if terminal in cur_state:
            terminals_in_state = True
    return (True, routines) if terminals_in_state else (False, routines)


###########################################################################


def main():
    trans = extract_trans(['SaS', 'SbS', 'SaA', 'AaB', 'AbB'])
    start_state = 'S'
    terminals = ['B']
    trans = convert_nfa_to_dfa(trans, start_state, terminals)

    while True:
        try:
            s = input().strip()
            status, routines = dfa(s, start_state, trans, terminals)
            for i in range(len(s) + 1 - len(routines)):
                routines.append('[]')
            print(state_to_str(eval(routines[0])), end='')
            for i in range(len(s)):
                print('-' + s[i] + '->', end='')
                print(state_to_str(eval(routines[i + 1])), end='')
            print()
            if status:
                print('accept')
            else:
                print('not accept')
        except:
            exit(0)


if __name__ == '__main__':
    main()

