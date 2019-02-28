# coding: utf-8
# author: ismdeep
# dateime: 2019-02-28 11:41:09
# filename: 1651.py
# blog: https://ismdeep.com

import time

def cmp(a, b):
    if a[1] > b[1]:
        return True
    elif a[1] == b[1]:
        if a[0] < b[0]:
            return True
    else:
        return False


def project_name_p(__val__):
    return True if 'A' <= __val__[0] <= 'Z' else False


def user_id_p(__val__):
    return not project_name_p(__val__=__val__)


def func(l):
    projects = dict()
    project = set()
    last_item = ''
    user_ids = set()
    for item in l:
        if project_name_p(item):
            if not last_item == '':
                projects[last_item] = project
            project = set()
            last_item = item
        else:
            project.add(item)
            user_ids.add(item)
    projects[last_item] = project
    for userid in user_ids:
        cnt = 0
        for _project_name_ in projects:
            if userid in projects[_project_name_]:
                cnt += 1
        if cnt > 1:
            for _project_name_ in projects:
                if userid in projects[_project_name_]:
                    projects[_project_name_].remove(userid)
    ans = []
    for _project_name_ in projects:
        ans.append((_project_name_, len(projects[_project_name_])))
    for i in range(len(ans)):
        for j in range(i + 1, len(ans)):
            if not cmp(ans[i], ans[j]):
                tmp = ans[i]
                ans[i] = ans[j]
                ans[j] = tmp
    for _project_name_, cnt in ans:
        print(_project_name_, cnt)


def main():
    l = []
    while True:
        s = input()
        if '0' == s:
            exit(0)
        if '1' == s:
            func(l)
            l = []
        else:
            l.append(s)


if __name__ == '__main__':
    main()
