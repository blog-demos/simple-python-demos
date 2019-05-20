# encoding=utf-8

__author__ = 'Q-Whai'
'''
DESC:   HTML文件的格式解析工具模块
        此模块为自定义模块，主要针对抓取豆瓣网的电影排行榜

Blog: http://blog.csdn.net/lemon_tree12138
Create Date: 2016/2/25
Last Modify: 2016/3/9
version: 0.0.2
'''

import HTMLParser

class DoubanMovieParser(HTMLParser.HTMLParser):

    # ----------------------------------------- #
    # 默认初始化方法                               #
    # ----------------------------------------- #
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.__tag_div_flag = False  # 进入影片排行榜标志开关
        self.__tag_a_flag = False  # 进入影片链接标志开关
        self.__tag_p_flag = False  # 进入影片简介标志开关

    # ----------------------------------------- #
    # 处理<!开头的内容                             #
    # ----------------------------------------- #
    def handle_decl(self, decl):
        # print '声明：' + decl
        pass

    # ----------------------------------------- #
    # 处理开始标签                                #
    # tag:      标签的名称                        #
    # attrs:    标签属性值                        #
    # ----------------------------------------- #
    def handle_starttag(self, tag, attrs):
        # 解析<div/>标签下的信息
        if tag == 'div':
            for name, value in attrs:
                if name == 'class' and value == 'indent':
                    self.__tag_div_flag = True

        # 解析<a/>标签下的信息
        if tag == 'a':
            for name, value in attrs:
                if self.__tag_div_flag and name == 'class' and value == 'nbg':
                    self.__tag_a_flag = True
                if self.__tag_a_flag and name == 'title':
                    print(u"电影名称：{0}".format(value))
                if self.__tag_a_flag and name == 'href':
                    print(u"具体链接：{0}".format(value))

        # 解析<p/>标签下的信息
        if tag == 'p':
            for name, value in attrs:
                if self.__tag_div_flag and name == 'class' and value == 'pl':
                    self.__tag_p_flag = True

    # ----------------------------------------- #
    # 处理结尾标签                                #
    # tag:      标签的名称                        #
    # ----------------------------------------- #
    def handle_endtag(self, tag):
        # if tag == 'div':
        #     self.__tag_div_flag = False

        if tag == 'a':
            self.__tag_a_flag = False

        if tag == 'p':
            self.__tag_p_flag = False

    # ----------------------------------------- #
    # 解析影片简介                                #
    # data:     简介内容                         #
    # ----------------------------------------- #
    def handle_data(self, data):
        if self.__tag_p_flag:
            print(u"电影简介：{0}\n".format(data.decode("utf-8")))

    # ----------------------------------------- #
    # 处理注释                                   #
    # comment:      注释内容                     #
    # ----------------------------------------- #
    def handle_comment(self, comment):
        # print '注释: ' + comment
        pass
