# coding=utf-8
from AbstractNews import AbstractNews


class LdhdNews(AbstractNews):
    def __init__(self, config, HTMLProcessor, fileProcessor):
        super(LdhdNews, self).__init__(config, HTMLProcessor, fileProcessor)

    def start(self):
        artcleList = self.getArtcleList()
        for item in artcleList:
            print item
            dest = artcleList[item]
            flag = self.validate_url(item)
            if flag:
                context = self.getArtcleContent(item)
                if len(context) > 1:
                    self.AbstractFileProcessor.writeToFile(context, dest)
                else:
                    # print "该文章为空,已跳过！"
                    continue
            else:
                continue

    def test(self):
        t = self.AbstractHTMLProcessor
        tt = self.start()
