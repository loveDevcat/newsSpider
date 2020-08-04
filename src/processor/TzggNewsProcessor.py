# coding=utf-8
import sys
import time

from CommonHTMLProcessor import CommonHTMLProcessor
from CommonNewsPaperProcessor import CommonNewsPaperProcessor


class TzggNewsProcessor(CommonHTMLProcessor):
    def __init__(self, name, url):
        reload(sys)  # reload 才能调用 setdefaultencoding 方法
        sys.setdefaultencoding('utf-8')
        super(TzggNewsProcessor, self).__init__(name, url)

    def getArtcleList(self):
        artcleList = {}
        titleList = self.titleList
        dateList = self.dateList
        if len(titleList) != len(dateList):
            print "注意，二者长度不想等！"
            for item in titleList:
                url = item.get("href")
                # artcleList2.append(self.url + item.get("href"))
                date = time.strftime("%m月%d日", time.localtime(time.time()))
                artcleList[url] = date
            return artcleList
        else:
            index = 0
            for item in titleList:
                # artcleList1[dateList[index]] = self.url + item.get("href")
                url = item.get("href")
                date = dateList[index].get_text()
                artcleList[url] = date[5:].replace('-', '月') + '日'
                index += 1
            return artcleList

    def getArtcleContent(self, artcleTitleSelector, contentSelector, url):
        html = self.getHTML(url, 'utf-8')
        artcleContentList = self.soup.select(contentSelector)
        title = self.soup.select(artcleTitleSelector)
        artcleTitle = title[0].get_text()
        artcleContentList.insert(0, artcleTitle)
        return artcleContentList
