# coding:utf-8

import requests
import os
import sys

ac_threshold_value = 500


def sys_argv(_key_):
    for i in range(len(sys.argv)):
        if sys.argv[i] == _key_:
            return sys.argv[i + 1]
    return ''


def login_cookie(_username_, _password_):
    login_success = False
    cookie = None
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
    return cookie


def main():
    username = sys_argv('-username')
    password = sys_argv('-password')
    cookie = login_cookie(username, password)
    print(cookie)


if __name__ == '__main__':
    main()
