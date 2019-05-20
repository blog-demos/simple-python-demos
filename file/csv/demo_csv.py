# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC: 与CSV文件操作相关测试Demo

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/2/25
Last Modify: 2016/3/9
version: 0.0.1
'''

import csv

# ----------------------------------------- #
# 读取CSV文件中的内容                          #
# ----------------------------------------- #
def read_csv(file_path):
    reader = csv.reader(file(file_path, 'rb'))
    for line in reader:
        print(line)

# ----------------------------------------- #
# 向CSV文件中写入指定内容                       #
# ----------------------------------------- #
def write_csv(file_path, data):
    writer = csv.writer(file(file_path, 'wb'))

    for data_raw in data:
        writer.writerow(data_raw)

# ----------------------------------------- #
# 程序入口                                   #
# ----------------------------------------- #
if __name__ == '__main__':
    data = [['0', '1', '2'], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    write_csv('F:/Temp/a.csv', data)

    read_csv('F:/Temp/a.csv')
