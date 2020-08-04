# coding=utf-8
import os
import shutil
import sys
import zipfile

from AbstractFileProcessor import AbstractFileProcessor


class CommonFileProcessor(AbstractFileProcessor):
    def __init__(self, parentDic):
        super(CommonFileProcessor, self).__init__(parentDic)
        self.path = os.path.dirname(os.getcwd()) + os.sep + 'output' + os.sep + parentDic
        if not os.path.exists(self.path):
            os.makedirs(self.path)
            print "该文件夹已经创建" + os.getcwd()
            # sys.exit(u'请先创建父文件夹' % os.getcwd())

    def writeToFile(self, context, dest):
        fileParentDic = self.path + os.sep + dest
        is_exists = os.path.exists(fileParentDic)
        if not is_exists:
            os.makedirs(fileParentDic)
        fileName = fileParentDic + os.sep + context[0].strip() + '.txt'
        f = open(fileName, 'w')
        f.write(context[0].strip() + '\n')
        for k in range(1, len(context)):
            f.write(
                "<div><span style='font-size:16px;margin-top:15px;line-height:25px;text-indent:30px;display:block'> " +
                context[k].get_text() + "</span></div>")
            f.write("<div>&nbsp;</div>")
        f.close()
        print '《' + context[0].strip() + '》' + '保存成功！'

    def fileToZip(self, context, dest):
        dest = str(dest)
        self.path = os.path.dirname(os.getcwd()) + os.sep + 'output' + os.sep + 'tempnewspaper'
        fileParentDic = self.path
        is_exists = os.path.exists(fileParentDic)
        if not is_exists:
            os.makedirs(fileParentDic)
        fileName = fileParentDic + os.sep + dest + '.pdf'
        f = open(fileName, 'wb')
        f.write(context)
        f.close()
        print '《' + '新闻' + dest + '》' + '保存成功！'

    def initFileDic(self, dest='tempnewspaper'):
        path = self.path
        files = os.listdir(path)
        for file in files:
            os.remove(path + os.sep + file)
            print ('删除文件:%s成功' % file)

    def compressFile(self, zipFileName, month, day, dirname='tempnewspaper', dest='output'):
        path = os.path.dirname(os.getcwd()) + os.sep + dest + os.sep + dirname
        destPath = os.path.dirname(os.getcwd()) + os.sep + dest
        print 'path is:' + path
        zipName = zipFileName + month + day + '.zip'
        if os.path.isfile(path):
            with zipfile.ZipFile(zipName, 'w') as z:
                z.write(dirname)
        else:
            with zipfile.ZipFile(zipName, 'w') as z:
                for root, dirs, files in os.walk(dirname):
                    print 'files is ' + files
                    for single_file in files:
                        if single_file != zipName and single_file != '.DS_Store':
                            z.write(single_file)
            shutil.move(zipName, destPath)
