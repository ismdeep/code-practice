# coding:utf-8
import re
import time

import requests
import sys

ac_threshold_value = 500

lang = {
    'g++': 0,
    'gcc': 1,
    'c++': 2,
    'c': 3,
    'pascal': 4,
    'java': 5,
    'c#': 6
}

running_results = ['Queuing', 'Compiling', 'Running']


def findall(content, pattern_str):
    pattern = re.compile(pattern_str, re.S)
    return re.findall(pattern, content)


## hdu-csdn-crawler.py begin ##########################################################
remove_list = [
    '<span class="hljs-number">', '</code>','</span>','<span class="hljs-keyword">','<span class="hljs-built_in">',
    '<span class="hljs-string">', '<span class="hljs-comment">', '<span class="hljs-preprocessor">', '<code class=" hljs cpp">',
    '<span class="hljs-stl_container">', '<span class="hljs-operator">', '<span class="hljs-variable">','<code class=" hljs perl">',
    '<code class=" hljs sql">', '<span class="hljs-regexp">', '<code class="language-cpp hljs ">', '<code class="language-c++ hljs perl">',
    '<code class="language-c++ hljs cpp">', '<code class="language-C++ hljs cpp">', '<code class="language-C++ hljs cs">',
    '<code class="language-CPP hljs cpp">'
]


def parse_code_fun1(content):
    try:
        code = findall(content, '''<pre class=\"prettyprint\">(.*?)</pre>''')[0]
        for item in remove_list:
            code = code.replace(item, '')
        code = code.replace('&lt;', '<')
        code = code.replace('&gt;', '>')
        code = code.replace('&amp;', '&')
        return code
    except:
        return ''


def parse_code_fun2(content):
    try:
        code = findall(content, '''<pre><code class=\"(.*?)\">(.*?)</code></pre>''')[0][1]
        code = code.replace('&lt;', '<')
        code = code.replace('&gt;', '>')
        code = code.replace('&amp;', '&')
        return code
    except:
        return ''


def get_code(csdn_blog_url):
    req = requests.get(url=csdn_blog_url)
    content = req.text
    code = parse_code_fun1(content)
    if code is '':
        code = parse_code_fun2(content)
    return code


def get_hdu_code_list(_problem_id_):
    url = 'https://so.csdn.net/so/search/s.do?q=hdu%20'+str(_problem_id_)+'&t=blog&u='
    req = requests.get(
        url=url
    )
    content = req.text
    items = findall(content, '''<div class=\"limit_width\">\r\n                                <a href=\"(.*?)\" target=\"_blank\" strategy=\"SearchFromCsdn\">(.*?)</a>\r\n                                <a href=\"(.*?)\" target=\"_blank\" strategy=\"SearchFromCsdn\">(.*?)</a>\r\n                            </div>''')
    codes = []
    for item in items:
        try:
            code = get_code(item[0])
            if len(code) >= 50:
                codes.append(code)
        except:
            pass
    return codes
## hdu-csdn-crawler.py end   ##########################################################


def sys_argv(_key_):
    for i in range(len(sys.argv)):
        if sys.argv[i] == _key_:
            return sys.argv[i + 1]
    return ''


def login_cookie(_username_, _password_):
    login_success = False
    cookie = None
    cnt = 3
    while not login_success:
        req = requests.get(
            url='http://acm.hdu.edu.cn/',
            headers={
                'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
            }
        )
        cookie = req.cookies
        cookie = cookie.get_dict()
        req = requests.post(
            url='http://acm.hdu.edu.cn/userloginex.php?action=login',
            data={
                'username': _username_,
                'userpass': _password_,
                'login': 'Sign+In'
            },
            cookies=cookie
        )
        if req.text.find('<a href="/userstatus.php?user=') >= 0:
            login_success = True
        cnt -= 1
        if cnt <= 0:
            return None
    return cookie


def submit_code(_username_, _cookie_, _problem_id_, _lang_, _code_):
    requests.post(
        url='http://acm.hdu.edu.cn/submit.php?action=submit',
        data={
            'check': 0,
            'problemid': _problem_id_,
            'language': _lang_,
            'usercode': _code_
        },
        cookies=_cookie_
    )
    time.sleep(1)
    result = 'Queuing'
    while result in running_results:
        req = requests.get(
            url='http://acm.hdu.edu.cn/status.php?user=' + _username_
        )
        content = req.text
        re_pattern = '''<tr(.*?)><td height\=22px>(.*?)</td><td>(.*?)</td><td>(.*?)<font color=(.*?)>(.*?)</font>(.*?)</td><td><a href\="/showproblem.php\?pid\=(.*?)">(.*?)</a></td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td(.*?)><a href\="/userstatus.php\?user\=(.*?)">(.*?)</a></td></tr>'''
        results = findall(content, re_pattern)
        print(results[0][1], results[0][5])
        result = results[0][5]
        time.sleep(0.1)
    return result


def show_help():
    print('''
Usage: python3 hdu-hack.py -username {username} -password {password} -pid {problem_id}

Options:
    -username username    Username on acm.hdu.edu.cn
    -password password    Password on acm.hdu.edu.cn
    -pid      problem_id  Problem ID
''')


def solve_problem(_problem_id_):
    username = sys_argv('-username')
    password = sys_argv('-password')
    if '' == username or '' == password:
        show_help()
        exit(0)
    cookie = login_cookie(username, password)
    if cookie is None:
        print('''Wrong username or password.''')
        exit(0)
    print(cookie)
    codes = get_hdu_code_list(_problem_id_)
    print('codes found: %d' % len(codes))
    if len(codes) <= 0:
        return False
    result = ''
    _index_ = 0
    while result != 'Accepted':
        if _index_ >= len(codes):
            return False
        lang_id = lang['g++']
        if codes[_index_].find('public class Main') >= 0 or codes[_index_].find('public static void main') >= 0:
            lang_id = lang['java']
        result = submit_code(
            _username_=username,
            _cookie_=cookie,
            _problem_id_=_problem_id_,
            _lang_=lang_id,
            _code_=codes[_index_])
        if result == 'Compilation Error':
            print('Compilation Error')
            # exit(0)
        _index_ += 1
    return True


def main():
    problem_id = sys_argv('-pid')
    if '' == problem_id:
        show_help()
        exit(0)
    problem_id = int(problem_id)
    print(solve_problem(problem_id), 'for', str(problem_id))


if __name__ == '__main__':
    main()
