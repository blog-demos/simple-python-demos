# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC: 这个是测试程序的入口

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/2/24
Last Modify: 2016/3/9
version: 0.0.1
'''

import sys
import config.config as conf
import cipher.image_cipher as cipher
from games.game_2048 import Game2048
import cipher.hash_cipher as hah
import cipher.base64_cipher as base64
import db.db_server as helper
import db.db_config as db_conf

# ----------------------------------------- #
# 基于图片的信息隐藏逻辑                        #
# ----------------------------------------- #
def data_cipher(argv=None):
    print("正在进行数据隐藏...")
    cipher.data_append(argv[1], argv[2], argv[3])

# ----------------------------------------- #
# 执行2048游戏代码逻辑                         #
# ----------------------------------------- #
def play_game(argv=None):
    print('玩游戏2048')
    game = Game2048()
    game.play()

# ----------------------------------------- #
# 哈希加密逻辑                                #
# ----------------------------------------- #
def hash_cipher(argv=None):
    print(hah.hash_sha1("F:/Temp/Trojans.zip"))

# ----------------------------------------- #
# base64加密算法加密字符串                     #
# ----------------------------------------- #
def base64_cipher(argv=None):
    ciphertext = base64.encode("这是一段明文。")
    print("base64加密结果：%s" % ciphertext)
    plaintext = base64.decode(ciphertext)
    print("base64解密结果：%s" % plaintext)

# ----------------------------------------- #
# 数据库的测试函数                             #
# ----------------------------------------- #
def database_demo(argv=None):
    print(argv)
    db_server = helper.DatabaseServer()
    print(db_server.fetch_all('show databases;'))
    db_server.update('CREATE TABLE %s(id INT NOT NULL AUTO_INCREMENT, name VARCHAR(20),'
                     ' sex INT, age INT, info VARCHAR(50), PRIMARY KEY (id));' % db_conf.DB_TABLE_NAME)
    db_server.close()

# 测试逻辑与标签的对应关系
operator = {
    conf.IMAGE_CIPHER_APPEND: data_cipher,
    conf.IMAGE_CIPHER_HIDE: data_cipher,
    conf.GAME_2048: play_game,
    conf.HASH_CIPHER_SHA1: hash_cipher,
    conf.HASH_CIPHER_DM5: hash_cipher,
    conf.HASH_CIPHER_SHA224: hash_cipher,
    conf.HASH_CIPHER_SHA256: hash_cipher,
    conf.HASH_CIPHER_SHA384: hash_cipher,
    conf.HASH_CIPHER_SHA512: hash_cipher,
    conf.BASE64_CIPHER: base64_cipher,
    conf.DATABASE_DEMO: database_demo,
}

# ----------------------------------------- #
# 程序的主执行逻辑                             #
# ----------------------------------------- #
def execute(argv=None, mode=conf.DEMO_MODE):
    operator.get(mode)(argv)

# ----------------------------------------- #
# 主程序入口                                  #
# ----------------------------------------- #
if "__main__" == __name__:
    execute(sys.argv)
