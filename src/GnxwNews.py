# coding=utf-8
import traceback

from AbstractNews import AbstractNews


class GnxwNews(AbstractNews):
    def __init__(self, config, HTMLProcessor, fileProcessor):
        super(GnxwNews, self).__init__(config, HTMLProcessor, fileProcessor)

    def start(self):
        print "开始执行start"
        artcleList = self.getArtcleList()
        for item in artcleList:
            dest = artcleList[item]
            flag = self.validate_url(item)
            if flag:
                try:
                    context = self.getArtcleContent(item)
                    if len(context) > 1:
                        self.AbstractFileProcessor.writeToFile(context, dest)
                    else:
                        print "该文章为空,已跳过！"
                        continue
                except Exception as e:
                    print('Error: ', e)
                    traceback.print_exc()

            else:
                continue

    def test(self):
        t = self.AbstractHTMLProcessor
        tt = self.start()
