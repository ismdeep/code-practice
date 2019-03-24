# coding: utf-8
# author: ismdeep
# dateime: 2019-03-24 16:03:14
# filename: url-monitor.py
# blog: https://ismdeep.com
import json
import os
import re
import sys
import requests
import codecs
import hashlib
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import logging

logging.basicConfig(
    filename='/data/ismdeep.log',
    level=logging.DEBUG,
    format='[%(asctime)s][%(filename)s][line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def load_last_md5(_url_):
    m = hashlib.md5()
    m.update(codecs.encode(_url_))
    md5_val = m.hexdigest()
    try:
        with open('/data/url-monitor-data/%s.md5' % md5_val, 'r') as f:
            return f.read().strip()
    except:
        return ''


def save_md5(_url_, _md5_):
    m = hashlib.md5()
    m.update(codecs.encode(_url_))
    md5_val = m.hexdigest()
    with open('/data/url-monitor-data/%s.md5' % md5_val, 'w') as f:
        f.write(_md5_)


def email_account():
    json_obj = json.load(open('/data/email.json', 'r'))
    return json_obj['server'], json_obj['port'], json_obj['email'], json_obj['password']


def send_email(server, port, from_email, password, to_email, title, content, content_type):
    logging.info('start sending email to %s' % to_email)
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
        logging.info('send email to %s successfully' % to_email)
        return True
    except smtplib.SMTPException:
        return False


def get_sys_argv(_key_):
    for i in range(len(sys.argv) - 1):
        if sys.argv[i] == _key_:
            return sys.argv[i + 1]
    return ''


def main():
    url = get_sys_argv('-url')
    start_point = get_sys_argv('-start')
    end_point = get_sys_argv('-end')
    start_point_str = ''
    end_point_str = ''
    with open(start_point, 'r') as f:
        start_point_str = f.read().strip()
    with open(end_point, 'r') as f:
        end_point_str = f.read().strip()
    req = requests.get(
        url=url,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
    )
    content = codecs.decode(req.content)
    content = content[content.find(start_point_str) + len(start_point_str):]
    content = content[:content.find(end_point_str)]
    content = content.strip()
    m = hashlib.md5()
    m.update(codecs.encode(content))
    logging.info('content md5() => {%s}' % m.hexdigest())
    if m.hexdigest() != load_last_md5(url):
        server, port, email, password = email_account()
        send_success = False
        while not send_success:
            try:
                msg = content
                send_success = True
                send_success = send_email(server, port, email, password, 'ismdeep@icloud.com', 'content in ' + url + ' changed' , msg, 'html')
            except:
                pass
        logging.info('content updated')
        save_md5(url, m.hexdigest())


if __name__ == '__main__':
    main()
