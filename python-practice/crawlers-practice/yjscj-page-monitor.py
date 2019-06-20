# coding: utf-8
# author: ismdeep
# dateime: 2019-06-20 08:23:44
# filename: yjscj-page-monitor.py
# blog: https://ismdeep.com

import logging
import json
import requests
import os
import re
import time
import smtplib
import hashlib
from email.mime.text import MIMEText
from email.header import Header
from redis import Redis

from PIL import Image
from PIL import ImageEnhance
import pytesseract

from ismdeep_utils import ArgvUtil
from ismdeep_utils import EmailUtil
from ismdeep_utils import ReUtil
from ismdeep_utils import StringUtil
from ismdeep_utils import QQEmailSender


logging.basicConfig(
    filename='yjscj-page-monitor.log',
    level=logging.DEBUG,
    format='[%(asctime)s][%(filename)s][line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def redis_client():
    return Redis(
        host=ArgvUtil.get_sys_argv('--redis-host'),
        port=6379,
        password=ArgvUtil.get_sys_argv('--redis-password')
    )


def email_account():
    client = redis_client()
    return json.loads(client.get('email_config').decode())


def load_yjscj_md5(username):
    client = redis_client()
    try:
        return client.get('yjscj-md5-%s' % username).decode()
    except:
        return ''


def save_yjscj_md5(username, md5_value):
    client = redis_client()
    client.set('yjscj-md5-%s' % username, md5_value)


def main():
    email_account_json = email_account()
    qqEmailSender = QQEmailSender(email_account_json['email'], email_account_json['password'])
    req = requests.get(
        url='http://yjsgl.jxust.edu.cn/login.html',
        headers={
            'User-Agent': 'IE11'
        }
    )
    cookies = dict(req.cookies)
    login_success = False
    while not login_success:
        img_req = requests.get(
            url='http://yjsgl.jxust.edu.cn/login/jpg.html',
            cookies=cookies,
            headers={
                'User-Agent': 'IE11'
            }
        )
        with open('img.png', 'wb') as f:
            f.write(img_req.content)
        im = Image.open('img.png')
        im = im.convert('L')
        im = ImageEnhance.Contrast(im)
        im = im.enhance(4)
        captcha_code = pytesseract.image_to_string(im)
        logging.info('captcha_code {%s}' % captcha_code)
        captcha_code = captcha_code.replace(' ', '')
        captcha_code = captcha_code.replace('.', '')
        if len(captcha_code) == 4:
            logging.info('try login with captcha: {%s}' % captcha_code)
            login_req = requests.post(
                url='http://yjsgl.jxust.edu.cn/login/validateLogin.html',
                cookies=cookies,
                data={
                    'loginName': ArgvUtil.get_sys_argv('-username'),
                    'loginPwd': ArgvUtil.get_sys_argv('-password'),
                    'code': captcha_code
                },
                headers={
                    'User-Agent': 'IE11'
                }
            )
            if not login_req.text.find('''/login/validateLogin.html''') >= 0:
                login_success = True
                logging.info('login successfully with captcha: {%s}' % captcha_code)
    timestamp_id = int(time.time() * 1000)
    url = 'http://yjsgl.jxust.edu.cn/train/score/my?_=%d' % timestamp_id
    content = requests.get(
        url=url,
        cookies=cookies,
        headers={
            'User-Agent': 'IE11'
        }
    ).text
    if content.find('validateLogin') >= 0:
        logging.error('Not Login. JSESSIONID invalid. %s' % jsessionid)
        qqEmailSender.send_text_email('ismdeep@icloud.com','ERROR @ yjscj-monitor', 'JSESSIONID invalid.')
        return
    last_yjscj_md5 = load_yjscj_md5(ArgvUtil.get_sys_argv('-username'))
    m = hashlib.md5()
    m.update(content.encode())
    logging.info(m.hexdigest())
    if m.hexdigest() != last_yjscj_md5:
        print('Changed!')
        save_yjscj_md5(ArgvUtil.get_sys_argv('-username'), m.hexdigest())
        send_successfully = False
        while not send_successfully:
            send_successfully = qqEmailSender.send_html_email('ismdeep@icloud.com', '研究生成绩更新', content)
        logging.info("成绩已发送。")
    else:
        logging.info('尚无成绩更新')


if __name__ == '__main__':
    main()
