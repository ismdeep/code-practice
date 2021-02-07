#!/usr/bin/env python3

import requests
import re


def is_login():
    req_test_login = requests.get(
        url='http://www.baidu.com',
        allow_redirects=False
    )
    try:
        if 'bfe' in req_test_login.headers['Server']:
            return True
    except:
        pass
    return False


def findall(_content_, pattern_str):
    pattern = re.compile(pattern_str, re.S)
    return re.findall(pattern, _content_)


if is_login():
    print('CMCC-WEB is login.')
    exit(-1)


req = requests.get(
    url='http://www.baidu.com',
    allow_redirects=False
)

login_page_url = req.headers['Location']

req_login_page = requests.get(
    url=login_page_url,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
)
content = req_login_page.text

jsessionid = req_login_page.headers['Set-Cookie']
jsessionid = jsessionid[:jsessionid.find(';')]

wlanacip = findall(content, '''<INPUT name="wlanacip" value="(.*?)" type="hidden">''')[0]
wlanacname = findall(content, '''<INPUT name="wlanacname" value="(.*?)"\r\n\t\t\t\t\t\t\t\t\t\t\ttype="hidden">''')[0]
wlanuserip = findall(content, '''<INPUT name="wlanuserip" value="(.*?)" type="hidden">''')[0]
uaid = findall(content, '''<INPUT name="uaId" value="(.*?)" type="hidden">''')[0]
csrf_token_raws = findall(content, """HW=(.*?)&wlanacname""")

req_login = requests.post(
    url='http://211.138.211.1:8080/cmcclogin.do',
    data={
        'scanToken': '',
        'bpssUSERNAME': '',
        'bpssBUSPWD': '',
        'textpwd': '输入固定密码/临时密码',
        'loginmode': 'static',
        'wlanacip': wlanacip,
        'wlanacname': wlanacname,
        'wlanuserip': wlanuserip,
        'wlanacssid': 'CMCC',
        'portion': 'cmcc',
        'uaId': uaid,
        'obsReturnAccount': '',
        'Token': 'First',
        'CSRFToken_HW': '7cd5e4c268d90765db76c0abef77c725'
    },
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
        'Cookie': jsessionid + '; qrrnd=92px1p09e884quscf88p38a3c9sb8zwr'
    }
)

print(req.text)
