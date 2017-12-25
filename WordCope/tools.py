# -*- coding:utf-8 -*-

import requests
from DealEnglish import dealCode
from TrainData import DB

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

def dict_update():
    r = requests.post(wordmodel_server_url + 'dict')

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

def saveABB():
    db = DB()
    f = open('DataSource/suoxie.txt', 'r')
    while True:
        lines = f.readline()  # 整行读取数据
        lines = unicode(lines)
        if(len(get_slots(lines))):
           Abb = get_slots(lines)[0]
        else:
            break
        for i in range(0, len(lines)):
            if(not dealCode().is_chinese(lines[i])):
                lines = lines.replace(lines[i]," ")
        lines = lines.strip()
        db.saveabb('ABB',Abb, lines)
    f.close()