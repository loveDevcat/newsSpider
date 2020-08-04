# coding=utf-8
import re
import time


class AbstractNews(object):
    def __init__(self, config, HTMLProcessor, fileProcessor, decode='utf-8'):
        """抽象News类初始化"""
        self.FLAGS = False
        self.AbstractHTMLProcessor = HTMLProcessor
        self.AbstractFileProcessor = fileProcessor
        self.html = self.AbstractHTMLProcessor.getHTML(decode=decode)
        self.parentDic = config['parentDic']
        self.title = config['title']
        self.classForName = config['classForName']
        self.originUrl = config['originUrl']
        self.appendixUrl = config['appendixUrl']
        self.headers = config['headers']
        self.titleSelector = config['titleSelector']
        self.dateSelector = config['dateSelector']
        self.artcleTitleSelector = config['artcleTitleSelector']
        self.contentSelector = config['contentSelector']
        self.year = time.strftime("%Y")
        self.month = time.strftime("%m")
        self.day = time.strftime("%d")

    """验证url是否正确"""

    def validate_url(self, url):
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        match = pattern.match(url)
        if match:
            self.FLAGS = True
        return self.FLAGS

    def getTitleList(self):
        self.AbstractHTMLProcessor.getTitleList(self.titleSelector)

    def getArtcleDateList(self):
        self.AbstractHTMLProcessor.getArtcleDateList(self.dateSelector)

    def getArtcleList(self):
        self.getTitleList()
        self.getArtcleDateList()
        artcleList = self.AbstractHTMLProcessor.getArtcleList()
        return artcleList

    def getArtcleContent(self, url):
        contentList = self.AbstractHTMLProcessor.getArtcleContent(self.artcleTitleSelector, self.contentSelector, url)
        return contentList


    def start(self):
        pass
