# ChiZaiDongNongWD
用于爬取[东农饭团](http://czneau.com/)上的数据。

## 样例
```python
import czneau

dld = czneau.CCN()

dld.crawlHot() # 获取热评(默认29条，不包含回复)
dld.crawlHot(3) # 继续获取热评，总共有 29 + 29 * 3 条
dld.crawlComment() # 获取 dld 下评论的回复
dld.saveData('czneau.json') # 存储数据

dld.print() # 输出数据信息
```

## 部分数据说明
获取评论保持原json数据不变。

获取的回复添加在原json数据中。

```python
CCN().data = {
    {
        'id': int(), # 使用 id 判定是否为相同数据
        'content': str(), # 评论内容
        'likeCount': int(), # 点赞数
        'commentCount': int(), # 评论数
        'commentList': list(), # 仅在 commentCount 非 0 时有该关键字，非原 json数据
        ##...
    },
    ##...
}

# commentCount非 0 时有
CCN().data[0]['commentList'] = {
    {
        'id': int() # 该 id 不参与任何判断
        'content': str(), # 回复内容
        'likeCount': int(), # 回复点赞数
        ##...
    },
    ##...
}
```

## 接口说明
```python
## 爬取热评
def crawlHot(self,
    crawlTimes=1, # 爬取次数；(2022/4/3)默认'pageSize'='29'下，当其值约为3500时可以爬取所有数据(该值为估算，没有测试)。
    sleepTime=None # 每次爬取间隔,默认在[0, 1]秒之间
) -> int: ...

## 爬取最新评论
def crawlNew(self,
    crawlTimes=1,
    sleepTime=None # 每次爬取间隔,默认在[0, 1]秒之间
) -> int: ...

## 爬取评论回复 // 默认爬取时不爬取评论
def crawlComment(self,
    sleepTime=None # 每次爬取间隔,默认在[0, 1]秒之间
) -> None: ...

## 加载已有数据
def loadData(self,
    file: str # 数据存放地址
) -> bool: ...

## 保存数据
def saveData(self,
    file: str # 数据存放地址
) -> bool:

## 输出相关信息
def print(self,
    allInfo=False # 为 True 时输出数据集
) -> None:
```

## 安装
```bash
pip install czneau
```
