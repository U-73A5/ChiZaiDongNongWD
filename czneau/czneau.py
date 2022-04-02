#! /usr/bin/python3

## 
# 
from rich import print

import requests
import csv
from lxml import etree

urlNew = 'http://czneau.com/api/posts'

params = {
  'pageSize': '15',
  # 'fromId': '162374'
}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55',
  'Referer': 'http://czneau.com/'
}

resp = requests.get(urlNew, params, headers=headers)
resp.close()


print(resp.json())

