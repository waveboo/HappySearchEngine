# -*- coding:utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
from tools import get_slots

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class QSBK(object):
    def __init__(self):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.dict = []

    def getPage(self, urlhead, pageIndex):
        try:
            url = urlhead + str(pageIndex)
            # print url
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            pageCode = response.read().decode('utf-8')
            return pageCode

        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"爬取错误！%s", e.reason
                return None

    def getQuestionItems(self, pageIndex):
        pageCode = self.getPage('http://ask.csdn.net/p',pageIndex)
        if not pageCode:
            print "未爬取到页面...."
            return None

        soup = BeautifulSoup(pageCode, 'html.parser', from_encoding='utf-8')
        titles = soup.find_all('div', class_ = 'questions_detail_con')

        if pageIndex == 1:
            f = open('Questions.txt', 'w');
        else:
            f = open('Questions.txt', 'a');

        for title in titles:
            tmp = title.dl.dt.a.get_text()
            self.dict = get_slots(tmp)
            f.write(tmp + '\n')
        f.close()

    def getTagItems(self, pageIndex):
        pageCode = self.getPage('http://ask.csdn.net/tags?page=',pageIndex)
        if not pageCode:
            print "未爬取到页面...."
            return None

        soup = BeautifulSoup(pageCode, 'html.parser', from_encoding='utf-8')
        tags = soup.find_all('div', class_ = 'tags_list')
        tags = tags[0].find_all('a')

        if pageIndex == 1:
            f = open('Tags.txt', 'w');
        else:
            f = open('Tags.txt', 'a');

        for tag in tags:
            t = tag.get_text().replace(tag.em.get_text(),'')
            t = t.strip().replace('\n','')
            f.write(t + '\n')

        f.close()

    def writeUserDict(self):
        f = open('Tags.txt', 'a');
        for word in self.dict:
            f.write(word + '\n')
        f.close()

    def catch(self):
        for page in range(1,80):
            print 'q' + str(page)
            self.getQuestionItems(page)
        for page in range(1,300):
            print 't' + str(page)
            self.getTagItems(page)
        self.writeUserDict()


if __name__ == '__main__':
    spider = QSBK()
    spider.catch()