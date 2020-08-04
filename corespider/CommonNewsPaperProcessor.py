# coding=utf-8
import sys
import time

import requests

from AbstractHTMLProcessor import AbstractHTMLProcessor


class CommonNewsPaperProcessor(AbstractHTMLProcessor):

    def __init__(self, name, url):
        reload(sys)  # reload 才能调用 setdefaultencoding 方法
        sys.setdefaultencoding('utf-8')
        super(CommonNewsPaperProcessor, self).__init__(name, url)

    def getArtcleList(self, url, appendixUrl):
        appendixList = self.soup.select("li[class='3'] > a")
        PDFURLList = {}
        index = 1
        for i in appendixList:
            parentURL = url[:-10] + i.get("href")
            self.getHTML(parentURL, decode='utf-8')
            tempUrl = self.soup.select("a[href$='.pdf']")[0].get("href")[-28:]
            PDFUrl = url[:-27] + tempUrl
            PDFURLList[PDFUrl] = index
            index += 1
        return PDFURLList

    def getArtcleContent(self, url):
        content = requests.get(url)
        return content.content
