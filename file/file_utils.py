# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC: 循环遍历文件目录测试文件

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/2/25
Last Modify: 2016/3/9
version: 0.0.1
'''

import os
import os.path

def cycle_visiting(root_dir=None):
    for parent, folder_names, file_names in os.walk(root_dir):
        for folder_name in folder_names:
            print 'folder: ' + folder_name
        for file_name in file_names:
            print 'file: ' + os.path.join(parent, file_name)

if __name__ == '__main__':
    cycle_visiting('F:/Temp/')
