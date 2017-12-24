# -*- coding:utf-8 -*-

import config
from pymongo import MongoClient

cfg = config.project_config

_client = MongoClient(host=cfg['mongo']['host'], port=cfg['mongo']['port'])
_db = _client[cfg['mongo']['db']]

class DB(object):
    def __init__(self):
        self.db = _db
        self.types = cfg['types']

    def save(self, table, sentence):
        query = {'_sentence': sentence}
        result = self.db[table].insert_one(query)
        return result.inserted_id

    def delete(self, table, sentence):
        pass

    def update(self, table, sentence):
        pass

    def save_exception(self, text, type_):
        result = self.db['exception'].insert_one(dict(text=text, type=type_))
        return result.inserted_id

    def get_sentence(self, type):
        titles = list()
        for i in self.db[type].find():
            titles.append(i['_sentence'])
        return titles


if __name__ == '__main__':
    db = DB()
    db.get_sentence('ai')