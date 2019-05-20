# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC:   邮件发送器

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/2/26
Last Modify: 2016/3/9
version: 0.0.1
'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

class Sender(object):
    def __init__(self, info=None):
        self.__info = info
        self.__handle = None

    # ----------------------------------------- #
    # 登录邮箱                                   #
    # ----------------------------------------- #
    def login_mail(self):
        sender = self.__info.get_account()
        passwd = self.__info.get_passwd()
        try:
            self.__handle = smtplib.SMTP()
            self.__handle.connect('smtp.163.com', 25)
            self.__handle.login(sender, passwd)
        except Exception, e:
            print("Login exception: {0}".format(e))

    # ----------------------------------------- #
    # 发送附件邮件                                #
    # ----------------------------------------- #
    def send_annex_mail(self):
        msg_root = self.__read_annex("F:/Temp/Mail-File.txt")
        self.__send(msg_root.as_string())

    # ----------------------------------------- #
    # 发送文本邮件                                #
    # ----------------------------------------- #
    def send_text_mail(self):
        msg = "To: {0}\nFrom: {1}\nSubject: 这是一封来自火星的邮件，请勿点开哦~"\
            .format(self.__info.get_contacts(), self.__info.get_account())
        self.__send(msg)

    # ----------------------------------------- #
    # 发送邮件                                   #
    # ----------------------------------------- #
    def __send(self, msg=None):
        sender = self.__info.get_account()
        contacts = self.__info.get_contacts()
        try:
            for receiver in contacts:
                self.__handle.sendmail(sender, receiver, msg)
            # self.__handle.close()
            return 1
        except Exception, e:
            print("Send mail has a exception: {0}, {1}".format(e, self.__handle))
            self.__handle.close()
            return 0

    # ----------------------------------------- #
    # 读取附件信息                                #
    # ----------------------------------------- #
    @staticmethod
    def __read_annex(annex_path=None):
        msg_root = MIMEMultipart('related')

        annex = MIMEText(open(annex_path, 'rb').read(), 'base64', 'utf-8')
        annex["Content-Type"] = 'application/octet-stream'
        annex["Content-Disposition"] = 'attachment; filename="Mail-File.txt"'
        msg_root['Subject'] = '这是一封来自火星的邮件，请勿点开哦~'
        msg_root.attach(annex)
        return msg_root
