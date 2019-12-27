# coding: utf-8
# author: ismdeep
# dateime: 2018-08-17 13:42:01
# filename: tsgd.py
# blog: https://ismdeep.com

import time
import urllib
import http.cookiejar
import re
import syslog
from ismdeep_utils import ArgvUtil
from ismdeep_utils import StringUtil



class JxustTSG:
    fullname = ''
    cj = http.cookiejar.CookieJar()
    home_site = 'http://218.87.136.111'
    username = ''
    password = ''
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }

    def __init__(self, _username_, _password_):
        self.username = _username_
        self.password = _password_

    def open(self):
        req = urllib.request.Request(self.home_site + '/dzjs/login_form.asp', None, self.header)
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj))
        r = opener.open(req)

    def login(self):
        login_form_data = {
            'gotourl': '',
            'user': self.username,
            'pw': self.password,
            'submit1': '(unable to decode value)'
        }
        req = urllib.request.Request(
            self.home_site + '/dzjs/login.asp',
            urllib.parse.urlencode(login_form_data).encode('utf-8'),
            self.header)
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj))
        r = opener.open(req)
        try:
            content = r.read().decode('gb2312', 'ignore')
        except:
            return ""
        if content.find('欢迎您登录') >= 0:
            self.fullname = StringUtil.between(content, "window.alert ('", '，')
            return self.fullname
        else:
            return ""

    def rent_list(self):
        post_data = {
            'nCxfs': '1',
            'submit1': '(unable to decode value)'
        }
        req = urllib.request.Request(
            self.home_site + '/dzjs/jhcx.asp',
            urllib.parse.urlencode(post_data).encode('utf-8'),
            self.header)
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj))
        r = opener.open(req)
        content = r.read().decode('gb2312', errors='ignore')
        pattern = re.compile(
            '''<td  class=tdborder4  >(.*?)&nbsp;</td><td  class=tdborder4  >(.*?)&nbsp;</td><td  class=tdborder4  >(.*?)</td><td  class=tdborder4  >(.*?)</td><td  class=tdborder4  >(.*?)&nbsp;</td><td  class=tdborder4  >(.*?)&nbsp;</td><td class=tdborder4  align=center  ><a href = '(.*?)' target=_blank >(.*?)</a></td>''',
            re.S)
        rents = re.findall(pattern, content)
        return rents

    def xj(self, xj_id):
        req = urllib.request.Request(self.home_site + '/dzxj/dzxj.asp?nbsl=' + xj_id, None, self.header)
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj))
        r = opener.open(req)
        content = r.read().decode('gb2312', errors='ignore')
        content = content[content.find('window.alert ("') + len('window.alert ("'):]
        content = content[:content.find('");')]

    def xj_all(self):
        rents = self.rent_list()
        rents_data = []
        for item in rents:
            from_date = item[2]
            to_date = item[3]
            book_name = item[0]
            rents_data.append({
                'from_date': item[2],
                'to_date': item[3],
                'book_name': item[0]
            })
            syslog.syslog(syslog.LOG_INFO, "%s => %s (%s - %s) %s " % (
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), self.fullname, from_date, to_date,
                "《" + book_name + "》"))
            self.xj(item[6][item[6].find('nbsl=') + 5:])

    def logout(self):
        req = urllib.request.Request(self.home_site + '/share/Exit.asp', None, self.header)
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj))
        r = opener.open(req)
        content = r.read().decode('gb2312')


def tsg_xj(username, password):
    tsg = JxustTSG(username, password)
    tsg.open()
    tsg.login()
    tsg.xj_all()


if __name__ == '__main__':
    tsg_xj(ArgvUtil.get_sys_argv('-username'), ArgvUtil.get_sys_argv('-password'))
