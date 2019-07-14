# coding:utf-8
# python3 iacr-eprint-downloader.py -url https://eprint.iacr.org/eprint-bin/search.pl?last=7&title=1

import os
import sys
import requests
from ismdeep_utils import ArgvUtil
from ismdeep_utils import ReUtil
from subprocess import call


def validate_filename(_filename_):
    valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=_+[],.~@#%&() '
    ans = ''
    for item in _filename_:
        if item in valid_chars:
            ans += item
    for item in range(10, 1, -1):
        ans = ans.replace('        ', ' ')
        ans = ans.replace('       ', ' ')
        ans = ans.replace('      ', ' ')
        ans = ans.replace('     ', ' ')
        ans = ans.replace('    ', ' ')
        ans = ans.replace('   ', ' ')
        ans = ans.replace('  ', ' ')        
    return ans.strip()


def http_content(_url_):
    req = requests.get(
        url=_url_
    )
    return req.text


def iacr_eprint_archives(_url_):
    content = http_content(_url_)
    archives = ReUtil.findall(content, '''<dt>\n<a href\=\"(.*?)\">(.*?)</a>(.*?)<b>(.*?)</b>(.*?)</em>''')
    archives_ans = []
    for archive in archives:
        archives_ans.append((archive[1].split('/')[0], archive[1].split('/')[1], archive[3]))
    return archives_ans


def main():
    url = ArgvUtil.get_sys_argv('-url')
    archives = iacr_eprint_archives(url)
    for year, no, title in archives:
        print("%s-%s-%s.pdf" % (year, no, validate_filename(title)))
        IDM = r'C:\Program Files (x86)\Internet Download Manager\IDMan.exe'
        DownUrl = 'https://eprint.iacr.org/%s/%s.pdf' % (year, no)
        DownPath = r'E:\iacr-eprint'
        OutPutFileName = '%s-%s-%s.pdf' % (year, no, validate_filename(title))
        call([IDM, '/d', DownUrl, '/p', DownPath, '/f', OutPutFileName, '/n', '/a'])
        # os.system('''idman /d https://eprint.iacr.org/%s/%s.pdf /n /f "%s"''' % (year, no, validate_filename(title)))



if __name__ == '__main__':
    main()
