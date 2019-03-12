import queue


def state_to_str(arr):
    ans = '{'
    for item in arr:
        if not ans == '{':
            ans += ','
        ans += str(item)
    ans += '}'
    return ans


trans = []
pre_trans = [
    '0a0', '0b0', '0a3', '3a4', '4a4', '4b4', '0b1', '1b2', '2a2', '2b2'
]

dfa_trans = []
done = set()

start_state = '0'
terminals = ['2', '4']

q = queue.Queue()
q.put([start_state])

for pre_tran in pre_trans:
    trans.append((pre_tran[0],pre_tran[1],pre_tran[2]))


while q.qsize() > 0:
    states = q.get()
    for _todo_link_ in ['a', 'b']:
        next_states = []
        for state in states:
            for _from_, _link_, _to_ in trans:
                if _from_ == state and _link_ == _todo_link_:
                    next_states.append(_to_)
        next_states2 = []
        for item in next_states:
            if item not in next_states2:
                next_states2.append(item)
        next_states2.sort()
        dfa_trans.append((str(states), _todo_link_, str(next_states2)))
        if str(next_states2) not in done:
            q.put(next_states2)
            done.add(str(next_states2))

def dfa(_str_):
    cur_state = '''['0']'''
    routines = [cur_state]
    for item in _str_:
        found = False
        new_state = ''
        for (_from_, _link_, _to_) in dfa_trans:
            if _from_ == cur_state and _link_ == item:
                found = True
                new_state = _to_
        if not found:
            return (False, routines)
        cur_state = new_state
        routines.append(cur_state)
    cur_state = eval(cur_state)
    terminals_in_state = False
    for terminal in terminals:
        if terminal in cur_state:
            terminals_in_state = True
    return (True, routines) if terminals_in_state else (False, routines)


s = ''
while True:
    try:
        s = input().strip()
        status, routines = dfa(s)
        routine_strs = []
        for routine in routines:
            routine_strs.append(state_to_str(eval(routine)))
        for i in range(len(s) + 1 - len(routine_strs)):
            routine_strs.append('{}')
        print(routine_strs[0], end='')
        for i in range(len(s)):
            print('-' + s[i] + '->', end='')
            print(routine_strs[i+1], end='')
        print()
        if status:
            print('accept')
        else:
            print('not accept')
    except:
        exit(0)
