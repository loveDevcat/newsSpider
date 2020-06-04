# coding=utf-8
class AbstractNews(object):
    def __init__(self, config, HTMLProcessor, fileProcessor):
        """抽象News类初始化"""
        self.AbstractHTMLProcessor = HTMLProcessor
        self.AbstractFileProcessor = fileProcessor
        self.html = self.AbstractHTMLProcessor.getHTML()
        self.name = config['name']
        self.classForName = config['classforname']
        self.originUrl = config['originUrl']
        self.appendixUrl = config['appendixUrl']
        self.headers = config['headers']
        self.titleSelector = config['titleSelector']
        self.dataSelector = config['dataSelector']

    def getTitleList(self):
        self.AbstractHTMLProcessor.getTitleList(self.titleSelector)

    def getArtcleList(self):
        self.AbstractHTMLProcessor.getArtcleList()

    def getArtcleContent(self):
        self.AbstractHTMLProcessor.getArtcleContent()

    def writeToFile(self):
        self.AbstractFileProcessor.writeToFile()

    def start(self):
        pass
