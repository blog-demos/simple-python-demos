# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC:   Sina登录测试
        http://lovenight.github.io/2015/11/23/Python-%E6%A8%A1%E6%8B%9F%E7%99%BB%E5%BD%95%E6%96%B0%E6%B5%AA%E5%BE%AE%E5%8D%9A/

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/3/7
Last Modify: 2016/3/9
version: 0.0.1
'''

import requests
import json
import base64

def login(user_name, password):
    user_name = base64.b64encode(user_name.encode('utf-8')).decode('utf-8')
    post_data = {
        "entry": "sso",
        "gateway": "1",
        "from": "null",
        "savestate": "30",
        "useticket": "0",
        "pagerefer": "",
        "vsnf": "1",
        "su": user_name,
        "service": "sso",
        "sp": password,
        "sr": "1440*900",
        "encoding": "UTF-8",
        "cdult": "3",
        "domain": "sina.com.cn",
        "prelt": "0",
        "returntype": "TEXT",
    }
    login_url = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
    session = requests.Session()
    res = session.post(login_url, data=post_data)
    json_string = res.content.decode('gbk')
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

if __name__ == '__main__':
    session = login('你的用户名', '你的密码')