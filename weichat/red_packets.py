# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC:   微信红包对象

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/3/7
Last Modify: 2016/3/9
version: 0.0.1
'''

import random

class RedPacket(object):
    def __init__(self):
        self.__total = 0  # 总数
        self.__remaining_amount = 0.0  # 余额
        self.__remaining_count = 0  # 剩余红包数
        pass

    def push(self, money=0.0, count=1):
        if money == 0 or money / count < 0.1:
            print("红包的配置不合法")
            return None

        self.__total = money
        self.__remaining_count = count
        self.__remaining_amount = money
        pass

    def pop(self):
        # print("({0}, {1})".format(self.__remaining_amount, self.__remaining_count))
        if self.__remaining_count == 0:
            print("红包已经发放完毕")
            return None
        elif self.__remaining_count == 1:
            return self.__remaining_amount
        figure = random.uniform(0.1, self.__remaining_amount / self.__remaining_count)
        self.__remaining_count -= 1
        self.__remaining_amount -= figure
        return figure

    def random_red(self):
        total = self.__remaining_count
        for item in xrange(total):
            yield self.pop()
