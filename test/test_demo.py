# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC:   小测试

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/2/24
Last Modify: 2016/3/9
version: 0.0.1
'''

import operator
from enum.enums import Seasons

# @DeprecationWarning
def test_dep(name):
    print("Hi, %s." % name)

    l = "The {0:,} in hex is: {0:#x}, the {1:,} in hex is: {1:#x}.".format(12, 15)
    print(l)

    a = [3, 4, 2, 5, 1]
    sa = sorted(a)
    # a.sort()
    print(a)
    print(sa)
    s = ['sdfa', 'swie', 'werw', 'pioui', 'njn']
    s.sort()
    print(s)

def build_connection_string(params):
    """
    Build a connection string from a dictionary of parameters.Returns string.
    """
    print(params)
    season = Seasons()
    print(season.Autumn)

def test_enumerate():
    array = [1, 2, 3, 4, 5, 6]
    for index, data in enumerate(array):
        print("%d: %d" % (index, data))

    e = enumerate(array)
    print(e.next())
    print(e.next())
    print(e.next())

def test_sort():
    my_list = [(1, 3), (1, 2), (4, 5), (3, 1), (4, 1)]
    my_list.sort()
    print(my_list)

def test_lamdba1():
    p = lambda x, y: x + y
    z = p(1, 2)
    print(z)

def test_lamdba2(x=0):
    return lambda y: x + y

def test_lamdba3():
    z = lambda x: lambda y: x + y
    print((z(3))(4))

if __name__ == "__main__":
    # test_dep("Bob")
    build_connection_string("Bob")
    # test_sort()
    # lam = test_lamdba(15)
    test_lamdba1()
    print(test_lamdba2(15)(16))
    print(test_lamdba3())
