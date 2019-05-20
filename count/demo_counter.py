# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC: 使用Counter进行计数统计

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/2/25
Last Modify: 2016/3/9
version: 0.0.1
'''

from collections import Counter

def get_counter(data):
    print("计数前：\n{0}".format(data))
    print("计数后：\n{0}".format(Counter(data)))

if __name__ == '__main__':
    get_counter(['d', 'a', 'd', 'a', 's', 'e', 'f', 'h', 'w', 'e', 'q', 'd', 'e', 'w', 'f', 's', 'd', 'a'])
