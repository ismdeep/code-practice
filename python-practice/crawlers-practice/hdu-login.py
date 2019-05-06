# coding: utf-8
# author: ismdeep
# dateime: 2019-03-30 10:18:45
# filename: hdu-login.py
# blog: https://ismdeep.com

import requests
import sys


def try_hdu_login(_username_, _password_):
    req = requests.get(
        url='http://acm.hdu.edu.cn/',
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
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
    return True if req.text.find('<a href="/userstatus.php?user=') >= 0 else False


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    print(try_hdu_login(username, password))
