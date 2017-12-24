# -*- coding:utf-8 -*-
"""
    用来把文字变成向量，方便计算机处理
"""
import fasttext
import numpy as np
import jieba

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

___all__ = ['Model']


MODEL_FILE_URL = '/home/wavelee/PycharmProjects/WordClassify/train.bin'


class Model(object):
    def __init__(self):
        print 'start to load model'
        self.model = fasttext.load_model(MODEL_FILE_URL)
        print 'load model completed'

    def word_vector(self, word):
        return self.model[word]

    def load_dict(self):
        jieba.load_userdict('DataSource/Tags.txt')

    """
    input sentence:  must be list of word
    """
    def sentence_vector(self, sentence):
        a = list(jieba.cut(sentence))
        words_vec = np.array(map(lambda x: self.model[x], a))
        num = words_vec.shape[0]
        sentence_vec = np.sum(words_vec, axis=0) / num
        return sentence_vec







