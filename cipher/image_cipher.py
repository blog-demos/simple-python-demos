# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC: 这个程序用于将信息的添加到图片文件中

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/2/24
Last Modify: 2016/3/9
version: 0.0.1
'''

# ------------------------------------------ #
# 将加密信息覆盖到图片的数据区域                   #
# 这里需要传入两个参数                           #
# container_file: 用于包装加密数据的容器图片      #
# data_file: 待加密的文件数据                   #
# output_file: 加密后生成的图片文件              #
# ------------------------------------------ #
def data_hide(container_file, data_file, output_file):
    container = open(container_file, "rb").read()
    data = open(data_file, "rb").read()

    if (len(data) + 1024) >= len(container):
        print "Not enough space to save", data_file
    else:
        f = open(output_file, "wb")
        f.write(container[: len(container)-len(data)])
        f.write(data)
        f.close()

# ------------------------------------------ #
# 将加密信息追加到图片的末尾                      #
# 这里需要传入两个参数                           #
# container_file: 用于包装加密数据的容器图片      #
# data_file: 待加密的文件数据                   #
# output_file: 加密后生成的图片文件              #
# ------------------------------------------ #
def data_append(container_file, data_file, output_file):
    container = open(container_file, "rb").read()
    data = open(data_file, "rb").read()
    f = open(output_file, "wb")
    f.write(container)
    f.write(data)
    f.close()
