# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

class dealCode(object):
    def __init__(self):
        self.end = [',','.','!','?','\'','\"','，','。','？','！','.',' ','\n']

    def is_chinese(self, uchar):
        """判断一个unicode是否是汉字"""
        if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
            return True
        else:
            return False

    def is_number(self, uchar):
        """判断一个unicode是否是数字"""
        if uchar >= u'\u0030' and uchar <= u'\u0039':
            return True
        else:
            return False

    def is_alphabet(self, uchar):
        """判断一个unicode是否是英文字母"""
        if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
            return True
        else:
            return False

    def is_end(self, uchar):
        """判断是否非汉字，数字和英文字符"""
        if(self.is_chinese(uchar)):
            return True
        else:
            for ch in self.end:
                if(ch == uchar):
                    return True
        return False

if __name__ == '__main__':
    a =dealCode()
    if(a.is_end('#')):
        print 1
    if (a.is_end(',')):
        print 2