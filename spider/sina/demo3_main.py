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

import demo3

# 保存微博账号的用户名和密码，第一行为用户名，第二行为密码
filename = 'account.cfg'

WBLogin = demo3.WeiboLogin()
if WBLogin.login(filename) == 1:
    print 'Login success!'
else:
    print 'Login error!'
    exit()
