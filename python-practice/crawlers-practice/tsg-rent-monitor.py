# coding: utf-8
# author: ismdeep
# dateime: 2019-05-05 13:39:48
# filename: tsg-book-monitor.py
# blog: https://ismdeep.com
import hashlib
import json
import logging

from ismdeep_utils import ArgvUtil
from ismdeep_utils import ReUtil
from ismdeep_utils import EmailUtil
import requests
import codecs


tsg_home_site = 'http://218.87.136.111'


logging.basicConfig(
    filename='tsg-book-monitor.log',
    level=logging.DEBUG,
    format='[%(asctime)s][%(filename)s][line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def md5_content(content):
    m = hashlib.md5()
    m.update(codecs.encode(content))
    md5_val = m.hexdigest()
    return md5_val


def email_account():
    json_obj = json.load(open('email.json', 'r'))
    return json_obj['server'], json_obj['port'], json_obj['email'], json_obj['password']


def load_rent_info(book_id):
    try:
        with open('%s.txt' % book_id, 'r') as f:
            return f.read()
    except Exception as e:
        return ''


def save_rent_info(book_id, content):
    with open('%s.txt' % book_id, 'wb') as f:
        f.write(codecs.encode(content))


def main():
    book_id = ArgvUtil.get_sys_argv('-id')
    logging.info('==> main() id: {%s}' % book_id)
    url = '%s/showmarc/table.asp?nTmpKzh=%s' % (tsg_home_site, book_id)
    req = requests.get(url=url)
    content = codecs.decode(req.content, 'gb2312')
    content_table = ReUtil.findall(content, '''<table align\="center" border\="0" cellspacing\="0" width\="90\%">(.*?)</table>''')
    basic_info_table = '''<table>%s</table>''' % content_table[0]
    rent_info_table = '''<table>%s</table>''' % content_table[1]
    book_name = ReUtil.findall(basic_info_table, '''正题名</td><td class\=tdborder2a >&nbsp;(.*?)</td>''')[0].strip()
    content_html = '''<!DOCTYPE html><html><head><title>%s</title></head><body>%s<hr>%s</body></html>''' % (
        book_name, basic_info_table, rent_info_table
    )
    if md5_content(rent_info_table) != load_rent_info(book_id):
        '''send email'''
        logging.info('''start sending email to => ismdeep@icloud.com''')
        server, port, email, password = email_account()
        save_rent_info(book_id, md5_content(rent_info_table))
        send_email_successfully = False
        while not send_email_successfully:
            send_email_successfully = EmailUtil.send_email(
                server=server,
                port=port,
                from_email=email,
                password=password,
                to_email='ismdeep@icloud.com',
                title='%s 借阅记录更新' % book_name,
                content=content_html,
                content_type='html'
            )
        logging.info('''email sent to => ismdeep@icloud.com successfully.''')
    logging.info('-' * 40)


if __name__ == '__main__':
    main()
