import czneau

dld = czneau.CCN()

dld.indentSize = 4
dld.pageSize = 2

dld.crawlHot() # 获取热评
dld.crawlHot(2) # 继续获取热评
dld.crawlComment()
dld.saveData('czneau.json')

for key in dld: # 遍历所有内容打印键和值
    print(key, dld[key]['likeCount'])

dld.saveStatus('downloadStatus.json') # 保存下载状态，在其它地方加载以继续下载

# print(a.values()) # 拥有所有 dict的方法
