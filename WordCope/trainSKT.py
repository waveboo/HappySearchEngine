# -*- coding:utf-8 -*-

import requests
from sklearn import tree
import numpy as np
import pickle
from tools import get_vec
from tools import dict_update
from tools import get_slots
from TrainData import DB
import config

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

cfg = config.project_config
types = cfg['types']

db = DB()

def get_label(type_id):
    return types[type_id]

def get_train_data():
    train_data = []
    train_label = []
    for i in range(0,len(types)):
        tmp = db.get_sentence(types[i]);
        for title in tmp:
            train_data.append(title)
            train_label.append(i)
    return train_data, train_label

train_data, train_label = get_train_data()

f = open('DataSource/Tags.txt', 'a');
words = []
for data in train_data:
    slots = get_slots(data)
    for slot in slots:
        words.append(slot)
for word in words:
    f.write(word + '\n')
f.close()

dict_update()

for record, label in zip(train_data, train_label):
    print record, label


train_data = map(get_vec, train_data)


clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_data, train_label)


for t, l in zip(train_data, train_label):
    t = np.asarray(t).reshape(1, -1)
    print clf.predict(t) == l

# save trained model to file
with open('tmpmodel/model.plk', 'w') as f:
    pickle.dump(clf, f)


if __name__ == '__main__':
    pass






