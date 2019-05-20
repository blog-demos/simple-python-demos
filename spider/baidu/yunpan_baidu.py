# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC: 测试抓取百度网盘资源

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/3/9
Last Modify: 2016/3/9
version: 0.0.1
'''

import urllib
import urllib.request
import webbrowser
import re
import urllib2

def yunpan_search(key):
    keyword = key
    keyword = keyword.encode('utf-8')
    keyword = urllib.request.quote(keyword)
    url = "http://www.wangpansou.cn/s.php?q="+keyword+"&wp=0&start=0"
    # webbrowser.open(url)
    req = urllib.request.Request(url, headers={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    })
    opener = urllib.request.urlopen(req)
    html = opener.read()
    html = html.decode('utf-8')
    rex = r'https?://pan.baidu.com.*\?uk=[0-9]{10}.*[\d+?]"'
    m = re.findall(rex, html)
    f = open('/root/Desktop/txt.txt', 'w')
    for i in m:
        f.write(i)
        f.write('\n\n')
    f.close()
    print("抓取成功!")

if __name__ == '__main__':
    print('爬取百度云盘资源快捷爬取')
    key = input('输入你想搜索的资源:')
    yunpan_search(key)
