'''
东农饭团http://czneau.com/
Xcard猹卡http://xcard.czneau.com/
'''

from ..refer import *


def crawl(x: dict) -> Any:
    class CrawlData(UserDict):
        def __init__(self) -> None:
            super().__init__()

        def __len__(self) -> int:
            return super().__len__()

        def __getitem__(self, key: Union[int, str]) -> Any:
            return super().__getitem__(key)

        def __setitem__(self, key: Union[int, str, tuple], item: Any) -> None:
            return super().__setitem__(key, item)

        def __delitem__(self, key: Union[int, str]) -> None:
            return super().__delitem__(key)

        def __iter__(self):
            return super().__iter__()

        def __repr__(self):
            return f'{type(self).__name__}({repr(self.data)})'

        @terminalInfo
        def loadData(self, file: str) -> bool:
            r'''加载json文件'''
            try:
                console = Console()
                with console.status('[bold red]Loading...') as status:
                    with open(file, 'r', encoding='utf-8') as f:
                        self.data = json.load(f)
            except:
                return False
            else:
                return True

        @terminalInfo
        def saveData(self, file: str) -> bool:
            r'''保存json文件'''
            try:
                console = Console()
                with console.status(f'[bold red]Saveing...', spinner_style='blue') as status:
                    with open(file, 'w', encoding='utf-8') as f:
                        json.dump(self.data, f)
            except:
                return False
            else:
                return True

        def barrage(self, sleepTime: int = 3, comment: bool = True) -> None:
            for value in self.data.values():
                outputStr = f"[yellow bold]{value['nickname']}[/yellow bold]\n[cyan]{value['content']}[/cyan]"
                if comment and value['commentCount'] != 0:
                    try:
                        for vv in value['commentList']:
                            outputStr += f"\n[yellow bold]{vv['nickname']}[/yellow bold]\n[#0066CC]{vv['content']}[/#0066CC]\n[#FF6666]LIKE: {vv['likeCount']}[/#FF6666]   [blue]TIME: {time.ctime(vv['date'])}[/blue]"
                    except KeyError:
                        outputStr += f"\n[#0066CC]{value['commentCount']} comments had not been download.[/#0066CC]"
                rich.print(Panel(outputStr,
                                 border_style='blue',
                                 title=time.ctime(value['date']), title_align='right',
                                 subtitle=f'''LIKE: {value['likeCount']}  COMMENT: {value['commentCount']}''', subtitle_align='right'
                                 ))
                time.sleep(sleepTime)

        @staticmethod
        def getTime(x: dict) -> str:
            r'''返回评论发表时间'''
            return time.ctime(x['date'])

        @staticmethod
        def getDay(x: dict) -> int:
            r'''返回评论发表当天是星期几'''
            day = {'Mon': 1, 'Tue': 2, 'Wed': 3,
                   'Thu': 4, 'Fri': 5, 'Sat': 6, 'Sun': 7}
            return int(day[time.ctime(x['date']).split(' ')[0]])

        @staticmethod
        def getMonth(x: dict) -> int:
            mouth = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                     'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
            return int(mouth[time.ctime(x['date']).split(' ')[1]])

        @staticmethod
        def getDate(x: dict) -> int:
            r'''返回评论发表当天几号'''
            return int(time.ctime(x['date']).split(' ')[2])

        @staticmethod
        def getHour(x: dict) -> int:
            return int(time.ctime(x['date']).split(' ')[-2].split(':')[0])

        @staticmethod
        def getMinute(x: dict) -> int:
            return int(time.ctime(x['date']).split(' ')[-2].split(':')[1])

        @staticmethod
        def getSecond(x: dict) -> int:
            return int(time.ctime(x['date']).split(' ')[-2].split(':')[-1])

        @staticmethod
        def getYear(x: dict) -> int:
            return int(time.ctime(x['date']).split(' ')[-1])

    class CrawlStatus(StatusContent):
        _urlComment = x['_urlComment']
        _urlNew = x['_urlNew']
        _urlHot = x['_urlHot']
        _referer = x['_referer']
        _userAgent = userAgentList

        def __init__(self) -> None:
            self._pageSize = 0  # this must less than 30
            self._fromId = ''
            self._postId = ''
            self._url = ''
            self._proxies: Optional[dict] = None

        @property
        def urlComment(self) -> str:
            return CrawlStatus._urlComment

        @urlComment.setter
        def urlComment(self, url: str) -> bool:
            try:
                CrawlStatus._urlComment = url
            except:
                return False
            else:
                return True

        @property
        def urlNew(self) -> str:
            return CrawlStatus._urlNew

        @urlNew.setter
        def urlNew(self, url: str) -> bool:
            try:
                CrawlStatus._urlNew = url
            except:
                return False
            else:
                return True

        @property
        def urlHot(self) -> str:
            return CrawlStatus._urlHot

        @urlHot.setter
        def urlHot(self, url: str) -> bool:
            try:
                CrawlStatus._urlHot = url
            except:
                return False
            else:
                return True

        @property
        def referer(self) -> str:
            r'''防盗链'''
            return CrawlStatus._referer

        @referer.setter
        def referer(self, value: str) -> bool:
            try:
                CrawlStatus._referer = value
            except:
                return False
            else:
                return True

        @property
        def userAgent(self) -> list:
            r'''User-Agent of headers'''
            return CrawlStatus._userAgent

        @userAgent.setter
        def userAgent(self, agents) -> bool:
            try:
                CrawlStatus._userAgent = [agents] if type(
                    agents) == str else agents
            except:
                return False
            else:
                return True

        @property
        def pageSize(self) -> int:
            r'''大小介于[1,30), 默认29'''
            return self._pageSize

        @pageSize.setter
        def pageSize(self, value) -> bool:
            if type(value) == str:
                value = int(value)
            if value <= 0 or value >= 30:
                rich.print('The size of page must in interval [1, 30)')
                return False
            try:
                self._pageSize = value
            except:
                return False
            else:
                return True

        @property
        def fromID(self) -> str:
            return self._fromId

        @fromID.setter
        def fromID(self, value) -> bool:
            try:
                self._fromId = value if type(value) == str else f'{value}'
            except:
                return False
            else:
                return True

        @property
        def postID(self) -> str:
            return self._postId

        @postID.setter
        def postID(self, value) -> bool:
            try:
                self._postId = value if type(value) == str else f'{value}'
            except:
                return False
            else:
                return True

        @property
        def url(self) -> str:
            return self._url

        @url.setter
        def url(self, value: str) -> bool:
            try:
                self._url = value
            except:
                return False
            else:
                return True

        @property
        def proxies(self):
            return self._proxies

        @proxies.setter
        def proxies(self, value: dict) -> bool:
            try:
                self._proxies = value
            except:
                return False
            else:
                return True

        @terminalInfo
        def loadStatus(self, file: str) -> bool:
            r'''加载下载信息，以继续上次退出时下载任务'''
            try:
                console = Console()
                with console.status('[bold red]Loading...') as status:
                    with open(file, 'r', encoding='utf-8') as f:
                        downloadStatus = json.load(f)
                self._pageSize = downloadStatus['pageSize']
                self._fromId = downloadStatus['fromId']
                self._postId = downloadStatus['postId']
                self._url = downloadStatus['url']
                self._proxies = downloadStatus['proxies']
            except:
                return False
            else:
                return True

        @terminalInfo
        def saveStatus(self, file: str) -> bool:
            r'''保存当前下载信息'''
            try:
                downloadStatus = {
                    'pageSize': self.pageSize,
                    'fromId': self.fromID,
                    'postId': self.postID,
                    'url': self.url,
                    'proxies': self.proxies
                }
                console = Console()
                with console.status(f'[bold red]Saveing...', spinner_style='blue') as status:
                    with open(file, 'w', encoding='utf-8') as f:
                        json.dump(downloadStatus, f)
            except:
                return False
            else:
                return True

    class Crawl(CrawlStatus, CrawlData):
        _raiseEE = True

        @property
        def raiseEE(self) -> bool:
            return Crawl._raiseEE

        @raiseEE.setter
        def raiseEE(self, value: bool) -> bool:
            try:
                Crawl._raiseEE = value
            except:
                return False
            else:
                return True

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
            try:
                self._errorMax = value
            except:
                return False
            else:
                return True

        @property
        def errorCount(self) -> int:
            return self._errorCount

        @errorCount.setter
        def errorCount(self, value: int) -> bool:
            try:
                self._errorCount = value
            except:
                return False
            else:
                return True

        @property
        def errorReturn(self) -> bool:
            return self._errorReturn

        @errorReturn.setter
        def errorReturn(self, value: bool) -> bool:
            try:
                self._errorReturn = value
            except:
                return False
            else:
                return True

        def _getJsonData(self, url) -> list:
            r'''获取json'''
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
            jsonData: dict = {'data': []}
            try:
                resp = requests.get(url=url, headers=headers,
                                    params=params, proxies=proxies)
                resp.close()
                if resp.status_code != 200:
                    rich.print(
                        f'\nResponse Status Code: [red]{resp.status_code}[/red]')
                    return []
                jsonData = resp.json()
            except requests.exceptions.ProxyError:
                rich.print(
                    f'\nAn [red bold]ProxyError[/red bold] Raised As Expected.\n网络不稳定或 [blue]ip[/blue] 被封了. 要等段时间或加代理。')
                if Crawl.raiseEE:
                    raise requests.exceptions.ProxyError
                if self.errorCount == self.errorMax:
                    raise RaiseCountError
                self.errorCount = self.errorCount + 1
                self.errorReturn = True
            except requests.exceptions.ChunkedEncodingError:
                rich.print(
                    f'\nAn [red bold]ChunkedEncodingError[/red bold] Raised As Expected.\n服务器错误关闭。')
                if Crawl.raiseEE:
                    raise requests.exceptions.ChunkedEncodingError
                if self.errorCount == self.errorMax:
                    raise RaiseCountError
                self.errorCount = self.errorCount + 1
                self.errorReturn = True
            return jsonData['data']

        def _crawlMain(self, url: str, crawlTimes: int, sleepTime: Optional[float]) -> int:
            r'''爬虫主循环'''
            dataList = []
            for _i in range(crawlTimes):
                console = Console()
                with console.status(f'[bold yellow]Crawling Times:{_i}...', spinner='line', spinner_style='red') as status:
                    sleepT: float = random.random() * 3 if sleepTime == None else sleepTime
                    dataList = self._getJsonData(url)
                    if self.errorReturn == True:
                        continue
                    elif len(dataList) == 0:
                        break
                    for dt in dataList:
                        self.data[dt['id']] = dt
                        self.fromID = dt['id']
                    time.sleep(sleepT)
                rich.print(
                    f'[yellow]{_i}: Crawl finish. Sleep {sleepT} second. Crawl {len(dataList)} datas.[/yellow]')
            return len(dataList)

        @terminalInfo
        def crawlNew(self, crawlTimes=1, sleepTime=None, level=0) -> int:
            r'''爬取最新评论'''
            self.errorCount = 0
            if self.url != self.urlNew:
                self.url = self.urlNew
                self.fromID = ''
            result = self._crawlMain(self.url, crawlTimes, sleepTime)
            return result

        @terminalInfo
        def crawlHot(self, crawlTimes=1, sleepTime=None, level=0) -> int:
            r'''爬取热评'''
            self.errorCount = 0
            if self.url != self.urlHot:
                self.url = self.urlHot
                self.fromID = ''
            result = self._crawlMain(self.url, crawlTimes, sleepTime)
            return result

        @terminalInfo
        def crawlComment(self, sleepTime=None) -> None:
            r'''爬取评论的回复'''
            self.errorCount = 0
            tempList = []
            for dt in self.data.values():
                if dt['commentCount'] == 0:
                    continue
                dt_id = dt['id']
                rich.print(f'[yellow]爬取 id 为 {dt_id} 评论的回复[/yellow]')
                tempCCN = Crawl()
                tempCCN.postID = dt['id']
                temp = 1
                while temp != 0:
                    temp = tempCCN._crawlMain(self.urlComment, 1, sleepTime)
                tempList.append((dt['id'], tempCCN.data.values(), ))
            for commentD in tempList:
                self.data[commentD[0]]['commentList'] = list(commentD[1])

    return Crawl
