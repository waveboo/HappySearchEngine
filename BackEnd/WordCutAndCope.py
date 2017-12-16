# encoding: utf-8
import jieba

#词性标注和关键词分析
import jieba.posseg
import jieba.analyse

from CopeBaidu import StartCope

class WordCut(object):
    def __init__(self,sentence):
        self.word = sentence

    def sentence_cut(self):
        seg_list = jieba.cut_for_search(self.word)  # 搜索引擎模式
        print(", ".join(seg_list))

class InformationGet(object):
    def __init__(self,sentence):
        self.word = sentence

    def sentence_cope(self):
        self.Cope = StartCope(self.word)
        return self.Cope.cope()