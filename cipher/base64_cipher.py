# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC: 进行base64加密和解密

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/2/24
Last Modify: 2016/3/9
version: 0.0.1
'''

import base64

# ----------------------------------------- #
# 使用base64加密算法加密                       #
# plaintext: 待加密的字符串                   #
# ----------------------------------------- #
def encode(plaintext):
    ciphertext = base64.b64encode(plaintext)
    return ciphertext

# ----------------------------------------- #
# 使用base64解密算法解密                       #
# ciphertext: 待解密的字符串                   #
# ----------------------------------------- #
def decode(ciphertext):
    plaintext = base64.b64decode(ciphertext)
    return plaintext
