# coding: utf-8
# author: ismdeep
# dateime: 2019-03-30 10:18:45
# filename: hdu-login.py
# blog: https://ismdeep.com


import requests
import os
import sys
import json
import http.cookiejar


def main():
    req = requests.get(
        url='http://acm.hdu.edu.cn/',
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }
    )
    cookie = req.cookies
    cookie = cookie.get_dict()
    username = sys.argv[1]
    password = sys.argv[2]
    req = requests.post(
        url='http://acm.hdu.edu.cn/userloginex.php?action=login',
        data={
            'username': username,
            'password': password,
            'login': 'Sign In'
        },
        cookies=cookie,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'Cookie': cookie['PHPSESSID']
        }
    )
    print(req.text)



if __name__ == '__main__':
    main()
