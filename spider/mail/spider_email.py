# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC:   邮件收发测试

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/2/25
Last Modify: 2016/3/9
version: 0.0.1
'''

import sys
import poplib
import smtplib

# 邮件发送函数
def send_mail():
    try:
        handle = smtplib.SMTP('smtp.163.com', 25)
        handle.login('return_zero0@163.com', 'your_email_passwd')
        msg = 'To: 1614813998@qq.com\r\nFrom:return_zero0@163.com\r\nSubject:hello\r\n'
        handle.sendmail('return_zero0@163.com', '1614813998@qq.com', msg)
        handle.close()
        return 1
    except Exception, e:
        print("send mail has a exception, {0}".format(e))
        return 0

# 邮件接收函数
def accpet_mail():
    try:
        p = poplib.POP3('pop.163.com', 110)
        p.user('return_zero0@163.com')
        p.pass_('shinichi260606')
        ret = p.stat()  # 返回一个元组:(邮件数, 邮件尺寸)
        print(ret)
        # p.retr('邮件号码')方法返回一个元组:(状态信息,邮件, 邮件尺寸)
    except poplib.error_proto, e:
        print("Login failed: ".format(e))
        sys.exit(1)


# 运行当前文件时，执行sendmail和accpet_mail函数
if __name__ == "__main__":
    # send_mail()
    accpet_mail()
