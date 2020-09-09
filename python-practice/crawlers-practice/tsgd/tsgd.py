# coding: utf-8
# author: ismdeep
# datetime: 2018-08-17 13:42:01
# filename: tsgd.py
# blog: https://ismdeep.com
import sys
import json
import smtplib
import time
import datetime
import urllib
import http.cookiejar
import re
from email.header import Header
from email.mime.text import MIMEText

from ismdeep_utils import StringUtil
import logging
import logging.config
import redis

work_dir = '.'

################## Configuration START ##################
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_RENT_ID_KEY = 'notify_rent_ids'


def init_logging():
    logging.basicConfig(
        filename=work_dir + "/product.log",
        level=logging.DEBUG,
        format='%(asctime)s %(filename)s[%(levelname)s][line:%(lineno)d] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')


################## Configuration END   ##################

class MailSender(object):
    def __init__(self):
        self.smtp_obj = None
        self.from_mail = ''
        self.from_nick = ''
        self.password = ''
        self.to_mail = ''
        self.to_nick = ''

    def set_server(self, __server__, __port__):
        self.smtp_obj = smtplib.SMTP_SSL(__server__, __port__)

    def set_from_info(self, __mail__, __nickname__, __password__):
        self.from_mail = __mail__
        self.from_nick = __nickname__
        self.password = __password__

    def set_to_info(self, __mail__, __nickname__):
        self.to_mail = __mail__
        self.to_nick = __nickname__

    def login(self):
        self.smtp_obj.login(self.from_mail, self.password)

    def send(self, __title__, __content__, __content_type__):
        message = MIMEText(__content__, __content_type__, 'UTF-8')
        from_header = Header(self.from_nick, 'utf-8')
        from_header.append('<' + self.from_mail + '>', 'ascii')
        to_header = Header(self.to_nick, 'utf-8')
        to_header.append('<' + self.to_mail + '>', 'ascii')
        message['From'] = from_header
        message['To'] = to_header
        message['Subject'] = Header(__title__, 'UTF-8')
        self.smtp_obj.sendmail(self.from_mail, self.to_mail, message.as_string())


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
            open(work_dir + '/rent-list.re', r).read(),
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
        email_account = json.load(open(work_dir + '/email.json', 'r'))
        mail_sender = MailSender()
        mail_sender.set_server(email_account['host'], email_account['port'])
        mail_sender.set_from_info(
            email_account['from']['mail'],
            email_account['from']['nick'],
            email_account['from']['password'])
        mail_sender.set_to_info(
            email_account['to']['mail'],
            email_account['to']['nick'])
        mail_sender.login()
        rents = self.rent_list
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
            logging.info("%s (%s - %s) 《%s》" % (
                self.fullname,
                from_date,
                to_date,
                book_name))
            self.xj(item[6][item[6].find('nbsl=') + 5:])
            rent_id = item[1] + '//' + from_date + '-' + to_date
            if date_need_notify(to_date) and not query_notify_rent_id(rent_id):
                logging.info("Send mail [%s:《%s》] %s ~ %s" % (self.fullname, book_name, from_date, to_date))
                mail_content = """%s借阅的《%s》快到期了，借阅时间：%s ~ %s.""" % (
                    self.fullname, book_name, from_date, to_date
                )
                mail_sender.send('书籍逾期提醒', mail_content, 'text')
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
        print("Usage: python3 tsgd.py {work_dir}")
        exit(-1)
    work_dir = sys.argv[1]
    init_logging()
    accounts = json.load(open(work_dir + "/accounts.json", 'r'))
    for account in accounts:
        tsg_xj(account['username'], account['password'])
    logging.info("-" * 60)
