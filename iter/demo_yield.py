# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC: 测试生成器关键yield

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/2/26
Last Modify: 2016/3/9
version: 0.0.1
'''

def fibonacci_yield(limit):
    print("I'm in yield function...")
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

def fibonacci_for(limit):
    a, b = 0, 1
    result = []
    while a < limit:
        result.append(a)
        a, b = b, a + b
    return result

def factorial(limit):
    m = 1
    for item in range(limit):
        m *= (item + 1)
    return m

if __name__ == '__main__':
    n = 1000000
    # for i in fibonacci_yield(n):
    #     print(i)
    #
    # print(fibonacci_for(n))

    f = factorial(n)
    print("{0}!={1}\nlen = {2}".format(n, f, len(str(f))))
