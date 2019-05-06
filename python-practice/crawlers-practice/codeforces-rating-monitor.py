# coding: utf-8
# author: ismdeep
# dateime: 2019-03-06 13:50:51
# filename: codeforces-rating-monitor.py
# blog: https://ismdeep.com
import requests
import sys
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import logging

username = ''
path = ''

logging.basicConfig(
    filename='/data/log/codeforces-rating-monitor.log',
    level=logging.DEBUG,
    format='[%(asctime)s][%(filename)s][line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


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


def load_saved_rating_ids():
    try:
        with open(path, 'r') as f:
            return eval(f.read())
    except:
        return []


def main():
    saved_rating_ids = load_saved_rating_ids()
    req = requests.get(
        url='http://codeforces.com/profile/%s' % username,
        timeout=3
    )
    content = req.text
    content = content[content.find('''data.push(''') + len('''data.push('''):]
    content = content[:content.find(''');''')]
    ratings = eval(content)
    new_rating_found = False
    new_rating = None
    for rating in ratings:
        if rating[0] not in saved_rating_ids:
            new_rating_found = True
            new_rating = rating
            saved_rating_ids.append(new_rating[0])
    if new_rating_found:
        server, port, email, password = email_account()
        send_success = False
        while not send_success:
            try:
                msg = '''%s's rating was changed in { %s }. => %d(%s%d)''' % (
                username, new_rating[3], new_rating[1], '+' if new_rating[5] > 0 else '', new_rating[5])
                print(msg)
                send_success = True
                send_success = send_email(server, port, email, password, 'ismdeep@icloud.com',
                                          username + '\'s rating changed', msg, 'plain')
            except:
                pass
        print('''%s's rating changed at %s''' % (username, new_rating[0]))
    with open(path, 'w') as f:
        f.write(str(saved_rating_ids))


if __name__ == '__main__':
    username = sys.argv[1]
    logging.info('start codeforces-rating-moitor => username: {%s}' % username)
    path = '/data/codeforces-%s-ids.dat' % username
    done_flag = False
    while not done_flag:
        try:
            main()
            done_flag = True
        except Exception as e:
            print(e)
