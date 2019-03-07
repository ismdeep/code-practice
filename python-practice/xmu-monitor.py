# coding: utf-8
# author: ismdeep
# dateime: 2019-03-07 10:40:50
# filename: xmu-monitor.py
# blog: https://ismdeep.com
import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import logging
import json

path = '/data/xmu-admissions.html'

logging.basicConfig(
    filename='/data/log/xmu-admissions.log',
    level=logging.DEBUG,
    format='[%(asctime)s][%(filename)s][line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def load_saved_html():
    try:
        with open(path, 'r') as f:
            return f.read()
    except:
        return ''


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


def main():
    logging.info('start...')
    req = requests.get(
        url='http://information.xmu.edu.cn/portal/postgraduate/admissions'
    )
    content = req.text
    content = content[content.find(
        '''<div id="block-system-main" class="block block-system first last odd" thmr="thmr_424">'''):]
    content = content[content.find('''<div class="content">'''):]
    content = content[:content.find('''<!-- /.block -->''')]
    saved_html = load_saved_html()
    if content != saved_html:
        server, port, email, password = email_account()
        send_success = False
        while not send_success:
            try:
                send_success = send_email(server, port, email, password, 'ismdeep@icloud.com',
                                          'xmu postgraduate admissions changed', 'xmu postgraduate admissions changed!',
                                          'plain')
                send_success = send_email(server, port, email, password, '375117392@qq.com',
                                          'xmu postgraduate admissions changed', 'xmu postgraduate admissions changed!',
                                          'plain')
            except:
                pass
        logging.info('xmu postgraduate admissions changed!')
    with open(path, 'w') as f:
        f.write(content)


if __name__ == '__main__':
    main()
