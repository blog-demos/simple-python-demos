# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC:   新浪微博脚本

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/3/7
Last Modify: 2016/3/9
version: 0.0.1
'''

# http://www.jianshu.com/p/7c5a4d7545ca

import re
import sys
import os
import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
from lxml import etree

reload(sys)
sys.setdefaultencoding('utf-8')

if len(sys.argv) >= 2:
    user_id = sys.argv[1]
else:
    user_id = raw_input("请输入user_id: ")

cookie = {
    "Cookie":
        "_T_WM=64b3bbfd017b7e7dbb4708c7a5a3c483; "
        "SUB=_2A2572TP2DeTxGeNP6FMR8i7FyTuIHXVZIl2-rDV6PUJbrdBeLWTMkW1LHes75MSYogi5WpipnUZSi_dMrKVE_Q..; "
        "SUHB=0ft56MbfaQ0Eoj; "
        "SSOLoginState=1457341350; "
        "gsid_CTandWM=4uSMCpOz5bPQsxwJzofPalwOoeX; "
        "H5_INDEX=0_all; "
        "H5_INDEX_TITLE=%E6%82%9F%E7%A9%BA%E7%9A%84%E7%B4%A7%E7%AE%8D; "
        "M_WEIBOCN_PARAMS=uicode%3D20000174"
}
url = 'http://weibo.cn/u/{0}?filter=1&page=1'.format(user_id)

html = requests.get(url, cookies=cookie).content
selector = etree.HTML(html)
pageNum = selector.xpath('//input[@name="mp"]')[0].attrib['value']

result = ""
urllist_set = set()
word_count = 1
image_count = 1

print("爬虫准备就绪...")

for page in range(1, int(pageNum) + 1):
    # 获取lxml页面
    # url = 'http://weibo.cn/u/%d?filter=1&page=%d' % (user_id, page)
    url = 'http://weibo.cn/u/{0}?filter=1&page={1}'.format(user_id, page)
    lxml = requests.get(url, cookies=cookie).content

    # 文字爬取
    selector = etree.HTML(lxml)
    content = selector.xpath('//span[@class="ctt"]')
    text = ''
    for each in content:
        text = each.xpath('string(.)')
        if word_count >= 4:
            text = "{0}: {1}\n\n".format((word_count-3), text)
        else:
            text += '\n\n'
    result = result + text
    word_count += 1

    # 图片爬取
    soup = BeautifulSoup(lxml, "lxml")
    urllist = soup.find_all('a', href=re.compile(r'^http://weibo.cn/mblog/oripic', re.I))
    first = 0
    for imgurl in urllist:
        urllist_set.add(requests.get(imgurl['href'], cookies=cookie).url)
        image_count += 1

fo = open("F:/Temp/sina/{0}_result.log".format(user_id), "wb")
fo.write(result)
print("-----------")
# word_path = os.getcwd() + '/%d' % user_id
word_path = "F:/Temp/sina/{0}".format(user_id)
print("文字微博爬取完毕")

link = ""
fo2 = open("/Users/Personals/%s_imageurls" % user_id, "wb")
for eachlink in urllist_set:
    link = link + eachlink + "\n"
fo2.write(link)
print("图片链接爬取完毕")

image_path = ''
if not urllist_set:
    print("该页面中不存在图片")
else:
    # 下载图片,保存在当前目录的pythonimg文件夹下
    image_path = os.getcwd() + '/weibo_image'
    if os.path.exists(image_path) is False:
        os.mkdir(image_path)
    x = 1
    for imgurl in urllist_set:
        temp = "{0}/{1}.jpg".format(image_path, x)
        print("正在下载第{0}张图片".format(x))
        try:
            urllib.urlretrieve(urllib2.urlopen(imgurl).geturl(), temp)
        except Exception, e:
            print("该图片下载失败: {0}\n{1}".format(imgurl, e))
        x += 1

print("原创微博爬取完毕，共{0}条，保存路径{1}".format(word_count-4, word_path))
print("微博图片爬取完毕，共{0}条，保存路径{1}".format(image_count-1, image_path))
