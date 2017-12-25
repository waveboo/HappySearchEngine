# encoding: utf8

import urllib2
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding('utf8')

#百度爬虫类
class GetBaidu(object):
    def __init__(self,baseUrl,wd):
        self.baseURL = baseUrl
        self.wd = '?wd='+str(wd)
        self.info = '&tn=baiduhome_pg&ie=utf-8'
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        # 初始化headers
        self.headers = {'User-Agent': self.user_agent}
        # 存放段子的变量，每一个元素是每一页的段子们
        self.Answers = list()

    def getPage(self, pageIndex):
        try:
            url = self.baseURL + self.wd + '&pn=' + str(pageIndex - 1) + '0&op' + self.wd + self.info
            # proxy_handler = urllib2.ProxyHandler({'http':'182.42.37.46:808'})
            # opener = urllib2.build_opener(proxy_handler)
            # urllib2.install_opener(opener)
            # 构建请求的request
            print url
            request = urllib2.Request(url, headers=self.headers)
            # 利用urlopen获取页面代码
            response = urllib2.urlopen(request)
            # 将页面转化为UTF-8编码
            pageCode = response.read().decode('utf-8')
            return pageCode

        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接失败,错误原因", e.reason
                return None

    def getPageInfo(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败...."
            return None
        soup = BeautifulSoup(pageCode,'html.parser',from_encoding='utf-8')
        tags_1 = soup.find_all('div',class_="result")
        tags_2 = soup.find_all('div',class_="result-op")
        #对于非百度类的问题
        for tag in tags_1:
            tempEle = dict()
            tempEle['title'] = tag.h3.a.get_text()
            abs = tag.find_all('div',class_="c-abstract")
            if abs:
                tempEle['abstract'] = abs[0].get_text()
            else:
                tempEle['abstract'] = ''
            link = tag.find_all('div',class_="f13")
            if link and link[0].a:
                tempEle['link'] = link[0].a['href']
            else:
                tempEle['link'] = tag.h3.a['href']
            self.Answers.append(tempEle)
        #对于百度类的问题
        for tag in tags_2:
            if tag.h3:
                print tag.h3.a.get_text() + '\n'

    def getAnswers(self):
        return self.Answers

