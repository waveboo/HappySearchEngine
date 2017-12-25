# -*- coding:utf-8 -*-

import config

import sys
reload(sys)
sys.setdefaultencoding('utf8')

cfg = config.project_config
types = cfg['types']

class AdvancedCope(object):
    def __init__(self):
        self.sentence = ''

    def set_sentence(self, sentence):
        self.sentence = sentence

    def addIndex(self,type):
        self.sentence = self.sentence + " index of " + types[type]

    def moveADS(self):
        self.sentence = self.sentence + " -广告 -推广 -评价 -广告推广"

    def Baidurepalce(self):
        BaiduTable = {
            '+':'%2B', '/':'%2F', '@':'%40', '#':'%23', '$':'%24',
            '^':'%5E', '&':'%26', '=':'%3D', '\'':'%27', '[':'%5B', ']':'%5D',
            '{':'%7B', '}':'%7D', ':':'%3A', ';':'%3B', '\\':'%5C', '|':'%7C',
            ',':'%2C', '?':'%3F', '`':'%60', ' ':'%20'
        }
        keys = BaiduTable.keys()
        self.sentence = self.sentence.replace("%","%25")
        for i in range(0, len(BaiduTable)):
            if(BaiduTable.get(keys[i])):
                self.sentence = self.sentence.replace(keys[i],BaiduTable[keys[i]])

        return self.sentence

if __name__ == '__main__':
    print AdvancedCope(u'你的眼睛 +-，。,').Baidurepalce()