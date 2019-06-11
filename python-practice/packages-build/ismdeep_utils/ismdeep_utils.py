#!/usr/bin/env python
#
# Copyright (c) 2015-2019, ismdeep <ismdeep@protonmail.com>
# All rights reserved.
#
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import sys
import smtplib
import time
import datetime
import re
from email.mime.text import MIMEText
from email.header import Header

__version__ = '0.0.9'


class ArgvUtil:
    @staticmethod
    def get_sys_argv(_key_):
        for i in range(len(sys.argv) - 1):
            if sys.argv[i] == _key_:
                return sys.argv[i + 1]
        return ''


def get_sys_argv(_key_):
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == _key_:
            return sys.argv[i + 1]
    return ''


class ReUtil:
    @staticmethod
    def findall(content, pattern_str):
        pattern = re.compile(pattern_str, re.S)
        return re.findall(pattern, content)


class EmailUtil:
    @staticmethod
    def send_email(server, port, from_email, password, to_email, title, content, content_type):
        sender = from_email
        receivers = to_email
        message = MIMEText(content, content_type, 'utf-8')
        message['From'] = from_email
        message['To'] = to_email
        subject = title
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtp_obj = smtplib.SMTP()
            smtp_obj.connect(server, port)
            smtp_obj.login(sender, password)
            smtp_obj.sendmail(sender, receivers, message.as_string())
            return True
        except smtplib.SMTPException:
            return False


class StringUtil:
    @staticmethod
    def between(_str_, _from_, _to_):
        _str_ = _str_[_str_.find(_from_) + len(_from_):]
        _str_ = _str_[:_str_.find(_to_)]
        return _str_


class DateTime:
    year = 0
    month = 0
    day = 0
    hour = 0
    minute = 0
    second = 0

    def __init__(self):
        now = datetime.datetime.now()
        self.year = now.year
        self.month = now.month
        self.day = now.day
        self.hour = now.hour
        self.minute = now.minute
        self.second = now.second

    def __str__(self):
        return '%04d-%02d-%02d %02d:%02d:%02d' % (self.year, self.month, self.day, self.hour, self.minute, self.second)

    def timestamp(self):
        return int(datetime.datetime.strptime(str(self), '%Y-%m-%d %H:%M:%S').timestamp())

    def parse(self, _date_str_):
        d = datetime.datetime.strptime(_date_str_, '%Y-%m-%d %H:%M:%S')
        self.year = d.year
        self.month = d.month
        self.day = d.day
        self.hour = d.hour
        self.minute = d.minute
        self.second = d.second

    def parse_from_timestamp(self, _timestamp_):
        d = datetime.datetime.strptime(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(_timestamp_)),'%Y-%m-%d %H:%M:%S')
        self.year = d.year
        self.month = d.month
        self.day = d.day
        self.hour = d.hour
        self.minute = d.minute
        self.second = d.second


class DateTimeUtil:
    @staticmethod
    def unix_timestamp(_datetime_):
        return int(_datetime_.timestamp())

    @staticmethod
    def unix_timestamp_now_second():
        return int(time.time())

    @staticmethod
    def unix_timestamp_now_millisecond():
        return int(time.time() * 1000)

    @staticmethod
    def simple_date_time_string(_date_time_=datetime.datetime.now(), _format_str_='%Y-%m-%d %H:%M:%S'):
        return _date_time_.strftime(_format_str_)

    @staticmethod
    def parse_to_datetime(_date_str_):
        return datetime.datetime.strptime(_date_str_, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def parse_from_timestamp_to_datetime(_timestamp_):
        return datetime.datetime.strptime(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(_timestamp_)),
                                          '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def add_minute(_datetime_):
        return DateTimeUtil.parse_from_timestamp_to_datetime(DateTimeUtil.unix_timestamp(_datetime_) + 60)


class Config:
    data = None

    def __init__(self):
        self.data = dict()

    def load(self, fp):
        s = fp.read()
        self.loads(s)

    def loads(self, s):
        s_list = list(map(str.strip, s.split('\n')))
        for item in s_list:
            if item.find('=') >= 0:
                key = item[:item.find('=')].strip()
                value = item[item.find('=')+1:].strip()
                self.data[key] = value

    def put(self, _key_, _value_):
        self.data[_key_] = _value_

    def dump(self):
        ans = ''
        for key in self.data:
            ans += '''%s = %s\n''' % (key, str(self.data[key]))
        return ans

    def save(self, fp):
        fp.write(self.dump())
