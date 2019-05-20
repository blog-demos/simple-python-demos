# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC: 测试Python的Hash加密算法

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/2/24
Last Modify: 2016/3/9
version: 0.0.1
'''

import hashlib

# ----------------------------------------- #
# 使用SHA1的哈希算法加密                       #
# file_path: 待加密文件的目录                  #
# ----------------------------------------- #
def hash_sha1(file_path):
    print("SHA1加密：")
    with open(file_path, 'rb') as f:
        sha1 = hashlib.sha1()
        sha1.update(f.read())
        hash_text = sha1.hexdigest()
        return hash_text

# ----------------------------------------- #
# 使用SHA224的哈希算法加密                     #
# file_path: 待加密文件的目录                  #
# ----------------------------------------- #
def hash_sha224(file_path):
    print("SHA224加密：")
    with open(file_path, 'rb') as f:
        sha1 = hashlib.sha224()
        sha1.update(f.read())
        hash_text = sha1.hexdigest()
        return hash_text

# ----------------------------------------- #
# 使用SHA256的哈希算法加密                     #
# file_path: 待加密文件的目录                  #
# ----------------------------------------- #
def hash_sha256(file_path):
    print("SHA256加密：")
    with open(file_path, 'rb') as f:
        sha1 = hashlib.sha256()
        sha1.update(f.read())
        hash_text = sha1.hexdigest()
        return hash_text

# ----------------------------------------- #
# 使用SHA384的哈希算法加密                     #
# file_path: 待加密文件的目录                  #
# ----------------------------------------- #
def hash_sha384(file_path):
    print("SHA384加密：")
    with open(file_path, 'rb') as f:
        sha1 = hashlib.sha384()
        sha1.update(f.read())
        hash_text = sha1.hexdigest()
        return hash_text

# ----------------------------------------- #
# 使用SHA512的哈希算法加密                     #
# file_path: 待加密文件的目录                  #
# ----------------------------------------- #
def hash_sha512(file_path):
    print("SHA512加密：")
    with open(file_path, 'rb') as f:
        sha1 = hashlib.sha512()
        sha1.update(f.read())
        hash_text = sha1.hexdigest()
        return hash_text

# ----------------------------------------- #
# 使用MD5的哈希算法加密                        #
# file_path: 待加密文件的目录                  #
# ----------------------------------------- #
def hash_md5(file_path):
    print("MD5加密：")
    with open(file_path, 'rb') as f:
        sha1 = hashlib.md5()
        sha1.update(f.read())
        hash_text = sha1.hexdigest()
        return hash_text
