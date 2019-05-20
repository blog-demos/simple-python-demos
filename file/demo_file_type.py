# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC: 测试文件类型

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/2/25
Last Modify: 2016/3/9
version: 0.0.1
'''

import struct

# 支持文件类型
# 用16进制字符串的目的是可以知道文件头是多少字节
# 各种文件头的长度不一样，少则2字符，长则8字符
def type_list_table():
    return {
        "FFD8FF": "JPEG",
        "89504E47": "PNG",
        "47494638": "GIF",
        "49492A00": "TIFF",
        "424D": "BMP",
        "41433130": "CAD",
        "38425053": "Adobe Photoshop",
        "7B5C727466": "Rich Text Format(rtf)",
        "3C3F786D6C": "XML",
        "68746D6C3E": "HTML",
        "D0CF11E0": "MS Word/Excel (xls.or.doc)",
        "5374616E64617264204A": "MS Access (mdb)",
        "4357530A": "Flash data [swf]"
    }

# ----------------------------------------- #
# 字节码转16进制字符串                         #
# ----------------------------------------- #
def bytes2hex(byte_array):
    num = len(byte_array)
    hex_string = u""
    for i in range(num):
        t = u"%x" % byte_array[i]
        if len(t) % 2:
            hex_string += u"0"
        hex_string += t
    return hex_string.upper()

# ----------------------------------------- #
# 获取文件类型                                #
# ----------------------------------------- #
def file_type(file_name):
    file_reader = open(file_name, 'rb')     # 必须二制制读取
    type_list = type_list_table()
    type_label = 'unknown'
    for value in type_list.keys():
        num_of_bytes = len(value) / 2       # 需要读多少字节
        file_reader.seek(0)                 # 每次读取都要回到文件头，不然会一直往后读取
        hbytes = struct.unpack_from("B" * num_of_bytes, file_reader.read(num_of_bytes))  # 一个“B”表示一个字节
        type_code = bytes2hex(hbytes)
        if type_code == value:
            type_label = type_list[value]
            break
    file_reader.close()
    return type_label

if __name__ == '__main__':
    print file_type('xxx/xxx.jpg')
