# coding: utf-8
# author: ismdeep
# dateime: 2019-06-21 14:50:15
# filename: iacr-subscribe-tool.py
# blog: https://ismdeep.com

from ismdeep_utils import ReUtil
from ismdeep_utils import ArgvUtil
from ismdeep_utils import QQEmailSender
import requests
import logging

iacr_archives_file_path = 'iacr-archiveids.txt'


logging.basicConfig(
    filename='/data/python.log',
    level=logging.DEBUG,
    format='[%(asctime)s][%(filename)s][line:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def load_archiveids():
    try:
        with open(iacr_archives_file_path, 'r') as f:
            return eval(f.read())
    except:
        logging.error('File open failed. {%s}' % iacr_archives_file_path)
        return set()


def save_archiveids(archiveids):
    try:
        with open(iacr_archives_file_path, 'w') as f:
            f.write(str(archiveids))
        logging.info('File write successfully. {%s}' % iacr_archives_file_path)
    except:
        logging.error('File write failed. {%s}' % iacr_archives_file_path)


def fetch_archive_list_from_site():
    # req = requests.get(
    #     url='https://eprint.iacr.org/complete/'
    # )
    # content = req.text
    # with open('iacr.html', 'w') as f:
    #     f.write(content)
    content = open('iacr.html', 'r').read()
    archives = ReUtil.findall(content, '''<dt>\n<a href\="(.*?)">(.*?)</a>''')
    archiveids = set()
    for archiveid1, archiveid2 in archives:
        archiveids.add(archiveid1.strip())
    return archiveids


def push_archive_to_email(archive_id):
    print(archive_id)


def main():
    old_archiveids = load_archiveids()
    archiveids = fetch_archive_list_from_site()
    for archiveid in archiveids:
        if archiveid not in old_archiveids:
            print(archiveid)
    save_archiveids(archiveids)


if __name__ == '__main__':
    main()
