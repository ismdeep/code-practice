# coding:utf-8

import requests
import re

remove_list = [
    '<span class="hljs-number">', '</code>','</span>','<span class="hljs-keyword">','<span class="hljs-built_in">',
    '<span class="hljs-string">', '<span class="hljs-comment">', '<span class="hljs-preprocessor">', '<code class=" hljs cpp">',
    '<span class="hljs-stl_container">', '<span class="hljs-operator">', '<span class="hljs-variable">','<code class=" hljs perl">',
    '<code class=" hljs sql">', '<span class="hljs-regexp">'
]


def findall(content, pattern_str):
    pattern = re.compile(pattern_str, re.S)
    return re.findall(pattern, content)


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
            codes.append(code)
        except:
            pass
    return codes


def main():
    codes = get_hdu_code_list(1000)
    for code in codes:
        print('-' * 80)
        print(code)


if __name__ == '__main__':
    main()
