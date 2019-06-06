# coding: utf-8
# author: ismdeep
# dateime: 2019-06-05 22:50:21
# filename: mrblank-dump.py
# blog: https://ismdeep.com
from ismdeep_utils import ArgvUtil
import json

mrblank_file_path = ArgvUtil.get_sys_argv('-in')
content = open(mrblank_file_path, 'r').read()
ssr_list = json.loads(content)
for ssr in ssr_list['configs']:
    data = json.loads("{}");
    data["obfs"] = ssr['obfs']
    data["obfsparam"] = ssr['obfsparam']
    data["obfs_param"] = ssr['obfsparam']
    data["protocol"] = ssr['protocol']
    data["method"] = ssr['method']
    data["password"] = ssr['password']
    data["server"] = ssr['server']
    data["server_port"] = int(ssr['server_port'])
    data["local_port"] = 1080
    data["local_address"] = "0.0.0.0"
    with open('%s.json' % (ssr['server']), 'w') as f:
        f.write(json.dumps(data))
    print(ssr)
    node_name = ssr['server']
    print(node_name)
    print('-' * 80)
