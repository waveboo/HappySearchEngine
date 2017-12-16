# encoding: utf-8
from GetBaiduPage import GetBaidu

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class StartCope(object):
    def __init__(self,sentence):
        self.sentence = sentence

    def copeSemtence(self):
        self.sentence = self.sentence.replace(" ","%20")
        self.sentence = self.sentence + '%20-广告%20-推广%20'

    def cope(self):
        self.copeSemtence()
        self.BaiduPy = GetBaidu('http://www.baidu.com/s',self.sentence)
        for i in range(1,4):
            self.BaiduPy.getPageInfo(1)
        return self.BaiduPy.getAnswers()