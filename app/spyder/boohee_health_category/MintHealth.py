"""
@author David Antilles
@description 
@timeSnapshot 2024/3/31-17:01:17
"""

import requests
from bs4 import BeautifulSoup

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://www.boohee.com/",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"102\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}


# print(requests.get("https://www.boohee.com/food/group/1?page=10", headers=headers).text)


category = [
    '谷薯芋、杂豆、主食', '蛋类、肉类及制品', '奶类及制品', '蔬果和菌藻', '坚果、大豆及制品',
    '饮料', '食用油、油脂及制品', '调味品', '零食、点心、冷饮', '其它'
]

session = requests.Session()

CATEGORY_INDEX = '#{category_index}'
PAGE_NUM = '#{page_num}'

aggregation_template = 'https://www.boohee.com/food/group/#{category_index}?page=#{page_num}'

for i in range(10):
    pageRange = 8 if i == 7 else 10
    for j in range(pageRange):
        aggregation_url = aggregation_template.replace(CATEGORY_INDEX, str(i+1)).replace(PAGE_NUM, str(j+1))

