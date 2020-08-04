# coding=utf-8
import time

from AbstractNews import AbstractNews


class NewsPapers(AbstractNews):
    year = time.strftime("%Y")
    month = time.strftime("%m")
    day = time.strftime("%d")

    def __init__(self, config, HTMLProcessor, fileProcessor):
        super(NewsPapers, self).__init__(config, HTMLProcessor, fileProcessor)
        self.url = NewsPapers.getURL(self.originUrl)
        self.html = self.AbstractHTMLProcessor.getHTML(self.url, decode='utf-8')

    @staticmethod
    def getURL(url, year=year, month=month, day=day):
        reUrl = url.replace('year', year).replace('month', month).replace('day', day)
        return reUrl

    def getArtcleList(self):
        artcleList = self.AbstractHTMLProcessor.getArtcleList(self.url, self.appendixUrl)
        return artcleList

    def getArtcleContent(self, url):
        contentList = self.AbstractHTMLProcessor.getArtcleContent(url)
        return contentList

    def start(self):
        self.AbstractFileProcessor.initFileDic()
        # self.AbstractFileProcessor.month = '06'
        # self.AbstractFileProcessor.day = '16'
        artcleList = self.getArtcleList()
        if artcleList < 2:
            print '今天没有该新闻'
            return 0
        for item in artcleList:
            dest = artcleList[item]
            flag = self.validate_url(item)
            if flag:
                context = self.getArtcleContent(item)
                if len(context) > 1:
                    self.AbstractFileProcessor.fileToZip(context, dest)
                else:
                    # print "该文章为空,已跳过！"
                    continue
            else:
                continue
        print '报纸已经下载完成'
        self.AbstractFileProcessor.compressFile(self.title, self.month, self.day)
        print '报纸已经压缩'

    def test(self):
        t = self.AbstractHTMLProcessor
        tt = self.start()
