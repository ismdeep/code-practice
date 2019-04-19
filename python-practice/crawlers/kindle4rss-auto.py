# coding:utf-8

import requests
from ismdeep_utils import ArgvUtil
import logging


logging.basicConfig(
    filename='tmp.log',
    level=logging.DEBUG,
    format='[%(asctime)s][%(filename)s][line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def main():
    logging.info('main() started')
    req = requests.get(url='http://kindle4rss.com', timeout=30)
    cookie = req.cookies
    logging.info('%s' % dict(cookie))
    req = requests.post(
        url='http://kindle4rss.com/login/',
        data={
            'email_address': ArgvUtil.get_sys_argv('-email'),
            'password': ArgvUtil.get_sys_argv('-password'),
            'persistent': 'True'
        },
        cookies=cookie,
        allow_redirects=False,
        timeout=30
    )
    cookie = req.cookies
    req = requests.get(url='http://kindle4rss.com/',cookies=cookie, timeout=30)
    logging.info('%d' % len(req.text))
    req = requests.get(url='http://kindle4rss.com/send_now/', cookies=cookie, timeout=30)
    logging.info('%d' % len(req.text))
    logging.info('main() ended')
    logging.info('-' * 40)


if __name__ == '__main__':
    main()
