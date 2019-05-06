# coding: utf-8
# author: ismdeep
# dateime: 2019-04-08 21:48:08
# filename: hdu-submit.py
# blog: https://ismdeep.com

import requests
import os
import sys
import re
import time


running_results = ['Queuing', 'Compiling', 'Running']

langs = {
    'g++': 0,
    'gcc': 1,
    'c++': 2,
    'c': 3,
    'pascal': 4,
    'java': 5,
    'c#': 6
}

def findall(content, pattern_str):
    pattern = re.compile(pattern_str, re.S)
    return re.findall(pattern, content)


def sys_argv(_key_):
    for i in range(len(sys.argv)):
        if sys.argv[i] == _key_:
            return sys.argv[i + 1]
    return ''


def login_cookie(_username_, _password_):
    login_success = False
    cookie = None
    cnt = 3
    while not login_success:
        req = requests.get(
            url='http://acm.hdu.edu.cn/',
            headers={
                'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
            }
        )
        cookie = req.cookies
        cookie = cookie.get_dict()
        req = requests.post(
            url='http://acm.hdu.edu.cn/userloginex.php?action=login',
            data={
                'username': _username_,
                'userpass': _password_,
                'login': 'Sign+In'
            },
            cookies=cookie
        )
        if req.text.find('<a href="/userstatus.php?user=') >= 0:
            login_success = True
        cnt -= 1
        if cnt <= 0:
            return None
    return cookie


def submit_code(_username_, _cookie_, _problem_id_, _lang_, _code_):
    requests.post(
        url='http://acm.hdu.edu.cn/submit.php?action=submit',
        data={
            'check': 0,
            'problemid': _problem_id_,
            'language': _lang_,
            'usercode': _code_
        },
        cookies=_cookie_,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }
    )
    time.sleep(1)
    result = 'Queuing'
    while result in running_results:
        req = requests.get(
            url='http://acm.hdu.edu.cn/status.php?user=' + _username_
        )
        content = req.text
        re_pattern = '''<tr(.*?)><td height\=22px>(.*?)</td><td>(.*?)</td><td>(.*?)<font color=(.*?)>(.*?)</font>(.*?)</td><td><a href\="/showproblem.php\?pid\=(.*?)">(.*?)</a></td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td(.*?)><a href\="/userstatus.php\?user\=(.*?)">(.*?)</a></td></tr>'''
        results = findall(content, re_pattern)
        print(results[0][1], results[0][5])
        result = results[0][5]
        time.sleep(0.1)
    return result



def main():
    username = sys_argv('-username')
    password = sys_argv('-password')
    pid = sys_argv('-pid')
    lang = sys_argv('-lang')
    code_path = sys_argv('-code')
    cookie = login_cookie(username, password)
    submit_code(username, cookie, pid, langs[lang], open(code_path, 'r').read())


if __name__ == '__main__':
    main()
