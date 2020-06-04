# coding=utf-8
import requests
from bs4 import BeautifulSoup


class AbstractHTMLProcessor(object):
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.html = None
        self.soup = None

    def getHTML(self, decode='gb2312'):
        try:
            response = requests.get(self.url)
            result = response.content.decode(decode, 'ignore')
            if response.status_code == 200:
                self.html = result
                self.soup = BeautifulSoup(self.html, 'lxml')
                return result

        except requests.RequestException:
            print('无法连接到' + self.url + ',请检查网络设置！')

    def getTitleList(titleSelector):
        pass

    def getArtcleList(self):
        pass

    def getArtcleContent(self):
        pass

    def getWriteToFile(self):
        pass
