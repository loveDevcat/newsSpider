# coding=utf-8
import json
import os
import sys

from CjdtNews import CjdtNews
from CommonHTMLProcessor import CommonHTMLProcessor


class App(object):
    def __init__(self):
        pass

    """获取config中的数据"""

    def get_config(self, fileName='cjdt.json'):
        configPath = os.path.dirname(os.getcwd()) + os.sep + 'config' + os.sep + fileName
        if not os.path.isfile(configPath):
            sys.exit(u'请先配置当前目录(%s)下的config.json文件' % os.getcwd())
        try:
            with open(configPath) as f:
                config = json.loads(f.read())
                return config
        except Exception:
            sys.exit(u'config.json 格式不正确，请参考 '
                     u'https://github.com/dataabc/weiboSpider#3程序设置')

    """初始化News类"""

    def builder(self, config):
        pass

    """批量初始化News类"""

    def builderFactory(self, confPath='config'):
        pass

    def workQueue(self):
        pass


#     def main(self):
#         HTMLProcessor = AbstractHTMLProcessor('test')
#         print(HTMLProcessor.getHTML())
#         # news = AbstractNews()
#
app = App()
conf = app.get_config()
name = conf['name']
url = conf['originUrl']
p = CommonHTMLProcessor(name, url)
c = CjdtNews(conf, p, None)
c.test()
