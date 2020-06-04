# coding=utf-8
from bs4 import BeautifulSoup

from AbstractHTMLProcessor import AbstractHTMLProcessor


class CommonHTMLProcessor(AbstractHTMLProcessor):
    def __init__(self, name, url):
        super(CommonHTMLProcessor, self).__init__(name, url)

    def getTitleList(self, titleSelector):
        # soup = BeautifulSoup(html, 'lxml')
        titleList = self.soup.select(titleSelector)
        return titleList

    def getArtcleList(self):
        pass

    def getArtcleContent(self):
        pass

    def getWriteToFile(self):
        pass
