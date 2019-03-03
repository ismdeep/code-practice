# coding: utf-8
# author: ismdeep
# dateime: 2019-03-02 20:37:46
# filename: hdu-monitor.py
# blog: https://ismdeep.com

# http://acm.hdu.edu.cn/status.php?first=&pid=&user=ismdeep&lang=0&status=0

import requests
import sys
import re
import prettytable as pt
from colorama import init, Fore, Back, Style
import os
import time

init(autoreset=False)


def findall(content, pattern_str):
    pattern = re.compile(pattern_str, re.S)
    return re.findall(pattern, content)


def main():
    url = 'http://acm.hdu.edu.cn/status.php?first=&pid=&user=%s&lang=0&status=0' % sys.argv[1]
    req = requests.get(
        url=url
    )
    content = req.text
    re_pattern = '''<tr(.*?)><td height\=22px>(.*?)</td><td>(.*?)</td><td>(.*?)<font color=(.*?)>(.*?)</font>(.*?)</td><td><a href\="/showproblem.php\?pid\=(.*?)">(.*?)</a></td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td(.*?)><a href\="/userstatus.php\?user\=(.*?)">(.*?)</a></td></tr>'''
    results = findall(content, re_pattern)
    # print(len(results))
    tb = pt.PrettyTable()
    tb.field_names = ["Run ID", "Submit Time", "Judge Status", "Pro.ID", "Language"]
    for item in results:
        _id_ = item[1]
        _run_time_ = item[2]
        _status_text_ = item[5]
        _problem_id_ = item[7]
        _lang_ = item[12]
        if _status_text_.find('Compilation Error') >= 0:
            _status_text_ = 'Compilation Error'
        if _status_text_.find('Runtime Error') >= 0:
            _status_text_ = 'Runtime Error'
        if _status_text_.find('Accepted') >= 0:
            _status_text_ = Fore.GREEN + ' ' + _status_text_ + ' ' + Fore.RESET
        tb.add_row([_id_, _run_time_, _status_text_, _problem_id_, _lang_])
    os.system('clear')
    print(tb)


if __name__ == '__main__':
    while True:
        main()
        time.sleep(0.3)
