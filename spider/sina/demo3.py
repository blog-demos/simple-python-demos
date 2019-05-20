# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC:   新浪微博脚本

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/3/7
Last Modify: 2016/3/9
version: 0.0.1
'''

# http://blog.csdn.net/monsion/article/details/8656690

import urllib
import urllib2
import cookielib
import base64
import re
import json
import rsa
import binascii

class WeiboLogin(object):
    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    postdata = {
        'entry': 'weibo',
        'gateway': '1',
        'from': '',
        'savestate': '7',
        'userticket': '1',
        'ssosimplelogin': '1',
        'vsnf': '1',
        'vsnval': '',
        'su': '',
        'service': 'miniblog',
        'servertime': '',
        'nonce': '',
        'pwencode': 'rsa2',
        'sp': '',
        'encoding': 'UTF-8',
        'prelt': '115',
        'rsakv': '',
        'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'META'
    }

    def __init__(self):
        pass

    @staticmethod
    @DeprecationWarning
    def get_servertime(username):
        # url = r'http://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&su=%s&rsakt=mod&client=ssologin.js(v1.4.4)' % username
        url = "http://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&" \
              "su={0}&rsakt=mod&client=ssologin.js(v1.4.4)".format(username)
        data = urllib2.urlopen(url).read()
        p = re.compile('.*')
        try:
            json_data = p.search(data).group(1)
            data = json.loads(json_data)
            servertime = str(data['servertime'])
            nonce = data['nonce']
            pubkey = data['pubkey']
            rsakv = data['rsakv']
            return servertime, nonce, pubkey, rsakv
        except Exception, e:
            print("Get severtime error! {0}".format(e))
            return None

    @staticmethod
    def get_servertime2(username):
        # url = r'http://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&su=%s&rsakt=mod&client=ssologin.js(v1.4.4)' % username
        url = "http://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&su={0}&" \
              "rsakt=mod&client=ssologin.js(v1.4.4)".format(username)
        data = urllib2.urlopen(url).read()
        try:
            json_data = data[35:-1]
            data = json.loads(json_data)
            servertime = str(data['servertime'])
            nonce = data['nonce']
            pubkey = data['pubkey']
            rsakv = data['rsakv']
            return servertime, nonce, pubkey, rsakv
        except Exception, e:
            print("Get severtime error! {0}".format(e))
            return None

    @staticmethod
    def get_pwd(password, servertime, nonce, pubkey):
        rsa_public_key = int(pubkey, 16)
        key = rsa.PublicKey(rsa_public_key, 65537)  # 创建公钥
        message = str(servertime) + '\t' + str(nonce) + '\n' + str(password)  # 拼接明文js加密文件中得到
        passwd = rsa.encrypt(message, key)  # 加密
        passwd = binascii.b2a_hex(passwd)  # 将加密信息转换为16进制。
        return passwd

    @staticmethod
    def get_user(username):
        username_ = urllib.quote(username)
        username = base64.encodestring(username_)[:-1]
        return username

    @staticmethod
    def get_account(filename):
        f = file(filename)
        flag = 0
        username = ''
        pwd = ''
        for line in f:
            if flag == 0:
                username = line.strip()
                flag += 1
            else:
                pwd = line.strip()
        f.close()
        return username, pwd

    def login(self, filename):
        username, pwd = self.get_account(filename)

        url = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
        try:
            servertime, nonce, pubkey, rsakv = self.get_servertime2(username)
            # print servertime
            # print nonce
            # print pubkey
            # print rsakv
        except Exception, e:
            print("Get servertime error! {0}".format(e))
            return
        weiboLogin.postdata['servertime'] = servertime
        weiboLogin.postdata['nonce'] = nonce
        weiboLogin.postdata['rsakv'] = rsakv
        weiboLogin.postdata['su'] = self.get_user(username)
        weiboLogin.postdata['sp'] = self.get_pwd(pwd, servertime, nonce, pubkey)
        weiboLogin.postdata = urllib.urlencode(weiboLogin.postdata)
        headers = {
            'User-Agent':
                'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0 Chrome/20.0.1132.57 Safari/536.11'
        }
        req = urllib2.Request(
            url=url,
            data=weiboLogin.postdata,
            headers=headers
        )
        result = urllib2.urlopen(req)
        text = result.read()
        # print text
        p = re.compile('location\.replace\"(.∗)\"')  # 此处和之前略有区别，小心！
        try:
            login_url = p.search(text).group(1)
            print login_url
            urllib2.urlopen(login_url)
            print("Login success!")
            return 1
        except Exception, e:
            print("Login error! {0}".format(e))
            return 0
