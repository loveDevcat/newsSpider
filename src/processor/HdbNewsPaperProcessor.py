# coding=utf-8
import sys

from CommonNewsPaperProcessor import CommonNewsPaperProcessor


class HdbNewsPaperProcessor(CommonNewsPaperProcessor):
    def __init__(self, name, url):
        reload(sys)  # reload 才能调用 setdefaultencoding 方法
        sys.setdefaultencoding('utf-8')
        super(HdbNewsPaperProcessor, self).__init__(name, url)
        self.box = ['col01.html', 'col02.html', 'col03.html', 'col04.html']

    def getArtcleList(self, url, appendixUrl):
        index = 1
        PDFURLList = {}
        for page in self.box:
            pageUrl = url[:-10] + page
            self.getHTML(pageUrl, decode='utf-8')
            try:
                appendixList = self.soup.select("a[href$='.pdf']")
            except Exception:
                return 0
            parentURL = appendixUrl + appendixList[0].get("href")[5:]
            PDFURLList[parentURL] = index
            index += 1
        return PDFURLList
