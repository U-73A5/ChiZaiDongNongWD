'''
微博_东北农业大学超话https://m.weibo.cn/p/index?containerid=10080822c440b7dcfa3683e7a50bcdbfe7159a
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

        def __setitem__(self, key: Union[int, str], item: Any) -> None:
            return super().__setitem__(key, item)

        def __delitem__(self, key: Union[int, str]) -> None:
            return super().__delitem__(key)

        def __iter__(self) -> Iterator[Union[int, str]]:
            return super().__iter__()

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

    class CrawlStatus(StatusContent):
        _urlComment = x['_urlComment']
        _urlFeed = x['_urlFeed']
        _urlNew = x['_urlNew']
        _urlHot = x['_urlHot']
        _urlEssence = x['_urlEssence']
        _userAgent = userAgentList

        def __init__(self) -> None:
            self._id = 0
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
        def urlFeed(self) -> str:
            return CrawlStatus._urlFeed

        @urlFeed.setter
        def urlFeed(self, url: str) -> bool:
            try:
                CrawlStatus._urlFeed = url
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
        def urlEssence(self) -> str:
            return CrawlStatus._urlEssence

        @urlEssence.setter
        def urlEssence(self, url: str) -> bool:
            try:
                CrawlStatus._urlEssence = url
            except:
                return False
            else:
                return True

        @property
        def userAgent(self) -> list:
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
        def id(self) -> str:
            return self._id

        @id.setter
        def id(self, value: str) -> bool:
            try:
                self._id = value
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

        def loadStatus(self, file):
            return super().loadStatus(file)

        def saveStatus(self, file):
            return super().saveStatus(file)

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

        def _getJsonData(self, url) -> dict:
            self.errorReturn = False
            headers = {
                'User-Agent': random.choice(self.userAgent),
            }
            params = {
                'id': self.id,
                'mid': self.id,
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
            return (jsonData['data'] if (
                isinstance(jsonData, dict) and ('data' in jsonData.keys())
                ) else {'cards': {}})

        def _crawlMain(self, url: str, crawlTimes: int, sleepTime: Optional[float]) -> int:
            dataDir = {}
            for _i in range(crawlTimes):
                console = Console()
                with console.status(f'[bold yellow]Crawling Times:{_i}...', spinner='line', spinner_style='red') as status:
                    sleepT: float = random.random() * 3 if sleepTime == None else sleepTime
                    dataDir = self._getJsonData(url)
                    if self.errorReturn == True:
                        continue
                    elif len(dataDir)==0:
                        break
                    dataNum = 0
                    for dt in dataDir['cards']:
                        if dt['card_type'] != '9':
                            continue
                        #TODO card_type == 11
                        dataNum += 1
                        self.data[dt['mblog']['id']] = dt['mblog']
                    time.sleep(sleepT)
                rich.print(
                    f'[yellow]{_i}: Crawl finish. Sleep {sleepT} second. Crawl {dataNum} dates.[/yellow]')
            return dataNum

        @terminalInfo
        def crawlFeed(self, crawlTimes=1, sleepTime=None) -> int:
            self.errorCount = 0
            if self.url != self.urlFeed:
                self.url = self.urlFeed
            result = self._crawlMain(self.url, crawlTimes, sleepTime)
            return result

        @terminalInfo
        def crawlNew(self, crawlTimes=1, sleepTime=None) -> int:
            self.errorCount = 0
            if self.url != self.urlNew:
                self.url = self.urlNew
            result = self._crawlMain(self.url, crawlTimes, sleepTime)
            return result

        @terminalInfo
        def crawlHot(self, crawlTimes=1, sleepTime=None) -> int:
            self.errorCount = 0
            if self.url != self.urlHot:
                self.url = self.urlHot
            result = self._crawlMain(self.url, crawlTimes, sleepTime)
            return result

        @terminalInfo
        def crawlEssence(self, crawlTimes=1, sleepTime=None) -> int:
            self.errorCount = 0
            if self.url != self.urlEssence:
                self.url = self.urlEssence
            result = self._crawlMain(self.url, crawlTimes, sleepTime)
            return result

        @terminalInfo
        def crawlComment(self, sleepTime=None) -> None:
            self.errorCount = 0
            tempList = []
            for dt in self.data.values():
                if dt['comments_count'] == 0:
                    continue
                dt_id = dt['id']
                rich.print(
                    f'[yellow]爬取 id 为 {dt_id} 评论的回复[/yellow]')
                tempWBDC = Crawl()
                tempWBDC.id = dt['id']
                try:
                    tempWBDC._getJsonData(self.urlComment)
                except:
                    print('Comment | _getJsonData')
                    raise
                time.sleep(random.random())
                tempList.append((dt['id'], tempWBDC.data.values(), ))
            for commentD in tempList:
                self.data[commentD[0]]['commentList'] = list(commentD[1])

    return Crawl
