# -*- coding:utf-8 -*-

import pickle
from tools import get_vec
from tools import dict_update
from tools import get_slots
import numpy as np
import config

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

cfg = config.project_config
types = cfg['types']

MODEL_FILE = 'tmpmodel/model.plk'


def load_model(filename):
    with open(filename, 'r') as f:
        model = pickle.load(f)
    return model

class Analyse(object):
    def __init__(self):
        self.model = load_model(MODEL_FILE)

    def comprehend(self, question):
        print '问题是{question}'.format(question=question)
        print '正在分析....'

        f = open('DataSource/Tags.txt', 'a');
        words = []
        slots = get_slots(question)
        for slot in slots:
            words.append(slot)
        for word in words:
            f.write(word + '\n')
        f.close()
        dict_update()

        vec = np.asarray(get_vec(question))
        type_ = self.model.predict(vec.reshape(1, -1))[0]
        print "类型是{0}".format(types[type_])
        return type_

if __name__ == '__main__':
    a = Analyse()
    a.comprehend(u'python3.6 与MYSQL的安装与连接')