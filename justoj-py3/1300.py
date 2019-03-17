# coding: utf-8
# author: ismdeep
# dateime: 2019-03-04 14:36:47
# filename: 1300.py
# blog: https://ismdeep.com


def dfa(_str_, _start_state_, _trans_, _terminals_):
    state = _start_state_
    for item in _str_:
        found = False
        new_state = ''
        for (_from_, _link_, _to_) in _trans_:
            if _from_ == state and _link_ == item:
                found = True
                new_state = _to_
        if not found:
            return False
        state = new_state
    return True if state in _terminals_ else False


def expand_links(_pre_trans_, _expand_map_):
    _trans_ = []
    for _from_, _link_, _to_ in _pre_trans_:
        if _link_ in _expand_map_:
            for item in _expand_map_[_link_]:
                _trans_.append((_from_, item, _to_))
        else:
            _trans_.append((_from_, _link_, _to_))
    return _trans_


def main():
    str_alpha = 'abcdefghijklmnopqrstuvwxyz'
    str_digital = '0123456789'
    pre_trans = [
        ('S', 'alpha', 'T'),
        ('T', 'all', 'T')
    ]
    trans = expand_links(pre_trans, {
        'alpha': list(str_alpha) + list(str_alpha.upper()) + ['_'],
        'all': list(str_alpha) + list(str_alpha.upper()) + list(str_digital) + ['_']
    })
    while True:
        try:
            s = input()
            s = s.strip()
            if '' is s:
                continue
            print('accept' if dfa(s, 'T', trans, ['T']) else 'not accept')
        except:
            exit(0)


if __name__ == '__main__':
    main()
