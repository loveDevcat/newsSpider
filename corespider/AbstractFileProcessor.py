# coding=utf-8
import time


class AbstractFileProcessor(object):
    def __init__(self, parentDic):
        self.fileName = None
        self.parentDic = parentDic

    def writeToFile(self, context, dest, fileName):
        pass

    def fileToZip(self):
        pass

    def initFileDic(self):
        pass

    def compressFile(self, zipFileName, month, day, dirname, dest):
        pass
