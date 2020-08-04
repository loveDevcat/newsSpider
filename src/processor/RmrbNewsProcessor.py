# coding=utf-8
import sys

from CommonNewsPaperProcessor import CommonNewsPaperProcessor


class RmrbNewsProcessor(CommonNewsPaperProcessor):
    def __init__(self, name, url):
        reload(sys)  # reload 才能调用 setdefaultencoding 方法
        sys.setdefaultencoding('utf-8')
        super(RmrbNewsProcessor, self).__init__(name, url)

    def getArtcleList(self, url, appendixUrl):
        print url
        print appendixUrl
        appendixList = self.soup.select("a[href$='.pdf']")
        PDFURLList = {}
        index = 1
        for i in appendixList:
            parentURL = appendixUrl + i.get("href")[-38:]
            PDFURLList[parentURL] = index
            index += 1
        return PDFURLList
