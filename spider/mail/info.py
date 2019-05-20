# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC:   一份邮件的详细信息

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/2/26
Last Modify: 2016/3/9
version: 0.0.1
'''

class MailInfo(object):
    def __init__(self):
        self.__account = None
        self.__passwd = None
        self.__contacts = None
        pass

    def set_account(self, account=None):
        self.__account = account

    def get_account(self):
        return self.__account

    def set_passwd(self, passwd=None):
        self.__passwd = passwd

    def get_passwd(self):
        return self.__passwd

    def set_contacts(self, contacts=None):
        self.__contacts = contacts

    def get_contacts(self):
        return self.__contacts
