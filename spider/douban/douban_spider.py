# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC:   豆瓣电影排行榜爬虫

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/3/2
Last Modify: 2016/3/9
version: 0.0.1
'''

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from spider.douban.douban_parser import DoubanMovieParser
import urllib2

# ----------------------------------------- #
# 抓取网站的请求结果                           #
# url: 请求的网址                             #
# ----------------------------------------- #
def crawl(url=None):
    request = urllib2.Request(url)
    html = urllib2.urlopen(request)
    text = html.read()
    html.close()
    return text

# ----------------------------------------- #
# 解析从网站抓取的文本结果                       #
# url: 请求的网址                             #
# ----------------------------------------- #
def analyze(url=None):
    html_text = crawl(url)
    if html_text:
        parser = DoubanMovieParser()
        parser.feed(html_text)
        parser.close()

if __name__ == '__main__':
    analyze("http://movie.douban.com/chart")
