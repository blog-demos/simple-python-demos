# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC: 拷贝的测试对象

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/2/26
Last Modify: 2016/3/9
version: 0.0.1
'''

class Student(object):

    def __init__(self, name=None):
        self.__name = name
        self.__sex = None
        self.__age = None
        self.__friends = None
        pass

    def get_name(self):
        return self.__name

    def get_sex(self):
        return self.__sex

    def set_sex(self, sex=None):
        self.__sex = sex

    def get_age(self):
        return self.__age

    def set_age(self, age=None):
        self.__age = age

    def get_friends(self):
        return self.__friends

    def set_friends(self, friends=None):
        self.__friends = friends

    def add_new_friend(self, friend=None):
        self.__friends.append(friend)

    def to_string(self):
        array = [self.get_name(), self.get_sex(), self.get_age(), self.get_friends()]
        return str(array)
