# -*- coding:utf-8 -*-

import requests
import demjson
import config
from TrainData import DB

import sys
reload(sys)
sys.setdefaultencoding('utf8')

cfg = config.project_config
types = cfg['types']

class TypeGet(object):
    def __init__(self):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.s = requests.session()
        self.db = DB()

    def get(self, type):
        url = "http://blog.csdn.net/api/articles?type=more&category=" + type +"&shown_offset=0"
        print url
        for i in range(1,100):
            req = self.s.get(url, headers = self.headers)
            if req:
                articles = demjson.decode(req.text)['articles']
                for article in articles:
                    self.db.save(type, article['title'])
            else:
                print '请求结束'
                return

if __name__ == '__main__':
    spider = TypeGet()
    for type in types:
        if type == 'other':
           spider.get(type)


