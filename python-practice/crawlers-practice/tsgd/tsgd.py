# coding: utf-8
# author: ismdeep
# datetime: 2018-08-17 13:42:01
# filename: tsgd.py
# blog: https://ismdeep.com
import os
import sys
import json
import smtplib
import time
import datetime
import urllib
import http.cookiejar
import re
import os
from email.header import Header
from email.mime.text import MIMEText

from ismdeep_utils import StringUtil
import argparse
import logging
import logging.config
import platform
import redis

################## Configuration START ##################
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_RENT_ID_KEY = 'notify_rent_ids'
REDIS_EMAIL_SERVER_KEY = 'email_server'
REDIS_EMAIL_PORT_KEY = 'email_port'
REDIS_EMAIL_USERNAME_KEY = 'email_username'
REDIS_EMAIL_PASSWORD_KEY = 'email_password'

log_file_path = os.environ['HOME']
if 'Windows' == platform.system():
    log_file_path += '\\'
else:
    log_file_path += '/'
log_file_path += 'tsgd.log'

logging.basicConfig(
    filename=log_file_path,
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[%(levelname)s][line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


################## Configuration END   ##################


def date_need_notify(__to_date__):
    tmp = time.strptime(__to_date__, '%Y/%m/%d')
    obj = datetime.datetime(tmp.tm_year, tmp.tm_mon, tmp.tm_mday)
    time_now = datetime.datetime.now()
    if (obj - time_now).days <= 70:
        return True
    return False


def redis_conn():
    conn = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    return conn


# 从 Redis 数据库查询 __rent_id__ 是否存在
def query_notify_rent_id(__rent_id__):
    conn = redis_conn()
    ans = conn.sismember(REDIS_RENT_ID_KEY, __rent_id__)
    conn.close()
    return ans


# 往 Redis 数据库写入 __rent_id__
def push_notify_rent_id(__rent_id__):
    conn = redis_conn()
    conn.sadd(REDIS_RENT_ID_KEY, __rent_id__)
    conn.close()


# TODO
# 发送邮件同志
def send_email_notify(__book_name__, __from_date__, __to_date__, __fullname__):
    logging.info("Send mail [%s:《%s》] %s ~ %s" % (__fullname__, __book_name__, __from_date__, __to_date__))
    content = """%s借阅的《%s》快到期了，借阅时间：%s ~ %s.""" % (
        __fullname__, __book_name__, __from_date__, __to_date__
    )
    while not send_email('ismdeep@icloud.com', '书籍逾期提醒', content, 'text'):
        time.sleep(1)


class EmailAccount(object):
    def __init__(self):
        self.server = None
        self.port = None
        self.email = None
        self.password = None


def load_email_account():
    conn = redis_conn()
    email_account = EmailAccount()
    email_account.server = conn.get(REDIS_EMAIL_SERVER_KEY).decode()
    email_account.port = int(conn.get(REDIS_EMAIL_PORT_KEY))
    email_account.email = conn.get(REDIS_EMAIL_USERNAME_KEY).decode()
    email_account.password = conn.get(REDIS_EMAIL_PASSWORD_KEY).decode()
    return email_account


def send_email(to_email, title, content, content_type):
    email_account = load_email_account()
    logging.info('start sending email to %s' % to_email)
    sender = email_account.email
    receivers = to_email
    message = MIMEText(content, content_type, 'utf-8')
    message['From'] = email_account.email
    message['To'] = to_email
    subject = title
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtp_obj = smtplib.SMTP_SSL(email_account.server, email_account.port)
        smtp_obj.connect(email_account.server, email_account.port)
        smtp_obj.login(sender, email_account.password)
        smtp_obj.sendmail(sender, receivers, message.as_string())
        logging.info('send email to %s successfully' % to_email)
        return True
    except smtplib.SMTPException as e:
        return False


class JxustTSG:
    fullname = ''
    cj = http.cookiejar.CookieJar()
    # home_site = 'http://218.87.136.111'
    home_site = 'http://tsgweb.jxust.edu.cn'
    username = ''
    password = ''
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/67.0.3396.99 Safari/537.36 '
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

    @property
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
            '''<td  class=tdborder4  >(.*?)&nbsp;</td><td  class=tdborder4  >(.*?)&nbsp;'''
            '''</td><td  class=tdborder4  >(.*?)</td><td  class=tdborder4  >(.*?)</td><td  class='''
            '''tdborder4  >(.*?)&nbsp;</td><td  class=tdborder4  >(.*?)&nbsp;</td><td class=tdborder4  align='''
            '''center  ><a href = '(.*?)' target=_blank >(.*?)</a></td>''',
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
        rents = self.rent_list
        rents_data = []
        for item in rents:
            rent_id = item[1]
            from_date = item[2]
            to_date = item[3]
            book_name = item[0]
            rents_data.append({
                'from_date': item[2],
                'to_date': item[3],
                'book_name': item[0]
            })
            logging.info("%s (%s - %s) 《%s》" % (
                self.fullname,
                from_date,
                to_date,
                book_name))
            self.xj(item[6][item[6].find('nbsl=') + 5:])
            rent_id = item[1] + '//' + from_date + '-' + to_date
            if date_need_notify(to_date) and not query_notify_rent_id(rent_id):
                send_email_notify(book_name, from_date, to_date, self.fullname)
                push_notify_rent_id(rent_id)

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
    if len(sys.argv) < 2:
        print("Usage: python3 tsgd.py {tsg accounts json file}")
        exit(-1)
    accounts = json.load(open(sys.argv[1], 'r'))
    for account in accounts:
        tsg_xj(account['username'], account['password'])
