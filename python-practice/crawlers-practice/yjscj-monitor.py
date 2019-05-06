# coding: utf-8
# author: ismdeep
# dateime: 2019-01-04 16:12:09
# filename: yjscj-monitor.py
# blog: https://ismdeep.com

import logging
import json
import requests
import os
import re
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from PIL import Image
from PIL import ImageEnhance
import pytesseract

from ismdeep_utils import ArgvUtil
from ismdeep_utils import EmailUtil
from ismdeep_utils import ReUtil
from ismdeep_utils import StringUtil


course_ids_path = '%s-course-ids.txt' % ArgvUtil.get_sys_argv('-username')

logging.basicConfig(
    filename='yjscj-monitor.log',
    level=logging.DEBUG,
    format='[%(asctime)s][%(filename)s][line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def push_data(_data_):
    data = {
        'keyid': 'yjscj',
        'data': _data_,
        'token': ArgvUtil.get_sys_argv('-token')
    }
    req = requests.post(
        url='https://info.ismdeep.com/api/info/push_data',
        data=data
    )
    print(req.text)


def email_account():
    json_obj = json.load(open('email.json', 'r'))
    return json_obj['server'], json_obj['port'], json_obj['email'], json_obj['password']


def main():
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
        logging.info('captcha_code {%s}'%captcha_code)
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
        send_email('ERROR @ yjscj-monitor', 'JSESSIONID invalid.', receiver_list)
        return
    courses = ReUtil.findall(
        content=content,
        pattern_str='''<td align\="left">\((.*?)\) (.*?)</td>(.*?)<td align\="left">\((.*?)\) (.*?)</td>(.*?)<td align\="right">(.*?)</td>(.*?)<td align\="right">(.*?)</td>(.*?)<td align\="right">(.*?)</td>(.*?)<td align\="right">(.*?)</td>'''
    )

    last_course_ids = []
    try:
        fin = open(course_ids_path, 'r')
        for course_id in fin:
            last_course_ids.append(course_id.strip())
    except FileNotFoundError as e:
        last_course_ids = []
    course_ids = []
    course_info_text = '''<html>
<head>
    <title>研究生成绩</title>
    <style type="text/css">
        body {
            font-family: Monaco;
        }

        table.timecard {
            border-collapse: collapse;
            border: 1px solid #f79646; /*for older IE*/
        }

        table.timecard caption {
            background-color: #f79646;
            color: #f79646;
            font-size: x-large;
            font-weight: bold;
            letter-spacing: .3em;
        }

        table.timecard thead th {
            padding: 8px;
            background-color: #fde9d9;
            font-size: large;
        }

        table.timecard th, table.timecard td {
            padding: 3px;
            border-width: 1px;
            border-style: solid;
            border-color: #f79646 #f79646;
        }

        table.timecard td {
            text-align: center;
        }

    </style>
</head>
<body>
<table class="timecard">
    <thead>
    <tr><th>课程</th>
        <th>平时成绩</th>
        <th>考试成绩</th>
        <th>最终成绩</th>
    </tr></thead>
    <tbody>'''
    courses_data = []
    for course in courses:
        course_ids.append(course[0])
        # print(course[0], course[1], course[6], course[8], course[12])
        logging.info('''{"课程": "%s", "平时成绩": %s, "考试成绩": %s, "最终成绩": %s}''' % (
            course[1], course[6], course[8], course[12]))
        courses_data.append({
            'course_name': course[1],
            'score': StringUtil.between(course[12], '>', '<')
        })
        course_info_text += '''<tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
    </tr>''' % (course[1], course[6], course[8], course[12])
    course_info_text += '''</tbody></table>'''
    try:
        push_data(json.dumps(courses_data))
    except Exception as e:
        print(e)
    updated_flag = False
    for course_id in course_ids:
        if course_id not in last_course_ids:
            updated_flag = True
    if updated_flag:
        server, port, email, password = email_account()
        send_successfully = False
        while not send_successfully:
            send_successfully = EmailUtil.send_email(server, port, email, password, 'ismdeep@icloud.com', '研究生成绩更新', course_info_text, 'html')
        logging.info("成绩已发送。")
    else:
        logging.info('尚无成绩更新')
    f = open(course_ids_path, 'w')
    for course_id in course_ids:
        f.write(course_id + '\n')
    f.close()


if __name__ == '__main__':
    main()
