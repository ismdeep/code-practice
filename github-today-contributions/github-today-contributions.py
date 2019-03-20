# coding: utf-8
# author: ismdeep
# dateime: 2019-02-22 17:17:39
# filename: github-today-contributions.py
# blog: https://ismdeep.com

import requests
import time
import sys
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def findall(content, pattern_str):
    pattern = re.compile(pattern_str, re.S)
    return re.findall(pattern, content)


def main():
    date_str = time.strftime('%Y-%m-%d', time.localtime())
    user = ''
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-user':
            user = sys.argv[i + 1]
    url = 'https://github.com/users/%s/contributions?to=%s' % (user, date_str)
    req = requests.get(
        url=url
    )
    days = findall(req.text,
                   '''<rect class\="day" width\="(.*?)" height\="(.*?)" x\="(.*?)" y\="(.*?)" fill\="#(.*?)" data-count\="(.*?)" data-date\="(.*?)"/>''')
    for day in days[-31::]:
        print(day[6], '■' * int(day[5]))


if __name__ == '__main__':
    main()
