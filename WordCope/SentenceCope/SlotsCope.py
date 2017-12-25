# -*- coding:utf-8 -*-

import jieba
from jieba import analyse
from tools import get_slots
from TrainData import DB

import sys
reload(sys)
sys.setdefaultencoding('utf8')

Path = '/home/wavelee/PycharmProjects/WordClassify/DataSource/'

class SlotsCope(object):
    def __init__(self):
        self.sentence = ''
        self.db = DB()
        self.words = []

    def set_sentence(self, sentence):
        self.sentence = sentence

    def slotsGet(self):
        f = open(Path + 'Tags.txt', 'a');
        slots = get_slots(self.sentence)
        for slot in slots:
            self.words.append(slot)
        for word in self.words:
            f.write(word + '\n')
        f.close()
        jieba.load_userdict(Path + '/Tags.txt')

        tfidy = analyse.extract_tags

        keywords = tfidy(self.sentence)
        for word in keywords:
            self.words.append(word)
        self.words = list(set(self.words))
        return self.words

    def slotsReplace(self):
        slots = self.words
        for slot in slots:
            if(self.db.findabb(slot)):
                whl = self.db.findabb(slot)
                tmp = "（" + slot + "|" + "“" + whl + "”" +"）"
                self.sentence = self.sentence.replace(slot, tmp)
        return self.sentence

    def slotsCope(self):
        slots = self.words
        for slot in slots:
            # 保证关键词不被过度切分
            tmp = "“" + slot + "”"
            self.sentence = self.sentence.replace(slot,tmp)
        return self.sentence

if __name__ == '__main__':
    t = SlotsCope(u"ABC使用")
    t.slotsGet()
    t.slotsReplace()
    t = t.slotsCope()

    print t