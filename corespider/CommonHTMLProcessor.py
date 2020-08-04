# coding=utf-8
import sys
import time

from bs4 import BeautifulSoup

from AbstractHTMLProcessor import AbstractHTMLProcessor


class CommonHTMLProcessor(AbstractHTMLProcessor):
    def __init__(self, name, url):
        reload(sys)  # reload 才能调用 setdefaultencoding 方法
        sys.setdefaultencoding('utf-8')
        super(CommonHTMLProcessor, self).__init__(name, url)

    def getTitleList(self, titleSelector):
        self.titleList = self.soup.select(titleSelector)
        return self.titleList

    def getArtcleDateList(self, dateSelector):
        self.dateList = self.soup.select(dateSelector)
        return self.dateList

    def getArtcleList(self):
        artcleList = {}
        titleList = self.titleList
        dateList = self.dateList
        if len(titleList) != len(dateList):
            for item in titleList:
                url = self.url + item.get("href")
                # artcleList2.append(self.url + item.get("href"))
                date = time.strftime("%m月%d日", time.localtime(time.time()))
                artcleList[url] = date
            return artcleList
        else:
            index = 0
            for item in titleList:
                # artcleList1[dateList[index]] = self.url + item.get("href")
                url = self.url + item.get("href")
                date = dateList[index].get_text()
                artcleList[url] = date[:6].replace('/', '月').replace(' ', '日')
                index += 1
            return artcleList

    def getArtcleContent(self, artcleTitleSelector, contentSelector, url):
        self.getHTML(url)
        artcleContentList = self.soup.select(contentSelector)
        title = self.soup.select(artcleTitleSelector)
        artcleTitle = title[0].get_text()
        artcleContentList.insert(0, artcleTitle)
        return artcleContentList
