# encoding: utf-8
from GetBaiduPage import GetBaidu
from SlotsCope import SlotsCope
from AdvancedCope import AdvancedCope


import sys
reload(sys)
sys.setdefaultencoding('utf8')

class StartCope(object):
    def __init__(self,sentence):
        self.sentence = sentence
        self.slotscope = SlotsCope()
        self.advancedcope = AdvancedCope()

    def cope(self, type):
        self.slotscope.set_sentence(self.sentence)
        self.slotscope.slotsGet()
        self.slotscope.slotsReplace()
        self.sentence = self.slotscope.slotsCope()

        self.advancedcope.set_sentence(self.sentence)
        if(not(type == -1)):
            self.advancedcope.addIndex(type)
        self.advancedcope.moveADS()
        self.sentence = self.advancedcope.Baidurepalce()

        BaiduPy = GetBaidu('http://www.baidu.com/s',self.sentence)
        for i in range(1,4):
            BaiduPy.getPageInfo(i)
        return BaiduPy.getAnswers()