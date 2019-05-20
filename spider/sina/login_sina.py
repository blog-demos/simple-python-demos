# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC:   模拟登录新浪微博

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/3/7
Last Modify: 2016/3/9
version: 0.0.1
'''

import requests
import json
import base64

login_url = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'

# ------------------------------------- #
# 登录微博帐户                            #
# account_info: 帐户信息                 #
# ------------------------------------- #
def login(account_info=None):
    if account_info is None or len(account_info) < 2:
        print("帐户信息不合法")
        return None
    name = base64.b64encode(account_info[0].encode('utf-8')).decode('utf-8')
    passwd = account_info[1]
    post_data = {
        "entry": "sso",
        "gateway": "1",
        "from": "null",
        "savestate": "30",
        "useticket": "0",
        "pagerefer": "",
        "vsnf": "1",
        "su": name,
        "service": "sso",
        "sp": passwd,
        "sr": "1440*900",
        "encoding": "UTF-8",
        "cdult": "3",
        "domain": "sina.com.cn",
        "prelt": "0",
        "returntype": "TEXT",
    }
    session = requests.Session()
    res = session.post(login_url, data=post_data)
    json_string = res.content.decode('utf8')
    info = json.loads(json_string)
    if info["retcode"] == "0":
        print("登录成功")
        # 把cookies添加到headers中，必须写这一步，否则后面调用API失败
        cookies = session.cookies.get_dict()
        cookies = [key + "=" + value for key, value in cookies.items()]
        cookies = "; ".join(cookies)
        session.headers["cookie"] = cookies
    else:
        print("登录失败，原因： %s" % info["reason"])
    return session

# ------------------------------------- #
# 获得微博帐户信息                         #
# ------------------------------------- #
def get_account_info():
    with open("account.cfg", "rb") as f:
        return f.readlines()

if __name__ == '__main__':
    login_session = login(get_account_info())
    print(login_session)
