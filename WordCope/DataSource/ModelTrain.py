# -*- coding:utf-8 -*-

import fasttext
from QuestionCut import QuestionCut

class train(object):
    def __init__(self):
        pass
        # self.cut = QuestionCut()
        # self.cut.cut()

    def train(self):
        model = fasttext.cbow("QuestionCut.txt","../train",lr=0.1, dim=300)

if __name__ == '__main__':
    model = train()
    model.train()