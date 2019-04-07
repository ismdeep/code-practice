# coding:utf-8

'''
POST /epay/electric/queryelectricbill HTTP/1.1
Host: ecard.jxust.edu.cn
Connection: keep-alive
Content-Length: 41
Accept: application/json, text/javascript, */*; q=0.01
Origin: http://ecard.jxust.edu.cn
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36
DNT: 1
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: http://ecard.jxust.edu.cn/epay/electric/load4electricbill?elcsysid=2
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,th;q=0.6,zh-TW;q=0.5,de;q=0.4,ja;q=0.3,fr;q=0.2,id;q=0.1,ru;q=0.1,es;q=0.1,am;q=0.1,pt;q=0.1,pl;q=0.1,ca;q=0.1,hu;q=0.1,lt;q=0.1,sq;q=0.1,nb;q=0.1,mt;q=0.1,cy;q=0.1,it;q=0.1,da;q=0.1,so;q=0.1,tr;q=0.1,la;q=0.1,nl;q=0.1,su;q=0.1,ro;q=0.1,vi;q=0.1,lb;q=0.1,ko;q=0.1,et;q=0.1
Cookie: JSESSIONID=A89F2BD81602867376FFB3A9890731C9
'''
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import requests
import urllib
import http.cookiejar
from PIL import Image
from PIL import ImageEnhance
import pytesseract
import sys
import logging
import time
import json

def sys_argv(_key_):
    for i in range(len(sys.argv)):
        if sys.argv[i] == _key_:
            return sys.argv[i + 1]
    return ''


def fetch_electric_bill(_cookie_):
    logging.info('''fetch_electric_bill('%s')''' % _cookie_)
    req = requests.post(
        url='http://ecard.jxust.edu.cn/epay/electric/queryelectricbill'
        , data={'sysid': 2, 'roomNo': 18606, 'elcarea': 1, 'elcbuis': 53}
        , headers={
            'Cookie': 'JSESSIONID=' + _cookie_
        }
    )
    content = req.text
    obj = json.loads(content.strip())
    logging.info(content)
    return float(obj['restElecDegree'])


def load_cookie(_username_):
    path = 'ecard-' + _username_ + '.cookie'
    try:
        with open(path, 'r') as f:
            return f.read().strip()
    except:
        return ''


def save_cookie(_username_, _cookie_):
    path = 'ecard-' + _username_ + '.cookie'
    try:
        with open(path, 'w') as f:
            f.write(_cookie_)
    except:
        pass


def test_authorized_cookie(_cookie_):
    req = requests.get(
        url='http://ecard.jxust.edu.cn/epay/',
        headers={
            'Cookie': 'JSESSIONID=' + _cookie_}
    )
    return True if req.text.find('''/epay/index/welcome.jsp''') >= 0 else False


def generate_login_cookie(_username_, _password_):
    cookie = load_cookie(_username_)
    if test_authorized_cookie(cookie):
        logging.info('cookie is authorized')
        return cookie
    req = requests.get('http://ecard.jxust.edu.cn/epay/person/index')
    cookies = dict(req.cookies)
    login_success = False
    try_time = 0
    print(cookies)
    while not login_success:
        img_req = requests.get(
            url='http://ecard.jxust.edu.cn/epay/codeimage',
            cookies=cookies
        )
        open('f.jpg', 'wb').write(img_req.content)
        im = Image.open('f.jpg')
        im = im.convert('L')
        im = ImageEnhance.Contrast(im)
        im = im.enhance(20)
        captcha_code = pytesseract.image_to_string(im)
        captcha_code = captcha_code.strip()
        captcha_code = captcha_code.replace(' ', '')
        try_time += 1
        logging.info("try_time: {%d} => %s" % (try_time, captcha_code))
        login_req = requests.post(
            url='http://ecard.jxust.edu.cn/epay/j_spring_security_check',
            data={
                'j_username': _username_,
                'j_password': _password_,
                'imageCodeName': captcha_code
            },
            headers={
                'Cookie': 'JSESSIONID=' + cookies['JSESSIONID']
            },
            allow_redirects=False
        )
        if login_req.headers['Location'].find('epay/') >= 0:
            login_success = True
            cookies = dict(login_req.cookies)
    save_cookie(_username_, cookies['JSESSIONID'])
    return cookies['JSESSIONID']


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
    logging.basicConfig(
        filename='ecard.log',
        level=logging.DEBUG,
        format='[%(asctime)s][%(filename)s][line:%(lineno)d] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    username = sys_argv('-username')
    password = sys_argv('-password')
    logging.info('''{username: "%s", password: "%s"}''' % (username, password))
    cookie = generate_login_cookie(username, password)
    print(cookie)
    remain = fetch_electric_bill(cookie)
    logging.info('remain: {%f}' % remain)
    if remain < 10:
        server, port, email, password = email_account()
        send_success = False
        while not send_success:
            send_success = send_email(
                server,
                port,
                email,
                password,
                'ismdeep@icloud.com',
                '电费余额不足',
                '电费余额不足: {%s}' % (str(remain)),
                'plain')


if __name__ == '__main__':
    os.chdir(sys_argv('-workspace'))
    main()
