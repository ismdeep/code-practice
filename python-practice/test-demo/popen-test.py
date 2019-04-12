# coding: utf-8
# author: ismdeep
# dateime: 2019-04-12 15:07:41
# filename: popen-test.py
# blog: https://ismdeep.com

import os

content = os.popen('LANGUAGE=en_US.UTF-8 free -mlh').read()
print(content)
