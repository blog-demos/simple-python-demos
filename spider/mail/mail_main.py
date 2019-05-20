# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC:   邮件收发测试

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/2/26
Last Modify: 2016/3/9
version: 0.0.1
'''

import time
import info
import mail_sender

# ----------------------------------------- #
# 创建邮件信息                                #
# ----------------------------------------- #
def create_mail_info(account, password, receiver):
    mail_info = info.MailInfo()
    mail_info.set_account(account)
    mail_info.set_passwd(password)
    mail_info.set_contacts(receiver)
    return mail_info

# ----------------------------------------- #
# 从文件中读取接收人的地址                       #
# ----------------------------------------- #
def read_receiver(receiver_path):
    receiver = []
    with open(receiver_path, "rb") as f:
        receiver.append(f.readlines())
    f.close()
    return receiver

# ----------------------------------------- #
# 定时发送邮件                                #
# ----------------------------------------- #
def timer_to_send(account, password, receiver_path):
    mail_info = create_mail_info(account, password, read_receiver(receiver_path))
    mail = mail_sender.Sender(mail_info)
    mail.login_mail()

    index = 0

    while index < 1000:
        mail.send_text_mail()
        print("第{0}封邮件已发出！".format(index))
        time.sleep(10)
        index += 1
    pass

if __name__ == '__main__':
    print("登录用户名："),
    user_name = raw_input()

    print("密码："),
    passwd = raw_input()

    print("请输入保存联系人的文件目录："),
    contacts = raw_input()

    timer_to_send(user_name, passwd, contacts)

