# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC:   微信红包测试

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/3/7
Last Modify: 2016/3/9
version: 0.0.1
'''


import red_packets as red

def random_red():
    packets = red.RedPacket()
    packets.push(10, 10)
    red_list = packets.random_red()
    for item in red_list:
        print(item)

if __name__ == '__main__':
    random_red()
