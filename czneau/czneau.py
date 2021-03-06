'''
提供CCN类
'''

from rich.console import Console
from collections import UserDict
from rich.panel import Panel
from typing import overload
from rich import traceback
from rich import print
import requests
import random
import time
import json

traceback.install()

##
userAgentList = [
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
"Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
"Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
"Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)"
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4094.1 Safari/537.36",
"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
"Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
"Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
"Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
"Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
"Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
"Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
]


class RaiseCountError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    def __str__(self) -> str:
        return 'RaiseCountError.'


class CrawlData(UserDict):
    def __init__(self) -> None:
        super().__init__()

    def __len__(self) -> int:
        return super().__len__()

    @overload
    def __getitem__(self, key: int) -> dict: ...
    @overload
    def __getitem__(self, key: str) -> dict: ...
    def __getitem__(self, key) -> dict:
        return super().__getitem__(key)
    
    @overload
    def __setitem__(self, key: int, item: dict) -> None: ...
    @overload
    def __setitem__(self, key: str, item: dict) -> None: ...
    @overload
    def __setitem__(self, key: tuple, item: dict) -> None: ...
    def __setitem__(self, key, item) -> None:
        return super().__setitem__(key, item)
    
    @overload
    def __delitem__(self, key: int): ...
    @overload
    def __delitem__(self, key: str): ...
    def __delitem__(self, key):
        return super().__delitem__(key)

    def __iter__(self):
        return super().__iter__()

    def __repr__(self):
        return f'{type(self).__name__}({repr(self.data)})'

    def loadData(self, file: str) -> bool:
        r'''加载json文件'''
        try:
            print('[purple]<load data start>[/purple]')
            console = Console()
            with console.status('[bold red]Start loading...') as status:
                with open(file, 'r', encoding='utf-8') as f:
                    self.data = json.load(f)
            print('[cyan]<load finish>[/cyan]')
        except: return False
        else: return True
    
    def saveData(self, file: str) -> bool:
        r'''保存json文件'''
        try:
            print('[purple]<save data start>[/purple]')
            console = Console()
            with console.status(f'[bold red]Start saveing...', spinner_style='blue') as status:
                with open(file, 'w', encoding='utf-8') as f:
                    json.dump(self.data, f)
            print('[cyan]<save finish>[/cyan]')
        except: return False
        else: return True

    def barrage(self, sleepTime: int=3, comment: bool=True) -> None:
        for value in self.data.values():
            outputStr = f"[yellow bold]{value['nickname']}[/yellow bold]\n[cyan]{value['content']}[/cyan]"
            if comment and value['commentCount'] != 0:
                try:
                    for vv in value['commentList']:
                        outputStr += f"\n[yellow bold]{vv['nickname']}[/yellow bold]\n[#0066CC]{vv['content']}[/#0066CC]\n[#FF6666]LIKE: {vv['likeCount']}[/#FF6666]   [blue]TIME: {time.ctime(vv['date'])}[/blue]"
                except KeyError:
                    outputStr += f"\n[#0066CC]{value['commentCount']} comments had not been download.[/#0066CC]"
            print(Panel(outputStr,
                border_style='blue',
                title=time.ctime(value['date']), title_align='right',
                subtitle=f'''LIKE: {value['likeCount']}  COMMENT: {value['commentCount']}''', subtitle_align='right'
            ))
            time.sleep(sleepTime)
    
    baseData = dict # 最基本的元素

    @staticmethod
    def getTime(x: baseData) -> str:
        r'''返回评论发表时间'''
        return time.ctime(x['date'])
    @staticmethod
    def getDay(x: baseData) -> int:
        r'''返回评论发表当天是星期几'''
        day = {'Mon': 1,'Tue': 2,'Wed': 3,'Thu': 4,'Fri': 5,'Sat': 6,'Sun': 7}
        return int(day[time.ctime(x['date']).split(' ')[0]])
    @staticmethod
    def getMonth(x: baseData) -> int:
        mouth = {'Jan': 1,'Feb': 2,'Mar': 3,'Apr': 4,'May': 5,'Jun': 6,'Jul': 7,'Aug': 8,'Sep': 9,'Oct': 10,'Nov': 11,'Dec': 12}
        return int(mouth[time.ctime(x['date']).split(' ')[1]])
    @staticmethod
    def getDate(x: baseData) -> int:
        r'''返回评论发表当天几号'''
        return int(time.ctime(x['date']).split(' ')[2])
    @staticmethod
    def getHour(x: baseData) -> int:
        return int(time.ctime(x['date']).split(' ')[-2].split(':')[0])
    @staticmethod
    def getMinute(x: baseData) -> int:
        return int(time.ctime(x['date']).split(' ')[-2].split(':')[1])
    @staticmethod
    def getSecond(x: baseData) -> int:
        return int(time.ctime(x['date']).split(' ')[-2].split(':')[-1])
    @staticmethod
    def getYear(x: baseData) -> int:
        return int(time.ctime(x['date']).split(' ')[-1])


##
class CrawlStatus:
    _urlComment = 'http://czneau.com/api/comments'
    _urlNew = 'http://czneau.com/api/posts'
    _urlHot = 'http://czneau.com/api/hot'
    _referer = 'http://czneau.com/'
    _userAgent = userAgentList

    def __init__(self) -> None:
        self._pageSize = 0 # this must less than 30
        self._fromId = ''
        self._postId = ''
        self._url = ''
        self._proxies = None
    
    @property
    def urlComment(self) -> str:
        return CrawlStatus._urlComment
    @urlComment.setter
    def urlComment(self, url: str) -> bool:
        try: CrawlStatus._urlComment = url
        except: return False
        else: return True
    @property
    def urlNew(self) -> str:
        return CrawlStatus._urlNew
    @urlNew.setter
    def urlNew(self, url: str) -> bool:
        try: CrawlStatus._urlNew = url
        except: return False
        else: return True
    @property
    def urlHot(self) -> str:
        return CrawlStatus._urlHot
    @urlHot.setter
    def urlHot(self, url: str) -> bool:
        try: CrawlStatus._urlHot = url
        except: return False
        else: return True
    @property
    def referer(self) -> str:
        r'''防盗链'''
        return CrawlStatus._referer
    @referer.setter
    def referer(self, value: str) -> bool:
        try: CrawlStatus._referer = value
        except: return False
        else: return True
    @property
    def userAgent(self) -> list:
        r'''User-Agent of headers'''
        return CrawlStatus._userAgent
    @userAgent.setter
    def userAgent(self, agents) -> bool:
        try: CrawlStatus._userAgent = [agents] if type(agents) == str else agents
        except: return False
        else: return True

    @property
    def pageSize(self) -> str:
        r'''大小介于[1,30), 默认29'''
        return self._pageSize
    @pageSize.setter
    def pageSize(self, value) -> bool:
        if value <= 0 or value >=30:
            print('The size of page must in interval [1, 30)')
            return False
        try: self._pageSize = value if type(value) == str else f'{value}'
        except: return False
        else: return True
    @property
    def fromID(self) -> str:
        return self._fromId
    @fromID.setter
    def fromID(self, value) -> bool:
        try: self._fromId = value if type(value) == str else f'{value}'
        except: return False
        else: return True
    @property
    def postID(self) -> str:
        return self._postId
    @postID.setter
    def postID(self, value) -> bool:
        try: self._postId = value if type(value) == str else f'{value}'
        except: return False
        else: return True
    @property
    def url(self) -> str:
        return self._url
    @url.setter
    def url(self, value: str) -> bool:
        try: self._url = value
        except: return False
        else: return True
    @property
    def proxies(self):
        return self._proxies
    @proxies.setter
    def proxies(self, value: dict) -> bool:
        try: self._proxies = value
        except: return False
        else: return True
    
    def loadStatus(self, file: str) -> bool:
        r'''加载下载信息，以继续上次退出时下载任务'''
        try:
            print('[purple]<load download status start>[/purple]')
            console = Console()
            with console.status('[bold red]Start loading...') as status:
                with open(file, 'r', encoding='utf-8') as f:
                    downloadStatus = json.load(f)
            self._pageSize = downloadStatus['pageSize']
            self._fromId = downloadStatus['fromId']
            self._postId = downloadStatus['postId']
            self._url = downloadStatus['url']
            self._proxies = downloadStatus['proxies']
            print('[cyan]<load finish>[/cyan]')
        except: return False
        else: return True

    def saveStatus(self, file: str) -> bool:
        r'''保存当前下载信息'''
        try:
            print('[purple]<save download status start>[/purple]')
            downloadStatus = {
                'pageSize': self.pageSize,
                'fromId': self.fromID,
                'postId': self.postID,
                'url': self.url,
                'proxies': self.proxies
            }
            console = Console()
            with console.status(f'[bold red]Start saveing...', spinner_style='blue') as status:
                with open(file, 'w', encoding='utf-8') as f:
                    json.dump(downloadStatus, f)
            print('[cyan]<save finish>[/cyan]')
        except: return False
        else: return True


##
class CrawlCzNeau(CrawlStatus, CrawlData):
    _indentSize = 2
    _raiseEE = True

    @property
    def indentSize(self) -> int:
        return CrawlCzNeau._indentSize
    @indentSize.setter
    def indentSize(self, value: int) -> bool:
        try: CrawlCzNeau._indentSize = value
        except: return False
        else: return True

    @property
    def raiseEE(self) -> bool:
        return CrawlCzNeau._raiseEE
    @raiseEE.setter
    def raiseEE(self, value: bool) -> bool:
        try: CrawlCzNeau._raiseEE = value
        except: return False
        else: return True

    def __init__(self) -> None:
        self._errorMax = 3
        self._errorCount = 0
        self._errorReturn = False
        CrawlStatus.__init__(self)
        CrawlData.__init__(self)
    
    @property
    def errorMax(self) -> int:
        return self._errorMax
    @errorMax.setter
    def errorMax(self, value: int) -> bool:
        try: self._errorMax = value
        except: return False
        else: return True
    
    @property
    def errorCount(self) -> int:
        return self._errorCount
    @errorCount.setter
    def errorCount(self, value: int) -> bool:
        try: self._errorCount = value
        except: return False
        else: return True
    
    @property
    def errorReturn(self) -> bool:
        return self._errorReturn
    @errorReturn.setter
    def errorReturn(self, value: bool) -> bool:
        try: self._errorReturn = value
        except: return False
        else: return True
    
    def _getJsonData(self, url, level=0) -> list:
        r'''获取json'''
        levelIndentSize = ' ' * self._indentSize * level
        self.errorReturn = False
        headers = {
            'User-Agent': random.choice(self.userAgent),
            'Referer': self.referer,
        }
        params = {
            'pageSize': random.randint(15, 29) if self.pageSize == 0 else self.pageSize,
            'fromId': self.fromID,
            'postId': self.postID
        }
        proxies = self.proxies
        jsonData = {'data': []}
        try:
            resp = requests.get(url=url, headers=headers, params=params, proxies=proxies)
            resp.close()
            if resp.status_code != 200:
                print(f'\n{levelIndentSize}Response Status Code: [red]{resp.status_code}[/red]')
                return []
            jsonData = resp.json()
        except requests.exceptions.ProxyError:
            print(f'\n{levelIndentSize}An [red bold]ProxyError[/red bold] Raised As Expected.\n{levelIndentSize}网络不稳定或 [blue]ip[/blue] 被封了. 要等段时间或加代理。')
            if CrawlCzNeau.raiseEE: raise requests.exceptions.ProxyError
            if self.errorCount == self.errorMax: raise RaiseCountError
            self.errorCount = self.errorCount + 1
            self.errorReturn = True
        except requests.exceptions.ChunkedEncodingError:
            print(f'\n{levelIndentSize}An [red bold]ChunkedEncodingError[/red bold] Raised As Expected.\n{levelIndentSize}服务器错误关闭。')
            if CrawlCzNeau.raiseEE: raise requests.exceptions.ChunkedEncodingError
            if self.errorCount == self.errorMax: raise RaiseCountError
            self.errorCount = self.errorCount + 1
            self.errorReturn = True
        return jsonData['data']
    
    def _crawlMain(self, url: str, crawlTimes: int, sleepTime: int, level: int) -> int:
        r'''爬虫主循环'''
        levelIndentSize = ' ' * self._indentSize * level
        dataList = []
        for _i in range(crawlTimes):
            console = Console()
            with console.status(f'[bold yellow]Crawling Times:{_i}...', spinner='line', spinner_style='red') as status:
                sleepT = random.random() * 3 if sleepTime == None else sleepTime
                dataList = self._getJsonData(url, level+1)
                if self.errorReturn == True: continue
                elif len(dataList) == 0: break
                for dt in dataList:
                    self.data[dt['id']] = dt
                    self.fromID = dt['id']
                time.sleep(sleepT)
            print(f'{levelIndentSize}[yellow]{_i}: Crawl finish. Sleep {sleepT} second. Crawl {len(dataList)} dates.[/yellow]')
        return len(dataList)

    def crawlNew(self, crawlTimes=1, sleepTime=None, level=0) -> int:
        r'''爬取最新评论'''
        levelIndentSize = ' ' * self._indentSize * level
        print(f'{levelIndentSize}[purple]<function crwalNew() In>[/purple]')
        self.errorCount = 0
        if self.url != self.urlNew:
            self.url = self.urlNew
            self.fromID = ''
        result = self._crawlMain(self.url, crawlTimes, sleepTime, level+1)
        print(f'{levelIndentSize}[cyan]<function crwalNew() Out>[/cyan]')
        return result

    def crawlHot(self, crawlTimes=1, sleepTime=None, level=0) -> int:
        r'''爬取热评'''
        levelIndentSize = ' ' * self._indentSize * level
        print(f'{levelIndentSize}[purple]<function crwalHot() In>[/purple]')
        self.errorCount = 0
        if self.url != self.urlHot:
            self.url = self.urlHot
            self.fromID = ''
        result = self._crawlMain(self.url, crawlTimes, sleepTime, level+1)
        print(f'{levelIndentSize}[cyan]<function crwalHot() Out>[/cyan]')
        return result
    
    def crawlComment(self, sleepTime=None, level=0) -> None:
        r'''爬取评论的回复'''
        levelIndentSize = ' ' * self._indentSize * level
        print(f'{levelIndentSize}[purple]<function crwalComment() In>[/purple]')
        self.errorCount = 0
        tempList = []
        for dt in self.data.values():
            if dt['commentCount'] == 0: continue
            dt_id = dt['id']
            levelIndentSize = ' ' * self._indentSize * (level+1)
            print(f'{levelIndentSize}[yellow]爬取 id 为 {dt_id} 评论的回复[/yellow]')
            tempCCN = CrawlCzNeau()
            tempCCN.postID = dt['id']
            temp = 1
            while temp != 0:
                temp = tempCCN._crawlMain(self.urlComment, 1, sleepTime, level+2)
            tempList.append((dt['id'], tempCCN.data.values(), ))
        for commentD in tempList:
            self.data[commentD[0]]['commentList'] = list(commentD[1])
        levelIndentSize = ' ' * self._indentSize * level
        print(f'{levelIndentSize}[cyan]<function crwalComment() Out>[/cyan]')


## nicknames
CCN = CrawlCzNeau

getTime = CCN.getTime
getDay = CCN.getDay
getMonth = CCN.getMonth
getDate = CCN.getDate
getHour = CCN.getHour
getMinute = CCN.getMinute
getSecond = CCN.getSecond
getYear = CCN.getYear
