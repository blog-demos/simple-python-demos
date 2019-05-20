# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC: 测试对象的拷贝

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/2/26
Last Modify: 2016/3/9
version: 0.0.1
'''

import copy
from object_mode import Student

def object_copy(obj):
    # return copy.copy(obj)
    return copy.deepcopy(obj)

if __name__ == '__main__':
    s1 = Student("Bob")
    s1.set_age(18)
    s1.set_sex("Boy")
    s1.set_friends(["A", "B", "C"])

    s2 = object_copy(s1)

    print(s1.to_string())
    print(s2.to_string())

    print(id(s1.get_friends()))
    print(id(s2.get_friends()))

    s2.set_age(19)

    s2.add_new_friend("D")

    print(s1.to_string())
    print(s2.to_string())

    a = 1
    b = -2
    print(b.__abs__())
    c = a.__xor__(b.__abs__())
    print(c)
