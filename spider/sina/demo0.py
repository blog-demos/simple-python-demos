# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC:   网页抓取测试

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/3/7
Last Modify: 2016/3/9
version: 0.0.1
'''

import urllib2

response = urllib2.urlopen('http://weibo.com/')
html = response.read()
print html
