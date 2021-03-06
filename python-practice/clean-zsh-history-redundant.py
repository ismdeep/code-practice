# coding: utf-8
# author: ismdeep
# dateime: 2019-04-14 22:50:09
# filename: clean-zsh-history-redundant.py
# blog: https://ismdeep.com

import os
import codecs
from ismdeep_utils import DateTimeUtil

ans = []
data_set = set()
black_list = ['exit', 'cd ~', 'lc']

os.system('cp /Users/ismdeep/.zsh_history /Users/ismdeep/.zsh_history_%d' % (DateTimeUtil.unix_timestamp_now_second()))

with codecs.open('/Users/ismdeep/.zsh_history', 'r', 'UTF-8', 'ignore') as f:
    for line in f.readlines():
        line = line.strip()
        left = line[:line.find(':0;')] + ':0;'
        right = line[line.find(':0;') + 3:]
        if right not in data_set and right not in black_list:
            ans.append(line + '\n')
            data_set.add(right)
            print(right)

with codecs.open('/Users/ismdeep/.zsh_history', 'w', 'utf-8', 'ignore') as f:
    f.writelines(ans)
