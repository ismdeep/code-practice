# coding: utf-8
# author: ismdeep
# dateime: 2019-03-03 09:56:08
# filename: gzjj8-monitor.py
# blog: https://ismdeep.com

import requests
import re
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header

data_path = '/data/gzjj8-monitor-info-oks.txt'
key_words = ['编程', 'C++', 'C', 'c', 'c++', 'Java', 'java', 'Python', 'python', '算法']


def email_account():
    json_obj = json.load(open('/data/email.json', 'r'))
    return json_obj['server'], json_obj['port'], json_obj['email'], json_obj['password']


def saved_info_ok_ids():
    try:
        return eval(open(data_path, 'r').read())
    except:
        return []


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


def findall(content, pattern_str):
    pattern = re.compile(pattern_str, re.S)
    return re.findall(pattern, content)


def fetch_jiajiao_info():
    url = 'http://www.gzjj8.net/student.asp'
    req = requests.get(
        url=url,
        timeout=3000
    )
    content = req.content.decode('utf-8')
    re_pattern = '''<span class\="red_b_14">(.*?)</span>\r\n</TD>\r\n<TD width\="12%" style\="line-height:20px;">(.*?)\.(.*?)<BR>(.*?)<BR></TD>\r\n<TD width\="38%"><DIV align\=left>【<FONT color\=#993300>(.*?)</FONT>】\r\n(.*?)\r\n\r\n</DIV></TD>\r\n<TD width\="14%"><div align\="center" style\="line-height:20px;">(.*?)<br />(.*?)<br />'''
    infos = findall(content, re_pattern)
    info_oks = []
    for info in infos:
        flag = False
        for key_word in key_words:
            if info[3].find(key_word) >= 0:
                flag = True
            if info[5].find(key_word) >= 0:
                flag = True
        if flag:
            info_oks.append(info)
    return info_oks


def main():
    saved_ok_ids = saved_info_ok_ids()
    server, port, email, password = email_account()
    ok_infos = fetch_jiajiao_info()
    for ok_info in ok_infos:
        if ok_info[0] not in saved_ok_ids:
            send_success = False
            while not send_success:
                try:
                    send_success = send_email(server, port, email, password, 'ismdeep@icloud.com', '找到一个新家教',
                                              str(ok_info), 'plain')
                    if send_success:
                        print('%s: Email sent successfully.' % ok_info[0])
                        saved_ok_ids.append(ok_info[0])
                    else:
                        print('%s: Email sent failed.' % ok_info[0])
                except:
                    pass
    with open(data_path, 'w') as f:
        f.write(str(saved_ok_ids))


if __name__ == '__main__':
    main()
