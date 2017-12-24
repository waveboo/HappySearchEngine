# -*- coding:utf-8 -*-
import jieba
from QuestionGet import QSBK

class QuestionCut(object):
    def __init__(self):
        self.spider = QSBK()
        self.spider.catch()
        jieba.load_userdict('Tags.txt')

    def cut(self):
        f = open('QuestionCut.txt', 'w');
        with open('Questions.txt', 'r') as file_to_read:
            while True:
                lines = file_to_read.readline()  # 整行读取数据
                if not lines:
                    break
                    pass
                tmp = ' '.join(jieba.cut(lines))
                f.write(tmp + ' ')
                pass
            pass
        f.close()

if __name__ == '__main__':
    Cut = QuestionCut()
    Cut.cut()