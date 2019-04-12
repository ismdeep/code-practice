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


__version__ = '0.0.4'


class ArgvUtil:
    @staticmethod
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


class DateTimeUtil:
    @staticmethod
    def unix_timestamp_now_second():
        return int(time.time())

    @staticmethod
    def unix_timestamp_now_millisecond():
        return int(time.time() * 1000)

    @staticmethod
    def simple_date_time_string(format_str='%Y-%m-%d %H:%M:%S'):
        return datetime.datetime.now().strftime(format_str)
