# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC:   下载网络上的文件

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/2/26
Last Modify: 2016/3/9
version: 0.0.1
'''

import urllib
import urllib2

url = 'http://www.someserver.com/register.cgi'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {
    'name': 'WHY',
    'location': 'SDU',
    'language': 'Python'
}
headers = {
    'User-Agent': user_agent
}

data = urllib.urlencode(values)     # 编码工作
req = urllib2.Request(url, data, headers)    # 发送请求同时传data表单
response = urllib2.urlopen(req)     # 接受反馈的信息
the_page = response.read()          # 读取反馈的内容
print(the_page)

# print "downloading with urllib"
# url = 'http://www.someserver.com/register.cgi'
# print "downloading with urllib"
# urllib.urlretrieve(url, "F:/Temp/262837429")
