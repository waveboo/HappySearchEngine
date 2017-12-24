# -*- coding:utf-8 -*-

import requests
from DealEnglish import dealCode

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')


wordmodel_server_url = 'http://localhost:8888/'


def get_vec(sentence):
    """
    得到一个句子的向量
    """
    params = dict(sentence=sentence)
    r = requests.post(wordmodel_server_url, params)
    return r.json()['vec']

def get_slots(sentence):
    code = dealCode()
    dict = []
    word = []
    for i in range(0, len(sentence)):
        if (i < (len(sentence) - 1) and (not code.is_end(sentence[i]))):
            word.append(sentence[i])
        elif (i == (len(sentence) - 1) and (not code.is_end(sentence[i]))):
            word.append(sentence[i])
        elif (code.is_end(sentence[i]) and len(word)):
            words = ''.join(word)
            dict.append(words)
            word = []
        else:
            pass
    return dict