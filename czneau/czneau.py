'''
CCN
XCD
WBDC
'''

from .refer import *
from .crawlF import (F1, F2)

ccn = {
    '_urlComment': 'http://czneau.com/api/comments',
    '_urlNew': 'http://czneau.com/api/posts',
    '_urlHot': 'http://czneau.com/api/hot',
    '_referer': 'http://czneau.com/',
}
CCN = F1.crawl(ccn)


class CCNAnalyseContent(AnalyseContent):
    def AnalyseContentIter(self, data: Union[str, CCN]):
        if type(data) == str:
            file, data = data, CCN()
            data.loadData(file)
        return (data[x]['content'] for x in data)


xcd = {
    '_urlComment': 'http://xcard.czneau.com/api/comments',
    '_urlNew': 'http://xcard.czneau.com/api/posts',
    '_urlHot': 'http://xcard.czneau.com/api/hot',
    '_referer': 'http://xcard.czneau.com/',
}
XCD = F1.crawl(xcd)


class XCDAnalyseContent(AnalyseContent):
    def AnalyseContentIter(self, data: Union[str, CCN]):
        if type(data) == str:
            file, data = data, CCN()
            data.loadData(file)
        return (data[x]['content'] for x in data)


wb_dongnong_chaohua = {
    '_urlComment': 'https://m.weibo.cn/comments/hotflow',
    '_urlFeed': 'https://m.weibo.cn/api/container/getIndex?containerid=10080822c440b7dcfa3683e7a50bcdbfe7159a_-_feed',
    '_urlNew': 'https://m.weibo.cn/api/container/getIndex?containerid=10080822c440b7dcfa3683e7a50bcdbfe7159a_-_sort_time',
    '_urlHot': 'https://m.weibo.cn/api/container/getIndex?containerid=10080822c440b7dcfa3683e7a50bcdbfe7159a_-_recommend',
    '_urlEssence': 'https://m.weibo.cn/api/container/getIndex?containerid=10080822c440b7dcfa3683e7a50bcdbfe7159a_-_soul',
}
WBDC = F2.crawl(wb_dongnong_chaohua)


class WBDCAnalyseContent(AnalyseContent):
    def AnalyseContentIter(self, data: Union[str, CCN]):
        if type(data) == str:
            file, data = data, WBDC()
            data.loadData(file)
        pass
        # TODO return
