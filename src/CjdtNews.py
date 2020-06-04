# coding=utf-8
from AbstractNews import AbstractNews


class CjdtNews(AbstractNews):
    def __init__(self, config, HTMLProcessor, fileProcessor):
        super(CjdtNews, self).__init__(config, HTMLProcessor, fileProcessor)

    def test(self):
        # t = self.AbstractHTMLProcessor
        tt = self.getTitleList()
        print tt
