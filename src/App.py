# coding=utf-8
import datetime

import json
import os
import shutil
import sys
import time

from AbstractNews import AbstractNews
from CjdtNews import CjdtNews
from CommonFileProcessor import CommonFileProcessor

from CommonHTMLProcessor import CommonHTMLProcessor
from CommonNewsPaperProcessor import CommonNewsPaperProcessor
from GjxwNews import GjxwNews
from GnxwNews import GnxwNews
from GnxwNewsProcessor import GnxwNewsProcessor
from HdbNewsPaperProcessor import HdbNewsPaperProcessor
from LdhdNews import LdhdNews
from LdhdNewsProcessor import LdhdNewsProcessor
from NewsPapers import NewsPapers
from RmrbNewsProcessor import RmrbNewsProcessor
from TzggNewsProcessor import TzggNewsProcessor


class App(object):
    year = time.strftime("%Y")
    month = time.strftime("%m")
    day = time.strftime("%d")

    def __init__(self):
        self.workQueue = []
        self.confQueue = {}
        path = os.path.dirname(os.getcwd()) + os.sep + 'output'
        files = os.listdir(path)
        for file in files:
            if 'zip' in file:
                os.remove(path + os.sep + file)
        print '系统初始化完成!'

    """获取config中的数据"""

    def getConfig(self, fileName='cjdt.json'):
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

    def getConfigs(self, confPath='config'):
        path = os.path.dirname(os.getcwd()) + os.sep + confPath
        index = 0
        for file in os.listdir(path):
            if '.DS_Store' not in file:
                config = self.getConfig(file)
                className = config['classForName'] + str(index)
                self.confQueue[className] = config
                index += 1
        return self.confQueue

    def buildFactory(self):
        configs = self.getConfigs()
        for item in configs:
            conf = configs[item]
            classForName = conf['classForName']
            classForProcessor = conf['classForProcessor']
            url = conf['originUrl']
            name = conf['parentDic']
            klass = globals()[classForProcessor]
            pObj = klass(classForName, url)
            clazz = globals()[classForName]
            fClass = CommonFileProcessor(name)
            nObj = clazz(conf, pObj, fClass)
            self.workQueue.append(nObj)
        return self.workQueue

    def run(self):
        workQueue = self.buildFactory()
        for item in workQueue:
            item.start()
        # self.deleteByDate()

    def deleteByDate(self, rootDic='output', date=''):
        c = (datetime.datetime.now() + datetime.timedelta(days=-5))
        month = c.strftime('%m')
        day = c.strftime('%d')
        dateStr = None
        if date:
            dateStr = date
        else:
            dateStr = month + '月' + day + '日'
        path = os.path.dirname(os.getcwd()) + os.sep + rootDic
        preDels = os.listdir(path)
        for item in preDels:
            print ('正在扫描 %s 文件夹下的过期新闻...' % item)
            sep_item = path + os.sep + item
            print sep_item
            if (os.path.isdir(sep_item)):
                preDels = os.listdir(sep_item)
                for file in preDels:
                    if dateStr not in file:
                        sep_file = sep_item + os.sep + file
                        shutil.rmtree(sep_file, True)
                        # print ('删除文件:%s成功' % file)
                print ('%s 文件夹下的过期新闻已经成功删除' % item)


app = App()
app.run()
